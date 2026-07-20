[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "routing-aid index — consolidates the scattered history-dependent (memory / hysteresis) canon by class and points at the canonical leaves; hosts no new physics (INVARIANT-S7: leaves are canonical, indexes are routing aids)"
-->

# Substrate Hysteresis / History-Dependent (Memory) Index

**Purpose**: routing-aid index that consolidates the AVE substrate's scattered **history-dependent (memory) physics** — Lenz-freeze latching, the τ_relax relaxation class, thixotropic / stick-slip / Bingham yield, cosmological defect-freezing, and the hysteresis loops of dynamic saturation — into one place, organized by class. The canon is real and partly derived, but it is spread across ~20 leaves in Vol 1, 2, 3, 4 + common with no consolidating section. This index closes that gap, applying the same kernel-catalog / analytical-toolkit-index pattern (see [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md), [`ave-analytical-toolkit-index.md`](ave-analytical-toolkit-index.md)) to memory physics.

**Origin**: 2026-06-08 (Grant directive). A dark-wake derivation cycle stalled because the smooth Axiom-4 kernel $S(A) = \sqrt{1 - A^2}$ is **memoryless** (algebraically symmetric in $A$), so the implementor went hunting for the Lenz-freeze latching that should have been one index-lookup away. The memory physics lives one level below the smooth kernel — in the *dynamics* of how the kernel relaxes — and was un-indexed.

**Routing-aid status (INVARIANT-S7)**: every claim cited below is owned by the canonical leaf it points to. This index asserts no new physics and carries no `clm-` of its own; consult the cited leaf (and, where one exists, its `claim-quality.md` entry) before treating any summary line here as a claim source.

---

## The headline scoping: reversible envelope vs. dynamic-crossing hysteresis

The load-bearing distinction — **already canonical** in [`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) §3 as the "two levels of the saturation kernel," recorded here as the organizing axis, not a new claim:

> **Same substrate, two regimes.**
>
> - **Reversible sub-yield envelope (Level 1, memoryless).** The smooth Axiom-4 kernel $S_{\text{eq}}(r) = \sqrt{1 - r^2}$ depends on $r^2 = (A/A_c)^2$ only — **no sign dependence, no path dependence.** Up-crossing and down-crossing see the same $S_{\text{eq}}$ at matched $r$. Below yield, away from a dynamic crossing, the substrate's saturation response is a reversible reactive envelope. ([`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) §3 Level 1, lines 68-72.)
> - **Dynamic-crossing hysteresis (Level 2, memristive).** The *actual* state $S(t)$ relaxes toward $S_{\text{eq}}$ with the finite time constant $\tau_{\text{relax}} = \ell_{\text{node}}/c$ via a first-order ODE $dS/dt = (S_{\text{eq}}(r(t)) - S(t))/\tau_{\text{relax}}$. The finite relaxation makes $S(t)$ lag — above equilibrium on up-crossing, below on down-crossing — so over a cycle $S(t)$ **encloses a hysteresis loop** $\oint S\, dr$ = dissipated energy per cycle. The substrate is therefore **memristive (path-dependent)**, even though the kernel form is symmetric. ([`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) §3 Level 2 + Key-Results table, lines 22-24, 74-89.)

Everything in the class tables below is a manifestation of Level 2 — the dynamics of crossing or being driven through saturation — at some scale. When a derivation needs memory, latching, freezing, or path-dependence, it is reaching for Level-2 physics; the smooth $\sqrt{1-A^2}$ envelope alone will not supply it.

> **🟢 Currency note (2026-06-10): this reversible-vs-memristive boundary is now empirically grounded, not just asserted.** The 2026-06-09 thixotropy bulk derivation landed the bulk volumetric-strain channel squarely on the **Level-1 (reversible / memoryless) side** — confirming, not contradicting, the scoping above. Details + citations in the §3 currency note below.

---

## §0 — Class taxonomy

| Class | What it is | Canonical home(s) |
|---|---|---|
| §1 Inductive / Lenz memory | Diverging $L_{\text{eff}}$ near $S \to 0$ generates Lenz back-EMF that blocks $d\omega/dt$ (or $dI/dt$); Op14 dynamic impedance is the substrate's history-dependent ("memristor") operating point | dark-wake BEMF synthesis; Op14 leaves; relativistic inductor; Newtonian-inertia-as-Lenz; geodynamo |
| §2 Relaxation-time class | $\tau_{\text{relax}} = \ell_{\text{node}}/c$ — the causal-minimum state-change time that makes the substrate memristive; the $\geq 100$-Compton-period persistence of frozen residues | τ_relax derivation; nonlinear vacuum capacitance |
| §3 Thixotropic / stick-slip / Bingham yield | Slow-grip / fast-slip: above yield the vacuum flows (Bingham plastic), then thixotropically re-freezes | saturation operator; temporal-regime tribology row; nonlinear vacuum capacitance |
| §4 Defect-freezing / matter-precipitation / ω-freeze | Topology that cannot unwind during a yield-crossing freezes in; cosmic spin frozen at lattice genesis; matter precipitation from cooling vacuum | τ_relax §4; Ω_freeze cascade; trampoline framework; Op14 cosmic-horizon profile |
| §5 Hysteresis loops in saturation | The reversible-envelope-vs-dynamic-latching scoping itself: pinched hysteresis loops, the loss-tangent temporal trichotomy, non-volatile kink memory | τ_relax §3; nonlinear vacuum capacitance (Vacuum Memristor); temporal-saturation-regime classifier; VCA kink trap |

---

## §1 — Inductive / Lenz memory (back-EMF yield-freeze, Op14 substrate memristor)

**WHEN TO USE**: deriving why a topologically non-trivial configuration resists change, latches, or freezes when driven through (or toward) saturation; any time the dynamics are governed by a *rate* ($d\omega/dt$, $dI/dt$) rather than an instantaneous amplitude.

| Leaf | What it covers | Canonical claim |
|---|---|---|
| [`dark-wake-bemf-foc-synthesis.md`](dark-wake-bemf-foc-synthesis.md) §1.2 (lines 42-46) | Diverging $L_{\text{eff}}$ (Op14 near $S = 0$) → diverging Lenz back-EMF **blocks $d\omega/dt$** during the $\tau_{\text{relax}}$ crossing window; topologically non-trivial $\omega$ **FREEZES**; residues persist $\geq 100$ Compton periods. Substrate-native (Axiom 1 + Op14 + Lenz), **not** a Kibble-Zurek import. | clm-exjfai |
| [`newtonian-inertia-as-lenz.md`](../vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md) (line 12) | Mass IS inductive resistance: $F = ma$ as the macroscopic consequence of Lenz back-EMF on a confined phase loop; inertia is the substrate's memory of its own flux. | clm-jwyy6l |
| [`relativistic-inductor.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md) (lines 14-16, 30-32) | $L_{\text{eff}}(I) = L_0/\sqrt{1 - (I/I_{\max})^2} \to \infty$ at $I_{\max}$ — the diverging-inductance mechanism that physically collapses the slew rate $dI/dt \to 0$ (the magnetic-sector projection of the same Axiom-4 kernel that the freeze rides on). | clm-p5cf3t |
| [`op14-local-clock-modulation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) | Op14 dynamic impedance $Z_{\text{eff}}(r) = Z_0/\sqrt{S(r)}$ — the **history-dependent (substrate-memristor) operating point**; at $A^2 \to 1$ the local clock freezes ($\omega_{\text{local}} \to 0$). The static limit gives gravity; the dynamic limit gives the BEMF-blocking (§5 of that leaf: inertial mass). | clm-1eg13f |
| [`op14-cross-sector-trading.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) | The **reactance pair**: Cosserat $\omega$ ↔ K4-inductive $\Phi_{\text{link}}$ energy trading via Op14 $Z_{\text{eff}}$ modulation, $\rho(H_{\text{cos}}, \Sigma\|\Phi_{\text{link}}\|^2) = -0.990$. The L-state ($\Phi_{\text{link}}$) is the inductive memory the C-state trades against. | clm-p2tp9i |
| [`geodynamo-vca-back-emf.md`](../vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md) | Planetary-scale instance: the geodynamo as a Topo-Kinematic inductive back-EMF generator (Earth dipole within factor-2 of empirical); Mars null = solid core → $R_{Fe} \to \infty$ collapses the eddy current. | clm-wd5rs0 |

**★ Cross-link (collapse-batch T2, KEEP-BOTH).** This §1 six-member rate-keyed family IS the "slew-instance catalog" that `common/universal-saturation-kernel-catalog.md:148-152` (RATING-TYPE block, GAP G2) calls "un-catalogued/empty," and that the X35 typing pass types as the slew column (`common/operators.md:82-93` §3.5; the headline GAP at `common/operators.md:128`). The two registers were not previously cross-linked *as the slew catalog*. The "slew" **label** is A4-contingent — the `common/operators.md:135-140` ratified 2×2 keys slew on the *conjugate rate*, but whether `L_eff(I)` keys on amplitude $I$ or its rate is the OPEN X35 A4; if amplitude-keyed this is the μ-sector dynamic-impedance/memory family, "same object, wrong column." Member count is **SIX** (per the #637 correction — `clm-p2tp9i` op14-cross-sector-trading was the omitted sixth).

**Pitfall**: the back-EMF freeze is **rate-dependent** — it only latches if the yield crossing takes $\geq \tau_{\text{relax}}$ (per dark-wake §1.2). A snapshot at one phase cannot distinguish a frozen latch from an oscillator caught at peak — record the C-state / L-state **pair** ([`op14-cross-sector-trading.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md)).

> **🔴 Correction pointer 2026-07-19 (clm-exjfai CONTESTED).** The row above ("residues persist ≥ 100 Compton periods") and this Pitfall's **direction** ("only latches if the crossing takes ≥ τ_relax" = slow→freeze) are both contested by the moving-front freeze-in engine result (`archive/analysis/moving-front-freezein` @ `f647f58b`): persistence measured **≤ 3.04 Cp** (~30× short), and the derivation gives the OPPOSITE direction (**fast→freeze / slow→heal**). See the demotion at `dark-wake-bemf-foc-synthesis.md` §1.2 + `claim-quality.md` (clm-exjfai, solidity `0.30→0.20`). CONTESTED not refuted (OPEN A44 fork; N=12–16 resolution-limited). Row/pitfall text preserved (KEEP-BOTH).
>
> **🔴 RULED 2026-07-20 (RULING 2, 2026-07-20 ratification batch — supersedes the CONTESTED status of the pointer above; KEEP-BOTH, both preserved).** Grant ratified 2026-07-20 (**Grant-verbatim, [sic]: "2 ratified"**; ruling content = the **orchestrator's walk, ratified in chat**). The N≥32 seed-controlled discharge (≤ 3.264 Cp; `research/2026-07-19_moving-front-freezein_landing-addendum.md` §2.1) closes the resolution caveat: **persistence RULED REFUTED-AS-STATED for BARE ω-loops** (A44 fork resolves toward corpus-over-claim — Ax1 does not promise pinning for a bare non-soliton loop; no engine pinning term "missing"), and **direction RULED fast→freeze** (this Pitfall's "only latches if the crossing takes ≥ τ_relax" = slow→freeze is BACKWARDS on its own τ_relax-slew-limit mechanism). **SCOPED OPEN for soliton-dressed defects.** Register now `clm-exjfai` confidence `0.20→0.15` ⇒ solidity `0.20→0.15` (refuted band). Row/pitfall text still preserved (KEEP-BOTH).

---

## §2 — Relaxation-time class (τ_relax, ≥100-Compton-period persistence)

**WHEN TO USE**: any time-domain problem with a transient, a finite response lag, a memristive ODE, a hysteresis-loop area, or a persistence/dwell timescale.

| Leaf | What it covers | Canonical claim |
|---|---|---|
| [`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) | **THE canonical relaxation-time leaf.** $\tau_{\text{relax}} = \ell_{\text{node}}/c \approx 1.288 \times 10^{-21}$ s from the per-cell K4 Lagrangian + causal propagation; no faster mode is axiom-permitted. Dynamic $S(t)$ relaxation ODE; up/down-crossing memristive lag; hysteresis loop area $\oint S\, dr$ = dissipated energy/cycle. | clm-n3un96 |
| [`nonlinear-vacuum-capacitance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) §"Vacuum Memristor" (lines 41-61) | Thixotropic relaxation time restated as the **memristor crossover**: at drive $f \gg 1/\tau_{\text{relax}} \approx 7.8 \times 10^{20}$ Hz the vacuum is too slow to yield (purely elastic / reversible); at $f \ll 1/\tau_{\text{relax}}$ full yield+recovery each cycle → maximum hysteresis loss. The crossover is set entirely by $\ell_{\text{node}}$ and $c$. | clm-8nkvwy, clm-vjv4zf |

**Persistence**: frozen-topology residues persist $\geq 100$ Compton periods in the post-heal solid regime ([`dark-wake-bemf-foc-synthesis.md`](dark-wake-bemf-foc-synthesis.md) §1.2, line 46) — i.e. $\tau_{\text{relax}}$ is the causal *minimum* state-change time, but the physical *persistence* of a frozen defect is far longer and memristive-state-dependent ([`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) §6).

> **🔴 Correction pointer 2026-07-19 (clm-exjfai CONTESTED).** The "≥100-Compton-period persistence" in this §2 header and paragraph is CONTESTED: the moving-front freeze-in engine run (`archive/analysis/moving-front-freezein` @ `f647f58b`) measured real-space persistence **≤ 3.04 Cp** (~30× short); mechanism = re-solidified Cosserat solid is linear-elastic with no topological-pinning term. CONTESTED not refuted (OPEN A44 fork; resolution-limited N=12–16). See `dark-wake-bemf-foc-synthesis.md` §1.2 + `claim-quality.md` (clm-exjfai). Header/paragraph text preserved (KEEP-BOTH).
>
> **🔴 RULED 2026-07-20 (RULING 2, 2026-07-20 ratification batch — supersedes the CONTESTED status of the pointer above; KEEP-BOTH, both preserved).** Grant ratified 2026-07-20 (**Grant-verbatim, [sic]: "2 ratified"**; ruling content = the **orchestrator's walk, ratified in chat**). The N≥32 seed-controlled discharge (≤ 3.264 Cp) closes the resolution caveat: the "≥100-Compton-period persistence" in this §2 header/paragraph is **RULED REFUTED-AS-STATED for BARE ω-loops** (A44 fork resolves toward corpus-over-claim; no engine pinning term "missing"). **SCOPED OPEN for soliton-dressed defects.** Register `clm-exjfai` confidence `0.20→0.15` ⇒ solidity `0.20→0.15` (refuted band). Header/paragraph text still preserved (KEEP-BOTH).

---

## §3 — Thixotropic / stick-slip / Bingham yield (slow-grip / fast-slip)

**WHEN TO USE**: a moving boundary, a yield-then-flow-then-reheal cycle, a rectification asymmetry between loading and unloading, or any problem where the vacuum behaves as a yield-stress (Bingham) plastic rather than a linear dielectric.

| Leaf | What it covers | Canonical claim |
|---|---|---|
| [`saturation-operator.md`](../vol1/operators-and-regimes/ch6-universal-operators/saturation-operator.md) (line 27) | Dielectric saturation as the **Bingham plastic yield**: the vacuum flows above $\tau_y = B_{\text{snap}}^2/2\mu_0$ (fluid-mechanics language for the Axiom-4 collapse of lattice permittivity under strong-field loading). | clm-gdd70j |
| [`peierls-nabarro-paradox.md`](../vol2/appendices/app-b-paradoxes/peierls-nabarro-paradox.md) (line 12) | The electron is a **co-moving self-matched envelope** presenting a **matched impedance** ($\Gamma \to 0$, Op17 $T^2 = 1-\Gamma^2 \to 1$) and coupling through **reactively** → zero-impedance phase slipstream; the nodes it passes **store and return reversibly** (sub-yield, lossless, Axiom 3). Resolves the would-be Bremsstrahlung paradox. *(Sub-yield lossless-reactive — distinct from the $\Gamma \to -1$ saturation confinement wall, and NOT the above-yield thixotropic re-freeze case of §3; entry retained here for cross-reference, not as a hysteresis/dissipative mechanism.)* | clm-ghs75o |
| [`temporal-saturation-regime-classifier.md`](temporal-saturation-regime-classifier.md) §11 Tribology (lines 178-186) | Stick-slip oscillation classified by static-vs-kinetic friction asymmetry → **Cyclic** temporal regime; Stribeck-curve mapping (hydrodynamic = lossless, boundary = lossy, dry/Coulomb = saturation boundary at slip). | clm-f0jwtk |
| [`nonlinear-vacuum-capacitance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) §"Vacuum Memristor (Thixotropic Hysteresis)" | In the near-yield dissipative channel (at/above $V_{yield}$), the dielectric-saturation→plastic transition requires a finite geometric relaxation time to liquefy the lattice — the thixotropic mechanism behind the pinched hysteresis loop (genuinely dissipative, Level-2 memristive; distinct from the sub-yield lossless regime). | clm-8nkvwy |

**Active research (off-branch — reference, not canon)**: the dark-wake rrad-L rectification thread (slow-grip / fast-slip Bingham-yield rectification of a driven dark wake) is being developed on the propulsion branch `analysis/2026-06-08-rrad-l-darkwake` as `research/2026-06-08_rrad-l-rectification_prereg.md` + `_result.md` (and the `_rrad-l-darkwake_` prereg/result pair). It is **not yet on main** and is not citable as canon from here; integration is handled separately by orchestration. (See report note: the seed-inventory-named `_rrad-l-stickslip-phase3_prereg.md` was not found on that branch as of this writing.)

> **🟢 Currency note (2026-06-10 — Rule 12, additive: the "Active research" paragraph above is preserved verbatim; points (1)-(2) supersede its now-stale status lines). Governing discipline: `verify-before-cite` + `ave-regime-phase-state-check`.**
>
> **(1) The rrad-L thread is now ON main, and its rectification leg is a regime-scoped NULL, not a surviving Bingham rectifier.** PR #144 (merged 2026-06-10, `7ee998f5`) landed all ten `research/2026-06-08_rrad-l-*` prereg/result docs — including `_rrad-l-stickslip-phase3_prereg.md` / `_result.md` — on `main` with **Rule-12 REGIME-RESCOPE headers (every body line preserved verbatim)**. This supersedes the "**not yet on main**" line and the "`_rrad-l-stickslip-phase3_prereg.md` was not found" report note above (both files are now on `main`). Per the merged rescope (`research/2026-06-08_rrad-l-rectification_result.md` header, 2026-06-09): the Phase 2-5 rectification nulls were **sub-yield-linear shear/chiral wrong-regime artifacts** — a null in a regime where the effect cannot exist, *not* a falsification. Rate-asymmetry / rectification can live only in the **bulk near-yield** regime. So §3 still scopes a real yield-and-reheal *thixotropic* physics; what does **not** survive is a substrate-intrinsic bulk *rectifier*.
>
> **(2) The §3 / Class-3 boundary is empirically grounded — the bulk channel is on the MEMORYLESS side.** The in-regime closure is the thixotropy bulk derivation (branch `analysis/2026-06-09-thixotropy-bulk-derivation`, tip `5969bda1`, **UNMERGED — cited by branch + commit + date, not a HEAD path**), verdict **OUTCOME B by derivation**: the near-saturation bulk relaxation time $\tau_{\text{bulk}}(\bar\rho) = \tau_0/\sqrt{1 + \bar\rho/(1-\bar\rho^2)}$ is a function of the **instantaneous $\bar\rho$ only — no $\operatorname{sign}(d\bar\rho/dt)$ memory** — so the bulk sat/desat channel has **no rate-asymmetry** and cannot rectify a symmetric cyclic drive (over a closed cycle the only nonzero integral is directionless scalar heat; net directed $\oint = 0$). The compression-vs-cavitation asymmetry is real but is a **magnitude** asymmetry in $\tau(\bar\rho)$ ($\tau_{\text{desat}}/\tau_{\text{sat}} \approx 5.57$), **not** a loading-vs-unloading path memory.
>
> **(3) Net effect on this index: CONFIRMS, does not contradict.** A thixotropic magnitude asymmetry that is instantaneous-in-$\bar\rho$ is exactly the **headline Level-1 (reversible / memoryless envelope)** case; **any** rectification / latching / path-memory requires the **Level-2 (memristive)** dynamics, which the smooth $\sqrt{1-A^2}$ kernel does not implement on its own. This is the boundary the derivation lands on, consistent with #144's merged regime-rescope. As a routing aid (INVARIANT-S7) this index adds/retires no `clm-`; §3 remains the correct home for the bulk yield-and-reheal physics, now with its rectification-vs-memory boundary **derived** rather than only asserted.

---

## §4 — Defect-freezing / matter-precipitation / ω-freeze (cosmological frozen grain)

**WHEN TO USE**: a cooling / crystallizing substrate, a frozen-in initial condition, defect-density prediction, or the cosmological matter-precipitation lifecycle.

| Leaf | What it covers | Canonical claim |
|---|---|---|
| [`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) §4 (lines 91-103) | **BEMF-driven defect freezing (AVE-native Kibble-Zurek)**: near saturation $L_{\text{eff}} \to \infty$ blocks $dI/dt$ and $d\omega/dt$ so topology cannot unwind during the yield-crossing → freezes. Mechanism for matter precipitation under cooling; predicts **linear** cooling-rate scaling (NOT the K-Z power law), because Axiom 4 is first-order. | clm-n3un96 |
| [`omega-freeze-cosmic-grain-cascade.md`](omega-freeze-cosmic-grain-cascade.md) §2 (lines 42-49) | Cosmic spin $\Omega_{\text{freeze}}$ **locked into the substrate at lattice genesis** as bond over-bracing $u_0^*$ + global chirality direction; survives forever as the cosmological initial condition; sets $\alpha$, $G$, $\mathcal{J}_{\text{cosmic}}$ jointly. | clm-dsb560, clm-a7cbqq |
| [`trampoline-framework.md`](trampoline-framework.md) (lines 97-105, 422) | The freeze-in mechanism in primer form: rotating-frame freeze-in sets $u_0$ + chirality at genesis (97-105); under saturation the local clock slows and **at rupture freezes** (422). | (see leaf) |
| [`op14-cosmic-horizon-profile.md`](../vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md) (lines 24, 57, 68) | The **frozen-horizon vs ongoing-crystallisation** distinction: BH event horizon is a one-shot $A^2 = 1$ frozen saturation lock; the cosmic horizon is maintained near $A^2 = 1$ by latent-heat balance with $\partial_t A^2 \neq 0$ — same profile shape, non-zero time-derivative. | clm-48g5qf |

**Pitfall**: matter precipitation from cooling vacuum is the *cosmological* instance of the §1 back-EMF freeze ([`dark-wake-bemf-foc-synthesis.md`](dark-wake-bemf-foc-synthesis.md) §1.2) — same mechanism, cosmic scale. Do not import a Kibble-Zurek power-law; the AVE prediction is linear in cooling rate.

---

## §5 — Hysteresis loops in saturation (the reversible-envelope-vs-dynamic-latching scoping)

**WHEN TO USE**: distinguishing reversible reactive cycling from genuine dissipative/latching history; classifying a system's time-pattern through saturation; non-volatile stored-state memory.

| Leaf | What it covers | Canonical claim |
|---|---|---|
| [`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) §3 (lines 66-90) | **The headline scoping itself**: Level 1 (Axiom-4 alone, algebraically symmetric, reversible) vs Level 2 (Axiom 4 + Axiom 1 + Axiom 3, dynamic, memristive) — the loop $\oint S\, dr$ appears only at Level 2. | clm-n3un96 |
| [`nonlinear-vacuum-capacitance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) §"Vacuum Memristor" (lines 51-61) | The **pinched hysteresis loop**: memristance $M(q) = d\Phi/dq$; the $V$–$I$ Lissajous passes through the origin but encloses finite area $\propto$ energy dissipated per thixotropic yield–heal cycle. The textbook memristor signature. | clm-8nkvwy |
| [`temporal-saturation-regime-classifier.md`](temporal-saturation-regime-classifier.md) | The **temporal trichotomy** — Lossless (reversible, $\delta_{\text{AVE}} \to 0$) / Cyclic / Lossy (irreversible, $\delta_{\text{AVE}} \to 1$) — via the substrate-native loss tangent $\delta_{\text{AVE}} = t_{\text{sat}}/t_{\text{period}}$. The classifier that separates reversible reactive cycling from dynamic-latching loss across 21 OOM. | clm-f0jwtk |
| [`appendix-vca-symbols.md`](appendix-vca-symbols.md) (line 39) | **Sine-Gordon kink trap = non-volatile memory** (Flash/NAND analog): $\phi(x) = 4\arctan(e^{\gamma(x-vt)})$ — a substrate-native stored-state memory primitive (integer topological charge held against the reversible envelope). Energy $U_{\text{kink}}$ at [`appendix-derived-numerology.md`](appendix-derived-numerology.md) (line 34). | (see leaf) |

> **🔴 Fork-OPEN context (dated, 2026-07-20; ratified-by-merge #735 + #744; KEEP-BOTH — the memristive-loop rows above (§5 line 126 "energy dissipated per cycle", §3 line 90 "genuinely dissipative, Level-2 memristive", §2 line 73 memristor crossover) are preserved verbatim).** The **DISSIPATIVE reading** of the pinched-hysteresis loop ("finite $\oint$ = energy dissipated per cycle") is **FORK-GATED, not settled**:
> - **#735 (merged):** the $(r,S)$-plane loop-area window test is **zero-information** — the peak is pinned at $\omega\tau \approx 1.0014$ across the whole drive family (a theorem of any first-order kernel), so it cannot adjudicate the fork.
> - **#744 (merged):** the one testable $(V,I)$-plane datum ($\omega\tau = 0.911$) is **THREE-WAY DEGENERATE** — Debye (shipped Eq 2.1), reactive, AND transductive forms all land in-window (`forms_in_window_count = 3`); the F-B2 no-origin-pinch caveat applies at the near-yield operating point. The discriminating power is the **shape-class axes** (Debye peak-pinned + phase caps 90° vs Resonant peak-tracks-$\omega_S$ + phase sweeps 180°), not the peak location.
> - **Crux = `#59` Flag F** (`research/2026-07-19_flag-f-s-dynamics-derivation.md` §0, ratified #744): whether the near-yield $S$-dynamics are first-order-overdamped **dissipative** or second-order-reactive **lossless** is **PARTIALLY discharged** — Eq 2.1 unlicensed at $\omega\tau\sim1$; isolated node reactive; resistor excluded — with the **(a)/(b) fork STAYS OPEN pending the z=3 bath spectral density $J(\omega)$**. Grant leans reversible-reactive; do NOT bank the loop as settled-dissipative.

**Framing discipline** (per `consistency-vs-emergence` light + `ave-evidence-framing-discipline`): the reversible-vs-hysteretic distinction is the **existing canonical Level-1-vs-Level-2 scoping** of [`tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md), not a new claim of this index. The smooth Axiom-4 kernel $S(A) = \sqrt{1 - A^2}$ (canonical: INVARIANT-S2 in [`../CLAUDE.md`](../CLAUDE.md); 26-instance catalog in [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md)) is unchanged; the memory physics is the dynamics *of* that kernel, not a modification of it.

---

## §5b — Genesis v10 discipline: LOOP GAP vs $\Omega_{\text{freeze}}$ (2026-06-11)

**WHEN TO USE:** adjudicating whether a genesis/kernel change "closes the LOOP GAP" or only adds a different memory class. The nine-architecture record diagnosed **remanence = mass** (zero-drive persistence) as the missing constitutive piece; v10 adds $\sigma$ + rate-gated snap + $\Omega_{\text{freeze}}$ IC. These are **not the same mechanism**.

| Mechanism | What it stores | Level | Canon / engine status |
|---|---|---|---|
| $S_{\text{eq}}(A)=\sqrt{1-A^2}$ | Reversible sub-yield envelope | Level 1 (memoryless) | Canon kernel; zero loop area (`06_spice_verification_manual.tex:127-133`) |
| $\tau_{\text{relax}}$ ODE lag | Dynamic-crossing hysteresis loop $\oint S\,dr$ | Level 2 (memristive) | Derived in `tau-relax-derivation.md` §3; SPICE memristor **placeholder** (below any timestep) |
| $\Omega_{\text{freeze}}$ IC | Frozen cosmic spin / phase at $t=0$ | Initial-data memory | v10 kernel + ablation arm; **not** a B–H remanence loop |
| $\sigma$ + rate-gated snap | Dynamic crossing / latching at rupture | Level 2 candidate | v10 kernel (Decision 2); tests mass **retention**, not ferrite remanence |
| Ferrite B–H loop (R2 bench) | $B_r$ at $H=0$ = remanence analogue | EE consistency bench | `2026-06-12_constitutive-loop-r2-prereg_FROZEN.md`; **bench not run** |

**The LOOP GAP remains open until a mechanism supplies zero-drive persistence with nonzero enclosed loop area** — either (a) the v10 snap verdict shows retention without drive, and/or (b) the R2 ferrite B–H bench maps remanence/coercivity/loop-area to mass/annihilation/latent-heat. $\Omega_{\text{freeze}}$ alone is **initial-condition** memory (ablatable); it does not replace thixotropic/ferrite **constitutive** hysteresis.

**v10 production read (2026-06-12; `research/2026-06-12_genesis-v10-cvr-convergence_result.md`):** snap+IC machinery executes; partial CVR-SET on 2/4 srs cells; **snap-OFF and Ω-free ablations still CVR-SET** at matched retention — snap is **not** bin-isolating; **LOOP GAP unchanged** (no zero-drive remanence demonstrated).

**v11 charter (2026-06-12):** prereg DRAFT `research/2026-06-12_genesis-v11-loop-closure_prereg_DRAFT.md` — primary falsifier **P11 zero-drive persistence** via ported $\tau_{\mathrm{relax}}$ ODE on discrete srs; orchestration `_orchestration/2026-06-12_loop-gap-v11-charter.md`.

> ↗ See also: [`loop-gap-electron-resonator-closure-doctrine.md`](loop-gap-electron-resonator-closure-doctrine.md); [`2026-06-11_chiral-vacuum-reactor-framing.md`](../../../research/2026-06-11_chiral-vacuum-reactor-framing.md) §5 v10 charter (Grant decisions D2/D5); vocab audit §4(c2) LOOP GAP diagnosis.

---

## §6 — Cross-references

- **LOOP GAP closure doctrine (2026-06-12):** [`loop-gap-electron-resonator-closure-doctrine.md`](loop-gap-electron-resonator-closure-doctrine.md) — plumber closure order, channel routing, fool modes, v11 direction; full audit in `research/2026-06-12_loop-gap-electron-resonator-synthesis.md`; charter `_orchestration/2026-06-12_loop-gap-v11-charter.md`.
- **Companion indexes**: [`ave-analytical-toolkit-index.md`](ave-analytical-toolkit-index.md) §4 Time-domain (τ_relax, memristive ODE, BEMF, cooling-rate scaling) is the problem-class entry point; this leaf is the memory-physics-specific consolidation under it.
- **Kernel catalog**: [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) — the spatial-instantaneous kernel across 26 scales; the Sine-Gordon kink-memory + sine-Gordon engineered rows are its memory-relevant entries.
- **Temporal companion**: [`temporal-saturation-regime-classifier.md`](temporal-saturation-regime-classifier.md) — the orthogonal temporal axis; the lossless/cyclic/lossy trichotomy is the time-domain partner of this index's reversible/hysteretic axis.
- **Substrate-observability**: [`boundary-observables-m-q-j.md`](boundary-observables-m-q-j.md) — the frozen interior (clock-stopped) vs externally-observable boundary invariants $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ that the §4 freeze produces.

## §7 — Maintenance

This index is a **routing aid** (INVARIANT-S7): it points at canonical leaves and hosts no claims. Discipline:

1. New canonical memory-physics leaf lands → add a row to the appropriate §1-§5 class table here with a grep-verified file:line + the governing `clm-` id.
2. A derivation cycle stalls for want of a memory mechanism (the failure mode that motivated this index) → record it as a worked example of the gap this index closes.
3. A cited leaf's section/line moves → re-grep and update the file:line citation.
4. Optional back-links: the most central leaves (τ_relax derivation, nonlinear-vacuum-capacitance, dark-wake BEMF synthesis, temporal-regime classifier) may carry a `> ↗ See also:` pointer back to this index — added at orchestration/PR time, not by this leaf.
