# Pump Inventory — Astrophysical — RESULT: [PUMP-SAFE]

**Date:** 2026-07-08 · **Branch:** `analysis/pump-inventory` · **Base:** `5219a0b0`
**Prereg (FROZEN, precedes this run):** `research/2026-07-08_pump-inventory-astrophysical_prereg_FROZEN.md`
**Driver:** `src/scripts/vol_9_device/pump_inventory_astrophysical.py` · **JSON:** `.../_output/pump_inventory_astrophysical.json`
**Nature:** the FINAL make-or-break gate for the P6 sidereal Lorentz-violation flagship (paper-hardening ledger, P6).
*(Result doc reconstructed by the orchestrator from the operative JSON after the implementer hit a transient API-500 mid-write-up; every number below is verbatim from the driver output, verified.)*

## VERDICT — **[PUMP-SAFE]**

No astrophysical environment pumps the AVE nonlinear vacuum birefringence to an observable level. The flagship
sidereal Lorentz violation (~4.9×10⁻³) is not constrained by any existing astrophysical observation, and the
CMB-birefringence numerical coincidence is **SPURIOUS**. The flagship closes clean.

## The question

The AVE birefringence is nonlinear (needs a pump: c_bir ∝ (field/E_yield)²) and survives existing *linear* LV bounds
because those don't reach a field-dependent effect. The remaining threat: astrophysical photons cross strong ambient
fields — a magnetar is pumped *harder* than the lab (A² ~ 7×10⁻⁴ vs the lab pump's 6×10⁻⁷). Does any environment fire
the nonlinearity where an existing observation would catch it?

## FORK-1 static-B transparency — HOLDS, computed (not assumed)

The driver **computes** the discrete curl of the field (it does not hardcode A_I=0):
- uniform static B (10¹¹ T magnetar): `A_I = 0.0` exactly ⇒ `S_B = 1` ⇒ `δn_μ = 0`.
- realistic magnetar *dipole* geometry: `A_I = 2.86×10⁻¹⁴` (an O(h²) discretization residual; curl B = 0 analytically for a static field).
- **POSITIVE CONTROL (informative-null proof):** a field with genuine circulation, B ∝ (−y, x, 0), fires `A_I = 4.94` — the curl operator returns nonzero *when circulation is present*, so the static-B zero is a real discrimination, not a rigged one. `positive_control_fires = True`, `fork1_holds = True`.
- **Honest counterfactual:** had the µ-grade been *magnitude*-keyed (B/B_snap)² instead of circulation-keyed, a magnetar would be A² ≈ 2.8×10³ (super-yield → vacuum rupture) — i.e. magnitude-keying *would* kill the flagship. Circulation-keying (FORK-1) is exactly what saves it. The escape is a real, load-bearing physics fact, not a convenience.

## Environment table (all astrophysical values tagged EXTERNAL)

| Env | Field | Kind | AVE-active A² | Outcome |
|---|---|---|---|---|
| E1 magnetar surface B | 10¹⁰–10¹¹ T | static-B | **0** | transparent (FORK-1) |
| E2 ordinary pulsar B | 10⁸ T | static-B | **0** | transparent (FORK-1) |
| E3 galactic B | ~µG | static-B | **0** | transparent (FORK-1) |
| E4 intergalactic B | ~nG | static-B | **0** | transparent (FORK-1) |
| E5a polar-cap gap E (unscreened) | ~10¹⁵ V/m | static-E | 7.8×10⁻⁵ | pair-screened, thin gap, off clean path → negligible integrated observable |
| E5b polar-cap gap E (screened) | ~10¹⁰ V/m | static-E | 7.8×10⁻¹⁵ | negligible |
| E6 ISM/IGM E | ~0 (quasi-neutral) | static-E | **0** | Debye-screened → no ε pump on any long baseline |
| E7 magnetar thermal X-ray | — | radiation | 1.9×10⁻¹² | far below lab pump |
| E8 magnetar giant-flare peak | — | radiation | 0.235 | **numerically strongest — but radial outflow ⇒ probe co-propagates ⇒ (1−cosθ)⁴ collision factor → 0** |
| E9 accreting NS / ULX | — | radiation | 2.3×10⁻⁶ | collinear + no clean birefringence bound |
| E10 GRB prompt emission | — | radiation | 2.3×10⁻⁸ | **strongest CLEAN-path pump — still below the lab pump (6×10⁻⁷)** |
| E11 CMB radiation bath | — | radiation | 3.7×10⁻³⁷ | utterly negligible |
| E12 interstellar radiation field | — | radiation | 8.8×10⁻³⁷ | negligible |

Two independent reasons nothing bites: **static fields are transparent** (FORK-1, circulation-keying), and **every
clean-geometry radiation pump is below the lab pump** (`clean_path_radiation_all_below_lab = True`); the only
numerically-strong radiation pump (E8) is geometrically dead (collinear outflow → zero collision angle).

## IXPE magnetar consistency

`δn_QED (static-B) = 0.0397`, `δn_AVE (static-B, FORK-1) = 0.0` ⇒ **AVE adds nothing to the static-B magnetar
birefringence**; the residual IXPE observes *is* the ordinary QED Euler–Heisenberg value. `AVE_overshoots_IXPE = False`.
AVE is consistent with the IXPE 4U 0142+61 detection — it simply does not contribute in the static-B channel.

## CMB coincidence — SPURIOUS

`cmb_path_pumps = False` (E4/E6/E11 all ≈ 0): cosmological baselines are field-free / static / transparent, so the AVE
nonlinear effect produces **no** cosmological rotation. The AVE sidereal 4β = 4.94×10⁻³ vs the detected cosmic
birefringence 5.2×10⁻³ rad (EXTERNAL) is a **dimensional coincidence** (fractional pump-induced modulation vs
cosmological rotation angle), not a physical connection. `cmb_coincidence = "SPURIOUS"`.

## What this closes

The P6 flagship sidereal Lorentz violation survives the full three-part make-or-break:
1. **Bounds** — un-parametrized by the SME (structurally invisible to linear/transverse coefficients).
2. **Sector** — a nonlinear transverse-T2 effect, A1-mass frame-anchored; shielded from linear bounds by its *nonlinearity*.
3. **Pump** — [PUMP-SAFE]: no astrophysical pump fires it; FORK-1 makes ambient static fields transparent.

The chord is real and testable, and no current observation constrains it.

## Honest caveats

- The verdict rests on FORK-1 (µ keys on circulation, not flux) — reconfirmed here at magnetar field with a live positive control, but it is the load-bearing assumption; if the µ-grade were ever shown magnitude-keyed, magnetars would kill the flagship (counterfactual A² ≈ 2.8×10³).
- E8 (giant-flare) is defeated by geometry (collinear outflow), not by weakness — a hypothetical transverse pump-probe crossing at a magnetar surface would be a different story, but no such clean observational configuration exists.
- Astrophysical field values and the CMB-birefringence datum are EXTERNAL inputs, tagged as such; the AVE responses are OUR compute from canonical constants.
- A dedicated *nonlinear/higher-dimension* photon-sector LV experiment could still, in principle, bound the effect (it is transverse, hence in-principle bounded) — "unconstrained" here means *by existing observations*, not *unfalsifiable*.
