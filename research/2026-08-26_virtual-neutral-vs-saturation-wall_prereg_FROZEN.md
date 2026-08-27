# PREREG — **FROZEN** — virtual neutral vs saturation wall: a discriminator on the electron's confinement surface

**Date:** 2026-08-26 · **Branch:** `research/2026-08-26-virtual-neutral-prereg` · **Base:** `origin/main` @ `a3f4fef7`
**Lane:** confinement-surface ontology discriminator (VN), prereg satellite
**Deliverable class:** frozen pre-registration. **Nothing runs until this document is pushed.**

> # 🔒 FREEZE STATEMENT
>
> This document is committed **ALONE** and **PUSHED** before any driver code, any solved
> state, and any measured number for this lane exists in the tree (freeze-by-push). **Rule 11
> binds from the push:** no bin edge, tolerance, observable definition, geometry, tone set,
> amplitude ladder or seed below may be edited, widened or re-labelled after any measurement
> content lands. A post-push change is a Rule-12 dated amendment carrying its own
> justification, appended — never a silent edit and never a rewrite of frozen text.
>
> **The §2 reproduction receipts are the ONE exception and they are exempt by construction:**
> they were computed on the shipped operator **before** this document was opened, they are
> reproductions of an inherited claim set rather than results of the pre-registered run, and
> two of them **correct** the inherited claim. They are banked here so the discriminator below
> stands on verified arithmetic instead of on trust.

**Class:** **DISCRIMINATOR** (a sub-class of ADJUDICATION-INPUT). This lane **mints no
`clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, axiom or ruling;
changes no solidity; propagates nothing; retires nothing.** It produces one verdict in one
pre-registered bin, which is then an **input** to a Grant ruling — never itself a ruling. **No
result from this lane may be framed as a chord, as emergence, or as a falsification of AVE.**

---

## §0 — SECTOR HEADER (declared once, binding on every claim in this document)

[`wall-taxonomy.md:160`](../manuscript/ave-kb/common/wall-taxonomy.md), verbatim, verified on this
branch: *"Before asserting a wall anywhere: name (i) the **channel**, (ii) the **axis** it lives
on, and (iii) the **phase-state** (cold/sub-yield vs saturated). A claim missing any of the three
is not yet a claim about a wall."* Declared here for the whole document; **every §4 bin inherits
this header and none of them may be quoted without it.**

| axis | declaration |
|---|---|
| **CHANNEL** | **SCALAR shunt-junction channel only** — one scalar phasor per directed port, the Op5 port set that `vacuum_varactor_scatter.admittance_scatter` and `harmonic_balance_srs.apply_M` actually compute on. **No Cosserat micro-rotation DOF is carried, driven, graded or read.** |
| **AXIS** | **node-voltage balance** — the shunt-junction KCL sum $\sum_j Y_j v_j$ at each node, evaluated by the shipped `harmonic_balance_srs.node_voltage`. This is a **network** axis, not a spatial-Brillouin one; the surface it defines is located in the bond graph, never on a Cartesian radius. |
| **PHASE-STATE** | **GRADED, mixed** — cold ($A=0$) in the far field, driven up to but not beyond the shipped kernel clip in the core. Both the cold arm and the graded arm are run, and the cold arm is a **control**, not a result. Ruptured and pre-bond states are OUT OF SCOPE; no result may be extrapolated across a phase boundary. |
| **MODE** | **DISCRIMINATOR** between two named ontologies (§1). Not a derivation, not an existence proof, not a measurement of any constant. |
| **CARRIER** | **srs-z3**, `build_srs_net(L=6)` — the D1-ratified production carrier, and the same $L=6$ carrier the incumbent claim's own wall figure is drawn on. The z=2 ring is a **fixture** only (§5), and its own carrier tag says so: `carrier="ring-z2-fixture"  # known-case fixture, NOT a physics carrier` (`harmonic_balance_srs.py:1088`). |
| **CROSS-WIRING CHECK** | **Performed.** Nothing in this lane couples the scalar channel to charge (Cosserat winding), to spin (the $\mu$ sign-selector), or to the A1 dilatation mass store. Both candidate ontologies are statements about **where a scalar node voltage vanishes**; neither is a statement about what the surface *carries*. |
| **consistency-vs-emergence** | **CONSISTENCY / ontology-discrimination.** Declared before any run. Neither outcome is an emergence result: the run does not ask whether the substrate hosts a bound state, it asks which of two descriptions locates a surface that is assumed to exist. |

