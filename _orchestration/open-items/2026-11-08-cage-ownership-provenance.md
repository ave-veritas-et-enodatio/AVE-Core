---
id: cage-ownership-provenance
title: "Cage ownership — Grant 2026-11-08 ruled two walls, then HELD BY T2; a second amplitude-level collision found while recording it is still his, and may require amending the ruling"
status: OPEN
owner: grant
opened: 2026-11-08
source: manuscript/ave-kb/common/vocabulary-register.md
anchor: 'the single-electron confining $\Gamma=-1$ TIR cavity self-creates here'
---

**Tracking row only. Nothing here adjudicates physics.** It records a collision,
its provenance, and the one question that collapses it.

## The collision, sixteen lines apart in one file

`manuscript/ave-kb/common/vocabulary-register.md`:

- **def-cf1srf** (*confinement surface*), `status: proposed — status OPEN: the
  shape-forcing CHAIN is not derived` — its `open-ambiguity-flag` reads: *"The
  confinement surface is the **A1 MASS wall** ($Z_{bulk}\to0$, the
  impedance-short $\Gamma=-1$). It must NOT be re-collided with the
  $\Gamma_{spinor}=-1$ topological $2\pi\to4\pi$ stability wall of the T2
  micro-rotation sector … the confinement surface is the mass one only."*
- **def-vyvsn1** (*V_yield / V_snap*), `status: SOLID — adjudicated (Grant
  2026-06-30)` — *"$V_{yield} = \sqrt{\alpha}\cdot V_{snap} \approx 43.65$ kV =
  the **transverse Cosserat ($T_2$) self-trap wall** … and the single-electron
  confining $\Gamma=-1$ TIR cavity **self-creates here**."*

Side B is asserted at full strength in three further live leaves, including
`electron-identification.md:32` — **Property 3 of the canonical four-property
electron definition**, banner-affirmed *"Property 3 STANDS"* — and
`hollow-vortex-binding.md:20`, *"EXISTENCE / CONFINEMENT (SOLID, already canon
on main) … an independent, sim-surviving binder."*

## Three Γ=−1 objects, not two — the guard does not cover the collision

def-cf1srf's guard excludes exactly one thing: the T2 **topological**
$2\pi\to4\pi$ spinor wall (a class-invariant SU(2) sign, no threshold, confines
nothing). def-vyvsn1's wall is the T2 **Axiom-4 saturation** self-trap at
$V_{yield}$ — a 43.65 kV amplitude crossing with an impedance consequence.
Those are categorically different objects, so **the guard names (2) while
def-vyvsn1 asserts (3), and neither node's guard fires.** A fourth object
exists: the Meissner $\Gamma_{EM}=-1$ ($\mu_{eff}\to0$), which
`node-up-small-large-signal.md:285-287` separates from (3) explicitly — *"the
two are bridged by a transducer, not a direct wire."*

## Provenance — verified by `git show`, and it is the reason this is Grant's

**The confining-cavity clause pre-dates the 2026-06-30 ruling by six weeks.**

| | commit | what happened |
|---|---|---|
| 1 | `ee2dc5a9` 2026-05-16 | born in `electron-identification.md:32` (Property 3) |
| 2 | `73a78a82` 2026-06-24 | enters def-vyvsn1 attributed **"per the #416 ruling"**, in a node the same document declares un-canonizable |
| 3 | `00f2bfdc` 2026-07-01 | **the hardening** — the same edit that flips `proposed` → `SOLID` re-stamps the attribution **#416 → "Grant 2026-06-30"**, upgrades *"wall is here"* to *"cavity self-creates here"*, and promotes it from tail parenthetical to the head of the node. The commit message discloses none of it. |

What the 2026-06-30 ruling was *asked* was narrower. The frozen criterion, before
any derivation line —
`research/2026-06-30_electron-portmap-derivation_prereg_FROZEN.md:173`:
*"FORK-FOR-GRANT if … depends on an un-adjudicated **grade-attribution** of
`V_yield`."* **The string "confin" does not occur in that fork clause.**

**But both sides nonetheless trace to Grant's own hand, thirteen days apart —
and this is what makes it his call and not a lane's:**

