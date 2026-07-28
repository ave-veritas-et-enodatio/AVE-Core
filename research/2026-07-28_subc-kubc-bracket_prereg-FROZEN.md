# SUBC/KUBC Bracket — FROZEN pre-registration (OWED-1: bound `K_eff` on BOTH sides, not one)

**Date:** 2026-07-28
**Class:** DERIVATION + lattice-derived research-driver (research-doc; **forms derived, values dimensionless/geometric; mints no `clm-`/`def-`; propagates to no KB/tex leaf**). This is COMMIT 1 — the pre-registration ALONE, frozen and pushed before any driver code (the #761/#767/#770/#775/#782/#796 frozen-first discipline).
**Result-doc pointer requirement (machine-checkable frozen-provenance convention, gate LIVE 2026-07-22).** The result doc that resolves these bins MUST carry a machine-readable pointer line `Prereg-file: research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md` near its top, and every criterion it labels `Frozen:` MUST byte-match a quoted string in THIS file (`manuscript/ave-kb/tools/verify-frozen-provenance.py`). Every frozen criterion below is written as an inline-code `` `quoted token` `` for exactly that byte-match.
**Provenance:** Grant-fired 2026-07-28, verbatim `[sic]`: *"yes, as above, so below, we should assume we have both boundaries right?"* — the ruling that the corpus should HAVE both boundary conditions, not one. This lane discharges **OWED-1**, named co-equally by merged **#782** (`research/2026-07-21_rve-aggregation-bench_result.md` §8.2 item 2) and merged **#796** (`research/2026-07-22_vessel-state-rve_result.md` §9 OWED-1). Every `K_eff` the corpus has banked from this bench family (#782 `K_eff/K_0 = 0.296`; #796 `K_tan/K_0 = 0.29548`) is measured under **KUBC** — a kinematic uniform boundary condition, i.e. the **stiff / upper-bound-class** side. With one side we have a BOUND, not a BRACKET; the #782 review's own §7.1 finding ("an UPPER bound cannot support a floor") rides directly on the missing lower side.
**Lane fences:** DERIVATION lane only. Engine `src/ave` **BYTE-UNTOUCHED** (imports read-only; all boundary-condition/homogenization statics live in the driver under `research/drivers/`). **No** `manuscript/` or `manuscript/ave-kb/` `.tex`/`.md` leaf edits; **no** port-register edit; **no** un-revert; **no** falsification-ledger edit; **no** edit to the #782 or #796 result docs — regardless of outcome. Consequence ROUTED to Grant / the auditor lane only. All `[canon]` inputs content-verified two-method at base HEAD `c8ceacc3` (verify-before-cite).

> **FREEZE STATEMENT.** This document freezes: (i) the SUBC extraction — exact boundary condition, load-set construction, energy functional, null-space handling — and the variational argument that it is the true LOWER-bound counterpart of the shipped KUBC (§1); (ii) the THREE bracket definitions (same-instrument PRIMARY, conservative THEOREM-GRADE, and the shipped core-energy ESTIMATOR that is neither) with their rigor status stated per-definition (§2); (iii) the exact list of bracketed configurations (§3); (iv) the frozen gates including the `SUBC ≤ KUBC` **VOID** condition and its fireability self-test (§4/§4B); (v) the frozen READ — bracket width per configuration and threshold-straddle determination — with an EXHAUSTIVE, REACHABLE outcome-class partition and a PRE-REGISTERED FALLBACK for a non-decisive read (§5); (vi) the mutual-satisfiability audit + the design-time feasibility-pilot disclosure (§6); (vii) the ★SCOPE FENCE: this brackets `K` ONLY, never `ρ` (§7); (viii) the undetermined-fork guard (§8); (ix) the ledger + owed-follow-ons fence (§9). Nothing below §9 is a result. **The verdict may cite ONLY the frozen criteria's outputs, read from the shipped `_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson NAMED).**

---

## §0 — REGIME / SECTOR / PHASE-STATE header + substrate-native walk + A46 + pre-test physics check

**MODE.** The same object as #782/#796: the EFFECTIVE MEDIUM an ensemble of `Γ_bulk = −1` bulk-only-caged compression cores homogenizes into at scales ≫ core spacing (`electron-bh-isomorphism.md:26` `[canon]`). This lane changes NOTHING about the medium. It changes only **what the box does at its outer surface** — from a rigidly imposed affine displacement (KUBC) to an imposed uniform traction (SUBC).

**REGIME.** Regime-I cold-linear STATIC constitutive response — NO drive, NO lock-in, NO radiation port, NO time axis. Ax3-lossless-reactive: the discrete quadratic form is PSD and the static solve is unique modulo its null space, so there is no hysteresis and no rate. The cage shells are a STATIC constitutive grade (`S(A) → 0`, Op14 not run dynamically) exactly as in #782/#796.

**PHASE-STATE.** Cold-reactive medium; saturated cage shells at deep rail `S_RAIL = 1e-4`. For the #796 grown arm the phase-state is the GROWN pressure-vessel operating point (hoop-tension / radial-compression) — carried into this lane as the **frozen tangent operator at that operating point**, per §1's grown-arm carve.

**SECTOR.** Under test = **A1 bulk/compression** (`K_eff`, the mass/dilatation sector) — the headline — AND **T2 shear** (`G_eff`) as a corroborative companion. Sector-ownership discipline (do NOT cross-wire): A1 owns compression/mass/dilatation (`master-equation.md:20` `[canon]`); T2 owns shear; the `(2,3)` Cosserat winding owns charge/spin. Fork W is NOT picked here: the `k_a`-only bulk-only surrogate is the verdict wall, SYMMETRIC and RIGID are controls (identical to #782).

**A46 PHASE-SPACE-COORDINATE CHECK (`phase-space-coordinate-check` — PASS).** The corpus claim under test lives in the **impedance plane** (`r_Z = Z_bulk,eff/Z_0`), and the two banked numbers this lane brackets (#782 `r_Z = 0.544`, #796 `r_Z = 0.5436`) are impedance-plane coordinates. This lane measures the SAME coordinate — a static effective-modulus ratio mapped to `r_Z = √((K_eff/K_0)·(ρ_eff/ρ_0))` — under a second boundary condition. Real-space constitutive + impedance-plane, matched to the corpus claim. NOT a `φ²` proxy, NOT a real-space-vs-phase-space mismatch. **The ρ factor is NOT measured here (§7) and the coordinate match is therefore on the `K` factor only** — stated, not glossed.

**SUBSTRATE-NATIVE WALK (`substrate-native-check`, fired BEFORE scaffolding the SUBC primitive; Rule-14 reuse).**
1. **K4 connectivity.** Rule-14 reuse of the #770/#775/#782/#796 rank-2 bond model on the chiral srs-z3 net (`ave.core.chiral_lattice._SRS_8A/_NN`; `Φ_b = k_a d̂⊗d̂ + k_s(I − d̂⊗d̂)`; `ρ* = 9.77337` DERIVED from `ν_Hill = 2/7`, `ave.core.constants.N_NU`). **z = 3, not 4** — the srs coordination is three struts per node; the design-time pilot CONFIRMED the shipped lattice is z=3 (`degmax = 3`; `deg3 = 12167/13824` at `L=12`). NO new stencil, NOT a Cartesian Laplacian, NOT a continuum-Helmholtz operator. The SUBC change is entirely in the BOUNDARY TERM — the same `forces(u, Φ, bi, bj, N)` operator is applied; only the partition into constrained/free DOFs and the right-hand side change.
2. **Cosserat / channel basis.** The macroscopic load is split TRACEFUL (hydrostatic ⇒ `K_eff`, A1) vs DEVIATORIC (pure shear ⇒ `G_eff`, T2) — the substrate-native constitutive decomposition, not a Lamé-parameter fit. Under SUBC the split is imposed on the macroscopic STRESS `Σ` (the work-conjugate of the KUBC macroscopic STRAIN `E`), which is the correct dual pairing.
3. **Op14 saturation — the caged inclusion.** `S(A) = √(1 − (A/A_yield)²) → 0` grades the local bond stiffness toward the rail on a `~1`-node shell, IMPOSED as a static Eulerian grade (`A_yield = 1.0` native kernel/strain units; `research/drivers/constituent_cage_ensemble.py:63`, `research/drivers/rve_aggregation_bench.py:76`). Unchanged from #782/#796; this lane does not touch the grade.
4. **Phase-space vs real-space (A46).** See above — matched on the `K` factor; ρ out of scope (§7).
5. **Checkpoint 8 (emergence/hosting) — FALLBACK, and here it BITES.** A self-bound saturated soliton is INFEASIBLE on the lossless engine. Cages are imposed constitutive grades. **The SUBC boundary makes this checkpoint sharper, not weaker:** a traction boundary lets the whole cell dilate/relax freely, which is closer to a real embedded RVE than a rigidly clamped one — and it is precisely because the engine cannot host a self-bound object that we must BOUND the answer from both sides rather than trust a single clamped reading.
6. **Checkpoint 10 (boundary-not-bulk).** Each cage is a bounded operating-point bias on the coefficients (a graded shell `~1` node thick), NOT a bulk force. **★And the whole point of this lane is checkpoint 10 applied to the RVE's OWN outer boundary:** the #782/#796 numbers are boundary-conditioned, and a boundary-conditioned number needs its opposite boundary before it can be read as bulk physics.
7. **★Born-model instrument fact (surfaced by the substrate walk, NOT assumed away).** The bond form `Φ_b = k_a d̂⊗d̂ + k_s(I − d̂⊗d̂)` is a **Born model**: a global rigid ROTATION `u = ω × x` produces `d̂·du = 0` but a nonzero transverse `du`, so it COSTS ENERGY (design-time pilot, `L=12`: `E(rotation, |u|_max scaled to 1e-3) = 8.28e-4` vs `E(hydro ε=1e-3) = 1.21e-2` — the same order, NOT zero). Consequence, frozen and disclosed: **the null space of the free (pure-Neumann) operator is the 3 uniform TRANSLATIONS only, not the 6 rigid-body modes.** The model carries an absolute-frame rotational stiffness — a real property of the shipped bond model that the KUBC arms never exposed because they pin the boundary. This is stated as an instrument fact, NOT repaired (repairing it would change the medium and break the Rule-14 apples-to-apples comparison with #782/#796).

**PRE-TEST PHYSICS CHECK (`pre-test-physics-check`; Rule 16 — ONE plumber-physical question surfaced to Grant BEFORE the design locks, not after the run).** *Grant — plumber-physically: KUBC is a test fixture that CLAMPS the specimen's whole outer skin to a rigid affine motion; SUBC hangs weights on the skin and lets it find its own shape. Every real RVE inside a real body is somewhere between the two, which is exactly why the pair brackets. But on a FINITE lattice cluster the SUBC side has a feature the KUBC side hides: the outer surface has dangling, under-coordinated nodes (design-time pilot: `deg1 = 93` singly-bonded nodes at `L=16` out of `32767` active), and under a traction boundary those free-surface nodes are genuinely floppy, which makes the specimen APPEAR more compliant than the bulk medium is. The uncaged-medium gap is real and measurable: at `L=12` the pilot reads `K_KUBC/K_SUBC = 1.345`, at `L=16` `1.242` — converging, but not converged. **The question: do you want the bracket reported RAW (honest, includes the free-surface floppiness, so the lower bound is conservative and the bracket is wider than the true bulk uncertainty), or do you want the free-surface compliance subtracted out (tighter, but that subtraction is a model, and a model in the denominator of a bound defeats the point of having a bound)?** This design freezes RAW — no subtraction — and instead reports the uncaged gap `g_0(L)` at `L ∈ {12,16,20}` as an explicit, separately-tabulated finite-size term, so you can see how much of the bracket width is medium and how much is surface. If you want the subtraction, that is a different bench with its own prereg; it is not silently folded in here.* Surfaced at design time.

---

## §1 — ★THE SUBC EXTRACTION (frozen): boundary condition, load set, energy functional, null space — and WHY it is the true lower-bound counterpart

### §1.1 The boundary condition (frozen, exact)

`SUBC = STATIC (uniform-traction) uniform boundary condition: t(x) = Σ·n(x) on ∂V, with Σ a constant symmetric macroscopic stress tensor and n the outward normal; NO displacement is prescribed anywhere`. Concretely, on `cce.build_finite_srs(L)`:

- **Frozen active-node restriction.** `SUBC active set = nodes of nonzero bond degree; degree-0 nodes are excluded from the solve and carry no load`. (Design-time pilot: exactly `1` degree-0 node exists at each of `L ∈ {12,16,20}`; the degree>0 subgraph is a SINGLE connected component at all three sizes — verified by union-find. Without this restriction the pure-Neumann operator is singular beyond its physical null space and the preconditioned CG diverges — the pilot reproduced that divergence, §6.)
- **Frozen load set (the discrete uniform-traction realization).** `For each of the 6 outer faces (normal ±e_d), the face shell F is the set of ACTIVE nodes within bw = 1.5 lattice units of that face plane; each node in F receives f_i += (Σ·n)·A_face/|F|, where A_face is the cell cross-section perpendicular to d`. Corner/edge nodes belonging to several face shells receive the SUM of their face contributions. The same `bw = 1.5` as the KUBC boundary shell is used, so the two boundary conditions act on the SAME skin — an apples-to-apples requirement, frozen.
- **Frozen self-equilibration + macroscopic-stress identification.** The load set is `translation-projected (f ← f − mean(f)) before the solve`, and the macroscopic stress actually realized is read by Hill's lemma from the shipped load set, NOT assumed: `Σ̄ = (1/V)·sym( Σ_i f_i ⊗ (x_i − x_c) )`. All moduli below use `Σ̄`, so any imperfection in the discrete surface quadrature is absorbed rather than hidden. (Design-time pilot at `L=12`: `|Σ_i f_i| = 3.8e-15`, `|Σ_i (x_i−x_c)×f_i| = 3.2e-14` — the constructed set is self-equilibrated AND moment-free to machine precision; `Σ̄ = 0.87231·Σ` at `L=12`, `0.90475·Σ` at `L=16`, the expected shell-mean-depth deficit, and it CANCELS in every ratio.)
- **Frozen null-space handling.** `The pure-Neumann solve is a Jacobi-preconditioned CG in which every operator application, every preconditioner application and the right-hand side are projected onto the complement of the 3 uniform translations (P w = w − mean(w, axis=0)); no rotational projection is applied, because rigid rotations are NOT null modes of the Born bond model (§0 walk item 7)`.
- **Frozen solver tolerance + cap.** `SUBC pure-Neumann CG: relative residual ‖K u − f‖/‖f‖ ≤ 1e-9, iteration cap 60000; residual and iteration count reported for EVERY solve`.

### §1.2 The energy functional (frozen)

`SUBC energy functional: U_SUBC(Σ) = ½ Σ_bonds du·Φ·du evaluated at the traction-equilibrium displacement — the WHOLE-CELL elastic energy, equal at equilibrium to the work of the imposed tractions ½ f·u`. The whole-cell (not core-restricted) measure is frozen because it is the quantity the complementary-energy theorem bounds; the core-restricted measure has no bound status under EITHER boundary condition (§2.3). Absolute apparent moduli:

- `hydrostatic: Σ = σ·I ⇒ U_SUBC/V = ½σ̄²/K_SUBC ⇒ K_SUBC = σ̄²·V/(2·U_SUBC), with σ̄ = tr(Σ̄)/3`
- `pure shear: Σ = σ·(e_x⊗e_y + e_y⊗e_x) ⇒ U_SUBC/V = ½σ̄²/G_SUBC ⇒ G_SUBC = σ̄²·V/(2·U_SUBC), with σ̄ = Σ̄_xy`

with `V = Π_d (max_d pos − min_d pos)` — the SAME `V` the KUBC arm uses (`rve_aggregation_bench.py:294`). The KUBC absolute counterparts are the shipped forms, unchanged and Rule-14 reused: `KUBC hydrostatic: U_KUBC/V = 4.5·K_KUBC·ε²`, `KUBC pure shear: U_KUBC/V = 2·G_KUBC·ε²`.

### §1.3 ★WHY SUBC is the true LOWER-bound counterpart of the shipped KUBC (the variational argument — frozen, stated in full)

Let `C*` be the true (infinite-medium / periodic) effective stiffness of the composite the RVE samples, and let the RVE occupy `V`.

- **KUBC ⇒ UPPER bound, by the principle of minimum POTENTIAL energy.** Under `u = E·x` on `∂V` the equilibrium field minimizes the potential energy over all KINEMATICALLY ADMISSIBLE fields. The KUBC problem is the SAME variational problem as the free composite but with the boundary DOFs additionally CONSTRAINED — and adding constraints to a minimization can only RAISE the minimum. Hence `E : C^KUBC : E ≥ E : C* : E` for every `E`: `KUBC is a rigorous upper (stiff) bound`.
- **SUBC ⇒ LOWER bound, by the principle of minimum COMPLEMENTARY energy.** Under `t = Σ·n` on `∂V` the equilibrium stress field minimizes the complementary energy over all STATICALLY ADMISSIBLE stress fields; the uniform field `σ ≡ Σ` is admissible, and the true composite's field is admissible for the constrained problem. The apparent COMPLIANCE therefore satisfies `Σ : S^SUBC : Σ ≥ Σ : S* : Σ`, i.e. the SUBC specimen is at least as compliant as the true medium, i.e. `SUBC is a rigorous lower (soft) bound on the stiffness`.
- **The pair.** `S^SUBC ≥ S* ⇔ C^SUBC ≤ C* ≤ C^KUBC` — the Hill (1963) / Huet (1990) / Hazanov–Huet (1994) apparent-modulus ordering: any intermediate boundary condition on the same specimen lands between them. **This is why SUBC and only SUBC is the counterpart that closes the bracket:** it is not "another boundary condition to try," it is the variational DUAL of the one already shipped. A periodic BC would give a third, intermediate estimate — informative but NOT a bound, and therefore not what OWED-1 asks for.
- **Discrete validity (frozen honesty).** Both principles are exact statements about the DISCRETE positive-semidefinite quadratic form `U(u) = ½ uᵀKu` under a Dirichlet vs a Neumann partition; nothing in the argument needs a continuum limit. What the discrete setting DOES add is (a) a finite boundary layer (both bounds carry it; measured as `g_0(L)`, §4 G2), and (b) the free-surface under-coordination of a finite cluster (which biases the SUBC side conservatively DOWNWARD — it widens the bracket, it cannot invert it). Both are disclosed and neither is subtracted.

### §1.4 ★The GROWN-ARM carve (frozen — the #796 arm is bracketed on its FROZEN TANGENT OPERATOR, and here is why)

The #796 verdict number `K_tan/K_0 = 0.29548` is a **small-signal TANGENT modulus at a grown operating point**, produced by a state-dependent operator `k_shear,eff(u) = k_s + k_a·ε_axial(u)` (`axiom-register.md:193` `[canon]`). Two candidate SUBC counterparts exist; exactly ONE is frozen as the bracket, and the other is frozen OUT with its reason:

- **FROZEN AS THE BRACKET — the frozen-tangent-operator carve.** `The grown arm is bracketed on the FROZEN secant/tangent operator Φ_eff(u_0) at the #796 grown operating point — the same u-independent operator #796's PAINTED-ANISOTROPIC arm uses — held byte-identical between the KUBC and SUBC solves`. **Why this is the right object:** the bound theorem brackets a FIXED linear microstructure under two boundary conditions. `Φ_eff(u_0)` IS the fixed linear medium whose apparent modulus the #796 tangent probe reads, so bracketing it is theorem-grade. It is also directly cross-checkable: our KUBC-on-frozen-operator number must reproduce #796's shipped `K_tan_over_K0_painted = 0.2982369862639104` within the frozen G6 tolerance (§4).
- **FROZEN OUT OF THE BRACKET (reported, if run, as a labelled COMPANION only) — the fully-SUBC-grown arm.** Growing the vessel under a traction-free boundary and probing it under traction produces a DIFFERENT microstructure (`T(r)` co-varies with the boundary condition), so the KUBC-grown and SUBC-grown specimens are not the same medium and their pair is **NOT a bracket**. `A fully-SUBC-grown arm, if run, is reported as a labelled companion and is explicitly NOT part of any bracket, because its microstructure co-varies with the boundary condition`. It may not enter any bound-robustness claim.

---

## §2 — ★THE THREE RATIO DEFINITIONS (frozen), each with its rigor status stated

All three are dimensionless ratios of the caged/grown arm to the cold uncaged reference. They are NOT interchangeable and the result doc must label every number with which one it is.

### §2.1 PRIMARY — the same-instrument bracket (the headline pair)

- `R_KUBC ≡ K_KUBC^arm / K_KUBC^uncaged` (both whole-cell energies, same imposed E)
- `R_SUBC ≡ K_SUBC^arm / K_SUBC^uncaged = U_SUBC^uncaged / U_SUBC^arm` (same imposed load set f; the energy ratio INVERTS under traction control, because at fixed load the energy tracks the COMPLIANCE)
- `PRIMARY bracket = [R_SUBC, R_KUBC]`, `bracket width w = R_KUBC − R_SUBC`, `relative width w_rel = (R_KUBC − R_SUBC)/(0.5·(R_KUBC + R_SUBC))`.

**Rigor status (frozen, stated plainly):** `the PRIMARY same-instrument bracket cancels the finite-size boundary-layer bias to leading order (numerator and denominator share the box and the boundary condition) but is NOT theorem-grade on the RATIO, because the uncaged reference is itself boundary-conditioned`. It is the number that is apples-to-apples with #782/#796, and it is the headline. The theorem-grade version is §2.2.

### §2.2 CONSERVATIVE — the theorem-grade bracket

- `R_lo ≡ K_SUBC^arm / K_KUBC^uncaged` and `R_hi ≡ K_KUBC^arm / K_SUBC^uncaged`
- `CONSERVATIVE bracket = [R_lo, R_hi]`, which is theorem-grade because each factor is bounded in the correct direction: K_SUBC^arm ≤ K*^arm, K_KUBC^uncaged ≥ K*^uncaged ⇒ R_lo ≤ R*; and symmetrically R_hi ≥ R*.
- The two brackets are related by the frozen uncaged gap `g_0 ≡ K_KUBC^uncaged / K_SUBC^uncaged ≥ 1`: `R_lo = R_SUBC/g_0` and `R_hi = R_KUBC·g_0`.

**Rigor status:** `the CONSERVATIVE bracket is theorem-grade and always contains the PRIMARY bracket; it is wider by exactly the uncaged gap g_0 on each side`. Both are reported for every configuration. A claim of bound-robustness may cite EITHER, but must say which.

### §2.3 ★THE SHIPPED ESTIMATOR — `R_KUBC_core`, which is NEITHER bound (the flag-don't-fix item)

`R_KUBC_core ≡ U_core^arm / U_core^uncaged`, the central-`L/2`-cube energy ratio — **this is the quantity #782 and #796 actually banked** (`rve_aggregation_bench.py:158 core_energy`; `#782 result §5` `0.296`; `#796 result §4` `0.29548`). It is a legitimate BIAS-REDUCED (windowed) estimator of the effective modulus, and #782 §3 disclosed it as such. But:

`R_KUBC_core carries NO bound status: the Hill/Huet ordering theorem is about the whole-cell apparent modulus, and a windowed sub-region energy is not an apparent modulus of anything`.

**KEEP-BOTH companion (frozen, so the shipped convention is still readable side-by-side).** `R_SUBC_core ≡ U_core^uncaged / U_core^arm is ALSO reported, giving a core-convention interval [R_SUBC_core, R_KUBC_core] that is apples-to-apples with the #782/#796 banked convention. That interval carries NO bound status under either end and is labelled CORE-CONVENTION COMPANION (NOT A BRACKET) everywhere it appears; the theorem-grade whole-cell pair is the headline.`

**★The design-time pilot already found this MATTERS, and it is frozen here as a reported comparison rather than papered over.** At a NON-verdict pilot configuration (`L=12`, `r_cage=1.3`, `s=4.5`, bulk-only deep rail) the pilot read `R_SUBC = 0.4333`, `R_KUBC_total = 0.6795`, `R_KUBC_core = 0.2425` — i.e. the shipped-style CORE estimator sat **BELOW the SUBC lower bound**, while the whole-cell pair ordered correctly. `Therefore the frozen VOID ordering gate (§4 G1) is stated on the whole-cell pair ONLY; the core estimator's position relative to the bracket is a REPORTED FINDING, never a VOID trigger`. Freezing the ordering gate on the core estimator instead would have VOIDed this bench on a non-error — that is the Protocol-E mutual-satisfiability lesson applied at freeze time (§6).

### §2.4 The impedance read (frozen, with its scope tattooed on)

`r_Z_bracket ≡ [√R_SUBC, √R_KUBC] at ρ_eff/ρ_0 ≡ 1 ASSUMED — a K-BRACKET AROUND AN ASSUMED ρ, not a bracket on r_Z` (§7). The same construction is reported for the conservative pair as `r_Z_bracket_conservative = [√R_lo, √R_hi]`. `G_eff` brackets are reported by the identical construction on the pure-shear mode and are CORROBORATIVE ONLY.

---

## §3 — ★THE BRACKETED CONFIGURATIONS (frozen list — nothing added after freeze, nothing dropped without a §7-class disclosure)

All at the #782/#796 verdict grid unless stated: `srs-z3, L = 16 baseline, bw = 1.5, deep rail S_RAIL = 1e-4, cage_w = 1.0, CAGE geometry route A s = 4.5`. `KUBC probe amplitude ε = 1e-3` (the #782 frozen value); `SUBC probe stress σ = 1` (arbitrary — every SUBC read is a ratio at fixed load, so the amplitude cancels exactly on a linear operator; the linearity is asserted and CHECKED, §4 G8).

**A. THE #782 ISOTROPIC ARMS — the φ scan (route A, `r_cage ∈ {1.3, 1.6, 1.9, 2.2}` at `s = 4.5`; `φ_sf` is `r_cage = 2.2`, `φ = 0.489`).**
1. `bulk_only_cold` (the #782 HEADLINE class) — hydrostatic at ALL FOUR route-A points; pure shear at `φ_sf`.
2. `symmetric_cold` (wall-class control) — hydrostatic at ALL FOUR route-A points.
3. `bulk_only_compressed` (`ε_pre = −0.08`) — hydrostatic at `φ_sf`. **This is the arm whose #782 `r_Z = 0.466` is the ONLY bound-robust macro-side reading in the corpus** (#782 §7.1), so it is the one the lower bound most needs.
4. `bulk_only_expanded` (`ε_pre = +0.08`) — hydrostatic at `φ_sf`.
5. `rigid` (the #782 STOP-gate mirror control, `k_a × 100` on the shell) — hydrostatic at `φ_sf`. Its bracket must sit ABOVE 1 (see §4 G7).
6. `route B` (`r_cage = 1.7`, `s ∈ {3.6, 4.2, 5.0, 6.5}`), `bulk_only_cold`, hydrostatic — supplies the second collapse route so the bracket can be read on the geometry-correct `f_incl` axis #782 §7.7 established.

**B. THE #796 GROWN VESSEL ARM + its controls (all on the frozen tangent operator per §1.4).**
7. `grown_frozen_tangent` — the frozen `Φ_eff(u_0)` at the #796 `fixed_budget` `p_ref = 0.040` operating point, `σ_src = 1.6`, bulk-only wall, `φ_sf`. Hydrostatic + pure shear.
8. `painted_anisotropic` — #796's PAINTED arm operator (`k_shear,eff(u_0)` frozen `u`-independent). **On the #796 carve this is the SAME operator as (7)**; running both is the cross-check that our reconstruction of the #796 operating point is faithful (§4 G6), not two physics arms.
9. `isotropic_control` — the #782 `bulk_only_cold` cage at `φ_sf` with `k_s ≡ KS0` (the crash BASELINE `K_ratio_lift` normalizes against; #796 shipped `0.29636822324939766`). Hydrostatic.

**C. NULLS, CONTROLS AND SIZE.**
10. `uniform_medium_null` — zero cages, both boundary conditions, hydrostatic + shear. Ratios must return exactly `1.0` (identity; §4 G2a) and the ABSOLUTE gap `g_0` is read here (§4 G2b).
11. `size scan` — `bulk_only_cold` at `φ_sf` at `L ∈ {12, 16, 20}`, both boundary conditions, hydrostatic. Reads the bracket-width size trend (§4 G7).

**D. COMPANION (explicitly NOT part of any bracket, §1.4).**
12. `fully_SUBC_grown_companion` — grow the vessel under a traction-free boundary through the #796 state-dependent operator, then probe under traction. `Reported ONLY if it converges within the frozen budget; explicitly NOT part of any bracket, because its microstructure co-varies with the boundary condition`. Frozen budget: `the fully-SUBC-grown companion is capped at 40 outer iterations and 20 minutes wall-clock; on exceeding either it is reported as NOT-RUN with the reason, and no verdict depends on it`.

---

## §4 — ★FROZEN GATES (feasibility-assessed at design time, §6; every gate reports PASS/FAIL from the shipped JSON)

**G1 — ★THE ORDERING GATE = the VOID condition (frozen; this is an EXTRACTION-CORRECTNESS gate, NOT a physics finding).**
`G1: for EVERY bracketed configuration and BOTH modes, R_SUBC ≤ R_KUBC must hold on the WHOLE-CELL pair, with a numerical slack of 1e-6 relative. A violation means the SUBC extraction is WRONG — the bench is VOID for that configuration and the violation is reported as an instrument failure, NEVER as a physical finding that the lower bound exceeds the upper bound.` The gate is stated on the whole-cell pair only, per §2.3. `G1 also requires the ABSOLUTE ordering K_SUBC ≤ K_KUBC and G_SUBC ≤ G_KUBC on every configuration INCLUDING the uncaged reference.`

**G2 — the UNIFORM-MEDIUM NULL, split into its identity half and its fireable half (the #782 amplitude-linearity lesson NAMED).**
- `G2a (IDENTITY, not a fireable gate — labelled as such): with zero cages both R_SUBC and R_KUBC return 1.0 to within 1e-12, because numerator and denominator are the same solve. This is a pipeline sanity check and is reported as an IDENTITY, never counted as a discriminating gate.`
- `G2b (FIREABLE): on the uniform cold medium the absolute gap g_0(L) = K_KUBC^uncaged/K_SUBC^uncaged must satisfy g_0(L) ≥ 1 at every L ∈ {12,16,20} AND must be non-increasing in L (the finite-size boundary layer must shrink, not grow, with box size).` A broken load-set normalization, a sign error, or a mis-identified macroscopic stress breaks G2b; that is demonstrated by the §4B SELFTEST-G2b.

**G3 — DETERMINISM.** `G3: two independent full driver runs, in separate processes writing separate output paths, produce byte-identical timing-stripped results (diff -q CLEAN) and an identical determinism digest.` The only RNG anywhere in the chain is `run_c2_speeds(seed=1)`; the statics carry no per-step RNG.

**G4 — SUBC SOLVER CONVERGENCE.** `G4: every SUBC pure-Neumann solve reaches relative residual ≤ 1e-9 within the 60000-iteration cap; the residual and iteration count of every solve are shipped in the JSON.` (Design-time pilot at `L=16`: worst observed = the `rigid` control at `6474` iterations / `26.8 s`; the deep-rail verdict walls converge in `755–1444` iterations / `3.2–6.0 s`. The frozen cap has ~9× headroom on the worst pilot case.)

**G5 — THE WORK IDENTITY.** `G5: for every SUBC solve, |U_SUBC − ½·f·u| / U_SUBC ≤ 1e-8.` This is exact iff `K u = f`, so it is a convergence-equivalent check and is labelled as such — NOT an independent gate. (Pilot: agreement to all printed digits, `U = 4.992942e+02` vs `½f·u = 4.992942e+02`.)

**G6 — REPRODUCTION CROSS-CHECK against the merged corpus (fireable).**
`G6: the driver's own KUBC re-computations must reproduce the merged numbers within 2e-3 relative: #782 bulk_only_cold core-energy ratio at φ_sf = 0.296 (research/2026-07-21_rve-aggregation-bench_result.md §5); #796 isotropic control = 0.29636822324939766; #796 painted-anisotropic = 0.2982369862639104 (research/drivers/vessel_state_rve_results.json).` A failure here means our reconstruction of the shipped arms is not the shipped arm, and the whole bracket is meaningless — so G6 is a PRECONDITION for reading §5.

**G7 — STOP-GATE MIRROR + SIZE TREND.**
- `G7a (mirror validity, carried from #782): under BOTH boundary conditions the deep-rail bulk-only cage array must SOFTEN (ratio < 1) while the RIGID control must STIFFEN (ratio > 1). A wrong-sign mirror under EITHER boundary condition stops the lane.`
- `G7b (size trend): the PRIMARY bracket width w(L) at φ_sf must be non-increasing across L ∈ {12,16,20} within a 0.02 absolute slack; a bracket that WIDENS with box size means the SUBC arm is dominated by the free-surface artifact rather than converging, and the bracket is reported as NOT SIZE-CONVERGED.` A NOT-SIZE-CONVERGED bracket is still a valid bound (§1.3) but may not be cited as a tight one.

**G8 — LOAD-AMPLITUDE INVARIANCE (labelled IDENTITY, per the #782 lesson).** `G8: R_SUBC is invariant under σ → 10σ to within 1e-10. On a u-independent (linear) operator this is exact by algebra and is reported as an IDENTITY, not a fireable gate; it exists to catch a coding error in the load-set scaling, nothing more.`

---

## §4B — ★THE GATE-FIREABILITY ACCEPTANCE SELF-TESTS (mandatory, frozen — a gate that cannot be shown to fire is a checklist, not a gate)

Both self-tests run at instrument-validation time, BEFORE any bracket is read, and both are DELIBERATELY-BROKEN-EXTRACTION demonstrations (the only honest way to show a correctness gate fires, since a correct extraction must never trip it).

- **`SELFTEST-G1 (the VOID ordering gate MUST fire on an inverted extraction)`.** `SELFTEST-G1: recompute R_SUBC with the ratio taken in the KUBC direction (U_SUBC^arm/U_SUBC^uncaged instead of U_SUBC^uncaged/U_SUBC^arm) on the bulk_only_cold φ_sf configuration, and assert G1 REPORTS A VIOLATION.` The inverted ratio is `1/R_SUBC` which, for any softening arm (`R_SUBC < 1`), exceeds `1 > R_KUBC`; so the gate must fire. `Frozen acceptance: selftest_G1_fires = True.`
- **`SELFTEST-G2b (the uniform-null gate MUST fire on a mis-normalized macroscopic stress)`.** `SELFTEST-G2b: recompute the uncaged g_0 using the NOMINAL applied σ instead of the Hill-lemma Σ̄ read from the shipped load set, and assert G2b REPORTS A VIOLATION (g_0 < 1 or non-monotone in L).` The nominal-σ mis-normalization inflates `K_SUBC` by `1/(Σ̄/σ)² ≈ 1/0.87²–1/0.90² ≈ 1.22–1.32`, which is the same order as the true gap `g_0 ≈ 1.24–1.35`, so this self-test genuinely probes the gate's discriminating power at the scale that matters. `Frozen acceptance: selftest_G2b_fires = True.` **Frozen calibration latitude, disclosed in advance:** `if the nominal-σ mis-normalization does not push g_0 below 1 at every L, the self-test is accepted on the MONOTONICITY clause alone provided the driver SHIPS the computed g_0(L) under both normalizations so the reader can see which clause fired` — a calibration-class choice, disclosed, made before any verdict arm.

- **`SELFTEST-PARTITION (the outcome classifier must be exhaustive, disjoint, and must return every class)`.** `SELFTEST-PARTITION: walk a synthetic grid of (bracket_lo, bracket_hi, threshold) tuples through the SAME classifier the verdict uses; assert every tuple lands in EXACTLY one of RESOLVES-LOW / RESOLVES-HIGH / STRADDLES / VOID, that each of the three non-VOID classes is returned by at least one tuple, and that no tuple is unclassified.` This is the §5.3 Layer-1 reachability discharge (the #796 `assert_partition` pattern, Rule-14). `Frozen acceptance: selftest_partition_pass = True.`

`Frozen self-test gate: gate_fireability_selftest_pass = selftest_G1_fires AND selftest_G2b_fires AND selftest_partition_pass. If ANY fails to force its target, the correctness gates are a checklist not gates ⇒ the bench is VOID before any bracket is read; route to Grant.`

---

## §5 — ★THE FROZEN READ: bracket width, threshold-straddle, an EXHAUSTIVE + REACHABLE outcome partition, and a PRE-REGISTERED fallback

**The deliverable is a BRACKET, not a new point estimate.** This lane does not produce a better `K_eff`; it produces an interval that the true `K_eff` provably lies in, per configuration.

### §5.1 What is read, per configuration (frozen)

`Per configuration and per mode the result reports: R_SUBC, R_KUBC (whole-cell), R_SUBC_core and R_KUBC_core (the CORE-CONVENTION COMPANION pair, no bound status), the PRIMARY bracket [R_SUBC, R_KUBC] with width w and relative width w_rel, the CONSERVATIVE bracket [R_lo, R_hi], the uncaged gap g_0, the r_Z brackets at ρ ≡ 1, the SUBC CG residual + iteration count, and the G1 ordering flag.` **The result must state explicitly, at every headline, that the theorem-grade bracket is around the WHOLE-CELL apparent modulus, whereas the numbers #782/#796 banked (`0.296`, `0.29548`) are CORE-convention estimators — and must report where each banked number falls relative to its bracket, without reframing either.** Every one of those is read from the shipped `_results.json` produced by the deterministic driver. **No prose-string conclusions** (the #770 lesson NAMED).

### §5.2 The frozen threshold set (all pre-existing corpus thresholds, quoted — none minted here)

- `T1: r_Z = 0.5` — the #782 frozen band edge, verbatim from `research/2026-07-21_rve-aggregation-bench_prereg-FROZEN.md` §2: *"**BIN 1 — MACRO-CAGE (short-class).** `r_Z ≤ 0.5` at `φ_sf`"*.
- `T2: r_Z = 0.45 and r_Z = 0.55` — the #796 frozen `Z_lo`/`Z_str`/`Z_hi` band edges at `δ_rZ = 0.05`, verbatim from `research/2026-07-22_vessel-state-rve_prereg-FROZEN.md` §6: *"`Z_lo: r_Z < 0.5 − δ_rZ`; `Z_str: |r_Z − 0.5| ≤ δ_rZ`; `Z_hi: r_Z > 0.5 + δ_rZ`"*.
- `T3: R = 1.0` — the soften/stiffen sign threshold the #782 STOP-gate turns on.
- `T4: K_ratio_lift = 1.2 and 1.5` — the #796 `L1`/`L2`/`L3` lift bands, applied per-boundary-condition to the grown-vs-isotropic-control pair.

### §5.3 ★THE OUTCOME PARTITION (frozen; exhaustive, mutually exclusive, and REACHABILITY-PROVEN before the run)

Per (configuration, threshold) pair, exactly one of:

| class | frozen condition | meaning |
|---|---|---|
| `RESOLVES-LOW` | `bracket_hi < threshold` | the low-side reading is BOUND-ROBUST — both boundary conditions agree it is below |
| `RESOLVES-HIGH` | `bracket_lo > threshold` | the high-side reading is BOUND-ROBUST |
| `STRADDLES` | `bracket_lo ≤ threshold ≤ bracket_hi` | the reading is BOUND-CONDITIONAL — the boundary condition, not the medium, decides |
| `VOID` | G1 violated for that configuration | the extraction is wrong; not a physical outcome |

**★REACHABILITY, discharged in THREE layers (frozen BEFORE the run — the #796 §9 requirement 1). The layers are separated deliberately, because "reachable by construction" and "reachable on this configuration set" are different claims and conflating them is exactly the #796 F7 fault.**

- **Layer 1 — the CLASSIFIER is exhaustive, disjoint, and every class is returned (design-level; forced).** `SELFTEST-PARTITION (§4B): the driver walks a synthetic grid of (bracket_lo, bracket_hi, threshold) tuples through the SAME classifier the verdict uses, and asserts (a) every tuple lands in EXACTLY one class, (b) each of RESOLVES-LOW / RESOLVES-HIGH / STRADDLES is returned by at least one tuple, and (c) no tuple is unclassified.` No class is a dead letter in the code.
- **Layer 2 — TWO classes are FORCED on the physical configuration set by an already-frozen gate.** Against `T3 (R = 1.0)`, gate G7a REQUIRES that every deep-rail cage arm softens under BOTH boundary conditions and that the `rigid` control stiffens under BOTH. Therefore: `RESOLVES-LOW against T3 is FORCED for every softening cage arm, and RESOLVES-HIGH against T3 is FORCED for the rigid control (configuration 5) — both by G7a, independent of any unseen number. VOID is FORCED by SELFTEST-G1 (§4B). RESOLVES-HIGH against T1/T2 is FORCED for configuration 10 (uniform_medium_null), whose bracket is [1.0, 1.0] by G2a.` Three of the four classes are thus reachable on the physical set before a single verdict number exists.
- **Layer 3 — RESOLVES-LOW against `T1`/`T2` is DATA-DETERMINED, and that is the honest and intended design (stated so it cannot be mistaken for the F7 fault).** It fires iff `R_KUBC < 0.25` (i.e. `r_Z_hi < 0.5`) on some configuration — i.e. iff the medium really is that soft under BOTH boundary conditions. **Nothing in the band placement blocks it**: the bands are the corpus's pre-existing thresholds and the discriminator is a bracket-vs-threshold RELATION, not a point against a band the baseline already occupies. The frozen set deliberately spans the widest range the #782 grid offers — the full route-A crash band from `φ = 0.101` to `φ_sf = 0.489`, both routes, plus the deepest-crashing `symmetric` wall (merged KUBC-core reading `r_Z = 0.386`, `#782` result §6). `Frozen honesty clause: whether any configuration actually reaches RESOLVES-LOW at T1 cannot be known before the run without computing a verdict number, and this prereg does NOT claim it will. If none does, that is a RESULT — the bracket never descends below the macro-cage edge — and NOT an unreachable-bin design fault; the difference is that the F7 fault made a bin unreachable REGARDLESS of the data, whereas this bin is unreachable only if the data says so.`

### §5.4 ★The headline READ (frozen)

`HEADLINE: the PRIMARY r_Z bracket of configuration 1 (bulk_only_cold at φ_sf) against T1 (r_Z = 0.5), and the PRIMARY r_Z bracket of configuration 7 (the #796 grown frozen-tangent arm) against T1 and T2 — each reported with its outcome class, its width, and its CONSERVATIVE counterpart.` Every headline sentence must carry the §7 scope tag.

### §5.5 ★THE PRE-REGISTERED FALLBACK (frozen — the #796 §9 requirement 2, second half, discharged)

Registered NOW, before any number exists, so the disposition is not chosen after seeing the data:

1. `If a bracket STRADDLES its threshold: the corresponding corpus verdict is recorded as BOUND-CONDITIONAL and is NOT tightened in either direction. The standing #782 BIN-4 and #796 UNDETERMINED labels STAND UNCHANGED. No new bin is minted, no side is picked, no rescue is derived (Rule 11/12).`
2. `If a bracket RESOLVES-LOW at T1 on a headline arm: that arm's macro-side reading becomes BOUND-ROBUST. This is an INPUT to the Reading-B re-open question and to nothing else — the re-open decision is Grant's alone, the auditor lane lands any port-register / ledger / matrix edit, and this lane surfaces and routes only.`
3. `If a bracket RESOLVES-HIGH at T1 on a headline arm: the matched-side reading becomes BOUND-ROBUST and the #782 §7.1 "matched-side is KUBC-conditional" caveat is discharged for that arm. Same routing: surfaced, not landed.`
4. `If a configuration VOIDs: its bracket is NOT reported as physics; the standing merged verdict for that configuration is left exactly as merged, and the extraction failure is reported as an instrument finding with its residuals.`
5. `If the fully-SUBC-grown companion (§3 D) exceeds its frozen budget: it is reported NOT-RUN with the reason, and NO verdict depends on it.`
6. `If G6 (the reproduction cross-check) FAILS: §5 is NOT read at all — a bracket around a number we cannot reproduce is meaningless. The lane reports the reproduction failure and STOPS.`

### §5.6 ★ANTI-SEDUCTION FENCE, both ways (frozen IN ADVANCE)

A wide, low-reaching bracket flatters the macro-cage / Reading-B re-open direction; a tight bracket that holds above `0.5` flatters the #761→#767→#770 kill-momentum. This lane sits inside BOTH blast radii. Two frozen rules: **(a)** every bracket claimed SHIPS its data and its code path (the deterministic driver + `_results.json`) — no prose-string conclusions; **(b)** `a wide bracket is a statement about the INSTRUMENT, not about the medium: the result doc may NOT convert bracket width into physical significance in either direction, and must report the uncaged gap g_0 alongside every width so the reader can see how much of it is finite-size boundary layer.`

---

## §6 — ★MUTUAL-SATISFIABILITY AUDIT + the design-time feasibility-pilot disclosure (the Protocol-E lesson, discharged at freeze time)

### §6.1 The satisfiability audit (every frozen requirement checked against every other BEFORE freeze)

| requirement pair | co-satisfiable? | resolution frozen here |
|---|---|---|
| Rule-14 identical medium (deep rail `1e-4`, srs-z3, `L=16`) × a CONVERGENT pure-Neumann solve | **YES** — verified | pilot: `755–6474` iterations to `1e-9` at `L=16`; frozen cap `60000` (~9× headroom on the worst case) |
| `SUBC ≤ KUBC` as a VOID gate × comparability with the SHIPPED #782/#796 core-energy numbers | **NO** — verified counterexample | gate stated on the WHOLE-CELL pair only (§2.3, §4 G1); the core estimator is reported as a separate NON-BOUND number. Freezing the gate on the core estimator would have VOIDed the bench on a non-error |
| "uniform-medium null: both bounds → 1.0" × "every frozen gate must be fireable" | **NO** — the ratio null is an algebraic identity | split into G2a (IDENTITY, labelled, not counted) + G2b (FIREABLE absolute gap `g_0`) with SELFTEST-G2b |
| theorem-grade bracket × bracketing the #796 GROWN (state-dependent) arm | **NO** — a re-grown SUBC specimen is a different microstructure | frozen-tangent-operator carve (§1.4); the fully-SUBC-grown arm demoted to a labelled non-bracket companion |
| whole-cell energy functional × the shipped `U_core` verdict convention | **partially** — different estimators | BOTH reported, each labelled with its bound status (§2) |
| pure-Neumann solvability × the shipped lattice | **only after a fix** | the degree-0 node must be excluded (§1.1); without it the solve DIVERGES (pilot-reproduced) |
| total wall-clock × the 2 h checkpoint threshold | **YES** | pilot-extrapolated `≈ 5–20 min` for the full frozen configuration set |

### §6.2 The design-time feasibility pilot — DISCLOSED IN FULL (what was run, what was seen, and the carve that kept the verdict reads unseen)

Three scratchpad pilots were run BEFORE this freeze; none is committed, and all three are disclosed here because their findings are load-bearing on the design:

1. **Pilot 1 — instrument construction (uncaged only, `L ∈ {12,16}`).** Established: node/bond counts (`N = 13824/32768`, `M = 19872/47616`); `z = 3` coordination; exactly `1` degree-0 node per box with a SINGLE connected active component; the Born-model rotational stiffness (§0 walk item 7); the load set is self-equilibrated and moment-free to `~1e-14`; the Hill macroscopic stress is `0.872·Σ` at `L=12` and `0.905·Σ` at `L=16`; the work identity `U = ½f·u` holds; `g_0(K) = 1.345 (L=12) → 1.242 (L=16)`, `g_0(G) = 2.498 → 2.160`. **These are uncaged-reference numbers, not verdict numbers.**
2. **Pilot 2 — the ordering counterexample, at a deliberately NON-VERDICT configuration** (`L = 12`, `r_cage = 1.3`, `s = 4.5`, which is neither the `φ_sf` verdict point nor the `L=16` verdict grid). SEEN and disclosed: `bulk_only R_SUBC = 0.4333, R_KUBC_total = 0.6795, R_KUBC_core = 0.2425`; `rigid R_SUBC = 1.4467, R_KUBC_total = 1.8465, R_KUBC_core = 2.3450`. **This is the evidence behind the §2.3 / §4 G1 design decision and it is disclosed rather than laundered.** It is a `L=12` dilute point; it is NOT a verdict configuration and it is NOT quoted as a result.
3. **Pilot 3 — COST-ONLY at the verdict grid** (`L = 16`, `φ_sf`, `bulk_only` / `symmetric` / `rigid`, both modes). The pilot script printed **iteration counts and wall-clock ONLY** — no energies, no moduli, no ratios — deliberately, so that no verdict-relevant read exists prior to this freeze. Output: `755/854`, `1131/1444`, `5130/6474` iterations at `3.2/3.6`, `4.7/6.0`, `22.2/26.8` seconds.

`Frozen disclosure: no verdict-configuration modulus, ratio, bracket or r_Z value was computed or seen before this prereg was frozen; the only ratios seen were at the L=12 dilute NON-verdict pilot configuration, and they are quoted in full above.`

---

## §7 — ★SCOPE FENCE: THIS BRACKETS `K` ONLY. IT DOES NOT BRACKET `ρ`, AND IT DOES NOT DISCHARGE OWED-2.

Stated here, and required verbatim at every headline in the result doc:

`SCOPE: this bench brackets K_eff ONLY. Every r_Z interval it reports is a K-BRACKET AROUND AN ASSUMED ρ_eff/ρ_0 ≡ 1 — the ρ half is ASSUMED, not measured, not bracketed. This lane does NOT resolve walk-1's ρ half; that is OWED-2 (research/2026-07-22_vessel-state-rve_result.md §9), a separate lane, and OWED-1 does not dispose of it.`

The #796 result already ruled on the provenance of the assumed factor (§9, verbatim): *"`ρ_eff/ρ_0 ≡ 1` is an `[assumption]` (the long-λ `k→0` uniform-point-mass limit), NOT `[derived]`"*. Every `r_Z` number in this lane's result doc therefore inherits `[derived]` in its `K` factor and `[assumption]` in its `ρ` factor — a MIXED-provenance number, cited as such downstream. **A bracket on `K` narrows the `K` uncertainty and does nothing whatsoever to the `ρ` uncertainty; if the ρ half later moves, every `r_Z` interval here moves with it.**

---

## §8 — THE UNDETERMINED FORK GUARD (state precisely; do NOT pick by fiat)

- **Fork B — the bound character (the fork this lane exists to CLOSE, and it may close only halfway).** `Frozen rule: a bracket that STRADDLES a threshold leaves Fork B OPEN for that configuration and the standing verdict is recorded BOUND-CONDITIONAL; only a RESOLVES-LOW or RESOLVES-HIGH closes it, and only for the configuration and threshold it was computed at.` No extrapolation across `φ`, across wall class, or to nuclear packing.
- **Fork ρ — out of scope by construction (§7).** `Frozen rule: this lane makes NO ρ claim; the ρ-ontology and the ρ-measurability question (OWED-2) are routed untouched.`
- **Fork W — which `Γ` a knot core presents to each channel (unchanged from #770/#775/#779/#782/#796).** `Frozen rule: the k_a-only bulk-only surrogate is the verdict wall; SYMMETRIC and RIGID are controls; if the bracket's outcome class turns on wall class in a controlling way, route to Grant.`
- **Fork SURFACE — the finite-cluster free-surface compliance (NEW, this lane's own).** The SUBC arm's lower bound includes the floppiness of an under-coordinated free surface (`deg1 = 93` at `L=16`), which widens the bracket beyond the true bulk uncertainty. `Frozen rule: NO surface correction is applied; g_0(L) and the bracket-width size trend (G7b) are reported so the size-dependence is visible, and a NOT-SIZE-CONVERGED bracket may not be cited as a tight one.` Whether to build a surface-corrected estimator is a separate bench with its own prereg — surfaced to Grant by the §0 pre-test physics check, not decided here.
- **Fork TANGENT — frozen-operator vs re-grown (§1.4).** `Frozen rule: the bracket is on the frozen tangent operator; the fully-SUBC-grown companion is NOT a bracket and may not enter any bound-robustness claim. If the companion disagrees materially with the frozen-tangent arm, that disagreement is REPORTED as an open question and routed, not resolved.`

---

## §9 — Calibration-vs-derived ledger (tags frozen) + owed follow-ons fence

**Ledger tags (`consistency-vs-emergence`, frozen).** `R_SUBC`, `R_KUBC`, `R_KUBC_core`, `R_lo`, `R_hi`, `g_0`, the bracket widths and the `G_eff` counterparts are `[derived]` dimensionless RATIOS (lattice static homogenization under two boundary conditions; **CONSISTENCY-class**, not emergence: they test whether an already-banked lattice number is boundary-condition-robust, which is an internal-consistency question, and NO new physical constant is produced). `ρ_eff/ρ_0 ≡ 1` is `[assumption]` (§7), so every `r_Z` interval is **MIXED-provenance** — `[derived]` in `K`, `[assumption]` in `ρ`. The srs bond model `ρ* = 9.77337` is `[import]` (`ν_Hill = 2/7`, GR-imported `K = 2G`, `ave.core.constants.N_NU`; CONSISTENCY-class). The probe amplitudes (`ε = 1e-3`, `σ = 1`) and the solver tolerances are `[engineering-choice]`, disclosed, and shown to cancel or be converged (G4/G8). The Hill/Huet apparent-modulus ordering is a `[derived]` textbook theorem — the FORM the extraction is built on, not a fit. `α`-CLEAN (no `α`, no `Q_TANK`; every value is a dimensionless ratio — the α-circularity lesson). **No emergence-class claim headlined. No claim-id minted.**

**Owed follow-ons (fenced; NOT executed here — Rule 12; slot NOT refilled with an assertion).**
1. **OWED-2 — the `ρ_eff` measurability question stands entirely untouched** (`research/2026-07-22_vessel-state-rve_result.md` §9). A `K`-bracket does not dispose of it; said again here so it cannot be quietly counted as closed.
2. The PERIODIC-BC homogenization (the third, intermediate estimate) remains un-run. It is NOT a bound and therefore NOT what OWED-1 asks for, but it would tighten the interior of the bracket; a separate lane with its own prereg.
3. A surface-corrected SUBC estimator (Fork SURFACE) — a separate bench; the §0 pre-test physics check routes the decision to Grant.
4. The true nuclear `φ → 1` limit remains analytic-only (#782 Leg 5 + #770); this lane brackets the lattice `φ` band ONLY and extrapolates nothing.
5. Any port-register / falsification-ledger / matrix / KB-leaf consequence of a RESOLVES-LOW or RESOLVES-HIGH outcome is the auditor lane's to land and Grant's to decide. This lane surfaces and routes.

---

> **Pre-registration provenance.** Fired by Grant 2026-07-28 (verbatim `[sic]`: *"yes, as above, so below, we should assume we have both boundaries right?"*). This is COMMIT 1 — the prereg ALONE, frozen and pushed before any driver code (the #761/#767/#770/#775/#782/#796 frozen-first discipline). Discharges **OWED-1** as named by merged **#782** (`research/2026-07-21_rve-aggregation-bench_result.md` §8.2 item 2, verbatim: *"SUBC / periodic lower-bound cross-check (Fork B) — the decisive owed resolver, FEASIBLE at `L=16`"*) and merged **#796** (`research/2026-07-22_vessel-state-rve_result.md` §9 OWED-1), and satisfies BOTH requirements #796 §9 handed the follow-on SUBC prereg — **reachability** (§5.3, proven before the run) and **executability / internal satisfiability with a pre-registered fallback** (§5.5, §6). All `[canon]` inputs content-verified two-method at base HEAD `c8ceacc3` (verify-before-cite): `electron-bh-isomorphism.md:26`, `master-equation.md:20`, `axiom-register.md:193`, `ave.core.constants.N_NU:397`, `research/drivers/constituent_cage_ensemble.py:63/271`, `research/drivers/rve_aggregation_bench.py:76/158/294`. **Attribution:** Grant's both-boundaries ruling; the SUBC uniform-traction load-set construction with Hill-lemma stress identification, the translation-only null-space handling on the Born bond model, the three-ratio (PRIMARY / CONSERVATIVE / core-ESTIMATOR) carve with its per-definition rigor status, the frozen-tangent-operator carve for the grown arm, the deliberately-broken-extraction fireability self-tests, and the reachability proof are this lane's. Engine `src/ave` byte-untouched; mints no `clm-`/`def-`; propagates to no leaf; port-register / falsification-ledger untouched regardless of outcome. **★SCOPE, repeated: this brackets `K` only — every `r_Z` interval is a `K`-bracket around an ASSUMED `ρ ≡ 1`, and OWED-2 is NOT discharged.** Companions: merged **#782**, merged **#796**, merged **#779**, merged **#789** (`research/2026-07-21_continuum-radial-solver_CHARTER.md`), and the docket fragment (`_orchestration/docket-entries/2026-07-28-subc-kubc-bracket-prereg.md`).
