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
