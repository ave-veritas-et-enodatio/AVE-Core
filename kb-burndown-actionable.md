# AVE KB Burndown — Actionable Items Only

**Total actionable: 2 items** (0 CRITICAL, 2 MAJOR, 0 MINOR, 0 TRIVIAL).

---

## MAJOR — Address before manuscript submission

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-1** | `einstein-field-equation.md` (~line 42) contradicts the canonical engine module `src/ave/gravity/gw_propagation.py` on Z and Γ at the BH event horizon. **Engine** (authoritative per project rule #10): Z(r) = Z₀ invariant **everywhere**; Γ = 0 **everywhere**; "There are NO black hole echoes. The event horizon is a refractive singularity (n → ∞, c_local → 0), not an impedance boundary" (gw_propagation.py docstring lines 17–29; `gravitational_impedance()` lines 134–159; `horizon_reflection()` lines 162–170). **Leaf**: "both μ_eff and ε_eff collapse to zero, the local impedance drops to zero (Z → 0), and Γ = -1 (total confinement) ... catastrophic impedance boundary." The "Z → 0, Γ = -1" pattern is the **electron** confinement mechanism (asymmetric magnetic-branch saturation, master-equation.md line 74), not the BH mechanism. The leaf is misattributing the electron mechanism to the BH event horizon, contradicting both (a) the engine's explicit Schwarzschild Z(r) computation and (b) the framework's own BH/electron isomorphism distinction (Master Prediction Table #45; cross-cutting boundaries Symmetric vs Asymmetric Saturation entry). The GW leaves (`invariant-gravitational-impedance.md`, `gw-propagation-lossless.md`) are correct and consistent with the engine. | `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` (~line 42); engine canonical: `src/ave/gravity/gw_propagation.py` | vol3-gravity domain expert (correct the leaf to match the engine, or — if the leaf is intentional — surface a documented divergence and update the engine) |
| **KB-12** | `radioactive-decay-impedance.md` reports tritium decay as ~11.3 MeV; empirical β-endpoint is 18.6 keV (~600× smaller). Either framework figure means something different from measured Q_β (and should say so) or substantive numerical error. | `vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` | vol6 framework author or nuclear-domain reviewer |

---

## Future work (captured at point of need; not in active burndown)

- **KB-9 recomputation** — `ybco-phased-array.md` and `autoresonant-breakdown/theory.md` carry INVALIDATED notices at top; the YBCO 2.5-tons/m² and PLL Schwinger-bypass numerical claims need recomputation against canonical V_yield = 43.65 kV. Notices are the future-work pointer; deferred per "shore up the core" scope discipline.

---

## Out of this scope (tracked elsewhere)

These are part of the broader plan but outside the AVE-Core repo:

- All `.claude/agents/*.md` edits (KB-touching agents + MAD-side agents) — separate repo
- Boundaries Mode codification in `kb-content-distiller.md` — separate repo
- Plan-doc updates in `mad-review/` — separate repo

---

## Counts

| Tier | Count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 2 |
| MINOR | 0 |
| TRIVIAL | 0 |
| **Total actionable** | **2** |
