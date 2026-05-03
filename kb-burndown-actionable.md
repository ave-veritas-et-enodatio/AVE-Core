# AVE KB Burndown — Actionable Items Only

**Total actionable: 3 items** (0 CRITICAL, 2 MAJOR, 1 MINOR, 0 TRIVIAL).

---

## MAJOR — Address before manuscript submission

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-9** | vol4 leaves use two different yield voltages for the same effective-permittivity saturation threshold in load-bearing numerical predictions. `metric-levitation-limit.md` (line 22) uses V_yield = 43.65 kV as the rupture threshold ("59.1 kV > 43.65 kV → spatial vacuum undergoes absolute impedance rupture"). `ybco-phased-array.md` (lines 6, 12, 18) uses 60 kV as the saturation limit and claims 59 kV is "safely below" it — the 2.49 g per-node lift force and "2.5 tons / m²" panel claim depend on this. `autoresonant-breakdown/theory.md` (line 24) puts 60 kV in the C_eff(V) detuning formula: `C_eff(V) = C_0·√(1 − (V/60k)²)`. Per Axiom 2, V_yield = √α·m_e c²/e ≈ 43.65 kV is canonical. The 60 kV figure originates from the tokamak D-T ion-collision strain (V_topo ≈ 60.3 kV) — a specific scenario-dependent strain — incorrectly imported into general yield-threshold contexts. **Two load-bearing numerical predictions (YBCO levitation force, PLL Schwinger bypass) are computed against the wrong yield voltage.** Either the 60 kV usage is correct and `metric-levitation-limit.md` (and Axiom 2's V_yield) need reconciliation, or the YBCO/PLL leaves need recomputation against 43.65 kV. | `vol4/simulation/ch15-autoresonant-breakdown/theory.md`, `vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md`, `metric-levitation-limit.md` | vol4-engineering domain expert (numerical reconciliation) |
| **KB-12** | `radioactive-decay-impedance.md` reports tritium decay as ~11.3 MeV; empirical β-endpoint is 18.6 keV (~600× smaller). Either framework figure means something different from measured Q_β (and should say so) or substantive numerical error. | `vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` | vol6 framework author or nuclear-domain reviewer |

---

## MINOR — Address before public release

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-1** | Z=Z₀ vs Z→0 horizon impedance interpretive tension between leaves: `einstein-field-equation.md` says Z → 0 at r_s; `invariant-gravitational-impedance.md` and `gw-propagation-lossless.md` say Z = Z₀ invariant under symmetric gravity. Both reconcilable but no in-leaf reconciling note. | `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` (~line 42), `vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md`, `gw-propagation-lossless.md` | kb-content-distiller or vol3-gravity domain expert |

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
| MINOR | 1 |
| TRIVIAL | 0 |
| **Total actionable** | **3** |
