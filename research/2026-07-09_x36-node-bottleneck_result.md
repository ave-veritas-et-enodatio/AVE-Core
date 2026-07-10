# RESULT — X36 node-bottleneck discriminator: **BRANCH P (NODE-PINS) — the shared node LC tank derives effective synchrony, pinning every channel at m_e c²**

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

## 0. TL;DR — the verdict

**Grant's D-I question:** does the CONTINUOUS-time network, with the node's own shunt LC tank modelled explicitly,
pin the multi-channel ceiling at the node rate — deriving effective synchrony from Axiom-1's node resonance with NO
tick postulate? **Answer: YES — Branch P (NODE-PINS), decisively and from first principles.**

- Axiom-1's node is an **intrinsic LC tank** (a channel-shared shunt resonator, resonance ω_C), NOT the mass-spring's
  node-as-inertia-only. X33's continuum was the tank-**removed** truncation. Adding the tank back, the tank presents
  the bonds a frequency-dependent effective mass diverging at ω_C, giving the **reciprocal bottleneck law
  1/ω² = 1/Λ + 1/ω_C²** (the slower of {bond network, node tank} binds) — DERIVED from shunt KCL + losslessness, NOT
  tuned (derivation §1–2).
- **The node tank PINS the ceiling at the node rate ~1 ω_C = m_e c² for EVERY ρ\***: node-tank top = **0.9608 →
  0.9921 → 0.9992 → 0.99992 ω_C** for ρ* ∈ {1, 9.77337, 100, 1000} (converging to m_e c² = 0.511 MeV as ρ*→∞),
  **lift ratio 1.041×**. The **bare continuum** (X33 control, tank removed) LIFTS **22.37×** (3.46 → 77.48 ω_C). ⇒
  the stiffness lift is REMOVED by the shared node bottleneck. **Effective synchrony is DERIVED, no tick postulate.**
- **⇒ BRANCH P.** The X33 in-engine-undecidable architecture fork **collapses** under the Axiom-1 η=1 node: the
  continuous network with node tanks pins ∀ρ*, reconciling Axiom-1's continuous LC language with the walk map's
  operational success. The bond-tick walk is the discrete-tick **shadow** of the continuous node-tank bottleneck.

**All 6 gates PASS.** The pin is not an artifact of the calibration: the tank-removed control recovers X33's 22× lift
exactly (G2), and the pin's mechanism is named algebraically (m_eff(ω) → ∞ at ω_C ⇒ 1/ω² = 1/Λ + 1/ω_C²; stiffness
locked out of the ceiling).

**One TENSION, flagged for Grant (do not silently reconcile):** the node tank pins at the **node rate ~1 ω_C = m_e
c² = 0.511 MeV**, a factor **π√3 BELOW** #604's time-stepped bond-tick scalar top **π√3 ω_C = 2.781 MeV**. The node
tank is the **TIGHTER** clock. #604's scatter+connect engine uses a **memoryless node** (no LC tank) and over-reads
the ceiling. Which clock binds — node-tank (~1 ω_C) or bond-tick (π√3 ω_C) — is the plumber question surfaced below.

---

## 1. Gate ledger (all PASS)

| Gate | Condition (frozen, prereg §5) | Result | Pass |
|---|---|---|---|
| **G1** low-k UNCHANGED | node tank decouples at ω→0 ⇒ acoustic velocity = X33 velocity | node-tank/bare low-k slope ratio dev from 1 = **5.7e-9** | ✅ |
| **G2** tank-removed control | ω_C→∞ recovers X33's LIFTING bare continuum | rel err vs bare = **0.0e+00**; lift ratio **22.4×** recovered | ✅ |
| **G3** scalar walk = #604 | ρ*=1 walk leg gives π√3; node-tank leg records its ω_C pin (#604 tension) | walk top **5.4414** (π√3); node-tank top **0.9608 ω_C** | ✅ |
| **G4** band-count | DOF = channels + node-tank DOF | η=1: **12/12**; η=0.5: **24/24**; augmented (u,q) cross-check err **1.1e-15** | ✅ |
| **G5** enantiomorph parity | isotropic tank preserves R/L handedness identity | R vs L node-tank top diff = **0.0e+00** | ✅ |
| **G6** gap structure | η<1 opens a D-INDEPENDENT node stop-band [ω_C, ω_C/√(1−η)] | edge err **< 1e-6**; D-independence (Λ ×1000) **< 1e-6** | ✅ |

