# AVE-Protein solver-currency hand-off — 2026-06-22 (Vol-5 solver audit follow-through)

**Provenance:** Vol-5 solver-currency / driver-honesty audit (`/tmp/vol5_solver_audit.json`,
30 scripts across 6 batches). The single AVE-Core-fixable item
(`src/ave/solvers/spice_netlist_compiler.py` V_YIELD/I_MAX drift + false
"from constants.py" docstrings) was fixed in this Vol-5 session on branch
`chore/vol5-solver-currency`. The 25 items below live in **AVE-Protein (IP)** and
are **hand-off only**.

**Purpose:** tracked findings for a *focused AVE-Protein session*. These are not
to be fixed from a Vol-5-manuscript / AVE-Core session — cross-repo discipline
(promotions/transfers happen in a dedicated AVE-Protein session; this session
only stages the finding-set). Do **not** edit AVE-Protein files from a Vol-5
context.

**Scope split (from the audit `_fix_split`):**
- `ave-core-fix-here`: 1 script (DONE this session — `spice_netlist_compiler.py`).
- `ave-protein-flag`: 25 scripts (this doc).
- `no-fix`: 4 clean (`spice_transient.py`, `spice_cvr_loop.py`,
  `generate_amino_spice.py`, `test_vswr_fold.py`).

**R3 corroboration (carry into the session):** NO solver in the Vol-5 chain
hard-codes `Z_backbone = 7` or `17.0`. `derive_z_topo_first_principles.py:61`
COMPUTES `Z_backbone = universal_impedance(L_bb, C_bb) = sqrt(L/C)`. The recurring
integer **7** (`validate_tau_fold:35`, `s14:32/16`, `s_param '= 1/7'` comment,
`protein_bond_constants:512 l=7`) is a **stale-label / rounding artifact** of the
analytic `Q_BACKBONE = 0.75·π² ≈ 7.402`, not an independent hard-coded 7-Ω baseline.

---

## §A — CONSTANTS-FIRST (value drift / provenance; **R1-independent — can proceed now**)

These are arithmetic/provenance fixes. They are independent of the impedance-folding
walk-back and can be executed without waiting on the R1 fork.

### A1 — `src/scripts/validate_tau_fold.py:35,36,40` (serious, CONSTANTS) — priority 2
- **Finding:** `Q_BACKBONE = 7` hard-coded INTEGER vs canonical `0.75·π² = 7.402`;
  it enters **SQUARED** in `TAU_FOLD_0 = 3·Q²·TAU_WATER` (line 40) → **~12% prefactor
  drift** (1.22 vs 1.36 ns). `F0_BACKBONE = 23e12` (line 36) is the stale literal the
  engine already retired for 21.7 THz (label-only here). Docstring (24) claims "All
  constants from ave.core.constants" but the file imports **nothing** — all three are
  local hard-codes.
- **Fix:** replace `Q_BACKBONE = 7` with canonical `0.75*np.pi**2` (= 7.402);
  replace `F0_BACKBONE = 23e12` with canonical 21.7 THz; import `TAU_WATER` instead of
  hard-coding `8.3e-12`; make docstring (24) true (actually import) and drop the "Zero
  empirical parameters" line that also renders into the output PDF (355).
- **Single most actionable value-drift in the Protein set.**

### A2 — `src/ave_protein/solvers/protein_bond_constants.py` (notable, CONSTANTS+currency) — priority 3
- **Finding (load-bearing, reproducibility-breaking):** `D_NH`/`D_CO` comments
  (200-201: 1.01/1.23 Å) contradict the live `BACKBONE_BONDS` (0.817/1.121), so
  `D_HB_DETECT` is actually **1.938 Å**, not the commented **2.24 Å**; the stale value
  propagates through the `Z_HB` and `R_OXYGEN_SP3` derivation walkthroughs (208/259/439/442-443).
  Line **512** `l=7 (= Q_BACKBONE = 0.75π²)` asserts an identity that is a ~5.7%
  coincidence (7 ≠ 7.402).
- **Fix:** correct `D_NH`/`D_CO` comments to 0.817/1.121; correct `D_HB_DETECT`
  comment 2.24 → 1.938 Å and the dependent `Z_HB`/`R_OXYGEN_SP3` walkthroughs; fix
  line 512 to state 7 is a rounding of 0.75π² ≈ 7.402, NOT an identity.
