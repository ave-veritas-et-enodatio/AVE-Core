# Bound-constitutive lane — item-(0) consequence-audit sweep RECORD (committed artifact)

**Base:** AVE-Core `main` @ `6c291196` (the sweep ran against the main checkout at base; this
record is the committed per-site artifact the Tier-2 findings C9/C13/C15 required — the first
cut left it as an uncommitted session artifact and scored G-AX0-2M/G-NUM on it anyway).

**Engines (as run, disclosed):** Engine 1 = BSD `/usr/bin/grep -rniE` (GNU grep absent on this
host; the `grep` shim is ugrep 7.5.0, bypassed — instrument deviation, direction-of-effect:
none observed, engines agreed on every text file). Engine 2 = `python3` `os.walk` + `re`
independent walk. Scope: `manuscript/ research/ src/`, excluding `.git`, `worktrees`,
`_archive`, `__pycache__`/binaries.

**Pattern families (printed, per prereg row 11):**
1. `standard Maxwell|Maxwell Lagrangian|vector-potential form`
2. `U\(1\)` within a ±3-line window matching `Noether|gauge symmetry|follow`
3. `Noether`
4. `gauge invarian` (manuscript only)
5. `recovered as the substrate|effective action in the linear regime`

**Counts as measured (measure-then-edit pin; both engines):**

| Family | grep (BSD) | python re | Agreement |
|---|---|---|---|
| 1 | 37 | 36 | Δ=1 = one `.pyc` binary-match line (compiled docstring of `saturation.py:134`); text sets byte-identical |
| 2 | 9 (of 163 raw `U(1)` lines) | 9 | identical |
| 3 | 18 | 18 | identical |
| 4 | 12 | 12 | identical |
| 5 | 4 | 4 | identical |

**Union: 73 distinct pattern file:line sites** (79 raw − 6 cross-family duplicates:
`eq_axiom_3.tex:22`, `:27`, `qed-trace-charter.md:33`, `bound-response_prereg:16`,
`_result:35`, `ch05-electroweak-mechanics/index.md:11`) **+ 4 off-pattern known sites
verified by direct read** (`trampoline-analogy-primer.md:202`; `ave-kb/CLAUDE.md` INVARIANT-S2
Ax3 row; `01_fundamental_axioms.tex:64-71`; `the-abandoned-interior.md:22`) **= 77.**
The sweep is PATTERN-BOUNDED: paraphrase-only consumers outside the known-site list would
evade both engines equally.

## NEEDS-RESCOPE (10)

| # | Site | What breaks under the repair |
|---|---|---|
| 1 | `manuscript/common_equations/eq_axiom_3.tex:22` | the anchor: "standard Maxwell" true only on the Gauss-constrained surface; constraint absent from the written action |
| 2 | `eq_axiom_3.tex:27` | full time-dependent U(1) is not a symmetry of `\|∂_t A\|²`; residual `A → A + ∇λ(x)` only; energy-conservation clause survives |
| 3 | `manuscript/backmatter/02_full_derivation_chain.tex:153-154` | verbatim label copy of :22 |
| 4 | `manuscript/backmatter/12_mathematical_closure.tex:79` | same label |
| 5 | `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:299` | "enforces local gauge invariance" — exact content is the residual symmetry / discrete Gauss-generator conservation |
| 6 | `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md:43` | KB mirror of #5 |
| 7 | `manuscript/ave-kb/vol1/claim-quality.md:752` | second KB mirror of #5 |
| 8 | `manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md:66` | load-bears BOTH labels + "relativistic" against :27's own emergent-Lorentz demotion |
| 9 | `research/2026-07-14_qed-trace-charter.md:33` (+`:110`,`:168`; `qed-trace-beta-gate_prereg_FROZEN.md:30`) | hosts :27 verbatim; content survives as the Gauss-generator statement; FROZEN docs get dated surface-notes only |
| 10 | `manuscript/ave-kb/session/axiom-homologation.md:14` | parenthetical label; session-historical |

## DRIFT findings (4, confirmed at HEAD)

