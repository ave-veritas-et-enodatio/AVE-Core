# LENS RECORD — the AUTONOMOUS-HARMONIC-BALANCE lens: the existence test may not need a scaffold at all (2026-08-25)

**Status: NEW LENS, WALK-GRADE, UNAUDITED. Nothing here is a claim, a ruling,
or a design decision.** It is proposed as a lens on the P2 existence solve and
it **requires an adversarial audit before any part of it reaches a prereg** —
the audit charter is §6 and the routing item is
`_orchestration/open-items/2026-08-25-autonomous-hb-lens-audit.md`.

**Provenance.** Grant, verbatim (2026-08-25): *"ok walk the physical picture of
the question for me, what do the options mean physically from the perspective
of the lattice, and what options are you not thinking of?"* — asked of the
coupled decision-1 / carrier fork recorded in
[`_orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md`](../_orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md)
§2 and §4. The lens is the answer to the second half of that question.

---

## §1 — The unexamined assumption

Every option put to Grant so far — source-terminated, injection-lock, Norton
node injection, tone-carrier, spatial-texture carrier, the common-mode
projection — **assumes the existence test must be DRIVEN**: that something is
attached to a boundary, and the verdict is whether the drive can then be
turned down (the source-idle criterion).

That assumption has never been examined. **Drop it and the fork does not get
resolved — it disappears**, because the whole cluster (ϖ, the projection,
matched-vs-mismatched generators, which carrier writes the winding at the
drive) exists *only* because a scaffold exists.

## §2 — What the two standing options mean from inside the lattice

Sit on a boundary node and ask what it feels.

**Option 1 — tone-ratio carrier (ports uniform).** Every boundary node feels
the SAME two-tone signal, all in phase. The interior sees a **breathing
drive** — the boundary pulsing together. There is no "around" anywhere in it,
and a winding is intrinsically an ANGULAR object (phase advancing as you go
around). **With every port in phase there is no around, hence no angular
momentum and no collective winding.** This is why the scoping lane measured it
annihilated *exactly* by the decision-1 projection and converging on the
TRIVIAL ZERO STATE (R58 §4): it is not a differential at all — it is a
monopole pulse carrying a 2:3 spectrum.

★ **And a conflation this exposes, not previously stated.** Canon's
phase-space (2,3) is a **PER-TANK** object — one bond-pair tank's trajectory on
its own Clifford torus. Imposing it uniformly across the boundary says *"every
tank runs this same trajectory, synchronously."* That is **not** the statement
*"the collective carries a winding."* Option 1 conflates a per-tank trajectory
with a collective topological charge. **[WALK — this is the lens's own
reading of the canon carve, and it is audit item A4.]**

**Option 2 — spatial texture carrier.** Each boundary node feels a drive whose
phase depends on where it sits: the boundary is **stirred with a definite
handedness**. The interior sees a rotating chiral push, which genuinely carries
angular momentum and genuinely is a collective winding. But it is a REAL-SPACE
winding, and canon holds the electron's real-space body is the `0₁` unknot
(INVARIANT-N1) — which is what epic guard 3 polices.

**The deadlock, physically:** option 1 imposes something that is not a winding;
option 2 imposes a winding of a kind canon says is not there.

## §3 — ★ THE LENS: four source-free formulations, one of them standard EE

### 3.1 The homogeneous nonlinear eigenvalue problem — AUTONOMOUS HARMONIC BALANCE

If the question is *does a self-sustaining state exist*, the direct form is:

> find **v ≠ 0** solving **`e^{iθ} v = M(S(|v|)) v`** with **no sources**,
> with both **θ** and **v** unknown.

That is a **nonlinear eigenvalue problem**, and it is exactly the G1 walk's own
one-line form — *an eigenmode of the saturating medium under a topological
boundary condition* — with the scaffold removed.

