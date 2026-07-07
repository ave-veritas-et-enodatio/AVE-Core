# RESULT — The electron tick-floor: N_min = 7 is a substrate-forced sampling integer; the ceiling is CONTRADICTED in the lossless substrate

**Arc:** analysis/electron-tick-floor · **Repo:** AVE-Core (PUBLIC) · **Branch:** analysis/electron-tick-floor off origin/main
**Prereg (FROZEN):** [`research/2026-07-07_electron-tick-floor_prereg_FROZEN.md`](2026-07-07_electron-tick-floor_prereg_FROZEN.md) · **Drivers:** `src/scripts/verify/electron_tick_floor_sampling.py` (Leg A), `src/scripts/verify/electron_tick_floor_engine.py` (Leg B) · **Tests:** `src/tests/test_electron_tick_floor.py` (19, all green) · **Figure:** `research/figures/2026-07-07-electron-tick-floor/electron_tick_floor.pdf`

> Adjudicated against the FROZEN prereg bins. No bin was redefined to convert a ❌ to a ✅ (Rule 11).
> The two deviations from the frozen prereg are recorded verbatim in the ERRATA section (append-only).

---

## ROUTED BIN: **[FLOOR-ONLY]** — robust floor $N_{min}=7$; the candidate ceiling is CONTRADICTED (not merely soft) in the Ax3-lossless substrate

