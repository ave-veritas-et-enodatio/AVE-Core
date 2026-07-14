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

**The load-bearing new finding (what the SELF-CONSISTENT DRESSING changes vs the beta gate's pairwise
dress).** The self-consistent inter-cell ladder — which the re-adjudication (§3) localizes to each probe's
OWN near-cloud dress, not a medium sum — **SOFTENS the falloff dramatically**, from the beta gate's pairwise
`p≈4.25` to a shallow near-field `p≈0.60`, flattening TOWARD the log-degenerate regime — **but it stops
decisively short of a genuine log** (the per-decade log-slope collapses ~33×, §2). And it **fixes the SIGN**:
the transfer coupling now **GROWS at short distance** (`α_eff>1`), the **QED anti-screening direction**,
where the beta gate's pairwise transfer register weakened. The sign is carried by the near-cloud
self-cloud-distortion channel (§5, prereg A1.6), not the mediated medium. So the dressed pair earns the right
SIGN and DIRECTION of softening, but the FORM is not a logarithm: **right sign, wrong form.**

**Object class: PAIRWISE-DRESS with a near-cloud-internal many-body correction (RE-ADJUDICATED 2026-07-14
after adversarial review — see §3 and the "Review findings + repairs" map).** The two frozen genuineness
knives were originally read as "genuinely many-body". The review's same-mesh spatial decomposition (now
shipped as `genuineness_decomposition`, §3) re-adjudicates that under the frozen RELABELED-PAIRWISE rule
(prereg §4:154-161, §6):
- **Knife A (Born vs converged):** self-consistency changes the transfer departure by up to **9.4%** — this
  is REAL, but **near-cloud-INTERNAL**: the Born-vs-converged change is fully reproduced on a near-cloud-only
  mesh (mid/far medium adds nothing to it). A genuine ~9% many-body correction to the dress of each probe's
  OWN cloud, not a screening sum through the medium.
- **Knife B (remove intervening cells) — RE-ADJUDICATED, KEEP-BOTH:** the shipped `|z|<R/2 & ρ<R/2` CYLINDER
  removal reads ~50% *only because it slices each probe's near dress in half* (a disclosed near-dress-slicing
  artifact; also a seed lottery — the driver measures 0.26% at the smoke seed vs 51.05% (R=100) / 58.31%
  (R=1000) at the shipped seed). The TRUE intervening medium (cylinder MINUS near dress) carries **~0.01–0.02%** while the
  two near clouds carry **~100%**. Under the corrected reading of "intervening cells" (the prereg's own
  structural-null stencil-lens intent) the medium is a **relative spectator ⇒ RELABELED-PAIRWISE**.
  **Primary = the corrected reading.**

