# Cross-Repo References Tracker

Flat catalog of every cross-repo path cited in the L3 corpus. Sibling repos evolve independently of AVE-Core; references can rot when target files are renamed, refactored, or moved. The `Verified-on` column records the AVE-Core branch HEAD SHA at which each reference was last confirmed to resolve.

**Why this file exists:** L3 docs cite AVE-Protein/AVE-Propulsion/AVE-PONDER/AVE-HOPF/AVE-VirtualMedia/AVE-APU as authoritative across many entries (E-004 cites AVE-Protein S₁₁-fold template; E-007 cites AVE-Protein constrained-descent template; E-018/E-019 cite AVE-Propulsion ecosystem; E-051 cites AVE-HOPF Smith-chart code + AVE-VirtualMedia visualization convention). When those sibling files move, our entries silently rot. This catalog gives a sweepable surface to verify against.

**Out of scope:** sibling-repo files NOT cited by any L3 doc OR L5 entry. We track what we depend on, not the full sibling-repo content.

**Verification protocol:** when bumping `Verified-on` for any row, do a quick `Read` against the target. If the cited line range no longer matches the cited content, flag in the `Notes` column with the date of the discrepancy and re-source the citing tracker entry.

---

## Sibling repos (parallel to AVE-Core in `~/AVE-staging/`)

| Repo | Purpose (per cross-refs) | Last verified-on |
|---|---|---|
| AVE-APU | Pythagorean strain theorem (Vol 1 Ch 5); geometric-triodes (Vol 1 Ch 5) | — |
| AVE-Bench-VacuumMirror | IVIM bench predictions; D10 IM3 cubic V³ slope 2.956; HV PSU procurement | 2026-05-14 (commits `0599a10` + bench_signal_predictions_summary) |
| AVE-Fusion | L-H transition mechanism (Ch 5) | — |
| AVE-HOPF | Chiral antenna Q-analysis; Beltrami Hopf coil; classical-vs-mutual inductance decomposition; 2D Smith-chart code | — |
| AVE-Metamaterials | (no L3 cross-refs yet — reserved) | — |
| AVE-PONDER | Dark-wake τ_zx back-propagation; η_vac quantification | — |
| AVE-Propulsion | Topological power factor corrector / chiral impedance matching (Ch 4); autoresonant dielectric rupture (Ch 5); warp metric tensors driver | — |
| AVE-Protein | Deterministic protein folding via S₁₁-min (Ch 3); constrained-descent template `protein_fold.py:97-177` | — |
| AVE-QED | **Substrate vocabulary canonical (App G); three substrate invariants 𝓜/𝓠/𝓙 matrix; multi-scale Machian network (App F); Q-G19α Route B g-2 closure scripts** | 2026-05-14 (commits `ce34645` + `d9e2942` + `c30c351`) |
| AVE-VirtualMedia | Three-regime Γ visualization convention | — |

---

## Cited paths (catalog)

