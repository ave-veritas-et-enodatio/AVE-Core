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

## §2 — REPRODUCTION GATE: the inherited claim set, re-derived on the shipped operator

**Every number below was recomputed on this branch at `a3f4fef7`, on the shipped operator, before
this document was opened.** Nothing here was taken on trust. Two entries came back **CORRECTED**
and both corrections are stated in full rather than absorbed.

### §2.1 — JUNCTION SPECTRUM THEOREM — REPRODUCED, and now proved in closed form

For $S = \dfrac{2}{\sum_k Y_k}\,\mathbf{1}\,Y^{\!\top} - I$
(`vacuum_varactor_scatter.py:28-34` derivation, `:156-185` implementation):
$\mathbf{1}Y^{\!\top}$ is rank one with eigenvalue $Y^{\!\top}\mathbf 1 = \sum_k Y_k$ on the
all-ones vector and $0$ on $\{v:\sum_j Y_jv_j=0\}$. Hence **for any $Y>0$ and any $z$:**

$$\boxed{\ \operatorname{spec}(S) = \{+1 \ \text{(once, COMMON, } v=\mathbf 1,\ \text{an OPEN)}\}\ \cup\ \{-1 \ \text{(multiplicity } z-1,\ \text{BALANCED, } \textstyle\sum_j Y_jv_j=0,\ \text{a SHORT)}\}\ }$$

**Saturation grading rotates the EIGENVECTORS and never the EIGENVALUES.** Measured
$\max|\lambda-\lambda_{\text{exact}}|$ on the shipped `admittance_scatter`:

| $z$ | cold-uniform | random 4-decade grading | one bond at $10^{6}$ |
|---|---|---|---|
| 2 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 3 | 2.220e-16 | 4.441e-16 | 1.110e-16 |
| 4 | 1.110e-16 | 8.882e-16 | 2.220e-16 |

