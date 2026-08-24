# RESULT — θ route 1: the n-component Brunnian embedding obstruction in the z=3 srs carrier

> **Class:** research-tier first-order pass. **No canon edit.** Nothing minted, no solidity moved,
> no leaf demoted. Every corpus tension found is **flagged with both sides quoted verbatim**, never
> reconciled by this lane (flag-don't-fix, Grant's standing directive).
>
> **Prereg:** [`2026-08-23_theta-route1-embedding-obstruction_prereg.md`](2026-08-23_theta-route1-embedding-obstruction_prereg.md)
> — frozen before any enumeration. Bins, kill condition and adjudication criteria are taken from it
> unchanged; none was dropped or relaxed.
>
> **Driver:** [`drivers/theta_route1_srs_scale_ladder.py`](drivers/theta_route1_srs_scale_ladder.py)
> (read-only characterisation).
> **Base:** `origin/main` @ `5fc8da8d`.
> **Route source:** open-item `theta-dressing-open-questions` route 1 + docket
> `2026-08-23-theta-fork-ruling`, both on branch `kb/2026-08-23-theta-carve` (PR #998) and
> **NOT on `main`** at this base — quoted here from `origin/kb/2026-08-23-theta-carve`.

---

## §0 — SECTOR DECLARATION

**MODE** Axiom-1 carrier geometry + real-space body topology (not V-sector dynamics, not a Cosserat
eigenproblem, not an energy minimisation). **REGIME** cold / Regime I for the carrier; the baryon
core is canonically Ax4-saturated (Regime IV) — the split is a declared scope caveat, not assumed
away. **PHASE-STATE** crystalline (cold, sub-yield) for the carrier; the saturated-core region is a
named-open hole under the R45 comprehensive-map doctrine. **CHANNEL** REAL-SPACE body topology per
INVARIANT-N1; the $(2,5)$ cinquefoil is phase-space and is barred as evidence here.

---

## §1 — VERDICT

| Item | Verdict |
|---|---|
| **Deliverable 1 — formalization fork** | **UNDETERMINED BY THE CORPUS.** Both candidate readings are *canonically asserted*, in different corpus locations, and the conflict is **already flagged KEEP-BOTH-unresolved** (`proton-identification.md`:145–156, dated 2026-07-19) and **already routed to the baryon lane**. Neither the sub-cell-tube reading nor the extended-lattice-cycle reading is corpus-*supported* in the sense the route asks for; the corpus holds both and has said so. |
| **Primary bin** | **B4 — QUESTION-ILL-POSED-AS-FROZEN.** Two independent premise defects, each holding under a *different* branch of the fork, so the question is defective **whichever way the fork resolves** (§4). Per the frozen precedence B4 → B3 → B2 → B1, B4 is primary. |
| **Co-firing bin** | **B3 — FORMALIZATION-UNDETERMINED** (the deliverable-1 verdict above). Also STOP-AND-ASK. |
| **B1 (n=3-FORCED)** | **UNAVAILABLE — cannot fire from this lane's evidence.** It fails prereg §4.4 criterion 1 (the one-per-port rule is nowhere derived in the searched corpus — it is a stipulation, hence the numeral rhyme the docket bars) and prereg §4.4 criterion 2 (the prescription fixes axes/ports, not a link type, so it does not deliver Brunnian-ness at n=3). |
| **B2 (KILL)** | **LEANS FIRE, NOT BANKED.** Under every sub-reading this pass could construct, n=4 is *exactly as* (un)clean as n=3 — which is the kill condition's literal wording — but by *degeneracy* (neither is forced), not by the anticipated mechanism. Banking a kill on a question this lane has just called ill-posed would be dishonest. Held for Grant. |
| **Stuck-point** | **STOP-AND-ASK fired**, one plumber-physical question, §7. |

**Headline, stated with its grade.** *This is a first-order pass with no second reader; its
load-bearing claims are the five flags in §6 and the two premise defects in §4, all of which are
argued from quoted canon plus computed carrier geometry.* Un-audited. It mints nothing.

---

## §2 — DISPATCH-GLOSS VERIFICATION (the orchestrator's gloss, checked not trusted)

The dispatch carried an explicit DISPATCH-GLOSS to verify:

> *"baryon flux loops are SUB-CELL objects (the electron loop's circumference is one ℓ_node; the
> baryon scale is ~1/1836 of that)"* — with the rider that the *"~1/1836"* arithmetic is
> *"the orchestrator's un-audited gloss"* and must be re-derived from canon.

### §2.1 — The electron-loop scale: gloss is HALF-RIGHT and picks one side of an already-flagged fork

Canon states **two incompatible electron-loop geometries in the same leaf**, and the corpus has
**already flagged this** — so the finding is *cite it, don't mint it*:

