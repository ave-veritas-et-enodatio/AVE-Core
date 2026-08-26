# LENS RECORD — the OVER-BRACED CHIRAL CRYSTAL walk: the knot may be in the stress, not the material (2026-08-26)

**Status: NEW LENS, WALK-GRADE, UNAUDITED. Nothing here is a claim, a ruling,
or a design decision.** It is proposed as a candidate REPLACEMENT framing for
the autonomous-harmonic-balance lens
([`2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`](2026-08-25_autonomous-harmonic-balance-lens_RECORD.md)),
whose core criterion was measured dead in review. It **requires an adversarial
audit before any part of it reaches a prereg** — the charter is §8, the kill
conditions are §9, and the routing item is
[`_orchestration/open-items/2026-08-26-overbraced-crystal-audit.md`](../_orchestration/open-items/2026-08-26-overbraced-crystal-audit.md).

**Why this record is written defensively.** The lens it replaces died at audit
on the step its author was *least* worried about — §3.1 of that record asserted
a source-free solution "cannot belong to the scaffold: there is nothing else it
could belong to", and §5.3 of the *same document* listed three other things it
could belong to. An unhedged absolute in a walk-grade document is the tell. So:
every statement below carries a grade tag, the weaknesses section (§7) is
written to be at least as prominent as the proposal, and the record ships its
own kill conditions.

**Provenance.** Grant, verbatim (2026-08-26), transcribed exactly:

> *"for question two I want you to think through how you can tie not in a
> spiderweb, except that spider is an over braced chiral chrystal."*

[Reading the two typos: *"tie not"* reads as *"tie a knot"*; *"chrystal"* reads
as *"crystal"*. Transcribed unaltered above per the verbatim-quote discipline;
the reading is the orchestrator's and is itself part of what an audit may
challenge.]

---

## §0 — Grade tags used in this record

Every substantive statement below carries one of these. A statement with no tag
is a structural/navigational sentence, not a claim.

| tag | meaning |
|---|---|
| **[WALK]** | the walk's own reading. Chat-grade. Un-audited by construction. |
| **[ASSEMBLY]** | assembles pieces the corpus already owns into a statement none of them makes alone. The pieces are cited; the assembly is not canon. |
| **[EXTERNAL-UNRETRIEVED]** | asserted from discipline knowledge with **no retrieval performed in this session**. Maxwell–Calladine, Kane–Lubensky, Berry/Chern, and the RF free-running-oscillator characterisation are **all** in this class. Treat as *"a claim about what the external literature says"*, not as literature. |
| **[MEASURED-ELSEWHERE]** | a numeric finding produced by the in-flight review of the autonomous-HB lens, attributed to that lane, not re-run here. |
| **[CANON-VERIFIED]** | read and quoted from the corpus **in this session**, with file:line. This tag is an addition to the four the dispatch named, because §6 needed to distinguish *"I read this"* from *"I assembled this"*. |

**A note on the [EXTERNAL-UNRETRIEVED] class.** Four load-bearing external
objects are named in this record and **not one of them was retrieved**. If the
audit does nothing else, it should retrieve those four, because three of the
walk's steps rest on them and the walk has no independent way to tell a correct
memory from a confident one.

## §1 — What this walk responds to: the measured state of the autonomous-HB lens

> **★ EVERY FINDING IN THIS SECTION IS A REVIEW-PHASE FINDING, VERIFY PENDING.**
> The adversarial VERIFY pass on the autonomous-HB lens is still in flight. These
> are reported here as **[MEASURED-ELSEWHERE]** — attributed to that lane, not
> re-run in this session, not this record's own results. If any of them moves,
> the motivation for this entire walk moves with it.

The autonomous-HB lens proposed replacing the driven existence test with a
source-free nonlinear eigenvalue problem: *find `v ≠ 0` solving
`e^{iθ} v = M(S(|v|)) v` with no sources.* The review measured the following.

