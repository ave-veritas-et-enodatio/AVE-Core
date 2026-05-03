# AVE KB Burndown — Actionable Items Only

**Total actionable: 13 items** (0 CRITICAL, 2 MAJOR, 3 MINOR, 8 TRIVIAL).

---

## MAJOR — Address before manuscript submission

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-7** | vol4 index Key Results / Domains tables cite "PONDER-05 469 µN predicted thrust" with link to `vol4/hardware-programs/index.md` — directory doesn't exist; PONDER-05 / 469 µN appear nowhere in vol4 leaves. Actual leaves give PONDER-01 with 40.1 µN. Either author missing leaves or normalize index numbering. | `vol4/index.md` (lines 12, 23) | kb-taxonomy-architect + kb-content-distiller |
| **KB-12** | `radioactive-decay-impedance.md` reports tritium decay as ~11.3 MeV; empirical β-endpoint is 18.6 keV (~600× smaller). Either framework figure means something different from measured Q_β (and should say so) or substantive numerical error. | `vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` | vol6 framework author or nuclear-domain reviewer |

---

## MINOR — Address before public release

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-1** | Z=Z₀ vs Z→0 horizon impedance interpretive tension between leaves: `einstein-field-equation.md` says Z → 0 at r_s; `invariant-gravitational-impedance.md` and `gw-propagation-lossless.md` say Z = Z₀ invariant under symmetric gravity. Both reconcilable but no in-leaf reconciling note. | `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` (~line 42), `vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md`, `gw-propagation-lossless.md` | kb-content-distiller or vol3-gravity domain expert |
| **KB-5** | vol5 index references `vol5/protein-folding-engine/` subtree (Chs. 3–5: Z_topo, 8-tier architecture, 2D TL solver, 20-protein PDB validation, S₁₁ objective, Kramers folding time). Directory unauthored in this repo (engine lives in private `AVE-Protein` repo). Multiple broken Key Results links; confirmed broken cross-link in `consciousness-cavity-eigenmode.md` line 53. | `vol5/index.md`, `vol5/biological-applications/consciousness-cavity-eigenmode.md` | kb-taxonomy-architect (replicate vs amend decision) + kb-content-distiller |
| **KB-9** | vol4 leaves switch between V_yield (43.65 kV) and "60 kV" without flagging. The 60 kV figure is the D-T tokamak ion-collision strain (V_topo ≈ 60.3 kV), not a third axiomatic yield threshold. Used as if equivalent in YBCO-array and autoresonant-PLL leaves. | `vol4/simulation/ch15-autoresonant-breakdown/theory.md`, `vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md`, `metric-levitation-limit.md` | kb-content-distiller or vol4-engineering domain expert |

---

## TRIVIAL — Polish; address opportunistically

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-2** | Hubble Key Results row in `vol3/index.md` shows H_∞ ≈ 69.32 km/s/Mpc with no qualifier. Boundaries cover; index headline still misleads direct readers. Add asterisk/footnote referencing `lattice-genesis-hubble-tension.md`'s consistency-proof framing. | `vol3/index.md` line 14 | kb-content-distiller |
| **KB-3** | Hubble value 69.32 (LIVING_REFERENCE, entry-point.md) vs 69.33 (`lattice-genesis-hubble-tension.md` table) — last-digit inconsistency. Pick one; reconcile. | `LIVING_REFERENCE.md` row #23, `entry-point.md`, `lattice-genesis-hubble-tension.md` | kb-content-distiller |
| **KB-4** | `common/index.md` Key Results: "8 derivation layers → genuinely zero free parameters" lacks the conditional qualifier (one currently-fitted δ_strain scalar). Boundaries cover; index headline still over-broad. | `common/index.md` | kb-content-distiller |
| **KB-6** | vol5 η_eq packing-fraction formula and S₁₁ folding-functional definition have no derivation leaf in this repo (functional-definition leaves are in private `AVE-Protein`). Either replicate sanitized leaves or accept honest invariant-doc provenance. | vol5 sidecar references | kb-content-distiller |
| **KB-8** | `optical-caustic-resolution/index.md` Key Results: "E_max = E_YIELD = √α·m_ec²/e ≈ 43.65 kV/m" — formula evaluates to 43.65 **kV** (voltage), not kV/m (field). Macroscopic field equivalent: ~1.13×10¹⁷ V/m. Units glitch only; substantive bound is correct. | `vol4/advanced-applications/ch20-optical-caustic-resolution/index.md` (~line 14) | kb-content-distiller |
| **KB-10** | vol6 `mass-defect-summary.md` and index Key Results show 0.00001%–0.02739% errors without the fit-vs-prediction qualifier present in `semiconductor-nuclear-analysis.md` (per-nucleus geometric fit). Boundaries cover; summary still misleads. | `vol6/framework/mass-defect-summary.md`, `vol6/index.md` | kb-content-distiller |
| **KB-11** | vol6 heavy-element catalog "<0.5% across 105 elements" headline — typical-case figure. `full-element-table.md` shows worst case Cl-35 at 1.465%, several others above 0.5%. Boundaries tier the accuracy; headline still clean. | `vol6/appendix/heavy-element-catalog/index.md`, `vol6/index.md` | kb-content-distiller |
| **KB-13** | vol6 ABCD transfer-matrix open-problem caveat (gates Z ≥ 15 catalog results) not surfaced from `full-element-table.md` or `appendix/heavy-element-catalog/index.md`. Add cross-link from heavy-element catalog to `abcd-transfer-matrix.md`. | `vol6/appendix/heavy-element-catalog/index.md`, `full-element-table.md` | kb-content-distiller |

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
| MINOR | 3 |
| TRIVIAL | 8 |
| **Total actionable** | **13** |