**Adjudication (prereg §4, no post-hoc drop):** frozen rule — node-tank lift ratio(1000/1) < 1.3 → Branch P;
> 3 → Branch L; intermediate/gap+upper → Branch M. **Measured node-tank lift = 1.041× (< 1.3) → Branch P.** The bare
continuum's 22.37× lift confirms the contrast is real (the pin is not because "nothing lifts anything").

---

## 2. The decisive spectrum numbers — ceiling vs ρ*, node tank ON vs OFF

**srs vector cell, band ceiling (ω_C) vs ρ\*** (R = √2 fixed elastic→ω_C conversion, anchored at ρ*=1):

| ρ* | bare continuum (tank OFF) | **node-tank (tank ON, η=1)** | node-tank (MeV) | walk (bond tick) |
|---|---|---|---|---|
| 1.0 | 3.4641 | **0.96077** | 0.4910 | 5.4414 |
| 9.77337 (canonical) | 7.8979 | **0.99208** | 0.5070 | 5.4414 |
| 100 | 24.5698 | **0.99917** | 0.5106 | 5.4414 |
| 1000 | 77.4833 | **0.99992** | 0.5110 | 5.4414 |
| **lift ratio (1000/1)** | **22.37×** (LIFTS) | **1.041×** (PINS) | — | flat (walk) |

The node-tank column is **flat and converges to ω_C = 1 exactly** (= m_e c² = 0.511 MeV) as the channel stiffens —
the shared node bottleneck caps every channel at the node rate. The bare continuum column lifts ∝ √stiffness
(unbounded, 22×). The walk column is flat at π√3 ω_C (the bond-tick Nyquist — a DIFFERENT, higher ceiling; §4).

## 3. The hybridization / gap structure near ω_C (the η-family — Branch-M anatomy)

The verdict is Branch P at the Axiom-1-pure **η = 1** (node IS the tank). The **η < 1** family (a bond-rigid bypass
inertia) is the Branch-M anatomy — reported first-class (prereg §3, a node-resonance stop-band is a new spectral
feature):

| η | lower-branch top (ω_C) | upper-branch top (ω_C) | node stop-band [ω_C, ω_C/√(1−η)] |
|---|---|---|---|
| 0.25 | 0.9980 | 9.138 (LIFTS) | [1.000, 1.1547] |
| 0.50 | 0.9960 | 11.214 (LIFTS) | [1.000, 1.4142] |
| 0.75 | 0.9940 | 15.891 (LIFTS) | [1.000, 2.0000] |
| **1.00** | **0.9921** | **— (no upper branch)** | **[1.000, ∞) — fully pinned** |

The **node stop-band [ω_C, ω_C/√(1−η)] is D-INDEPENDENT** (a pure node-resonance feature — driver G6: independent of
Λ to 1e-6 over a 1000× range). For η < 1: the **lower/acoustic manifold PINS at ω_C** (effective synchrony holds for
the shared sector) while the **stiff channel's upper branch LIFTS** through the stop-band (the architecture fork
survives above the gap). At η = 1 the gap → ∞ (no upper branch) ⇒ full pinning ⇒ Branch P. **η is the physical fork
parameter** — surfaced to Grant (§6). The figure's centre panel shows the η=0.5 MIXED structure (lower pinned + node
stop-band shaded + upper branch lifting).

## 4. Does the node-tank spectrum converge to the WALK's? — NO (both pin; the node tank is TIGHTER)

The X33-walk overlay (prereg §4 gate; figure right panel): the node tank and the bond-tick walk **both PIN**, but by
DIFFERENT mechanisms and at DIFFERENT ceilings:

| clock | mechanism | ceiling | in MeV |
|---|---|---|---|
| **node tank** (X36) | node LC resonance ω_C = c₀/ℓ_node | **~1 ω_C** | **0.511** (m_e c²) |
| **bond tick** (X33 walk, #604) | one bond per tick, Nyquist π·ω_link | **π√3 ω_C** | **2.781** |

`reproduces_walk = False` (node-tank/walk ratio = 0.182). The laws differ (rational 1/ω²=1/Λ+1/ω_C² vs
ω_link·arccos), so even the band SHAPE differs — **the node tank is NOT the walk**, and it is TIGHTER by π√3 (the
node resonance sits a factor π√3 below the per-bond Nyquist). Convergence would require ω_C(tank) = π√3 ω_C — the
plumber question of §6. **So the effective-synchrony derivation succeeds (Branch P) but yields a NEW, tighter,
node-set ceiling m_e c², not a reproduction of the walk.**

## 5. The discriminating OBSERVABLE — the longitudinal-only window CLOSES

X33's discriminating observable was the **longitudinal-only window** [2.78, 8.69] MeV (present under the lifting
continuum, absent under the pinning walk). Under the node tank, **every channel is pinned at ~m_e c²**, so the
window **CLOSES** (Branch P deliverable): there is no band where only the stiff longitudinal channel propagates —
the shared node bottleneck caps all channels together. (Under η < 1 the window re-opens above the node stop-band as
the upper polariton branch — the Branch-M residue.)