- `electron-unknot.md`:13 — *"The unknot has circumference $l_{node}$ and tube radius
  $l_{node}/(2\pi)$"*. ⇒ $C_{loop} = 1.000\,\ell_{node}$.
- `electron-unknot.md`:59 — *"The minimum discrete diameter of the flux tube is normalised to one
  fundamental lattice pitch ($d \equiv 1 l_{node}$). The unknot … achieves a minimum ropelength of
  $2\pi$---the circumference of a circle with unit tube diameter."* ⇒ $C_{loop} = 2\pi\,\ell_{node}
  = 6.283\,\ell_{node}$.
- **Already flagged** at
  `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/common-mode-twist-ledger.md`
  (⚑ FLAG, THIRD ITEM): *"canon carries TWO INCOMPATIBLE TUBE GEOMETRIES for the electron, in ONE
  leaf … **They differ by $\pi$ on the tube diameter and by $2\pi$ on the circumference. They cannot
  both be right.**"*

**Verdict on the gloss:** *"the electron loop's circumference is one ℓ_node"* is a faithful quote of
`:13`, but it silently adopts one arm of a live, already-flagged, unresolved fork. Both arms are
carried below wherever the number is used.

**And the two arms are not interchangeable for a linking question — see FLAG-5 (§6).** Computed:
the `:13` arm gives loop radius $R = \ell_{node}/2\pi$ and tube radius $r = \ell_{node}/2\pi$, i.e.
$R/r = 1.000000$ and **open-hole radius exactly $0$** (a horn torus — the tube fills its own hole);
the `:59` arm gives $R/r = 2.000000$ and hole radius $\ell_{node}/2$. The arm the gloss picked is the
one with **no hole to thread**.

### §2.2 — The baryon scale: the "~1/1836" gloss is off by exactly 4×

Computed from canonical constants (no CODATA on the path — `PROTON_ELECTRON_RATIO` is the
AVE-derived `_X_CORE + 1.0` at `constants.py`:987):

| Quantity | Value | Provenance |
|---|---|---|
| $\ell_{node}$ | $3.8615926772\times10^{-13}$ m $= 386.159$ fm | `constants.py`:293 |
| $m_p/m_e$ (AVE-derived) | $1836.1170402$ | `constants.py`:987 |
| $\lambda_p = \ell_{node}/(m_p/m_e)$ | $0.21031$ fm | derived |
| $D_p = 4\lambda_p$ | $0.84125$ fm | `constants.py`:1147 (`D_PROTON`) |
| $D_p/\ell_{node}$ | $2.1785\times10^{-3}$ | derived |
| $\ell_{node}/D_p$ | $\mathbf{459.03}$ | derived |

The corpus states the same number verbatim: `proton-identification.md`:23 — *"the only measured
proton size is the charge radius $D_p = 0.841$ fm (property 4), which is **sub-node — $\approx
460\times$ smaller than one $\ell_{node} = 386$ fm**"*.

**Verdict on the gloss:** *"~1/1836"* is the **reduced Compton wavelength** ratio $\lambda_p/\ell_{node}$,
not the corpus's stated **body size** ratio $D_p/\ell_{node} = 1/459$. The gloss dropped the factor
$D_p = 4\lambda_p$. The qualitative point — *deeply sub-bond* — survives intact; the number is wrong
by 4× and the corrected value **1/459** is used throughout below.

### §2.3 — The gloss's formalization preference is not corpus-supported

The dispatch continued: *"so the live reading is tubes-anchored-at-a-node's-3-bond-directions, NOT
extended lattice cycles."* **This pass does not confirm that preference.** §3 shows the corpus
asserts *both* scale readings and has flagged the conflict unresolved; and the *multi-node* side is
precisely the side that would license extended lattice cycles. The gloss's preferred reading takes
Route A's **scale** while borrowing Route B's **connectivity** — a hybrid that is neither of the two
things canon actually says.

---

## §3 — DELIVERABLE 1: THE FORMALIZATION FORK — the corpus holds BOTH, and says so

### §3.1 — The two canonical assertions, quoted

**Reading A — sub-node body** (KB leaf, `proton-identification.md`:23, part of the 2026-06-08
dimensional-provenance relabel):

> *"**The proton is NOT $\sim 5$ lattice spacings extended:** the only *measured* proton size is the
> charge radius $D_p = 0.841$ fm (property 4), which is **sub-node — $\approx 460\times$ smaller
> than one $\ell_{node} = 386$ fm** … The real-space sub-node geometry (why a $0.841$ fm body) is an
> OPEN item, not a $\sim 5\,\ell_{node}$ extended object."*

