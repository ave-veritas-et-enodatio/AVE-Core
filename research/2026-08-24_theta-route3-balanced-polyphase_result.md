# RESULT — θ route 3: the balanced-N-phase reading of the 𝒥-dressing

**Ran:** 2026-08-24
**Lane:** implementer (analytic first-order pass; research-tier, no canon edit, nothing minted)
**Branch:** `research/2026-08-24-theta-route3` (off `origin/main`)
**Prereg (freeze STATED but UNVERIFIABLE by git ordering — see the footer surface-note; the
"frozen BEFORE the pass" claim is WITHDRAWN):**
[`2026-08-24_theta-route3-balanced-polyphase_prereg.md`](2026-08-24_theta-route3-balanced-polyphase_prereg.md)
**Driver:** [`drivers/theta_route3_balanced_polyphase.py`](drivers/theta_route3_balanced_polyphase.py)
**Output:** `drivers/theta_route3_balanced_polyphase_results.json`
**Program:** open item `theta-dressing-open-questions` route 3, on branch `kb/2026-08-23-theta-carve`
(**not on `main`**; every quote from it below is marked `[kb-branch]`).

---

## §0 — SECTOR HEADER (restated; the fences this pass ran inside)

| Axis | Declaration |
|---|---|
| **MODE** | T2 / Cosserat charge-and-spin sector, on the boundary-observable algebra (𝒬, 𝒥) at a Γ=−1 surface. **NOT** A1/mass. |
| **REGIME** | Host is Ax4-saturated (`proton-identification.md` §1 property 4); the phasor mathematics performed here is regime-free, so no cold-vs-saturated claim is made. |
| **CHANNEL** | **Phase-space, fibre / common-phase coordinate only.** |
| **FENCE (absolute)** | No step may tie θ_i to the z=3 node's three spatial bond directions. Route-1 adversarial verdict, verbatim `[kb-branch]`: *"the internal-phase-vs-spatial-star tie is route 3's unproven content, imported silently."* |
| **CLASS** | Nothing minted. No `clm-`/`def-`/`exp-`/`sup-`/`ilk-` node authored; no solidity moves; no leaf edited. |

---

## §1 — HEADLINE

### §1.0 — THE FROZEN QUESTION, VERBATIM (quoted before any verdict is delivered against it)

Source `[kb-branch]`, `_orchestration/open-items/2026-08-23-theta-dressing-open-questions.md`
lines 79-82, route 3, quoted in full and unedited:

> *"**Balanced-3-phase reading.** θ ∈ {0, ±2π/3} as the balanced polyphase angles of a
> rotating internal field **on a 3-port junction** (a balanced 3-phase set IS a rotating field
> = the J-dressing). Would collapse "why thirds" + "what the dressing is" **into the port
> count**, and would discharge the Witten formula-import."*

