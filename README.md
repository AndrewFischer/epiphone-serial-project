# Epiphone Serial Number Project

**Research into modern Epiphone YYMMFFrrrrr serial numbers (≈2008–present).**

This project collects **publicly observable Epiphone serial numbers** to study:
- production month/year patterns  
- factory code usage  
- batching and sequencing behaviour  

It is an **observational dataset**, not a certification or valuation tool.

If you own an Epiphone, have spotted one for sale, or enjoy serial-number archaeology — **your data is welcome**. We are only interested in YYMMFFrrrrr serials. Older letter-code serials like S3021234 are not part of this project. 

---

## What this project is (and isn’t)

### ✅ This project *is*
- a dataset of real Epiphone serial numbers  
- focused on **patterns**, not individual instruments  
- based only on **visible serials** from guitars, listings, and forum posts  
- open, conservative, and evidence-driven  

### ❌ This project is *not*
- an authentication service  
- a way to verify originality or value  
- a quality, QC, or “good vs bad factory” ranking  
- an estimate of total production numbers (__yet__)
- a replacement for Gibson/Epiphone internal records  

If you’re asking *“Is my guitar real or fake?”* — this repo is **not** the right tool.

---

## Scope

- Modern Epiphone serial numbers (≈2008–present)  
- Production timing, factory codes, batching behaviour  
- Data sourced from:
  - private instruments  
  - shop listings and dealer demo stock  
  - eBay and Reverb listings with visible serials  
  - forum and Reddit posts  

No private or identifying personal data is collected.

---

## Serial number format (modern Epiphone)

Modern Epiphone serials follow: **YYMMFFrrrrr**

Where:
- **YY** = production year  
- **MM** = production month  
- **FF** = factory code  
- **rrrrr** = batch-local sequence number (aka *rank*)  

---

## Observed factory codes (current dataset)

| FF | Location | Notes |
|----|---------|-------|
| 13 | China | Details currently unknown |
| 15 | Qingdao, China | Epiphone / Gibson-managed factory; all observed **Inspired by Gibson Custom (IGC)** guitars (acoustic & electric) |
| 16 | Qingdao, China | No confirmed entries yet |
| 23 | Indonesia | Samick factory |

Other factory codes are mentioned online but are **not treated as real until supported by data**.

Absence of evidence ≠ evidence of absence.

---

## Factory-specific semantics

Where sufficient data exists, **factory-specific behaviour is documented explicitly**.

At present:
- **FF 15** shows strong evidence of batching and serial-order semantics  
- Other factories may share the same *syntax* but **no semantics are assumed without evidence**

This is deliberate and conservative.

---

## How to contribute

You do **not** need GitHub expertise to help.

### Required (text only)
- **Serial number** (exactly as shown)
- **Exact model name**


## Dataset format (`.csv`)

The canonical dataset is stored as a **UTF-8 encoded CSV file**.

The column names, order, and casing **must match exactly**.

### Required columns (current schema)

| Column | Description |
|------|-------------|
| `Model` | Exact model name as advertised or labelled |
| `Colour` | Finish or colour (may be empty) |
| `Source` | Where observed (e.g. eBay, Reverb, Ishibashi, Sweetwater, private owner) |
| `Serial` | Full serial number (eg. `22011512345`) |

If you do not want to publish the full serial for a personal instrument, **wildcards (`X` or `?`) are allowed in the final one or two digits**, e.g. `2201151234X`.
 
All four columns are required to exist, but **fields may be empty** except for `Serial`.

---

### CSV rules

- One guitar per row  
- Text only (no formulas)  
- No embedded commas unless the field is quoted  
- Do **not** pad serials with spaces or punctuation  
- Use empty fields rather than placeholders like `N/A`  
- Preserve column order and header spelling  

---

### Example (valid)

```csv
Model,Colour,Source,Serial
Epiphone Les Paul Studio Custom Shop,,eBay,10011512788
Epiphone Les Paul Standard Plus Top Heritage Cherry Sunburst,,Ishibashi,10051509041
```




### Where serials come from
- your own guitar  
- dealer or shop listings  
- Reverb / eBay  
- forum or Reddit posts  

No photos are required in submissions.

---

## Data rules (important)

- Text-only submissions  
- No owner names  
- No addresses or contact details  
- No identifying personal data.  

If it’s visible on a headstock or internal label, it’s acceptable.


---

## Project status

- Actively developed  
- Dataset still small relative to global production  
- Conclusions are intentionally conservative  

Bug reports, corrections, and negative findings are all valid contributions.

---

## License

This project is licensed under  
**Creative Commons Attribution–ShareAlike 4.0 (CC BY-SA 4.0)**.

You may:
- share  
- adapt  
- build upon the data  

Provided that you:
- give appropriate credit  
- distribute derivative works under the same license  

See `LICENSE` for full details.