**★ The one cross-wiring hazard this header exists to close.** [`k4-port-irrep-decomposition.md:23`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md)
names the $-1$ eigenvalue *"$T_2$"*, and [`vocabulary-register.md:747-758`](../manuscript/ave-kb/common/vocabulary-register.md)
(`def-vyvsn1`) puts the incumbent electron wall in the **transverse Cosserat $T_2$ sector**. **These
are two different objects wearing one name and this document uses NEITHER name for its own
observable.** The K4 leaf's $A_1 \oplus T_2$ split is the **port-space irrep decomposition of a
$z=4$ scalar shunt junction** — it is the same linear algebra this lane generalises, on the same
scalar port space, and it is *not* the Cosserat rotation sector. Throughout this document the two
eigenspaces are called **COMMON** ($+1$, all ports equal) and **BALANCED** ($-1$, $\sum_j Y_j v_j =
0$), and no sentence here licenses reading a BALANCED-subspace result as a statement about the
$T_2$ micro-rotation channel or about `def-vyvsn1`'s threshold.

**Circuit statement, before any framework word.** Lossless delay lines meet at 3-way shunt
junctions. Some of the lines are varactor-loaded, so their admittances differ. **Question: when the
common node voltage at a junction goes to zero, is that because the loading got extreme, or
because the incoming waves cancelled?** Those are different circuits and they fail differently.

**Coordinates (`phase-space-coordinate-check`).** The claim under test is a statement about the
**node-voltage phasor field**, and every measurement below is taken in that field. The locus scalar
is a **bond-graph hop count**, never a Cartesian radius — `build_bond_table`'s own docstring binds
this: *"Canonical (min,max)-keyed undirected-bond tables from the net's own neighbor lists (**never
a Cartesian distance posit**)"* (`harmonic_balance_srs.py:262-264`).

## §0.5 — GUARD DISCHARGE (a)–(e) *(placeholder)*

## §1 — THE QUESTION, stated so it can return NO

### §1.1 — The two named ontologies

Both are descriptions of **the same assumed object**: a closed surface, on the srs bond graph,
across which a bound scalar state does not leak. They differ in **what puts the surface where it
is**. Each is stated here in its own terms, with its own locating equation, before either is
tested.

> **H-SAT — SATURATION WALL.** The surface is the **level set of the saturation amplitude**:
> $\{u : A(u) = A^{*}\}$. It exists because the varactor loading becomes extreme — $S(A)\to$ its
> floor, $Z_{\text{core}}\to0$, $\Gamma\to-1$ — and the wave cannot cross a short. This is the
> incumbent. It is [`boundary-observables-m-q-j.md:58`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)'s
> **register 1, AMPLITUDE LEVEL-SET**, which files the electron row there verbatim: *"the boundary
> is the locus where the saturation amplitude hits threshold ($S(A)\to0$, $\Gamma\to-1$; the leaf's
> own opening definition)."*

> **H-VN — VIRTUAL NEUTRAL.** The surface is the **balance locus** of the shunt-junction KCL:
> $\{u : \sum_j Y_j v_j = 0\}$. It exists because the incident waves arriving at a node sum to
> zero in the admittance-weighted sense, so the common node voltage vanishes and every port sees
> $\Gamma=-1$ *simultaneously* — a mirror built out of cancellation rather than out of loading.
> This is [`boundary-observables-m-q-j.md:61`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)'s
> **register 4, BALANCE LOCUS**, the register that leaf tabulates for the *Solar* rung and not for
> the electron.

**The proposal this lane exists to test is a REGISTER MOVE, not a new category:** move the electron
row from register 1 to register 4. The category already exists in canon, and
[`vocabulary-register.md:404`](../manuscript/ave-kb/common/vocabulary-register.md) (`def-anat3s`)
already banks the conjecture that the two coincide, verbatim: *"**(ii) the balance shell** (the
$\sigma$-opposite-equal crossing, $\approx 1.6\,\ell_{node}$; **CONJECTURED $\equiv$ wall** per
Ruling 6)."* **A VIRTUAL-NEUTRAL verdict would discharge that banked conjecture; a SATURATION
verdict would refute it.** Both are bankable.

### §1.2 — The question

