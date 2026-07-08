# RESULT — The electron tick-floor: N_min = 7 is an ANALYTIC linear-regime sampling-representability floor for a uniform (2,3) winding

**Arc:** analysis/electron-tick-floor · **Repo:** AVE-Core (PUBLIC) · **Branch:** analysis/electron-tick-floor off origin/main
**Prereg (FROZEN):** [`research/2026-07-07_electron-tick-floor_prereg_FROZEN.md`](2026-07-07_electron-tick-floor_prereg_FROZEN.md) · **Drivers:** `src/scripts/verify/electron_tick_floor_sampling.py` (Leg A), `src/scripts/verify/electron_tick_floor_engine.py` (Leg B) · **Tests:** `src/tests/test_electron_tick_floor.py` (21, all green) · **Figure:** `research/figures/2026-07-07-electron-tick-floor/electron_tick_floor.pdf`

> **RE-SCOPED 2026-07-07 (Grant-ratified after adversarial review; Rule-11 honest closure).** The
> first-cut RESULT over-built the claim. Adversarial review found (from source, not re-litigated
> here — see the RE-SCOPE FINDINGS box) that the engine leg is NOT a second, independent, dynamical
> derivation of the floor: the internal (2,3) angles are hard-wired algebraic functions of the mode
> phase, the δ=0 trajectory is a force-free fixed point, and the engine's tick-sampled estimator IS
> the modular reduction Leg A computes analytically. The result therefore gets **smaller and truer**:
> a single **analytic, linear-regime, sampling-representability floor** N_min = 7, *illustrated* (not
> independently confirmed) by the engine. The kill-joints are non-fireable-as-shipped designed nulls;
> the Ax3-lossless machine-floor claim is scoped to the δ=0 family; the lock-range dt-convergence
> (skipped in the first cut) is run; and the linear-vs-nonlinear scoping hole is stated as a
> prominent LIMITATION. No bin was redefined to convert a ❌ to a ✅ (Rule 11). The frozen prereg body
> is unedited; all four recorded deviations live in the append-only ERRATA.

---

## RE-SCOPE FINDINGS (orchestrator-verified from source — the defects this doc now honestly reflects)

1. **The (2,3) angles have NO dynamical channel.** In `electron_tick_floor_engine.py::integrate` the
   internal angles are hard-wired `alpha_arr = 2·phi`, `beta_arr = 3·phi` (K1/K2_WINDING = 2, 3 at
   `electron_tick_floor_engine.py:55-56`) — algebraic in the single mode phase φ, with no independent
   state and no update rule. The mode cannot alias or de-cohere by any dynamics; only the *sampling*
   of the (already-exact) winding can alias.
2. **δ=0 is a force-free fixed point.** At the cold initial condition every acceleration is identically
   0; `locked=True` holds at **all** N including the sub-floor N=4,5,6 — automatic, carrying zero
   stability information (`|force|≈0`, `|ΔH/H|` at machine floor).
3. **Leg B re-evaluates Leg A's theorem.** The "blind" time-domain estimator
   `electron_tick_floor_engine.py::_winding_from_ticks` IS the discrete principal-branch modular
   reduction `electron_tick_floor_sampling.py::principal_winding` computes analytically. Feeding a
   uniform trajectory through it re-expresses the sampling theorem; it does not test it against
   anything the theorem did not already contain.

**Consequence:** every "derived twice independently / blind / two independent code paths"
claim from the first cut is **withdrawn**. The sampling theorem (Leg A) is the derivation; the
engine (Leg B) is a **representability illustration** that re-evaluates it through a constructed
trajectory.

---

## ROUTED BIN: **[FLOOR-ONLY]** — a linear-regime representability floor $N_{min}=7$; dynamical-stability + nonlinear-regime floor DEFERRED to round-2

