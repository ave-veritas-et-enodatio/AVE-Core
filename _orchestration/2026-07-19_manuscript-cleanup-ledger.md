# Manuscript (TeX Volumes) Documentation Cleanup — Ledger (2026-07-19)

**Lane:** manuscript / tex-volumes cleanup (implementer). **Scope:** `manuscript/vol_0…vol_9`, `frontmatter`, `backmatter`, `common`, `common_equations`, `structure`, `bibliography.bib`, `predictions.yaml`. **OUT of scope (sibling lanes):** `manuscript/ave-kb/` (KB lane), `_orchestration/` except this ledger, `research/`, `src/`.
**Branch:** `docs/manuscript-cleanup-2026-07-19` off `origin/main` `1be045a1`. **Worktree-isolated.**
**Windows:** CLASS-1 mechanical = all-time; CLASS-2 honesty-lag = `2026-07-01 → 2026-07-19` (the 07-01 full-corpus sweep cleared prior debt).

## Method (verify-before-cite two-method on every finding)
- **Integrity scan (grep + read, never arithmetic offsets):** a Python crawler over 209 in-scope tex files collected every `\cite`-family key, `\label`, `\ref/\eqref/\autoref/\cref`, `\xvref`, and `\kbleaf{…}` arg (tex comments stripped). Cross-checked bib keys with a second ripgrep pass.
- **`\kbleaf` path resolution** with suffix-stripping (`:line`, `:line-range`, `::function`) and multi-prefix resolution (`''`, `manuscript/`, `manuscript/ave-kb/`, `research/`, `src/`, `_orchestration/`), plus directory + basename indices of the whole checkout.
- **Second method on the load-bearing zeros:** the repo's own `manuscript/ave-kb/tools/verify-md-links.py` (which DOES crawl `manuscript/**/*.tex` via `iter_tex_files` and checks `\kbleaf` targets) was run — result `kbleaf: 1066 cites checked · gating: 0 · waived: 1`, EXIT 0. My independent scan and the repo checker converge (exactly 1 genuinely-dead kbleaf, and it is the pre-adjudicated waiver).
- **CLASS-2 ground truth** read verbatim at HEAD: `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md`, `research/2026-07-19_f6-thermal-floor-arm_result.md`, `research/2026-07-19_yield-fork-discriminators_result.md`, `research/2026-07-19_noise-floor-arrow-walk_RECORD.md`, `manuscript/ave-kb/common/retention-transition-split.md`, `_orchestration/2026-07-10_rulings-docket.md` (RULINGS 19–22, ENTRIES 16–22), `manuscript/vol_9…/17_engine_requirements.tex` vs `engine-capability-map.md`.
- **Rule-12 idiom** matched to the in-corpus pattern: `% 🔴 …` tex comment banner + `\noindent\textbf{Scope …}` in-text dated note, original body preserved verbatim beneath (KEEP-BOTH). Verified against the three deep-space demotion banners already on main.

---

## CLASS 1 — MECHANICAL HYGIENE

**Headline: the compiled manuscript is mechanically clean. No fixes required in compiled content.** Prior sweeps + the two sibling lanes kept hygiene tight; the repo's own tex-kbleaf checker is green.

| Check | Result |
|---|---|
| Dead `\cite` keys vs `bibliography.bib` (41 keys, 29 used) | **0** (cross-checked two methods) |
| Dead `\ref/\eqref/\cref` targets vs `\label` set (1280 labels, 335 targets) | **1**, and it is in an **UNCOMPILED** orphan file (ledgered below) |
| Dead `\kbleaf` pointers (420 distinct args, 1066 cites) | **1**, already **WAIVED report-don't-fix** by `verify-md-links.py` (ledgered below) |
| Duplicate `\label` | **7**, all **cross-document / uncompiled** — benign for the build (ledgered below) |
| `\xvref` cross-volume labels unresolved anywhere | 0 |
| `make verify-md-links` (tex + md) | **green**, gating 0, waived 1, EXIT 0 |

### C1-a — dead `\ref{sec:dielectric_yield}` in an UNCOMPILED orphan (LEDGER, not fixed)
- Site: `manuscript/backmatter/01_appendices.tex:73` — `\ref{sec:dielectric_yield}`; no such `\label` exists (nearest is `sec:dielectric_rupture`, defined in `vol_1/…/02_macroscopic_moduli.tex:51` and `vol_3/…/03_macroscopic_relativity.tex:167`).
- **Why not fixed:** `01_appendices.tex` is **not `\input` by any `main.tex`** — every volume inputs `01_appendices_lean.tex` instead. The dead ref renders in no PDF. Whether `01_appendices.tex` should be repaired, retired, or deleted is a judgment call above mechanical-typo scope (and the file may be dead weight to be removed by a different pass). Routed to auditor/Grant.

