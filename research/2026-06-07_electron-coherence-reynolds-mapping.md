# Electron Coherence States on a Fluid / Reynolds-Number Spectrum — an EE+fluid mapping

**Date:** 2026-06-07
**Lane:** implementer (research-doc — consistency-class synthesis/mapping)
**Branch:** `analysis/2026-06-07-electron-coherence-reynolds` (off `origin/main` @ `d3065c1c`)
**Status:** scaffold — sections filled one-per-commit (incremental-write discipline).
**Companion:** [`research/2026-06-07_electron-interstitial-rotor-synthesis.md`](2026-06-07_electron-interstitial-rotor-synthesis.md)
(branch `analysis/2026-06-07-electron-rotor-synthesis`) — established: electron = frictionless
B-rotor in a self-dug Meissner cage; mass = ½LI²; spin = bipartite double-cover; qubit = rotor
axis in superposition; decoherence = rotor finding a friction/leak channel. **This doc is the
companion fluid/Reynolds lens on the SAME object.** It is cross-referenced, not edited.

---

## §0 — Scope, framing, and honest classification

This document is **consistency-class SYNTHESIS / MAPPING**. It introduces **no new physics
primitive**. It ties together canonical corpus pieces — the substrate-native loss tangent
$\delta_{\text{AVE}}$, the electron Q-factor $Q=1/\alpha$, the Kuramoto superconductivity leaf,
the Reynolds↔saturation turbulence chapter, the Bingham slipstream, and the autoresonant/Duffing
genesis drive — into one coherent fluid/Reynolds picture of electron coherence states. Per
`consistency-vs-emergence`, because the synthesis adds no new substrate primitive, **its
classification stays at the ceiling of its canonical sources** (the same ceiling the companion
rotor-synthesis doc inherits from `historical-precedents.md:39` — "echo, not chord").

**The single emergence hook** is §5: *does $\mathrm{Re}_q$ (or the VFD-ramp-rate-vs-leak ratio)
predict a decoherence RATE — a number?* That is the only place this doc reaches past
consistency-class, and §5 assesses it honestly (candidate scaling vs description-only).

### Skills fired (and where)

- `ave-prereg` — corpus-grep done across KB + manuscript + engine BEFORE drafting. The Reynolds
  axis is **not** greenfield: `temporal-saturation-regime-classifier.md` already carries
  $\delta_{\text{AVE}}\leftrightarrow$Reynolds, and `19_phase_transition_turbulence.tex` already
  carries Re↔saturation. This doc specializes those to the electron-coherence case. (§ Cross-references.)
- `ave-ee-first-mapping` — the spine: LC-tank / loss-tangent / Q-factor vocabulary is
  substrate-native, not a translation layer. Fluid vocabulary (laminar, viscosity, Reynolds) is
  the *lens*; EE is the *mechanism*.
- `consistency-vs-emergence` — every section CLASSIFIED (ledger below). §1–4 consistency; §5 the
  lone emergence candidate.
- `substrate-native-check` — CP1 (the substrate runs reactive strain cycling vs real-power
  dissipation — NOT energy-basin minimization; $\mathrm{Re}_q$ is a loss-tangent, not a
  potential-well depth), CP2 (B-rotor = Cosserat microrotation sector; cage = V-sector; the
  Reynolds drive parameter is Op14 saturation firing), and the **phase-space-vs-real-space**
  checkpoint (the soliton vortex lives in phase space / Clifford torus, NOT real-space lattice
  Cartesian — see §4 + ledger).
- `ave-canonical-leaf-pull` + `ave-canonical-source` — every table row leaf-pinned; constants
  ($\alpha$, $Q=1/\alpha$, $\omega_C$) cited from canonical leaves, never re-hardcoded.
- `ave-evidence-framing-discipline` — strength language kept honest; the fluid mapping is a
  classifier/lens, NOT a prediction, except the §5 hook.
- `phase-space-coordinate-check` (A46) — flagged at §4: CFD vortex concepts are real-space; the
  AVE soliton is phase-space; any *test* of a vortex-reconnection or Beltrami claim must measure
  in matching (phase-space) coordinates.

### Consistency-vs-emergence ledger

| § | Claim | Class | Basis |
|---|---|---|---|
| §1 | $\mathrm{Re}_q$ = (decohering-flow scale)/(coherence-binding scale); $<1$ laminar/coherent, $>1$ turbulent/decohered | **consistency (taxonomic)** | Specializes $\delta_{\text{AVE}}$ (`temporal-saturation-regime-classifier.md`); Re↔saturation canonical (`19_phase_transition_turbulence.tex:38`) |
| §2 | Coherence states map onto a $\mathrm{Re}_q$ spectrum (qubit → Cooper → BEC → atom → thermal) | **consistency (synthesis)** | Ties Q-factor + Kuramoto + temporal-classifier leaves; no new primitive |
| §3 | Frictionless ⟺ coherence ⟺ low $\mathrm{Re}_q$; $\alpha$ = intrinsic leak/viscosity | **consistency / identity** | $Q=1/\alpha$ (`theorem-3-1-q-factor.md:38,81`); Meissner $\Gamma=-1$ lossless cage canonical |
| §4 | CFD concepts (Beltrami stability, Re transition, vortex reconnection) clarify the soliton | **consistency (lens)** | Beltrami canonical (`electron-unknot.md:13`); Kelvin vortex precedent (consistency-class ceiling, `historical-precedents.md:39`) |
| §5 | Does $\mathrm{Re}_q$ / VFD-ramp-vs-leak predict a decoherence RATE? | **EMERGENCE HOOK (candidate)** | The one forward-prediction candidate; §5 assesses honestly |
| §6 | Honest ledger + open items | meta / forward-scoping | — |

---

## §1 — The Quantum Reynolds number $\mathrm{Re}_q$