> **Q.** On the srs-z3 carrier, for a bound scalar state solved by the shipped harmonic-balance
> operator, **is the closed surface of vanishing node voltage located by the amplitude level set
> $A(u)=A^{*}$ (H-SAT), or by the balance condition $\sum_j Y_j v_j = 0$ (H-VN)?**

**This question can return NO to both.** It returns `AMBIGUOUS` when both keys fire or neither
does, `ARTIFACT` when the surface is an instrument product, and `INCONCLUSIVE` when the solve does
not produce a comparable state. Those are three of the five bins in §4 and **§9 pre-registers
`AMBIGUOUS-ON-THIS-CARRIER` as the single most likely outcome.**

### §1.3 — Why the keys are ORTHOGONAL (the reason a discriminator is possible at all)

| | **H-SAT** | **H-VN** |
|---|---|---|
| located by | $A(u)$ hitting threshold | $\sum_j Y_j v_j = 0$ |
| needs a spatial gradient in $A$ | **YES** — a level set of a constant field is empty or everything | **NO** — balance is a condition on the *incident phasors*, and holds at uniform loading |
| moves with drive amplitude | **YES** — raising the drive moves where $A$ crosses $A^{*}$ | **NO** — the balance condition is homogeneous of degree 1 in $v$, hence scale-invariant in $\lVert v\rVert$ |
| moves with mode / tone | **NO** — the Axiom-4 kernel $S(A)=(1-A^2)^{p}$ is **frequency-blind**: it reads an envelope, and $\theta$ does not appear in it | **YES** — the phasor pattern $v$ is what balances, and $v$ is a function of $\theta$ |

**The two rows in bold are the whole design.** H-SAT's locus is keyed on **amplitude** and blind to
**mode**; H-VN's locus is keyed on **mode** and blind to **amplitude**. The keys are not merely
different in size — they are on **different knobs**, so no amount of precision on one substitutes
for the other, and a result cannot be moved from one bin to the other by re-scaling anything.

**The frequency-blindness of the kernel is a property of the shipped code, not an assumption.**
`vacuum_varactor_scatter.saturation_kernel(A)` (`:125-150`) takes exactly one argument, an
amplitude; `harmonic_balance_srs.bond_admittance(A_bond)` (`:309`) takes exactly one argument, an
amplitude. **No $\theta$ enters either signature.** Conversely `solve_tone(a_nodes, conn, theta,
...)` (`:534-537`) takes $\theta$ as an input and returns a $\theta$-dependent phasor field. The
orthogonality of the keys is therefore readable off the two call signatures.

### §1.4 — What a verdict here does and does not license

- **DOES:** supply one pre-registered input to a Grant ruling on the register of the electron's
  confinement surface.
- **DOES NOT:** move `def-vyvsn1`, whose status is `SOLID`, whose sector attribution is
  Grant-adjudicated (2026-06-30), and which this lane does not touch. **A VIRTUAL-NEUTRAL verdict
  in the scalar channel is not a refutation of a $T_2$-sector threshold** (§0's cross-wiring
  check). What it would put in question is the *register* the incumbent's surface is filed under,
  and only in the channel measured.
- **DOES NOT:** bear on whether the substrate hosts an electron. The run assumes a bound state and
  asks where its surface is; a null here is a null about **location**, never about **existence**.

## §2 — REPRODUCTION GATE: the inherited claim set, re-derived on the shipped operator *(placeholder)*

## §3 — SCOPE FENCE: the LOCAL junction property is a CONTROL; the GLOBAL surface is the RESULT *(placeholder)*

## §4 — THE FROZEN DISCRIMINATOR: observables, keys, and the exact bin definitions *(placeholder)*

## §5 — GEOMETRY AND PARAMETERS, FROZEN *(placeholder)*

## §6 — THE FIVE GUARDS AS PRE-REGISTERED CHECKS *(placeholder)*

## §7 — THE NON-TRIVIALITY GATE *(placeholder)*

## §8 — WHAT WOULD FALSIFY THE VIRTUAL-NEUTRAL READING *(placeholder)*

## §9 — THE HONEST EXPECTED OUTCOME *(placeholder)*

## §10 — ANTI-RESCUE GUARD *(placeholder)*

## §11 — ROUTED FLAGS *(placeholder)*

## §12 — SKILL-SELECTION PLAN *(placeholder)*