### C1-b — dead `\kbleaf{p2.9b\_goldstone\_proof.md}` — already WAIVED (LEDGER, do-not-fix)
- Site: `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:370` (the neutrino-mixing four-lemma Goldstone proof).
- This exact pair is in the KB checker's `WAIVED_KBLEAF` frozenset (`manuscript/ave-kb/tools/verify-md-links.py:364-372`) with the adjudication: *"p2.9b_goldstone_proof.md never existed in tracked history (it named a gitignored session-handoff-era artifact); the four-lemma Goldstone derivation needs a canonical tracked anchor before this cite can be repointed."* Report-don't-fix; the correct canonical target is an open judgment call (candidate content-home: `ave-kb/vol3/applied-physics/ch07-stellar-interiors/neutrino-flavor-mixing.md`, unverified). **Out of my lane to repoint** (the waiver lives in the KB tools + the target is a judgment call). Surfaced for the auditor.

### C1-c — duplicate `\label` (7) — all benign (LEDGER, verified-benign)
All 7 are cross-document (different volumes compiled as separate PDFs) or involve `backmatter/01_appendices.tex` / `backmatter/02_full_derivation_chain.tex`, **neither of which is `\input` by any `main.tex`**. LaTeX labels are document-scoped, so none collide in any actual build:
- `app:translation_matrix` — `01_appendices.tex` (uncompiled) vs `01_appendices_lean.tex` (compiled). No collision.
- `eq:T_EM`, `eq:delta_th`, `eq:me_unknot`, `eq:xi_topo` — `backmatter/02_full_derivation_chain.tex` (uncompiled) vs vol_2/vol_3/vol_5 chapters. No collision.
- `fig:casimir_superconductor` — vol_3 ch18 vs vol_4 ch10 (separate PDFs). No collision.
- `sec:dielectric_rupture` — vol_1 ch02 vs vol_3 ch03 (separate PDFs; vol_3 imports vol_1 aux via xr-hyper, but xr prefixes external labels, so no local clash). No collision.

---

## CLASS 2 — HONESTY-LAG / OVERCLAIM DRIFT (window 2026-07-01 → 07-19)

### C2-HANDLED — the deep-space demotion (#733) already propagated to all three tex sites (verified, NO drift)
The brief flagged three candidate sites as possibly missing the #733 Rule-12 demotion banners. **All three carry correct, dated Rule-12 KEEP-BOTH banners on main** (verified verbatim at HEAD):
- `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:245-246` — asteroid-belt/Oort resistive-stall DEMOTED; original preserved `:248-254`. ✅
- `vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:227-228` — "Lunar Inductive Joule Heating" `P_topo≈1.04` TW DEMOTED; resultbox + figure preserved `:236-247`. ✅
- `vol_4_engineering/chapters/11_experimental_falsification.tex:358` — Protocol-10 boundary-trapping energy-shedding-drag DEMOTED + flipped into a KEEP-BOTH discriminator. ✅

### C2-FIX-1 — vol_4 vacuum-memristor banks the DISSIPATIVE branch of the OPEN yield fork (FIXED, KEEP-BOTH caveat)
See "Fix log" below. Site: `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:336-355`.

### C2-FLAG-1 — internal contradiction: WHERE the near-yield loop loss maximises (FLAG-DON'T-FIX, routed to Grant)
Three corpus statements disagree about the drive-frequency dependence of the near-yield hysteresis loss:
- **`vol_4/…/01_vacuum_circuit_analysis.tex:355` (verbatim):** *"At drive frequencies $f \gg 1/\tau_{relax} \approx 7.8 \times 10^{20}$ Hz, the vacuum responds too slowly to yield and behaves as a purely elastic (linear) medium. At $f \ll 1/\tau_{relax}$, complete yield and recovery occur within each cycle, producing **maximum hysteresis loss**."*
- **`backmatter/06_spice_verification_manual.tex:146-148` (verbatim):** *"At any practical SPICE simulation frequency ($f \ll 7.8 \times 10^{20}$~Hz), the lattice responds purely elastically---the hysteresis loop has **zero enclosed area**."*
- **Ground truth `research/2026-07-19_yield-fork-discriminators_result.md` (Leg B):** loop area `= ℓ_node²·m_e c²·f(ωτ)`, a K4-nonlinear Debye shape **peaking at `ωτ≈0.9`** (window `[0.85,0.95]`); the `(r,S)`-plane loop-area peak is "pinned at `ωτ≈1.00` across the entire drive family."
- **The tension:** vol_4 says the same `f ≪ 1/τ_relax` regime is *maximum loss*; the SPICE manual says it is *zero-area / elastic*; #735 measures the loop-area peak at `ωτ≈0.9–1.0` (`fτ ~ 1`), i.e. loss maximises at `fτ~1`, not `fτ≪1`. Reconciling this is substrate physics (Debye/relaxation loss-location) — Grant's call. **Surfaced, not resolved.** (A disclosed pointer to this tension is embedded in the C2-FIX-1 caveat per flag-don't-fix; the resolution is not written into either site.)