| ID | Site | Drift |
|---|---|---|
| D1 | `manuscript/backmatter/02_full_derivation_chain.tex:163-164` | still lists **Lorentz invariance** in the Noether list, against `eq_axiom_3.tex:27` at HEAD |
| D2 | `manuscript/ave-kb/common/axiom-register.md:174` vs `:231` | ":174 proven internal theorem" vs ":231 ASSERTED-not-derived" — the Ax3 equivalence status contradicts itself in one register |
| D3 | `axiom-register.md:173` | flat equivalence assertion against `eq_axiom_3.tex:37`'s necessary-not-sufficient flag |
| D4 | `01_fundamental_axioms.tex:71` | same pre-flag equivalence claim as D3 |

## TRUE-UNDER-REPAIR (bulk class; representative enumeration)

`frontmatter/00_foreword.tex:110`; `trampoline-analogy-primer.md:202` (off-pattern);
`01_fundamental_axioms.tex:79`; regime tables (`07_regime_map.tex:90`, `four-regimes.md:68`,
`regimes-of-operation.md:27`, `vol_9 …/02_absolute_maximum_ratings.tex:118`,
`14_phase_diagrams.tex:140`); `the-abandoned-interior.md:22` (MYTH-GUARD — with the lane's
caution: its "gauge slot" story is true of TEXTBOOK Maxwell; the WRITTEN action differs on
exactly that point until the constraint is supplied); `axiom-register.md:231` DERIVED column;
`bound-response_prereg-FROZEN.md:16` + `_result.md:35` (frozen; surface-note class);
`2026-08-06_iomega-law_result.md:280`; `2026-06-11_annihilation-evaporation_prereg.md:114`;
the 2026-05-18 research trio; all `src/` docstring sites (`saturation.py:134` + `.pyc`,
`fdtd_3d.py:87`, `fdtd_3d_jax.py:503`, `master_equation_fdtd.py:34`, `regime_map.py:450-451`,
`vacuum_engine.py:1477`, `q_g47_path_d_full_cross_validation.py:691,:703,:708,:712`,
`photon_chiral_yee.py:15`, `r10_master_equation_v14.py:13,:631`,
`r10_v8_2a_gamma_pair_production.py:14`, `r10_v8_o1_electron_ic_stability.py:7`,
`r8_diag_a_cosserat_wave_speed.py:11`, `test_fdtd3d_cavity_e_b_correlation.py:12`,
`test_fdtd_nonlinear.py:5,:24`).

## INDEPENDENT (with two flags routed)

`ave-kb/CLAUDE.md` INVARIANT-S2 Ax3 row (off-pattern; carries neither label; mild D3-adjacent
softness). The vol2 ch05 Helmholtz-U(1) complex (`05_electroweak_gauge_theory.tex:8,:30-31,
:35,:51,:137-159` + KB mirrors `gauge-boson-masses.md:28,:30,:34,:50`, `index.md:11,:29`,
`forward-to-ch6.md:40`; claim `clm-jkpfd4`) — self-derived, does not cite :22/:27. **Flags
(routed, flag-don't-fix):** (a) ch05's closure "a channel with no restoring force stores no
energy" is FALSE for time-dependent Λ (the kinetic term stores `½ε₀|∂_tA_L|²`) — per the
Tier-2 C22 correction, ch05 attempts the FULL single-valued time-dependent family and its
E-leg closure fails on exactly this point, so canon holds NO valid derivation of any U(1)
family; the residual time-independent family is the only exact statement. (b) the `:155`
Wilson-plaquette "recovers −¼F_{μν}F^{μν}" builds only the magnetic term from spatial
plaquettes — covariant-label overreach of the same A₀-less shape as the anchor.
Also INDEPENDENT: `electron-identification.md:102` (different thread);
`secondshell_screw_holonomy.py:18` (different U(1)); `.index/claims.jsonl` (generated);
`iomega_law_scan_results.json:103,:193` (generated snapshots, different Noether thread).

## Machine-checkable totals

```json
{"pattern_sites": 73, "off_pattern_sites": 4, "total": 77,
 "needs_rescope": 10, "drift": 4,
 "engine_disagreements_text_files": 0}
```
