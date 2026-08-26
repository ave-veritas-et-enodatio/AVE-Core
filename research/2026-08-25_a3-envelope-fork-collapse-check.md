> **⚠ LANE RECEIPT — pre-ruling, preserved for the record.** This is the A3
> collapse-check lane's output as repaired after adversarial verification.
> Its verdict (the envelope fork and the storage/response contour fork are
> DISTINCT) is **demoted to "definitional, empirically un-separated"** — the
> lane's "decisive" static-dress receipt was found CIRCULAR and is withdrawn.
> Its banked finding — that the two 0.9963 clocks are the **same number
> exactly**, canon's Δ=1.4e-5 being a linearization artifact — is routed as
> `_orchestration/open-items/2026-08-25-storage-response-clock-identity.md`
> and is Grant's to rule on. Nothing here is canon.

# LANE A3 — ENVELOPE-FORK COLLAPSE CHECK — RECEIPT (v2, REPAIRED)

**Status: CHECK, not a ruling.** Mints nothing, moves no solidity. Every number below was
computed, not asserted (`check.py`, `exact_collapse.py`, repo `ALPHA`). Corpus read-only at
`/Users/grantlindblom/AVE-staging/AVE-Core`, `origin/main` = `766d5179`.

> **v2 REPAIR NOTICE.** v1 (`RECEIPT.v1-superseded.md`) is superseded. Three changes of substance:
> 1. **§6 WITHDRAWN — the "decisive" static-dress receipt is withdrawn in full.** It misreported
>    its source (quoted the source NOTE's *secondary* comparison as if it were the verdict) **and**
>    it is structurally circular (it measures a contour it was handed as input). Neither defect is
>    repairable by re-quoting; the receipt is gone, not fixed.
> 2. **§2's "structural clincher" is DEMOTED** from load-bearing to supporting. It is algebraically
>    true and undisputed, but it refutes a hypothesis nobody posed. The load-bearing leg is
>    textual and now leads.
> 3. **§5 is NEW and is the most useful thing in this document.** The two 0.9963 clocks that canon
>    annotates at five sites as a "near-collision, Δ = 1.4e-5" are **the same number exactly**. The
>    1.4e-5 is a linearization artifact of canon's own truncation, not a physical gap.
>
> The four numbers (§3), all ten canon quotations (§1), the §8(B) discriminator table and the
> §10 two-ruling separation were independently reproduced by the verify lane and are unchanged.

---

## VERDICT: **DISTINCT — but the confidence drops, and one leg is gone.**

**DISTINCT, on definitional grounds, empirically un-separated.**

The two criteria are distinct because `strain-registers.md`:63-64 **states them with one symbol
$A$ and one kernel** — the storage/response split is a choice of *which condition to impose at
fixed coordinates*, not a choice of coordinates. That is textual, verifiable, and sufficient. The
envelope fork is a coordinate choice ($A^2 \to 2A^2$); it cannot *be* a criterion fork.

What v1 got wrong: it delivered this with two load-bearing legs, and the empirical one does not
survive. **There is no measurement in the corpus that separates the two criteria.** The honest
line is *definitional, empirically un-separated* — not *"structural clincher + decisive receipt"*.

**And one thing v1 missed entirely, which changes how the fork should be read (§5):** under the
exact response condition the two clock readouts are **identically equal for all $\alpha$**. So no
clock/rate observable can ever discriminate the contour fork — not at 1.4e-5 precision, not at any
precision. Canon's *"the rate alone cannot discriminate the contour"* is true for a **stronger
reason than canon states**.

---

## §1 — The four canonical texts, verbatim

*(Unchanged from v1. Every line below was independently re-verified at its cited line at
`766d5179` by the verify lane and again by this pass.)*

**DP-1 — C-state row** (`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md`:56, :62):

> | $A^2_{\text{local}}$ | $(\sum_{\text{ports}} V_{\text{inc}}^2) / V_{\text{SNAP}}^2$ | Per-cell aggregate saturation level (chi-squared-of-4 across ports) |

> **What $A$ is (DP-1, 2026-07-02, Grant-ratified).** The Axiom-4 argument $A$ is the **normalized substrate strain** ... and is the reactive-amplitude **envelope** (the cycle time-average / conserved reactive energy of the $(V_{\text{inc}},\Phi_{\text{link}})$-type tank), NOT an instantaneous phase snapshot. ... The $A^2_{\text{local}}=\Sigma V_{\text{inc}}^2/V_{\text{SNAP}}^2$ row above is the C-state projection of this envelope for the K4-V sector.

**DP-3 — full-tank form** (same file, :85, :87):

> $$A^2_{\text{total}} = A^2_V + A^2_\omega$$
> where $A^2_V = (V_{\text{inc}}^2 + \Phi_{\text{link}}^2/(LC)) / V_{\text{SNAP}}^2$ and $A^2_\omega = \kappa^2 / \omega_{\text{yield}}^2$.

> **R2 fix (DP-3, 2026-07-02, Grant-ratified).** The V-sector strain is the bond-LC tank's **reactive-energy envelope** — its C-state $V_{\text{inc}}$ plus its *conjugate* L-state $\Phi_{\text{link}}$ ... *(Normalization of the $\Phi_{\text{link}}^2/(LC)$ term flagged for review-on-merge.)*

**Contour tag** (`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md`:49-55):

> The reflection magnitude $|\Gamma| = \sqrt{1-\alpha} = 0.996345$ is the **STORAGE clock** — the $\sqrt{S}$-projection of the **storage-α** criterion ($A^2 = \alpha$, stored fraction $= \alpha$). It is **NOT** the response clock $(1-2\alpha)^{1/4} = 0.996331$ (the **response-α** knee $A^2 = 2\alpha$, deficit $\Delta S = \alpha$ ...). The two 0.9963s **near-collide, $\Delta = 1.4\times10^{-5}$** (two readings of one kernel one Taylor-order apart) ...

**Op14 companion** (`.../op14-local-clock-modulation.md`:60-67) states the mirror image of the same tag.

**The carve that already exists — THE LOAD-BEARING TEXT** (`manuscript/ave-kb/common/strain-registers.md`:63-68):

> - **STORAGE criterion — "stored fraction $= \alpha$":** $A^2 = \alpha \Rightarrow A = \sqrt{\alpha} \approx 0.0854$.
> - **RESPONSE criterion — "deficit $\Delta S = \alpha$":** $A^2 = 2\alpha \Rightarrow A = \sqrt{2\alpha} \approx 0.1208$.
>
> **The 2 is the Taylor-½ of the root kernel — UNCONDITIONAL.** The deficit of the quarter-arc kernel is $\Delta S = 1 - \sqrt{1-A^2} \approx A^2/2$ (leading order). So "deficit $=\alpha$" gives $A^2/2 = \alpha \Rightarrow A^2 = 2\alpha$, while "stored fraction $=\alpha$" gives $A^2=\alpha$ directly. **The factor of 2 is the $\tfrac12$ from the square-root's Taylor expansion** — a property of the kernel's *shape*, present whether or not any wave is involved.

---

## §2 — The algebra, written out

**LEG 1 (load-bearing) — the carve is DEFINITIONAL, and canon writes it that way.**
`strain-registers.md`:63-64 states both criteria in **one convention**: one symbol $A$, one kernel
$S=\sqrt{1-A^2}$, two different *conditions imposed on that one $A$*.

| criterion | condition imposed on the one $A$ | solves to |
|---|---|---|
| STORAGE-α | stored fraction $=\alpha$ | $A^2=\alpha$ |
| RESPONSE-α | deficit $\Delta S = 1-\sqrt{1-A^2} = \alpha$ | $A^2 = 1-(1-\alpha)^2 = 2\alpha-\alpha^2$ (canon truncates to $2\alpha$) |

Two conditions on one coordinate cannot be a *coordinate* ambiguity. The CANDIDATE ("the two
contours are one contour seen in two envelope conventions") requires the separation to be a
convention artifact; canon's own text says it is a choice of condition at fixed convention. **That
is the whole anti-collapse argument, and it is textual, not numerical.**

**LEG 2 (supporting, DEMOTED) — the ratio-invariance observation.**
A global rescale $A^2\to 2A^2$ acts on both rows identically (storage $\alpha\to2\alpha$, response
$2\alpha\to4\alpha$), so the *ratio* between the two criteria is invariant under the envelope map;
a global rescaling cannot generate a relative factor.

> **Honest labelling of Leg 2.** This is algebraically true (sympy: $\text{map(storage)}/\text{map(response)} = 1/(2-\alpha) =$ the unmapped ratio) and it was **not disputed** at verify. But it is
> **weak**: it is true of *any* global rescale, and it presupposes that two distinct criteria exist
> in order to have a ratio — which is exactly what the collapse hypothesis denies. It refutes
> *"the envelope map carries storage onto response"* (which no one claimed) rather than *"α and 2α
> are one contour in two conventions"* (which is the CANDIDATE). v1 led with this; v2 does not.
> It is retained as a consistency observation, not as a clincher.

**Where the near-collision comes from (v1's reading — superseded by §5).**
The two canonical numbers use different *readout exponents* as well as different arguments:

$$\underbrace{(1-\alpha)^{1/2}}_{\text{storage clock, CVR }|\Gamma|}
\qquad\text{vs}\qquad
\underbrace{(1-2\alpha)^{1/4}}_{\text{response clock, }c_{\text{shear}}=c_0(1-A^2)^{1/4}}$$

Both $\approx 1-\tfrac{\alpha}{2}$ because $\tfrac12\!\cdot\!\alpha = \tfrac14\!\cdot\!2\alpha$. The
exponent difference (½ vs ¼) is separately-ratified physics — the $c_{\text{shear}}=c_0\sqrt S$
correction (`clm-8nkvwy`, 2026-06-22; `op14-local-clock-modulation.md`:16, `scale_invariant.py`:294).

> **PRIOR-ART CREDIT (v1 omission, corrected).** This exponent×argument reading is **not new here**.
> `research/2026-07-14_quarter-power-map.md`:256-262 already carries it as
> *"★ THE NEAR-COLLISION HAZARD ROW (mandatory annotation on the map)"*, verbatim at :259-260:
> *"identical to `1.35e-5` (both `= 1 − α/2 + O(α²)`; diff recomputed this session `= 1.346e-5`)"*.
> v1's headline complaint was that the walk record *"rediscovered an answered question and does not
> cite the answer"* — while v1 itself re-derived the quarter-power map's central algebra without
> citing it, from a document dated the same day as the NOTE it did cite. Charged to this lane.

## §3 — The four numbers (computed, repo `ave.core.constants.ALPHA = 0.0072973525693`, `constants.py`:163)

| # | criterion | envelope convention | $A^2$ | readout | value |
|---|---|---|---|---|---|
| **N1** | storage-α | **C-state (native)** | $\alpha$ | $(1-A^2)^{1/2}$ | **0.9963446429** |
| **N2** | storage-α | full-tank (mapped) | $2\alpha$ | $(1-A^2)^{1/2}$ | **0.9926758257** |
| **N3** | response-α | C-state (mapped) | $\alpha$ | $(1-A^2)^{1/4}$ | **0.9981706482** |
| **N4** | response-α | **full-tank (native)** | $2\alpha$ | $(1-A^2)^{1/4}$ | **0.9963311827** |

- canon's near-collision = |N1 − N4| = **1.3460e-05** — **see §5: this is an artifact, not a scale**
- envelope map applied to storage = |N1 − N2| = **3.6688e-03** = **273×** that gap
- envelope map applied to response = |N4 − N3| = **1.8395e-03** = **137×** that gap

**Read:** the envelope map does not carry N1 onto N4. It carries N1→N2 and N4→N3, both two-to-three
orders of magnitude *away* from the collision. The collision relates the two **native** readings,
which no envelope map connects.

> **Yardstick caveat (v2).** The "273×/137×" ratios are measured against |N1−N4| = 1.346e-5, and §5
> shows that gap is entirely the corpus's own $\alpha^2$ truncation — **not a physical scale**. The
> ratios are arithmetically correct and reproduce bit-for-bit, but they should be read as
> *"two-to-three orders of magnitude, against a denominator that is an artifact"*, not as a
> calibrated significance. The qualitative conclusion (the map does not connect N1 to N4) does not
> depend on the denominator.

## §4 — Exact or O(α)? — EXACT on arguments **under two stated conditions**, ABSENT on readouts

1. **EXACT on arguments — CONDITIONAL, and v1 stated it unconditionally.**
   $A_C^2=\alpha \Rightarrow A_F^2=2\alpha$ is exact — bit-for-bit the same float as
   `A_YIELD_SQ = 2.0 * float(ALPHA)` (`src/ave/core/chiral_lattice_v10.py`:30). **But the $\times2$
   requires BOTH:**
   - **(i) equipartition** $\langle\Phi_{\text{link}}^2/(LC)\rangle=\langle V_{\text{inc}}^2\rangle$
     — a cycle-average, traveling-wave property. Standing waves slosh between quadratures
     (`strain-registers.md`:68 makes exactly this point), so (i) is regime-dependent.
   - **(ii) the normalization of the $\Phi_{\text{link}}^2/(LC)$ term** — which canon itself flags as
     unsettled at `substrate-perspective-electron.md`:87, verbatim: *"(Normalization of the
     $\Phi_{\text{link}}^2/(LC)$ term flagged for review-on-merge.)"*

   **If (ii) resolves to anything but 1, the map is not $\times2$ and the CANDIDATE dissolves for a
   different reason than this check gives.** v1 stated (i) in prose and cited (ii) in its §8, but
   wrote "exact, not O(α)" unconditionally in the verdict line. Corrected.

   The cross-constraint stands and Grant should have it: **if the electron's $A=\sqrt\alpha$ was
   computed in the C-state convention and the corpus flips the envelope fork to full-tank, the
   electron's operating point lands exactly on the response knee `A_YIELD_SQ`.** That is a collision
   of **addresses**, not of criteria — and it means the yield family (`constants.py`:499,505,516)
   and the knee family (`:525`, `chiral_lattice_v10.py`:30) must move in lockstep.

2. **ABSENT on readouts.** The two criteria's readouts (§3) are not related by the map at any order.

3. **The $O(\alpha^2)$ separation inside the response criterion** — see §5, which is where this
   ingredient actually leads.

---

## §5 ★ — THE TWO 0.9963 CLOCKS ARE THE SAME NUMBER, EXACTLY

**This is the banked result and it is new to this receipt.** v1 computed the ingredient
($A^2 = 2\alpha-\alpha^2$) and filed it as *"a residual O(α²) degeneracy inside the response
criterion"* without ever connecting it to the readouts. Connected here.

**The derivation.** Take canon's own response condition, `strain-registers.md`:66, and solve it
**exactly** instead of at leading order:

$$\Delta S \;=\; 1-\sqrt{1-A^2} \;=\; \alpha
\quad\Longrightarrow\quad \sqrt{1-A^2} = 1-\alpha
\quad\Longrightarrow\quad 1-A^2 = (1-\alpha)^2
\quad\Longrightarrow\quad A^2 = 2\alpha-\alpha^2 .$$

Now read the response clock at that contour:

$$c_{\text{shear}}/c_0 \;=\; (1-A^2)^{1/4} \;=\; \big((1-\alpha)^2\big)^{1/4} \;=\; (1-\alpha)^{1/2}
\;\equiv\; \text{the STORAGE clock } |\Gamma| = \sqrt{1-\alpha}.$$

**Identically, for all $\alpha \in (0,1)$. Not to leading order — exactly.**

**The one-line reason.** The exact response condition *defines* $S_{\text{resp}} = 1-\alpha$, while
the storage condition gives $S_{\text{store}} = \sqrt{1-\alpha}$. So
$S_{\text{resp}} = (S_{\text{store}})^2$, hence $\sqrt{S_{\text{resp}}} = S_{\text{store}}$. **The
¼-vs-½ exponent difference is exactly cancelled by the $\alpha$-vs-$(2\alpha-\alpha^2)$ argument
difference.** It was never a coincidence to be mined; it is a tautology of the two definitions.

**Receipts (`exact_collapse.py`, re-runnable):**

- **sympy:** `solve(1 - sqrt(1-A2) = alpha, A2)` → `alpha*(2 - alpha)`; `factor(1 - A2)` →
  `(alpha - 1)**2` (a perfect square); with $b=1-\alpha>0$ both clocks simplify to `sqrt(b)`;
  `simplify(response - storage)` → **`0`**, `IDENTITY HOLDS: True`. Kernel form:
  `S_resp = b`, `S_store**2 = b`, difference **`0`**.
- **mpmath, 50 dps, repo ALPHA:**
  storage `0.996344642897576882435001713050946036643071`,
  response-exact `0.996344642897576882435001713050946036643071`,
  `|difference| = 0.0` — **exactly zero at 50 decimal places.**

**Therefore canon's $\Delta = 1.4\times10^{-5}$ is a LINEARIZATION ARTIFACT.** It is the gap between
canon's *motivating condition* ($\Delta S=\alpha$) and canon's *operative contour*
($A^2=2\alpha$, `chiral_lattice_v10.py`:30 — which `quarter-power-map.md`:245-250 designates
"coordinate authority"). Computed decomposition:

| quantity | computed |
|---|---|
| $\sqrt{1-\alpha}-(1-2\alpha)^{1/4}$ (canon's "near-collision") | **1.34601747527e-05** |
| series of that difference (sympy) | $\alpha^2/4 + 3\alpha^3/8 + O(\alpha^4)$ |
| $\alpha^2/4$ | 1.33128386302e-05 |
| $\alpha^2/4 + 3\alpha^3/8$ | 1.34585613459e-05 |
| residual after two terms | 1.61e-09 |
| deficit **at** the operative contour, $1-\sqrt{1-2\alpha}$ | 0.0073241743341384 (vs $\alpha=0.0072973525693$; excess $2.68\text{e-}5 \approx \alpha^2/2$) |

The last row is canon's own: `quarter-power-map.md`:250 already records
*"`ΔS = α` (exactly `α+α²/2`)"* — i.e. the corpus already knew the operative contour does **not**
satisfy the motivating condition exactly. What was missing is the consequence for the readouts.

### Grade, and what is NOT claimed

- **DERIVED.** This is exact algebra on canon's own definitions (`strain-registers.md`:66 for the
  condition, `cvr-reflection-smith.md`:50 and `op14-local-clock-modulation.md`:61 for the two
  readouts), verified symbolically and to 50 dps. Nothing is assumed, nothing is fitted, no new
  structure is introduced.
- **NOT a collapse of the two criteria.** The *contours* remain distinct — $A^2=\alpha$ vs
  $A^2=2\alpha-\alpha^2$ are different surfaces in $A$. What collapses is the pair of *numbers*
  canon reads off them. §2 Leg 1 (DISTINCT) is untouched, and is if anything sharpened.
- **NOT a ruling.** Whether canon's contour-tagging discipline should be re-scoped in light of
  this — whether the operative contour should stay the truncated $2\alpha$ (which is what all
  downstream code consumes) or move to the exact $2\alpha-\alpha^2$, and whether the five
  "$\Delta=1.4\text{e-}5$" annotations should be restated — is an adjudication, not this lane's.
  **Routed, not decided.**

### What it changes for the tagging discipline (the payload)

Canon's tag says *"the rate alone cannot discriminate the contour — always carry the tag"*
(`cvr-reflection-smith.md`:55, `op14`:66). That is **right, for a stronger reason than canon
gives.** Canon presents it as a precision problem — the numbers differ by only 1.4e-5. It is not a
precision problem: **under the exact criterion the clock readouts are equal identically, so no
measurement of a clock/rate at any precision can ever separate the criteria.** A contour fork read
through the clock face is not merely hard to resolve — it is *unobservable through that face*.

That closes off one whole class of would-be discriminators. It does **not** by itself explain the
§6 withdrawal — the static-dress receipt fails for a separate reason (it takes $\sqrt{2\alpha}$ as
a measurement *input*, not as a clock readout). The two defects are independent; what they share is
that neither instrument could have returned a different answer.

---

## §6 — **WITHDRAWN:** the static-dress "no-wave receipt". It was not decisive and it was not a receipt.

v1 §5 claimed canon *"already has a no-wave receipt that kills the collapse"*, resting on
`strain-registers.md`:68 (*"the static dress (no wave, no equipartition) uses $\sqrt{2\alpha}$ and
matches $r99$"*) plus `research/2026-07-14_knee-contour-check_NOTE.md` §4.3 as the measurement
behind it. **That receipt is withdrawn in full.** Three defects, any one of which is fatal.

### 6.1 It materially misreported its source

v1 presented the NOTE §4.3 as **"ALREADY REPORTS"** with *"r99 ratio 1.06 (frozen) / 1.27
(refined), resolution-stable"*. That is the NOTE's **pre-declared secondary** comparison. Verbatim
at `knee-contour-check_NOTE.md`:

- **:173** — *"**PRIMARY (declared basis: field-strain `s_knee` vs `r90`): `PARTIAL`.**"*
  (:174: *"`ratio = 2.877 / 1.257 = 2.29` (frozen), `= 2.51` (refined)"* — recomputed here:
  2.877/1.257 = **2.2888**, 2.877/1.144 = **2.5149**.)
- **:178** — *"Secondary reported comparisons (NOT the declared verdict basis, reported per class rules):"*
  — the r99 line v1 quoted is the **first bullet under that heading** (:180).
- **:233-234** — *"It is NOT landed into the KB and NOT a MATCH-class
  \"the-knee-IS-the-dress-edge\" claim (the declared `r90` verdict is PARTIAL)."*
- **:248** — *"The `s_knee = 2.877 d_sat` VALUE candidate rides the `α`-echo (it is `(2α)^{−1/4}` in
  native units) — it is a consistency-class measured address, not an independent prediction."*

v1 quoted the secondary number, called it PRIMARY, and omitted all three of the source's own
disclaimers. **A number its own source classifies as riding the α-echo and explicitly not an
independent prediction cannot be the receipt that kills a collapse hypothesis.**

### 6.2 It is circular — the instrument was handed the factor it was supposed to measure

`knee-contour-check_NOTE.md`:110 defines the observable verbatim:

> Log-log interpolate the radius where the measured `A(s)` crosses `√(2α)` (`= R_I`)

and `R_I` is `constants.py`:525 — `R_I: float = np.sqrt(2.0 * ALPHA)`, tagged in that same line
*"[criterion: response-α — deficit ΔS=α, √(2α) knee family]"*. Verified: `R_I == math.sqrt(2*ALPHA)`
→ `True`, both `0.12080854745670937`.

**The response-α contour is an INPUT to the measurement.** And `:138` reports the profile:

> The measured single-probe `A(s)` tracks the bare field-strain `(d_sat/s)²` to `< 10⁻⁴`

Given $A(s)=(d_{sat}/s)^2$, setting $A=\sqrt{2\alpha}$ yields
$s/d_{sat} = (2\alpha)^{-1/4} = 2.8770749$ **algebraically** (computed). So the NOTE's "PRIMARY
2.877 matches the bare closed form 2.877" (`:143` vs `:144`) is an arithmetic identity confirming
the $1/s^2$ profile — it is **not** a measurement of the 2. Nothing in that configuration could
have returned a different factor. v1's claim *"Yet the response-criterion 2 is still present and
measured"* is unsupported.

### 6.3 It rests on the field-strain arm of an OPEN fork, unstated

`research/2026-07-14_quarter-power-map.md`:189-194, verbatim:

> **★ The voltage-strain fork (the sharpest internal falsifier).** Under the canonical
> `methodological-contamination.md:48-52` voltage strain `A = d_sat/r` (`∝ 1/r`), the knee radius
> is `d_sat/√(2α) = 8.278 ℓ_node` — a **HALF-power** (recomputed: `1/√(2α) = 8.2776`). The
> quarter-power radius exists ONLY under the inverse-square FIELD composition `A = (d_sat/s)²`.
> **Member 3's ¼-membership is therefore conditional on an OPEN fork** (knee-NOTE :241, branch
> `analysis/knee-contour-check`).

(Recomputed here: $1/\sqrt{2\alpha} = 8.277560$.) The NOTE flags the same fork at :240-243 and
reports the FLAGGED voltage-strain knee at :145. v1 quoted only the field-strain arm, with no
statement that the address is fork-conditional.

### 6.4 Canon says this evidence is still owed — v1 cited the line and softened it

`manuscript/ave-kb/.index/strengthen-by.jsonl`:212 on `clm-crit2a`, verbatim:

> a driven two-quadrature demo separating the wave's equipartition-½ from the kernel's Taylor-½
> (confirming the static dress needs no wave to carry the response-criterion 2)

That is canon recording the static-dress separation as **not yet confirmed** — i.e. canon has
already marked v1's load-bearing leg as owed evidence. v1 cited :212 but recast the ask as
*"the one-line hardening is to confirm $\Phi_{\text{link}} \equiv 0$ in that config"* — a narrower
and much easier item than what canon actually asks for. Corrected: **the ask is a driven
two-quadrature demo, and it has not been run.**

### 6.5 What a NON-circular test would have to do

The instrument must be able to return a factor other than 2. Three requirements, and the reason
each is needed:

1. **The contour must come OUT, not go IN.** Locate a feature by something independent of
   $\sqrt{2\alpha}$ — e.g. the $s^{-6}$ falloff onset, the $\chi_{sat}$ divergence edge, or an
   enclosed-fraction radius (`r50/r90/r99`) — and then *report what $A$, and hence what deficit,
   is found there*. The NOTE's §5 already does exactly this at `r90` and gets
   $A = 0.633$, $\Delta S = 0.226 \approx 31\alpha$ (`:194-200`) — i.e. when the contour is allowed
   to come out of the measurement, it does **not** come out at $\alpha$. That is the honest shape
   of the answer, and it is not a confirmation.
2. **It must read an observable the fork is not blind to.** Per §5, any clock/rate readout is
   *identically* degenerate between the two criteria — it can never separate them. The separating
   observables are the **leak/linewidth** ($|\Gamma|^2$ complement: $\alpha$ vs $2\alpha$ — a clean
   factor 2, computed 7.297e-3 vs 1.459e-2) and the **wall location** (§8B).
3. **It must actually remove the wave.** Not "assume $\Phi_{\text{link}}=0$", but drive the two
   quadratures independently and show the response-criterion 2 survives at zero L-state — which is
   verbatim what `strengthen-by.jsonl`:212 asks for and what nobody has run.

**Net effect of the withdrawal on the verdict:** the empirical leg is gone; the definitional leg
(§2 Leg 1) is untouched. DISTINCT survives, at lower confidence, with *"empirically un-separated"*
now stated rather than papered over.

---

## §7 — Coincidence-density flag — **DEMOTED from three routes to two**

v1 claimed the corpus reaches $A^2=2\alpha$ by *"at least three structurally independent routes"*
and used that base rate as evidence for DISTINCT. **Route 3 is not independent.**

1. kernel Taylor-½ on "deficit $=\alpha$" (`strain-registers.md`:66) — independent.
2. envelope $\sqrt2$ map applied to storage-α (the CANDIDATE, §4.1) — independent.
3. ~~shared-radius two-grade sum~~ — **withdrawn as an independent route.**
   `trampoline-framework.md`:255 reads verbatim: *"the electron confines at
   $A_{A1}=\sqrt\alpha\approx0.085$, where a single-radius total would read only $2\alpha=0.0146$"*
   — that $2\alpha$ is $\alpha+\alpha$ summed across grades, where the $\alpha$ is **the same
   storage mark $A_{A1}=\sqrt\alpha$ that route 1 uses**. It is the same input counted twice, not a
   third route.

**Consequence:** the base rate is lower than v1 claimed, so the coincidence-density argument is
correspondingly weaker. It still points toward DISTINCT (two routes to one number is still
over-determination), but it is a hint, not evidence, and it was never load-bearing.

## §8 — The distinguishing operating points

**(A) ~~SEPARATOR — the static (DC) dress~~ — STATUS CHANGED: `ALREADY REPORTS` → `NOT RUN`.**
The *logic* of the operating point is still right: on a static dress $\Phi_{\text{link}}=0$, so
$A_F=A_C$, the envelope map is the identity, and any $2\alpha$ surviving there is not the envelope
2. **What is withdrawn is the claim that it has been run.** Per §6, the knee-contour NOTE does not
supply that measurement: its declared verdict is PARTIAL, its knee address is circular in
$\sqrt{2\alpha}$, and it is conditional on the open field-vs-voltage strain fork. The correct
status is the one canon already carries at `strengthen-by.jsonl`:212 — **owed**.

**(B) ENVELOPE-FORK DISCRIMINATOR — a driven tank swept to $A_C^2 \sim 0.3$–0.5. UN-RUN.**
*(Unchanged from v1; independently recomputed at verify.)* The envelope fork is a **factor 2 in
the kernel argument at every amplitude**, so its signature is only α-suppressed in the electron's
low-amplitude corner. Computed, $S=\sqrt{1-A^2}$, $Z_{\text{eff}}=Z_0/\sqrt S$:

| $A_C^2$ | $S$ (C-state) | $S$ (full-tank) | $S_F/S_C$ | $\|\Delta Z\|/Z$ |
|---:|---:|---:|---:|---:|
| $\alpha$ = 0.0073 | 0.996345 | 0.992676 | 0.9963 | 0.0018 |
| 0.10 | 0.948683 | 0.894427 | 0.9428 | 0.0299 |
| 0.20 | 0.894427 | 0.774597 | 0.8660 | 0.0746 |
| 0.30 | 0.836660 | 0.632456 | 0.7559 | 0.1502 |
| 0.40 | 0.774597 | 0.447214 | 0.5774 | 0.3161 |
| 0.49 | 0.714143 | 0.141421 | 0.1980 | 1.2472 |

Sharpest form: **the two conventions disagree about where the wall is by a factor 2 in $A^2$** —
full-tank hits $S\to0$ at $A_C^2=0.5$ while C-state still reads $S=0.707$. Reachable by a driven
high-amplitude resonator or the loop-gap engine.

**And at the electron, read the right face and the envelope fork already separates 542×:**
- envelope fork → per-cycle leak $|\Gamma|^2$ complement $=\alpha$ vs $2\alpha$: a **factor 2**
  (7.297e-3 vs 1.459e-2) in radiative leak / linewidth.
- contour fork → rate gap 1.346e-5 (**and per §5 that gap is an artifact, so the real contrast is
  even starker: the leak sees the envelope fork at O(1), the rate sees the contour fork at zero**).

**Note on DP-3's own open discriminator.** `trampoline-framework.md`:255's *"a non-$\alpha$-suppressed
operating point is needed"* refers to the **cross-grade combine** (L∞-max vs normalized-L2) — a
**third** fork, distinct from both of these. Operating point (B) serves it too; worth ruling all
the factor-in-$A^2$ questions at one operating point.

## §9 — Canon-hygiene items surfaced (flag-don't-fix; nothing edited, corpus read-only)

1. **`√S`-projection is mislabelled in two of three sites.** At $A^2=\alpha$: $S=\sqrt{1-\alpha}=
   0.9963446429$ and $\sqrt S=(1-\alpha)^{1/4}=0.9981706482$ (computed). So
   `cvr-reflection-smith.md`:50 calling $|\Gamma|=\sqrt{1-\alpha}=0.996345$ *"the $\sqrt{S}$-projection
   of the storage-α criterion"* names **$S$, not $\sqrt S$**. `op14-local-clock-modulation.md`:61 IS
   correct ($(1-2\alpha)^{1/4} = \sqrt S$ at $A^2=2\alpha$), but :63 repeats the wrong label for the
   storage side, and `strain-registers.md`:70 applies one phrase to both
   (*"These are the two criteria's $\sqrt{S}$-projections"*). **One phrase, two different functional
   forms.** This matters here: reading both as "$\sqrt S$ of something" is precisely the reading
   that manufactures the collapse intuition this lane was sent to test. Stated correctly, the pair
   is *$S$ at the storage contour* vs *$\sqrt S$ at the response contour* — and §5 shows those are
   equal because $S_{\text{resp}} = S_{\text{store}}^2$ exactly.
2. **The quoted $\Delta = 1.4\times10^{-5}$ is stale in the first digit.** Computed:
   **1.34601747527e-05**, which rounds to 1.3e-5. `quarter-power-map.md`:259-260 already recorded
   the correct value (*"diff recomputed this session `= 1.346e-5`"*), so five KB sites carry the
   stale digit: `cvr-reflection-smith.md`:54, `op14-local-clock-modulation.md`:65,
   `strain-registers.md`:70 and :128, `common/claim-quality.md`:1506. **Superseded in importance by
   §5** — the more consequential correction is that the quantity is a truncation artifact, not that
   its first digit is off.

## §10 — What Grant is being asked to rule (unchanged in structure; one status corrected)

Two independent rulings, not one:

- **ENVELOPE FORK (OPEN):** is Axiom-4's $A$ the C-state projection (DP-1) or the full-tank
  reactive envelope (DP-3)? Arms: (i) C-state — `A²=ΣV_inc²/V_SNAP²`, electron at $A^2=\alpha$,
  leak $=\alpha$, wall at $A_C^2=1$; (ii) full-tank — `A²=(V_inc²+Φ²/LC)/V_SNAP²`, electron at
  $A^2=2\alpha$, leak $=2\alpha$, wall at $A_C^2=0.5$. **Canon knows this is open and says so in
  both leaves** — `substrate-perspective-electron.md`:62 calls the C-state row *"the C-state
  projection of this envelope"*, and :87 carries *"(Normalization of the $\Phi_{\text{link}}^2/(LC)$
  term flagged for review-on-merge.)"* The arms are not free: whichever wins, $V_{\text{SNAP}}$ must
  be normalized in the same counting or the whole yield family (`constants.py`:499,505,516) moves,
  and under the full-tank arm the electron lands **exactly** on `A_YIELD_SQ` (`:525`,
  `chiral_lattice_v10.py`:30) — so the yield and knee families must be re-normalized in lockstep.
  **Best available discriminator: §8(B), un-run.**
- **CONTOUR FORK (already carved, Ruling 12, 2026-07-17):** storage-α vs response-α — a tagging
  discipline, already discharged. Nothing here reopens it. **But §5 routes one question back to
  whoever owns Ruling 12:** the two tagged clock values are exactly equal under the exact
  criterion, so the five "$\Delta=1.4\times10^{-5}$ near-collision" annotations describe a
  truncation, not a coincidence — and the tag's justification is stronger than what it currently
  says. Whether to re-scope the annotation, and whether the operative contour stays the truncated
  $2\alpha$ (all downstream code consumes it) or moves to the exact $2\alpha-\alpha^2$, is a
  **ruling, not this lane's call**.

**One-line version:** ruling the envelope fork does not rule the contour fork, and the contour fork
does not need ruling — but it does need one annotation corrected. Ruling the envelope fork moves
the electron's operating point by exactly a factor 2 in $A^2$, and the yield-family constants must
move with it.

---

## §11 — Disposition of every verify-lane finding (the spec for this repair)

| # | sev | finding (abbrev) | disposition |
|---|---|---|---|
| 1 | PASS | all four numbers reproduce bit-for-bit; 273×/137× correct; §8(B) table and 542× correct | **UNDISTURBED.** §3 and §8(B) carry forward unchanged. One qualifier added (§3 yardstick caveat): the 273×/137× denominator is an artifact per §5. |
| 2 | PASS | every quoted canon text verifies verbatim at its cited line; no fabrication, no drift | **UNDISTURBED.** All quotes re-verified this pass at `766d5179`, plus the newly-cited lines (NOTE:110,138,143-145,173-180,194-200,233-234,240-248; quarter-power-map:189-194,245-262; strengthen-by:212; constants.py:163,525). |
| 3 | **HIGH** | §5's "decisive" static-dress receipt materially misreports its source | **FIXED — receipt WITHDRAWN.** §6.1 restates the NOTE's actual declared PRIMARY verdict (PARTIAL, 2.29/2.51 — recomputed 2.2888/2.5149), quotes :178 marking the r99 line secondary, and adds the omitted :233-234 and :248. Not re-quoted-and-kept: withdrawn. |
| 4 | **HIGH** | the static-dress receipt is CIRCULAR — NOTE:110 crosses $\sqrt{2\alpha}$ = `R_I` = the response-α value | **FIXED — receipt WITHDRAWN.** §6.2 shows `R_I == sqrt(2*ALPHA)` (computed, `True`) and that $A(s)=(d_{sat}/s)^2$ makes $s_{knee}=(2\alpha)^{-1/4}=2.8770749$ algebraic. §6.5 states what a non-circular test needs. §8(A) status changed `ALREADY REPORTS` → `NOT RUN`. |
| 5 | MED | ★ MISSED RESULT: exact response criterion makes the two clocks identically equal | **BANKED — §5, new section, headline of this receipt.** sympy `IDENTITY HOLDS: True`; mpmath 50 dps difference exactly `0.0`; series $\alpha^2/4+3\alpha^3/8$; $\alpha^2/4=1.33128386302\text{e-}5$, two-term $1.34585613459\text{e-}5$ vs measured $1.34601747527\text{e-}5$. Graded DERIVED; re-scoping the canon tag routed as a ruling, not decided. |
| 6 | MED | on-point prior work not cited (`quarter-power-map.md`:256 hazard row) while headlining a citation failure | **FIXED.** §2 carries an explicit PRIOR-ART CREDIT block quoting :259-260 and charging the omission to this lane. :250 (*"ΔS = α (exactly α+α²/2)"*) is now cited in §5 as canon's own prior record of the truncation. |
| 7 | MED | static-dress receipt rests on the field-vs-voltage strain arm of an OPEN fork, unstated | **FIXED.** §6.3, quoting `quarter-power-map.md`:189-194 verbatim, with $1/\sqrt{2\alpha}=8.277560$ recomputed. Moot for the verdict (§6 is withdrawn), retained because it independently conditions the 2.877 address. |
| 8 | MED | `strengthen-by.jsonl`:212 softened into a Φ_link-initialization check | **FIXED.** §6.4 restates :212 verbatim and states plainly that canon marks this leg as owed and the driven two-quadrature demo has not been run. |
| 9 | MED | the "structural clincher" is a tautology aimed at a weaker hypothesis; the load-bearing leg is textual and buried | **FIXED — DEMOTED.** §2 now leads with Leg 1 (`strain-registers.md`:63-64, one symbol/one kernel = definitional). The ratio argument is Leg 2, explicitly labelled weak and explicitly noted as *undisputed but not load-bearing*. Verdict re-issued as *"definitional, empirically un-separated"*. |
| 10 | MED | "EXACT, not O(α)" is conditional but stated unconditionally | **FIXED.** §4.1 now states both conditions — equipartition (regime-dependent) and the `substrate-perspective-electron.md`:87 normalization flag — and says that if (ii) ≠ 1 the CANDIDATE dissolves for a different reason. The verdict line no longer carries an unconditional "exact". |
| 11 | LOW | one of three "independent routes" to $2\alpha$ is not independent | **FIXED — DEMOTED.** §7 withdraws route 3 (it re-uses route 1's $A_{A1}=\sqrt\alpha$), lowers the base rate, and re-labels the whole argument a hint rather than evidence. |
| 12 | LOW | canon's `√S`-projection label is applied to two different functional forms | **FIXED — SURFACED.** §9.1, with $S=0.9963446429$ vs $\sqrt S=0.9981706482$ at $A^2=\alpha$ computed, and the connection to §5 made explicit ($S_{\text{resp}}=S_{\text{store}}^2$). |
| 13 | LOW | quoted $\Delta=1.4\text{e-}5$ is stale in the first digit at five KB sites | **FIXED — SURFACED.** §9.2, computed 1.34601747527e-05, five sites listed, and noted as superseded in importance by §5. |
| 14 | PASS | the "one ruling settles both" trap is correctly avoided; §8 two-fork separation and the `A_YIELD_SQ` address-collision are correct | **UNDISTURBED.** §10 carries it forward, with one addition (the §5 annotation question routed back to Ruling 12's owner). |

**Nothing was minted. No solidity moved. No corpus file was edited** — the corpus was opened
read-only at `766d5179` and every write in this lane is under
`/private/tmp/.../scratchpad/a3collapse/`.

## §12 — Files

| file | what |
|---|---|
| `RECEIPT.md` | this document (v2, repaired) |
| `RECEIPT.v1-superseded.md` | v1, retained verbatim as the audit trail |
| `check.py` | the four numbers + the §8(B) discriminator table (`PYTHONPATH=/Users/grantlindblom/AVE-staging/AVE-Core/src python3 check.py`) |
| `exact_collapse.py` | **§5's proof** — sympy identity, mpmath 50-dps check, the series decomposition, the `√S`-label check, and the circularity arithmetic (same invocation) |
