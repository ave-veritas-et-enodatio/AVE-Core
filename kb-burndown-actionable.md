# AVE KB Burndown — Actionable Items Only

**Total actionable: 5 items** (0 CRITICAL, 2 MAJOR, 3 MINOR, 0 TRIVIAL).

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
| TRIVIAL | 0 |
| **Total actionable** | **5** |