**Consistent with canon at the one site canon states it:**
[`k4-port-irrep-decomposition.md:23`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md)
(*"$T_2$ eigenvalue $-1$, triply degenerate"*) and `:55` (*"Basis spans the traceless 3D subspace
$\{v : \sum_i v_i = 0\}$"*). **Scope, stated because it is load-bearing: that leaf is the $z=4$
$K_4$ 4-port at UNIFORM admittance**, where $\sum_i Y_iv_i=0$ degenerates to $\sum_iv_i=0$. The
generalisation to arbitrary $z$ and to graded $Y$ is this lane's, is elementary, and mints nothing.

### §2.2 — TRACE IDENTITY — REPRODUCED

$\sum_i S_{ii} = \dfrac{2\sum_iY_i}{\sum_kY_k} - z = 2-z$ **exactly, for any admittances.** Measured
$\max\bigl|\operatorname{tr}S-(2-z)\bigr|$ over 2000 random 12-decade draws: $4.441\times10^{-16}$
($z{=}2$), $5.551\times10^{-16}$ ($z{=}3$), $8.882\times10^{-16}$ ($z{=}4$).

**★ The consequence that closes one route by arithmetic.** At $z=3$ the three diagonal reflections
must sum to $-1$. So **$\Gamma=-1$ on all three ports of an srs node is arithmetically
unreachable** — it would need a trace of $-3$. Driving one port to $-1$ by grading *forces* the
other two to sum to $0$. **A saturation-graded srs junction cannot be a three-port mirror.** The
only way all three ports see $\Gamma=-1$ at once is the balanced *incident field*, where the
reflection is a property of $v$, not of $S$'s diagonal.

### §2.3 — THE BALANCED NODE IS A MIRROR WITH NO SATURATION — REPRODUCED

The shunt reduction gives $V_u = 2\bigl(\sum_j Y_jV_j^{\text{inc}}\bigr)/\sum_kY_k$
(`harmonic_balance_srs.node_voltage`, `:506-512`). With $\sum_j Y_jV_j^{\text{inc}}=0$:

| $z$ | $|Y\!\cdot\!v^{\text{inc}}|$ | $\max|v^{\text{ref}}+v^{\text{inc}}|$ | $|V_{\text{node}}|$ |
|---|---|---|---|
| 3 | 7.067e-16 | **2.483e-16** | 1.420e-16 |
| 4 | 0.000e+00 | **1.144e-16** | 0.000e+00 |

$\Gamma=-1$ on **every port simultaneously**, with all admittances finite, all bonds sub-yield,
and **Axiom 4 never invoked**. *(The inherited receipts were 1.1e-16 and 4.4e-16; this lane's
independent draw gives 2.5e-16 and 1.1e-16. Same statement, different random vectors — both are
machine epsilon and neither is a tighter claim than the other.)*

### §2.4 — LEVEL-SET ARITHMETIC — REPRODUCED, with a **LABEL CORRECTION**

Canon's own named wall value: [`resonant-lc-solitons.md:54`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md),
verbatim, *"the set of 19 wall nodes at yield (A>0.9, S→0.045)"*. Evaluating
$\Gamma_{pp} = 2Y_p/\sum_kY_k - 1$ with $Y=1/\sqrt S$:

**⚑ THE PROBE-PORT CONVENTION, FROZEN, because it is what the numbers depend on.** $\Gamma$ is read
**at the COLD port** — the radial bond pointing out of the shell, which is the port an incident
wave actually arrives on. Reading at a saturated in-shell port gives entirely different numbers
and is not the probe geometry.

| configuration ($S_{\text{sat}}=0.045$) | $\Gamma$ at the COLD port | $\Gamma$ at a SATURATED port |
|---|---|---|
| all three bonds saturated (**uniform**) | **−0.3333333333** | −0.3333333333 |
| **two** saturated, one cold | **−0.8082103319** | −0.0958948341 |
| **one** saturated, two cold | **−0.7021169894** | +0.4042339788 |
| cold vacuum (reference) | **−0.3333333333** | −0.3333333333 |

> **🔧 CORRECTION 1 — the inherited pair of labels is TRANSPOSED.** The claim set this lane
> inherited reads *"Two saturated one cold: −0.702. One saturated two cold: −0.808."* **Both values
> reproduce to ten digits, attached to the opposite configurations.** −0.8082 is the **two**-saturated
> case and −0.7021 is the **one**-saturated case. The corrected ordering is the physically
> meaningful one — more saturated neighbours ⇒ closer to $-1$ — and the transposed version inverts
> it. **No conclusion in the inherited set depends on the labels**, because the load-bearing row is
> the uniform one; it is corrected here so the arithmetic can be checked rather than believed.

**THE PUNCHLINE, UNCHANGED AND NOW SHARPER.** The sequence over the number of saturated bonds is
$-1/3,\ -0.702,\ -0.808,\ -1/3$ — it is **NOT monotone and it returns to cold vacuum at full
uniformity.** A uniformly saturated shell reflects **exactly** like cold vacuum, because the
common factor $Y_0/\sqrt S$ cancels through a sum and a division. **The mirror is the GRADIENT at
the shell edge, and the strongest mirror sits at maximal gradient, not at maximal saturation.**

### §2.5 — SHIPPED-KERNEL CEILINGS — REPRODUCED, with a **KERNEL-PATH CORRECTION**

| kernel state | $S$ | best-case $\Gamma$ (2 saturated + 1 cold, probed cold) |
|---|---|---|
| shipped `vacuum_varactor_scatter` at its clip $A_{\text{cap}}=0.99$ | **0.1410673598** | **−0.6837926976** |
| canon's figure value $S=0.045$ | 0.045 | −0.8082103319 |
| un-floored ideal kernel at $A=1-10^{-12}$ | 1.414198e-06 | −0.9988115061 |

> **🔧 CORRECTION 2 — there are TWO live kernel-clip conventions in-tree and they do not meet.**
> `vacuum_varactor_scatter.py:122` pins `A_cap=0.99, S_min=0.05`; because the cap binds first, its
> **minimum reachable $S$ is 0.1410673598** and **$S=0.045$ is unreachable through that path**. The
> figure the incumbent wall picture comes from uses a *different* path —
> `src/scripts/viz/electron_lattice_scene.py:93-94` (`exponent=0.5`, `S_min=1e-3`) on
> `srs_cage_winding.py:293` (`A_cap: float = 0.999`), whose $S(A_{\text{cap}})=0.0447$, which **is**
> canon's 0.045. **So `resonant-lc-solitons.md:54`'s "(A>0.9, S→0.045)" is internally consistent** —
> `A>0.9` is the *selection threshold* for the node set and `S→0.045` is the value at the *clip*,
> $A=0.999$ — and the two numbers describe different things, not one thing. **§5 freezes the
> `vacuum_varactor_scatter` path**, because that is the one `harmonic_balance_srs.bond_admittance`
> delegates to; the divergence is routed as a flag in §11, not fixed here.

### §2.6 — THE A1 BRANCH IS TRANSPARENT AT THE STATED OPERATING POINT — REPRODUCED EXACTLY

$Z_{\text{core}} = Z_0\sqrt{S(A)}$, evaluated at `def-vyvsn1`'s own A1 operating point
$A=\sqrt\alpha$ (`vocabulary-register.md:757`, verbatim: *"the electron's A1 mass core operates at
strain $A=V_{\text{yield}}/V_{\text{snap}}=\sqrt\alpha$"*):

| quantity | value at `a3f4fef7` |
|---|---|
| `ALPHA` | 0.0072973525693 |
| $A_{\text{op}}=\sqrt\alpha$ | 0.085424543132 |
| $S(A_{\text{op}})$ | 0.996344642898 |
| $\sqrt{S}$ | 0.998170648185 |
| **$\Gamma_{\text{bulk}}$** | **−9.155133055855e−04** |
| $\Gamma_{\text{bulk}}(A{=}0.99)$, analytic Fresnel step | −0.453922 |

**A 0.09% reflection. Not a mirror.** *(Both inherited values — −9.155133e−04 and the −0.453922
analytic step — reproduce to every digit quoted.)*

### §2.7 — WHAT §2 ESTABLISHES, AND WHAT IT DOES NOT

**The consequence, stated as the fork it is.** The corpus confinement number is either

- **FREE EVERYWHERE** — the BALANCED $-1$ is an eigenvalue of *every* node of *empty cold vacuum*
  (§2.1), so it does not distinguish an electron from nothing; or
- **ABSENT HERE** — the A1 $-1$, the one that would localise because an amplitude level set has a
  radius, is $-9.155\times10^{-4}$ at the stated operating point (§2.6).

**Never in between**, and §2.2 forecloses the obvious escape by arithmetic. **Therefore the
localising object cannot be the LOCAL eigenvalue**; it would have to be a **closed surface of
simultaneously balanced nodes** — a property of the composed map
$M = C\cdot\mathrm{blockdiag}(S)$, which no leaf in the corpus computes and which §4 is built to
measure.

**⚠ §2 IS NOT A RESULT AND DOES NOT ADJUDICATE ANYTHING.** It is arithmetic on an operator. It
does not show that a balance surface exists on the srs carrier, does not show that it is closed,
does not show that a bound state sits inside one, and does not weigh on `def-vyvsn1`. **Every one
of those is what §4 pre-registers, and all of them can come back NO.**

### §2.8 — PROVENANCE OF THE INCUMBENT (verified, not summarised)

`def-vyvsn1` is `SOLID` and is the only `SOLID` electron-wall statement in the corpus. Its own
entry records, verbatim and verified on this branch:

- `vocabulary-register.md:753` — *"BOTH are **CALIBRATION, not derived** ($V_{\text{snap}}\equiv
  m_ec^2/e$ definitional with $m_e$ in voltage units; $V_{\text{yield}}\equiv\sqrt{\alpha}\cdot
  V_{\text{snap}}$, the $\sqrt{\alpha}$ being **the imported $\alpha$-echo**)."*
- `vocabulary-register.md:756` — `clm-cross-links:` *"(none verified-specific yet)"* — **no scored
  claim, no numeric solidity.**
- `vocabulary-register.md:758` — the `verification:` field records that the ruling **landed in
  prose** at three sites. That is a **propagation** receipt, not a derivation receipt.
- The mechanism sentence, `pair-production-axiom-derivation.md:102`, is **one sentence**: *"the
  transverse micro-rotation wave's amplitude crosses Axiom-4 onset, $\Gamma \to -1$, and the
  lattice self-creates its TIR cavity."* **No solved BVP, no eigensolve.**
- Canon says so itself at [`device-circuit-models.md:163`](../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md),
  verbatim: *"What is **NOT** derived is the **shape-forcing chain**: no solved boundary-value
  problem produces the electron's surface from its $0_1$-unknot topology."*

**Grant directive governing this arc, verbatim:** *"I think we need to be ok challenging past
rulings that don't have hard math tied to them."*

**And this lane's own limit on that directive:** `SOLID` status plus an explicit Grant
adjudication is not overturned by a discriminator run. §1.4 binds — the most this lane can produce
is an input.

### §2.9 — 🔧 CORRECTION 3 — the inherited reading of `device-circuit-models.md:165` was already wrong the other way

`device-circuit-models.md:165` does **NOT** argue against the A1/bulk wall — **it asserts it**,
verbatim: *"The confinement surface is the **A1 MASS wall** ($Z_{\mathrm{bulk}}\to0$, the
impedance-short $\Gamma=-1$ of the Pauli/TIR derivation)."* Its guard sentence warns against
**colliding** that A1 mass wall with the $\Gamma_{\text{spinor}}$ $T_2$ wall — *"Reading the two
$-1$'s as one wall would wire the cage into the charge-winding and break the two-'3's
orthogonality"* — which is an argument **on the A1 side**, not a prohibition against it. **Any
document that inherited the framing that `:165` is a prohibition against the 2026-06-30 ruling is
wrong and must be corrected.** Recorded here; routed in §11.