- Feeds many downstream scripts → fix early in the session.
- **KEEP-AS-IS:** the `R_WS` deprecation block (349-362, "BACK-FITTED NOT FIRST
  PRINCIPLES") is **exemplary honesty** — do NOT touch (see KEEP-AS-IS below).

### A3 — `src/ave_protein/regime_2_nonlinear/protein_fold.py:215-216` (serious; CONSTANTS half) — priority 4
- **Finding:** molecular branch hard-codes `K_attr = 1.0`, `d_sat = 3.5` under a
  comment claiming all-axiom-derived (nuclear branch constants are clean canon).
- **Fix:** axiom-trace or explicitly tag `K_attr`/`d_sat` as molecular-branch numeric
  choices. (The honesty half of this script is in §B.)

### A4 — `src/scripts/s17_dalembertian_allostery.py:82` (serious; CONSTANTS half) — priority 5
- **Finding:** damping **0.887** hard-coded uncited — it is exactly canonical
  `R_DAMP_TOTAL = 0.887` (`protein_bond_constants.py:491`) which the v4 engine imports.
  `DT = 0.05` is printed as "dt=0.05s" (40,87) — dimensionally **FALSE** label (it is a
  dimensionless LC step). Arrays forced `jnp.float32` (55-69) despite `jax_enable_x64=True`.
- **Fix:** import `R_DAMP_TOTAL` instead of vendoring 0.887; fix the "dt=0.05s" label
  to a dimensionless LC step; remove the `float32` casts. (The "VERIFIED Total Emergence"
  honesty half is in §B.)

### A5 — `src/scripts/s14_folding_kinetics.py:32,37,38` (notable, CONSTANTS) — priority 15
- **Finding:** `Q = 7.0` ImportError fallback (32) + docstring `Q = 7` (16) drift from
  canonical 7.4022 (~5.4%, squared → ~11% bias when the import fails). `TAU_H2O = 8.3e-12`
  (37) hard-coded under an "ABSOLUTE PHYSICS CONSTANTS" banner — it is a MEASURED solvent
  BC. `BETA = ln(3)·(3/7)` (38) appears ONLY in this script — no corpus provenance.
- **Fix:** fix the `Q=7.0` fallback + docstring to canonical 0.75π² = 7.4022; import
  `TAU_WATER` instead of vendoring + drop the "absolute" relabel; provide corpus
  provenance for `BETA` or tag it uncorroborated-inline-derivation.

### A6 — `src/scripts/fret_chiral_parallax.py:30-31,39,63` (notable, CURRENCY) — priority 10
- **Finding:** `v_esc = 11.2e3`, `eps_11 = 0.5·(v_esc/C_0)² = 6.98e-10` — **factor-~7
  BELOW** canonical `eps_11 = 4.87e-9` (7GM/(c²R)); reproduces the 7e-10-class value the
  KB **retired 2026-05-17**. Downstream `fractional_relaxation = ALPHA·eps_11 = 5.09e-12`
  vs KB-corrected 3.56e-11; stdout (63) prints "eps_11 ~ 7e-10" verbatim (retired number).
- **Fix:** re-derive `eps_11` from canonical 7GM/(c²R) Machian strain (4.87e-9) instead
  of the v_esc route; fix the printed "eps_11 ~ 7e-10" and the downstream 5.09e-12 →
  3.56e-11. **Headline verdict ("CURRENTLY UNFALSIFIABLE") is correct + matches KB — keep.**

### A7 — `src/scripts/spice_organic_mapper.py:55,37` (minor) — priority 21
- **Finding:** `_DA` hard-codes `1.66e-27` duplicating canonical `M_U`. Docstring line 37
  "IR-spectroscopic bond force constants (measured)" is stale — code now derives `k` from
  `soliton_bond_solver`. `AMINO_SOURCE_FREQ = '30THz'` conflates Wien freq-form (18.2 THz)
  and wavelength-form (32 THz) peaks.
- **Fix:** import `M_U` instead of `_DA = 1.66e-27`; remove the stale "measured" docstring
  line; fix the 30-THz Wien-form conflation.

### A8 — `src/scripts/derive_z_topo_first_principles.py:261` (minor) — priority 22
- **Finding:** line 261 "Zero free parameters. Zero empirical fits." overclaims given
  CODATA-mass + measured-force-constant inputs. (This script is the R3 ground-truth that
  `Z_backbone` is a COMPUTED sqrt(L/C) — keep that.)
- **Fix:** qualify to "no fitted parameters; inputs = CODATA masses + axiom-derived force
  constants."

### A9 — `src/ave_protein/engines/s_param_network_engine.py:12,81,74` (notable; CONSTANTS half) — priority 11
- **Finding (CONSTANTS):** `Z_HB_SCALE` comment "= 1/7" rounds `1/Q_BACKBONE` (actual
  0.1351); `CHI_SCALE = d0³/11.0` (81) has an unexplained `/11` divisor; solvent Debye
  constants (86-92) are literature.
- **Fix (CONSTANTS):** fix the `Z_HB_SCALE` "= 1/7" comment to the actual `1/Q_BACKBONE`
  (0.1351); document or trace the `/11` divisor. (The "Zero magic numbers" headline-honesty
  half is in §B and is **R1-contingent.**)

> CONSTANTS items A1–A8 (and the A9 numeric half) are **R1-independent** and can be landed
> in the AVE-Protein session regardless of the impedance-folding fork.

---

## §B — HONESTY-NEXT (framing / verdict overclaim)

Listed in `_priority` order. Items tagged **[R1-contingent]** ride the staged
impedance-folding walk-back (see R1-CONTINGENCY below) — their constants fixes are
independent but their "validates / zero-parameter / emerges" framing cannot be finalized
until the fork closes.

### B1 — `src/ave_protein/regime_2_nonlinear/protein_fold.py:5-8,375,12,266,333-334` (serious) — priority 4 **[R1-contingent]**
- **Finding (highest-magnitude overclaim):** docstring 5-8 claims the same math "will
  seamlessly assemble 235 nucleons into the precise geometry of **Uranium**" AND folds
  proteins — no 0.30 caveat, contradicts the staged R1 negative. Line 375 stdout "Quench
  complete! **Absolute lowest-energy** structural matrix resolved." — a global-min claim a
  quench cannot back. Docstrings repeatedly assert "absolute geometric minimum" / "guarantees
  emergence" (12, 266, 333-334).
- **Fix:** retract the "proteins-AND-Uranium will seamlessly assemble" docstring + add the
  0.30 caveat; down-scope line 375 (a quench cannot guarantee a global min); remove
  "guarantees emergence" / "absolute geometric minimum."

### B2 — `src/scripts/s17_dalembertian_allostery.py:13,149-150` (serious) — priority 5 **[R1-contingent]**
- **Finding:** "Zero empirical parameters. True Level 6 (Total Emergence) validation!"
  (13) + "VERIFIED: Macroscopic D'Alembertian Wave Mechanics emerge completely
  spontaneously…" (149-150) — highest-overclaim driver: a hand-written damped
  velocity-Verlet (not from-axioms SPICE), "VERIFIED" printed **unconditionally** with NO
  dispersion-relation test (only `argmax` printed, never compared to a predicted wave speed).
- **Fix:** retract/down-scope the "True Level 6 Total Emergence" + "VERIFIED … emerge
  completely spontaneously" to a "qualitative wavefront demo." (Constants half = §A4.)

### B3 — `src/scripts/s18_oligomer_assembly.py:148-149,6` (serious) — priority 6 **[R1-contingent]**
- **Finding:** "VERIFIED: The universal LC-network gradient successfully bounds disjoint
  topologies … confirming multi-chain limits!" — unconditional "VERIFIED … confirming" with
  **NO pass/fail criterion evaluated** (prints loss + offset, never tests docking;
  print-vs-compute mismatch). Docstring (6) "final means testing validation" over-scopes a
  5-Ala+5-Gly demo. Operative loss term is `steric_penalty`, not the headline "admittance
  bridging."
- **Fix:** retract the unconditional "VERIFIED … confirming multi-chain limits"; down-scope
  the "final means testing validation"; reconcile the "admittance bridging" headline with the
  operative steric term; add 0.30 caveat. `dock_params` 15 Å X-sep / `lr=0.5` / 150 steps are
  uncited solver knobs — tag.

### B4 — `src/scripts/rmsd_benchmark.py:175,3-7` (serious) — priority 7 **[R1-contingent]**
- **Finding:** verdict-box (175) "VERIFIED: Operator 14 successfully inverted structure
  limits in epsilon=2.0 phase" gated only on `rmsd > baseline+2.0 Å` on **N=1** (Trp-cage) —
  conflates "RMSD got worse in a different dielectric" with "Op14 verified"; no 0.30 caveat.
  Title (3-7) "zero empirical structural data / PDB never enters prediction" is contradicted
  by the post-hoc `ave_s = ave_coords·(pdb_d/ave_d)` scale-normalization (96-99,149-153) that
  re-pins AVE output to PDB mean Cα-Cα before RMSD. `lipid_params=[2.0,2.0,8.2e-12,1e12]` (137)
  is a stipulated dielectric env.
- **Fix:** retract the line-175 verdict-box; reconcile "PDB never enters" with the post-hoc
  scale-normalization; verify the "Operator 14" label vs current Op-numbering.
- **Cross-cut:** calls `fold_cascade_transient_v7` on the **v4** engine — see cross-cutting
  item #2 (v4 may be out of D5-locked v3-only scope).

### B5 — `src/scripts/amino_chain_pipeline.py:18,807` (serious) — priority 8 **[R1-contingent]**
- **Finding:** "NO FREE PARAMETERS. NO STATISTICAL FITTING." (18) is falsified by the
  script's own hand-tuned force-field (`r_group_R` 20 hand-assigned, `_HYDROPHOBICITY` table,
  `k_bond=50`, β-sheet `d_sheet=4.7`, helix `d_hb=5.4` i→i+4, `k_hbond=3.0`, `_ROT_FACTOR=0.25`,
  cos-targets). Prints Kabsch RMSD (807) + fold classification + AVE-vs-PDB overlay WITHOUT the
  clm-s11nf0 0.30 caveat; fold is steric/hydrophobic-driven yet framed S11-driven (the S11
  "feedback gain" is cosmetic, `1+|Γ|²` ∈ [1,2]).