(Bold added here only to mark the two clauses — *"on a 3-port junction"* and *"into the port
count"* — that this lane's prereg and the earlier drafts of this result both dropped.)

### §1.0.1 — WHAT THIS PASS ACTUALLY ADJUDICATED (scope correction, read this before §1.1)

**The verdict below is delivered against a RELOCATED question, not against the frozen one.** The
frozen text puts the phases **on a 3-port junction** and collapses the thirds **into the port
count** — i.e. it is explicitly a *spatial, port-counting* question. This lane's prereg §0.1 then
installed an absolute fence forbidding any tie between θ_i and the node's spatial bond directions,
and §0's CHANNEL row relocated the phases to the **Hopf fibre / common-phase U(1)** on the strength
of an input the open item itself tags **WALK-grade and un-audited** (*"the thirds live in the
coordinate the chart deletes — the common-phase U(1)"*; cf. §7 item 3, where this lane records that
it *used* that input without auditing it).

Consequence, stated plainly:

- **The B6 "ill-posed as frozen" verdict impeaches the RELOCATED (fibre-coordinate) question.**
  D1 and D2 below are both defects of the fibre reading: D1 is the share-vs-angle type error as it
  appears once θ is read on the fibre, and D2's "no rotating field to decompose" is true *because
  the fence removed the spatially displaced windings that the frozen text supplied via its 3-port
  junction*.
- **The frozen (spatial, 3-port) question's status is therefore: UNTESTED BY THIS PASS.** It was
  not answered, and it was not shown ill-posed. It was fenced out before the pass began.
- The fence itself is not challenged here — route 1's adversarial verdict installed it for cause
  (*"the internal-phase-vs-spatial-star tie is route 3's unproven content, imported silently"*).
  The honest reading is that route 1's corpse and route 3's frozen text are **in tension**: route 3
  as frozen *requires* the spatial tie that route 1 forbids importing. Resolving that tension is an
  adjudication for Grant / the auditor lane, **not** something this lane discharged by relocating
  the question and then declaring the relocated version ill-posed.

### §1.1 — VERDICT ON THE RELOCATED (FIBRE-COORDINATE) QUESTION

**PRIMARY BIN: B6 — QUESTION-ILL-POSED-AS-FROZEN.** The route-3 question *as this lane relocated
it* asks whether the dressing **θ_i/2π = 𝒥_i/𝒥_total** can be realized as *a balanced-N-phase
decomposition of ONE rotating field structure on the fibre coordinate*. Two of its own premises are
mutually exclusive, and both defects are established against canon's own frozen text plus checked
arithmetic:

- **D1 — the share is degenerate exactly where the balanced set needs distinctness.** `θ_i/2π =
  𝒥_i/𝒥_total` is a **magnitude share**, and canon's ratified result says that share is **1/N for
  every constituent by symmetry** (T2). Identical constituents therefore carry *identical* θ_i.
  A balanced polyphase set requires *distinct* θ_i. The premise and the target cannot both hold.
- **D2 — there is no "rotating field" on the fibre to decompose.** Driver check C: the resultant of
  a balanced N-phase set summed on a single (fibre) coordinate is **identically zero at every N**
  (max |resultant| ≤ 1.9 × 10⁻¹⁵ for N = 2…6) — not rotating, not even pulsating. A polyphase set
  becomes a rotating field only when the N phases are fed into **N spatially displaced** windings,
  and that spatial half is exactly what the §0 fence forbids importing.

**Per the frozen instruction, the question is NOT repaired here.** A repaired question is a new
question and needs its own freeze.

**Co-verdict, reported prominently so the process is not hiding behind "ill-posed" —
SECONDARY BIN B5 (KILL: contradicts a canon receipt), which is what the pass returns if D1/D2 are
set aside and the question is read charitably:** with θ treated as a **genuine phase** (compact,
mod 2π — which is what "polyphase" *means*), canon's five-element θ list collapses to **three**
classes, and the observed up (+2/3) and down (−1/3) charges are then **both** at the **same** class
θ/2π = 2/3, differing only in the integer n ∈ {0, −1}. The phases are **degenerate, not balanced**.
Canon's examplebox derivation (T3) obtains ±1/3 and ±2/3 at n_twist = 0 only by reading θ
**non-compactly**, i.e. by silently using the (n, θ) gauge freedom.

**And the answer to the chord question the route was aimed at — do the thirds stop being imported?
NO, on the fibre.** Every criterion that can actually be *stated* on the fibre is N-generic (§4);
the one criterion that *is* N-selective (§5) rests on three premises none of which the corpus
supplies. **This is not an answer for the frozen 3-port reading, which was fenced out (§1.0.1).**

| Route-3 goal (from the open item `[kb-branch]`) | Verdict (on the RELOCATED fibre question only — §1.0.1) |
|---|---|
| verbatim, no elision: *collapse "why thirds" + "what the dressing is" into the port count* | **NOT ACHIEVED — but note the goal's own mechanism was fenced out.** The thirds stay imported on the fibre. The *"into the port count"* half was never tested at all: the port count is a spatial-star quantity that §0.1 forbids this lane from touching. Earlier drafts of this row silently dropped that clause. |
| *"would discharge the Witten formula-import"* | **NOT DISCHARGED — and the import diagnosis SHARPENS** (§6): compactifying θ pushes the corpus's usage *back toward* Witten's actual structure (one common θ, integer n varying per object), which is more import, not less. |
| **This lane's own pairwise-cos(Δθ)=0 specialization** of Grant's banked mode-orthogonality reading (input 3), applied to N identical constituents differing only by fibre phase | **ANTI-SELECTS 3** (§3.3; §4's C-ORTH row): pairwise time-average orthogonality of co-located identical modes differing only by fibre phase is achievable at **N = 2 only**. **SCOPE — this is NOT a verdict on Grant's banked reading.** Grant's reading is about a *threaded electron sitting in a cage's null*, i.e. two distinct objects in a host geometry; the specialization to *N identical constituents differing only by fibre phase*, and the reduction of "orthogonality" to pairwise cos(Δθ)=0, are **this lane's constructions**, not his. The banked reading is untouched by this row. |

---

## §2 — NULL-LIVENESS GATE, AND THE INSTRUMENT DEFECT IT CAUGHT (report first, per Rule 10)

The prereg (§6) required the driver to reproduce a *known* rigidity at N=3 and a *known* freedom at
N=4 before any "no selection" answer would be trusted. **On the first run the gate FAILED and the
lane halted** — correctly.

- **Defect found:** the second (independent) dimension measurement used a **global SVD** of a
  solution cloud. A global SVD measures the dimension of the cloud's *affine hull*, not of the
  manifold; a curved 2-manifold in ℝ⁵ has an affine hull of dimension up to 5. It reported
  moduli-dimension **4** at N=5 where the Jacobian count says **2**.
- **Second defect in the same function:** it quotiented relabelling by *sorting*, a non-smooth
  operation that mixes branches.
- **Repair (visible in the driver, not silent):** local PCA on constraint-projected displacements
  with the global-rotation direction projected out, plus an **absolute** singular-value floor
  alongside the relative one — the relative cut alone mis-counts round-off as signal when the
  moduli space is a *point* (every singular value is then ~10⁻¹⁴ and one is trivially "largest").
- **Third defect, caught by inspection rather than by the gate (§7.1):** the common-θ charge
  function held the constituent count at **3** while sweeping the dressing denominator N, which
  manufactured a false "only N=3 gives charge +1". That is precisely the fed-in-N failure this
  program polices, appearing inside this lane's own instrument.

**After repair the gate PASSES** (`NULL_LIVENESS_GATE.PASS = true`, all five sub-checks true), and
the two independent dimension measurements agree at every N = 2…8.

---

## §3 — WHAT WAS COMPUTED (all numbers from the driver; no CODATA, no `ave.core.constants`)

### §3.1 — C-SUM: the equal-modulus zero-sum configuration variety

For N unit phasors with Σ e^{iθ_i} = 0, measured two independent ways:

| N | Jacobian rank at the balanced point | dim(solution surface) | **dim mod global rotation** | local-PCA dim (independent) | balanced set collinear? |
|---|---|---|---|---|---|
| 2 | **1** (rank-DEFICIENT) | 1 | **0** | 0 | **YES** |
| 3 | 2 | 1 | **0** | 0 | no |
| 4 | 2 | 2 | **1** | 1 | no |
| 5 | 2 | 3 | **2** | 2 | no |
| 6 | 2 | 4 | **3** | 3 | no |
| 7 | 2 | 5 | **4** | 4 | no |
| 8 | 2 | 6 | **5** | 5 | no |

**dim = N − 3 for N ≥ 3.** N=3 is the critical case where the constraint count exactly consumes
the freedom. N=2 is *also* isolated but for a **degenerate** reason — the Jacobian drops to rank 1
— and its solution is **collinear** (antipodal). Positive control: the known one-parameter N=4
family {φ+δ, φ−δ, φ+π+δ, φ+π−δ} was constructed explicitly, max residual **4.6 × 10⁻¹⁶** over the
sweep, and the balanced 4-set is recovered as its δ = π/4 member.

### §3.2 — The rotating-field null (driver check C)

Balanced-N phasors summed on a single coordinate: |resultant| ≤ **1.9 × 10⁻¹⁵ for every N = 2…6**,
i.e. **identically zero**. Zero-sum *is* the statement that the net vanishes at every instant.
The "balanced set = rotating field" image requires N spatially displaced windings — fenced out.

### §3.3 — C-ORTH: pairwise mode orthogonality (Grant's input 3)

Time-averaged cross-energy between two co-located identical modes differing only by fibre phase
∝ cos(θ_i − θ_j). Requiring this to vanish for **all** pairs:

- **Maximum N with a solution: 2** (example: {0, π/2} — quadrature). Exhaustive search.
- **Analytic reason** (checked against the search): cos(Δ) = 0 ⇔ Δ ≡ π/2 (mod π). If
  θ₁−θ₂ ≡ π/2 and θ₂−θ₃ ≡ π/2 (mod π), then θ₁−θ₃ ≡ π ≡ 0 (mod π) ⇒ cos = ±1, not 0. No triple
  exists.
- **The balanced 3-set is the opposite of orthogonal:** every pairwise cos(2π/3) = **−1/2**, i.e.
  maximally *destructive*, not null.

**Finding: net-null and pairwise-null are different criteria, and only net-null is compatible with
thirds.** *This lane's pairwise-cos(Δθ)=0 specialization* of the mode-orthogonality reading and the
balanced-polyphase reading cannot be the same mechanism; applied to identical fibre-phase-offset
constituents, orthogonality caps N at 2. **Scope, per the §1.1 table:** the specialization is this
lane's construction; Grant's banked reading concerns a threaded electron in a cage's null, not N
identical constituents differing only by fibre phase, and is not adjudicated here.

### §3.4 — C-CLOSURE: Σθ_i ≡ 0 (mod 2π)

| N (balanced set) | Σθ/2π | closes? |
|---|---|---|
| 2 | 0.5 | no |
| 3 | **1.0** | **yes** |
| 4 | 1.5 | no |
| 5 | **2.0** | **yes** |
| 6 | 2.5 | no |
| 7 | **3.0** | **yes** |
| 8 | 3.5 | no |

Closure selects **odd N**, not N=3 — and it is **doubly weak**:

1. **It does not force the balanced set even at fixed N.** The driver constructs five non-balanced
   3-phase sets with Σθ/2π = 1.0 exactly (e.g. θ/2π = {0.280093, 0.107995, 0.611913}).
2. **It is representative-dependent.** Σθ_i is not invariant under θ_i → θ_i + 2π, so it is not a
   well-defined function of the phases; only q_eff is physical. Canon already reached the same
   place from the other side — T4 `[kb-branch]`, verbatim: *"the net Σθ ≡ 0 (mod 2π) across the
   nucleon's constituents is arithmetically EQUIVALENT to integer total charge — it is a
   restatement of charge integrality, not an independent EDM-cancellation argument."*

### §3.5 — The compact-θ charge enumeration (exact rationals, no floating point)

With θ a genuine phase, canon's five listed values **{0, ±2π/3, ±4π/3}** have **3** distinct
classes mod 2π: θ/2π ∈ {0, 1/3, 2/3}. Enumerating q_eff = n + θ/2π over integer n:

| Target | Unique (n, θ/2π) solution |
|---|---|
| up, +2/3 | **(n = 0, θ/2π = 2/3)** |
| down, −1/3 | **(n = −1, θ/2π = 2/3)** |
| anti-up, −2/3 | (n = −1, θ/2π = 1/3) |
| anti-down, +1/3 | (n = 0, θ/2π = 1/3) |

**Up and down share one θ class** (`up_and_down_share_theta_class = true`). The quark-charge
*difference* is carried entirely by the **integer n**, not by the phase. Under a compact θ the
proton's three constituents are **phase-degenerate**, which is the exact negation of a balanced
polyphase set.

This is a hard collision with T3's own derivation, which fixes **n_twist = 0** and then obtains
−1/3 by writing θ = −2π/3 — a value that, compactified, *is* +4π/3 and yields **+2/3**, not −1/3.
Canon's negative quark charges exist only in the non-compact reading.

### §3.6 — The common-θ (equal-share) reading is N-generic

For an N-constituent composite where every constituent carries the **same** dressing −1/N and an
integer part n_i (k of them equal to 1): total = k − 1 **for every N** (verified N = 2…6 in exact
rationals; total dressing = N·(−1/N) = −1 identically). Proton-like k=2 → +1 and neutron-like
k=1 → 0 at **every** N. **N is not selected by charge integrality.** This reproduces T2's finding
by an independent route: *"The denominator equals N for every N; the substrate EXCLUDES none."*

---

## §4 — CRITERION-BY-CRITERION VERDICT AGAINST THE FROZEN AXES

Frozen axes (prereg §4): (1) does it force the balanced set at fixed N? (2) does it select N?

| Criterion | (1) forces balanced set at fixed N? | (2) selects N? | Bin |
|---|---|---|---|
| **C-CLOSURE** (Σθ ≡ 0) | **NO** — explicit non-balanced counter-examples (§3.4) | NO (selects odd N; representative-dependent; canon already calls it a restatement of charge integrality) | **B2 — N-GENERIC** |
| **C-ORTH** (pairwise null) | N/A — no 3-phase solution exists | **ANTI-SELECTS**: caps N at 2 | **B5-shaped** for the thirds: the criterion excludes them |
| **C-SUM** (net-null, equal moduli) | **YES at N=3** (isolated solution); **NO for N ≥ 4** (moduli of dim N−3) | **YES, mathematically** — N=3 is the unique N that is both *isolated* and *non-collinear* (§5) | **B3 — N-SELECTIVE BUT PREMISE-UNDERIVED** |
| Common-θ / equal-share reading (canon's own T2) | N/A (all θ equal) | **NO** — total = k−1 at every N (§3.6) | **B2 — N-GENERIC** |

---

## §5 — THE ONE N-SELECTIVE RESULT, AND WHY IT IS NOT A CHORD (B3, secondary — NOT banked)

**The mathematics (verified, §3.1 + §3.2).** For N identical constituents carrying equal-modulus
phasors on one coordinate, subject to net-null:

> **N = 3 is the unique N ≥ 2 whose balanced solution is simultaneously (a) ISOLATED — a single
> point modulo global rotation, no flat direction — and (b) NON-COLLINEAR.** N = 2 is isolated but
> collinear *and* its isolation is degenerate (Jacobian rank 1, not 2). Every N ≥ 4 is
> non-collinear but carries an (N−3)-dimensional family of zero-sum configurations of which the
> balanced set is only one point.

This is the substrate-independent sense in which three-phase is the RIGID balanced set — the
zero-sum condition alone pins the configuration at N=3, whereas balanced N≥4 sets are equally
self-balancing (§3.2) but are one point of an (N−3)-dimensional zero-sum family. It is
**genuinely not N-imported**: it is a statement proved for all N that happens to be satisfied
uniquely at 3.

**Why it is nevertheless not a chord — three premises, none supplied by the corpus, plus a
contradiction. Each is stated so it can be attacked or discharged:**

1. **NET-NULL ON THE FIBRE IS UNDERIVED.** Nothing in the corpus requires the composite's
   common-phase coordinate to carry zero net excitation. The Γ-chart *deletes* the common phase;
   deletion is not vanishing. The route-1 adversarial pass killed the **spatial** analogue of this
   criterion FATALLY on a cross-sector argument `[kb-branch]`, and no fibre version has ever been
   stated. **Tagged IMPORTED-PREMISE in the prereg before the pass ran, and it stays imported.**
2. **RIGIDITY IS NOT STABILITY** (prereg §5.4 criterion 4, barred in advance). "Isolated solution
   ⇒ phase-lock ⇒ bound; flat direction ⇒ drift ⇒ unbound" is an *energetic* inference. The
   dimension of a constraint variety says nothing about restoring forces without an energy
   functional — and the corpus has **none**: *"no body-angular-momentum coupling in any engine"*
   (`research/2026-06-23_witten-angular-momentum-charge_result.md`:253-254 — the phrase spans the
   line wrap, so a single-line grep for it false-negatives; verified by grepping each half).
   Making this step would be exactly the barred move.
3. **THE PHASE-VS-SHARE TYPE ERROR** (this is D1 again, and it is fatal on its own). C-SUM needs
   θ_i to be **angles**; T1 defines θ/2π to be a **magnitude ratio** 𝒥_i/𝒥_total ∈ [0,1]. These are
   different kinds of object sharing one glyph. If θ is a share, C-SUM cannot be written. If θ is
   an angle, T1's identification is false as stated.
4. **CANON CARRIES STABLE BALANCED N-PHASE STRUCTURES AT N ≠ 3 — at low weight AND in the wrong
   channel, reported as found.** `vol6/claim-quality.md`:625 catalogues *"3-Phase Delta-Wye (C),
   […] Tetraphase Network (O), […] 5-Phase Ring Oscillator (Ne), Octahedral 6-Phase (Mg), 7-Phase
   Pentagonal Bipyramid (Si)"* (**stitched quote — the bracketed ellipses elide intervening
   archetype entries from the same list; not continuous text**), and the O-16 leaf calls its
   four-phase network *"immensely stable"* / *"perfectly symmetrical"* / *"profound symmetry
   ($Q \gg 1$)"* (`vol6/period-2/oxygen/ee-equivalent.md`:10, :12, :14 — **three separate
   paragraphs, quoted as three fragments rather than one stitched sentence**).
   **⚠ CHANNEL MISMATCH (A46), and it is the primary caveat on this gap, ahead of the solidity
   one:** every vol6 archetype above is a **REAL-SPACE / spatial** network — the O-16 leaf's own
   text derives its four-phase structure from *"four identical … Alpha Cores equally spaced in 3D
   geometry"* coupled by *"the sheer spatial distance $R_{tet}$"* — whereas the claim this gap is
   offered against is a **fibre / common-phase coordinate** claim (§0 CHANNEL). Spatial N-phase
   networks are not counter-evidence to a fibre-coordinate selection statement; they are
   measurements in a different coordinate system. Under this lane's own §0.1 fence they are also
   exactly the spatial-star reading that may be *cited as context but never as support* — and the
   symmetric application of that fence is that they cannot be load-bearing as *refutation* either.
   **Weight caveat, additionally:** these sit on `clm-sd04x4`, **solidity 0.30, build-status "do
   not build on, rework needed"**, and the register itself calls the archetype names *"explicitly
   analogies with no claimed falsifiable EE observables"*. So this is a direction-of-travel
   receipt in an adjacent channel, not a kill on its own — but it is the corpus's own answer to
   "does the substrate host balanced N-phase structures at N ≠ 3?" *in real space*, and that
   answer is yes.

**Net on B3:** the selection is real mathematics attached to no substrate premise. Recorded as a
named, attackable object; **not banked**, and explicitly **not** a replacement hypothesis for the
route-3 slot (Rule 12 / substitution-not-retraction).

---

## §6 — THE IMPORT DIAGNOSIS SHARPENS RATHER THAN DISCHARGES (finding, flag-don't-fix)

Route 3's stated payoff was *"would discharge the Witten formula-import"*. The pass finds the
opposite, and the mechanism is worth surfacing because it is a *consistency* observation, not a
demotion:

In Witten's actual construction, **θ is a single global property of the vacuum**, identical for
every dyon; what varies between objects is the integer n. §3.5 shows that **compactifying θ — i.e.
insisting it be a genuine phase, which is precisely what the polyphase reading requires — forces
canon's usage back into exactly that structure**: one common θ class, integer n distinguishing the
constituents. Route 3, pursued honestly, therefore makes the corpus's θ *more* Witten-like, not
less. The formula-import disclosure (`clm-67jn9o`) stands, and the *"standing strengthen-by asks
for an engine-derived θ"* is untouched.

**Two live corpus statements are surfaced here with both sides quoted, not resolved by this lane:**

- **(F1) Canon asserts per-constituent distinct θ.** `proton-identification.md`:47 (§2 observables
  table, "Fractional quark charges" row), verbatim:
  *"The three quark 'flavors' are the three θ-vacuum sectors of the same Borromean linkage."*
  — versus the compact-θ arithmetic (§3.5), under which up and down occupy the **same** class.
  These cannot both be right unless θ is non-compact, and if θ is non-compact then "polyphase"
  does not apply to it. **Adjudication is Grant's / the auditor lane's, not this lane's.**
- **(F2) The n_twist = 0 convention.** T3 fixes n_twist = 0 and derives four charges from three
  phase classes. Three classes at fixed n give three charges, not four. The fourth is obtained by
  an implicit n = −1. **Flagged, not repaired.**

---

## §7 — HONEST SCOPE, AND WHAT THIS PASS DOES NOT SHOW

1. **Analytic and configuration-counting only.** No lattice field, no engine evolution, no energy.
   CP9 of the substrate-native walk returned **WALL-engine**: no engine in the tree evolves a
   θ-bearing multi-constituent baryon, so the *dynamical* form of route 3 (does the substrate
   phase-lock N constituents?) is currently untestable. That is a capability finding, not a
   physics floor.
2. **Planted end-state (CP8).** This lane reasoned about a planted N-constituent composite. A
   positive could never have been banked from it, by the prereg's own construction.
3. **The fibre is asserted, not derived, as the phase's home.** The Hopf-fibre input (open item,
   *"the thirds live in the coordinate the chart deletes — the common-phase U(1)"*) is
   **WALK-grade and un-audited** by its own tag `[kb-branch]`. This pass *used* it as the channel
   declaration and did not audit it. If the fibre reading falls, §3–§5 are unaffected as
   mathematics but lose their claimed physical home.