**Reading B — multi-node body** (manuscript, `vol_2_subatomic/chapters/02_baryon_sector.tex`:41):

> *"A challenge in discrete models is reconciling the empirical $0.84$ fm charge radius of the proton
> with a fundamental lattice pitch of $\ell_{node} \approx 386$ fm. The AVE framework resolves this
> via solid-state scattering theory. The $0.84$ fm measurement is not the bounding box of the
> geometric loops. **The $6^3_2$ Borromean knot spans multiple fundamental nodes.** However, the
> orthogonal intersections of these three flux tubes generate localised tensor strain gradients …
> The $0.84$ fm radius corresponds to the Root-Mean-Square (RMS) effective scattering cross-section
> of the topological core gradients."*

### §3.2 — The corpus has ALREADY flagged this, KEEP-BOTH, unresolved, and routed it elsewhere

`proton-identification.md`:145–156, dated **2026-07-19**, append-only block, verbatim:

> *"**🔴 FLAG (2026-07-19, electron/proton shape-walk) — $r_p$ two-routes tension (KEEP-BOTH, routed
> to baryon lane)** … **The tension:** Route A treats $0.841$ fm as a sub-node Compton-scale
> saturation transition of an object $\approx 460\times$ smaller than one node; Route B treats it as
> an RMS-scattering artifact of a knot that "spans multiple fundamental nodes" — a **sub-node vs
> multi-node** framing mismatch underneath a shared numerical target. **Mechanisms not obviously
> compatible.** … **Disposition: KEEP-BOTH — FLAGGED, not resolved. Routed to the baryon lane for
> reconciliation.**"*

**This is the fork the frozen route asked this lane to resolve, and the corpus has already declared
it open and assigned it to another lane.** Resolving it here would be this lane overriding a standing
KEEP-BOTH disposition — outside its fence.

The same open-ness is stated twice more, independently:

- `topological-fractionalization.md`:59 — *"The denominator VALUE $3$ is FED IN … There is NO 3-loop
  stability theorem … The remaining chord-decider is whether the lattice FORCES exactly-3-loop
  Borromean stability (OPEN, parked)."*
- `neutron-identification.md`:54 — a second 🔴 FLAG carrying the same defect into the neutron sector:
  *"the bound below treats 'threading an electron unknot through the central void requires the
  Borromean rings to **expand by at least $\ell_{node}$ radially**' as a real-space radial expansion
  in $\ell_{node}$ units. Because the only measured proton size is the sub-node $D_p = 0.841$ fm
  ($\approx 460\times$ smaller than $\ell_{node} = 386$ fm), an '$\ell_{node}$ radial expansion'
  length premise is **not established** and is flagged for adjudication."*

### §3.3 — Neither named formalization is what canon says (search reported, not asserted)

The frozen route names two formalizations: *extended lattice cycles* and *tubes anchored at a node's
3 bond directions*. **Searches run** (all from the worktree root, `origin/main` @ `5fc8da8d`):

| Search | Scope | Total hits | How much was read |
|---|---|---|---|
| `grep -rn "Brunnian"` | `manuscript/ research/ src/ _orchestration/` | **0** | n/a |
| `grep -rn "Milnor"` | same | **0** | n/a |
| `grep -rn "flux tube\|flux loop"` | `manuscript/ave-kb/…/ch02-baryon-sector` | 19 | all 19 |
| `grep -rn "Borromean"` | `manuscript/ave-kb/…/ch02-baryon-sector` | 52 | all 52 |
| `grep -rln "Borromean"` | `manuscript/ave-kb` | 68 files | the 6 baryon-sector leaves + `vol_2_subatomic/chapters/02_baryon_sector.tex` read in full; the other 62 files **not** read |
| `grep -rn "flux tube"` | `manuscript/ave-kb/vol2` (whole volume) | 67 | first page only (~25) |
| `grep -rn "sub-node\|sub-cell\|spans multiple"` | `manuscript/ave-kb` | 50 | first page only (~17) |

**What the searches show — and what they do not.** *A search answers "what is the STATE of X", never
"which X's exist".* So the honest statement is: **in the material actually read** — the six
baryon-sector leaves, `electron-unknot.md`, the vol-2 baryon chapter, `axiom-register.md` Axiom 1,
`k4-port-irrep-decomposition.md`, `srs-band-structure.md` — *nothing states how a baryon flux loop
sits relative to lattice bonds, node ports, or graph cycles.* The loop↔lattice relation is absent
there: not asserted, not denied, not forked. **On that basis both named formalizations read as
constructions of the route brief rather than corpus readings** — a finding whose scope is the
material read, and which a fuller read of the 62 unread `Borromean`-bearing files could overturn.