## §3 — SCOPE FENCE: the LOCAL junction property is a CONTROL; the GLOBAL surface is the RESULT

**This lane tests two things and they must never be reported as one.**

| | **LOCAL** — the junction property | **GLOBAL** — the surface property |
|---|---|---|
| object | $S_u$, one node's scatter matrix | $M = C\cdot\mathrm{blockdiag}(S)$, the composed one-step map |
| statement | $\operatorname{spec}(S_u) = \{+1\}\cup\{-1\}^{z-1}$ for any $Y>0$ | does a **closed** set of simultaneously balanced nodes exist, and where |
| status | **PROVED in closed form and reproduced (§2.1). Free at every node of empty cold vacuum.** | **UNKNOWN. No leaf in the corpus computes it.** |
| role in this lane | **CONTROL** | **THE RESULT** |
| can it be a verdict? | **NO — never.** | **YES — this is what §4 bins.** |

### §3.1 — Why the LOCAL property is a control and not a finding

The BALANCED eigenvalue $-1$ is present at **every node of empty cold vacuum**, at every
admittance grading, at every drive level and at every tone. **It therefore has zero discriminating
power: it does not distinguish an electron from nothing.** Reporting it as a confinement result
would be reporting a property of the shunt-junction *algebra* as a property of the *state*.

