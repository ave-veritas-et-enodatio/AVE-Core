# PREREG (FROZEN) — The electron tick-floor: a substrate-forced sampling integer for the (2,3) mode

**Arc:** analysis/electron-tick-floor · Task #10-family (Grant-fired after a full three-joint in-chat walk, 2026-07-06/07)
**Repo:** AVE-Core (PUBLIC) · **Branch:** analysis/electron-tick-floor off origin/main (tree-proof: HEAD @ `a95f772d`)
**Date frozen:** 2026-07-07 · **Status:** PRE-REGISTRATION — ontology + model definition + deliverable bins + firewall + homonym guard + expected outcomes, frozen BEFORE the RESULT / drivers / figure.

> This document is frozen in its own commit. The RESULT doc, the two drivers, the figure, and the
> tests land in subsequent commits and are adjudicated against the bins below. **No bin is redefined
> post-hoc to convert a ❌ to a ✅ (Rule 11).** This arc has CHORD POTENTIAL (a substrate-forced
> dimensionless integer); the discipline bar is maximal, and the α-circularity firewall (below) is
> load-bearing, not decorative.

---

## THE GRANT-BLESSED ONTOLOGY (walked and ratified in-chat 2026-07-06/07 — the FRAMING; this arc TESTS it, does not re-derive it)

Cite of the walk: **Grant-blessed, three joints, 2026-07-06/07.** The four joints:

1. **TEMPORAL, NOT SPATIAL.** The electron is a $0_1$-unknot LC-tank mode whose $(2,3)$ content lives
   in **phase space** — two internal angles winding 2 and 3 times per mode period on the Clifford
   torus (existing canon: `manuscript/ave-kb/CLAUDE.md` INVARIANT-N1 knot-disambiguation; the $(2,q)$
   labels are *phase-space winding portraits*, NOT real-space body knots). The lattice constraint on
   it is **ticks per mode period**, not nodes per ring. The electron is an injection-locked $\div N^*$
   subharmonic of the local lattice clock: $\omega_{lattice} = N^* \cdot \omega_{mode}$.
2. **RELATIVE CLOCKS, ABSOLUTE FRAME.** No master oscillator — each cell is its own LC tank; "the
   carrier" is the **mutual injection lock** of a neighborhood (power-grid synchrony — Grant's own
   domain). The lattice rest frame exists (canon: third-deletion / INVARIANT-S2), but tick *rates*
   are local and only rate-*gradients* are observable (the temporal twin of INVARIANT-S2).
3. **LATTICE SPEED CEILING.** $c = a\cdot\omega_{lattice}$ per cell ($=1/\sqrt{LC}$). **Critical
   invariance:** under the re-pricing $a\to \lambdabar_C/N^*$, $\omega_{lattice}\to N^*\cdot\omega_C$,
   the product $c$ is FIXED — the derivation cannot move $c$ or $Z_0$ (the true canon anchors);
   $N^*$ only splits granularity between space and time.
4. **"Electron = absolute clock floor."** Stability requires $N \ge N_{min}$ (sampling floor);
   candidate ceiling $N \le N_{max}$ (mutual-lock range shrinks with division ratio, Adler-class). If
   the window is tight, $m_e$ is FORCED as a dimensionless ratio of the lattice clock. Qualitative
   corollaries (NOT number-fit): heavier leptons = fewer ticks = undersampled = decay (muon
   instability structural); dilation = carrier down-regulation with integer-protected lock ratios
   (universality derived).

---

## REGIME HEADER (mandatory — read before any dynamical claim)

- **MODE:** small-signal phase dynamics of a coupled LC-tank ensemble; no rupture, no pair
  production. Below every yield threshold.
- **REGIME:** COLD lattice base ($A=0\Rightarrow S=1$ on every bulk port), **lossless-reactive**
  (Ax3): the ensemble is a conservative (Hamiltonian) phase lattice — energy $H=T+V$ is a tracked
  conserved quantity, NOT a Lyapunov function relaxed to a basin. Any first-order-Kuramoto reading
  (relaxation-to-sync, gradient-descent-to-equilibrium) is an **SM/continuum leak** and is rejected
  in favour of the second-order (inertial, energy-conserving) rotator lattice — see the
  substrate-native walk, CP1/CP-lossless.
