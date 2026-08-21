### ENTRY 2026-08-20-phase2-destination-map (2026-08-20): implementer — Wave-3 lane 1 Phase 2, the ratified figure/data destination map and its three resolved forks

- **Class: execution authorization, NOT adjudication.** This entry records a ruling Grant issued ("ratified, relaunch phase 2", 2026-08-20) and the re-verified measurement the ruling is executed against. It mints no claim, moves no grade, and opens no physics question. It exists because the Phase-2 stop-and-ask in [PR #991](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/991) was answered **in chat and not in the tree** — the lesson of the untracked authorization: an execution mandate that lives only in a session transcript cannot be audited, cannot be cited by the commits that discharge it, and re-litigates itself the next time the lane resumes.

**Prior state.** `_orchestration/2026-07_repo-conventions.md` §(a) is RATIFIED (Grant, 2026-07-04): *"cited renders live in tracked per-volume `figures/`; `_output/`=scratch"*, with the **link-coupled 5-step migration procedure** at `:56-66` as the only sanctioned way to execute a move, and the data-artifact half ruled **Option (1)** — *"a tracked per-volume `results/` dir mirroring `figures/`"*. Phase 2 halted on 2026-08-20 because three questions the ruling-as-written did not answer blocked destination assignment for 62 of 81 artifacts.

---

#### FORK-A — `src/scripts/vol_9_device/` has no manuscript volume of that name: **DISSOLVED**

The fork presumed a missing destination. There is none missing: **both** `src/scripts/vol_9_device/**` and `src/scripts/vol_9_vacuum_datasheet/**` feed the single manuscript volume `manuscript/vol_9_vacuum_datasheet/`, and the tree already says so in its own wiring.

- `manuscript/vol_9_vacuum_datasheet/figures/a1_spatial_cavity_mode_fft.tex:3-4` — the volume's own figure wrapper names the vol_9_device driver as its source (*"% Renders the native-engine output of: % src/scripts/vol_9_device/a1_radial_fft.py"*), and `:11` `\includegraphics{a1_spatial_cavity_mode_fft.png}` renders that driver's output.
- `manuscript/vol_9_vacuum_datasheet/figures/node_2domain_nport.tex:3` — *"% Renders the structure computed by src/scripts/vol_9_device/node_2domain_nport.py:"*.
- `manuscript/vol_9_vacuum_datasheet/figures/node_circulator_ring.tex:3` — same shape, same driver dir.
- `manuscript/vol_9_vacuum_datasheet/main.tex:7` already carries `{../../src/scripts/vol_9_device/cvr_ee_sweep/_output/}` **inside its `\graphicspath`** — the volume reaches into the vol_9_device scratch dir to build. That entry is exactly the policy smell §(a) names, and it is retired by this migration.

**Ruling: `vol_9_device` is the driver-side name for the vol_9 datasheet volume.** Destination for both driver trees is `manuscript/vol_9_vacuum_datasheet/`.

#### FORK-B — no `manuscript/vol_*/results/` exists, and a repo-root `results/` is in use: **ALREADY RULED, no conflict**

- The per-volume `results/` dirs were ratified 2026-07-04 (`_orchestration/2026-07_repo-conventions.md:12`, *"**data-artifact policy = Option (1)**: tracked per-volume `results/` dirs mirroring `figures/`"*). They do not exist on disk because **P3 never ran** — the execution phase the ratification gated them on. Absence is un-executed ratification, not a missing decision.
- Root `results/` holds 15 tracked artifacts at branch tip (`chiral_drive_selforbit_results.json`, `photon_chiral_yee.json`, the localization-readjudication pair, …). It is the **research-tier** data home and it **coexists**: per-volume `results/` is the canonical-corpus tier (a KB leaf or a `.tex` cites it), root `results/` is the research/orchestration tier.

**Ruling: create the per-volume dirs; the two tiers are not competitors.**

#### FORK-C — "the citing volume's `figures/`" undefined for research-only-cited artifacts: **CORRECTED**

Phase 1 counted any citer as a citer, so 62 of 81 looked unplaceable. The correction is a **definition**: a *KB citation* means a **canonical-corpus citation — the HARD-gated link class** that `manuscript/ave-kb/tools/verify-md-links.py` enforces on kbleaf→figure edges. A research doc naming an artifact is a *record*, not a canonical citation; it is repointed by the move, it does not determine the destination.

**Grant, 2026-08-20 — the residual treatment (ratified):** artifacts with no canonical-corpus citer are not stranded and are not held. Research/orchestration-only **renders** go to `research/figures/`; research/orchestration-only **data** goes to the existing root `results/`; `src/tests`-cited **fixtures** stay in place with a `.gitignore` allowlist comment naming the citer.

---

#### THE DESTINATION MAP (ratified; the classification rule is deterministic)

| # | class | trigger | destination |
|---|---|---|---|
| 1 | canonical render | KB and/or `manuscript/**.tex` citer | `manuscript/vol_<N>/figures/` of the **driver** volume |
| 2 | canonical data | KB and/or `manuscript/**.tex` citer | `manuscript/vol_<N>/results/` (created; Option 1) |
| 3 | research render | research/orchestration citer only | `research/figures/` |
| 4 | research data | research/orchestration citer only | `results/` (root, existing) |
| 5 | fixture | `src/tests` citer only | **stays**, `.gitignore` allowlist comment names the citer |

Driver-volume mapping: `vol_1_foundations` → `manuscript/vol_1_foundations/`, `vol_4_engineering` → `manuscript/vol_4_engineering/`, **`vol_9_device` ∪ `vol_9_vacuum_datasheet`** → `manuscript/vol_9_vacuum_datasheet/` (FORK-A).

---

#### Re-verification at branch tip (`9e5f1863`) — the map is executed against MEASURED classes, not the Phase-1 index

Phase 1's per-artifact citer map is an **index**, not a verdict. Every artifact was re-scanned at the tip with the four-method census (m1 basename · m1 word-boundary stem · m2 full repo-relative path · m3 glob/dir-context) over all **4 489** tracked text-readable files (of 5 088 tracked), then **every** KB/`.tex` hit was validated line-by-line against a second, independent method (`git grep -F <basename>` scoped to `manuscript/`, plus an extension-less `\includegraphics{<stem>}` scan). The line-by-line pass is load-bearing: it **demoted 25 of 81**.

**Measured split: 19 canonical (classes 1+2) · 62 research-tier (classes 3+4) · 0 fixtures.** Naive four-method scoring had said 43 / 37 / 1. This does **not** reproduce the map's stated 63/18 either way — flagged, not reconciled by bending either side; the per-artifact rule is deterministic and is what the moves execute against. The gap is the stem-hit class:

- **The false-citer class the second method killed (14 artifacts demoted 2 → 4, 1 demoted 5 → 4, 10 demoted 1 → 3).** A KB leaf citing the **driver** `.py` is not citing the artifact: `srs-band-structure.md:22` links `src/scripts/vol_1_foundations/srs_band_survey.py` and nothing else, so `srs_band_survey.png` has **zero** canonical citers. `k4-bloch-dispersion-quartic.md:42` links `k4_bloch_dispersion.py`; the only `.tex` hit for that stem is `12_falsifiable_predictions.tex:164` `\label{sec:k4_bloch_dispersion}` — a cross-reference label, not a citation. Same shape for `node_2domain_nport.json`, `node_circulator_coupling.json`, `oq1_field_to_cavity_phase_coupling.json`.
- **The dir-context false positive.** `manuscript/ave-kb/vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md:24` cites one full path — at the pre-migration location `src/scripts/vol_9_device/_output/` + `im3_vacuum_harmonic_distortion.json` (now `manuscript/vol_9_vacuum_datasheet/results/im3_vacuum_harmonic_distortion.json`). Because that line contains the **directory** and the substring `.json`, a glob-method scan attributes it to all 12 `.json` artifacts in the dir. Only `im3_vacuum_harmonic_distortion.json` is actually cited there.
- **★ The self-referential citation.** `manuscript/ave-kb/common/engine-capability-map.md:477` reads *"inside scratch `_output/` dirs (e.g. `src/scripts/vol_9_device/_output/*.png` cited by the vol-9 datasheet)"*. That wildcard is the **only** KB mention of 9 renders (`electron_s11_gate/unknown`, `s11_denovo_{gate,made,paired,planted}`, the three `vacuum_birefringence_facility_sweep_*.png`). It is not a markdown link, `verify-md-links` does not gate it, and it is not a content citation — it is a sentence **about the policy smell**, inside the paragraph that D15f-3 ratifies rewording away. Letting it fix a destination would be circular: the same commit that used it as evidence deletes it. Scored **not a canonical citer**; those 9 route by their research citers to `research/figures/`.

#### Held, not moved — 6

- **3 · birefringence facility-sweep `.pdf`s** (`vacuum_birefringence_facility_sweep_{signal_vs_field,time_to_5sigma,window_E_vs_g}.pdf`) — the Phase-1 allowlist-contradiction flag. Their `.png` twins are research-cited and move to `research/figures/`; the `.pdf`s are orchestration/src-only and are held per the lane's DO-NOT-TOUCH list. **The migration therefore splits an allowlisted pdf/png pair — disclosed, not smoothed over**: the contradiction is now visible in `.gitignore` (3 surviving `.pdf` lines, 0 `.png`) rather than hidden inside a symmetric block, and it still needs its own ruling.
- **★ 3 · FLAG-DUP — new finding, byte-identical twin already tracked in the destination.** `git hash-object` is equal across each pair:
  - `src/scripts/vol_9_device/_output/a1_spatial_cavity_mode_fft.png` = `manuscript/vol_9_vacuum_datasheet/figures/two_natured/a1_spatial_cavity_mode_fft.png` (`50a3dee9…`)
  - `src/scripts/vol_9_device/_output/two_natured_electron_native_engine.png` = `manuscript/vol_9_vacuum_datasheet/figures/two_natured/two_natured_electron_native_engine.png` (`b60c92af…`)
  - `src/scripts/vol_4_engineering/outputs/optical_caustic_resolution.png` = `assets/sim_outputs/optical_caustic_resolution.png` (`4e4d8747…`)

  In all three cases the destination directory is **already** on the volume's `\graphicspath` (`figures/two_natured/` at `vol_9_vacuum_datasheet/main.tex:7`; `../../assets/sim_outputs/` at `vol_4_engineering/main.tex:7`), so the build **already resolves to the manuscript-side copy** and the `_output` twin is dead weight. Moving it would place two identically-named blobs on one `\graphicspath` — ambiguous resolution, a build hazard a repoint cannot fix. Retiring the twin is a **deletion** on the D15c orphan-DATA axis, which `src/scripts/_archive/MANIFEST.md:131` records as not ruled for this lane. **Held and routed, not resolved.**

**No overlap with the other Phase-1 flag sets.** The FLAG-PAIRED 21 artifacts live under `research/`, `assets/`, `results/` and directly under `src/scripts/vol_1_foundations/` — none under an `_output`/`outputs` dir, so none is in the 81. FLAG-VOL6ANIM is `.gif`/`vol_6` and likewise disjoint. Verified against `src/scripts/_archive/MANIFEST.md:131-200`, not assumed.

#### Fixtures (class 5) measured EMPTY — the rule stands unexercised

Every `src/tests` hit against the 81 resolves to the **driver module**, never the artifact: `src/tests/engine_acceptance/test_p1b_dispersion_gate.py:53` `from scripts.vol_4_engineering import srs_bloch_dispersion as SBD`; `src/tests/test_cr_rotational_curvature_sqrt2.py:34` `from scripts.vol_1_foundations.cosserat_band_structure_two_sublattice import (…)`. No test reads a tracked `_output` artifact as an input fixture, so no `.gitignore` allowlist-with-citer-comment line is written by this phase and `cosserat_band_structure_two_sublattice.json` routes by its research citers to root `results/`.

#### D15f-3 rider — the count that was stale in both directions

`engine-capability-map.md:477` claims *"38 CITED figures currently live inside scratch `_output/` dirs"*. Measured at branch tip: **32** tracked renders (29 `.png` + 3 `.pdf`) under `src/scripts/**/{_output,outputs}`, of which **29 migrate** here and **3** are held. `.gitignore:58` was already corrected to **36** on 2026-08-19 — a different number because it counts allowlist *lines* (29 under `src/scripts/` + 7 under `src/tests/outputs/`), not renders. Both are reconciled to measured truth in the batch that touches them, and the paragraph is reworded to the ratified past-tense policy note.

#### Execution shape

Five link-coupled commits, one per batch, so a broken batch bisects: **vol_1** (2) · **vol_4** (5) · **vol_9-family** (9) · **research renders** (15) · **research data** (44), then a policy-reconciliation commit for `.gitignore` + `engine-capability-map.md` + the `\graphicspath` retirement. Per batch: full citer inventory → `git mv` + every citer repointed in the same commit → allowlist lines retired in the same commit → `make verify-md-links` + `make verify-kb-metadata` green → generating driver's write path updated `_output/` → new home.
