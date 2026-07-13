# CVR Bench — Requirements / Derived Boundary-Conditions Datasheet

**Date:** 2026-07-13 · **Lane:** CVR dielectric-C-V bench (implementer) · **Status:** DERIVED requirements datasheet; NOT canonized. Requirements are physics-set; every design CHOICE lives in the sibling trade-study (STATUS:OPEN).

**Sibling docs.**
- `research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md` — the OPEN make-vs-buy + design-knob decision-space (STATUS:OPEN throughout; SELECTS NOTHING; cost out of scope). Derived physics is HERE; choices are THERE.
- Ratified prediction leaf this datasheet specs the bench against: `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:25-38` (the transverse-T2 roll-off / tangent / 1/√2 NDC; ruling chain PR#562/#558, Grant-ratified 2026-07-06/07).
- Structural template: the CLEAVE-01 doc set (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md`, `…/cleave-01-trade-study-decision-register.md`, `…/project-cleave-01.md`). This datasheet copies its single-source-of-truth REQ-ID discipline (`cleave-01-requirements-boundary-conditions.md:43`) and its corroborative-null rescope (`project-cleave-01.md`).

> **★ OPEN DECISION FOR GRANT — KB chapter home.** These CVR docs live in `research/` for now. The natural KB home is Vol-4 (either `vol4/falsification/ch11-experimental-bench-falsification/` alongside CLEAVE-01, or `vol4/circuit-theory/ch1-vacuum-circuit-analysis/` alongside `cvr-dc-operating-point.md`). Chapter placement + whether the requirements leaf becomes a `clm-*` claim vs a `no-claim` consolidation leaf is flagged OPEN — not decided here.

---

## PAGE ONE — the binding epistemic frame (`CVR-REQ-FRAME`)

<!-- CVR-REQ-FRAME skeleton — filled in the next commit -->

---

## REQ-ID INDEX — the canonical CVR requirement identifiers

<!-- REQ-ID INDEX skeleton — filled in the next commit -->

---

## §1 — `CVR-REQ-BIAS` — the bias/field requirement is CLASSIFIER-driven, not magnitude-driven

<!-- §1 skeleton -->

## §2 — `CVR-REQ-STANDOFF` — HV C-V topology: sense node at virtual ground

<!-- §2 skeleton -->

## §3 — `CVR-REQ-FIXTURE` — stiffness from the d⁻³ subtraction; gap sweep ≥4× at fixed V

<!-- §3 skeleton -->

## §4 — `CVR-REQ-FIELDVOL` — Class-I / vacuum spacer ONLY in the DC field volume

<!-- §4 skeleton -->

## §5 — `CVR-REQ-ACQ` — I/Q separation + 3–4 simultaneous probe tones + mandatory INCONCLUSIVE bin

<!-- §5 skeleton -->

## §6 (D3) — ASSEMBLY: the tangent-slope expression d(δC/C)/dE²

<!-- D3 assembly skeleton -->

---
