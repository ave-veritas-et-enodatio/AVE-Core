# WALK RECORD — the cold-vacuum phase-space / real-space EE mapping: a floating polyphase mesh with an asymmetric reference (2026-08-27)

**Status: WALK-GRADE, UNAUDITED, MINTS NOTHING.** Nothing in this record is a
claim, a ruling, a promotion, or a design decision. It supersedes nothing. The
audit charter is §8, the kill conditions are §9, and the routing item is
[`_orchestration/open-items/2026-08-27-cold-vacuum-ee-mapping-audit.md`](../_orchestration/open-items/2026-08-27-cold-vacuum-ee-mapping-audit.md).
**Only Grant rules on any of it.**

**Provenance.** Grant, verbatim (2026-08-27): *"what is the ee circuit mapping
between phase space and real space with a 'cold' vacuum? isolated ground/ref?"*
The orchestrator answered walk-grade in seven items; three check lanes then ran
against item 7. This record carries the walk, the check result, the fences, and
what each item is graded at.

**Grade tags used throughout, applied per sentence, not per section:**
`[MEASURED]` — reproduced this session on the shipped operator, script named;
`[CANON]` — verified in-corpus with file:line and quoted;
`[WALK]` — the orchestrator's reading, un-audited;
`[OPEN]` — raised and not answered.

---

## §0 — ★ HEADLINE: the checked item is REFUTED

**Walk item 7 — the proposal that the common-mode open explains why $\mathcal{M}$
is continuous while $\mathcal{Q}$ and $\mathcal{J}$ are integers — DID NOT
SURVIVE. All three check lanes returned REFUTES, on independent grounds, and the
orchestrator's own flagged self-refutation is the one that lands hardest.** The
walk's own verdict on its own fork, carried as the lanes worded it: **category
error, not explanation.**