- **Fix:** retract "NO FREE PARAMETERS / NO STATISTICAL FITTING"; add the 0.30 caveat wherever
  RMSD / fold-class / overlay prints; re-label the mechanism as a steric+hydrophobic force-field
  with S11 as a secondary gain term.

### B6 — `src/scripts/simulate_protein_spice_transmission_line.py:29-32,34-40,161` (serious) — priority 9 **[R1-contingent]**
- **Finding:** header asserts secondary structure "determined **STRICTLY** by AC impedance
  match" (29-32), Z0-matched "cleanly wraps into Alpha-Helix" / mismatched "violently unwinds
  into Beta-Sheet" (34-40); plot titles "AVE Deterministic Protein Folding" (161). The script
  never folds / computes RMSD — it only Bode-sweeps `|H(jω)|` + an integrated-strain proxy
  (print-vs-compute); the helix-vs-sheet outcome is narrative-asserted. `(1+z)` sidechain-loading
  (100-102) is an asserted ansatz, not axiom-derived.
- **Fix:** add the 0.30 caveat to header + figure titles; scope "determined STRICTLY by AC
  impedance match" down to what the code actually computes (a strain proxy — it never folds).
- **Note:** uses `np.sum(strain)` here vs `np.trapz` in `amino_chain_pipeline` — "integrated
  strain" numbers are NOT comparable across the two scripts.