- **2026-06-17, `5d83b67c`** — author **and** committer `Grant-L`, directly.
  Subject: *"Rule-12 demote stale 'confinement via magnetic branch' prose
  (PR#260 B3-DEGENERATE)."* This is the commit that put the A1-mass-cage
  sentence into `master-equation.md:106`. Every other commit in the chain is
  authored `AVE Vol6 D2 Implementer`. **It is not in PR #260's diff** —
  `git show --stat 04bda99b` is 7 files and `master-equation.md` is not among
  them.
- **2026-07-01 01:17:57, `2ff5ff41`** — `resonant-lc-solitons.md:140` gains
  *"**RESOLVED (Grant 2026-06-30, reading (ii)).** … The $\Gamma=-1$ confinement
  cage is the transverse-$T_2$/charge self-trap at $V_{yield}$; the A1 mass sits
  inside it sub-saturated."* Grant merged PR #441 eleven minutes later
  (`e1e14572`, 01:28:58), so he was live. **No verbatim words of his survive for
  2026-06-30 in any reachable store**, and the fork that record answers was
  framed as an A1-core *amplitude* question (√α vs A→1) with cage ownership
  riding on both horns.

## RESOLVED 2026-11-08 (Grant) — two walls at two energies

**Grant's call, in chat:** both walls are real and they sit at different
energies. The electron operates at $A=\sqrt\alpha$, which is **sub-saturated on
A1** ($S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$), so at the operating point the
A1 wall is **not engaged** — it is $1/\sqrt\alpha\approx11.7\times$ up at
$V_{snap}$, where pair nucleation lives. The boundary the electron actually rests
against is the T2 self-trap at $V_{yield}$.

**So neither record was wrong, and nothing is superseded.**
`master-equation.md:106` names the **A1 wall** — real, at $V_{snap}$.
`resonant-lc-solitons.md:140` names **which wall the electron leans on** — T2, at
$V_{yield}$. They were read as competing claims about one wall; they are claims
about two.

**def-vyvsn1 already said this and nobody joined it up.** Its own
adjudicated-meaning: *"**The A1 mass channel does NOT saturate at $V_{yield}$**
— it saturates at the $1/\sqrt\alpha\approx11.7\times$-higher $V_{snap}$."*

**The carve is Grant's own, from #260, extended from the mass sector to the
cage** — `research/2026-06-15_wall-branch-fork_result.md:42`:
*"**Provenance≠state (Grant's refinement):** … Both unretracted, both right *in
their frame*. **Not a contradiction — two frames of one mode.**"*

**And A1 ⊥ T2 is not threatened.** Two sectors each having their own saturation
wall is orthogonality working, not breaking. A cross-wire would require one
sector's wall to **constitute** the other's quantity, and #260 already ruled that
out: *"the wall **confines** the A1 mass, it does not **constitute** it."*

**GRADE: chat-walk.** This is Grant's physical ruling given in conversation. It
has **not** had an adversarial pass, so it is not SIGNED by the house standard
(adversarial review **plus** Grant review). Propagate it as a Grant ruling;
do not stamp it SOLID on this row's authority alone.

**What this closes:** the adjudication. There is no longer a fork to pick. What
remains is propagation and one real defect.

**RULED TOO, 2026-11-08 (Grant): HELD BY T2.** At the operating point the A1 mass
is **not** self-confined — it is held by the transverse-$T_2$/charge self-trap
boundary at $V_{yield}$. `resonant-lc-solitons.md:140` is therefore correct as
written, including *"which is **why** it binds"*.

**Two clauses are now false, and one of them is not in this file.**

- `resonant-lc-solitons.md:145` — *"two orthogonal **self-confining** sectors
  (A1-mass + Cosserat-charge), **NOT a nesting**"*. A1 is not self-confining at
  $A=\sqrt\alpha$; its own wall is $11.7\times$ up and unengaged.
- `node-up-small-large-signal.md`, the orthogonal-grades block — *"the electron's
  two-natured structure is **two orthogonal self-confining sectors** (A1-mass +
  Cosserat-charge), **NOT** a charge-holds-mass nesting."* **"Held by T2" IS a
  charge-holds-mass nesting**, so that clause does not survive the ruling.

**The carve that keeps the rest of that block — apply it, do not delete the
block.** Its *argument* is narrower than its *conclusion*. The argument is
*"the **EM $\mu$-sector (Meissner)** has **no handle on the dilatation (mass)
port**"*, and the reading it forbids is specifically *"the $(2,3)$ micro-rotation
**Meissner**-confines the A1 mass"*. That **survives**, because the $T_2$
self-trap wall is **mechanical** ($Z_{shear}\to0$), not the EM $\mu$-sector —
and the same block says the two are *"bridged by a transducer, NOT a
$\mu$-on-$Z_{shear}$ direct wire."*

So: **charge-holds-mass via the mechanical self-trap is RULED TRUE;
Meissner-confines-mass stays forbidden/falsified.** What needs rewording is only
the broad clauses that collapse those two into one prohibition. The narrow
Meissner verdict, PR#260's mass=A1, and $A1\perp T2$ at the DOF level all stand
untouched.

**Still Grant's, and the last thing on this row:** whether *"nesting"* is the
word he wants. He ruled the mass is **held by** the $T_2$ wall; *"sits inside"*
and *"nesting"* are stronger spatial words for the same relationship. The physics
is ruled; the noun is not. **Do not pick it for him.**

## SECOND COLLISION, found while recording the ruling — amplitude, not ownership

**This one is not wording.** Verifying "held by T2" against the leaves turned up a
live corpus split on **what strain the A1 port actually rides at**, and one side of
it carries a ratified sector-attribution. Found 2026-11-08 by reading the leaves
after the ruling; it was not known when the first half of this row was written.

**Side A1-IS-SUB-SATURATED** — agrees with Grant 2026-11-08, and carries his own
2026-06-30 banner:

- `nonlinear-vacuum-capacitance.md:18`, under **Grade-fork RESOLVED = T2 (Grant
  2026-06-30)** — *"a standing electron's A1 mass core operates at strain
  $A=V_{yield}/V_{snap}=\sqrt\alpha\approx0.085$ — deeply **sub-saturated**
  ($S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$), which is *why* it binds (the
  $S\to0$ varactor runaway never fires on the mass channel)."*
- `nonlinear-vacuum-capacitance.md:40` — the table row at $\sqrt\alpha\approx0.085$:
  *"$V_{yield}$ = T2 self-trap wall; electron A1-core operating point"*.
- `vocabulary-register.md:757` (def-vyvsn1's own flag) — same consequence, *"which
  is why the mass channel does not run away."*

**Side A1-RIDES-AT-SATURATION** — three sites, one inheriting from the next:

- `cvr-dc-operating-point.md:49` — *"The electron's reflective wall
  ($|\Gamma|^2=1-\alpha$ …) sits at a residual $A_\star$ where
  $\sqrt{S_\star}\approx\alpha/4$ — i.e. **essentially at saturation**
  ($A_\star\to1$) with a tiny non-zero residual impedance that IS the radiative
  leak."*
- `cvr-dc-operating-point.md:51` — the **★ Keying disambiguation (KEEP-BOTH;
  ruling 2026-07-06/07, PR #562/#558; propagated 2026-07-13)** banner on that
  sentence: *"the $A_\star\to1$ saturation of the divergent varactor is the
  **$V_{snap}$ (longitudinal-$A_1$) wall**, NOT the transverse-$T_2$ '$V_{yield}$
  yield onset' the sentence also names ($A_\star=V/V_{snap}$, not $V/V_{yield}$)…
  the conflated wording is preserved KEEP-BOTH."*
- `node-up-small-large-signal.md:358-359`, a Resultbox — *"The **MASS port** (A1
  dilatation $\to Z_{\mathrm{bulk}}$, mechanical) is biased to $A\to1$ (the
  $V_{snap}$ rail, $Z_{bulk}\to0$, $\Gamma=-1$ cage); the **CHARGE port** … is
  biased to $V_{yield}$ (the self-trap onset)."* And `:375-376` names
  `cvr-dc-operating-point.md:43-45` as the canonical home of that bias step — so
  node-up **inherits** the $A\to1$, it does not assert it independently.

**The two numbers do not reconcile as "two frames of one mode."**
$\sqrt{S_\star}=\alpha/4 \Rightarrow S_\star=\alpha^2/16 \Rightarrow
A_\star=\sqrt{1-\alpha^4/256}\approx 1-\alpha^4/512$ — saturation to four powers of
$\alpha$. Against $A=\sqrt\alpha=0.0854$, $S=0.996$. **node-up:358 is the strongest
statement in the corpus of exactly the thing the 2026-11-08 ruling ruled against:
it puts $Z_{bulk}\to0$ and the $\Gamma=-1$ cage on the A1 port at its own rail,
which is A1 self-confinement.**

**What the 07-06/07 ruling does and does not cover — do not overstate this.** Its
job was **normalization**: which scale $A_\star$ is measured against. It ratifies
that *that* saturation event belongs to the **A1/$V_{snap}$** sector. It does
**not** re-derive the claim that the electron *sits* there — that is body prose
older than the banner, which the banner explicitly **preserves** rather than
re-establishes. So this is a ratified sector-attribution sitting on an
un-re-derived amplitude claim, **not** a head-on ruling-vs-ruling conflict.

**Two candidate reconciliations. Neither is recorded anywhere in the corpus.**

1. **CORE vs WALL (a spatial profile).** The A1 strain runs from $\sqrt\alpha$ in
   the core to $\approx1$ at the reflective surface, and the two sides are each
   right about a different *place*. If this is the answer then **part of the
   2026-11-08 ruling needs amending**: the A1 wall is **not** "unengaged, 11.7×
   up" — it is engaged, at the surface — and node-up:358's only defect is calling
   a wall location a *port bias*.
2. **$A_\star$ IS BACK-DERIVED, NOT A BIAS.** $\sqrt{S_\star}\approx\alpha/4$ is
   reverse-engineered from the reflectivity target $|\Gamma|^2=1-\alpha$ (itself
   an $\alpha$-echo), making it a fitted residual impedance rather than an
   independent statement that the A1 port rides at its rail. If this is the answer
   then held-by-T2 stands unamended and `cvr-dc-operating-point.md:49` plus
   `node-up:358-359` both need rewording.

**GRANT'S, and bigger than the nesting noun.** It decides whether the 2026-11-08
ruling is complete or needs an amendment, and it is an amplitude question, which is
his call and not a lane's.

**MUST-NOT, until he rules:** do not touch `node-up-small-large-signal.md:358-359`,
`cvr-dc-operating-point.md:49`, or its `:51` KEEP-BOTH banner. Do not "harmonize"
$A_\star$ and $\sqrt\alpha$ by picking one. Do not treat the $S^{0.25}$ exponent
defect flagged at `cvr-dc-operating-point.md:40-45` as part of this — it is a
separate surfaced-not-fixed physics-review item and it moves $\Gamma$ magnitudes,
so it may interact, but it is not this collision.

## Why it matters beyond bookkeeping

The T2-holds-A1 reading is structurally Poincaré's move — a cohesive boundary
supplied by a sector other than the one owning the confined quantity — and it is
the side that propagated outward as SOLID. The corpus already owns the
consequence: `manuscript/ave-kb/common/physics-lineage-map.md` K8 — *"if the
K=2G import never becomes a derivation, **AVE's stabilizer is a modern Poincaré
stress** — the corpus's own words."* K=2G was ruled GR-imported at PR #261, so
the antecedent holds. And
`research/2026-08-14_electron-identity-checkpoint1-walk_RECORD.md:51` (SIGNED
fence): *"Corpus split: **this is Poincaré 1905** (cohesive stress named, not
derived)."*

## What a lane does now (all of it unblocked by the 2026-11-08 ruling)

- **Propagate the two-walls carve** into `def-cf1srf`, `def-vyvsn1`,
  `master-equation.md:106` (surface note, never a rewrite — **Grant authored
  that sentence**) and `resonant-lc-solitons.md:131`, so the two walls are named
  as two and the operating point is stated.
- Strike the `00f2bfdc` misattribution and restore the clause's `#416` /
  Grant-2026-06-24 / `electron-identification.md` §1.3 descent. def-vyvsn1's
  SOLID stamp survives on its actual scope.
- Add a dated **surface note** (never a rewrite) at `master-equation.md:106`
  recording that the sentence post-dates #260's merge by two days and is in a
  file #260's diff never touched. **Note: Grant authored it — say so.**
- Repair stale pins: `nonlinear-vacuum-capacitance.md:16`→`:18`;
  `resonant-lc-solitons.md:127`/`:136`→`:131`/`:141`.
- Fix `src/ave/solvers/graded_vacuum_network.py:425,:514` — the
  `best is None` branch bypasses the `core_frac` gate and returns `ok=True` for
  a fully port-localized mode.
- `def-cf1srf`'s root cite is mis-attributed: it grounds *"the $\Gamma=-1$ TIR
  condition itself is canonical"* on `clm-kezk9z`, whose actual Specific Claims
  are $Z_0$ from the discrete LC ladder and gravitational stealth — **no
  electron-confinement content.** Both sides lean on this cite.

## What a lane must NOT do

- **Do not touch** `resonant-lc-solitons.md:140` or `:141`. Grant-attributed.
- **Do not assert** which sector owns the cage, in either direction.
- **Do not declare** PR #260 superseded or reaffirmed.
- **Do not dispatch the sim work first.** The isolation solver cannot support
  side B by construction (one scalar dilatation grade, no terminable Cosserat
  grade), and a prior lane's headline number — *"A=√α: core_frac 0.0000,
  Q 6.704"* — **does not reproduce**: it is an artifact of the shift-invert guess
  passing through the selection bug above. Do not let it reach Grant as evidence.
- **The second collision has its own must-nots** — see that section. In short:
  do not touch `node-up-small-large-signal.md:358-359`,
  `cvr-dc-operating-point.md:49`, or its `:51` KEEP-BOTH banner, and do not
  harmonize $A_\star$ with $\sqrt\alpha$ by picking one.
- **A prior challenge to this exact fork was already withdrawn once**, on
  2026-08-24, on the stated ground *"That premise is inverted against SOLID
  canon"* + *"def-vyvsn1 (SOLID)"* (`four-regimes.md:62-89`). Deferring to the
  side under dispute is how that one died.

## Currency

Re-verified at `7bbf3c5e` (2026-11-07): the five files above have **zero
commits** across 181 of `main` since the 2026-09-06 analysis pin
`6b8b49a0`. The collision is live exactly as recorded and nothing here has
drifted.

**The second collision's three leaves, verified separately at `origin/main`
= `73e324b5a` (2026-11-08)** — they are not among the five above and were
not covered by that check. Last touch on `main`:
`node-up-small-large-signal.md` `8f75ca5e9` (2026-08-12),
`cvr-dc-operating-point.md` `8f268747e` (2026-08-20),
`nonlinear-vacuum-capacitance.md` `1edd6c582` (2026-07-02). All three predate
the 2026-11-08 ruling by months, so every clause quoted from them is current
`main` state, not a stale read. The $A_\star$ arithmetic was recomputed rather
than copied: $\sqrt{S_\star}=\alpha/4 \Rightarrow 1-A_\star =
5.5386\times10^{-12}$ against $\alpha^4/512 = 5.5385\times10^{-12}$, and
$S(\sqrt\alpha)=\sqrt{1-\alpha}=0.99634$.

Fuller context, including the discriminator set and the blast radius in both
directions, is in a handoff brief in the private channel repo
(`Grant-L/the-electron-plumber`,
`_orchestration/2026-09-06_confinement-wall-sector-fork.md`). **This row is
self-contained on every AVE-Core fact it states** — nothing above requires that
brief to verify.

**History:** surfaced 2026-09-06 by episode-001 research into whether AVE pays
Poincaré's cohesion debt. A first attempt landed as content PR #1040, which was
the wrong artifact from the wrong session and is **CLOSED 2026-11-08** — see its
closing comment. This row is what should have been written then.