## 6. Flag surfaced to Grant — one plumber/CIRCUIT question (prereg §1)

**Where does the node's shunt LC tank resonate, relative to the bond band?** The identity says ω_C = c₀/ℓ_node =
1 ω_C = m_e c², which sits a factor **π√3 ≈ 5.44 BELOW** the per-bond Nyquist π√3 ω_C = the #604/walk ceiling.
- **If the tank resonates at that base node rate** (this result's frozen reading), it is a **within-band** bottleneck
  → it pins the vector band ceiling **DOWN at ~m_e c² = 0.511 MeV**, BELOW the bond-tick walk's 2.781 MeV,
  **contradicting** #604's time-stepped scalar top (whose memoryless-node engine omits the tank).
- **If the node tank resonates at the per-bond tick rate π√3 ω_C**, it reproduces the walk (2.781 MeV), and #604
  stands.
- **AND:** is ALL bond current forced through the shared tank (**η = 1** ⇒ everything pinned = Branch P), or does part
  of the node inertia bypass the tank rigidly (**η < 1** ⇒ the stiff channel pokes through a node stop-band = Branch
  M)?

This is a corpus/Grant anchor question (which clock the vacuum runs, and the node inertia partition), not an
in-engine numeric run — surfaced, not resolved by fiat.

## 7. Consistency-vs-emergence + corpus-state consequence

**CONSISTENCY / characterization.** ω_C IDENTITY (`OMEGA_C`; ℏω_C = m_e c²); R = √2 Class-B (√eig↔arccos velocity
conventions); ρ* GR-imported (ν=2/7). The node-tank law is DERIVED (shunt KCL + losslessness) and every gate COMPUTED
vs an independently-established number (X33's 22× lift for the control; π√3 for the walk leg; the closed-form node
stop-band edges). The literal augmented (u,q) eigensolve cross-checks the per-eigenvalue map (G4, 1.1e-15). No
α/Q_TANK on any verdict path; forward computation only. X33 walk+continuum + srs vector Born-Huang pipelines REUSED
(Rule 14).

**Corpus-state consequence (for the auditor to land, not this lane):**
1. **X33's "in-engine-undecidable architecture fork" (PR #611) is RE-TYPED** by X36: once Axiom-1's node is modelled
   as its explicit LC tank (η=1), the continuous network **PINS** ∀ρ* — the fork **collapses to Branch P** for the
   Axiom-1-pure node. The bond-tick walk and the node-tank are two synchrony mechanisms; the node tank is the
   binding (tighter) one. The board row for the X33 fork should be updated from "in-engine-undecidable" to "collapses
   to Branch P under the Axiom-1 node tank, PENDING the §6 tank-frequency anchor."
2. **A new TENSION with #604 is surfaced** (not resolved): the node-tank predicts the vector band tops at the node
   rate m_e c² = 0.511 MeV, a factor π√3 BELOW #604's time-stepped bond-tick top π√3 ω_C = 2.781 MeV. This is a
   flag-don't-fix cross-engine conflict (#604 memoryless-node vs X36 node-tank), requiring a Grant/corpus anchor of
   which clock binds. Both file+content are surfaced; no leaf reframed to match the other.
3. **The FORK-A tone floor narrative** (survey #607: bracket [5.441, 17.011] ω_C, conservative floor 17.01) is
   affected conditionally: under Branch P the vector band tops at ~1 ω_C (m_e c²), FAR below the bracket — the entire
   fork-A floor would drop to the node rate. This is CONTINGENT on the §6 anchor (base node rate vs bond tick) and is
   surfaced as a pending-Grant decision, NOT a settled re-floor.
4. **Op5 / node-tank methodological fact:** the Op5 scatter+connect engine (memoryless node, frequency-independent
   Householder coin) CANNOT see the node LC tank — it is a bond-tick engine. A continuous-time solver with an
   explicit node reactance is needed to read the node-tank ceiling. Candidate note for `substrate-native-check` /
   regime-discipline (pairs with X33's "Op5 is a PINNING clock" note): **there are TWO pinning clocks (bond-tick and
   node-tank); do not read one engine's ceiling as the other's.**

These are ledger rows + note updates surfaced to the auditor's manuscript / COLLABORATION_NOTES queue; the manual
entries are the auditor's to land (lane discipline). No leaf edit from this lane.
