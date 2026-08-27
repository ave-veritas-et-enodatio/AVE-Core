# ARC RECORD — the VIRTUAL-NEUTRAL boundary: is the electron's wall a level-set in real space, or a balance locus in port space? (2026-08-26)

**Status: NEW ARC, WALK-GRADE, UNAUDITED — except §2, which is MEASURED and
independently reproduced. Nothing here is a claim, a ruling, or a supersession.**
The arc does **not** supersede `def-vyvsn1`; only Grant rules that. It
**requires an adversarial audit before any part of it reaches canon** — the
audit charter is §10, the kill conditions are §11, and the routing items are
`_orchestration/open-items/2026-08-26-virtual-neutral-register-move.md` and
`_orchestration/open-items/2026-08-26-device-circuit-models-165-correction.md`.

**GRADE TAGS.** Every statement below carries one:
`[MEASURED]` computed on the shipped operator, reproduced in this arc, numbers in §2/Appendix ·
`[CANON]` verified canon, file:line quoted · `[WALK]` this arc's reading, un-audited ·
`[OPEN]` what the arc raises and does not answer.

---

## §0 — Sector declaration (before any physics word)

| | |
|---|---|
| **MODE** | static / stationary. No drive, no pump, no time-dependence is invoked anywhere in §2. |
| **REGIME** | linear-in-the-scatter. The junction reduction is exact for **any** fixed per-port admittances; saturation enters only through the value of `Y`, never through the algebra. |
| **PHASE-STATE** | **both**, deliberately. §2.1–§2.3 hold at **cold vacuum** (`S=1`, all `Y` equal) *and* at arbitrary grading up to 4 decades. §2.4 is the **saturated-shell** arithmetic at canon's own named yield level-set. §2.5 is the **sub-saturated A1 core** at `A=√α`. |
| **SECTOR** | §2.1–§2.4 are **port-space / junction-scatter** — sector-agnostic linear algebra on the shunt reduction, which is the same operator whichever channel rides it. §2.5 is explicitly the **A1 longitudinal / bulk-dilatation** branch. The **T2 Cosserat** channel is *named* but never computed here. |
| **Does the engine carry this DOF?** | Yes for the scatter (`vacuum_varactor_scatter.py`, shipped, run in this arc). **No** for the composed map `M = C · blockdiag(S)` — see §4 `[OPEN]`. |
| **Cold vs saturated** | The load-bearing surprise of §2.4 is precisely that a **uniformly** saturated shell is *indistinguishable* from cold vacuum at the junction. Any statement that omits "uniform vs graded" is underspecified. |

**Vocabulary fence, stated up front.** "Virtual neutral" is used here in its
**power-engineering** sense: the node of a Wye (star) connection that sits at
zero potential *because the phasor sum of the leg currents cancels*, with no
conductor to ground. It is **not** the hollow-vortex "balance shell" (§3
caution 2), and it is **not** a new coinage — canon already writes
"virtual-neutral surface" once, and "virtual ground" once, both cited in §5.

## §1 — The reframe, and what "virtual neutral" means on the schematic

**Provenance — Grant, verbatim (2026-08-26):**

> *"It makes sense to me that the 'boundary' is the virtual neutral, and isn't
> resolvable in 'real space' but like only exist is any sense of a discrete
> form in phase space. What does the equivalent circuit EE model/schematic
> say?"*

**And the directive governing the arc — Grant, verbatim:**

> *"I think we need to be ok challenging past rulings that don't have hard math
> tied to them."*

### 1.1 What the schematic actually is `[CANON]`

Every interior node of the chiral srs net is a **three-connected shunt
junction**. Canon writes this in power-engineering words already, without
hedging:

> *"each interior node (e.g., carbon, nitrogen, oxygen) is a 3-connected WYE
> junction — a three-phase node. A bond between two interior atoms (a
> 'heavy-heavy' bond) represents a **balanced three-phase system**"*
> — `manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md:110`

The shipped operator is the admittance-weighted shunt reduction
(`src/ave/solvers/vacuum_varactor_scatter.py:28-34, :156-185`):

```
V_u = 2 (Σ_j Y_j V_j^inc) / (Σ_k Y_k)          [the node voltage]
S_ij = 2 Y_j / (Σ_k Y_k) − δ_ij                [the scatter]
```

### 1.2 The reframe in one sentence `[WALK]`

Grant's move is to stop asking *"at what radius does `S(A)` hit threshold?"*
and instead ask *"where does the phasor sum `Σ_j Y_j V_j^inc` vanish?"* — i.e.
to treat the boundary as the locus where the Wye node sits at its own virtual
neutral. On such a node the star point is at zero volts **with no conductor to
ground and no saturation**: the leg phasors cancel each other. That is the
`V_u = 0` branch of the reduction above.

