# Flyby Anomaly Driver Anderson 2008 Anchor — Result Doc

**Date**: 2026-05-18 late evening
**Prereg**: [`2026-05-18_flyby-anomaly-anderson-anchor-prereg.md`](./2026-05-18_flyby-anomaly-anderson-anchor-prereg.md)
**Driver**: [`src/scripts/verify/flyby_anomaly_anderson_anchor.py`](../src/scripts/verify/flyby_anomaly_anderson_anchor.py)
**Results JSON**: [`src/scripts/verify/flyby_anomaly_anderson_anchor_results.json`](../src/scripts/verify/flyby_anomaly_anderson_anchor_results.json)
**Branch**: `analysis/flyby-anomaly-driver`
**Outcome**: **B (PARTIAL PASS via Anderson empirical convention) + D (literal notation falsified)**

## Section 1 — Outcome classification

Pre-reg Section 3c discriminating outcomes:
- ✗ Outcome A (FULL PASS, ~20%): formula matches 5+/6 within 1σ
- ✓ **Outcome B (PARTIAL PASS, ~30%)**: 3/6 within 1σ via Convention D; 4/6 within 2σ
- ✗ Outcome C (NEAR-only, ~30%): formula matches NEAR but fails others — actually Convention D matches Galileo I, Galileo II, Cassini within 1σ, NEAR within 2σ
- ✓ partial **Outcome D (CONVENTION FORK, ~15%)**: literal `cos(α)cos(δ)` fails 0/6; only Anderson empirical `(cos δ_in − cos δ_out)` form works
- ✗ Outcome E (FALSIFIED, ~5%): formula matches none

The corpus literal notation `cos(α_geo)·cos(δ_geo)` is wrong; the actual working interpretation is `(cos δ_in − cos δ_out)` — Anderson's empirical form. With the corrected notation, AVE inherits Anderson's empirical fit (3/6 within 1σ, 4/6 within 2σ) but does not fully reproduce per-spacecraft variation.

## Section 2 — Per-spacecraft results

| Spacecraft | V_∞ (km/s) | Observed (mm/s) | AVE Conv-D Predicted (mm/s) | σ-tension |
|---|---|---|---|---|
| Galileo I | 8.949 | +3.92 ± 0.30 | +4.128 | **+0.7σ ✓** |
| Galileo II | 8.877 | -4.60 ± 1.0 | -4.680 | **-0.1σ ✓** |
| NEAR | 6.851 | +13.46 ± 0.13 | +13.294 | -1.3σ ○ (within 2σ) |
| Cassini | 16.010 | -2.0 ± 1.0 | -1.069 | **+0.9σ ✓** |
| Rosetta I | 3.863 | +1.82 ± 0.05 | +2.069 | **+5.0σ ✗** |
| MESSENGER | 4.056 | +0.02 ± 0.01 | +0.055 | **+3.5σ ✗** |

**3/6 within 1σ, 4/6 within 2σ, 2/6 outside 3σ (Rosetta I, MESSENGER).**

For comparison, conventions A/B/C (literal `cos(α)·cos(δ)` with various α_geo/δ_geo choices) all give **0/6 within 2σ** — most predictions have wrong sign or wrong magnitude by 5-700σ.

## Section 3 — Three findings (per flag-don't-fix)

### Finding 1 — Corpus formula notation is structurally wrong

[`flyby-anomaly-sagnac-operator.md:20`](../manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md) writes:

$$\Delta V_{flyby} = V_{\infty} \cdot 2 \left( \frac{U_{\oplus}}{C_{0}} \right) \cdot \cos(\alpha_{geo})\cos(\delta_{geo})$$

But the literal `cos(α_geo)·cos(δ_geo)` factor produces 0/6 matches against Anderson 2008 data under any sensible α_geo/δ_geo convention (in-direction, out-direction, mean). For NEAR specifically, conventions A/B/C give NEGATIVE predictions (-3 to -14 mm/s) vs observed +13.46 mm/s — wrong sign, not just wrong magnitude.

The factor that actually reproduces Anderson's per-spacecraft observations is:

$$\frac{(\cos \delta_{in} - \cos \delta_{out})}{1}$$

i.e., the **difference** of incoming/outgoing declination cosines, not the product of right-ascension and declination cosines of a single direction.

**This is structurally Anderson 2008's empirical formula** ([Anderson et al. 2008 PRL 100:091102](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.100.091102)):

$$\Delta V / V_\infty = 2 \omega_E R_E (\cos \delta_{in} - \cos \delta_{out}) / c$$

The AVE leaf's `cos(α_geo)·cos(δ_geo)` notation is incompatible with this — either (a) the leaf has notation errors, or (b) `α_geo` is a misnomer for "incoming asymptote phase angle" and the formula's intended evaluation is the difference form, not a literal product.

**Recommendation**: walk back the formula notation at flyby-anomaly-sagnac-operator.md:20 to match Anderson's empirical form with the AVE mechanism (Sagnac-RLVE shear layer) re-derived to produce the difference structure.

