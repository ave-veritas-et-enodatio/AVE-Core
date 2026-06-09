# Vacuum z=4 Diamond — Coordination/Chirality Walk-Back (orchestration brief)

**Status:** **Tier C EXECUTED** (9 gate-independent edits, this branch, 2026-06-08; KB verify PASS, scripts compile, `Z_COORDINATION` resolves). **Gates A (θ₁₃) + B (axiom-naming) HELD pending two Grant calls.**
**Branch:** `analysis/2026-06-08-vacuum-z4-coordination-walkback` (off `origin/main` @ `3088232d`, PR #141).
**Worktree:** `/Users/grantlindblom/AVE-staging/AVE-Core-z4walkback-wt` (isolated; self-isolate discipline — the shared checkout is on a coworker branch 120 behind origin/main).
**Skills applied:** `ave-walk-back` (Type D + Step 3h-exhaustive), `ave-prereg`, `ave-handoff-canonical-locale`, `verify-before-cite`, `ave-canonical-source`, `ave-discipline-translate` (W2 c_EM/c_shear), `ave-evidence-framing-discipline`.

---

## 0. Pre-registration

**What I expect / why / what discriminates.** The 2026-06-07 lattice-net resolution-of-record ([`2026-06-07_lattice-net-resolution.md`](2026-06-07_lattice-net-resolution.md)) settled that the vacuum substrate is a **z=4 (degree-4) achiral diamond net (Fd-3m)**, chirality being an *excited* Cosserat order-parameter (`k_χ`), not a cold-lattice property. The engine computes z=4 (`k4_tlm.py`, `cosserat_field_3d.py`); the legacy "chiral Laves K4 / chiral srs / 3-connected / coordination z=3" framing is the numerological outlier. The resolution's walk-back queue was **adjudicated but never executed** — re-verified against fresh `origin/main` (`3088232d`): `eq_axiom_1.tex:20`, `delta-cp-violation.md:23`, `vol1/claim-quality.md:141` all still carry the contradicted z=3 framing (only `d018b88b`, the unrelated c_L fix, touched these files since).

**Walk-back type:** **Type D (mechanism re-scope)** — predictions unchanged, mechanism narrowed (the "3" is the 3 Cosserat microrotational sectors, not lattice bonds). **No Predictions-matrix surgery** (`divergence-test-substrate-map.md` has 0 coordination hits — verified). Numbers are preserved everywhere (δ_CP = 61/45 = 1.3556π stays exact).

**Collision check:** none — scanned all ~40 in-flight worktrees; no other branch touches the z=3/z=4 files.

---

## 1. The honest scale (ave-walk-back Class-G 5× miss-rate, confirmed)

Manual investigation found ~8 files. The exhaustive Step-3h sweep (`wf_dbddc807`, 388 agents, adversarially classified) found **1319 hits / 382 files**:

| Bucket | Hits | Files | Meaning |
|---|---|---|---|
| **FALSE_POSITIVE** | 1011 | — | atomic number Z=3 (lithium), the *correct* 3 Cosserat sectors, 3 lepton generations, knot crossing-number c=3, correct z=4 statements — **protected from over-correction** |
| **LOAD_BEARING_UNCONDITIONAL** | 53 | 41 | z-independent re-groundings (not θ₁₃-gated) |
| **GATED_ON_THETA13** | 20 | 9 | neutrino Δc_crit screening |
| **STALE_PROSE** | 101 | 53 | narrative wrapping (lower urgency, still required) |
| **FROZEN_SNAPSHOT** | 130 | — | dated `_orchestration/` handoffs, frozen preregs, `_archive/` — no change |
| **PRESERVED_HISTORICAL** | 1 | — | walk-back provenance (Rule 12) |

**Actionable = 174 sites** (53 + 20 + 101) across the manuscript (97 in `ave-kb`), engine (`src/ave` 11), datasheet (vol 9, 9), frontmatter/backmatter, and three research docs. **Separately, the bare name "chiral Laves K4" appears in 47 files** — the full naming footprint of Gate B.

> ⚠ **Coverage caveat:** the dedicated net-names finder (`parallel[3]`) failed its schema mid-run. Net-name sites were largely caught by the other five finders, but **before executing Gate B, re-grep `chiral Laves K4` / `SRS/K4` / `chiral SRS` (47/9/5 files)** to close the gap.

---

## 2. Decision structure — two Grant gates + one unconditional tier

### Gate A — θ₁₃ / Δc_crit (your call) — 20 hits / 9 files
Neutrino screening routes Δc_crit through bond-count = 3. **Plumber question (from the neutrino result doc):** is the angular-momentum-transfer bottleneck the **3 AM components** (→ Δc_crit = 3, SU(2) selection rule, θ₁₃ survives, pure re-ground) or the **4 bond channels** (→ Δc_crit = 4 on diamond, θ₁₃ unscreens and breaks ~20×, 0.022 → ~0.44, Rule-12 walk-back of θ₁₃ alone)?
Files: `chiral-screening.md` (3), `vol2/claim-quality.md` (3), `mixing_derivation.py` (3), `03_neutrino_sector.tex` (5), `ch03-neutrino-sector/index.md` (2), `06_electroweak_and_higgs.tex`, `02_full_derivation_chain.tex`, `full-derivation-chain.md`, `constants.py:609`. δ_CP, θ₁₂, θ₂₃, and the JUNO inverted-hierarchy falsifier survive **either way**.

### Gate B — axiom-naming + cold-chirality reframe (your call) — framing-level
The canonical Axiom-1 statement still names the cold substrate "**Chiral Laves K4 Cosserat Crystal**" / "I4₁32 chiral space group." The resolution says cold = **achiral Fd-3m diamond**; chirality is the *excited* `k_χ` decoration (I4₁32 = Fd-3m + chiral decoration). The edits are individually trivial, but **renaming Axiom 1 is framing-level** (INVARIANT-S2 is a "do not redefine" register) → your call, with a scope sub-decision:
- **B-rename:** change the axiom name + the ~47-file "chiral Laves K4" footprint to the diamond form. Most thorough; biggest propagation.
- **B-clarify (recommended):** fix the *self-contradiction* in the axiom statement (state "4-fold diamond Fd-3m + 3-phase Cosserat spin + excited `k_χ` chirality"), mark "Chiral Laves K4" explicitly as a **legacy alias**, and re-ground only the *load-bearing* cold-chirality assertions (e.g. `02_full_derivation_chain.tex:1217` "SRS/K4 lattice is chiral" as the baryogenesis CP source). Leaves passing legacy-alias mentions intact. Far smaller, preserves audit trail.
Canonical sites: `eq_axiom_1.tex:20`, `eq_axiom_2.tex`, `CLAUDE.md:55/56`, `LIVING_REFERENCE.md:72`, `axiom-definitions.md:16`, `full-derivation-chain.md:72`, `02_full_derivation_chain.tex:104/1217`, `open_problems.py:158`, `mathematical-closure.md`, `01_fundamental_axioms.tex`.

### Tier C — truly unconditional, execute-now (touches neither gate)
Number-preserving re-groundings + pure hygiene; safe to land on this branch immediately on your go:

| Site | Edit | Note |
|---|---|---|
| `delta-cp-violation.md:23` | "1/3 per bond *because* 3-connected" → "1/3 per Cosserat sector (SU(2))"; drop "same geometric fact" weld; keep trefoil c=3 as independent knot property | **δ_CP = 61/45 preserved exactly** (per-bond on z=4 would break it to 1.272π). **Scope-lock:** do NOT touch the θ₁₃ screening blockquotes at `:37/:46/:53` (Gate A). |
| `ch03-neutrino-sector/index.md:11` | third PMNS input "K4 lattice connectivity (3)" → "3 Cosserat microrotational sectors" | preserves δ_CP |
| `first-principles-bond-force-constants.md:110` | "each interior node is a 3-connected WYE junction" → three-phase from the 3 spatial DOF / Cosserat sectors | keeps 1/3 and 1/√3 |
| `op14-local-clock-modulation.md:37,45` | `n(r)=1+2GM/rc² ≈ 1/√S` → slope-1 clock `1/√S ≈ 1+GM/rc²`; note 1+2GM/rc² is the slope-2 bulk/Shapiro index | **separate axis** — already-adjudicated W2 (2026-06-05) Pitfall-#5 fix, not z=3 |
| `plot_emt_packing_landscape.py:21` | hard-coded `z0=51.25` → `from ave.core.constants import Z_COORDINATION` | **pure hygiene** (`ave-canonical-source`) |
| `simulate_3d_lattice.py` | add SUPERSEDED/LEGACY banner (driver wires "exactly 3 neighbors") | z=4 rebuild = separate follow-up |
| `simulate_electroweak_unification.py:15` | re-ground "coordination 3"/"chiral 3D network" docstring | `ν_vac=2/7` untouched |
| `q_g47_path_d_full_cross_validation.py:128` | additive annotation on dated Grant comment (frozen quote preserved) | additive only |
| `k4-tlm-simulator.md:73` | drop "bipartite *therefore* natively chiral" non-sequitur (diamond is achiral) | corpus already correct at `translation-circuit.md:652` |

> `vol1/claim-quality.md:141` (`clm-9s9apq` "chiral SRS net z=3" vs `clm-gx1mpl` z=4 at :1187 — same number 1.187, two net-names) is the cleanest *claim-base* self-contradiction. It is Tier C **if** label-only, but the "chiral SRS" wording overlaps Gate B; fold it with B-clarify.

---

## 3. Other easy wins surfaced (beyond the walk-back) — `wf_91e9cc46`

- **#24 gravity factor-2 fork** ([`2026-06-05_gravity-sign-frequency-modulation-result.md:136`](../research/2026-06-05_gravity-sign-frequency-modulation-result.md)): does a propagating photon ride c_shear = c₀√S (index 1/√S) or c₀·S (index 1/S)? Explicitly queued for a separate session — **genuine open fork, NOT easy.** Flag for Grant.
- **#10** "3 Cosserat sectors" undeclared dual-use (`vol1/claim-quality.md:520` {translation, rotation, curvature-twist} vs CLAUDE.md ω-components) — one definitional call.
- **#18** `born_huang_percolation.py:11` z₀≈54.5 (large-z approx) vs canonical `Z_COORDINATION`≈51.25 — reconcile label.
- **#19** `defense_context_checker.py:177` instructs authors to call the vacuum "amorphous (not a crystal)" — tension with Axiom-1 "crystal."
- **PONDER-05 mis-cite:** [`ax4-saturation-narrow-aperture-amplitude-shape.md:38`](ax4-saturation-narrow-aperture-amplitude-shape.md) still cites PONDER-05 as a vacuum-kernel falsifier "per INVARIANT-S2" — S2 now says the opposite (W6 SYMMETRIC/ASYMMETRIC). Trivial epic-doc fix.

**Confirmed clean (adversarial negatives — the filter worked):**
- Refuted claims `clm-r6uef4`, `clm-8zwyl3` have **zero inbound citations** — DAG is clean on "refuted-but-still-cited."
- `docs/glossary.md:59` cold-chirality assertion is **already self-flagged** by the same file's §1.7 — not a silent contradiction.

---

## 4. Execution plan (after Grant's two calls) — ave-walk-back Step 3 order

1. **Tier C** — ✅ **EXECUTED 2026-06-08** (this branch): the 9 number-preserving/hygiene edits above. KB metadata verify PASS (no drift — prose-only, no claim/frontmatter change, so `refresh` not needed); 4 scripts `py_compile` OK; `Z_COORDINATION` import resolves to 51.2482. δ_CP scope-lock honored (θ₁₃ blockquotes at `:35-55` untouched). Changelog entry **deferred** to the complete-walk-back merge (Tier C is on a draft branch; the closure-roadmap tracks canon/main state, nothing merged yet).
2. **After Gate A (θ₁₃):** the 20 screening sites (re-ground to sectors, or Rule-12 walk-back θ₁₃ + 🔴 header on `pmns-eigenvalues.md:40-49` + `delta-cp-violation.md:30`).
3. **After Gate B (axiom-naming):** source leaves → axiom statements (`eq_axiom_1/2.tex`, CLAUDE.md, LIVING_REFERENCE.md, axiom-definitions.md) → claim-quality entries (`clm-9s9apq`, `clm-q39qct`, `clm-9gh0a1`, `clm-zuf7g1`) → engine (`mixing_derivation.py`, `soliton_bond_solver.py`, `constants.py`, `open_problems.py`) → datasheet (vol 9 ×9) → frontmatter/backmatter → STALE_PROSE tail (53 files).
4. **Changelog (bidirectional, 3l):** `claim-quality-closure-roadmap.md` (root — **note: not `common/closure-roadmap.md`**) — forward entry + reverse SUPERSEDED-marker on the original z=3 canonization; back-pointer to the 2026-06-07 resolution.
5. **Refresh + verify + driver re-run** between tiers (`ave-walk-back` live-fire); re-grep the 47-file "chiral Laves K4" footprint before declaring Gate B complete.

---

## 5. The two open Grant calls (headline)

1. **θ₁₃ / Δc_crit:** AM-component bottleneck (3 → θ₁₃ survives) or bond-channel bottleneck (4 → θ₁₃ walks back)? Gates 20 sites.
2. **Axiom-naming scope:** **B-rename** (47-file footprint) or **B-clarify** (fix the self-contradiction + mark "Chiral Laves K4" legacy-alias + re-ground only load-bearing cold-chirality)? Recommended: **B-clarify**.

Tier C (incl. the δ_CP flagship + the op14 W2 fix + the constant-import) is ready to land independently of both.
