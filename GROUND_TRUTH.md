Epiphone Serial Number Project — Ground Truth & Rules
Scope
* Modern Epiphone serial numbers (≈2008–present)
* (the YYMMFFxxxxx serial format is first observed on 2008 instruments)
* Focus on production timing, factory codes, batching behaviour
* Data collection and pattern analysis only

Data Submission (text only)
Required
* Serial number
* Exact model name
Optional
* Finish
* Condition (new / demo / B-stock / used)
* Vendor (e.g. Gibson EU/UK, Sweetwater)
* Listing or purchase month/year
* Country/region
* Price
No photos required in-thread. Images (if any) are processed off-line.

Serial Format
YYMMFFxxxxx
* YY = year
* MM = month
* FF = factory code
* xxxxx = batch-local sequence number
* FF is not a day of the month
* Final digits are not global counters
* YY is interpreted as 20YY within the project scope (≈2008–present). No other century interpretation is permitted.


Given serial s:
Parse Gate (must pass before any analysis):
1. raw = s as-entered
2. norm = remove all spaces and hyphens; strip leading/trailing punctuation; uppercase
3. Valid characters: digits 0–9 plus ? and X only
    * If any other character appears → invalid, stop
4. len(norm) must be 11 → else invalid, stop
5. YY=norm[0:2], MM=norm[2:4], FF=norm[4:6], seq=norm[6:11]
6. YY, MM, FF must be digits only
    * If ?/X appears in YY/MM/FF → invalid for timing/factory; keep as record but exclude from FF/timing counts
7. MM must be 01–12 (numeric)
    * If not → invalid, stop
8. seq may contain digits and/or ?/X only.

Serial numbers ending in X or ? are valid. Each X or ? represents exactly one unknown digit (0–9) and carries no other meaning.
? and X are equivalent wildcards (single digit 0–9).
They do not encode “unknown factory” or “unknown month”; they are only unknown digits.
When comparing batch proximity, treat wildcards as “range” not a number (no numeric sorting unless you expand to min/max).
Wildcards must not be used to infer or impute missing digits during analysis unless explicitly expanded to a numeric min/max range.

Duplicate handling
* Define duplicate as: same norm and same model name (case-insensitive trimmed).
* If same serial appears with different model names, do not dedupe; flag as a conflict for human review.





What Serials Can / Cannot Do
Can
* Identify production month/year
* Indicate factory code
* Show batch proximity
Cannot
* Give exact build day
* Give total production numbers
* Predict quality, QC outcome, or tone
* Authenticate an instrument on their own

FF Factory Codes
Confirmed elsewhere with high confidence.
* 15 — Qingdao, China
* 16 — Qingdao, China
* 21 — Unsung, Korea
* 23 — Samick, Indonesia
* 13  — China

FF 16 is included to allow future observations to pass the parse gate; no production or serial semantics are currently defined due to lack of observed serials.

If an FF appears in analysis results but no serial contains that FF in positions 5–6, the result is invalid and must be rechecked.

FF 15 — Serial Semantics (Factory-Specific Ground Truth)


Serial number placement and application differ by construction type.

Acoustics, hollow-body, and centre-block electrics:
- Serial numbers are printed on a paper or synthetic label inside the body.
- No serial is present on the neck or headstock.
- The timing of serial assignment within the build process is unknown.
- No inferences about neck join, finishing stage, or production order may be made from label-based serials.

Solid-body electrics (e.g. Les Paul, SG):

Serial number application methods vary by production era.

Earlier production solid-body electrics:
- Serial numbers may be printed on the headstock.
- These are not physically stamped into the wood.
- No assumptions about build-stage timing can be made from printed serials.

Current and recent production solid-body electrics:
- Serial numbers are stamped into the headstock wood and lie beneath the finish.
- This constrains serial assignment to pre-final-finishing, but no finer sequencing is implied.

The timing and scope of the transition between printed and stamped serials are not yet defined.

Batch boundaries at FF 15 are defined by production scheduling (model, finish, neck spec), not by serial-number discontinuities alone.




Acronyms

Epiphone and Gibson specific:

IGC: Inspired by Gibson Custom
IBG: Inspired by Gibson
IBC ≠ IGC

LP: Les Paul
LPTD+: Les Paul Traditional Plus
SC: Single Cut
DC: Double Cut

Finishes:
* AS / ASB: Antique Sunburst
* AW: Alpine White
* BK: Black (Solid)
* CH: Cherry
* CS: Cherry Sunburst
* HS / HCS: Heritage Cherry Sunburst
* EB: Ebony (Standard Gloss Black)
* HB: Honey Burst
* IT: Iced Tea  
* FT: Faded Iced Tea
* NA: Natural
* PE: Pelham Blue
* TA: Trans Amber
* TB: Trans Black
* TR: Trans Red
* TV: TV Yellow
* VS: Vintage Sunburst
* WR: Wine Red 
* AA: Appetite Amber (Slash signature)
* AB: Arctic Blue
* AC: Aged Cherry
* AI: Antique Ivory
* AP: Aged Pelham Blue
* BC: Black Cherry
* BS: Silverburst
* BU: Bourbon Burst
* EBK: Black (Matte or Satin)
* MG: Metallic Gold
* GT: Goldtop
* PB: Plain Black / Pitch Black


Analysis Rules
* Textual data only
* Evidence > anecdotes
* Single examples do not define patterns
* Inference must be labelled as inference
* Corrections require data
* Store serials as-entered + a normalised form; never silently “fix” serials


Forbidden inference
* Do not infer factory code from model line (IGC/IBG/Original Collection), country, vendor, or price.
* Do not infer missing digits.
* Do not infer that two different FF codes are the “same factory” unless you have multiple independent sources showing the mapping.


Pattern claim tags
* Observation: directly counted/measured from parsed serials.
* Inference: plausible explanation consistent with observations, but not proven.
* Speculation: interesting idea with weak support (allowed, but must be labelled).


Purpose
* Build a clean observational dataset
* Identify production patterns