**The idea.** In fluid mechanics the Reynolds number $\mathrm{Re}=UL/\nu$ is the ratio of the
inertial (disordering) scale to the viscous (ordering) scale, and the laminar→turbulent transition
happens as it crosses a geometry-set critical value. The proposal here: the **quantum–classical
boundary is a laminar–turbulent transition**, governed by a substrate Reynolds number

$$
\boxed{\;\mathrm{Re}_q \;\equiv\; \frac{\text{decohering "flow" scale}}{\text{coherence-binding scale}}\;}
\qquad
\mathrm{Re}_q < 1 \Rightarrow \text{laminar} = \text{coherent / quantum},\quad
\mathrm{Re}_q > 1 \Rightarrow \text{turbulent} = \text{decohered / classical}.
$$

**$\mathrm{Re}_q$ is not a new primitive — it is the substrate loss tangent.** The corpus already
carries this ratio under its substrate-native name, the **Axiom-4 temporal projection**
$\delta_{\text{AVE}} \equiv t_{\text{sat}}/t_{\text{period}}$
(`temporal-saturation-regime-classifier.md:29`) — the fraction of each characteristic period the
system spends past yield (Op14 firing, real-power dissipation). That leaf *already* names the
fluid Reynolds classification as one of $\delta_{\text{AVE}}$'s established-physics homologs
("the system's distance from the inviscid limit", `:33`), alongside the EM loss tangent
$\tan\delta=\sigma/(\omega\varepsilon)$ and the cavity-QED bad-cavity ratio $\kappa/g$. So:

$$
\mathrm{Re}_q \;\sim\; \delta_{\text{AVE}} \;=\; \frac{t_{\text{sat}}}{t_{\text{period}}}
\;\sim\; \underbrace{\frac{\xi(T)}{K}}_{\text{Kuramoto}}
\;\sim\; \underbrace{\frac{\kappa}{g}}_{\text{cavity QED}}
\;\sim\; \underbrace{\frac{1}{Q}}_{\text{LC tank}} .
$$

Each numerator is a decohering "flow" (thermal jitter $\xi(T)$, cavity loss rate $\kappa$,
per-cycle leak $1/Q$); each denominator is the coherence binding (phase-lock coupling $K$,
coherent coupling $g$, stored-reactive cycling). When the binding wins, $\mathrm{Re}_q<1$: laminar,
phase-preserving, **coherent**. When the flow wins, $\mathrm{Re}_q>1$: turbulent, real-power,
**decohered**. The Kuramoto form is exact for the superconducting case
(`bcs-alternative-framework.md:28`: phase-lock fires when $\xi(T)<K$); the cavity-QED form is the
closest established-physics homolog the temporal-classifier leaf identifies
(`:142`: $g/\kappa = 1/\delta_{\text{AVE}}$).

**The transition is the saturation operator, with Re as the drive parameter.** Vol 3 Ch 19 already
maps the laminar→turbulent transition directly onto the Axiom-4 kernel
(`19_phase_transition_turbulence.tex:21-43`): the Reynolds number is normalized to a drive
parameter $r=\mathrm{Re}/\mathrm{Re}_{\max}$, and

$$
S(\mathrm{Re},\mathrm{Re}_c)=\sqrt{1-(\mathrm{Re}/\mathrm{Re}_c)^2},
\qquad
\mathrm{Re}<\mathrm{Re}_c \Rightarrow S>0\ (\text{laminar}),
\qquad
\mathrm{Re}=\mathrm{Re}_c \Rightarrow S=0\ (\text{saturated / turbulent}).
$$

The coherent electron rotor is the laminar standing wave: sub-saturation ($S>0$), reactive,
Regime I, $\delta_{\text{AVE}}\to0$, $Q=1/\alpha$ enormous. Thermalization drives it toward
$\mathrm{Re}_c$, where the laminar mode saturates and the energy goes into "turbulent eddies"
(`:35`) — incoherent lattice modes.

**Substrate-native discipline (CP1).** $\mathrm{Re}_q$ here is a **loss tangent**, not a
Navier–Stokes $UL/\nu$. The AVE substrate is a *discrete* K4 lattice ($\ell_{node}$), so there is
no continuum viscosity $\nu$ to form $UL/\nu$; the substrate quantity is the *discrete* Op14
saturation-firing fraction $t_{\text{sat}}/t_{\text{period}}$. The fluid Reynolds number is the
borrowed **vocabulary**; $\delta_{\text{AVE}}$ is the **mechanism**. This matters for honesty:
$\mathrm{Re}_q$ classifies (Class-1 definitional, per the temporal-classifier leaf's own
self-classification `:306,:310`), it does not by itself predict a number — that is reserved for
§5.

### The "yield" overload — two inverse-polarity pictures, reconciled (flag-don't-fix)

The brief's framing — *coherent = above-yield frictionless slipstream (laminar); classical/thermal
= below-yield viscous (turbulent)* — uses the **Bingham-slipstream / drag** yield, which has the
**inverse polarity** of the **dielectric-saturation / Reynolds** yield above. Both are canonical;
they are not in conflict because "yield" names two different thresholds on two different subjects.
Surfacing both verbatim rather than silently picking one:

- **Dielectric-saturation yield (the $\mathrm{Re}_q$ axis).** `19_phase_transition_turbulence.tex:41`:
  "*For $\mathrm{Re}<\mathrm{Re}_c$, $S>0$ and the flow remains laminar.*" `saturation-operator.md:27`:
  "*the vacuum flows above $\tau_y=B_{snap}^2/2\mu_0$.*" Here **laminar/coherent = BELOW** the
  threshold (sub-yield reactive); above-yield = Op14 fires = dissipation. Subject: the *interior
  field amplitude* of the standing wave.