The one thing canon *does* fix is the sector: INVARIANT-N1 — *"the electron's **real-space body** is
the $0_1$ **unknot**; the proton's is the $6^3_2$ **Borromean** linkage"* — so the loops are
real-space bodies, and the question is legitimately a real-space embedding question. It is the
*embedding rule* that is missing.

**DELIVERABLE-1 VERDICT: B3 — FORMALIZATION-UNDETERMINED.** The corpus does not determine it, has
flagged the underlying scale fork KEEP-BOTH since 2026-07-19, and routed it to the baryon lane. This
is a walk-candidate for Grant, not a lane decision.

---

## §4 — FIRST-ORDER PASS: both branches, and why the question is defective under each

Per the frozen method, the pass is run **conditionally** under each branch, since the fork is
undetermined. Enumeration was **not** performed: the fork did not resolve to a single formalization,
and per truth-per-token an enumeration under a possibly-void reading is waste. What *was* computed is
the carrier geometry the arguments turn on.

### §4.1 — Carrier characterisation (COMPUTED, both enantiomorphs, `build_srs_net(L=4)`, 512 nodes)

| Measured quantity | Value | Note |
|---|---|---|
| degrees present | $\{3\}$ | the ratified $z=3$ carrier |
| pairwise bond angle, min / max | $120.000000^\circ$ / $120.000000^\circ$ | every angle at every node |
| $\lVert\sum_p \hat d_p\rVert$, max over nodes | $0.0$ (exact) | **the three bonds at every node close on zero ⇒ they are exactly COPLANAR** |
| girth (shortest closed cycle) | $10$ | the $(10,3)$-a net |
| nearest-neighbour bond length | $1.0000000$ pitch unit $= \ell_{node}$ | `build_srs_net` pins NN bond $=\ell_{node}$ (engineering choice, self-tagged in the constructor docstring) |
| right vs left enantiomorph | identical on all of the above | expected invariance, recorded not read as signal |

Derived from those plus §2.2:

| Ratio | Value |
|---|---|
| minimum lattice-cycle perimeter | $10\,\ell_{node} = 3861.6$ fm |
| min lattice cycle / electron loop (`:13` arm) | $\mathbf{10.0}\times$ |
| min lattice cycle / electron loop (`:59` arm) | $1.59\times$ |
| min lattice cycle / proton body $D_p$ | $\mathbf{4590}\times$ |
| closed passages a $z=3$ node can host | $\lfloor 3/2 \rfloor = \mathbf{1}$ |

### §4.2 — Branch C (extended lattice cycle) — PREMISE DEFECT D1

**The arithmetic.** A closed flux loop that runs along bonds and passes *through* a node must **enter
by one port and leave by another** — it consumes **two** ports per passage. A $z=3$ node has three.
Therefore **at most one** closed loop can pass through any given node, with one port left unused;
two loops would need four ports and three loops would need six.

⇒ **The frozen premise — "$n$ mutually-Brunnian flux structures meet a node at one-per-port" — is
arithmetically impossible for $n \ge 2$ under branch C.** The maximum is $n=1$, not $3$ and not $4$.
The premise has no referent here. This is **defect D1**.

The only way to rescue one-per-port under C is to let each tube **terminate** at the node, consuming
one port — but the corpus's flux objects are **closed** loops (`electron-unknot.md`:11: *"a single
**closed** flux tube loop"*), so termination is not available.

**Setting the premise aside and asking the underlying question anyway** ("can 3 / 4 vertex-disjoint
srs cycles carry a Brunnian link?"): the carrier supplies **no cap on $n$**. Cycles in a 3-periodic
net are unbounded in length, and Brunnian links exist in $\mathbb{R}^3$ for every $n \ge 3$ (external
mathematics, tagged). Frozen criterion §4.4 requires B1 to **prove $n=4$ impossible**; nothing in the
carrier does that, so **B1 cannot fire under C**. Demonstrating B2 positively would require an
explicit $n=4$ srs-cycle construction, which this first-order pass did not produce — hence *leans
kill, not banked*.

**Scale check on C.** Under C the smallest possible body is $10\,\ell_{node} = 3861.6$ fm. That is
$4590\times$ the corpus's stated proton body ($D_p = 0.841$ fm, Reading A) and $10\times$ the
electron's stated loop (`:13` arm). So branch C is consistent **only** with Reading B
(*"spans multiple fundamental nodes"*), and is excluded outright by Reading A — which is the fork,
restated in computed numbers.

### §4.3 — Branch N (sub-cell tube at a node's bond directions) — PREMISE DEFECT D2

**D2(i) — a sub-bond object cannot resolve a super-bond structure.** Under Reading A the proton body
is $\ell_{node}/459$. The three "bond directions" are directions toward neighbours **459 body-
diameters away**. For the object to be *"anchored at a node's 3 bond directions"*, the node must
carry that 3-fold information at sub-bond scale. **Canon supplies no such mechanism in the material
searched.** Axiom 1's per-node structure is *"six intrinsic DOF per node (3 translational → E, 3
microrotational → B)"* (`axiom-register.md`:145, Axiom-1 canonical-statement) — an **orthogonal
Cartesian triad**, not the **coplanar 120° bond triad** measured in §4.1. Those are two different
3-fold objects with different geometry, and identifying them is exactly the homonym class the corpus
already polices. **Defect D2.**

