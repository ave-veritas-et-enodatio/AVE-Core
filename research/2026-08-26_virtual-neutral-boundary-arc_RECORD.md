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
## §4 — The consequence: FREE EVERYWHERE or ABSENT HERE, never in between
## §5 — Canon already carries the structure — in four unconnected places — and has the slot
## §6 — Where Grant's reading is SUPPORTED (seven places)
## §7 — Provenance of the incumbent, and one correction that must propagate
## §8 — The symmetric standard, both directions
## §9 — Honest caveats, stated before the audit finds them
## §10 — ★ AUDIT CHARTER
## §11 — ★ KILL CONDITIONS
## §12 — What this arc does NOT do
## Appendix A — reproduction receipt