- **PHASE-STATE:** cold identical cells for the FLOOR + the two internal-null kill-joints; a
  deliberately down-regulated sub-patch (per the canonical $\sqrt{S}$ loading) ONLY inside the
  tower/strain kill-joint (ii).
- **METHOD-NOT-PHYSICS declarations:** discrete-time integration (symplectic leapfrog), the
  phase-reduced coupling form $\sin(\Delta\theta)$, the ring reduction of the K4 topology, and the
  substep $dt$ are ALL numerical method. The substrate-native check (below) requires an explicit
  proof that the integrator substep is **not** the answer's clock — a $dt\to0$ convergence study is
  mandatory and pre-committed here.

## SECTOR HEADER + HOMONYM GUARD

- **Which sector?** The mode is the **V-sector / phase-space** object (the $(2,3)$ winding of the
  bond-LC phasor on the Clifford torus). It is NOT measured in real-space (R,r) lattice-Cartesian
  coordinates — see the phase-space-coordinate-check section. The ensemble "carrier" is the mutual
  lock of the cells' LC clocks.
- **Does the engine carry the DOF?** The two internal angles $(\alpha,\beta)$ winding $(2,3)$ are
  the phase-space DOF; the ensemble phase $\theta_i$ per cell is the clock DOF. A lightweight
  verify-script-class phase-lattice carries both (no new engine version — see PLATFORM).
- **NAMED HOMONYM GUARD (binding, load-bearing):**
  - **$N$** (this arc) = **sampling count** = ticks per mode period = the division ratio of the
    $\div N$ subharmonic. An integer of *representability + lock*.
  - **$Q$** (elsewhere in canon) = **coherence count** = radians rung per unit energy lost =
    $Q_{TANK}=1/\alpha$ (an *identity*, per memory `project_alpha_keystone_echo_resolved`, NOT a
    derivation). An integer/real of *dissipation*.
  - **These are two different numbers on the same object.** If the derivation lands $N^*$ near 137 it
    must arrive with **zero contact** with the $Q=1/\alpha$ identity, or it is circular and gets
    binned so. (Pre-commitment: the FLOOR derived below lands at **7**, three-and-a-half OOM away
    from 137 and with zero $\alpha$ content — the guard is armed but not expected to fire.)

## THE α-CIRCULARITY FIREWALL (the knife — binding on the DERIVATION CHAIN)

The Leg-A + Leg-B **derivation chain** (the drivers `electron_tick_floor_sampling.py` and
`electron_tick_floor_engine.py`, and every number they consume) **MAY NOT reference**, import, or be
tuned to:

- `ALPHA`, `ALPHA_COLD`, `ALPHA_COLD_INV`, `M_E`, `L_NODE` (= $\lambdabar_C$), `OMEGA_C` as the
  electron scale, `Q_TANK`/`1/ALPHA`, the Compton relation $\lambdabar_C=\hbar/m_ec$, `R_I=\sqrt{2\alpha}`,
  or ANY measured lepton mass / mass ratio.

They enter ONLY in the clearly-firewalled **§COMPARISON** of the RESULT doc, which is written AFTER
the window verdict is routed. **F-FIREWALL (kill condition):** if either driver imports any
quarantined symbol on the derivation path, or if $N_{min}$/lock-range/window moves when a coupling is
re-tuned toward a lepton target, the "substrate-forced" claim is void and the result is binned an
ECHO (calibration), not a chord. A CI test (`test_firewall_no_alpha_on_derivation_path`) greps both
drivers for the quarantined symbols and fails on any hit outside a `# FIREWALL-COMPARISON` block.

The couplings the drivers DO use ($\kappa_{ens}$, $\kappa_{mode}$, cell count $M$, cluster size $P$,
ensemble frequency $\omega_{ens}$ in method units) are **dimensionless method parameters**, declared
as such; the FLOOR result is proved **independent** of all of them (it is pure representability), and
the window's ceiling is reported **parametrically** in the loading, never number-fit.

---

## CORPUS GROUNDING (re-grepped verbatim at branch tip `a95f772d` — prior art, prefer-extension check)