**D2(ii) — the one-per-port prescription does not determine a link type.** Even granting the anchor,
"one structure per port" fixes an *assignment of structures to directions*. It does **not** fix the
loops' positions, radii, or planes — and the link type of three curves is determined by exactly those
data. Two rings assigned to two different rays can be linked or split depending on placement, and the
prescription says nothing about placement. ⇒ **the prescription cannot force Brunnian-ness at $n=3$
nor forbid it at $n=4$.** This fails prereg §4.4 criterion 2 directly.

**D2(iii) — the most favourable sub-reading, and why B1 still cannot fire.** The strongest coherent
version of branch N is: *three loops sharing the node as centre, each loop's axis along one of the
three bond directions.* This is the reading under which "$n=4$ needs a 4th direction the node lacks"
sounds forced. Three findings against it:

1. **The rule is a stipulation, not a derivation.** In the material searched, canon nowhere assigns a
   flux loop an axis along a lattice bond. Prereg §4.4 criterion 1 then applies verbatim: *"Absent
   that derivation, $n \le z = 3$ is the numeral rhyme and does not satisfy B1."* This is the docket's
   own weld hazard — *"'N=3 because z=3' counts only as a derived embedding obstruction, never as the
   numeral rhyme"* — firing exactly as written.
2. **The node is NOT short of a 4th direction.** Because the three bonds are *exactly coplanar*
   (§4.1: bond-star sum $=0$, all angles exactly $120^\circ$), every $z=3$ srs node possesses a
   distinguished **non-bond** axis: the normal to the bond plane, which is the local $C_3$ axis. A
   fourth loop with its axis along that normal is **geometrically expressible**. So the frozen
   route's *"does n=4 force over-subscription"* and the docket's *"n=4 needs a 4-junction the lattice
   lacks"* are **rule-dependent, not geometric**: they hold only if the rule is *one-loop-per-bond*,
   and fail if the rule is *one-loop-per-distinguished-direction*. The rule is undecided and
   underived, so no obstruction follows either way. **Answering the route's own sub-question
   directly: a 4th structure IS geometrically expressible; it is not blocked by a missing direction.**
3. **The corpus's $\mathbb{Z}_3$ comes from the linkage, not the lattice.** The node's coplanar
   $120^\circ$ star does supply a local $C_3$ symmetry, and it is tempting to read that as the source
   of the corpus's thirds. But `topological-fractionalization.md`:20 sources the $\mathbb{Z}_3$
   elsewhere: *"The $6_{2}^{3}$ Borromean linkage possesses three-fold permutation symmetry
   ($\mathbb{Z}_{3}$). This topological constraint restricts the allowed degenerate phase angles…"* —
   the symmetry is the **linkage's own permutation symmetry**, not the lattice's. A symmetry *match*
   between the two is a rhyme, and this is precisely the site where the numeral rhyme would enter the
   chain if it were not named. **Named.**

### §4.4 — What this does and does not settle about the frozen sub-question

The route asked: *"is a 4th structure geometrically expressible (needs a 4th direction the node
lacks) or merely energetically disfavoured?"* The first-order answer, under the only branch where the
question has a referent (N-iii):

- **Geometrically expressible: YES** — the plane normal is a real, distinguished, non-bond axis
  (computed). The parenthetical premise *"needs a 4th direction the node lacks"* is **false on the
  measured carrier geometry**.
- **Energetically disfavoured:** not evaluated, and **barred as a verdict form** by the prereg's
  CP3 — an energy answer is not an embedding obstruction and would not satisfy the route.

---

## §5 — BIN ADJUDICATION AGAINST THE FROZEN CRITERIA

| Frozen criterion (§4.4 of the prereg) | Applied |
|---|---|
| 1. one-per-port rule must be **derived**, else numeral rhyme | **NOT derived** in the material searched ⇒ B1 blocked. |
| 2. B1 additionally requires the $n=3$ assignment to **carry a Brunnian link** | The prescription fixes axes/ports, not placements ⇒ link type undetermined ⇒ B1 blocked independently. |
| 3. "energetically disfavoured" never satisfies B1 or B2 | Honoured; no energy argument used. |
| 4. every number **computed** from `ave.core.constants` / the certified constructor | Honoured; see §2.2 and §4.1. Driver banked. |

