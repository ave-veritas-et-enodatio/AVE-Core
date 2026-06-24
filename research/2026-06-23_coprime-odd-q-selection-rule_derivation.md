# Lane D-gate — The Coprime-Odd-q Stability Selection Rule

**Date:** 2026-06-23 · **Lane:** D-gate (Lattice Dynamic-Regime Discovery Program §3 Lane D)
**Branch:** `analysis/coprime-odd-q-selection-rule`
**Type:** Derivation + pre-registration + validate-on-known (research doc; small code check of the rule against the known ladder)
**Status:** DRAFT for orchestrator audit + Grant adjudication

---

## 0. The one-line gate

> **Why does the chiral K4 Laves lattice admit only coprime-odd-q $(2,q)$ torus knots as STABLE loop excitations?**

Everything downstream of Lane D (the $c\ge21$ ladder continuation, strangeness-as-index,
the tetra/penta-quark prime-$N$ test) hangs on this selection rule. This doc derives the rule
from substrate primitives, validates it against the known stable set, and renders an
**honest FORCED-vs-FITTED verdict** — the prize is a rule *forced* by substrate topology that
*then* happens to select the knowns, not a rule reverse-engineered from them.

---

## SECTION INDEX (skeleton — sections filled incrementally)

1. Pre-registration (frozen before derivation)
2. Asserted-vs-derived map of the current taxonomy
3. The derivation — three independent substrate constraints
4. Validate-on-known
5. Predictions the rule forces (NOT the full enumeration — that is D-full)
6. The critical guard — FORCED or FITTED?
7. Scope, open gaps, recommendation

<!-- sections appended below in order -->

---

## 1. Pre-registration (frozen BEFORE the derivation)

Per `ave-prereg`. Corpus survey (Phase 0) confirmed there is **no existing dedicated leaf or
research doc** that assembles the coprime-odd-q rule as a single derived gate. The pieces exist
scattered:

- coprimality → single knot vs link: `torus-knot-uniqueness.md` §4 (clm-8c3yhs)
- both-windings ≥ 2 → non-trivial knot vs unknot: `torus-knot-uniqueness.md` §3
- "the ladder uses only odd q": ASSERTED in `constants.py:913` + `torus-knot-ladder.md:8`,
  but **the WHY is not derived as a rule** — it is justified only by the gcd argument applied at
  the *already-fixed* $p=2$ (i.e. "no $(2,4)$ because $\gcd=2$"), which presupposes $p=2$.
- $p=2$ itself: never derived as a constraint. The corpus *asserts* the electron is $(2,3)$ by
  "smallest non-trivial coprime pair" minimality, and the baryon ladder is $(2,q)$ "by the same
  family" — but **WHY the family is $p=2$ and not $p=3$** (i.e. why $(3,4),(3,5),(3,7),\dots$ are
  excluded from the stable set) is the load-bearing un-derived step.

**This doc's job is to derive $p=2$ and $q$-odd as a SINGLE forced gate, not to re-assert them.**

### 1.1 Pre-registered adjudication criteria (frozen)

| # | Pre-registered claim | PASS condition | FAIL condition |
|---|---|---|---|
| **P1** | The rule recovers the known stable set | Selects $(2,3)$ electron, the $(2,5)$ proton-class winding, and forbids $(2,4),(2,2),(1,n),(3,3),(2,6)$ | Selects an unknot/link as stable, OR fails to select $(2,3)$ |
| **P2** | $p=2$ is FORCED, not fitted | A substrate constraint (independent of the particle list) forces the minor winding to $p=2$ | $p=2$ only follows from "match the electron" |
| **P3** | $q$-odd is FORCED, not fitted | Given $p=2$, a substrate constraint forces $q$ odd | $q$-odd only follows from "match the baryon masses" |
| **P4** | The rule has predictive content beyond the knowns | It forbids specific $(p,q)$ that a naive "any coprime pair" rule would allow ($(3,4),(3,5),(2,4),\dots$), and continues the ladder to $c\ge21$ | The rule's allowed set $=$ exactly the hand-listed known particles with no exclusions and no continuation |

### 1.2 Pre-registered honest-closure trap (Rule 11)