4. **Wind(∂Ω) was NOT defined here** (prereg T5 discipline). §8 states what a definition leaf would
   need; this lane mints none of it.
5. **Symmetric-standard check (prereg §5.2, mandatory).** The Standard Model does not derive
   N_c = 3 either — it is measured (R-ratio, π⁰→γγ) — and SM quark hypercharges are assigned by
   hand. The B6/B5 verdict is an **object-level verdict on this specific mechanism**, not a
   comedown relative to SM. Both frameworks import the 3; AVE's import is now more precisely
   located.

### §7.1 — Flag on this lane's own instrument (flag-don't-fix, applied to myself)

The common-θ function's first version fixed the constituent count at 3 while sweeping the dressing
denominator N, and produced an apparent *"only N=3 gives total charge +1"*. **That was a false
positive of exactly the class this program exists to catch**, generated inside the checking
instrument. It is recorded in the driver docstring and here rather than quietly corrected, because
a repaired instrument is only trustworthy if the repair is visible. The corrected construction
(§3.6) is N-generic.

---

## §8 — WHAT A `Wind(∂Ω)` DEFINITION LEAF WOULD NEED (owed prerequisite; nothing minted)

The double-booking gap is prerequisite-adjacent to every route-3-shaped result. Sole KB definitional
site is the `boundary-observables-m-q-j.md`:21 table cell; the engine carries only a proxy
(`src/ave/core/boundary_invariants.py`:221, *"FIRST-PASS proxy implementation"*, with the rigorous
version *"deferred"*). A definition leaf would have to supply, at minimum:

