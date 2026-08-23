# `src/scripts/_archive/` — archive manifest

**Status:** ACTIVE — append-only. One row per archived driver, with the verification receipts
that justified the move.
**Governing ruling:** D13 (Wave-2 adjudication sitting, 2026-08-18) — *unreferenced drivers:
**ARCHIVE-AFTER-VERIFICATION**, verification lane mandatory (~50% false-dead rate measured on
the 8-sample; the 95-list is a candidate set)*. **NO DELETIONS** — archive only.
**Lane:** repo-cleanup epic Wave-3 item 1 (bundled D13 verification + D15f-3 migration).

## What this directory is

Frozen drivers that no tracked text file references and whose outputs no tracked text file
cites. They stay in-tree, runnable, and readable — the move is a live-tree hygiene action
(the tree stops advertising a dead entry point), not a retraction. `git log --follow` on any
path below reaches its full pre-archive history. To revive one, `git mv` it back.

`src/tests/test_scripts_import_smoke.py` excludes `_archive` from its walk
(`_EXCLUDED_DIR_NAMES = {"_archive"}`), so archived drivers are outside the import gate.

## Flat-tier note (pre-existing, 2026-08-20)

The 23 files directly under `src/scripts/_archive/` predate this manifest (no per-volume
subdir, no receipts). Four of them are **same-named but byte-DIFFERENT twins** of files that
were still live in `src/scripts/vol_1_foundations/` at HEAD `5164d000`
(`r8_phase1_attractor_characterization_v2_fft_fix.py`,
`r8_phase1_attractor_winding_characterization.py`, `r8_phase1_reactance_tracking.py`,
`r8_phase1_reactance_tracking_v2.py` — `git hash-object` differs on all four pairs). Those
live twins are **not** archived by this pass (they are FLAG-PAIRED — see the routed section);
the duplicate-pair class is flagged, not resolved. Per-volume subdirs are used from this pass
forward so a future move cannot collide with the flat tier.

## Verification method (what every receipt below rests on)

Candidate set re-derived at HEAD `5164d000`; the method reproduces the 2026-08-17 census
**exactly** (152 drivers unreferenced by a word-boundary stem scan excluding `_archive`
*citers*; 57 of those are cited **only** from `research/_archive/` or `src/scripts/_archive/`
and are therefore NOT candidates; **95** have zero citers anywhere — the census's 95, same
membership at both HEADs).

Per candidate, the D13 checklist:

| # | method | what it catches |
|---|---|---|
| a1 | plain-substring + word-boundary stem grep over every tracked text file | direct name citers |
| a2 | hyphen/underscore-normalized token grep | docs writing `foo-bar` for `foo_bar` |
| a3 | **output-filename grep** — parse the driver's artifact literals, grep the corpus for them | *a driver whose OUTPUT is cited is alive* |
| a4 | extension-less artifact linking — intersect the driver's string literals with tracked figure/data stems | helper-saved figures (`style.save(fig, "name")`) with no `.png` literal in source |
| b | cross-repo grep over every sibling `AVE-*` repo under the workspace root (read-only) | out-of-repo citers |
| c | `git log -3` | recency / last-touch context |
| d | docstring run-by-hand-instrument judgment | standalone instruments with an explicit `Run:` / `Usage:` invocation |
| e | four-citer-class census methods incl. directory-as-container | ledger-only, brace-expansion, brace+glob, directory-level citers |

Every method-1 stem hit was validated line-by-line per the 2026-08-19 both-directions
addendum (stem matching MANUFACTURES citers). Validated false-citer classes found in this
pass: function-name collisions, sibling-filename prefix collisions (`_v2`, `_reanalysis`),
`src/scripts/_archive/` twins writing the same output name, competing generators mistaken for
citers, and English words matching a figure stem.

