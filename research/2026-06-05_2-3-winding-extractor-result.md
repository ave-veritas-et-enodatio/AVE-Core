# (2,3)-Winding Extractor — Coordinate Fix + Validation (RESULT)

**Date:** 2026-06-05
**Branch:** `analysis/2026-06-05-2-3-winding-extractor` (worktree `AVE-Core-2-3-wt`)
**Prereg (FROZEN):** [`2026-06-05_2-3-winding-extractor-coordinate-prereg.md`](2026-06-05_2-3-winding-extractor-coordinate-prereg.md)
**Brief:** [`_orchestration/2026-06-05_2-3-winding-extractor.md`](../_orchestration/2026-06-05_2-3-winding-extractor.md)
**Predecessor:** [`2026-06-04_full-electron-option-B-discrete-emergence-result.md`](2026-06-04_full-electron-option-B-discrete-emergence-result.md) — auditor item **#1 (BLOCKING)**.
**New extractor:** `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py` (KEEP-BOTH: the shipped `phasor_temporal_winding` is **untouched**).

---

## §0 Headline

_(filled on run completion)_

---

## §1 The coordinate diagnosis — why the prior extractor was blind, and where the (2,3) actually lives

The prior extractor (`r10_…_2_3_emergence.py:phasor_temporal_winding`) set θ₁ = port-1 `(V_inc,V_ref)` phasor angle, θ₂ = port-2 phasor angle. Two facts collapse it (prereg §1, confirmed in code):

1. A port's `(V_inc,V_ref)` phasor angle **IS** that port's capacitive↔inductive (C↔L) angle (transmission-line identity: `(V_inc,V_ref)` is a 45° rotation of `(V, Z₀I) = (C-state, L-state)`).
2. Two ports of one bond ring at the **same LC frequency** → θ₁ and θ₂ wind at the same rate → ratio structurally ~1:1. The extractor lived in **(C↔L-phase, C↔L-phase)** and left `Phi_link` (the L-state) **unused**.

