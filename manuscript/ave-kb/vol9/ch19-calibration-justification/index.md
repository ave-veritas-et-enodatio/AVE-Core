[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.19 Calibration Parameter Justification

Chapter 19 of the Vol 9 datasheet is the volume's single **consolidated reference / calibration-conditions** section. The substrate's calibration provenance — which numbers are genuine inputs, which are derived, and (for each input) what is forced-FORM versus imported-VALUE — is otherwise **scattered** across the per-chapter scope/provenance tables (Ch.2 `tab:vol9_absmax_scope`, Ch.4 `tab:vol9_dc_scope`, Ch.5 `tab:vol9_ac_scope`, Ch.10 `tab:vol9_magnetic_scope`) and the Ch.12 / Ch.14 / Ch.15 cosmological-anchor + chord-vs-echo material. This chapter pulls all of it into **one master calibration-parameter table** classifying every calibration-relevant parameter by (i) **role** — genuine-input / definitional-anchor / SI-primitive / derived / cosmological-initial-data; (ii) the CI-gated **chord / echo / mixed** axis (`real_or_fitted`, INVARIANT-S13); (iii) provenance / FORM-vs-VALUE justification; and (iv) the up-link to the canonical Vol 1–6 derivation leaf. It does **not** move or duplicate the per-chapter scope tables (each serves its local chapter); it is the cross-cutting consolidation that references them.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitive is introduced. Every per-constant verdict it tabulates is **already settled** in an existing canonical leaf: the FORM-deriving / VALUE-importing organizing principle and the per-constant accounting live at [`common/form-deriving-value-importing.md`](../../common/form-deriving-value-importing.md); the machine-enforced per-mechanism classification lives in the CI-gated [`common/interlock-register.md`](../../common/interlock-register.md) (`real_or_fitted` axis, `expected-independent-count: 3`); the chord / echo / mixed **definitions** are `def-ch0rd1` / `def-ech0v1` / `def-fmv001` in [`common/vocabulary-register.md`](../../common/vocabulary-register.md). This chapter is a **datasheet-format consolidation home** that points up at those, exactly as Vol 9 chapters point up to their canonical derivations (INVARIANT-S7: no primary derivation in Vol 9).

The chapter also states the **"zero free parameters" claim precisely**: the framework reduces ~26 Standard-Model empirical inputs to **3 genuine calibration inputs `{m_e, α, G}` + the 4 axioms**, with the live independent-parameter count machine-pinned at **3** in the interlock register; the further reduction to a single cosmological initial-datum (`Ω_freeze` / the magic-angle operating point `u_0*`) is an *aspirational* collapse that holds only if the independent `𝒥_cosmic` route confirms the back-fit `u_0*` (else it is a two-parameter `(α, G)` fit). The one named currently-fitted residual beyond the 3 — the CMB thermal scalar `δ_strain` (a definitional residual, magnitude not yet derivable) — is tracked at [`common/full-derivation-chain.md`](../../common/full-derivation-chain.md) Layer 8.

## Primary canonical sources

| Source | Content |
|---|---|
| [`common/form-deriving-value-importing.md`](../../common/form-deriving-value-importing.md) | The organizing-principle umbrella + per-constant accounting (α echo, G mixed, K=2G GR-imported, E_yield mixed, m_e definitional); the testing consequence (FORM-EXISTENCE / FORCED-RATIO chord classes) |
| [`common/interlock-register.md`](../../common/interlock-register.md) `ilk-rr14gt`, `ilk-gravmb`, `ilk-cmptrp` | CI-gated `real_or_fitted` chord/echo/mixed classification (INVARIANT-S13); `calibration-params: {m_e, α, G}`; `expected-independent-count: 3` recomputed by `make verify-kb-metadata` |
| [`common/vocabulary-register.md`](../../common/vocabulary-register.md) `def-ch0rd1` / `def-ech0v1` / `def-fmv001` | Canonical chord / echo / mixed definitions |
| [`vol1/ch8-alpha-golden-torus.md`](../../vol1/ch8-alpha-golden-torus.md):11,13 | α honest-scope + scoped-echo register (closed-form `4π³+π²+π` FORM; `R·r=1/4` value the substrate does not independently select; all 3 named lift-routes closed-negative) |
| [`common/q-g47-substrate-scale-cosserat-closure.md`](../../common/q-g47-substrate-scale-cosserat-closure.md):28 | `K = 2G` (`ν_vac = 2/7`) GR trace-reversal identity — GR-imported value (PR #261 merged) |
| [`common/full-derivation-chain.md`](../../common/full-derivation-chain.md) Layer 8, `clm-9oazz0` | "From Three Limits to Zero Parameters"; the honest 26→`{m_e, α, G}`+4-axiom reduction; `δ_strain` definitional residual; `G = ℏc/(7ξ m_e²)` Machian termination |
| [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) `clm-dsb560` | Single cosmological initial-datum `Ω_freeze` → `u_0*`; three-route (α, G, 𝒥_cosmic) falsification commitment |
| [`claim-quality-closure-roadmap.md`](../../claim-quality-closure-roadmap.md) §4.1 | Magic-angle-provenance walk-back: `u_0* ≈ 0.187` asserted / back-fit, not forward-derived; three-route re-scope (α, G fix; 𝒥_cosmic tests) |
| [`common/divergence-test-substrate-map.md`](../../common/divergence-test-substrate-map.md) | FORM-EXISTENCE vs FORCED-RATIO chord-class lens (which predictions are AVE-distinguishable from SM/GR/ΛCDM) |
| Per-chapter Vol 9 scope tables — Ch.2 `tab:vol9_absmax_scope`, Ch.4 `tab:vol9_dc_scope`, Ch.5 `tab:vol9_ac_scope`, Ch.10 `tab:vol9_magnetic_scope`; Ch.12 `tab:vol9_cosmo_spec`; Ch.15 `tab:vol9_forward_prediction_register` | The scattered Scope / Provenance / Bench-access + chord-vs-echo content this chapter consolidates (left in place; referenced, not moved) |
| `manuscript/common_equations/eq_calibration_constants.tex`, `eq_gravity_derived.tex`; `src/ave/core/constants.py` symbols `M_E`, `L_NODE`, `ALPHA`/`ALPHA_COLD_INV`, `G`, `XI_MACHIAN`, `XI_TOPO`, `T_EM`, `Z_0`, `V_YIELD`, `DELTA_STRAIN` | Canonical symbols, formulae, and numerical values (per `ave-canonical-source`; no hard-coded values in the chapter) |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/19_calibration_parameter_justification.tex` (Vol 9 canonical chapter file; populated at this PR landing).

---
