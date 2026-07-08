# P6 — sidereal boost-order re-derivation: RESULT

**Status:** RESULT. Adjudicates the FROZEN fork in `research/2026-07-08_p6-sidereal-boost-order_prereg.md`.
**Date:** 2026-07-08
**Class:** CONSISTENCY (order-of-magnitude registration audit; no new claim-id / constant / axiom).
**Driver:** `src/scripts/vol_9_device/p6_sidereal_boost_order.py` (run: `PYTHONPATH=src python3 src/scripts/vol_9_device/p6_sidereal_boost_order.py`).
**Artifact:** `assets/sim_outputs/p6_sidereal_boost_order.json` (gitignored; regenerate with the driver).
**Loci audited (NOT edited here):** `papers/2026_birefringence_letter/main.tex:420-432`, `.../provenance.md:40-43`.

---

## VERDICT

**FIRST-ORDER in β (radiation-field Doppler).** The pump is a propagating EM plane wave; its amplitude
obeys the relativistic Doppler transform, which carries a nonzero **linear-in-β** term. The registered
`(v/c)² ≈ 1.5e-6` is the order of a STATIC field and does not apply to the radiation-driven observable.
The registration is off by **~3–3.5 orders of magnitude** and mislabels the dominant harmonic.

## THE LOAD-BEARING PREMISE (stated up front, per flag-don't-fix)

The sidereal signal exists **only if the model's dynamical response frame is the CMB rest frame**
(v ≈ 370 km/s). This is the paper's own conditional (`main.tex:420-421`). There is an *unresolved internal
tension* we do NOT settle: `main.tex:404-406` states the prediction is "stated in the lab frame of the
optical focus, where the pump field magnitude is defined." **If the response frame is the lab frame, the
sidereal modulation is exactly zero** (nothing to Doppler-modulate). This re-derivation fixes the ORDER
*given the CMB-frame premise*; it does not adjudicate the frame. That premise is what carries the whole
result and is surfaced for Grant, not silently chosen.

## THE PHYSICS (why radiation is O(β) and static is O(β²))

The signal-carrying field is the **pump**: a propagating vacuum EM mode with `E` and `B` locked as
`B = E/c`. Under a boost, that locked companion supplies a `v×B` cross-term, so the field amplitude
transforms by the plane-wave **Doppler factor** `D(θ) = 1/[γ(1 − β cosθ)] = γ(1 + β cosθ′)`. A **static**
reactive field has no such locked companion in its own rest analysis; its transverse magnitude picks up
only the tensor dilation `γ`. The β-expansions make the fork decisive
(sympy-verified — `src/scripts/vol_9_device/p6_sidereal_boost_order.py::symbolic_orders`):

```
D   (pump amplitude, field^1) = 1 + β cosθ + β²(cos²θ − ½) + …      linear coeff = cosθ  ≠ 0
D²  (δn_bir ~ A^2, field^2)    = 1 + 2β cosθ + …                     linear coeff = 2cosθ ≠ 0
D⁴  (P_flip ~ field^4)         = 1 + 4β cosθ + (10cos²θ − 2)β² + …   linear coeff = 4cosθ ≠ 0
γ   (STATIC field magnitude)   = 1 + ½β²                             linear coeff = 0
```

The radiation branch has a nonzero linear-in-β term at every power of the field; the static branch's
first nonzero term is `β²`. Per the frozen §3 adjudication rule (`D` linear ≠ 0 AND `γ` linear = 0),
the pump is **branch (a), O(β)**. The registration used the static-branch order (`γ`) for a
radiation-branch observable — a REGIME substitution (static field ↔ radiation field), the exact
class of error the regime-discipline gate exists to catch.

## PROPAGATION TO THE OBSERVABLE (P_flip ∝ field⁴)

Repo chain (`ave.bench.birefringence`): `δn_bir = −½A²`, `A = E/E_YIELD` ⇒ `δn ∝ E²`; flip probability
`P_flip = sin²(Δφ/2) ≈ (Δφ/2)²`, `Δφ ∝ δn·L` ⇒ **`P_flip ∝ E⁴`**. With `E → D·E`:

| observable | scaling | leading sidereal modulation | best-case amplitude |
|---|---|---|---|
| δn_bir coefficient | `∝ D²` | `2β cosθ` | **2β = 2.468×10⁻³** |
| P_flip (headline) | `∝ D⁴` | `4β cosθ` | **4β = 4.937×10⁻³** |

`β = v_CMB/c = 370×10³ / 299792458 = 1.234187×10⁻³` (c from `ave.core.constants.C_0`, CODATA-exact;
v_CMB EXTERNAL astrophysical input). Both amplitudes carry a per-site geometric projection factor
`c₁ ≤ 1` (below); the table gives the aligned best case `c₁→1`.