1. **An integrand and a field.** Which field's winding — the Cosserat microrotation ω (what the
   engine's deferred-rigorous note names), or the (V_inc, V_ref) phase-space pair? A46 discipline
   makes this decisive: a winding of the wrong field is a different observable.
2. **A surface and an orientation** for ∂Ω, so that "2D surface integral" has a referent.
3. **A partition rule for the double-booking**: 𝒥 currently carries BOTH the SU(2) half-integer
   spin AND the 1/N dressing share, unpartitioned. Are these one object or two? If one, the
   partition must be stated; if two, the glyph must split.
4. **A type: magnitude or angle.** This is route 3's specific contribution to the owed list.
   `θ/2π = 𝒥_i/𝒥_total` only type-checks if 𝒥 is a **magnitude**; the polyphase reading needs an
   **angle**. The definition leaf must say which, because the corpus currently uses both.
5. **A compactness statement**: is the associated θ valued in ℝ or in ℝ/2πℤ? §3.5 shows canon's
   quark-charge arithmetic depends on the answer.

---

## §9 — ROUTED, NOT BANKED (Rule 12: the slot is not refilled)

Two candidates surfaced by this pass. **Neither is a replacement hypothesis for route 3; each would
need its own number and its own freeze.**

- **(R1) The polyphase structure, if it is anywhere, is in the COLOUR sector — not the charge
  dressing.** Canon already reads colour as a phase label:
  `vol2/particle-physics/ch05-electroweak-mechanics/forward-to-ch6.md`:52, verbatim: *"The 'colour'
  quantum number is the permutation label of which flux loop carries the dominant phase winding at
  any given lattice site"*, with *"the ℤ₃ center of SU(3) enforces the strict topological
  constraint that only color-singlet (1) composite states … can propagate"* (`:50`). ~~Colour-singlet **is** a zero-sum condition on three phase labels — i.e. C-SUM with a
  corpus-carried premise, which is exactly the premise route 3 lacked (§5 gap 1).~~
