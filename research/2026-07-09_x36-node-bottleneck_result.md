# RESULT — X36: node-shunt characterization — **ceiling = the installed node resonance; Branch P iff series-anti-resonant (mass-in-mass) node topology at η=1; X33 fork SHARPENED, not collapsed**

**Date:** 2026-07-09 · **Branch:** `analysis/x36-node-bottleneck` (off main @ ba662d57, incl. merged #611) · **Task:** X36 (Grant-fired, the D-I discriminator)
**Prereg (FROZEN):** [`research/2026-07-09_x36-node-bottleneck_prereg_FROZEN.md`](2026-07-09_x36-node-bottleneck_prereg_FROZEN.md)
**Derivation:** [`research/2026-07-09_x36-node-bottleneck_derivation.md`](2026-07-09_x36-node-bottleneck_derivation.md)
**Driver:** [`src/scripts/vol_1_foundations/x36_node_bottleneck.py`](../src/scripts/vol_1_foundations/x36_node_bottleneck.py) (extends `x33_clock_architecture.py`, Rule 14)
**Data:** [`research/2026-07-09_x36-node-bottleneck_result.json`](2026-07-09_x36-node-bottleneck_result.json) · **Figure:** `src/scripts/vol_1_foundations/_output/x36_node_bottleneck.png`
**Class (consistency-vs-emergence):** **CONSISTENCY / characterization.** A math+numerics typing of the substrate's
own node architecture. ω_C = c₀/ℓ_node is an **IDENTITY** (`OMEGA_C`; ℏω_C = m_e c² exactly); R = √2 is a Class-B
manifestation of the √eig↔arccos velocity conventions; ρ* is GR-imported (ν=2/7). **No CODATA on any verdict path;
this is an exact-spectrum computation, not an empirical vote.**

---

## ⚠ CORRECTION / DEMOTION-TO-CHARACTERIZATION (2026-07-09, post adversarial review of PR #613)

The adversarial review of PR #613 returned **BLOCKED: 17/17 findings CONFIRMED, 0 refuted (3 CRITICAL)**. This
document is **demoted from a verdict to a conditional characterization**. The original run's *verdict* dies; its
*content* survives as fork cartography. **No new physics claim is made here.** KEEP-BOTH — the superseded verdict
sentences are quoted verbatim below and preserved in git; they are not silently erased, only demoted.

**Restated verdict (replaces "Branch P, decisively and from first principles"):**

> **CONDITIONAL CHARACTERIZATION.** Branch P holds **iff ALL THREE** un-derived model choices are made together:
> **(1)** the node shunt is **series anti-resonant** (mass-in-mass / locally-resonant-metamaterial topology), **AND
> (2) η = 1** (every bit of node inertia is the tank, no bond-rigid bypass), **AND (3)** the tank is anchored at
> **ω_C**. Flip any one → a different branch: a **parallel-LC band-pass** shunt (equally passive/lossless/KCL-consistent)
> is transparent at ω_C and does **NOT** pin → **Branch L**; **any η < 1** (even η = 0.999) → the full-spectrum ceiling
> lifts ≈ the bare continuum (21.5× vs 22.4×) → effectively **Branch L**; the tank anchored at **any** frequency ω_r
> pins the ceiling at **ω_r**, not at a derived rate (placement probe: ω_r ∈ {0.5, 1.0, π√3, 10}·ω_C → ceiling
> {0.500, 1.000, 5.428, 9.918}). **The ceiling is wherever the tank is installed.**

**Reconciliation with the prereg's own alternative (`prereg_FROZEN.md:85`):** the prereg *itself* lists "(b) a
**parallel-LC band-pass** shunt (transparent AT ω_C — would NOT pin, → Branch L)" as an equally passive / lossless /
KCL-consistent construction. That alternative is the direct contradiction of derivation.md:30's claim that the
series (mass-in-mass) topology is **forced** by shunt KCL + losslessness. **The topology choice IS the P-vs-L
selector — it is a modelling choice, not a forced consequence.** Branch P was mathematically entailed by the frozen
model choice (series notch + η=1 + anchor=ω_C) combined with the merged X33 continuum inputs **before any X36 code
ran**; the adjudication rule (lift ratio < 1.3 → P) could not have fired L or M given those frozen choices.

**Superseded verdict sentences (KEEP-BOTH, quoted verbatim, now demoted):**
- ~~"Answer: YES — Branch P (NODE-PINS), **decisively and from first principles**."~~ (TL;DR §0)
- ~~"The √(shunt) normalization and the mass-in-mass topology are **forced** by shunt KCL + losslessness"~~ (derivation.md:30)
- ~~"the node-tank predicts the vector band tops at the node rate **m_e c² = 0.511 MeV**"~~ (§7.2 / derivation.md:98) — ω_C
  is the definitional calibration anchor (`OMEGA_C`; ℏω_C ≡ m_e c²). This is **calibration-in, calibration-out**, not
  a prediction (consistency-vs-emergence: identity, not emergence).
- ~~"the X33 in-engine-undecidable architecture fork **collapses** under the Axiom-1 η=1 node"~~ (§0 / §7.1 / derivation.md:110)
- ~~"the bond-tick walk is the discrete-tick **shadow** of the continuous node-tank bottleneck"~~ (§0 / §4 / derivation.md:109)

**What SURVIVES (fork cartography, characterization-class):**
1. the reciprocal bottleneck **FORM** `1/ω² = 1/Λ + 1/ω_C²` as the standard **locally-resonant-metamaterial
   anti-resonance** law (a mass-in-mass series notch), local to the chosen topology;
2. the **placement probe**: the coupled ceiling equals the installed anchor ω_r (a general methodological caution —
   the engine returns whatever the node model installs);
3. the **η-singularity map**: Branch P is a **singular point at exactly η = 1**; any η < 1 lifts ≈ bare continuum.

**What DIED:** "derived from first principles"; "collapses X33"; the "m_e c² prediction" language; "forced by KCL +
losslessness"; the "discrete-tick shadow" narrative.

**Process caveat (freeze unverifiable):** prereg + driver + result + verdict landed in a **single commit** with
"frozen expectations" identical to the results to 5 digits. The freeze **cannot be claimed** as pre-run; the §5 /
prereg §5 "frozen expectations" are demoted to **post-hoc analytic cross-checks**. See §8.

---

## 0. TL;DR — the verdict

**Grant's D-I question:** does the CONTINUOUS-time network, with the node's own shunt LC tank modelled explicitly,
pin the multi-channel ceiling at the node rate? **Answer (demoted, see the correction banner above): CONDITIONAL —
the ceiling is pinned at whatever resonance the node shunt is INSTALLED at, and only under a specific 3-choice model
(series anti-resonant topology AND η=1 AND anchor=ω_C). This is a characterization of the chosen node model, not a
derivation of effective synchrony.**

- Axiom-1's node is modelled as an **intrinsic LC tank** (a channel-shared shunt resonator). One passive/lossless
  choice — the **series anti-resonant (mass-in-mass)** shunt — presents the bonds a frequency-dependent effective
  mass diverging at its resonance, giving the **reciprocal bottleneck FORM `1/ω² = 1/Λ + 1/ω_C²`** (the standard
  locally-resonant-metamaterial anti-resonance law). This FORM is **local to the chosen topology**, NOT forced:
  `prereg_FROZEN.md:85` lists an equally passive/lossless/KCL-consistent **parallel-LC band-pass** shunt that is
  transparent at ω_C and does **not** pin (→ Branch L). The topology choice IS the P-vs-L selector.
- With the series-notch topology at **η = 1** and the tank **anchored at ω_C**, the coupled ceiling sits at ~1 ω_C
  for every ρ* (node-tank top **0.9608 → 0.9921 → 0.9992 → 0.99992 ω_C**, lift ratio **1.041×**), vs the bare
  continuum's **22.37×**. But the **placement probe** shows this ceiling **= the installed anchor**: a tank at
  ω_r ∈ {0.5, 1.0, π√3, 10}·ω_C gives ceiling {0.500, 1.000, 5.428, 9.918}. The engine returns whatever the node
  model installs — it does not derive the anchor.
- The **η = 1 pin is a singular point**: at η = 0.999 the full-spectrum ceiling already lifts **21.5×**
  (indistinguishable from the bare continuum's 22.4×), because a lifting upper polariton branch reappears for **any**
  η < 1. Branch P exists only at exactly η = 1.
- **⇒ CONDITIONAL CHARACTERIZATION.** X33's in-engine-undecidable ruling **STANDS and is REINFORCED**: X36
  demonstrates the continuous engine returns whatever node model is installed, so it cannot by itself adjudicate the
  architecture fork. The physical content is a **3-axis question** — (node shunt topology: series-anti-resonant-notch
  vs parallel-band-pass-transparent) × (η partition) × (anchor frequency) — **PENDING-GRANT-WALK**, not a collapse.

**Gate status (demoted, see §1 and §8):** the 6 gates are internally consistent but several are **self-comparisons,
not independent checks** — G2's "recovers X33's 22× lift exactly (0.0 rel err)" is a **bit-level self-comparison**
(the same `tank_omega2_eta1` function evaluated with ω_C→∞ against its own bare input, MAJOR-10); the original G6
D-independence loop evaluated the **same constant** at both Λ samples (CRITICAL-3 no-op); G1 as shipped checked
tank/bare = 1 at ρ*, not the frozen √2 slope clause (MINOR-8/13). The pin's mechanism is named algebraically
(m_eff(ω) → ∞ at the anchor ⇒ `1/ω² = 1/Λ + 1/ω_C²`; stiffness locked out) — that FORM survives; its *derivation
from first principles* does not (COMMIT-2 repairs the gates; see §1).

**One flag for Grant (do not silently reconcile):** with the tank ANCHORED at ω_C, the ceiling sits at ~1 ω_C
(= the definitional anchor, ℏω_C ≡ m_e c²; **this is calibration-in, calibration-out, NOT a prediction**), a factor
π√3 below #604's time-stepped bond-tick scalar top π√3 ω_C. But the placement probe (banner above, §2) shows the
ceiling would sit at π√3 ω_C **if the tank were anchored there** — so the "two-clock tension" **REDUCES to the
un-derived anchor/topology question**, not a physical contradiction between engines. Which anchor/topology the vacuum
runs is the plumber question surfaced in §6 — PENDING-GRANT-WALK.

---

## 1. Gate ledger (internally consistent; several are self-comparisons — see the "meaning" column)

The gates run green, but green ≠ independent. The COMMIT-2 repair replaces the self-comparisons (G2, G6) with
independent checks and reconciles G1 with its frozen clause; the table below records both the shipped result and its
honest meaning.

| Gate | Condition (prereg §5) | Result (shipped) | Meaning (post-review) |
|---|---|---|---|
| **G1** low-k UNCHANGED | node tank decouples at ω→0 ⇒ acoustic velocity = X33 velocity | tank/bare low-k ratio dev from 1 = **5.7e-9** ✅ | **DRIFT (MINOR-8/13):** shipped check ≠ the frozen "walk/node-tank/bare low-k slope ratio = √2 to <1e-5" clause; documented as a post-freeze change in COMMIT 2 |
| **G2** tank-removed control | ω_C→∞ recovers X33's LIFTING bare continuum | rel err **0.0e+00**; lift **22.4×** ✅ | **SELF-COMPARISON (MAJOR-10):** `tank_omega2_eta1(ω_C→∞)` vs its OWN bare input = bit-level identity, not an independent X33 recovery; COMMIT 2 adds an independent X33 reference path |
| **G3** scalar walk = #604 | ρ*=1 walk leg gives π√3; node-tank leg records its anchor | walk top **5.4414** (π√3); node-tank top **0.9608 ω_C** ✅ | OK — walk leg is an independent arccos computation |
| **G4** band-count | DOF = channels + node-tank DOF | η=1: **12/12**; η=0.5: **24/24**; aug (u,q) err **1.1e-15** ✅ | OK — the augmented eigensolve is an independent cross-check |
| **G5** enantiomorph parity | isotropic tank preserves R/L handedness | R vs L top diff = **0.0e+00** ✅ | OK — parity identity |
| **G6** gap structure | η<1 opens a D-INDEPENDENT node stop-band [ω_C, ω_C/√(1−η)] | edge err **<1e-6**; "D-independence (Λ ×1000) <1e-6" ✅ | **NO-OP (CRITICAL-3):** the shipped D-independence loop discarded the Λ loop variable and evaluated the SAME constant at Λ=1e-9 twice; COMMIT 2 actually varies Λ and adds a planted stop-band-violation test that must fire |

**Adjudication — could not fire L or M (MAJOR-11):** the frozen rule (lift ratio < 1.3 → P) returned Branch P, but
Branch P was **mathematically entailed** by the frozen model choice (series anti-resonant notch + η=1 + anchor=ω_C)
combined with the merged X33 continuum inputs **before any X36 code ran**. Under those choices the reciprocal law
forces the stiff channel to ω_C regardless of ρ*, so lift → 1 is guaranteed analytically; L (parallel-band-pass
topology) and M (η<1) were excluded by the model, not tested by the run. The 22.37× bare-continuum contrast is real,
but it is the contrast between "tank installed at ω_C" and "no tank", not evidence that ω_C is the *derived* ceiling.

---

## 2. The spectrum numbers — ceiling vs ρ*, node tank ON vs OFF (at anchor = ω_C)

**srs vector cell, band ceiling (ω_C) vs ρ\*** (R = √2 fixed elastic→ω_C conversion, anchored at ρ*=1; **tank
anchored at ω_C, series-notch topology, η=1**):

| ρ* | bare continuum (tank OFF) | **node-tank (tank ON, η=1)** | node-tank (MeV) | walk (bond tick) |
|---|---|---|---|---|
| 1.0 | 3.4641 | **0.96077** | 0.4910 | 5.4414 |
| 9.77337 (canonical) | 7.8979 | **0.99208** | 0.5070 | 5.4414 |
| 100 | 24.5698 | **0.99917** | 0.5106 | 5.4414 |
| 1000 | 77.4833 | **0.99992** | 0.5110 | 5.4414 |
| **lift ratio (1000/1)** | **22.37×** (LIFTS) | **1.041×** (PINS) | — | flat (walk) |

The node-tank column flattens toward the **installed anchor** (here ω_C = 1, ℏω_C ≡ m_e c², an identity — **not a
predicted value**) as the channel stiffens; the bare continuum lifts ∝ √stiffness (22×). This is a characterization
of *the tank installed at ω_C*, not a derivation of where the ceiling "must" sit.

**Placement probe (the promised prereg §6 disclosure — the tautology made explicit).** Install the same series-notch
tank at a different resonance ω_r and re-read the stiffest (ρ*=1000, Λ=77.48²) ceiling:

| tank anchor ω_r (×ω_C) | 0.5 | 1.0 | π√3 = 5.4414 | 10 |
|---|---|---|---|---|
| **coupled ceiling (ω_C)** | **0.5000** | **0.9999** | **5.4280** | **9.9177** |

**The ceiling is wherever the tank is installed.** A tank at π√3·ω_C reproduces the walk's ceiling (5.428 ≈ 5.441) —
so the §4 "two-clock tension" reduces to the un-derived choice of anchor, not a physical fact the engine returns.
(Driver field `placement_sweep`; added in COMMIT 2.)

## 3. The η-family — and why Branch P is a SINGULAR POINT at exactly η = 1 (MAJOR-7)

The pin exists **only at exactly η = 1**. For **any** η < 1 a lifting upper polariton branch reappears, and the
**full-spectrum ceiling** (max over both branches) lifts ≈ the bare continuum. This is not a smooth "mostly pinned"
neighbourhood of η = 1 — it is a discontinuity:

| η | lower-branch top (ω_C) | upper-branch top at ρ*=1000 | **full-spectrum ceiling lift (ρ1000/ρ1)** |
|---|---|---|---|
| **1.000** | 0.9999 | — (no upper branch) | **1.041× (PINS)** |
| 0.999 | 0.9999 | 2450 | **21.49× (≈ bare continuum)** |
| 0.99 | 0.9999 | 775 | **21.50×** |
| 0.90 | 0.9999 | 245 | **21.57×** |
| 0.75 | 0.9999 | 155 | **21.69×** |
| 0.50 | 1.0000 | 110 | **21.90×** |
| (bare continuum, no tank) | — | — | **22.37×** |

At η = 0.999 the full-spectrum ceiling lifts **21.49×** — **indistinguishable from the bare continuum's 22.37×**.
So "Branch P" is not a robust regime; it is the measure-zero point η = 1. The lower/acoustic manifold does pin at the
anchor for all η, but the *ceiling* (the load-bearing quantity for the longitudinal-only window and the fork-A floor)
lifts for any η < 1. The **node stop-band [ω_C, ω_C/√(1−η)]** is a genuine D-INDEPENDENT spectral FORM (survives;
the standard locally-resonant-metamaterial band gap), but the "full pinning" only obtains when the bypass inertia is
*exactly* zero. **η is the fork parameter, and η=1 is a knife-edge** — surfaced to Grant (§6). (Driver field
`eta_singularity`; added in COMMIT 2. The figure's centre panel shows the η=0.5 structure — lower pinned + node
stop-band + upper branch lifting.)

## 4. The node-tank ceiling vs the WALK — the "two-clock tension" REDUCES to the anchor choice

The node-tank ceiling (at anchor ω_C) and the bond-tick walk ceiling differ by π√3:

| clock | mechanism | ceiling | in MeV |
|---|---|---|---|
| **node tank** (X36, anchored at ω_C) | node LC resonance = the INSTALLED anchor | ~1 ω_C | 0.511 (= the anchor identity) |
| **bond tick** (X33 walk, #604) | one bond per tick, Nyquist π·ω_link | π√3 ω_C | 2.781 |

`reproduces_walk = False` (ratio 0.182) **at anchor ω_C**. But the placement probe (§2) shows a tank anchored at
π√3·ω_C gives ceiling 5.428 ≈ 5.441 = the walk — i.e. the node tank *does* reproduce the walk's ceiling **if
installed there**. So the band SHAPE (rational vs arccos) differs, but the CEILING is set entirely by the un-derived
anchor. **The "discrete-tick shadow" narrative is withdrawn** (it is contradicted by the branch's own
`reproduces_walk = False` / ratio 0.182 at anchor ω_C). The honest statement: **the placement probe shows the
ceiling equals the installed anchor, so the "two-clock tension" reduces to the un-derived anchor/topology question,
not a derived fact about which clock the vacuum runs.**

## 5. The longitudinal-only window — CLOSES only on the η=1 knife-edge (conditional)

X33's discriminating observable was the **longitudinal-only window** [2.78, 8.69] MeV. **Conditional result:** the
window closes **only** under the full 3-choice Branch-P model (series notch AND η=1 AND anchor=ω_C). For **any η < 1**
the upper polariton branch re-opens the window above the node stop-band (§3), and for a **parallel-band-pass**
topology it never closes. So this is not a robust deliverable — it holds on the same knife-edge as Branch P itself.
**Caveat (MINOR-16/17):** the window's upper edge 8.69 MeV inherits #607's stiffness-lifted bracket [5.441, 17.011]
ω_C, itself PENDING-GRANT; it is carried here as an inherited number, not re-established by X36.

## 6. The 3-axis question surfaced to Grant (PENDING-GRANT-WALK)

X36 shows the engine returns whatever node model is installed; it cannot adjudicate the fork by itself. The physical
content is a **3-axis question**, none of the axes derived in-engine:

1. **Node shunt topology** — a **series anti-resonant notch** (mass-in-mass; pins at its resonance → Branch P) vs a
   **parallel-LC band-pass** (transparent at its resonance → does NOT pin → Branch L). Both are passive, lossless,
   KCL-consistent; the prereg itself lists both (`prereg_FROZEN.md:85`). This choice IS the P-vs-L selector.
2. **η partition** — is ALL node inertia the tank (**η = 1**, the knife-edge that pins the ceiling) or does any of it
   bypass rigidly (**η < 1**, upper branch lifts ≈ bare continuum, §3)? P requires η *exactly* 1.
3. **Anchor frequency** — the tank pins the ceiling at **whatever ω_r it is installed at** (§2 placement probe): base
   node rate ω_C, per-bond tick π√3 ω_C (reproduces the walk / #604), or elsewhere. Un-derived.

This is a corpus/Grant anchor question (which topology, partition, and anchor the vacuum runs), **not** an in-engine
numeric run and **not** a contradiction with #604 — surfaced, not resolved by fiat. **PENDING-GRANT-WALK.**

## 7. Consistency-vs-emergence + corpus-state consequence (fork bookkeeping — demoted)

**CONSISTENCY / characterization.** ω_C is an IDENTITY (`OMEGA_C`; ℏω_C ≡ m_e c²) — a **calibration anchor**, so a
ceiling that lands at ω_C is **calibration-in, calibration-out** (identity-class), NOT an emergence-class prediction.
R = √2 is Class-B (√eig↔arccos velocity conventions); ρ* is GR-imported (ν=2/7). What is genuinely **DERIVED** is the
reciprocal **FORM** `1/ω² = 1/Λ + 1/ω_C²` **given** the series-anti-resonant topology — the standard
locally-resonant-metamaterial anti-resonance law — **not** the topology choice, the η=1 partition, or the anchor
value (those three are un-derived modelling inputs; §6). No α/Q_TANK on any path.

**Corpus-state consequence (for the auditor to land, not this lane — all DEMOTED to candidates / no-ops):**
1. **X33's "in-engine-undecidable architecture fork" (PR #611) STANDS and is REINFORCED — NOT re-typed.** X36 does
   **not** collapse the fork. On the contrary, it demonstrates that the continuous engine returns **whatever node
   model is installed** (topology × η × anchor), so the engine cannot adjudicate the architecture fork on its own.
   That is a **general methodological caution** worth stating plainly: *a continuous node-shunt solver returns the
   ceiling you build into the shunt; it does not derive it.* **No X33 board-row re-type.**
2. **No #604 re-floor and no new cross-engine contradiction.** The earlier "node-tank predicts the vector band tops
   at m_e c², in TENSION with #604's π√3 ω_C" claim is **withdrawn**: the placement probe (§2) shows the ceiling is
   the installed anchor, so the apparent tension is the un-derived anchor choice, not a physical conflict between the
   #604 memoryless-node engine and X36. The #604 **memoryless-node note becomes a caveat CANDIDATE only** (worth
   recording that a memoryless-node scatter+connect engine and a node-shunt continuum solver install *different* node
   models, so their ceilings are not directly comparable), pending Grant.
3. **No FORK-A floor change.** The survey #607 bracket [5.441, 17.011] ω_C is **not** re-floored by X36. Any "floor
   drops to the node rate" statement is contingent on the un-derived 3-choice model and is withdrawn as a settled
   consequence; #607 stands PENDING-GRANT as before.
4. **The fork's physical content is the 3-axis question** (§6): (node shunt topology: series-anti-resonant-notch vs
   parallel-band-pass-transparent) × (η partition) × (anchor frequency) — flagged **PENDING-GRANT-WALK**.

These are candidate note updates surfaced to the auditor's manuscript / COLLABORATION_NOTES queue; the manual entries
are the auditor's to land (lane discipline). No leaf edit from this lane. **No new physics claim is made by X36.**

## 8. Process caveat — the freeze is unverifiable (MINOR-12)

The prereg, driver, result doc, JSON, and verdict all landed in a **single commit** (`c2136718`), and the prereg's
"frozen expectations" (prereg §4 line 122, §5) match the run's results to 5 digits. Because there is no pre-run
commit of the prereg preceding the driver output, the **freeze cannot be claimed as pre-registered**. The
"frozen expectations" are therefore demoted to **post-hoc analytic cross-checks** (they are correct closed-form
values, but they cannot function as a pre-commitment that constrained the run). The prereg file's content is
**annotated, not rewritten** (KEEP-BOTH) — see its added dated header.