## CORRECTED NUMBER vs REGISTERED (verbatim from the driver compute)

```
P_flip     first-harmonic amp (4 beta)   : 4.937e-03      <-- CORRECTED headline
delta_n_bir first-harmonic amp (2 beta)  : 2.468e-03      <-- CORRECTED coefficient
P_flip     second-harmonic amp (5 beta^2): 7.616e-06      <-- the O(beta^2) piece (subdominant)
registered (v/c)^2 static branch          : 1.523e-06      <-- what the paper carries
P_flip 1st-harmonic is 3.51 OOM ABOVE the registered number
```

So the registered **1.523×10⁻⁶** should read **≈ 4.9×10⁻³** for the flip probability (or ≈ 2.5×10⁻³ for
the δn coefficient) — **~3.5 OOM larger**, and the falsifier becomes correspondingly more accessible.

**Precise diagnosis (flag-don't-fix):** the registered `β²` is NOT nonsense — it is the correct order of
the **second-harmonic** term (`5β² ≈ 7.6×10⁻⁶`, within a factor ~5 of the quoted `1.5×10⁻⁶`). The
registration captured the sub-dominant piece and **missed the dominant first-harmonic β term**. The
paper's phrase "at the sidereal frequency (and its harmonics)" is also imprecise: at O(β²) the dominant
sidereal harmonic is the SECOND (2×sidereal); the first harmonic only appears once the O(β) radiation
term is included.

## ANGULAR / TEMPORAL SIGNATURE

`cosθ(t) = n̂(t)·d̂` (lab pump/probe axis `n̂` rotating with Earth; CMB dipole `d̂` fixed inertial)
`= c₀ + c₁ cos(Ω_sid t − φ)`. Substituting into `D⁴ ≈ 1 + 4β cosθ + (10cos²θ − 2)β²`:

- **FIRST (fundamental) sidereal harmonic — DOMINANT:** amplitude `4β·c₁`, up to `4β = 4.9×10⁻³`.
  Period = one **sidereal day, 86164.1 s** (23h56m04s). Phase locked to the CMB dipole direction.
- **SECOND harmonic (2×sidereal) — subdominant:** amplitude `5β²·c₁²`, up to `5β² = 7.6×10⁻⁶`. This is
  where the old `β²` registration actually belongs.
- **DC offset:** `4β·c₀` (a pump-on level shift, not a modulation).
- **Annual sideband:** Earth's orbital velocity (≈ 29.78 km/s, EXTERNAL) vector-adds to the CMB boost,
  modulating the amplitude at the fractional level `v_orb/v_CMB ≈ 0.080` (≈ 8%) with a one-year period.
- **Harmonic content is itself the discriminator:** a first-harmonic-dominant sidereal signal ⇒ radiation
  branch (a); a second-harmonic-only signal ⇒ static branch (b). Pre-registered before the compute
  (prereg §5), so this is not a retro-fit.

## CAVEATS (honest)

1. **The frame premise carries the entire result.** The number is `0` if the response frame is the lab
   frame (`main.tex:404-406`) and `≈ 4.9×10⁻³` if it is the CMB frame (`main.tex:420-421`). The two paper
   statements are in tension; that fork is Grant's to adjudicate, not this branch's. The corrected ORDER
   is correct *conditional on* the CMB-frame premise being the operative one.
2. **Best-case projection.** The amplitudes assume the pump/probe axis sweeps the full projection onto
   the CMB dipole (`c₁→1`). A poorly-oriented experiment (axis ∥ Earth's rotation axis) has `c₁→0` and
   sees only the annual term. Real amplitude = `4β·c₁`.
3. **Order-counting, not a full tensor transform.** This settles the leading β-ORDER and the harmonic
   structure. A complete treatment would also carry aberration (an O(β) rotation of the birefringence
   axis — same order, reinforcing (a)) and the probe-frequency Doppler (also O(β)); none change the
   verdict, all are first-order. No cancellation of the linear term occurs for generic geometry.

## RECOMMENDATION TO ORCHESTRATOR (paper NOT edited here)

Given the CMB-frame premise, `main.tex:420-432` and `provenance.md:40-43` should move the registered
sidereal amplitude from `(v/c)² ≈ 1.5×10⁻⁶` to the O(β) radiation value **≈ 4.9×10⁻³** for the flip
probability (2β ≈ 2.5×10⁻³ for the δn coefficient), re-attribute the DOMINANT signal to the
**first (fundamental) sidereal harmonic**, keep `5β² ≈ 7.6×10⁻⁶` as the labeled second-harmonic term, and
state the CMB-frame premise explicitly as the load-bearing conditional (and note the lab-frame → null
alternative). A frozen table cannot carry a number off by ~1000.
