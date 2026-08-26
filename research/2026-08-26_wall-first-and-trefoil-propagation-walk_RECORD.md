# WALK RECORD — the WALL-FIRST reframe and the trefoil-vs-photon propagation walk (2026-08-26)

**Status: WALK-GRADE, UNAUDITED. Nothing here is a claim, a ruling, a
retraction, or a design decision.** Four connected chat walks between Grant and
the orchestrator on 2026-08-26, recorded as ONE arc because they are one arc.
Every statement below carries a grade tag: `[WALK]` (the walk's own reading),
`[CANON]` (verified against a file:line this session), `[MEASURED-ELSEWHERE]`
(an audit/driver finding, cited not re-run), `[OPEN]` (a question the walk
raises and does not answer). Audit charter is §6; kill conditions are §7; the
routing item is `_orchestration/open-items/2026-08-26-wall-first-reframe-audit.md`.

<!-- SKELETON: sections land one per commit -->

## §0 — Framing: why this record under-claims

**Provenance.** Four chat walks, Grant and the orchestrator, 2026-08-26,
following the autonomous-HB lens audit (`research/2026-08-25_autonomous-hb-lens-audit_RESULT.md`
— **forthcoming input, owned by a concurrent lane; its findings are NOT folded
in here**, and are cited by document name only). The four walks collectively
**re-pose the electron-existence question** from *"does a state exist?"* to
*"is there a wall?"* None of it was in the repo before this record.

**The reason this record under-claims, stated first because it is the whole
point.** This arc's two immediate predecessors were both walk-grade lenses, and
**both died at audit on the step their author was least worried about**:

- The **autonomous-HB lens** (`research/2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`)
  put its own worry on A3 (*"the most load-bearing unverified step"*, §6) —
  topology-preservation on the discrete solve. `[MEASURED-ELSEWHERE — the audit
  result doc, forthcoming, is the authority on where it actually died; this
  record does not characterize its verdict.]`
- The **electron-wall / saturation-tension reading** carried into this arc by
  the orchestrator (electron core at $A=\sqrt\alpha$, $S\approx0.996$, versus a
  wall requiring $S\to0$) is flagged **in §3.5 below as probably a
  three-surfaces-collapsed-into-one error** — an error on a step nobody in the
  arc was worried about, because "the wall" was assumed to be one surface.

So the discipline applied here is: **the confident steps get the audit
instructions, not the hedged ones.** §6's charter deliberately puts its
sharpest attack instructions on the claims this arc states most fluently
(W1-1, W3-3, W4-2), not on the ones it already hedges.

**A second reason, structural.** Every one of the four walks turned out, on
verification, to be **partly a rediscovery of something canon already carries**
— in two cases carrying Grant's own prior ruling. That is recorded as a result
(§3.6, §5), not smoothed away. An arc that keeps rediscovering canon is an arc
whose novelty claim should start at zero.

**And a third, load-bearing one.** Verification this session found **three
places where canon contradicts or demotes this arc's own framing** (§1.3, §3.4,
§4.5). They are surfaced, not resolved (flag-don't-fix). One of them — the R40
demotion of channel 3's band entry — **removes the premise WALK 1 argues
from**, while leaving WALK 1's conclusion standing for a *different* reason.
That is the single most important thing in this document.


## §1 — WALK 1: the channel diagnosis

### §1.1 — The reading

`[WALK]` **The whole P2 arc has been solving in the one channel that
structurally cannot localize.**

`[CANON]` The port register's four inherent channels
([`port-register.md`](../manuscript/ave-kb/common/port-register.md):47–50, §1)
carry the relevant split:

| # | Channel | Irrep | Gap | verified at |
|---|---|---|---|---|
| 1 | EM-transverse (photon; $T_2$ shear-EM) | $T_2$ | **none** (gapless acoustic) | `:47` |
| 2 | Mechanical shear / GW | $T_2$ | **none** (gapless acoustic) | `:48` |
| 3 | Bulk-longitudinal / dilatation ($A_1$ **mass**) | $A_1$ | **none** (gapless acoustic) — ⚑ **see §1.3** | `:49` |
| 4 | Cosserat micro-rotation / wryness (the $(2,3)$ winding = **charge**) | (micro-rot.) | **GAPPED**, $\omega^2 = c_\kappa^2 k^2 + m_\omega^2$, $m_\omega = \sqrt{4G_c/I_\omega} \sim c/\ell_{node}$, Yukawa reach $\sim \ell_{node}$ | `:50` |

`[CANON]` Sector ownership: **mass is the A1 longitudinal dilatation** and
**charge/spin is the Cosserat $(2,3)$ winding**, held orthogonal —
[`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md):25,
verbatim: *"**MASS (A1) $\perp$ CHARGE/spin (T2) — never one phasor** (def-portmp)."*

`[WALK]` **The diagnosis.** A gapless channel has no intrinsic length scale.
Nothing in its dispersion picks out a size, so there is nothing for a solution
to localize *at*: any localized packet in a gapless linear branch is a
superposition that disperses. A gapped channel does have one — the gap
$m_\omega$ is an inverse length, and $m_\omega \sim c/\ell_{node}$ makes the
Yukawa reach exactly **one node length**, which is the same scale canon puts
the electron envelope at (`[CANON]`
[`electron-unknot-cosserat-seeder.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot-cosserat-seeder.md):79–83,
*"the entire electron envelope fits inside ONE K4 cell"*, $R_{loop} = r_{tube} = \ell_{node}/2\pi$).