The refutation in one line: **$n$ is a local constitutive modulus, not a phasor,
so an argument about phasor reference cannot reach $\int_\Omega (n-1)\,dV$ at
all.** `[CANON]` — `manuscript/ave-kb/common/boundary-observables-m-q-j.md:110`
(clm-3bwhad), verified verbatim this session: *"The canonical
gravity-as-substrate-strain prediction $n(r) = 1 + 2GM/(rc^2)$ is **refractive
index** modulation (i.e., **impedance modulation** $\varepsilon_{\text{eff}},
\mu_{\text{eff}}$ via Axiom 4's kernel $S(A)$ at each cell), NOT geometric
bond-length compression."* A per-cell index is a real magnitude ratio set by the
local saturation state. It has no phase and no phasor reference to lose.

Three further kills, each sufficient on its own, each from a different lane:

1. **The minus sign IS a reference.** $\mathcal{M} = \int_\Omega (n(\mathbf{r})
   - 1)\,dV$ `[CANON]`, `boundary-observables-m-q-j.md:19`, verified verbatim.
   The $-1$ subtracts the asymptotic unstrained vacuum $n=1$, which
   $n(r)=1+2GM/(rc^2)$ makes explicit at $r\to\infty$. So $\mathcal{M}$ is not
   "an integral over the one mode that has no reference" — it is an integral of
   a quantity **defined by its reference**. Strip the reference and $\mathcal{M}$
   diverges with the integration volume. The premise is inverted on the face of
   the formula the walk cites.
2. **The explanans does not discriminate.** The L3 lane measured the
   $\Gamma=-1$ balanced subspace to be a continuous $(z-1)$-dimensional real
   vector space — a one-parameter family $t\mathbf{b}$ satisfies $S\mathbf{v} =
   -\mathbf{v}$ to $\le 3.5\times10^{-18}$ for $t$ from $0.1$ to $137$. **Both**
   eigenspaces are continuous. Having a virtual-neutral reference quantizes
   nothing, so reference-vs-no-reference cannot produce the integer/continuous
   split it was invoked to explain.
3. **The identification it rides on is a tautology by canon's own label.**
   `[CANON]` —
   `manuscript/ave-kb/vol9/ch3-pin-port-configuration/node-scattering-multiplicity.md:159`:
   *"| A1 longitudinal scalar $=$ $+1$ common mode | projector-algebra
   **sector-orthogonality FACT** (scramble-invariant) | **true by construction,
   NOT a test** |"*, enforced by a live regression named
   `verdict_is_projector_tautology`. An identity has no explanatory content to
   spend.

**And the explanandum was never open.** $\mathcal{Q} = \mathrm{Link}(\partial
\Omega, \mathbf{F}) \in \mathbb{Z}$ and $\mathcal{J} = \mathrm{Wind}(\partial
\Omega)$ `[CANON]`, `boundary-observables-m-q-j.md:20-21`, verified verbatim.
Link and Wind are homotopy invariants: they are integers because they **count**,
and a count cannot vary continuously. $\mathcal{M}$ is continuous because it
integrates a continuous field. That answer is canonical, referenceless, and
never touches the junction spectrum.

**Consequence for the rest of this record.** Item 7 is dead and is recorded as a
closed negative. **The walk stands or falls on items 1–6 alone**, which the
lanes did not test and which this record grades independently in §3–§7. Two of
those items gained MEASURED support this session (§3, §4); two collide with
canon (§7); the bundle noun in item 6 is fenced (§6).

## §1 — Sector, regime and phase-state declaration

Stated before any substrate word, per standing discipline. **The walk mixes four
objects that share vocabulary, and most of its trouble is here.**

| # | object | space it lives in | regime | what $\Gamma$ means there |
|---|---|---|---|---|
| **O1** | node scatter $S_{ij} = 2Y_j/\sum_k Y_k - \delta_{ij}$ | $z$-port **amplitude** space $(V_{inc},V_{ref})$ at ONE node | any $Y>0$; cold is $Y$ uniform | eigenvalue of the local scatter |
| **O2** | bond reflection at a terminating load | ONE bond's impedance | saturated, $S(A)\to0$ | $\Gamma = (Z-Z_0)/(Z+Z_0)$ at a wall |
| **O3** | $\varepsilon_{11}$ bias / clause-Q reference | real-space **bound** A1 sector | quasi-static, elliptic | not a $\Gamma$ at all |
| **O4** | $(2,3)$ phase-space winding | per-tank Clifford torus | — | not a $\Gamma$ at all |

**CHANNEL/SECTOR.** This walk is about **O1**, the cold node scatter: A1
common-mode $\oplus$ balanced/differential, longitudinal port-amplitude space.
It is **not** about the Cosserat $(2,3)$ carrier. `[CANON]` sector ownership:
mass $=$ A1 dilatation, charge/spin $=$ Cosserat $(2,3)$ winding, **never one
phasor** — `manuscript/ave-kb/common/boundary-observables-m-q-j.md:25`, verified
verbatim: *"**MASS (A1) $\perp$ CHARGE/spin (T2) — never one phasor**
(def-portmp)."*

**REGIME.** COLD: $A=0$, so $S(A)=1$, so every bond admittance $Y = Y_0/\sqrt{S}
= Y_0$ and the network is uniform and **linear**. Everything item 1–6 asserts is
scoped to this regime. §4 measures exactly where that scope ends.

**PHASE-STATE.** Unsaturated, sub-yield, lossless-reactive. No $\Gamma=-1$
saturation surface exists anywhere in a cold vacuum — which is the first
collision, because canon defines all three boundary observables *at* such a
surface (§7, C1).

**★ THE HOMONYM THAT DOES THE MOST DAMAGE.** O1 and O2 both produce the symbols
$\Gamma=+1$ and $\Gamma=-1$, and they mean **opposite things**:

- In **O1**, the $+1$ eigenvalue is the common mode and $-1$ is the differential
  sector — present in **empty cold vacuum**, at every node, always. `[MEASURED]`
  §3.
- In **O2**, `[CANON]` `src/ave/solvers/vacuum_varactor_scatter.py:44-49`,
  verified verbatim: *"As the core SATURATES (S -> 0): Z_bond -> 0 => Gamma ->
  -1 (the mass cage, the Z->0 SHORT) ... It is NOT the FORBIDDEN ε-load (Z_eff =
  Z0/sqrt(S) -> inf, **Gamma=+1**; the SCOPE ASSERTION / EPSILON-LOAD FORBID)."*

So in the O2 register the A1 mass wall is $\Gamma=-1$ (a **SHORT**) and
$\Gamma=+1$ is the **forbidden** $\varepsilon$-load. The walk says "the common
mode sees $\Gamma=+1$, an OPEN" — true in O1, and it must never be read across
into O2, where $+1$ names a load the engine explicitly forbids and where the
mass wall is the short. **Two different measurements, two different regimes.**
Any restatement of this walk must name which object it means. `[WALK]` — the
walk did not.

## §2 — The walk as asked and answered

Grant's question had two halves: *what is the EE circuit mapping between phase
space and real space with a cold vacuum*, and *isolated ground/ref?* The
orchestrator's seven-item answer, carried as given, with this record's grade
appended to each. **The grades are this record's; the items are the walk's.**

| # | the walk's item, as answered | grade after this record |
|---|---|---|
| **1** | Cold, the network is a FLOATING polyphase mesh with no ground conductor; the balanced condition collapses to the traceless subspace, which canon names $T_2$ | **SUPPORTED, with a valence caveat** — collapse `[MEASURED]` §3; $T_2$ naming `[CANON]` at $z=4$ ONLY, and the ratified carrier is $z=3$ (§7, C2) |
| **2** | The COMMON mode sees $\Gamma=+1$, an OPEN — galvanically isolated, no current, nothing to reference it against. The DIFFERENTIAL modes see $\Gamma=-1$, a SHORT — a virtual neutral pinned at 0 V in every cell, with no wire | **SUPPORTED on the circuit facts, CORRECTED on the gloss** — zero port current and the 0 V virtual neutral are `[MEASURED]` §3.2 and are stronger than the walk claimed; but the star point does **not** float (§7, C3) |
| **3** | The reference structure is ASYMMETRIC: the differential subspace has a ground everywhere; the common mode has none and cannot have one | **SUPPORTED** `[MEASURED]` §3.2 and §4 — this is the walk's most robust item |
| **4** | That makes clause Q's status precise — it fixes the common-mode value, and the choice is FREE because the mode is isolated. Which is what R55 ratified: *"a ground reference is a gauge choice, not a material primitive."* The gauge freedom is a property of an open circuit, not a convention adopted | **SUPPORTED-AND-SHARPENED IN THE COLD LIMIT, with a sector cross-wire** — the freedom is `[MEASURED]` exact at $A=0$ and degrades $\propto(1-S)$ (§4); the R55 quote is `[CANON]` but sits in the findings section, not the ruling (§5); and clause Q references $\varepsilon_{11}$, a **different object** from the port amplitudes measured here (§7, C4) |
| **5** | It offers phase-only epistemology as a circuit fact: only differences are observable because only the differential subspace has a reference | **`[WALK]`, PLAUSIBLE, UNTESTED — and §4 puts a crack in it**: the asymmetry is exact only at $A=0$, so "only differences are observable" is a cold-limit statement, not a structural one. No readout model was built, so observability was never actually tested (§8, A5) |
| **6** | Phase space is a FIBER over real space; cold, every fiber is identical, so the bundle is TRIVIAL — a product — and a product carries no topology, which is the same fact as the srs manifold being topologically trivial. A defect is a region where the bundle stops being trivial, and only a GRADIENT in $Y$ can twist it | **SPLIT.** "Cold, every fiber is identical / only a $Y$-gradient can twist it" is `[MEASURED]` §3.3 and is the item's real content. The **bundle noun is fenced** `[WALK — NOT-RATIFIED]` (§6, F1). The *"same fact as"* identification is an **overreach** (§7, C5) |
| **7** | Whether the common-mode open explains $\mathcal{M}$ continuous vs $\mathcal{Q},\mathcal{J}$ integer | **REFUTED** — §0. Recorded as a closed negative |

**What survives, stated in one paragraph.** Cold, the vacuum is a floating
polyphase mesh whose every node splits its ports into one common direction that
carries **zero current at a doubled voltage** and $z-1$ differential directions
that carry **current at exactly zero volts**. The common direction is a
symmetry of the cold dynamics — a genuine gauge freedom, `[MEASURED]` exact to
machine precision — and that freedom is **not a convention; it is a property of
the operator, and it dies continuously as the medium saturates.** That is the
answer to *"isolated ground/ref?"*: **yes, cold, exactly; and only cold.**
Everything the walk built on top of that — the observables story (item 7), the
bundle noun (item 6) — is dead or fenced.

## §3 — MEASURED: the cold specialisation, reproduced

**Not taken on trust.** Reproduced this session on the shipped operators
(`admittance_scatter` and `bond_admittance_from_saturation`,
`src/ave/solvers/vacuum_varactor_scatter.py:156,188`; `scatter_matrix`,
`build_srs_net`, `scalar_tlm_step`, `src/ave/core/chiral_lattice.py:81,206,294`).
Driver: [`research/drivers/cold_vacuum_ee_mapping_walk.py`](drivers/cold_vacuum_ee_mapping_walk.py),
committed with this record, read-only on every engine primitive. Worktree
detached at `a3f4fef7` $=$ `origin/main`.

### 3.1 The cold specialisation (M1, M2)

At $A=0$ the Axiom-4 kernel gives $S(A)=1$, so $Y = Y_0/\sqrt{S} = Y_0$ at every
bond and the varactor operator collapses to the bedrock $(2/z)J - I$.
**`[MEASURED]` the collapse is BIT-IDENTICAL** (`np.array_equal`), at both
valences — not merely close.

| $z$ | varactor $=$ bedrock at $A{=}0$ | eigenvalues | $\#(+1)$ | $\#(-1)$ | $\|S\mathbf{1}-\mathbf{1}\|$ | $\|SB+B\|$, $B$ traceless |
|---|---|---|---|---|---|---|
| **3** (ratified srs carrier) | **bit-identical** | $\{+1,-1,-1\}$ | 1 | 2 | $1.9\times10^{-16}$ | $2.8\times10^{-17}$ (dim 2) |
| **4** (diamond) | **bit-identical** | $\{+1,-1,-1,-1\}$ | 1 | 3 | $0.0$ | $1.7\times10^{-16}$ (dim 3) |

**`[MEASURED]` the cold collapse to the traceless subspace is SPECIAL, not
generic** — this is walk item 1's real content and it needed a contrast to be
worth anything. Grading the admittances breaks the identification:

| $Y$ | eigenvalues | residual on $v=(1,-1,0)$ (**traceless**) | residual on $\sum_j Y_j v_j = 0$ (**balanced**) |
|---|---|---|---|
| cold uniform $[1,1,1]$ | $\{+1,-1,-1\}$ | $0.0$ | $0.0$ |
| graded $[10^{-2},1,10^{2}]$ | $\{+1,-1,-1\}$ | $\mathbf{3.4\times10^{-2}}$ | $0.0$ |
| one bond at $10^{6}$ | $\{+1,-1,-1\}$ | $0.0$ *(coincidence — see note)* | $0.0$ |

The spectrum $\{+1, -1^{(z-1)}\}$ is **invariant** under grading; what moves is
*which subspace* carries the $-1$. Cold, and only cold, that subspace is
$\{v : \sum_i v_i = 0\}$. **Note on the third row, stated so it is not
over-read:** $v=(1,-1,0)$ happens to satisfy $\sum_j Y_j v_j = 1 - 1 + 0 = 0$
for $Y=[1,1,10^6]$, so it is admittance-balanced by accident of the chosen test
vector, not evidence that grading preserves tracelessness. The graded row is the
discriminating one.

### 3.2 The circuit reading — and it is STRONGER than the walk claimed (M3)

Using the operator's own KCL (`vacuum_varactor_scatter.py:23-26`):
$V_{node} = V^{inc}_i + V^{ref}_i$ at every port, $I_i = Y_i(V^{inc}_i -
V^{ref}_i)$.

**COMMON mode**, drive $V^{inc} = a\mathbf{1}$: `[MEASURED]`

| $a$ | $V_{node}$ | port spread | $\max_i \|I_i\|$ |
|---|---|---|---|
| $+1.00$ | $+2.000000$ | $0.0$ | $1.1\times10^{-16}$ |
| $+0.25$ | $+0.500000$ | $0.0$ | $2.8\times10^{-17}$ |
| $-3.70$ | $-7.400000$ | $0.0$ | $0.0$ |

**Every individual port current is identically zero at a doubled node voltage.**
That is the textbook open circuit, and it is a stronger statement than the walk
made: the walk said the *net* current has nowhere to go; measured, **no port
carries any current at all.** Walk item 2's "no current" is `[MEASURED]`-correct
and under-claimed.

**DIFFERENTIAL mode**, $v$ with $\sum_j Y_j v_j = 0$: `[MEASURED]` at $z=3$ and
$z=4$, cold and graded — $\max_i|V_{node,i}| = \mathbf{0.0}$ exactly, while
$\max_i|I_i| = 2.0$ and $\sum_i I_i = 0.0$. **The node sits at exactly zero
volts while real current flows through it.** That is precisely a virtual neutral
with no wire. Walk item 2's second half is `[MEASURED]`-correct as stated.

**The asymmetry (walk item 3) is therefore real and measured**: the differential
sector is referenced to $0$ V at every node, in every cell, with no conductor;
the common direction has no such pin — its node voltage is $2a$, whatever $a$ is.

### 3.3 Fibers identical cold; only a $Y$-gradient twists anything (M1, M2)

`[MEASURED]` — cold, the local scatter matrix is the **same matrix at every
node** (it depends only on $z$ and on $Y$, and cold $Y$ is uniform everywhere),
so the per-node port-space structure is literally a product over the node list.
`[MEASURED]` — a per-**node**-uniform admittance **cancels** at the shunt
junction (the common factor divides out of $2Y_j/\sum_k Y_k$), so a uniform
saturation is also invisible; **only a per-BOND gradient in $Y$ changes the
operator.** This is the shipped module's own load-bearing Finding 2, stated at
`src/ave/solvers/vacuum_varactor_scatter.py:53-60` and re-measured here. Walk
item 6's *"only a GRADIENT in $Y$ can twist it"* is the item's genuine content
and it is `[MEASURED]`-correct. The **noun** it is dressed in is fenced — §6, F1.

## §4 — MEASURED: the reference asymmetry is real, and the gauge freedom is COLD-ONLY

This is the one place this record adds something the walk did not have and the
three check lanes did not run. It bears on walk items 3, 4 and 5.

**The test.** Walk item 4 says the common-mode reference *"choice is FREE
because the mode is isolated"* — that the gauge freedom is a **property of the
circuit**, not a convention. That is a testable statement about the dynamics:
if it is true, adding a constant $\delta$ to **every** incident amplitude on
**every** port of **every** node must be an exact symmetry of the lattice
evolution. Measured on the shipped srs net ($L=3$, $N=216$ nodes, degree 3) by
evolving two lattices that differ only by a global offset and tracking
$\max|(B-A) - \delta|$.

### 4.1 Cold: the offset is an EXACT symmetry `[MEASURED]`

| $\delta$ | $\max|(B-A)-\delta|$ over 8 steps |
|---|---|
| $0.001$ | $1.6\times10^{-17}$ |
| $0.01$ | $2.6\times10^{-17}$ |
| $0.05$ | $9.0\times10^{-17}$ |

**Floating-point zero.** The offset rides exactly, never decays, never couples
into the differential sector, and is conserved for as long as the run lasts.
Mechanically this is forced: $S(\mathbf{v} + \delta\mathbf{1}) = S\mathbf{v} +
\delta\mathbf{1}$ because $\mathbf{1}$ is the $+1$ eigenvector, and CONNECT is a
permutation, which fixes $\delta\mathbf{1}$. **So cold, the common-mode value is
a genuine gauge freedom of the shipped dynamics** — an exact symmetry, measured,
not a convention adopted. Walk item 4's core assertion is `[MEASURED]`-SUPPORTED
in the cold limit. Cold energy drift over 40 steps: $2.7\times10^{-15}$
relative — the evolution is unitary, so this is not a dissipative washout.

### 4.2 Saturated: the symmetry BREAKS, structurally `[MEASURED]`

Same test with the varactor reading the local $|V|$ per bond, at amplitudes far
below yield so **no clipping occurs** (verified: zero clip events):

| $\delta$ | break at **step 1** | break / $\delta$ at step 1 | after 8 steps |
|---|---|---|---|
| $0.001$ | $1.59\times10^{-6}$ | $1.585\times10^{-3}$ | $5.5\times10^{-6}$ |
| $0.01$ | $1.59\times10^{-5}$ | $1.586\times10^{-3}$ | $5.5\times10^{-5}$ |
| $0.05$ | $7.98\times10^{-5}$ | $1.596\times10^{-3}$ | $2.8\times10^{-4}$ |

**Two controls that make this a result rather than an artifact.** (i) The
breaking is present at **step 1** — it is structural, not an accumulated
integration error or a chaotic divergence. (ii) `break/$\delta$` is **constant
to three digits across a 50$\times$ span of $\delta$** — the effect is linear in
the offset, so it is a fixed property of the operator at that saturation depth,
not an amplification. (iii) Zero clip events, so it is not a saturation-cap
artifact.

### 4.3 ★ The gauge freedom degrades CONTINUOUSLY, tracking $(1-S)$ `[MEASURED]`

There is no sharp cold/hot boundary. Sweeping the field scale at fixed
$\delta = 0.01$:

| field scale | $\max A$ | $1-S(\max A)$ | break / $\delta$ |
|---|---|---|---|
| $0$ (exact cold vacuum) | $0.0$ | $0.0$ | $\mathbf{1.7\times10^{-16}}$ |
| $10^{-4}$ | $10^{-4}$ | $5.0\times10^{-9}$ | $2.3\times10^{-9}$ |
| $10^{-3}$ | $10^{-3}$ | $5.0\times10^{-7}$ | $2.3\times10^{-7}$ |
| $10^{-2}$ | $10^{-2}$ | $5.0\times10^{-5}$ | $2.3\times10^{-5}$ |
| $10^{-1}$ | $0.1$ | $5.0\times10^{-3}$ | $2.3\times10^{-3}$ |
| $3\times10^{-1}$ | $0.3$ | $4.6\times10^{-2}$ | $2.2\times10^{-2}$ |
| $6\times10^{-1}$ | $0.6$ | $2.0\times10^{-1}$ | $1.0\times10^{-1}$ |

**The breaking tracks $(1-S)$ across seven decades at a ratio of $\approx0.47$,
and is machine-zero at $A=0$ exactly.**

### 4.4 What this does and does not license

**It SHARPENS walk item 4** `[MEASURED]`: the common-mode gauge freedom is not
asserted, it is a measured exact symmetry of the shipped cold operator, and its
gauge character has a **quantitative domain of validity** — it is exact at
$A=0$ and degrades in proportion to local saturation depth.

**It puts a crack in walk item 5.** *"Only differences are observable"* is a
**cold-limit** statement, not a structural one. Wherever the medium is saturated
the common direction stops being a symmetry direction, and a non-symmetry
direction is, in principle, the kind of thing a measurement can see. `[OPEN]` —
whether it is *actually* observable is NOT settled here: no readout model was
built, and a broken symmetry is not automatically an observable. This is
audit item **A5** and it is the most interesting thing this record raises.

**It does NOT derive clause Q, and must not be read as doing so.** Clause Q
fixes a reference on $\varepsilon_{11}$ in the **bound A1 / bias sector**
(object **O3** of §1) for an elliptic solve; what is measured here is a symmetry
of **port amplitudes in the cold TLM** (object **O1**). These are different
objects in different spaces, and identifying them is exactly the cross-wire §7
C4 flags. The resemblance is suggestive and it is `[OPEN]`, not banked.

## §5 — Where canon SUPPORTS the walk

**This section exists because this arc has a documented habit of reporting only
the negative.** The walk is wrong in places (§7) and its headline item is dead
(§0), but several of its steps are not merely plausible — they are what canon
already says, and saying so is part of an honest record. Every quote below was
read at `a3f4fef7` this session, not inherited from the lane reports.

**S1 — The $A_1$/$T_2$ split of the port space is canon, verbatim, and the walk
uses it correctly.** `[CANON]` `manuscript/ave-kb/common/port-register.md:37`
(*"Taxonomy foundation `[canon]`"*): *"$A_1$ $=$ common-mode scalar/longitudinal
(dilatation, mass), $T_2$ $=$ traceless triplet (shear, the photon/GW)."* And at
the irrep leaf, `k4-port-irrep-decomposition.md:23`: *"$T_2$ eigenvalue: $-1$,
triply degenerate (basis spans traceless 3D subspace...)"*, with `:55`: *"Basis
spans the traceless 3D subspace $\{v : \sum_i v_i = 0\}$"*. Walk item 1's
identification of the cold balanced subspace with canon's $T_2$ is **the
corpus's own naming**, not an import — subject only to the $z$ caveat at §7 C2.

**S2 — The identification of the common mode with the A1 dilatation is canon,
explicitly, not a homonym.** `[CANON]`
`manuscript/ave-kb/vol9/ch3-pin-port-configuration/node-scattering-multiplicity.md:100-101`:
*"The longitudinal A1 dilatation **scalar IS the $+1$ common mode** of $S_n =
(2/n)J - I$ (the all-ones eigenvector), and it is orthogonal to the entire $-1$
differential sector by construction."* The walk was right to treat these as one
object. **The caveat is not that it is false but that it is analytic** — canon
grades the same identification *"true by construction, NOT a test"* (§0). It is
a legitimate **redirect** and an illegitimate **explanation**; canon says so in
its own words at `node-scattering-multiplicity.md:129-131`: *"A tautological-but-USEFUL
sector redirect ... Useful as a redirect; not a test result."*

**S3 — Clause Q really is a gauge/ground choice, and R55 really did rule it so.**
`[CANON]` `_orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md:58`,
verified two methods (literal grep plus a markup-stripped normalised slurp):
*"A ground reference is a gauge choice, not a material primitive."* **Precision
note, because verify-before-cite requires it:** that sentence sits in **§2 — The
findings**, not in §3 — The ruling. The *substance* is nonetheless ratified —
§3's own cut names *"where the reference sits (Q — the gauge/ground choice)"*
and ratified consequence 1 reads *"clause Q is its reference fixing."* So walk
item 4's attribution is **substantively correct and citationally loose**: it
quotes a finding as if it were the ruling clause. Related `[CANON]` at
`manuscript/common_equations/eq_axiom_5.tex:87`: clause Q is *"the quiescent
reference (Q-point) that makes the potentials defined and clause G's elliptic
solve well-posed."*

**S4 — The srs manifold really is topologically trivial, and it was measured, not
assumed.** `[CANON — research-grade]`
`research/2026-07-02_cleave-registry-pump-chern-nband_result.md:36`: *"It
reports 0 on the srs manifold because the srs manifold *is* topologically
trivial in both readings."* This is a gate-validated result — the same
integrator recovers a known $|C|=2$ that flips sign under pump reversal, and
converges across $n=24/36/48$ — so the zero is not a trivially-returned zero.
Walk item 6's triviality half has a real measured referent. **What it does not
license is the identification** the walk makes between that manifold and the
port-space bundle (§7 C5).

**S5 — The walk's central circuit picture is measured-correct and was
under-claimed.** Not canon, but this record's own measurement: §3.2's zero port
currents at a doubled node voltage, and the exact-$0$ V node with real current
flowing, are the open and the virtual neutral the walk described. Item 3's
reference asymmetry is the walk's most robust claim and it survives everything
in §7.

**S6 — Sector-ownership discipline was honoured.** The walk kept mass on A1 and
charge/spin on the Cosserat $(2,3)$ and never crossed them. `[CANON]`
`boundary-observables-m-q-j.md:25`: *"MASS (A1) $\perp$ CHARGE/spin (T2) — never
one phasor."* The cross-wire this record does flag (§7 C4) is a different one —
A1-port-amplitude versus A1-bias-sector — and it is subtler than the classic
sector error.

## §6 — ★ MANDATORY FENCES (verified and quoted this session)

**These three fences are at least as load-bearing as the walk itself.** Each was
verified independently at `a3f4fef7` — read, not inherited. A reader who takes
the walk and drops these fences will reconstruct a claim canon has already
fenced off.

### F1 — The bundle noun is `[WALK — NOT-RATIFIED]`

Walk item 6 calls phase space *"a FIBER over real space"* and reasons about a
*"TRIVIAL bundle."* **That noun is explicitly un-ratified in canon, and the leaf
that fences it also supplies the statement underneath it.**

`[CANON]` `manuscript/ave-kb/common/translation-tables/translation-phase-space.md`,
§3.2 — whose heading (`:290`) is itself the fence: *"### §3.2 — Fibered over the
lattice, not containing it **[WALK — the bundle noun is NOT-RATIFIED]**"*.

The ratifiable statement, `:292-294`: *"Standard property (5): real space sits
INSIDE phase space as the $q$-half. The substrate inverts this: real space is
**not** a subspace of the phasor coordinate space at all — canon states exactly
*coordinates-distinct-from-real-space* (`def-69f472`, §1), with a tank plane
attached at every lattice bond."*

The fence proper, `:296-307`: *"**[WALK — NOT-RATIFIED]** The natural
mathematical noun for "a phasor plane attached to every site" is a *fiber
bundle* ... This noun is **walk-level and un-ratified**: canon commits only to
the coordinates-distinct statement, and the corpus has an open adjudication
posture on fiber-bundle language ... **Minting "fiber bundle" as a substrate
noun would import the F11 abstraction the corpus explicitly contests.** The
bundle noun therefore stays WALK until Grant adjudicates; the ratifiable content
underneath it is only the canon coordinates-distinct statement plus Ax2's
transduction constant."*

The F11 clash it names, quoted at `:302` and `:303`: F11 asks whether internal
symmetries are *"irreducible abstract structure (connections on fiber bundles),
or the bookkeeping of a medium's topology and sectors?"* — and the AVE position
*"CLASHES — SECTOR $\perp$ GAUGE canon."*

**Consequence for this record.** Everything in walk item 6 that is stated in
bundle language is WALK. What survives is (a) `[CANON]` real space is not a
subspace of the phasor coordinate space, and (b) `[MEASURED]` §3.3, the cold
scatter is the same matrix at every node and only a per-bond $Y$-gradient
changes it. **Neither of those needs the noun.** This record uses the noun only
in quoting the walk, and mints nothing.

**★ METHOD WARNING, recorded because it cost this lane real time and will cost
the next one the same.** My first two searches for this fence — a literal
`git grep` and a whitespace-normalised full-corpus slurp — **both returned
ZERO hits** on the phrase *"not a subspace of the phasor"*. The text is present.
It reads `not a subspace of the phasor` with **markdown bold markers inside the
phrase**: `**not** a subspace of the phasor`. Whitespace normalisation does not
strip `*`. **A grep over this corpus that does not strip markdown emphasis will
false-negative on any phrase containing a bolded word**, which in this corpus is
most load-bearing phrases. The search that found it was a direct READ of the
section. This is a fresh instance of the standing grep-false-negative pattern,
with a new and specific cause.

### F2 — Canon's documented projection chain is LOSSY and drops exactly the winding

`[CANON]`
`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md:142`,
the row of the 5-level projection table, verbatim: *"| 2 | $\hat{\mathbf{n}}
(\mathbf{r}) \in S^2$ via Hopf fibration $SU(2) \to S^2$ | **$w_1=2$ survives,
$w_2=3$ DROPPED (lives in U(1) fibre)** |"*

The mechanism, `:146`: *"The Hopf fibration $SU(2) \to S^2$ has $U(1)$ fibre.
The U(1) fibre phase is precisely what carries the $4\pi$ closure ... **The U(1)
fibre phase — and with it the $4\pi$ closure — was dropped at the projection
step.**"*

**Why this fences the walk.** Walk item 6 treats the phase-space-over-real-space
relation as a structure from which one can read topology off cleanly. Canon's
documented projection between these levels **destroys the topological
information that matters** — $w_2=3$, the charge winding, is precisely what does
not survive. So a projection argument in this neighbourhood cannot be assumed
faithful; the one canon actually wrote down is not.

**Scope honesty, and it matters.** This is the projection chain the corpus
documents at **this** leaf, running Cosserat $\omega$-field $\to SU(2) \to S^2
\to$ EM polarization. **It is not the phase-space-to-real-space map of walk item
6** — different objects. I am not claiming it is the only projection chain in
the corpus; I read this one and enumerate it. What it establishes is that
**losslessness of a projection is something to be shown, never assumed**, and
that the corpus has a worked case where the winding is exactly what is lost.

### F3 — Real-space trap and phase-space winding measured physically DECOUPLED

`[CANON]` `manuscript/ave-kb/common/relational-cancellation-identity.md:266`,
verbatim: *"detuning the carriers to $\omega_b:\omega_s = 2:3$ makes the global
phases wind **2:3** (measured ratio 0.644 vs the carrier ratio 0.667) — the
winding follows the carriers ... **while the static topological charge
$\mathrm{Link}(\partial\Omega,F)$ on its separate real-space coordinate does not
move**."*

The primary measurement, `research/2026-06-24_engine-phase-space-winding_result.md:44-45`
(PR #417), verbatim: *"the winding ratio of the phase-space orbit is set by
$\omega_b:\omega_s$, **the carrier ratio** — an **oscillator
(Lissajous-of-the-carriers) artifact** — NOT by a topological (2,3) that would
be carrier-independent."* And the discriminator, `:33`: *"the winding ratio
tracks $\omega_b:\omega_s$ continuously (1:1$\to$0.93, 2:3$\to$0.65,
3:2$\to$1.54, 1:2$\to$0.48), **which a topology-protected charge could NOT do**."*

The consequence canon drew, `[CANON]`
`manuscript/ave-kb/common/engine-capability-map.md:23` (a Rule-12 relabel):
*"both internal dynamical loci now NEGATIVE: winding + H_couple does **NOT**
pin the dispersing core ... the **(2,3) winding RIDES the cage as STATIC
charge** (`Link`, un-walked-back), it does not pin the mass."*

**Why this fences the walk.** The walk's item 6 proposes that a defect is *"a
region where the bundle stops being trivial"* — one object with a real-space
location and a phase-space twist, coupled. **Measured, they are not coupled.**
The phase-space winding follows the carrier detuning; the real-space Link does
not move. Two loci, tested, **both NEGATIVE for a joint dynamical object**
(#415 real-space, #417 phase-space). Any restatement of item 6 that makes the
real-space defect and the phase-space winding two aspects of one twisted bundle
is proposing precisely what these two tests looked for and did not find.

## §7 — Where canon CONTRADICTS the walk

Five collisions, ordered by how much they cost. **Flag-don't-fix: no canon was
edited. Each is surfaced with verbatim evidence for Grant to rule on.**

### C1 — A cold vacuum has NO $\Gamma=-1$ surface, but canon defines all three observables AT one

`[CANON]` `manuscript/ave-kb/common/boundary-observables-m-q-j.md:11`, verified
verbatim: *"At every $\Gamma = -1$ saturation surface $\partial\Omega$ in the
substrate — the boundary where Axiom 4's kernel ... reaches $S(A) \to 0$
locally — exactly **three integrated quantities are externally observable**."*

Cold means $A=0$, $S(A)=1$ **everywhere**; no saturation surface exists. So the
walk's item-7 move did not merely mis-explain the observables — **it reached for
them from a regime in which canon does not define them.** This is the
regime/phase-state error underneath the §0 refutation, and it is independent of
the phasor/modulus category error. It also cuts against any future attempt to
re-run item 7 in a repaired form: the observables live on the saturated wall,
the junction spectrum being discussed is the cold node scatter, and §1's O1/O2
homonym is the bridge that does not exist.

### C2 — The $T_2$ name the walk uses is canon at $z=4$ ONLY; the ratified carrier is $z=3$

Walk item 1 says the cold balanced condition *"collapses to the traceless
subspace, which canon names $T_2$."* True at $z=4$ `[CANON]`
(`k4-port-irrep-decomposition.md:23,:55`, quoted §5 S1). **But that leaf is
$z=4$-only**, and the production carrier is not $z=4$.

- `[CANON]` `unified-engine-design-doctrine.md:222`, verbatim: *"**Decision 1
  (RATIFIED, Grant 2026-06-25): the production engine substrate is the chiral
  z=3 srs net.**"*
- `[CANON]` — the code says the coverage gap in its own words,
  `src/ave/core/chiral_lattice.py:79`: *"# Op5 trivalent scatter — DERIVED, new
  instantiation (**canon: n=4 only**)"*.
- **Method, three ways, on the 310-line irrep leaf:** a full read; a
  case-insensitive line grep for `srs|trivalent|degree-3|z ?= ?3` → **0 hits**;
  a markup-stripped whitespace-normalised slurp for the same → **0 hits**. The
  leaf's operator is $S = (1/2)\mathbf{1} - I$, i.e. $z=4$.
- `[MEASURED]` §3.1: at $z=3$ the balanced eigenspace is **2-dimensional**, so
  canon's *"$T_2$ ... **triply degenerate**"* and *"traceless **3D** subspace"*
  have **no referent** on the ratified carrier.

`[CANON]` canon names the $z=3$ balanced sector by **multiplicity, never by
irrep** — `node-scattering-multiplicity.md:60-61`, verbatim: *"**$S_3$**:
$\{+1\times 1,\ -1\times 2\}$ → differential multiplicity **2**. **$S_4$**:
$\{+1\times 1,\ -1\times 3\}$ → differential multiplicity **3**."*

**Asymmetry that saves half the item:** the $+1$/common half carries to $z=3$
cleanly — `[MEASURED]` §3.1 at both valences. The **common-mode half of the
entire walk is valence-robust; the $T_2$ label is not.** `[OPEN]` — whether the
$z=3$ irrep naming gap gets closed is a Grant call, not this record's.

### C3 — The star point does NOT float; the walk's own physical gloss is wrong

The framing this walk was checked against reads: *"drive all ports equally and
KCL has nowhere to send the net current, so the star point floats."*
`[MEASURED]` §3.2 — **it does not float. It sits at exactly $2a$**, single-valued
across every port (spread $0.0$), for every drive tested, at both valences and
under grading. What is zero is **every port current**, not the node voltage.

This is a **correction, not a demolition**: open-circuit voltage doubling at a
defined node with zero port current *is* an open, so the walk's conclusion
("$\Gamma=+1$ is an OPEN, no current") survives — §5 S5 — while its stated
*reason* ("the star point floats / has no defined potential") is measured-false.
The distinction matters because "floats" is what makes the leap to "nothing to
reference it against" feel licensed, and that leap is what item 7 died on.
`[CANON]` runs the same way: `k4-port-irrep-decomposition.md:85` glosses this
eigenvalue as *"like a **DC bias** passing through a reflector unchanged"* — a
**referenced** object, not an isolated one.

### C4 — Walk item 4 cross-wires the A1 PORT amplitude with the A1 BIAS sector

Item 4 says clause Q *"fixes the common-mode value."* Two different objects
(§1, O1 vs O3):

- **Clause Q's reference** is on $\varepsilon_{11}$, the bound-sector bias, for
  an elliptic solve. `[CANON]` `manuscript/common_equations/eq_axiom_5.tex:87`:
  *"the **quiescent reference (Q-point) that makes the potentials defined and
  clause G's elliptic solve well-posed** — without it the conserved data is
  unpinned far from sources and the potential problem has no boundary
  condition."*
- **What §4 measured** is a symmetry of **port amplitudes** $(V_{inc},V_{ref})$
  under the cold TLM scatter-and-connect.

These live in different spaces and are pinned by different constructions. The
resemblance is real and interesting — both are a free additive constant on an
A1-labelled object — but **identifying them is an assertion, not an
observation**, and this record does not make it. Compounding it: the A1/bulk
channel is **DEMOTED at HEAD**. `[CANON]`
`k4-port-irrep-decomposition.md:118` and `common/port-register.md:49` both carry
*"🔴 [DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead]"*, and the
R40 replacement states the A1 slot has *"no independent propagating branch, no
port and zero longitudinal characteristic speed."* **What survives untouched is
exactly what this walk uses** — R40's own audited rationale,
`k4-port-irrep-decomposition.md:300`: *"the irrep decomposition (group theory)
**survives untouched**, but the A1 propagation-speed formula consumes the
phantom."* So the port-space algebra is live; "A1 as a propagating bulk channel"
is not, and no restatement may quietly use the second.

### C5 — "The same fact as the srs manifold being topologically trivial" is an overreach

Item 6 asserts the trivial-product bundle and the srs manifold's triviality are
*"the same fact."* They are two different statements about two different
objects:

- The measured result `[CANON — research-grade]` is a **Chern number of the srs
  Bloch band manifold over a $(k_z,\theta)$ parameter torus**
  (`2026-07-02_cleave-registry-pump-chern-nband_result.md:36`).
- The walk's object is a **port-amplitude structure over the node lattice**.

Different base spaces, different fibers, different invariants. Additionally, the
implication runs one way only: a trivial bundle forces $C=0$, but $C=0$ does not
force triviality — the Chern number is one invariant among several, and a
vanishing one is not a proof of a product structure. **The walk asserts an
equivalence where at most a one-directional consistency holds.** `[MEASURED]`
§3.3 gives item 6 the content it actually has — cold, the scatter is literally
the same matrix at every node, and only a per-bond $Y$-gradient changes it —
and that content needs neither the equivalence nor the noun.

## §8 — ★ AUDIT CHARTER

## §9 — ★ KILL CONDITIONS

## §10 — What this record does NOT do

## §11 — Method, and its known blind spots
