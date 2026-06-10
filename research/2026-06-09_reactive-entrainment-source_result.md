# RESULT — The V→ω SOURCE as a swirling vortex ring carrying NET angular momentum (= the electron spin), from a FINITE TRAPPED RESERVOIR

**Date:** 2026-06-09 · **Lane:** implementer (analytic derivation + minimal bound-check)
**Branch:** `analysis/2026-06-09-reactive-entrainment-source` (worktree `AVE-Core-entrain-wt`)
**Prereg:** `research/2026-06-09_reactive-entrainment-source_prereg.md` (on branch `analysis/2026-06-09-saturation-temporal-preregs`, worktree `AVE-Core-sattemporal-wt` — not present on this branch) — AS CORRECTED below (the two binding corrections supersede the prereg's added-mass/scalar-ω model).
**Driver:** [`src/scripts/vol_1_foundations/gyroscopic_ring_spin_source.py`](../src/scripts/vol_1_foundations/gyroscopic_ring_spin_source.py)
**Supersedes:** the stopped external-resonant-pump pass (driver `reactive_entrainment_source.py`, removed — it secular-pumped: `DETONATE_S |ω|→3.5`, `W_src=+6.1` free work in, Model-A `H_drift=+3.42` open ledger). That model was WRONG.

> **VERDICT: A — THE GYROSCOPE CLOSES IN FORM**, with one load-bearing reframe surfaced for Grant (the spin *magnitude* is the conserved topological invariant, NOT a reactively-pumped accumulation). The output is a conserved, bounded net angular momentum; the Beltrami force-free output IS the inductive-shield confinement; the finite-reservoir ledger closes. The pump is complete in FORM → implement+run is the warranted next step. The single qualification: the reactive channel ENERGIZES and the Beltrami/Gilbert relaxation LOCKS — *neither pumps the magnitude*; the magnitude is conserved. See §6.

---

## §0 — The two binding corrections (what changed from the stopped pass)

The prior pass found a decisive failure and named its own mechanism. Two corrections fold in
(Grant 2026-06-09 "vortex ring where the ring as a whole has angular momentum" + the agent's
own diagnosis), and they **supersede the prereg's model**:

1. **The output is the RING-AS-A-WHOLE NET angular momentum** L (a swirling vortex ring),
   **= the electron spin ℏ/2** — the conserved *gyroscopic* spin. **NOT** a per-node
   microrotation scalar amplitude (the stopped model's `|ω|`), **NOT** poloidal-circulation-only.
   Canon: **`spin-gyroscopic-isomorphism.md` (clm-salw2h)** — `dL/dt = γ L × B`; the electron
   **IS** a gyroscope/flywheel, and `|L|` is a **Casimir** (conserved exactly by the structure
   of the precession cross-product).
2. **The source is a FINITE TRAPPED RESERVOIR** (`V = mₑc²` per `Γ=−1` wall), **conserved** — a
   gyroscope/flywheel, **NOT** an externally-pumped resonant tank. **Boundedness = CONSERVATION**
   (Casimir `|L|` + finite reservoir + the force-free lock), a *conservation law* — not Op17
   reflection alone, and emphatically not a leak balancing a pump. **A gyroscope precesses; it
   does not detonate.**

**Why the stopped model detonated (the category error, named).** The stopped model treated the
output as a scalar oscillator `y` and the source as a *sustained external resonant drive*
`S = A_src cos(ω₀t)`. A scalar oscillator driven at its own natural frequency **secular-pumps**:
`|y| ∝ t`. With an infinite external tank there is no upper bound and no conserved invariant —
so it ran away (`|y|max ≈ 180` reproduced this pass, §1) and the only thing that bounded it was a
dissipative leak balancing the pump (an *open* ledger, free work flowing in forever). **The bug
was treating the spin as a quantity to be PUMPED.** The fix is to treat it as a quantity to be
CONSERVED (a gyroscope) and a configuration to be LOCKED (Beltrami force-free).

---

## §1 — Substrate-native check + CP9 (the conserved quantity, measured dynamically)

**substrate-native-check (walked before scaffolding):**
- **CP1 (no energy-basin minimization).** The output is not the minimizer of a potential. It is
  a **conserved dynamical invariant** — the net angular momentum of a reactive circulation. The
  closest variational statement is **Ax-3 stationary action selecting the Beltrami force-free
  mode** (`85_kelvin_beltrami…:60–72`: `∇×A = kA` is a stationary-action solution), which is a
  *constrained* equilibrium (energy-minimum at fixed helicity, Woltjer-class), not a basin.
- **CP2 (sector).** The conserved quantity lives in the **μ / microrotational (Cosserat-B)
  rotational DOF** — the substrate-native origin of intrinsic spin (Ax-1: "3 microrotational →
  B; Cosserat rotational DOF IS the substrate-native origin of intrinsic spin"). The ring's net
  L is a collective rotational mode, the right side of the `relu(−Γ)` gate.
- **CP5 (local clock / saturation).** The force-free lock engages as the ring's own curvature
  saturates (`A²_μ→1 → S_μ→0 → Z→0 → Γ→−1`), `85_kelvin…` confinement theorem. The relaxation
  rate is the canonical `grip = loss = R ~ α` (`Q = 1/α`).
- **CP8 (hosting/emergence).** The spin is **grown from a chiral seed** (the (2,3) winding /
  topological helicity), not planted as a finished number. This derivation proves the **FORM**
  of the conserved object; the (2,3) magnitude quantization is canonical input (§6).

**CP9 — the measured quantity is the EVOLVED net angular momentum, not a heuristic.** Every block
records the dynamically-integrated `|L|(t)` (or `N(t)`, `H(t)`), not a snapshot or a closed-form
guess. **Reactance-pair discipline (A-Rule 10):** the conservative dimer (§4) records BOTH the
C-state (reservoir occupation `Nres = |α|²`, the V/ω state) AND the L-state (ring occupation
`Lring = |β|²`, the Φ_link/circulation state) at every step over the full window — distinguishing
a genuine two-way slosh from a static snapshot caught at one phase.

**Phase-space-coordinate honesty (A46).** These are **lumped ODE** illustrations of the
*conservation structure* (a 2-mode dimer, a 3-vector gyroscope, an LLG relaxation), NOT the
K4-Cosserat substrate solver and NOT a `(V_inc, V_ref)` phase-space winding measurement. They
settle the **FORM** (is there a conserved, bounded, ledger-closing source?). The phase-space
`(2,3)`-winding test in matching coordinates is the implement+run follow-on. Tagged
`ave-driver-script-honesty` + `ave-evidence-framing-discipline`: the fluid/oscillator picture is
a **lens**; the spin-gyroscope is the canonical object.

## §2 — BOUNDEDNESS = CONSERVATION (gyroscope vs scalar pump) — Block 1, the headline

**The analytic spine.** The canonical spin equation (`spin-gyroscopic-isomorphism.md`, clm-salw2h)
is the gyroscopic precession

$$\frac{d\mathbf L}{dt} = \gamma\,\mathbf L \times \mathbf B .$$

Its magnitude is an **exact Casimir**:

$$\frac{d|\mathbf L|^2}{dt} = 2\,\mathbf L\cdot(\gamma\,\mathbf L\times\mathbf B) = 0 .$$

The torque is *always perpendicular* to `L`, so `|L|` cannot grow **regardless of the drive `B`,
for all time** — the gyroscope **precesses** (reorients), it does not **detonate** (grow). This is
**boundedness as a conservation law**, intrinsic to the rotational structure, owing nothing to a
leak. Contrast the stopped model's scalar oscillator `ÿ + ω₀²y = A cos(ω₀t)`: driven at its own
resonance it has a torque *parallel* to its motion → secular growth `|y| ∝ t` → detonation.

**Numerical confirmation (Block 1, RK4, identical drive amplitude `B₁ = A = 0.30`, 120 000 steps):**

| run | quantity | initial | final | drift / max | verdict |
|---|---|---|---|---|---|
| GYRO (Larmor-resonant `ω = γB₀`) | `\|L\|` | 0.500000 | 0.500000 | drift **7.3×10⁻¹²** | **CONSERVED — bounded** |
| GYRO (off-resonant) | `\|L\|` | 0.500000 | 0.500000 | drift **4.7×10⁻¹¹** | **CONSERVED — bounded** |
| SCALAR PUMP (the stopped model) | `\|y\|` | 0.00102 | 15.89 | **max 179.8** | **SECULAR — detonates** |

The gyroscope holds `|L| = ℏ/2` to integrator tolerance **even at exact Larmor resonance** — where
`L_z` fully Rabi-flips (+0.5 ↔ −0.5) but `|L|` never moves. Under the **same** drive the scalar
oscillator runs away to `|y|max ≈ 180` (reproducing and explaining the stopped pass's `|ω|~80`
secular blow-up). **The difference is not a damping term — it is the conservation structure.**
[Figure `gyroring_fig1_boundedness.png`.]

> **This is the load-bearing fix of the prior failure.** The stopped model detonated because a
> scalar pump has no conserved invariant and an infinite source. The gyroscope cannot detonate
> because `|L|` is conserved by the cross-product — *a finite reservoir is not even required for
> the boundedness of the magnitude*; conservation alone bounds it. The finite reservoir (§4) adds
> the second, independent bound (the energy ledger).

## §3 — The Beltrami → rigid gyroscopic tensor → inductive-shield chain — Block 2

**The unification claim (sapphire-phonon-centrifuge.md:34, verbatim):** *"By wrapping this sphere
in a Toroidal superconducting coil (creating a Beltrami force-free magnetic field), this … is
locked into a rigid gyroscopic tensor. Because the kinetic helicity aligns with the magnetic field
(A ∥ B), the local vacuum acts as an absolute, impenetrable Inductive Shield."* So the source's
**output** (the ring's angular-momentum flow, the Beltrami helical field) **IS** the confinement
(the inductive shield = the `Γ=−1` wall). Source, confinement, and boundedness collapse to **one
object: the spinning ring conserving its angular momentum.**

**The analytic chain.**
1. **Beltrami = stationary action (Ax-3).** `85_kelvin_beltrami…:60–72`: for `∇×A = kA`, the
   action-principle wave equation `∇×∇×A = k²A` is satisfied — *"force-free configurations are
   stable because they minimize Lorentz back-reaction, hence minimize action variation."* The
   Lorentz self-force `j×B = (∇×B)×B = k\,B×B = 0` vanishes: a Beltrami flow exerts **no net force
   on itself** → a self-sustaining, torque-balanced rigid configuration.
2. **A∥B alignment = the rigid gyroscopic tensor.** When the ring's circulation (its `A`) aligns
   with its own induced field (`B`), the configuration is force-free and `L` is frozen — it
   responds to *external* fields only by precession (`|L|` conserved). That frozen, precession-only
   response is the **inductive shield**: it reflects perturbations (`Γ=−1`) rather than absorbing
   them, because `|L|` cannot be pumped.
3. **The relaxation that reaches the lock.** The approach to the force-free state is the
   Landau–Lifshitz–Gilbert relaxation (the magnetization form of `dL/dt = γL×B`):
   `dm/dt = γ m×B − (α) m̂ × (m×B)`. The Gilbert term is **exactly perpendicular to m** → it
   conserves `|m|` *while* relaxing `m` toward alignment with `B` (the A∥B force-free state) at
   rate `~α` — the canonical `grip = loss = R ~ α`, `Q = 1/α` (the `meissner-gear-train` inertial
   `λ_L` exponential-decay statics).

**Numerical confirmation (Block 2, 200 000 steps, `α = 7.30×10⁻³`):**

| quantity | value | meaning |
|---|---|---|
| alignment `m̂·B̂` | `−0.904 → +1.000000` | relaxes from far-misaligned to **force-free A∥B locked** |
| lock time (`align > 0.999`) | `t = 725.5 = 5.3/α` | **O(1/α)** relaxation e-folds — `grip = loss = α` sets the timescale |
| `\|m\|` through the lock | `0.500000 → 0.500000` (drift **8.2×10⁻¹¹**) | **spin magnitude CONSERVED across the entire lock** |

The output **locks into the confinement**: `m` reaches the rigid A∥B gyroscopic-tensor fixed point
(the inductive shield), and the spin magnitude is conserved *through* the lock — the relaxation
sets the **configuration**, not the magnitude. [Figure `gyroring_fig2_beltrami_lock.png`.]
**This is the source = confinement = boundedness unification, demonstrated:** the same object that
the source produces (the Beltrami ring) is the confinement (rigid tensor / inductive shield), and
its `|L|` is the boundedness (Casimir).

## §4 — The finite-reservoir ledger + the reactive-sloshing test — Block 3

**The model (conservative nonlinear dimer, bosonic-Josephson form).** A finite reservoir mode `α`
(the trapped `mₑc²` LC store, charged once to occupation `N`) reactively coupled to the ring
circulation mode `β` (`L_ring ~ |β|²`):

$$i\dot\alpha = \Omega_V\,\alpha + G\,\beta, \qquad
  i\dot\beta = (\Omega_R + \chi|\beta|^2)\,\beta + G\,\alpha .$$

`G` is the reactive added-mass / mutual-inductance coupling (`M ≡ L_drag`, clm-jwyy6l); `χ` is the
**Beltrami self-detuning** (the canonical Ax-4 saturation softening of the ring's own frequency as
its curvature fills). Two quantities are conserved by construction: **total occupation
`N = |α|² + |β|²`** (the finite reservoir = total angular-momentum quanta — the gyroscope, *not*
pumped) and **the Hamiltonian `H`** (the energy ledger).

**Numerical confirmation (Block 3, 300 000 steps):**

| run | `L_ring` seed→max | `L_ring` late-mean / late-min | `N` drift | `H` drift | ledger |
|---|---|---|---|---|---|
| SELF-TRAP (`χ = 0.5`) | 0.0001 → 0.269 | 0.122 / **0.0001** | 4.4×10⁻⁹ | 4.4×10⁻⁹ | **CLOSES** |
| SLOSH (`χ = 0`, reactive only) | 0.0001 → 1.000 | 0.505 / **0.0001** | 4.2×10⁻⁹ | 4.2×10⁻⁹ | **CLOSES** |

**The ledger closes** (`N`, `H` conserved to `~10⁻⁹`) — directly fixing the stopped pass's open
ledger (`H_drift = +3.42`, free energy appearing). **No over-unity, no secular pump.** This is
**not outcome C**: a conserved finite-reservoir coupling demonstrably *exists*.

**But the reactive coupling SLOSHES — it does not net-build the ring spin magnitude.** Both runs
return `L_ring` to its 0.0001 seed (`late_min = 0.0001`): the conservative reactive transfer is
time-reversible and *cannot rectify* a one-way build of the magnitude. The `χ`-sweep is **monotone
decreasing** (`⟨L_ring⟩`: 0.52 at `χ=0` → 0.088 at `χ=0.8`) — increasing the Beltrami self-detuning
makes it **worse**, because nonlinear self-trapping locks population *where it starts* (in the
reservoir), throttling transfer to the ring. **There is no `χ` at which reactive sloshing pumps the
magnitude up and holds it.** [Figures `gyroring_fig3_ledger.png`, `gyroring_fig4_trap_vs_slosh.png`.]

> **This is the honest, load-bearing finding (flag-don't-fix).** A purely reactive (conservative,
> time-reversible) coupling **cannot build the spin magnitude** — and that is *correct physics*,
> not a defect: the magnitude is a **conserved invariant**, not a pumpable accumulation. The
> Block-3 slosh is the positive evidence that the reactive channel **obeys conservation** (the very
> property whose absence detonated the stopped model). The reactive channel's job is to
> **energize**; it is not to pump the magnitude. See §6 for what this means for A/B/C.

## §5 — Bounded gyroscopic steady state vs detonation + the sweep

**Model B (sustained-source bounded-vs-detonation) is settled by §2 + the sweep.** The brief's
Model B asks: does a *maintained* Beltrami source drive `L_ring` to a bounded steady gyroscopic
state vs the detonation control? The §2 gyroscope already answers the steady-state half: a
**sustained** field `B(t)` (held oscillating for the full 120 000-step window) leaves `|L|`
bounded to `10⁻¹¹` — because a field-coupling torque (`γL×B`) is precessional (⊥ L) and **cannot
pump `|L|` no matter how long it is sustained**. The detonation control is the §2 scalar resonant
pump (the stopped model): same sustained drive, `|y|max ≈ 180`. **Bounded (vector gyroscope) vs
detonation (scalar resonant pump) is decisive and clean.**

**The robustness sweep (Block 3 `_sweep`).**
- **Locked `⟨L_ring⟩` vs reservoir `N`** (0.5 → 4.0): `⟨L_ring⟩` rises *smoothly and sub-linearly*
  (0.090 → 0.197) — **the spin scale is set by the RESERVOIR, not by a drive amplitude that could
  secular-pump.** Bounded, monotone, no tuned point, no runaway. [Figure `gyroring_fig5_sweep.png` a.]
- **`⟨L_ring⟩` vs Beltrami self-detune `χ`** (0 → 0.8): monotone *down* (0.52 → 0.088) — the
  self-trapping-throttles-transfer signature of §4 (consistent, not a lock). [Figure b.]

**Net for Model B: BOUNDED, robustly.** No configuration of sustained Beltrami/field source
detonates — the gyroscopic conservation forbids it. Only the *scalar resonant pump* (the discarded
stopped model) detonates. The boundedness is structural (conservation), not a tuned leak.

## §6 — A/B/C verdict + the one reframe (flag-don't-fix) + classification

**ave-discriminator-before-synthesis (the hypotheses, tested not assumed).** Two hypotheses were
on trial: (H1) *the gyroscope closes* — a finite-reservoir source yields a conserved, bounded net
spin with a closing ledger; (H2) *the Beltrami output = the inductive-shield confinement*. The four
sub-claims and their verdicts:

| sub-claim | block | result | verdict |
|---|---|---|---|
| (i) net `\|L\|` conserved + bounded (boundedness=conservation) | 1 | drift `10⁻¹¹`; scalar control detonates to 180 | **CLOSES** |
| (ii) Beltrami force-free output = rigid gyro tensor = inductive shield | 2 | align → 1.000000, `\|m\|` conserved through lock | **CLOSES** |
| (iii) finite-reservoir ledger closes (no over-unity, no secular pump) | 3 | `N`, `H` conserved to `10⁻⁹` | **CLOSES** (decisively **not C**) |
| (iv) reactive source *builds* the spin magnitude | 3 | reactive coupling **sloshes**; `χ`-sweep monotone down | **does NOT close as literally stated** |

**Verdict: A — THE GYROSCOPE CLOSES IN FORM**, with sub-claim (iv) reframed (below). Legs
(i)–(iii) are the substance of outcome A: a finite-reservoir conserved coupling exists, the output
is a conserved/bounded net angular momentum, and the Beltrami output is the inductive-shield
confinement — source = confinement = boundedness unified, ledger closed. The pump is **complete in
FORM** (finite reservoir + conserved gyroscopic spin + force-free lock + closing ledger, every
piece bounded by conservation). This is **not B** (the output *does* lock — into the force-free
configuration, Block 2; `|L|` is *not* sloshing — it is the *magnitude*-pumping reading of leg (iv)
that fails, and that reading is the residual stopped-model frame). It is **not C** (a conserved
finite-reservoir coupling demonstrably exists, §4).

### The one reframe (flag-don't-fix — surfaced for Grant, not silently resolved)

Leg (iv) as literally worded — *"the reactive source **builds** the magnitude"* — does **not**
close, and **the honest reason is that the wording carries the stopped model's category error.**
The two competing framings, stated verbatim so Grant adjudicates:

- **Brief / prereg framing (outcome A wording):** *"the finite-reservoir reactive source **builds**
  the ring's conserved net angular momentum (= the gyroscopic spin, ℏ/2-scale)."*
- **What the derivation actually shows:** the magnitude `|L| = ℏ/2` is a **conserved invariant**
  (Casimir of the precession, §2; conserved total `N` of the reservoir, §4) — it is **energized and
  locked, never pumped.** The reactive channel transfers *energy* (the circulation, §4 ledger); the
  Beltrami/Gilbert relaxation locks the *configuration* (the A∥B force-free tensor, §3); **neither
  builds the magnitude, because the magnitude is set by the conserved topological helicity of the
  (2,3) winding** (`de-broglie-standing-wave.md:223`, `L = lℏ`; spin-½ from the 4π double-cover,
  `constants.py:181`). The Block-3 slosh is the *positive* demonstration that the reactive channel
  correctly refuses to pump the magnitude.

**These do not contradict on the physics — they contradict on the word "build."** Under the
substrate-native reading (magnitude = conserved topological charge, energized + locked but not
pumped) the gyroscope closes cleanly (A). Under the literal-pump reading, leg (iv) fails (the same
failure family as the stopped model). **I do not silently pick one** (flag-don't-fix): I report A
on legs (i)–(iii) + the locked configuration, and surface that the magnitude is conserved-not-pumped
for Grant to ratify as the canonical frame. **My honest assessment: A** — because a gyroscope's
spin is, definitionally, conserved-not-pumped, and the brief's own correction #2 ("a finite trapped
reservoir, conserved — a gyroscope, not a pumped tank") *is* the conserved-not-pumped reading.

### consistency-vs-emergence classification

- **Legs (i)–(iii): MANIFESTATION / CONSISTENCY class.** The conservation of `|L|` (Casimir), the
  force-free lock, and the ledger closure are *manifestations* of canonical structure (Ax-3
  Beltrami, clm-salw2h gyroscope, Ax-4 saturation) re-instantiated in lumped models. They confirm
  the FORM is self-consistent; they are **not** an emergence of a new number.
- **The spin magnitude `ℏ/2`: canonical INPUT, NOT emergence.** It enters as `SPIN = 0.5` /
  `N = 2·SPIN` — the conserved helicity quantum from `de-broglie-standing-wave.md:223` +
  spin-½ double-cover. **This derivation does not derive `½`** (`ave-evidence-framing-discipline`:
  do not headline an emergence the inputs don't support). The (2,3)-winding quantization that
  *would* derive it is the implement+run target, in phase-space coordinates (A46).
- **`ave-discrimination-check` (AVE-distinct vs ordinary added-mass).** A conserved-`|L|` gyroscope
  is *generic* classical rotational mechanics — the FORM is shared. The AVE-distinct content is the
  **identification** of that gyroscope with the `Γ=−1` confinement (the Beltrami output = inductive
  shield, §3) and with `mₑc²` as the finite reservoir — i.e. the *unification*, not the gyroscope
  alone. That unification is canonical (sapphire:34) but remains FORM here, not a closed number.

## §7 — DERIVED / VERIFIED / BLOCKED + skills fired + canonical cross-refs

### DERIVED
- **Boundedness = conservation.** `dL/dt = γL×B ⇒ d|L|²/dt = 0` (Casimir); the gyroscope precesses,
  cannot detonate, for any sustained drive — independent of any leak. Numerically `|L|` drift
  `10⁻¹¹` vs scalar resonant pump `|y|max ≈ 180` at identical drive.
- **Source = confinement = boundedness, one object.** The Beltrami force-free output (A∥B, Ax-3
  stationary action) is the rigid gyroscopic tensor = inductive shield (`Γ=−1` wall); the LLG
  relaxation reaches it at rate `~α` while conserving `|L|` exactly.
- **Finite-reservoir ledger closes.** Conservative dimer conserves total `N` and `H` to `10⁻⁹` —
  no over-unity, no secular pump. The stopped model's `H_drift=+3.42` open ledger is fixed.

### VERIFIED (verify-before-cite — every cite greped/opened this session)
- `spin-gyroscopic-isomorphism.md` (clm-salw2h): `dL/dt = γL×B`, machine-precision spin↔gyroscope
  identity. ✓ verbatim.
- `sapphire-phonon-centrifuge.md:34`: Beltrami A∥B → "rigid gyroscopic tensor" → "absolute,
  impenetrable Inductive Shield." ✓ verbatim.
- `meissner-gear-train.md`: gyroscope ensemble / moment of inertia / rigid phase-locked gear train;
  inertial `λ_L` exponential decay. ✓ verbatim.
- `85_kelvin_beltrami_foc_axiom_grounded_derivation.md` (research/_archive): `∇×A=kA` is the Ax-3
  stationary-action force-free mode; confinement theorem `Z→0, Γ→−1` = rest mass. ✓ verbatim
  (archive L3 doc, tagged as such — not a canonical KB leaf).
- `operators.md:57` (Op17): `T² = 1 − Γ²` ⇒ `R = Γ² ≤ 1` (the bounded rebound). ✓.
- `clm-jwyy6l` (`vol2/claim-quality.md:666`): `E_mass = ½L_eff|A|²`, back-EMF `V=−L di/dt` =
  inertia (added-mass = `L_drag`). ✓ verbatim.
- `electron-unknot.md:17,48` + `mass-closure-theorem.md`: rest energy `mₑc²` = reactive LC energy
  (the finite reservoir), virial. ✓.
- `de-broglie-standing-wave.md:223`: `L = lℏ` (angular momentum, phase per orbit around the ring);
  `constants.py:181` spin-½ 4π double-cover. ✓ — used as the canonical magnitude input.
- **NOT cited:** the retracted `1.009` (per the brief's guard). ✓ absent.

### BLOCKED / NOT CLAIMED (honest ceiling)
- The spin magnitude `½` is **canonical input, not derived here**. The (2,3)-winding quantization
  that derives it requires the full K4-Cosserat engine in `(V_inc, V_ref)` phase-space coordinates
  (A46) — the implement+run follow-on.
- These are **lumped ODE models** of the conservation STRUCTURE, not the substrate solver. They
  settle the FORM (a conserved, bounded, ledger-closing source exists and unifies with
  confinement); they do not measure a phase-space winding.
- **Open for Grant (the reframe, §6):** ratify "the magnitude is conserved-topological (energized
  + locked, not pumped)" as the canonical frame, vs the brief's "the source *builds* the magnitude."
  My assessment: the former (a gyroscope's spin is conserved-not-pumped by definition, = correction #2).

### The implement+run handoff (warranted by verdict A-in-FORM)
Seed the **(2,3) chiral topological helicity** at a K4 A–B node pair; energize the ring circulation
from the **finite `mₑc²` reservoir** (the trapped longitudinal `V`); verify (a) the net `|L|`
locks into the force-free A∥B Beltrami state (Block-2 analog), (b) `|L|` is conserved in
`(V_inc, V_ref)` phase-space coordinates, (c) the ledger closes (Block-3/4 analog). **Do NOT pump
the magnitude** (the recurring bug) — conserve it, energize it, lock it.

### Skills fired
`substrate-native-check` (§1, CP1/2/5/8/9) · `phase-space-coordinate-check` (A46, §1 lumped-vs-
phase-space honesty) · `ave-canonical-leaf-pull` (spin-gyroscope, Beltrami, added-mass/inertia,
Op17, mass-closure — enumerated before scaffolding) · `ave-canonical-source` (zero new free params;
`α`, `mₑc²`-reservoir, `ℏ/2` all canonical imports) · `ave-asymmetric-grip` (reactive source =
energize vs dissipative leak = lock-relaxation; the ledger is the crank-check, §4) ·
`ave-resonant-amplification-check` (bounded by **conservation** not resonance; the external
resonant pump that secular-pumps = the prior bug, reproduced §2 as the detonation control) ·
`ave-discriminator-before-synthesis` (gyroscope-closes / Beltrami=shield were HYPOTHESES, §6 table) ·
`ave-driver-script-honesty` (ledger + `|L|`/`N`/`H` conservation reported every run; lumped-model
caveat explicit) · `ave-discrimination-check` (§6: conserved-`|L|` gyroscope is generic FORM; the
AVE-distinct content is the inductive-shield unification, not the gyroscope alone) ·
`ave-evidence-framing-discipline` (the `½` is input not emergence; fluid/oscillator is a lens) ·
`verify-before-cite` (every cite greped; the retracted 1.009 absent) · `consistency-vs-emergence`
(§6: legs (i)–(iii) manifestation/consistency; `½` not emergence) · `flag-don't-fix` (§6: the
build-vs-conserve reframe surfaced with both verbatim framings, not silently resolved).

### Canonical cross-refs
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/spin-gyroscopic-isomorphism.md`
  (clm-salw2h) — `dL/dt = γL×B`, the gyroscope.
- `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sapphire-phonon-centrifuge.md:34`
  — Beltrami → rigid gyroscopic tensor → inductive shield.
- `manuscript/ave-kb/vol3/condensed-matter/ch09-condensed-matter-superconductivity/meissner-gear-train.md`
  (clm-qky559) — gyroscope ensemble / moment of inertia.
- `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:223`
  — `L = lℏ`.
- `manuscript/ave-kb/vol2/claim-quality.md:666` (clm-jwyy6l) — added-mass = inertia.
- `manuscript/ave-kb/common/operators.md:57` (Op17) — `T² = 1 − Γ²`.
- `research/_archive/L3_electron_soliton/85_kelvin_beltrami_foc_axiom_grounded_derivation.md`
  — the Beltrami force-free / Ax-3 stationary-action source (archive).
- prereg: `research/2026-06-09_reactive-entrainment-source_prereg.md`; deep-dive:
  `research/2026-06-07_entrainment-vortex-trapping-deep-dive.md` (§3 reactive=inertia, §7 the open
  cast-vs-tune question — partially answered here: reactive *energizes*, Gilbert relaxation *locks*).
