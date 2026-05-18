# C8-BARYON-LADDER PDG-Anchored Driver — Pre-Registration

**Date**: 2026-05-18
**Target**: Build clean driver that re-anchors C8-BARYON-LADDER against PDG 2024 baryon table per matrix:557 explicit task. Re-verify 6 retrospective matches with pinned PDG row IDs + J^P consistency check; validate 3 forward predictions (2,17)/(2,19)/(2,21).
**Branch**: `analysis/c8-baryon-ladder-pdg-anchor`
**Skills applied explicitly per "full skills ahead" discipline**: `ave-prereg`, `pre-test-physics-check`, `substrate-native-check`, `ave-canonical-source`, `ave-driver-script-honesty`, `ave-discrimination-check`, `ave-evidence-framing-discipline`, `consistency-vs-emergence`, `verify-before-cite`

## Section 1 — Derivation target (precise)

Verify the AVE baryon mass formula `m(c)/m_e = I_SCALAR(8π/c) / (1 - V·8πα) + 1` at c ∈ {5, 7, 9, 11, 13} against PDG 2024 baryon masses, AND at c ∈ {17, 19, 21} as forward predictions. Where:

- `I_SCALAR(8π/c)` = Faddeev-Skyrme 1D solver scalar trace at coupling 8π/c
- `V = 2.0` (Borromean halo topological invariant, [`constants.py:693`](../src/ave/core/constants.py:693))
- `α = CODATA fine-structure constant`
- `m_e = CODATA electron mass`
- `c` = topological crossing number (odd, ≥ 5 for baryons; c=3 trefoil is electron, separate mechanism)

## Section 1.5 — Physical picture (5 bullets, mechanical/topological)

1. **Knot progression**: K4 substrate is chiral (I4_1 32), forces chiral knot selection. Golden Torus geometry forces torus-knot embedding (excludes hyperbolic). z=4 tetrahedral coordination matches p=2 simplicity. Result: (2,q_odd) ladder uniquely selected → q=3 electron, q=5 proton, q=7 Δ(1232), ...

2. **Mass mechanism**: Faddeev-Skyrme soliton on substrate. Phase profile φ(r) = π/(1 + (r/r_opt)^n) wound c times. Energy minimization over (r_opt, n) gives I_SCALAR(c). Confinement radius bound r_opt ≤ κ/c (more crossings = tighter winding = different inertia).

3. **Borromean halo**: V_total = 2 from Borromean linkage (3 mutually linked flux tubes, tensor crossing integral evaluates to ±2 chiral count). Renormalizes mass via (1 - V·p_c)⁻¹ factor.

4. **Zero free parameters per c**: AVE's FS solver replaces standard Skyrme's tunable F_π + e with substrate constants (ℓ_node = ℏ/m_e c, κ = 8π). For given c, solver output is determined.

5. **Discrete event**: at c=5 (cinquefoil) → proton 938 MeV; at c=7 (septafoil) → Δ(1232); at c=17 (forward) → predicted ~2742 MeV. Mass ratio m_p/m_e ~1836 emerges from 1 input (electron mass) + 1 topology (cinquefoil) + 1 halo (Borromean V=2).

## Section 2 — Corpus state (per ave-prereg Step 2, corpus-grep verified)

**Existing driver**: [`src/scripts/vol_2_subatomic/baryon_ladder_extension_c5_c25.py`](../src/scripts/vol_2_subatomic/baryon_ladder_extension_c5_c25.py) (197 lines) — extends production ladder to c=15-25, computes via canonical `_compute_i_scalar_dynamic`. **Honesty issues found**: hardcodes PDG values; no J^P consistency check; uses nearest-mass-only matching; stale docstring at line 17 ("c=9 → Δ(1620)" vs Vol 2 anchor "Δ(1600)").

**Production code**: [`constants.py:733-756`](../src/ave/core/constants.py:733) — `TORUS_KNOT_CROSSING_NUMBERS = [5, 7, 9, 11, 13]`; `_compute_baryon_ladder()` computes masses via FS solver.

**KB anchors**:
- Vol 2 canonical: [`torus-knot-ladder-baryons.md:11-13,17-24`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:11) — formula + 6 matches table
- Vol 4 KB anchor: [`torus-knot-baryon-predictions.md:8-13`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md:8) — forward predictions
- Vol 4 alt (STALE per audit): [`baryon-mass-predictions.md:11-17`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/baryon-mass-predictions.md:11) — uses different (2,q) convention; **walk-back queued, not in scope this commit**

**FI-13 independence**: C8 indexes by integer c (not by (p,q) tuple); FI-13 (2,5)-naming ambiguity affects LABELS not numerical masses. Driver is FI-13-independent per Section C of corpus-grep verification.

## Section 3 — Pre-Registration

### Step 3a — Skill discipline classification

Per `consistency-vs-emergence` 4-class taxonomy:

- **Class 4 (emergence test)** for c=7,9,11,13 baryons: formula computes mass from 1 input (m_e) + 1 topological integer (c) + 1 halo (V=2). No baryon-specific calibration.
- **Class 4 for c=5 (proton) also**: m_e is the calibration anchor; m_p/m_e is the prediction. Proton was NOT used to calibrate I_SCALAR (FS solver has no proton-anchored tuning per audit).
- **Class 4 for forward predictions** c=17,19,21: zero new inputs beyond existing calibration.

