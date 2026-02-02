#!/usr/bin/env python3
"""
Epiphone Serial Sanity Check
- Validates modern numeric Epiphone serials (2008–present scope) using a strict parse gate.
- Reports malformed serials with reasons.
- Reports counts n by FF (factory code) for VALID serials only.

Usage examples:
  python epiphone_serial_sanity.py epiphone_full_dataset_bucket.csv
  python epiphone_serial_sanity.py epiphone_full_dataset_bucket.csv --serial-col Serial --model-col Model
  python epiphone_serial_sanity.py epiphone_full_dataset_bucket.csv --outdir out --dedupe
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

VALID_LEN = {10, 11, 12}
VALID_CHAR_RE = re.compile(r"^[0-9X\?]+$")  # after normalisation
DIGITS_RE = re.compile(r"^\d+$")
SEQ_RE = re.compile(r"^[0-9X\?]+$")

# Characters to strip from both ends (punctuation/quotes/brackets)
STRIP_CHARS = " \t\r\n\"'`.,;:!()[]{}<>"

CANDIDATE_SERIAL_COLS = [
    "serial", "Serial", "SERIAL",
    "serial_number", "SerialNumber", "Serial_Number", "SERIAL_NUMBER",
    "sn", "SN", "s/n", "S/N"
]

CANDIDATE_MODEL_COLS = [
    "model", "Model", "MODEL",
    "model_name", "ModelName", "Model_Name",
    "instrument", "Instrument", "instrument_name", "InstrumentName",
    "Product", "product"
]


@dataclass
class ParseResult:
    raw: str
    norm: str
    is_valid: bool
    reason: Optional[str] = None
    yy: Optional[str] = None
    mm: Optional[str] = None
    ff: Optional[str] = None
    seq: Optional[str] = None


def normalise_serial(s: str) -> str:
    """
    Ground-truth-ish normalisation:
    - keep as-entered raw elsewhere
    - strip surrounding punctuation/whitespace
    - remove spaces and hyphens internally
    - uppercase
    """
    if s is None:
        return ""
    s = str(s)
    s = s.strip(STRIP_CHARS)
    s = s.replace(" ", "").replace("-", "")
    s = s.upper()
    return s


def parse_serial(raw: str) -> ParseResult:
    norm = normalise_serial(raw)

    if norm == "":
        return ParseResult(raw=raw, norm=norm, is_valid=False, reason="empty")

    # Gate 3: valid characters
    if not VALID_CHAR_RE.match(norm):
        return ParseResult(raw=raw, norm=norm, is_valid=False, reason="invalid_chars")

    # Gate 4: length
    if len(norm) not in VALID_LEN:
        return ParseResult(raw=raw, norm=norm, is_valid=False, reason=f"invalid_length_{len(norm)}")

    # Gate 5: fixed fields
    yy = norm[0:2]
    mm = norm[2:4]
    ff = norm[4:6]
    seq = norm[6:]

    # Gate 6: YY/MM/FF digits only (no X/? allowed)
    if not (DIGITS_RE.match(yy) and DIGITS_RE.match(mm) and DIGITS_RE.match(ff)):
        return ParseResult(
            raw=raw, norm=norm, is_valid=False,
            reason="nondigit_in_yy_mm_ff",
            yy=yy, mm=mm, ff=ff, seq=seq
        )

    # Gate 7: MM must be 01–12
    mm_i = int(mm)
    if mm_i < 1 or mm_i > 12:
        return ParseResult(
            raw=raw, norm=norm, is_valid=False,
            reason=f"invalid_month_{mm}",
            yy=yy, mm=mm, ff=ff, seq=seq
        )

    # Gate 8: seq digits/?/X only (already enforced by VALID_CHAR_RE, but keep explicit)
    if not SEQ_RE.match(seq):
        return ParseResult(
            raw=raw, norm=norm, is_valid=False,
            reason="invalid_seq_chars",
            yy=yy, mm=mm, ff=ff, seq=seq
        )

    return ParseResult(raw=raw, norm=norm, is_valid=True, yy=yy, mm=mm, ff=ff, seq=seq)


def detect_column(headers: List[str], candidates: List[str]) -> Optional[str]:
    header_set = {h.strip(): h for h in headers}
    # exact match first
    for c in candidates:
        if c in header_set:
            return header_set[c]
    # case-insensitive match
    lower_map = {h.lower(): h for h in headers}
    for c in candidates:
        if c.lower() in lower_map:
            return lower_map[c.lower()]
    return None


def write_csv(path: str, headers: List[str], rows: Iterable[List[str]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in rows:
            w.writerow(r)


def main() -> None:
    ap = argparse.ArgumentParser(description="Validate Epiphone serials + report n by FF.")
    ap.add_argument("csv_path", help="Input CSV file path")
    ap.add_argument("--serial-col", default=None, help="Column name containing serials")
    ap.add_argument("--model-col", default=None, help="Optional model column (used for dedupe key if --dedupe)")
    ap.add_argument("--outdir", default="serial_sanity_out", help="Output directory for reports")
    ap.add_argument("--dedupe", action="store_true",
                    help="Dedupe by (norm_serial, model_name_casefold) when model-col available; else by norm_serial only.")
    ap.add_argument("--max-examples", type=int, default=20, help="Max example rows per error reason in the text summary")
    args = ap.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        if not headers:
            raise SystemExit("ERROR: CSV has no headers.")

        serial_col = args.serial_col or detect_column(headers, CANDIDATE_SERIAL_COLS)
        if not serial_col:
            raise SystemExit(
                "ERROR: Could not detect serial column. "
                "Pass --serial-col with the exact header name."
            )

        model_col = args.model_col or detect_column(headers, CANDIDATE_MODEL_COLS)
		
        construction_col = detect_column(headers, ["ConstructionBucket"]) #AF - add construction 

        valid_ff = Counter()
        invalid_reasons = Counter()
        invalid_examples: Dict[str, List[Tuple[str, str]]] = defaultdict(list)  # reason -> [(raw,norm)]
        seen_keys = set()

        # For optional “what FF would be if you sliced invalid strings” diagnostics:
        invalid_ff_sliced = Counter()

        # Collect row-level detail for outputs
        malformed_rows_out: List[List[str]] = []
        valid_rows_out: List[List[str]] = []

        for i, row in enumerate(reader, start=2):  # start=2 (header is line 1)
            raw_serial = row.get(serial_col, "")
            pr = parse_serial(raw_serial)

            model_val = row.get(model_col, "") if model_col else ""
            model_key = str(model_val).strip().casefold()

            construction_val = row.get(construction_col, "") if construction_col else ""  #AF - get acoustic/hb/solid


            if args.dedupe:
                if model_col and model_val is not None and str(model_val).strip() != "":
                    key = (pr.norm, model_key)
                else:
                    key = (pr.norm, "")
                if key in seen_keys:
                    continue
                seen_keys.add(key)

            if pr.is_valid and pr.ff is not None:
                valid_ff[pr.ff] += 1
                valid_rows_out.append([
    				str(i),
    				pr.raw,
    				pr.norm,
    				pr.yy or "",
    				pr.mm or "",
    				pr.ff or "",
    				pr.seq or "",
    				str(model_val),
    				str(construction_val)
				])

            else:
                reason = pr.reason or "invalid_unknown"
                invalid_reasons[reason] += 1
                if len(invalid_examples[reason]) < args.max_examples:
                    invalid_examples[reason].append((pr.raw, pr.norm))

                # If norm is long enough to slice FF-like positions, record it (diagnostic only)
                if len(pr.norm) >= 6:
                    invalid_ff_sliced[pr.norm[4:6]] += 1
                else:
                    invalid_ff_sliced["<too_short>"] += 1

                malformed_rows_out.append([
                    str(i), pr.raw, pr.norm, reason, pr.yy or "", pr.mm or "", pr.ff or "", pr.seq or "", str(model_val),str(construction_val)
                ])

        # Prepare output dir
        outdir = args.outdir
        os.makedirs(outdir, exist_ok=True)

        # Write CSVs
        write_csv(
            os.path.join(outdir, "valid_serials_parsed.csv"),
            ["source_line", "raw_serial", "norm_serial", "YY", "MM", "FF", "seq", "model","ConstructionBucket"],
            valid_rows_out
        )

        write_csv(
            os.path.join(outdir, "malformed_serials.csv"),
            ["source_line", "raw_serial", "norm_serial", "reason", "YY", "MM", "FF", "seq", "model","ConstructionBucket"],
            malformed_rows_out
        )

        # Write n by FF (VALID ONLY)
        ff_rows = [[ff, str(n)] for ff, n in sorted(valid_ff.items(), key=lambda x: (-x[1], x[0]))]
        write_csv(
            os.path.join(outdir, "n_by_FF_valid_only.csv"),
            ["FF", "n"],
            ff_rows
        )

        # Write invalid sliced FF diagnostics
        inv_ff_rows = [[ff, str(n)] for ff, n in sorted(invalid_ff_sliced.items(), key=lambda x: (-x[1], x[0]))]
        write_csv(
            os.path.join(outdir, "n_by_FF_sliced_from_invalid.csv"),
            ["FF_sliced_from_invalid_norm[4:6]", "n"],
            inv_ff_rows
        )

        # Write a human-readable summary
        total_valid = sum(valid_ff.values())
        total_invalid = sum(invalid_reasons.values())
        total = total_valid + total_invalid

        summary_lines: List[str] = []
        summary_lines.append(f"Input: {args.csv_path}")
        summary_lines.append(f"Serial column: {serial_col}")
        summary_lines.append(f"Model column: {model_col or '(none)'}")
        summary_lines.append(f"Dedupe: {'ON' if args.dedupe else 'OFF'}")
        summary_lines.append("")
        summary_lines.append(f"Rows processed (post-dedupe if ON): {total}")
        summary_lines.append(f"Valid serials: {total_valid}")
        summary_lines.append(f"Invalid serials: {total_invalid}")
        summary_lines.append("")

        summary_lines.append("Invalid reasons (count):")
        for reason, n in sorted(invalid_reasons.items(), key=lambda x: (-x[1], x[0])):
            summary_lines.append(f"  - {reason}: {n}")
        summary_lines.append("")

        summary_lines.append("Examples by invalid reason (raw -> norm):")
        for reason, ex in sorted(invalid_examples.items(), key=lambda x: x[0]):
            summary_lines.append(f"  [{reason}]")
            for raw, norm in ex:
                summary_lines.append(f"    {raw!r} -> {norm!r}")
        summary_lines.append("")

        summary_lines.append("n by FF (VALID serials only):")
        for ff, n in sorted(valid_ff.items(), key=lambda x: (-x[1], x[0])):
            summary_lines.append(f"  - {ff}: {n}")

        summary_path = os.path.join(outdir, "summary.txt")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write("\n".join(summary_lines) + "\n")

        print("\n".join(summary_lines))
        print("")
        print(f"Wrote reports to: {os.path.abspath(outdir)}")
        print(f"  - {os.path.join(outdir, 'summary.txt')}")
        print(f"  - {os.path.join(outdir, 'n_by_FF_valid_only.csv')}")
        print(f"  - {os.path.join(outdir, 'malformed_serials.csv')}")
        print(f"  - {os.path.join(outdir, 'valid_serials_parsed.csv')}")
        print(f"  - {os.path.join(outdir, 'n_by_FF_sliced_from_invalid.csv')} (diagnostic only)")


if __name__ == "__main__":
    main()

