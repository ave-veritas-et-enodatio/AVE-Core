# CORRECTION NOTE — `_reflection_density` Γ² coefficient 1/64 → 1/16

> **Dated 2026-07-14. Quarter-power Family-E hygiene burn-down (Item 1).**
> Surfaced by the implementer (HYGIENE) lane for the **auditor lane**. This note
> FLAGS banked quantities that consumed the legacy coefficient; it does **NOT**
> retro-edit any merged result (forward-only disclosure per flag-don't-fix). The
> auditor lane owns any downstream matrix / KB relabel.

## The fix

`src/ave/topological/cosserat_field_3d.py` `_reflection_density` (:441-495 post-fix):
the Γ² reflection-power coefficient was corrected from **1/64 → 1/16**.

**Derivation (from the function's own chain).** The function is a continuum
Op3 reflection density `Γ² ~ (½ ∇ln Z)²`:

- **Legacy (removed):** `Z = Z₀·S^(−1/4)` ⇒ `∇ln Z = −(1/4)∇S/S` ⇒
  `Γ = ½∇ln Z = −(1/8)∇S/S` ⇒ `Γ² = (1/64)|∇S|²/S²`.
- **Canonical (Op14-forced):** `Z = Z₀·S^(−1/2) = Z₀/√S` ⇒ `∇ln Z = −(1/2)∇S/S`
  ⇒ `Γ = −(1/4)∇S/S` ⇒ `Γ² = (1/16)|∇S|²/S²`.

The `S^(1/4)` branch is `(1−A²)^(1/8)` — an eighth-power in A² matching no
physical register (map §Kernel-conventions). The `√S` register is the one
op14 forces via the clock (`ω_local = (1−2α)^{1/4}`; an `S^{1/4}` impedance
would give the contradicted `(1−2α)^{1/8} = 0.998164`). See
`research/2026-07-14_quarter-power-map.md` §2/§3.

**In-file corroboration (the fix removes a same-file inconsistency):** the two
sibling functions in `cosserat_field_3d.py` already carried `√S` —
`_s11_density` (:425, `Z_eff = 1/√S`) and `_reflection_density_asymmetric`
(:574-579, `Z = Z₀√(S_μ/S_ε)` ⇒ `Γ = (1/4)[…]` ⇒ `Γ² = (1/16)|…|²`, coded as
`0.25 * (…)` at :627). Only the symmetric `_reflection_density` still rode the
legacy S^(1/4). The fix makes all three register-consistent.

**Effect: a UNIFORM 4× rescale** of the reflection density at every site
(`1/16 = 4 × 1/64`). Empirically confirmed on the electron (2,3) ansatz
(R=6, r=2, 24³): total reflection energy `Λ_refl` = **2.239998e5 (legacy 1/64)
→ 8.959991e5 (fixed 1/16), ratio = 4.000000**; the engine output now matches
the fixed value exactly. No qualitative property changes (vanishes-in-vacuum,
positivity, grows-near-yield ratio are all rescale-invariant).

## Consumer audit — banked quantities that consumed the coefficient

Live consumers of the symmetric `_reflection_density`: Cosserat self-energy
`_energy_density_bare`/`_energy_density_saturated` (:706, :745, scaled by the
default `k_refl = 1.0`); the LEGACY `_coupling_energy_total`
(`k4_cosserat_coupling.py:122`, regression-only — the default Phase-4 coupled
engine uses `_coupling_energy_total_asymmetric`, already 1/16-register); and the
driver `charge_sector_two_winding.py` (default `k_refl = 1.0`, reflection term
in the `−∂W/∂ω` force path).

| Banked doc (do NOT retro-edit) | Quantity consumed | Coefficient-sensitivity | Verdict impact |
|---|---|---|---|
| `research/_archive/L3_electron_soliton/33_phase3b_x3_energy_analysis.md` (:91, :288, :315) | `Λ_refl` energy-budget integral (banked `8.90e5 / 7.68e5 / 6.94e5`), labeled `← (1/64)\|∇S\|²/S²` | **YES** — scales 4× | Verdict is NEGATIVE ("Λ_refl ~250000× too large / dominates / Λ decomposition ≠ α⁻¹"). A 4× increase makes Λ_refl *larger* ⇒ verdict **strengthened, not moved**. |
| `research/2026-06-23_charge-sector-two-winding_result.md` (:133-135, :258-261) | "Arm A (like) == Arm C (achiral)" force-blind-to-charge equality | **NO** — a uniform rescale of a charge-blind (symmetric) force preserves the equality exactly | Verdict **not moved**. |
| `research/2026-07-14_qed-trace-beta-gate_RESULT.md` (:178, :339) | `a_init` centroid-drift trajectory (`+0.029, −0.116, −0.167, −0.118, −0.054`) via the reflection-term force | **PARTIAL** — the specific `a_init` values are coefficient-dependent (driver runs default `k_refl=1.0`); the reflection contribution to `−∂W/∂ω` quadruples | Verdict ("non-monotone, R²=0.15 **uninformative**, dispersion-dominated, force-blind-to-charge") is structural to a charge-blind symmetric drive and **not moved**. **AUDITOR FLAG:** if `a_init` is ever promoted from "uninformative," the specific values must be recomputed under the 1/16 coefficient. |
| `research/2026-07-08_electron-lock-barrier_result.md` (:94) | — (explicitly `wall_form="omega_front"`, BC-not-bulk) | N/A — does NOT consume the bulk `_reflection_density` | Unaffected. |

## ⚑ FLAG-DON'T-FIX — numerical anomaly for the auditor (unresolved here)

The archived `33_phase3b` banked `Λ_refl = 8.90e5` (smallest R/r config) and its
markdown labels the formula `← (1/64)|∇S|²/S²`. But a genuine **1/64**
computation on a comparable (2,3) ansatz gives **2.24e5**, whereas the
**corrected 1/16** computation gives **8.96e5** — i.e. the archived banked value
matches the *corrected* coefficient to <1%, not the value its own `(1/64)` label
implies. This suggests the doc's `(1/64)` prose-label may not reflect the
coefficient actually in the code at that doc's compute-time, OR reflects a
different S-normalization. This repo's git history cannot order the authorship
(the `1/64` line and the `33_` doc were both migrated from `analysis/integration`
on 2026-05-21). **Surfaced, not resolved** — the auditor lane should adjudicate
whether `33_`'s banked `Λ_refl` was actually computed on a 1/16-equivalent
coefficient (in which case the `(1/64)` label was the stale one all along, and
this fix simply re-aligns code to what `33_` already measured).

## Regression pin

`src/tests/test_cosserat_field_3d.py::test_reflection_density_coefficient_pinned_to_one_sixteenth`
pins the coefficient to its derivation (reconstructs `Z^(−1/2) → Γ → Γ²` and the
internal `|∇S|²/S²` chain; asserts `1/16`, explicitly rejects `1/64`).