**Two deeper findings this work surfaced (load-bearing, beyond the prereg's stated diagnosis):**

**(A) The imposed (2,3) is a SPATIAL standing pattern, not a temporal one.** `initialize_2_3_voltage_ansatz` (`tlm_electron_soliton_eigenmode.py:34`) plants the winding as
`θ_wind = 2φ + 3ψ` where **φ = toroidal (major-circle) angle** and **ψ = poloidal (minor-circle) angle** on a toroidal shell, via the K4 port quadrature (`cos θ` on ports {0,1}, `sin θ` on ports {2,3}). **At any single fixed bond, φ and ψ are constants → θ_wind is a constant → a single-bond TIME series carries NO 2φ+3ψ winding** (only the temporal LC slosh). This is exactly the predecessor auditor's conjecture (`…option-B…result.md:354`: *"the imposed (2,3) may live in a coordinate neither the temporal-single-bond nor the spatial-ring extractor reads"*). The shipped `*_capture.npz` carries **only single-bond `(V_inc,V_ref,Phi_link)` time series** — structurally incapable of hosting the spatial (2,3). The validation therefore **required a full-field spatial walk** (re-running the imposed control to capture the converged field — allowed per prereg §0).

**(B) Both windings live in the internal U(1) quadrature phase; the C↔L↔fibre identification is subtle.** The "2" (φ) and "3" (ψ) both sit in the single internal phase `Θ = 2φ+3ψ` carried by the V_inc port-quadrature. The corpus projection map (`06_winding §3-4`) labels the "2" as the n̂-direction (S² base, survives Hopf) and the "3" as the U(1) fibre (lost in the Hopf projection) — and indeed on the lattice `n̂ ≈ ±t̂(φ,ψ)` (the knot tangent), so the n̂-direction azimuth carries the φ-structure. But the cleanest, most robust read of **both** windings is the chirality-corrected internal U(1) phase Θ, walked around the two circles (see §2). The **literal V_inc-vs-Phi_link C↔L fibre angle** is degenerate in the *pristine* ansatz (the imposed ansatz plants V_inc ≡ Phi_link in phase, corr = +1.000 on all ports) and only becomes non-degenerate once Phi_link develops temporal quadrature dynamically — it is reported as a **diagnostic** alongside the load-bearing Θ read.

---

## §2 The coordinate-correct extractor (what it reads)

On the converged **full field**, the new extractor reads the internal U(1) phase `Θ = 2φ+3ψ` and its winding around each torus circle:

| Axis | Quantity | Circle | Expect |
|---|---|---|---|
| **"2" (base)** | winding of Θ (≈ n̂-direction, S² base — survives Hopf, `06_winding §3`) | **major** φ | **2** |
| **"3" (fibre)** | winding of Θ (the U(1) fibre / LC-slosh phase, `06_winding §4`) | **minor** ψ | **3** |
| **`c` (invariant)** | torus-knot crossing number `min(p(q−1), q(p−1))`, **derived from the measured (w₁,w₂)** | — | **3** |

Robustness machinery (each anti-fit — see §4 discipline walk):
- **`interp_vinc`** — trilinear interpolation of V_inc port-components over the A-sublattice (defeats thin-tube A-site undersampling that aliased a naive point-walk).
- **`internal_u1_phase`** — chirality-corrected port-quadrature phase: the raw `arctan2(V·{2,3}, V·{0,1})` is distorted by the per-port chirality weights `c_p = p̂·t̂(φ,ψ)` (their ratio winds once → a −1 offset on each axis); dividing out the **known geometric** weights (amplitudes from the field) recovers Θ. **A coordinate transform, not a fit-to-(2,3).**
- **`shell_params_from_field`** — per-angular-sector density **crest** radius (median) locates R free of the radial-volume bias `dV∝ρdρ`.
- **`_modal_winding`** — the **modal** integer across 12 circles at varied φ₀/ψ₀ (anti-fit; robust to single-ring lattice aliasing).

**Validation on controls (before the real Arm-C field):**
- Clean planted ansatz (V_inc only, end-to-end from field): `w₁=2` (modal 12/12), `w₂=3` (modal 11/12), `c=3` → **is_2_3 = True**. (Legacy on the same control: `(8,0)/c=16`.)
- Negative control (random V_inc field): `w₁=3, w₂=1, c=0` → **is_2_3 = False** (discriminates present-vs-absent).

---

## §3 V0 / V1 gate outcome (the real dynamically-evolved Arm-C field)

_(filled on run completion — the new extractor's read on the converged Arm-C imposed control vs the legacy `(8,0)/c=16`, and the V1 null on Arm-B baseline)_

---

## §4 C1 — single-bond vs bond-pair (GATED on V0 pass)

_(filled on run completion if V0 passes; else SKIPPED per prereg C2)_

---

## §5 Discipline walk (which skills fired)

- **`phase-space-coordinate-check`** (THE load-bearing skill) — the entire result. Axes are **direction + fibre on the shell circles**, never **port-vs-port**. The fix is reading the spatial internal U(1) phase Θ around the major (→2) and minor (→3) circles, not the temporal phasor at one bond.
- **`ave-canonical-source`** — `ALPHA` imported from `ave.core.constants` (verified `0.0072973525693`); no literals. A²_op14 = √(2α) derived.
- **`ave-driver-script-honesty`** — V0 is a forward READ of a KNOWN-imposed signal (anti-fit gate); no optimizer is run onto (2,3). The chirality correction divides out **known geometry**, not fitted parameters; the modal-winding read tunes nothing toward a target.
- **`substrate-native-check` CP8** — the Arm-C state is the **seeded** imposed control; nothing fresh is planted by the extractor. The shell is **located from the field** (crest-finder), not hardcoded.
- **`consistency-vs-emergence`** — this is **tool-VALIDATION (consistency) + structural-ID**. NOT an emergence claim, NOT an α-derivation. The (2,3) is present-by-construction in Arm C; recovering it certifies the measurement tool.
- **`ave-evidence-framing-discipline`** — V0-fail ⇒ honest INCONCLUSIVE (no single/pair verdict on an unvalidated tool, prereg C2).
- **Flag-don't-fix / KEEP-BOTH** — the shipped `phasor_temporal_winding` is **not redefined**; the new extractor is a separate module (audit-trail continuity).

---

## §6 Artifacts

- Extractor + V0/V1/C1 driver: `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py`
- Results JSON: `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate_results.json`
- Converged full-field capture (Arm C + Arm B): `src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate_capture.npz`