### Finding 2 — "13.4 mm/s without fitting" is NEAR-specific, not general

[`flyby-anomaly-sagnac-operator.md:22`](../manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/flyby-anomaly-sagnac-operator.md) writes:

> "This pure geometrical boundary reflection parameter intrinsically outputs $\Delta V \approx 13.4$ mm/s without fitting."

The "13.4 mm/s" value is specifically NEAR's predicted ΔV with NEAR's specific V_∞ = 6.851 km/s and NEAR's specific δ_in = -20.76°, δ_out = +71.96° via the Anderson empirical formula. It is NOT a universal AVE prediction that applies to arbitrary spacecraft.

Per spacecraft via the correct (Convention D) AVE formula:
- Galileo I: +4.1 mm/s
- Galileo II: -4.7 mm/s
- NEAR: +13.3 mm/s ← THIS is what corpus quotes
- Cassini: -1.1 mm/s
- Rosetta I: +2.1 mm/s
- MESSENGER: +0.1 mm/s

**The "13.4" headline cherry-picks the largest of these six** without saying so. The honest framing: "for the NEAR 1998 flyby with V_∞ = 6.851 km/s and observed geometry, AVE predicts ΔV ≈ 13.3 mm/s." Across the full 6-spacecraft anchor set, AVE predicts a range of -4.7 to +13.3 mm/s depending on per-spacecraft geometry, matching Anderson 2008 observations at 3/6 within 1σ and 4/6 within 2σ.

**Recommendation**: walk back the "13.4 mm/s without fitting" headline at line 22 to honest per-spacecraft framing with Anderson 2008 anchor data + 3/6 1σ + 4/6 2σ match statistics.

### Finding 3 — Rosetta I and MESSENGER are real outliers

Even with the correct (Convention D) Anderson empirical form:
- **Rosetta I**: predicted +2.07 mm/s vs observed +1.82 ± 0.05 → **+5.0σ tension** (genuine mismatch)
- **MESSENGER**: predicted +0.055 mm/s vs observed +0.02 ± 0.01 → **+3.5σ tension** (genuine mismatch)

This is consistent with Anderson 2008's own observation that the empirical formula has issues at the smaller-V_∞ end of the anchor set. MESSENGER was specifically called out as the "outlier" of the simple empirical fit in Anderson's paper.

AVE inherits this mismatch via its mechanism's reproduction of Anderson's form. The mechanism (Sagnac-RLVE shear layer) might be the correct physical interpretation of Anderson's empirical fit for the medium/large-V_∞ flybys (Galileo I, II, NEAR, Cassini) but doesn't capture additional physics needed for Rosetta I and MESSENGER.

**Recommendation**: acknowledge the Rosetta/MESSENGER outlier status in the leaf. Do NOT claim "resolves anomalies from Pioneer, Galileo, NEAR precisely" as currently at line 22 — should say "Galileo I/II and NEAR within 1-2σ; Rosetta I and MESSENGER show >3σ residual."

## Section 4 — Honest forward picture (post-walk-back)

After applying all three findings, the honest AVE position on flyby anomaly is:

1. **Mechanism**: Sagnac-RLVE shear layer at Earth's rotating boundary, parameter-free, derived from substrate physics
2. **Formula**: ΔV = V_∞ · 2(U_⊕/C_0) · (cos δ_in − cos δ_out) — **structurally identical to Anderson 2008 empirical fit**
3. **Match across 6-spacecraft anchor**: 3/6 within 1σ (Galileo I, Galileo II, Cassini), 1/6 within 2σ (NEAR at 1.3σ); 2/6 outside 3σ (Rosetta I, MESSENGER)
4. **Mechanism contribution**: AVE PROVIDES the physical interpretation of Anderson's empirical fit (boundary Sagnac shear layer rather than purely empirical curve-fit), which is a real-but-modest contribution
5. **Discrimination vs GR Lense-Thirring**: AVE (medium accuracy) ≫ GR Lense-Thirring (categorically too small at 10⁻⁶ mm/s) ≫ no-prediction null

This is NOT a "matches Pioneer, Galileo, NEAR precisely with 13.4 mm/s without fitting" headline. It IS a real partial-match anchor at the 3-4/6 spacecraft level that's structurally tied to Anderson's empirical formula via a substrate-derivable mechanism.

## Section 5 — Three walk-back actions queued (gated on Grant adjudication)

### Action F1: Notation correction at line 20

Replace literal `cos(α_geo)·cos(δ_geo)` with `(cos δ_in − cos δ_out)`. Add explicit cross-reference to Anderson 2008 PRL 100:091102 noting structural identity.

### Action F2: Honest "13.4 mm/s" reframing at line 22