### B7 — `src/ave_protein/engines/s_param_network_engine.py:12` (notable) — priority 11 **[R1-contingent]**
- **Finding (HONESTY):** docstring line 12 "All constants audited and traced to AVE axioms.
  Zero magic numbers." is FALSE on the file's own contents (literature solvent Debye constants
  86-92 + the `/11` divisor at 81). Steric block (459-558, 18 terms) dominates the objective —
  consistent with the R1 steric-driven finding.
- **Fix:** retract the "Zero magic numbers" headline. (Numeric half = §A9, R1-independent.)

### B8 — `src/scripts/s12_pdb_validation.py:6,9` (notable) — priority 12 **[R1-contingent]**
- **Finding:** docstring (6,9) "Validates … zero fitted parameters" on the 0.30-graded
  clm-s11nf0 (walk-back STAGED); undercut by embedded classical DSSP constants (188-207,
  Q=27.888, -0.5, 1.24, 1.0 — Kabsch-Sander, labeled). STDOUT prints bare "RMSD < 5 Å"
  pass-counts — the exact MD-borrowed threshold the substrate-first audit flagged; corpus
  moved to per-protein size-scaled thresholds (1.52-2.91 Å). `Rg_eq = 1.7·(N/ETA_EQ)^(1/3)·sqrt(3/5)`
  (275) is a semi-empirical consistency formula (1.7 Slater radius + solid-sphere factor).
