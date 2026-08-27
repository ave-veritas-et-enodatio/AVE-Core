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

## §6 — ★ MANDATORY FENCES (verified and quoted this session)

## §7 — Where canon CONTRADICTS the walk

## §8 — ★ AUDIT CHARTER

## §9 — ★ KILL CONDITIONS

## §10 — What this record does NOT do

## §11 — Method, and its known blind spots
