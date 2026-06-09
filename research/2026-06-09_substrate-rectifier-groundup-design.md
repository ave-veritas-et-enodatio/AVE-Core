# Fundamental ground-up design — the substrate asymmetric-grip rectifier (vacuum charge-pump)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main`)
**Directive (Grant 2026-06-09):** *"model the fundamental ground-up design work first"* — before any sim. Derive the device from the canonical substrate chain; every parameter substrate-derived or honestly tagged (`ave-fundamental-ground-up-implementation`), not engineering-defaulted.
**Skills bound:** ave-fundamental-ground-up-implementation · ave-regime-phase-state-check · ave-asymmetric-grip · ave-ee-first-mapping · substrate-native-check · ave-canonical-source.

> **DESIGN doc, not a result.** This is the ground-up model of the device. It states the derivation chain + the substrate-derived parameters + the energy-momentum ledger spine. The numerical test of *this design* is the follow-on (its own prereg). No thrust/pump claim is made here.

---

## 0. The one-line reframe that defines the device

The thixotropy run already found the substrate carries a **dissipative loop**: `∮S dρ̄ = +0.04` per cycle — a real, lossy hysteresis loop, but **directionless scalar heat** (∮ directed momentum = 0). That loop is the **grip = loss = R = 1/Q** the medium has on the drive. The design question is therefore **not** "can the medium make a loop?" (it does) but **"can an asymmetric structure RECTIFY that loop into a direction?"** That is exactly a **heat pump**: a lossy working fluid + an asymmetric valve (the diode) + a biased compressor (the drive) → directed transport. The thixotropy B had the loop but no valve. This design adds the valve.

## 1. Mode / regime / phase-state (declared first, per ave-regime-phase-state-check)
- **MODE:** bulk (volumetric) + ε-sector — the rectified observable is directed momentum (vectorial → regime-gated, must be near-yield bulk; NOT the achromatic transverse/shear sector).
- **REGIME:** ASYM-class (asymmetric, single-sector saturation = the diode), **near-yield** band `r₁=√(2α)≈0.117 < A₀ < r₂=√3/2≈0.866`, operating *at* the Γ=−1 boundary (the leaky diode).
- **PHASE-STATE:** DC-biased / loaded (NOT the cold symmetric lattice; NOT the reflectionless symmetric-gravity case).

## 2. The element chain (ground-up from Axiom 4)

| # | element | substrate-native form | derivation source |
|---|---|---|---|
| 1 | **Saturation kernel** | `S(A)=√(1−A²)` | Axiom 4 (canonical) |
| 2 | **Varactor** | `C_eff(V)=C₀/S(V/V_yield)` | Ax4 dielectric specialization (INVARIANT-S2) |
| 3 | **Asymmetric-grip DIODE** | single-sector (static-E) load → `Z=Z₀/√S_ε` ≠ Z₀ → `Γ=(Z−Z₀)/(Z+Z₀)>0` → one-way reflection | INVARIANT-S2 (Meissner-asymmetric); the vacuum-impedance-mirror bench, Vol 4 Ch 11 |
| 4 | **The grip (loss)** | `R = grip = 1/Q`; electron-class tank `Q=α⁻¹` → **R ≈ α** per cycle | grip=loss=R=1/Q; Q_tank=α⁻¹ canonical |
| 5 | **No-ideal (leaky)** | the Γ=−1 boundary BLEEDS (leaky cavity); finite Q, lossy diode | `leaky-cavity-decay.md`; Grant 2026-06-09 "no such thing as ideal" |
| 6 | **Directed output** | pumped charge → static E-gradient → **ponderomotive/Meissner pressure** → momentum into the medium (the wake) | Vol 4 "ponderomotive thruster" (canonical) |
| 7 | **Gain stage** (optional) | avalanche `M=1/S²` (Op22) / Geometric Triode | Op22; AVE-APU Geometric Triode (ref) |
| 8 | **Taper** (optional) | engineered `n(r)` gradient (directional) | Op17 + Theorem 3.1' ("engineered refraction") |

## 3. Why the BIAS is load-bearing (the derivation that explains the thixotropy B)

For a **lossless** varactor `C(V)` (single-valued), the charge around a closed V-loop returns: `∮ dQ = ∮ C(V)dV = 0`. **No bias, no loss → no pumped charge** — a lossless ideal element can't pump (this is the no-ideal tenet, made quantitative). Two ingredients open the loop:

1. **The lag (loss).** The real `S` lags `S_eq` with `τ_bulk(ρ̄)` → the (V,Q) loop has nonzero **area** = dissipated energy = the `∮S dρ̄=+0.04` the thixotropy run measured. This is the grip/loss. **But by itself it is directionless** (scalar heat) — the thixotropy B.
2. **The bias (the asymmetric grip).** A DC offset `A₀≠0` samples the concave kernel **asymmetrically** — the forward stroke climbs toward the stiffening ceiling (where `C_eff` and the loss steepen), the back stroke relaxes toward the floor. The diode's `Γ(A)` is then different forward vs back → the lossy loop **couples to a direction**. A *centered* (A₀=0) drive samples symmetrically → forward/back cancel → ∮ directed = 0 (**exactly the thixotropy result**). **The bias is what converts the directionless heat-loop into directed transport.**