The pre-registered most-likely outcome. Re-stated honestly: **$N_{min}=7$ is the first tick count on
which a UNIFORM (linear) $(2,3)$ winding is sampling-representable with chirality intact** — an
analytic sampling-theorem floor, **not** a two-sided window that pins $m_e$, **not** a
dual-independent derivation, and **not** a dynamical-stability result. The dynamical-stability floor
and the nonlinear-saturation-regime floor (the physically relevant one — see LIMITATION) are deferred
to round-2 (the genuinely-dynamical engine). The candidate ceiling half of the ontology (joint 4)
does not survive the lossless dynamics as modelled (see the flag-don't-fix finding); the resolution
hinges on an under-determined harmonic-dilution knob $\eta(N)$.

## REGIME + SECTOR + HOMONYM (as frozen)

Cold lattice; **Ax3-lossless only in the δ=0 zero-force family** ($|\Delta H/H|=4.11\times10^{-15}$,
machine floor — see the scoped Ax3 note below; the δ≠0 loaded runs are NOT machine-floor Hamiltonian).
Small-signal phase dynamics; discrete-time leapfrog declared METHOD (the $dt\to0$ study proves the
substep is not the clock). V-sector / phase-space object; the $(2,3)$ windings are read in the
internal-angle coordinates $(\alpha,\beta)$ — but note these are algebraically slaved to φ (RE-SCOPE
finding 1). Homonym guard: $N$ (sampling count) $=7$; $Q$ (=$1/\alpha$ coherence count) $\approx137$ —
three-plus OOM apart, zero $\alpha$ contact — guard armed, NOT tripped.

---

## LEG A (analytic) — the sampling floor + the Adler lock condition (THE derivation)

**A(a) THE FLOOR — $N_{min}=7$** — driver-confirmed (`electron_tick_floor_sampling.py::floor_scan`),
sympy-verified (`electron_tick_floor_sampling.py::prove_nyquist_floor`), test-locked
(`test_electron_tick_floor.py::test_analytic_N_min_is_seven`).

To carry the $k_1=2$ AND $k_2=3$ phase windings **distinctly** on $N$ ticks/period, a **uniform**
(constant per-tick advance $2\pi k/N$) winding requires (1) handedness-preserving strict Nyquist
$2k_{max}<N$ (the binding one, $k_{max}=3\Rightarrow N>6$) and (2) non-collision
$k_1\not\equiv\pm k_2\pmod N$. The classification (verbatim):

| $N$ | classification | why |
|---|---|---|
| 4 | ALIASED | both windings past Nyquist ($k=2$ at $N/2$; $k=3\to-1$) |
| **5** | **COLLIDE** | $3\equiv-2\pmod5$ — the 3-winding aliases onto the reflection of the 2-winding (the reflection collision happens iff $N\mid(k_1+k_2)=5$, sympy-verified `electron_tick_floor_sampling.py::prove_reflection_collision_N`) |
| **6** | **NYQUIST-MARGINAL** | $k=3$ sits exactly at $N/2$ → the $\pm3$ alias merges, chirality lost (sampling-phase-sensitive) |
| **7** | **CLEAN** | $3<7/2$ and $2\not\equiv\pm3\pmod7$ — first tick count carrying a uniform $(2,3)$ with chirality intact |
| $\ge 8$ | CLEAN | $2k_{max}<N$ |

**$N_{min}=2k_{max}+1=7$.** Independent of every coupling (pure representability) — **and conditional
on the winding being uniform** (LIMITATION below).

**A(b) THE ADLER LOCK CONDITION** (sympy-verified `electron_tick_floor_sampling.py::prove_adler_lock_condition`). The div-$N$ subharmonic phase error
obeys $\dot\psi=\delta-(\kappa/N)\sin(N\psi)$; a stable fixed point (lock) exists iff
$\sin(N\psi^*)=N\delta/\kappa$ is solvable, i.e. **$|\delta|\le\kappa/N$**, so the *first-order*
(dissipative-reduction) lock half-range is $\kappa/N$ and $N_{max}=\kappa/\delta$. **Cold identical
lattice** ($\delta=0$) $\Rightarrow N_{max}=\infty\Rightarrow$ **window verdict FLOOR-ONLY**
(driver-confirmed `electron_tick_floor_sampling.py::window_verdict`, test-locked
`test_electron_tick_floor.py::test_cold_identical_lattice_is_floor_only`). A finite ceiling needs a
substrate-intrinsic detuning; the physical candidate is the seed down-regulation
$\delta_{seed}=1-\sqrt{1-A^2}$ (Op14), reported PARAMETRICALLY in $A^2$ (firewall):
$A^2=0.05\to N_{max}\approx39$, $A^2=0.10\to19.5$, $A^2=0.20\to9.5$ (at $\kappa=1$). **Caveat below:
this first-order Adler ceiling is the DISSIPATIVE reduction; the lossless substrate contradicts it.**

## LEG B (engine) — a representability ILLUSTRATION (re-evaluates Leg A through a constructed trajectory)

Lossless Hamiltonian inertial phase lattice ($M=24$ cells, cluster $P=4$, $\kappa_{ens}=\kappa_{mode}=1$,
$\omega_{ens}=1$ — all dimensionless method params) hosting a div-$N$ mode whose internal angles are
**hard-wired** $\alpha=2\varphi,\ \beta=3\varphi$ (algebraic in φ; no independent DOF — RE-SCOPE
finding 1). This is why Leg B **cannot** independently confirm the floor: the winding is exact by
construction and only the tick-sampling can alias.

**(i) SAMPLING TRANSITION vs $N$ — engine reproduces the alias structure** (engine-confirmed `electron_tick_floor_engine.py::measurement_i`; test-locked `test_electron_tick_floor.py::test_engine_N_min_is_seven`). The tick-sampled winding estimator (= the modular
reduction of Leg A, RE-SCOPE finding 3) reads:

| $N$ | tick-sampled $(w_2,w_3)$ | verdict |
|---|---|---|
| 5 | $(2,-2)$ | not clean — the 3-winding **aliases to $-2$** (COLLIDE reproduced) |
| 6 | $(2,-1)$ | not clean — Nyquist-marginal (sampling-phase-sensitive) |
| 7 | $(2,3)$ | first CLEAN |
| 8–16, 20, 30 | $(2,3)$ | CLEAN |

**G1 ReconcileGate — a PLUMBING-CONSISTENCY check, NOT independent-physics confirmation.** engine
$N_{min}$ == analytic $N_{min}$ == **7**, max_rel_discrepancy $=0.0$:
engine-confirmed (`electron_tick_floor_engine.py::reconcile_gates`),
test-locked (`test_electron_tick_floor.py::test_G1_cross_leg_floor_reconciles`). This catches an
implementation bug; it does **not** show the floor was derived twice. Both legs are the same
$2k_{max}+1$ formula: **swapping the winding pair to $(3,5)$ moves BOTH legs to 11 in lock-step** —
test-locked (`test_electron_tick_floor.py::test_G1_is_plumbing_swap_to_35_moves_both_to_11`), the
property that proves G1 is plumbing.

**(ii) Lock-range vs $N$ (converged) + the two NON-FIREABLE-AS-SHIPPED designed nulls** (engine-confirmed `electron_tick_floor_engine.py::measurement_ii`).

- **[TOWER-EMERGES] is a DESIGNED NULL, not a passed strain test.** Re-pricing the whole tower's clock
  by a **global** $s=\sqrt{1-A^2}$ ($A^2=0.05,0.10,0.20$) keeps the div-$N=7$ ratio exactly intact,
  $(2,3)$ preserved — but this is a **global by-hand rescale that trivially preserves any integer
  ratio and passes even with $\kappa_{mode}=0$ (the mode fully DECOUPLED)**. It is NOT the frozen
  sub-patch $\sqrt S$ loading (which was never run — no $N_{max}(A^2)$ map was produced). It therefore
  measures **no** locking or coupling property. Pinned only as a regression on the trivial
  ratio-preservation (test-locked `test_electron_tick_floor.py::test_dilation_universality_tower_emerges`); the genuinely-dynamical strain test is **deferred to round-2**.
- **THE LOCK-RANGE FINDING (converged) — the lossless lock-range GROWS with $N$.** The conservative
  (Ax3-lossless) lock half-range, measured by bisection at the **converged** resolution $n_{sub}=96$
  (engine-confirmed `electron_tick_floor_engine.py::measurement_ii`; the first cut shipped
  un-converged $n_{sub}=24$ values — corrected below, ERRATUM E2):

  | $N$ | conservative half-range ($n_{sub}=96$) | first-order Adler $\kappa/N$ |
  |---|---|---|
  | 7 | 3.7092 | 0.1429 |
  | 8 | 3.9643 | 0.1250 |
  | 10 | 4.4299 | 0.1000 |
  | 12 | 4.8533 | 0.0833 |
  | 14 | 5.2431 | 0.0714 |
  | 16 | 5.6008 | 0.0625 |

  The lossless half-range **grows as $\sqrt N$** — least-squares power-law exponent **0.499**, max
  deviation from a pure $\sqrt N$ law **0.068 %** at $n_{sub}=96$
  (engine-confirmed `electron_tick_floor_engine.py::sqrt_n_fit`) — the **opposite** of the first-order
  dissipative Adler $\kappa/N$, and $\approx26\times$ larger already at $N=7$, diverging further with
  $N$; test-locked (`test_electron_tick_floor.py::test_lossless_lock_range_grows_not_shrinks`). This
  lock-range is a real **model** property (the conservative pendulum separatrix $\sim2\sqrt{N\kappa}$
  — the measured half-range is a constant $0.700\times$ it at every $N$); it is genuine dynamics of
  the lattice clock, distinct from the (illustration-only) floor above.

**(iii) [C-INVARIANT] is a DESIGNED NULL, not a measured invariance** — engine-confirmed (`electron_tick_floor_engine.py::measurement_iii`), test-locked (`test_electron_tick_floor.py::test_c_invariance_michelson_null`). Signal speed
$c_{signal}=1.1234$ (method units) is identical with the mode present vs absent (rel_diff $=0.0$
**exactly**). But the signal path (src $=12\to$ tgt $=18$) **never crosses the mode's cluster (cells
0–3)**: rel_diff $=0.0$ is **causal disconnection**, not a measured invariance of $c$ through the
mode. **The $c=a\cdot\omega_{lattice}$ invariance under re-pricing is ALGEBRAICALLY true regardless**
(see §COMPARISON — that part is real); this driver simply does not *measure* it. Deferred to round-2:
route the probe THROUGH the cluster.

