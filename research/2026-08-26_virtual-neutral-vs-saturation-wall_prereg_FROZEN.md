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

## §0.5 — GUARD DISCHARGE (a)–(e), by name

Five guards ride this arc. Each is named here with where it is discharged; each is a
**pass/fail check with a criterion** in §6, not a reassurance.

| guard | what it polices | discharged at |
|---|---|---|
| **(a) SECTOR HEADER on every claim** | `wall-taxonomy.md:160` — a claim missing channel/axis/phase-state is not yet a claim about a wall | **§0** (document-wide) + **gate SEC-1** (§6) |
| **(b) THE STRUCTURAL-NULL TRAP** | `harmonic_balance_srs.py:191-195` — *"any null obtained through a per-node broadcast is an artifact, not a result"* | **§4.2** (in $\beta$'s definition, by construction) + **gate BCAST-1** (§6) + **bin A4** |
| **(c) THE $\alpha$-ECHO TRAP** | the engine's radiative leak is literally `1.0 - alpha`; re-deriving 137 from the loaded port is adjudicated CIRCULAR, *"do NOT pose it"* | **gate ALPHA-1** (§6) + **§4.7** |
| **(d) FREEZE + INSTRUMENT FENCE** | `harmonic_balance_srs` self-declares INSTRUMENT-GRADE INFRASTRUCTURE that *"mints no physics claims"* | **the freeze statement** + **§5** frozen geometry + **gate FENCE-1** (§6) |
| **(e) THE SILENT-ZERO TRAP** | `solve_tone(..., term=None)` returns $\lVert v\rVert = 0$ with `converged=True`; *"converged" is not "non-zero"* | **§7** (the non-triviality gate) + **bin 0** |

**⚑ Guard (b) is the one that bites this arc directly, and it is why $\beta$ is defined the way it
is.** The entire content of the §2 finding is that **uniform grading cancels identically**. A
broadcast-induced null would look **exactly** like a virtual neutral. So $\beta$ is built to be
**invariant under a per-node uniform $Y$ rescale** (§4.2), which makes a broadcast structurally
incapable of producing a $\beta$ null; BCAST-1 and bin A4 then catch the case where the *converged*
$A$ field happens to be uniform at the null anyway.

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

## §4 — THE FROZEN DISCRIMINATOR: observables, keys, and the exact bin definitions

### §4.1 — The pre-registered discriminator table (frozen)

| | **H-SAT — SATURATION WALL** | **H-VN — VIRTUAL NEUTRAL** |
|---|---|---|
| located by | $A(u)$ hitting threshold | $\sum_j Y_j v_j = 0$ |
| needs a spatial gradient | **YES** | **NO** |
| moves with drive amplitude | **YES** | **NO** — scale-invariant in $\lVert v\rVert$ |
| moves with mode / tone | **NO** — the Axiom-4 kernel is frequency-blind | **YES** |

### §4.2 — The observables, defined completely, before any run

**(O1) The node-balance ratio $\beta_u$ — the primary field.** For node $u$, with `a_nodes` and the
per-tone phasors $v^{(m)}$ as the shipped code produces them:

$$\beta_u \;=\; \frac{\Bigl[\sum_m \bigl|\sum_j a_{uj}\,v^{(m)}_{uj}\bigr|^2\Bigr]^{1/2}}{\Bigl[\sum_m \sum_j \bigl(a_{uj}\,\bigl|v^{(m)}_{uj}\bigr|\bigr)^2\Bigr]^{1/2}}$$

The numerator is the shipped `node_voltage` magnitude, tone-summed. The denominator is **the same
sum with the cancellation removed** — each term's magnitude entered incoherently. Three properties,
each of which is load-bearing and each of which is a theorem about the formula, not an assumption:

- **$\beta_u \in [0,1]$**, by the triangle inequality on the numerator against a term-wise
  Cauchy–Schwarz bound on the denominator. $\beta_u=0 \iff$ **perfect balance**;
  $\beta_u \to$ its ceiling $\iff$ no cancellation at all.
- **$\beta_u$ is INVARIANT under any rescale of $\lVert v\rVert$** — numerator and denominator are
  both homogeneous of degree 1 in $v$. **So $\beta$ measures BALANCE, never SIZE, and cannot be
  driven to zero by the solution shrinking.** This is the single most important property in this
  document and it is the reason FL-4's silent zero cannot masquerade as a virtual neutral.
- **$\beta_u$ is INVARIANT under a per-node UNIFORM rescale of $Y$** — a uniform factor cancels
  out of `a_nodes` identically (§2.4). **So a per-node broadcast cannot produce a $\beta$ null.**
  This is guard (b) discharged at the level of the observable's definition, not by a downstream
  check.

**(O2) The null set $\mathcal N$.** $\mathcal N = \{u : \beta_u < \tau_\beta\}$ with
$\boxed{\tau_\beta = 1.0\times10^{-2}}$ **FROZEN**.

*Justification, stated in both directions.* On a generic incident field at $z=3$ the coherent sum
is $\sim1/\sqrt3$ of the incoherent one, so the generic population sits near $\beta\approx0.58$ —
**$\tau_\beta$ is nearly two decades below it.** And the numerical floor of the solve is
$\lesssim10^{-8}$ (§7 NT-4), so **$\tau_\beta$ is six decades above the instrument's noise.** *A
threshold the instrument cannot resolve always fires; a threshold the instrument cannot reach
never does.* Both edges are named so neither can be re-cut later.

**(O3) The separation receipt.** $\mathrm{sep} = \bigl(\min_{u\notin\mathcal N}\beta_u\bigr) /
\bigl(\max_{u\in\mathcal N}\beta_u\bigr)$, **COMPUTED and REPORTED for every configuration**.
$\mathrm{sep} < 10$ ⇒ $\tau_\beta$ is not resolving two populations ⇒ **`ARTIFACT`** (§4.5).

**(O4) The locus scalar $d_{\text{null}}$ — substrate-native, in hops.**
$d_{\text{null}}$ = the **mean bond-graph (hop) distance from the core/seed node set to
$\mathcal N$**, computed by BFS on the net's own `neighbors` lists. **Units: bonds. Never a
Cartesian radius** (§0 coordinates).

**(O5) The closure predicate $\mathcal C$.** As frozen in §3.2: `True` iff deleting $\mathcal N$
leaves the core in a finite component not touching the periodic wrap.

**(O6) The mode-sign pair $(\Gamma_{\text{common}},\Gamma_{\text{diff}})$ — SUPPLEMENTARY.** At
fixed amplitude, on the frozen $\mathcal N$ from the primary run, drive the surface's outward-facing
ports with (i) a **surface-common** incident set (equal amplitude and phase on every outward port)
and (ii) a **surface-differential** set (outward-port weights satisfying $\sum_j Y_jv_j=0$ over the
surface's outward port set). Apply the shipped `apply_M` once; project the reflected field back
onto the same port set; report the two complex ratios.

### §4.3 — The two keys (frozen)

$$K_{\text{amp}} = \bigl|\,d_{\text{null}}(s_{\text{hi}}) - d_{\text{null}}(s_{\text{lo}})\,\bigr| \qquad\text{over the §5 amplitude ladder, at FIXED tone set}$$
$$K_{\text{mode}} = \bigl|\,d_{\text{null}}(T_B) - d_{\text{null}}(T_A)\,\bigr| \qquad\text{over the §5 tone sets, at FIXED amplitude}$$

Both in **hops**. Frozen edges, with the dead band between them:

| verdict on a key | condition |
|---|---|
| **MOVES** | key $> 1.00$ hop |
| **DEAD BAND** | $0.25 \le$ key $\le 1.00$ hop |
| **STATIC** | key $< 0.25$ hop |

**Why one hop.** One bond is the smallest displacement that puts the surface on a **different node
set**; below one hop the surface has not moved anywhere the carrier can represent. The 0.25 floor
is one quarter of that, four times the coarsest thing the graph can express.

**★ THE STRUCTURAL PRECONDITION ON $K_{\text{amp}}$ — surfaced here, because it is not in the
inherited claim set and it can void the amplitude arm outright.** $M$ is **linear in $v$ once the
$Y$ field is fixed.** So in a *single* linear tone solve, scaling the drive scales the solution and
**nothing moves** — $K_{\text{amp}} \equiv 0$ **by linearity, for both ontologies.** A zero there
would be a structural null, not a virtual neutral. **Therefore the amplitude arm is only defined
inside the self-consistent outer loop** (`solve_self_consistent`, `:714`), where the drive changes
$A_{\text{bond}}$, which changes $Y$, which changes `a_nodes`. **Gate AMP-1 (§6) enforces this and
a linear-solve amplitude arm is `ARTIFACT`, never `VIRTUAL-NEUTRAL`.**

### §4.4 — 🔒 THE EXACT BIN DEFINITIONS

**Evaluation order is FIXED and the first matching bin wins.** `ARTIFACT` and `INCONCLUSIVE` are
evaluated FIRST and OVERRIDE everything, so no failed run can reach a selecting bin.

> **BIN 0 — `INCONCLUSIVE`** *(evaluated first)*
> Fires iff **any** of: the §7 non-triviality gate fails on any tone of any configuration; any
> tone reports `converged == False`; any tone's `residual_rel` $\ge 1.0\times10^{-8}$; the outer
> S-field loop does not reach `outer_tol` within `max_outer`; or any configuration fails to build.
> **Mandatory bin. Never folded into any other. `INCONCLUSIVE` is reachable with the physics
> entirely correct** (a solver stall reaches it), which is what makes it a real bin.

> **BIN 1 — `ARTIFACT`** *(evaluated second; OVERRIDES bins 2–5)*
> Fires iff **any** of:
> **(A1)** $\mathcal N = \varnothing$ or $\mathcal N$ = all nodes, in any configuration —
> $\beta$ resolved no surface.
> **(A2)** $\mathcal C = $ `False` — $\mathcal N$ is not a closed surface (§3.2), so there is no
> global object to bin.
> **(A3)** $\mathrm{sep} < 10$ in any configuration — $\tau_\beta$ is not separating two
> populations.
> **(A4)** The converged $A_{\text{bond}}$ field is **per-node uniform to within $10^{-12}$** at
> any node of $\mathcal N$ — the broadcast trap; the null could have been produced by uniformity
> alone (guard b, `harmonic_balance_srs.py:191-195`).
> **(A5)** $\mathcal N$ **equals** the cold empty-vacuum control run's null set (§3.1) — a surface
> present in empty vacuum is not a confinement surface.
> **(A6)** The amplitude arm was evaluated **outside** the self-consistent loop (gate AMP-1, §6),
> or `max` $A_{\text{bond}}$ did not increase monotonically across the amplitude ladder — the knob
> did not move the thing it exists to move.
> **(A7)** Any §6 guard check returns FAIL.

> **BIN 2 — `SATURATION`**
> Fires iff **all** of: $K_{\text{amp}} > 1.00$ hop **AND** $K_{\text{mode}} < 0.25$ hop, **in every
> one of the §5 configurations** (all seeds, both envelope modes, both tone pairs).

> **BIN 3 — `VIRTUAL-NEUTRAL`**
> Fires iff **all** of: $K_{\text{amp}} < 0.25$ hop **AND** $K_{\text{mode}} > 1.00$ hop, **in every
> one of the §5 configurations** (all seeds, both envelope modes, both tone pairs).

> **BIN 4 — `AMBIGUOUS`**
> Fires iff none of bins 0–3 fires. Exhaustively, this is:
> **(B4a) BOTH-FIRE** — $K_{\text{amp}} > 1.00$ **and** $K_{\text{mode}} > 1.00$. Both keys move
> the surface; neither ontology is selected.
> **(B4b) NEITHER-FIRES (`AMBIGUOUS-DEGENERATE`)** — $K_{\text{amp}} < 0.25$ **and**
> $K_{\text{mode}} < 0.25$. The surface is insensitive to both knobs, so the run discriminates
> nothing. **§9 pre-registers this as a real possibility with a real meaning.**
> **(B4c) DEAD-BAND** — either key lands in $[0.25, 1.00]$.
> **(B4d) CONFIGURATION DISAGREEMENT** — the keys select different bins across seeds, envelope
> modes or tone pairs. **A bin that is not stable across the frozen robustness axes is not a bin.**
> **(B4e) PRIMARY/SECONDARY CONTRADICTION** — the primary keys select bin 2 or 3 and the §4.6
> mode-sign pair selects the other one.

**Bin-integrity check, run now, before any value exists.** The four key-verdict states
{MOVES, DEAD, STATIC} × {MOVES, DEAD, STATIC} tile into exactly one of bins 2, 3, 4 with no gap and
no overlap: (MOVES, STATIC)→2, (STATIC, MOVES)→3, all seven remaining cells→4. Bins 0 and 1 are
evaluated first and are disjoint from each other by construction (0 is about the solve, 1 is about
the surface). **Every §8 falsifier routes to exactly one bin; none routes to two.** ✅

**These edges cannot be re-cut after the push.** They are stated as absolute numbers on
dimensionless, unit-free quantities (hops, ratios), so there is no unit choice, no normalisation
and no fitted scale through which they could be moved.

### §4.5 — The bins are not equally likely and the document says so before the run

**§9 pre-registers `AMBIGUOUS` — specifically B4b, `AMBIGUOUS-ON-THIS-CARRIER` — as the most
likely single outcome.** That is written before any measurement precisely so that landing there
cannot later be presented as a disappointment requiring a rescue.

### §4.6 — The SECONDARY test (mode-sign check) — SUPPLEMENTARY, and it can only *break* a bin

At fixed amplitude, on the frozen $\mathcal N$, using O6:

| pattern | reading |
|---|---|
| $\operatorname{sign}(\operatorname{Re}\Gamma_{\text{common}}) = +$ **and** $\operatorname{sign}(\operatorname{Re}\Gamma_{\text{diff}}) = -$, with $\bigl||\Gamma|-1\bigr| < 0.1$ on both | **VN key** — an OPEN on the breathing mode, a SHORT on the differential modes |
| $\operatorname{sign}(\operatorname{Re}\Gamma_{\text{common}}) = \operatorname{sign}(\operatorname{Re}\Gamma_{\text{diff}}) = -$ | **SAT key** — a level-set mirror does not care which mode hits it |
| anything else | **NO-KEY** — reports, selects nothing |

**This is a SIGN FLIP BETWEEN MODES AT FIXED AMPLITUDE, against a MAGNITUDE RAMP WITH AMPLITUDE in
the primary test — two different measurements, not a matter of precision.**

**Binding asymmetry, frozen:** the secondary test **cannot select bin 2 or bin 3 on its own** and
cannot upgrade a primary `AMBIGUOUS`. It has exactly one power: if it contradicts a primary bin-2
or bin-3 selection, the verdict becomes **`AMBIGUOUS` (B4e)**. *A supplementary observable may
break a verdict; it may never make one.*

### §4.7 — The known imbalance behaviour is a CONTROL, and is fenced from $\alpha$

Perturbing a balanced incident set by $\varepsilon$ gives $|V_{\text{node}}| = 2\varepsilon/3$ at
$z=3$, and power-out / power-in stayed $1.000000$ at every $\varepsilon$ tested. **An imbalanced
virtual-neutral wall does not dissipate — it TRANSMITS.** That is the correct shape for lossless
confinement with finite external coupling and is consistent with Axiom 3.

**It is entered here as a CONTROL and it is NOT a route to $\alpha$** — see guard (c), §6. **The
result document may not contain the sentence "the wall falls short of unity by $\alpha$" in any
form.**

## §5 — GEOMETRY AND PARAMETERS, FROZEN

### §5.1 — Carriers

| role | object | why this one |
|---|---|---|
| **PHYSICS carrier** | `build_srs_net(L=6, enantiomorph="right")` — srs-z3, $N = 8L^3 = 1728$ nodes, degree 3, $B = 3N/2 = 2592$ bonds | The D1-ratified production carrier, **and the same $L=6$ carrier the incumbent claim's own wall figure is drawn on** (`resonant-lc-solitons.md:54`, verbatim: *"L=6, 1728 interior z=3 nodes"*). The run is therefore on the same object the incumbent illustrates, not on a convenient smaller one. |
| **FIXTURE, never physics** | `build_ring_net(N=12)` — z=2, carrier tag `ring-z2-fixture` | The §7 non-triviality-gate host and the FL-4 reproduction fixture. **Its own carrier tag forbids physics use** and this document uses it for nothing else. |
| **CONTROL** | `build_srs_net(L=6)` with $A_{\text{bond}} \equiv 0$ (cold, empty) | The §3.1 negative control, the A5 artifact test, and the LOC-1 instrument receipt. |

**The carrier is asserted, not assumed:** the driver asserts `net.carrier == "srs-z3"` before any
physics configuration runs, so a fixture net reaching the physics path fails loudly.

### §5.2 — The saturation kernel path, FROZEN

**`vacuum_varactor_scatter.saturation_kernel`, with the canonical engine values
`A_cap = 0.99`, `S_min = 0.05`** (`vacuum_varactor_scatter.py:122`) — the path
`harmonic_balance_srs.bond_admittance` (`:309-322`) actually delegates to.

**Its measured consequence, banked at freeze so it cannot be discovered mid-run:** the cap binds
before the floor, so the **minimum reachable $S$ is 0.1410673598** and the shipped scatter path's
**best-case single-node reflection is $-0.6837926976$** (§2.5). **The physics arm therefore cannot
produce a $|\Gamma| \to 1$ single-node mirror at all, and no result may be read as a failure to
find one.** The alternative in-tree path (`graded_vacuum_network` / `srs_cage_winding`,
`A_cap=0.999`, `S_min=1e-3`) is **NOT used** and the divergence is routed in §11.

### §5.3 — Tone sets, FROZEN

`ToneSet` enforces the **canonical open interval $(0,\pi)$** on every tone and raises otherwise
(`harmonic_balance_srs.py:339-378`). Every value below is inside it, and $\theta \in \{0,\pi\}$ is
structurally unreachable.

| id | thetas (rad/step) | exact form | role |
|---|---|---|---|
| **T_A** | (0.6283185307179586,) | $(2\pi/10)$ | mode-key arm A, single tone |
| **T_B** | (1.8849555921538759,) | $(6\pi/10)$ | mode-key arm B, single tone |
| **T_A2** | (0.9424777960769379, 1.8849555921538759) | $(3\pi/10,\ 6\pi/10)$ | robustness: two-tone arm A |
| **T_B2** | (0.6283185307179586, 2.5132741228718345) | $(2\pi/10,\ 8\pi/10)$ | robustness: two-tone arm B |

$K_{\text{mode}}$ is evaluated on **both** pairs (T_A vs T_B, and T_A2 vs T_B2). Disagreement
between the pairs is `AMBIGUOUS` (B4d).

### §5.4 — Amplitude ladder, FROZEN

Drive scale $s \in \{1.0,\ 3.0,\ 10.0\}$ — **one decade, log-spaced, three points.**
$K_{\text{amp}}$ is evaluated between $s_{\text{lo}}=1.0$ and $s_{\text{hi}}=10.0$; the midpoint
$s=3.0$ is a **monotonicity receipt**, not a data point.

**Every rung reports its achieved $\max A_{\text{bond}}$.** If that does not increase monotonically
across the three rungs, the amplitude arm is **`ARTIFACT` (A6)** — the knob did not move the thing
it exists to move. **The amplitude arm runs ONLY inside `solve_self_consistent` (§4.3, gate
AMP-1).**

### §5.5 — Seeds, FROZEN

`20260826`, `20260827`, `20260828` — three integer seeds, driving the drive-phase pattern and
`A_init`. **The bin must be identical on all three.** Disagreement is `AMBIGUOUS` (B4d), never a
majority vote.

### §5.6 — The envelope-normalisation fork: NOT frozen by fiat, run as a ROBUSTNESS AXIS

`envelope_A_bond`'s own docstring binds this, verbatim (`harmonic_balance_srs.py:631-634`):
*"Two envelope forms exist in canon and this instrument supports BOTH — the choice is an **OPEN
normalization fork** the G2 prereg must freeze, **NOT settled here** (post-re-audit demotion,
2026-08-25; an earlier docstring asserted the two agree on traveling content — that was WRONG)."*

**This lane does not own that fork and does not close it.** Both arms are run:
`envelope_mode="c-state"` and `envelope_mode="full-tank"`. **The bin must be identical under both.**
A bin that differs between the arms is `AMBIGUOUS` (B4d) — which is the honest outcome, because a
verdict that depends on an un-adjudicated normalisation choice is a verdict about the choice.

### §5.7 — Termination

A **real** `Termination` with a non-empty port set and a non-zero drive, on every physics
configuration. **`term=None` is FORBIDDEN on the physics path** (§7 NT-2) — see guard (e).

### §5.8 — TAGGED ENGINEERING CHOICES (exhaustive; none can move a verdict)

| # | choice | value | why it cannot move a verdict |
|---|---|---|---|
| EC-1 | inner-solve `tol` | $1.0\times10^{-11}$ | Sits three decades below NT-4's gating $10^{-8}$; the achieved `residual_rel` is COMPUTED and gated per tone. |
| EC-2 | inner-solve `maxiter` | 20000 | Non-convergence routes to `INCONCLUSIVE`, never to a bin. |
| EC-3 | outer `outer_tol` | $1.0\times10^{-10}$ | Same: a stalled outer loop is `INCONCLUSIVE`. |
| EC-4 | outer `max_outer` | 200 | Same. |
| EC-5 | outer `relax` | 0.5 | Under-relaxation changes the path to the fixed point, not the fixed point. The converged $A$ field is what is measured, and its convergence is gated by EC-3. |
| EC-6 | `Y0` | 1.0 | A global admittance scale. **It cancels identically out of `a_nodes` (§2.4) and out of $\beta$ (§4.2), so it cannot move any observable in this document.** |
| EC-7 | `v_norm` | 1.0 | The envelope normalisation constant. Held fixed across the whole run so the amplitude ladder moves the drive and nothing else. |
| EC-8 | BFS hop metric | unweighted | The bond graph is the metric (§0 coordinates); there is no weight to choose. |

**No other numerical parameter exists in the driver.** If one appears during implementation it is a
design defect and is reported as one, not tuned.

### §5.9 — Configuration matrix (the full frozen run)

For each of the 3 seeds and each of the 2 envelope modes: the MODE arm runs the 4 tone sets at $s=1.0$ (4 solves), and the AMPLITUDE arm runs T_A at the 3 amplitude rungs inside `solve_self_consistent` (3 solves). Plus, per seed, one cold empty-vacuum control and one z=2 fixture run. **Every cell is run; no cell is dropped on the basis of what another cell
returned.**

## §6 — THE FIVE GUARDS AS PRE-REGISTERED CHECKS

**Every gate below is machine-evaluated and its result is REPORTED whether it passes or fails.
UNRUN ≠ PASSED.** A gate that cannot be shown to fire in both directions is not a gate.

### GATE SEC-1 — guard (a), the sector header

**Check.** The result document's every numbered claim carries the §0 triple (channel, axis,
phase-state) or an explicit pointer to it, and the driver's JSON stamps
`{"channel": "scalar-shunt", "axis": "node-voltage-balance", "phase_state": <"cold"|"graded">}`
on **every** configuration record.
**PASS.** Every configuration record carries all three fields, and the `phase_state` field is
COMPUTED from the converged $A$ field (`"cold"` iff $\max A_{\text{bond}} < 10^{-12}$), never
declared.
**FAIL.** Any record missing a field, or any record whose declared `phase_state` contradicts the
computed one. → the run is **VOID**, not binned. *(A gate that consumes a self-declared field is a
checklist, not a gate — so this one reconciles the label against the computed truth and a
contradiction is a FAIL.)*

### GATE BCAST-1 — guard (b), the structural-null trap

**Check.** Two parts, both required.
1. **NON-BROADCAST BY CONSTRUCTION.** The driver asserts that the converged $A_{\text{bond}}$ field
   has $\mathrm{std}(A_{\text{bond}}) / \mathrm{mean}(A_{\text{bond}}) > 10^{-6}$ globally — the
   grading is genuinely spatial, not a uniform level.
2. **NON-BROADCAST AT THE NULL.** At every node $u \in \mathcal N$, the driver asserts that the
   three incident port admittances are **not** equal to within $10^{-12}$ relative.
**PASS.** Both assertions hold on every configuration.
**FAIL.** Either fails → **bin A4, `ARTIFACT`**.
**BOTH-DIRECTIONS RECEIPT (mandatory).** A mutation fixture runs the identical pipeline with a
deliberately **per-node-uniform** $Y$ field and asserts BCAST-1 **FAILS** on it. *A gate that has
never been seen to fire is not evidence.*

### GATE ALPHA-1 — guard (c), the $\alpha$-echo trap

**The adjudication being honoured, quoted verbatim from canon** and verified on this branch at
[`device-circuit-models.md:207`](../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md):
*"The tempting follow-up — 'derive the loaded $Q=1/\alpha$ from the EM-port admittance' — is
**ADJUDICATED CIRCULAR (do NOT pose it):** the engine's radiative leak is literally `1.0 - alpha`
… = the instrument-echo trap … **no $\alpha$-free path to $137$.**"*

**Check.** Three parts.
1. **$\alpha$-FREE BY CONSTRUCTION.** A test asserts the driver module imports **no** $\alpha$
   symbol — not `ALPHA`, not `ALPHA_COLD_INV`, not `Q_TANK` — and that no emitted number in the
   results JSON is within $10^{-6}$ relative of $\alpha$, $1-\alpha$, $\sqrt\alpha$,
   $\sqrt{1-\alpha}$, $\alpha^{-1}$ or $\alpha^{-3}$.
2. **NO $|\Gamma|^2$-TO-$\alpha$ MAP.** The driver computes **no** quantity of the form
   $1 - |\Gamma|^2$ and the result document contains **no** sentence mapping residual imbalance
   onto $\alpha$ in any form.
3. **THE FORBIDDEN SENTENCE, NAMED.** *"the wall falls short of unity by $\alpha$"* — and any
   paraphrase — **may not appear in the result document.** It is named here explicitly because it
   is exactly the number this arc would most like to explain, and because naming it is the only
   way the prohibition can be checked rather than intended.
**PASS.** All three hold.
**FAIL.** Any fails → the run is **VOID**, not binned.

**★ Why this gate has real work to do.** $\beta$'s ceiling and the level-set ceilings of §2.5 both
sit in the neighbourhood of numbers that $\alpha$-adjacent quantities also occupy. **The gate is
not decorative: the whole design is one coincidence away from an instrument echo, and the defence
is that $\beta$ is $\alpha$-free by construction (pure linear algebra on $Y$ and $v$), not that
anyone intends to be careful.**

### GATE FENCE-1 — guard (d), the freeze and the instrument fence

**The fence being honoured:** `harmonic_balance_srs` self-declares **INSTRUMENT-GRADE
INFRASTRUCTURE** that *"mints no physics claims"*. This lane consumes it as an instrument and mints
nothing through it.

**Check.**
1. **FREEZE-BY-PUSH.** This document's frozen content SHA is recorded in its own freeze commit and
   the branch is pushed **before** any driver file exists in the tree. Verified by `git ls-remote`,
   **never** by a push exit code.
2. **FROZEN GEOMETRY.** Every §5 value enters the driver by named constant, and a test asserts the
   driver contains no numeric literal for carrier size, tone, amplitude, seed, $\tau_\beta$, or
   either key edge outside the frozen constant block.
3. **NO ENGINE TOUCH.** The lane modifies **no** file under `src/ave/`. Verified by diff at PR.
**PASS.** All three.
**FAIL.** Any → the run is **VOID**.

### GATE LOC-1 — the §3.1 instrument receipt (the LOCAL control)

**Check.** On the run's **own** converged $Y$ field, at every node of every configuration:
$\max\bigl|\operatorname{spec}(S_u) - \{+1\}\cup\{-1\}^{z-1}\bigr| < 10^{-12}$ and
$\bigl|\operatorname{tr}S_u - (2-z)\bigr| < 10^{-12}$.
**PASS.** Both, everywhere. **This is an instrument receipt and it is NOT evidence for either
ontology** (§3.3).
**FAIL.** → the run is **VOID** — the shipped operator is not the operator §2 characterised.

### GATE AMP-1 — the §4.3 structural precondition on the amplitude arm

**Check.** Every amplitude-arm datum comes from a `solve_self_consistent` call whose outer loop
reports `converged=True` and $\ge 2$ outer iterations, **and** the achieved $\max A_{\text{bond}}$
increases monotonically across $s = 1.0, 3.0, 10.0$.
**PASS.** Both.
**FAIL.** Either → **bin A6, `ARTIFACT`**. **A single linear tone solve can never supply an
amplitude-arm datum**, because $K_{\text{amp}} \equiv 0$ there for both ontologies by linearity.

### GATE SEP-1 — the §4.2 threshold-resolution receipt

**Check.** $\mathrm{sep} \ge 10$ (O3) on every configuration; the value is REPORTED for each.
**FAIL.** → **bin A3, `ARTIFACT`**.

### §6.1 — Gate summary table

| gate | guard | failure routes to |
|---|---|---|
| SEC-1 | (a) | VOID |
| BCAST-1 | (b) | `ARTIFACT` (A4) |
| ALPHA-1 | (c) | VOID |
| FENCE-1 | (d) | VOID |
| NT-1…NT-4 (§7) | (e) | `INCONCLUSIVE` (bin 0) |
| LOC-1 | §3.1 | VOID |
| AMP-1 | §4.3 | `ARTIFACT` (A6) |
| SEP-1 | §4.2 | `ARTIFACT` (A3) |

**VOID ≠ a bin.** A VOID run interprets nothing, produces no verdict, and is reported as a
mechanism finding about the instrument. It is not `INCONCLUSIVE` (which is a statement about the
solve) and it is not `ARTIFACT` (which is a statement about the surface).

## §7 — THE NON-TRIVIALITY GATE — guard (e), and the live silent-zero trap it closes

### §7.1 — The trap, verified at source on this branch

`solve_tone(a_nodes, conn, theta, term=None, ...)` (`harmonic_balance_srs.py:534-541`) returns
$\lVert v\rVert = 0$ with `converged=True` and `residual_rel = 0.0`. **Mechanism, read off the
shipped code and reproduced:**

1. With `term=None`, `_term_mask` returns an all-`False` mask (`:527-532`) and `v_s` stays all
   zeros (`:565-567`).
2. So the right-hand side is $b = M(v_s)\!\mid_{\text{free}} = \mathbf 0$ (`:572`).
3. `lgmres(A, b, x0=x_init, rtol=tol, atol=0.0, ...)` (`:600`) is then called with $b=\mathbf 0$.
   **SciPy's iterative solvers short-circuit on $\lVert b\rVert = 0$ and return the zero vector
   with `info = 0`, DISCARDING any `x0`.** Reproduced on the installed SciPy 1.15.3: a call with
   $b=\mathbf 0$ and a non-zero `x0` returns $\lVert x\rVert = 0.0$, `info = 0`.
4. `residual_rel` is then $0 / \max(0, 10^{-300}) = 0$ (`:606`), and `converged` is
   `bool(info == 0)` = **`True`** (`:611`).

**This is why $\theta$ being an INPUT matters** (`:534-537`): with no drive, the system is
**homogeneous**, and the warm-start path (`:586-597`) cannot rescue it because its only product is
`x_init`, which `lgmres` discards at step 3. **Warm-starting at the exact true ring mode still
returns zero.**

**The module's only `term=None` disclosure covers a DIFFERENT function.** The
`SCAFFOLD-ABSENT BRANCH` note at `:805-815` sits in `source_idle_report`'s docstring (that function
is defined at `:787`) and is about *that* function returning literal zeros for
`source_amp`/`exchange_amp`/`P_in`/`P_out`. **`solve_tone` carries no such note.**