### 1.3 Why "not resolvable in real space" is the right instinct `[WALK]`

An amplitude level-set is a **real-space** object: `A(r) = A_yield` has a
radius, and you can point at it. A virtual neutral is a **port-space** object:
it is a condition on the *relative phases and admittances of the legs meeting
at one node*, not on any scalar field evaluated at a point. The set of
`V^inc` vectors satisfying it is a **hyperplane through the origin** of the
port space — a discrete-in-form object (a codimension-1 subspace with a
definite dimension `z−1`) that has no radius at all.

**This is the whole content of the reframe**, and §2 shows the schematic
answers it *exactly*, with no approximation and no fitted parameter — and §3
shows immediately why the exactness is a trap.

## §2 — ★ THE MEASURED CORE

**Reproduction discipline.** Every number in this section was **recomputed in
this arc**, from the shipped operator, on a fresh worktree at `a3f4fef7`, and is
**not** inherited from the dispatch brief. The script and its verbatim output
are in Appendix A. Where the brief and the reproduction disagree, the
reproduction wins and the disagreement is recorded (§2.4.1).

### 2.1 The junction spectrum theorem `[MEASURED]`

**Statement.** For `S = (2/ΣY)·𝟙·Yᵀ − I` and **any** per-port admittances
`Y > 0`, the spectrum is exactly:

| eigenvalue | multiplicity | eigenspace | circuit reading |
|---|---|---|---|
| `+1` | 1 | `span{(1,1,…,1)}` — all ports equal | the **COMMON / breathing** mode sees an **OPEN** |
| `−1` | `z−1` | `{v : Σ_j Y_j v_j = 0}` — the **BALANCED** subspace | the **DIFFERENTIAL** modes see a **SHORT** |

**Proof sketch.** `S = (2/ΣY)·𝟙 Yᵀ − I` is rank-one plus a multiple of the
identity. `𝟙 Yᵀ` has one nonzero eigenvalue `Yᵀ𝟙 = ΣY` with right eigenvector
`𝟙`, and a kernel of dimension `z−1` equal to `{v : Yᵀv = 0}`. So `S𝟙 = 2𝟙 − 𝟙 = +𝟙`,
and `Sv = 0 − v = −v` for every `v` in the kernel. Nothing about the *values*
of `Y` enters. **Saturation grading rotates the EIGENVECTORS and never the
EIGENVALUES.**

**Reproduced.** `n = 3` and `n = 4`, three loadings each — cold-uniform
(`S=1`), random 4-decade grading, and one bond at `1e6` — eigenvalue residual
vs the exact target `≤ 2.220e-16`; `|S·𝟙 − 𝟙| ≤ 2.220e-16`; balanced-vector
residual `|S·v + v|/|v| ≤ 2.095e-16`.

### 2.2 The trace identity `[MEASURED]`

**Statement.** `Σ_i S_ii = 2 − z` **exactly**, for any admittances. Immediate
from §2.1 (`trace = sum of eigenvalues = (+1) + (z−1)(−1)`), and equally from
the closed form (`Σ_i [2Y_i/ΣY − 1] = 2 − z`).

**Reproduced.** 2000 random 6-decade draws per `z`:

| `z` | target trace | max deviation, 2000 draws |
|---|---|---|
| 2 | `+0` | `4.441e-16` |
| 3 | `−1` | `5.551e-16` |
| 4 | `−2` | `8.882e-16` |

**Why it bites.** At `z = 3` the three diagonal reflections are constrained to
sum to `−1`. Driving one port to `Γ = −1` by grading therefore **forces the
other two to sum to 0** — at least one of them must be non-negative. **`Γ = −1`
on all three ports of an srs node is ARITHMETICALLY UNREACHABLE by any
saturation grading whatsoever.** This is a conservation law on the diagonal,
not a numerical limit; no kernel, no floor, and no operating point can evade it.

Cold-uniform closed form, reproduced over `z ∈ {2,3,4,6,12}`:
`Γ_port = 2/z − 1 = (2−z)/z`, which canon already writes at
`manuscript/ave-kb/common/relational-cancellation-identity.md:268` `[CANON]`.

### 2.3 The balanced node is a MIRROR, with no saturation `[MEASURED]`

**Statement.** If `Σ_j Y_j V_j^inc = 0` then `V_u = 0`, and therefore
`V_p^ref = V_u − V_p^inc = −V_p^inc` on **every port simultaneously** — a
`Γ = −1` mirror on all `z` ports at once.

**Reproduced.** 2000 draws per `n`, `Y` spanning 4 decades, `V^inc`
unit-normalised and constructed to satisfy the balance condition exactly:

| `n` | `max‖v_ref + v_inc‖` | `max|V_node|` |
|---|---|---|
| 3 | `2.498e-16` | `2.372e-16` |
| 4 | `2.220e-16` | `2.060e-16` |

**All admittances finite. All bonds sub-yield. Axiom 4 never invoked.** The
mirror is produced by *cancellation*, not by *stiffness*.

*(Reproduction note: an un-normalised `V^inc` inflates the absolute residual to
`~1e-12` purely through the dynamic range of the constructed vector. That is
conditioning, not physics; the normalised figures above are the honest ones.)*

### 2.4 Level-set arithmetic at canon's own named wall `[MEASURED]` + `[CANON]`

Canon names the wall nodes and their kernel value:

> *"the ring of open markers is the set of **19 wall nodes at yield (A>0.9,
> S→0.045)** — the `Z_core→0`, `Γ=−1` short-circuit boundary derived above
> rendered on the real carrier"*
> — `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:54`

Evaluating the shipped scatter on a `z=3` node with `Y = Y₀/√S` per bond:

| bond loading (S per bond) | `Γ` on each port | most negative `Γ` |
|---|---|---|
| **cold vacuum** `[1, 1, 1]` | `−1/3, −1/3, −1/3` | `−0.333333` |
| **uniformly saturated shell** `[0.045, 0.045, 0.045]` | `−1/3, −1/3, −1/3` | `−0.333333` |
| 2 saturated, 1 cold `[0.045, 0.045, 1]` | `−0.095895, −0.095895, −0.808210` | `−0.808210` (at the **cold** port) |
| 1 saturated, 2 cold `[0.045, 1, 1]` | `+0.404234, −0.702117, −0.702117` | `−0.702117` (at a **cold** port) |

**★ A UNIFORMLY SATURATED SHELL REFLECTS EXACTLY LIKE COLD VACUUM.** Not
approximately — the measured difference is `0.000e+00`, bit-identical, because
the common factor `Y₀/√S` cancels identically through the ratio `2Y_j/ΣY`.
**The mirror is the GRADIENT at the shell edge, never the saturation level.**