It is run anyway, and it is run first, for exactly two purposes:

1. **Instrument receipt.** If the shipped operator does not reproduce $\{+1\}\cup\{-1\}^{z-1}$ and
   $\operatorname{tr}S = 2-z$ on the run's own graded $Y$ field, the instrument is broken and every
   downstream number is void. **Gate LOC-1**, §6.
2. **The negative control for the global test.** The null set the global test finds must be
   **strictly smaller** than "every node". If the pre-registered null locus coincides with the
   null locus of the **cold empty-vacuum control run**, the result is an `ARTIFACT` (§4) — because
   a surface that is present in empty vacuum is not a confinement surface.

### §3.2 — What "global" means here, operationally

**The claim under test is a property of the composed map $M$, not of any $S_u$.** $M$ is built by
the shipped `apply_M` (`harmonic_balance_srs.py:492-503`): scatter at every node, then apply the
CONNECT permutation. The observable is the **node-voltage field** $V_u$ that $M$'s fixed point
carries, read by the shipped `node_voltage` (`:506-512`).

**A closed surface, defined so a machine can decide it (frozen):** the null set $\mathcal N$
(§4.2) is a **CLOSED SURFACE** iff deleting $\mathcal N$'s nodes from the bond graph leaves the
core/seed node in a **finite** connected component that does **not** touch the periodic wrap. This
is a connected-components call on the net's own `neighbors` lists — bond-graph native, no Cartesian
geometry, no posited sphere.

**This is the object the corpus has never computed**, and it is the only thing in this document
that could be a finding.

### §3.3 — The fence, stated as a binding reporting rule

**No sentence in the result document may report a LOCAL number as evidence for either ontology.**
The LOCAL section of the result doc reports **PASS/FAIL of an instrument gate** and nothing else.
Any prose of the form *"the engine shows $\Gamma=-1$ at the wall nodes"* is **forbidden by this
fence** regardless of what the numbers do, because §2.1 already established that sentence is true
of empty vacuum.

## §4 — THE FROZEN DISCRIMINATOR: observables, keys, and the exact bin definitions *(placeholder)*

## §5 — GEOMETRY AND PARAMETERS, FROZEN *(placeholder)*

## §6 — THE FIVE GUARDS AS PRE-REGISTERED CHECKS *(placeholder)*

## §7 — THE NON-TRIVIALITY GATE *(placeholder)*

## §8 — WHAT WOULD FALSIFY THE VIRTUAL-NEUTRAL READING *(placeholder)*

## §9 — THE HONEST EXPECTED OUTCOME *(placeholder)*

## §10 — ANTI-RESCUE GUARD *(placeholder)*

## §11 — ROUTED FLAGS *(placeholder)*

## §12 — SKILL-SELECTION PLAN *(placeholder)*