**Method controls.** $dt\to0$ convergence of the sampling transition: engine $N_{min}$ invariant
$=[7]$ across $n_{sub}\in\{16,32,64,128\}$ — test-locked (`test_electron_tick_floor.py::test_dt_convergence_substep_is_not_the_clock`).
**Lock-range** $dt$-convergence — the quantity the first cut skipped, mandatory, now run:
engine-confirmed (`electron_tick_floor_engine.py::lock_range_dt_convergence`),
test-locked (`test_electron_tick_floor.py::test_lock_range_dt_converges`):

| $n_{sub}$ | half-range $N=7$ | half-range $N=16$ |
|---|---|---|
| 24 (shipped, UNCONVERGED) | 3.5316 | 4.8818 |
| 48 | 3.6712 | 5.4789 |
| 96 | 3.7092 | 5.6008 |
| 192 (converged) | 3.7168 | 5.6296 |

The last doubling ($96\to192$) moves the value **0.2 %** ($N=7$) / **0.5 %** ($N=16$). The
$\sqrt N$ fit **tightens with convergence**: exponent $0.395\to0.499$ and max deviation $\sim2.5\%\to
0.068\%$ from $n_{sub}=24$ to $n_{sub}=96$. The shipped $n_{sub}=24$ values (3.53 / 4.88) are 5–13 %
below the converged values and are **superseded** by the $n_{sub}=96$ table above.