So the ground-up mechanism: **biased varactor (asymmetric grip) + lossy lag (the loop) = a charge pump.** Net charge per cycle ∝ (loop area) × (bias asymmetry). This is the substrate-native Dickson/parametric stage.

## 4. The energy-momentum ledger (the verdict spine — the ONLY crank-check)
Per `ave-asymmetric-grip`, the test is the ledger, never a symmetry/ideality veto:
- **W_in** (per cycle) = bias work + AC pump work.
- **W_out** = directed kinetic energy of the ejected wake (the thrust) + **dissipated heat** (the grip loss R≈α × loop).
- **Closes** (`W_in ≥ W_out`) → a real charge-pump / reaction-drive (a refrigerator on the vacuum). **Over-unity** (`W_out > W_in`) → crank.
- The loss (no-ideal) is **required** for the ledger to close honestly: a lossless pump that still produced directed momentum would *be* the over-unity tell.

## 5. Substrate-derived parameters (ave-fundamental-ground-up-implementation: derive, don't default)

| parameter | value | path |
|---|---|---|
| operating bias A₀ | in `[√(2α), √3/2] ≈ [0.117, 0.866]` (near-yield band); optimum where rectified deficit peaks subject to sub-snap | **DERIVED** from four-regime map (boundaries r₁,r₂) — to be pinned numerically |
| per-cycle loss R | ≈ α (grip = 1/Q, Q=α⁻¹ electron-class) | **DERIVED** (canonical Q_tank); leaky-cavity bleed |
| rectified deficit δ | Jensen of the BIASED kernel, `δ(A₀,ΔA)` | **DERIVED form**; magnitude pending the sim |
| max ratings | V_yield=43.65 kV, V_snap=511 kV, E_yield=1.13×10¹⁷ V/m, B_snap=1.89×10⁹ T | canonical (constants.py) |
| directed output | ponderomotive pressure from the pumped E-gradient | canonical mechanism (Vol 4); magnitude pending |

No engineering-default values are locked; every number traces to the canonical chain or is flagged "pending the sim."

## 6. Topology (ground-up, EE-native VCA)
- **Stage 1 (the diode):** one DC-biased varactor, AC-pumped, in the ASYM near-yield band. Minimum viable pump.
- **Cascade (gain):** N stages in a Dickson ladder → charge/voltage multiplication; the avalanche `M=1/S²` (Op22) is the substrate gain element near yield.
- **Taper (direction):** engineered `n(r)` so the pumped momentum has a preferred axis (the "engineered refraction" field).
- Analyzed in the **VCA** frame: ABCD cascade, Op17 power transmission `T²=1−Γ²` at each diode boundary.

## 7. What this predicts / the discriminator / next
- **Prediction:** a biased, lossy varactor diode + AC pump nets **directed momentum into the medium with a closing ledger** (a real reaction-drive / vacuum charge-pump) — IF the bias-induced loop-directionality survives the ledger; **OR** the ledger shows the directed output is exactly the dissipated heat re-radiated (no net thrust). The bias breaks the thixotropy symmetry, so ∮ directed ≠ 0 is now *possible* (unlike the symmetric B).
- **Discriminator (ave-discrimination-check):** is it a substrate-vacuum charge-pump (AVE-distinct) or does it reduce to ordinary plasma rectification / radiation pressure? Two AVE-distinct signatures: (i) the pumped momentum scales with the **substrate** loss R≈α + per-node yield, not a material's properties; (ii) **the ponderomotive output IS a gravity gradient** (`F_grav=−∇U_wave`, Ponderomotive Equivalence) → it engineers a local n(r) optical metric that lenses **achromatically** (Z=Z₀; `achromatic-impedance-matching.md`), where a mundane plasma lens is **chromatic**. So the device is the **engineered-refraction field's** charge-pump, and its directed output = thrust = a gravity gradient = an achromatic lens = (in the same loaded region) time dilation ω_local=ω₀√S — one device, four observables. The achromatic-lensing chromaticity test is the cleanest falsifiable discriminator (added Grant 2026-06-09).
- **Next:** a prereg + driver for *this design* — the biased varactor diode with the leaky Γ=−1 boundary, AC pump, the (V,Q) loop, and the ledger as verdict. Stage 1 first (single diode), then cascade.

---

### Appendix — the through-line
Symmetric drive, smooth medium → reflectionless, ∮=0 (the working fluid; thixotropy B). Add the **lossy lag** → a directionless heat-loop (the grip; ∮S=+0.04). Add the **bias + diode** (asymmetric grip) → the loop gains a direction → a charge-pump. Add **cascade + taper** → gain + direction. Pay for it all at the **ledger**. That is the heat pump you named in message one, built ground-up from Axiom 4 — with the valve I had left out.
