[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Coordinate-discipline register for Hamiltonian phase-space mechanics: collects the corpus's existing phase-space canon (def-69f472 coordinate space, DP-1 tank envelope, A46 firewall, Nyquist-cell phasor area, (2,q) winding portraits) into one register organized by a coordinate-ladder spine; every row is a pointer at its canonical home carrying that home's own status, or an explicitly graded ASSEMBLY/WALK identification, and every row carries the three per-row fields inline in §2.1; all Smith-chart-ontology content is pointer-only at the Grant-PARKED cp1-canonization open item; mints no claim, moves no solidity, adjudicates nothing (consistency/translation register only)."
-->

# Phase Space ↔ AVE Translation (the coordinate-discipline register)

> **Register: NO-CLAIM consistency/translation leaf.** This leaf mints no claim, moves no
> solidity, and adjudicates nothing. It closes a documented gap — the corpus uses phase-space
> vocabulary everywhere (`def-69f472`, the A46 firewall, the $(2,q)$ winding portraits, the
> Nyquist-cell phasor area) but no spoke ever translated the *formalism* of Hamiltonian
> phase-space mechanics itself: [`translation-qm.md`](translation-qm.md) has **zero** hits for
> hamiltonian / symplectic / liouville / conjugate / action-angle / adiabatic (two-method
> search, 2026-08-24). Every row's canonical-home column carries the home the row POINTS AT
> plus that home's status as stated there. Scope fence: the electron's particle-identity
> content is owned by
> [`electron-identification.md`](../../vol2/particle-physics/ch01-topological-matter/electron-identification.md)
> and siblings, NOT duplicated here — this leaf owns the COORDINATE-SPACE FORMALISM axis only.
>
> **Per-row fields (no exemption claimed).** The diagrammatics per-row-fields EXEMPT status
> ([`README-architecture.md`](README-architecture.md) §5) is a **per-spoke Grant ruling and is
> NOT inherited**; no exemption is claimed or presumed for this spoke. **Every** §2 row —
> pointer rows included — carries the three §4 fields (means-test / Ax3 / provenance) inline
> in §2.1. Whether Grant wants to grant this spoke a pointer-row exemption is his question to
> rule on in the registering PR; nothing in this leaf presumes the answer.
>
> **Smith-chart-ontology PARK (binding).** All Smith-chart-ontology content in this leaf is
> **pointer-only** at the Grant-PARKED open item
> `_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md` — title verbatim:
> *"ℂP¹ Smith-chart ontology canonization — PARKED; re-open only if an engine lane wants the chart as an instrument"*.
> This leaf mints nothing there and re-opens nothing; un-parking is Grant's alone
> (§2 row 7, §2.1 row 7, §5 gap 8).
>
> **Charter-gate note (deliberate non-carry).** The ⚑ qed-trace-charter standing gate on
> [`translation-diagrammatics.md`](translation-diagrammatics.md):43 stands, by its own text, *"over this section"* — the diagrammatics leaf's §1 Feynman-formalism reading. It is
> diagrammatics-specific: no other spoke carries it and `README-architecture.md` never
> references the charter. This spoke restates no diagram-formalism reading, so the gate's
> scope does not reach it (verified 2026-08-24; if a future edit adds diagram-formalism
> content here, re-adjudicate).
>
> **Provenance.** 2026-08-24, from Grant's directive to formally audit and document the
> chat-walked standard-mechanics ↔ substrate phase-space translation. Built on a three-lane
> corpus pull (prior-art / receipts / structural-template), each lane returning file:line
> receipts, all verified against AVE-Core `main` at `90753eef`, then put through a
> three-lens adversarial audit (echo-prune / canon-collision / read-and-run gates) whose 28
> findings — 3 BLOCKER findings, 2 distinct blocker defects — were repaired in place 2026-08-24: the Smith-chart row re-scoped
> under the standing Grant PARK, the ladder's T1→T2 link restated as a coordinate change,
> the action-cell row downgraded to WALK pending the T1↔T2 area bridge (§5 gap 9), the
> PROPOSED statuses carried onto rows 4/5 and the rim-inversion pointers, and the gap
> ledger's search receipts corrected against the audit's counter-hits. Where the walk
> disagreed with receipts, the receipts won. The organizing ladder in §1 is a new assembly
> of individually-canonical rungs; it is recorded so it can be attacked, not because it is
> settled. Per the repairs-need-reaudit discipline, this repaired draft is NOT a verified
> draft until a fresh audit pass runs.

> **Sector declaration (house rule — declare before any substrate word).**
> **SECTOR:** per-sector per DP-1 — each sector's tank envelope is normalized against its own yield: `vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md:62` — *"It is **per-sector** (each sector against its *own* yield, per the per-yield-normalized combine)"*.
> The A1 dilatation sector and the Cosserat/T2 sector each carry their own tank plane; nothing below cross-wires them (mass = A1, charge = Cosserat winding): `vol2/particle-physics/ch01-topological-matter/electron-identification.md:53` — *"real-space body ⊥ phase-space winding ⊥ mass dilatation"* … *"**Never cross-wire**"*.
> **REGIME / PHASE-STATE:** sub-yield lossless-reactive interior (Ax3) up to and including
> the Axiom-4 saturation rim; the disk interior is the cold / sub-saturation state, the rim
> is saturation onset. No ruptured/plastic-regime content.
> **COORDINATES:** everything below is phase-space (phasor) coordinates, never real-space lattice-Cartesian — the A46 discipline: [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):17 — *"the disk/rim below is a **PER-MODE PHASE-SPACE** statement"* … *"**NOT** a real-space radial profile"* (that home's own banner is ⚠ PROPOSED — carried at §3.1).

## §1 — The two definitions and the coordinate ladder [ASSEMBLY — ladder framing new in this leaf; every rung individually canonical]

**Standard-mechanics side (the discipline being translated).** Phase space is the cotangent
bundle $T^*Q$ with coordinates $(q,p)$ and symplectic form $\omega = \sum dq \wedge dp$. Its
load-bearing properties: (1) a point is a complete state — deterministic flow, trajectories
never cross; (2) the irreducible unit is the *conjugate pair* — dimension is always even;
(3) the invariant geometry is **area, not length** — Liouville's theorem, adiabatic
invariants, and the action $\oint p\,dq$ are all area statements, and no metric appears in
the definition; (4) for a **2-DOF integrable system** (a 3-dimensional energy surface),
bounded motion lives on invariant 2-tori and a $p{:}q$ frequency-locked periodic orbit
traces a $(p,q)$ torus knot on its invariant torus — but this orbit–knot weld is
**2-DOF-specific**: closed curves in $\geq 4$ dimensions can always be unknotted, so it is
NOT a theorem of higher-DOF phase spaces; (5) real space sits *inside* phase space as the
$q$-half, and the space is unbounded; QM tiles the conjugate plane in cells of area
$h = 2\pi\hbar$ (the semiclassical cell per conjugate pair is $h$, not $\hbar$ —
$\oint p\,dq = nh$, state count = volume$/h^n$).

**Substrate side (the hub).** The corpus's adjudicated definition is `def-69f472`: [`vocabulary-register.md`](../vocabulary-register.md):164 — *"the $(V_{inc}, V_{ref})$ / Clifford-torus **phasor coordinate space** — a distinct coordinate space from real space"* — status **ambiguous**, held so solely because the surface form is conflated with a SIZE (the A46 leak; `vocabulary-register.md:170` — *"Real-space ≠ phase-space is canonical as COORDINATES, NOT a size-claim"*).
The register pins the canonical home at `vol1/ch8-alpha-golden-torus.md` (its `:29` pin; the coordinate-meaning sentence sits in the identity block at `vol1/ch8-alpha-golden-torus.md:31` — *"The trefoil lives in phase space; the soliton lives in real space."*).

**The coordinate ladder (the register's spine — new assembly; each rung individually
canonical, the LADDER framing itself 0-hit new, two-method verified 2026-08-24).** What the
corpus calls "phase space" is not one space but a family of related coordinate spaces. The
ladder below names each space, what it carries, and how it is reached from its neighbour.
**The links are NOT all reductions** — T0→T1 and T2→T3 restrict, T2→T4 quotients, T2→T5
time-averages, but **T1→T2 is a change of coordinates and of support, not a forgetting**
(the draft's "tower of successive reductions" spine claim was wrong at exactly that link;
repaired 2026-08-24). Every phase-space statement in the corpus lives on exactly one rung,
and every claim drawn on a lower rung must declare which rung it came down from.

| Rung | Space | Carries | Link from neighbour | Canonical home |
|---|---|---|---|---|
| **T0** | Full network state — all node/bond DOF of the chiral LC network | The complete state (the only rung where "point = complete state" holds) | — | Ax 1–4 (INVARIANT-S2) |
| **T1** | One bond tank's conjugate plane $(V_{inc}, \Phi_{link})$ | The conjugate-pair / area structure (§2 row 2); DP-1 envelope defined here | T0→T1: **restriction** (forgets every other tank) | `vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md:37` — *"Integrated flux on bond LC's L-state (conjugate to $V_{inc}$ per A-010)"* — and DP-1 at its `:62` |
| **T2** | Bond-pair phasor space $(V_{inc}, V_{ref}) \in \mathbb{C}^2$ | The Golden-Torus metric content $(R,r)$; the phasor-area/Nyquist-cell statement (§2 row 3) | T1→T2: **COORDINATE CHANGE + support change, NOT a reduction** — the second coordinate changes physical variable ($\Phi_{link}$, an L-state flux → $V_{ref}$, a C-state read-out) and the support changes (one bond → a bond pair); no corpus map bridges the two planes' areas (§5 gap 9), and the A1⊥T2 fence stands over any future bridge: `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` — *"$V_{ref}$ is a read-only projection of the same scalar $V$, not an independent DOF"* | `def-69f472`; `vol2/particle-physics/ch01-topological-matter/electron-identification.md:31` — *"The $(2,3)$ 'trefoil' is the phase-space winding pattern, NOT a real-space trefoil knot"* |
| **T3** | Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (fixed-magnitude phase circles) | $\pi_1 = \mathbb{Z}\times\mathbb{Z}$ winding classes — the $(2,q)$ portraits | T2→T3: **restriction** to the rim circles (amplitudes frozen at the rim, §3.1) | [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):47 — *"each factor is a rim-circle (frozen amplitude, free phase)"* (home banner ⚠ PROPOSED, §3.1); KB `manuscript/ave-kb/CLAUDE.md:22` — *"labels refer to **phase-space winding portraits** on the bond-pair LC tank"* |
| **T4** | $\Gamma = V_{ref}/V_{inc}$ ratio disk (the Smith chart, as an instrument) | The reflection ratio — impedance-boundary content. Its **ontology is Grant-PARKED** (§2 row 7 — pointer only) | T2→T4: **ratio** — overall amplitude and common phase drop out of $\Gamma$ by definition (the action scale); the draft's claim that this deletes *the symplectic (area) content* was mathematically WRONG — corrected at §2.1 row 7 | alive canonical layer: `vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md:78` — *"the Smith locus is convention-independent"*; ontology parked (§2 row 7, §5 gap 8) |
| **T5** | Per-mode envelope disk $(A, \theta)$ | The DP-1 reactive-amplitude envelope; the A46 disk/rim statement (`PER-MODE PHASE-SPACE`) | T2/T3→T5: **cycle time-average** — DP-1: *"NOT an instantaneous phase snapshot"* | `vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md:62`; [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):17 (home banner ⚠ PROPOSED, §3.1) |

**Basis note (d–q / I-Q axes — required to place canon's own winding statements).** Canon
states the same T2/T3 objects in TWO bases: the $(V_{inc}, V_{ref})$ basis above, and the
**d–q** basis of the bond-pair tank — `vol1/ch8-alpha-golden-torus.md:31` — *"the **phase-space Clifford-torus winding pattern** of the electron's bond-pair LC tank (2 windings on the d-axis, 3 windings on the q-axis)"*;
same assignment at `electron-plumbing-primer.md:57` — *"2 windings on the d-axis, 3 on the q-axis"* — and the two written as one plane at `vol2/particle-physics/ch01-topological-matter/electron-identification.md:50` — *"on the bond-pair LC-tank $(V_{inc}, V_{ref})$ / d–q plane"*.
A per-axis winding-count assignment is basis-dependent, so any rung-T2/T3 statement quoting
per-axis integers must declare its basis alongside its rung; canon's per-axis $(2,3)$
statements are d–q-basis statements. This register adjudicates no preferred basis.

**The three-disk firewall (formalizing A46 + the register's ambiguity flag — the two prior
homes of this discipline).** Three different disks appear above and are routinely conflated;
they are different rungs and carry different structure:

1. the **per-mode amplitude disk** (T5) — the A46 object; its rim is Axiom-4 saturation;
2. the **phasor plane** (T1/T2) — where the area/Nyquist-cell and Golden-Torus $(R,r)$ metric content live; the $\pi_1$ factorization is explicitly **radius-blind**: [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):47 — *"NOT a metric identification of the rim-radius with the Golden-Torus `R·r=¼` semi-axes"*;
3. the **$\Gamma$-ratio disk** (T4) — a ratio coordinate: overall amplitude and common phase drop out of $\Gamma$ by definition, so amplitude- or action-normalized claims cannot be read off it alone (§2.1 row 7); its ontological reading is PARKED (§2 row 7).

A physics claim drawn on any disk must declare its rung. This is the discipline whose prior
homes are the A46 blocks and the `def-69f472` open-ambiguity flag; the ladder gives it a
formal shape, nothing more.

## §2 — The correspondence table

Grades: **CANON** = both sides separately canonical AND the identification already stated in
the corpus (column 5 cites where); **CANON-POINTER** = as CANON but the home's own status is
below canon (restated verbatim, never upgraded); **ASSEMBLY** = both sides canonical, the
identification is new in this leaf — consistency-class, buys no number;
**ASSEMBLY-on-PROPOSED** = as ASSEMBLY but the substrate home's own status is PROPOSED /
not-yet-canonical — the row inherits that status and lands nothing; **PARKED-POINTER** =
the content is Grant-PARKED — the row is a pointer at the parked item and mints nothing;
**WALK** = un-ratified framing, explicitly tagged. Per-row payload direction + echo-prune
verdicts + the §4 `README-architecture.md` fields for EVERY row are in §2.1.

| # | Phase-space concept | Substrate object | Grade | Canonical home + status |
|---|---|---|---|---|
| 1 | Phase space (the state-space noun) | the $(V_{inc}, V_{ref})$ / Clifford-torus **phasor coordinate space**, distinct from real space | **CANON** | `def-69f472`, [`vocabulary-register.md`](../vocabulary-register.md):160 — status **ambiguous** (A46 size-conflation only; the coordinate-space meaning is *"canonical, well-cited"* per its `:170`); register-pinned canonical home `vol1/ch8-alpha-golden-torus.md` (see §1) |
| 2 | Canonical conjugate pair $(q,p)$; the symplectic 2-plane | the bond LC tank's $(V_{inc}, \Phi_{link})$ pair — *"Integrated flux on bond LC's L-state (conjugate to $V_{inc}$ per A-010)"* | **ASSEMBLY** | pair itself CANON at `vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md:37`; node-level E/B conjugacy [`translation-circuit.md`](translation-circuit.md):35 — *"the structural origin of $\mathbf{E}$ and $\mathbf{B}$ as conjugate variables at every node"*; state variable at `common/physics-lineage-map.md:62` — *"The state variable is the V↔Φ_link flux-linkage conjugate pair"*. The *symplectic-2-plane* naming is new here (0 corpus hits for symplectic form/structure, two-method) |
| 3 | Action / area invariant $\oint p\,dq$; the $h$-area cell ($h = 2\pi\hbar$, §1 property 5) | the time-averaged phasor enclosed area at Axiom-4 self-saturation onset = the **Nyquist cell** cross-section, $\pi R r = \pi(d/2)^2$ — pointed at, with its home's caveat; the $\oint p\,dq$ LABELING of it is **un-bridged** (T1-vs-T2 area mismatch, §2.1 row 3, §5 gap 9) | **CANON-POINTER** (the identification, at its home) **+ WALK** (the action-cell labeling) | Q-EMBED-SEL-1: [`boundary-observables-m-q-j.md`](../boundary-observables-m-q-j.md):81 — *"the time-averaged phasor enclosed area at Axiom-4 self-saturation onset equals the Nyquist cell cross-section area"* — and `vol1/ch8-alpha-golden-torus.md:48`. **Mandatory status caveat**: `vol2/particle-physics/ch01-topological-matter/electron-identification.md:77` — *"substrate-canonical INPUT (not separately Class-2 derived"* … Class B. $\hbar$ = *"Ax1 action quantum"* (its `:95` — the only corpus site) |
| 4 | Resonant $(p,q)$ torus-knot orbit — for a **2-DOF integrable system only** (§1 property 4), a $p{:}q$ frequency-locked periodic orbit traces a $(p,q)$ torus knot on its invariant torus | the $(2,q)$ **phase-space winding portrait** on the bond-pair Clifford torus — canonical strictly as a **static resonance LABEL**, NOT as a frequency-locked orbit: the dynamical orbit reading was tested and read NEGATIVE (#417), and canon rules the winding a static texture — `common/the-abandoned-interior.md:113` — *"it is a **static Clifford-torus / Link texture**"* | **CANON (as label only)** — the dynamical reading is FENCED OFF, not translated | KB `manuscript/ave-kb/CLAUDE.md:22` (quoted §1, rung T3); `vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:116` — *"The neutrino COUPLES to these resonances; it doesn't INHABIT them"* (resonance classes). The 2:3-Lissajous ↔ (2,3)-winding mapping is a deliberately held-back candidate: [`translation-circuit.md`](translation-circuit.md):266 — *"**Held back deliberately** (still candidates, NOT promoted)"* — this row does NOT promote it (§4 guard 4) |
| 5 | Periodic orbit vs homotopy class (a trajectory is not its $\pi_1$ class) | dynamical **carrier-ratio orbit-winding** (#417: detunes with $\omega_b{:}\omega_s$) vs static **topological charge-winding** ($\mathrm{Link}$, `def-3638f2`) | **ASSEMBLY-on-PROPOSED** — the substrate home is a ⚑ PROPOSED SHARPEN, carried verbatim: *"awaiting Grant ratification; NOT yet canonical"* (both blocks); this row inherits that status and lands nothing | [`vocabulary-register.md`](../vocabulary-register.md):140 — *"the **dynamical orbit-winding** of the coupled A1↔ω system reads the **LC oscillator carrier ratio**"* … *"**DISTINCT from the static topological charge-winding**"* — and its `:643` (both headed PROPOSED SHARPEN). Honesty-lag flagged, not papered over: the epic summary + rim-inversion leaf call the two-natured ruling Grant-ratified ([`saturation-rim-inversion.md`](../saturation-rim-inversion.md):43 — *"STANDS per the Grant-ratified **#416 two-natured ruling**"*) while both register SHARPEN blocks still read awaiting-ratification; carried here as the register states it. Cite **#417**, never the #59 fossil (§4 guard 7) |
| 6 | Phase portrait / Lissajous trajectory | the phasor/Lissajous loops in $(V_{inc}, V_{ref})$ / (E,B) / (V,I) coordinates — one plane, multiple bases; per-axis statements declare their basis (§1 basis note) | **CANON** | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-phasor-reactance.md:16` — *"trajectories here live in **phase-space $(V_{inc}, V_{ref})$ / (E,B) / (V,I) coordinates**, NOT real-space lattice-Cartesian"* — and its `:34`; agent-side: the `phase-space-coordinate-check` skill |
| 7 | — (status row) — the Smith chart / $\Gamma$-disk as an *ontology* (projective phase-space, ℂP¹, quotient readings) | **Grant-PARKED — pointer only, nothing minted.** The parked item: `_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md:4` — `status: PARKED` — with the audit's attack unanswered and *"Two months of correct inaction since."* (its `:16`) | **PARKED-POINTER** | park re-open condition at the item's `:24` — *"an engine lane actually wants the dual-sector Smith chart as a live instrument"* — un-parking is Grant's alone. Nearest corpus statement (WALK-grade, NOT restated as a row): `_orchestration/open-items/2026-08-23-theta-dressing-open-questions.md:137` — *"Smith chart is the Hopf projection of the two-phasor state space"*. Alive canonical layer (explicitly NOT parked, per the item): `vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md:78` (quoted §1, rung T4) and its `:86` — *"the biquaternion Möbius/SL(2,ℂ) identity at its existing echo ceiling"* |
| 8 | KAM / resonance-capture islands, Arnold tongues | **Hamiltonian resonance capture** (the Adler carve: substrate oscillators beat, they do not Adler-lock) | **CANON-POINTER** (home status: ⚑ **PROPOSED**, un-audited — the LOCK entry header at [`vocabulary-register.md`](../vocabulary-register.md):1317 carries `licenses nothing`) | [`vocabulary-register.md`](../vocabulary-register.md):1346 — *"phase-locked islands with KAM / Arnold-tongue structure, which exist with no dissipation at all"*; its circuit-spoke row is QUEUED-not-landed by ruling. This row points, it does not land |
| 9 | The readable-state assumption (standard mechanics assumes the state $(q,p)$ is an observable) | **phase-only epistemology**: observables are phase comparisons; the bulk self-cancels — no direct observable of the substrate state | **ASSEMBLY** (the contrast framing is new; the AVE side is canon) | [`substrate-native-terminology.md`](../substrate-native-terminology.md):19 — *"the bulk self-cancels; no direct observable"* (verbatim in-parenthetical, order as at the source); [`relative-offset-principle.md`](../relative-offset-principle.md):19 — *"In a phase-only substrate there is no spatial frame beneath the node graph"*; refined by the AC/DC carve: `common/program-arc-map.md:344` — *"**AC = shared ground** (agreed with SM/QED), **DC = contested**"* — claim `clm-acdc07`, homed at `form-deriving-value-importing.md` (receipts line `common/program-arc-map.md:136`) |

### §2.1 — Per-row payload ledger (echo-prune applied; §4-README fields for EVERY row)

Echo-prune discipline (`ave-discrimination-check` v1.2 payload-direction test): each row
states what the identification BUYS and whether it survives direction-inversion; a row that
only decorates is cut, not dressed. The consensus-bias symmetric standard was applied — a
correspondence was not cut merely for being one that standard physics would also claim.

- **Row 1 (CANON).** Payload: anchors WHICH corpus object receives every other row —
  definitional, survives any inversion. **Means-test:** none needed (definitional pointer;
  no number). **Ax3:** CLEAN (coordinate statement only). **Provenance class:** identity
  (definition pointer; the home's `ambiguous` status carried, never upgraded).
- **Row 2 (ASSEMBLY).** Payload: importing the *conjugate-pair* slot makes the T1 area
  element $dV_{inc}\wedge d\Phi_{link}$ well-posed as the $dq\wedge dp$ analog and imports
  the even-dimension pairing as a structural check. **It does NOT transfer to the T2 phasor
  plane** — T1→T2 is a coordinate change (§1), and the T1↔T2 area bridge is unbuilt (§5
  gap 9); row 3's labeling is held at WALK for exactly that reason. Inversion test: if the
  tank pair were NOT the conjugate-pair analog, row 5 and the T1 rung would lose their
  footing — load-bearing, not decorative. **Means-test:** structural only (no number; the
  pair's conjugacy is stated by A-010, the symplectic naming adds no quantity). **Ax3:**
  CLEAN (lossless-reactive; no dissipation imported). **Provenance class:** consistency.
  **Guard:** the AXIOMS state no tank Hamiltonian — Axiom 3 carries a *Lagrangian*
  ($\mathcal{L}_{node}$, INVARIANT-S2) — and the axiom-set grep discloses exactly one
  different-sense hit (§5 gap 5, repaired receipt). The corpus's OTHER Hamiltonian sites
  are enumerated at §5 gap 5; the absence claim is scoped to the axioms and the A-010 tank
  pair, NOT the corpus. Asserting Hamiltonian flow or Liouville volume-preservation on the
  tank plane would be minting (§5 gaps 2, 5).
- **Row 3 (CANON-POINTER + WALK).** DOWNGRADED from the draft's ASSEMBLY (audit repair
  2026-08-24). What is pointed at (with its home's Class-B caveat carried): the
  phasor-area-equals-Nyquist-cell identification, which is *substrate-canonical INPUT*, not
  a derivation — mis-tagging it "derived" would repeat the honest-α relabel failure. What
  is WALK: the $\oint p\,dq$ action-cell LABELING of that area. Why WALK and not ASSEMBLY:
  the standard action-area is a **T1 conjugate-plane** $(V_{inc}, \Phi_{link})$ area, while
  the Nyquist-cell area lives in the **T2 $(V_{inc}, V_{ref})$ phasor plane** — a different
  plane in different variables; no corpus map bridges the two areas (§5 gap 9); the A1⊥T2
  fence stands in the way of any naive bridge (rung T2, §1 — $V_{ref}$ a read-only
  projection, not an independent DOF); and the phasor plane is graded *dimensionless* by
  `def-69f472` (its `dimension/type` field: `phasor coordinate (dimensionless plane)`)
  while $\oint p\,dq$ carries action — the dimensional bridge is also unstated. The ladder's
  own binding rule (declare your rung) forbids landing the label across that gap. **Means-
  test:** the pointed-at identification's receipt lives at its home ($\pi R r = \pi(d/2)^2$
  at $d = 1\,\ell_{node}$, Q-EMBED-SEL-1) — as INPUT, not derivation; the WALK labeling has
  no receipt, which is why it is WALK. **Ax3:** CLEAN. **Provenance class:**
  identity-as-INPUT (Class B; echo-adjacent per the α-keystone verdict — cite
  $Q_{tank} = 1/\alpha$ as identity NOT derivation) for the pointer; WALK for the labeling.
- **Row 4 (CANON as label only).** Payload: the 2-DOF standard fact *explains why* the
  corpus's Rolfsen/torus-knot labels can be resonance labels without being orbits — it
  welds INVARIANT-N1's knot-disambiguation to the standard 2-DOF result, with the
  dynamical-orbit reading explicitly FENCED: #417 read the dynamical orbit as
  carrier-ratio-tracking, and canon holds the winding *"a **static Clifford-torus / Link texture**"* (`common/the-abandoned-interior.md:113`, quoted in the row cell).
  The weld leans on NO un-ratified content: its receipts are the ratified resonance-class
  sites — the *"phase-space winding portraits"* invariant (`manuscript/ave-kb/CLAUDE.md:22`, quoted §1 rung T3)
  and the *"torus-knot resonance classes"* statement (`vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:116`, quoted in the row cell)
  — not the PROPOSED carrier-ratio SHARPEN (which belongs to
  row 5 and carries its status there). Survives inversion (the corpus asserts the label
  reading independently). **Means-test:** none needed at label level; the #417 negative is
  the fence's receipt, restated from its home. **Ax3:** CLEAN. **Provenance class:**
  consistency (label weld only).
- **Row 5 (ASSEMBLY-on-PROPOSED).** Payload: the corpus found *experimentally* (carrier-
  ratio detuning) a distinction standard mechanics states *formally* (orbit ≠ homotopy
  class). Recording the correspondence compresses the two-natured reading into standard
  vocabulary and guards against re-conflation. Inversion test: if the #417 split were NOT
  the orbit/class distinction, the two-natured reading stands on its own receipts — the row
  adds interpretive compression + a guard, and is kept for that guard. **Status carry
  (repair 2026-08-24):** the substrate home is a ⚑ PROPOSED SHARPEN (*"awaiting Grant
  ratification; NOT yet canonical"* — carried in the row), so this row lands nothing.
  **Means-test:** the home's own CI-gated receipt — the detuning test at
  `src/tests/test_phase_space_winding.py:147` — `test_stage_b_winding_tracks_carrier_ratio` —
  asserting $|\text{ratio} - 0.667| < 0.15$; receipts belong to the home, restated not
  re-derived. **Ax3:** CLEAN. **Provenance class:** consistency, on a PROPOSED home.
- **Row 6 (CANON).** Payload: coordinate-matching discipline for test design (the
  `phase-space-coordinate-check` failure mode), now with the basis declaration (§1 basis
  note) so canon's d–q per-axis statements are placeable. **Means-test:** none needed
  (pointer). **Ax3:** CLEAN. **Provenance class:** consistency (pointer).
- **Row 7 (PARKED-POINTER) — and the recorded correction.** The draft graded this row
  ASSEMBLY ("the Smith chart is a QUOTIENT of phase space; $\Gamma$ forgets … exactly the
  symplectic (area) content", novelty-claimed at 0 corpus hits, cross-referencing a
  "smith-annulus open item"). ALL of that is repaired (2026-08-24, three-lens audit): **(a)
  the PARK** — the content is Grant-PARKED at the cp1-canonization item (named verbatim in
  the row; the "smith-annulus" name was a phantom, 0 repo hits); the novelty claim was
  false (the item's own lean and the theta-dressing WALK insight both pre-state
  projective/Hopf readings; the draft's search scope never covered `_orchestration/`); this
  register points at the park and mints nothing — un-parking is Grant's alone. **(b) the
  math**, recorded so the wrong claim cannot propagate: the map $\Gamma = V_{ref}/V_{inc}$
  on $\mathbb{C}^2 \setminus \{V_{inc} = 0\}$ lands in the **affine chart**
  $\mathbb{C} \subset \mathbb{CP}^1$ (the point $\Gamma = \infty$, i.e. $[0:1]$, is not in
  its image; the map whose image is all of $\mathbb{CP}^1$ is
  $\mathbb{C}^2 \setminus \{0\} \to \mathbb{CP}^1$); and quotienting by overall amplitude +
  common phase is U(1) **symplectic reduction**, whose image inherits the **Fubini–Study
  area form** (the Bloch sphere is a textbook phase space) — the quotient deletes ONE
  conjugate pair (the moment map $|V|^2$ and its conjugate common phase, i.e. the action
  SCALE), not area/symplectic structure wholesale. What survives as register discipline
  (definitional, minting nothing): $\Gamma$ is a ratio, so overall amplitude and common
  phase drop out of it by definition — amplitude- or action-normalized claims cannot be
  read off the $\Gamma$-disk alone and must climb back to T1/T2 declaring their rung. Any
  *ontological* reading of the disk stays with the parked item. **Means-test:** none — the
  row asserts no mapping. **Ax3:** not applicable (no substrate claim made). **Provenance
  class:** pointer (parked).
- **Row 8 (CANON-POINTER).** Payload: routes any future KAM/locking question to the Adler
  carve instead of a fresh mint. Home status PROPOSED restated, never upgraded. **Means-
  test:** none needed (pointer at a PROPOSED home that itself licenses nothing). **Ax3:**
  CLEAN — the carve is itself the Ax3 statement (lossless capture, no dissipative
  attractor). **Provenance class:** consistency (pointer).
- **Row 9 (ASSEMBLY).** Payload: states the epistemic *inversion* — in AVE the phase-space
  coordinates sit closer to the observables than the real-space coordinates do (observables
  are phase comparisons), where standard mechanics treats $q$ as primary and readable. This
  grounds §3.2's departure framing. Inversion test: if phase-space coordinates were NOT
  observation-primary, phase-only epistemology (canon) would itself be in question — the
  row restates canon in the discipline's vocabulary. **Means-test:** structural. **Ax3:**
  CLEAN. **Provenance class:** consistency. (Quote-fidelity repair 2026-08-24: the draft's
  spliced quote of `substrate-native-terminology.md:19` reversed the source's clause order;
  the row now quotes the source's own order — *"the bulk self-cancels; no direct
  observable"* — and the `clm-acdc07` pointer is split so the claim-id is not attributed to
  the arc-map line that does not carry it.)

**Rows CUT by echo-prune (recorded so the cut is auditable, not silently dropped):**

1. *"Deterministic no-crossing flow ↔ Symplectic-Euler integration"* — CUT. The corpus's "symplectic" is integrator / numerical-method vocabulary — `vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md:23` — *"iterates explicit Symplectic Euler updates"* — plus the same family's `Symplectic Kirchhoff` loops (`common/appendices-overview.md:149`) and `Symplectic Raymarching` mappings (its `:105`), and one generated-index reference to the integrator's approximate invariant: `.index/strengthen-by.jsonl:510` — `energy/symplectic invariant` (`clm-q39qct`) — conservation-property wording, still not geometric-structure usage. (The draft's "exclusively integrator vocabulary" was an overreach — repaired; gap 4's narrow claim is what is actually search-verified.) An integrator choice is not a geometric statement; the row decorates in both directions.
2. *"Even dimensionality ↔ dual C/L reactance storage"* — CUT by the symmetric standard: every discretized second-order wave system pairs its storages; the identification buys nothing and survives no discriminating use. (The conjugate-pair content it gestures at is carried properly by row 2; the SWING/SLEW keying at [`operators.md`](../operators.md):142 — *"**SLEW** (keyed on the element's rate/conjugate)"* — is cross-cited there, not duplicated.)
3. *"Liouville area-preservation ↔ Ax3 losslessness"* — CUT as premature minting. Lossless ≠ Hamiltonian: without a tank Hamiltonian on the A-010 pair (§5 gap 5) the tank plane has no stated symplectic flow for Liouville to be a theorem OF. The seductive version of this row is exactly the kind of shared-narrative echo the prune exists to catch; it is demoted to gap-ledger items 2 + 5, where it can be built honestly or die.

## §3 — The two axiom-forced departures

Where the substrate's phase space is NOT standard phase space. Both departures are where the
translation earns its keep: a spoke that only found agreement would be an echo.

### §3.1 — Bounded: the per-mode space is a DISK with a physical rim (Axiom 4)

Standard phase space has no boundary — $(q,p)$ ranges over all of $T^*Q$. The substrate's
per-mode space does: the Axiom-4 kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$ (INVARIANT-S2)
bounds the reactive amplitude, so the per-mode phasor space is a **disk with a physical
boundary** at saturation. The rim is where amplitude freezes and topology is protected —
the rim-inversion content, stated at its home. **Home status, carried (repair
2026-08-24):** the home leaf's own banner is [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):11 — *"⚠ STATUS: PROPOSED — Grant-ratification-at-merge."* — the MAPPING (`clm-riminv`) is Grant-ratified at that banner while the leaf-level ratification and the leaf NAME are pending; so the disk/rim content pointed at here is **Grant-ratified-mapping-on-a-PROPOSED-leaf**, not flat CANON, and the paragraph-level content flag is carried too: its `:47` — *"flag, not overclaim"* — *"each factor is a rim-circle (frozen amplitude, free phase)"* — the saturated phase space is toroidal because each bond-pair mode's rim-circle is one **factor** of the Clifford torus, and the winding is an integer pair because $\pi_1(\mathbb{T}^2) = \mathbb{Z}\times\mathbb{Z}$.
The *departure framing* — "standard phase space has no boundary; the substrate's boundary
is where particles live" — is ASSEMBLY (this leaf). Payload: it explains structurally why
the substrate's stable objects are RIM objects (topology-protected at frozen amplitude)
rather than interior orbits — standard mechanics has no analogous locus, so the row is a
genuine discriminating departure, not an echo. Radius-blindness guard: quoted at §1
(three-disk firewall, item 2). The A46 second flag composes the two coordinate systems:
[`saturation-rim-inversion.md`](../saturation-rim-inversion.md):84 — *"The disk/rim inversion (`clm-riminv`) is **per-mode PHASE-SPACE**"* — with the real-space envelope anatomy joined only through `S(A(r))`.

### §3.2 — Fibered over the lattice, not containing it [WALK — the bundle noun is NOT-RATIFIED]

Standard property (5): real space sits INSIDE phase space as the $q$-half. The substrate
inverts this: real space is **not** a subspace of the phasor coordinate space at all —
canon states exactly *coordinates-distinct-from-real-space* (`def-69f472`, §1), with a tank
plane attached at every lattice bond.

**[WALK — NOT-RATIFIED]** The natural mathematical noun for "a phasor plane attached to
every site" is a *fiber bundle* (base = lattice, fibers = tank planes), with the Axiom-2
TKI transduction constant $\xi_{topo} = e/\ell_{node}$ as the fiber→base dictionary. This
noun is **walk-level and un-ratified**: canon commits only to the coordinates-distinct
statement, and the corpus has an open adjudication posture on fiber-bundle language —
`common/physics-lineage-map.md:149` poses F11 verbatim: *"are the internal symmetries of the interactions irreducible abstract structure (connections on fiber bundles), or the bookkeeping of a medium's topology and sectors?"*
— and the AVE position is at its `:154` — *"CLASHES — SECTOR ⊥ GAUGE canon. Gauge structure = bookkeeping of medium topology and sector assignment"*.
Minting "fiber bundle" as a substrate noun would import the F11 abstraction the corpus
explicitly contests. The bundle noun therefore stays WALK until Grant adjudicates; the
ratifiable content underneath it is only the canon coordinates-distinct statement plus
Ax2's transduction constant (both CANON independently). The TKI-as-dictionary *framing* is
likewise walk-level.

## §4 — Anti-collision guards (standing discipline, restated not re-derived)

- **A46 three-disk firewall**: every phase-space statement declares its rung/disk — [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):17 (the *"PER-MODE PHASE-SPACE"* block, quoted in the sector declaration) and its `:84` (quoted §3.1); the `def-69f472` open-ambiguity flag — the size-reading is *forbidden*. The ladder (§1) is the formal shape of this guard, not a replacement.
- **Radius-blind $\pi_1$**: the rim-circle/Clifford-torus factorization never touches the Golden-Torus $(R,r)$ metric — [`saturation-rim-inversion.md`](../saturation-rim-inversion.md):47, quoted §1 (three-disk firewall): *"NOT a metric identification of the rim-radius with the Golden-Torus `R·r=¼` semi-axes"*.
- **Nyquist-cell Class-B caveat**: the phasor-area = Nyquist-cell identification is *"substrate-canonical INPUT (not separately Class-2 derived"* per `vol2/particle-physics/ch01-topological-matter/electron-identification.md:77`; and $Q_{tank} = 1/\alpha$ is a **definitional identity, never a derivation** (the α-keystone ruling). Any row-3 consumer inherits both caveats — plus row 3's own WALK fence on the action-cell labeling (§2.1 row 3, §5 gap 9).
- **The (2,3)-emergence hold**: the 2:3-Lissajous ↔ (2,3)-winding description is held back at [`translation-circuit.md`](translation-circuit.md):266 — *"**Held back deliberately** (still candidates, NOT promoted)"* … *"they stay here until the emergence question itself resolves"*. Row 4 points at the hold; nothing in this leaf promotes it or may be cited as promoting it.
- **No tank Hamiltonian in the AXIOMS (scoped — repair 2026-08-24)**: the axioms carry Axiom 3's *Lagrangian* ($\mathcal{L}_{node}$, INVARIANT-S2), and no Hamiltonian or canonical-conjugate statement (the axiom-set grep's single different-sense hit is disclosed at §5 gap 5). The corpus at large is NOT Hamiltonian-free — the lattice-Hamiltonian construction, the conserved $H_{couple}$ pairs, and the live `TopologicalHamiltonian1D` solver are enumerated at §5 gap 5 so no future worker "mints against" them. What IS absent: a tank Hamiltonian on the A-010 $(V_{inc}, \Phi_{link})$ pair and any symplectic-geometry formulation — Hamiltonian-flow, Liouville, or symplectic-geometry assertions on the TANK PLANE are NEW assemblies (§5 gaps 2, 4, 5), not translations.
- **Smith-chart-ontology PARK**: any projective/ℂP¹/quotient reading of the Smith chart is Grant-PARKED (preamble banner; §2 row 7; §5 gap 8). This leaf points at the park by name and mints nothing; un-parking is Grant's alone, on the item's own re-open condition.
- **Sector ownership**: mass = A1 dilatation; charge = Cosserat $(2,3)$ winding; the phase-space winding portraits are Cosserat-sector objects — *"Never cross-wire"* (`vol2/particle-physics/ch01-topological-matter/electron-identification.md:53`, quoted in the sector declaration). The per-sector DP-1 envelope (sector declaration, top) is the same guard at the amplitude level.
- **#417, never #59 (provenance refreshed — repair 2026-08-24)**: the phase-space coupling-winding test is #417. The mis-number correction is at `research/2026-06-24_engine-reroute-epic-summary.md:91` — *"the correct identifier is **PR #417**"* — and its propagation is no longer merely routed: per the summary's own `:94` — *"propagation LANDED in this same PR #793 continuation"* (commit `bd587ef5`). RESIDUAL FOSSIL, surfaced by the 2026-08-24 audit as a corpus cleanup item (NOT fixed by this leaf): [`vocabulary-register.md`](../vocabulary-register.md):1130 still ends in `#59 phase-space carrier-lock` and is absent from the landed propagation list. Do not conflate #416 (the two-natured *ruling* PR) with #415 (the eigensolve *test* PR).

## §5 — Gap ledger (three-lane corpus pull 2026-08-24 + audit-repaired receipts; negative results are search-derived, two-method — case-insensitive recursive grep from `manuscript/` + independent python regex walk. Scope honesty: `_orchestration/` was NOT swept — the two open items cited in this leaf (gap 8) were read directly, and the draft's novelty claims that ignored that scope limit were repaired. Item 8 is the corpus-registered open; item 9 is this leaf's own recorded bridge gap)

1. **Cotangent bundle** — 0 hits. The substrate side never states its phase space as
   $T^*(\text{configuration space})$; given §3.2 (fibered, not containing), it plausibly is
   NOT one — an honest structural question, unclaimed either way.
2. **Liouville theorem / phase-space volume invariance** — 0 hits. Blocked on gap 5 (no
   tank Hamiltonian / symplectic form on the A-010 plane); the echo-pruned cut row 3
   (§2.1) is the seductive shortcut, deliberately not taken.
3. **Action-angle variables** — 0 hits with a letter-boundary regex; the two substring "hits" are false positives, disclosed per the grep-completeness discipline: `vol4/falsification/ch11-experimental-bench/pcba-bench-protocols.md:31` — *"detect anomalous refraction angle via 2D baseline array"* — and `vol_4_engineering/chapters/11_experimental_falsification.tex:201` — *"the anomalous scattered refraction angle"*.
4. **Symplectic form / manifold / structure / geometry** — the exact phrases: 0 hits. Corpus "symplectic" is integrator / numerical-method vocabulary plus one generated-index conservation-property reference — enumerated with receipts at §2.1 cut-row 1 (the draft's "exclusively integrator" overreach repaired there).
5. **A tank Hamiltonian** — absent from the AXIOMS, with the receipt CORRECTED (repair 2026-08-24): the grep for hamiltonian|conjugate over `eq_axiom_*.tex` + `axiom-register.md` + `master-equation.md` + `vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md` returns exactly ONE hit, not zero — the different-sense spin-chirality usage at `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:106` — *"are the **spin-conjugate** signs"* — disclosed (the draft's "0 hits" was the grep-completeness false-negative pattern). No canonical-conjugate or Hamiltonian statement exists in the axiom set; Axiom 3 carries a Lagrangian. The corpus at large, however, DOES carry Hamiltonians (the draft's "one site" completeness claim was false — repaired): the QM-operator consistency site `vol1/dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md:54` — *"the full minimal-coupling Schrödinger Hamiltonian"*; the substrate lattice-Hamiltonian construction at `vol2/nuclear-field/ch12-millennium-prizes/yang-mills-steps1-2.md:20` — `Step 1: The Lattice Hamiltonian` — with boundedness/self-adjointness asserted at `vol2/claim-quality.md:433` — *"the lattice Hamiltonian is bounded below ($H \ge 0$)"*; the engine-requirements coupling canon `vol9/ch17-engine-requirements/index.md:19` — *"Cross-sector couplings as CONSERVED Hamiltonian pairs"*; and the live baryon solver `TopologicalHamiltonian1D` (`vol2/particle-physics/ch02-baryon-sector/thermal-softening.md:13`). What remains genuinely unbuilt: a TANK Hamiltonian on the A-010 $(V_{inc}, \Phi_{link})$ pair, and any symplectic-geometry formulation of it — a NEW assembly on canon footings, prerequisite to gaps 2 and 4.
6. **Adiabatic invariant** — phrase-level: exactly 1 site, standard plasma usage — `vol3/cosmology/ch06-solar-system/dipole-loss-cone-fraction.md:10` — *"Trapped magnetospheric particles contribute pressure via the adiabatic invariant."* Content-level (repair 2026-08-24 — the draft's "no substrate statement exists" drew a content conclusion from a phrase search, the grep-vs-read failure mode): the cleave-01 surviving mechanism class IS adiabatic-transport mathematics asserted on the substrate — `vol4/claim-quality.md:45` — *"an adiabatic Thouless-class **registry pump** over the 4₁ screw texture"* — riding an uncomputed Chern number over the $(k_z,\theta)$ registry torus. No *translation row* exists for it yet; the gap is the row, not the content.
7. **Bohr–Sommerfeld quantization** — the exact string: 0 hits. Content-level (repair 2026-08-24 — the draft's "nearest corpus object is the Nyquist cell" was wrong): the corpus DOES do phase-integral quantization — `vol1/dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md:52` — *"satisfying Bohr quantization"* (the $2\pi r = n\lambda$ impedance-matching condition reproducing $E_n$) — and the radial eigenvalue solver names its phase integral the Sommerfeld integral: `vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md:216` — *"the phase accumulated by the soliton standing wave is the Sommerfeld integral"* (tex mirror `vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:2063` — `Sommerfeld integral:`). Those are the nearest corpus objects; the Nyquist cell remains the cell-AREA object, with its Class-B caveat (row 3).
8. **Smith-chart ontology** — the corpus-registered open, correctly named (the draft's "smith-annulus" name was a phantom, 0 repo hits — repaired): `_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md:4` — `status: PARKED` — Grant's Wave-2 park, the audit's attack unanswered, re-open condition quoted at §2 row 7. The nearest corpus statement of a projective reading is WALK-grade: `_orchestration/open-items/2026-08-23-theta-dressing-open-questions.md:137` — *"Smith chart is the Hopf projection of the two-phasor state space"*. Nothing in this leaf adjudicates, re-opens, or mints here; un-parking is Grant's alone.
9. **The T1↔T2 area bridge** — unbuilt (this leaf's own recorded gap, minted as a GAP not a claim). No corpus map relates the T1 conjugate-plane area element $dV_{inc}\wedge d\Phi_{link}$ to the T2 $(V_{inc}, V_{ref})$ phasor-plane area where the Nyquist-cell receipt lives; any future bridge must also reconcile the A1⊥T2 fence — $V_{ref}$ *"not an independent DOF"* (`vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`, fully quoted §1 rung T2) — and state the dimensional bridge (dimensionless phasor plane vs action-valued $\oint p\,dq$). Until built, row 3's action-cell labeling stays WALK.