**CRITICAL — the existence criterion cannot fail.** `M` is unitary in the
`Y`-weighted inner product for **any** `S`-field: measured
`||M^H diag(Y) M − diag(Y)||_max / ||diag(Y)||_max = 3.083e−16` on
`build_srs_net(2,'right')`, `ndof=192`. So `|e^{iθ}| = 1` holds for every
eigenvector — 192 source-free solutions on empty cold vacuum, with no electron,
no winding and no saturation anywhere in the problem.
**[MEASURED-ELSEWHERE, VERIFY PENDING]**

**CRITICAL — the seed is the selection device.** Six independent random
topologically-trivial seeds gave six *different* exact autonomous solutions
(`θ = 2.499991678, 0.721070511, 2.515633304, …`), all passing `r_auto` at or
near machine zero, all topologically trivial and delocalized.
**[MEASURED-ELSEWHERE, VERIFY PENDING]**

**CRITICAL — the production winding observer is a pure function of the seed.**
`srs_cage_winding.py:480` returns `np.abs(self.b_w)[:, None] * self.e_w`;
replacing the entire dynamical DOF with pure random noise leaves the read
unchanged at `(2,3)`. **[MEASURED-ELSEWHERE, VERIFY PENDING]** *(The docstring
directly above it states the design intent without concealment —
`srs_cage_winding.py:402`, `:478-482`: "the FIXED winding template ê_w carries
the (2,3) winding integer (conserved by construction)"; "the winding integer
lives in ê_w, |b_ω| only modulates it". The measured finding is that a reader
built this way cannot return "no".* **[CANON-VERIFIED]**)