If the derivation of P2/P3 **only** closes by invoking "the electron is the lightest lepton" or
"the proton is at $c=5$" — i.e. if removing the known-particle identifications collapses the
derivation — then the verdict is **FITTED (echo)**, the gate does NOT unblock D-full, and this doc
records a clean negative: *the selection rule is a re-encoding of the known assignments, not a
substrate chord.* No rescue-debugging toward a FORCED label is permitted post-hoc.

### 1.3 Coordinate discipline (phase-space-coordinate-check, A46 / def-kn0t01)

The $(p,q)$ label is a **phase-space Clifford-torus winding portrait** on the bond-pair LC tank
(`def-kn0t01` SOLID), NOT a real-space body knot (electron body $=0_1$ unknot; proton body
$=6^3_2$ Borromean). Any substrate constraint invoked to force $p$ or $q$ must be stated in
**matching coordinates**: a real-space mechanism (e.g. the FM kink's $SU(2)$ holonomy) and a
phase-space winding pair are different coordinate systems. The derivation below is explicit about
which constraint lives in which system, and flags the cross-system bridge as the load-bearing
(and least-secure) link — exactly per A46.

---

## 2. Asserted-vs-derived map of the current taxonomy

What the corpus ACTUALLY has, separated honestly (verify-before-cite — every cite grepped on this
branch HEAD):

| Ingredient | Status in corpus | Cite |
|---|---|---|
| $\gcd(p,q)=1 \Rightarrow$ single-component knot (else $d$-component link) | **DERIVED** (standard knot theory, correctly applied) | `torus-knot-uniqueness.md:67-71` (clm-8c3yhs) |
| $p,q\ge2 \Rightarrow$ non-trivial knot (else unknot, $c=0$) | **DERIVED** (standard knot theory) | `torus-knot-uniqueness.md:61-65` |
| Fractional/non-integer winding forbidden (severs the manifold) | **DERIVED** (charge $=$ integer winding $N\in\mathbb{Z}$) | `topological-fractionalization.md:12` (clm-mnb3lt/clm-67jn9o) |
| Electron $=(2,3)$ smallest non-trivial coprime knot | **DERIVED-given-identification** ("electron $=$ lightest non-trivial lepton") | `torus-knot-uniqueness.md:85-93` |
| The baryon ladder is the $(2,q_{\text{odd}})$ family | **ASSERTED** — "the ladder uses only odd q" stated, justified post-hoc by gcd at fixed $p=2$ | `constants.py:913`, `torus-knot-ladder.md:8` (clm-k6olj8) |
| **$p=2$ (the family is $p=2$, not $p=3$)** | **NOT DERIVED** — presupposed throughout; the gcd argument is applied *after* $p=2$ is fixed | (gap — this doc) |
| Spin-½ via $4\pi$ FM double-cover ($K_4\to A_4\to 2T\subset SU(2)$, $\mathbb{Z}_2$ quotient) | **DERIVED** (real-space; engine-corroborated representability) | `finkelstein-misner-spin-half-derivation.md` §3 (clm-salw2h); gate `research/2026-06-19_spin-doublecover-gate_result.md` |
| $\Gamma_{spinor}=-1$ stability wall ($2\pi\to4\pi$ spinor sign, T2 micro-rotation) | **DERIVED-as-class-invariant** (ALL fermions) | `resonant-lc-solitons.md:91` |
| Borromean $N=3$ baryon, $\mathbb{Z}_3$ permutation → quark thirds | **DERIVED-given-identification** | `topological-fractionalization.md:20-45` |
| Strange baryons $\Lambda,\Sigma,\Xi,\Omega$ + all mesons | **NOT NATIVELY DERIVED — open GAP** (corpus honestly flags) | `torus-knot-ladder-baryons.md:11` SCOPE FLAG |
| Neutrino $=0_1$ screw defect coupling to $(2,5)$ resonance; $c_1=5$ start | **PARTIALLY DERIVED** ($\Delta c=2$ from $\nu_{vac}=2/7$; absolute start asserted) | FI-13 resolution, `closure-roadmap:147`; FLAG-1 `closure-roadmap:187` |

**The honest gap is sharp:** the corpus has correctly derived *coprimality* and *non-triviality*
(both standard knot theory). It has NOT derived the two things that actually pin the family —
**$p=2$** and **$q$-odd-given-$p=2$** — as substrate constraints. It asserts them and then uses
minimality + gcd as a *consistency* check. The minimality argument ("$(2,3)$ is the smallest
non-trivial coprime pair, so the electron is $(2,3)$") is a **selection among knots given that
the electron is the lightest** — it does NOT forbid $(3,4)$ from being *some other* stable
particle. That is the predictive hole this gate must close or expose.

---

## 3. The derivation — three independent substrate constraints

The selection rule is the **conjunction** of three constraints, each from a distinct substrate
primitive. I derive each WITHOUT reference to the particle list, then take the intersection in §4.

### Constraint C-α — Closure: $\gcd(p,q)=1$ (single-component loop)

**Substrate primitive:** charge is a conserved *integer* topological winding number; a fractional
twist would sever the continuous manifold (`topological-fractionalization.md:12`). A stable
charged excitation must therefore be a **single closed flux-tube loop** carrying one integer
winding — not a multi-component link of separately-closing loops.

A $(p,q)$ curve on the Clifford torus closes as a *single* component iff $\gcd(p,q)=1$; if
$\gcd(p,q)=d>1$ it is a $d$-component link (`torus-knot-uniqueness.md:67`). A $d$-component link is
$d$ separately-closing loops — $d$ separate charge quanta sitting at one site, not bound into one
excitation. For a *single* stable charged soliton:
$$\boxed{\gcd(p,q)=1}\qquad\text{(C-α, single-loop closure)}$$
This is **standard knot theory applied to the substrate's integer-charge primitive.** Fully derived,
particle-list-independent. **DERIVED.**

### Constraint C-β — Non-triviality: both windings $\ge 2$ (a real knot, not the unknot)

**Substrate primitive:** topological protection. A stable particle must be *protected* against
continuous deformation back to the vacuum. The protection mechanism in AVE is the phase-space
winding being topologically non-removable (`phase-locked-topological-thread.md`, clm-zuf7g1:
the $(2,3)$ phase-space winding is protected against continuous deformation below the Schwinger
threshold). An unknot in phase-space ($c=0$, one winding $=1$) carries no such protection — it can
be continuously unwound.

A $(p,q)$ portrait is the unknot (crossing number $c=\min(p(q{-}1),q(p{-}1))=0$) whenever $p=1$ or
$q=1$. For non-trivial protection:
$$\boxed{p\ge2 \ \text{and}\ q\ge2}\qquad\text{(C-β, non-trivial winding)}$$
**DERIVED** (standard knot theory + the protection primitive). Particle-list-independent.

> Note the electron's *real-space body* is the $0_1$ unknot; C-β is a constraint on the
> *phase-space winding portrait*, not the real-space body (`def-kn0t01`). The protection is carried
> by the phase-space winding, which is why a real-space unknot can still be a protected fermion.

### Constraint C-γ — Spinor closure: the minor winding is $p=2$ (the $\mathbb{Z}_2$ double cover)

**This is the load-bearing new step.** It is what pins the family to $p=2$.

**Substrate primitive (real-space):** A stable *charged matter* excitation carries spin-½ — it is a
fermion. (Charge sits on the Cosserat T2 micro-rotation grade; a charged loop excites that grade.)
Spin-½ in AVE is NOT a postulate: it is the Finkelstein–Misner kink on the extended loop, which
picks up the $K_4\to A_4\to 2T\subset SU(2)$ double cover. The defining property of this cover is
the $\mathbb{Z}_2$ quotient: a $2\pi$ real-space rotation lifts to $-I\in SU(2)$, and only $4\pi$
returns to $+I$ (`finkelstein-misner-spin-half-derivation.md` §3; engine-corroborated:
`probe_spin_doublecover_holonomy` returns $-I$ at $2\pi$, $+I$ at $4\pi$,
`research/2026-06-19_spin-doublecover-gate_result.md`).

**Substrate primitive (dynamical):** the $\Gamma_{spinor}=-1$ stability wall. The $2\pi\to4\pi$
spinor sign is a class-invariant **stability** boundary carried by ALL fermions
(`resonant-lc-solitons.md:91`, T2 sector). A loop that does NOT close its spinor sign under the
$4\pi$ cover does not sit at the $\Gamma_{spinor}=-1$ wall — it is not a stable fermion mode.

**The bridge (phase-space ↔ real-space — flagged per A46):** the minor winding number $p$ of the
phase-space portrait *is* the number of times the loop's frame wraps the poloidal (minor) circle of
the Clifford torus per real-space traversal. The poloidal circle is the $S^1$ fibre of the Hopf
fibration $SU(2)\to S^2$ whose $U(1)$ phase carries the $4\pi$ closure
(`finkelstein-misner...md` §6.5.2, Level-2 table: $w_1=2$ survives the Hopf projection, the fibre
carries the double-cover). For the loop to be a spinor — to pick up exactly the $\mathbb{Z}_2$
$(-I\ \text{at}\ 2\pi,\ +I\ \text{at}\ 4\pi)$ sign — the minor winding must wrap the fibre an
**even** number of times so the $\pm$ sign is single-valued under the $4\pi$ return, and the
**minimal** even wrap that is also $\ge2$ (C-β) is:
$$\boxed{p=2}\qquad\text{(C-γ, the }\mathbb{Z}_2\text{ spinor double cover)}$$

Why minimal-even and not any even? An even wrap $p=2k$ with $k\ge2$ is $k$ traversals of the $p=2$
double-cover — it re-enters the $\mathbb{Z}_2$ class with a redundant integer multiple, raising
the stored winding energy without changing the spinor sector (the $\mathbb{Z}_2$ quotient is
insensitive to $k$). By the minimum-reflection / least-stored-reactance principle (Axiom 3), the
substrate selects the **lowest-energy representative of each topological sector**, which is the
$k=1$, $p=2$ wrap. So $p=2$ is the unique stable minor winding for a spinor loop; $p=4,6,\dots$ are
excited (unstable / decay to $p=2$), and $p$ odd ($p=1,3,\dots$) does not close the $\mathbb{Z}_2$
sign single-valuedly (it would be a $2\pi$-periodic SO(3) object = a boson, not a charged-matter
fermion).

**Honest status of C-γ:** the *real-space* half (FM double cover → spin-½ → $\mathbb{Z}_2$) is
DERIVED and engine-corroborated. The *bridge* ("minor winding $p$ = Hopf-fibre wrap, so spinor
$\Rightarrow p=2$") is a **plausibility-strong cross-coordinate argument, NOT theorem-rigorous** —
it is exactly the kind of phase-space↔real-space identification A46 warns about. It is the
load-bearing and least-secure link in the whole gate. See §6.

### The odd-q corollary (falls out, no extra primitive)

With $p=2$ fixed by C-γ, C-α ($\gcd=1$) immediately forces $q$ **odd**: $\gcd(2,q)=1 \iff q$ is
odd. Even $q$ gives $\gcd(2,q)=2$ → a 2-component link (C-α violated). So:
$$\boxed{q\ \text{odd},\ q\ge3}\qquad\text{(C-α $\cap$ C-β at $p=2$)}$$
There is **no separate "odd-q primitive."** Odd-q is a *consequence* of the spinor constraint
$p=2$ intersected with the single-loop constraint. This is the cleanest part of the result: the
corpus's standing assertion "the ladder uses only odd q" is *correct and now derived* — but only
once $p=2$ is itself derived (C-γ), which is the step the corpus was missing.

---

## 4. Validate-on-known

**The rule, stated as a predicate:** $(p,q)$ is a stable charged-matter loop iff
$$\underbrace{\gcd(p,q)=1}_{\text{C-α}}\ \wedge\ \underbrace{p,q\ge2}_{\text{C-β}}\ \wedge\ \underbrace{p=2}_{\text{C-γ}}
\ \ \Longleftrightarrow\ \ \boxed{p=2,\ q\ \text{odd},\ q\ge3}$$

Code check: `src/scripts/vol_2_subatomic/coprime_odd_q_selection_rule_check.py`
(reads only the canonical crossing-number ladder; no CODATA / mass / α — value-echo immune).
Verbatim output (run on this branch):

**P1 — recovers every known stable assignment:**

| $(p,q)$ | $c$ | selected | particle |
|---|---|---|---|
| $(2,3)$ | 3 | ✅ True | electron |
| $(2,5)$ | 5 | ✅ True | proton (per-loop on Borromean $N=3$) |
| $(2,7)$ | 7 | ✅ True | $\Delta(1232)$ ladder |
| $(2,9)$ | 9 | ✅ True | $\Delta(1600)$ ladder |
| $(2,11)$ | 11 | ✅ True | $\Delta(1900)$ ladder |
| $(2,13)$ | 13 | ✅ True | $N(2190)$ ladder |

→ **P1 PASS.** The rule selects exactly the known $(2,q_{\text{odd}})$ set.

**P1-neg — forbids every canonical anti-case, with the correct reason:**

| $(p,q)$ | forbidden | failing constraint |
|---|---|---|
| $(1,1)$, $(1,3)$ | ✅ | C-γ ($p\ne2$) — unknot, no spinor cover |
| $(2,2)$, $(2,4)$, $(2,6)$ | ✅ | C-α ($\gcd(2,\text{even})=2$) — 2-component LINK |
| $(3,3)$ | ✅ | C-γ ($p\ne2$) |

→ **P1-neg PASS.** Note $(2,4)$ is correctly excluded *as a link* (C-α), which is the corpus's
standing "there is no stable $(2,4)$ torus knot" — now with the constraint named.

**Verdict: VALIDATE-ON-KNOWN = PASS** (P1 ∧ P1-neg ∧ P4 — P4 below). The rule recovers the
knowns and recovers the canonical exclusions. A rule that failed this would be wrong; this one
does not.

---

## 5. Predictions the rule FORCES (gate-only — NOT the full enumeration)

The full a-priori enumeration of all stable $(p,q,N,\chi)$ is **Lane D-full**, gated on this gate.
Here I report only the gate's *immediate* predictive content (P4 + the continuation), to show the
rule has teeth — i.e. it is not just a re-listing of the knowns.

**P4 — the rule EXCLUDES coprime knots a naive "any coprime knot" rule would admit.** The C-γ
spinor constraint ($p=2$) forbids the **entire $p\ge3$ tower** of coprime non-trivial knots. Over
the scanned window ($3\le p\le6$, $q\le11$), a naive rule admits **23** portraits; the spinor rule
admits only the **6** $p=2$ portraits, **forbidding 17** coprime knots:

$(3,4),(3,5),(3,7),(3,8),(3,10),(3,11),(4,5),(4,7),(4,9),(4,11),(5,6),(5,7),(5,8),(5,9),(5,11),(6,7),(6,11)$ — all FORBIDDEN.

This is the predictive payload: **there is no stable $(3,q)$ "first excited family" of particles.**
A framework with only coprimality + minimality (the corpus's standing position) cannot forbid
$(3,4)$ from being some heavier stable soliton; the spinor constraint does. If a stable
charged-matter particle were ever found whose phase-space portrait is genuinely $p\ge3$ (an object
needing a $4\pi/p$ cover, i.e. *not* spin-½), the rule is falsified. → **P4 PASS (has teeth).**

**Forward continuation the rule forces stable** ($c\ge21$ — the ladder D-full must continue):
$(2,21),(2,23),(2,25),\dots$ — all selected. The rule forces an *infinite* odd-q ladder; whether
each rung is *populated* by an observed resonance is the D-full mass/$J^P$ question, NOT this gate.
This gate only forces *which windings can be stable at all*.

**What this gate does NOT predict (deferred to D-full / flagged open):**
- The loop-count $N$ (lepton $N=1$ / baryon Borromean $N=3$) — that is an orthogonal axis
  (`topological-fractionalization.md`); this gate constrains the *per-loop* $(p,q)$ winding only.
  The tetra/penta-quark prime-$N$ test lives on the $N$ axis, which this gate does not touch.
- Strangeness-as-index — strange baryons are off-ladder and NOT natively derived
  (`torus-knot-ladder-baryons.md:11`); this gate does not close that GAP.
- The neutrino $c_1=5$ start (FLAG-1) — partially derived ($\Delta c=2$ from $\nu_{vac}=2/7$); the
  absolute start is still asserted. This gate's odd-q result is *consistent* with $c_1=5$ but does
  not derive the start.

---

## 6. THE CRITICAL GUARD — is the rule FORCED or FITTED?

Symmetric-standard + refute-by-default. The prize is a rule forced by substrate topology that
*then* selects the knowns. A rule reverse-engineered from the knowns is an echo with zero
predictive content. Brutally honest per-constraint adjudication:

| Constraint | Forced by a substrate primitive *independent of the particle list*? | Verdict |
|---|---|---|
| **C-α** ($\gcd=1$) | YES — integer-charge primitive (fractional twist severs the manifold) forces single-loop closure. Removing all particle identifications leaves C-α intact. | **FORCED (chord)** |
| **C-β** ($p,q\ge2$) | YES — topological-protection primitive (stable ⟺ non-removable winding). Particle-list-independent. | **FORCED (chord)** |
| **C-γ** ($p=2$) — real-space half | YES — FM double cover: a *charged-matter* loop is a fermion (charge on T2 micro-rotation grade), fermion ⟹ spin-½ ⟹ $\mathbb{Z}_2$ $4\pi$ cover. Engine-corroborated (`spin-doublecover-gate`). This does NOT reference which particle. | **FORCED (chord)** |
| **C-γ** ($p=2$) — the phase-space bridge | PARTIAL — "minor winding $p$ = Hopf-fibre wrap, so spinor ⟹ $p=2$" is a cross-coordinate identification (A46 risk zone). Plausibility-strong, theorem-pending. It is *motivated* by the FM cover, not *proven* from it. | **FORCED-pending (chord-candidate)** |
| odd-q | YES — pure corollary of C-γ ∩ C-α. No fitting. | **FORCED (chord)** |

### 6.1 The reverse-engineering stress test (Rule 11 trap, pre-registered §1.2)

The pre-registered trap: *does the derivation collapse if I delete the known-particle
identifications?* Walking it:

- Delete "electron = lightest lepton": C-α, C-β, C-γ all still stand (none invoked the electron).
  The rule still says $p=2,\ q$ odd. ✅ does NOT collapse.
- Delete "proton = $c=5$": the ladder $(2,q_{\text{odd}})$ is still forced. ✅ does NOT collapse.
- Delete *the entire particle list*: the rule still selects $\{(2,3),(2,5),(2,7),\dots\}$ as the
  stable set, because the three constraints are stated over substrate primitives (integer charge,
  protection, spinor cover), not over masses. ✅ does NOT collapse.

**This is the discriminating result.** Contrast with the corpus's *minimality* argument
("electron = $(2,3)$ because it's the smallest non-trivial coprime pair AND the lightest lepton") —
*that* argument DOES collapse without the particle identification: minimality only tells you which
knot is *smallest*, not which windings are *stable*. The corpus had a fitted selection (assign the
smallest knot to the lightest particle); this gate replaces it with a forced one (the spinor
constraint forbids $p\ne2$ for *any* charged-matter loop, observed or not).

### 6.2 Honest verdict

> **The coprime-odd-q selection rule is FORCED (chord-candidate), with one load-bearing
> theorem-pending link.**
>
> - C-α (single-loop), C-β (non-trivial), and the odd-q corollary are **FORCED chords** — standard
>   knot theory on substrate primitives, fully derived, particle-list-independent.
> - C-γ's **real-space half** (charged-matter ⟹ fermion ⟹ $\mathbb{Z}_2$ spinor cover ⟹ even
>   minor winding, minimal $=2$) is **FORCED and engine-corroborated**.
> - C-γ's **phase-space bridge** (minor winding $p$ *is* the Hopf-fibre wrap) is the one
>   **theorem-pending** link — plausibility-strong, A46-flagged. It is NOT reverse-engineered from
>   the particles (the FM cover is derived independently), but it is NOT yet theorem-rigorous.
>
> The rule is therefore **NOT a fit.** It does not re-encode the known assignments; it forbids an
> entire $p\ge3$ tower the knowns never needed forbidden, and it survives deletion of the particle
> list. The gate's verdict is **chord-candidate, conditional on closing the one bridge.**

---

## 7. Scope, open gaps, recommendation

### 7.1 Consistency-vs-emergence classification (per `consistency-vs-emergence`)

This gate is a **structural/topological selection rule**, not a numerical prediction — no CODATA
value is read or matched (value-echo immune by construction; the code reads only integer crossing
numbers). On the 4-class axis:

- **The odd-q recovery** (matching the corpus's standing $(2,q_{\text{odd}})$ ladder) is a
  **CONSISTENCY result** — it reproduces an already-asserted corpus structure, now with the
  constraint derived rather than asserted.
- **The $p=2$ forcing + the $p\ge3$ exclusion tower** is the **EMERGENCE-class** content: the
  substrate spinor primitive forbids configurations the framework never put in by hand. This is the
  AVE-distinct payload (the chord), *conditional on the C-γ bridge closing*.

Honest headline: **do NOT headline this as a closed emergence result** while the phase-space bridge
is theorem-pending. Headline it as: *"the odd-q ladder is recovered as a derived corollary of a
spinor selection rule; the rule's $p=2$ forcing is a chord-candidate with one theorem-pending
cross-coordinate link."*

### 7.2 Open gaps (flag-don't-fix)

1. **C-γ phase-space bridge (load-bearing, theorem-pending).** The identification "minor winding
   $p$ = Hopf-fibre wrap count" needs a rigorous proof that the Clifford-torus poloidal winding
   *is* the $SU(2)\to S^2$ fibre wrap, so spinor $\Rightarrow p=2$ is theorem-forced not
   plausibility-strong. This is the single thing standing between "chord-candidate" and "chord."
   It is the same class of phase-space↔real-space embedding-selection gap already tracked in the
   corpus (cf. Q-EMBED-SEL-1 $R\cdot r=1/4$ and the ropelength-minimality embedding-selection
   framing, `closure-roadmap:93`) — **surfacing the parallel, not asserting they are the same gap.**
2. **Loop-count $N$ axis untouched.** This gate constrains per-loop $(p,q)$; the tetra/penta-quark
   prime-$N$ test (D-full) lives on $N$, which needs its own gate (why $N=1$ lepton / $N=3$
   Borromean baryon are stable, why $N=2$ is a medium resonance not a particle —
   `closure-roadmap:147`). **D-full needs an $N$-axis gate in addition to this $(p,q)$ gate.**
3. **Strangeness + mesons** remain off-ladder, NOT natively derived (`torus-knot-ladder-baryons.md:11`).
   This gate does not close that GAP and does not claim to.
4. **The $p=4,6,\dots$ "excited/decay" claim** (that even-$p$ wraps are unstable excited states
   decaying to $p=2$, not links) rests on the Axiom-3 least-stored-reactance selection. That is
   argued, not engine-demonstrated. A 2-soliton / decay driver (Lane A territory) could test it.

### 7.3 Recommendation on unblocking D-full

**RECOMMEND: unblock Lane D-full for the $(p,q)$-winding axis, with two explicit gates carried
forward as caveats**, NOT a clean green:

- ✅ The validate-on-known PASSED — the rule recovers all known $(2,q_{\text{odd}})$ assignments and
  all canonical exclusions, with nontrivial exclusion teeth (forbids 17 coprime $p\ge3$ knots).
- ✅ The rule is FORCED (chord-candidate), survives the reverse-engineering stress test, and is NOT
  a re-encoding of the knowns.
- ⚠️ **Carry-forward caveat 1:** the C-γ phase-space bridge is theorem-pending. D-full enumeration
  results on the $(p,q)$ axis are *conditional* on this bridge; any forward particle prediction must
  carry the caveat until the bridge closes.
- ⚠️ **Carry-forward caveat 2:** D-full's strangeness-as-index and tetra/penta-quark prime-$N$ tests
  need a **separate $N$-axis gate** — this gate does not provide it. D-full should NOT treat the
  prime-$N$ taxonomy as gated-open by *this* result.

This is a **Grant adjudication point**: unblock D-full-$(p,q)$ now (caveated), or hold D-full
entirely until the C-γ bridge is theorem-closed. The implementer recommendation is the former
(the validate-on-known + the exclusion teeth are strong enough to make the $(p,q)$ enumeration
bankable-with-caveat), but this is a framing call and is surfaced, not decided, here.

---

## 8. Artifacts

- This doc: `research/2026-06-23_coprime-odd-q-selection-rule_derivation.md`
- Code check: `src/scripts/vol_2_subatomic/coprime_odd_q_selection_rule_check.py` (VALIDATE-ON-KNOWN = PASS)
- Load-bearing cites (verified on branch HEAD): `torus-knot-uniqueness.md` (clm-8c3yhs),
  `topological-fractionalization.md` (clm-mnb3lt/clm-67jn9o), `finkelstein-misner-spin-half-derivation.md`
  (clm-salw2h), `research/2026-06-19_spin-doublecover-gate_result.md`, `resonant-lc-solitons.md:91`,
  `constants.py:913`, `def-kn0t01` (vocabulary-register).

**Disposition:** for orchestrator audit + Grant merge pending. No corpus/KB leaf edits in this PR —
this is a research doc + driver only; KB-leaf propagation (if the chord-candidate is ratified) is a
gated follow-on the auditor lands, not this lane.