> ⚑ **FLAGGED for Grant ratification (do-not-bury).** Whether "intervening cells" (prereg §4:157) should be
> read as the TRUE mid-bridge medium (excluding each probe's own near dress) is the crux interpretive step.
> KEEP-BOTH is recorded (shipped-cylinder = 50% near-dress-slicing / corrected mid-bridge = ~0.02% spectator);
> the corrected reading is primary; **Grant ratifies this interpretive step before the q-g20f re-tag propagates.**

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

- **TRANSFER register** (through-coupling `F_transfer(R)/F_bare(R)`, PRIMARY): departs **ABOVE 1** and grows
  at short distance (`α_eff>1`, larger near `R=30`) — the QED anti-screening direction (sign attribution in
  §3/§5: carried by the near-cloud channel, not the mediated medium). **FORM (reframed 2026-07-14 per
  adversarial review):** the departure is a **steep near-field falloff plus an R-independent floor**
  (`dep ≈ 0.006` in the outer decade, NOT `→1`), and it is **decisively NOT a log** — the per-decade
  log-slope collapses **~33×** (`c₁ ≈ −0.0161 → −0.0005`) where a genuine log requires it constant. The
  whole-window fit `M_pow, p≈0.600, a≈0.333, ΔBIC = −24.7` is a compromise over that composite (§2 floor
  note); the DECISIVE content is the collapsing per-decade slope, not the global exponent. **WRONG-FORM
  (not-a-log), RIGHT sign.**
- **REACTIVE register** (`W_sat/W_lin`, stored-energy dress, KEEP-BOTH, NOT binned): departs **ABOVE 1**
  (grows at short distance), fit `M_log` `p=0.300` (railed at the grid floor = the log-degenerate limit).
  The reactive register is dominated by the `R`-independent near-probe cloud (the innermost shell sits at
  `ρ≈1.05 d_sat` regardless of `R`), so its scale-dependence is weak and log-degenerate — exactly the
  register the beta gate flagged as sign-artifactual. Reported for completeness; **the verdict is read on
  the transfer register**, per the frozen requirement.
- **`register_flip_observed = False`.** Unlike the beta gate (opposite SIGN by register), here BOTH
  registers grow at short distance — the sign does not flip between registers, though the FORM differs
  (transfer = steep near-field power + R-independent floor; reactive = log-degenerate near-cloud dress).

See figure (`qed_trace_screening_sum_gate.png`): the transfer departure is a **steep near-field falloff that
flattens to an R-independent floor in the outer decade** (CORRECTED 2026-07-14 — it is NOT a straight line in
log-log across the whole window; the earlier "straight line, a genuine log would curve" claim was false in
the outer decade, where the departure is flat-to-rising). The no-log evidence is the per-decade log-slope
collapsing ~33×, not straightness. Born and converged nearly overlap (self-consistency softens but does not
change the form).

---

## 2. Frozen 5-bin classification

| Bin | Fired? | Evidence |
|---|---|---|
| LOG-EMERGES | ✗ | transfer fit selects `M_pow`, not `M_log`; per-decade log-slope collapses ~33× (a log needs it constant). NOTE: the OUTER-HALF `[300,3000]` alone refits `M_log` (`ΔBIC=+11.9`) — this is the **R-independent floor masquerading as a log** (a flat plateau read as a slow log by a family with no floor term), NOT log-emergence (§2 floor note); the bin does NOT flip. |
| **WRONG-FORM** | **✓ (SELECTED)** | transfer register is a **steep near-field falloff + R-independent floor, decisively not-a-log** (per-decade log-slope collapses ~33×); `α0`-independent (never `M_log`); 3-decade-robust (`ΔBIC=−21.0`). The global `p≈0.60` is a whole-window compromise over the composite (floor = pairwise-class, §2). |
| WRONG-SIGN | ✗ | transfer α GROWS at short distance (`α_eff>1`) = the RIGHT (QED) sign — the wrong-sign bin does NOT fire (contrast the beta gate, whose transfer register weakened) |
| NULL-FLAT | ✗ | the departure is non-negligible (`α_eff−1 ≈ 0.006–0.044`); the sum is not inert |
| INCONCLUSIVE-RANGE | ✗ | separability gate PASSES at 2 decades; `ΔBIC` is decisively past `±10` |

**★ Form-number honesty (2026-07-14 adversarial review — cluster-2 repair).** The decisive content is the
*collapsing per-decade log-slope*, not the global exponent `p`:
- The full-window `ΔBIC=−24.7 / p≈0.60` is **not window-stable**: sub-window `[30,300]` refits `p≈0.68,
  ΔBIC=−3.5` (INCONCLUSIVE) and `[300,3000]` refits `p≈0.06, ΔBIC=+0.05` (INCONCLUSIVE); on the frozen
  155-point grid the outer window rails to `M_log ΔBIC=+11.9`. The "decisive" margin lives only across the
  whole window, driven by the steep inner decade (my refits reproduce all of these).
- The outer decade sits at an **R-INDEPENDENT floor** (`dep ≈ 0.006–0.008`, flat-to-rising), which a
  3-parameter `1 + a(R_ref/R)^p + c` fit captures (`floor≈0.0051, p≈0.87, SSE 7.1e-5`) better than the
  frozen fixed-intercept-1 power (`SSE 1.2e-4`). The frozen fit family has **no floor term**, so it cannot
  represent the plateau and compromises the exponent.
- **The floor is pairwise-class** (consistent with §3): it is the dressed-probe induction term
  (`δp ∝ E₂ ∼ 1/R²` gives `F/F_bare = const`), i.e. the near-cloud dress — NOT a medium screening sum.
- **The bin does NOT flip to LOG-EMERGES.** The outer-half `M_log` is the floor artifact (a flat plateau
  read as a slow log by a family with no floor term), not a genuine constant-per-decade accumulation. The
  no-log verdict is SAFE and, via the 33× slope-collapse, STRONGER than the raw BIC statement.
- **The naked `p≈0.60` must NOT be cited in the q-g20f re-tag** until a floor-augmented refit
  (`1 + a(R_ref/R)^p + c`) resolves it — registered as the routed follow-on fit family in the prereg
  amendment (A1.7).

**Genuineness precondition (frozen §4) — RE-ADJUDICATED (2026-07-14).** As shipped, both knives passed on
the cylinder reading (§3), reporting "genuinely many-body". The corrected same-mesh decomposition (§3, now a
committed code path) re-adjudicates to **RELABELED-PAIRWISE-class** under the frozen rule: the true
intervening medium is a relative spectator (~0.02% vs ~100% near-dress), so the object is a
self-consistently-dressed PAIRWISE pair, not a screening sum through the medium. KEEP-BOTH recorded;
corrected reading primary; the "intervening cells" interpretive step FLAGGED for Grant. **The `WRONG-FORM` /
no-log verdict is UNAFFECTED and in fact STRENGTHENED** — a spectator medium has nothing to accumulate per
decade, so no log can form.

**Consequence (frozen, prereg §4).** Category closure COMPLETE: the many-body scale-integrated route
ALSO fails to emit `ln(R)`. The beta gate's §7 "many-body screening SUM … UNPROBED, NOT CLOSED" boundary
is now **CLOSED (WRONG-FORM)**. The q-g20f "Identical (RT-equivalence)" scoped-import re-tag can now DROP
the "unprobed, not closed" caveat and read as a full scoped import. **The re-tag is routed to the
auditor** (implementer lane does not land the KB/manuscript entry).

**Scope of the null (frozen concession).** Scoped to *the classical + kernel-ON lattice, self-consistent
polarizable-cell screening between seeded windings, perturbative window*. It does not re-open or re-close
the sourced-charge no-go (`clm-nogo4l`), which stays closed by its own argument.

---

## 3. ★ MANY-BODY-GENUINENESS RECEIPT — RE-ADJUDICATED (2026-07-14 adversarial review)

The load-bearing question the prereg's structural-null stencil lens demands: is this the many-body sum, or
the pairwise dress relabeled? The two frozen knives, as shipped, read "genuinely many-body." The review's
same-mesh spatial decomposition (now the committed `genuineness_decomposition` code path) shows the shipped
Knife B receipt does NOT measure medium-mediation, and **re-adjudicates the object to
RELABELED-PAIRWISE-class** (a self-consistently-dressed pairwise pair). KEEP-BOTH is recorded below; the
corrected reading is primary; the interpretive step is FLAGGED for Grant.

**Knife A — Born vs converged (self-consistency must change the result).** The Born comparator turns the
inter-cell dipole coupling OFF in the `p`-equation (dipoles respond to the probe field only):

| | selected | `p` | max frac-change (conv vs Born) | coeff ratio (conv/Born) | exponent shift |
|---|---|---|---|---|---|
| Born | `M_pow` | 0.650 | — | — | — |
| Converged | `M_pow` | 0.600 | **9.4%** | **0.778** | **−0.05** |

Self-consistency changes the transfer departure by up to **9.4%** (`≫ 1e-6` threshold), reduces the
coefficient to `0.78×`, and softens the exponent by `0.05` (`G_genuineness_A_pass = True`). It does NOT
change the FORM (both power). **Re-adjudication (2026-07-14):** this ~9% self-consistency correction is
**near-cloud-INTERNAL** — an implementer live-fire rerun of Knife A on a near-cloud-only mesh reproduces the
SAME fractional change as the full mesh (`0.60% ≡ 0.60%` at R=100, `0.00% ≡ 0.00%` at R=1000, same
decomposition mesh; the 9.4% peak is at small `R`). So the "many-body" content of Knife A is the inter-cell
ladder WITHIN each probe's own
dress cloud responding to the other probe — a genuine ~9% many-body correction to a **pairwise dress**, not
a screening sum through the medium. This is why the object re-adjudicates to pairwise-dress-class (below).

**Knife B — remove intervening (bridge) cells — RE-ADJUDICATED (corrected decomposition, KEEP-BOTH).** The
shipped knife removed the `|z|<R/2 & ρ<R/2` CYLINDER and read ~50%. The review's same-mesh decomposition
(committed as `genuineness_decomposition`; **near** = within `10·d_sat` of either probe = each probe's OWN
dress; **mid-bridge** = cylinder MINUS near dress = the genuine intervening medium; **far** = beyond
`10·d_sat` of both) shows what that ~50% actually is (my orientation-averaged run, seed `ORIENT_SEED+1`):

| `R/d_sat` | remove FAR (exterior) | remove NEAR (each probe's dress) | remove TRUE mid-bridge (the medium) | remove SHIPPED cylinder |
|---:|---:|---:|---:|---:|
| 100  | 0.009% | **99.99%** | **0.012%** | 51.05% (n_mid 140 / n_cyl 213) |
| 1000 | 0.026% | **99.97%** | **0.016%** | 58.31% (seed-lottery; smoke seed gives 0.26%) |

**The two near clouds carry ~100%; the TRUE intervening medium carries ~0.01–0.02%; the exterior ~0.01–0.03%.**
The shipped cylinder's ~50% arises ONLY because `|z|<R/2 & ρ<R/2` slices each probe's near dress in half
(the ~73 near-cloud cells captured by the cylinder carry the whole ~50%; the ~140 genuine mid cells carry ~0).
Its magnitude is a **seed lottery** (0.26% at the smoke seed → 51–72% at the shipped seed), confirming it is
not a stable medium-mediation measurement.

- **KEEP-BOTH.** *Shipped-cylinder reading:* `α_eff` changes ~50% ⇒ (as-read) `G_genuineness_B_pass = True`
  — RETAINED, but disclosed as **near-dress slicing**, not medium-mediation.
- **Corrected reading (PRIMARY):** removing the TRUE intervening medium (mid-bridge) changes `α_eff`
  ~0.01–0.02% — ~4 orders of magnitude below the near dress. The medium is a **relative spectator** ⇒
  **RELABELED-PAIRWISE** under the frozen rule (prereg §4:157: "removing the intervening cells does not
  change the result → RELABELED-PAIRWISE"), read with "intervening cells" = the genuine mid-bridge medium.

> ⚑ **FLAGGED for Grant ratification.** The frozen rule keys on "removing the intervening cells." Reading
> "intervening cells" as the mid-bridge medium (excluding each probe's own dress) — the prereg's own
> structural-null stencil-lens intent — is the crux interpretive step; Grant ratifies before propagation.

**Self-adversarial receipts (now shipped as committed code paths).**
- **H1 (spatial specificity) — CORRECTED by the decomposition above.** The originally-quoted "bridge-removal
  64.7% vs equal-count exterior 0.0%, a 4369× ratio" measured NEAR-vs-FAR specificity (real: far removal
  ~0.01%, near removal ~100%) but was MIS-READ as interaction-path-vs-exterior. The genuine interaction-path
  mid-bridge contributes the SAME ~0 as the exterior, so the specificity discriminates near-dress from
  everything-else, NOT the screening path from the exterior. Shipped as `genuineness_decomposition` (replaces
  the previously un-committed 4369× receipt).
- **H2 (short-range-dominated) — SHIPPED as `dipole_truncation_leg`.** Truncating the inter-cell dipole
  matrix at `5 d_sat` leaves the exponent essentially IDENTICAL (`p` 0.600→0.600 in the shipped run) — the
  coupling lives entirely within ~5 d_sat, i.e. it is **near-cloud-internal / short-range-dominated**,
  exactly what CANNOT carry a long-range scale-invariant `1/r³` log. This STRENGTHENS the no-log verdict and
  is consistent with the pairwise-dress re-adjudication.
- **H3 (grows-short null controls) — SHIPPED (kernel-off + all-cells-removed).** Both `α0=0` (no dipoles) and
  all-cells-removed give `α_eff−1 = 0.0` EXACTLY; the grows-short signal is real medium physics, not a
  subtraction artifact of two empty-medium forces.
- **Tol-invariance — SHIPPED as `tol_invariance_leg`** (transfer curve invariant across SCF `tol` 1e-8↔1e-12;
  residual scatter is deterministic angular-discretization, orientation-averaged, not iterative).

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

> 🔴 **FALSIFYING-EVIDENCE HEADER (2026-07-14 adversarial review; Rule-12 preserve-plus-header — no silent
> rewrite, no substituted mechanism).** The mechanism paragraph PRESERVED VERBATIM below is **AFFIRMATIVELY
> MISATTRIBUTED**. The same-mesh spatial decomposition (§3, committed `genuineness_decomposition`) shows the
> intervening medium's shell integral contributes **~0.01–0.02%** of the departure (the near dress carries
> ~100%). Therefore `p≈0.60` is **NOT a shell-integral exponent over a scale-invariant medium density** — it
> is the near-cloud (pairwise-dress) falloff. Per the anti-substitution rule (A47 v11b) NO replacement
> shell-integral mechanism is offered; the corrected no-log mechanism is stated AFTER the preserved text.
>
> *Preserved (falsified) body:* "A single mechanism explains the whole result. The many-body self-consistent
> dipole-dipole ladder carries a `1/r³` coupling whose spherical-shell integral `∫4πr²dr·r⁻³` would be
> logarithmic IF the self-consistently-induced dipole DENSITY between the probes were scale-invariant
> (`∝1/r³`). The gate measures that it is NOT: the Op14 saturation response — analytic and local per-cell —
> produces a dipole density that falls FASTER than `1/r³`, so the shell integral yields a power-law screening
> correction (`p≈0.60`), not the constant-per-decade accumulation a logarithm requires, even after the full
> self-consistent resummation. The self-consistency genuinely softens the pairwise `p≈4.25` toward the
> log-degenerate regime (`0.65 Born → 0.60 converged`, and softer at larger `α0`) but is bounded away from
> `p=0` in the perturbative regime probed."

**Corrected no-log mechanism (2026-07-14).** The object is two self-consistently-dressed probes interacting
through their OWN near clouds — a **pairwise dress** with a ~9% near-cloud-internal many-body correction
(Knife A, §3). The intervening medium between the probes — the region whose scale-invariant `1/r³` dipole
density WOULD be required to make a shell integral logarithmic — contributes **~0 per decade** (mid-bridge
removal changes `α_eff` ~0.01–0.02%, §3). **There is nothing to accumulate, so no log can form.** This is a
STRONGER no-log statement than the BIC margin: the medium simply does not carry a scale-integrated response.
Independently, the per-decade log-slope of the departure collapses **~33×** between decades (`c₁ ≈ −0.0161 →
−0.0005`), where a genuine log requires it constant (§2). The `p≈0.60` is a whole-window compromise fit over
a composite (steep near-field falloff + an R-independent floor, §2), not a medium shell-integral exponent.

**This CLOSES the last open route** the beta gate named. The two gates together answer the QED-TRACE
program's only chord-class question completely: neither the two-body pairwise dress (beta gate,
WRONG-FORM, `p≈4.25`) nor the many-body self-consistent screening SUM (this gate, WRONG-FORM, `p≈0.60`)
emits `ln(q)`. QED's `ln` requires scale-integration over a NONLOCAL / scale-invariant polarization
kernel; the AVE saturation medium's response, being local-per-cell and analytic, does not supply the
scale-invariant density that would make the shell integral logarithmic. **Branch closed** — no rescue
attempted, no post-hoc criterion drop.

**The one honest upgrade over the beta gate (surfaced, not headlined; channel-attributed 2026-07-14).** The
transfer SIGN is RIGHT (QED anti-screening; `α_eff>1` growing at short distance), where the beta gate's
pairwise transfer register had the WRONG sign. **Channel attribution (adversarial-review repair, cluster-3;
disclosed in prereg A1.6):** the verdict-carrying signal — the power FORM AND the QED sign — lives in the
**near-cloud self-cloud-distortion channel** (probe-2's presence distorting probe-1's OWN dress cloud), NOT
in the mediated medium screening the mechanism sentence described. A linear source-decomposition (force on
probe-1 from probe-2-sourced dipoles at the frozen converged medium) — the mediated-only channel — is flat
at ~1.001–1.002 across the window (~0–10% of the departure); the shipped `F(both)−F(self)` total-force
definition (A1.1) lumps in the nonlinear saturation cross-term that carries the other ~90%+. This lumping is
a **legitimate EFT-style total-interaction-force definition** (the actual change in force on probe-1 caused
by probe-2, including the nonlinear cross-term), and no alternative repair yields a decisive CONTRARY (log)
bin — but it must be **disclosed as such**: the "right sign" is a near-cloud saturation-cross-term result,
consistent with the pairwise-dress re-adjudication (§3), not a medium-mediated screening result. A genuine
discriminating finding about the dressed pair, but **not a chord**: the FORM is a power law, not a logarithm.

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