`[WALK]` **Consequence for the audit's finding.** If a solve that hunts a
localized state runs in channel 3, a universal-delocalization result is what
the channel structure predicts. It would be explained by **the channel**, not
by solver failure — which is a different diagnosis, and a cheaper one, than
"the solver cannot converge the top rung."
`[MEASURED-ELSEWHERE]` The delocalization finding itself belongs to
`research/2026-08-25_autonomous-hb-lens-audit_RESULT.md` (concurrent lane;
this record does not restate its verdict, its scope, or its confidence).

### §1.2 — What is NOT claimed here

- Not claimed: that the P2 solver ran only in channel 3. `[OPEN]` **Which
  channel(s) the shipped solve actually carries is an unverified premise of
  this whole walk** and is audit item **W1-1**.
- Not claimed: that gaplessness is *sufficient* to forbid localization. A
  gapless nonlinear medium can host solitons (that is what a soliton is for).
  The walk's argument is about a *linear* branch having no scale, and the P2
  problem is explicitly nonlinear (saturating medium). **This is the walk's
  weakest step and it is stated here rather than buried** — audit item W1-2.
- Not claimed: that channel 4 *does* localize. The gap supplies a scale; it
  does not supply a solution.

### §1.3 — ★ CANON CONTRADICTS THE PREMISE (flag-don't-fix, surfaced not resolved)

**WALK 1 argues from "channel 3 is gapless acoustic." That cell of the port
register is 🔴 DEMOTED.**

`[CANON]` [`port-register.md`](../manuscript/ave-kb/common/port-register.md):49
carries **two** dated demotion stamps. The relevant one is the R40 batch-2a
NEEDS-RE-DERIVATION row, whose audited rationale is quoted verbatim in the same
file (§ *R40 batch-2a*, row `:49`):

> *"Prereg-explicit: Z_bulk=rho\*c_bulk owes formula-level re-derivation; **the
> gapless band-edge entry presumes a spectrum branch the carve removes**; covers
> the :126 FLAG-A label-flag (provenance case (b): the speed fracture is
> carve-explained, no fact-of-the-matter)."*

`[CANON]` And the replacement, stated in that note's clause 4: under the
ratified **Axiom 5 (Substrate DC Bias), clause G**, the A1 / bulk slot is a
**bound response** $\mathbf{u}_0 = -\mathcal{A}_g\nabla\varepsilon_{11}$ — with
*"**no independent propagating branch, no port and zero longitudinal
characteristic speed**"*, so that *"a bulk **wave speed**, a bulk **radiative
port**, a bulk **band-branch** and a bulk **transit clock** therefore have **no
referent**."*

**What this does to WALK 1** `[WALK]`:

1. **The conclusion survives and gets stronger.** If channel 3 has no
   propagating branch at all, then it is not merely scale-free — **there is no
   dispersion relation in which to look for a localized state**. "You cannot
   localize in a gapless branch" becomes "there is no branch."
