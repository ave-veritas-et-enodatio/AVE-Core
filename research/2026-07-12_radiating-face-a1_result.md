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
| **(i) FACE-PASSIVE-MATCHED** | **LANDED** (full + fast suites) |

| gate | result |
|---|---|
| Closed-box | PASS — `rel_drift_end ≈ −6e-6` (N=16) |
| Open-port passivity | PASS — `Hmax/H0 = 1.0` (≤ 1+ε_inj) |
| \(\mathcal{R}=H_{\rm end}/H_0\) | PASS — \(\mathcal{R}≈8×10^{-6}\) (full) / \(3×10^{-4}\) (fast) ≪ \(10^{-2}\) |
| Sabotage | TRIPS — multiply/injector `Hmax/H0 ≫ 1` |
| Rule 10 | Interior / shell masks on carrier |
| ClaimClass | face = `C_consistency`; refuse `D_emergence` |

---

## Numbers (full suite, `fast=False`)

| quantity | value |
|---|---:|
| `rel_drift_end` (closed) | −5.85×10⁻⁶ |
| `R` = H_end/H0 (open) | 8.21×10⁻⁶ |
| `Hmax/H0` (open) | 1.0 |
| `A_face_max` | 0.011 (sub-yield; linear leg) |
| `Γ_port` analytic mean on shell | ≈1.5×10⁻⁵ ≈ 0 |
| sabotage `Hmax/H0` | ~172 |

**Honesty — ΣV² residual:** after the port kills wave energy, interior `ΣV²` can retain a soft DC offset (`E_int_end/E_int_0 ~ 0.1`). Prereg \(\mathcal{R}\) is **wave** energy via `total_energy` H (kinetic + native stiffness), not raw ΣV². Documented; not used to fake PASS.

---

## What this does / does not claim

**Does:** local solid model can radiate into the NativeCageIMEX energy-consistent face without injection; reflection residual below frozen floor; sabotage gate live.

**Does not:** live Machian / \(\Omega_{\rm freeze}\) universe stub (A2); equate PML with cosmic \(\Gamma=-1\); R10 / node-mint / melt; merge authority.

---

## Next

A2 charter only after Grant accepts (i) and wants the slow projection stub. **No PR merge** until Grant trusts the trail.