**Kill condition, quoted and adjudicated.**

> *"Kill condition: if n=4 embeds as cleanly as n=3 under the corpus-supported formalization, routes
> 2-3 lose their lattice anchor and the thirds stay honestly imported."*

Its antecedent presupposes *a* corpus-supported formalization. §3 finds there is none — the corpus
holds both scale readings KEEP-BOTH and states no loop↔lattice embedding rule at all. So the kill
**cannot be evaluated as written**. What *can* be said, and is: **under every sub-reading this pass
could construct, $n=4$ is exactly as (un)clean as $n=3$** — which is the kill's literal wording,
reached by degeneracy rather than by the anticipated obstruction-vs-no-obstruction mechanism.
**Recorded as LEANS-KILL, explicitly not banked**, because banking a kill from a question this same
document calls ill-posed would be the post-hoc-criterion move the discipline forbids in reverse.

**What survives regardless of how Grant collapses the fork:** the docket's `N=3` debt is **not
discharged** by route 1. `topological-fractionalization.md`:59's *"The denominator VALUE $3$ is FED
IN … There is NO 3-loop stability theorem"* stands untouched by this pass.

---

## §6 — FLAGS RAISED (flag-don't-fix; both sides quoted, nothing repaired)

**FLAG-1 — the port count itself is corpus-contested.** Two canonical statements, no cross-reference:

- `axiom-register.md`:147 — *"The lattice IDENTITY (D1) is **RATIFIED (Grant 2026-07-03, PR #486):
  the chiral z=3 srs net is the production carrier**"*.
- `k4-port-irrep-decomposition.md`:11 (clm-j550uh) — *"The K4 **4-port** amplitude space decomposes
  under the tetrahedral group $T_d$ as $V_{\text{4-port}} = A_1 \oplus T_2$ … **This is the canonical
  group-theoretic foundation**"*.

Any route-1-style argument that counts ports must first say **which node**. This was independently
noticed on 2026-08-12 in `research/2026-08-11_dof-vs-port-ontology_walk-record.md` (header): *"M1's
three-wire common-mode analogy (§2) was run on a **four-port node**, so the analogy's premise was
wrong independently of the state-vector question."* — i.e. the same trap has already caught one lane.
**Not resolved here.** Routed.

**FLAG-2 — the corpus's Borromean picture may not be realisable with round loops.** External
mathematics, tagged as such: Lindström & Zetterström, *"Borromean Circles Are Impossible"*
(Amer. Math. Monthly 98, 1991) — the Borromean rings admit **no realisation by three round circles**
in $\mathbb{R}^3$. Corpus context: `02_baryon_sector.tex`:31 describes the proton as *"three LC
standing waves interlinked"*, and `electron-unknot.md`:59 puts the sibling $0_1$ loop at *"a minimum
ropelength of $2\pi$---the circumference of a **circle**"*. **If** the three baryon loops are round
LC loops of the same type, the $6^3_2$ cage is geometrically impossible and at least one loop must be
non-planar. Canon does not currently say. **Surfaced for the baryon lane, not adjudicated here.**

**FLAG-3 — a canonical composite appears to need Reading B.** `neutron-identification.md`:13 makes
$n = 6^3_2 \cup 0_1$ canonical: *"a proton ($6_2^3$ Borromean linkage) with an electron ($0_1$
unknot) **topologically threaded through its central structural void**"*, and `:64` calls it
*"**Authoritative.**"* Under Reading A the electron loop (diameter $\ell_{node}/\pi = 0.318\,
\ell_{node} = 122.9$ fm on the `:13` arm) would have to thread a void inside a proton body of
$0.841$ fm — an at-least-$146\times$ mismatch (the void is smaller than the body it sits in). The
other arm makes it worse, not better: on `:59` the same loop has diameter $2\ell_{node} = 772.3$ fm,
a $918\times$ mismatch. **So FLAG-3 holds under both arms of the electron-geometry fork**, and under
the `:13` arm it is joined by FLAG-5 (that loop has no hole at all). Under Reading B the threading is
dimensionally unobstructed. **So the canonical neutron composite appears to weigh on the multi-node
side of a fork the corpus has flagged KEEP-BOTH.** Both sides quoted; **not** resolved here — this
is new evidence *for the existing baryon-lane fork*, and it belongs to that lane.