- **Fix:** down-scope "Validates … zero fitted parameters"; replace bare "RMSD<5Å" with the
  per-protein size-scaled thresholds + a note that RMSD<5Å is MD-borrowed.

### B9 — `src/scripts/stress_test_20_sequences.py` (notable) — priority 13 **[R1-contingent]**
- **Finding:** near-byte-identical twin of `s12` (shares the same overclaim docstring, bare
  RMSD<5Å, missing 0.30 caveat). ADDITIONAL: docstring says "v7 Multi-Scale S11 Engine" but
  calls `fold_network` from `s_param_network_engine` (Y-matrix path) — a reader cannot tell
  which engine produced a given Vol-5 number.
- **Fix:** inherits all `s12` fixes; resolve the engine-attribution ambiguity. See cross-cutting
  item #1 (dedup-adjudicate s12 vs stress_test_20).

### B10 — `src/scripts/s17_sub5_rmsd_benchmark.py:327-328` (notable) — priority 14 **[R1-contingent]**
- **Finding:** stdout "SUB-5 Å TARGET ACHIEVED!" celebrates the MD-borrowed RMSD<5Å threshold
  as the falsification line; no 0.30 caveat. Best-of-three `min(global,cotrans,restart)` is
  favorable-tail selection (honestly disclosed 19-20). TARGETS (225-231) are the pre-D1 5-set,
  honestly scope-noted.
- **Fix:** replace the "SUB-5 Å TARGET ACHIEVED!" celebration; add 0.30 caveat.
- **KEEP-AS-IS:** the Method-B+ "Independent restart" label correction (Q-PROTEIN-10) is the
  good pattern — do NOT touch (see KEEP-AS-IS).

### B11 — `src/scripts/s15_allosteric_yield.py:124,17,37,67` (notable) — priority 16 **[R1-contingent]**
- **Finding:** stdout (124) "SUCCESS: … manifesting classical ALLOSTERY" on a synthetic
  `ligand_load = 15.0+15.0j` into an all-alanine homopolymer — overstates a built-in
  angle-redistribution manifestation as a confirmed phenomenon (no SM-counterfactual, no real
  allosteric system). Calls `fold_s11_jax` (clm-s11nf0 0.30) with NO caveat. "Bingham Plastic
  Yield … tearing the secondary structure" (17,37) is dissipation-leak vocabulary that FAILS
  the lossless-reactive substrate.
- **Fix:** down-scope "SUCCESS … classical ALLOSTERY" to a manifestation demo + 0.30 caveat;
  re-express "Bingham Plastic Yield / tearing" as reactive/impedance-native (plastic/yield =
  dissipation-leak per the amorphous-retirement ruling).

### B12 — `src/scripts/s16_allosteric_pathway_map.py:20,39` (notable) — priority 17 **[R1-contingent]**
- **Finding:** "Z→Γ→S11 minimisation (zero empirical parameters)" (20) on `fold_s11_jax`
  (clm-s11nf0 0.30). `LIGAND_Z = 15.0+15.0j` (39) same synthetic load as s15. On an all-alanine
  homopolymer there is no sequence heterogeneity to carry a genuine pathway — the off-diagonal
  structure is a uniform-line standing-wave artifact over-read as an "allosteric pathway."
- **Fix:** add 0.30 caveat to the "zero empirical parameters" line; scope down the "allosteric
  pathway" label (uniform-line standing-wave, not a sequence pathway).

### B13 — `src/scripts/s13_oligomer_assembly.py:361,363,371` (notable) — priority 18 **[R1-contingent]**
- **Finding:** SUCCESS/FAILED verdict on a single min-Cα-distance threshold for a random-seeded
  polyalanine HOMODIMER — axiom-manifestation of the attractive basin, not validated biological
  assembly. "Dimer assembly validation completed" (371) overstates. Docstring "conjugate Z
  matching" mechanism is the un-landed clm-s11nf0 claim while code (162-166) admits sterics are
  what's evaluated. Stray developer-uncertainty comments (188-195, "Wait, JAX cannot close over
  dictionaries…") left in a tracked driver.
- **Fix:** down-scope the SUCCESS/FAILED "validation" to an attractive-basin manifestation demo +
  0.30 caveat; reconcile "conjugate Z matching" with the operative steric term; axiom-trace or tag
  the docking heuristics (20 Å spread, 6 Å cutoff); remove the stray dev comments.

