#Epiphone Serial Number Project — Ground Truth & Rules
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
###Serial Format
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
    * If ?/X appears in YY/MM/FF → invalid 
7. MM must be 01–12 (numeric)
    * If not → invalid, stop
8. seq may contain digits and/or ?/X only.

Serial numbers containing X or ? in the sequence portion (positions 7–11) are valid. Each X or ? represents exactly one unknown digit (0–9) and carries no other meaning.
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
* 13  — China
* 15 — Qingdao, China
* 16 — Qingdao, China
* 21 — Unsung, Korea
* 23 — Samick, Indonesia
* 29 — unknown factory (Kramer; observed)

FF 16 is included to allow future observations to pass the parse gate; no production or serial semantics are currently defined due to lack of observed serials.

If an FF appears in analysis results but no serial contains that FF in positions 5–6, the result is invalid and must be rechecked.

青岛吉森乐器有限公司 – Qingdao Jisen Musical Instrument Co., Ltd.
is a wholly-owned subsidiary (全资子公司) of Gibson Brands, Inc.

“吉森 (Jisen)” is a standard phonetic rendering of Gibson in mainland Chinese business usage.

Based on ownership, location (Qingdao), production scope, and consistency with observed serial-number patterns, 青岛吉森乐器有限公司 is very likely the legal entity corresponding to factory code FF 15.
青岛吉森乐器有限公司 is Located in Puji Town, Jiaozhou City — a county-level city administered by Qingdao

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
IBG ≠ IGC

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

## Instrument Class Ground Truth — Tier A (Explicit Models)

### Normalisation rules (applied)
* Leading "Epiphone" ignored
* Case-insensitive matching
* LEFT-HANDED normalised exactly as `LEFT-HANDED`
* Finish, condition, vendor excluded
* Instrument class is authoritative; construction notes are annotations only

---

### Acoustic — Steel-string

IGC 1960 HUMMINGBIRD REISSUE  
IGC 1960 HUMMINGBIRD REISSUE LEFT-HANDED  
IGC HUMMINGBIRD DELUXE EC  

HUMMINGBIRD  
HUMMINGBIRD 12-STRING  
HUMMINGBIRD STUDIO  
HUMMINGBIRD STUDIO EC  
HUMMINGBIRD STUDIO EC LEFT-HANDED  

IGC 1957 SJ-200 REISSUE  
IGC PRE-WAR SJ-200 ROSEWOOD REISSUE  

J-200 STUDIO  
J-200 STUDIO EC  
J-200 STUDIO EC LEFT-HANDED  
J-200 EC STUDIO  
J-200 EC STUDIO PARLOR 
J-200 STUIDIO BASS 

IGC 1942 BANNER J-45 REISSUE  
IGC 1942 BANNER J-45 REISSUE LEFT-HANDED  

J-45 STUDIO  
J-45 STUDIO EC  
J-45 EC STUDIO  
J-45 EXPRESS  

IGC 1963 DOVE REISSUE  
IGC 1963 DOVE REISSUE LEFT-HANDED  
DOVE STUDIO  

BLUES KING STUDIO  
L-00 STUDIO  

MASTERBILT EXCELLENTE  
MASTERBILT TEXAN  
MASTERBILT FRONTIER  

PRO-1 (STEEL STRING; SQUARE SHOULDER)  

SONGMAKER DR-100  
SONGMAKER DR-100 LEFT-HANDED  
DR-100  

SONGMAKER DR-212  
DR-212  
MIRANDA LAMBERT BLUEBIRD
MIRANDA LAMBERT BLUEBIRD STUDIO  
MIRANDA LAMBERT BLUEBIRD ACOUSTIC-ELECTRIC
MIRANDA LAMBERT BLUEBIRD ACOUSTIC-ELECTRIC GUITAR
---

### Acoustic — Nylon