**Cross-repo result: 0.** No sibling `AVE-*` repo cites any of the 95 candidates. (The raw
scan's 28 hits were all `AVE-Core-worktrees/*` — worktrees of this same repo, i.e. self-hits.)

## Outcome of the 95-candidate verification (2026-08-20)

| verdict | n | disposition |
|---|---:|---|
| LIVE (output-cited) | 22 | untouched |
| LIVE (run-by-hand instrument) | 7 | untouched |
| LIVE (sole regeneration path for a D14-pruned regenerable) | 2 | untouched |
| FLAG — routed, not archived | 35 | untouched; classes listed below |
| **CONFIRMED-DEAD → archived here** | **29** | rows below |

**31 of 95 candidates (33%) were false-dead** on the citer axis alone, and a further 35 (37%)
were routed rather than archived — consistent with the ~50% false-dead rate D13 measured on
its 8-sample.

---

## Archived 2026-08-20 — D13 verification lane

### `vol_1_foundations/` — 17 files

| file | last touch | writes | receipts |
|---|---|---|---|
| `back_emf_conservative_v4.py` | 2026-06-28 `5d99ae77` — Retract stabilized-electron ε̄→α result as artifact (Rule-12) | `back_emf_conservative_results.json` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **last touch is the Rule-12 retraction of the stabilized-electron ε̄→α result; the retraction RECORD (a research doc) is untouched and stays live.** |
| `cosserat_beltrami_isolated_test.py` | 2026-05-27 `c159b318` — src: pin encoding="utf-8" on all text read/write (D15 clean sweep) | `cosserat_beltrami_isolated.json`, `cosserat_beltrami_isolated_panels.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `dark_wake_extended_baseline.py` | 2026-05-27 `c159b318` — src: pin encoding="utf-8" on all text read/write (D15 clean sweep) | `dark_wake_extended_baseline.gif`, `dark_wake_extended_baseline.json`, `dark_wake_extended_baseline.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `electron_convergence_study.py` | 2026-05-21 `03f35f85` — initial transfer of python code from analysis/integration - NOT PASSING COMMIT H | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `electron_path_c_validation.py` | 2026-05-21 `03f35f85` — initial transfer of python code from analysis/integration - NOT PASSING COMMIT H | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `electron_propagation_3d.py` | 2026-06-07 `972dd988` — Electron genesis: native Γ ceiling, propagation snap, α-engine adjudication. | `electron_propagation_3d.gif`, `electron_propagation_3d_results.json` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **the `_orchestration/2026-06-08_…handoff.md:60` GIF line names `electron_propagation_native.gif` (the LIVE `electron_propagation_showcase.py`), NOT `electron_propagation_3d.gif`.** |
| `electron_tlm_y_matrix_diagnostic.py` | 2026-05-21 `03f35f85` — initial transfer of python code from analysis/integration - NOT PASSING COMMIT H | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `k4_port_control_diagnostic.py` | 2026-06-28 `5d99ae77` — Retract stabilized-electron ε̄→α result as artifact (Rule-12) | `k4_port_control_diagnostic.png`, `k4_port_control_diagnostic_results.json` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **same Rule-12 retraction commit as above.** |
| `phase3b_canonical.py` | 2026-05-24 `48a3db98` — coding standard fixup/unification - only modern annotations, no  - that is a dep | `phase3b_canonical.npz`, `phase3b_canonical.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `phase3b_x2_seed_indep.py` | 2026-05-24 `48a3db98` — coding standard fixup/unification - only modern annotations, no  - that is a dep | `phase3b_x2_seed_indep.npz`, `phase3b_x2_seed_indep.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `photon_rifling_full.py` | 2026-05-24 `48a3db98` — coding standard fixup/unification - only modern annotations, no  - that is a dep | `photon_rifling_full_` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `photon_rifling_propagation.py` | 2026-05-24 `48a3db98` — coding standard fixup/unification - only modern annotations, no  - that is a dep | `photon_rifling_axis_`, `photon_rifling_propagation_` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `photon_rifling_with_wake.py` | 2026-05-24 `48a3db98` — coding standard fixup/unification - only modern annotations, no  - that is a dep | `photon_rifling_dark_wake_` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `render_balanced_electron_soliton.py` | 2026-06-28 `5d99ae77` — Retract stabilized-electron ε̄→α result as artifact (Rule-12) | `balanced_electron_soliton.gif`, `balanced_electron_soliton.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **same Rule-12 retraction commit as above.** |
| `theorem_3_1_neumann_validation.py` | 2026-05-21 `03f35f85` — initial transfer of python code from analysis/integration - NOT PASSING COMMIT H | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **`theorem_3_1` hits in the corpus are all `research/_archive/L3_electron_soliton/1{4,6,7}_theorem_3_1_*.md` DOC names, not this driver.** |
| `vacuum_engine_asymmetric_genesis.py` | 2026-06-28 `5d99ae77` — Retract stabilized-electron ε̄→α result as artifact (Rule-12) | `asymmetric_genesis.gif`, `phase_iiib_sigma_omega.png`, `phase_iiib_sweep_summary.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **same Rule-12 retraction commit. Its `/tmp/phase_iiib_*.png` names are CLAIMED BY THE CITED SIBLING `vacuum_engine_pair_creation.py:21-22` (two drivers, same /tmp filenames) — the archive-doc citations of those names attach to the sibling, which stays live.** |
| `validate_cosserat_alpha_via_s11.py` | 2026-06-03 `d81d7c44` — docs(framing): honest-α relabel — narrow derives→closed-form-Class-B (ave-walk-b | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **the corpus-cited α driver is the DIFFERENT `validate_cosserat_alpha_via_ch8_ratios.py` (5+ citers incl. `assets/3d_models/ACCURATE_SCALING.md:114`); this `_via_s11` variant has zero.** |

### `vol_3_macroscopic/` — 4 files

| file | last touch | writes | receipts |
|---|---|---|---|
| `design_tabletop_ferrofluid.py` | 2026-04-22 `b267124b` — annotations uniformity for scripts. | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `simulate_lunar_inductive_heating.py` | 2026-06-23 `5599101c` — D3: repair 3 stale ave.core imports + add AST import-resolution smoke gate | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **last touch is the D3 stale-import repair sweep (mechanical, not a content revival).** |
| `solar_system_animation.py` | 2026-04-22 `b267124b` — annotations uniformity for scripts. | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `solar_system_induction_tensors.py` | 2026-04-22 `b267124b` — annotations uniformity for scripts. | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |

### `vol_4_engineering/` — 8 files

| file | last touch | writes | receipts |
|---|---|---|---|
| `compare_standard_vs_ave_doping.py` | 2026-04-22 `b267124b` — annotations uniformity for scripts. | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `means_test_doping.py` | 2026-04-22 `b267124b` — annotations uniformity for scripts. | — (no artifact) | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `run_impedance_gravity_well.py` | 2026-06-18 `68ddc647` — notation: retire substrate-as-condensate noun — extend INVARIANT-N1 (#291) | `impedance_gravity_well_time_domain.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `run_memristor_and_skineffect.py` | 2026-06-18 `68ddc647` — notation: retire substrate-as-condensate noun — extend INVARIANT-N1 (#291) | `memristor_and_skineffect.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `run_orbital_reactive_power.py` | 2026-06-18 `68ddc647` — notation: retire substrate-as-condensate noun — extend INVARIANT-N1 (#291) | `orbital_reactive_power.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers · **the `orbital_reactive_power` hits are a FUNCTION def at `src/ave/gravity/orbital_lc_damping.py:22` (imported by the live `vol_3_macroscopic/simulate_binary_lc_damping.py`), not this driver's figure.** |
| `run_vacuum_imd_spectroscopy.py` | 2026-06-18 `68ddc647` — notation: retire substrate-as-condensate noun — extend INVARIANT-N1 (#291) | `condensate_imd_spectroscopy.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `simulate_alchemist_forge.py` | 2026-05-24 `a28132e9` — output paths: move resolver to layer-neutral ave_path_util; add asserting manusc | `alchemist_forge_stage1_He.png`, `alchemist_forge_stage2_O16.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |
| `simulate_polyhedral_rlvg_gradient.py` | 2026-05-24 `a28132e9` — output paths: move resolver to layer-neutral ave_path_util; add asserting manusc | `polyhedral_rlvg_compass.png` | a1/a2 0 citers · a3 0 output-citers · a4 writes no tracked artifact · b 0 cross-repo · e 0 ledger/brace/glob/dir citers |

---

## Routed, NOT archived — 35 candidates (2026-08-20)

These verified as zero-citer but were **not** archived. Each is a one-liner for the
orchestrator/Grant, recorded here so the decision is visible where the archive lives.

### FLAG-PAIRED — 21 · writes a TRACKED-but-uncited artifact

Archiving the driver alone strands a tracked artifact from its generator; moving the pair
crosses into the orphan-DATA axis (D15c), which this lane was not ruled to touch. **The
question:** archive driver + its adjacent result artifact as a pair, or leave both live?

| driver | tracked artifact it wrote |
|---|---|
| `src/scripts/vol_1_foundations/genesis_v8_threaded_smoke.py` | `research/2026-06-11_genesis-v8-threaded_smoke.json` |
| `src/scripts/vol_1_foundations/photon_axis_kinematics.py` | `assets/photon_axis_kinematics.png`, `results/photon_axis_kinematics.json` |
| `src/scripts/vol_1_foundations/photon_chiral_comparison.py` | `assets/photon_chiral_comparison.png`, `results/dark_wake_chiral_validation.json`, `results/photon_chiral_comparison_summary.json`, `results/photon_chiral_yee.json` |
| `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t1_extensions.py` | `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t1_extensions_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t1_extensions_reanalysis.py` | `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t1_extensions_bandpass_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t2_dispersion.py` | `src/scripts/vol_1_foundations/r10_v8_foundation_audit_t2_dispersion_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_o1b_v_inc_topology.py` | `src/scripts/vol_1_foundations/r10_v8_o1b_v_inc_topology_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_o1c_corrected_winding.py` | `src/scripts/vol_1_foundations/r10_v8_o1c_corrected_winding_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_o1d_winding_v2.py` | `src/scripts/vol_1_foundations/r10_v8_o1d_winding_v2_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_o1e_fft_cavity_vs_flux.py` | `src/scripts/vol_1_foundations/r10_v8_o1e_fft_cavity_vs_flux_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_phi_link_capture.py` | `src/scripts/vol_1_foundations/r10_v8_phi_link_capture.npz`, `src/scripts/vol_1_foundations/r10_v8_phi_link_capture_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v1.py` | `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v1_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v2_high_T.py` | `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v2_high_T_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v3_cusp.py` | `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v3_cusp_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v4_chronic.py` | `src/scripts/vol_1_foundations/r10_v8_t_st_corpus_vacuum_v4_chronic_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_t_st_dispersion_check.py` | `src/scripts/vol_1_foundations/r10_v8_t_st_dispersion_check_results.json` |
| `src/scripts/vol_1_foundations/r10_v8_t_st_v2_n96.py` | `src/scripts/vol_1_foundations/r10_v8_t_st_v2_n96_capture.npz`, `src/scripts/vol_1_foundations/r10_v8_t_st_v2_n96_results.json` |
| `src/scripts/vol_1_foundations/r8_phase1_attractor_characterization_v2_fft_fix.py` | `src/scripts/vol_1_foundations/r8_phase1_attractor_characterization_v2_fft_fix_results.json` |
| `src/scripts/vol_1_foundations/r8_phase1_attractor_winding_characterization.py` | `src/scripts/vol_1_foundations/r8_phase1_attractor_winding_results.json` |
| `src/scripts/vol_1_foundations/r8_phase1_reactance_tracking.py` | `src/scripts/vol_1_foundations/r8_phase1_reactance_tracking_results.json` |
| `src/scripts/vol_1_foundations/r8_phase1_reactance_tracking_v2.py` | `src/scripts/vol_1_foundations/r8_phase1_reactance_tracking_v2_results.json` |

### FLAG-VOL6ANIM — 13 · the `vol_6_periodic_table/animations/animate_*.py` family

All 13 (plus the 2 non-candidate siblings `animate_hydrogen.py`, `animate_silicon.py`)
import `periodic_table.simulations.simulate_element`, which is **unresolvable at HEAD**
(`importlib.util.find_spec('periodic_table')` → None; the module lives at
`src/scripts/vol_6_periodic_table/simulations/simulate_element.py` under a different
package path). They write `<element>_<A>_dynamic_flux.**gif**` into a relative
`periodic_table/figures` dir that does not exist. The manuscript cites
`<element>_<A>_dynamic_flux.**png**` — 14 tracked under
`manuscript/vol_6_periodic_table/figures/` (aluminum · argon · calcium · chromium ·
fluorine · hydrogen · iron · magnesium · neon · oxygen · silicon · sodium · sulfur ·
titanium). That is the addendum's **sibling-extension** false-citer class, so by method
these drivers are dead. Two sub-cases:

- **6 of the 13** (`aluminum`, `fluorine`, `magnesium`, `neon`, `oxygen`, `sodium`) are the
  nominal — and only in-tree — provenance for a cited manuscript `.png`. Archiving them
  leaves those 6 figures with **no generator at all** anywhere in the tree.
- **7 of the 13** (`beryllium`, `boron`, `carbon`, `dt_fusion`, `helium`, `lithium`,
  `nitrogen`) have no tracked `.png` counterpart; nothing cites their `.gif` either.
  (`helium`/`lithium` look cited only because `src/tests/test_dynamic_density.py:229,240`
  is a **competing generator** of the same `.gif` names, not a citer.)

Separately: 8 of the 14 cited `.png`s (argon, calcium, chromium, hydrogen, iron, silicon,
sulfur, titanium) have no candidate generator in this family at all — hydrogen and silicon
have `animate_*.py` siblings that are not candidates, the other 6 have nothing.
`src/tests/test_scripts_import_smoke.py` does not catch the broken import: it scopes to
`from ave.core.<mod> import NAME` only. **The question:** archive the family and record the
figure-provenance gap, or repair the import + output path first?

- `src/scripts/vol_6_periodic_table/animations/animate_aluminum.py`
- `src/scripts/vol_6_periodic_table/animations/animate_beryllium.py`
- `src/scripts/vol_6_periodic_table/animations/animate_boron.py`
- `src/scripts/vol_6_periodic_table/animations/animate_carbon.py`
- `src/scripts/vol_6_periodic_table/animations/animate_dt_fusion.py`
- `src/scripts/vol_6_periodic_table/animations/animate_fluorine.py`
- `src/scripts/vol_6_periodic_table/animations/animate_helium.py`
- `src/scripts/vol_6_periodic_table/animations/animate_lithium.py`
- `src/scripts/vol_6_periodic_table/animations/animate_magnesium.py`
- `src/scripts/vol_6_periodic_table/animations/animate_neon.py`
- `src/scripts/vol_6_periodic_table/animations/animate_nitrogen.py`
- `src/scripts/vol_6_periodic_table/animations/animate_oxygen.py`
- `src/scripts/vol_6_periodic_table/animations/animate_sodium.py`

### FLAG-OPENITEM — 1

- `src/scripts/vol_3_macroscopic/simulate_spacecraft_flyby.py` — 0 citers (the CITED flyby driver is the different src/scripts/verify/flyby_anomaly_anderson_anchor.py) BUT open-item p19-flyby-readjudication is live on this observable — routed, not archived

