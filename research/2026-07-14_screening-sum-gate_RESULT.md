# RESULT — QED-TRACE Many-Body Screening-Sum Gate

**Date:** 2026-07-14 · **Prereg (frozen, pushed before run):**
[`research/2026-07-14_screening-sum-gate_prereg_FROZEN.md`](2026-07-14_screening-sum-gate_prereg_FROZEN.md)
(freeze commit `ee1fc728`, pushed BEFORE the driver ran)
· **Driver:** [`src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py`](../src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py)
· **Output:** `assets/sim_outputs/qed_trace_screening_sum_gate.{json,png}`
· **Predecessor:** [`research/2026-07-14_qed-trace-beta-gate_RESULT.md`](2026-07-14_qed-trace-beta-gate_RESULT.md) (§7 opened this route).

---

## TL;DR

**Verdict — bin `WRONG-FORM` (category closure COMPLETE), read on the frozen TRANSFER register.**
The self-consistent many-body screening SUM — the intervening lattice cells between two seeded windings,
each polarizing in the TOTAL field including every other cell's induced polarization (the
Clausius-Mossotti / self-consistent-screening ladder), kernel-ON — produces a **decisive POWER LAW**
(`M_pow`, `p≈0.60`, `ΔBIC = −24.7` at 2 decades, `−21.0` at 3 decades), **NOT a logarithm**. This closes
the last route the beta gate left explicitly open (its §7: "the many-body screening SUM between the two
probes … UNPROBED, NOT CLOSED").

**The load-bearing new finding (what the many-body sum changes vs the pairwise dress).** The
self-consistent inter-cell ladder **SOFTENS the falloff dramatically** — from the beta gate's pairwise
`p≈4.25` to a shallow `p≈0.60`, flattening TOWARD the log-degenerate regime (`p→0` is where a power
becomes indistinguishable from a log) — **but it stops decisively short of a genuine log.** And it
**fixes the SIGN**: the transfer coupling now **GROWS at short distance** (`α_eff>1`, `1/α_eff: 0.958 →
0.994`), the **QED anti-screening direction** — where the beta gate's pairwise transfer register had the
WRONG sign (weakened). So the many-body sum earns the right SIGN and the right DIRECTION of softening,
but the FORM is a power law, not a logarithm: **right sign, wrong form.**

**Genuinely MANY-BODY, not a relabeled pairwise dress (both genuineness knives PASS).**
- **Knife A (Born vs converged):** self-consistency changes the transfer departure by **9.4%** (coeff
  `×0.78`, exponent `−0.05`) — the inter-cell ladder is ACTIVE, not a spectator.
- **Knife B (remove intervening cells):** removing the bridge cells between the probes changes `α_eff`
  by **51% (R=100) / 58% (R=1000)** — the intervening medium carries HALF the effect. This is the
  many-body screening SUM, not the two-body dress under a new name.

**Class (consistency-vs-emergence): CONSISTENCY / ECHO.** The per-cell Op14 saturation grade is
charge-agnostic (same kernel as the beta gate). The earnable content is the FORM/SIGN **category answer
of the SUM**, not a value. No emergence claim is headlined — and the FORM is not a log, so no FORM-chord
is earned either. **A clean, corpus-completing negative (Rule 11).**

---

## Sector header (as-run)

MODE static two-body TRANSFER coupling between two seeded Cosserat windings, mediated by a self-consistent
polarizable medium (the many-body screening SUM); REGIME cold, **KERNEL ON** (Op14/Ax4 saturation sets
per-cell polarizability) with a kernel-OFF (α0=0) null that reads flat to machine ε; PHASE-STATE
sub-yield **perturbative** — the intervening bridge medium is weakly strained (`A≪1`), fit over `R/d_sat
∈ [30, 3000]` (2 decades; the near-saturated small-`R` bridge = non-perturbative Pauli-wall analog,
EXCLUDED); SECTOR the graded-Coulomb screening cloud of induced cell dipoles = the vacuum-polarization
cloud, and the two-probe transfer force through it = the vacuum-polarization-corrected Coulomb law.
Platform: the canonical Op14 capacitive/saturation grade (`universal_saturation`, clm-gdd70j) sets the
per-cell polarizability; a NEW static electrostatic self-consistent-field dipole-lattice solver performs
the many-body sum. No new ENGINE.

---

## 1. THE α_eff(R) TABLE — both registers (KEEP-BOTH), self-consistent dipole-lattice sum

Scale variable: `R/d_sat` (separation; `d_sat/R` = energy proxy, larger = shorter = higher energy).
Kernel-OFF (α0=0) ⇒ `α_eff^transfer ≡ 1` at all scales (verified flat to `0.0`). Orientation-averaged
over 8 SO(3) mesh rotations (AMEND A1.3); `orient_std` = the residual angular-discretization scatter.

| `R/d_sat` | **α_transfer** | `1/α_tr` | **α_reactive** | `α_tr` (Born) | orient_std |
|---:|---:|---:|---:|---:|---:|
| 30.0  | **1.044187** | 0.95768 | 1.591699 | 1.048351 | 5.4e-03 |
| 40.8  | 1.035189 | 0.96601 | 1.561741 | 1.037224 | 5.7e-03 |
| 55.4  | 1.034744 | 0.96642 | 1.520744 | 1.036003 | 6.1e-03 |
| 75.4  | 1.023268 | 0.97726 | 1.515374 | 1.023608 | 5.0e-03 |
| 102.4 | 1.017998 | 0.98232 | 1.506503 | 1.018074 | 4.4e-03 |
| 139.2 | 1.012845 | 0.98732 | 1.448730 | 1.012850 | 5.8e-03 |
| 189.3 | 1.015817 | 0.98443 | 1.465463 | 1.015813 | 8.6e-03 |
| 257.3 | 1.008931 | 0.99115 | 1.391210 | 1.008930 | 2.7e-03 |
| 349.8 | 1.008243 | 0.99182 | 1.417376 | 1.008243 | 3.1e-03 |
| 475.5 | 1.007127 | 0.99292 | 1.403404 | 1.007127 | 3.0e-03 |
| 646.3 | 1.006977 | 0.99307 | 1.386770 | 1.006977 | 3.2e-03 |
| 878.6 | 1.007251 | 0.99280 | 1.367335 | 1.007251 | 3.0e-03 |
| 1194  | 1.007696 | 0.99236 | 1.348403 | 1.007695 | 2.0e-03 |
| 1624  | 1.008271 | 0.99180 | 1.330637 | 1.008271 | 1.6e-03 |
| 2207  | 1.007154 | 0.99290 | 1.313805 | 1.007154 | 2.7e-03 |
| 3000  | **1.005849** | 0.99418 | 1.297996 | 1.005849 | 2.7e-03 |

- **TRANSFER register** (through-coupling `F_transfer(R)/F_bare(R)`, PRIMARY): departs **ABOVE 1** — the
  coupling **GROWS at short distance** (`α_eff>1`, larger near `R=30`, → 1 far-field) = **QED
  anti-screening sign**. Fit: **`M_pow`, `p≈0.600`, `a≈0.333`**, **`ΔBIC = −24.7`** (a power law fits ~25
  BIC-units better than a log — decisive per the frozen `|ΔBIC|>10`). The log model's slope is a tiny
  `−0.0072`; it loses decisively. **WRONG-FORM, RIGHT sign.**
- **REACTIVE register** (`W_sat/W_lin`, stored-energy dress, KEEP-BOTH, NOT binned): departs **ABOVE 1**
  (grows at short distance), fit `M_log` `p=0.300` (railed at the grid floor = the log-degenerate limit).
  The reactive register is dominated by the `R`-independent near-probe cloud (the innermost shell sits at
  `ρ≈1.05 d_sat` regardless of `R`), so its scale-dependence is weak and log-degenerate — exactly the
  register the beta gate flagged as sign-artifactual. Reported for completeness; **the verdict is read on
  the transfer register**, per the frozen requirement.
- **`register_flip_observed = False`.** Unlike the beta gate (opposite SIGN by register), here BOTH
  registers grow at short distance — the many-body sum does not flip the sign between registers, though
  the FORM still differs (transfer = decisive power; reactive = log-degenerate near-cloud dress).

See figure (`qed_trace_screening_sum_gate.png`): the transfer departure is a straight line in log-log (a
genuine log would curve); Born and converged nearly overlap (self-consistency softens but does not change
the form).

---

## 2. Frozen 5-bin classification

| Bin | Fired? | Evidence |
|---|---|---|
| LOG-EMERGES | ✗ | transfer fit selects `M_pow` (`ΔBIC=−24.7`), not `M_log`; decisive at 2 AND 3 decades |
| **WRONG-FORM** | **✓ (SELECTED)** | transfer register is a decisive power law `p≈0.60`; `α0`-independent (never `M_log`); 3-decade-robust (`ΔBIC=−21.0`, `p≈0.55`) |
| WRONG-SIGN | ✗ | transfer α GROWS at short distance (`α_eff>1`) = the RIGHT (QED) sign — the wrong-sign bin does NOT fire (contrast the beta gate, whose transfer register weakened) |
| NULL-FLAT | ✗ | the departure is non-negligible (`α_eff−1 ≈ 0.006–0.044`); the sum is not inert |
| INCONCLUSIVE-RANGE | ✗ | separability gate PASSES at 2 decades; `ΔBIC` is decisively past `±10` |

**Genuineness precondition (frozen §4): SATISFIED as MANY-BODY** — both knives pass (§3), so the verdict
is reported as a genuine many-body result, NOT `RELABELED-PAIRWISE`.

**Consequence (frozen, prereg §4).** Category closure COMPLETE: the many-body scale-integrated route
ALSO fails to emit `ln(R)`. The beta gate's §7 "many-body screening SUM … UNPROBED, NOT CLOSED" boundary
is now **CLOSED (WRONG-FORM)**. The q-g20f "Identical (RT-equivalence)" scoped-import re-tag can now DROP
the "unprobed, not closed" caveat and read as a full scoped import. **The re-tag is routed to the
auditor** (implementer lane does not land the KB/manuscript entry).

**Scope of the null (frozen concession).** Scoped to *the classical + kernel-ON lattice, self-consistent
polarizable-cell screening between seeded windings, perturbative window*. It does not re-open or re-close
the sourced-charge no-go (`clm-nogo4l`), which stays closed by its own argument.

---

## 3. ★ MANY-BODY-GENUINENESS RECEIPT (the two frozen knives — is the SUM genuinely many-body?)

The load-bearing question the prereg's structural-null stencil lens demands: is this the many-body sum,
or the pairwise dress relabeled? BOTH frozen knives fire correctly and confirm **genuinely many-body**:

**Knife A — Born vs converged (self-consistency must change the result).** The Born comparator turns the
inter-cell dipole coupling OFF in the `p`-equation (dipoles respond to the probe field only):

| | selected | `p` | max frac-change (conv vs Born) | coeff ratio (conv/Born) | exponent shift |
|---|---|---|---|---|---|
| Born | `M_pow` | 0.650 | — | — | — |
| Converged | `M_pow` | 0.600 | **9.4%** | **0.778** | **−0.05** |

Self-consistency changes the transfer departure by up to **9.4%** (`≫ 1e-6` threshold), reduces the
coefficient to `0.78×`, and softens the exponent by `0.05`. The inter-cell ladder is **ACTIVE, not a
spectator** (`G_genuineness_A_pass = True`). It does NOT change the FORM (both power) — i.e. the
self-consistent resummation softens the falloff but does not convert power → log.

**Knife B — remove intervening (bridge) cells (the medium must carry it).** Re-run at fixed `R` with the
cells in the region BETWEEN the probes (`|z|<R/2` AND cylinder `ρ<R/2`) removed:

| `R/d_sat` | n_bridge cells | `α_tr` full | `α_tr` no-bridge | frac change |
|---:|---:|---:|---:|---:|
| 100 | 213 | 1.018208 | 1.008912 | **51.1%** |
| 1000 | 211 | 1.006698 | 1.002792 | **58.3%** |

Removing the intervening medium changes `α_eff` by **>50%** at both scales (`G_genuineness_B_pass =
True`). The transfer coupling genuinely FLOWS through the intervening lattice cells — this is the
screening SUM between the probes, not a two-body dress. **Verified the result CHANGES when intermediate
cells are removed**, exactly the self-consistency-genuineness knife the task required.

**Self-adversarial live-fire (implementer pass; three refutation hypotheses, all fail to overturn).**
- **H1 — "removing ANY cells changes it, so knife B is vacuous."** REFUTED. Bridge-removal (interaction
  path) changes `α_eff` **64.7%**; removing an EQUAL COUNT of exterior/off-path cells changes it
  **0.0%** — a **4369× ratio**. The screening is spatially specific to the intervening medium; the
  exterior cloud does not mediate the probe–probe coupling. Knife B is not a generic sensitivity.
- **H2 — "the coupling is effectively local, so 'many-body' overclaims."** The inter-cell coupling is
  **short-range-dominated** (truncating the dipole matrix at `5 d_sat` barely moves the result: `p`
  0.600→0.550). It is still genuinely many-body/self-consistent (Born ≠ converged, knife A, 9.4%), just a
  SHORT-range self-consistent ladder — and a short-range-dominated coupling is exactly what CANNOT carry
  a log (a log needs the long-range scale-invariant `1/r³` tail). This STRENGTHENS the no-log mechanism.
- **H3 — "grows-short is a self-subtraction artifact."** REFUTED. Both null controls — `α0=0` (no
  dipoles) and all-cells-removed — give `α_eff−1 = 0.0` EXACTLY. The grows-short signal is real medium
  physics, not an artifact of subtracting two empty-medium forces.

**Prereg parity (self-adversarial frozen-vs-shipped diff).** Every frozen §5 parameter matches the
shipped constants (K, d_sat, α0=0.03, damp=0.4, tol=1e-8, maxiter=400, n_r=16, n_ang=24, r_max_fac=1.2,
r_min_fac=1.05, min_sep=0.25, r_soft=0.3, window [30,3000] × 16); `χ_sat=1/√(1−A²)−1`, `E_yield=K/d_sat²`,
the exact inner linear solve, and the α0-robustness grid all match. The only deviations are the disclosed
verdict-preserving amendments A1.1 (interaction-force self-subtraction — a REPAIR of an ill-posed frozen
definition), A1.2 (antipodal sampling, n_ang=24 count preserved), A1.3 (orientation-averaging). No silent
deviation.

---

## 4. Machine gates (all pass under the pre-corrected criteria)

| Gate | Test | Result |
|---|---|---|
| **G-null (kernel-OFF)** — AMENDED amplitude axis | α0=0 ⇒ flat | ✓ `max\|α_eff−1\| = 0.0` (no dipoles ⇒ machine-ε flat) |
| **G-plant-log** — SIGN-CORRECT plant (`α/3π`, not the beta gate's sign-contradictory `1/3π`) | inject QED-form log → detect as log, right sign | ✓ `M_log`, `ΔBIC=+883`, grows-short detected |
| **G-plant-pow** | inject `p=0.3` power → detect as power, NOT log | ✓ `M_pow`, `ΔBIC=−1013`, recovered `p=0.300` (fitter does not over-privilege the log) |
| **G-separability** | at 2 decades, planted log and `p=0.3` power both decisively classified | ✓ PASS (`INCONCLUSIVE-RANGE` does not fire) |
| **G-genuineness-A** | Born ≠ converged | ✓ 9.4% change (not a spectator) |
| **G-genuineness-B** | bridge-removal changes result | ✓ 51% change (medium carries it) |

The beta gate's two frozen-design defects were **pre-corrected, not repeated** (prereg §6): the G-null
uses the amplitude criterion (not model-selection on `~1e-10` numerical noise), and the G-plant-log uses
the sign-correct `α/3π` plant (not the frozen `1/3π` formula that made `1/α` grow = the WRONG QED sign).

**Robustness (self-adversarial live-fire).**
- **`α0`-independent:** across `α0 ∈ {0.01, 0.03, 0.1, 0.2}` the transfer is NEVER `M_log` (all
  grows-short, `p ∈ [0.45, 0.65]`; the exponent softens with stronger coupling — moving TOWARD but never
  reaching the log-degenerate limit). `no_log_at_any_alpha0 = True`.
- **Window-independent:** at 3 decades (`R/d_sat ∈ [30, 30000]`) still decisive `M_pow`, `ΔBIC=−21.0`,
  `p≈0.55`, grows-short.
- **Tol-independent:** the transfer curve is byte-identical at SCF `tol = 1e-8` vs `1e-12` (the residual
  scatter is deterministic angular-discretization, killed by the orientation-average, NOT iterative).

---

## 5. Honest framing of the negative (Rule 11)

A single mechanism explains the whole result. The many-body self-consistent dipole-dipole ladder carries
a `1/r³` coupling whose spherical-shell integral `∫4πr²dr·r⁻³` would be logarithmic IF the
self-consistently-induced dipole DENSITY between the probes were scale-invariant (`∝1/r³`). The gate
measures that it is **NOT**: the Op14 saturation response — analytic and local per-cell — produces a
dipole density that falls FASTER than `1/r³`, so the shell integral yields a **power-law** screening
correction (`p≈0.60`), not the constant-per-decade accumulation a logarithm requires, even after the full
self-consistent resummation. The self-consistency genuinely softens the pairwise `p≈4.25` toward the
log-degenerate regime (`0.65 Born → 0.60 converged`, and softer at larger `α0`) but is bounded away from
`p=0` in the perturbative regime probed.

**This CLOSES the last open route** the beta gate named. The two gates together answer the QED-TRACE
program's only chord-class question completely: neither the two-body pairwise dress (beta gate,
WRONG-FORM, `p≈4.25`) nor the many-body self-consistent screening SUM (this gate, WRONG-FORM, `p≈0.60`)
emits `ln(q)`. QED's `ln` requires scale-integration over a NONLOCAL / scale-invariant polarization
kernel; the AVE saturation medium's response, being local-per-cell and analytic, does not supply the
scale-invariant density that would make the shell integral logarithmic. **Branch closed** — no rescue
attempted, no post-hoc criterion drop.

**The one honest upgrade over the beta gate (surfaced, not headlined):** the many-body sum gets the
transfer SIGN RIGHT (QED anti-screening; `α_eff>1` growing at short distance), where the beta gate's
pairwise transfer register had the WRONG sign. So the self-consistent screening ladder is qualitatively
MORE QED-like (right sign, softer exponent) than the pairwise dress — it is a near-miss in FORM, not a
categorical mismatch in sign. This is a genuine discriminating finding about the many-body sum, but it is
**not a chord**: the FORM (the thing QED's running IS) is a power law, not a logarithm.

---

## 6. Flags (flag-don't-fix — for auditor adjudication)

1. **Routed to auditor — q-g20f scoped-import re-tag can now DROP the "unprobed" caveat.** The beta
   gate's RESULT §7 required the q-g20f re-tag wording to inherit the "many-body scale-integrated route
   unprobed, NOT closed" boundary. **That boundary is now CLOSED (WRONG-FORM).** The re-tag can read as a
   full scoped import: AVE reproduces QED running as a scoped import, with BOTH the pairwise (`p≈4.25`)
   and many-body-self-consistent (`p≈0.60`) routes shown to give power laws, not `ln`. Implementer does
   NOT land the KB/manuscript entry.
2. **The many-body sum fixes the SIGN but not the FORM — a discriminating finding (surfaced).** The
   transfer register grows at short distance (QED direction) here, vs weakens in the beta gate. Any AVE
   "screening/running" claim should note that the many-body self-consistent ladder is qualitatively more
   QED-like (right sign, softened exponent) than the pairwise dress, but still power-law in FORM. Surfaced
   as a cross-cutting note (not landed).
3. **Numerical-robustness amendments (A1.1–A1.4) are integrator-time refinements, verdict-preserving.**
   The frozen transfer definition was ill-posed (self-force dominated); the self-subtraction (A1.1) is a
   REPAIR delivering the frozen intent (analog of the beta gate's own A1). Disclosed in the prereg
   amendment; the genuineness knives validate the repaired observable is physical.

---

## References (grep/read-verified this session at base `240d59d8`)

- Beta gate §7 open route (many-body SUM unprobed) — `research/2026-07-14_qed-trace-beta-gate_RESULT.md:214-217`
- Beta gate corrected mechanism (log via scale-integration over self-consistent hierarchy) — `…beta-gate_RESULT.md:210-213`
- Op14 capacitive/saturation grade — `src/ave/core/universal_operators.py:75-115,140-216` (clm-gdd70j)
- Beta-gate fitter + gates reused verbatim — `src/scripts/vol_2_subatomic/qed_trace_beta_gate.py:118-157,264-309`
- Frozen prereg (freeze commit `ee1fc728`) + AMENDMENT A1 — `research/2026-07-14_screening-sum-gate_prereg_FROZEN.md`
- Winding = charge carrier; sourced-charge no-go stays closed by its own argument — `clm-ze4clw`; `the-sourced-charge-no-go-cascade.md` (clm-nogo4l)