CLASSICAL E1 (NYLON; 1.75" NUT)

---

### Acoustic — Resophonic

DOBRO HOUND DOG M-14 METALBODY (ROUND NECK)

---

### Electric — Semi-hollow / Hollow / Archtop

ES-335  
ES-335 FIGURED  
IGC 1962 ES-335 REISSUE  

ES-345  
IBG ES-345  
IBG DOT ES-335
INSPIRED BY GIBSON DOT ES-335
IGC 1959 ES-355
INSPIRED BY GIBSON CUSTOM 1959 ES-355
1959 ES-355 SEMI-HOLLOWBODY ELECTRIC
1959 ES-355 SEMI-HOLLOWBODY ELECTRIC GUITAR 
DAVE GROHL DG-335
DAVE GROHL DG-335 SEMI-HOLLOWBODY ELECTRIC
DAVE GROHL DG-335 SEMI-HOLLOWBODY ELECTRIC GUITAR

BB KING LUCILE
RIVIERA  
NOEL GALLAGHER RIVIERA  

SHERATON  
EMILY WOLFE "WHITE WOLFE" SHERATON  

UPTOWN KAT ES  

CASINO  
CASINO LEFT-HANDED  

BROADWAY  
BROADWAY LEFT-HANDED  

EMPEROR SWINGSTER  

150TH ANNIVERSARY ZEPHYR DELUXE REGENT  
JACK CASADY BASS
JACK CASADY FRETLESS SIGNATURE BASS GUITAR

---

### Electric — Solid Body

WILSHIRE P-90S  
CRESTWOOD CUSTOM  
CORONET  

SG TRIBUTE PLUS  
SG STANDARD  
IBG SG STANDARD  
SG CUSTOM  
IBG SG CUSTOM  
G-400

LES PAUL STANDARD 50S  
LES PAUL STANDARD 50S LEFT-HANDED  
LES PAUL STANDARD 60S  
IBG LES PAUL STANDARD 60S  

LES PAUL MODERN FIGURED  
LES PAUL TRIBUTE  
LES PAUL PROPHECY  
LES PAUL JUNIOR  

IGC 1959 LES PAUL STANDARD REISSUE  
IGC 1960 LES PAUL STANDARD REISSUE  
IGC 1957 LES PAUL GOLDTOP REISSUE  

INSPIRED BY GIBSON CUSTOM 1958 KORINA EXPLORER
IGC 1958 KORINA EXPLORER

JEFF BECK OXBLOOD 1954 LES PAUL  
IGC JEFF BECK OXBLOOD 1954 LES PAUL  
LES PAUL CLASSIC-T (ROBOT TUNERS)
JOE BONAMASSA 1955 LES PAUL STANDARD
JOE BONAMASSA 59 LPS LAZARUS 
JERRY CANTRELL "WINO" LES PAUL CUSTOM  
ADAM JONES 1979 LES PAUL CUSTOM  
ALEX LIFESON LES PAUL CUSTOM AXCESS  
ADAM JONES LES PAUL CUSTOM ART COLLECTION: KORIN FAUGHT’S “SENSATION”  
TAK MATSUMOTO DC CUSTOM
TAK MATSUMOTO DC CUSTOM EBONY FINGERBOARD
TAK MATSUMOTO 1955 LES PAUL STANDARD
LES PAUL CUSTOM LEFT-HANDED  
JOAN JETT OLYMPIC SPECIAL
NIGHTHAWK CUSTOM REISSUE


WAXX NIGHTHAWK STUDIO  
EXTURA PROPHECY
EMBASSY BASS  
EMBASSY BASS GUITAR
GRABBER BASS
GRABBER BASS GUITAR
EB-0 BASS
EB-2 BASS
EB-3 SG BASS
EB-3 BASS GUITAR
THUNDERBIRD E1
THUNDERBIRD E1 BASS GUITAR
IGC 1963 LES PAUL SG CUSTOM WITH MAESTRO VIBROLA  

---
### Electric - Through Neck
THUNDERBIRD '64 BASS GUITAR
THUNDERBIRD 1964
THUNDERBIRD 1964 BASS GUITAR
THUNDERBIRD CLASSIC PRO IV
THUNDERBIRD IV
REX BROWN THUNDERBIRD
---

### Electric — Firebird / V Family

IGC 1963 FIREBIRD I REISSUE  
IGC 1963 FIREBIRD V  
IGC 1963 FIREBIRD V REISSUE WITH MAESTRO VIBROLA  

JIMI HENDRIX "LOVE DROPS" FLYING V  
DAVE MUSTAINE FLYING V CUSTOM  
DAVE MUSTAINE FLYING V PROPHECY  


---

### Notes
* This section defines **Tier-A authoritative instrument class only**
* Construction details (semi-hollow, centerblock, archtop, etc.) are annotations and must not be used to infer class
* Wildcard / pattern rules must never override entries in this list

## Instrument Class Ground Truth — Tier B (Pattern Rules, Non-Authoritative)

### Status
* **Non-authoritative**
* Used only when **no Tier-A exact model match exists**
* Must never override Tier-A classifications
* Intended to reduce `unknown` rates caused by naming variation only

### Confidence
* All Tier-B classifications are **MED confidence**
* Any conflict between Tier-B rules results in `instrument_class = unknown`

---

## Tier-B Pattern Rules

### Electric (pattern-based)

Apply **only if Tier-A did not match**.

* `^ES-\d{3}\b`  
  → electric  
  *(ES-335, ES-339, ES-345, ES-355, etc.)*

* `\bLES PAUL\b`  
  → electric

* `(^| )SG( |$)`  
  → electric  
  *(Standalone token only; do not match substrings)*

* `\bFIREBIRD\b`  
  → electric

* `\bFLYING V\b`  
  → electric  
  *(Do not match lone "V")*

* `\bSHERATON\b`  
  → electric

* `\bRIVIERA\b`  
  → electric

* `\bCASINO\b`  
  → electric

* `\bBROADWAY\b`  
  → electric

* `\bWILSHIRE\b`  
  → electric

* `\bCRESTWOOD\b`  
  → electric

* `\bCORONET\b`  
  → electric
  
* `\bFLYING[- ]?V\b`
  → electric
  
* `\bTHUNDERBIRD\b`
	→ electric
	→ construction: unknown


---

### Acoustic (pattern-based)

Apply **only if Tier-A did not match**.

* `\bHUMMINGBIRD\b`  
  → acoustic

* `\bJ-45\b`  
  → acoustic

* `\bSJ-200\b|\bJ-200\b`  
  → acoustic

* `\bJ-180\b`
  → acoustic

* `\bDOVE\b`  
  → acoustic

* `\bL-00\b`  
  → acoustic

* `\bMASTERBILT\b`  
  → acoustic

* `\bDR-100\b`  
  → acoustic

* `\bDR-212\b`  
  → acoustic

* `\bPRO-1\b`  
  → acoustic

---

### Subtype Tags (Optional, Orthogonal)

Subtype tags may be applied **after** instrument class resolution.
They must not be used to infer instrument class.

* `\b12-STRING\b|\b12 STRING\b`  
  → subtype: `12-string`

* `\bCLASSICAL\b|\bNYLON\b`  
  → subtype: `nylon`

* `\bDOBRO\b|\bRESONATOR\b|\bRESOPHONIC\b`  
  → subtype: `resophonic`

* `\bPARLOR\b`  
  → subtype: `parlor`

---

## Conflict Handling

* Tier-A exact match always wins
* If multiple Tier-B rules match with different classes:
  - Set `instrument_class = unknown`
  - Flag record for human review
* Tier-B rules must not be expanded without observed dataset examples

---

## Design Constraints

* Tier-B rules exist solely to absorb naming variation
* They must not encode assumptions about construction, factory, or era
* Unknown is a valid and preferred outcome over misclassification




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
