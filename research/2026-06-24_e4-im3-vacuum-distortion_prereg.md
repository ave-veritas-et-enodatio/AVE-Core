# PRE-REG — E4-IM3-DISTORTION (vacuum IM3 / harmonic-distortion / nonlinear-birefringence δn(E))

**Frozen:** 2026-06-24 · **Branch:** `analysis/e4` (off origin/main `bffc16b9`) · **SHA-pinnable on `analysis/e4` HEAD**
**Driver:** `src/scripts/vol_9_device/im3_vacuum_harmonic_distortion.py` (constants live from `ave.core.constants`)
**Result doc:** `research/2026-06-24_e4-im3-vacuum-distortion.md`
**Claims touched:** clm-pp3qwf (coefficient discriminator), clm-vjv4zf (vacuum varactor)

---

## Hypothesis

The AVE vacuum (Axiom-4 saturation kernel `S(A) = √(1−A²)`, `A = E/E_yield`) produces nonlinear optics: an E²-leading index shift `δn`, cubic-in-drive IM3 distortion, and a **categorical static-B transparency** (the μ-grade is an `I`-keyed relativistic inductor, so a static `B` with `∂B/∂t = 0` leaves it unloaded, `S_μ = 1`, `δn_μ = 0` exactly).

## Frozen derived values (live from `ave.core.constants`, `bffc16b9`)

| Quantity | Frozen value | Status |
|---|---|---|
| `S(A)` | `√(1−A²)` | Axiom-4 (input) |
| `C(V)/C₀` Taylor | `1 + ½A² + ⅜A⁴` | DERIVED (MANIFESTATION) |
| `δn_iso` (single-arm) | `−¼A²` | DERIVED (E²-leading) |
| `δn_bir` (par−perp) | `−½A²` | DERIVED (falsifier observable) |
| IM3 drive exponent | `3` (cubic) | DERIVED — SHARED with QED |
| `E_yield` | `1.130×10¹⁷ V/m` | `√α·E_crit` (α-echo) |
| `E_crit` | `1.323×10¹⁸ V/m` | Schwinger |
| `(E_crit/E_yield)²` | `1/α = 137.036` | substrate identity |
| ratio_diff `7.5/α³` | `1.930×10⁷` | FORM derived / MAGNITUDE α-echo |
| static-B `δn_μ` | `0` exactly | DERIVED, parameter-free |

## Bankable number (the prediction)

At `E = 2.745×10¹⁴ V/m` (PW-class focal, `A = 2.43×10⁻³`):
**AVE: `δn_bir = −2.95×10⁻⁶`** vs **QED: `δn_bir = +1.53×10⁻¹³`** → ratio `1.93×10⁷` (field-independent, matched par−perp differential).

## FALSIFIERS

### PRIMARY (the chord — parameter-free, ranked first)
A **static-B vacuum birefringence detection at or above the QED level (~10⁻²³ at 5 T)** FALSIFIES AVE. AVE predicts `δn_μ = 0` EXACTLY at every static-B field (`S_μ = 1`, `A_I ≡ 0`, no `∂B/∂t`). Parameter-free — rides no α, no fitted coefficient. QED is E/B symmetric and predicts nonzero static-B birefringence; AVE predicts categorical zero.
*Decisiveness caveat: requires static-B sensitivity at QED ~10⁻²³ level; until then a clean falsifier without a confirming measurement.*

### SECONDARY (coefficient — α-echo magnitude)
At the matched par−perp E-route differential, a **QED-sized coefficient** (`δn_bir ~ (3/45)α²(E/E_crit)²`, ~10⁷× below AVE at matched field) FALSIFIES AVE; an AVE-sized coefficient (`−½(E/E_yield)²`) falsifies QED. Magnitude ratio `7.5/α³ ≈ 1.93×10⁷` is α-echo-flagged (FORM AVE-distinct, value rides α⁻³).

## NON-FALSIFIERS (explicitly excluded — do NOT re-open)
- An **E² slope** does NOT falsify AVE (both AVE and QED are E²-leading; "E⁴ vs E²" is RETRACTED, clm-pp3qwf, √ε-conflation).
- An **IM3 cubic (slope-3) drive law** does NOT discriminate (both AVE/QED IM3 are χ⁽³⁾ cubic; QED's "sextic" is the frequency exponent, not a drive slope).

## Bench (E-route / HIBEF)
- **Route:** static / DC-biased **E** (NOT static B — that leaves the μ-grade unloaded).
- **Facility:** HIBEF @ European XFEL + PW-laser focal sources.
- **Observable 1:** par−perp δn → ellipticity ψ (CW high-F cavity, `g_eff = 0.251`, `ψ_AVE ≈ 2.2×10⁻² rad` at PW field; polarimetry floor ~10⁻⁹ rad).
- **Observable 2:** dual-tone IM3 at `2f₁−f₂`/`2f₂−f₁`; −80 dBc floor needs `E ≈ 1.3×10¹⁵ V/m` (facility-class).
- **Static-B null check:** apply 2.5 T → 1 kT; AVE δn = 0 exactly (the chord's kill-switch).

## Adjudication criteria (frozen — no post-hoc drop, Rule 11)
- PRIMARY decides the chord; SECONDARY decides the coefficient form/value.
- E²-slope and IM3-cubic results are pre-committed NON-falsifiers and will not be converted to falsifiers post-hoc.
- A QED-sized coefficient ⇒ AVE falsified at the coefficient observable (clean negative, record + close).