## AX3-LOSSLESS — SCOPED TO THE δ=0 ZERO-FORCE FAMILY ONLY

The $|\Delta H/H|=4.11\times10^{-15}$ "machine floor" is the **δ=0 zero-force family** (nothing moves;
CP6 reactance pair $\theta$ and $\Omega$ tracked every step). The δ≠0 loaded runs — the ones that
**decide the lock-range** — are **not** machine-floor Hamiltonian: their $|\Delta H/H|$ is of order
$10^{-4}$–$10^{-3}$ at the shipped $n_{sub}=24$ lock edge, falling **$\times4$ per $n_{sub}$-doubling**
(e.g. $4.35\times10^{-4}\to2.44\times10^{-5}$ from $n_{sub}=24$ to $96$ at $\delta=2$) — an exactly
symplectic $\sim dt^2$ integrator truncation, **bounded and reversible**, not physical loss. The
lossless *direction* survives (the drift vanishes as $dt\to0$), but the unqualified "genuinely
Hamiltonian, Ax3-lossless" headline is **withdrawn** for the loaded family.

---

## LIMITATION (PROMINENT) — the floor is a LINEAR-REGIME lower bound; the physical soliton's floor is unknown

**The $N_{min}=7$ derivation assumes a UNIFORM / LINEAR winding** ($\alpha=2\varphi$ exact — constant
per-tick advance $2\pi k/N$). Canon places the physical electron $(2,3)$ in the **nonlinear-saturation
regime, NOT the linear regime** — verbatim, two anchors (they phrase the placement differently; both
agree on the load-bearing not-linear-regime point):