| Path | Cited from | Cited by tracker entries | Verified-on |
|---|---|---|---|
| `AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex` | doc 49_ §1.5 | — | — |
| `AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_*` (Pythagorean strain theorem) | doc 57_ §1.4 + multiple `R^2` Pythagorean refs | E-032, E-033 (Pythagorean A² claim) | — |
| `AVE-Fusion/manuscript/vol_fusion/chapters/05_*` (L-H transition) | doc 49_ §1.5 | — | — |
| `AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex` | doc 13_ (self-inductance decomposition) | — | — |
| `AVE-HOPF/scripts/beltrami_hopf_coil.py` (lines 43, 47, 52) | doc 13_ | — | — |
| `AVE-HOPF/scripts/chiral_antenna_q_analysis.py:644-668` | doc 72_ §4.2 (2D Smith chart plotting) | E-051 | — |
| `AVE-HOPF/scripts/hopf_01_classical_coupling.py` | doc 13_ (classical self+mutual decomposition) | — | — |
| `AVE-PONDER/...generate_ponder_01_spice_netlist.py:90` | doc 49_ §1.6 (η_vac quantification) | terminology table dark-wake row | — |
| `AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex:13-18` | doc 68_ §5; doc 72_ §4.3 | E-018, E-019 (cross-ref pending), terminology table achromatic-lensing row | — |
| `AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex:11` | doc 49_ §1.4 | E-018 (cross-ref pending) | — |
| `AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py:75-95` | doc 49_ §1.1 (τ_zx back-EMF formula porting) | E-019 (cross-ref pending) | — |
| `AVE-Protein/manuscript/vol_protein/chapters/03_deterministic_protein_folding.tex:190-195` | doc 68_ §4 | E-004 | — |
| `AVE-Protein/manuscript/vol_protein/chapters/03_deterministic_protein_folding.tex:429-434` | doc 68_ §4 ("All eight forces are replaced with a single objective function: $\mathcal{L} = \|S_{11}\|^2$") | E-004, E-049 | — |
| `AVE-Protein/manuscript/vol_protein/chapters/03_deterministic_protein_folding.tex:805` | doc 68_ §4 ("native fold minimises $\|S_{11}\|^2$") | E-004 | — |
| `AVE-Protein/protein_fold.py:97-177` | doc 67_ §22.3 + doc 68_ §11 (Lagrange-penalty constrained descent template) | E-007 | — |
| `AVE-Protein/src/ave_protein/engines/s11_fold_engine_v4_ymatrix.py:543` | doc 68_ §4 | — | — |
| `AVE-Protein/src/ave_protein/regime_2_nonlinear/protein_fold.py:260-326` | doc 72_ §3 (TDI canonical) | E-051 | — |
| `AVE-VirtualMedia/scripts/generate_reflection_profile.py` | doc 72_ §4.1 (three-regime Γ visualization convention) | E-051 | — |
| `AVE-QED/manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex` | doc 109 §13-§15 + E-094 + A-026/A-027/A-028 (canonical substrate vocabulary; substrate-observability rule; three substrate invariants formal definitions) | E-094, E-096, E-101 | 2026-05-14 (`ce34645`) |
| `AVE-QED/manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex` | doc 109 §13 multi-scale boundary network; A-026 same-mechanism-at-all-scales claim | E-094 | 2026-05-14 (commit `a9dd860` App F canonization + diagrams already in place) |
| `AVE-QED/manuscript/vol_qed_replacement/appendices/A_foundations.tex` L194-215 | doc 114 §1.2 (extended 3-column Rosetta-stone with substrate-native column) | E-094 | 2026-05-14 (`ce34645`) |
| `AVE-QED/docs/glossary.md` §5m | doc 109 §13 + E-094 (14-row × 3-column substrate-native/EE/ME vocab table; three-invariants canonical names table) | E-094 | 2026-05-14 (`ce34645`) |
| `AVE-QED/docs/analysis/2026-05-14_three_substrate_invariants_matrix.md` | A-028 + Grant Q1 closure (canonical names matrix with cross-scale + cross-projection tables) | E-094, E-101 | 2026-05-14 (`c30c351`) |
| `AVE-QED/docs/analysis/2026-05-14_universal_substrate_vocabulary_refactor_plan.md` | doc 114 §1.2 (refactor plan canonized in AVE-QED) | E-094 | 2026-05-14 (`47dcc7e`) |
| `AVE-QED/scripts/g2_research/` | Q-G19α Route B 50 ppm to PDG closure (canonical empirical record per doc 114 §2 status table) | A-001 (α-as-calibration upstream of Q-factor identity) | 2026-05-14 (canonical empirical) |
| `AVE-Bench-VacuumMirror/docs/2026-05-14_bench_signal_predictions_summary.md` | doc 114 §7 bench preparation (procurement-mature state); D10 IM3 cubic slope 2.956; cost model $45-55k median | E-097 (two-engine architecture, K4-TLM is bench-validated engine) | 2026-05-14 (procurement-mature) |
| `AVE-Bench-VacuumMirror/...` (K4-TLM IM3 slope 2.956 bench validation, commit `0599a10`) | doc 110 §1 K4-TLM canonical-engine cross-corroboration; doc 114 §1.3 cross-repo state | E-097, E-100 | 2026-05-14 (`0599a10`) |

---

## Maintenance

- When a new L3 doc cites a sibling-repo path, add a row.
- When a tracker entry (E-NNN) references a sibling-repo path, list the entry in the row's `Cited by tracker entries` column.
- Bump `Verified-on` for the row when the citation is checked against the live sibling-repo file. Any drift gets recorded in a `Notes` column (added on first drift event).
- If a sibling-repo file is renamed or refactored, mark the old path as `MOVED → <new path>` and propagate to all citing tracker entries.