Canon banks this same cancellation independently, at
`relational-cancellation-identity.md:265` (instance 1, *"`Γ_end = −1/3` exactly,
at ALL orders … max deviation 5.6e-17"*) and `:268` (instance 3, *"a uniform
impedance scale cancels in `Γ = (2−z)/z`"*) `[CANON]`. That leaf's own status
is **PROPOSED** and it carries an explicit fence — *"must NEVER be cited as a
step in deriving any value"* (`:229`) — so it is cited here as **corroboration
of an independently-measured algebraic fact**, never as a derivation step.

**Best achievable with the SHIPPED kernel floors** (`A_cap = 0.99`,
`S_min = 0.05` → `S(A_cap) = 0.141067`): the optimum is 2 bonds floored-saturated
+ 1 cold, read at the cold port, giving **`Γ = −0.683793`**. Un-floored ideal
kernel, same configuration:

| `A` | `S = √(1−A²)` | best `Γ` |
|---|---|---|
| `1 − 1e-2` | `1.411e-1` | `−0.683793` |
| `1 − 1e-3` | `4.471e-2` | `−0.808770` |
| `1 − 1e-6` | `1.414e-3` | `−0.963088` |
| `1 − 1e-9` | `4.472e-5` | `−0.993335` |
| `1 − 1e-12` | `1.414e-6` | `−0.998812` |

Reaching `|Γ| = 0.9988` on **one** port requires `A = 1 − 10⁻¹²` — and by §2.2
the other two ports must still sum to `+0.9988`.

#### 2.4.1 ⚑ A correction to the dispatch brief `[MEASURED]`

The brief supplied *"Two saturated one cold: −0.702. One saturated two cold:
−0.808."* **These two labels are transposed.** The reproduction gives
2-saturated-1-cold → `−0.808210` and 1-saturated-2-cold → `−0.702117`. The
number **set** is exactly right; the assignment is not.

Two independent cross-checks confirm the reproduction's assignment:
(i) monotonicity — more saturated bonds raise `ΣY` faster than they raise `Y_p`
at the cold port, so `Γ_cold = 2Y_cold/ΣY − 1` must be *more* negative with two
saturated bonds than with one; (ii) the shipped-floor best case `−0.683793`
arises from the **2-saturated-1-cold** configuration, and the ideal-kernel
sweep at `A = 1−1e-3` (`S = 0.0447 ≈ 0.045`, two saturated) returns `−0.808770`
— the `−0.808` family. Any downstream document that inherited the brief's
assignment must be corrected.

### 2.5 The A1 branch is TRANSPARENT at the stated operating point `[MEASURED]` + `[CANON]`

Canon's bulk-branch impedance route is `Z_eff = Z₀√S`, `Γ = (Z−1)/(Z+1)`
(`src/ave/core/crystal_engine.py:463, 477-478` — *"`Z_eff = Z0·√S → 0` … `Γ → −1`"*).
`def-vyvsn1` puts the electron's **A1 mass core** at `A = V_yield/V_snap = √α`.
Evaluating canon's own formula at canon's own operating point:

| | value |
|---|---|
| `A = √α` | `0.085424543132` |
| `S(√α)` (shipped kernel and ideal kernel agree — no floor is active) | `0.996344642898` |
| `Z_eff = √S` | `0.998170648185` |
| **`Γ_bulk`** | **`−9.155133056e-04`** |

**That is a 0.09% reflection. It is not a mirror; it is a window.**

Three cross-checks, all `[CANON]`:

1. `def-vyvsn1`'s own open-ambiguity flag already states the physics:
   *"the electron's A1 mass core operates at strain `A = V_yield/V_snap = √α` …
   **sub-saturated** (`S(√α) = √(1−α) ≈ 0.996`), which is why the mass channel
   does not run away"* — `manuscript/ave-kb/common/vocabulary-register.md:757`.
   The measured `S = 0.996344642898` **is** canon's `≈ 0.996`. The arc's number
   is not news to canon; it is canon's own number, carried out to `Γ`.
2. `pair-production-axiom-derivation.md:103` says the same in prose:
   *"deeply **sub-saturated**. This is *why* the electron binds: the `S→0`
   varactor runaway never fires on the mass channel."*
3. The engine acceptance suite's own Fresnel step reproduces:
   `Γ_bulk(A=0.95) = −0.283044` and `Γ_bulk(A=0.99) = −0.453922`, matching
   canon's recorded gate values *"`Γ_min(0.95)=−0.283`, `Γ_min(0.99)=−0.454`"*
   at `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md:226`.

#### 2.5.1 ⚑ What the acceptance gate actually tested `[CANON]` + `[WALK]`

The same canon line records the gate's own verdict verbatim:

> *"**T3.3** `Γ=−1` wall | `Γ_bulk` crosses `−0.25`, monotone toward `−1`, `→0`
> vacuum; **literal `−1` unreachable** | **PASS** — `Γ_min(0.95)=−0.283`,
> `Γ_min(0.99)=−0.454`, vacuum=0, **floor>−1**. α-FREE"*
> — `electron-bound-resonator-coverage.md:226` (`sup-1ecv2m`)

`[WALK]` So canon has already booked *"literal −1 unreachable"* on this branch
and passed the rung on a `−0.25` threshold — but it probed at `A = 0.95` and
`A = 0.99`, **amplitudes the electron's own A1 core never reaches**, because
`def-vyvsn1` pins that core at `A = √α = 0.0854`. At the operating point the
gate's subject actually occupies, `Γ_bulk = −9.155e-4` — **273× weaker than the
gate's own `−0.25` threshold**. The gate is not wrong; it is evaluated off the
operating point. `[OPEN]` Whether T3.3 should be re-run at `A = √α` is a
question for the audit, not a ruling here.

## §3 — ★★ THE TWO CAUTIONS

**These are not footnotes to §2. They are as load-bearing as §2, and they must
travel with every downstream citation of it. Neither may be softened.**

### ★ CAUTION 1 — a `−1` eigenvalue of a LOCAL junction is NOT confinement

`[MEASURED]` The `−1` eigenspace of §2.1 has dimension `z−1`. The balance
condition `Σ_j Y_j v_j = 0` is a **single linear equation** — **codimension 1**
per node. Balanced port-vectors are therefore **CHEAP, not special**: they form
a hyperplane through the origin at *every node of the lattice*, and they do so
in **empty cold vacuum**, where `Y_j = Y₀` for all `j` and nothing whatsoever is
confined.

`[WALK]` The consequence is blunt. **A local `Γ = −1` that is present
everywhere is undiagnostic — it does not distinguish an electron from
nothing.** Reading the `T2` irrep's `−1` as "the confinement wall" reads a
property of the *empty medium* as a property of a *particle*.

`[CANON]` Canon carries the same warning from a different direction, on the
`−1/3` floor: *"the `−1/3` intercept belongs to the **isolated vertex, which
does not exist in-lattice**"* —
`research/2026-08-24_engine-gamma-meanstest_result.md:214-215`. Every number in
§2.4 is an **isolated-junction** number for exactly the same reason.

`[OPEN]` **What the electron would have to be, if this route is right:** not a
node with a balanced eigenvalue, but a **CLOSED SURFACE of SIMULTANEOUSLY
balanced nodes** — a set of nodes on which the balance condition holds *jointly
and self-consistently under the connect map*. That is a property of the
**composed map**

```
M = C · blockdiag(S)
```

(`C` the connect/permutation map, `blockdiag(S)` the per-node scatter), and
**no leaf in the corpus computes `M`.** The junction spectrum theorem says
nothing about `M`'s spectrum: a direct sum of operators each having `−1` in its
spectrum tells you nothing about the spectrum of `C` composed with that sum.
**The entire physical question is displaced from §2 into an object this arc did
not compute.**

### ★ CAUTION 2 — the hollow-vortex BALANCE SHELL and the VIRTUAL NEUTRAL are DIFFERENT OBJECTS

Both are called "balance loci". **Do not weld them.**

| | hollow-vortex **balance shell** | **virtual neutral** |
|---|---|---|
| space | **real space** — a radius | **port space** — a hyperplane through the origin |
| what balances | two **opposed scalars**: outward circulation pressure `∝ Γ²/R³` vs inward surface tension `σ/R` | `z` **phasors** on the legs of one Wye node: `Σ_j Y_j V_j^inc = 0` |
| the balanced quantity | a **pressure** (dimensioned) | a **current sum** (KCL, phasor) |
| result | `R* = Γ/√σ ≈ 1.6 ℓ_node` | `V_u = 0`, a **dimensionless** condition on a direction |
| citation | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:49` `[CANON]` | `src/ave/solvers/vacuum_varactor_scatter.py:28-34` `[MEASURED]` |

`[WALK]` The collision is real and near: `boundary-observables-m-q-j.md:61`
itself glosses register 4 as *"BALANCE LOCUS … cf. the hollow-vortex balance
locus, `hollow-vortex-binding.md:49`"* — i.e. **the register-4 slot this arc
proposes to move the electron into is currently illustrated by the
pressure-balance object, not the phasor-balance one.** The register-move
proposal (§7, and the routed open item) must therefore either (a) split
register 4 into two sub-registers, or (b) argue that both are instances of one
kind. **This arc does neither, and takes no position.** `[OPEN]`

`[CANON]` The `Γ` symbol itself is overloaded across the two rows: in
`hollow-vortex-binding.md` `Γ` is the **Cosserat circulation**; in §2 `Γ` is the
**reflection coefficient**. Same glyph, different objects, one line apart in the
table above. Any downstream prose must disambiguate.

## §4 — The consequence: FREE EVERYWHERE or ABSENT HERE, never in between

`[WALK]` Put §2.1 and §2.5 side by side and the corpus's confinement number is
caught between two walls with no gap:

| the `−1` in question | where it lives | what §2 measures | verdict |
|---|---|---|---|
| the **`T2` irrep eigenvalue** `−1` (`k4-port-irrep-decomposition.md:23`) | the junction scatter's balanced subspace | present at **every node of empty cold vacuum**, at every grading, exactly, `z−1` fold | **FREE EVERYWHERE** — undiagnostic |
| the **`A1` bulk/mass** `−1` (`Z_eff = Z₀√S → 0`) | the amplitude level-set, which *has* a radius and *could* localize | `−9.155e-4` at `def-vyvsn1`'s own operating point `A = √α` | **ABSENT HERE** — a 0.09% window |

**The one that is free is not localizing. The one that would localize is not
there.** And by the trace identity (§2.2) there is no intermediate settlement to
be had by grading harder: at `z = 3` the diagonal sums to `−1` no matter what,
so buying `Γ → −1` on one port sells `Γ ≥ 0` on another.

`[OPEN]` **Therefore the localizing object cannot be the LOCAL eigenvalue at
all.** If a virtual-neutral boundary exists, it is a **global** property — a
closed surface of simultaneously balanced nodes, i.e. a statement about
`M = C · blockdiag(S)`. This arc has established what the *local* operator can
and cannot do. It has established **nothing** about `M`, and the corpus
contains no leaf that computes `M`'s spectrum on a closed surface.

`[WALK]` **The honest summary of the arc's own weight:** §2 is a set of exact,
reproducible, negative results about the local junction. Its positive content
is entirely a **relocation of the question**, not an answer to it. Anyone
citing §2 as support for "the electron's boundary is a virtual neutral" is
citing the wrong half.

## §5 — Canon already carries the structure — in four unconnected places — and has the slot

`[CANON]` The balanced-polyphase condition is **already written in the
corpus**, four times, by four different lanes, none of them citing any other,
and **never at the electron-wall site**.

| # | site | what it says, verbatim | scope |
|---|---|---|---|
| 1 | `vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md:23` | *"`T_2` eigenvalue \| `−1`, triply degenerate"* | the `z=4` `K4` 4-port only |
| 1b | same leaf, `:55` | *"Basis spans the traceless 3D subspace `{v : Σ_i v_i = 0}` — **for every excitation at one port, an equal and opposite excitation exists at some combination of other ports.**"* | **that IS the balanced-polyphase condition**, in canon, at equal admittance |
| 2 | `common/relational-cancellation-identity.md:265, :268` | instance 1: *"`Γ_end = −1/3` **exactly, at ALL orders**"* under uniform grading; instance 3: *"a uniform impedance scale cancels in `Γ = (2−z)/z`"* | status **PROPOSED**; fenced *"must NEVER be cited as a step in deriving any value"* (`:229`) |
| 3 | `vol6/period-2/carbon/ee-equivalent.md:12` | *"establishing a **perfectly canceled vacuum 'neutral' node** in the geometric center — structurally analogous to a **Wye (Y) ground**"* | the C-12 nucleus; `clm-sd04x4` solidity **0.30**, **do-not-build** |
| 4 | `vol2/particle-physics/ch02-baryon-sector/proton-identification.md:158-167` | Grant's own 2026-08-23 Route C: *"a **virtual-neutral surface** pinned by the mutual frustration of the cage's saturated strain projections"* | registered **candidate ontology ONLY** — see the fence below |
| 5 | `vol5/molecular-foundations/organic-circuitry/first-principles-bond-force-constants.md:110` | *"each interior node … is a 3-connected **WYE junction — a three-phase node**"*, and a heavy-heavy bond is *"a **balanced three-phase system**"* | every srs interior node, already |

`[CANON]` **The generalization is what is new, not the structure.** Site 1
proves the `−1` eigenvalue for the **`z=4` `K4` 4-port at equal admittance**.
§2.1 extends it to **arbitrary `z` and arbitrary graded `Y`**, with the
eigenspace correctly re-weighted to `{v : Σ_j Y_j v_j = 0}`. That extension is
this arc's only genuinely new algebra, and it is a two-line proof.

### 5.1 ⚑ The fence canon puts on site 4 — which the arc must honour `[CANON]`

Grant's own Route C entry is **explicitly fenced**, verbatim:

> *"Registered as a candidate ontology **ONLY**: the cold-geometry-into-saturated-core
> conditional is **undischarged**, and **no neutrality/minimum-N argument may be
> built on it** (both uses **adversarially refuted**, see the docket).
> Discriminator: the `def-cf1srf` shape-forcing BVP."*
> — `proton-identification.md:161-165`

`[WALK]` This is the sharpest constraint on the whole arc, and it did not come
from the dispatch brief — it came from reading the leaf. **A neutrality
argument built on the virtual neutral has already been adversarially refuted
once, in the baryon sector, four days ago.** Nothing in §2 discharges the
`cold-geometry-into-saturated-core` conditional; §2 is *isolated-junction*
algebra. The lepton-sector version of the same move must expect the same
attack, and §10/§11 are written accordingly.

### 5.2 And canon has the SLOT `[CANON]`

`common/boundary-observables-m-q-j.md:56-63` enumerates **four boundary
registers** and files the electron under register 1:

> *"**AMPLITUDE LEVEL-SET** — Electron, Nucleus, Atom rows: the boundary is the
> locus where the saturation amplitude hits threshold (`S(A)→0`, `Γ→−1`)"* (`:58`)
> … *"(**BALANCE LOCUS** — the fourth register — appears at the *Solar* rung …
> not tabulated here; cf. the hollow-vortex balance locus,
> `hollow-vortex-binding.md:49`.)"* (`:61`)

And `common/vocabulary-register.md:404` (`def-anat3s`) already banks the
conjecture the move would discharge:

> *"**(ii) the balance shell** (the `σ`-opposite-equal crossing, `≈ 1.6 ℓ_node`;
> **CONJECTURED `≡` wall** per Ruling 6)"*

`[WALK]` So the proposal in §7 is to **move a row between two registers canon
already defines**, and to **discharge a conjecture canon already banked** — not
to mint a category. `[OPEN]` But per caution 2, register 4's *own gloss*
currently points at the pressure-balance object, so the move as stated is
ambiguous until register 4 is split or unified. That ambiguity is the open
item, not a detail.

## §6 — Where Grant's reading is SUPPORTED (seven places)

**Why this section exists.** This arc has a documented habit of reporting only
the negative — §2 is four exact results, three of them negative, and §3/§4 are
cautions. A record that stops there misreports the state. **Seven places the
reading is right, listed at their honest grade:**

| # | the support | grade | receipt |
|---|---|---|---|
| **S1** | **The engine's operative scatter equation is the Wye reduction.** Grant's "what does the schematic say" question has a literal answer in shipped code, not an analogy: `V_u = 2(Σ_j Y_j V_j^inc)/(Σ_k Y_k)`, and `V_u = 0` on balance. | `[MEASURED]` | `src/ave/solvers/vacuum_varactor_scatter.py:28-34, :156-185`; run in §2 |
| **S2** | **Canon has the register slot AND the banked conjecture.** Register 4 (**BALANCE LOCUS**) exists and is un-tabulated for the electron; `def-anat3s` already says surface (ii) is *"**CONJECTURED `≡` wall**"*. The move discharges a banked conjecture rather than minting a category. | `[CANON]` | `common/boundary-observables-m-q-j.md:61`; `common/vocabulary-register.md:404` |
| **S3** | **The rim-inversion he already ratified points the same way.** `def-satrim`/`clm-riminv` (**SOLID** def, claim solidity 0.55, Grant-ratified mapping): a saturated core is *"pinned **ON the RIM** … amplitude-frozen, **phase-topological**"*, and *"the dynamics and topology **swap roles**; the core's state space is the **BOUNDARY** of the baseline's."* A boundary that is a phase-space object, not a real-space one, is exactly what Grant said. | `[CANON]` | `common/vocabulary-register.md:1126` (`def-satrim`); `common/saturation-rim-inversion.md` |
| **S4** | **His rejection of the propagation question was correct.** Asking "what `Γ` does the wall present to an incoming wave" presupposes a wave propagating *through* a medium the defect sits *in*. On this substrate matter **is** the lattice's lock-state, not an object embedded in it — so there is no second medium for `Γ` to be defined against, and the question has **no referent**. Killing it was right. | `[WALK]` — ★ **provenance: prior-session chat; this arc did NOT verify a canon statement of it.** The nearest in-corpus support is the `def-satrim` role-swap (S3) and `resonant-lc-solitons.md:52` (*"The particle dynamically weaves its **own** perfect topological mirror"*). Treat as un-audited. |
| **S5** | **de Broglie survives the matched (reflector-free) reading — two routes, both in-corpus.** (i) **Turning point:** *"The matter wave **does not bounce off a physical tear** in the vacuum; it bounces when it simply runs out of kinetic energy… the local acoustic impedance becomes purely imaginary, forcing a total reflection."* (ii) **Self-match:** *"the precise radius where this trapped … wave achieves a **lossless resonant impedance match with itself** (`2πr = nλ`)."* Neither needs a material mirror. | `[CANON]`, with a caveat | `vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:54`. ⚑ **Caveat:** the two immediately-preceding lines (`:50`, `:52`) carry `🔴 [DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION]`. Line `:54` itself carries **no** demotion marker, but it sits inside the demoted passage's argument; a lane citing it must check the R40-B2a re-derivation status first. |
| **S6** | **Canon states the kernel-free `Γ = −1` and calls it a virtual ground, in as many words.** *"**Antisymmetric (differential) eigenmodes** `(1,−1,0)`, `(1,1,−2)` — memoryless value **`Γ_A = −1`**: the differential mode sees a **SHORT** (**the node is a virtual ground for it**)."* Written independently, from `C3v` symmetry, with no saturation kernel anywhere in the derivation — the same theorem §2.1 proves for graded `Y`. | `[CANON-adjacent]` — an in-corpus **research derivation**, not a KB leaf | `research/2026-07-10_x37-junction-parasitics_derivation.md:39-40` |
| **S7** | **He reinvented, from EE intuition alone, a structure his own corpus carries in five unconnected places.** §5's table lists them; none cites any other; none is at the electron-wall site. That convergence is evidence the reading is picking up real structure in the operator, independent of whether it localizes anything. | `[WALK]` over `[CANON]` receipts | §5 table, rows 1–5 |

`[WALK]` **What S1–S7 do and do not buy.** They establish that the reframe is
**well-posed, operator-grounded, and already latent in the corpus**. They do
**not** establish that the electron's boundary *is* a virtual neutral — that is
blocked by caution 1 (balance is cheap) and by the §5.1 fence (a neutrality
argument on this object was adversarially refuted once already). Support for
the *question* is not support for the *answer*.

## §7 — Provenance of the incumbent, and one correction that must propagate

### 7.1 What `def-vyvsn1` actually rests on `[CANON]`

`def-vyvsn1` is **SOLID** and is the **only SOLID electron-wall statement in the
corpus**. It is not being superseded here — only Grant rules that. But
Grant's directive is *"we need to be ok challenging past rulings that don't have
hard math tied to them"*, so the honest inventory of what is tied to it:

| field | what canon says, verbatim | reading |
|---|---|---|
| `dimension/type` (`vocabulary-register.md:753`) | *"voltage (both); **BOTH are CALIBRATION, not derived** (`V_snap ≡ m_e c²/e` definitional …; `V_yield ≡ √α · V_snap`, the **√α being the imported α-echo**)"* | the two thresholds are **calibration**, and their ratio is an **imported α-echo** — canon's own words |
| `clm-cross-links` (`:756`) | *"**(none verified-specific yet)**"* | **no scored claim**, no numeric solidity attached |
| `verification` (`:758`) | *"VERIFIED the Grant 2026-06-30 T2 ruling **landed in prose** at …; VERIFIED the A1-horn **reconciliation** …; VERIFIED the calibration **definitions** …"* | a **propagation** receipt — that the ruling was written down consistently — **not a derivation receipt** |
| mechanism (`pair-production-axiom-derivation.md:102`) | *"Above `V_yield` the transverse micro-rotation wave's amplitude crosses Axiom-4 onset, `Γ → −1`, and the lattice self-creates its TIR cavity"* | **one sentence.** No solved BVP, no eigensolve |
| shape-forcing (`vol9/ch3-pin-port-configuration/device-circuit-models.md:163`) | *"**Status: OPEN.** … What is **NOT** derived is the **shape-forcing chain**: **no solved boundary-value problem produces the electron's surface** from its `0₁`-unknot topology."* | canon **already** books the shape as underived |

`[WALK]` So the incumbent's SOLID grade attaches to a **sector attribution**
(which sector owns which threshold — genuinely adjudicated, 2026-06-30) and to a
**calibration**, not to a derivation that the wall is an amplitude level-set.
The level-set *character* of the wall is the part with no hard math tied to it,
and it is precisely the part §2 and the register-move proposal touch.
**Nothing in this arc touches the sector attribution, which is the part that
was adjudicated.** `[OPEN]`

### 7.2 ⚑ THE CORRECTION THAT MUST PROPAGATE `[CANON]`

`vol9/ch3-pin-port-configuration/device-circuit-models.md:165` reads, verbatim:

> *"**Two coincident `Γ=−1` walls — do NOT re-collide.** The confinement surface
> is the **A1 MASS wall** (`Z_bulk→0`, the impedance-short `Γ=−1` of the
> Pauli/TIR derivation). It is numerically coincident with — but a **DISTINCT
> object** from — the **`Γ_spinor = −1`** topological `2π→4π` stability wall of
> the T2 micro-rotation sector … Reading the two `−1`'s as one wall would wire
> the cage into the charge-winding and break the two-"3"s orthogonality."*

**`:165` does NOT argue against the A1/bulk wall. It ASSERTS it.** Its guard
sentence warns against **colliding** the A1 mass wall with the `Γ_spinor` T2
wall; it argues **on the A1 side**. **Any document that inherited the earlier
framing — that `:165` is a prohibition against the 2026-06-30 ruling — is
wrong and must be corrected.** Routed as
`_orchestration/open-items/2026-08-26-device-circuit-models-165-correction.md`.

### 7.3 ⚑ And the correction exposes a live canon-vs-canon tension `[CANON]`

Reading `:165` correctly makes a **second** problem visible, which the earlier
misreading concealed:

| site | who owns the confinement surface |
|---|---|
| `device-circuit-models.md:165` | *"The confinement surface **is the A1 MASS wall**"* |
| `vocabulary-register.md:751` (`def-vyvsn1`, **SOLID**) | *"`V_yield` … = the **transverse Cosserat (`T_2`) self-trap wall** … the **single-electron confining `Γ=−1` TIR cavity self-creates here**"*; and *"**The A1 mass channel does NOT saturate at `V_yield`**"* |
| `pair-production-axiom-derivation.md:102` | *"a single electron's confining `Γ = −1` wall is **already here**"* — at `V_yield`, the **T2** threshold |

`[MEASURED]` §2.5 puts a number on the A1 side of that tension: at
`def-vyvsn1`'s own A1 operating point, `Γ_bulk = −9.155e-4`. `[WALK]` The A1
branch **cannot** be the confinement surface at the amplitude canon assigns the
A1 core. Either `:165` is using "A1 mass wall" for a different operating point
than `def-vyvsn1` assigns, or the two sites disagree about sector ownership of
the confinement surface — which is exactly the `A1 ⊥ T2` cross-wiring class the
corpus already watches for.

`[OPEN]` **This arc does not adjudicate it.** It records it, with numbers, and
routes it. Resolving it is an audit/lane job, and it is upstream of the
register-move question: *which sector owns the wall* must settle before *which
register the wall belongs to* is meaningful.

## §8 — The symmetric standard, both directions
## §9 — Honest caveats, stated before the audit finds them
## §10 — ★ AUDIT CHARTER
## §11 — ★ KILL CONDITIONS
## §12 — What this arc does NOT do
## Appendix A — reproduction receipt