**Provenance, stated honestly.** The label *"FL-4"* for this trap is **lane-local and unregistered
in the corpus** — `grep` across the tree returns **zero** hits for it in this sense; the only
registered `FL-4` is an unrelated $K_4$-homonym flag at
`research/2026-08-24_solver-crosscheck-phase0_requirements.md:385`. **The MECHANISM above is
verified at source and reproduced; the LABEL is not a corpus object.** It is routed in §11.

**The canonical statement of the rule**, verified verbatim on this branch at
[`_orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md`](../_orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md) §4:
*"**Mandatory regardless:** a **non-triviality gate** — "converged" is not "non-zero" (the lane
produced a converged trivial solution that would have read as a result)."*

### §7.2 — The gate, frozen. All four parts, on EVERY tone of EVERY configuration, evaluated BEFORE any $\beta$ is computed.

| # | assertion | rationale |
|---|---|---|
| **NT-1** | $\lVert v^{(m)}\rVert > 10^{-6}\cdot s$ for every tone $m$, with $s$ the configuration's drive scale | A literal zero fails. The bound scales with the drive so it is a **relative** floor, not an absolute one that a small-drive rung could trip innocently. |
| **NT-2** | `term is not None` **and** `len(term.ports) > 0`, asserted at the call site | **`term=None` is FORBIDDEN on the physics path.** This closes step 1 of §7.1 structurally. |
| **NT-3** | $\lVert$`term.drive[m]`$\rVert > 0$ for every tone, asserted, **and** $\lVert b\rVert > 0$ asserted immediately after the RHS is formed | This is the assertion that makes SciPy's $\lVert b\rVert = 0$ early-return branch **unreachable**. It is placed on $b$ itself, not on a proxy. |
| **NT-4** | `converged == True` **AND** `residual_rel` $< 10^{-8}$ **AND** $\lVert v\rVert > 0$ | **`converged` alone is never accepted** (R58 §4). Three conjuncts, because the trap satisfies the first and the third-with-zero simultaneously. |