### C2-FLAG-2 — vol_9 ch5 thixotropy cite is honestly hedged but predates the #735 Leg-A outcome (LEDGER, judgment)
- Site: `vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex:599` (verbatim, abridged): *"**Open (not asserted):** Whether the bulk-mode amplitude-limit asymmetry … produces a relaxation-time asymmetry `τ_bulk,sat ≠ τ_bulk,desat` is unresolved pending experimental confirmation; the datasheet records the structure but asserts no non-zero value (`research/2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md`)."*
- **Drift class:** NOT an overclaim (the line is carefully hedged "not asserted / asserts no non-zero value"). The lag is a **missing citation of the prereg's own OUTCOME**: `#735` Leg A returned **verdict B** — the canonical kernel carries **no genuine `sign(dr/dt)` memory** and the two-τ thixotropic-rectifier sub-branch is **excluded by derivation** (`research/2026-07-19_yield-fork-discriminators_result.md` §3). The line frames the sat/desat asymmetry as "unresolved pending **experimental** confirmation," whereas a **derivation-level** result has since narrowed it (any surviving asymmetry lives only in the second-order-reactive Flag-F branch, not "pending experiment").
- **Why LEDGER not FIX:** whether the `τ_sat ≠ τ_desat` amplitude-asymmetry axis is the *same* object as Leg-A's `sign(dr/dt)` two-τ sub-branch, and exactly what remains open (the Flag-F second-order-reactive route), is a physics mapping that touches the still-OPEN fork. Per "when in doubt, ledger." Routed to Grant/auditor. Suggested (non-applied) update: append to the cite "— the two-τ thixotropic-rectifier sub-branch of this prereg was subsequently excluded by derivation (#735 Leg A verdict B); any surviving asymmetry is the open Flag-F second-order-reactive branch, not pending experiment."

### C2-CONSISTENT — checked, NOT drift (verified against merged state)
- **`vol_9…/17_engine_requirements.tex`** (ground-up acceptance arc) — accurate: `:74` "L0–L2 … pass, establishing the engine as a valid medium; they force zero chords — the chords … live at the **unbuilt** L3–L5 rungs"; `:97-116` L3 "**posited** mass-cage" section is rigorously hedged (consistency-class, "does not show it self-forming," `Q_ringdown≈30.8` NOT 137, "no dimensionful electron VALUE is a cage output"). Matches `engine-capability-map.md` §8c and the merged state.
- **`vol_3…/11_thermodynamics_and_entropy.tex:43-68`** ("The Arrow of Time") — derives the arrow from **geometric mode-spreading** (spherical FDTD irreversibility, reconvergence probability ≈ 0). This is the **licensed counting arrow** (`retention-transition-split.md:31-36`: "mode-count or a click, never a valve"), consistent with the F6 result leaving the counting/mode-spread arrow OPEN. Predates the window; not contradicted.
- **F6 noise-floor arrow** — **no** manuscript passage asserts an arrow-of-time-from-noise-floor result, the F6 meter as invalid, or the counting arrow as decided. All `noise floor` hits are legitimate Johnson-Nyquist / `kT/C` usages (vol_1 ch03 ZPE, vol_4 ch17 boundary, vol_4 ch10 decoherence). The F6 arm's STRONG floor-arrow hypothesis was excluded ~5σ + structurally inexpressible (`research/2026-07-19_f6-thermal-floor-arm_result.md`); nothing propagated to the manuscript. Clean.
- **`vol_3…/03_macroscopic_relativity.tex:163`** "positive bulk resistance" = positive **bulk modulus** (`K_vac ≡ 2G_vac`, stiffness/resistance-to-compression), a reactive elastic property — **not** a dissipative `Re(Z)`. Not an Ax3-tension site. (Loose EE wording, pre-window; noted, not a honesty-lag.)
- **`predictions.yaml`** — no entries reference the deep-space stall, lunar Joule, yield fork, memristor loop, or F6 arrow; those arcs never minted prediction entries, so no status flags are owed here.

---

## NOT-SWEPT (honest disclosure)
- **Full 8-volume PDF build** was not exhaustively diffed page-by-page; integrity was verified by (a) the grep crawler + (b) `verify-md-links.py` (tex-covering) + (c) targeted compile of the edited volume (see Fix log). A cover-to-cover prose re-read for pre-07-01 overclaims is out of window and was not done.
- **KB leaves (`ave-kb/`)** were read for ground truth only, never edited (sibling lane owns them). Any KB-side lockstep for C2-FIX-1 / the flags is the KB lane's to land.
- **Bare-filename / KB-relative `\kbleaf` house-style cites** (≈190) resolve by basename but a few are basename-ambiguous (`claim-quality.md`, `translation-circuit.md`, `index.md` resolve to multiple files). Not dead; disambiguation is a house-style question, not mechanical hygiene — not swept.
- **Cross-repo `\kbleaf` / md links** (AVE-Propulsion, AVE-PONDER, AVE-VirtualMedia, AVE-QED, AVE-HOPF) are inter-repo warn-class and unresolvable in this checkout by design — not touched.
- **Pre-07-01 honesty debt** is by-charter out of window (cleared by the 07-01 sweep); only 07-01→07-19 arcs were chased.

---

## Fix log
_(populated by the fix commit)_