> `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:33` —
> "**(p,q) is fundamentally a nonlinear-saturation-confined-soliton topological property at the
> K4-bond-pair LC-tank phase-space level; NOT a linear-regime substrate-mode-eigenvalue label** —
> Path B-prime K4-TLM linear-regime band-splitting test FALSIFIED 2026-05-27 empirically per outcome C".

> `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:35` —
> "(p,q) is fundamentally a nonlinear-saturation-confined-soliton topological property at $\Gamma = -1$
> TIR boundary above $V_{yield}$, NOT a linear-regime substrate-mode-eigenvalue label (Path B-prime
> linear-regime K4-TLM band-splitting test FALSIFIED 2026-05-27 per outcome C)."

For an **anharmonic** winding the per-tick advance is not constant: the maximum per-tick advance
exceeds the mean $2\pi k/N$. Faithful principal-branch unwrap then requires
$N > 2\,k_{max}\cdot(\text{max advance}/\text{mean advance})$, so the representability floor **can only
move UP**. Therefore:

**$N_{min}=7$ is a LINEAR-REGIME LOWER BOUND. The physical soliton's floor is $\ge 7$ and unknown
until its harmonic content is derived.** — **NEEDS-DERIVATION (round-2):** derive the physical
$(2,3)$ soliton's per-tick harmonic content and re-run the representability floor for the anharmonic
winding.

---

## THE LEG-A ↔ LEG-B CEILING DISCREPANCY (flag-don't-fix — surfaced for Grant, NOT reconciled by tuning)

**The two legs disagree on the ceiling's $N$-scaling, and the disagreement traces to
lossy-vs-lossless.**

- **Leg A** derived the ceiling from the *first-order* Adler equation (lock half-range $\kappa/N$,
  shrinking with $N$) — the **dissipative / overdamped reduction** (it implicitly carries a finite
  $Q$, a capture mechanism that needs loss).
- **Leg B** integrated the **conservative (lossless) substrate directly**. The subharmonic lock is a
  Hamiltonian pendulum whose lock range is the **separatrix $\sim2\sqrt{N\kappa}$ — GROWING as
  $\sqrt N$** (converged, exponent 0.499), not shrinking.

The Ax3-lossless axiom forbids the dissipative reduction as the substrate's own dynamics, so at
$\eta=1$ (the modelled case) the **conservative $\sqrt N$ result is the physical one**: no high-$N$
lock-range ceiling. Grant's joint-4 framing ("mutual-lock range shrinks with division ratio,
Adler-class") rests on the dissipative-Adler intuition and is **contradicted-as-modelled** by the
lossless dynamics at $\eta=1$.