### B14 — `src/scripts/ramachandran_steric.py:18,9` (notable) — priority 19
- **Finding:** "NO FREE PARAMETERS. Every constant traces to the lattice axioms." (18) is false —
  `OVERLAP_FACTOR=2.08`, basin windows (86-91), `C-N:1.33` (40), `K_BB=15.0`/`K_SC`, `F_DIPOLE`/`F_PRO`,
  1.22 Å reach, `CF_ALPHA` Chou-Fasman targets are empirical/tuned. Provenance mislabel: docstring (9)
  says bond lengths are "d_eq from soliton_bond_solver (Axioms 1-2)" but the code imports `KNOWN_D` —
  the EXPERIMENTAL reference table (`soliton_bond_solver.py:378`), not axiom-computed `d_eq`.
- **Fix:** retract "NO FREE PARAMETERS / Every constant traces to the lattice axioms"; fix the
  `KNOWN_D`-as-`d_eq` provenance label. (Mostly empirical-input honesty, R1-independent.)

### B15 — `src/scripts/plot_folding_progressions.py:8-10,52/72/80,161` (notable) — priority 20 **[R1-contingent]**
- **Finding:** docstring (8-10) "saves 4 Cartesian frames (uncoiled → … → crystallized) **proving**
  the deterministic nature of the gradient" — "proving" is verdict-grade for a single L-BFGS-B
  visualization; frame label "crystallized" asserts a physical fold endpoint; "Axiomatic Convergence"
  titles above-grade; NO scoped disclaimer (unlike `animate_villin_fold`). RUNTIME-BUG (read-only flag):
  bare `jax` used at 52/72/80 but `import jax` only inside `__main__` (161) → NameError if
  `run_progression` is imported elsewhere.
- **Fix:** change "proving" → "illustrating"; reconsider "crystallized" + "Axiomatic Convergence";
  add a scoped disclaimer; hoist `import jax` to module top.

### B16 — `src/ave_protein/engines/s11_fold_engine_v3_jax.py:6-7` (minor) — priority 23 **[R1-contingent]**
- **Finding:** docstring 6-7 "Everything emerges from S11 minimisation" / "Zero force constants"
  contradicted by the actual loss = `s11_combined + LAMBDA_STERIC·steric + P_C·packing` (1450/1558);
  rides the staged R1 0.30 negative.
- **Fix:** down-scope the "everything emerges from S11 / zero force constants" framing.

### B17 — `src/ave_protein/engines/s11_fold_engine_v4_ymatrix.py:21,44` (minor) — priority 24 **[R1-contingent]**
- **Finding:** docstring (21) "Zero new parameters / Same Axiom 1-4 physics as v3" inherits v3's
  above-grade posture; objective `f_i` (1075) = per-port `|Γ|²` + packing/N + steric/N +
  Op10 junction-projection, not S11-alone. (Internally HONEST: 1031-1043 self-flags scalar-mean-S11
  is not the EE-canonical multiport solve.)
- **Fix:** down-scope the inherited "Zero new parameters / emerges from S11"; avoid propagating
  "proven backbone" (44) verbatim.

### B18 — `src/scripts/ramachandran_steric_jax.py:16-19,13` (minor) — priority 25
- **Finding:** inherits all of `ramachandran_steric`'s constants + the "AVE DERIVATION CHAIN:
  Axioms 1-2 → soliton_bond_solver → d_eq" attribution (though `BOND_LEN` is built from `KNOWN_D`).
  Discloses a JAX-port simplification (424 Ile, 600 Y duplicate) that softly contradicts the line-13
  "identical physics" claim.
- **Fix:** inherits B14's docstring fixes via the single-source import — fix the original and it
  propagates; note the disclosed port-fidelity gap vs the "guarantee identical physics" claim.