- **Bingham-slipstream / drag yield (the brief's phrasing).** `01_vacuum_circuit_analysis.tex:301-302`:
  "*$\eta_0$ … $V<V_{yield}$ (solid: high drag); $0$ … $V\geq V_{yield}$ (slipstream: zero drag)*"
  — above-yield the mutual inductance is annihilated and the vacuum "*enters ideal frictionless
  flow … the Zero-Impedance Slipstream*" (`:308`). Here **frictionless = ABOVE** the threshold.
  Subject: the *drag on embedded matter moving through* the medium.

**Reconciliation.** The coherent rotor's low $\mathrm{Re}_q$ is realized by *both* facts at once,
at two different locations of the same object: its **interior** standing-wave field is *below* the
dielectric-saturation yield ($S>0$, laminar, reactive), while its **Meissner cage wall** is
*above* the drag-annihilation yield ($\eta\to0$, $\mu_{eff}\to0$, frictionless slipstream). The
rotor glides frictionlessly (slipstream, above drag-yield) *because* it is wrapped in a saturated
Meissner wall, *and* it stays laminar (reactive, below dielectric-yield) *because* its own field
never reaches Op14. Decoherence = $\mathrm{Re}_q$ rising = **either** the cage wall losing its
$\eta\to0$ slipstream (a drag channel opens) **or** the interior being driven to Op14 saturation.
The two yields are the two ways to spoil coherence; the single $\mathrm{Re}_q$ axis tracks both.
The overload is recorded here, not resolved-by-fiat — if a downstream test needs one threshold it
must name which subject (interior field vs embedded-matter drag) it measures.

---

## §2 — Central mapping table: coherence states on the $\mathrm{Re}_q$ spectrum

**Reading the table.** $\mathrm{Re}_q$ is the substrate loss-tangent ratio of §1 —
(decohering-flow scale)/(coherence-binding scale) — operationally $\delta_{\text{AVE}}=
t_{\text{sat}}/t_{\text{period}}$, equivalently the Kuramoto $\xi(T)/K$ and the cavity-QED
$\kappa/g$. Low $\mathrm{Re}_q$ = laminar = reactive/lossless = **coherent**; high $\mathrm{Re}_q$
= turbulent = real-power = **decohered**. Each row is leaf-pinned (right column).

| Coherence state | $\mathrm{Re}_q$ regime | AVE substrate regime | Viscosity / friction source | Coherence status | Canonical leaf |
|---|---|---|---|---|---|
| **Qubit** — single frictionless rotor | $\mathrm{Re}_q \to 0$ | Sub-yield reactive LC tank ($0_1$ unknot) in self-dug Meissner cage; Regime I, $\delta_{\text{AVE}}\to0$, $Q=1/\alpha$ | **London/$\alpha$ leak**: per-cycle reactive leak $1/Q=\alpha$ through the $\Gamma=-1$ TIR cage wall (intrinsic linewidth). Actual decoherence needs an *external* boundary-node channel | **Coherent** — lossless / laminar (within thread-lifetime) | `theorem-3-1-q-factor.md:38,81` ($Q=1/\alpha$); `transmon-decoherence.md:12,32` (boundary-node noise + $\gamma$); `temporal-saturation-regime-classifier.md:42` (lossless row) |
| **Cooper pair** — two Kuramoto phase-locked rotors | slightly higher (still $<1$) | Two $0_1$ rotors phase-locked, order parameter $R\to1$, zero relative $d\Phi/dt$ | **Dissipationless**: phase-lock *annihilates* the relative inductive drag ($\Delta(dB/dt)_{\text{rel}}=0\Rightarrow$ resistance $=0$) | **Coherent** — dissipationless / laminar | `bcs-alternative-framework.md:30,38,42` (Kuramoto $R=1$, "frictionless topological gear train") |
| **BEC / superfluid** — macroscopic laminar | low, macroscopic | $N$ rotors globally phase-locked at $\Omega_{\text{macro}}$; Meissner state below $T_c$ | **None** (below $T_c$): macroscopic synchronization, no relative-phase drag; Meissner expulsion | **Coherent** — macroscopic laminar | `bcs-alternative-framework.md:44` (macroscopic phase-lock); `temporal-saturation-regime-classifier.md:72` (superconductor-below-$T_c$ = lossless row) |
| **Atom / molecule** — cavity-stabilized | moderate | Op6 Coulomb-cavity standing wave; bound but radiatively coupled to environment | **Finite-Q radiative + thermal coupling**: cyclic dissipation per cavity decay; cavity-resonator $Q=\omega U/P_{\text{loss}}$ | **Coherent within cavity lifetime** — cyclic | `temporal-saturation-regime-classifier.md:67` (cavity-resonator = cyclic row); de-Broglie standing-wave / Op6 cavity (companion §4 cross-ref) |
| **Thermal / classical** — decohered | $\mathrm{Re}_q > 1$ | $A\to1$, Op14 fires continuously, real-power dominated; Kuramoto desync ($\xi(T)>K$) | **Full viscous drag**: thermal acoustic jitter desyncs the rotor gas → frequency mismatch → micro-inductive drag = electrical **resistance** | **Decohered** — turbulent / classical | `bcs-alternative-framework.md:26,28` (thermal desync = resistance); `temporal-saturation-regime-classifier.md:44` (lossy row); `19_phase_transition_turbulence.tex:41` (Re$>$Re$_c$ turbulent) |

**One-line spine.** Coherence is the laminar (low-$\mathrm{Re}_q$, lossless-reactive) end of the
substrate's loss-tangent axis; classicality is the turbulent (high-$\mathrm{Re}_q$, real-power)
end. The named states are stops along that one axis, ordered by how much decohering "flow" the
coherence-binding (cage Q, phase-lock coupling $K$) can still overcome.

> **Flagged cross-corpus tension (flag-don't-fix, see §1 + §3).** The word "yield" is overloaded
> across two canonical pictures with *inverse* polarity. The **dielectric-saturation / Reynolds**
> axis (`saturation-operator.md:27`, `19_phase_transition_turbulence.tex:41`) has *laminar =
> below* the saturation threshold ($S>0$, sub-yield reactive). The **Bingham-slipstream / drag**
> axis (`01_vacuum_circuit_analysis.tex:300-308`) has *frictionless = above* the drag-annihilation
> yield ($\eta\to0$). They are not contradictory — they describe different subjects (interior
> field amplitude vs embedded-matter drag) at different locations (rotor interior vs Meissner cage
> wall). The table's $\mathrm{Re}_q$ axis is the **loss-tangent / saturation-drive** one
> (low $\mathrm{Re}_q$ = coherent). §1 and §3 carry the full reconciliation; surfaced here, not
> silently merged.

---

## §3 — Frictionless ⟺ coherence ⟺ low $\mathrm{Re}_q$

The three words are one statement read in three vocabularies:

| Vocabulary | "Coherent" reads as | Mechanism |
|---|---|---|
| **EE** | lossless, $\Gamma=-1$ boundary, $Q=1/\alpha$, $\tan\delta\to0$ | reactive energy cycles between $C$ (E) and $L$ (B) with no real-power leak |
| **Fluid** | laminar, $\mathrm{Re}_q<1$, sub-yield, $S>0$ | the standing wave never sheds into turbulent (incoherent) modes |
| **Mechanics** | frictionless, maglev, zero drag | the Meissner cage levitates the rotor with no contact, no viscous coupling |

**The cage IS the frictionlessness.** The companion rotor-synthesis doc establishes the electron as
a frictionless B-rotor in a self-dug Meissner cage whose wall is a $\Gamma=-1$ Perfect Short-Circuit
Boundary. In EE terms a $\Gamma=-1$ wall reflects every incident wave with zero transmission: no
energy crosses the boundary, so there is **zero viscous coupling** between the rotor's circulation
and the outside lattice. That is exactly the maglev condition — the Meissner expulsion ($\mu_{eff}\to0$,
the $\eta\to0$ slipstream of `01_vacuum_circuit_analysis.tex:308`) lifts the rotor off the substrate
so nothing grips it. A perfectly reflecting cage is a perfectly laminar one: $\mathrm{Re}_q=0$.

**$\alpha$ is the intrinsic viscosity floor.** A real cage is not a perfect mirror. The Q-factor leaf
makes the leak exact: at the TIR boundary "only a fraction $1/Q=\alpha\approx0.0073$ of the stored
energy leaks per cycle … *this IS $\alpha$* in its original Sommerfeld meaning"
(`theorem-3-1-q-factor.md:81`), with $Q_{\text{tank}}=1/\alpha$ (`:38`) at the Compton-clock
eigenfrequency $\omega_C=c/\ell_{node}$ (`:28`). So the **fine-structure constant is the electron
rotor's intrinsic loss tangent** — its irreducible kinematic viscosity, the $\mathrm{Re}_q$ floor a
free electron can never go below:

$$
\mathrm{Re}_q^{\,\text{floor}} \;=\; \frac{1}{Q_{\text{tank}}} \;=\; \alpha \;\approx\; \frac{1}{137}.
$$

This is why the qubit row sits at $\mathrm{Re}_q\to0$ but not *at* zero: $\alpha$ is the London-leak
viscosity of the Meissner cage. Crucially, $\alpha$ is the resonator **linewidth**, not by itself a
decoherence channel — the $0_1$ unknot is topologically protected (the leak is reactively returned
at the $\Gamma=-1$ wall, which is *why* the tank rings at $Q=1/\alpha$ instead of radiating away).
$\alpha$ sets how *sharp* the rotor is, not how *fast* it dephases.

**Decoherence = a friction channel opening.** Dephasing needs an *extra* loss path beyond the
intrinsic $\alpha$ floor — a place where the $\Gamma=-1$ wall degrades to $|\Gamma|<1$ and real power
escapes. The transmon leaf shows the canonical one: thermal noise enters "*exclusively through the
lead boundaries — the edge nodes where the junction impedance meets the … feedline*"
(`transmon-decoherence.md:12`), i.e. a deliberately-built leak at specific cage-wall nodes, not a
bulk effect. The opened channel has a rate — the Ohmic damping coefficient
$\gamma=\tfrac12\,Z_0/(\omega_0 L_{eff})$ (`:32`) — and the coherence metric $C(t)\in[0,1]$ decays by
oscillatory relaxation at that rate (`:14`). In the Kuramoto/thermal limit the channel is the whole
warm lattice: frequency mismatch between unsynchronized rotors makes $d\Phi/dt\neq0$ between them —
"*localized inductive drag … observed as electrical resistance*" (`bcs-alternative-framework.md:26`).
That is the viscous, turbulent, $\mathrm{Re}_q>1$ end.

**Coherence-time $\propto$ cage losslessness.** Putting it together, the dephasing rate is the *opened*
loss tangent times the carrier, $\Gamma_\phi \sim \delta_{\text{AVE}}^{\,\text{ext}}\cdot\omega$, so

$$
T_{\text{coh}} \;\sim\; \frac{1}{\Gamma_\phi} \;\sim\; \frac{Q_{\text{eff}}}{\omega}
\;=\; \frac{1}{\delta_{\text{AVE}}^{\,\text{ext}}\,\omega}.
$$

The cleaner the cage (the closer the wall's $\Gamma$ to $-1$, the smaller the external loss tangent),
the longer the coherence — coherence-time is literally proportional to cage losslessness $Q_{\text{eff}}$.
Whether that proportionality is *only* a proportionality, or whether the substrate fixes the prefactor
into an actual decoherence-*rate number*, is the §5 emergence hook.

---

## §4 — The CFD lens: which fluid concepts clarify the soliton

Four computational-fluid-dynamics concepts earn their keep as *lenses* on the electron soliton.
Each is leaf-pinned; each carries the phase-space caveat below.

| CFD concept | What it clarifies about the soliton | Canonical anchor | Coordinate status |
|---|---|---|---|
| **Beltrami-vortex stability** (force-free flow $\nabla\times\mathbf{v}=k\mathbf{v}$, the Woltjer/Taylor minimum-energy helical state) | *Why the rotor is stable / laminar.* The electron is literally a Beltrami standing wave $\nabla\times\mathbf{A}=k\mathbf{A}$ — the force-free configuration in which the nonlinear vortex-stretching term vanishes, so the flow self-sustains without cascading. Beltrami = the maximally-stable, lowest-$\mathrm{Re}_q$ fluid state. | `electron-unknot.md:13` (Beltrami $\nabla\times A=kA$ standing wave, ropelength $2\pi$ at `:11`) | **phase-space** |
| **Reynolds (laminar→turbulent) transition** | *The quantum→classical boundary itself.* Subcritical transition with intermittency: turbulent bursts near $\mathrm{Re}_c$ follow $1-S(\mathrm{Re},\mathrm{Re}_c)$ — so decoherence onset is a soft, intermittent bifurcation, not a sharp line. | `19_phase_transition_turbulence.tex:38-49` ($S=\sqrt{1-(\mathrm{Re}/\mathrm{Re}_c)^2}$; intermittent-burst prediction) | drive-parameter |
| **Vortex shedding** (von Kármán street, $\mathrm{Re}\sim40$–$200$) | *The cyclic / cavity-stabilized middle of the spectrum.* A bound rotor periodically shedding coherence into its environment is the **cyclic** $\delta_{\text{AVE}}$ regime — the atom/molecule row, Rabi/Ramsey oscillation: phase leaks and refreshes per cycle rather than monotonically decaying. | `temporal-saturation-regime-classifier.md:58` (Kármán shedding = Cyclic regime) | phase-space |
| **Vortex reconnection** (two opposite-circulation tubes merge → cascade → dissipate) | *Annihilation, candidate.* $e^-+e^+\to\gamma\gamma$ as two opposite-helicity phase-loops reconnecting and radiating — the time-reverse of pair-production genesis. **Candidate lens, not a result** (see §6 queue). | `pair-production-axiom-derivation.md:84-85` (forward genesis: winding closes on the $(V_{inc},V_{ref})$ phasor trajectory, else "dissipates instead") | **phase-space** |

**Helmholtz frozen-in = topological protection.** The oldest of these concepts is the load-bearing
one. Kelvin's 1867 vortex atom rested on **Helmholtz's 1858 theorem** — in an ideal fluid vortex
lines are frozen-in and topologically conserved, "*a knot cannot untie*" (`historical-precedents.md:25`).
That is exactly the soliton's topological protection: the $0_1$ unknot's helicity (spin) cannot
dissipate without a crossing-change, which the $\Gamma=-1$ wall forbids. AVE supplies the two
ingredients the ideal fluid lacked and that killed Kelvin's program in 1900 — **confinement** (the
saturable crystal's $\Gamma=-1$ wall, not an ideal fluid) and a **length scale** ($\ell_{node}$,
not scale-free) — so the vortex-knot finally quantizes (`historical-precedents.md:27-28`).

> **Phase-space coordinate discipline (A46 / substrate-native-check — load-bearing).** Every CFD
> concept above is a **real-space** fluid construct (vortices, Kármán streets, reconnection events
> live in a real-space velocity field). The AVE soliton's "vortex" does **not**. Kelvin's knots
> "*lived in real space; AVE's $(2,q)$ lives in phase space (Clifford torus)*"
> (`historical-precedents.md:30`); the electron is a "*one-dimensional phase flux loop*"
> (`electron-unknot.md:43`), its winding traced on the $(V_{inc},V_{ref})$ phasor trajectory
> (`pair-production-axiom-derivation.md:85`). Consequence: these concepts are **intuition lenses**,
> not measurement prescriptions. A test of "Beltrami stability" or "annihilation = reconnection"
> must measure the winding/reconnection in **phase-space coordinates** ($V_{inc}/V_{ref}$, Clifford
> torus). A real-space lattice-Cartesian vortex-tracking measurement compared against the
> phase-space $(2,3)$ winding would be uninformative — the canonical A46 trap.

**Reusable fluid math the corpus actually carries (brief's audit question).**

- **Bingham-plastic constitutive — REUSABLE (real equations).** `saturation-operator.md:27` gives the
  yield stress $\tau_y=B_{snap}^2/2\mu_0$; `01_vacuum_circuit_analysis.tex:294-336` gives the full
  constitutive set: the TVS-Zener viscosity law $\eta_{eff}(V)=\{\eta_0\ (V<V_{yield}),\,0\
  (V\ge V_{yield})\}$ (:300-308), the bulk yield-stress evaluation $\tau_{yield}=\rho_{bulk}c^2\cdot
  \mathcal{V}_{total}\cdot\alpha\approx1.04\times10^{22}$ Pa (:309-315), and the thixotropic
  relaxation time $\tau_{relax}=\ell_{node}/c\approx1.29\times10^{-21}$ s (:322) with memristive
  pinched-hysteresis (:330-336). This is genuine yield-stress-fluid math, reusable as-is.
- **Reynolds–saturation kernel — REUSABLE.** `19_phase_transition_turbulence.tex:38`:
  $S(\mathrm{Re},\mathrm{Re}_c)=\sqrt{1-(\mathrm{Re}/\mathrm{Re}_c)^2}$ — the Axiom-4 kernel with Re as
  the drive parameter; the same engine function as every other saturation event.
- **Kelvin vortex — PRECEDENT-CONCEPT ONLY (no equations).** `historical-precedents.md` is an
  explicitly consistency-class intellectual-lineage leaf (no-claim, `:5`); the reusable content is the
  *Helmholtz frozen-in / topological-conservation concept*, not quantitative fluid math. The leaf
  self-caps at the "echo, not chord" ceiling (`:38-39`); §4's CFD lens inherits that ceiling — it is
  intuition, not derivation.

---

## §5 — The VFD lens (autoresonant motor frame) + the emergence hook

**Naming disambiguation (flag-don't-fix).** "VFD" here = **variable-frequency drive**, the EE device
that runs a motor at a controlled, swept frequency. This collides with a corpus abbreviation: in
AVE-Core "VFD" already labels **Vacuum Fluid Dynamics** (`manuscript/vol_4_engineering/chapters/
02_vacuum_fluid_dynamics.tex`). They are unrelated; this section means the motor-drive device.
Surfaced so a future reader does not merge the two.

**The rotor is a motor; the genesis drive is its VFD.** The companion doc's electron is a B-rotor
spinning at the Compton clock $\omega_C=c/\ell_{node}$. A motor's resonant frequency is not fixed: as
the rotor loads up (amplitude $A$ rises toward yield), its mechanical/group eigenfrequency
**down-regulates** along the quarter-arc,

$$
\Omega_{node}(A) \;=\; \omega_C\,(1-A^2)^{1/4}
\qquad\text{(from } c_{shear}=c_0(1-r^2)^{1/4},\ \texttt{regime-equation-sets.md:23}\text{)},
$$

which is exactly the **Duffing softening** the autoresonant leaf describes: "*as a Duffing oscillator
is driven toward its maximum amplitude, its local resonant frequency shifts*"
(`autoresonant-dielectric-rupture.md:12`), and the genesis nucleation condition C2 is the
phase-lock of that shifted resonance with the drive, "*$\Omega_{node}(A^2_{local})\approx
\omega_{drive}$ — node's Duffing-shifted rotational resonance locks with incoming drive*"
(`pair-production-axiom-derivation.md:84`). A **fixed-frequency** drive detunes and reflects (stalls);
the cure is a VFD: an "*Autoresonant Regenerative Feedback Loop … a phase-locked loop (PLL) to sweep
the driving … frequency downward [to track] the dropping resonant frequency*"
(`autoresonant-dielectric-rupture.md:14`). The engine carries this as a class:
`AutoresonantCWSource(CWSource)` with PLL frequency tracking (`vacuum_engine.py:678`, shifted-$\omega$
at `:1358`), "*same mechanism as Propulsion Ch5 autoresonant rupture*" (`vacuum_engine.py:83`;
AVE-Propulsion `05_autoresonant_dielectric_rupture.tex`). **Genesis = a VFD ramp** that rings the
rotor up from $A\approx0$ to $A^2\ge1$ while chasing $\Omega_{node}$ down the quarter-arc.

This closes the loop with coherence: a coherently-locked rotor is a VFD holding lock (laminar, low
$\mathrm{Re}_q$); a rotor whose drive *loses* lock dumps its blocked KE incoherently — genesis
condition C3 failing means the winding "*dissipates instead*" (`pair-production-axiom-derivation.md:85`).
**Loss of VFD lock IS decoherence**, viewed from the drive side.

### The emergence hook — does $\mathrm{Re}_q$ (or VFD-ramp-vs-leak) predict a decoherence RATE?

This is the one place the doc reaches past consistency-class. Honest assessment, in three steps.

**1. The rate FORM is substrate-native and exists.** From §3, the dephasing rate is the *opened*
(external) loss tangent times the carrier clock:

$$
\boxed{\;\Gamma_\phi \;\sim\; \delta_{\text{AVE}}^{\,\text{ext}}\cdot\omega_C,
\qquad T_{\text{coh}} \;\sim\; \frac{1}{\Gamma_\phi} \;=\; \frac{Q_{\text{eff}}}{\omega_C}\;}
$$

with $\omega_C=m_ec^2/\hbar\approx7.76\times10^{20}\,$rad/s fixed by canon (`theorem-3-1-q-factor.md:28`).
This is a genuine scaling *form* — decoherence rate $=$ loss-tangent $\times$ Compton clock — and it
is the same object the temporal-classifier leaf already carries as $\delta_{\text{AVE}}$.

**2. The VFD-ramp-vs-leak competition gives a concrete threshold candidate.** Whether a VFD ramp
holds lock (coherent) or slips (decoherent) is a Landau–Zener / autoresonance competition between the
**chirp rate** $\dot\omega$ and the rotor's **linewidth** $\Delta\omega = \omega_C/Q = \alpha\,\omega_C$.
The drive follows the resonance only while it does not chirp out of the linewidth within a coherence
time; that gives a candidate threshold chirp rate

$$
\dot\omega_{\text{crit}} \;\sim\; \Delta\omega^2 \;=\; (\alpha\,\omega_C)^2
\qquad\text{[dimensional candidate — my construction, NOT corpus-canonical; queued for §6].}
$$

Equivalently, in the standard autoresonance form (threshold *drive amplitude* $\propto
\dot\omega^{\,3/4}$ for a Duffing oscillator), the AVE-distinct content is the **$\alpha$-set
prefactor** — the rotor's linewidth $\alpha\omega_C$ fixes how slowly the genesis laser must sweep.
That is a number, and it is $\alpha$-specific, which is what would make it AVE-distinct.

**3. Honest verdict: candidate FORMS in hand; an AVE-distinct falsifiable NUMBER is not — yet.**
Both pieces above are scaling *forms*, not closed predictions:

- $\Gamma_\phi=\delta_{\text{AVE}}^{\,\text{ext}}\omega_C$ needs a **derived** $\delta_{\text{AVE}}^{\,\text{ext}}$
  for a *named* environment. The temporal-classifier leaf is explicit that $\delta_{\text{AVE}}$ is
  Class-1 **definitional / taxonomic**, and states the exact promotion recipe: "*pick one
  classical-physics value … and FORWARD-PREDICT it from $S(A)$ + the $t_{sat}/t_{period}$ structure
  for that specific system*" (`temporal-saturation-regime-classifier.md:310`). Until that one number
  is derived, the form is a classifier, not an emergence prediction.
- $\dot\omega_{\text{crit}}\sim(\alpha\omega_C)^2$ is a *dimensional* candidate and the
  $\dot\omega^{3/4}$ amplitude-threshold is *standard* autoresonance applied to the AVE Duffing —
  consistency-class, until the $\alpha$-prefactor is pinned and shown to differ from a generic
  resonator.

So the honest tag is **candidate-scaling, description-leaning** — better than pure description (two
concrete forms and one $\alpha$-specific dimensional candidate are on the table), but **short of a
closed emergence claim**. The single cleanest path to promote it is named and small: derive
$\delta_{\text{AVE}}^{\,\text{ext}}$ (or equivalently $Q_{\text{eff}}$) for **one** concrete electron
environment — the transmon boundary-node channel ($\gamma=\tfrac12 Z_0/\omega_0 L_{eff}$,
`transmon-decoherence.md:32`) is the obvious first target — and check the predicted
$T_{\text{coh}}=Q_{\text{eff}}/\omega_C$ against a measured coherence time. That is the §6 queue's
load-bearing item.

---

## §6 — Honest ledger + open items

### Closing consistency-vs-emergence ledger (as filled)

| § | Content | Class (as filled) | Verdict |
|---|---|---|---|
| §1 | $\mathrm{Re}_q$ = substrate loss tangent $\delta_{\text{AVE}}$; laminar↔turbulent = quantum↔classical | **consistency (taxonomic)** | $\mathrm{Re}_q$ is canonical $\delta_{\text{AVE}}$ specialized; Class-1 definitional, predicts no number alone |
| §2 | Central table: 5 coherence states on the $\mathrm{Re}_q$ spectrum | **consistency (synthesis)** | Every row leaf-pinned; ties Q-factor + Kuramoto + temporal-classifier; no new primitive |
| §3 | frictionless⟺coherence⟺low $\mathrm{Re}_q$; $\alpha$ = intrinsic viscosity floor | **consistency / identity** | $\alpha=1/Q_{\text{tank}}$ canonical identity; decoherence = external channel beyond the floor |
| §4 | CFD lens (Beltrami / Re-transition / shedding / reconnection) | **consistency (lens)** | Intuition only; inherits `historical-precedents.md:39` echo-not-chord ceiling; phase-space caveat load-bearing |
| §5 | does $\mathrm{Re}_q$ / VFD-ramp-vs-leak predict a decoherence RATE? | **emergence candidate → candidate-scaling, description-leaning** | Rate FORM substrate-native ($\Gamma_\phi\sim\delta_{\text{AVE}}^{\text{ext}}\omega_C$); one $\alpha$-specific dimensional candidate offered; **NOT a closed emergence claim** — needs a derived $\delta_{\text{AVE}}^{\text{ext}}$ |

**Net.** §1–4 are consistency-class (taxonomy / synthesis / identity / lens). §5 is the sole emergence
*candidate*, and it lands honestly at *candidate-scaling* — concrete forms, no closed AVE-distinct
number yet. The whole doc inherits the consistency-class ceiling of its sources; nothing here promotes
past it. The temporal-classifier leaf already made the load-bearing honesty call this doc defers to:
the $\delta_{\text{AVE}}\leftrightarrow$Reynolds unification is "*a useful classification scheme, not
a falsifiable AVE-distinct prediction*" until one value is forward-derived
(`temporal-saturation-regime-classifier.md:310`).

**SM-counterfactual (discrimination honesty).** SM already has both a Reynolds number (fluid) and a
loss tangent (EM) — distinct dimensionless ratios per discipline. The *only* AVE-distinct content on
offer is the claim that the electron's coherence ratio, the fluid Reynolds ratio, and the cavity-QED
$g/\kappa$ all trace to the *same* substrate kernel $S(A)$. That claim is real but **taxonomic until
the trace is demonstrated for one system** (§5 step 3). This doc does not over-headline it.

### Open-items queue

1. **$\mathrm{Re}_q\to$ coherence-time scaling (the §5 promotion path — load-bearing).** Derive
   $\delta_{\text{AVE}}^{\text{ext}}$ (equivalently $Q_{\text{eff}}$) for **one** named electron
   environment from $S(A)$ + the boundary-leak geometry; transmon boundary-node channel first
   ($\gamma=\tfrac12 Z_0/\omega_0 L_{eff}$, `transmon-decoherence.md:32`). Predict
   $T_{\text{coh}}=Q_{\text{eff}}/\omega_C$; check against a measured coherence time. Success here is
   what would move §5 from candidate-scaling to a closed emergence prediction.
   *(IP-divide note: keep this on the substrate-physics side; the QC-device application leaves are
   in AVE-Metamaterials per `transmon-decoherence.md:18`.)*
2. **Annihilation = vortex-reconnection check (the §4 candidate).** Test whether $e^-+e^+\to\gamma\gamma$
   is a phase-space reconnection of two opposite-helicity $(2,3)$ loops (time-reverse of genesis,
   `pair-production-axiom-derivation.md`). **Must be measured in phase-space coordinates**
   ($V_{inc}/V_{ref}$, Clifford torus) per the §4 A46 caveat — a real-space lattice-Cartesian
   reconnection metric would be uninformative.
3. **Two-yields overload resolution (§1).** If a downstream driver needs a single "yield" threshold,
   it must name its subject (interior field amplitude → dielectric-saturation yield; embedded-matter
   drag → Bingham-slipstream yield). Recorded, not resolved-by-fiat; left open for the test that needs it.
4. **VFD-ramp threshold exponent (§5 step 2).** The $\dot\omega_{\text{crit}}\sim(\alpha\omega_C)^2$
   dimensional candidate and the standard $\propto\dot\omega^{3/4}$ autoresonance amplitude-threshold
   need reconciling against autoresonance theory (Fajans–Friedland), and the $\alpha$-prefactor shown
   to differ from a generic resonator, before either is more than consistency-class.

### KB-leaf placement — FLAG, do not create (return question to orchestrator/auditor)

This doc and the companion rotor-synthesis doc are two lenses on **one** object (the electron rotor),
both consistency-class, mutually cross-referenced. Two defensible distillation targets:

- **(a) One shared KB leaf** — e.g. `electron-rotor-coherence-synthesis.md` hosting the rotor-ontology
  sections (companion §§1–6) *and* a coherence-Reynolds subsection (this doc's §§1–5), since they share
  the same canonical sources and the same echo-not-chord ceiling.
- **(b) Two leaves** — the rotor doc distills to its own ontology leaf; this doc becomes a `temporal-
  saturation-regime-classifier`-adjacent **electron-specialization** leaf (it is literally
  $\delta_{\text{AVE}}$ applied to the electron), cross-linking the rotor leaf.

Recommendation leans **(b)**: this doc's natural home is *beside* `temporal-saturation-regime-classifier.md`
(it specializes that leaf), while the rotor doc's home is in Vol 2 particle-topology. But both are
viable and the call is a corpus-placement decision. **Per incremental-write + lane discipline I do not
create either leaf** — surfaced here for the auditor/orchestrator to land at promotion time.

---

## Cross-references (canonical leaves + engine — all verify-before-cite checked)

**Substrate-native loss tangent / Reynolds axis**
- `manuscript/ave-kb/common/temporal-saturation-regime-classifier.md` — $\delta_{\text{AVE}}=
  t_{\text{sat}}/t_{\text{period}}$ substrate loss tangent (:29); maps to fluid Reynolds
  (:33, :50-59), cavity-QED $g/\kappa=1/\delta_{\text{AVE}}$ (:142), quantum T1/T2 (:212-223);
  "$\delta_{\text{AVE}}\times N$ = Reynolds analogue" (:302); TAXONOMIC-not-derivational (:310).
- `manuscript/vol_3_macroscopic/chapters/19_phase_transition_turbulence.tex` — Re→drive parameter
  $r=\mathrm{Re}/\mathrm{Re}_{\max}$ (:21-25); $S(\mathrm{Re},\mathrm{Re}_c)=\sqrt{1-(\mathrm{Re}/
  \mathrm{Re}_c)^2}$ (:38); laminar below $\mathrm{Re}_c$, saturated above (:41-43).
- `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/saturation-operator.md` —
  $S=\sqrt{1-(A/A_c)^2}$; "Bingham plastic yield: vacuum flows above $\tau_y=B_{snap}^2/2\mu_0$" (:27).

**Electron Q-factor / intrinsic viscosity**
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` —
  $\alpha^{-1}=Q_{\text{tank}}$ (:15,:38); $\omega_C=c/\ell_{node}$ = Compton = tank eigenfrequency
  (:28); "$1/Q=\alpha$ leaks per cycle through TIR boundary — this IS $\alpha$" (:81).

**Superconductivity = Kuramoto (Cooper pair / BEC rows)**
- `manuscript/ave-kb/vol3/condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md`
  — electron = $0_1$ flux loop spinning at high AC freq (:18); thermal desync = micro-inductive
  drag = resistance (:26,:28); Kuramoto phase-lock $R=1$ (:30-36); "frictionless topological gear
  train" (:44).
- `manuscript/ave-kb/vol3/condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md`
  — the Kuramoto resultbox.

**Qubit decoherence (boundary-node friction channel)**
- `manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md` — noise
  enters ONLY at boundary/lead nodes (:12); coherence metric $C(t)\in[0,1]$ (:14); Ohmic damping
  $\gamma=\tfrac12 Z_0/(\omega_0 L_{eff})$ (:32). **IP-divide note (:18):** QC *application* leaves
  migrated to AVE-Metamaterials private repo; substrate-physics anchors stay canonical in Core.
  This doc stays on the substrate-physics side (mapping), not device engineering.

**Bingham slipstream / drag yield**
- `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` — TVS-Zener
  solid→slipstream: $\eta_0$ (drag) below $V_{yield}$, $\eta=0$ (frictionless slipstream) above
  (:300-308); thixotropic relaxation $\tau_{relax}=\ell_{node}/c$ (:322); zero-impedance skin
  effect / Faraday cage (:338-362).

**CFD lens — Beltrami / Kelvin vortex precedent**
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md` — electron
  = $0_1$ unknot, ropelength $2\pi$ (:11); **Beltrami standing wave $\nabla\times A=kA$** (:13);
  "one-dimensional phase flux loop" / phase-plane (:43) — PHASE space, not real space.
- `manuscript/ave-kb/common/historical-precedents.md` — Kelvin 1867 vortex-atom / Helmholtz 1858
  frozen-in vortex lines (:25); ideal-fluid failure: no confinement / no length scale (:27); AVE
  realizes it via saturable crystal + $(2,q)$ topology + $\ell_{node}$ (:28); **Kelvin = real
  space; AVE $(2,q)$ = phase space / Clifford torus** (:30); consistency-class ceiling (:38-39).

**VFD lens — autoresonant / Duffing / genesis drive**
- `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/autoresonant-dielectric-rupture.md`
  — Duffing detune as amplitude rises (:12); autoresonant PLL sweeps drive freq DOWNWARD to track
  the dropping resonance (:14).
- `src/ave/topological/vacuum_engine.py` — `class AutoresonantCWSource(CWSource)` (:678), PLL
  frequency tracking (:679-720); "same mechanism as Propulsion Ch5 autoresonant rupture" (:83-84);
  autoresonant $\sigma(\omega)$ monotonic rise to $A^2=1.009$ (:104); shifted-$\omega$ tracking (:1358).
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md`
  — genesis C2: $\Omega_{node}(A^2_{local})\approx\omega_{drive}$, Duffing-shifted resonance locks
  with drive (:84); C3 phase-fail → "dissipates instead" (:85) — the genesis-side decoherence.
- AVE-Propulsion `manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex`
  (sibling repo — PLL ring-up picture; cited via engine docstring `vacuum_engine.py:116`).

**Annihilation = reverse genesis (§6 queue)**
- `pair-production-axiom-derivation.md` (above) — forward genesis = drive rings up vacuum →
  nucleates $(e^-,e^+)$; annihilation = reverse (phase-matched rotor pair reconnects → radiates).
