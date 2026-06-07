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

*[scaffold — filled in a following commit]*

---

## §4 — The CFD lens: which fluid concepts clarify the soliton

*[scaffold — filled in a following commit]*

---

## §5 — The VFD lens (autoresonant motor frame) + the emergence hook

*[scaffold — filled in a following commit]*

---

## §6 — Honest ledger + open items

*[scaffold — filled in a following commit]*

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
