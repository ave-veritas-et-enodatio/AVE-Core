# Manuscript Pending Changes

Mirrors `manuscript/vol_*/chapters/` layout. Each pending change for a chapter sits under its chapter heading; if multiple research docs converge on the same chapter or section, their entries cluster together. Empty headings are placeholders — the file IS the index.

**Entry schema:**

```
- **[E-NNN] <short concept title>**
  - **Sources:** doc_NN §X.Y (`<sha>`, YYYY-MM-DD); doc_MM §A.B (`<sha>`, YYYY-MM-DD)
  - **Action:** <what specifically changes>
  - **Status:** queued | in-review | applied (`<sha>`)
  - **Cross-refs:** E-NNN, E-MMM
```

`E-NNN` IDs are monotonic and shared across `manuscript_pending.md` and `engine_pending.md`. Next free ID is recorded at the bottom of this file.

KB leaves at `manuscript/ave-kb/vol*/` are tracked alongside their parent chapter when a change must propagate to both.

---

## Vol 0 — Engineering Compendium

### Ch 1 — Theoretical Stress Tests (`01_theoretical_stress_tests.tex`)
### Ch 2 — Analytical Summaries (`02_analytical_summaries.tex`)
### Ch 3 — Computational Graph (`03_computational_graph.tex`)
### Ch 4 — DCVE (`04_dcve.tex`)

## Vol 1 — Foundations

### Ch 0 — Intro (`00_intro.tex`)
### Ch 1 — Fundamental Axioms (`01_fundamental_axioms.tex`)

