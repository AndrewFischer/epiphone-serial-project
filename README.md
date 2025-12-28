# Epiphone Serial Number Project

This project is an observational analysis of  **modern Epiphone serial numbers (≈2008–present)** to better understand **production timing, factory codes, and batching**.

It does **not** authenticate instruments or assess quality. The current dataset is well short of being able to estimate total production. 

---

## Scope

- Focus on:
  - production month/year indicators
  - observed factory code usage
  - batch proximity and production patterns
- Based on **publicly observable serial numbers** from listings, auctions, forum posts, and private instruments

- Epiphone Serial Format: YYMMFFxxxxx:
	- YY Year
	- MM Month
	- FF Factory
	- xxxxx is sequence or “rank” number.
### Observed and well-known FF Codes
- 13 China, details unknown
- 15 Qingdao, China.  Epiphone / Gibson managed. All observed IGC guitars,acoustic and electric
- 16 Qingdao, China. None in dataset
- 23 Indonesia, Samick factory

Other FF are anecdotally known, but are not in the dataset. 

---

This project does **not**:

- authenticate guitars
- determine originality or provenance
- estimate total production numbers
- predict quality, QC outcome, or tone
- replace expert appraisal or manufacturer records

---



## Factory-Specific Semantics

Where sufficient evidence exists, **factory-specific serial semantics are defined explicitly**.

Notably:
- **FF 15** (Epiphone-managed Qingdao) has well-supported batching and serial-order semantics.
- Other factory codes may exist syntactically but have **no defined semantics unless supported by data**.

Absence of evidence is treated as a data limitation, not a conclusion.

---

## Data & Methodology

- Textual data only

Evidence > anecdotes.

---

## License

This project is licensed under the  
**Creative Commons Attribution–ShareAlike 4.0 International (CC BY-SA 4.0)** license.

You are free to share and adapt the material for any purpose, provided that:
- appropriate credit is given, and
- derivative works are distributed under the same license.

See the [`LICENSE` file](https://creativecommons.org/licenses/by-sa/4.0/) for full details.

---

## Status

This repository is under active development.  
Ground Truth is versioned and changes are recorded in `CHANGELOG.md`.

Contributions are welcome, provided they adhere to Ground Truth.