2. **The stated mechanism is wrong.** The walk's argument is *gaplessness*, and
   gaplessness is a property of a *band* — the exact object the carve removes.
   A walk that reasons from a demoted band entry has reasoned from a phantom
   even when it lands somewhere defensible.
3. **The honest status is therefore: right answer, dead premise.** That is a
   worse epistemic position than a wrong answer with a live premise, because it
   is the position that survives casual review.
4. **⚑ BIAS-DEBT rides.** `[CANON]` The same note's honesty rider: **THE BIAS
   PROPAGATION THEOREM** is Axiom 5's standing named-open debt — clause G's
   elliptic law is *"the static abstraction of underived finite-speed bias
   dynamics."* So the replacement is **owed, not held**, and this section may
   not be cited as though channel 3's status were settled either way.

**This section resolves nothing.** Whether the walk's diagnosis should be
re-stated on the bound-response footing, or is void with its premise, is audit
item **W1-3** and ultimately Grant's.


## §2 — WALK 2: what the substrate already settles

### §2.1 — Three "does X exist?" questions that died the same death

`[WALK]` The pattern: **the empty vacuum passes the test.** A test whose
positive control is satisfied by *nothing at all* is not a test of the
electron.

**(a) "Does a self-sustaining state exist?" — Axiom 3 answers YES for every
input.** `[CANON]`
[`axiom-register.md`](../manuscript/ave-kb/common/axiom-register.md):169,:176,
quoted through the wall taxonomy's own citation
([`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):100,
verbatim): *"Axiom 3's lossless-reactive extremal content is the primitive that
MAKES the bond-LC L2 energy invariant exact."* `[WALK]` In a medium with no
dissipative channel, **everything persists**. "Self-sustaining" is not a
discriminator in a lossless medium; it is the medium's defining property. Any
nonzero initial condition is self-sustaining by construction.

**(b) "Is there a chiral pre-stress?" — the rest vacuum already has one,
everywhere.** `[CANON]`
[`trampoline-analogy-primer.md`](../manuscript/ave-kb/common/trampoline-analogy-primer.md):157,
verbatim:

> ***"At rest the fabric is wound, not spinning.** The twist-lacing winds every
> gyroscope to a handed **rest-angle $\theta$** — that *is* the chirality,
> stored as elastic energy. But the rotation **rate $\omega = 0$ at rest**: the
> gyroscopes sit cocked, they do not turn. So the rest vacuum carries **no net
> circulation, no net B-field — it is magnetically neutral** (load-bearing:
> $\omega = 0$ is an *exact fixed point*; a term that spun the fabric below
> threshold would "manufacture spin," wrong physics). The handed winding is
> **parity**, not angular momentum."*

`[WALK]` So "handed load-free held twist" describes **empty space**. A test
that confirms one has been created confirms the vacuum.

**(c) "Is there a lattice topological invariant?" — closed negative, already
computed.** `[CANON]`
[`research/2026-07-02_cleave-registry-pump-chern-nband_result.md`](2026-07-02_cleave-registry-pump-chern-nband_result.md):36,
verbatim: *"It reports 0 on the srs manifold because the srs manifold **is**
topologically trivial in both readings."* Same doc `:28`,`:34`: the load-bearing
GATE-VOK pair — an integrator that **recovers the validated 2-band 0** AND
**detects a real $|C|=2$ that flips sign** — so the zero is not a trivially-zero
instrument artifact. `[MEASURED-ELSEWHERE]` Four configurations, both
enantiomorphs, both readings, converged at $n = 24/36/48$ (`:42`–`:47`).

### §2.2 — The reading

`[WALK]` **The electron cannot be defined by a property the vacuum lacks in
KIND.** Persistence, handedness, and lattice topology are all *properties of
empty space* in this framework. Every existence test built on one of them has a
positive control that the vacuum passes.

`[CANON]` What the vacuum *does* lack is **rotation RATE** — the very next
paragraph of the same primer,
[`trampoline-analogy-primer.md`](../manuscript/ave-kb/common/trampoline-analogy-primer.md):159,
verbatim:

> ***"Spin-up is what excitation does.** Apply a field or trap a soliton and
> the fabric's gyroscopes spin up to net $\omega$, biased the **handed** way.
> That net $\omega$ IS the **magnetic moment**; the spun-up region is the
> electron **flywheel** ($L = I\omega$)."*

`[WALK]` So the carve canon already draws is **parity (everywhere, static) vs
angular momentum (only where excited)**. A discriminating existence test has to
key on the *rate*, not the winding.

### §2.3 — Honest limits of §2

- `[OPEN]` **"The vacuum passes the test" is an argument about test DESIGN, not
  about physics.** It does not show any particular prereg was mis-designed; it
  shows a *class* of criteria is non-discriminating. Naming which shipped
  criteria are in that class is audit item **W2-1** and is NOT done here.
- `[OPEN]` The (c) result is about the **srs Bloch manifold's** Chern number.
  It is not a statement that no topological invariant of any kind exists
  anywhere in the framework — the $(2,3)$ winding and the $0_1$ unknot are
  topological objects that live elsewhere (phase space, real-space body). The
  walk uses (c) narrowly: *the lattice band structure* is not where the
  electron's integer comes from. Over-reading (c) is audit item **W2-2**.
- `[WALK]` The primer is a **pedagogy leaf**. Its :157/:159 statements are
  load-bearing prose, but a walk should not lean its central carve on the
  analogy layer without checking the physics leaf behind it. Audit item
  **W2-3**.


## §3 — WALK 3: wall first, contents never

### §3.1 — Grant's ratification of the reframe (verbatim, `[sic]`)

> **"yes, but what are the properties of the wall we can measure on the electron?"**

**That is the complete Grant-attributed content of this walk.** Everything from
§3.2 down is orchestrator walk-level reading, labelled as such.

### §3.2 — `[CANON]` The substrate-observability rule makes interiors unobservable IN PRINCIPLE

[`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md):33–39,
verbatim:

> *"For any localized region $\Omega$ in the substrate enclosed by a $\Gamma = -1$
> saturation surface:*
>
> 1. *The boundary totally reflects substrate waves outside and totally traps
>    them inside.*
> 2. *The interior is causally and impedance-disconnected from external
>    observers.*
> 3. ***Only $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ are externally measurable.**
>    Interior eigenmode wavelengths, microrotation profiles, soliton topology,
>    and bond-stress distributions are invisible to the substrate."*
>
> *"This is the **no-hair theorem applied universally** — not as a
> black-hole-specific theorem but as the substrate's fundamental observability
> constraint at every scale."* (`:39`)

`[CANON]` The same leaf, `:92`: *"**The interior topology is invisible from
outside** — only the boundary integrals matter."* And `:54`: *"**The substrate
observes integer/half-integer counts of relational observables; everything else
is interior plumbing.**"*

### §3.3 — CONSEQUENCE, and a retraction

`[WALK]` **Any test whose verdict lives in the interior is testing something
the substrate itself cannot see.** Under Grant's phase-only epistemology — no
direct observables, only relational phase — a quantity the *medium* cannot
read should not be load-bearing in an existence verdict **even when a simulator
can trivially peek at it**. The simulator's omniscience is an artifact of being
outside the physics, not a measurement channel.

**★ RETRACTION, recorded rather than quietly dropped.** The orchestrator's own
immediately-preceding framing of the existence question was:

> *"does the lattice admit a localized rotational state inside the gap?"*

That is an **interior question**: "inside the gap" names an interior spectral
property, and "localized rotational state" names an interior microrotation
profile — `[CANON]` **exactly two of the four items the observability rule at
`:37` lists as invisible** (*"interior eigenmode wavelengths, microrotation
profiles"*). It is **retracted on those grounds**, per Rule 12: the wording is
preserved above, and it is not being replaced by silently re-scoping it. §3.4
is a *different* question with a *new* framing, not a repair of this one.

`[OPEN]` **What the retraction does NOT settle:** whether interior questions
are illegitimate *as engine diagnostics* (they are clearly useful for debugging
a solver) versus illegitimate *as existence verdicts*. The walk asserts only
the latter. Audit item **W3-1**.

### §3.4 — The question, re-posed

`[WALK]` Not *"is there a state?"* but:

> **Does the lattice form a $\Gamma = -1$ saturation surface around a region,
> unforced — and what are $\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$ across
> it?**

**Is there a WALL.** Not what is inside it.

`[WALK]` **This explains the delocalization finding cleanly.** A delocalized
state **encloses nothing**. With no enclosing surface there is no $\partial\Omega$,
and the three boundary integrals are not *zero* — they are **UNDEFINED**. A
solver reporting "no localization" and a solver reporting "$\mathcal{M} = 0$"
are saying different things; the first is the honest one.

`[CANON]` Canon carries the same structure from the other side —
[`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):119, on why
the cutoff-class rows are scoped out of the boundary-register list: *"A lattice
band edge, a Cosserat gap, and an evanescent cutoff length **do not enclose a
region and emit a mass, a charge and an angular momentum.** They are dispersion
facts about a channel."*

### §3.5 — ★ MASS AND CHARGE AS SHADOWS: the Stokes dimensional ladder

`[CANON]` [`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md):17–23:

| Symbol | Operational definition | Dimensionality | quantized? |
|---|---|---|---|
| $\mathcal{M}$ | $\int_\Omega (n(\mathbf{r}) - 1)\, dV$ | **3D volume** | **no** — a continuous integral |
| $\mathcal{J}$ | $\mathrm{Wind}(\partial\Omega)$ | **2D surface** | **half-integer** per $SU(2)$ double-cover |
| $\mathcal{Q}$ | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ | **1D line/loop** | **integer** |

`[CANON]` `:23`, verbatim: *"Each invariant uses one fewer integration
dimension than the substrate's 3D bulk … **The three dimensions are exhaustive:
there is no fourth integrated boundary observable at this scale-invariant
structure.**"*

`[WALK]` **The reading: this is why charge quantizes and mass does not.** You
cannot link half a loop — linking is a count of crossings of a 1D curve, and
counts are integers. You *can* displace half a volume — a volume integral of a
continuous field takes any real value. Quantization is not an extra postulate
bolted onto charge; it is **the dimensionality of the integral that defines
it**. $\mathcal{J}$ sits in between and is half-integral, which is what a 2D
winding under a double cover should be.

`[WALK]` **So Grant's "projected strain" framing is literally right for
$\mathcal{M}$ and wrong for $\mathcal{Q}$.** $\mathcal{M}$ *is* an integrated
strain excess over a volume — projection language is exact. $\mathcal{Q}$ is
not a projection of anything; it is a **linking count**, and no amount of
strain-projection produces an integer.

`[OPEN]` The walk does **not** establish that the dimensional ladder *causes*
the quantization rather than merely *co-occurring* with it. A skeptic's version:
the integers come from the topology ($\pi_1$ of the configuration space), and
the 1D/2D/3D labels are a bookkeeping restatement. **Distinguishing "the
dimension forces the integer" from "the topology forces the integer and the
dimension labels it" is audit item W3-2**, and the walk has no argument that
picks between them.

### §3.6 — ★ WHAT CANON ANSWERS BACK (1): there is no "the wall"

`[CANON]` [`vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md):404
(`def-anat3s`, **FORM minted per Grant Ruling 8 option C, 2026-07-14**),
verbatim:

> *"a bound soliton's boundary region is **THREE physically-distinct radial
> surfaces** on $S(A(r))$: **(i) the wall** (fully-yielded $S\to0$,
> $\lvert\Gamma\rvert=1$ mirror; carries $\mathcal{M},\mathcal{Q},\mathcal{J}$;
> ground-state floor $\ell_{node}/2\pi$; sign = the ruled-degenerate selector
> #260); **(ii) the balance shell** (the $\sigma$-opposite-equal crossing,
> $\approx 1.6\,\ell_{node}$; CONJECTURED $\equiv$ wall per Ruling 6);
> **(iii) the knee / dress edge** (the $\Delta S=\alpha$ proportional limit,
> $A^2=2\alpha$)."*

`[CANON]` Canonical home [`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md):40:
*"The reflection off the knee is **small** ($\lvert\Gamma\rvert \ll 1$, the
near-matched sub-yield regime — distinct from the wall's
$\lvert\Gamma\rvert = 1$)."* Same leaf `:32`: the wall *"is the substrate's
observability boundary … giving total internal reflection
($\lvert\Gamma\rvert = 1$) and hiding the interior. It carries exactly the
three integrated boundary observables."*

**★ FLAGGED, NOT RESOLVED — the orchestrator's earlier "saturation tension" was
probably a three-surfaces-collapsed-into-one error.** The tension as it was
stated: *the electron core sits at $A = \sqrt\alpha$, so $S = \sqrt{1-\alpha}
\approx 0.996$, but a $\Gamma=-1$ wall requires $S \to 0$ — so where is the
wall?*

`[WALK]` Against the three-surface anatomy that reads as a **conflation**, on
arithmetic that is checkable in one line: `[CANON]` the knee is at
$A^2 = 2\alpha$, $S = \sqrt{1-2\alpha} \approx 0.9927$
([`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md):40).
`[WALK]` An amplitude of $A = \sqrt\alpha$ gives $A^2 = \alpha$, which is
**below the knee** — i.e. inside the near-matched sub-yield region, at the
surface canon says reflects with $\lvert\Gamma\rvert \ll 1$. Reading a
$\Gamma=-1$ requirement onto that amplitude compares surface (iii) against
surface (i)'s condition. There is no tension between the wall and the knee;
they are different radii with different $\Gamma$.

**This record does NOT resolve it.** `[OPEN]` The adjudication is routed to the
**electron-wall-properties corpus sweep** that was in flight at authoring time
(§9). Reasons this record refuses to close it: (a) surface (ii) is
**CONJECTURED $\equiv$ wall per Grant Ruling 6** and surface (iii)'s radius is a
**REGISTERED CHECK, not pinned**
([`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md):40),
so the three-surface geometry is not itself settled; (b) `def-anat3s` carries
**status: proposed** with the FORM ruled and *"every numerical value …
gate-measured, NOT SOLID"*; (c) the provenance of the $A=\sqrt\alpha$ figure was
not traced this session, and `[CANON]`
[`l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md):118
carries a **different** $\sqrt\alpha$ object — $V_{\text{yield, macro}} =
\sqrt\alpha \cdot V_{SNAP}$ — and whether these are the same number wearing two
hats is exactly the kind of homonym this corpus has been bitten by before.

### §3.7 — `[CANON]` The interaction ledger at an ideal $\Gamma = -1$ wall

[`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):97–103 (§2.1,
labelled walk-level at its own site):

| Channel of interaction | At an ideal $\Gamma=-1$ wall | why |
|---|---|---|
| **transmission** | **zero** | $\lvert\Gamma\rvert = 1 \Rightarrow$ nothing crosses; the interior is hidden |
| **absorption** | **zero** | *"**ideal saturation dissipates nothing** — it is a **lossless refusal**, Axiom-3-compatible"* ([`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md):101) |
| **reflection contact** | **MAXIMAL** | standing pattern with a node pinned at the wall; the **full** radiation-pressure / Maxwell-stress exchange happens there |

`[CANON]` `:103`: *"**a $\Gamma=-1$ wall is maximally interacting and completely
impenetrable at the same time.** It is the *most* forceful surface in the theory
precisely because it returns everything."*

`[WALK]` **So the only open channel across the wall is momentum exchange.** If
the wall is where the physics is readable, then what is readable there is
*force*, not *content* — which is the same statement as $\mathcal{M},
\mathcal{Q}, \mathcal{J}$ and nothing else.

`[CANON]` **⚑ The zero-absorption row rides an OPEN FORK** and the taxonomy
says so itself at `:105`: the standing manuscript
`vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`:324,:339,:341 models
the **near-yield channel as dissipative / thixotropic / memristive**. *"Grant
leans reversible; the fork stays open."* **If the dissipative branch wins, the
absorption row is wrong at the crossing** — carried, not adjudicated.

### §3.8 — ★ WHAT CANON ANSWERS BACK (2): Grant already answered his own question, three weeks earlier

`[CANON]` [`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):129,
**Grant, 2026-08-03, verbatim `[sic]`**:

> **"There can still be a gradient toward the wall vs the wall itself"**

`[CANON]` And canon's reading of it, `:131`: *"**This is the load-bearing
correction to §2, and it is Grant's.** Everything §2 says is about a *surface* —
and a surface with $\lvert\Gamma\rvert = 1$ is, by construction, a **boundary
condition**: a line in the bookkeeping where the field is told what to do. **It
is not where anything *happens*.** What happens happens in the **gradient
skin** hugging it, on the inside."*

`[CANON]` `:139`: *"**So the corpus's own answer to 'gradient vs wall' is: the
gradient is the sub-yield, near-matched, energy-storing region; the wall is the
yielded mirror at its inner edge.** Grant's framing names, in the general case,
a carve canon had already made for the single-particle case."*

**RECORDED AS A RESULT** `[WALK]`: **the arc rediscovered a ruling Grant made
three weeks before it.** WALK 3 arrives at "measure the wall, not the contents"
and canon's answer is *"the wall is a boundary condition, not where anything
happens — look at the skin."* Those are not the same conclusion. **If §3.8 is
right, WALK 3's re-posed question in §3.4 is aimed at the one radius canon says
is featureless**, and the physics it wants is one surface out.

### §3.9 — ★ MANDATORY FENCE (carried verbatim, non-negotiable)

`[CANON]` [`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):151,
the fence on §3.2 (the skin section), verbatim:

> *"**⚑ Fence on §3.2.** Observation 1 is arithmetic on Op16. Observations 2 and
> 3 are **pictures**, not results: the corpus has no certified measurement of a
> skin structure at any wall … **Neither state changes this fence:** §3.2 is
> still pictures, **nothing on `origin/main` measures a skin**, and a
> `ROOT-CERTIFIED` verdict is instrument-class by its own lane's fence. **Do not
> cite §3.2 as evidence of anything.**"*

**That fence rides on everything in §3.7–§3.8 and on any downstream use of this
record.** The skin is where the walk wants the physics to be; **nothing on
`origin/main` measures a skin.**

### §3.10 — ★ CANON CONTRADICTS THE RE-POSED QUESTION (flag-don't-fix)

`[CANON]` [`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):160,
the operational rule: *"Before asserting a wall anywhere: name (i) the
**channel**, (ii) the **axis** it lives on, and (iii) the **phase-state**
(cold/sub-yield vs saturated). A claim missing any of the three is not yet a
claim about a wall."*

**§3.4's re-posed question names none of the three.** *"Does the lattice form a
$\Gamma=-1$ saturation surface around a region"* has no channel subscript. By
canon's own rule it **is not yet a claim about a wall.**

`[CANON]` And this is not a formality —
[`wall-taxonomy.md`](../manuscript/ave-kb/common/wall-taxonomy.md):157: *"**At
$r_{sat}$, the same physical surface is FOUR different things at once**"* —
$\Gamma_{shear} = -1$, $\Gamma_{bulk} = -1$, **$\Gamma_{EM} = 0$** (*"the EM
channel is matched, not reflecting"*), and *"**row 4, the Cosserat
micro-rotation channel, has NO WALL HERE AT ALL**"* (with its own cross-grade
fence: that carve-out holds on the **separate-kernel** member of an **open**
fork, and canon records the cross-grade combine rule as **underdetermined at
$O(\alpha)$**).

`[WALK]` **The consequence is sharp and unwelcome to this arc.** WALK 1 places
the electron's **charge** on channel 4 (Cosserat). Canon places the electron
$\Gamma=-1$ wall on channels **2/3** (`[CANON]`
[`port-register.md`](../manuscript/ave-kb/common/port-register.md):72, row P4,
*"Channel(s): 2/3 (shear/bulk)"*). And canon says channel 4 **has no wall at
$r_{sat}$**. So on the arc's own channel assignment, **the surface the walk
wants to interrogate is not a wall for the channel that carries the charge**.

`[OPEN]` Either (a) the charge is not on channel 4, or (b) the wall is not the
right surface for $\mathcal{Q}$, or (c) the $\kappa$-amplitude surface that
canon does give channel 4 (`wall-taxonomy.md` §10.2) is the relevant one and
the walk is looking at the wrong radius, or (d) the cross-grade fork resolves
the other way and channel 4 does have a wall there. **This record picks none of
them.** Audit item **W3-3** — and note this lands on the step the walk states
most fluently, per §0.


## §4 — WALK 4: the trefoil vs the photon

## §5 — The open question this arc produced — and the sweep that mostly closed it

## §6 — AUDIT CHARTER

## §7 — KILL CONDITIONS

## §8 — What this record does NOT do

## §9 — Forthcoming inputs not folded in