- **[E-046] F1 — Cosserat sector is natively massive via `m² = 4·G_c/I_ω` (not 2·G_c/I_ω)**
  - **Sources:** [doc 41_ §2-§3:L84-L165](../L3_electron_soliton/41_cosserat_time_domain_validation.md#L84) (`f99b3b3`, 2026-04-22); [S_GATES_OPEN.md F1 + F4](../L3_electron_soliton/S_GATES_OPEN.md)
  - **Action:** Phase I time-domain validation of Cosserat solver established that the rotational mass-gap is `m² = 4·G_c/I_ω`, NOT `2·G_c/I_ω` (factor-of-2 correction from initial derivation). This is a load-bearing engine fact ("the Cosserat sector is natively massive via G_c") that currently appears only in research doc 41_, not in Vol 1 Ch 1 or Ch 8 prose. F4 in S_GATES_OPEN.md flags this as a manuscript update. Add a Vol 1 Ch 1 §sec:axiom_4 (or similar) note explaining the rotational mass-gap origin and its factor-of-4 form per the validated Verlet integrator.
  - **Status:** queued
  - **Cross-refs:** E-045

- **[E-013] Ax 4 restated as "flux-density ceiling per lattice cell" — pedagogical reframe**
  - **Sources:** [doc 66_ §6:L115-L127](../L3_electron_soliton/66_single_electron_first_pivot.md#L115) (`a53ce1c`, 2026-04-25)
  - **Action:** wherever Ax 4 is presented (currently constitutive form `C_eff(Δφ) = C_0/√(1−(Δφ/α)²)` per [01_fundamental_axioms.tex:68-74](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L68-L74)), add a parallel "flux-density ceiling" framing: A²=1 means every bond at maximum Φ_link, no more flux lines fit, topology must rearrange. Both framings are physically identical (constitutive singularity = elastic response diverges; flux-density ceiling = flux counting maxes out). The ceiling framing makes Ax 4 countable and engineering-intuitive. Engine math unchanged. (Flag 66-G — defer to Vol 1 revision pass.)
  - **Status:** queued
  - **Cross-refs:** —

- **[E-094] Substrate-native vocabulary discipline — AVE-QED App G propagation to AVE-Core**
  - **Sources:** [AVE-QED `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex`](../../../AVE-QED/manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex) (`ce34645`, 2026-05-14); [AVE-QED `docs/glossary.md` §5m](../../../AVE-QED/docs/glossary.md) (`ce34645`, 2026-05-14); [AVE-QED `docs/analysis/2026-05-14_three_substrate_invariants_matrix.md`](../../../AVE-QED/docs/analysis/2026-05-14_three_substrate_invariants_matrix.md) (`c30c351`, 2026-05-14); [doc 109_ §13-§15 boundary-envelope reformulation](../L3_electron_soliton/109_elastic_substrate_finite_strain_investigation.md) (`ad90c87`, 2026-05-14, Grant-confirmed canonical)
  - **Action:** AVE-QED canonized the substrate-native vocabulary in App G (~340 lines) + glossary §5m. The three substrate invariants $\mathcal{M}$ (integrated strain integral), $\mathcal{Q}$ (boundary linking number), $\mathcal{J}$ (boundary winding number) are the canonical names (Grant-locked 2026-05-14 evening, Q1 closure). The substrate-observability rule (substrate observes boundary, not interior) is canonical (doc 109 §13 Grant-confirmed). Propagation needed to AVE-Core: **(1) Vol 1 Ch 1** (Axioms) add substrate-vocabulary box near Ax 1 statement; **(2) Vol 1 Ch 4** (Continuum EM) reference App G near eq:master_wave; **(3) Vol 2 Ch 1** (Topological Matter) cross-ref at "rest mass is contained reactance" canonical statement L35 with $\mathcal{M} = T_{EM}\,\ell_{\text{node}}$ identity; **(4) Vol 3 Ch 2** (GR) substrate-observability rule cross-reference at L35-43 with $\mathcal{M} \to M_{ADM}$ projection mapping; **(5) Vol 4 Ch 1** extend the existing Rosetta-stone (source for AVE-QED `A_foundations.tex`) to 3-column form (substrate-native / EE / ME); **(6) `docs/glossary.md`** (if exists; else create) mirror AVE-QED §5m; **(7) `src/ave/core/constants.py` module docstring** add cross-reference to App G. ~5-8 hours focused authoring. Mostly additive (no destructive rewrites).
  - **Status:** queued (HIGH PRIORITY — load-bearing for substrate-native discipline going forward)
  - **Cross-refs:** E-085 (Vol 4 Ch 1 Virial sum already canonical), A-026 (substrate-observability rule), A-028 (three substrate invariants); doc 109 §13 (Grant-confirmed canonical)

- **[E-096] Boundary-envelope reformulation — substrate observes boundary not interior (Grant-confirmed canonical)**
  - **Sources:** [doc 109_ §13-§15](../L3_electron_soliton/109_elastic_substrate_finite_strain_investigation.md) (`ad90c87`, 2026-05-14, Grant-confirmed canonical); [doc 92 Nyquist wall reframe](../L3_electron_soliton/92_round_11_vi_v10_finer_sampling_structural.md) (now reframed: measured wrong observable per substrate-observability rule)
  - **Action:** Vol 1 Ch 7 (Regime Map) and Vol 1 Ch 4 (Continuum EM) need the boundary-envelope reformulation as a canonical principle: **the lattice doesn't need to support the smallest flux tube; it needs to support the smallest envelope containing that flux tube.** Doc 92's Nyquist wall ($k = 6.36/\ell_{\text{node}}$ vs K4 Nyquist 0.577) measured an interior observable that is not substrate-visible — the substrate only sees the boundary envelope's three invariants. Same mechanism at BH (Schwarzschild) and electron (horn-torus tube wall): "You can resolve what's in a black hole? Why could you resolve what's in an electron's envelope/boundary?" (Grant 2026-05-14). Reframing un-blocks lattice scale: ℓ_node sets envelope scale (~10⁻¹³ m for electron), not interior eigenmode wavelength (~10⁻¹⁴ m). Engine consequence: subsequent simulations target boundary envelope on the lattice, not interior structure.
  - **Status:** queued (Grant-confirmed canonical — HIGH PRIORITY)
  - **Cross-refs:** E-094 (substrate-vocabulary), A-026 (substrate-observability rule axiom-status)

- **[E-098] Cubic K4 anisotropy at saturation collapse — empirically observable substrate-symmetry**
  - **Sources:** [doc 114_ §1.1 + §1.5](../L3_electron_soliton/114_next_steps_consolidation_plan.md) (`fd19914`, 2026-05-14); [src/scripts/vol_1_foundations/r10_master_equation_v14_anisotropy.py](../../src/scripts/vol_1_foundations/r10_master_equation_v14_anisotropy.py) (commit `160498d`, 2026-05-14); empirical artifact `assets/sim_outputs/v14_collapse_cubic_emergence.png` (gitignored, regenerable)
  - **Action:** Vol 1 Ch 1 (Axioms) or Vol 1 Ch 6 (Universal Operators) — add a brief empirical-observation note: at low-amplitude saturation collapse on Master Equation FDTD, the breathing soliton's collapse is **visibly cubic** (Pearson(V_peak, asphericity) = −0.191; collapse axis/diagonal ratio 1.089 cubic, vs 0.937 spherical at high-phase). The substrate's intrinsic K4 tetrahedral symmetry — which Axiom 1 declares but which past simulations didn't make visually evident — is empirically observable in the FDTD time-domain evolution. Cubic symmetry emerges naturally from the K4 bipartite lattice's 4-port topology. Reframes K4 substrate from "an abstract topological structure" to "a substrate whose intrinsic symmetry is empirically visible in dynamics."
  - **Status:** queued
  - **Cross-refs:** E-095 (Master Equation FDTD engine), E-097 (two-engine architecture)

### Ch 2 — Macroscopic Moduli (`02_macroscopic_moduli.tex`)
### Ch 3 — Quantum and Signal Dynamics (`03_quantum_and_signal_dynamics.tex`)

- **[E-041] "Quantum foam" terminology BANNED — replace with "thermal lattice noise" + cite quantitative σ values from doc 47_**
  - **Sources:** [doc 46_ §C6:L106-L116](../L3_electron_soliton/46_vacuum_engine_scope.md#L106) (`7ab82c0`, 2026-04-22); [doc 47_ §2:L26-L72](../L3_electron_soliton/47_thermal_lattice_noise.md#L26) (`87b502c`, 2026-04-22)
  - **Action:** Vol 1 Ch 3 §Quantum Foam (~lines 188-198) currently provides QUALITATIVE framing ("quantum foam is baseline electrical noise"). Doc 47_ provides QUANTITATIVE σ_V, σ_ω, σ_ω̇, σ_u, σ_u̇ from classical Maxwell-Boltzmann equipartition on the K4 lattice. **Doc 46_ §C6 explicitly bans "quantum foam" terminology in AVE-native physics** — it imports a QFT framework AVE rejects. Replace with "thermal lattice noise" (or "Maxwell-Boltzmann lattice equipartition") and add cross-ref to doc 47_ for the quantitative values + T_V-rupt = 3.44 MK threshold (E-042 captures the Vol 4 Ch 1 side). Subsumes existing queue [20].
  - **Status:** queued
  - **Cross-refs:** E-042; supersedes existing queue entry [20] in DOCUMENTATION_UPDATES_QUEUE.md
### Ch 4 — Continuum Electrodynamics (`04_continuum_electrodynamics.tex`)

- **[E-048] Photon identification — K4-TLM photon for +x propagation is linear T₂ mode, NOT circular**
  - **Sources:** [doc 30_](../L3_electron_soliton/30_photon_identification.md) (`a9853d9`, 2026-04-22); [doc 40_ §2.2:L79-L107](../L3_electron_soliton/40_modeling_roadmap.md#L79) (`ed6ab8e`, 2026-04-22)
  - **Action:** Vol 1 Ch 4 (continuum EM) and any Ch 6 universal-operators-photon discussion currently lacks an explicit identification of the K4-TLM photon mode. Per doc 30_: the photon for +x̂ propagation is the **linear T₂ mode T_a** (port amplitudes (+1,-1,+1,-1)), NOT a circular mode. Has direct implications for engine source design (`PlaneSource`, `AutoresonantCWSource`). Add a manuscript box identifying the photon's K4-TLM port-amplitude pattern + the electron-photon duality mechanism (doc 30_ §3-§5). Cross-ref to engine [`vacuum_engine.py photon_propagation` source classes](../../src/ave/topological/vacuum_engine.py).
  - **Status:** queued
  - **Cross-refs:** E-045

- **[E-095] Master Equation FDTD engine — canonical bound-state regime engine, v14 Mode I PASS empirical**
  - **Sources:** [doc 111_](../L3_electron_soliton/111_master_equation_audit_and_engine_gap.md) (`3815158`, 2026-05-14, audit identifying c_eff(V) gap in K4-TLM-only architecture); [doc 112_](../L3_electron_soliton/112_master_equation_fdtd_first_iteration.md) (`6a40610`, 2026-05-14, Path B first iteration); [doc 113_ §0-§4](../L3_electron_soliton/113_v14_closure_master_equation_fdtd_mode_I.md) (`345d55d`, 2026-05-14, Mode I PASS canonical closure on breathing-soliton criterion); [Vol 1 Ch 4 eq:master_wave:L73](../../manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex#L73) (canonical equation); [src/ave/core/master_equation_fdtd.py](../../src/ave/core/master_equation_fdtd.py) (canonical engine module)
  - **Action:** Vol 1 Ch 4's canonical Master Equation $\nabla^2 V - \mu_0\varepsilon_0 \sqrt{1-(V/V_{\text{yield}})^2}\,\partial_t^2 V = 0$ (eq:master_wave, line 73) now has a canonical FDTD engine in `src/ave/core/master_equation_fdtd.py`. Add a manuscript reference near eq:master_wave: (a) cite the engine module as the canonical numerical realization; (b) cite doc 113_ as the empirical v14 Mode I PASS validation (breathing-soliton on K4 substrate, 4/4 on breathing-soliton-appropriate criterion); (c) note the two-engine architecture (see E-097). Engine implements leapfrog on eq:master_wave with $c_{\text{eff}}(V) = c_0 \cdot (1-A^2)^{-1/4}$ and saturation kernel $S(A) = \sqrt{1-A^2}$ (Axiom 4 canonical form). PML radiation absorber + native-units mode + SI-units mode. ~9.7KB module, currently passing smoke tests + import-test on merged research branch.
  - **Status:** queued
  - **Cross-refs:** E-097 (two-engine architecture), E-099 (engine-side canonical entry), A-027 (axiom-status entry for two-engine architecture)

### Ch 5 — Universal Spatial Tension (`05_universal_spatial_tension.tex`)
### Ch 6 — Universal Operators (`06_universal_operators.tex`)

- **[E-045] K4-TLM cardinal-axis signal speed is `c·√2`, not `c` — engine geometric fact**
  - **Sources:** [doc 40_ §2.1:L65-L78](../L3_electron_soliton/40_modeling_roadmap.md#L65) (`ed6ab8e`, 2026-04-22); engine constant `dt = ℓ_node/(c·√2)` per [k4_tlm.py](../../src/ave/core/k4_tlm.py)
  - **Action:** when Vol 1 Ch 6 (or Ch 7 regime map) discusses the K4-TLM dispersion relation, add a footnote/note: cardinal-axis signal speed in K4-TLM is `c·√2`, not `c`. The factor √2 reflects the tetrahedral port-vector geometry (each step propagates one bond-length per timestep, but the bond projects onto cardinal x at length 1/√2 per port). This is engine-fundamental: CFL timestep is `dt = ℓ_node/(c·√2)`. Easy reader-misread without the note. Connects to E-046 (mass-gap correction also tied to natural-units scaling).
  - **Status:** queued
  - **Cross-refs:** E-046

- **[E-097] Two-engine architecture canonical — K4-TLM (sub-saturation bench) + Master Equation FDTD (bound-state)**
  - **Sources:** [doc 111_ §3-§4](../L3_electron_soliton/111_master_equation_audit_and_engine_gap.md) (`3815158`, 2026-05-14, audit identifying c_eff(V) gap in K4-TLM); [doc 113_ §3.2](../L3_electron_soliton/113_v14_closure_master_equation_fdtd_mode_I.md) (`345d55d`, 2026-05-14, two-engine architecture canonical statement); [src/ave/core/k4_tlm.py](../../src/ave/core/k4_tlm.py) (K4-TLM canonical engine — sub-saturation bench regime); [src/ave/core/master_equation_fdtd.py](../../src/ave/core/master_equation_fdtd.py) (Master Equation FDTD canonical engine — bound-state regime)
  - **Action:** add a "regime-map" subsection (Vol 1 Ch 6 universal operators or Vol 1 Ch 7 regime map) declaring the canonical two-engine architecture: **K4-TLM hosts the sub-saturation bench regime** (linear response, weakly nonlinear up to V_yield onset, op3_bond_reflection for memristive Op14 dynamics); **Master Equation FDTD hosts the bound-state regime** (A → 1 saturation, c_eff(V) modulation, breathing soliton solutions). Both are Axiom-1/2/3/4 compliant; they cover different operating regimes. K4-TLM is the bench-validated engine (D10 IM3 cubic V³, slope 2.956 vs target 3.0 — AVE-Bench-VM `0599a10`). Master Equation FDTD is the bound-state engine (v14 Mode I PASS on breathing-soliton criterion, 4/4 — doc 113). The pre-2026-05-14 architecture (K4-TLM + Cosserat coupling for everything) is superseded; Cosserat coupling on Master Equation FDTD is deferred (doc 113 §5.4) but not load-bearing.
  - **Status:** queued
  - **Cross-refs:** E-095 (Master Eq FDTD canonical engine), E-099 (engine-side canonical entry), A-027 (axiom-status entry for two-engine architecture)

### Ch 7 — Regime Map (`07_regime_map.tex`)

- **[E-043] V_YIELD = 1 in lattice natural units — explicit annotation**
  - **Sources:** [doc 45_ §3.1:L131-L141](../L3_electron_soliton/45_lattice_impedance_first_principles.md#L131) (`fa89466`, 2026-04-22)
  - **Action:** Vol 1 Ch 7 §domain-catalog (lines 96-217) lists `V_yield = √α·V_SNAP ≈ 43.65 kV` for the EM voltage row but doesn't note that in **lattice natural units** (V_SNAP = 1, ε_yield = 1, etc.) this becomes V_YIELD = √α and the engine's subatomic override (per Vol 4 Ch 1:711 — see E-030) sets it to V_YIELD ≡ V_SNAP = 1. Add an explicit "in natural units" column to the domain-catalog table OR a footnote at the EM row clarifying the engine-side numerical values. Connects to E-030.
  - **Status:** queued
  - **Cross-refs:** E-030, C-002
### Ch 8 — Zero-Parameter Closure: α from the Golden Torus (`08_alpha_golden_torus.tex` + KB `vol1/ch8-alpha-golden-torus.md`)

- **[E-057] Corpus Golden Torus PARAMETERS empirically falsified at coupled-engine scale; framework qualitatively supported (gated on Move 6 outcome)**
  - **Sources:** [doc 74_ §9 joint R7.1+R7.2 closure](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L322) (`d3adcc2`, 2026-04-26); [doc 74_ §10 envelope-closing tests](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L416) (`39f656a`, 2026-04-26); [doc 74_ §11 Move 5 result](../L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md#L501) (`c772211`, 2026-04-26)
  - **Action:** Vol 1 Ch 8 + KB ch8-alpha-golden-torus.md presents the Golden Torus geometry (R = φ/2, r = (φ−1)/2 in canonical units; R_anchor = 10 + r = R/φ² ≈ 3.82 at engine N=32) and peak |ω| = 0.3π as zero-parameter-closure target. Round 7+8 empirical work falsifies these specific PARAMETERS at the engine: 7 tests across V-block, Cos-block, R7.2 pair injection, Test A c-via-Op10, Test B v2/v3 spatial all returned Mode III at corpus GT. Move 5 finds the engine hosts a self-stable (2,3) orbit at sub-corpus parameters (peak |ω| = 0.3044 ≈ 1/3 of corpus, orbit migrates off corpus shell). **The corpus framework (electron = self-trapped (2,3) soliton) survives qualitatively; specific (R, r, |ω|) values do not.** Round 8 Move 6 (E-062) is load-bearing: if R'/r' ≈ φ² at non-corpus absolute scale, recalibrate R_anchor + the Vol 1 Ch 8 derivation chain still works at qualitative level (bounded edit). If R'/r' ≠ φ², the φ² ratio is also wrong → deeper Vol 1 Ch 8 rework + hardens A-001 α-as-calibration framing. **Defer this entry's actual edits until Move 6 outcome lands** — current state is a manuscript-side flag, not a queued edit.
  - **Status:** adjudication-open (gated on Move 6)
  - **Conflicts:** corpus says Golden Torus geometry IS the (2,3) bound state; engine says NOT at those parameters. See A-006.
  - **Cross-refs:** E-001, E-047, E-049, E-062 (Move 6 driver — load-bearing); **A-006 (canonical entry for engine-empirical-vs-corpus-claim adjudication)**, **A-001 (α-as-calibration — closely connected pending Move 6)**

- **[E-047] α-as-calibration framing — chapter title + intro need honest reframe — PARTIALLY ADVANCED via homologation P1**

  **Update 2026-04-27:** the axiom-homologation commit `75d1fde` (P1) added an explicit note to `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2: *"ℓ_node, α, G are calibration constants per Vol 1 Ch 1:14-21, NOT primitive axioms."* This is a partial validation of E-047's framing — the corpus now (in the KB header) acknowledges α-as-calibration. Vol 1 Ch 8 chapter title "Zero-Parameter Closure" + intro + README headline + LIVING_REFERENCE axioms table STILL claim α is axiom-derived. E-047 action remains queued; the partial advancement makes the residual reframe less radical and more locally bounded.
  - **Sources:** [doc 39_ §1-§3:L1-L80](../L3_electron_soliton/39_alpha_is_calibration.md) (`a9853d9`, 2026-04-22); [doc 35_ §10](../L3_electron_soliton/35_halfcover_derivation_audit.md) (`a9853d9`, 2026-04-22) [historical]; [doc 36_ §3.1](../L3_electron_soliton/36_pathB_trefoil_z2_investigation.md) (`a9853d9`, 2026-04-22) [partial closure]; `manuscript/backmatter/02_full_derivation_chain.tex:629-737`
  - **Action:** Vol 1 Ch 8 title "Zero-Parameter Closure" + intro + backmatter Layer 7→8 + README headline + LIVING_REFERENCE axioms table all currently claim α is axiom-derived. Per A-001 audit: half-cover argument requires SU(2) projective postulate at the load-bearing step (R·r = 1/4 from spin-½ Clifford-torus area match). Path B (doc 36_) showed (2,3) topology does NOT force antipodal identification. Honest reframe: AVE is a **one-dimensionless-parameter theory** (α), not zero-parameter. Reduction from SM's 19+ free parameters is still significant. Recipe `4π³+π²+π+δ_strain` is correct as a calibration recipe; framing as "derived" is overstated. **Defer pending decision** on whether to (a) revise framing now or (b) keep pursuing the half-cover derivation gap (currently tabled per existing queue [4]).
  - **Status:** queued
  - **Conflicts:** corpus says "derived"; audit says "calibration"; see A-001 for the framework-level adjudication record.
  - **Cross-refs:** E-001; **A-001 (canonical entry for α-as-calibration framework status)**

- **[E-001] A30 — Cosserat-energy ↔ S₁₁ co-location at Golden Torus FALSIFIED at coupled-engine scale**
  - **Sources:** [doc 67_ §22](../L3_electron_soliton/67_lc_coupling_reciprocity_audit.md) (`3fede52`, 2026-04-25); [doc 70_ §1](../L3_electron_soliton/70_phase5_resume_methodology.md) (`e1f6eac`, 2026-04-25)
  - **Action:** add footnote (or KB-leaf addendum) stating that the analytic Golden-Torus result $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ is preserved, but the implicit corpus claim that "Cosserat-energy descent and $|S_{11}|^2$ descent co-locate at the Golden Torus" was empirically falsified at coupled-engine scale by F17-K v2-v2: dual descent under saturation pin gave R/r = 3.40 (energy) vs R/r = 1.03 ($S_{11}$), neither at $\varphi^2 = 2.62$. Topology is encoded by ansatz initialization (doc 34_ X4 pattern), not by dynamical descent. Doc 03_ §4.3 anchors: "$R\cdot r = 1/4$ is topologically quantized, NOT dynamically derived."
  - **Status:** queued
  - **Cross-refs:** E-006; **A-001 (α-as-calibration framework status)**

- **[E-004] Cross-ref AVE-Protein Ch 3 S₁₁-fold template as the sibling-repo precedent**
  - **Sources:** [doc 68_ §4](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25)
  - **Action:** add a citation (footnote or "see also" line) pointing to `AVE-Protein/manuscript/vol_protein/chapters/03_deterministic_protein_folding.tex:429-434` ("All eight forces are replaced with a single objective function: $\mathcal{L} = |S_{11}|^2$") and `:805` ("native fold minimises $|S_{11}|^2$"). The single-electron eigenmode-finder methodology mirrors the protein-fold template; the cross-ref makes this explicit.
  - **Status:** queued
  - **Cross-refs:** E-003

## Vol 2 — Subatomic

### Ch 1 — Topological Matter (`01_topological_matter.tex`)
### Ch 2 — Baryon Sector (`02_baryon_sector.tex`)
### Ch 3 — Neutrino Sector (`03_neutrino_sector.tex`)
### Ch 4 — Quantum Spin (`04_quantum_spin.tex`)
### Ch 5 — Electroweak Gauge Theory (`05_electroweak_gauge_theory.tex`)
### Ch 6 — Electroweak and Higgs (`06_electroweak_and_higgs.tex`)
### Ch 7 — Quantum Mechanics and Orbitals (`07_quantum_mechanics_and_orbitals.tex`)

- **[E-014] KVL/Ampère mapping — pedagogical gap, ∇·B=0 → KCL is present, ∇×B = μJ → KVL is missing**
  - **Sources:** [doc 66_ §2:L41-L52](../L3_electron_soliton/66_single_electron_first_pivot.md#L41) (`a53ce1c`, 2026-04-25); [Vol 2 Ch 7:1316-1358](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex#L1316-L1358)
  - **Action:** Vol 2 Ch 7 currently maps ∇·B = 0 to Kirchhoff's Current Law on the discrete lattice's flux graph (every node: flux in = flux out). The dual mapping — ∇×B = μ_0 J expressed as Kirchhoff's Voltage Law on a closed loop in the lattice — is absent. Add a parallel paragraph or subsection completing the Maxwell-as-Kirchhoff translation. (Flag 66-C — defer to Vol 2 revision pass.)
  - **Status:** queued
  - **Cross-refs:** —

- **[E-090] KB IE validation leaf — commit-SHA anchoring + adjudication-pending table values**
  - **Sources:** [doc 100 §9.1-§9.10](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md#L147) (`8a3dd82`, 2026-04-30); [doc 100 §10.7-§10.8](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md#L439) (`7cf8243`, 2026-04-30); [`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md)
  - **Action:** Two-part edit pending Grant adjudication. **(1) SHA-anchor footnote** (mandatory regardless of α/β/γ/δ outcome): add footnote after "computed using the engine solver `ionization\_energy\_e2k(Z)`" reading *"Table values generated against `ionization_energy_e2k(Z)` at parent-repo commit `0401388` (2026-04-09)."* This is the first instance of the A-019 SHA-anchor convention; pattern then sweeps across all `manuscript/ave-kb/**/*-validation.md` + Vol 0/Vol 4 numerical-quote files. **(2) Table values** depend on Grant's adjudication: (α) re-run at HEAD post-Q1/Q2/Q3-surgical-fix and update table — manuscript "±2.8%" claim either re-validates or needs prose revision; (β) keep current table values, footnote pin to `0401388`, manuscript prose stands; (γ) ship surgical-fix per Q1/Q2/Q3, re-validate, update or pin per outcome; (δ) bifurcate — atomic-orbital validation references `0401388` cherry-pick path, HEAD continues with extensions. Manuscript "±2.8% maximum error" + Period-2/Period-3 sub-claims hold at `0401388` but not at HEAD; final prose depends on adjudication.
  - **Status:** queued (SHA-anchor footnote unblocked); adjudication-open (table values + prose claims pending Q1/Q2/Q3 + α/β/γ/δ)
  - **Cross-refs:** A-018, A-019, C-003, E-091

- **[E-092] Sweep all manuscript files quoting solver-pinned numerical values for SHA-anchor convention**
  - **Sources:** [doc 100 §9.7](../L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md#L253) (`8a3dd82`, 2026-04-30)
  - **Action:** After E-090 lands the SHA-anchor footnote pattern at the IE table, sweep across `manuscript/ave-kb/**/*-validation.md`, `manuscript/predictions.yaml`, Vol 0 worked examples, Vol 4 Ch 1 derived-value cross-refs, and any other manuscript file that quotes specific numerical values from named engine functions. Apply the same SHA-anchor footnote convention. Without this, A-019 (silent invalidation through solver evolution) remains a systemic exposure.
  - **Status:** queued (blocked on E-090 landing the convention first)
  - **Cross-refs:** A-019, E-090
### Ch 8 — Planck and String Theory (`08_planck_and_string_theory.tex`)
### Ch 9 — Computational Proof (`09_computational_proof.tex`)
### Ch 10 — Open Problems (`10_open_problems.tex`)
### Ch 11 — Standard Model Overdrive (`11_standard_model_overdrive.tex`)
### Ch 12 — Appendix Formal Proofs (`12_appendix_formal_proofs.tex`)
### Ch 12 — The Millennium Prizes (`12_the_millennium_prizes.tex`)

## Vol 3 — Macroscopic

### Ch 1 — Gravity and Yield (`01_gravity_and_yield.tex`)
### Ch 2 — General Relativity and Gravity (`02_general_relativity_and_gravity.tex`)
### Ch 3 — Macroscopic Relativity (`03_macroscopic_relativity.tex`)

- **[E-015] Time = local clock rate from lattice strain — τ_local = n(r)·τ_unstrained**
  - **Sources:** [doc 66_ §17.1:L507-L517](../L3_electron_soliton/66_single_electron_first_pivot.md#L507) (`a53ce1c`, 2026-04-25)
  - **Action:** add an explicit derivation chain in the refractive-index-of-gravity section: τ_local = n(r) · τ_unstrained where n(r) = 1 + 2GM/(c²r). Twice the strain → half the refresh rate. Implicit chain across [Vol 3 Ch 3 c_local = c₀/n(r)](../../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md) + [doc 59_ §1.2 τ_relax = ℓ_node/c](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md). Currently uncited. Companion engine note: τ_relax is global constant; cosmological/strong-gravity work would need spatial n(r) modulation (E-016).
  - **Status:** queued
  - **Cross-refs:** E-016
### Ch 4 — Generative Cosmology (`04_generative_cosmology.tex` + KB `vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md`)

- **[E-102] Cosmic $\mathcal{J}_{\text{cosmic}}$ as the cosmological IC — explicit identification (Grant adjudication 2026-05-15 evening)**
  - **Sources:** **A-031** (`research/L5/axiom_derivation_status.md`, Grant adjudication 2026-05-15 evening); `manuscript/ave-kb/common/trampoline-framework.md` §1.3.7 + §5.6 + §8.2 (canonical "God's Hand" framing + three-route falsifiability); Vol 3 Ch 4 current canonical $G = c^4/(7\xi T_{EM})$; AVE-QED `manuscript/vol_qed_replacement/appendices/F_local_machian_network.tex` (multi-scale Machian network — cosmic row)
  - **Action:** Vol 3 Ch 4 (generative cosmology) currently presents Newton's $G$ as the Machian impedance integral $G = c^4/(7\xi T_{EM})$. Add explicit identification of the cosmic boundary's THIRD invariant: $\mathcal{J}_{\text{cosmic}} = \Omega_{\text{freeze}} \cdot I_{\text{cosmic}}$ is the cosmological initial-data parameter, encoding the freeze-in rotation rate at lattice genesis. The substrate-observability rule applies fractally — we sit inside our cosmic $\Gamma=-1$ boundary; we observe $\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$ from inside; we cannot observe what set them ("God's Hand"). Specifically add: (a) §sec:cosmic_horizon — explicit statement that the cosmic horizon has three integrated observables; (b) §sec:cosmological_origin — universe-as-vortex framing (E-019 MECHANIZED) tying $\mathcal{J}_{\text{cosmic}}$ to the freeze-in vortex; (c) §sec:falsifiability — three-route consistency check ($\alpha$ + $G$ + $\mathcal{J}_{\text{cosmic}}$ must give same $u_0^*$). Cross-ref to trampoline-framework.md §1.3.7 as picture-first reference; cross-ref to A-031 in L5 axiom-derivation-status.
  - **Status:** **APPLIED 2026-05-15** — landed as new §sec:cosmic_J_as_IC + §sec:three_route_falsifiability (Vol 3 Ch 4 between §Black Holes and summarybox); 100+ lines of canonical content covering 3 observables, three-route framework, universe-as-vortex MECHANIZED, God's Hand epistemic horizon; summarybox extended with 3 new bullets capturing the canonical additions
  - **Cross-refs:** A-031 (canonical); A-001 (α-as-calibration, sharpened); A-030 (α + G + $\mathcal{J}$ three-route); E-019 (MECHANIZED, manuscript-side companion); E-103 (Vol 3 Ch 21 same-epistemic-horizon companion); E-094 (App G propagation); E-095 (Master Equation FDTD canonical); cross-repo: AVE-QED App F multi-scale Machian network

- **[E-024] Explicit acknowledgment of AVE's 1970s-Hawking info-loss alignment**
  - **Sources:** [doc 63_ §5:L121-L131, Flag 63-B:L161](../L3_electron_soliton/63_info_loss_stance_reaudit.md#L121) (`740b1a3`, 2026-04-24)
  - **Action:** in KB-ch04 `black-holes-impedance-mismatch.md` (the corpus already says "explicitly sides with Hawking's original assessment"), and in Vol 3 Ch 4 / Vol 3 Ch 11 wherever info-loss is discussed, add an explicit publication-level note: AVE's info-loss stance is the 1970s-Hawking position, AGAINST modern QG consensus (post-Maldacena AdS/CFT, Susskind complementarity, Almheiri-Marolf-Polchinski-Sully firewalls, Maldacena-Susskind ER=EPR, post-2019 entanglement islands + Page-curve resolution). This is a load-bearing empirical commitment — observationally distinguishable in principle. AVE is taking the unpopular-but-specific side; this is a legitimate scientific posture worth honest acknowledgment.
  - **Status:** queued
  - **Cross-refs:** C-001

- **[E-026] KB-ch04 — link entropy-distinction quantification (3-4 distinct entropies)**
  - **Sources:** [doc 62_ §10](../L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md) (`2671a54`, 2026-04-23); [doc 63_ §4.1-4.3](../L3_electron_soliton/63_info_loss_stance_reaudit.md#L94) (`740b1a3`, 2026-04-24); [doc 65_ §6-§9](../L3_electron_soliton/65_flag_62g_discrete_lattice_gamma.md#L156) (`f9b463e`, 2026-04-24)
  - **Action:** KB-ch04 currently states info-loss qualitatively. Add the four-way entropy distinction now established by docs 62/63/65: (a) corpus continuum Ŝ_horizon = 0; (b) corpus + discrete-lattice correction Ŝ_horizon ≈ 8.7·k_B (mass-independent universal constant per doc 65_); (c) doc 61_ A-B interface Ŝ_geometric = A·log(2)/ℓ_node² (vindicated as AVE-native by doc 62_ §10); (d) standard thermodynamic S_BH = A/(4·ℓ_P²) (imported from GR first law, currently NOT axiom-derived in AVE — Flag 62-A). All four measure different physics; ratio Ŝ/S_BH ~ 10⁻⁴⁴ is Machian dilution (NOT a contradiction).
  - **Status:** queued
  - **Cross-refs:** E-022, E-027, C-001

- **[E-017] Genesis-chirality / supercooled-seed crystallization mechanism — Grant's hypothesis, not yet in corpus**
  - **Sources:** [doc 66_ §5:L93-L113](../L3_electron_soliton/66_single_electron_first_pivot.md#L93) (`a53ce1c`, 2026-04-25); [doc 59_ §5.4](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md) (`03cb9d5`, 2026-04-23)
  - **Action:** formalize the lattice-genesis single-seed mechanism. Universe crystallized from one supercooled-plasma seed whose chirality is our observed A-dominance. Subsequent crystallization inherits via coherent wavefront. Universe is one giant single-domain. B-matter lives in pre-genesis plasma or causally-disconnected seed-patches. Replaces SM Sakharov conditions: no CP violation, baryon-number violation, or out-of-equilibrium needed. Open: pre-genesis plasma axiomatics (Flag G — currently outside Ax 1-4). Vol 3 Ch 4 crystallization framework is the natural home. (Flag 66-D.)
  - **Status:** queued
  - **Cross-refs:** E-018, E-019; **A-003 (Ax5 candidate A: pre-genesis plasma axiomatics)**
### Ch 5 — Cosmology Dark Sector (`05_cosmology_dark_sector.tex`)

- **[E-018] Density-vs-saturation cosmological reframing — matter as low-density slipstream pockets**
  - **Sources:** [doc 66_ §17.2:L519-L582](../L3_electron_soliton/66_single_electron_first_pivot.md#L519) (`a53ce1c`, 2026-04-25)
  - **Action:** add cosmological-scale interpretation paragraph: A² = local field-energy density; S = √(1−A²) = "free capacity" / effective density of unfilled lattice substrate. S = 1 → unstrained vacuum (high free-density). S → 0 → fully saturated slipstream (low free-density). Z_eff = Z_0/√S → ∞ as S → 0 matches "empty space carries no waves." **Cosmologically:** matter = low-density slipstream pockets in high-density vacuum (inverted from standard cosmology). Engine has been computing this all along; the relabeling clarifies cosmological-scale interpretation without changing engine code.
  - **Status:** queued
  - **Cross-refs:** E-017, E-019

- **[E-019] Universe-as-vortex cosmology — Grant's macro-scale framing (MECHANIZED 2026-05-15 evening via A-031 cosmic-$\mathcal{J}$ identification)**
  - **Sources:** [doc 66_ §17.3:L584-L596](../L3_electron_soliton/66_single_electron_first_pivot.md#L584) (`a53ce1c`, 2026-04-25); **A-031** (Grant adjudication 2026-05-15 evening — $\Omega_{\text{freeze}}$ as cosmic-boundary $\mathcal{J}/I$); **`manuscript/ave-kb/common/trampoline-framework.md` §1.3.7** ("God's Hand and the cosmic IC"); [E-017 phase-transition-while-spinning mechanism in trampoline-framework.md §1.3]
  - **Action:** formalize Grant's universe-as-vortex framing as a macroscopic application of the lattice-genesis + density-vs-saturation reframings (E-017, E-018). The universe IS a vortex in the pre-genesis plasma; the crystallized lattice is the vortex's coherent body. **MECHANIZED 2026-05-15 evening:** the vortex IS the freeze-in rotating region; the cosmic angular momentum $\mathcal{J}_{\text{cosmic}}$ is the macroscopic signature of this vortex; $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}}/I_{\text{cosmic}}$ is the IC. Three observational routes (α, G, $\mathcal{J}_{\text{cosmic}}$) constrain the same $u_0^*$. **Manuscript section:** Vol 3 Ch 4 §sec:cosmological_origin or new §sec:universe_as_vortex_machian — should explicitly state vortex = freeze-in rotating region, with cross-ref to trampoline-framework.md §1.3.7 and A-031.
  - **Status:** MECHANIZED 2026-05-15 evening (framework-level closure); manuscript propagation still queued. Specific Vol 3 Ch 4 / Vol 3 Ch 5 edits pending.
  - **Cross-refs:** E-017 (genesis-chirality, mechanized via same phase-transition-while-spinning); E-018 (density-vs-saturation cosmological reframing); A-031 (cosmic-$\mathcal{J}$ IC identification); A-030 (α + G + cosmic-$\mathcal{J}$ three-route); A-001 (α-as-calibration, sharpened); trampoline-framework.md §1.3.7 (canonical "God's Hand" framing)
### Ch 6 — Solar System (`06_solar_system.tex`)
### Ch 7 — Stellar Interiors (`07_stellar_interiors.tex`)
### Ch 8 — Gravitational Waves (`08_gravitational_waves.tex`)
### Ch 9 — Condensed Matter Superconductivity (`09_condensed_matter_superconductivity.tex`)
### Ch 10 — Macroscopic Material Properties (`10_macroscopic_material_properties.tex`)
### Ch 11 — Thermodynamics and Entropy (`11_thermodynamics_and_entropy.tex`)

- **[E-022] Formalize the four-entropy distinction at the BH horizon**
  - **Sources:** [doc 62_ §10:L1-L60](../L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md) (`2671a54`, 2026-04-23); [doc 63_ §4.1-4.3:L94-L120](../L3_electron_soliton/63_info_loss_stance_reaudit.md#L94) (`740b1a3`, 2026-04-24); [doc 64_ §3-§4:L74-L186](../L3_electron_soliton/64_first_law_derivation_attempt.md#L74) (`b74ac19`, 2026-04-24); [doc 65_ §9:L201-L213](../L3_electron_soliton/65_flag_62g_discrete_lattice_gamma.md#L201) (`f9b463e`, 2026-04-24)
  - **Action:** Vol 3 Ch 11 introduces Ŝ = -k_B Σ ln(1−|Γᵢ|²) and explicitly rejects Boltzmann S = k_B ln(Ω). Add a new subsection (or boxed table) cataloging the four distinct entropies that arise at the BH horizon and their physical meanings: (a) **Corpus continuum Ŝ_horizon = 0** (symmetric saturation, idealized smooth boundary); (b) **Corpus + discrete-lattice Ŝ_horizon ≈ 8.7·k_B** mass-independent universal constant (doc 65_ — likely "phase ambiguity" topological invariant of the horizon-forming transition, NOT a degrees-of-freedom count); (c) **Surface Ŝ_geometric = A·log(2)/ℓ_node²** (doc 61_'s A-B interface picture, vindicated as AVE-native by doc 62_ §10 via |Γ|²=1/2 per frustrated A-B bond); (d) **Standard thermodynamic S_BH = A/(4·ℓ_P²)** (imported from GR first law, NOT currently axiom-derived; Flag 62-A). Ratio Ŝ_geometric/S_BH ~ 10⁻⁴⁴ is Machian dilution (NOT a contradiction). Surface-vs-volume info-destruction location is the observable discriminator (Flag 63-A). Companion: E-027 records the open Ax5 candidate.
  - **Status:** queued
  - **Cross-refs:** E-024, E-025, E-026, E-027, C-001

- **[E-025] Area theorem δA ≥ 0 — axiom-first derivation from Ax1+Ax4+Ax2**
  - **Sources:** [doc 64_ §1:L36-L62](../L3_electron_soliton/64_first_law_derivation_attempt.md#L36) (`b74ac19`, 2026-04-24)
  - **Action:** add a standalone Vol 3 Ch 11 subsection (or appendix in Ch 21) deriving the BH area theorem from AVE axioms: r_sat = 7GM/c² (Ax4 saturation boundary, linear in M) → δr_sat = 7G·δM/c² > 0 for δM > 0 → δA = 8π·r_sat·δr_sat = 392π·G²M·δM/c⁴ > 0. AVE's version is stronger than Hawking's 1971 area theorem because it derives WHY the horizon can only grow (Ax4's saturation threshold scales with embedded mass). This is a publishable axiom-first result. Companion mass-energy: dE = dM·c² from Ax2 + Lenz BEMF (mass-as-inductance) at [higgs_impedance_mapping.py:48-52](../../src/scripts/vol_2_subatomic/higgs_impedance_mapping.py#L48-L52).
  - **Status:** queued
  - **Cross-refs:** E-022, E-027

- **[E-027] First-law T·dS = dE closure — Flag 62-A open derivation gap (Ax5 candidate)**
  - **Sources:** [doc 64_ §3-§5:L74-L213](../L3_electron_soliton/64_first_law_derivation_attempt.md#L74) (`b74ac19`, 2026-04-24); [doc 62_ §0 + Flag 62-A](../L3_electron_soliton/62_ruptured_plasma_bh_entropy_derivation.md) (`2671a54`, 2026-04-23)
  - **Action:** the BH first law T·dS = dE does NOT close axiom-first with AVE's native Ŝ_geometric — it's off by 7ξ ≈ 10⁴⁴ (the Machian dilution factor). Standard S_BH = A/(4·ℓ_P²) makes T·dS = dE work numerically but uses Boltzmann equipartition that Vol 3 Ch 11:15 explicitly rejects. **Two paths to closure (research work, not editorial):** (a) complete Vol 3 Ch 11:14-48's "geometric spreading" volume-entropy mechanism for the ruptured-plasma BH interior (open derivation); (b) accept S_thermodynamic as a new AVE quantity distinct from Ŝ_geometric (potential Ax5). Until one path closes, mark Flag 62-A explicitly in any chapter that cites the first law for BH thermodynamics so the import is honest.
  - **Status:** adjudication-open
  - **Conflicts:** dependent on resolution of the entropy-formula question; see C-001 for entropy-framework status.
  - **Cross-refs:** E-022, E-025; **A-002 (axiom/derivation status: open gap), A-003 (Ax5 candidate B)**
### Ch 12 — Ideal Gas Law and Fluid Pressure (`12_ideal_gas_law_and_fluid_pressure.tex`)
### Ch 13 — Geophysics (`13_geophysics.tex`)
### Ch 13 — Water LC Lattice (`13_water_lc_lattice.tex`)
### Ch 14 — Macroscopic Orbital Mechanics (`14_macroscopic_orbital_mechanics.tex`)
### Ch 14 — Sonoluminescence and Tabletop Relativity (`14_sonoluminescence_and_tabletop_relativity.tex`)
### Ch 15 — Black Hole Orbital Resonance (`15_black_hole_orbital_resonance.tex`)
### Ch 16 — Kolmogorov Spectral Cutoff (`16_kolmogorov_spectral_cutoff.tex`)
### Ch 18 — Superconductivity Intro (`18_superconductivity_intro.tex`)
### Ch 18 — Superconductivity Phase-Locked (`18_superconductivity_phase_locked.tex`)
### Ch 19 — Phase Transition Melting (`19_phase_transition_melting.tex`)
### Ch 19 — Phase Transition Turbulence (`19_phase_transition_turbulence.tex`)
### Ch 19 — Phase Transition Water (`19_phase_transition_water.tex`)
### Ch 20 — White Dwarf Predictions (`20_white_dwarf_predictions.tex`)
### Ch 21 — Black Hole Interior Regime IV (`21_black_hole_interior_regime_iv.tex`)

- **[E-023] Flag 64-A — r_sat = 7GM/c² (AVE) = 3.5·r_s (standard Schwarzschild) falsifiable observational prediction**
  - **Sources:** [doc 64_ §1 Flag 64-A:L64](../L3_electron_soliton/64_first_law_derivation_attempt.md#L64) (`b74ac19`, 2026-04-24); [Vol 3 Ch 15:291-355](../../manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex#L291) (Buchdahl bound)
  - **Action:** Vol 3 Ch 21 (or Ch 15) should explicitly call out: AVE predicts the BH horizon at r_sat = 7GM/c², which is **3.5× the standard Schwarzschild radius** r_s = 2GM/c². This is a falsifiable observational prediction for any high-gravity test (EHT imaging, gravitational-wave ringdown, gravitational lensing of nearby objects). Box this prediction with its derivation chain so it's findable by reviewers. The factor-of-7 vs factor-of-2 reflects AVE's stricter Buchdahl bound per Vol 3 Ch 15:291-355 — derived from Ax2+Ax3 Poisson-ratio projection (ν_vac = 2/7).
  - **Status:** queued
  - **Cross-refs:** E-025, predictions.yaml entry should follow (track in engine_pending under predictions.yaml as part of the BH-prediction registration)

- **[E-103] Same-epistemic-horizon framing — BH interior vs cosmic interior (Grant adjudication 2026-05-15 evening via A-031)**
  - **Sources:** **A-031** (Grant adjudication 2026-05-15 evening); `manuscript/ave-kb/common/trampoline-framework.md` §1.3.7 ("God's Hand and the cosmic IC"); Vol 3 Ch 2:43 (canonical same-mechanism BH-electron framing)
  - **Action:** Vol 3 Ch 21 (BH Interior Regime IV) should add a brief cross-cutting note: the substrate-observability rule's "you can characterize the boundary but not what set it" structure applies fractally at every scale. Just as we (inside our cosmic boundary) can measure cosmic $\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$ but cannot see "God's Hand" beyond — outside observers of a BH measure $M, Q, J$ at the horizon but cannot see the matter-history that formed it. **Same epistemic horizon, applied at different scales.** Cross-ref to trampoline-framework.md §1.3.7 + A-031.
  - **Status:** **APPLIED 2026-05-15** — landed as new §sec:substrate_observability_horizon in Vol 3 Ch 21 between exercisebox + summarybox; updated summarybox with same-epistemic-horizon framing bullet
  - **Cross-refs:** A-031; A-026 (substrate-observability rule); E-102 (Vol 3 Ch 4 cosmic-$\mathcal{J}$ companion); Vol 3 Ch 2:43 BH-electron parallel

## Vol 4 — Engineering

### Ch 1 — Vacuum Circuit Analysis (`01_vacuum_circuit_analysis.tex`)

- **[E-042] T_V-rupt = 3.44 MK — vacuum-rupture temperature prediction from Ax 1**
  - **Sources:** [doc 47_ §2.2:L73-L93](../L3_electron_soliton/47_thermal_lattice_noise.md#L73) (`87b502c`, 2026-04-22)
  - **Action:** Vol 4 Ch 1 currently does not cite the AVE-native vacuum-rupture temperature: if K4 substrate were in thermal equilibrium at T > α/(4π)·m_e c² ≈ 5.8×10⁻⁴·m_e c² → **T ≈ 3.44×10⁶ K**, the vacuum spontaneously ruptures from thermal V alone. Add a result-box (likely in §sec:axiom-4-nonlinear or §sec:thixotropic-relaxation). Important clarification: solar-core plasma (1.5×10⁷ K) does NOT imply vacuum-substrate heating — the vacuum BETWEEN particles stays cold. **Falsifiable:** any process that heats the VACUUM (not just plasma) above 3.44 MK without spontaneous pair creation falsifies AVE. Subsumes/extends existing queue [17]; line refs added.
  - **Status:** queued
  - **Cross-refs:** E-041; supersedes existing queue entry [17] in DOCUMENTATION_UPDATES_QUEUE.md

- **[E-085] Vol 4 Ch 1 §rest-energy explicit Virial-sum framing — m_e c² is STRUCTURAL, not predicted**
  - **Sources:** [doc 79 v5.1 §3.5.1-§3.5.3](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L116) (`9f565d6`, 2026-04-28); [Vol 4 Ch 1:175-184](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L175) (corpus-verbatim Virial sum)
  - **Action:** Vol 4 Ch 1:175-184 contains the Virial sum `½ L I_max² + ½ C V_peak² = m_e c²` at bond-pair LC tank saturation onset, but doesn't frame it as "rest energy is STRUCTURAL, not predicted." Add explicit framing: the (2,q) particle's rest energy is structurally fixed by Virial sum at bond-pair LC tank saturation onset; this is not a derived prediction the framework needs to validate, it's a structural constraint pinned by the LC tank saturation boundary. Path α tests GEOMETRY (R/r=φ², chirality), NOT energy. Cross-ref to A-001 (α-as-calibration) and A-017 (Virial-sum rest energy as structural). Cross-ref to Vol 1 Ch 8 chapter-level revision per E-086.
  - **Status:** queued (doc 79 §9 corpus revision package — chapter-level editorial work post-L3-closure)
  - **Cross-refs:** A-017 (canonical entry); E-086, E-087, E-088, E-089 (companion §9 corpus-revision-package entries); A-001 (α-as-calibration analog)

- **[E-086] Vol 1 Ch 8 + KB-ch8 — lemniscate-with-q-half-twists framing as primary; (2,q) torus knot as derived equivalent**
  - **Sources:** [doc 79 v5.1 §1 + §9(a)](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L70) (`6d27e58`, 2026-04-28); chapter's own handoff comment lines 1-56 already flags F1/F2/F3 fixes pending
  - **Action:** Vol 1 Ch 8 + KB-ch8 currently presents (2,3) torus knot as primary. Per doc 79 §1 plumber framing: lemniscate-with-q-half-twists is the primary description; mathematical (2,q) torus knot is the derived equivalent. Add lemniscate-with-twists language as primary; preserve (2,q) torus knot as derived mathematical equivalent. Spatial-trefoil framing → phase-space (R, r) per doc 28 §5.4 (already flagged in queue [1] + chapter handoff comment). Subsumes existing queue [1].
  - **Status:** queued (doc 79 §9(a) corpus revision package)
  - **Cross-refs:** A-014 (L3 closure framework structure stands); E-085, E-087, E-088, E-089; supersedes existing queue [1]

- **[E-087] Vol 4 Ch 1 §sec:LC_tank or new §6.7-style section — Meissner-asymmetric saturation as substrate-native magnetic-moment generator + AVE-HOPF birefringence anchor**
  - **Sources:** [doc 79 v5.1 §6.7](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L407) (`6d27e58`, 2026-04-28); doc 54 §6 (Meissner-asymmetric mechanism); AVE-HOPF birefringence prediction
  - **Action:** Vol 4 Ch 1 (or new section) should land the **Meissner-asymmetric saturation as substrate-native magnetic-moment generator** framing per doc 79 §6.7 — corpus-verbatim from doc 54 §6 lines 197-199. **Pair with AVE-HOPF birefringence prediction as the corpus-empirical anchor.** A-015's 100% CCW chirality on (Φ_link, |ω|) magnitude pairing is the engine-side empirical anchor; AVE-HOPF birefringence is the corpus-cross-repo empirical anchor. Both should land together in any framework-validation summary.
  - **Status:** queued (doc 79 §9 corpus revision package)
  - **Cross-refs:** A-015 (canonical entry); doc 20 χ_(p,q) parallel-impedance derivation; E-019 (cross-repo AVE-Propulsion Ch 4 chiral impedance matching — companion)

- **[E-088] Doc 20 §3 spatial-axis language retirement + Vol 2 Ch 4 SU(2)→SO(3) framing reframe (Rule 6)**
  - **Sources:** [doc 79 v5.1 §9(b) + §9(c)](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L583) (`6d27e58`, 2026-04-28)
  - **Action:**
    - **Doc 20 §3:** retire "p cycles around major circumference 2πR / q cycles around minor 2πr" spatial-axis language → (bipartite-cycle, scalar-crossing) channels per doc 07 §3 reconciliation. Parallel-impedance formula χ = α·pq/(p+q) preserved; physical interpretation of channels updated.
    - **Vol 2 Ch 4:** SU(2)→SO(3) framing reframe (Rule 6) — gyroscopic precession + half-cover stays mathematically; replace "spinor wraps 720°" with bipartite-K4 lobe-count / lemniscate-two-traversal framing. SU(2) language renamed as derived equivalent representation.
    - **Doc 03 §4.3:** add "(2, q) torus knot" framing channel-not-axis annotation per doc 07 §3 + doc 20 §3 reconciliation under bond-pair object class.
  - **Status:** queued (doc 79 §9(b)+(c)+(d) corpus revision package)
  - **Cross-refs:** E-086 (companion Vol 1 Ch 8 lemniscate framing); A-014; doc 07 §3 (Op10 scalar c reframe — already applied as queue [11])

- **[E-089] Doc 37 §3.1 Pauli mechanism revision (PROVISIONAL pending He/Li/Cooper pressure-test)**
  - **Sources:** [doc 79 v5.1 §6.6 + §9(e)](../L3_electron_soliton/79_l3_branch_closure_synthesis.md#L388) (`6d27e58`, 2026-04-28); Grant Q3 2026-04-28
  - **Action:** doc 37 §3.1's "Two electrons of opposite spin share same node-pair via complementary +n̂/−n̂ orientations" framing is structurally questionable at the substrate (vector ω-superposition cancels rather than splits A² budget under free-field reading). Working alternative: "one bound state per saturated node-pair; atomic shells = multiple bond-pair locations within an atomic envelope, each with rotation axis set by local bond geometry." **Load-bearing pressure-tests required before canonicalizing:**
    1. **Helium 1s²:** does substrate-native framing predict 2 saturated bond-pairs within 1s spatial envelope?
    2. **Lithium 1s²2s¹:** 3 bond-pairs distributed across 1s + 2s envelopes (2 + 1 split)?
    3. **Cooper pair (singlet superconductivity):** opposite-spin electrons in same momentum/spatial state — does cancellation argument explain bound state, or does Cooper require separate (BCS-style phonon-mediated) framework?
    4. AVE-Protein + chemistry-application corpus work may have used doc 37 §3.1's pair-sharing framing — auditor lane work to grep + verify; flagged as significant downstream cleanup.
  - **Status:** queued + adjudication-open (PROVISIONAL pending pressure-test)
  - **Cross-refs:** A-014 (L3 closure framework structure includes substrate-native Pauli marked PROVISIONAL); doc 37 §3.2 numerics may still hold under either framing (only per-node mechanism description in question)

- **[E-049] Theorem 3.1 v2 — Q-factor of electron LC tank at TIR boundary (canonical statement in Vol 4 Ch 1)**
  - **Sources:** [doc 17_:L1-L80](../L3_electron_soliton/17_theorem_3_1_reframed_Q_factor.md#L1) (`4aff1d3`, 2026-04-21); [doc 16_ §1.2-§1.3:L38-L55](../L3_electron_soliton/16_theorem_3_1_Q_factor_reframe_plan.md#L38) (`4aff1d3`, 2026-04-21); [doc 24_:L1-L60](../L3_electron_soliton/24_step3_bond_lc_compton.md) (`4aff1d3`, 2026-04-21) (single A-B bond LC = ω_Compton); [doc 27_:L1-L80](../L3_electron_soliton/27_step6_phase_space_Q.md) (`4aff1d3`, 2026-04-21) (α⁻¹ = phase-space Q-factor)
  - **Action:** the Q-factor reframe — "electron's α⁻¹ ≈ 137 is the dimensionless Q-factor of its LC tank at the topological-defect TIR boundary, NOT a Neumann integral over a continuous wire" — supersedes the earlier `14_` Neumann-integral framing. Full numerical verification in doc 17_; algebraic chain via doc 24_/27_. Currently lives only in research docs. Needs explicit canonical statement in Vol 4 Ch 1 §sec:LC_tank (where Theorem 3.1 lives) and a Vol 1 Ch 8 cross-ref. Companion to E-003 (operational form of Ax 3 = |S₁₁|² minimization). The LC-tank framing IS the bridge that makes Vol 1 Ch 8's multipole partition (4π³+π²+π) and Vol 4 Ch 1's LC-tank Q-factor agree at α⁻¹.
  - **Status:** queued
  - **Cross-refs:** E-002 (bare K4 ≠ LC tank context), E-003 (Ax 3 operational form), E-046 (F1 mass correction)

- **[E-075] Doc 75 §1 framing-error — "Ax 3 = energy conservation" reading is Scheme-B-flavored under Scheme-A-canonical numbering — APPLIED via `69fd974`**
  - **Sources:** axiom-homologation commit [`75d1fde`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/75d1fde) (out-of-scope flag); applying commit [`69fd974`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/69fd974) (P3+ framing-error pass)
  - **Action:** [original] under canonical Scheme A, Ax 3 = Effective Action Principle, NOT energy conservation. Doc 75 §1 conflated Ax 3 with Hamiltonian flow / Noether energy conservation.
  - **Status:** **applied (`69fd974`).** Title + §0 + §1 reworded across 4 sites. New framing: "violates Ax 4's symmetric L/C scaling, Noether-broken energy conservation." Doc 75 empirical findings (Diag A Mode I, V·S/T·1 negligible at corpus amplitudes, H_cos drift = Op14 trading) unchanged.
  - **Cross-refs:** A-008 (resolved); A-010 (saturation as local clock); doc 76 SUPERSEDED for analogous Scheme-B framing (now superseded by doc 77_)

- **[E-076] doc 10_ §8(a) "strain-induced chirality-dependent dynamic impedance" — CLOSED via doc 77_ §6.4 chirality EE-translation**
  - **Sources:** [doc 77_ §6.4 + §1 cross-refs](../L3_electron_soliton/77_lattice_to_axiom4_bridge.md#L173) (`6968398`, 2026-04-27); doc 10_ §8 open item (existing); old `DOCUMENTATION_UPDATES_QUEUE.md` queue [16] item ("Future research — strain-induced chirality-dependent dynamic impedance")
  - **Action:** chirality acquisition for the photon-tail (2,3) electron is **standard chiral electrodynamics + Cosserat micropolar elasticity translated into AVE units** — NOT a new derivation gap. Synthesis is a translation gap, now closed. Corpus pieces it rests on per doc 77_ §6.4: 2/7 + 9/7 Poisson decomposition (eq_gravity_derived.tex:38-43 + Vol 3 Ch 20:262-271); chirality from (2,3) parallel-impedance via χ_(p,q) = α·pq/(p+q) per doc 20_ (electron = α·6/5); photon as transverse Cosserat ω wave per doc 30_; spin-½ as gyroscopic precession of topological flywheel per Vol 2 Ch 4; photon-bends-2× per Vol 3 Ch 2:121-159 "The Double Deflection". **No new manuscript writing required**; future agents should cite doc 77_ §6.4 as the closure.
  - **Status:** **closed** — research-doc-level closure documented; no open manuscript work. (May warrant a footnote in Vol 1 Ch 8 / Vol 2 Ch 1 saying "see doc 77_ §6.4 for chirality EE-translation"; defer.)
  - **Cross-refs:** A-008 (spin-½ half-cover citation strengthened in doc 77_ §3); doc 20_ (chirality projection χ_(p,q)); supersedes existing queue [16] in DOCUMENTATION_UPDATES_QUEUE.md

- **[E-067] Op14 saturation as local clock-rate modulation — cross-volume parallel to Vol 3 Ch 3 gravitational n(r)**
  - **Sources:** A-010 (synthesizer audit 2026-04-27); [doc 16_/17_ Q-factor reframe](../L3_electron_soliton/17_theorem_3_1_reframed_Q_factor.md) (`4aff1d3`); [doc 66_ §17.1 time-as-local-clock](../L3_electron_soliton/66_single_electron_first_pivot.md#L507) (`a53ce1c`); [Vol 3 Ch 3 refractive-index-of-gravity](../../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md)
  - **Action:** Vol 4 Ch 1 §sec:thixotropic-relaxation should add explicit subsection: Op14 saturation `Z_eff(r) = Z_0/√S(r)` modulates local effective wave speed `c_eff(r) = c·√(1−A²(r))`, hence local clock rate `ω_local(r) = ω_global · √(1−A²(r))`. Same physics as gravitational refractive-index slowing (E-015 covers Vol 3 Ch 3 case): saturation = lattice's intrinsic refractive-index source. Cross-volume parallel: gravity n(r) and saturation S(r) are two manifestations of the same impedance-as-clock-rate mechanism. **Methodology constraint:** any bound-state analysis using global ω_target must report local ω_local(r) at load-bearing sites (load-bearing = where eigvec or seed concentrates). At rupture boundary (A² → 1), local clock freezes — explains the static-fixed-point reading per A-009. Companion to E-015 (gravity case) + E-049 (Q-factor reframe).
  - **Status:** queued
  - **Cross-refs:** E-015 (gravity τ_local — same physics), E-049 (Q-factor reframe — ω·L = ℏ/e² assumes uniform ω), A-010 (canonical methodology entry), A-009 (saturation-frozen-core empirical case)

- **[E-029] τ_relax = ℓ_node/c — formalize derivation in thixotropic-relaxation section**
  - **Sources:** [doc 59_ §1:L32-L80](../L3_electron_soliton/59_memristive_yield_crossing_derivation.md#L32) (`03cb9d5`, 2026-04-23); engine constant landed at [`constants.py:231-232 TAU_RELAX_SI / TAU_RELAX_NATIVE`](../../src/ave/core/constants.py#L231)
  - **Action:** Vol 4 Ch 1 §sec:thixotropic_relaxation should explicitly derive τ_relax = ℓ_node/c from per-cell K4 Lagrangian + minimum state-change time argument (doc 59_ §1.2). Currently the relaxation time is referenced ([Vol 4 Ch 1:214](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L214)) but the derivation chain isn't shown. Engine constant is in place; manuscript citation closes the loop.
  - **Status:** queued
  - **Cross-refs:** E-015 (Vol 3 Ch 3 τ_local), E-021 (engine global τ_relax flag), E-035 (engine constant — applied)

- **[E-030] V_yield scale-dependence — make explicit cross-volume cross-ref between Vol 1 Ch 7 and Vol 4 Ch 1:711**
  - **Sources:** [doc 55_ banner L1-L19](../L3_electron_soliton/55_cosserat_normalization_derivation.md#L1) (`224cad0`, 2026-04-23); [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711); [Vol 1 Ch 7:104, :115, :130](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L104)
  - **Action:** Vol 4 Ch 1:711 already states the subatomic override (V_yield ≡ V_SNAP for K4-TLM/bond-energy/Yang-Mills). Vol 1 Ch 7:115 (r=1) and :130 (r=11.7) are scale-dependent under this override but read as "inconsistency" without an explicit cross-ref. Add a cross-ref at Vol 1 Ch 7:115/:130 → "see Vol 4 Ch 1:711 — subatomic override" and at Vol 4 Ch 1:711 → "Vol 1 Ch 7:115/:130 are unified under this override." Prevents future agents (and external readers) from re-flagging the perceived inconsistency. See clash C-002 for the adjudication trail.
  - **Status:** queued
  - **Cross-refs:** C-002

- **[E-002] Bare K4 ≠ LC tank — clarify continuum LC-tank framing requires both K4 and Cosserat sectors**
  - **Sources:** [doc 69_ §2.1, §2.2](../L3_electron_soliton/69_bootstrap_chain_calibration.md) (`c830f07`, 2026-04-25)
  - **Action:** add a clarifying paragraph (or footnote) wherever the LC-tank model is introduced: bare K4-TLM at the single-bond level produces grid dispersion (2-step alternation between A and B as the wave shuttles back and forth), NOT a Compton-frequency LC tank. The continuum LC-tank model requires BOTH K4 (capacitance via vacuum permittivity) AND Cosserat (kinetic inductance via mass density) sectors active. The "simplest unknot $O_1$" in AVE is the smallest COUPLED (K4 + Cosserat) oscillator, not a bare K4 lattice bond.
  - **Status:** queued
  - **Cross-refs:** E-009, E-012

- **[E-003] Operational form of Ax 3 = "$|S_{11}|^2$ minimization" — make explicit**
  - **Sources:** [doc 68_ §1, §3.2](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25)
  - **Action:** Vol 4 Ch 1 §LC-tank (or wherever Theorem 3.1 is stated) should explicitly name the operational form of the Effective Action Principle: minimize $|S_{11}|^2$ at the topological boundary. The corpus has this implicit across multiple chapters (Vol 4 Ch 1 LC-tank framing, Vol 1 Ch 8 multipole partition, doc 16_/17_ Q-factor reframe), and AVE-Protein Ch 3 names it explicitly. AVE-Core should match. Equivalent statements: lossless reactive cycling at 90° phase quadrature; $Q \to \infty$ at $\delta = 0$; $\lambda_{min}(S^\dagger S) \to 0$.
  - **Status:** queued
  - **Cross-refs:** E-004, E-007

- **[E-005] Autoresonant is the DRIVE mechanism, not the eigenmode finder**
  - **Sources:** [doc 68_ §11](../L3_electron_soliton/68_phase_quadrature_methodology.md) (`3f6d544`, 2026-04-25); [doc 50_:138-154](../L3_electron_soliton/50_autoresonant_pair_creation.md) (`224cad0`, 2026-04-23)
  - **Action:** wherever AutoresonantCWSource is introduced (likely Vol 4 Ch 1 §sec:autoresonant or Vol 4 Ch 11 FOC section), add a clarifying note: autoresonant driving is the operational regime drive mechanism — it brings the lattice up to and through the saturation boundary — but it is NOT the eigenmode finder for stationary bound states like the (2,3) electron. Phase III-B v2 reached Regime III (median 87% of rupture) but 0/20 seeds crossed Regime IV. Bound-state finding requires $|S_{11}|^2$ minimization (per E-003), not autoresonant pumping.
  - **Status:** queued
  - **Cross-refs:** E-003, related to existing queue [18] in DOCUMENTATION_UPDATES_QUEUE.md
### Ch 2 — Vacuum Fluid Dynamics (`02_vacuum_fluid_dynamics.tex`)
### Ch 10 — Quantum Computing and Decoherence (`10_quantum_computing_and_decoherence.tex`)
### Ch 11 — Experimental Falsification (`11_experimental_falsification.tex`)
### Ch 12 — Falsifiable Predictions (`12_falsifiable_predictions.tex`)
### Ch 13 — Future Geometries (`13_future_geometries.tex`)
### Ch 14 — Particle Decay SPICE (`14_particle_decay_spice.tex`)
### Ch 15 — Autoresonant Breakdown SPICE (`15_autoresonant_breakdown_spice.tex`)
### Ch 16 — Sagnac Inductive Drag SPICE (`16_sagnac_inductive_drag_spice.tex`)
### Ch 17 — Noise Floor Boundary (`17_noise_floor_boundary.tex`)
### Ch 19 — Silicon Design Engine (`19_silicon_design_engine.tex`)
### Ch 20 — Optical Caustic Resolution (`20_optical_caustic_resolution.tex`)

## Vol 5 — Biology

### Ch 1 — Biophysics Intro (`01_biophysics_intro.tex`)
### Ch 2 — Organic Circuitry (`02_organic_circuitry.tex`)
### Ch 6 — Biophysics Pharmacology (`06_biophysics_pharmacology.tex`)
### Ch 7 — Solvent Damping (`07_solvent_damping.tex`)

## Vol 6 — Periodic Table

### Ch 0 — Introduction (`00_introduction.tex`)
### Ch 0 — Summary Table (`00_summary_table.tex`)
### Ch 1 — Computational (`01_computational.tex`)
### Ch 2 — Chemistry (`02_chemistry.tex`)
### Ch 3 — Hydrogen (`03_hydrogen.tex`)
### Ch 4 — Helium (`04_helium.tex`)
### Ch 5 — Lithium (`05_lithium.tex`)
### Ch 6 — Beryllium (`06_beryllium.tex`)
### Ch 7 — Boron (`07_boron.tex`)
### Ch 8 — Carbon (`08_carbon.tex`)
### Ch 9 — Nitrogen (`09_nitrogen.tex`)
### Ch 10 — Oxygen (`10_oxygen.tex`)
### Ch 11 — Fluorine (`11_fluorine.tex`)
### Ch 12 — Neon (`12_neon.tex`)
### Ch 13 — Sodium (`13_sodium.tex`)
### Ch 14 — Magnesium (`14_magnesium.tex`)
### Ch 15 — Aluminum (`15_aluminum.tex`)
### Ch 16 — Silicon (`16_silicon.tex`)
### Appendix A — Heavy Element Catalog (`A_heavy_element_catalog.tex`)
### Appendix B — High-Z Boundary (`B_high_z_boundary.tex`)

## Top-level repo docs

### `README.md`
### `LIVING_REFERENCE.md`
### `CLAUDE.md`
### `.agents/handoffs/CURRENT_STATE.md`

## `manuscript/common_equations/` (canonical equation single-source-of-truth)

### `eq_axiom_1.tex` (Substrate Topology — LC Network)
### `eq_axiom_2.tex` (Topo-Kinematic Isomorphism)
### `eq_axiom_3.tex` (Effective Action Principle)
### `eq_axiom_4.tex` (Saturation Kernel)
### `eq_calibration_constants.tex` (NEW per `05f8ac3` — ℓ_node, Z_0, ξ_topo, α, V_snap, V_yield)
### `eq_gravity_derived.tex` (NEW per `05f8ac3` — G, n(r), Symmetric Gravity, α-invariance, n_temporal/n_spatial split as DERIVED consequences of Ax 1 + Ax 4)

## `manuscript/ave-kb/` (KB invariants header)

### `CLAUDE.md` — INVARIANT-S2 axiom statements (canonical Scheme A per `75d1fde`)
### `common/axiom-homologation.md` — canonicalization audit (NEW per `6968398` — promoted from `.agents/handoffs/` to manuscript-tree per INVARIANT-S3 cross-cutting-notes pattern; load-bearing reference for ≥6 tracked-file citations)

## `manuscript/backmatter/`

### `12_mathematical_closure.tex` (Ax 1↔Ax 2 swap fix per `75d1fde`)

## `manuscript/frontmatter/`

### `00_foreword.tex` (two-section split per `05f8ac3`: four foundational axioms + three calibration boundaries explicitly decoupled)

---

**Next free entry ID:** E-104 (post-2026-05-15 evening sweep — added E-102 (Vol 3 Ch 4 cosmic-$\mathcal{J}$ identification per A-031) + E-103 (Vol 3 Ch 21 same-epistemic-horizon framing). Sweep history: E-094-E-098 substrate-vocab + Master Eq FDTD + boundary-envelope + two-engine arch + cubic anisotropy (2026-05-14); E-099-E-101 used in engine_pending.md; E-102-E-103 cosmic IC framing (2026-05-15 evening structural-closure capture).)
