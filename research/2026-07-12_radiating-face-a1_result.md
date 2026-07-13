# A1 radiating face — RESULT

**Date:** 2026-07-12 · **Branch:** `analysis/radiating-face-a1`  
**Prereg (FROZEN by push):** `research/2026-07-12_radiating-face-a1_prereg_FROZEN.md` (`318ae0dc`)  
**Driver:** `src/scripts/vol_1_foundations/radiating_face_a1.py`  
**Carrier:** `NativeCageIMEX` (Rule-14 / GX5 Newmark port)  
**Class:** boundary instrumentation. **No chord. No merge until Grant says.**

α-CLEAN. PASS ≠ EMERGENCE / genesis. A2 Machian stub **out of scope**.

---

## Frozen-bin verdict

| bin | outcome |
|---|---|
| **(i) FACE-PASSIVE-MATCHED** | **LANDED** (full + fast suites) — selected via the **FROZEN lossless-limit** closed-box leg (`A=2e-4`, `1e-6`); see Deviation ledger R1 |

| gate | result |
|---|---|
| **Closed-box (FROZEN lossless-limit leg — bin-selecting)** | **PASS** — `A=2e-4`, `rel_drift_end = −5.98×10⁻¹⁰` < frozen **1e-6** (N=16) |
| Closed-box (operating-amplitude canary leg — diagnostic) | PASS — `A=0.02`, `rel_drift_end = −5.85×10⁻⁶` < landed **1e-3** (`native_cage_imex.py:561` CANARY_DRIFT) |
| Open-port passivity | PASS — `Hmax/H0 = 1.0` (≤ 1+ε_inj) |
| \(\mathcal{R}=H_{\rm end}/H_0\) | PASS — \(\mathcal{R}≈8×10^{-6}\) (full) / \(3×10^{-4}\) (fast) ≪ \(10^{-2}\) |
| Sabotage | TRIPS — `plant_fired = primary_multiply`, `Hmax/H0 = 172.06` (primary sponge-MULTIPLY injects directly; fallback injector not needed) |
| Rule 10 | Interior / shell masks on carrier |
| ClaimClass | face = `C_consistency`; refuse `D_emergence` |

---

## Numbers (full suite, `fast=False`)

| quantity | value |
|---|---:|
| `rel_drift_end` (closed — **FROZEN lossless-limit**, `A=2e-4`) | **−5.98×10⁻¹⁰** (< 1e-6) |
| `rel_drift_end` (closed — canary diagnostic, `A=0.02`) | −5.85×10⁻⁶ (< 1e-3) |
| `R` = H_end/H0 (open) | 8.21×10⁻⁶ |
| `Hmax/H0` (open) | 1.0 |
| `A_face_max` | 0.011 (sub-yield; linear leg) |
| `Γ_port` analytic mean on shell | ≈1.5×10⁻⁵ ≈ 0 |
| sabotage `Hmax/H0` (`plant_fired = primary_multiply`) | ~172 |

**Honesty — ΣV² residual:** after the port kills wave energy, interior `ΣV²` can retain a soft DC offset (`E_int_end/E_int_0 ~ 0.1`). Prereg \(\mathcal{R}\) is **wave** energy via `total_energy` H (kinetic + native stiffness), not raw ΣV². Documented; not used to fake PASS.

---

## Deviation ledger (dated; frozen prereg byte-untouched)

**2026-07-12 (post-adversarial-review) — closed-box criterion (R1).** The frozen
prereg ("Closed-box control") names the lossless-limit criterion
`|ΔH/H| < 1e-6` and forbids a looser number. The **original ship** ran the
closed-box control at the *operating* amplitude `A=0.02` and enforced only the
landed `1e-3` canary (`native_cage_imex.py:561` CANARY_DRIFT) — i.e. it enforced
the canary at operating amplitude, **not** the frozen lossless-limit criterion.
This deviation was **undisclosed at ship time**; it is now receipted. Because the
closed-box drift scales cleanly as `A²`, the true lossless limit `A=2e-4` gives
`rel_drift_end = −5.98×10⁻¹⁰ ≪ 1e-6` (measured; N=16). REPAIR (this commit): the
driver now runs a **FROZEN lossless-limit leg** (`run_closed_box_lossless_limit`,
`A=2e-4`, enforces `1e-6`) that **selects the bin**, and keeps the `A=0.02` run as
a labeled **operating-amplitude canary** diagnostic leg (`run_closed_box_canary`,
`1e-3`). **Bin (i) stands via the new frozen-criterion leg.** KEEP-BOTH: the
canary receipt is retained alongside.

**2026-07-12 (post-adversarial-review) — sabotage plant transparency (R3).** The
original `run_sabotage_multiply` silently fell back to a guaranteed-injection
plant, making `trips=False` unreachable. REPAIR (this commit): the report now
records **which** plant fired (`primary_multiply` vs `fallback_injector`), the
primary plant reports its own honest `trips` flag, and the gate is
`at least one NAMED plant trips`. On this carrier the legacy sponge-MULTIPLY
injects directly (`plant_fired = primary_multiply`, `Hmax/H0 = 172.06`); the
fallback injector is **not** exercised (`fallback_ratio = NaN`).

---

## What this does / does not claim

**Does:** local solid model can radiate into the NativeCageIMEX energy-consistent face without injection; reflection residual below frozen floor; sabotage gate live.

**Does not:** live Machian / \(\Omega_{\rm freeze}\) universe stub (A2); equate PML with cosmic \(\Gamma=-1\); R10 / node-mint / melt; merge authority.

---

## Next

A2 charter only after Grant accepts (i) and wants the slow projection stub. **No PR merge** until Grant trusts the trail.