**CRITICAL — there is no wound sector on the object the lens solves.** The HB
unknown is a scalar / `A1`-adjacent port phasor; every `(2,3)` reader consumes a
Cosserat 3-vector `ω` field. That is an `A1`/`T2` cross-wire.
**[MEASURED-ELSEWHERE, VERIFY PENDING]** *(The solver says so about itself:
`harmonic_balance_srs.py:147-149` — "the A1-adjacent longitudinal slot. The
T2/Cosserat channel is NOT wired in (A1 perpendicular to T2,
master-equation.md:20); no winding observable exists here."* **[CANON-VERIFIED]**)

**MAJOR — the operating point is free.** Sweeping the imposed norm gave a
continuous family of exact solutions, `A_max 0.211922 → ~0.91`, all at
`r_auto ~5e−15`, with `θ` moving only `2.410 → 2.343` across a 5× amplitude
range. **[MEASURED-ELSEWHERE, VERIFY PENDING]**

**MAJOR — the RF prior art was imported without its amplitude-selecting
mechanism.** An RF free-running oscillator has an *isolated* solution because
the circuit is **lossy with an active device**: small-signal gain grows the
oscillation, large-signal compression balances the loss, and the crossing pins
the amplitude — an Andronov–Hopf limit cycle. Axiom 3 removes exactly that.
**[MEASURED-ELSEWHERE, VERIFY PENDING]** *and the characterisation of RF
oscillator HB is itself* **[EXTERNAL-UNRETRIEVED]**.

**Context finding — the termination WAS the boundary.** The review also found
the srs carrier is a **periodic torus with no free boundary** (bijective connect
map, `interior_mask.all() == True`, uniform degree 3). Removing the scaffold
therefore removes the only channel through which a topological *boundary*
condition was to be imposed. **[MEASURED-ELSEWHERE, VERIFY PENDING]**

**The one-line diagnosis this walk starts from.** Losslessness (Ax 3) removed
the dissipative amplitude-selector that the imported RF analogy was silently
relying on, and nothing structural was put in its place — so existence became
generic and selection fell to the seed. **[WALK]**


## §2 — The picture: you cannot thread a knot through a crystal

**[WALK] throughout this section.**

Tying a knot in a spiderweb works because a web has two things a crystal does
not: **slack**, and **strands free to pass each other through the embedding
space**. You pull a bight through a loop. Both operations need the material to
move relative to itself.

A crystal has frozen connectivity. Node `i` is bonded to node `j` and stays
bonded to node `j`; no strand can pass through another, and there is no slack to
pull. So **on this picture the knot cannot be in the material** — there is
nothing in the material that can be re-routed to hold it. **[WALK]**

The candidate the walk proposes: *the knot is in the **stress**.*

An **over-braced** (hyperstatic) structure has more constraints than degrees of
freedom. The excess does not go away — by Maxwell–Calladine it appears as
**states of self-stress**: distributions of bar tension and bond moment in
equilibrium with **zero external load**. A load-free equilibrium. Chirality
makes those states **handed**. **[EXTERNAL-UNRETRIEVED for the
Maxwell–Calladine content; [WALK] for the identification with the knot.]**

The image, in Grant's own frame: **the spider does not thread a knot; it builds
the web already twisted, then braces it until the twist has nowhere to relax
to.** **[WALK]**

> **⚠ This picture is not new to the corpus, and §6 is where that is dealt
> with.** "Over-bracing" is already a corpus term with an assigned meaning, and
> the corpus already describes a handed, load-free, rest-state twist in almost
> these words — assigned to a *different object*. Read §6 before treating any of
> §2–§5 as novel.


## §3 — The candidate: a STRUCTURAL amplitude-selector instead of a dissipative one

### 3.1 The repair, stated as narrowly as it can be stated

The autonomous-HB lens inherited its confidence from RF oscillator practice,
where the amplitude is isolated because gain compression balances loss. That
selector is **dissipative**, and Axiom 3 forbids it. **[MEASURED-ELSEWHERE for
the diagnosis; [EXTERNAL-UNRETRIEVED for the RF characterisation.]**

The walk's proposal is that the right class of amplitude-selector for a
**lossless** medium is a **structural** one — a constraint count, not an energy
balance. Over-bracing is a structural property: it is a statement about the rank
of a constraint system, and it survives Ax 3 untouched because it never mentions
loss. **[WALK]**

**That is the entire claim of §3, and it is a claim about a CLASS of mechanism,
not about a mechanism.** It says: *look for the selector in the structure.* It
does not exhibit one, does not say what it selects, and does not say the
selected value is right. §7.2 is where that gap is priced honestly.

### 3.2 Why the class-level argument is worth something anyway

A wrong *class* of mechanism is a failure mode that repeats. The autonomous-HB
lens did not fail because of an arithmetic slip; it failed because a mechanism
was imported together with its picture and *without* the part of the picture Ax 3
deletes. Naming the class explicitly ("lossless media select structurally, not
dissipatively") is a check that would have caught it at design time.
**[WALK]**

Under the consensus-bias symmetric standard: the equivalent move in an SM/QED
context — *"this selection cannot be dissipative in this theory, so look for a
topological/structural selector"* — would be regarded as ordinary reasoning, not
a stretch. The tag it earns is *organizing*, not *predictive*, in both cases.
**[WALK]**


## §4 — The proposed discrete question: degeneracies, not existence

### 4.1 Why existence went generic

`M` stays unitary at every amplitude **[MEASURED-ELSEWHERE, VERIFY PENDING]**,
so its eigenvalues slide around the unit circle and never leave it. Nothing
"opens" or "closes" as amplitude is swept. A criterion phrased as *does a
solution exist* therefore has no way to answer no. **[WALK]**

### 4.2 What is discrete on a unitary family

What *is* discrete is where eigenvalues **collide**. In a one-parameter sweep,
degeneracies are isolated. Degeneracies are also where eigenvectors twist, and
the twist accumulated on a closed loop around a degeneracy is a **counted
integer** — Berry phase / Chern number / Weyl charge — which in a chiral crystal
is **signed**. **[EXTERNAL-UNRETRIEVED — none of Berry, Chern or Weyl was
retrieved in this session.]**

Two properties the walk claims for such an integer, both **[WALK]**:

1. **Nothing is seeded.** It is computed by transporting eigenvectors around a
   closed loop in parameter space. There is no template to plant an answer in.
   This is the direct structural answer to §1's finding 3.
2. **It can return zero.** A template-based reader structurally cannot produce
   "no"; a transport integral can, and often does.

> **⚠ A structure this proposal does not name, and needs.** A Chern-type
> invariant on an occupied manifold needs a **gap** to define "occupied". `M` is
> **unitary**, not Hermitian — its spectrum lies on a circle, where "below the
> gap" is not defined without an extra choice (a branch cut / a quasi-energy
> zone, the Floquet-style construction). The walk asserts the integer exists
> without supplying that choice. **[WALK — flagged as a hole, audit item B4.]**

### 4.3 An inversion worth recording

The **periodic-torus** finding is *fatal* for the driven framing — a periodic
carrier has no free boundary, so there is no surface on which to impose a
boundary condition, and the termination that was removed **was** the boundary
**[MEASURED-ELSEWHERE, VERIFY PENDING]**.

But it is exactly what a **band-topology** framing wants: a periodic lattice has
a Brillouin zone, and Brillouin-zone-like parameter tori are where transported
invariants live. The same measured fact reads as a kill for one framing and a
prerequisite for the other. **[WALK]**

*This inversion is the walk's cleanest single move. It is also the one most
likely to be doing rhetorical rather than physical work — see §7.4 and audit
item B5.*

### 4.4 A count — ★ FLAGGED, NOT CLAIMED

Which side of the isostatic line the vacuum sits on is decided by arithmetic.
The walk's arithmetic, stated so it can be attacked:

- a Cosserat node carries **6 DOF** (3 translation + 3 microrotation);
- a **rigid-jointed** bond transmits **6 constraints** (3 force + 3 moment);
- srs is **z = 3**, so bonds per node = 3/2, and constraints per node
  = `3 × 6 / 2 = 9` against 6 DOF;
- **over-braced by 3 per node.**

> **★ THREE WARNINGS, all of which the audit should treat as live.**
>
> **(a) This is a coordination-number estimate, NOT a Maxwell–Calladine index.**
> The real object is `rank` of the equilibrium (or compatibility) matrix on the
> **actual srs connectivity**. Per-node coordination arithmetic ignores rank
> deficiency, and rank deficiency is exactly what the count is trying to
> measure. On the corpus's own prior computation, per-node arithmetic and exact
> rank **disagreed by a factor of ~2.7** (§6.2).
>
> **(b) The corpus has a documented habit of finding meaningful-looking small
> integers.** The standing caution is recorded at
> [`_orchestration/2026-06-07_electron-synthesis-epic.md`](../_orchestration/2026-06-07_electron-synthesis-epic.md):189 —
> *"over-determination of ¼ alone = the coincidence-magnet tell"*
> **[CANON-VERIFIED]**. A "3" landing next to a `z=3` carrier and a `(2,3)`
> winding is **a tell to check, not a finding.**
>
> **(c) The "6 constraints per bond" input is NOT the corpus's own convention.**
> The corpus has an implemented micropolar constraint model and it uses **3 rows
> per bond**, not 6 — see §6.2. Under that convention the same arithmetic gives
> `3 × 3 / 2 = 4.5` constraints per node against 6 DOF, i.e. **under**-braced by
> 1.5 — *the opposite sign*. **The answer to Q1 flips on a modelling choice the
> walk made without knowing the corpus had already made a different one.**


## §5 — The re-ranking this implies: the bracing IS the couple-stress

**This is the walk's main practical consequence, and the part with the most
canon support (§6.1) — which is also why it is the least novel part.**

Bracing that carries **moment** is bending stiffness. In this substrate, the
channel that carries moment between adjacent nodes is the **Cosserat
couple-stress `γ_c`** — canon's own reading, *"Transformer mutual inductance
gradient / reluctance / transconductance — couples adjacent flywheel
rotations"*, [`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):101
**[CANON-VERIFIED]**.

And that channel is exactly what the solver under discussion says it does not
have: *"The T2/Cosserat channel is NOT wired in (A1 perpendicular to T2,
master-equation.md:20); no winding observable exists here"*,
[`harmonic_balance_srs.py`](../src/ave/solvers/harmonic_balance_srs.py):147-149
**[CANON-VERIFIED]**.

**So under this walk the scalar-only solver is a PIN-JOINTED web.** Pin joints
transmit force and not moment; a pin-jointed assembly has no bending stiffness,
carries no moment-bearing self-stress, and — on this walk's reading — can hold no
knot. **[WALK]**

**The re-ranking.** In the autonomous-HB record, the missing T2 wiring was
listed as caveat 5 of 5: *"The T2 blocker is untouched. This lens changes how
the state is found, not what can be read off it"*
([`2026-08-25_autonomous-harmonic-balance-lens_RECORD.md`](2026-08-25_autonomous-harmonic-balance-lens_RECORD.md):148-149)
**[CANON-VERIFIED]** — i.e. a blocker on two *observables*. Under the present
walk it is not a blocker on observables at all: **it is what makes the object
under test representable in the first place.** A pin-jointed model of a
moment-bearing structure is not a partial model of it; it is a model of a
different structure. **[WALK]**

**What this does and does not buy.** It does not make the T2 wiring easier, and
it does not say the wired model will find anything. What it changes is the
*priority argument*: the T2 channel stops being "needed for the readout" and
becomes "needed for the physics to be present at all". If the audit sustains
only one item from this record, this is the one with a downstream consequence
attached. **[WALK]**

**And the honest discount.** §6.1 shows the corpus already identifies
over-bracing with couple-stress, in a pedagogical leaf, in almost these words.
So the re-ranking is a *re-derivation* of an existing corpus identification
applied to a solver that post-dates it — useful as a priority argument, **not**
a new physical identification. **[CANON-VERIFIED / WALK]**


## §6 — Canon collisions and prior art found while writing this record

**★ This is the most valuable section in the record, and it is mostly bad news
for the walk's novelty.** Every term the walk reached for was grepped before use.

### 6.0 COINAGE GREP (whole tracked repo, `git grep -I -i`, 2026-08-26 at `origin/main` = `a3f4fef7`)

| term | files | hits | verdict |
|---|---|---|---|
| `self-stress` | 5 | 12 | **ALREADY EXISTS with a meaning** — reuse, do not overload |
| `over-braced` | 21 | 37 | **ALREADY EXISTS with a meaning** — reuse, do not overload |
| `overbraced` (unhyphenated) | 3 | 29 | same object, alternate spelling in code |
| `over braced` (spaced) | 0 | 0 | — |
| `hyperstatic` | 0 | 0 | **0 hits — a coinage.** Prefer canon's `over-braced` |
| `isostatic` | 30 | 58 | **ALREADY EXISTS with a meaning** — reuse |
| `Maxwell-Calladine` | 1 | 7 | exists, in the driver; `Calladine` alone: 22 files / 41 hits |
| `Kane-Lubensky` | 0 | 0 | 0 hits (`Lubensky` alone also 0) — would be a coinage |
| `Berry phase` | 2 | 3 | present, sparse |
| `Chern` | 67 | 364 | **heavily used — and already COMPUTED on this carrier**, see §6.3 |

**Consequence: the walk introduces no new term.** Where it reached for
`hyperstatic` and `Kane–Lubensky` (0 hits each), canon's existing `over-braced` /
`isostatic` cover the first and the second should be introduced, if at all, only
with retrieval attached. **[CANON-VERIFIED]**

### 6.1 ★ "Over-bracing = couple-stress" is ALREADY the corpus's identification

[`trampoline-analogy-primer.md`](../manuscript/ave-kb/common/trampoline-analogy-primer.md):155,
verbatim:

> *"**The chirality lives in the twist, not the stretch.** What laces the
> micro-gyroscopes together is the **couple-stress** — the handed over-bracing
> ($\sigma^A$) of Steps 2–3 — an *inductive* coupling (mutual-$\mu$ between
> neighbours), not a stretch."*

and [`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):190
— *"Coupling through $\sigma^A$ (antisymmetric stress = couple-stress source from
Step 3 over-bracing)"*; :560 — *"The Cosserat couple-stress contribution to $G$
depends on the **over-bracing magnitude** $u_0$…"*. **[CANON-VERIFIED]**

**§5's central identification is therefore not new.** *(Scope note, stated so
the finding is not inflated: both leaves carry `no-claim` frontmatter — they are
pedagogical/synthesis leaves, so this is canon-adjacent framing, not a
claim-graded node. It still establishes the term's meaning, which is what a
coinage-grep is for.)* **[CANON-VERIFIED]**

### 6.2 ★ The Maxwell–Calladine count Q1 asks for has ALREADY BEEN RUN — on the wrong carrier, with a different bond model

[`research/2026-06-15_alpha-crystal-mc-count_result.md`](2026-06-15_alpha-crystal-mc-count_result.md),
driver `src/scripts/vol_1_foundations/alpha_crystal_mc_count.py`. Exact sparse-SVD
rank, `f = DOF − rank`, `s = #C − rank`, `f − s = DOF − #C`. **[CANON-VERIFIED]**

Three findings in it that bear directly on this walk:

**(i) The micropolar (Cosserat) bond model is 3 rows per bond, not 6.**
`alpha_crystal_mc_count.py:259-275`, verbatim: *"We model each bond as
constraining all 3 components of the relative GENERALISED displacement at the
bond midpoint: `g = (u_j − u_i) − (1/2)(phi_i + phi_j) × r_ij` … This yields 3
rows per bond (the full vector compatibility), the standard Cosserat-rod /
micropolar-lattice constraint."* **This is the modelling choice §4.4(c) flags,
and it flips the sign of the walk's answer.** **[CANON-VERIFIED]**

**(ii) On that convention the primary micropolar lattice is EXACTLY isostatic.**
Table, `:71` — `L=8, N=128, DOF=768, #C=768, rank=672, f=96, s=96, f−s=0`.
Ninety-six floppy modes *and* ninety-six self-stress states, Maxwell–Calladine
index exactly zero. **That is the ISOSTATIC side of Q1 — the side §7.1 says the
rich topological mechanics lives on.** **[CANON-VERIFIED]**

**(iii) Per-node arithmetic and exact rank disagreed badly there.** The bond
multiplicity was 16/node; the exact independent-constraint coordination was
`z_eff → 6`. The doc's own words, `:154-155`: *"the **independent-constraint**
coordination (rank-based z_eff) is the **isostatic 6**, because rank(R) ≤ 3N−6
regardless of bond count."* **[CANON-VERIFIED]** — the empirical basis for
§4.4(a).

**The gap that keeps Q1 genuinely open:** that count was run on the **achiral
z=4 diamond**, and the lattice identity was ratified the *following month* the
other way. [`axiom-register.md`](../manuscript/ave-kb/common/axiom-register.md):147:
*"The lattice IDENTITY (D1) is **RATIFIED (Grant 2026-07-03, PR #486): the
chiral z=3 srs net is the production carrier**; the achiral z=4 diamond is
re-tagged a non-canonical…"* **[CANON-VERIFIED]**. So the corpus has the
machinery, the conventions and a worked precedent — on a carrier that is no
longer the production one, and on an **achiral** lattice, which is precisely the
property the walk says makes the self-stress states handed.

**Also already named as outstanding work:**
[`common/claim-quality.md`](../manuscript/ave-kb/common/claim-quality.md):1666 —
*"build the bond-based micropolar constitutive model that DOES transfer to the
z=3 srs carrier, and re-run the k·p there"*. **[CANON-VERIFIED]** Q1 is adjacent
to, and possibly the same work as, an item the corpus already carries.


### 6.3 ★ A Chern number has ALREADY been computed on the srs carrier — and it is ZERO

[`research/2026-07-02_cleave-registry-pump-chern-nband_result.md`](2026-07-02_cleave-registry-pump-chern-nband_result.md),
headline: *"The genuine 8-band srs-cell occupied-manifold Chern over the
`(k_z, θ)` registry torus is **C_N = 0 in BOTH readings AND BOTH
enantiomorphs** (gapped, grid-converged n=24/36/48)"*, with a validate-on-known
gate that both recovers a known 0 and detects a known `|C| = 2`. Its `:36`:
*"It reports 0 on the srs manifold because the srs manifold *is* topologically
trivial in both readings."* Status **NULL-CONFIRMED-FINAL**; the register entry
is `clm-clvchn`, cross-referenced from
[`vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md):445.
**[CANON-VERIFIED]**

**What this does and does not do to §4.2.** It is **not** the same computation:
that Chern was taken on a **cold, unsaturated** 8-band Bloch Hamiltonian over a
**registry** parameter `θ` (a screw-displacement pump), whereas §4.2 proposes an
**amplitude** parameter on the **saturating** operator. Different manifold,
different parameter.

But it is a headwind and it sharpens the question **[ASSEMBLY]**: if the cold srs
manifold is topologically trivial, and saturation deforms continuously away from
cold, then a nonzero invariant on the saturated family must be **born at an
amplitude-driven gap closure**. That is a strictly sharper (and more falsifiable)
version of §4.2 than the walk stated — and it is also a much heavier lift, since
it requires exhibiting the closure, not just the integer. **Routed, not
claimed.**

### 6.4 ★★ The handed load-free rest-twist is ALREADY ASSIGNED — to the vacuum ground state, not to a particle

[`trampoline-analogy-primer.md`](../manuscript/ave-kb/common/trampoline-analogy-primer.md):157,
verbatim:

> *"**At rest the fabric is wound, not spinning.** The twist-lacing winds every
> gyroscope to a handed **rest-angle $\theta$** — that *is* the chirality, stored
> as elastic energy. But the rotation **rate $\omega = 0$ at rest**: the
> gyroscopes sit cocked, they do not turn. … The handed winding is **parity**,
> not angular momentum"*

**[CANON-VERIFIED]**

This is the walk's §2 image — *built already twisted, braced until the twist has
nowhere to relax to* — **already in the corpus, and assigned to the empty
vacuum**. Every cell, everywhere, with no particle present.

**The objection this raises, which the walk does not answer.** If the ubiquitous
ground state is itself a handed load-free held twist, then *"the electron is a
self-stress state"* does not by itself pick out an electron. **The walk needs a
statement of what distinguishes the particle's self-stress from the vacuum's,
and it does not have one.** This is audit item B6 and kill condition K3.
**[ASSEMBLY]**

The same passage continues *"Spin-up is what excitation does. Apply a field or
trap a soliton and the fabric's gyroscopes spin up to net $\omega$"*
**[CANON-VERIFIED]** — i.e. canon's pedagogical register puts the *excitation*
on the moving side, which leans **against** the `ω = 0` branch of Q2.

### 6.5 ★ The Cosserat channel is GAPPED — a live obstruction to the `ω = 0` branch

[`port-register.md`](../manuscript/ave-kb/common/port-register.md):50, channel 4
— *"**Cosserat micro-rotation / wryness** (couple-stress; the $(2,3)$ winding)
… **GAPPED**: $\omega^2 = c_\kappa^2 k^2 + m_\omega^2$ … gap
$m_\omega = \sqrt{4G_c/I_\omega} \sim c/\ell_{node}$"* (`clm-kmliqx`).
**[CANON-VERIFIED]**

**[ASSEMBLY, flagged not resolved]** A self-stress state is a zero-frequency
load-free equilibrium — a null vector of the static stiffness. In a **gapped**
sector the static operator carries the `m_ω²` term, so `ω = 0` admits no
non-trivial solution at real `k` **unless the gap closes**. Since `G_c` is
saturation-modulated, the amplitude-dependence the walk needs and the gap
closure are potentially the *same* object.

**This is deliberately left as a flag, not a repair.** It could be (a) a clean
kill of Q2's self-stress branch, (b) the walk's mechanism in disguise, or (c) a
sector/scope confusion on my part between the bulk dispersion relation and a
localized defect state, which is exactly the kind of thing this record is not
entitled to settle. Grant and the auditor lane adjudicate; see B7.

### 6.6 The canon evidence on Q2 points BOTH ways — recorded as a contradiction, not reconciled

**Toward `ω = 0` (self-stress):**
- [`vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md):510 —
  *"**CHARGE** = the **MECHANICAL** Cosserat **micro-rotation** $(2,3)$-winding
  port … the **static reactive charge boundary** ($\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$,
  lossless, no real power)"*. **[CANON-VERIFIED]**
- [`saturation-rim-inversion.md`](../manuscript/ave-kb/common/saturation-rim-inversion.md):43 —
  *"Charge is the **STATIC imposed Link**"*. **[CANON-VERIFIED]**

**Toward `ω ≠ 0` (ringing):** §6.4's *"spin-up is what excitation does"*, and
§6.5's mass gap in the very sector the winding lives in.

**Flag-don't-fix: both readings are in canon, on the same sector, and this
record does not choose between them.** That the corpus supports both is itself
the argument for settling Q2 by computation rather than by more walking.

### 6.7 The static-existence test Q2 describes is ALREADY a routed candidate

[`saturation-rim-inversion.md`](../manuscript/ave-kb/common/saturation-rim-inversion.md):55 —
*"**The named test (ROUTED-CANDIDATE, NOT fired) — static existence.** Impose the
`(2,3)` winding as a **boundary condition**, relax the lattice, and ask whether
the relaxed core **rails `S → 0` at the center**"*, identified there with the
standing eigenmode-existence open item. **[CANON-VERIFIED]**

**Two things follow.** (a) Q2's self-stress branch may not be a new test at all
— it may be this one, re-motivated. (b) That test is phrased as *"impose … as a
**boundary condition**"*, and §1's periodic-torus finding says the carrier has
no free boundary **[MEASURED-ELSEWHERE, VERIFY PENDING]**. **If that finding
holds, it lands on this routed candidate too, not only on the autonomous-HB
lens.** Surfaced for the auditor lane; not acted on here.

That leaf also carries a mandatory guard for anyone prereg-ing it: the
static-existence relaxation is **distinct** from the leans-falsified
energize-LOCK formation route, and any future prereg must carry that
carve. **[CANON-VERIFIED]**

### 6.8 Two REGIME fences on the walk's own vocabulary

**(a) The mechanical register is regime-scoped.**
[`substrate-native-terminology.md`](../manuscript/ave-kb/common/substrate-native-terminology.md):39 —
*"**Mechanical/elastic — PASS *in the linear sub-yield regime*** (clean reactive
storage via the TKI dictionary)"*. **[CANON-VERIFIED]** The truss/bracing
language is clean in regime I; the object the walk wants to describe (the
saturated core, `A → A_yield`) is **not** in regime I. The walk never declared a
regime. **[WALK — flagged; audit item B8.]**

**(b) The mechanics↔EE co-equality is regime-scoped too.** `def-tk1xfm` is SOLID
and Grant-ratified, and its ratified sentence reads *"co-equality of the
mechanical and electrical descriptions **BELOW the band edge** ($\omega\tau\ll1$ /
long-wave regime) … the co-equality is REGIME-SCOPED"*
([`vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md):441).
**[CANON-VERIFIED]**

**Why this matters and why it is NOT a departure from EE-first.** Axiom 2 makes
clean elastic/Cosserat mechanics **co-equal** with the EE description, not an
added-DOF framework — so a mechanical walk is substrate-native by construction
and needs no defence on that axis. What it *does* need is a regime declaration,
because the co-equality is exact only below the band edge, and a lattice-scale
defect is not obviously there.

### 6.9 Two naming/notation hazards this record must not create

**(a) R43 is BINDING.** *"the **canonical term is "DC operating point /
quiescent point (Q-point)"**. **"Ground (reference)" is the EE-ANALOGY GLOSS,
NEVER the canonical noun**"*
([`vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md):500).
**[CANON-VERIFIED]** The autonomous-HB record's §3.1 leaned on Grant's *"we need
a ground reference"* line; **this record does not repeat that framing**, and any
successor should write **Q-point**, or **clause Q / reference-fixing** at
substrate scope.

**(b) `ω` is now carrying three distinct jobs in this discussion** — the Cosserat
**microrotation field** `ω`, its **rate** `dθ/dt` (§6.4's *"wound, not
spinning"*), and the HB **mode frequency** `θ`/`ω` of `e^{iθ}v = Mv`. Q2 is
phrased in the third sense. §6.4 and §6.5 are in the first two.
**Any audit of Q2 should restate it with the glyphs disambiguated before
computing anything.** **[WALK]**

## §7 — The walk's own weaknesses

## §8 — AUDIT CHARTER (numbered claims with attack instructions)

## §9 — KILL CONDITIONS

## §10 — The two open questions, routed to computation

## §11 — What this walk does NOT do