🔴 **RETRACTED 2026-08-24 (checker-audit Finding 5; strike preserved per Rule 12).** The
cited receipts do not carry a zero-sum condition: `forward-to-ch6.md:50` frames
colour-singlet as a ℤ₃-centre/linkage condition ("where all three loops are linked") and
`:52` as a **permutation label** — a discrete selector with no additive structure. A
two-direction proximity search finds ZERO corpus sites framing colour-singlet as a sum
condition. Whether the ℤ₃-centre condition on a permutation label is equivalent to a
zero-sum condition on phasor angles is **itself an owed derivation** — R1 does NOT supply
§5 gap 1; it relocates it. (Note the irony, recorded deliberately: this was the same
label-vs-angle type error this doc's own D1 identified as fatal.) R1's honest status: a
follow-on freeze CANDIDATE conditional on that derivation, not a corpus-premised route. The §3.1 rigidity result would then be a
  statement about **confinement**, not about quark charge. *Caveat that must travel with it:* the
  same register records the SU(3) identification as *"asserted as the structural identification …
  not a uniqueness theorem"* (`vol2/claim-quality.md`:815).
- **(R2) The dynamical question the engine cannot yet answer:** is there a restoring torque between
  constituent phases (phase-lock) or not? This is the §10 plumber question, and it is the gate on
  whether the rigidity-vs-stability step (§5 gap 2) can ever be taken. Requires a θ-bearing
  primitive that does not exist (`gamma_c`-style capability gap; cf. route 4's retag).

---

## §10 — STUCK-POINT / QUESTION SURFACED TO GRANT (2-attempt cap; lane proceeded under a stated premise)

Corpus-searched first (`polyphase|three-phase|balanced` across `manuscript/`, `research/`, `src/`):
the corpus carries N-phase *archetype names* at N = 3,4,5,6,7 but **no statement of what physically
holds N constituent phases apart**. Genuinely open, so surfaced:

> **On the real bench, what holds the three loops at 120° from each other — is there a restoring
> torque between them (a phase-lock, like paralleled alternators pulling into step), or is 120°
> just where they sit because nothing is pushing them anywhere?**

- If **restoring torque**: the balanced set is an energy minimum, the question moves into a
  dynamics this lane is barred from (prereg CP1/CP3) and the engine cannot run (§7 item 1, the
  WALL-engine finding). §5's gap 2 becomes the whole problem.
- If **nothing pushing**: the balanced set can only be selected by a constraint — which is what
  §3–§4 tested, and the answer is the one above.

**The lane proceeded on the constraint reading and states the dependency explicitly.** The B6/B5
verdict does not depend on the answer (D1, D2 and §3.5 are arithmetic, not dynamics), but §5's
status as B3-rather-than-dead does.

---

## Reproduce

```
PYTHONPATH=<worktree>/src python research/drivers/theta_route3_balanced_polyphase.py
```

Value-echo immunity: the driver asserts at entry that `ave.core.constants` and `scipy.constants`
are not imported. Inputs are the integer N and, in §3.5, the target rationals entered as
enumeration targets. All charge arithmetic is exact (`fractions.Fraction`); no floating point, no
fit, no CODATA.

---

> 🔴 **Dated surface-note 2026-08-24 (checker-audit Finding 6a): the prereg freeze is
> UNCLAIMABLE by git ordering, per the ratified P9 rule** (`_orchestration/
> 2026-07-09_breakthrough-patterns-methods-note.md` §P9: "a freeze you cannot point to in
> the git log is a promise, not a freeze"; counterexample X36/#613, review finding
> MINOR-12). Prereg, driver, and result landed as ONE commit (`bdf51221`), so the prereg
> header's "Frozen … before the driver ran" and §1's five not-known-at-freeze claims cannot
> be shown from git. The audit's independent re-derivation confirms every number bit-exactly
> and corroborates the self-reported instrument repairs, so no result is impeached — but the
> freeze CLAIM is withdrawn to "stated, unverifiable". **This withdrawal is now also carried
> on the prereg itself** (header surface-note), and the header of THIS doc is corrected — line 6
> previously still read *"Prereg (frozen BEFORE the pass)"*, contradicting this footer.
> **Contrast route 1, which had genuine ordering:** prereg `b50c0d86` (2026-08-23 20:56)
> precedes result `4f963e29` (2026-08-23 21:07), so route 1's freeze IS checkable from git —
> the P9 note applies to it only partially (#999, merged: its prereg commit carried driver
> code). Orchestrator-side cause owned in the dispatch record: the lane briefs said "prereg
> discipline" without quoting P9's push-first rule; the rule travels verbatim in all future
> lane briefs.
>
> **Compounding (checker-audit Finding 6b), recorded because an unverifiable freeze cannot rule
> it out:** bin **B3** was **added by this lane beyond the dispatch's three named bins** (prereg
> §5, B3 cell, self-disclosed under the KEEP-BOTH discriminator pattern) — **and B3 is the bin
> this lane's own positive finding landed in** (§5 above, the N=3 rigidity result). With the
> freeze unverifiable, the git record cannot establish that the bin predates the finding. No
> post-hoc addition is alleged; the point is that it cannot be excluded, which is why §5's
> **not banked** marking is load-bearing rather than decorative.

> ★ **Audit strengtheners (same pass):** (i) the stronger canon receipt for N-genericity is
> `proton-identification.md:47`'s own Grant-ratified line — "the denominator $3$ is the
> FED-IN observed loop count ($N$-generic; no 3-loop stability theorem…) NOT forced" —
> which this doc under-cited in favor of the research doc. (ii) §3.3's "Exhaustive search"
> reads as continuum-exhaustive; the code is grid-exhaustive (720 points at N=3, π/2
> multiples at N≥4), justified BY the analytic argument, which is primary. (iii) §3.2's
> resultant ≡ 0 numeric is a tautological consequence of the zero-sum constraint (as the
> driver docstring itself says); D2's substantive content is the fence argument, and the
> numeric is not independent evidence for B6.
