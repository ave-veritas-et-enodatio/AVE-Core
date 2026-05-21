# Round-2 Claim-Graph Triage

Drives the round-2 port (L3 `analysis/integration` → `migrate-l3-to-blr`) for claim-graph machinery only. For each leaf currently carrying a `claims:` list or inline `<!-- claim-quality: ... -->` markers that L3 has dropped, decides per-claim disposition: **stay** (keep our machinery as-is), **rehome** (move to a different leaf), **split** (one claim → multiple), **drop** (claim retired), or **needs-assessment** (decision deferred pending closer read of L3 text).

## Methodology

L3 systematically strips our claim-quality machinery (it uses a different leaf-convention: `<!-- leaf: verbatim --><!-- path-stable: X -->` rather than `kb-frontmatter` blocks with `claims:`). The machinery removal itself is convention-only — **not** a retirement signal. Default disposition is therefore **stay**: re-apply our convention on top of L3's prose updates. Exceptions are flagged with explicit evidence.

**Time heuristic** (per `2026-05-20 02:56` working principle): when a claim's text changes between L3's two snapshots, the later statement wins. Resolution evidence cited per-row.

**Clarity heuristic**: contemporaneous restatements — pick the formulation that's clearer; when L3 drops a guardrail/qualification with no explicit supersession marker, preserve our current text (silent regression loses to explicit qualification).

## Per-leaf triage

### common/appendix-experiments.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-t5ybqw` Experimental Falsification Index — Catalog Status, Not Validation Status | **stay** | L3 adds many new entries with explicit per-experiment status (CONFIRMED, RETRACTED, demoted). The catalog-status-vs-validation-status meta-framing is *more* visible in L3, not less. |