| Anchor | Content / role | Relation |
|---|---|---|
| `CLAUDE.md` (ave-kb) INVARIANT-N1 | "$(2,q)$ torus knot labels refer to **phase-space winding portraits** on the bond-pair LC tank (Clifford torus), **not** real-space body knots" | The $(2,3)$-lives-in-phase-space anchor. Load-bearing for the phase-space-coordinate discipline. |
| `INVARIANT-S2` (ave-kb CLAUDE.md) | Ax1 = "intrinsic LC oscillators at each node … Trace-Reversed Chiral LC Network"; Ax3 = "lossless reactive cycling, $S_{11}$ minimization" | The ensemble = coupled intrinsic LC oscillators; Ax3 forces the **lossless** (conservative) model. |
| `src/scripts/vol_4_engineering/k4_bloch_dispersion.py` + `research/2026-06-22_k4-bloch-dispersion-quartic_result.md` | K4 Bloch band structure; the loaded-line dispersion | Prior art for the ring/lattice dispersion; the c-invariance (iii) measurement composes with the sine-law band. |
| `graded-network-response.md` (via semiconductor prereg :69) | "series $L$ per bond, shunt $C$ per node"; $\omega(q)=(2c_0/\ell_{node})|\sin(q\ell_{node}/2)|$ | The canonical propagating LC-ladder dispersion. The engine's finite signal velocity (iii) is this band's group speed. |
| `src/scripts/vol_1_foundations/pilot_field_wavetrain.py` | 2-DOF elastic RingChain, velocity-Verlet, PERIODIC ring, "no PML (closed ring)" | Prior art for the closed-ring conservative-integrator pattern. **NOT reused** (it is an FDTD-class elastic host, not a phase-oscillator clock lattice — wrong abstraction level for a clock-ratio question); pattern (closed ring + symplectic) inherited, code not imported. |
| `src/scripts/vol_1_foundations/op21_multimode_derivation.py` | Op21 mode counting | Prior art for lattice-mode counting; orthogonal (spatial modes, not temporal ticks). |
| `src/scripts/vol_3_macroscopic/simulate_phase_locked_superconductivity.py` | phase-locked (Josephson-class) synchrony | The lossless-injection-lock precedent (Josephson/Shapiro-step $\div N$ locking is lossless subharmonic lock — the physical warrant that injection lock exists in an Ax3-lossless medium). |
| memory `project_alpha_keystone_echo_resolved` | $Q_{TANK}=1/\alpha$ is an **identity**, not a derivation | The homonym guard's $Q$ side; cite as identity NOT derivation. |

**Prior-art verdict:** no existing driver models the temporal $\div N$ tick-floor for a $(2,3)$
subharmonic. The closest platforms (pilot-field ring, k4-bloch) are real-space spatial-mode drivers.
This arc's model is a **new lightweight verify-script-class phase lattice** (justified
substrate-natively below), NOT a new engine version, with tests + standing falsifiers.

---

## SUBSTRATE-NATIVE CHECK (walked BEFORE any solver code — the 8-checkpoint walk)

Fired per operating-principle 1. Walk recorded so the auditor can re-run it.

- **CP1 — substrate dynamics.** The problem is **coupled LC-tank clock synchrony** (mutual injection
  lock) + **discrete-time sampling** of a phase-space winding. The substrate runs **wave propagation
  on a lossless reactive network**, NOT energy minimization. **CATCH:** first-order Kuramoto
  ($\dot\theta=\omega+K\sin\Delta\theta$) has a Lyapunov function → relaxes to sync = a
  *dissipative* (gradient-descent) reading → an **Ax3-lossless violation / SM leak**. Rejected. The
  substrate-native model is the **second-order (inertial, Hamiltonian) rotator lattice** — energy
  conserving, mutual-locking, and (crucially) it **propagates perturbations at a finite wave speed**
  (needed for kill-joint iii). This is the Josephson-array / conservative-swing family.
- **CP2 — sector.** V-sector / phase-space (the $(2,3)$ winding of the phasor), NOT Cos-sector
  real-space. The mode's topology is measured in the internal angles $(\alpha,\beta)$, not lattice
  positions.
- **CP3 — AVE-native objective.** Not "minimize an energy functional." The objective is
  **representability** (can $N$ ticks distinctly carry the $(2,3)$ pair) + **lock stability** (does
  the $\div N$ subharmonic stay entrained). Both are wave/sampling questions.
- **CP4 — phase-space vs real-space (A46).** The $(2,3)$ prediction is in phase-space (Clifford
  torus). The engine **seeds and measures the windings in the internal-angle coordinates**
  $(\alpha,\beta)$ — the correct phase-space coordinates — NOT via real-space lattice-Cartesian
  proxies. See the dedicated phase-space section below.
