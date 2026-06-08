# Vol 0 ↔ KB reconciliation ledger

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-07-vol0-kb-reconciliation-ledger` (off `main` @ `f1f927c8`) · **Lane:** auditor (READ-ONLY — this is the Vol 0 sync *worklist*, no Vol 0 / KB edits applied)
**Prereg:** [`2026-06-07_vol0-kb-reconciliation-prereg.md`](2026-06-07_vol0-kb-reconciliation-prereg.md)
**Source of truth:** `manuscript/ave-kb/`. Vol 0 is a downstream synthesis; where they disagree the KB wins (unless the KB leaf is itself under open adjudication → HOLD).

## Method & coverage

13 reconciler agents (one per Vol 0 chunk) + 1 supplementary (frontmatter) mapped **every load-bearing Vol 0 claim → governing KB leaf at file:line**, each non-A finding adversarially re-verified by an independent skeptic, then a completeness critic over the aggregate. **Surfaces covered:** Ch 1–4, the 8 manifest-chain backmatter/appendix `\input`s, `common/appendix_experiments.tex`, **and** (critic-recovered gap) `frontmatter/00_foreword.tex` + `00_title.tex` (compiled via `main.tex:32-33` before the manifest).

**Tally:** **502 load-bearing claims examined · 324 confirmed Class-A** (match current KB) · **42 drift findings** after adversarial verify:

| Class | Meaning | Count |
|---|---|---|
| **D** | correctness drift — Vol 0 asserts what the KB no longer says | **16** |
| **O** | open-adjudication — governing leaf unresolved → **HOLD** | **3 items** (5 sites) |
| **B** | provenance/status drift — value matches, KB reframed/renamed/rescoped | **15** |
| **M** | KB-missing / internal Vol 0 collision | **7** |
| ~~→A~~ | skeptic-downgraded (drift not real) | 3 |

**Priority for the eventual sync:** D > B > O(HOLD) > M. **Class-O rows must NOT be synced** until the named adjudication closes.

---

## Class D — correctness drift (sync targets, highest priority)

### D1 · A-034 saturation-kernel catalog count: Vol 0 says "19", KB says "26" — SYSTEMIC (5 backmatter files)
The KB leaf `common/universal-saturation-kernel-catalog.md` now titles itself **"The 26-instance catalog"** (`:15`, `:30`, `:33` = 17 physical + 2 bio + 5 engineered + 2 companion, span 21 OOM). Vol 0 still says **19** as the catalog *total* in five places. ("19" is not random — it equals the **SYM-subset** count, `catalog.md:83` — which is why a careless reader misses the drift.)

| Vol 0 site | claim | KB |
|---|---|---|
| `backmatter/02_full_derivation_chain.tex:14,:178` | "19 manifestations of the SAME mechanism" / "19 cross-scale … spanning 21 OOM" | catalog.md:9,15,33 → 26 |
| `backmatter/03_geometric_inevitability.tex:530,:536` | "full 19-instance catalog" / "19 distinct phenomena" | catalog.md:30,33,140 → 26 |
| `backmatter/04_physics_engine_architecture.tex:20-21` | "all 19 catalog instances of A-034" | catalog.md:9,140,83 → 26 (was tagged B; **corrected to D** on verify) |
| `backmatter/07_universal_saturation_kernel.tex:29,:120-124` | "19 canonical instances" **and** "16 SYM, 2 ASYM-N, 1 ASYM-E" | catalog.md:15,26,83-86 → 26 total; symmetry split also stale (SYM≠16) |
| `backmatter/12_mathematical_closure.tex:79,:174,:176` | "19 cross-scale instances" / "19-instance catalog" / engine "across all 19" | catalog.md:30,33,140 + counterpart mathematical-closure.md:153,157 → 26 |

*(foreword:177 carries the same "19-instance" total but is graded B — see B4 — because the foreword reverses no physics, the count simply grew.)*
**Sync:** bump every "19" → 26 (and the per-symmetry split) against `catalog.md` as the single source. One coordinated edit; touches 5 backmatter files + the foreword.

### D2 · τ_yield Bingham form (ch2) — KB explicitly *dropped* it
`vol_0/chapters/02_analytical_summaries.tex:14` carries `τ_yield = (ħc/ℓ_node⁴)(1/α²) ≈ 7.21×10³⁴ Pa` ("Bingham-Plastic Limit"). The KB twin `common/appendices-overview.md:66` gives canonical `τ_yield = e²V_total/(8πε₀ℓ_node⁴) ≈ 1.04×10²² Pa`, and `:68-75` is an explicit **DROPPED-CLAIM** note (2026-04-20 audit): *"no derivation; Planck-scale dimensional estimate; stated value off by 10^6.4 from the stated formula. Do not re-add without a derivation."* Vol 0's own line self-computes to ~3×10²⁸, not 7.21×10³⁴ — internally inconsistent. **Corroborated in-repo:** `backmatter/01_appendices.tex:78-83` already carries it commented-out as "numerically inconsistent with itself," canonical `1.04e22` live at `:71`.
**Sync:** replace ch2:14 with `1.04×10²² Pa` (e²V_total/8πε₀ℓ⁴), or drop the bullet — matching the 2026-04-20 KB decision.

### D3 · z=3 "K4 lattice is 3-connected" (bm02) — contradicts canonical z=4 Axiom 1
`backmatter/02_full_derivation_chain.tex:510` "The K4 lattice is 3-connected." Canonical **Axiom 1** (`common_equations/eq_axiom_1.tex:20`, on main) = **"4-fold K4 nearest-neighbor connectivity at each node."** Critic-confirmed against the axiom. *(The Δc_crit=3 threshold this feeds at `:511` is separately **HOLD** — see O1.)*
**Sync:** "3-connected" → "4-fold (z=4)"; leave `:511` Δc_crit pending O1.

### D4 · Confinement force value — Vol 0 0.999 GeV/fm vs KB chain 1.002 GeV/fm (+ a KB-internal split)
`backmatter/02_full_derivation_chain.tex:670-671,:1077` = `F_conf = 3(m_p/m_e)α⁻¹T_EM ≈ 160,037 N ≈ 0.999 GeV/fm`. Counterpart `common/full-derivation-chain.md:880,:568-571` is internally self-consistent at **1.002 GeV/fm (160,584 N)**. **Note a KB-internal split the sync must resolve first:** the ch2 twin `common/appendices-overview.md:89` *also* carries 0.999/160,037 (so Vol 0 ch2:28 reads Class-A against *its* twin), while `full-derivation-chain.md` carries 1.002/160,584. Vol 0 mirrors both. **This is a KB-side inconsistency** (appendices-overview vs full-derivation-chain) that Vol 0 inherits — fix the KB split, then sync Vol 0 to the resolved value.

### D5 · Stale experiment/prediction status in `appendix_experiments.tex` + `title`
The appendix lists several tests as live/flagship that the KB has retired or superseded (governing leaf `common/appendix-experiments.md`):

| Vol 0 site | stale claim | KB current state | verify |
|---|---|---|---|
| `appendix_experiments.tex:28` | C11 Mach-Zehnder "**35-radian** topological phase shift" | canonical **~250 rad / 249.64**; "35 rad inherited a factor-7-low driver bug, corrected 2026-05-17" (appendix-experiments.md:17; divergence-test-substrate-map.md:233-236) | ✓ real — **correct twin is foreword:114** |
| `appendix_experiments.tex:17` | Sagnac Ψ_W/Al≈7.15 "**flagship Kill Switch #3**" | "Sagnac-RLVE **RETIRED to corroborative-null** (2026-06-03); Ψ=7.15 is NOT a forward AVE-vs-GR discriminator" (appendix-experiments.md:37) | ✓ — **correct twin is foreword:137** |
| `title.tex:31` | abstract advertises "**High-Voltage Active Sagnac Interferometry**" as a live flagship tabletop test | same retirement (appendix-experiments.md:37) | ✓ — also un-propagated in Vol 4 `falsification/ch12-.../active-sagnac-impedance-drag.md` + `index.md:19,22,32,44` (**cross-volume stale-live**) |
| `appendix_experiments.tex:34` | "[Axiom 1] VLBI Gravitational Impedance Parallax" listed live, no retraction | KB counterpart state differs (appendix-experiments.md:24; divergence-test-substrate-map.md:467) | ✓ real |
| `appendix_experiments.tex:46` | "[Axiom 3] Sagnac-Parallax (Galactic Wind Vectoring)" live falsification | superseded (appendix-experiments.md:45) | ✓ real |
| `appendix_experiments.tex:17 (Kill-Switch #3 header), :47 (GEO-sync impedance differential)` | listed live | appendix-experiments.md:37,46 | reconciler-flagged D; skeptic verdict pending (re-verify on sync) |

**Sync:** propagate the 2026-06-03 Sagnac retirement + the factor-7 Mach-Zehnder fix into appendix:17,28 and title:31; reconcile the 3-way internal Sagnac contradiction (appendix:17 flagship / foreword:137 retired / title:31 live) to the foreword/KB "retired-corroborative-null" framing. **Note "[Axiom 3]" label** in :41,:46 also needs the Axiom-3→"Minimum Reflection" rename (see B2).

---

## Class O — open adjudication (HOLD — do NOT sync until the named call closes)

### O1 · Δc_crit = 3 chiral-screening threshold — `backmatter/02_full_derivation_chain.tex:511`
The screening "3" that the (Class-D) "3-connected" feeds is **Grant's open neutrino-3 call** (bond-channel z=4 vs 3-Cosserat-sector selection-rule). Governing: `research/2026-06-07_neutrino-3-regrounding-check.md` (merged, walk-back **surfaced-not-executed**). **HOLD** the threshold value until Grant adjudicates Δc_crit; the connectivity *number* (D3) is independently fixable.

### O2 · BH event-horizon Γ=−1 vs canonical Γ=0 — `backmatter/07:72`, `foreword:80↔:145`
`bm07:72` "R_S formation: Γ=−1" on a BH SYM row; `foreword:80` "BH event horizon = Γ=−1 saturation surface" vs `foreword:145` "Γ=0, Z=Z_0 everywhere for EM (per electron-bh-isomorphism.md)." This mirrors a **live KB-internal tension**: `boundary-observables-m-q-j.md:47` treats the BH horizon *as* Γ=−1 (no sector qualifier); `universal-saturation-kernel-catalog.md:53` sector-splits (Γ=−1 shear/GW, Γ=0 EM); `electron-bh-isomorphism.md:24` says Γ=0 for EM. Flagged un-fixed in doc-reconciles Finding 5; **load-bearing for the LIGO-echo falsification.** *(The workflow skeptic downgraded bm07:72 to B; the critic correctly re-tags it O per the prereg's own BH-Γ rule — recorded as O.)* **HOLD** pending the Γ-sector adjudication.

### O3 · Crystalline vs amorphous substrate identity — `ch3`, `foreword:9/:30`, `title:14`, `bm02:354,:788`
Canonical Axiom 1 (`eq_axiom_1.tex:20`) = **"chiral Laves K4 Cosserat *crystal* … crystallized substrate … 4-fold connectivity."** Yet the **amorphous** framing appears across Vol 0: `title:14` "Discrete **Amorphous** Condensate M_A"; `foreword:30` "3D **amorphous** central-force network, z_0≈51.25" — *directly alongside* `foreword:9`'s crystalline "long-range I4_132 chiral order"; `ch3` generates the substrate as an amorphous Poisson-disk/Delaunay net (see M6). **Each framing matches a canonical leaf in its own context** (crystal = Axiom 1; amorphous z_0=51.25 = FTG-EMT percolation engine, `claim-quality-closure-roadmap.md:32`) — so the *values* are fine, but the **crystal-vs-amorphous identity of M_A is unadjudicated** and asserted both ways inside the foreword itself. **Canon-level Grant call** (not a mechanical Vol 0 fix). **HOLD.**

---

## Class B — provenance / status drift (value OK, framing stale)

| # | Vol 0 site | drift | governing KB | sync |
|---|---|---|---|---|
| B1 | `bm02:918,:1181,:1206` | "SRS/K4 lattice" legacy naming | Axiom 1 names it "Laves K4" (`eq_axiom_1.tex:20`); chain-leaf still uses SRS (`full-derivation-chain.md:775,950,974`) | **Nuanced:** the SRS→Laves rename is **UNEXECUTED on main** — leaves still carrying SRS are A; only the Axiom-1-context mismatch is B. Defer to the corpus-wide SRS rename. |
| B2 | `bm04:153` + `appendix_experiments.tex:41,:46` | G / tests attributed to "**Axiom 3**" (old name) | 2026-04-27 homologation renamed Axiom 3 → **"Minimum Reflection"** (`eq_axiom_3.tex`; settled, 7+ leaves) | rename "Axiom 3" label everywhere it appears in Vol 0. |
| B3 | `ch2:13` (collides `:22`,`:30`) | `ν_vac = αcℓ_node ≈ 8.45e-7 m²/s` (viscosity) reuses the symbol `ν_vac` ≡ 2/7 (Poisson) | `bm02:728-731` **already uses the disambiguated `ν_kin`** for the same 8.45e-7 quantity | **rename ch2:13 → `ν_kin`** (actionable internal rename, not just a flag). |
| B4 | `foreword:177` | A-034 "19-instance enumeration" | `catalog.md:15,33` → 26 | same as D1 but B here (count grew, no physics reversed). |
| B5 | `title:27` | proton ratio "≈**1836.14** m_e" | AVE-canonical eigenvalue **1836.12** (`self-consistent-mass-oscillator.md:61`); CODATA 1836.153 | orphan value (matches neither); align to 1836.12. |
| B6 | `bm07:107` | DC-biased piezoelectric "bench-measurable at ~30 kV bias", bare V_DC/V_yield | KB leaf now carries an added caveat (`catalog.md:72`) | add the KB caveat. |
| B7 | `bm12:44,:49,:87` | gravity bullet titled "(Axioms 1 & 4)", no orbital/Sagnac scope | `mathematical-closure.md:52,58,95` additively rescoped (+ASTROPHYSICS, +baryon-phase-shear row, +orbital) | widen scope to match. |
| B8 | `ch1:7,:9` | spin-½ challenge frames rotational DOF as "elastic medium … SO(3)" | resolution matches (`spin-half-paradox.md:12`) but KB carries an added committed scope at `:10,:14` | add the scope note. |
| B9 | `bm03:159-161` | V_halo row commits derivation column "Skew-line integral of Borromean link"; value 2.0 | value settled (`dual-reactance-storage-taxonomy.md:13`); derivation-column framing is the drift | (watch-item per critic: confirm V_halo ≡ dual-reactance count → would be A; else B.) |
| B10 | `bm03:66` | cites `pi-topological-horizon.md:15-23` for the −√2/2 phrase | phrase actually lives at `vol6/period-2/boron/structure-isotope-stability.md:27` | repoint the citation. |
| B11 | `bm02:546` | CP-phase "K4 bond chirality share (π/3)" attribution | neutrino-3 re-grounding (sector vs bond); `full-derivation-chain.md:458` | re-attribute per neutrino-3 (number preserved). |
| B12 | `ch2:38-40,:42` | H_∞/R_H/a_genesis under chapter title "**Exact** Analytical Derivations" | KB scopes these as **consistency-identities / Class E**, not independent predictions (`mathematical-closure.md:168`; `claim-quality-closure-roadmap.md:41`) | soften "Exact" framing (shared with the KB twin). |
| B13 | `appendix_experiments.tex:60` | turbulence/water-condensation phase transitions, standalone | KB rescoped into A-034 cross-scale instances (`appendix-experiments.md:55`) | note the A-034 rescope. |
| B14 | `appendix_experiments.tex:41` | "[Axiom 3] Solid-State Active Phase Induction" | mechanism matches (`appendix-experiments.md:37`); status/bench-identity reframed | (reconciler said D; skeptic corrected to B — KB doesn't contradict the literal mechanism.) |
| B15 | `ch1`/`ch4` Cauchy framing | — | — | see M7 (promoted to a collision). |

---

## Class M — KB-missing / internal Vol 0 collision (needs grounding before trust)

| # | Vol 0 site | issue |
|---|---|---|
| M1 | `bm04:97-99` | Tier-2b tree asserts `mechanics/impedance.py` + `hardware/` (7 modules) as `src/ave/` subpackages — **absent from AVE-Core src/**. No governing KB leaf. |
| M2 | `bm04:78,:113,:232` | `regime_2_nonlinear/protein_fold.py` + `protein_bond_constants` documented as engine modules — **absent from AVE-Core**. **Critic correction:** governing leaves DO exist, in `vol5/molecular-foundations/organic-circuitry/` (not `solver-toolchain.md`). ⚠️ **These rows sit adjacent to the live AVE-Protein impedance-folding walk-back (README/B4 row STALE, Core walk-back STAGED)** — confirm none inherit it before trusting (cross-repo). |
| M3 | `bm05:302` vs `:439` vs `:480` | internal identity collision: "trefoil at 637 MeV is **not** the electron" (:302) vs "Trefoil c=3 (**electron**)" (:439) vs "0_1 unknot = electron" (:480). KB `solver-toolchain.md:286/372/397` — disambiguate. |
| M4 | `bm06:158-161` | "No constants are hardcoded in the .lib file" — **no KB leaf supports this**; counterpart `appendix-spice-verification.md` is silent. |
| M5 | `bm07:25,:254,:259` vs `:29,:120` | internal collision: prose says "**six** known canonical manifestations / all six rows" while the catalog section says "**19**". (KB total is 26 — see D1.) Vol 0 contradicts itself **six vs 19**. |
| M6 | `ch3:9,:11,:22,:24,:32` | substrate generated as **amorphous** Poisson-disk random + Delaunay net vs canonical **crystalline** z=4 Laves K4 (`eq_axiom_1.tex:20`). Overlaps O3 (the canon-level identity is the Grant call; the *engine-description* mismatch is the M surface). |
| M7 | `ch4:22` & `ch3:15` (+5/3) vs `ch3:22` (−4/3) | **NEW (critic GAP-3e):** "standard Cauchy elastic solid" given as `K=5/3 G` (ch4:22, ch3:15) but `K=−4/3 G` at ch3:22. −4/3 is the longitudinal-modulus-vanishing implosion spinodal, **mislabeled** as the Cauchy value. Confirm against the DCVE/micropolar KB leaf; likely internal collision. |

---

## Skeptic-downgraded to A (drift NOT real — audit trail)

- `appendix_experiments.tex:24` (×2 findings) — reconciler claimed "no 2026-05-15 A-034 doc" / "no CMB-axis prereg." **False premise:** a non-recursive `ls research/` missed the docs in `research/_archive/L3_electron_soliton/` (and the 2026-05-19 CMB-axis prereg exists). → **A.**
- `bm03:505-508` — "SRS minimal unit cell." On main the SRS→Laves rename is **unexecuted**, and the governing geometric-inevitability leaf still uses SRS → Vol 0 is consistent with it. → **A** (not yet drift; folds into B1's deferred rename).

---

## Cross-cutting findings (only visible reading frontmatter against chapters — from the completeness critic)

1. **Sagnac status is 3-way inconsistent inside Vol 0:** flagship-kill-switch (`appendix:17`) / retired-corroborative-null (`foreword:137`) / live-tabletop (`title:31`). Foreword is correct. (→ D5)
2. **Mach-Zehnder phase is 2-way inside Vol 0:** 35 rad (`appendix:28`, stale) vs ~250 rad (`foreword:114`, correct). (→ D5)
3. **ν_vac symbol is already disambiguated as ν_kin in bm02** but reused for viscosity in ch2:13. (→ B3)
4. **τ_yield Bingham already retired in-repo** at `backmatter/01_appendices.tex:78-83`. (→ D2)
5. **Crystalline/amorphous duality is asserted within the foreword itself** (:9 vs :30) and in the title — canon-level. (→ O3)
6. **KB-internal tension flagged, not Vol-0 drift:** g_* "measurable via LISA" (`divergence-test-substrate-map.md:245`) vs "NOT a separately measurable observable" (`vol3/claim-quality.md:458`); and the confinement 0.999 vs 1.002 GeV/fm split (D4). These are **KB-side** fixes the sync depends on.

---

## Coverage note (honest scope bounds)

- **Examined & in-scope:** Ch 1–4, the 8 manifest backmatter/appendix inputs, `common/appendix_experiments.tex`, `frontmatter/00_foreword.tex`, `00_title.tex`.
- **Correctly out of scope:** `backmatter/01_appendices*.tex`, `appendix_c_derived_numerology.tex`, `appendix_vacuum_engineering.tex` — NOT `\input` by the Vol 0 manifest or `main.tex` (used as corroboration only).
- **10 of 42 findings lack an explicit skeptic verdict** (the verify-agent StructuredOutput flakiness that crashed the first run); their reconciler evidence is grep-grounded and, for the systemic items (A-034 19→26, SRS, Sagnac), corroborated across sibling findings. Flagged for a one-pass re-verify at sync time.

---

## Sync worklist (for a SEPARATE adjudicated session — nothing applied here)

**Do first (KB-side, the sync depends on them):** resolve D4 confinement split (appendices-overview 0.999 vs full-derivation-chain 1.002) and the g_* measurability tension; both are KB-internal.

**Then Vol 0 Class-D (mechanical, KB is unambiguous):** D1 (19→26, 5 files + foreword) · D2 (τ_yield → 1.04e22) · D3 (3-connected → z=4) · D5 (Sagnac retirement + Mach-Zehnder 250 + Axiom-3 label, across appendix+title+Vol4-leaves).

**Then Class-B** (renames/rescopes: B2 Axiom-3, B3 ν_kin, B4 count, B5 1836.12, B10 citation, …).

**HOLD (Class-O) until adjudicated:** O1 Δc_crit (Grant/neutrino-3) · O2 BH-Γ (LIGO-echo-load-bearing) · O3 crystalline-vs-amorphous (canon-level Grant call).

**Ground before trusting (Class-M):** M2 protein modules (check impedance-folding walk-back inheritance, cross-repo) · M1/M4 module/SPICE claims · M3/M5/M7 internal collisions.

## Discipline & verifier status

Skills: `ave-sweep-audit` (spine), `ave-prereg`, `ave-audit` (pre-spawn grounding), `verify-before-cite` (every row grep/Read-verified + skeptic-checked), `ave-evidence-framing-discipline` (age≠stale; "19=SYM-subset" precision), `flag-don't-fix` + `ave-walk-back` (read-only — worklist, no propagation), `self-isolate-worktree`. No Vol 0 or KB file was edited. This ledger + the figure-staleness plan are the only artifacts.