**CORRECTED $\eta(N)$ FORK STATEMENT (item 6 — the first cut mis-stated the boundary).** The one
under-determined knob is the div-$N$ **harmonic-dilution** factor $\eta(N)=N^{-e}$. With the pendulum
lock-range $\propto 2\sqrt{N\eta\kappa}/\omega$, the range scales as $\propto N^{(1-e)/2}$. The
**grow/shrink boundary is therefore $\eta\propto N^{-1}$** ($e=1$, flat), **not** $N^{-3/2}$ as the
first cut wrongly wrote. Verified with the wired `eta_exponent` knob —
engine-confirmed (`electron_tick_floor_engine.py::LatticeConfig`):
$e=0.5\to$ range exponent $+0.25$ (GROWS,
half-range $N{=}7{\to}16$: $2.30\to2.83$); $e=1.0\to$ exponent $0.00$ (FLAT: $1.418\to1.414$);
$e=1.25\to$ exponent $-0.125$ (SHRINKS: $1.112\to1.000$). **The plumber-physical question for Grant**
(see prereg PHYSICS-CHECK): *does the electron's div-$N$ subharmonic lock couple through a full
$N$-th harmonic ($e=0$, range grows → FLOOR-ONLY) or through a diluted harmonic falling faster than
$N^{-1}$ ($e>1$, range shrinks → a real high-$N$ ceiling could pin $N^*$ and hence $m_e$)?* A
fork-to-computable once $\eta(N)$ is named — the knob is wired.

---

## §COMPARISON (FIREWALLED — written AFTER the window was routed; physical constants enter ONLY here)

Everything above is $\alpha$-clean (mechanically enforced: `test_firewall_no_alpha_on_*_derivation_path`).
The pricing below is CONSISTENCY-class — it originates no new number, and is **DOUBLY CONDITIONAL**
(item 8): it assumes **(i)** the electron sits *at* the floor (undecided — there is no ceiling to pin
it) AND **(ii)** the linear-regime assumption (LIMITATION — the physical floor is $\ge7$, unknown).

**Pitch pricing $a=\lambdabar_C/N^*$ and the $c/Z_0$ invariance** (driver-confirmed `electron_tick_floor_sampling.py::firewall_comparison_pricing`; test-locked `test_electron_tick_floor.py::test_firewall_comparison_pricing_is_c_and_Z0_invariant`). With
$N^*=7$ (the *illustrative* floor-sitting candidate, conditional on (i)+(ii)):

$$a=\lambdabar_C/7=5.5166\times10^{-14}\ \text{m},\quad \omega_{lattice}=7\,\omega_C=5.4344\times10^{21}\ \text{rad/s},$$
$$c=a\cdot\omega_{lattice}=2.99792458\times10^{8}\ \text{m/s}=c\ \textbf{(EXACTLY invariant)},\quad Z_0=376.730\ \Omega\ \textbf{(untouched)}.$$

The re-pricing $a\to\lambdabar_C/N^*$, $\omega_{lattice}\to N^*\omega_C$ moves NEITHER $c$ NOR $Z_0$ —
$N^*$ only splits granularity between space and time, exactly as joint 3 requires. **The $c$/$Z_0$
invariance is ALGEBRAIC and survives UNCONDITIONALLY** (it holds for any $N^*$, independent of both
conditions above).

**Downstream (stated plainly):**
1. **Muonic band-split / [B-AVE] arm.** A finer pitch ($a=\lambdabar_C/N^*$ with $N^*\ge7$) pushes the
   continuum-validity floor DEEPER — the continuum approximation holds to finer scale, so the [B-AVE]
   exclusion **STRENGTHENS**. This closes our own hatch further; we say so plainly.
