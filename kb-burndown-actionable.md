# AVE KB Burndown — Actionable Items Only

**Total actionable: 3 items** (0 CRITICAL, 1 MAJOR, 2 MINOR, 0 TRIVIAL).

---

## MAJOR — Address before manuscript submission

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-12** | `radioactive-decay-impedance.md` reports tritium decay as ~11.3 MeV; empirical β-endpoint is 18.6 keV (~600× smaller). Either framework figure means something different from measured Q_β (and should say so) or substantive numerical error. | `vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` | vol6 framework author or nuclear-domain reviewer |

---

## MINOR — Address before public release

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-1** | Z=Z₀ vs Z→0 horizon impedance interpretive tension between leaves: `einstein-field-equation.md` says Z → 0 at r_s; `invariant-gravitational-impedance.md` and `gw-propagation-lossless.md` say Z = Z₀ invariant under symmetric gravity. Both reconcilable but no in-leaf reconciling note. | `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` (~line 42), `vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md`, `gw-propagation-lossless.md` | kb-content-distiller or vol3-gravity domain expert |
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
| MAJOR | 1 |
| MINOR | 2 |
| TRIVIAL | 0 |
| **Total actionable** | **3** |