The pre-registered most-likely outcome. The floor is a clean, firewall-clean, substrate-forced
dimensionless integer. The ceiling half of the ontology (joint 4, "candidate ceiling $N\le N_{max}$,
mutual-lock range shrinks with division ratio, Adler-class") **does not survive the lossless
dynamics** — see the flag-don't-fix finding below. The chord candidate is therefore the FLOOR
integer $N_{min}=7$ alone (a substrate-forced minimum tick count), **not** a two-sided window that
pins $m_e$.

## REGIME + SECTOR + HOMONYM (as frozen)

Cold lattice, lossless-reactive ($|\Delta H/H|=4.11\times10^{-15}$, machine floor — the model is
genuinely Hamiltonian, Ax3-lossless), small-signal phase dynamics; discrete-time leapfrog declared
METHOD (the $dt\to0$ study proves the substep is not the clock). V-sector / phase-space object; the
$(2,3)$ windings are measured in the internal-angle coordinates $(\alpha,\beta)$, not real-space.
Homonym guard: $N$ (sampling count) $=7$; $Q$ (=$1/\alpha$ coherence count) $\approx137$ — three-plus
OOM apart, zero $\alpha$ contact — guard armed, NOT tripped.

---

## LEG A (analytic) — the sampling floor + the Adler lock condition

**A(a) THE FLOOR — $N_{min}=7$** — driver-confirmed (`electron_tick_floor_sampling.py::floor_scan`),
sympy-verified (`electron_tick_floor_sampling.py::prove_nyquist_floor`), test-locked
(`test_electron_tick_floor.py::test_analytic_N_min_is_seven`).

To carry the $k_1=2$ AND $k_2=3$ phase windings **distinctly** on $N$ ticks/period requires (1)
handedness-preserving strict Nyquist $2k_{max}<N$ (the binding one, $k_{max}=3\Rightarrow N>6$) and
(2) non-collision $k_1\not\equiv\pm k_2\pmod N$. The classification (verbatim):

| $N$ | classification | why |
|---|---|---|
| 4 | ALIASED | both windings past Nyquist ($k=2$ at $N/2$; $k=3\to-1$) |
| **5** | **COLLIDE** | $3\equiv-2\pmod5$ — the 3-winding aliases onto the reflection of the 2-winding (the reflection collision happens iff $N\mid(k_1+k_2)=5$, sympy-verified `electron_tick_floor_sampling.py::prove_reflection_collision_N`) |
| **6** | **NYQUIST-MARGINAL** | $k=3$ sits exactly at $N/2$ → the $\pm3$ alias merges, chirality lost (sampling-phase-sensitive) |
| **7** | **CLEAN** | $3<7/2$ and $2\not\equiv\pm3\pmod7$ — first tick count carrying $(2,3)$ with chirality intact |
| $\ge 8$ | CLEAN | $2k_{max}<N$ |

**$N_{min}=2k_{max}+1=7$.** Independent of every coupling (pure representability).

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

## LEG B (engine) — three blind measurements

Lossless Hamiltonian inertial phase lattice ($M=24$ cells, cluster $P=4$, $\kappa_{ens}=\kappa_{mode}=1$,
$\omega_{ens}=1$ — all dimensionless method params) hosting the div-$N$ $(2,3)$ mode.

**(i) LOCK/DECAY vs $N$ — engine $N_{min}=7$** (engine-confirmed `electron_tick_floor_engine.py::measurement_i`; test-locked `test_electron_tick_floor.py::test_engine_N_min_is_seven`). The INDEPENDENT time-domain
tick-sampled winding estimator reads:

| $N$ | tick-sampled $(w_2,w_3)$ | verdict |
|---|---|---|
| 5 | $(2,-2)$ | not clean — the 3-winding **aliases to $-2$** (COLLIDE reproduced) |
| 6 | $(2,-1)$ | not clean — Nyquist-marginal (sampling-phase-sensitive) |
| 7 | $(2,3)$ | first CLEAN |
| 8–16, 20, 30 | $(2,3)$ | CLEAN |

**G1 ReconcileGate** (can-fire self-test proven): engine $N_{min}$ == analytic $N_{min}$ == **7**,
max_rel_discrepancy $=0.0$ — engine-confirmed (`electron_tick_floor_engine.py::reconcile_gates`),
test-locked (`test_electron_tick_floor.py::test_G1_cross_leg_floor_reconciles`). Two independent code
paths (modular arithmetic vs time-domain integration) agree exactly.

**(ii) [TOWER-EMERGES] + the lock-range finding** (engine-confirmed `electron_tick_floor_engine.py::measurement_ii`).

- **Global uniform dilation → TOWER-EMERGES.** Re-pricing the whole locked tower's clock by
  $s=\sqrt{1-A^2}$ ($A^2=0.05,0.10,0.20$) keeps the div-$N=7$ ratio **exactly intact**, $(2,3)$
  preserved — dilation universality demonstrated (test-locked `test_electron_tick_floor.py::test_dilation_universality_tower_emerges`). The integer lock ratio is
  protected under clock down-regulation: the qualitative dilation corollary.
- **THE FLAG-DON'T-FIX FINDING — the lossless lock-range GROWS with $N$.** The conservative (Ax3-lossless) lock half-range, measured by bisection (engine-confirmed `electron_tick_floor_engine.py::measurement_ii`):

  | $N$ | conservative half-range | first-order Adler $\kappa/N$ |
  |---|---|---|
  | 7 | 3.53 | 0.143 |
  | 8 | 3.74 | 0.125 |
  | 10 | 4.11 | 0.100 |
  | 12 | 4.43 | 0.083 |
  | 14 | 4.68 | 0.071 |
  | 16 | 4.88 | 0.0625 |

  The lossless half-range **grows as $\sqrt N$** (step ratios track $\sqrt{N_2/N_1}$ to ~1%) — the
  **opposite** of the first-order dissipative Adler $\kappa/N$, and $\gtrsim25\times$ larger already at
  $N=7$, diverging further with $N$ (test-locked `test_electron_tick_floor.py::test_lossless_lock_range_grows_not_shrinks`).

**(iii) [C-INVARIANT]** — engine-confirmed (`electron_tick_floor_engine.py::measurement_iii`),
test-locked (`test_electron_tick_floor.py::test_c_invariance_michelson_null`). Signal speed
$c_{signal}=1.1234$ (method units) is **identical** with the mode present vs absent
(rel_diff $=0.0$) and at $N=7$ vs $N=12$ (rel_diff $=0.0$). **G2 ReconcileGate** (can-fire proven):
$c_{with}$ == $c_{without}$. The Michelson-class internal null passes: the mode is a subharmonic
passenger; the coupling velocity is set by the ensemble band, not the mode or $N$.

**Method controls.** $dt\to0$ convergence: engine $N_{min}$ invariant $=[7]$ across $n_{sub}\in\{16,32,64,128\}$
— the integrator substep is NOT the answer's clock (F5 passes, test-locked `test_electron_tick_floor.py::test_dt_convergence_substep_is_not_the_clock`). Energy:
$|\Delta H/H|=4.11\times10^{-15}$ — the lossless (Ax3) check at machine floor (CP6 reactance pair
tracked: both $\theta$ and $\Omega$ every step).

---

## THE LEG-A ↔ LEG-B CEILING DISCREPANCY (flag-don't-fix — surfaced for Grant, NOT reconciled by tuning)

**The two legs disagree on the ceiling's $N$-scaling, and the disagreement traces to
lossy-vs-lossless — which the Ax3-lossless substrate settles against the ceiling.**

- **Leg A** derived the ceiling from the *first-order* Adler equation (lock half-range $\kappa/N$,
  shrinking with $N$) — this is the **dissipative / overdamped reduction** (it implicitly carries a
  finite $Q$, a capture mechanism that needs loss).
- **Leg B** integrated the **conservative (lossless) substrate directly**. The subharmonic lock is a
  Hamiltonian pendulum $\ddot\psi+N\kappa\sin\psi=0$ whose lock range is the **separatrix
  $\sim2\sqrt{N\kappa}$ — GROWING as $\sqrt N$**, not shrinking.

The Ax3-lossless axiom forbids the dissipative reduction as the substrate's own dynamics, so the
**conservative $\sqrt N$ result is the physical one**: in a lossless substrate there is **no high-$N$
lock-range ceiling**. Grant's joint-4 framing ("mutual-lock range shrinks with division ratio,
Adler-class") rests on the dissipative-Adler intuition; **it is contradicted-as-modeled by the
lossless dynamics.** One under-determined knob could in principle restore a shrinking ceiling — the
div-$N$ **harmonic-dilution** factor $\eta(N)$ (how much $N$-th-harmonic content couples the
subharmonic to its reference); at $\eta=1$ (full harmonic, the modeled case) the lock range grows,
and only a steeply-falling $\eta(N)\lesssim N^{-3/2}$ would make it shrink. **This is the one
plumber-physical question surfaced to Grant** (see prereg PHYSICS-CHECK): *does the electron's div-$N$
subharmonic lock couple through a full $N$-th harmonic (lock range grows → FLOOR-ONLY, floor 7 the
only forced integer) or through a steeply-diluted harmonic (lock range shrinks → a real high-$N$
ceiling could pin $N^*$ and hence $m_e$)?* The engine can decide it once $\eta(N)$ is named (the
`eta_exponent` knob is already wired) — a fork-to-computable, not a fiat call.

---

## §COMPARISON (FIREWALLED — written AFTER the window was routed; physical constants enter ONLY here)

Everything above is $\alpha$-clean (mechanically enforced: `test_firewall_no_alpha_on_*_derivation_path`).
The pricing below is CONSISTENCY-class — it originates no new number.

**Pitch pricing $a=\lambdabar_C/N^*$ and the $c/Z_0$ invariance** (driver-confirmed `electron_tick_floor_sampling.py::firewall_comparison_pricing`; test-locked `test_electron_tick_floor.py::test_firewall_comparison_pricing_is_c_and_Z0_invariant`). With
$N^*=7$ (the floor, as the illustrative floor-sitting candidate):

$$a=\lambdabar_C/7=5.5166\times10^{-14}\ \text{m},\quad \omega_{lattice}=7\,\omega_C=5.4344\times10^{21}\ \text{rad/s},$$
$$c=a\cdot\omega_{lattice}=2.99792458\times10^{8}\ \text{m/s}=c\ \textbf{(EXACTLY invariant)},\quad Z_0=376.730\ \Omega\ \textbf{(untouched)}.$$

The re-pricing $a\to\lambdabar_C/N^*$, $\omega_{lattice}\to N^*\omega_C$ moves NEITHER $c$ NOR $Z_0$ —
$N^*$ only splits granularity between space and time, exactly as joint 3 requires. The derivation
cannot move the true canon anchors.

**Downstream (stated plainly):**
1. **Muonic band-split / [B-AVE] arm.** A finer pitch ($a=\lambdabar_C/N^*$ with $N^*\ge7$) pushes the
   continuum-validity floor DEEPER — the continuum approximation holds to finer scale, so the [B-AVE]
   exclusion **STRENGTHENS**. This closes our own hatch further; we say so plainly.
2. **Eigencavity arc (Task #11) starting grid:** hand it $N\ge7$ (the floor); the eigencavity search
   need not consider $N<7$ (no representable $(2,3)$ below the floor).
3. **Muon-decay corollary (QUALITATIVE; quantitative content = NEEDS-DERIVATION).** Heavier lepton =
   higher $\omega_{mode}$ = fewer ticks $N$ = closer to / below the sampling floor = undersampled →
   structurally unstable → decays. The electron (lightest) has the most ticks (best sampled = most
   stable). **NO mass-ratio numerology** — the map $N\leftrightarrow$ mass and any $m_\mu/m_e$ value
   is explicitly NEEDS-DERIVATION; no fit to 206.77 is attempted or implied.
4. **Dilation universality (QUALITATIVE, engine-demonstrated at (ii)).** The locked tower
   down-regulates rigidly by $\sqrt{1-A^2}$ with the integer $N$ protected → universality of time
   dilation across the tower. Quantitative dilation law = NEEDS-DERIVATION.

**The "7" coincidence (flagged, NOT claimed as source).** $N_{min}=7$ coincides numerically with the
AVE "7"-family (Poisson $2/7$, the $/7$ couplings, $\sqrt7$). The floor derivation makes **zero
contact** with any of those — it is pure $(2,3)$ Nyquist ($2k_{max}+1$). Flagged as a
coincidence-to-watch, not asserted as a shared mechanism.

## CONSISTENCY-vs-EMERGENCE TAG

- **$N_{min}=7$ (the floor):** **EMERGENCE-class candidate** — a dimensionless integer forced by the
  substrate's own sampling of the $(2,3)$ topology, with the $\alpha$-firewall mechanically certified
  green (no CODATA / $\alpha$ / lepton-mass input on the derivation path). It is NOT a
  CODATA-derived-through-SI-substitution echo (contrast the A47 v17 family). The honest caveat: it is
  an emergent *floor*, not an emergent $m_e$ — the ceiling that would turn the floor into a
  mass-forcing window is contradicted (lossless) / open (pending $\eta(N)$).
- **The pricing + dilation + $c/Z_0$ invariance:** CONSISTENCY-class (re-express canon; no new number).
- **No emergence headline beyond the floor integer** until (a) $\eta(N)$ is adjudicated and (b) if a
  ceiling re-emerges it is re-checked for hidden circularity.

---

## ADJUDICATION AGAINST THE FROZEN PREREG BINS

| Prereg bin / falsifier | Outcome |
|---|---|
| Window bin | **[FLOOR-ONLY]** — as pre-registered most-likely ✅ |
| Expectation 1 ($N_{min}=7$, both legs, N=5/6/7 transitions) | ✅ exact (G1 reconciled) |
| Expectation 2 (lock-range $\kappa/N$, cold ⇒ no ceiling) | Partial — cold ⇒ no ceiling ✅; but the lossless form is $\sqrt N$ not $\kappa/N$ (see flag-don't-fix; ERRATUM E2) |
| Expectation 3 (routed [FLOOR-ONLY]) | ✅ |
| Expectation 4 (TOWER-EMERGES) | ✅ (global dilation, $N$ intact) |
| Expectation 5 (C-INVARIANT) | ✅ (rel_diff 0.0, $N$-independent) |
| F-FIREWALL | Green — no quarantined symbol on either derivation path (mechanically enforced) ✅ |
| F1 (floor≠7) | Not triggered ($N_{min}=7$) |
| F2 (engine≠analytic) | Not triggered (G1 exact) |
| F3 (strain de-coheres all $N$) | Not triggered (TOWER-EMERGES) |
| F4 (C-VIOLATED) | Not triggered |
| F5 ($dt$-is-the-clock) | Not triggered ($N_{min}$ invariant) |

---

## ERRATA (append-only; freeze integrity — prereg body unedited)

- **ERRATUM E1 (collision framing, cosmetic).** The prereg states the reflection collision as
  "$3\equiv-2\pmod5$" (the $k_2\equiv-k_1$ framing). The Leg-A driver initially reported the
  equivalent $k_1\equiv-k_2$ framing (both $\equiv2$); aligned to the prereg's $k_2\equiv-k_1$ framing
  (both $\equiv3$) in the tests-commit. Same congruence ($2+3\equiv0\pmod5$); no physics change.
- **ERRATUM E2 (the ceiling's $N$-scaling — a REFINEMENT forced by the lossless dynamics).** The
  prereg's Leg A(b) pre-committed the *first-order* Adler lock half-range $\kappa/N$ (shrinking).
  Running the Ax3-lossless substrate directly (Leg B) showed the conservative pendulum lock range
  **grows as $\sqrt N$** — the first-order $\kappa/N$ is the *dissipative reduction*, not the lossless
  substrate's own dynamics. This does NOT change the routed bin (still FLOOR-ONLY — both readings give
  no clean $\alpha$-free ceiling in the cold/lossless case), but it CONTRADICTS the direction of
  joint-4's "shrinks with $N$" ceiling candidate. Surfaced flag-don't-fix (both numbers shown); the
  resolution hinges on the div-$N$ harmonic dilution $\eta(N)$, a plumber-physical question for Grant.