2. **Eigencavity arc (Task #11) starting grid:** hand it $N\ge7$ (the linear-regime lower bound); the
   eigencavity search need not consider $N<7$ (no representable uniform $(2,3)$ below the floor).
3. **Muon-decay corollary (QUALITATIVE; quantitative content = NEEDS-DERIVATION).** Heavier lepton =
   higher $\omega_{mode}$ = fewer ticks $N$ = closer to / below the sampling floor = undersampled →
   structurally unstable → decays. The electron (lightest) has the most ticks (best sampled = most
   stable). **NO mass-ratio numerology** — the map $N\leftrightarrow$ mass and any $m_\mu/m_e$ value
   is explicitly NEEDS-DERIVATION; no fit to 206.77 is attempted or implied.
4. **Dilation universality (QUALITATIVE).** A rigid global $\sqrt{1-A^2}$ re-pricing keeps the integer
   $N$ protected → universality of time dilation across the tower. **Caveat:** the engine's
   TOWER-EMERGES is the trivial global-rescale null (above), not dynamical evidence; the quantitative
   dilation law and the dynamical strain test are NEEDS-DERIVATION (round-2).

**The "7" coincidence (flagged, NOT claimed as source).** $N_{min}=7$ coincides numerically with the
AVE "7"-family (Poisson $2/7$, the $/7$ couplings, $\sqrt7$). The floor derivation makes **zero
contact** with any of those — it is pure $(2,3)$ Nyquist ($2k_{max}+1$). Flagged as a
coincidence-to-watch, not asserted as a shared mechanism.

## CONSISTENCY-vs-EMERGENCE TAG

- **$N_{min}=7$ (the floor):** **EMERGENCE-class candidate, SCOPED** — a dimensionless integer forced
  by the sampling theorem for a UNIFORM $(2,3)$, with the $\alpha$-firewall mechanically certified
  green (no CODATA / $\alpha$ / lepton-mass input on the derivation path). It is NOT a
  CODATA-derived-through-SI-substitution echo (contrast the A47 v17 family). The honest caveats: (a)
  it is an emergent *linear-regime floor*, not an emergent $m_e$; (b) it is a **lower bound** — the
  physical nonlinear-regime floor is $\ge7$, unknown (LIMITATION); (c) the ceiling that would turn it
  into a mass-forcing window is contradicted (lossless, $\eta=1$) / open (pending $\eta(N)$).
- **The pricing + dilation + $c/Z_0$ invariance:** CONSISTENCY-class (re-express canon; no new number).
- **No emergence headline beyond "a linear-regime floor lower bound of 7"** until (a) the physical
  winding's harmonic content is derived, (b) $\eta(N)$ is adjudicated, and (c) if a ceiling re-emerges
  it is re-checked for hidden circularity.

---

## ADJUDICATION AGAINST THE FROZEN PREREG BINS

| Prereg bin / falsifier | Outcome |
|---|---|
| Window bin | **[FLOOR-ONLY]** — as pre-registered most-likely ✅ (re-stated: linear-regime representability floor) |
| Expectation 1 ($N_{min}=7$; N=5/6/7 transitions) | ✅ analytic; engine reproduces the alias structure (illustration, not independent — RE-SCOPE) |
| Expectation 2 (lock-range $\kappa/N$, cold ⇒ no ceiling) | Partial — cold ⇒ no ceiling ✅; lossless form is $\sqrt N$ not $\kappa/N$ (flag-don't-fix; ERRATUM E2) |
| Expectation 3 (routed [FLOOR-ONLY]) | ✅ |
| Expectation 4 (TOWER-EMERGES) | Non-fireable-as-shipped designed null (global rescale; not the frozen $\sqrt S$ sub-patch) — deferred round-2 |
| Expectation 5 (C-INVARIANT) | Non-fireable-as-shipped designed null (causally-disconnected probe) — c-invariance algebraic, deferred round-2 |
| F-FIREWALL | Green — no quarantined symbol on either derivation path (mechanically enforced) ✅ |
| F1 (floor≠7) | Not triggered ($N_{min}=7$) |
| F2 (engine≠analytic) | Not triggered (G1 exact — but G1 is a plumbing check, RE-SCOPE) |
| F3 (strain de-coheres all $N$) | Not fired as a test (the strain test was not run; global rescale is a null) |
| F4 (C-VIOLATED) | Not fired as a test (probe causally disconnected from the mode) |
| F5 ($dt$-is-the-clock) | Not triggered (sampling $N_{min}$ invariant; lock-range now dt-converged) |

---

## ERRATA (append-only; freeze integrity — prereg body unedited)

- **ERRATUM E1 (collision framing, cosmetic).** The prereg states the reflection collision as
  "$3\equiv-2\pmod5$" (the $k_2\equiv-k_1$ framing). The Leg-A driver initially reported the
  equivalent $k_1\equiv-k_2$ framing (both $\equiv2$); aligned to the prereg's $k_2\equiv-k_1$ framing
  (both $\equiv3$) in the tests-commit. Same congruence ($2+3\equiv0\pmod5$); no physics change.
- **ERRATUM E2 (the ceiling's $N$-scaling — a REFINEMENT forced by the lossless dynamics; the
  lock-range values are also dt-CONVERGED here).** The prereg's Leg A(b) pre-committed the
  *first-order* Adler lock half-range $\kappa/N$ (shrinking). Running the Ax3-lossless substrate
  directly (Leg B) showed the conservative pendulum lock range **grows as $\sqrt N$** — the
  first-order $\kappa/N$ is the *dissipative reduction*, not the lossless substrate's own dynamics.
  This does NOT change the routed bin (still FLOOR-ONLY — both readings give no clean $\alpha$-free
  ceiling in the cold/lossless case), but it CONTRADICTS the direction of joint-4's "shrinks with $N$"
  ceiling candidate. **Correction to the first cut:** the shipped lock-range values (3.53 / 4.88 at
  $N=7/16$) were computed at an UNCONVERGED $n_{sub}=24$; the dt-converged values are **3.72 / 5.63**
  ($n_{sub}=192$; the $n_{sub}=96$ table is the reported primary), and the $\sqrt N$ fit tightens to
  exponent 0.499 / 0.068 % deviation. Surfaced flag-don't-fix (both numbers shown); the resolution
  hinges on the div-$N$ harmonic dilution $\eta(N)$, whose grow/shrink boundary is $\eta\propto N^{-1}$
  (corrected from the first cut's $N^{-3/2}$).
- **ERRATUM E3 (unrecorded model deviation — the cluster back-reaction factor).** The frozen prereg
  (`..._prereg_FROZEN.md:217`) wrote the bilateral back-reaction on each cluster cell as
  $\dot\Omega_i \mathrel{+}= (\kappa_{mode}/P)\sin(N\varphi-\theta_i)$. The shipped engine
  (`electron_tick_floor_engine.py::_accel`) implements $(\kappa_{mode}/(P\,N))\sin(N\varphi-\theta_i)$
  — an extra $1/N$. This is REQUIRED for the back-reaction + the mode torque to be a consistent
  Hamiltonian gradient of a single potential $V=-(\kappa_{mode}/(P\,N))\sum\cos(\theta_i-N\varphi)$
  (the $d/d\varphi$ chain rule supplies the factor $N$ that cancels the $1/N$, restoring the frozen
  mode torque $(\kappa_{mode}/P)\sum\sin(\cdot)$). The frozen literal pair (both $\kappa/P$) is
  Hamiltonian only if the mode is given inertia $N$; Ax3-lossless (exact $H$ conservation) was kept
  over prereg-literal. Append-only, honest.
- **ERRATUM E4 (unrecorded model extension — the $\eta(N)$ dilution dial).** The
  `eta_exponent` knob (`electron_tick_floor_engine.py::LatticeConfig`, $\eta(N)=N^{-\text{eta\_exponent}}$)
  exists nowhere in the frozen model. It is INERT at the default (eta_exponent $=0\Rightarrow\eta=1$,
  the frozen full-harmonic case), so no shipped number depends on it, but it is a model extension —
  the harmonic-dilution fork knob (see the corrected $\eta(N)$ fork statement). Append-only, honest.

> **Deviation count correction:** the first cut stated "exactly two deviations from the frozen
> prereg." That was wrong — there are **four** (E1–E4), the two model deviations (E3, E4) having gone
> unrecorded in the first cut. All four are recorded verbatim above.