**It has a name and a standard method in the discipline this corpus is written
in.** Free-running-oscillator analysis in RF/microwave design solves precisely
this: **autonomous (oscillator) harmonic balance** — the HB equations with the
source term dropped, one extra unknown (the oscillation frequency) and one
extra equation (a **phase-normalization / gauge-fixing condition**, typically
pinning one node's phase to zero).

★ **The three consequences that make this more than a convenience:**

1. **The arbitrary phase that the normalization condition fixes IS ϖ.** The
   standard technique's way of handling it is **gauge-fixing by choosing a
   reference**, not projecting a mode out. That is canon's own clause Q —
   Grant's ratifying words on 2026-08-10 were *"makes perfect sense, we need a
   ground reference."* **The EE method and the source law agree on the
   treatment.** [ASSEMBLY — audit item A2.]
2. **The source-idle criterion becomes unnecessary**, because there was never a
   source to go idle. Decision 1, the carrier fork at the drive level, the
   projection receipt, the matched-vs-mismatched generator question and the
   `term=None` structural-zero branch all cease to be questions.
3. **It is stronger on the physics, not merely cheaper.** A driven test can
   always be accused of having found the scaffold's own mode — that was the
   A1 lane's (withdrawn but well-motivated) worry. **A source-free nontrivial
   solution cannot be: there is nothing else it could belong to.**

### 3.2 Winding as a LAGRANGE CONSTRAINT, with the multiplier as the idle measure

Impose the Link integral as a constraint on the solve rather than as a drive;
let the solver find the state that satisfies it. **The multiplier IS the
external agent, so `multiplier → 0` IS self-sustaining** — a precise,
*internal* restatement of source-idle with nothing attached to a boundary.

### 3.3 Scattering-resonance / pole search

Drive from far away and look for a pole of the reflection response. This is the
textbook way to FIND a bound state without imposing one — the state announces
itself as a trapped frequency. It also reuses the response-map machinery
already merged (Class-C scalar, Stage-1 transverse).

### 3.4 Adiabatic continuation with a turning point

Wind up slowly and watch for the branch to fold back; **the fold IS the
existence boundary.** Partially explored already: the scoping lane's amplitude
continuation ladder *"converges 8/11/20/41 outers up the rungs but does not fix
the top rung alone."* Under this lens that stall is **not necessarily a
numerical failure — it may be a result**, and distinguishing the two is itself
a test. [Audit item A5.]

## §4 — How the topology enters without a drive

The constraint becomes a **restriction on the search space**, not a source:
seed the iteration in the wound sector and let it relax *within* that sector.
Topology cannot change under continuous deformation, so the sector is preserved
automatically **provided nothing forces the field through zero amplitude** —
which is exactly the rim-inversion mechanism (the interior confers no
protection; the unwinding channel is the `A→0` path). [Audit item A3 — this is
the lens's most load-bearing unverified step.]

## §5 — Honest caveats, stated before the audit finds them

1. **Convergence is harder.** A nonlinear eigenvalue solve is worse-conditioned
   than a driven solve, and the scoping lane already found P2's
   strongly-engaged regime needs Anderson/DIIS (66 outers where plain Picard
   fails at 150).
2. **A trivial solution always exists** (`v = 0`). The non-triviality gate R58
   §4 makes mandatory is *more* important here, not less.
3. **Autonomy does not by itself confer physicality.** A source-free nontrivial
   solution of a lossless network could still be an artifact of the truncation,
   the tone set, or the boundary treatment (periodic vs terminated). The
   scaffold-artifact worry is reduced, not eliminated.
4. **S2 still bites.** The shipped varactor kernel does not mix tones (coupling
   is amplitude-only, R58 §3), so whether a 2:3 tone structure is even
   *representable* as an autonomous solution on this machinery is open.
5. **The T2 blocker is untouched.** This lens changes how the state is found,
   not what can be read off it. M, Q and g still need the Cosserat channel.

## §6 — ★ AUDIT CHARTER (what must be attacked before any of this reaches a prereg)

| # | claim | class | how to attack it |
|---|---|---|---|
| **A1** | The shipped `harmonic_balance_srs` can be run autonomously — same fixed point, source term dropped, one phase pinned | MACHINERY | read the solver; try it; report what actually breaks. If it cannot, say what the minimal change is |
| **A2** | Autonomous/oscillator HB is standard external prior art AND its phase-normalization is the same move as clause Q | EXTERNAL + ASSEMBLY | verify the external claim honestly (it is asserted here from discipline knowledge, NOT retrieved); then check the clause-Q identification is real and not a resemblance |
| **A3** | Topology is preserved by seeding the sector, because deformation cannot change it unless the field passes through zero | NUMERICAL + CANON | the most load-bearing unverified step. Does the discrete solve actually preserve the winding? What is the discrete analogue of "passing through zero"? |
| **A4** | The phase-space (2,3) is a PER-TANK object, so uniform imposition conflates per-tank trajectory with collective charge | CANON READING | check against the two-threes carve, INVARIANT-N1, and the electron-plumbing primer. This reading has not been swept |
| **A5** | The scoping lane's top-rung continuation stall may be a RESULT rather than a numerical failure | INTERPRETIVE | re-run it; distinguish the two. A false positive here would be a serious error |
| **A6** | Dropping the scaffold dissolves decision 1 and the carrier fork rather than hiding them | LOGIC | adversarial: find where the fork re-enters in disguise (the tone set? the seed? the boundary treatment?) |
| **A7** | A source-free solution "cannot belong to the scaffold" | LOGIC | true but possibly vacuous — enumerate what it COULD still be an artifact of (§5.3) |

**Also required of the audit:** the consensus-bias symmetric standard (would
the equivalent move be flagged in an SM/QED context?), and the
discrimination check (does this lens buy organizing power, a number, or
neither — the honest answer is expected to be "organizing power and zero
numbers").

## §7 — What this lens does NOT do

It does not answer the existence question; it proposes a cleaner way to ask it.
It mints nothing, moves no solidity, and does not supersede R58 — decision 1
and the carrier fork remain **live and un-ruled** unless and until this lens
survives audit and Grant rules that it replaces them.

---

## 🔴 STATUS NOTE — 2026-08-26: THE AUDIT HAS RUN. Criterion DEAD as posed.

**Additive only (Rule 12). Nothing above this line is edited; the body of this
record is byte-identical to its merged state at `a3f4fef7`.**

The §6 audit charter (A1–A7) ran in two phases — a six-lane adversarial review,
then twelve refuter votes plus a completeness-critic synthesis. **Result:**
[`research/2026-08-25_autonomous-hb-lens-audit_RESULT.md`](2026-08-25_autonomous-hb-lens-audit_RESULT.md).

**Headline disposition: the existence criterion as posed is DEAD.** *"Does a
nontrivial source-free solution exist"* cannot return NO — existence is generic
(continuous one-parameter families at `r_auto ~5e-15`, in every winding sector,
delocalized across 54–85 % of the lattice, running continuously to `A→0` where
they **are** the cold lattice's own linear eigenmodes). The lens is repairable
**only as a SELECTION test, never as an EXISTENCE test.** All seven charter
items are discharged or partially discharged; the disposition table is §5 of the
result doc.

**One sentence in this record is now FALSIFIED BY MEASUREMENT rather than merely
hedged** — §3.1 consequence 3, at **`:97-98`**:

> *"**A source-free nontrivial solution cannot be: there is nothing else it
> could belong to.**"*

**It can be. It belongs to the cold lattice, continuously.** §6's charter row
A7 hedged this as *"true but possibly vacuous"*; the measurement is stronger
than the hedge. Per Rule 12 the sentence is **preserved, not edited** — this
note is the correction of record.

**Two further items measured against this record:** §3.4's backup selector
(*"the fold IS the existence boundary"*, `:116-117`) is **measurably absent** —
no turning point to `A_max 0.950`, and the top-end break is a numerical failure
on the **approach to** the saturation kernel's declared clip domain
(`A_max = 0.986728` against `A_cap = 0.99` — the clip is never entered), which
is also the **negative answer to charter item A5**. And §3.2's
Lagrange-constraint formulation **survives the audit intact** and is the
strongest formulation in the record.

**§7 is UNCHANGED and still governs.** This lens **mints nothing, moves no
solidity, and does not supersede R58** — decision 1 and the (2,3) carrier fork
remain **LIVE and un-ruled**, and the audit's finding is that the lens does not
currently qualify to moot them. **Only Grant rules that it replaces them.**