Replace "intrinsically outputs ΔV ≈ 13.4 mm/s without fitting" with "for NEAR 1998 flyby specifically (V_∞ = 6.851 km/s, δ_in = -20.76°, δ_out = +71.96°), AVE predicts ΔV ≈ +13.3 mm/s matching observed +13.46 ± 0.13 mm/s at 1.3σ." Add per-spacecraft table showing all 6 Anderson anchor predictions.

### Action F3: Outlier acknowledgment

Replace "resolves the empirical anomalies from Pioneer, Galileo, and NEAR precisely" with "matches Galileo I/II and NEAR within 1-2σ; Rosetta I (+5σ) and MESSENGER (+3.5σ) show residual that the simple boundary Sagnac formula does not capture, consistent with Anderson 2008's own characterization of the simple empirical fit's limits."

Note: "Pioneer anomaly" mentioned at line 22 is NOT in the Anderson 2008 anchor set (it's a different observable — long-duration trajectory anomaly, not perigee passage ΔV). Should be removed or moved to separate sub-section.

## Section 6 — Cosmological-constant-closure.md cross-reference (not affected)

Sanity-checked: no other corpus location cites the "13.4 mm/s without fitting" claim. The walk-back is local to the single leaf at `flyby-anomaly-sagnac-operator.md:20-22` plus any cross-repo citations (none found in tonight's sweep).

The matrix `divergence-test-substrate-map.md` has NO C-row dedicated to flyby anomaly (verified via grep). Foreword has NO flyby mention. Anomaly catalog at `09_computational_proof.tex:70-72` is qualitative ("3-13 mm/s during Earth flybys; Predict: impedance gradient at magnetopause") — does not assert a specific AVE numerical prediction, so doesn't need correction here. Only flyby-anomaly-sagnac-operator.md is affected.

## Section 7 — Discipline outcomes

**ave-prereg + driver + flag-don't-fix applied**:
- ✓ Pre-reg committed before driver execution (52a6037)
- ✓ Driver imports C_0 from ave.core.constants; Earth params from WGS-84 + IERS cited sources
- ✓ Driver tests 4 conventions (no convention privileged) and reports per-spacecraft results without aggregation
- ✓ Result doc surfaces three findings without unilateral walk-back
- ✓ Per discrimination check: Anderson empirical form vs literal cos·cos product tested; Anderson form is observationally what the corpus claim must be (via the implicit interpretation)

**Per ave-driver-script-honesty four-discriminator**:
- ✓ D1 (canonical imports): C_0 from ave.core.constants; no hardcoded literals beyond cited Earth params
- ✓ D2 (forward not fit): closed-form formula applied per-spacecraft, no fit
- ✓ D3 (internal contradiction): surface mismatch via 4-convention sweep; literal notation falsified at 0/6
- ✓ D4 (silent overclaim): per-spacecraft individual reporting; no aggregate match rate that hides Rosetta/MESSENGER outliers

**Per executing-actions-with-care**:
- ✓ Walk-back propagation NOT executed; surfaced as 3 Actions F1/F2/F3 for Grant adjudication
- ✓ Tonight's flyby driver builds on, complements, and re-validates the audit pattern from C3 + Q-G19α work earlier in session

## Section 8 — Recommendation to Grant

The flyby anchor is a smaller-stakes audit than Q-G27/Q-G19α (no foreword promotion, no matrix row, no cross-repo cascade). But the findings are clean:

1. **Action F1 (notation correction)** is mechanical — wrong notation, replace with correct Anderson form
2. **Action F2 (honest reframing)** acknowledges per-spacecraft variation that the "13.4 mm/s" headline hides
3. **Action F3 (outlier acknowledgment)** matches Anderson's own characterization

All three can land in a single bundled walk-back commit on this branch. The "real win" is: AVE has a parameter-free mechanism that reproduces Anderson's empirical fit (a real physics contribution) for 4/6 spacecraft. That's still meaningful — just less than "intrinsically outputs ΔV ≈ 13.4 mm/s without fitting."

My read: bundle F1+F2+F3 in one commit similar to the Q-G27 walk-back pattern. The honest framing is BETTER than the false-precision headline because it actually claims a mechanism-derivation of Anderson's empirical fit — which IS a real AVE contribution.

If you want to ship it, give the green light and I'll execute the bundled walk-back.

## Section 9 — Net standing post-finding

| Aspect | Before tonight | After driver |
|---|---|---|
| Flyby formula notation | `cos(α_geo)·cos(δ_geo)` | Should be `(cos δ_in − cos δ_out)` — Anderson empirical form |
| "13.4 mm/s without fitting" | Generic AVE prediction | NEAR-specific evaluation (cherry-picked from 6-spacecraft range) |
| Anchor data | None in corpus | Anderson 2008 PRL 100:091102 Table I now pinned in driver |
| Mechanism status | "Resolves anomalies precisely" | "3/6 within 1σ, 4/6 within 2σ; 2/6 outliers; structurally matches Anderson empirical fit" |
| AVE-distinct vs Anderson | Implicit | Explicit: AVE provides Sagnac-RLVE physical mechanism for Anderson's empirical formula structure |