**Any NT failure routes to `INCONCLUSIVE` (bin 0). Never to a bin 2/3/4 verdict.**

### §7.3 — The both-directions receipt (mandatory; the gate must be seen to fire)

**FL4-FIXTURE.** On the z=2 ring fixture (`build_ring_net(12)`, §5.1), the driver runs the
identical pipeline **twice**:

1. **`term=None`** — and asserts **NT-1, NT-2 and NT-3 all FAIL**, with the returned
   $\lVert v\rVert$ recorded as literally `0.0` and `converged` recorded as `True`. **This is the
   receipt that the trap is real and that the gate catches it.**
2. **warm-started at the exact ring mode** `ring_mode(12, m)` with `term=None` — and asserts the
   result is **still** $\lVert v\rVert = 0$. **This is the receipt that a warm start does not
   rescue it**, which is the part of the trap that would otherwise look like a safe workaround.

**Neither fixture run may appear in any bin, on any carrier, for any purpose other than this
receipt.** The ring's own carrier tag (`"ring-z2-fixture"  # known-case fixture, NOT a physics
carrier`) binds this.

**Anti-tautology property, stated explicitly.** The FL4-FIXTURE does **not** encode this lane's
branch shape, live line numbers, or its own key bytes: it calls the shipped `solve_tone` and reads
the shipped `ToneSolution` fields. If a future change to `solve_tone` removed the trap, part 1's
assertion would fail — **which is the correct behaviour for a fixture that measures a defect** and
is recorded here so that failure is read as "the defect is gone", not as "the gate is broken."

## §8 — WHAT WOULD FALSIFY THE VIRTUAL-NEUTRAL READING — stated before the run, in the run's own terms

**H-VN is falsified by this run if any of the following is measured.** Each is stated as a
numerical condition on a quantity §4 defines, so none of them can be argued about after the fact.

| # | falsifier of **H-VN** | bin |
|---|---|---|
| **FS-1** | $K_{\text{amp}} > 1.00$ hop **and** $K_{\text{mode}} < 0.25$ hop, on every configuration. **The surface tracks the drive and ignores the tone — the H-SAT key fires and the H-VN key does not.** This is the clean falsification. | `SATURATION` |
| **FS-2** | $\mathcal C = $ `False` — the balanced set exists but **is not closed**. H-VN requires a *closed surface* of simultaneously balanced nodes; an open sheet, a filament, or a scatter of isolated balanced nodes **does not confine anything** and does not support the register move. | `ARTIFACT` (A2) |
| **FS-3** | $\mathcal N$ = the **cold empty-vacuum** control's null set. A balance surface that is already present in empty vacuum is the §3.1 free-everywhere object and diagnoses nothing. | `ARTIFACT` (A5) |
| **FS-4** | $\mathcal N = \varnothing$ at every configuration — **no node is ever balanced to $\tau_\beta$** on the srs carrier with a bound state on it. H-VN's locating equation has no solutions, so H-VN has no referent here. | `ARTIFACT` (A1) |
| **FS-5** | BCAST-1 fails at the null: the balanced nodes are exactly the nodes where the admittances happen to be uniform. **The null is then the broadcast artifact guard (b) exists to catch, not a virtual neutral.** | `ARTIFACT` (A4) |
| **FS-6** | The §4.6 mode-sign pair returns the **SAT key** ($\operatorname{Re}\Gamma_{\text{common}}$ and $\operatorname{Re}\Gamma_{\text{diff}}$ both negative) while the primary keys select `VIRTUAL-NEUTRAL`. **A virtual neutral must be an OPEN on the breathing mode; a surface that shorts both modes is not one.** | `AMBIGUOUS` (B4e) |
| **FS-7** | The bin is `VIRTUAL-NEUTRAL` under one envelope normalisation and not the other, or on one seed and not another, or on one tone pair and not the other. | `AMBIGUOUS` (B4d) |

**And the symmetric statement, because a discriminator that can only kill one side is not one.
H-SAT is falsified by:** $K_{\text{amp}} < 0.25$ **and** $K_{\text{mode}} > 1.00$ on every
configuration (bin 3) — the surface ignores the drive and tracks the tone. **Plus one structural
falsifier already banked at freeze:** the shipped kernel's clip puts the best single-node
reflection at $-0.6837926976$ (§5.2), so **if the measured surface reflects harder than that, the
reflection cannot be coming from single-node saturation on this kernel path.** *(That is a
consistency observation, not a gating criterion — it is REPORTED, and it cannot move a bin.)*

**★ The falsifier that is NOT here, and why.** *"The residual imbalance does not equal $\alpha$"*
is **not** a falsifier of anything in this document, and its converse is not evidence. Guard (c)
and gate ALPHA-1 forbid the mapping in both directions. **A run in which the residual imbalance
came out at $1-\alpha$ would be reported as an instrument echo to be investigated, never as a
result.**

## §9 — THE HONEST EXPECTED OUTCOME

**Written before any measurement, so that landing here cannot later be presented as a
disappointment requiring a rescue.**

### §9.1 — The most likely single outcome is `AMBIGUOUS-ON-THIS-CARRIER` (bin 4, B4b)

**Three independent reasons, each of which alone would be enough:**

1. **The carrier may not host a bound state sharp enough to have a surface.** The run *assumes* a
   bound state and asks where its boundary is. On a $L=6$ periodic srs cell with a driven scaffold,
   the converged $A$ field may be a broad, smooth hump with no sharp edge at all — in which case
   $\mathcal N$ is either empty (A1) or fails the closure test (A2), and there is no surface to
   bin. **This is the single most likely failure and it is a failure of the CARRIER to present the
   object, not of either ontology.**
2. **The shipped kernel cannot make a hard wall.** §5.2's clip puts the best single-node reflection
   at $-0.684$, which is not a mirror. If H-SAT's surface needs a hard level set to be sharp, the
   frozen kernel path may not be able to produce a sharp enough one for $K_{\text{amp}}$ to clear
   one hop — landing $K_{\text{amp}}$ in the dead band (B4c) rather than at STATIC.
3. **The two keys may not be cleanly separable on a $z=3$ periodic cell.** Changing $\theta$
   changes the phasor field, which changes the DP-1 envelope, which changes $A$, which changes $Y$
   — **the mode knob leaks into the amplitude channel through the self-consistent loop.** If that
   leak is large, **both** keys fire and the verdict is B4a. **This is a real coupling in the
   shipped operator and no amount of care in the driver removes it**; the design's answer is to
   measure it and bin it honestly, not to pretend the knobs are independent.

### §9.2 — What `AMBIGUOUS-ON-THIS-CARRIER` would MEAN

**It would mean the discriminator does not resolve on this carrier, and nothing more.** In
particular it would **NOT** mean:

- that the register move is wrong (`AMBIGUOUS` selects nothing);
- that `def-vyvsn1` is confirmed (an un-resolving test confirms no incumbent);
- that the virtual-neutral picture is unfalsifiable (§8 lists seven ways this run could kill it);
- that a larger $L$ or a different carrier would resolve it (that is a hypothesis for a **next**
  prereg, not a conclusion of this one).

**What it WOULD license** is one narrow, bankable statement: *the closed-balance-surface condition
on $M = C\cdot\mathrm{blockdiag}(S)$ was computed for the first time, on the $L=6$ srs carrier, and
the two ontologies' keys did not separate there — with the measured $K_{\text{amp}}$, $K_{\text{mode}}$,
$\mathrm{sep}$ and closure receipts reported.* **That is a real result and it is worth the run**,
because §2.7's fork means the corpus currently has **no** computed answer to the question at all.

### §9.3 — Rough prior on the five bins, declared

| bin | rough prior | why |
|---|---|---|
| `AMBIGUOUS` (all sub-cases) | **~45%** | §9.1's three reasons |
| `ARTIFACT` | **~30%** | A1/A2 dominate — the surface may simply not close on a periodic $L=6$ cell |
| `INCONCLUSIVE` | **~10%** | the self-consistent loop under strong grading is where Picard stalls |
| `VIRTUAL-NEUTRAL` | **~10%** | it is the reading the arc favours, and that is exactly why it gets the lower number here |
| `SATURATION` | **~5%** | §2.6 already measured the A1 branch as transparent at the stated operating point, so a clean amplitude key is the least expected |

**These priors are not a prediction and they gate nothing.** They exist so that the strength of a
surprise can be judged against something written down, and so that the arc's own preference is on
the record as a preference **before** it can be mistaken for a finding.

### §9.4 — The one outcome that would be a genuine surprise

**A clean bin-3 `VIRTUAL-NEUTRAL` — $K_{\text{amp}} < 0.25$ and $K_{\text{mode}} > 1.00$ on all
twelve configurations, with $\mathcal C$ = `True` and the §4.6 mode-sign pair returning the VN
key.** That would discharge `def-anat3s`'s banked *"CONJECTURED $\equiv$ wall"* conjecture in the
scalar channel and would be a real input to a register ruling.

**It would still not be a chord.** It would be a statement about where a surface sits in a model
we built, on a carrier we chose, in one channel, measured by an instrument that self-declares it
mints no physics claims. **The §1.4 fence binds on a positive result exactly as hard as on a
negative one** — and historically that is the direction in which this discipline slips.

## §10 — ANTI-RESCUE GUARD *(placeholder)*

## §11 — ROUTED FLAGS *(placeholder)*

## §12 — SKILL-SELECTION PLAN *(placeholder)*
