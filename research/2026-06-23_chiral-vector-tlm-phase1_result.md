# Genesis v9 Phase-1 (deferred) — Writhe-aware vector-TLM optical activity g0: RESULT

**Status:** RESULT (committed driver + keeper; no genesis sim).
**Date:** 2026-06-23 (re-adjudicated 2026-06-23 — outcome C REFUTED, see §0).
**Branch:** `analysis/chiral-vector-tlm-phase1` (PR #374).
**Driver:** [`src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py`](../src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py).
**Keeper:** `src/tests/test_chiral_vector_tlm_phase1.py`.
**Prereg context:** [`research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md`](2026-06-11_genesis-v9-phase1-prereg_FROZEN.md) (the ETA-injected P1–P4 gates); this driver supersedes the *injected-rotation* channel with a *derived* transport.
**Classification (`consistency-vs-emergence`):** EMERGENCE test (does substrate geometry SOURCE a gyration QED's parity-even vacuum cannot?); c/Z₀ reproduction is CONSISTENCY-class, the diamond null is a MANIFESTATION of mirror symmetry.

## §0 RE-ADJUDICATION — the original OUTCOME C was an ARTIFACT

The first cut of this result reported **OUTCOME C (ill-defined)**, on the grounds that the dynamical packet rate "does not converge in L" (rates +9.2 / −26.9 / +3.4 / +2.8 at L=6/8/10/12). An adversarial verify found that verdict was a **launch-transient fit-window artifact**, not physics:

- The legacy `dynamical_packet_rate` fit the **first `end=max(stop,4)` steps**, which are the **launch transient** — the flux-weighted z-centroid moves *backward* for ~3 steps while the packet settles (verified: at L=10, z = 4.65 → 4.59 → 4.49 → 4.27 over steps 0–3, with θ swinging wildly). Fitting that transient produced the wild swing.
- The §3 mechanism ("~4 forward steps before PBC wrap") was **factually wrong**. Forward z-advance/step = 0.7071, box = 16.97 (L=6) → 45.25 (L=16), so **box/advance = 24 (L=6) to 64 (L=16)** forward steps available; the flux-weighted centroid never reaches the boundary in the swept window. **The packet does not wrap.**
- **Skipping the launch transient** and fitting the steady forward-propagating segment (window growing with L) collapses the swing to O(1) with an exact enantiomorph sign-flip — *not* the ±27 chaos. The outcome-C "non-convergence" does not survive the transient fix.

This document is the re-adjudicated result.

## VERDICT — OUTCOME A (CHANNEL OPEN), with a NOT-bankable physical-mapping caveat

The writhe-aware operator **sees chirality cleanly** (GATE-1 PASS: signed, equal-magnitude loop holonomy ±0.256776 rad, EXACT diamond null) **and** the bulk forward-propagating polarization-rotation rate **converges** — to the **4₁ screw pitch** (∓2.21589 rad / lattice-z-unit, srs-R / srs-L), **L-independent to machine precision** (std 2e-16 across L=6,8,10,12,16), with an **exact enantiomorph sign-flip**. A driven steady-state transfer cascade (a genuinely propagating wave) reproduces this rate at **R² ≈ 1.0**, so the propagating wave **does inherit** the screw-chain rotation. This is **outcome A** (a converged, nonzero, signed bulk g₀ exists) — **not** the retracted outcome C.

**CAVEAT (refute-by-default; this is NOT yet a bankable chord).** The converged value is the **lattice-pitch-scale** holonomy. Converting it literally to a vacuum optical-activity coefficient gives g₀/a_cell ≈ **2.0e12 rad/m ≈ 1e14 °/m** — roughly **40 orders of magnitude ABOVE the cosmic bound (~4e-29 rad/m)** and ~22 OOM above the lab-polarimetry floor (~1e-9 °/m). That is physically a **per-node lattice-scale rotation**, *not* a validated **k→0 continuum gyration** at an optical wavelength (633 nm). The k→0 continuum extraction remains **unsettled**: the packet-centroid rate is strongly packet-width (k) dependent (§3), and the degree-3 srs band has **no isolated transverse photon band** (the original Bloch-split probe failed even its positive control). So: **existence of a converged signed bulk g₀ — YES (outcome A); a bankable physical optical-rotation prediction — NO (the literal value is enormously over-bound and the continuum mapping is unsettled).** g₀ is **deliberately NOT** mapped onto the live cosmic-birefringence β ~ 0.3° anomaly (different mechanism, §9).

---

## §1 The writhe-aware operator — how it escapes FAIL-1

FAIL-1 (the prior static Bloch eigensolve, g₀=0) was a **writhe-blind operator-stencil artifact**: operators built from local bond directions `{d̂, k·d}` cannot see handedness, because the LEFT and RIGHT srs bond-direction *multisets are identical* (spec_R − spec_L ≈ 4.4e-15). Chirality lives in the ring TOPOLOGY (writhe ±0.04087, sign-flipped between enantiomorphs, exactly 0 on the diamond), not in local bond geometry.

**The key design choice (the FAIL-1 escape):** the transverse polarization 2-frame is parallel-transported by the **rotation-minimizing (Bishop) rotation across the BEND at each node** — from the *arrival* bond tangent to the *departure* bond tangent. The frame rotation accumulated around a closed ring equals the geometric **solid angle** subtended by the ring's tangent sequence on the unit sphere — a reflection-ODD pseudoscalar, sign-flipped between enantiomorphs, EXACTLY zero for a mirror-symmetric ring.

**This was a non-trivial design crux.** Two writhe-BLIND connections were tried and rejected during design (both verified to give 0 on srs too):
- a **change-of-basis-only** edge map (frame absolute orientation held fixed) telescopes to identity around any loop → blind;
- a **local-bond** operator (the FAIL-1 stencil) → blind.

It is the **bend at the node**, not the local bond direction, that carries the chiral holonomy. The connection is **orthogonal** (RMF is a rotation), so the dynamical vector-TLM is **lossless** (Axiom 3; energy drift 1.66e-14 over 40 steps) — no κ_chiral injection, no ETA decree.

> **Contrast with the existing engine (`def-0pt1ac` / #195).** `chiral_lattice_vector.measure_optical_activity` rides `ETA_ROT_PER_WRITHE = 1.0` (`chiral_lattice_vector.py:27`), a tagged *engineering decree*, applied as a per-node SO(2) twist `ETA × mean_writhe` (`:93`). That ±75.46°/unit magnitude is *injected, not derived.* This driver **derives** the rotation from the transport instead. (See §6 flag.)

## §2 GATE-1 — chirality-sensitivity (the FAIL-1 guard): **PASS**

Gauge-invariant RMF-bend loop holonomy over the distinct shortest rings:

| net | mean loop holonomy (rad) | per-ring std | n rings |
|---|---|---|---|
| srs-R (I4₁32) | **−0.256776** | 1.4e-15 | 36 |
| srs-L (I4₃32) | **+0.256776** | 1.5e-15 | 35 |
| diamond (achiral) | **+0.0** (exact) | 0.0 | 9 |

The operator distinguishes L vs R (exact sign-flip, equal magnitude, `|R+L| < 1e-9`) and gives **EXACTLY zero** on the achiral diamond control — the null **EMERGES** from a single net's transport, not a hand-imposed odd-projection. This is the FAIL-1 guard passed: the operator is **writhe-AWARE**, structurally capable of sourcing optical activity. (Gauge-invariance matters: a per-edge *reference-angle* sum carries a spurious 2π reference-field winding on the L net; tracking the actual transported 3-vector removes it. This is the SAME gauge convention used by GATE-3.)

## §3 GATE-2 — convergence of the bulk forward-channel rate: **PASS** (re-adjudicated)

Three independent measurements of the bulk forward-propagating polarization-rotation rate, all converging on the **4₁ screw pitch**:

**(a) Geometric forward-winding — converged to machine precision, exact sign-flip.**

| L | forward-winding rate (srs-R, rad / lattice-z-unit) | (srs-L) |
|---|---|---|
| 6, 8, 10, 12, 16 | **−2.21589** (std 5e-16, identical at every L) | **+2.21589** |

Isotropic (identical along x/y/z); `R+L = 0` to machine precision; diamond ≈ −0.002 (greedy-tie residual, *not* the clean null — the clean achiral null is the GATE-1 loop holonomy, exactly 0.0). This equals the bare **4₁ screw pitch** `(π/2)/(t_z·a_cell) = +2.22144` to within **0.25%**.

**(b) Driven steady-state transfer cascade — dispersion-free, R² ≈ 1.0, exact sign-flip.**

The deciding tool (a transfer-matrix-cascade along the z-axis): hold a fixed transverse-polarized source on the entry z-slab, evolve the lossless writhe-aware step, sponge the far face (no PBC wrap), and read dθ/dz of the **steady forward-flux** polarization across z-bins — a *genuinely propagating wave*, free of the centroid-dispersion and PBC contamination of the packet probe.

| net | L=8 | L=10 |
|---|---|---|
| srs-R | **−2.227** (R²=1.000) | **−2.219** (R²=1.000) |
| srs-L | **+2.227** (R²=1.000) | **+2.219** (R²=1.000) |

The propagating wave **inherits the screw-chain rotation** — refuting the legacy claim that "the screw pitch never propagates / is just a unit-cell constant." (For larger L the simple sponge develops reflections that degrade R²; the machine-precision converged value is (a).)

**(c) Why the legacy packet-centroid rate is a DOUBLE artifact (the source of the retracted outcome C).** The legacy `dynamical_packet_rate` fits the launch transient (steps 0–3, centroid moving backward) — that produced the +9.2/−26.9/+3.4/+2.8 swing. **Even with the transient skipped** (`dynamical_packet_rate_steady`, fitting the longest strictly-forward segment), the centroid rate is **strongly packet-width (k) dependent**:

| launch σ (frac of box) | 0.05 | 0.08 | 0.12 | 0.18 | 0.25 |
|---|---|---|---|---|---|
| centroid rate (L=12, srs-R) | +0.42 | +0.62 | +0.80 | +1.25 | +1.81 → (screw pitch) |

As the packet widens (lower k, toward the continuum), the centroid rate climbs toward the screw pitch; as it narrows it drops. The "~0.7" one gets at σ ≈ 0.10–0.12 is therefore **not a bulk constant** — it is a dispersion-suppressed value set by the measurement σ. The genuinely converged, measurement-*independent* bulk rate is (a)/(b). The transient-skip fix kills the outcome-C swing (rates become O(1) with exact sign-flip), but the centroid is not the right bulk observable; the forward-winding / cascade is.

**Diagnosis of the FAIL-2 L=6/L=8 sign-flip (the prereg's open item):** it was a **fit-window / packet-width artifact of the centroid probe**, NOT a finite-box / PBC-wrap pathology. The bulk forward-channel rate (a)/(b) does not sign-flip with L — it is L-independent to machine precision.

## §4 GATE-3 — validate-on-known: **PASS**

| check | result | pass |
|---|---|---|
| network velocity factor (1/√3 reproduction) | 0.57636 vs 0.57735 (0.17%) | ✅ |
| Z₀ (imported by symbol from `constants.py`) | 376.73 Ω | ✅ |
| C₀ (imported by symbol) | 299 792 458 m/s | ✅ |
| dynamical vector-TLM losslessness (Axiom 3) | energy drift 1.66e-14 | ✅ |
| diamond loop-holonomy null | 0.0 (exact) | ✅ |

c, Z₀, the achiral null, and losslessness all reproduce.

> **Design-time observations NOT reproduced by this PR (re-tagged, do not carry the verdict).** During design two further probes were explored: (i) a one-step Bloch circular-birefringence split ω₊(k) − ω₋(k), and (ii) an imposed-twist positive control. Neither extraction was reliable in the dense degree-3 srs band (no isolated transverse photon band; the imposed-twist control did not recover a clean slope-1 odd-in-k signature). **That Bloch-split / positive-control code is NOT committed in this PR**, so those numbers are **design-time observations, not reproduced here, and carry no part of the verdict.** They are recorded only as the reason the **k→0 continuum** extraction (not the *existence* of a converged screw-pitch g₀) remains open — see §9. The verdict rests solely on the committed-and-tested GATE-1/2/3 quantities above.

## §5 Why outcome A (existence) but NOT a bankable physical chord

- **Outcome A (existence):** there IS a converged, nonzero, exact-sign-flipping bulk forward-channel g₀ = the 4₁ screw pitch (∓2.21589 rad / lattice-z-unit), L-independent to machine precision, dynamically confirmed by a propagating wave (the cascade, R²≈1.0). This is a genuinely different and **stronger** result than FAIL-1 (writhe-blind null) and than the retracted outcome C (ill-defined).
- **NOT a bankable physical prediction:** the literal rad/m conversion is `dθ/dz [rad/lattice-z-unit] / a_cell_physical`, with `a_cell_physical = 2√2·L_NODE ≈ 1.092e-12 m` (verified). That gives **±2.0e12 rad/m ≈ ±1.16e14 °/m** — ~40 OOM above the cosmic bound (~4e-29 rad/m), ~22 OOM above the lab floor (~1e-9 °/m). A vacuum that rotated light's polarization through a full turn every ~1.6 pm is excluded by ~40 orders of magnitude. So the *literal* value is **not** the physical vacuum optical activity; it is a lattice-pitch holonomy that a real long-wavelength (633 nm ≫ a_cell) photon would **average over**. The physical k→0 continuum gyration — which is what would map to a measurable optical rotation — is **not extracted here** (the centroid probe's k-dependence and the dense band both obstruct it).
- **Not B (closed-negative g₀=0):** the rate is a clean *nonzero* signed constant, not a converged zero.

**Honest landing:** the channel is **OPEN** — the substrate carries a real, signed, converged chiral helicity that a propagating wave inherits at the lattice scale. Whether that survives to a bankable, bound-respecting **continuum** optical activity is the remaining open question (§9), and the *literal* lattice-scale value is enormously over-bound, so it must **not** be quoted as a vacuum optical-rotation prediction.

## §6 flag-don't-fix — conflict with corpus `def-0pt1ac` (SOLID)

**Surfaced, NOT silently resolved** (Flag-don't-fix; Grant adjudicates):

- **Corpus claim** (`manuscript/ave-kb/common/vocabulary-register.md:529`, `def-0pt1ac`, status **SOLID**): *"the chiral-grid optical-activity result is validated (±75.46°/unit, #195)."* And `engine-capability-map.md:44`: *"the only engine with the validated chiral grid (srs I4₁32, optical-activity ±75.46°/unit, [#195])."*
- **This result:** that ±75.46°/unit is the **injected** rate — it rides `ETA_ROT_PER_WRITHE = 1.0` (`chiral_lattice_vector.py:27`, applied `:93`), a tagged engineering decree, applied as a per-node SO(2) twist `ETA × mean_writhe`. It is **not** a substrate-derived transport coefficient. When the rotation is DERIVED from a genuine writhe-aware transport (this driver), the bulk g₀ **does converge** (to the screw pitch) but the *derived* value is the lattice-pitch holonomy, NOT the ETA-decree ±75.46°/unit.

**The conflict:** the corpus carries a SOLID "validated magnitude" for optical activity whose magnitude is an injected decree. I am **not** rewriting the sign/sense/sourcing claims (signed, enantiomorph-odd, diamond-null, sourced by writhe, lossless reciprocal gyrator) — those **all survive** (GATE-1 confirms them). It is specifically the **magnitude as "validated/derived"** that this result challenges. Per the audit Finding-4, the magnitude clause of `def-0pt1ac` is demoted to engineering-decree, with the substrate-derived status recorded as "bulk g₀ = the 4₁ screw pitch (converged, signed, PR #374); k→0 continuum / physical-rad-m mapping pending." (Edits made — see §10.)

## §7 substrate-native-check walk (Operating Principle 1)

- **Dynamics:** discrete srs/K4-TLM scatter+connect wave propagation (`k4-tlm-simulator.md:36-40`). NOT Lagrangian / gradient-descent / continuum-Helmholtz / energy-basin.
- **Sector:** V-sector, transverse EM polarization 2-frame on the ports.
- **Objective:** the reflection-ODD polarization-plane rotation per unit forward length = the gyration. NOT an injected SO(2) twist.
- **Coordinates (A46):** the observable is the reflection-ODD polarization-plane rotation (a handedness coordinate), matching the corpus pseudoscalar claim — NOT a real-space lattice-Cartesian amplitude vs φ².
- **Saturation:** OFF (linear, A ≪ 1). No local-clock modulation (A→1 is genesis scope).
- **CP9 (heuristic-vs-dynamical):** the load-bearing observable is the polarization frame DYNAMICALLY evolved by the vector-TLM scatter+connect loop with a geometric per-bond transverse connection; the driven steady-state cascade is the genuinely-propagating-wave confirmation. (The CP9 distinction is what surfaced the §3 finding: the geometric forward-winding and the dynamical cascade agree on the screw pitch, while the centroid probe is dispersion/k-contaminated.)
- **CP10:** closed system for the gate quantities (the cascade adds a sponge boundary only to read the steady forward profile); conservation exact in the closed loop (drift 1.66e-14).

## §8 Honest closure (Rule 11 / Rule 12) + reproduction

The original outcome-C verdict is **retracted via Rule 12** (the body is preserved as §0 + this §; the slot is refilled with the *re-adjudicated, verified* outcome A, with its own verification chain — not an unverified replacement). A single mechanism (launch-transient fit window + packet-width-dependent centroid) explains the entire retracted swing; the geometric forward-winding and the dispersion-free cascade converge on the screw pitch with an exact sign-flip and machine-precision L-independence. No rescue-toward-a-chord was attempted — the bankable-physical-prediction claim is explicitly **withheld** (the literal value is ~40 OOM over the cosmic bound; the continuum mapping is open).

Reproduce:

```
PYTHONPATH=$PWD/src python3 src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py
pytest src/tests/test_chiral_vector_tlm_phase1.py -q
```

## §9 What could NOT be done / open

- **The k→0 continuum gyration is unsettled.** The converged screw-pitch g₀ is a **lattice-scale** (k ~ π/a) holonomy. The physically-relevant k→0 limit — which a 633 nm photon (λ ≫ a_cell) would sample, and which alone could map to a measurable, bound-respecting optical rotation — is not cleanly extracted here: the centroid rate is packet-width/k dependent (§3c), and the degree-3 srs band has **no isolated transverse photon band**, so a Bloch-eigenphase circular-split (the gold-standard k-resolved tool) is unreliable even on a known imposed gyration. A converged continuum g₀ would need either a clean isolated photon band, or a much larger / aperiodic-slab supercell with a hardened (PML-grade) absorbing face for the cascade (the simple sponge here is prototype-grade for large L). Both are flagged as the route IF the channel is revisited.
- **This result does NOT touch the AVE cosmic-birefringence observable** (E/B decoupling from K/G ≠ 2) — a *different mechanism*, deliberately kept separate. g₀ is **not** mapped onto the live β ~ 0.3° anomaly (and could not be: the literal lattice-scale value is ~40 OOM too large to be that anomaly).

## §10 Edits made by this re-adjudication (PR #374)

- **Driver** `src/scripts/vol_4_engineering/chiral_vector_tlm_phase1.py`: legacy `dynamical_packet_rate` re-tagged as KNOWN-ARTIFACT (kept for reproduction); added `dynamical_packet_rate_steady` (transient-skip, window grows with L, with the packet-width caveat) and `driven_cascade_rate` (dispersion-free transfer cascade); GATE-2 rewritten to lock the converged screw-pitch forward-channel rate + sign-flip + cascade confirmation; verdict logic → OUTCOME A with the not-bankable caveat.
- **Test** `src/tests/test_chiral_vector_tlm_phase1.py`: removed the regression that protected the artifact (`test_gate2_dynamical_bulk_rate_does_not_converge`); added tests locking the corrected outcome (converged forward-channel rate, exact sign-flip, screw-pitch coincidence, transient-skip kills the swing, dispersion-free cascade confirmation).
- **def-0pt1ac** `manuscript/ave-kb/common/vocabulary-register.md:529` + `engine-capability-map.md:44`: magnitude clause demoted from "validated ±75.46°/unit" to "ETA-decree engineering scale"; substrate-derived bulk g₀ status recorded (= 4₁ screw pitch, converged + signed, PR #374; continuum/physical-rad-m mapping pending). Qualitative facts (signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless reciprocal gyrator) kept SOLID.