Per `ave-discrimination-check` D3 (post-hoc-fit risk): nearest-mass match without J^P discrimination has degree-of-freedom inflation risk. **Mitigation**: this driver requires J^P consistency check before declaring a match.

Per `ave-evidence-framing-discipline`: previous "0.00%" framing for proton is precision-rounding (true error 0.09%). **This driver reports true per-event errors to ≥3 sig figs.**

### Step 3b — Predictions (with verified PDG 2024 values)

| c | AVE prediction (MeV) | Candidate PDG state (J^P) | PDG 2024 mass (MeV) | Expected error |
|---|---|---|---|---|
| 5 | 938.3 | proton (1/2⁺) | 938.272 | 0.09% (precise) |
| 7 | 1262 | Δ(1232) (3/2⁺) | 1232 ± 2 | ~2.4% |
| 9 | 1582 | Δ(1600) (3/2⁺) | 1500-1700 | ~1.1% to center |
| 11 | 1895 | Δ(1900) (1/2⁻) | 1830-1930 | ~0.3% to center |
| 13 | 2195 | N(2190) (7/2⁻) | 2100-2200 | ~0.2% to center |
| 15 | 2478 | Δ(2420) (11/2⁺) | 2300-2500 | ~2.4% |
| 17 (forward) | 2742 | Δ(2750) (11/2⁻ ?) — PDG ** rating | ~2750 | ~0.3% |
| 19 (forward) | 2983 | N(3000)? — PDG * rating | uncertain | ~0.6% |
| 21 (forward) | 3199 | beyond current PDG catalog | — | TBD |

### Step 3c — Outcomes (discriminating)

- **Outcome A (PASS, ~50% pre-reg probability)**: all 6 retrospective matches reproduce per Vol 2 anchor's claimed errors (within rounding to 3 sig figs); J^P consistency holds for all 6 retrospective. Driver landed cleanly. Walk-back of Vol 4 alt anchor still queued separately.

- **Outcome B (PARTIAL, ~30%)**: 4-5 of 6 retrospective match; one or two have J^P inconsistency or have updated PDG masses that exceed claimed precision. Identify which fails honestly; document as scoping correction.

- **Outcome C (POST-HOC FIT EXPOSED, ~15%)**: J^P discrimination shows 1-3 matches are post-hoc-fit (nearest-mass that happens to be wrong J^P). Per `ave-discrimination-check`: walk back claimed match count.

- **Outcome D (FRAMEWORK FAIL, ~5%)**: PDG 2024 has substantially shifted from older values; multiple matches now exceed claimed precision; framework needs revisiting.

### Step 3d — Falsifiers

1. **J^P inconsistency**: if PDG row at predicted mass has WRONG spin-parity per (2,q) topological winding selection rule, match is post-hoc fit (Outcome C)
2. **Forward prediction miss**: if c=17 prediction (2742 MeV) has no PDG entry within ±5% AND PDG 2024 has any catalog entries in 2600-2900 MeV with conflicting J^P, forward chain weakens
3. **Cross-state consistency**: if formula's per-state errors are random-walk (no improvement at higher precision), the apparent "ladder" is coincidence; if errors are systematic (drift in one direction with c), formula has a derivable correction (~good)

### Step 3e — Driver scope

New file: [`src/scripts/verify/baryon_ladder_pdg_2024_anchor.py`](../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py)

Must:
- Import from `ave.core.constants` (no hardcoded α, m_e, p_c, V) — per `ave-canonical-source`
- Use canonical FS solver (`_compute_i_scalar_dynamic`) — per `substrate-native-check`
- Pin PDG row IDs in code comments (per matrix:557 task)
- J^P consistency check per state (allowed (2,q) torus-knot J^P from topological winding)
- Report ALL per-state errors to ≥3 sig figs (per `ave-evidence-framing-discipline`)
- Report null-hypothesis match rate (random hits in 24-baryon PDG window) for discrimination
- Output: structured JSON + human-readable summary

Result doc: [`research/2026-05-18_c8-baryon-ladder-pdg-anchor-result.md`](2026-05-18_c8-baryon-ladder-pdg-anchor-result.md) — log outcome regardless.

## Section 4 — Falsifier discipline (per `ave-prereg` Step 4)

Pre-reg committed BEFORE running script. Result will be logged regardless of outcome. No outcome rewrite. Failing matches will be documented honestly.

## Section 5 — Out of scope (this commit)

- Vol 4 anchor walk-back ([`baryon-mass-predictions.md:11-17`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/baryon-mass-predictions.md:11) uses different (2,q) convention) — separate walk-back cycle
- "0.00%" → "0.09%" framing correction in Vol 2 anchor — separate evidence-framing pass
- Stale docstring fix in existing `baryon_ladder_extension_c5_c25.py:17` — separate
- FI-13 (2,5) namespace disambiguation work — multi-week corpus-level

## Section 6 — Why this driver is the right next move

C8-BARYON-LADDER is FI-13-independent (formula uses integer c, not (p,q) topology assignment). Matrix:557 has an explicit pending task ("Pull PDG 2024 baryon table; verify 6 retrospective matches; pin PDG row IDs"). The existing extension script has honesty issues (hardcoded PDG, no J^P, nearest-mass-only). One clean driver addresses all three.

If this lands at Outcome A or even B, C8 becomes a forward-experimental anchor that's RIGOROUSLY documented per the 8-skill discipline. The framework gains a 6-emergence-test row with explicit PDG-2024 cross-reference. Strong position for matrix promotion.
