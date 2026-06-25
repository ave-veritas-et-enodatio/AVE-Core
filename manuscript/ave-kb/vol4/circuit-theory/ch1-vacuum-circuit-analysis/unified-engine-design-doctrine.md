[↑ Up](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "ARCHITECTURE / ONTOLOGY doctrine for the unified vacuum engine (CONSISTENCY-class — no new physics, no new derived number). Captures the engine-design conclusions worked out 2026-06-24/25 so future engine work stays ON TRACK and knows HOW TO USE the engine. Every load-bearing statement is grounded against an existing file:line or an existing research-doc verdict; the OPEN forks (§ honesty + § open-forks) are flagged-not-closed per flag-don't-fix. Extends `computational-solver-selection.md` (the FDTD-vs-K4 selection matrix) from solver-selection to engine-architecture; referenced from `../../../common/engine-capability-map.md`. Hosts no claim id and mints no number."
-->

## The Unified-Engine Design Doctrine — ontology, scale-invariance, coupling, and what the engine is FOR

> **Class + scope (read first).** This leaf is **CONSISTENCY / ARCHITECTURE-class**. It does **not**
> derive a new number, mint a constant, or advance any chord-DOF. It records the *engine architecture*
> — the ontology the engine implements, the dispatch rule between its continuum and discrete cores, the
> coupling layer, and (the load-bearing part) **what the engine is for and what it must never be asked
> to do.** It extends the FDTD-vs-K4 [`computational-solver-selection.md`](computational-solver-selection.md)
> selection matrix from *which solver* to *the whole engine design*, and it is the design companion to the
> capability map [`../../../common/engine-capability-map.md`](../../../common/engine-capability-map.md)
> (which audits *what each engine carries*; this leaf says *how the converged engine is built and used*).
>
> **The single sentence.** The grid IS the lattice; the lattice is a distributed-reactance chiral-LC
> transmission-line network; linear excitations are its normal-mode WAVES and nonlinear saturation builds
> the soliton CAVITY; and the engine's JOB is to be the microscope **below** the screening scale that
> computes the forward-prediction leaks — **not** to watch the electron form (that is closed-negative).

---

## §A — Ontology: the grid IS the lattice

**The grid is not a discretization of a continuum — it IS the physical lattice at $\ell_{node}$.**
The physical vacuum is a *chiral Laves K4 Cosserat crystal* of nodes at pitch $\ell_{node}$
([`../../../../common_equations/eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):26).
The engine's computational grid is the *same object*, not a numerical stand-in for a smooth field. This
inverts the usual FDTD reading (where the grid is a convenience that converges to a continuum truth as
$\Delta x \to 0$):

- **The lattice is NON-refinable.** $\ell_{node}=\hbar/(m_ec)$ is the physical node spacing, not a mesh
  parameter. There is no sub-$\ell_{node}$ physics to resolve — the lattice has no internal structure
  below its own nodes. **Sub-$\ell_{node}$ refinement is forbidden** (it would invent degrees of freedom
  the substrate does not carry). This is the Nyquist limit as a *physical* statement, not a numerical one.
- **The continuum is the coarse-grain-UP limit, not a refine-down convenience.** "Continuous" means the
  macroscopic effective theory you get by averaging the lattice over many cells — the direction is *up*
  (toward longer wavelengths), never *down* (toward sub-node structure). Classical mechanics and network
  dynamics are macroscopic effective theories of the substrate's bulk dynamics, not fundamental primitives
  ([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):40).

**The lattice is a distributed-reactance chiral-LC transmission-line network.** Each node is a native LC
oscillator: three translational DOF couple capacitively ($\varepsilon_0$, the E-field), three
microrotational DOF couple inductively ($\mu_0$, the B-field) — the same structural reality described in
mechanical (Cosserat micropolar) and electromagnetic (LC resonant) terms
([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):26). The engine therefore has:

- a **FIXED graph** — the K4 connectivity (the topology of who is wired to whom), which never changes
  during cold-lattice operation; and
- a **DYNAMIC constitutive law** $S(A)$ — the per-node saturation kernel $S(A)=\sqrt{1-A^2}$ that modulates
  the cell reactances with the local excitation amplitude $A$. The graph is the wiring diagram; $S(A)$ is
  the varactor/saturable-inductor on every cell.

**Rigid-grid Eulerian until rupture.** The engine field lives *on* fixed nodes — it is field-on-a-lattice
(Eulerian), **not** a moving substance (Lagrangian). The nodes do not flow; the excitation does. The only
exception is the **ruptured-plasma phase** (Axiom 4 Regime IV — BH interiors, pre-crystallization cosmos):
there the K4 topology is destroyed and long-range order is lost
([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):32). The phase transition between the
crystallized and ruptured states IS the A-034 universal strain-snap, occurring identically at every scale
([`eq_axiom_1.tex`](../../../../common_equations/eq_axiom_1.tex):34). Genesis (node birth / pair production)
is likewise a topology-changing event, outside the rigid-Eulerian regime — and is deferred (see §I).

## §B — Scale-invariance: the reactance does not renormalize with resolution

**$Z_0$ and $c_0$ are scale-invariant because $\ell_{node}$ cancels.** The per-cell lumped elements are
$L_{cell}=\mu_0\,\ell_{node}$ and $C_{cell}=\varepsilon_0\,\ell_{node}$, so the cell impedance

$$
Z_{cell}=\sqrt{\frac{L_{cell}}{C_{cell}}}=\sqrt{\frac{\mu_0\,\ell_{node}}{\varepsilon_0\,\ell_{node}}}
=\sqrt{\frac{\mu_0}{\varepsilon_0}}\equiv Z_0\approx376.73\;\Omega
$$

— **the lattice pitch cancels identically** ([`z0-derivation.md`](z0-derivation.md):37,40). Every cell, at
every location, presents the same $Z_0$; this is the lattice's *node-to-node impedance ratio*, a property
independent of the absolute scale $\ell_{node}$. This is the corpus "self-similar at every scale" property
(`clm-zuf7g1`, dual-axis classification: **Class-2 substrate-mechanism emergence on the scale-invariance
sub-axis** — the K4 topology forces $L_{cell}\propto\ell_{node}$ and $C_{cell}\propto\ell_{node}$, producing
the pitch cancellation; the *numerical value* 376.73 Ω is Class-B manifestation via SI substitution of
$\mu_0/\varepsilon_0$, not a substrate-derived number — see [`claims.jsonl`](../../../.index/claims.jsonl)
`clm-zuf7g1` rationale).

**Consequence for the engine: the reactance does NOT renormalize with resolution.** Because $Z_0=\sqrt{\mu_0/\varepsilon_0}$
holds *independent of $\ell_{node}$*, the physics the engine carries (the impedance, the wave speed, the
reflection coefficients) is invariant under a change of cell size. Therefore:

- **$\Delta x$ is a NUMERICAL-convergence knob, not a physics-renormalization knob.** Refining $\Delta x$
  must *reproduce* the scale-invariant physics (it is a convergence test — does the discretization recover
  $c_0,Z_0$?), it must never *change* the physics. A correctly-built engine returns the same $c_0$ and $Z_0$
  at $\Delta x=\ell_{node}$ and at $\Delta x=2\ell_{node}$; if the answer drifts with $\Delta x$, that is a
  numerical bug, not a physical renormalization.
- This is the **validate-on-known** gate in operational form: the small-$|k|$ acoustic branch of the K4
  Bloch matrix recovers $\omega=c_0|k|$ to rel-err $\sim2\times10^{-16}$ and $Z_0$ to rel-err 0
  ([`../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md`](../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md):59-63) —
  the $\ell_{node}$ cancellation is the *check*, NOT an emergence claim.

> **🔴 CORRECTION CAPTURED (this session, 2026-06-24/25; consistency-class, no body to retract elsewhere).**
> An earlier framing held that the cell reactances "renormalize with resolution" — i.e. that
> $L_{eff}(\Delta x)$ / $C_{eff}(\Delta x)$ must be re-scaled as the grid is refined to keep the physics
> fixed. **That framing was WRONG.** $L_{cell}/C_{cell}=\mu_0/\varepsilon_0$ is scale-invariant *by
> construction* — the $\ell_{node}$ cancels in the ratio. There is no reactance renormalization-group flow
> with $\Delta x$: the reactance is fixed by the constitutive constants $\mu_0,\varepsilon_0$ and the local
> $S(A)$, period. The only $\Delta x$-dependence a correct engine shows is *numerical convergence to the
> scale-invariant answer*. (Where genuine $\Delta x$-physics DOES appear is the band edge — see §D — but
> that is dispersion *signal*, set by $q\cdot\ell_{node}$, not a renormalization of the reactance.)

## §C — Coupling architecture: linear WAVES, nonlinear CAVITY, integer winding

<!-- SECTION C PLACEHOLDER -->

## §D — Continuum-vs-discrete dispatch

<!-- SECTION D PLACEHOLDER -->

## §E — Connectivity: chiral z=3 srs vs achiral z=4 diamond

<!-- SECTION E PLACEHOLDER -->

## §F — Algebra: the biquaternion at the coupling layer

<!-- SECTION F PLACEHOLDER -->

## §G — Screening: what the engine is FOR

<!-- SECTION G PLACEHOLDER -->

## §H — Honesty guards: what keeps the engine on track

<!-- SECTION H PLACEHOLDER -->

## §I — Open forks: flagged, NOT closed

<!-- SECTION I PLACEHOLDER -->

---

## Cross-references

<!-- XREF PLACEHOLDER -->
