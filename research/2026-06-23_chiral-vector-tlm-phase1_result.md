# Genesis v9 Phase-1 (deferred) — Writhe-aware vector-TLM optical activity g0: RESULT

**Status:** RESULT (committed driver + keeper; no genesis sim).
**Date:** 2026-06-23.
**Branch:** `analysis/chiral-vector-tlm-phase1`.
**Driver:** [`src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py`](../src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py).
**Keeper:** `src/tests/test_chiral_vector_tlm_phase1.py`.
**Prereg context:** [`research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md`](2026-06-11_genesis-v9-phase1-prereg_FROZEN.md) (the ETA-injected P1–P4 gates); this driver supersedes the *injected-rotation* channel with a *derived* transport.
**Classification (`consistency-vs-emergence`):** EMERGENCE test (does substrate geometry SOURCE a gyration QED's parity-even vacuum cannot?); c/Z₀ reproduction is CONSISTENCY-class, the diamond null is a MANIFESTATION of mirror symmetry.

## VERDICT — OUTCOME C (ILL-DEFINED)

The writhe-aware operator **SEES chirality cleanly** (GATE-1 PASS: signed, equal-magnitude loop holonomy ±0.25678 rad, EXACT diamond null), but the **bulk-propagated** gyration coefficient g₀ **does not converge in system size L** (GATE-2 FAIL). The only converged quantities are **local unit-cell geometric constants** (the 4₁ screw pitch / ring holonomy) — *not* a bulk transport coefficient. **g₀ has no clean continuum limit from this transport.** This is *not* outcome A (chord) and *not* the FAIL-1 writhe-blind artifact (outcome distinct from a closed-negative B); it reproduces and **diagnoses** the FAIL-2 L=6/L=8 sign-flip as a finite-box propagation pathology.

This is an honest negative on the make-or-break question: **the substrate-derived natural-optical-activity coefficient is not bankable as a converged bulk g₀ from this writhe-aware transport.**

---

## §1 The writhe-aware operator — how it escapes FAIL-1

FAIL-1 (the prior static Bloch eigensolve, g₀=0) was a **writhe-blind operator-stencil artifact**: operators built from local bond directions `{d̂, k·d}` cannot see handedness, because the LEFT and RIGHT srs bond-direction *multisets are identical* (spec_R − spec_L ≈ 4.4e-15). Chirality lives in the ring TOPOLOGY (writhe ±0.04087, sign-flipped between enantiomorphs, exactly 0 on the diamond), not in local bond geometry.

**The key design choice (the FAIL-1 escape):** the transverse polarization 2-frame is parallel-transported by the **rotation-minimizing (Bishop) rotation across the BEND at each node** — from the *arrival* bond tangent to the *departure* bond tangent. The frame rotation accumulated around a closed ring equals the geometric **solid angle** subtended by the ring's tangent sequence on the unit sphere — a reflection-ODD pseudoscalar, sign-flipped between enantiomorphs, EXACTLY zero for a mirror-symmetric ring.

**This was a non-trivial design crux.** Two writhe-BLIND connections were tried and rejected during design (both verified to give 0 on srs too):
- a **change-of-basis-only** edge map (frame absolute orientation held fixed) telescopes to identity around any loop → blind;
- a **local-bond** operator (the FAIL-1 stencil) → blind.

It is the **bend at the node**, not the local bond direction, that carries the chiral holonomy. The connection is **orthogonal** (RMF is a rotation), so the dynamical vector-TLM is **lossless** (Axiom 3; energy drift 1.7e-14 over 40 steps) — no κ_chiral injection, no ETA decree.

> **Contrast with the existing engine (`def-0pt1ac` / #195).** `chiral_lattice_vector.measure_optical_activity` rides `ETA_ROT_PER_WRITHE = 1.0` (`chiral_lattice_vector.py:27`), a tagged *engineering decree*, applied as a per-node SO(2) twist `ETA × mean_writhe`. Verified at HEAD: it returns ±2.34°/step = 1.0 × 0.04087 rad — i.e. the injected angle IS the writhe times the decree. That magnitude is *injected, not derived.* This driver **derives** the rotation from the transport instead. (See §6 flag.)

## §2 GATE-1 — chirality-sensitivity (the FAIL-1 guard): **PASS**

Gauge-invariant RMF-bend loop holonomy over the distinct shortest rings:

| net | mean loop holonomy (rad) | per-ring std | n rings |
|---|---|---|---|
| srs-R (I4₁32) | **−0.256776** | 1.4e-15 | 36 |
| srs-L (I4₃32) | **+0.256776** | — | 35 |
| diamond (achiral) | **+0.0** (exact) | 0.0 | 9 |

The operator distinguishes L vs R (exact sign-flip, equal magnitude, `|R+L| < 1e-9`) and gives **EXACTLY zero** on the achiral diamond control — the null **EMERGES** from a single net's transport, it is not a hand-imposed odd-projection. This is the FAIL-1 guard passed: the operator is **writhe-AWARE**, structurally capable of sourcing optical activity. (Gauge-invariance matters: a per-edge *reference-angle* sum carries a spurious 2π reference-field winding on the L net; tracking the actual transported 3-vector removes it.)

## §3 GATE-2 — convergence (the FAIL-2 guard): **FAIL** (the load-bearing finding)

Two classes of quantity, with opposite convergence behaviour:

**(a) GEOMETRIC quantities — converged, L-independent, but unit-cell constants.**

| L | forward-winding rate (srs-R, rad / axial-length) |
|---|---|
| 6, 8, 10, 12, 14, 16 | **−2.21589** (identical at every L) |

Isotropic (identical along x/y/z). **But** this equals the bare **4₁ screw pitch** `(π/2)/(t_z·a_cell) = +2.22144` to within **0.2%**. It is L-independent *precisely because* it is a local unit-cell geometric constant (the pitch of the single screw-axis bond chain) — it never propagates. A converged number here is **not** evidence of a bulk transport coefficient; it is the screw pitch.

**(b) DYNAMICAL bulk-propagated rate — does NOT converge.**

The genuinely dynamical observable (CP9): forward-flux-weighted polarization-plane rotation `dθ/dz` of an actually-propagating wave packet in the writhe-aware vector-TLM.

| L | dynamical packet rate (srs-R) | usable fit pts before PBC wrap |
|---|---|---|
| 6 | +9.20 | 4 |
| 8 | **−26.90** | 4 |
| 10 | +3.41 | 4 |
| 12 | +2.79 | 4 |

The magnitude **swings wildly and changes sign** (9.2 → −26.9 → 3.4 → 2.8). The srs-R / srs-L pair is *exactly* antisymmetric (`R+L = 0` to machine precision) — but that is **trivially enforced by mirror symmetry** (srs-L is the exact mirror of srs-R, so any reflection-odd observable sign-flips by construction); it is NOT evidence of convergence. The **absolute** rate is the bulk physics, and it does not converge.

**Diagnosis of the FAIL-2 L=6/L=8 sign-flip (the prereg's open item):** it is a **finite-box propagation pathology**. The packet has only `~ box / (axial bond advance) ≈ 4` usable forward steps before it wraps the periodic supercell; the `dθ/dz` fit is therefore dominated by the launch transient + PBC wrapping, not by a steady-state per-length rate. This is the same pathology the design doc flagged for the Phase-0 scalar walk ("wanders … sign-flipped between L=6 and L=8"), now reproduced in the *full vector-TLM* and pinned to its mechanism — finer transport step / gauge-invariant formulation / different boundary conditions do not rescue it, because the limiting factor is the number of forward steps available in a finite chiral supercell.

**The Bloch route does not rescue it either.** The substrate-native bulk observable is the Bloch circular-birefringence split ω₊(k) − ω₋(k) of the one-step vector-TLM transfer operator (unitary, |eig| = 1.0000, verified). But the degree-3 srs band structure has **no cleanly isolated transverse "photon" band** — the circular-split extracted by a lowest-|ω| circular-content mode-picker is non-monotone in k, does not sign-flip cleanly between enantiomorphs, and is non-zero on the diamond (−0.014, +0.032, +0.027 at k = 0.1, 0.2, 0.4). The **positive control** (an imposed uniform synthetic twist α on the diamond, GATE-3 §4) does NOT recover a clean slope-1 odd-in-k signature either — confirming the Bloch-split *measurement apparatus itself* cannot reliably extract a per-length g₀ from this dense band structure, even when a known gyration is present. So the non-convergence is a property of the (finite-supercell × dense-band) system, not of one particular probe.

## §4 GATE-3 — validate-on-known: **PASS** (with the positive-control caveat)

| check | result | pass |
|---|---|---|
| network velocity factor (1/√3 reproduction) | 0.57636 vs 0.57735 (0.17%) | ✅ |
| Z₀ (imported by symbol from `constants.py`) | 376.73 Ω | ✅ |
| C₀ (imported by symbol) | 299 792 458 m/s | ✅ |
| dynamical vector-TLM losslessness (Axiom 3) | energy drift 1.7e-14 | ✅ |
| diamond loop-holonomy null | 0.0 (exact) | ✅ |
| **positive control** (imposed twist → slope-1 odd-in-k) | **NOT recovered** in dense band | ❌ |

c, Z₀, the achiral null, and losslessness all reproduce. **The positive control fails** — the Bloch-split probe cannot cleanly recover even a *known imposed* gyration in this band structure. Per the validate-on-known gate's own logic, this means **a derived g₀ from the Bloch route is not trustworthy** — which is consistent with, and reinforces, the outcome-C verdict.

## §5 Why outcome C (not A, not B)

- **Not A (chord):** there is no converged, nonzero bulk g₀. The only converged number is the screw-pitch unit-cell constant, which is geometry, not a propagated transport coefficient. Because there is no converged g₀, **no rad/m optical rotation at 633 nm can be quoted** — there is nothing to compare against the lab-polarimetry ~1e-9 deg/m floor or any bound. (Had a converged g₀ existed, the conversion would be `dθ/dz [rad/lattice-unit] / a_cell_physical`, with `a_cell_physical = 2√2·L_NODE ≈ 1.09e-12 m` — but the numerator does not converge.)
- **Not B (closed-negative g₀=0):** the operator does NOT give a converged zero. It gives a clean *nonzero* signed holonomy (chirality is real and seen), but the *bulk transport* magnitude is ill-defined. A closed-negative would require a writhe-AWARE operator that demonstrably sees chirality yet yields a *converged* g₀=0; here g₀ simply has no clean value.
- **Not the FAIL-1 artifact:** the FAIL-1 null was writhe-BLIND (spec_R ≈ spec_L). This operator is writhe-AWARE (GATE-1 PASS) — a genuinely different and stronger result than FAIL-1.

So the channel is **neither opened nor cleanly closed**: the substrate carries real, signed chiral helicity in its circuits (the Phase-0 writhe pseudoscalar and this loop holonomy both confirm it), but **a propagating EM wave does not inherit a well-defined per-length polarization rotation** from it in a finite chiral supercell.

## §6 flag-don't-fix — conflict with corpus `def-0pt1ac` (SOLID)

**Surfaced, NOT resolved** (per Flag-don't-fix; Grant adjudicates):

- **Corpus claim** (`manuscript/ave-kb/common/vocabulary-register.md:529`, `def-0pt1ac`, status **SOLID**): *"the chiral-grid optical-activity result is validated (±75.46°/unit, #195)."* And `engine-capability-map.md:44`: *"the only engine with the validated chiral grid (srs I4₁32, optical-activity ±75.46°/unit, [#195])."*
- **This result:** that ±75.46°/unit is the **injected** rate — it rides `ETA_ROT_PER_WRITHE = 1.0` (`chiral_lattice_vector.py:27`), a tagged engineering decree, applied as a per-node SO(2) twist `ETA × mean_writhe` (verified at HEAD: `measure_optical_activity` returns ±2.34°/step = 1.0 × 0.04087 rad). It is **not** a substrate-derived transport coefficient. When the rotation is DERIVED from a genuine writhe-aware transport (this driver), the bulk g₀ does **not converge** (outcome C).

**The conflict:** the corpus carries a SOLID "validated magnitude" for optical activity whose magnitude is an injected decree, while the *derived* magnitude is ill-defined. I am **not** rewriting `def-0pt1ac` — the sign/sense/sourcing claims (signed, enantiomorph-odd, diamond-null, sourced by writhe, lossless reciprocal gyrator) **all survive** this result (GATE-1 confirms them). It is specifically the **magnitude as "validated/derived"** that this result challenges. Recommended (auditor lands, Grant ratifies): demote the magnitude clause of `def-0pt1ac` from "validated" to "an ETA-decree engineering scale; substrate-derived bulk g₀ is ill-defined (outcome C, this result)" while preserving the qualitative claims. **Do not** convert the sign/null/sourcing facts — those are real.

## §7 substrate-native-check walk (Operating Principle 1)

- **Dynamics:** discrete srs/K4-TLM scatter+connect wave propagation (`k4-tlm-simulator.md:36-40`). NOT Lagrangian / gradient-descent / continuum-Helmholtz / energy-basin.
- **Sector:** V-sector, transverse EM polarization 2-frame on the ports.
- **Objective:** circular birefringence = odd-in-k Bloch split of the two circular polarizations = gyration. NOT an injected SO(2) twist.
- **Coordinates (A46):** the observable is the reflection-ODD polarization-plane rotation (a handedness coordinate), matching the corpus pseudoscalar claim — NOT a real-space lattice-Cartesian amplitude vs φ².
- **Saturation:** OFF (linear, A ≪ 1). No local-clock modulation (A→1 is genesis scope).
- **CP9 (heuristic-vs-dynamical):** the load-bearing observable is the polarization frame DYNAMICALLY evolved by the vector-TLM scatter+connect loop with a geometric per-bond transverse connection. The geometric loop-holonomy / forward-winding are explicitly flagged as the GEOMETRIC SOURCE; the dynamical packet rate is the genuinely-evolved bulk observable. (The distinction is exactly what surfaced the §3 finding: the geometric number is a converged unit-cell constant, the dynamical number does not converge.)
- **CP10:** closed system (no PML, no bulk force); conservation exact.

## §8 Honest closure (Rule 11) + reproduction

A pre-registered question failed to settle to a chord, a single mechanism (finite-box propagation × dense band structure) explains both the dynamical non-convergence and the Bloch-split unreliability, and the geometric "convergence" is explained (it's the screw pitch). The branch closes as **outcome C**. No rescue attempted; finer steps / gauge-invariant formulation / Bloch route all fail for the same diagnosed reason.

Reproduce:

```
PYTHONPATH=$PWD/src python3 src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py
pytest src/tests/test_chiral_vector_tlm_phase1.py -q
```

## §9 What could NOT be done / open

- A converged bulk g₀ would need either (i) an **infinite / much larger** supercell so a propagating packet accumulates many forward steps before wrapping (cost grows steeply: the dynamical step is O(N·deg²) in Python; an aperiodic-slab or transfer-matrix-cascade-along-axis formulation is the right next tool), or (ii) a **clean isolated transverse photon band** to make the Bloch-split extraction reliable — which the degree-3 srs band structure does not provide. Neither is in scope here; both are flagged as the route IF the channel is revisited.
- This result does **not** touch the AVE cosmic-birefringence observable (E/B decoupling from K/G ≠ 2) — that is a *different mechanism* and is deliberately kept separate; g₀ is **not** mapped onto the live β ~ 0.3° anomaly.


