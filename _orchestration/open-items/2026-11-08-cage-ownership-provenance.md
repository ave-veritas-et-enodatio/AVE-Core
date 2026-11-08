---
id: cage-ownership-provenance
title: "Cage ownership resolved by Grant 2026-11-08 — two walls at two energies, neither record wrong; propagate the carve and strike one misattribution"
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

**What it does NOT close — still open, and the only question left for Grant:**
the nesting language. `resonant-lc-solitons.md:140` says the A1 mass *"sits
inside"* the T2 boundary; `:145`, four lines down in the same resultbox, says
*"two orthogonal self-confining sectors … **NOT a nesting**."* Under two-walls
both sentences can be true — the mass rests against the lower wall without being
*nested in* a structure the other sector owns — but the two words still
contradict on the page and one of them needs rewording. **Wording is Grant's;
the two-walls picture does not settle which word goes.**

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
- Fix `src/ave/topological/graded_vacuum_network.py:425,:514` — the
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
- **A prior challenge to this exact fork was already withdrawn once**, on
  2026-08-24, on the stated ground *"That premise is inverted against SOLID
  canon"* + *"def-vyvsn1 (SOLID)"* (`four-regimes.md:62-89`). Deferring to the
  side under dispute is how that one died.

## Currency

Re-verified at `7bbf3c5e` (2026-11-07): the five files above have **zero
commits** across 181 of `main` since the 2026-09-06 analysis pin
`6b8b49a0`. The collision is live exactly as recorded and nothing here has
drifted.

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