**FLAG-4 — regime mismatch between carrier and object.** The carrier facts used above (girth,
coplanarity, $z=3$) are **cold-lattice, Regime-I** properties. The baryon core is canonically
Ax4-saturated: `proton-identification.md`:24 — *"the cinquefoil core operates in the saturated regime
($S \to 0$, $G_{shear} = 0$)"*. Whether the $z=3$ port geometry survives into the saturated core
region is, under the R45 comprehensive-map doctrine, a **named-open hole** in Axiom 1's phase map.
Every geometric argument in §4 inherits this caveat. **Declared, not discharged.**

**FLAG-5 — on one arm of the already-flagged electron-geometry fork, the loop has NO HOLE, so it
cannot link or be threaded at all.** *(This lane's own observation, not a corpus quote — un-audited,
first-order, arithmetic shown so it can be checked in one line.)*

`electron-unknot.md`:13 gives the $0_1$ loop a circumference $\ell_{node}$ **and** a tube radius
$\ell_{node}/(2\pi)$. Those two data fix both radii of the torus:

$$R = \frac{C}{2\pi} = \frac{\ell_{node}}{2\pi}, \qquad r = \frac{\ell_{node}}{2\pi}
\;\Longrightarrow\; \frac{R}{r} = 1, \qquad R - r = 0 .$$

That is a **horn torus**: the tube exactly fills its own hole, and the open-hole radius is
identically zero. **A curve with no open hole cannot be linked with, cannot be threaded, and cannot
participate in a Borromean linkage.** On the other arm (`:59`, ropelength $2\pi$ with $d \equiv
\ell_{node}$) the same object has $R/r = 2$ and hole radius $\ell_{node}/2$ — perfectly threadable.
Both numbers are computed in the banked driver
(`reading13_hole_radius_over_L_NODE = 0.0`, `reading59_hole_radius_over_L_NODE = 0.5`).

