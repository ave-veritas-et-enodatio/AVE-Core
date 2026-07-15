# THE 1/4 MAP — Quarter-Power Families, the One-Contour Test, and the Knee Ladder

> **Map-and-document research doc. Landed 2026-07-14 (Grant-authorized: "do the sweep
> regardless and paint the full circuit/picture/map and document").** Synthesized from a
> four-modality corpus sweep (prose/KB, adjudication-trail, git-history, operative-code);
> **every file:line anchor re-verified two-method against `AVE-Core @ bb58727f`** before
> landing. Anchors that failed re-verification were dropped or corrected — see the
> `## Re-verification corrections` appendix at the end. All numerics recomputed this
> session (CODATA `ALPHA = 7.2973525693e-3`; `2*ALPHA = 0.0145947051386`).
>
> **Base note:** branched from `bb58727f` (the synthesis's verification HEAD); `origin/main`
> had advanced to `c50a997f` when this landed — line-anchors are pinned to `bb58727f`.
>
> **Epistemic posture:** report-only map. The `r_knee` VALUE stays echo-classified per the
> knee-NOTE's own ruling (it rides the α-echo). No new KB claim; KB candidacy is routed to
> the auditor lane. All defect rows are **FLAGGED-NOT-FIXED** (flag-don't-fix): the hygiene
> burn-down is a QUEUED follow-on, not this doc's work.

## Kernel and contour conventions (the single largest source of historical churn)

- **Kernel:** `S(A) = (1 − A²)^{1/2}` (Op2, `src/ave/core/universal_operators.py:112`).
  **"Half-in-S = quarter-in-A²":** `√S = (1−A²)^{1/4}` but `S^{1/4} = (1−A²)^{1/8}`. The
  eighth-power `S^{1/4}` is the historical DEFECT (Family E); the quarter-power `√S =
  (1−A²)^{1/4}` is the physical register.
- **Knee contour:** `A² = 2α` (deficit `ΔS = 1−S = α + α²/2 ≈ α`). Coordinate authority
  `src/ave/core/chiral_lattice_v10.py:30` (`A_YIELD_SQ = 2.0 * float(ALPHA)`),
  `src/ave/core/constants.py:525` (`R_I = np.sqrt(2.0 * ALPHA)`). Ruled the **deficit knee /
  LOADING BC**, not the wall (`_orchestration/2026-07-10_rulings-docket.md:540,556`; Grant
  "accept!" :553).

---

## 1. MASTER TABLE — the nine families

~100 raw quarter-power sites collapse to **nine families**. One representative anchor per
member; duplicates folded. Every anchor below was re-verified two-method (`grep -F` for the
math literal + line-content confirmation) at `bb58727f`.

### Family A — the three story members (knee-contour evaluations)

| # | Quantity | Expression | Value | Anchor | Class | Status |
|---|---|---|---|---|---|---|
| A1 | Local clock at knee | `ω_local = (1−2α)^{1/4} ω_global` | 0.996331 | `op14-local-clock-modulation.md:22,44,54` | rate | **ADJUDICATED** (PR#690/#683 REPLACE; supersedes the provenance-unclear 0.95; the 0.22/0.84 half-exponent artifacts are KEEP-BOTH at :122) |
| A2 | Shear speed register | `c_shear = c₀√S = c₀(1−A²)^{1/4}` | — | `scale_invariant.py:294`; Op16 `universal_operators.py:1018` | velocity / register-flag | **RESOLVED in code** (Grant F1); **STALE "not settled" flag survives** at `manuscript/common_equations/eq_axiom_4.tex:47` |
| A3 | Knee radius (field-strain) | `r_knee = (2α)^{−1/4} ℓ_node` | 2.877 ℓ_node ≈ 1.11 pm | `research/2026-07-14_knee-contour-check_NOTE.md:144,180,226` — **BRANCH `analysis/knee-contour-check` (PR #696), NOT on main** (code-span cite, not md-link) | length | measured, resolution-stable, `= r99` outer envelope (ratio 1.06); **echo-classified / report-only** (:248); field-vs-voltage-strain fork OPEN (:241) |

`(1−2α)^{1/4} = 0.9963311827` and `(2α)^{−1/4} = 2.8770749` recomputed this session;
`2.877 × λ̄_C (0.38616 pm) = 1.111 pm`. The A3 value is NOT landed into the KB and stays
report-only per the knee-NOTE ruling.

### Family B — kernel √S projections (the ONE-kernel family; all live-canonical)

Every member is `(1−A²)^{±1/4} = S^{±1/2}` at some operating point — same kernel, different
port. The corpus has ALREADY adjudicated this as ONE kernel: `gw_propagation.py:374-375`
("`(1 − A²)^{1/4}` … is a DERIVED projection … NOT a second kernel; … never used AS the
kernel"), `grqed-stage1 result:40,56`, `test_l1_multiwave.py:54` (base-notation identity
discharge — the two notations AGREE, :56).

| Member | Form | Sign | Anchor (canonical) | Notes |
|---|---|---|---|---|
| Node/varactor clock | `Ω_node = ω₀(1−A²)^{1/4}` | + | `vacuum_engine.py:552,806`; origin `research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md`; tests `test_axiom_4_vacuum_varactor.py:59`, `test_phase2_node_resonance.py:103` | `ω = 1/√(LC)`, `C_eff = C₀/S` — the BIRTH site of the quarter power |
| Komar / clock weight | `w = √S` | + | `gravity/backreaction.py:252` (pins DEC-1 `exponent=0.5`, "NO new kernel" :246) | clock-deficit ledger consumes `1 − √S ≈ A²/4` (`:420`) |
| c_shear (matter/GW) | `c₀√S` | + | `scale_invariant.py:294`, `gw_propagation.py:294`, `rupture_solver.py:120`, `categorization.py:239`, facade `unified_engine.py:413`, spine `_transverse.py:85` | Schwarzschild identity `(1−A²)^{1/4} ≡ √(1−r_s/r)` (`dark-sector-response-characterization.md:228`; datasheet `05_ac_electrical_characteristics.tex:552`) |
| c_EM stiffening | `c₀(1−A²)^{−1/4}` | − | `master_equation_fdtd.py:13,166` (`c_eff² = c₀²/S`); `regime_map.py` | opposite-sign branch (bulk/A1-cage); the wave-typing fork |
| Birefringence n_⊥ | `(1−A²)^{1/4} ≈ 1−¼A²` | + | `src/ave/qed/birefringence.py:66`; `vacuum-birefringence-e4.md:97`; bench `src/ave/bench/birefringence.py:159,179` (`expm1(0.25·log1p(−A²))` guard) | **the flagship falsifier observable IS a quarter-power kernel projection**; symbolically checked (`bench/birefringence.py`) |
| n_∥ mixed | `√[(1−2A²)/√(1−A²)]` | mixed | `src/ave/qed/__init__.py:19`; `vacuum-birefringence-e4.md:97` | half×quarter product of the SAME kernel |
| Op4/Op14 impedance dress | `Z = Z₀/(1−(d_sat/r)²)^{1/4}` | − | `universal_operators.py:184,229`; `operators.md:44`; `pairwise-potential.md:20`; `qed_trace_beta_gate.py:108` (running-α reactive register, 2026-07-14) | inverse-square field strain feeding the pinned quarter — the r_knee generator shape |
| μ-load short / mirror | `Z₀√S → 0, Γ→−1` | + | `crystal_engine.py:483`; `vacuum_varactor_scatter.py:199`; Op14 load flag `universal_operators.py:828` | sign = load-type selector (electric OPEN `/√S` vs magnetic SHORT `·√S`) — H3-degenerate class |
| ASYM sector split | `Z = Z₀√(S_μ/S_ε)` | ± | `cosserat_field_3d.py:1852`; `graded-network-response.md:165`; `categorization.py:245-249` | SYM ⇒ `Z = Z₀` invariant — the loading-symmetry switch that decides whether Z carries any ¼ at all |
| Vacuum-impedance-mirror falsifier | `Z₀(1−(V/V_y)²)^{−1/4}` | − | `vacuum-impedance-mirror.md:92` (`clm-5s5b0d`) | bench-facing |
| Superband force / energy | `F ∝ r/√S`, `U ∝ 1−(1−r²)^{3/4}` | — | `superband_carrier_fork.py:80,110` | ¾ = integral of the ¼ force; kernel-derived |
| Aperture skewness | `S₀^{1/4}` | + | `parametric-coupling-kernel.md:456` | stacked half-powers of the kernel |
| Bond propagation | `f_ij = (S_i S_j)^{1/4}` | + | `research/_archive/L3_electron_soliton/111_master_equation_audit_and_engine_gap.md` | geometric mean of two √S |
| Coefficient-¼ class | `δn ≈ −¼A²`, `δC = ¼C₀(V/V_y)²`, `Γ-gradient ¼`, `pc = −0.25` | — | `parametric-coupling-kernel.md:70`; `p4_forward_voltage_threshold.py:263`; `cosserat_field_3d.py:627` | O(A²) Taylor projections of the same kernel — same contour, coefficient guise |

### Family C — kernel-adjacent, DIFFERENT base (mechanism-isomorphic, contour-foreign)

| Member | Form | Anchor | Note |
|---|---|---|---|
| Be cascade correction | `k_eff = k_pair/(1+k_inner)^{1/4}` | `hierarchical-cascade-correction.md:30-31`; `radial_eigenvalue.py:2018` | in-corpus statement that ¼ = √∘√ (normal-mode `(1+k)^{1/2}` then coupling `√`); base is `(1+k)`, NOT the deficit kernel; **already adjudicated a coincidental collision** |

### Family D — non-kernel quarter-powers (imports / dimensional analysis)

| Member | Form | Anchor | Provenance |
|---|---|---|---|
| MOND / Tully-Fisher floor | `v_flat = (GM a₀)^{1/4}` | `translation-gravity.md:25` (+ dupes) | √∘(inverse-square) of dimensionful imports; the corpus's FIRST chased ¼ (2026-02-13) |
| Kolmogorov microscale | `η = (ν³/ε)^{1/4}` | `regime_3_saturated/kolmogorov_cutoff.py:59` | standard turbulence import |
| Stefan-Boltzmann | `T ∝ (…)^{1/4}` | `Applied-Vacuum-Engineering …/06_02_model.tex:12` — **cross-repo, NOT in this AVE-Core checkout (anchor unverified here)** | historical: FIRST ¼ in the corpus lineage (2026-02-10), T⁴ inversion |
| Shakura-Sunyaev disk | `(1−√x)^{0.25}` | `simulate_gargantua_acoustic_vortex.py:261` | astrophysics import |
| Higgs VEV (EXCLUDED) | `(√2 G_F)^{−1/2}` | `constants.py:670` | inner sqrt acts on the constant 2 — NOT a kernel/coupling quarter-power; excluded |

### Family E — legacy `S^{1/4}` = (1−A²)^{1/8} defect (history + live residue)

The genuine bug class: an eighth-power-in-A² matching NEITHER physical register. Corrected in
the engines (`master_equation_fdtd.py:176,188`; `k4_tlm.py:292` — "prior `S_factor**0.25`
(`= (1−A²)^{1/8}`) … off by a factor of 2 … corrected to `sqrt(S_factor)`"; `crystal_engine.py:431`).
**Zero surviving `S**0.25` c_shear/kernel assignments in live `src/ave`.** Surviving residue
(all FLAGGED-NOT-FIXED):

| Residue | Anchor | Kind |
|---|---|---|
| `1/64` reflection coefficient from a legacy `Z = Z₀/S^{1/4}` chain | `cosserat_field_3d.py:453,482` (`reflection = (1.0/64.0)*grad_S_sq/(S*S+eps)`) | **live operative code**; corrected register (`Z=Z₀/√S`) implies `1/16` |
| "not settled" flag + stale `refractive_index() returns S^{1/4}` claim | `eq_axiom_4.tex:47` | stale vs code (impl returns `S**0.5` at `fdtd:188`) — doubly stale, honesty-lag |
| Stale docstrings | `boundary_invariants.py:31-32` (impl `:132` is correct `S**-0.5`); `crystal_graft_v2.py:87` `Γ_floor` formula | doc/code mismatch in-file |
| Legacy-exponent figure/verify scripts | `cvr_model.py:126` (deliberate AS-CODED exposure); `apparatus_floor_wall_run.py:78`; `test_gamma_sign_gate.py:138` | figure/regression anchors, no gates |
| Live KB `Z = Z₀/S^{1/4}` leaves | `k4-tlm-lensing-validation.md:22`; `k4-tlm-simulator.md:44` | the impedance-law discrepancy that let the bug ride in — un-propagated |
| DEC-1 sensitivity knob | `graded_vacuum_network.py:295,306` (`exponent ∈ {0.5, 0.25}`, primary 0.5) | deliberate robustness knob, adjudicated robust — but can silently propagate 0.25 |

### Family F — VALUE-¼ lane (NOT an exponent; closed-negative; do not conflate)

`R·r = 1/4` Golden-Torus identity (`08_alpha_golden_torus.tex:69`) — Class-B **standing echo**,
every named route closed-negative with the flip-condition LIVE (`interlock-register.md:236-248`;
α-free flip on record `forka-alpha-flip_prereg.md:14`; the ½/¼ over-determination = coincidence-
magnet tell). **A different object from the quarter-POWER story.** (Synthesis's
`translation-circuit.md:252` rescue pointer dropped — that file is 16 lines; see corrections.)

### Family G — quarter-ARC (kernel SHAPE, not power)

`S(A)` traces a quarter circle — the "universal quarter-arc kernel" (`axiom-register.md:186`;
`∫₀¹√(1−A²)dA = π/4`); SHAPE-DERIVED (conditional), L2-norm-forced (:187-188). A different
"quarter."

### Family H — stale / superseded numerics

The 0.22/0.84 half-exponent artifacts (op14 leaf `:105,:120,:122` KEEP-BOTH; origin
`research/_archive/L5/axiom_derivation_status.md:204`); the superseded 0.95 (op14 `:120`, carrying
the A²-vs-√(2α) slip); `electron-bind-sim_result.md:59` uses the superseded `√(1−A²)` clock at
`A=√α` and lands on 0.9963 only via the near-collision (§4); **`chiral_drive_selforbit.py:173`
LIVE** clock `ω₀·√(1−A²) = ω₀(1−A²)^{1/2}` — a half-exponent clock in operative code disagreeing
with the ratified √S.

### Family I — register-fork on the knee amplitude itself

`loop_gap_seeds.py:26` pins `A_YIELD = √α` (no 2) — same √α register in `regime_map.py:369` — vs
`constants.R_I = √(2α)` / `chiral_lattice_v10.py:30`. A quarter-power projected from the √α
register differs from `(2α)^{−1/4}` by `2^{1/4} = 1.189` — a silent 19% address error if
conflated. **Separately:** `lense_thirring.py:172` is a hardcoded `(2·α)^{0.5} = √(2α)` literal
(the R_I register, inlined instead of importing `constants.R_I`) — a should-import hygiene item,
NOT a √α-register member (synthesis mis-grouped it; see corrections).

## 2. THE ONE-CONTOUR TEST

**SECTOR:** kernel-projection algebra (Op2 `S` → each wave/impedance register). **REGIME:**
general operating point (H-weak) vs the deficit-knee contour `A²=2α` (H-strong).

**Hypothesis as posed:** all quarter-power sites are projections of ONE kernel contour
(`A²=2α` deficit knee) through square-root dispersion relations. **The test splits into two
claims with different verdicts.**

### H-weak (one KERNEL, many √-projections): **HOLDS** for every Family-B site — corpus-adjudicated

Common algebra: `S(A) = (1−A²)^{1/2}`; every physical register applies exactly one more
half-power. Each site reduces to `(1−A²)^{±1/4}` with a NAMED one-sqrt chain:

| Site | Projection chain (algebra) | Reduced form | At knee `A²=2α` |
|---|---|---|---|
| Clock / Ω_node | `C_eff = C₀/S` (varactor ε-load) ⇒ `ω = 1/√(LC_eff) = ω₀ S^{1/2}` | `(1−A²)^{+1/4}` | `(1−2α)^{1/4} = 0.996331` — **member 1, exact** |
| c_shear | `G_eff = G₀·S` ⇒ `c = √(G_eff/ρ) = c₀ S^{1/2}` | `(1−A²)^{+1/4}` | 0.996331 (clock RIDES this — same number by construction) |
| c_EM (stiffening) | `c_eff² = c₀²/S` ⇒ `c₀ S^{−1/2}` | `(1−A²)^{−1/4}` | `(1−2α)^{−1/4} = 1.003682` |
| Z (single-sector) | `Z = √(L_eff/C_eff)`; one sector loaded ⇒ `Z₀ S^{±1/2}` | `(1−A²)^{∓1/4}` | `1 ∓ 0.003682`; **sign = load selector, not a power question** |
| Γ at knee | `Γ = (√S−1)/(√S+1)` | `≈ −A²/4` | computed **−0.001838 ≈ −α/4** (`α/4 = 0.001824`; docket's `Γ≈−0.002` ✓) |
| r_knee | field strain `A(s) = (d_sat/s)²` (inverse-square); invert at `A = A_yield = (2α)^{1/2}`: `s = d_sat·A_yield^{−1/2}` | `(2α)^{−1/4}` | **2.877 ℓ_node — member 3, exact** (`= 1/√(A_yield)`) |
| n_⊥ / δn / δC / ¼-coefficients | Taylor of the above at small A | `1−¼A²` etc. | O(A²) guise of the same kernel |
| Aperture `S₀^{1/4}`, bond `(S_iS_j)^{1/4}`, superband ¾ | stacked half-powers / integrals of the above | kernel functions | arbitrary operating point |

Corpus precedent for exactly this reading: `gw_propagation.py:374-375`, `grqed-stage1
result:40,56` ("DERIVED √S projection, NOT a second kernel"), Grant F1 (`S^{0.25}` is a
reduced-form via a factor-of-2 projection). Every genuine kernel quarter-power writes as
`(1−A²)^{p/4}` (or `(2α)^{p/4}` on the knee) with `p ∈ {−1,+1}` and a nameable one-sqrt chain.

**Affirmative evidence (the algebra detects errors):** the ONE deviation ever found — the
`S^{1/4} = (1−A²)^{1/8}` engine index — matched NO chain and was KILLED as a defect (`k4_tlm.py:292`,
`master_equation_fdtd.py:176`, `crystal_engine.py:431`). A wrong exponent is detectable because
the projection algebra is tight enough to reject it.

### H-strong (one CONTOUR — all sites live AT `A²=2α`): **FAILS.** The five falsifiers:

1. **Be cascade `(1+k_inner)^{1/4}`** (`hierarchical-cascade-correction.md:30-31`;
   `radial_eigenvalue.py:2018`) — √∘√ mechanism, but the base is a coupling stack `(1+k)`, not
   the deficit kernel; no α; no knee. *Mechanism-shared, contour-foreign.*
2. **MOND `v_flat = (GM a₀)^{1/4}`** (`translation-gravity.md:25`) — √∘(inverse-square), the SAME
   composition class as r_knee, but of dimensionful imports with no kernel and no α.
   *Composition-shared, contour-foreign.*
3. **Kolmogorov η, Stefan-Boltzmann T, Shakura-Sunyaev** — dimensional/thermal quarter-powers;
   no kernel content at all.
4. **Off-contour kernel sites** — birefringence n_⊥, Op4 dress `Z(r)`, aperture `S₀^{1/4}` are
   kernel projections evaluated at *arbitrary* A, not the knee. They share the kernel, not the
   contour.
5. **★ The voltage-strain fork (the sharpest internal falsifier).** Under the canonical
   `methodological-contamination.md:48-52` voltage strain `A = d_sat/r` (`∝ 1/r`), the knee radius
   is `d_sat/√(2α) = 8.278 ℓ_node` — a **HALF-power** (recomputed: `1/√(2α) = 8.2776`). The
   quarter-power radius exists ONLY under the inverse-square FIELD composition `A = (d_sat/s)²`.
   **Member 3's ¼-membership is therefore conditional on an OPEN fork** (knee-NOTE :241, branch
   `analysis/knee-contour-check`).

**Honest verdict for the map:** *"Every kernel quarter-power in the corpus is √S of the ONE
kernel, and the three story members are that projection evaluated at the ONE knee contour
`A²=2α`"* — with Families C/D fenced out as generic sqrt-composition algebra, and member 3
fork-conditional.

## 3. c_shear ADJUDICATION INPUT (present-both, no ruling)

**SECTOR:** shear / matter-clock (deviatoric G-modulus). **REGIME:** cold→loaded, deficit
knee at `A²=2α`. Present-both; the exponent question is presented, NOT ruled here.

**What shipped code implements — `c_shear = c₀·√S = c₀·(1−A²)^{1/4}`, uniformly, in every
live path:**
- Op16 `universal_operators.py:1018,1022` (`c_base * (1.0 - ratio_sq) ** 0.25`)
- `scale_invariant.py:294` (canonical docstring + `local_wave_speed` returns `c_base·√S`)
- `gw_propagation.py:294` (`C_0 * np.sqrt(S)  # c·(1 − ε₁₁²)^(1/4)`)
- `rupture_solver.py:120` (`C_0 * np.sqrt(S)  # c₀·√S = c₀·(1−r²)^{1/4}`)
- `categorization.py:239` (`c_shear = float(np.sqrt(S))`)
- facade `unified_engine.py:413` (`"c_shear_over_c0": np.sqrt(S)`)
- acceptance spine `_transverse.py:85` (the "CONSTITUTIVE IDENTITY")

The competing `S^{1/4}` (`= (1−A²)^{1/8}`) survives NOWHERE as a live c_shear. It persists only
as: the DEC-1 sensitivity knob (`graded_vacuum_network.py:295,306`, adjudicated robust), figure/
regression anchors, two stale docstrings, the live `1/64` coefficient (`cosserat_field_3d.py:482`),
and the un-flipped `eq_axiom_4.tex:47` flag.

**What the one-contour identity PREDICTS — `c₀√S` — via two independent forcings:**
- **(a) The clock adjudication is upstream and the clock rides c_shear.** PR #690 ratified
  `ω_local = (1−2α)^{1/4}` at the knee (op14 leaf `:22`), and `ω_local = ω_global·c_shear/c₀`.
  If c_shear were `c₀·S^{1/4}`, the knee clock would be `(1−2α)^{1/8} = 0.998164` — contradicting
  the adjudicated 0.996331. (Both recomputed this session.)
- **(b) The dispersion chain admits exactly one half-power.** `G_eff = G₀S`, `c = √(G/ρ)` gives
  one √. An `S^{1/4}` would require a quarter-root dispersion relation that exists nowhere in the
  circuit vocabulary.

**Net:** shipped register and one-contour prediction **AGREE** (√S). The residual work is
**hygiene** (Family-E residue), NOT physics — **with one exception:** the *sign/ontology*
selector (`n = S^{+1/2}` matter/bending vs `S^{−1/2}` binding wall; plan §ii-b; Op14 Z-sign note
`cosserat_field_3d.py:422`) is a genuinely separate, still-open question, orthogonal to the
exponent, and stays **PENDING Grant**.

## 4. THE CIRCUIT MAP — radial ladder with the quarter-power identity overlaid

**SECTOR:** graded vacuum-impedance network (all three channels). **REGIME:** strain A rises
inward along the Op4 field composition `A(s) = (d_sat/s)²`. **Ladder: far-field → knee → dress
→ wall → floor.**

| Rung | Quantity | Value at rung | Projection chain | Corpus site | Status |
|---|---|---|---|---|---|
| Far-field (A→0) | everything | `S=1`; Maxwell exact; `Z=Z₀=√(μ₀/ε₀)` | — | `constants.py`; Op2 `universal_operators.py:112` | canonical |
| **KNEE (`A²=2α`)** | radius (field-strain) | `r_knee = (2α)^{−1/4} ℓ_node = 2.877 ℓ_node ≈ 1.11 pm` | inverse-square field ∘ threshold-√: `s = d_sat·A_yield^{−1/2}` | knee-NOTE `:144,:226` (**branch/PR #696**) | measured, report-only, echo-classified; **fork:** voltage-strain twin = 8.278 (half-power) |
| KNEE | clock | `ω_local = (1−2α)^{1/4} ω_global = 0.996331` | `C_eff=C₀/S`, `ω=1/√(LC)` | op14 leaf `:22` | **adjudicated** (PR #690) |
| KNEE | c_shear | `0.996331 c₀` | `G_eff=G₀S`, `c=√(G/ρ)` | `scale_invariant.py:294` | canonical code (register RESOLVED; stale tex flag) |
| KNEE | Z | `Z₀(1−2α)^{∓1/4} = Z₀(1 ∓ 0.003682)` | `Z=√(L/C)`; sign = load selector | `universal_operators.py:828`; open sign note `cosserat_field_3d.py:422` | canonical magnitude; **sign reconciliation OPEN** |
| KNEE | Γ magnitude | `≈ −α/4 ≈ −0.001838` (engine: −0.002) | `Γ=(√S−1)/(√S+1)` | rulings-docket `:540` | **ruled** — knee is LOADING BC / port, NOT wall |
| KNEE | deficit | `ΔS = α` (exactly `α+α²/2`) | contour definition | `chiral_lattice_v10.py:30` | coordinate authority |
| KNEE | role | r99 outer envelope of the coupling-correction cloud (ratio 1.06) | — | knee-NOTE `:180` | branch-corroborated; F5 knee-vs-wall tension KEEP-BOTH |
| Dress (`2α < A² ≪ 1`) | pairwise Z(r) | `Z₀/(1−(d_sat/r)²)^{1/4}`, running-α reactive register | Op4 inverse-square ∘ `Z=√(L/C)` | `universal_operators.py:229`; `qed_trace_beta_gate.py:108` (2026-07-14) | canonical; freshest site |
| Wall (S→0) | Z, Γ | `Z→0` (μ-short) or `→∞` (ε-open); `Γ→∓1`; c_shear→0 (freeze), c_EM→∞ (steepen) | same chains, saturated limit | `crystal_engine.py:483`; `mass-closure-theorem.md:40`; `node_2domain_nport.py:468` | canonical; quantizing BC (mirror) per docket `:555` |
| Floor (apparatus) | Γ_floor | `(n−1)/(n+1)` at `S_min` clip; −0.2400 legacy vs −0.4539 physical | apparatus clip, not physics | `apparatus_floor_wall_run.py:78` | flagged/qualified — apparatus artifact |

### ★ THE NEAR-COLLISION HAZARD ROW (mandatory annotation on the map)

`√(1−α) = 0.9963446` (CVR `|Γ|`; the `A²=α` coordinate) **vs** `(1−2α)^{1/4} = 0.9963312`
(knee clock; the `A²=2α` coordinate) — **identical to `1.35e-5`** (both `= 1 − α/2 + O(α²)`;
diff recomputed this session `= 1.346e-5`). Two different contours through different √-chains
produce indistinguishable 0.9963s: `cvr-reflection-smith.md:38` (`|Γ| = √(1−α) ≈ 0.99635`) vs
op14 `:22` (`(1−2α)^{1/4} ≈ 0.9963`).

**One mis-use already found (verified this session):** `electron-bind-sim_result.md:59` records
`ω_local(r) = ω_global·√(1−A²) = 0.9963 at A=√α`. That is the **half-exponent** clock (`S`, not
`√S`) evaluated at the **`A²=α`** coordinate — a DIFFERENT (exponent, contour) pair from the
knee's quarter-exponent at `A²=2α`, yet numerically indistinguishable via the near-collision.
(In that doc the 0.9963 was not load-bearing — the result was Class-C/inconclusive, `:60,:62` —
so no downstream claim broke; the hazard is that a load-bearing use could.)

**Mandate proposal (routed to auditor lane):** every `0.9963` in the corpus carries a **contour
tag** — `A²=α` (CVR `|Γ|`, half-exponent) vs `A²=2α` (knee clock, quarter-exponent). Without the
tag the rate alone cannot discriminate the contour.

## 5. PHASE-SPACE READING (WALK-LEVEL)

> **WALK-LEVEL — Grant-walked 2026-07-14, in-chat.** This section is a framing walk, NOT a
> corpus-derivation. It rides on two already-canonical phase-space facts and adds a reading of
> the anatomy; the reading itself is not asserted as derived. Per A46 (phase-space coordinate
> discipline): the corpus quarter-power claim lives in phase space, so its natural coordinates
> are the impedance/action plane, not lattice-Cartesian.

**Two canonical anchors this walk rides on:**
- The lossless bond-LC tank's dynamical phase-plane vector `(V/V_max, Φ/Φ_max)` traces a
  machine-precision **circle** — the L2 invariant is FORCED for the dynamical `(V_inc, Φ_link)`
  pair (`axiom-register.md:188`).
- The `(V_inc, V_ref)` phasor trajectory closes as the `(2,3)` winding on the **Clifford torus**
  (`08_alpha_golden_torus.tex:28`), the static phase-space embedding the seed carries.

**The walked mapping (framing):**
- **orbit area = action = `A²`** in yield units (`A² = 2α` at the knee is an enclosed-action
  contour, not a radius).
- **impedance = the orbit-ellipse aspect ratio** (`Z/Z₀` is how squeezed the phase-orbit is;
  a circle is `Z=Z₀`, matched).

**The anatomy in phase space (the radial ladder, re-read):**
- **far-field** → circular orbits (`A→0`, `Z=Z₀`, `Γ=0`).
- **KNEE** → the **eccentricity-onset contour** (enclosed action `= 2α`; squeeze `Γ ≈ α/4`) —
  the first departure from a matched circle.
- **dress** → a squeeze GRADIENT (the orbit ellipse tightening with depth).
- **wall** → a **fully-flattened orbit** = a pure standing wave. *(This is what total internal
  reflection IS in phase space: the orbit collapses to a line, `|Γ|=1`.)*

**The cross-register rule (the punchline of the walk):** half-powers live *within* one register;
**quarter-powers appear exactly when a quantity crosses the real-space ↔ phase-space boundary.**
The knee RADIUS `r_knee = (2α)^{−1/4} ℓ_node` is the **real-space shadow of a phase-space action
contour** `A²=2α`: the `²` of the field-strain composition `A=(d_sat/s)²` is the register-crossing,
and it is precisely that crossing that turns the half-power (`√(2α)`, staying in one register)
into the quarter-power (`(2α)^{−1/4}`, crossing registers). This is why the voltage-strain twin
(`A=d_sat/r`, no register crossing) is a half-power and the field-strain radius is a quarter.

**Registered companion observable (walk-level):** the phase-space twin of gate (b) (the knee-NOTE
r99 / coupling-correction adjudicator) — **orbit eccentricity vs enclosed action** — measured in
the impedance plane rather than as a lattice radius. Registered here as a candidate; not yet a
pre-reg.

## 6. BIQUATERNION BINDING

> **Corpus-thread verification FIRST (this section's gate).** Grepped AVE-Core (KB + research
> + src + manuscript) for biquaternion / complex-quaternion / Clifford / SL(2,ℂ) / SU(2) /
> double-cover content. **A substantial corpus thread EXISTS** (193 "biquaternion", 999
> "Clifford", 108 "double cover", 409 "double-cover", 24 "SU(2)" hits; a dedicated KB leaf +
> a verify driver + result docs). So the walked mapping is bound to it honestly — NOT landed
> as a home-less proposal.

**The corpus thread (canonical anchors):**
- KB leaf `biquaternion-complex-coupled-network-equations.md` (Class-C consistency synthesis).
- Result `research/2026-06-06_biquaternion-node-algebra-result.md` (the node-algebra
  prove-or-disprove, with the G1–G3 genuinely-new gates).
- `src/scripts/vol_1_foundations/verify_biquaternion_node_algebra.py`.

**The corpus thread's VERDICT (load-bearing — the mapping is real but consistency-class):**
the biquaternion is a **CONSISTENCY-CLASS re-expression, G1–G3 FAIL** (result `:13-21`):
- **G1** (does ONE algebra FORCE closure + longitudinal + Möbius to co-occur?) — **FAIL**: they
  co-occur (`SU(2) ⊂ SL(2,ℂ)`; scalar grade; null cone) but this is standard math over
  already-canonical, independently-substrate-derived facts; no new primitive.
- **G2** (does it forward-derive `α⁻¹ = 4π³+π²+π`?) — **FAIL**: the grades give the dimensional
  skeleton `{3D,2D,1D}`, none of the π-powers.
- **G3** (does it force a NEW testable longitudinal prediction?) — **FAIL**: re-expresses *why*
  (Heaviside's deleted scalar), adds no new number/dispersion/coupling.

The leaf `:84` states it outright: unit biquaternions `≅ SL(2,ℂ)`, adjoint action = the Lorentz
group (textbook — Silberstein 1912/14, Conway, Lanczos); **"AVE adds no new algebra here — the
biquaternion is coupling-layer notation (G1–G3 FAIL)."**

**Honest bind of the walked rotation/boost split to this thread:**

| Walked register (§5) | Biquaternion object | Corpus anchor | Status |
|---|---|---|---|
| **real quaternion part = ROTATION register** | real unit quaternions = `SU(2)` (the `i,j,k` rotation/spin sector); the `4π`-closure of `SU(2)`'s double cover is its instrument; Cosserat winding / the `(2,3)` integers ride this grade | result §3 `:75,:154,:159`; leaf rotation-flavor tag `:73` | structure holds; consistency-class |
| **imaginary (ι) part = BOOST / SQUEEZE register** | the `ι`-complexification → `SL(2,ℂ)` Lorentz action = the `Γ`/impedance Möbius reflection on the Smith sphere; activates at the `ΔS=α` eccentricity-onset contour (§5), saturates at the wall (`Γ→∓1`) | result §5 `:263,:270,:276`; leaf `:79,:84` | structure holds; consistency-class |

**The one honest divergence to flag (flag-don't-fix).** The corpus leaf's PRIMARY decomposition
is a DIFFERENT axis-assignment: the scalar slot `w = V_A1 + ι·Q_wind` splits **`Re(w)=V_A1`
(A1 dilatation / mass "3", leaf `:70`)** vs **`Im(w)=Q_wind` (charge = Link integer / shear "3",
leaf `:71`)** — a mass-vs-charge split, NOT rotation-vs-boost. The walked rotation/boost split
corresponds instead to the GROUP structure (`SU(2)` real ↔ `SL(2,ℂ)` complexified), which the
result doc §3/§5 establishes but which is *orthogonal* to the leaf's port-slot decomposition.
**Same object, two different reading-axes** — the walked reading shares the biquaternion with the
corpus thread and matches its §3/§5 group structure, but it is not the leaf's §1 port-slot
assignment, and it inherits the corpus's consistency-class (G1–G3 FAIL) verdict. It earns no
chord credit; it is a re-expression with a corpus home.

## 7. DISCRIMINATION CHECK (symmetric standard)

**The generic fence (NOT distinct).** A quarter-power from composing two square roots is
textbook algebra — standard physics mints them constantly (Stefan-Boltzmann, Tully-Fisher fits,
Kolmogorov, disk profiles; all present here as Family-D imports). Likewise **any rate/index of
the form `1 − α/2 + O(α²)`** (the 0.9963 class): at leading order it is an unlabeled small kernel
correction, degenerate with `√(1−α)` and with generic `O(α)` shifts — the near-collision (§4)
proves rates cannot discriminate the contour. **Symmetric standard applied:** the Standard Model
produces small-α-correction rates everywhere and gets a pass; AVE's 0.9963 rate class earns no
chord credit either.

**Candidate AVE-distinct content — the α-power bookkeeping of LENGTHS.** SM observables carry
*integer* powers of α between length rungs (`λ̄_C → a₀ = λ̄_C/α → r_e = α·λ̄_C`); amplitudes carry
`α^{1/2}` (via `e = √(4πα)`); **no SM observable is an `α^{1/4}` length ratio.** `r_knee/ℓ_node =
(2α)^{−1/4}` is a physical length at a quarter-power of the coupling above the node/Compton rung
(1.11 pm, sitting between `λ̄_C` and `a₀`) — a FORM SM does not make. Per the FORM-deriving /
VALUE-importing meta-finding, the **FORM is the candidate; the VALUE rides the α-echo** (knee-NOTE
`:248` already classifies it consistency-class, and this doc keeps it report-only).

**What would COUNT as an observable consumer** (the criterion that decides chord-vs-identity):
- a measurable onset/knee in the running-α reactive register at momentum transfer `q ~ 1/r_knee`
  (the `qed_trace_beta_gate.py:108` dress is the natural host);
- a correction-cloud (`r99`) envelope signature in a form-factor;
- a bench observable whose GAP-dependence pins `2.877 ℓ_node` against the `8.278` voltage-strain
  twin — which *simultaneously adjudicates the fork* (a Cleave-01-style gap-independence design).

**The honest kill-line:** *if nothing observable consumes `r_knee`, the length member is internal
bookkeeping and the ¼ story has no chord, only a tidy identity.*

**Explicitly NOT distinct:** the clock 0.996 (rate = small correction); the birefringence `−¼A²`
coefficient *as a quarter-power claim* (its distinctness case is the E-route coefficient vs
Euler-Heisenberg — already the flagship lane; the ¼ exponent adds nothing to it); the c_shear
register (internal consistency); everything in Families C/D.

## 8. GRANT'S OPEN QUESTIONS (ranked)

> **All defect rows are FLAGGED-NOT-FIXED (flag-don't-fix).** This doc surfaces contradictions
> with verbatim evidence + file paths; it does NOT silently reconcile them. The Family-E hygiene
> burn-down is a **QUEUED follow-on PR (auditor-lane KB fixes + engine hygiene), not this lane's
> work.** Each defect site below was re-verified live at `bb58727f`.

1. **Field-strain vs voltage-strain fork** (knee-NOTE `:241`, branch `analysis/knee-contour-check`).
   Field strain `A=(d_sat/s)²` gives `r_knee = 2.877` (quarter-power); canonical
   `methodological-contamination.md:48-52` voltage strain `A=d_sat/r` gives `8.278` (half-power).
   This decides whether member 3 is in the ¼ story AT ALL — the one-contour hypothesis's own
   kill-test. Walk-the-picture candidate: which strain does the cell at radius `s` actually feel?

2. **Does any observable consume `r_knee`?** (§7.) Without a consumer, adjudicate the ¼ map as
   identity-class and stop polishing it.

3. **Op14 Z sign / load reconciliation.** `cosserat_field_3d.py:419-423` OPEN flag: the `Z=Z₀/√S`
   form coexists with the live-wall SHORT `Z=Z₀·√(S_μ/S_ε)` in the SAME file, and with
   `operators.md:54` (`Z₀/√S`) vs `k4-tlm-lensing-validation.md:22` (`Z₀/S^{1/4}`). Which sign does
   the knee port present? (Feeds the §ii-b sign/ontology item, PENDING.)

4. **Live half-exponent clock** `chiral_drive_selforbit.py:173` (`ω₀·√(1−A²)`, VERIFIED live) —
   defect vs deliberate different-sector clock? Same class as the corrected op14 half-exponent.
   **FLAGGED-NOT-FIXED.**

5. **Family-E residue burn-down** (single hygiene PR, QUEUED): `eq_axiom_4.tex:47` stale flag +
   stale `refractive_index() returns S^{1/4}` claim (code returns `S**0.5` at `fdtd:188`);
   `cosserat_field_3d.py:482` **`1/64 → 1/16`** (the live coefficient off the legacy `Z=Z₀/S^{1/4}`
   chain at `:453`); `boundary_invariants.py:31-32` + `crystal_graft_v2.py:87` docstrings; KB
   `Z=Z₀/S^{1/4}` leaves (`k4-tlm-lensing-validation.md:22`, `k4-tlm-simulator.md:44`);
   `cvr_model.py:126` legacy exposure; the figure/regression anchors (`apparatus_floor_wall_run.py:78`,
   `test_gamma_sign_gate.py:138`). **All FLAGGED-NOT-FIXED.**

6. **A_yield register fork.** `loop_gap_seeds.py:26` (`A_YIELD = √α`, no 2) — same √α register in
   `regime_map.py:369` — vs `constants.R_I = √(2α)` / `chiral_lattice_v10.py:30`: a `2^{1/4}=1.189`
   silent address error for any knee-keyed quantity. Which is canonical for genesis seeds?
   **(Correction from the sweep:** `lense_thirring.py:172` is NOT in the √α register — it is a
   hardcoded `√(2α)` literal, the R_I register inlined; its hygiene item is "should import
   `constants.R_I`," a separate concern.)

7. **F5 knee-vs-wall yield-surface tension** (charter; gate-b adjudicates) — constrains what the
   knee rows may be CALLED.

8. **0.22/0.84 KEEP-BOTH follow-on** (op14 `:122`) — re-derive core/shell `A²` under the ¼
   exponent (`0.47/0.92`) or demote to illustrative-only. **KEEP-BOTH, FLAGGED-NOT-FIXED.**

9. **Contour-tagging hygiene mandate** — an `A²=α` vs `A²=2α` tag on every 0.9963 (§4
   near-collision row); one existing mis-use already found (`electron-bind-sim_result.md:59`).

## Re-verification corrections

<!-- filled per-commit -->