- **CP5 — saturation-modulated local clock.** Used ONLY in kill-joint (ii): the strained sub-patch's
  cells run at $\omega_{local}=\omega_{global}\sqrt{1-A^2}$ (Op14). This is the substrate-native
  source of the ceiling detuning — and it is presented **parametrically in $A^2$** (the firewall
  forbids plugging $A^2=\sqrt{2\alpha}$ on the derivation path; that substitution lives only in the
  firewalled §COMPARISON).
- **CP6 — reactance pair.** The lossless check tracks BOTH the C-state (phase $\theta$) AND the
  L-state (momentum $\Omega=\dot\theta$) at every step; $H=\tfrac12\sum\Omega_i^2 - \kappa\sum\cos\Delta\theta$
  is recorded over the whole window and its conservation asserted ($|\Delta H/H|\le$ tol). A
  single-phase snapshot is NOT accepted as a lock verdict.
- **CP7 — sampling discipline.** No PML (closed ring; boundedness on the ring itself). The winding is
  read from the *whole* tick-sampled trajectory, not a single peak/centroid.
- **CP8 — model the generative process, not the finished product (hosting-test discipline).** This
  test asks *"at which $N$ does a GIVEN $(2,3)$ mode hold its windings?"* — a **representability +
  persistence-vs-$N$** question, NOT *"does the engine spontaneously grow a $(2,3)$?"*. Planting the
  $(2,3)$ and measuring **where across the blind $N$ sweep it FAILS** is the disambiguating design
  (the DECAY / ALIAS bin is the discriminator; the $N$-dependence of the failure localizes the floor,
  exactly as injecting a known signal and finding its Nyquist alias localizes a sampler's floor).
  This is the sampling-floor analog of CP8, not a plant-and-confirm-persistence.

**Exit:** all checkpoints resolved; the one genuinely open physics fork (whether the ceiling is a
clean substrate-intrinsic integer or a soft parametric/size-dependent bound) is converted to a
**computable discriminator** (the four window bins below) rather than pressed for a fiat ruling —
per pre-test-physics-check Trigger 9 (fork-to-computable). See "PHYSICS-CHECK QUESTION" below.

## PHASE-SPACE COORDINATE CHECK (A46 — fired at test-design time)

- **Corpus claim coordinates:** the $(2,3)$ topology is in **phase-space** on the Clifford torus
  (INVARIANT-N1). Phase-space.
- **Test coordinates:** the engine reads the two internal angles $(\alpha,\beta)$ directly (the mode's
  own phase-space), and the winding numbers are counted from the tick-sampled angle trajectories. The
  ensemble clock is read from cell phases $\theta_i$. **No real-space (R,r) lattice-Cartesian
  extraction is on the load-bearing path.**
- **Match:** YES. The sampling floor is a statement about how many ticks per period are needed to
  carry the phase-space winding pair distinctly — a phase-space-native question answered in
  phase-space-native coordinates.

## PHYSICS-CHECK QUESTION (pre-test-physics-check — surfaced, corpus-searched, converted to computable)

One plumber-physical question the walk surfaced: **"Is the electron's $N^*$ pinned by a clean
substrate-intrinsic CEILING (a second forced integer), or does the electron sit AT the sampling
floor with the ceiling only soft/parametric — so that the robust forced quantity is the floor
integer alone?"** Corpus-searched (injection-locking / Adler / subharmonic / mode-counting): the
corpus has the floor ingredients (Nyquist, LC-ladder dispersion) but **no derived clean ceiling
integer**. Per the fork-to-computable discipline this is NOT pressed for a fiat ruling — it is the
axis the four window bins discriminate, and both legs report into them. The Grant-blessed ontology
already rates the ceiling "candidate" (joint 4), consistent with this being the open half.

---

## THE MODEL (Leg B — FROZEN BEFORE ANY RESULT)

**Platform:** a new lightweight **verify-script-class** phase lattice
(`src/scripts/verify/electron_tick_floor_engine.py`), with tests. NOT a new engine version. Justified
substrate-natively: the clock-ratio / mutual-lock question lives at the LC-tank **phase-dynamics**
abstraction; a full K4-TLM lattice would over-model it and bury the $N$-window under spatial-mode
clutter. This is the "honest 1D/ring reduction, justified substrate-natively" the brief permits.

**Ensemble (the carrier — mutual lock, NO master oscillator).** $M$ cells on a periodic ring, each a
lossless rotator (the phase-reduced intrinsic LC clock). Second-order (inertial, Hamiltonian):
$$\dot\theta_i = \Omega_i,\qquad \dot\Omega_i = \kappa_{ens}\big[\sin(\theta_{i+1}-\theta_i)+\sin(\theta_{i-1}-\theta_i)\big].$$
Conserved: total momentum $\sum\Omega_i$ and energy $H$. Mutual lock = frequency entrainment to an
**emergent** common $\Omega$ (computed from the cells each step; never imposed). Cold: $\Omega_i(0)=\omega_{ens}$
for all $i$. Finite signal velocity (second-order ⇒ hyperbolic ⇒ waves) — the object kill-joint (iii)
measures.

**Mode (the electron — a $\div N$ subharmonic with internal $(2,3)$).** A subharmonic oscillator at
$\Omega_{mode}\approx\omega_{ens}/N$ with fundamental phase $\varphi$, whose two internal angles are
$\alpha = 2\varphi$, $\beta = 3\varphi$ (the phase-space $(2,3)$ winding). Bilaterally coupled to a
sub-cluster of $P$ cells via the $\div N$ (N-fold) Adler torque:
$$\dot\varphi = \Omega_{mode},\qquad \dot\Omega_{mode} = \frac{\kappa_{mode}}{P}\sum_{i\in cluster}\sin(\theta_i - N\varphi),$$
with the **bilateral** back-reaction on each cluster cell $\dot\Omega_i \mathrel{+}= \frac{\kappa_{mode}}{P}\sin(N\varphi-\theta_i)$.

**Ticks + winding measurement (phase-space-native).** A lattice tick is marked when the ensemble mean
phase $\Psi=\arg\sum_i e^{i\theta_i}$ advances by $2\pi$. The mode's $(\alpha,\beta)$ are **sampled at
ticks** and the winding pair is counted with the **discrete principal-branch estimator** (nearest
$2\pi$ branch per step) — the estimator that ALIASES exactly when a per-tick advance exceeds $\pi$,
i.e. the physical sampling floor. This is an INDEPENDENT code path from Leg A's modular arithmetic.

**Integrator:** symplectic leapfrog, substep $dt = T_{tick}/n_{sub}$; the $dt\to0$ (increasing
$n_{sub}$) convergence study is mandatory and its result reported (the window verdict must be
$dt$-invariant, proving the substep is not the clock).

---

## LEG A (analytic) — what it derives

**A(a) THE FLOOR — $N_{min}$ from sampling (sympy + modular arithmetic).** Represent $k=2$ AND $k=3$
phase windings **distinctly** on $N$ ticks/period. Two conditions:
1. **Handedness-preserving non-aliasing (strict Nyquist):** each $|k| < N/2$ so the sign (chirality)
   of the winding survives; the binding one is $k_{max}=3\Rightarrow N>6$.
2. **Non-collision:** $k_1=2$ and $k_2=3$ land in distinct principal bins, $k_1\not\equiv\pm k_2\pmod N$.

Pre-committed transitions (to be sympy-proved): **$N=5$ collides** ($3\equiv-2\pmod5$, so the 3-winding
is indistinguishable from the reflection of the 2-winding); **$N=6$ is Nyquist-degenerate for $k=3$**
($3=N/2$, the $\pm3$ alias merges, chirality lost — alias-marginal, sampling-phase-sensitive);
**$N=7$ first clean** ($3<7/2$, $2\not\equiv\pm3\pmod7$). **$N_{min}=7$.**

**A(b) THE CEILING — Adler-class $\div N$ lock range.** Adapt injection-locking (Adler's first-order
phase equation, the 2-oscillator Kuramoto) to a $\div N$ subharmonic in a bilaterally-coupled mesh
whose reference IS the emergent mutual-lock frequency. Derive the fractional lock half-range vs
division ratio $N$ and coupling $\kappa$; pre-committed form (phase-averaging dilution of the
subharmonic pull):
$$\frac{\Delta\omega_{lock}}{\omega_{mode}} \;=\; \frac{\kappa}{N},$$
so the lock holds iff the detuning $\delta$ (the fractional offset the mode must overcome) satisfies
$\delta \le \kappa/N$, i.e. **$N \le N_{max}=\kappa/\delta$.** In a **cold identical** lattice
$\delta=0\Rightarrow N_{max}=\infty$ (FLOOR-ONLY). A finite ceiling requires a substrate-intrinsic,
$N$-independent absolute detuning; the physical candidate is the seed's own down-regulation
$\delta_{seed}=1-\sqrt{1-A^2}$ (Op14, CP5) — reported **parametrically in $A^2$** (firewall). The
lock-range formula is checked in sympy (RESULT doc); whether it yields a clean integer ceiling is the
open half the bins discriminate.

**A(c) THE WINDOW — intersect.** Route the verdict into exactly one bin (below).

---

## DELIVERABLE BINS (the window verdict — pre-committed, mutually exclusive, Rule-11 frozen)

- **[WINDOW-DERIVED: $N^*$]** — floor AND a clean substrate-intrinsic ceiling intersect to a tight
  window; $N^*$ (hence a forced dimensionless mass ratio) is pinned. Requires the ceiling to be a
  clean integer with NO $\alpha$ contact on the derivation path.
- **[FLOOR-ONLY]** — $N_{min}$ is robustly forced (=7 expected) but the ceiling is soft / parametric
  / size-dependent; the robust forced quantity is the floor integer alone. **(Pre-registered as the
  most likely outcome** — the cold identical lattice has $\delta=0\Rightarrow$ no clean ceiling, and
  the ceiling candidate needs the seed loading which is parametric.)
- **[NO-CONSTRAINT]** — neither a floor nor a ceiling survives (sampling does not obstruct any $N$).
- **[UNSTABLE-ALL-N]** — no $N$ holds the $(2,3)$ (the mode never locks / always aliases) — would
  falsify the subharmonic ontology.

## THE THREE ENGINE MEASUREMENTS (all blind; the two kill-joints named)

- **(i) LOCK/DECAY vs $N$** (sweep $N=4..16$, spot checks 20, 30). Two sub-axes, both blind:
  (i-a) **representability** — does the tick-sampled $(\alpha,\beta)$ read the correct $(2,3)$ pair?
  (i-b) **lock** — does $\varphi$ stay $\div N$-entrained over $\ge$ many mode periods (phase error
  bounded)? The empirical window = $\{N:\text{both hold}\}$, compared to Leg A. **G1 ReconcileGate:**
  engine representability-transition $N_{min}$ == analytic modular $N_{min}$ == 7 (independent code
  paths).
- **(ii) [TOWER-EMERGES / TOWER-FAILS]** (kill-joint). Down-regulate a sub-patch's cells per the
  canonical $\sqrt S$ loading ($\Omega\to\Omega\sqrt{1-A^2}$). Does the locked cluster down-regulate
  **rigidly with the integer ratio $N$ intact** (dilation universality derived — TOWER-EMERGES) or
  **de-cohere** (lock breaks — TOWER-FAILS)? Map the ceiling $N_{max}(A^2)$.
- **(iii) [C-INVARIANT / C-VIOLATED]** (kill-joint, Michelson-class internal null). Signal velocity
  through the patch WITH vs WITHOUT the locked mode present; must equal the bare coupling velocity and
  be $N$-independent. **G2 ReconcileGate:** $|c_{with}-c_{without}|/c_{without}\le$ tol, and
  $N$-independence.

## EXPECTATIONS (pre-committed — honest, no rescue)

1. **$N_{min}=7$** from both Leg A (modular/sympy) and Leg B (engine representability transition),
   agreeing exactly (G1). $N=5$ COLLIDE, $N=6$ NYQUIST-MARGINAL, $N=7$ CLEAN.
2. **Lock-range** $\Delta\omega/\omega=\kappa/N$ proved in sympy (RESULT doc); **cold** ⇒ no ceiling.
3. **Routed bin: [FLOOR-ONLY]** is the pre-registered most-likely outcome (robust floor 7; soft
   parametric ceiling). [WINDOW-DERIVED] only if a clean α-free integer ceiling emerges — not
   expected; if it emerges it is scrutinised hard for hidden circularity before being headlined.
4. **(ii) TOWER-EMERGES** expected for $N$ below the parametric ceiling (rigid down-regulation,
   integer protected) → dilation-universality qualitative corollary; **TOWER-FAILS** at high $N$/high
   strain → maps $N_{max}(A^2)$.
5. **(iii) C-INVARIANT** expected: the mode is a subharmonic passenger; the coupling velocity is set
   by the ensemble band, not the mode. A C-VIOLATED result would be a serious internal inconsistency.
6. **CONSISTENCY / EMERGENCE tag:** the FLOOR integer is an **emergence-class** candidate *only if*
   it is fully lattice-derived with zero α-contact (the firewall's job to certify). If any α-contact
   is found it demotes to consistency/echo. The $\sqrt S$ loading and the $c$/$Z_0$ invariance are
   consistency-class (they re-express canon). No emergence headline is written until the firewall test
   is green.

## DIMENSIONAL / MAGNITUDE PRE-CHECK (ave-prereg Step 3.5)

$N_{min}$ and $N_{max}$ are **dimensionless integers**; no dimensionful magnitude is predicted on the
derivation path. The lock-range $\Delta\omega/\omega=\kappa/N$ is dimensionless in $\kappa$ (a
coupling ratio) and $N$. The only dimensionful re-pricing ($a=\lambdabar_C/N^*$) is firewalled to
§COMPARISON and is a *consistency* restatement with $c,Z_0$ held invariant by construction — no new
number originates. Power-counting for the floor: the binding exponent is the Nyquist $2k_{max}<N$
(linear in $k_{max}$), giving $N>6$; no hidden dimensional assumption.

## WHAT WOULD FALSIFY (pre-committed kill conditions)

- **F-FIREWALL** (above): any quarantined α/$m_e$/$\lambdabar_C$ symbol on the derivation path, or a
  window that moves under coupling re-tune toward a lepton target ⇒ ECHO not chord.
- **F1 (kills the floor):** if the sympy modular derivation does NOT give $N_{min}=7$ (e.g. $N=6$ is
  clean, or $N=5$ does not collide), the FLOOR framing is wrong; re-derive or bin NO-CONSTRAINT.
- **F2 (kills the engine↔analytic bridge):** if the engine representability transition $N_{min}\ne7$
  (G1 DISCREPANT-HALT fires), the two legs disagree — surface the conflict (flag-don't-fix), do NOT
  reconcile by tuning either path.
- **F3 (kills the dilation corollary):** if strain (ii) de-coheres the lock for ALL $N$ (even small
  $N$ well below any ceiling), the "rigid integer-protected down-regulation" corollary is false;
  TOWER-FAILS is routed and the dilation-universality claim is NOT written.
- **F4 (kills the internal null):** if C-VIOLATED — signal velocity depends on the mode's presence or
  on $N$ — the "mode is a passenger" reading fails; surface as an internal inconsistency, do not
  massage the tolerance.
- **F5 (integrator-is-the-clock):** if the window verdict moves with $dt$ (fails the $dt\to0$
  convergence study), the substep is the answer's clock — the result is a numerical artifact, void.

## §COMPARISON PLAN (firewalled — written in the RESULT only AFTER the window is routed)

If a floor/window emerges: (1) price pitch $a=\lambdabar_C/N^*$ and state $c=a\cdot\omega_{lattice}$
and $Z_0$ **invariance explicitly** under the re-pricing; (2) re-state what a finer pitch does to the
muonic band-split and the [B-AVE] arm — a finer pitch pushes continuum validity DEEPER, so the
exclusion STRENGTHENS (this closes our own hatch further; say so plainly); (3) hand the eigencavity
arc (Task #11) its starting grid ($N\ge7$); (4) state the muon-decay ("heavier = fewer ticks =
undersampled = decay") and dilation-universality corollaries as QUALITATIVE consequences with their
quantitative content marked **NEEDS-DERIVATION** — NO mass-ratio numerology (if I catch myself fitting
206.77, I stop and bin it). The homonym note (7 is the sampling floor, three-plus OOM from the
$Q=1/\alpha$ coherence count) is restated. The AVE "7"-family coincidence (2/7 Poisson, /7 couplings,
$\sqrt7$) is FLAGGED as a coincidence-to-watch, NOT claimed as the source (the floor is pure $(2,3)$
Nyquist).

## LANE DISCIPLINE

Implementer lane. The window verdict + §COMPARISON are STAGED in the RESULT for the orchestrator/Grant;
no KB manual is landed here (the auditor lands manuals). Flag-don't-fix on any Leg-A↔Leg-B conflict:
surface both paths + verbatim numbers, do not reframe one to match the other. PR opens
`[REVIEW: pending-orchestrator]`, DO-NOT-MERGE, no self-merge.
