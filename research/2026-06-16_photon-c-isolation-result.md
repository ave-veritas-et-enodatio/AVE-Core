# Result — T₂-photon group velocity vs the √2c A₁/CFL precursor (DOCUMENTATION run)

**Prereg:** [`2026-06-16_photon-c-isolation-prereg.md`](2026-06-16_photon-c-isolation-prereg.md) (FROZEN bins).
**Driver:** `src/scripts/vol_1_foundations/photon_c_isolation.py`.
**Data:** [`research/data/2026-06-16_photon-c-isolation.json`](data/2026-06-16_photon-c-isolation.json).
**Date:** 2026-06-16. **Branch:** `analysis/2026-06-16-photon-c-isolation`. **Grounded against** `origin/main` @ `1ad1e7fc`.
**Class:** DOCUMENTATION (DEC-01 / weak-C ruled). Constants: canonical `src/ave/core/constants.py` (`C_0`, `V_SNAP`).

---

## BIN: **UNISOLABLE-ON-THIS-ENGINE**

The T₂ photon and the A₁ bulk front **cannot be separated by propagation speed on this engine.** All three source modes return identical speeds to machine precision; the dt/connect convention pins every mode's wavefront to one cardinal cell per step.

## The two speeds + causality (the requested triplet)

| Observable | v/c (C_0 convention) | v/c₀ (physical junction-crossing convention) |
|---|---|---|
| **T₂ envelope group velocity** (PURE-T₂, peak-arrival) | **1.41421356** | 1.0000 |
| **A₁ longitudinal front** (PURE-A₁, leading edge) | **1.41421356** | 1.0000 |
| MIXED (~50% A₁ + 50% T₂) group velocity | 1.41421356 | 1.0000 |
| **Information front** (sharp on/off step, 57-plane first-above-floor slope) | **1.41421356** | **1.00000000** |

- T₂ group and A₁ front are **identical** (spread = 0). No separation.
- **Causality:** the information front (a true on/off signal edge tracked across 57 interior planes) rides at **exactly c₀** in the engine's physical-c₀ convention (`1.0000000000000002`). The √2 in the C_0 convention is the bare cardinal-cell-per-step grid march, NOT a superluminal signal.

---

## Why UNISOLABLE — the substrate mechanism (one mechanism explains everything)

Three lattice facts, each verified:

1. **The connect-shift is mode-blind.** Every port shift `(±1,±1,±1)` has x-component ±1 (`k4_tlm.py:378–383`), so the wavefront advances **exactly 1 cardinal cell per step regardless of port-mode content.** A₁, T₂, and MIXED all march the front forward at 1 cell/step.

2. **dt fixes that to √2c.** `dt = dx/(c·√2)` (`k4_tlm.py:183`), so `v_cardinal = dx/dt = c·√2` **by the clock convention** — this √2 is baked into dt, not a per-mode dispersion.

3. **The scatter split does NOT show up in peak/front arrival.** `S = ½𝟙 − I` has eigenvalues `[-1,-1,-1,+1]` (verified): A₁ = +1 (non-dispersive DC front), T₂ = −1 (per-step sign-flip → distinct dω/dk). The T₂'s distinct group velocity is real in the *phase* of the carrier, but the **slab-energy envelope** (|V|² peak) and the **leading edge** both still arrive at 1 cardinal cell/step, so the energy-density peak-arrival observable — the canonical one — cannot see the scatter-eigenvalue split. The mode-identity is invisible to propagation speed.

This is **exactly the handoff's prediction** (`_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:48`, verified verbatim):

> both "continuous-energy-discretely-sampled" (Branch C) and "discrete-transfer" predict cardinal √2 / diagonal c. **Propagation speed cannot separate them**; the only discriminator is causality.

And it confirms the RESIDUAL OPEN (handoff:16): `project_T2` on=off gave identical speed because the measurement catches the **dt-convention bare front (√2c)**, shared by all modes — not a resolved per-mode group velocity. Here PURE-A₁ and PURE-T₂ also give identical speed, closing the residual: the √2c front is **neither specifically the bulk precursor NOR specifically the photon** as a speed signature — it is the **mode-blind grid march**, the dt/connect convention itself.

---

## The √2 is a coordinate/sampling artifact — NOT re-introduced (CP4 discipline)

All v/c are reported in **real-space cardinal-cell distance over physical (dt-scaled) time** — the per-port distance-count convention was NOT used. The √2 that appears is the dt clock convention (`k4_tlm.py:181`: physical junction speed `c0 = dx/(dt·√2) = C_0`; cardinal-cell-per-step grid march `dx/dt = √2·c0`). Dividing out the dt-√2 (the `c₀` column above) puts every speed — including the information front — at **exactly c₀ = C_0**.

