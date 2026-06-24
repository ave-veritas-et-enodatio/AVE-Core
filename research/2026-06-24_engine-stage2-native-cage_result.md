# Stage-2 native cage — make-or-break RESULT (the source-of-truth disposition)

**Date:** 2026-06-24 · **Lane:** full-engine-pathway, Stage 2 ("THE NATIVE CAGE") · **Status:** SETTLED NEGATIVE — canonical source doc.
**Verdict:** 🔴 **MODE-III DISPERSE — GENUINE FALSIFICATION, energy-conservation-certified.**
**Scope-lock (read first):** *Bulk self-trap mechanism RULED OUT; boundary/topological localization STANDS.* This is **NOT** "the electron is falsified." **mass = A1 (PR#260) is UNTOUCHED** — only the *localization mechanism* changes: the A1 core is pinned by the (2,3) winding + `H_couple` (topology/coupling) + the Γ=−1 boundary cavity, **not** by an autonomous bulk self-focusing well.

**Prereg (frozen, pre-run):** [`research/2026-06-23_engine-stage2-native-cage_prereg.md`](2026-06-23_engine-stage2-native-cage_prereg.md) (RE-FROZEN; SHA-pin `9fe5b9c2`).
**Make-or-break driver:** `src/scripts/engine_stage2_native_cage_imex_makeorbreak.py`.
**Solver:** `src/ave/solvers/native_cage_imex.py` (frozen-D Crank–Nicolson IMEX).
**Validation gates:** `src/tests/test_stage2_native_cage_imex.py` (GX1–GX5, live-run).
**Result gate (CI):** `src/tests/test_stage2_native_cage_imex_result_gate.py` (committed-JSON verdict + energy proof).
**Results JSON:** `results/engine_stage2_native_cage_imex_makeorbreak_results.json`.

**Source provenance:** curated from `analysis/engine-stage2-native-cage-imex @ edb19872` (the IMEX make-or-break commit). The make-or-break run was executed on that branch lineage and is brought onto a main-based branch by this PR so it is **citable on main** (A47 cross-tree-citation: nothing downstream may cite a branch-only result).

---

## 1. The pre-registered question and its disposition

The frozen make-or-break question (prereg §0.2):

> Does a seeded SECH precursor (v14 Mode-I config: N=24, A=0.85, sech)
> TIME-DOMAIN self-trap and PERSIST — a localized breathing core that does NOT
> disperse (Mode I) — on the native tetrahedral K4 stencil, with the co-acting
> cage engaged?

Two scope locks, both load-bearing and unchanged by this result:

1. **POSITED PERSISTENCE ONLY — NOT genesis self-formation.** We seed an
   already-localized eigen-precursor and ask whether the native dynamics HOLD it
   (Mode I) or SHED it (Mode III). Genesis-from-free-precursor is out of scope
   (the separately-tracked leaning-negative keystone-pump).
2. **TIME-DOMAIN, not frequency-domain.** Static native c_eff(V) eigenmode
   existence is already established (prereg §0.1); the open question was the
   nonlinear time-domain self-trap.

The prereg's two-sided disposition (§0.4):

- **Mode I** ⇒ the self-trap is a substrate property; the native cage hosts a
  dynamical bound breathing core.
- **Mode III** ⇒ "the self-trap was a **Cartesian artifact**. This is a **clean
  FALSIFICATION**, reported early, NOT a bug to debug away" (prereg §0.4:90-92).

**DISPOSITION: the Mode-III branch FIRED.** The IF-conditional written into the
prereg before the run resolved to its falsification arm. This is the discipline
working at full strength (Rule 11 honest closure): a clean negative, a single
mechanism explaining it, branch closed — NOT debugged toward a rescue.

## 2. The IMEX Mode-III result

Production run: N=24, dx=0.5, sech seed A=0.85, radius=2.5, co-acting cage,
frozen-D Crank–Nicolson IMEX, dt=0.066 (accuracy-set, dt-converged), 600 steps
(200-step transient + 400-step recording window).

| Quantity | Value | Reading |
|---|---|---|
| `FINAL.mode` | `MODE_III_DISPERSE_FALSIFICATION` | the verdict |
| `primary_N24.verdict` | `MODE_III_DISPERSE` | bins do not clear Mode-I PERSIST |
| Mode-I bins | I-1..I-4, I-6 true; **I-5 FALSE** | the radiation-floor discriminator fails ⇒ the core stalls at the seed level then sheds (disperses), it does NOT clear the persistent-bound-core bar |
| `sech.max_abs_over_run` | **0.849** ≈ seed (0.85) | the interior peak → seed at every dt; NO self-focus above seed |
| `physical_rupture` | False | does NOT over-saturate past A→1 under stable integration |
| `bounded_under_stable_integration` | True | bounded, energy-conserving — a clean call |

**A-stall, not self-focus.** The core does not collapse into a persistent
breathing soliton; max|V| over the run holds at ≈0.850 = the seed amplitude (it
neither self-focuses past it nor sustains a bound core) and then disperses below
the radiation floor. The "apparent self-focus past A→1" in the earlier explicit
run was an artifact (§4).

**dt-convergence (the explicit run's gap):** every finer dt (0.165, 0.066,
0.0264) returns `MODE_III_DISPERSE` with no detonation —
`dt_verdict_stable=true`, `dt_no_detonation=true`.

**N-robustness:** N=20 and N=32 both return `MODE_III_DISPERSE` —
`n_robust_agree=true`.

**Apparatus validity (known-goods):**
- Cartesian v14 reference DOES self-trap (`reproduces_v14_mode_i=true`) — the
  continuum cross-check is alive (the instrument can SEE a self-trap).
- matched Gaussian control DOES disperse (`disperses=true`) — the instrument can
  SEE dispersion.

So the native sech's dispersal is the substrate's verdict, not a dead apparatus.

## 3. Energy-conservation certification (the verdict is physics, not numerics)

A dispersal verdict from a dissipative integrator is worthless — over-damping
would shed the core for a numerical reason. The IMEX is PROVEN non-dissipative by
the production-N=24 energy-conservation gate (GX2), so the dispersal is the
physics, not the stepper:

| Energy proof (N=24, A=0.02 linear limit, 600 steps) | Value |
|---|---|
| `H0` | 0.0063610 |
| `H_end` | 0.0063609 |
| `rel_drift_end` | **−8.77e-6** |
| `secular_slope_per_time` | 2.66e-9 |
| `inv_Q_numerical` | **4.43e-8** |
| `Q_numerical` | **2.26e7** |
| `n_periods_resolved` | 31.5 |
| `passed` | **true** |

Energy is conserved to ~5 digits over 31.5 periods; the numerical 1/Q is ~5e-8,
nine orders below any O(1) physical effect. The certification is backed by a
LIVE negative control (GX3): the rejected backward-Euler form DOES bleed energy
(>5%) on the same lossless cage, so a PASS on the Crank–Nicolson scheme is
meaningful, not vacuous.

The make-or-break driver REFUSES to run if this gate fails (HARD HALT) — the
verdict cannot be a numerical artifact by construction.

## 4. Why the explicit run was INCONCLUSIVE — and why edb19872 SUPERSEDES 3a4c3227

The predecessor explicit-stepper run (`3a4c3227`, same branch lineage) returned
**INCONCLUSIVE** — a Rule-10 stepper instability, NOT a clean falsification. Two
distinct numerical pathologies corrupted it, both now fixed in the IMEX:

1. **CFL blow-up.** The explicit nonlinear leapfrog could not carry the
   self-focus transient into the stiff `1/S(A→1)` kernel; at fine dt it
   detonated (secular blow-up, peak 5.5→15.6 in the explicit dt-robustness
   sweep). The frozen-D Crank–Nicolson IMEX is unconditionally stable (GX4: it
   stays bounded WELL above the explicit blow-up CFL).
2. **PML sponge-injection.** The explicit run's post-solve sponge-MULTIPLY PML
   INJECTED energy under the implicit solve (a 142× gain at fine dt — physically
   impossible for a passive absorber), manufacturing a spurious self-focus past
   A→1. The IMEX replaces it with an energy-consistent Newmark velocity-damping
   port (PSD ⇒ passive, Hmax/H0 ≤ 1), regression-guarded by GX5.

The explicit run's apparent self-focus was therefore **both** pathologies
combined, not physics. The IMEX, energy-certified and dt-converged, gives the
clean call the explicit run could not.

**SUPERSESSION:** `edb19872` (IMEX, energy-certified MODE-III) **SUPERSEDES**
`3a4c3227` (explicit, INCONCLUSIVE). The new ledger entry for `stage2-native-cage`
records the supersession. This is the substrate-correct test the 2026-06-16
keystone reframe called for — now RUN and NEGATIVE.

**Anti-substitution discipline (A47 v11b / Rule 12):** the falsified bulk-soliton
slot is NOT refilled with a new unverified hypothesis. The "entrainment-trap" and
similar are untested candidates and get their own version + verification chain if
ever pursued; they do not silently occupy the closed slot.

## 5. What is ruled out, what stands (the scope discipline)

**RULED OUT (this falsification):**
- The **bulk self-trap / bulk self-focusing well** as the rest-mass localization
  mechanism. A seeded sech precursor does NOT self-focus into a persistent bound
  interior mode on the native K4 stencil. The Cartesian v14 Mode-I self-trap is a
  **grid artifact** of the Cartesian leapfrog, not a substrate property.
- The escape-hatch "it only disperses because c_eff(V) modulation is missing" is
  REFUTED: the native K4 stencil **WITH** c_eff(V) still disperses. Mode-III is
  the substrate's verdict, not a missing-modulation artifact.

**STANDS (UNTOUCHED by this falsification):**
- **mass = A1 (PR#260).** The rest mass IS the A1 dilatation scalar. This result
  does not touch the mass SECTOR — it only changes WHAT LOCALIZES the A1 core.
- **mc² = E_reactive** (mass-closure identity). Unchanged.
- **Boundary/topological localization.** The A1 core is pinned by the (2,3)
  Cosserat winding + `H_couple` (topology/coupling) and the Γ=−1 TIR boundary
  cavity — NOT by an autonomous bulk self-focusing well. The Γ=−1 cavity as a
  BOUNDARY CONDITION (electron-identification §1 property-3, clm-sjjvhf) survives;
  only self-trap-as-a-BULK-interior-mode is ruled out.
- **Static native c_eff(V) eigenmode existence** (prereg §0.1) — a frequency-domain
  property of the linearized operator, established independently and not at issue.

The one-line framing on every downstream edit: **bulk self-trap RULED OUT;
boundary/topological localization STANDS. mass = A1 is untouched.**

## 6. CI gating

Two complementary gates protect this result on main (both in the PR-blocking
`make test` lane — fast: ~4.4s GX suite, ~0.01s result gate):

1. **Live-run validation gates** — `src/tests/test_stage2_native_cage_imex.py`:
   - GX1 operator-unchanged (IMEX sparse L_D == validated dense native operator,
     symmetric PSD);
   - **GX2 THE energy-conservation gate** (rel_drift, inv_Q at the certification
     tolerance) — the rigor guard;
   - GX3 backward-Euler dissipative negative control (proves GX2 is live);
   - GX4 unconditional stability above the explicit blow-up CFL;
   - GX5 radiative-port-is-passive regression (the PML sponge-injection artifact).
2. **Result gate** — `src/tests/test_stage2_native_cage_imex_result_gate.py`:
   asserts the COMMITTED results JSON carries `MODE_III_DISPERSE_FALSIFICATION`,
   the energy proof at tolerance, the failing **I-5 radiation-floor bin** (the
   A-stall discriminator — bound so a post-hoc bin-drop can't convert ❌→✅),
   the seed-level max|V| (no self-focus), dt-stability, N-robustness, and the
   known-good apparatus validity.

Re-generate the JSON with:
`PYTHONPATH=src python src/scripts/engine_stage2_native_cage_imex_makeorbreak.py`.

---

## Appendix — provenance chain

- Prereg RE-FROZEN: `research/2026-06-23_engine-stage2-native-cage_prereg.md`
  (SHA-pin `9fe5b9c2`, = origin/main HEAD at freeze).
- Make-or-break executed on `analysis/engine-stage2-native-cage-imex @ edb19872`.
- Predecessor explicit run: `3a4c3227` (INCONCLUSIVE) — SUPERSEDED.
- Recovery/source commit (this PR): brings the IMEX subset onto a main-based
  branch for citability.