**Why it matters here:** every topological question in this lane — linking, threading, Brunnian-ness
— presupposes the loops have holes. The `:13` arm does not supply one. This gives the existing
`common-mode-twist-ledger.md` ⚑ FLAG a **physical discriminator** it did not previously have (the
`:59` arm is the one under which canon's own linking claims are expressible), and it makes FLAG-3's
neutron-threading problem sharper still. **Surfaced, not resolved** — choosing an arm is the
electron-geometry fork's owner's call, not this lane's.

---

## §7 — STUCK-POINT REPORT (stop-and-ask; 2-attempt cap honoured)

**Attempt 1** — resolve the fork from the KB baryon-sector leaves. *Outcome:* found both readings
asserted and the conflict already flagged KEEP-BOTH (§3.2).
**Attempt 2** — resolve it from the manuscript source + the engine's own carrier code, looking for
any loop↔bond / loop↔port / loop↔cycle mapping. *Outcome:* none found in the material read (§3.3);
the embedding rule is absent from canon, not forked.

**Cap reached. Stopping.**

### The one plumber-physical question for Grant

> **When three flux tubes lock into the proton's Borromean cage, is a tube a wire that runs
> node-to-node along the bonds, or a sub-bond eddy that never leaves one cell?**

Why it decides everything downstream, in one line each:

- **Wire along bonds** ⇒ the smallest cage the lattice permits is the girth-10 ring,
  $10\,\ell_{node} = 3861$ fm; the proton's $0.841$ fm becomes an internal RMS feature (Reading B);
  and "one loop per port" is arithmetically dead (a closed wire eats two ports).
- **Sub-bond eddy** ⇒ the cage is $\ell_{node}/459$ across (Reading A); the three bonds are 459
  body-diameters away and invisible to it; and the only sub-bond 3-fold structure canon gives the
  node is the **orthogonal** Cosserat triad, not the **coplanar 120°** bond triad — a different "3".

Either answer collapses route 1 in one move. Neither is this lane's to pick.

**Secondary, only if the answer is "sub-bond eddy":** does a loop that small couple to the *bond*
directions at all, or only to the node's own microrotation frame? That is the question route 3
(balanced-3-phase) would actually need answered, and it is a different 3.

---

## §8 — WHAT WOULD SETTLE IT (routing, not requests)

1. **The fork itself** — already routed to the baryon lane by `proton-identification.md`:156. Route 1
   should be **held** behind that reconciliation, not run ahead of it.
2. **If Reading B (multi-node) wins:** the concrete computable question becomes *"do vertex-disjoint
   cycles of the srs net realise a 3-component Brunnian link, and if so a 4-component one?"* That is
   a real enumeration (girth-10 ring census + pairwise Gauss linking + a triple-linking / Milnor
   invariant on the pairwise-unlinked triples) and the graph tooling for it already exists
   (`ave.core.chiral_lattice.build_srs_net`). Worth doing **only after** the fork lands.
3. **If Reading A (sub-node) wins:** route 1 is void as posed, and the live question moves to *"what
   sub-bond structure does an Axiom-1 node have?"* — which is the `2026-08-11_dof-vs-port-ontology`
   thread and the $z=3$-vs-4-port FLAG-1, not a Brunnian embedding question.
4. **Either way, per prereg CP8/CP9:** a positive $n=3$-forcing result can never come from reasoning
   about a *planted* Borromean cage. It needs a hosting test — seed the generative precursor and let
   the dynamics build the cage — and **no engine in the tree currently evolves a baryon-scale
   three-loop configuration** (WALL-engine, capability gap, not a physics floor).

---

## §9 — REPRODUCTION

```bash
PYTHONPATH="$PWD/src" .venv/bin/python research/drivers/theta_route1_srs_scale_ladder.py
```

Read-only. Touches no engine state, writes no files, prints JSON. All §2.2 and §4.1 numbers come
from that single invocation.

---

## ★ CHECKER-AUDIT INTAKE (2026-08-23, post-publication; body above preserved unedited)

The checker-tier audit re-ran the driver and reproduced every computed claim by independent
second methods (all-roots BFS girth; all-1536-bond census; exact-zero coplanarity at 512/512
nodes both hands). Its findings land here as an append-only block:

1. **§4.2 D1 — the unstated premise, now stated.** The port arithmetic assumes two distinct
   structures cannot share a bond. That premise is FORCED, not assumed: link components are
   pairwise-disjoint embedded curves, so sharing a bond would be an intersection and the
   object would not be a link. The conclusion holds a fortiori. Baryon-side closed-loop
   support (cleaner than the lepton-leaf cite used in the body):
   `proton-identification.md:22` — "three mutually entangled electromagnetic flux loops in
   the substrate" — and `vol_2_subatomic/chapters/02_baryon_sector.tex:31` — "three LC
   standing waves interlinked".

2. **FLAG-5 — convention dependence (audit Finding 3; external mathematics, tagged; the
   in-body FLAG-5 must be read WITH this).** Standard ropelength is L/τ with τ = tube
   RADIUS; the round unknot's minimum 2π is attained at R = τ. Under that convention the
   `:13` numbers ARE the ropelength-2π unknot (horn torus), while the `:59` construction
   yields L/r = 4π — contradicting its own 2π headline — because its parenthetical measures
   against tube DIAMETER. Consequence: **whether ANY arm has an open hole is
   convention-dependent; under the standard convention both arms are horn tori and canon's
   threading/linking claims are geometrically inexpressible on both.** The in-body sentence
   "the `:59` arm is the one under which canon's own linking claims are expressible" is
   therefore conditional on the non-standard convention. No arm is picked here — the
   question rides the Grant-routed tube-geometry fork (`common-mode-twist-ledger.md:85`,
   fence 8).

3. **§4.3 D2(i) — quote precision + a stronger replacement argument.** The body's quote of
   `axiom-register.md:145` elides without ellipses; byte-verbatim it reads: "six intrinsic
   DOF per node (3 translational → $\varepsilon_0$/E, 3 microrotational → $\mu_0$/B; …".
   And the body's label "orthogonal Cartesian triad" is a gloss; the audit substantiates the
   point more strongly from the measured geometry: **the three bond directions sum exactly
   to zero, hence span a rank-2 plane, hence cannot serve as a basis for 3 translational
   DOF at all** — the bond star and the DOF triad are different objects by rank, not by
   orthogonality convention.

4. **§5 criterion-4 precision.** The four torus-geometry driver keys (`reading13_*`,
   `reading59_*`) were added in the result commit, post-freeze, for FLAG-5. Not a bin, no
   §4.4 criterion changed; noted so "Driver banked" is not read as fully-frozen-with-prereg.

5. **§3.3 coverage caveat.** The "6 baryon-sector leaves read in full" set is lane-reported
   and not enumerated; `ch02-baryon-sector/` holds 8 non-index leaves. Treat the read-set
   claim accordingly.

6. **§2.2/§2.3 re-attribution (timeline corrected by the orchestrator, owned).** The
   sentence §2.3 quotes was the FROZEN open-item text as it stood at dispatch time (branch
   `2270f238`); a blind-audit repair (`c42f3299`) then corrected that same frozen text
   MID-FLIGHT — SUB-CELL→SUB-NODE, ~1/1836→D_p=0.841 fm≈ℓ_node/460 with the category-error
   note, and the Q3 fork named — while this lane ran. The lane's §2.1/§2.2 re-derivations
   CONVERGED with that repair independently. So: not a dispatch paraphrase (the dispatch
   quoted the then-frozen text verbatim and labeled the number a gloss to verify), and not
   lane novelty-inflation (the corrected route text did not exist in the lane's inputs) — a
   frozen-input-changed-under-a-running-lane process datum, banked orchestrator-side.