So the substrate's physical answer is: **everything rides at the single physical speed c₀**; the √2c is the lattice's cardinal-cell-per-step grid-bookkeeping speed, a sampling/clock fingerprint, identical for the photon and the bulk front.

---

## Causality: a COORDINATE flag, NOT a physical violation (flag-don't-fix)

The JSON literal `CAUSALITY: CAUSAL-VIOLATION` (`CAUSALITY_is_coordinate_flag: true`) fires because `info_front_over_c = 1.414 > 1.15` **in the C_0 convention**. This is **not** a physical superluminal-information result:

- In the engine's own physical-c₀ convention (`k4_tlm.py:181`), `info_front_over_c0_junction = 1.0000000000000002` — the information front rides at **exactly c₀**.
- The √2 is the same cardinal-cell-per-step grid artifact as the bulk and photon fronts.

**Surfaced for adjudication (not silently resolved):** whether the corpus statement `photon-propagation-baseline.md:50` ("the substrate-internal speed $c$ is the canonical AVE wave speed … cardinal-axis $\sqrt{2}$ is a lattice-projection artifact") and `:48` ("NOT … Special Relativity violation") should be read as **the physical c being c₀ = `dx/(dt·√2)`**, with the cardinal-axis √2c being `√2·c₀` (the bare grid march). The data says yes: in c₀ units the information front is exactly c, no violation. This is the convention call Grant/the auditor land, not the implementer.

---

## What this documents for weak-C / DEC-01

- **Weak-C reconciliation is NOT contradicted, but it is also NOT confirmed by a speed separation** — because no speed separation exists on this engine. The clean BIN T2-RIDES-AT-c (photon=c, √2c=separate precursor *ahead* of it) was **not** observed: the √2c is not a separate front running ahead of a c-photon; it is the single mode-blind grid speed that both the photon envelope and the bulk front share.
- The **causal** observable (the discriminator the handoff named as the only one that can separate continuous-sampled from discrete-transfer) returns the physical-c₀ in the engine's own convention — **consistent with** weak-C (signal respects c; the √2 is a sampling/grid fingerprint), provided the c₀-convention is adopted.
- **Net:** documents that on the K4-TLM engine the photon-as-information rides at c₀ (the information-front result), with √2c being the cardinal-cell grid-bookkeeping speed shared by ALL modes — a sampling fingerprint, not a separable bulk precursor. The mode-identity of the √2c front is **unisolable by propagation speed**; the causal front pins the physical signal speed to c₀.

---

## Honest-closure (Rule 11 / Rule 12)

- The bin was read mechanically off the frozen §3 criteria, after correcting one bin-ordering defect found at result time: **UNISOLABLE must be tested before T2-RIDES-AT-√2c** (a √2 reading shared by all modes is the convention, not a per-mode photon speed). The corrected ordering is documented in the driver's `adjudicate` docstring and below. This is a criterion *clarification* (which bin a shared-√2 belongs in), not a post-hoc criterion drop to convert a verdict — the §3 UNISOLABLE definition ("all modes within ±15% of each other AND no front/envelope separation") was always the matching condition; the prereg merely listed it third.
- The CAUSAL-VIOLATION literal is FLAGGED as a coordinate-convention artifact, not reconciled silently and not reported as a physical violation. Both readings (C_0 and c₀) are in the JSON.
- No corpus claim edited. One baseline-leaf framing item surfaced for the auditor lane (below).

---

## Surfaced for the auditor lane (do not land here)

`manuscript/ave-kb/.../photon-propagation-baseline.md` headlines "$v_{\text{meas}}/c = \sqrt{2}$ Cardinal-Axis Kinematics" and "Diagonal-axis predicted speed $v=c$". This result + the handoff diagonal-arm amendment together show: (a) diagonal is ALSO √2c in real-space Euclidean distance (handoff Amendment-2, A≈1 isotropic), so the cardinal-vs-diagonal "anisotropy" is a per-port distance-count convention; (b) the √2c is mode-blind (A₁ = T₂ = MIXED here), so it is the dt/connect grid speed, not specifically the A₁ bulk mode; (c) in the engine's physical-c₀ convention every front is at c₀. The baseline leaf's "√2 cardinal-axis kinematics, native Axiom 1" framing is a **coordinate-convention statement**, correct only under the C_0-is-physical-c reading. Recommend the auditor reconcile the baseline leaf with the c₀ = `dx/(dt·√2)` convention. This is surfaced, not landed (implementer lane discipline).