### B19 — `src/scripts/animate_villin_fold.py:9,18-19,303` (minor) — priority 26 **[R1-contingent]**
- **Finding:** "native three-helix bundle" (9) + "validated against crystal/NMR" (19) assert
  fold-correctness the R1 caveat undercuts; on-figure "Zero free parameters" (303) above-grade given
  empirical Z_TOPO. **Strong top-level scoped disclaimer (12-19, "visualises the MATHEMATICAL
  CONVERGENCE … does NOT simulate the physical folding pathway") substantially mitigates — low
  priority.**
- **Fix:** add the staged-walk-back caveat to "native three-helix bundle" + "validated against
  crystal/NMR"; soften the on-figure "Zero free parameters."

---

## R1-CONTINGENCY callout

**19 scripts are R1-entangled** (audit `_r1_entangled`). Their **HONESTY** fixes (the
"validates / zero-parameter / emerges / VERIFIED / robust" framing) **cannot be finalized**
until the **clm-s11nf0** (solidity 0.30) impedance-folding walk-back **lands** and/or the
**eigenmode-vs-cavity fork closes** (memory `project_ave_protein_impedance_folding_negative`:
impedance does NOT carry the fold; the engine's own objective rejects native, 12/12 decoys,
steric-driven). Their **CONSTANTS / currency** fixes are **independent** and may proceed now.

R1-entangled set:
`s11_fold_engine_v3_jax`, `s11_fold_engine_v4_ymatrix`, `s_param_network_engine`,
`protein_fold` (regime_2_nonlinear), `amino_chain_pipeline`,
`simulate_protein_spice_transmission_line`, `s12_pdb_validation`, `rmsd_benchmark`,
`s17_sub5_rmsd_benchmark`, `stress_test_20_sequences`, `validate_tau_fold`,
`s14_folding_kinetics`, `s15_allosteric_yield`, `s16_allosteric_pathway_map`,
`s17_dalembertian_allostery`, `s13_oligomer_assembly`, `s18_oligomer_assembly`,
`animate_villin_fold`, `plot_folding_progressions`.

**Sequencing recommendation for the AVE-Protein session:** land §A CONSTANTS first (R1-independent),
then land the §B honesty fixes whose framing is decoupled from the fold-mechanism (B14, B15 import-bug,
B18), and hold the impedance-fold-mechanism framing (the "validates / emerges / zero-parameter"
headline retractions) until clm-s11nf0 lands.

---

## Cross-cutting items (adjudicate in the AVE-Protein session)

1. **Dedup-adjudicate `s12_pdb_validation.py` vs `stress_test_20_sequences.py`.** They are
   title-identical near-byte-identical twins that call **different engines** (`fold_s11_jax` vs
   `fold_network` from `s_param_network_engine`). Consequence: a Vol-5 number is **non-traceable to a
   single engine**. Decide which driver/engine is canonical for the Vol-5 20-protein claim, or
   disambiguate both docstrings + the engine attribution.

2. **Adjudicate the v4 / `s_param_network` pathway vs the D5-locked v3-only scope.** `rmsd_benchmark.py`
   calls `fold_cascade_transient_v7` on the **v4** engine and `stress_test_20` calls `fold_network`
   (s_param/Y-matrix). Per the HANDOFF F3/D5 lock the v4 pathway **may be out of locked v3-only scope** —
   confirm before treating v4/s_param outputs as in-scope Vol-5 results.

---

## KEEP-AS-IS (positive patterns — do NOT flag/touch)

- **`s17_sub5_rmsd_benchmark.py`** Method-B+ label corrected from "Refinement" to **"Independent
  restart"** after the F2 print-vs-impl audit (Q-PROTEIN-10) — the good pattern; do not touch the label.
- **`protein_bond_constants.py:349-362`** the `R_WS` "BACK-FITTED NOT FIRST PRINCIPLES" deprecation
  block — exemplary honesty; cite as a positive, do not flag.

---

## R3 residuals (carry into that session — claim-quality, not fixes)

1. **`Q = ℓ ≟ 0.75π² = 7.402` asserted-coincidence** (`protein_bond_constants:512`, and the recurring
   integer-7 family) needs an **honest claim-quality tag** — it is a ~5.7% rounding coincidence asserted
   as an identity, not a derived equality.
2. **`d₀/a₀ = 7.18` (Vol-5) vs 7.22 (App-F)** — unreconciled cross-reference value.
3. **`Z_BOND_MEAN ≈ 3.338` vs `Z_backbone ≈ 17.0 Ω`** — two coexisting backbone-impedance scales;
   adjudicate which is the load-bearing baseline (note: the same `Z_backbone ≈ 17.x Ω` /
   `K_CN = 461 N/m` value is the carried-flag 17.6-vs-17.0 item in the AVE-Core
   `solvent_damping_analysis.py` — do NOT reconcile from a Vol-5 session).