### common/full-derivation-chain.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-sxn6eo` Mathematical Closure Status — Structurally Zero-Parameter, Not Absolutely | **stay** (strengthened) | L3 walks G back to "Bounding Limit 3 + Class E joint constraint" per Grant 2026-05-19 EOD canonicalization. This *strengthens* the claim's "not absolutely zero-parameter" content. Likely rescore-up after merge. |
| `clm-ibfyda` Full Derivation Chain — Acyclicity and Identified Methodology Disclosures | **stay** | L3 silently removes the "Methodology disclosure" callout block from the lepton derivation. **Rigor regression — preserve current callout** (clarity over silent removal; the disclosure is the claim's substantive content). |

### common/omega-freeze-cosmic-grain-cascade.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-dsb560` Three-Route Framework: α, G, and J_cosmic from a Single Ω_freeze | **stay** | Class E framing addition strengthens it (joint-constraint structure now explicit). |
| `clm-a7cbqq` Ω_freeze Freeze-In at Lattice Genesis | **stay** | No substantive change. |
| `clm-pe8lpx` Eight Cosmic-Axis Observables Aligned with the Ω_freeze Axis | **stay** (refined) | New empirical CMB-axis pin `(l=60.28°, b=50.48°)` updates the citation but not the count. Rescore-up likely (Planck PR3 SMICA empirical anchor replaces literature placeholder). |
| `clm-fndptx` G-Anisotropy Angular Shape P₂(cos θ) | **stay** | Unchanged. |

**Rigor regression to NOT port**: L3 drops the "Provisional discussion — not a framework claim" guardrails around §4 nested-cascade and §6 with no explicit supersession marker. Preserve current guardrails (clarity wins).

### common/operators.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-sysqaf` Universal Operator Catalog (Op1–Op22) — Catalog of Record | **stay** | Still the canonical catalog. |
| `clm-6mvtsf` Op1 Universal Impedance — the Single Structural Invariant | **stay** | Unchanged. |
| `clm-gdd70j` Universal Operators (Z, S, Γ) — Same Function, Different Scales | **stay** | Unchanged. |

**Cross-cutting**: New §5.5 Hoop Stress motif — canonical home is `mond-hoop-stress.md` (see that leaf below). Reduce operators.md §5.5 to a one-paragraph cross-ref. **Rigor regression to NOT port**: LaTeX→unicode notation downgrade in §2 catalog (~22 rows). Keep current LaTeX.

### common/q-g47-substrate-scale-cosserat-closure.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-iouqn9` K4 Magic-Angle Condition (K=2G at u₀*≈0.187, ν_vac=2/7) | **stay** | Unchanged. |
| `clm-qwmnhn` \|T\|=12 Universality — Four Independent K4 Routes | **stay** | Unchanged. |
| `clm-bjceop` Substrate-Scale Cosserat Prefactors (ξ_K2/ξ_K1 = 12) | **stay** (strengthened) | L3 closes individual prefactors ξ_K1 = 8/3 and ξ_K2 = 32 as clean rationals (consistent with the forced ratio = 12). Rescore-up likely. |
| `clm-gr8d63` Two-Engine Convergence on p* = 8πα | **rehome** | L3 moves the two-engine convergence narrative out of q-g47 and into a cross-ref to `two-engine-architecture-a027.md`. Drop from q-g47 `claims:` and inline markers; canonical home is two-engine. |

### common/translation-tables/translation-cosmology.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-fy05jc` Translation Tables — Notation Mappings, Not Physical Equivalences | **stay** | L3 adds 8 new rows = more notation mappings. Same claim. |

### common/two-engine-architecture-a027.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-zgllr2` A-027 Two-Engine Architecture — Regime-Partitioned Simulation | **stay** | Unchanged. |
| `clm-zfqd9v` Wave-Speed Modulation Is Required to Localize a Bound State | **stay** (strengthened) | L3 applies sign-flip correction `c_eff = c₀√S` → `c₀/√S` with explicit "Prior verbal description superseded" retraction tag. Wave-speed modulation IS still required; the direction was simply inverted in our current text. Rescore-up likely. **Apparent conflict with operators.md Op16 `c_shear = c₀√S` is resolved by two-engine's own note** — different physical quantities (phase velocity inside saturated core vs shear wave on boundary). |
| `clm-gr8d63` Two-Engine Convergence on p* = 8πα | **stay** (inbound from q-g47 rehoming) | Canonical home post-merge. |

### common/universal-saturation-kernel-catalog.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-gz7ryg` A-034 Single-Kernel Unification | **stay** | Catalog growth doesn't change the unification thesis. |
| `clm-dxdsvt` A-034 Catalog — 21 Canonical Cross-Scale Instances | **stay + title/text update** | Catalog grew 21 → 26 in L3. Update claim title and rationale to "26 Canonical Cross-Scale Instances" during rescore. Same claim, larger N. Rescore-up likely (more instances = stronger empirical support). |
| `clm-hvvvop` A-034 Symmetry Classification — SYM / ASYM-N / ASYM-E | **split** | L3 adds an orthogonal **ε vs μ axis classification** with explicit gap-cell table. The two classification axes are conceptually distinct dimensions. Keep `clm-hvvvop` as the 3-way SYM/ASYM classification; **assign a new clm-id for the ε/μ axis classification** during rescore. |
| `clm-l4o7hv` Cosmic-Scale Instance (Big Bang as A-034) | **stay** | Unchanged. |

**Adjudication resolved by time**: MOND classification — catalog row tagged `2026-05-19 EOD adjudication item` says **SYM**; `common/vol3/condensed-matter/.../saturated-lattice-mutual-inductance.md` (unchanged in this round, strictly older) says ASYM-N(μ). Catalog wins. Propagate SYM to `saturated-lattice-mutual-inductance.md` during the merge sweep.

### common/xi-topo-traceability.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-sxn6eo` Mathematical Closure Status (shared with full-derivation-chain) | **stay** | Cross-leaf cite preserved. |
| `clm-hmiytz` ξ_topo Traceability — Conversion Constant, Not Free Parameter | **stay** | Unchanged. |

**Rigor regression to NOT port**: L3 simplifies the zero-free-parameter chain equation, dropping the "conditional on thermal closure of δ_strain at T_CMB" qualifier (silent regression). Preserve current qualified form. Also: L3 leaks LaTeX `\ref{}` into markdown — keep current Markdown form.

### vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-9s9apq` EMT p_c = 8πα — Consistency Relation, NOT α Derivation | **stay** (strengthened) | L3 G walk-back (Grant canonized 2026-05-19 EOD) parallels the same "consistency-not-derivation" framing this claim asserts for α/p_c. Meta-framing is captured by `clm-sxn6eo` on full-derivation-chain — no new claim needed here. Rescore-up likely. |

### vol1/dynamics/ch4-continuum-electrodynamics/bullet-cluster.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-m3z5ux` H_∞ and MOND a_0 (cross-leaf cite from mond-hoop-stress) | **needs-assessment + likely drop + new** | L3 fully replaces the bullet-cluster mechanism (TT shockwave retired → ponderomotive halos + Einstein lensing on Gordon optical metric). The leaf no longer hinges on H_∞/MOND a_0 derivation. **Likely drop `clm-m3z5ux` from this leaf's `claims:`** and **assign a new clm-id for "Bullet Cluster as Ponderomotive Halo + Einstein Lensing on Gordon Optical Metric"** during merge. Confirm by re-reading L3 bullet-cluster.md text. |

### vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-crbl60` Vacuum Bulk Mass Density and Shear Modulus | **stay** (strengthened) | L3 corrects the 13-orders-of-magnitude G_vac error (was conflating 1D string-tension with 3D shear modulus) with explicit audit note. Same claim, much higher local rigor. Rescore-up likely. |

### vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-m3z5ux` H_∞ and MOND a_0 | **stay** (refined) | L3 adds explicit Class E operating-point projection framing for H_∞ (mirrors `clm-sxn6eo` strengthening). GC-class scope correction (Outcome III walk-back) sharpens the claim's locus to LSR-class kinematics only. Same claim, sharper boundary. Rescore likely. |

**Canonical-home decision**: mond-hoop-stress.md is the canonical home for the new Hoop Stress 2π projection motif material (operators.md §5.5 collapses to a cross-ref).

### vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-3npynp` Photon Identification — T_2-Only Cosserat Microrotation | **stay + small text update** | L3 expands 3 → 4 photon properties (adds "impedance-matched at Z_0"). Same claim, 4th property is a refinement. Update claim text to reflect 4 properties. |
| `clm-i4p11y` Electron = Photon + TIR Confinement | **stay** | L3's new §4.0 "symmetric framing" is a restatement of this claim in symmetric language. Same claim. |
| `clm-fr3mos` Compton Frequency ω_C as Photon→Electron Transition Threshold | **stay** | Unchanged. |

### vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-b2anl4` Four-Regime Map — Boundary Derivations Sector-Dependent (cross-leaf) | **stay** | Unchanged. |
| `clm-82dxbj` Domain Catalog Operating-Point Examples | **stay** | Unchanged. |

### vol1/operators-and-regimes/ch7-regime-map/four-regimes.md

| Claim | Disposition | Rationale |
|---|---|---|
| `clm-2dwzib` V_snap vs V_yield — Two Distinct Thresholds | **stay** | Unchanged. |
| `clm-b2anl4` Four-Regime Map — Boundary Derivations Sector-Dependent | **stay** | **Rigor regression in L3 — preserve current**. L3 silently removes the spin-sector-dependence note for r₂ = √3/2 and the "Note (cross-link with Ch.3)" sidebar. The sector-dependence note IS the claim's substantive content; removal contradicts the claim's own title. Keep current. |

### Indexes (no leaf-claims; subtree-claims auto-refresh)

- `common/index.md` — subtree-claims; refresh-managed.
- `common/translation-tables/index.md` — subtree-claims; refresh-managed.
- `vol1/dynamics/ch4-continuum-electrodynamics/index.md` — subtree-claims; refresh-managed. Add new `preferred-frame-and-emergent-lorentz.md` leaf row.
- `vol1/index.md` — subtree-claims; refresh-managed. **Foreword text regression — revert**: L3's "G from the Machian boundary (Axiom 3)" contradicts the parallel walk-back in `zero-parameter-universe.md` (Grant canonized 2026-05-19 EOD). Update vol1/index.md to "G is Bounding Limit 3 / Class E joint constraint" or equivalent to align with the walk-back.

### Trampoline framework

`common/trampoline-framework.md` is `no-claim` (picture-first synthesis). No claim triage. **One numeric correction to apply**: BH-event-horizon ε₁₁(r) coefficient `2GM/(c²r)` → `7GM/(c²r)` (verify against `dielectric-rupture-event-horizon.md` and the saturation-kernel catalog before adopting; if correct, propagate to any other locus with the same form).

## Cross-cutting summary

### Claim entries needing canonical updates during merge

| Claim | Update |
|---|---|
| `clm-dxdsvt` | Title/text 21 → 26 instances; rationale notes ε/μ axis (refers to split below) |
| `clm-hvvvop` | Split — new clm-id for ε/μ axis classification |
| `clm-3npynp` | Text update — 3 → 4 photon properties |
| `clm-m3z5ux` (mond-hoop-stress side) | Add Class E framing + GC-class scope correction |
| `clm-bjceop` | Note ξ_K1 = 8/3, ξ_K2 = 32 closure (forced ratio = 12 already in title) |

### Rehomings

| Claim | From | To |
|---|---|---|
| `clm-gr8d63` | q-g47 | two-engine-architecture-a027 |
| `clm-m3z5ux` (bullet-cluster side, pending confirm) | bullet-cluster | (likely removed; new claim assigned for ponderomotive-halo mechanism) |

### New claims to assign during rescore

1. **ε/μ axis classification** (split off from `clm-hvvvop`) — universal-saturation-kernel-catalog.
2. **Bullet Cluster as Ponderomotive Halo + Einstein Lensing on Gordon Optical Metric** — bullet-cluster.md (pending confirmation that `clm-m3z5ux` no longer applies).

### Rigor regressions to NOT port (preserve current text)

| Leaf | Regression | Preserve |
|---|---|---|
| `omega-freeze-cosmic-grain-cascade.md` | §4 / §6 "Provisional discussion — not a framework claim" guardrails dropped | Keep guardrails. |
| `xi-topo-traceability.md` | "conditional on thermal closure of δ_strain at T_CMB" qualifier dropped from chain equation; LaTeX `\ref{}` leak | Keep qualifier + Markdown form. |
| `four-regimes.md` | Spin-sector-dependence note for r₂ = √3/2 dropped; "Note (cross-link with Ch.3)" sidebar dropped | Keep both. |
| `operators.md` §2 | LaTeX → unicode notation regression across catalog table | Keep LaTeX. |
| `full-derivation-chain.md` | "Methodology disclosure" callout block on lepton derivation dropped | Keep callout. |
| `vol1/index.md` | "G from the Machian boundary (Axiom 3)" regresses vs zero-parameter-universe walk-back | Align with walk-back ("G is Bounding Limit 3 / Class E joint constraint"). |

### Adjudications resolved by time/clarity heuristics

| Item | Resolution | Evidence |
|---|---|---|
| G framing — vol1/index vs zero-parameter-universe | Walk-back wins | zero-parameter-universe.md carries `Grant canonized 2026-05-19 EOD` tag + `research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md` cite. vol1/index.md is a stale summary with no canonicalization tag. |
| MOND classification — SYM vs ASYM-N(μ) | SYM wins | Catalog row tagged `2026-05-19 EOD adjudication item`; `saturated-lattice-mutual-inductance.md` not in round-2 diff (strictly older). |
| c_eff sign — `c₀/√S` vs `c₀√S` | Both stand | two-engine's explicit `Prior verbal description superseded` tag fixes the phase-velocity case (`c₀/√S`); Op16's `c_shear = c₀√S` is a different physical quantity (shear wave on boundary). |
| Hoop Stress motif canonical home | mond-hoop-stress wins | Contemporaneous additions; clarity call (topic leaf > catalog index). |

### Adjudications deferred (need brief L3-text inspection during merge)

| Item | What to check |
|---|---|
| `omega-freeze` "Provisional" guardrail drop | Run `git log -p analysis/integration -- common/omega-freeze-cosmic-grain-cascade.md` in AVE-Core_L3. If commit message names an explicit "no longer provisional" promotion → accept the drop. If silent → keep guardrails. |
| `bullet-cluster` clm-m3z5ux still load-bearing? | Read L3 `bullet-cluster.md` body; if H_∞/MOND a_0 derivation is still cited as the load-bearing background, keep clm-m3z5ux; if the new ponderomotive-halo mechanism is self-contained, drop it and add the new claim. |

## Summary counts

- **21 modified leaves scanned**; 11 carry leaf-level claim machinery; 4 are indexes; 1 is no-claim; 5 are single-leaf claim cites with simple stay-disposition.
- **31 unique claim IDs touched**.
- **Dispositions**: 27 **stay**, 1 **rehome** (`clm-gr8d63` → two-engine), 1 **split** (`clm-hvvvop` → +1 new claim), 1 **stay+title-update** (`clm-dxdsvt`), 1 **needs-assessment** (`clm-m3z5ux` on bullet-cluster).
- **New claims to assign**: 2 (ε/μ axis classification; bullet-cluster ponderomotive-halo mechanism).
- **Rigor regressions to NOT port**: 6 leaves carry silent L3 regressions; preserve current text in those passages.
- **Rescore candidates after merge**: clm-sxn6eo, clm-pe8lpx, clm-bjceop, clm-zfqd9v, clm-dxdsvt, clm-9s9apq, clm-crbl60, clm-m3z5ux (mond-hoop-stress side), and the 2 new claims — most likely lift, none likely drop.
