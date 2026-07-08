# Electron Equivalent Circuit — Frozen Model Definition (round-2b lock test)

**Date:** 2026-07-07
**Arc:** `analysis/electron-equivalent-circuit`
**Nature:** **DESIGN ARTIFACT / HYPOTHESIS-CLASS.** This is the *frozen model
definition* — the equivalent circuit that round-2b ("B") **will** simulate — in
the Vol 9 device-datasheet register. It is **NOT a run and NOT a result.** Every
statement is of the form *"the circuit B will simulate is X"* or *"the design
rationale for element Y is Z"* — never *"the electron is this circuit"* and never
*"X was measured."* Nothing here has been run except the base-tank
well-formedness sanity check (§8). It comes back to Grant for review **before any
2b simulation.**

**Predecessor context.** This artifact formalizes the topology walked in the
electron-lock design-rationale note (`research/2026-07-07_electron-lock_design-note.md`,
PR #568, DO-NOT-MERGE). The topology is **FROZEN from that Grant-walk**; this
document formalizes it into a component table, a physical-mapping table, and a
SPICE netlist. It does **not** redesign the physics. The Stage-1 minimal result
(`electron-lock-stage1`, verdict **[DOMINATED]** — bare two-oscillator dynamics
prefers a 1:1 lock, so (2,3)-selection is *topological*, not bare-dynamical) is
the load-bearing input that shapes the flags in §9.

---

## FIREWALL (mechanical exclusion — load-bearing)

This is a **datasheet model**, so a firewall runs down its middle:

- **LEGITIMATE (consistency-class) — the component VALUES.** Every element value
  (`L_cell = μ₀·ℓ_node`, `C_cell = ε₀·ℓ_node`, `Z₀ = √(L/C) = 377 Ω`,
  `V_snap ≈ 511 kV`, `V_yield ≈ 43.65 kV`, `I_max ≈ 124.4 A`) is imported from
  the vacuum's **calibrated datasheet constants** (`ave.core.constants`). Using
  the datasheet's own numbers to *define the model* is exactly what a datasheet
  model is for. These are consistency-class inputs. **No value is hard-coded** —
  all flow from `ave.core.constants` (per `ave-canonical-source`).

- **FORBIDDEN (emergence-class OUTPUTS) — the (2,3)-selection and ⟨N⟩.** The
  circuit exists to test whether the dynamics **select** the (2,3) winding and
  **self-sustain at zero drive**. Those *outputs* — the settled winding pair, the
  selectivity verdict, and any sampling count ⟨N⟩ — **must be topological /
  dynamical / scale-invariant.** They may **never** be tuned to, seeded from, or
  checked against `m_e` (or any mass ratio) *during* a derivation. A blind-derived
  output priced against a target only *afterward*, in a firewalled comparison, is
  the only admissible route (the ⟨N⟩ knife, design-note §FIREWALL).

- **α and Q = 1/α are EXCLUDED from any selection claim.** The tank
  quality-factor identity `Q = 1/α` is an **identity, never a derivation input**
  (memory: cite `Q_TANK = 1/ALPHA` as identity NOT derivation). It must not enter
  the (2,3)-selection logic. **Homonym guard:** a small integer this circuit might
  eventually derive (a winding 2 or 3, a floor ~7) is >3 OOM from 137 and has
  ZERO α contact — do not let the numeric coincidence of "small integers" blur the
  firewall.

- **Datasheet operating-point caveat (α-echo touch — surfaced).** The A1 mass
  varactor's *static bias magnitude* is the datasheet value `V_A1 = √α·V_snap =
  V_yield ≈ 43.65 kV` (the electron's A1 core sits at `A = V/V_snap = √α ≈ 0.085`,
  `S ≈ 0.996`, deeply sub-saturated — `device-circuit-models.md` §electron
  operating-point). This magnitude carries the α-echo. It is admissible **only as
  a consistency-class operating point for the DC-converge sanity check**; the
  (2,3)-selection verdict must be **invariant** to the absolute bias magnitude
  (scale-invariant), so the α-echo in the bias never reaches the selection claim.
  In the netlist the bias is a free parameter (`V_A1`) defaulted to the datasheet
  value, explicitly NOT a selection input.

## §0 — Canon anchors (verified verbatim, two-method)

All quotes read from the working tree at HEAD `bdf48720` (== `origin/main`) and
cross-checked by `grep`. Line numbers are as of that HEAD.

**A0.1 — the two orthogonal saturating "capacitances" are sector-keyed
(A1 ⊥ T2), keys NEVER crossed**
(`manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex:15`;
mirrored in `src/ave/solvers/spice_models/ave_vacuum_cell.lib:34,101` and KB
`CLAUDE.md` INVARIANT-S2):
> The cell's metric varactor is the *divergent* longitudinal-A1 bond compliance
> $C_{eff}(V) = C_0/S(V)$ … it **knees at $V_{snap} = m_ec^2/e \approx 511$ kV** …
> *not* at $V_{yield}$. This is distinct from the *roll-off* transverse-$T_2$
> permittivity $\varepsilon_{eff}=\varepsilon_0 S$ … which keys on the transverse
> yield wall $V_{yield}=\sqrt\alpha\,V_{snap}\approx43.65$ kV. The two share the
> EE name "capacitance" but are **orthogonal reactances (A1 $\perp$ T2)**;
> identifying them is the genesis-24 double-count.

So: **A1 metric varactor `C₀/S`, keyed `V_snap` (mass sector)** vs. **T2 dielectric
`ε₀·S`, keyed `V_yield` (charge sector)** — two orthogonal reactances. Crossing
the keys is the recurring failure mode; this artifact keeps them separate.

**A0.2 — the (2,3) is the phase-space winding: "2 windings d-axis, 3 windings
q-axis," NOT a real-space knot** (`torus-knot-uniqueness.md:15`):
> the electron is the $0_1$ **unknot** in real space … The "$(2, 3)$ trefoil" …
> refers to the **phase-space Clifford-torus winding pattern** of the electron's
> bond-pair LC tank **(2 windings on the d-axis, 3 windings on the q-axis)**, NOT
> a real-space trefoil knot. The trefoil lives in phase space; the soliton lives
> in real space.

This artifact models the **phase-space tank** (the (d, q) / Park quadratures);
the winding is measured in *those* coordinates (phase-space-coordinate discipline,
A46). The real-space $0_1$ ring is a Stage-2 addition, not part of this circuit.

**A0.3 — the "3" is the empty V-sector U(1) fibre that does NOT yet
self-assemble** (`historical-precedents.md:31`):
> The **full `(2,3)`** does not yet self-assemble — its "3" is the **V-sector
> U(1) fibre**, needing the coupled K4+Cosserat engine — a *localized* remaining
> gap …

The "2" Cosserat winding forms; the "3" V-sector quadrature is **empty**. Filling
it is the open question this circuit is built to test (§9).

**A0.4 — the (2,3) is a nonlinear-saturation-confined-soliton topological
property, NOT a linear mode** (`electron-identification.md:33`):
> **(p,q) is fundamentally a nonlinear-saturation-confined-soliton topological
> property at the K4-bond-pair LC-tank phase-space level; NOT a linear-regime
> substrate-mode-eigenvalue label** — Path B-prime … band-splitting test
> FALSIFIED 2026-05-27 …

So the winding is a **nonlinear / saturated** property — the saturation kernel on
each reactance is load-bearing, not decoration.

**A0.5 — the Γ=−1 wall is the Ax4 saturation short at `V_yield`**
(`electron-identification.md:30,51`):
> when the underlying transverse Cosserat-microrotation wave's amplitude crosses
> $V_{yield}$ … Axiom 4 engages: $C_{eff} \to \infty$, $Z_{local} \to 0$,
> $\Gamma \to -1$. The lattice self-creates a perfect TIR mirror … (Ax4 kernel
> $S(A)=\sqrt{1-A^2}$; $A\to1 \Rightarrow S\to0 \Rightarrow Z\to0 \Rightarrow
> \Gamma\to-1$).

The confinement wall = the saturation-driven reflective short, a **boundary
condition** (property 3, the SURVIVING route per the leaf's 2026-06-24 banners),
not a bulk interior well.

**A0.6 — mass requires ZERO-DRIVE persistence; the kernel is anhysteretic**
(`loop-gap-electron-resonator-closure-doctrine.md:18`):
> Canon Level-1 kernel $S_{\mathrm{eq}}(A)=\sqrt{1-A^2}$ is **anhysteretic** —
> zero enclosed loop area — so **reactive storage under drive is not mass**; mass
> requires **zero-drive persistence** (ferrite $B_r$ at $H=0$ analogue) …

So the lock test must be run at **zero external drive** (the anhysteretic-kernel
constraint): reactive storage under a continuing drive is a fool-mode (CVR-SET ≠
mass, doctrine §5), not the electron.

## §1 — The equivalent circuit (ASCII schematic)

**HYPOTHESIS/DESIGN-CLASS.** The circuit B *will* simulate. Two coupled
saturating LC tanks (the phase-space (d, q) Park quadratures), a DC-biased A1
metric varactor (the mass), a bias-controlled parametric mutual coupling
`M(V_A1)` (the L↔C pump — chosen fork, §4), and a saturation-driven `Γ=−1` wall
on the q-tank (the confinement cage). **Zero external drive** (A0.6).

```
                         A1 MASS SECTOR (DC bias = the operating point)
                     ┌───────────────────────────────────────────┐
                     │   V_A1 ──[ C_A1 = C₀/S(V/V_snap) ]── gnd    │   keyed V_snap
                     │        (divergent metric varactor;          │   (511 kV)
                     │         the electron's mass; sub-saturated   │   A=√α, S≈0.996
                     │         static bias A = √α ≈ 0.085)          │
                     └───────────────────┬───────────────────────┘
                                         │ V_A1 sets the coupling depth
                                         │ (parametric pump strength)
                                         ▼
   d-AXIS QUADRATURE = "2" (Cosserat)         q-AXIS QUADRATURE = "3" (V-sector)
   the winding that RINGS/FORMS               the EMPTY one (fill target)
 ┌─────────────────────────────────┐       ┌─────────────────────────────────┐
 │  ND ●───[ L_d = L_cell/S(I) ]──┐ │       │ ┌──[ L_q = L_cell/S(I) ]───● NQ  │
 │      │   (saturating inductor)  │ │       │ │  (saturating inductor)   │     │
 │   [ C_d = C_cell ]             │ │◄═════►│ │        [ C_q = C₀·S(V/V_yield) ]│
 │      │       d-tank ω_d        │ │  M(V_A1)│ │  T2 collapse cap, keyed V_yield│
 │     gnd ───────────────────────┘ │  mutual │ └────────────────┬──────────────┘
 └─────────────────────────────────┘  flux   │                   │
                                              │          [ Γ=−1 WALL: Z=Z₀·√S(V/V_yield) ]
   ω_d : ω_q  locked to  2 : 3                │          (reflective short → gnd at yield;
   (the (2,3) winding = MEASURED output,      │           the confinement cage termination)
    compute_Q_link-style; never planted)      │                   │
                                              └──────────────────gnd
```

**Reading the schematic.**
- The **two tanks** are independent evolved DOFs (design-note §7 P2:
  co-keying must be *read out*, never hard-wired). The `◄═M(V_A1)═►` link is the
  **only** channel between them — a **parametric mutual inductance** whose strength
  is set by the A1 mass bias (§4, chosen fork).
- The **A1 mass varactor** (top) is the divergent `C₀/S`, keyed `V_snap` — the
  DC operating point. Its bias voltage `V_A1` is the "slow" control that pumps the
  fast d↔q exchange (varactor framing, design-note §4; the slow/fast hierarchy is
  the open gut-check, design-note §9 → flag (i)).
- The **q-tank cap** is the T2 dielectric collapse `C₀·S`, keyed `V_yield` — the
  AC/charge element. The **Γ=−1 wall** on the q-node is the saturation short
  `Z=Z₀·√S→0` at `V_yield` (A0.5).
- The **d↔q frequency ratio** is locked toward 2:3; the winding pair (2,3) is a
  **measured output** of the settled phasor trajectory in the (d, q) phase plane,
  not a seed.

## §2 — Component table

**All values from `ave.core.constants` — no hard-coding** (`ave-canonical-source`).
Values shown to the precision the constants module carries; the netlist
substitutes the live constants, not these rounded literals.

| Element | Symbol | Value (from `ave.core.constants`) | Physical role |
|---|---|---|---|
| Base bond inductor | `L_cell = μ₀·ℓ_node` | `L_CELL ≈ 4.8526×10⁻¹⁹ H` | The cell tank's inductance (the LC-tank "L") |
| Base node capacitor | `C_cell = ε₀·ℓ_node` | `C_CELL ≈ 3.4191×10⁻²⁴ F` | The cell tank's capacitance (the LC-tank "C") |
| Cell impedance | `Z₀ = √(L_cell/C_cell)` | `Z_0 = 376.7303 Ω` | Characteristic impedance = √(μ₀/ε₀) (matched-port anchor) |
| Cell frequency | `ω_cell = 1/√(L_cell·C_cell)` | `OMEGA_C ≈ 7.7634×10²⁰ rad/s` (`f_C ≈ 1.2356×10²⁰ Hz`) | Compton frequency = single-bond LC eigenfrequency |
| d-tank saturating inductor ("2") | `L_d = L_cell/S(I/I_max)` | `S(A)=√(1−A²)`, `I_MAX ≈ 124.384 A` | The **Cosserat inductive** quadrature — the winding that rings/forms |
| d-tank capacitor | `C_d = C_cell` | `C_CELL` (cold) | Completes the d-tank resonator |
| q-tank saturating inductor | `L_q = L_cell/S(I/I_max)` | `S(A)=√(1−A²)`, `I_MAX ≈ 124.384 A` | Completes the q-tank resonator (the "3" carrier) |
| q-tank T2 dielectric cap ("3") | `C_q = C₀·S(V/V_yield)` | **collapse** form, keyed `V_YIELD ≈ 43651.85 V` | The **T2 charge/AC** quadrature — the empty V-sector "3" (fill target) |
| A1 metric varactor (mass) | `C_A1 = C₀/S(V/V_snap)` | **divergent** form, keyed `V_SNAP ≈ 510998.95 V` | The **A1 mass** element (DC bias = operating point); mass = A1 |
| A1 static bias magnitude | `V_A1 = √α·V_snap = V_yield` | `≈ 43651.85 V` → `A = √α ≈ 0.0854`, `S ≈ 0.996` | Sub-saturated mass-core bias (consistency-class; NOT a selection input — §FIREWALL) |
| Parametric mutual coupling | `M(V_A1)` (chosen fork §4) | `M ∝ V_A1/V_snap` (bias-controlled) | The **L↔C pump** — mass bias sets the d↔q energy-trade strength |
| Γ=−1 confinement wall | `Z_wall = Z₀·√S(V/V_yield)` | `→ 0` as `S→0` at `V_yield` ⇒ `Γ→−1` | The **confinement cage** termination on the q-tank (reflective short) |
| (drive) | — | **ZERO external drive** | Mass = zero-drive persistence (A0.6); no source in the lock test |

**Saturation kernel (all reactances):** `S(A) = √(1 − A²)` from
`ave.axioms.saturation` / `ave.axioms.scale_invariant` — the Axiom-4 quarter-arc
kernel (A0.4). `Γ = (Z − Z₀)/(Z + Z₀)` from `ave.axioms.saturation.reflection_coefficient`;
`Z = Z₀·√S` (the μ/shear-load short) from `impedance_at_strain`.

## §3 — Physical-mapping table (circuit element ↔ physics)

The load-bearing table: **which circuit element IS which piece of physics.**
Sector column keeps `A1 ⊥ T2` explicit (A0.1); coordinate column keeps
phase-space vs real-space explicit (A0.2, A46).

| Circuit element | Physics it IS | Sector | Coordinate | Canon anchor |
|---|---|---|---|---|
| **A1 metric varactor** `C₀/S`, keyed `V_snap`; DC-biased at `V_A1` | **THE MASS** (A1 dilatation; mass = A1, #260). The DC operating point *is* the rest-mass bias. | **A1** | phase-space (bias/DC) | A0.1; `electron-identification.md:60` (m_e = calibration anchor) |
| **d-tank** (`L_d/S`, `C_d`), the winding that rings | **THE "2"** — the Cosserat micro-rotation winding (d-axis; 2 windings). The one that self-traps / forms. | **T2** (Cosserat) | phase-space, d-axis | A0.2, A0.3 (the "2" Cosserat winding forms) |
| **q-tank** (`L_q/S`, `C_q = C₀·S` keyed `V_yield`) | **THE "3"** — the V-sector U(1) fibre (q-axis; 3 windings). The **empty** quadrature. | **T2 / V-sector** | phase-space, q-axis | A0.2, A0.3 ("the '3' is the V-sector U(1) fibre, does not yet self-assemble") |
| **Parametric mutual coupling** `M(V_A1)` (chosen fork §4) | **THE L↔C PUMP** — the `A1·|T2|²` reactive coupling; the mass bias modulates the d↔q energy trade (the candidate mechanism for *filling* the "3"). | **A1 × T2** (cross-sector, reactive) | phase-space (d↔q channel) | design-note §4 (`A₁·|T₂|²` parametric, Ax3-selected) |
| **Γ=−1 wall** `Z=Z₀·√S(V/V_yield)→0` | **THE CONFINEMENT CAGE** — the saturation-driven reflective TIR short at `V_yield` (boundary condition, property 3). | **T2 yield wall** | real-space boundary | A0.5; `electron-identification.md:30,51` |
| **Zero external drive** | **THE MASS PERSISTENCE CONSTRAINT** — mass requires zero-drive persistence; reactive storage under drive is *not* mass. | — | — | A0.6; loop-gap doctrine §1 |
| **(2,3) winding readout** `compute_Q_link`-style on the (d,q) phasor | **THE MEASURED OUTPUT** — the settled winding pair; firewalled emergence-class output, never planted. | T2 topology | phase-space (Clifford torus) | A0.2, A0.4; §FIREWALL |

**The one-line summary of the mapping:** *the mass (A1 varactor) biases a
parametric pump `M(V_A1)` that trades energy between the ringing "2" tank
(Cosserat, d-axis) and the empty "3" tank (V-sector, q-axis), inside a Γ=−1
saturation cage — and the test asks whether the (2,3) winding emerges, selectively,
at zero drive.*

## §4 — The parametric-coupling element (MODELING FORK — flag for Grant)

**🚩 FLAG (i) — prominently surfaced.** The parametric coupling is the
symmetry-forced `A₁·|T₂|²` term (design-note §4): dilatation × the scalar
invariant of the shear. In circuit terms, the **A1 bias voltage (the DC operating
point = the mass) modulates the mutual coupling between the inductive "2" (d-axis)
and the capacitive "3" (q-axis) quadratures.** This element is **the candidate
mechanism for filling the "3."** Getting its form right is the whole point of the
artifact, so the fork is flagged here for Grant.

### Chosen element: (a) nonlinear mutual inductance `M(V_A1)`

**Choice: (a) a bias-controlled mutual inductance `M(V_A1)` between the two
tanks** (the orchestrator's lean — *the mass bias sets the d↔q energy-trade
strength*). Realized as a mutual-flux term in each tank's flux law:
`Φ_d = L_cell·I_d/S(I_d) + M(V_A1)·I_q` and symmetrically for `Φ_q`, with
`M(V_A1) = M₀·(V_A1/V_snap)` (the coupling depth ∝ the normalized mass bias).

**Justification (four reasons, in priority order):**

1. **Ax3-clean / genuinely reactive.** A mutual inductance stores no energy
   dissipatively; the coupling energy `M·I_d·I_q` is conservative. Design-note §4
   is explicit that the coupling **must be parametric, not resistive** — a
   dissipative `A₁→T₂` transduction is a velocity-coupled loss term that **Axiom 3
   forbids below yield.** A mutual inductance satisfies the Ax3 selection rule by
   construction.
2. **It IS "the mass bias sets the energy-trade strength."** `M = M(V_A1)` makes
   the d↔q energy-exchange coefficient a direct function of the mass operating
   point — the literal circuit reading of "A₁ modulates the mutual coupling"
   (`A₁·|T₂|²` as a bias-dependent mutual reactance).
3. **It preserves the two tanks as INDEPENDENT evolved DOFs** (design-note §7 P2 —
   the emergent-co-keying guard, the #567-tautology preemption). A mutual
   inductance couples two otherwise-galvanically-separate resonators *without
   merging them into one tank*; the winding-lock stays a **measured** attractor,
   not a definitional harmonic of a shared reactance.
4. **Homonym-clean.** `M` couples the two *windings* (the "2" and the "3"); it
   does not touch the 2×-per-cycle L↔C energy exchange *within* either tank
   (§6). No aliasing between the two "2"s.

### Alternatives (documented, NOT chosen — with the physical trade-off)

- **(b) a bias-controlled coupling varactor** (a shared capacitance `C_c(V_A1)`
  bridging the two tanks' voltage nodes). *Also* reactive and Ax3-clean, and a
  legitimate parametric element. **Trade-off / why not chosen:** a shared bridging
  capacitance ties the two tanks' q-axis (capacitive/voltage) states together,
  which **partially merges** their voltage nodes — exactly the co-keying-by-
  construction hazard the design-note §7 P2 guard warns against (it can make the
  two tanks harmonics of one effective tank, rendering the winding-lock
  definitional). Mutual **inductance** keeps the tanks galvanically separate, so
  (a) is the safer instantiation of the same reactive-coupling physics.
- **(c) a controlled source** (a behavioral VCVS/VCCS injecting `A₁·|T₂|²`
  directly). Most flexible, **least physical.** **Trade-off / why not chosen:** a
  behavioral source is a *math element*, not a reactance — it can silently inject
  net energy (an active / non-reciprocal element), which would be a **PUMP**, not
  a reactive coupling. That is precisely the *pump-detonation* fool-mode (loop-gap
  doctrine §5.6) and the Ax3-forbidden dissipative/active transduction. Admissible
  **only as an instrumented diagnostic**, never as the physical model.

### Load-bearing caveat on the whole fork (folds into flag (i))

The choice **presumes the varactor framing** — A1 a *slow* bias, T2 a *fast*
small-signal (design-note §4 leading hypothesis). Whether that slow/fast
hierarchy is real, **or** the two sectors are co-equal two-mode-resonance
oscillators with no clean bias/signal split, is the **UNRESOLVED gut-check
(design-note §9)** and is **Grant's framing call.** If the co-equal reading wins,
the modelling backbone changes (a genuine two-mode resonance, not a
parametric-varactor), and `M(V_A1)`'s "bias-controlled" form is the wrong
idealization. Surfaced, not resolved.

## §5 — The Γ=−1 confinement wall

**HYPOTHESIS/DESIGN-CLASS.** The confinement cage is the **saturation-driven
reflective short** on the q-tank: as the transverse-T2 amplitude approaches
`V_yield`, `S(V/V_yield) → 0`, the μ/shear-load impedance `Z = Z₀·√S → 0`, and
the reflection coefficient `Γ = (Z − Z₀)/(Z + Z₀) → −1` (A0.5). This is the
**boundary-condition** flip (impedance-matched `Γ=0` → TIR `Γ=−1`), the property-3
route that SURVIVES per the leaf's 2026-06-24 banners — **not** a bulk
self-focusing interior well (that reading is falsified).

- **Canonical sign — the SHORT, not the OPEN.** `Z = Z₀·√S → 0 ⇒ Γ → −1` (the
  μ/shear "mass-cage SHORT"), the corrected sign — **not** the forbidden `ε`-load
  `Z = Z₀/√S → ∞ ⇒ Γ → +1` (the OPEN anti-trap). Both have `|Γ| = 1`; they differ
  only in boundary phase (KB `CLAUDE.md` INVARIANT-S2). This circuit uses the
  `Γ = −1` short.
- **Source primitives.** `Γ` from `ave.axioms.saturation.reflection_coefficient`;
  `Z = Z₀·√S` from `impedance_at_strain` (Op3/Op14 primitives). The wall keys on
  `V_yield` (the T2 yield wall), consistent with the T2 dielectric cap.
- **🚩 Modeling honesty flag (Ax3-lossless).** In the netlist the wall is realized
  as a **saturation-gated reflective termination** whose impedance ramps toward a
  short at `V_yield` (a behavioral element, DC-convergent). A *genuinely lossless*
  reactive short (Z→0 via a diverging reactance, zero dissipation) is the more
  faithful Ax3 form; the reflective-termination realization is adequate for the
  well-formedness sanity check but is a **2b-sim refinement** — surfaced, not
  silently approximated. This matters because a *resistive* short would leak the
  cavity (loss below yield), which Ax3 forbids and which would confound a
  zero-drive persistence verdict.

## §6 — Homonym guard + sector discipline

### The two "2"s are DIFFERENT objects (name them distinctly)

- **The winding-"2"** (`n_d = 2`): the **topological winding number** of the
  d-axis (Cosserat) quadrature — how many times the phasor wraps the toroidal
  angle per closed orbit. An **integer, phase-space, topological** object (A0.2).
  This is *the* "2" of the (2,3) electron.
- **The reactive-"2"** (the 2×-per-cycle L↔C exchange): in *any* LC tank, energy
  sloshes between L and C **twice per RF cycle** — the reactive-power "2×." A
  **continuous, per-tank, dynamical** object present in every resonator. This is
  **NOT** the winding "2."

They are numerically both "2" and physically unrelated. Throughout this artifact,
"the 2" / "winding-2" always means the **topological d-axis winding**; the
2×-per-cycle exchange is always spelled out as such. (Same discipline applies to
"3": the winding-"3" `n_q = 3` is the V-sector q-axis winding number, never a
harmonic index of the reactive exchange.)

### Sector discipline (A1 ↔ V_snap, T2 ↔ V_yield — NEVER crossed)

The recurring failure mode (the "genesis-24 double-count," A0.1) is identifying
the two orthogonal saturating "capacitances." This artifact keys them separately
and never crosses the keys:

| Sector | Element | Form | Key | Role |
|---|---|---|---|---|
| **A1** (mass, dilatation) | metric varactor `C_A1` | **divergent** `C₀/S` | **`V_snap`** (511 kV) | the mass / DC bias |
| **T2** (charge, Cosserat) | dielectric cap `C_q` | **collapse** `C₀·S` | **`V_yield`** (43.65 kV) | the AC / charge tank + yield wall |

The **A1 key is `V_snap`; the T2 key is `V_yield`.** Crossing them (e.g. keying the
divergent varactor on `V_yield`, or the collapse cap on `V_snap`) is the
mis-scoping the `.lib` sector-keying fix (2026-07-03, `def-vyvsn1`) corrected — do
not re-introduce it. `A1 ⊥ T2`: the two "capacitances" are **orthogonal
reactances**, never one phasor.

## §7 — The netlist

The SPICE realization is the `AVE_ELECTRON_EQUIVALENT` subckt in
`src/ave/solvers/spice_models/ave_electron_equivalent.lib` (a new design-artifact
lib that `.INCLUDE`s the base `ave_vacuum_cell.lib`). It follows the base lib's
ngspice-46 idioms (charge element `C…Q={}` for nonlinear caps; flux element
`L…Flux={}` for nonlinear inductors; `min(…,0.9999)` kernel clamp).

- **Ports:** `ND` (d-axis "2" tank), `NQ` (q-axis "3" tank), `A1B` (A1 mass bias).
- **A1 mass varactor:** `C_A1 = C₀·V/S(V/V_snap)` on `A1B` (divergent, keyed
  `V_snap`).
- **d-tank ("2"):** `L_D` saturating inductor with the **mutual flux term**
  `M(V_A1)·i(L_Q)`, `M(V_A1) = KM0·V(A1B)/V_snap` (the chosen fork (a)); plus
  `C_D`.
- **q-tank ("3"):** `C_Q = C₀·S(V/V_yield)·V` (collapse, keyed `V_yield`) plus
  `L_Q` carrying the reciprocal mutual flux term.
- **Γ=−1 wall:** `R_WALL = W_OPEN·S(V/V_yield) + W_MIN` on `NQ` (reflective short
  at yield).

A driver emits the probe netlist via
`ave.solvers.spice_netlist_compiler.compile_electron_equivalent_dc_probe(...)` and
substitutes the live constants (`L0=L_CELL`, `C0=C_CELL`, `V_A1=V_YIELD`, …) for
the physical run. The `.op` probe applies the A1 bias, instantiates the circuit at
**zero external drive**, and asks for a DC operating point.

> **Design-class note.** This netlist DEFINES the model; it does not select
> anything. The mutual-flux coupling, the collapse/divergent sector split, and the
> reflective wall are all present so the eventual 2b driver (Grant-gated) can seed
> the tanks via initial conditions and evolve them — the netlist itself asserts no
> lock and no winding.

## §8 — Sanity check (base-tank resonance + well-formedness ONLY)

**SCOPE.** The sanity check asserts (a) the base tank's electrical anchors and
(b) the netlist is well-formed. It **does NOT** run the zero-drive self-sustain /
(2,3)-lock test — that is **2b-Stage-1**, gated on Grant's review of this circuit.

Test: `src/tests/test_electron_equivalent_circuit.py::TestBaseTankResonance`
(and the ngspice siblings). Result at HEAD:

| Check | Assertion | Outcome |
|---|---|---|
| Cell values are lumped-per-node | `L_cell = μ₀·ℓ_node`, `C_cell = ε₀·ℓ_node` | PASS |
| Base-tank impedance | `√(L_cell/C_cell) = Z₀ = 376.7303 Ω` | PASS |
| Base-tank resonance | `1/√(L_cell·C_cell) = ω_cell = OMEGA_C ≈ 7.7634×10²⁰ rad/s` | PASS |
| Netlist parses + DC-converges | `AVE_ELECTRON_EQUIVALENT` `.op`, ngspice exit 0, no `aborted`/`singular` | PASS |
| A1 bias holds | `V(A1B) = V_A1 = V_yield ≈ 43651.85 V`; tanks at 0 (zero drive) | PASS |
| AC resonance positive control | ngspice peak `= 1/(2π√LC)` on scaled linear cell (within 1%) | PASS (5.041 GHz vs 5.033 GHz analytical) |

**7/7 passed** (`test-locked`,
`src/tests/test_electron_equivalent_circuit.py::TestBaseTankResonance`). ngspice
46 present; all three ngspice checks exercised. **This is the ONLY thing run in
this artifact.** No lock, no persistence, no winding was measured or claimed.

## §9 — Flags for Grant (three)

**🚩 FLAG (i) — the parametric-coupling element choice (the modeling fork).**
Chosen: **(a) nonlinear mutual inductance `M(V_A1)`** between the two tanks
(genuinely reactive, Ax3-clean, keeps the tanks independent, homonym-clean;
justification + the (b)/(c) alternatives with trade-offs in §4). **Load-bearing
caveat:** the choice **presumes the §4 varactor framing** (A1 a slow bias, T2 a
fast small-signal). Whether that slow/fast hierarchy is real, or the two sectors
are **co-equal two-mode oscillators** with no clean bias/signal split, is the
**UNRESOLVED design-note §9 gut-check** and is **Grant's framing call.** If the
co-equal reading wins, `M(V_A1)`'s bias-controlled form is the wrong
idealization and the modelling backbone changes.

**🚩 FLAG (ii) — the open question this circuit is built to test.** In one
sentence: **can the parametric pump `M(V_A1)` fill the empty capacitive "3"
(V-sector) quadrature and self-sustain at ZERO external drive, and is the
resulting (2,3) winding SELECTIVE (coprimality closing the resonance)?** Three
sub-questions, each firewalled (§FIREWALL):
- **Fill:** does energy transfer from the ringing "2" (d-axis Cosserat) into the
  empty "3" (q-axis V-sector), which canon says *does not yet self-assemble*
  (A0.3)?
- **Self-sustain:** does it persist at **zero drive** (A0.6 — mass = zero-drive
  persistence; reactive storage under drive is not mass)?
- **Select:** is (2,3) a *selective* attractor (neighbours (2,2), (2,5), off-ratio
  do NOT all lock), not a seeded fixed point (design-note §7 NEIGHBOR gate)? The
  winding is a **measured** output, never planted.

**🚩 FLAG (iii) — the check owed: did genesis-24 already have a resonant reactive
L↔C channel to the q-axis? (If so, this candidate is AT RISK.)** Verified against
the corpus (verify-before-cite, two-method) — the answer is **nuanced, and the
candidate is genuinely at risk on two axes:**

- **The DEFAULT genesis engine had NO such channel (a structural zero).** The
  `ω→V` source (the channel that would pump the V-sector "3") was a **measured
  structural zero: `max|V_inc| = 0`, `w_pol ≡ 0`** (genesis GAP-1,
  `manuscript/ave-kb/vol9/ch3-pin-port-configuration/index.md:18`;
  "topology-selection REFUTED (no (2,3) self-assembles, w_pol ≡ 0)"). To *that*
  extent the parametric `M(V_A1)` is genuinely the **missing coupled-K4+Cosserat
  channel** A0.3 says is needed — it is not pre-empted by the base engine.
- **BUT a prior candidate reactive coupling into the V-sector EXISTS and is
  OFF-BY-DEFAULT precisely because it DOUBLE-COUNTS the Op14 varactor.** The
  flag-gated Lagrangian-EMF reciprocal (the −2 Lenz back-EMF,
  `src/ave/topological/k4_cosserat_coupling.py:223` `use_lagrangian_emf_coupling=False`
  by default) stays off **"because on small-amplitude mixed-mode it double-counts
  the Op14 varactor `C_eff(V)`, where both signs diverge"** (`index.md:18`,
  2026-06-21 Rule-12 update). **My `M(V_A1)` touches the SAME q-tank Op14 varactor**
  (the T2 collapse cap `C_eff(V/V_yield)`), so the candidate is **at risk of the
  identical double-count** — the genesis-24 double-count restated for this circuit.
  The 2b driver MUST check that `M(V_A1)` does not re-inject a reactive path
  already carried by the q-tank's `C_eff(V)`.
- **Forbidden-wiring guard (must not degenerate into it).** `M(V_A1)` uses the A1
  **bias magnitude** `V(A1B)` as a coupling control. It must **NOT** degenerate,
  in the 2b sim, into wiring the (2,3) **winding** into the A1 breather's own
  `(V_inc, V_ref)` phasor — `V_ref` is a *read-only projection* of the same scalar
  `V`, not an independent DOF; doing so self-inflicts the genesis-24 `w_pol=0`
  double-count (`master-equation.md:20`, Grant-ratified). The two "3"s stay
  orthogonal (A1 ⊥ T2).
- **And the Stage-1 verdict compounds the risk.** `electron-lock-stage1` returned
  **[DOMINATED]** — bare two-oscillator dynamics prefers a **1:1** lock, so
  (2,3)-selection is **topological, not bare-dynamical.** A purely reactive
  `M(V_A1)` that only *couples* the tanks is therefore unlikely to *select* (2,3)
  on dynamics alone; the selective closure may need the topological ingredient
  (coprimality / the Γ=−1 cage geometry), not just a fuller pump. **This is the
  sharpest risk to the candidate — surfaced, not resolved: Grant's call whether
  the parametric pump is expected to select, or only to fill.**

**Net (flag-don't-fix):** the candidate is NOT dead — genesis's V-sector channel
was a structural zero, so `M(V_A1)` adds a genuinely-absent channel. But it faces
(1) the Op14 `C_eff(V)` double-count risk, (2) the forbidden-phasor-wiring guard,
and (3) the Stage-1 "[DOMINATED]: selection is topological" verdict. All three are
surfaced for Grant's adjudication before any 2b run.

---

**Closing register reminder.** Nothing above is a result. This is the frozen
model definition — the circuit B *will* simulate — plus a base-tank
well-formedness sanity check. The (2,3)-selection and ⟨N⟩ outputs the eventual
2b run must produce are firewalled per the §FIREWALL: topological / dynamical /
scale-invariant, never tuned to m_e, and α / Q=1/α excluded from any selection
claim. This artifact lands *model definition only.*
