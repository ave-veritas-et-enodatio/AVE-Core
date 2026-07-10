# PREREG (FROZEN) — X36: the node-bottleneck discriminator (does the node LC tank derive effective synchrony?)

**Date:** 2026-07-09 · **Branch:** `analysis/x36-node-bottleneck` (off main @ ba662d57, incl. merged #611) · **Task:** X36 (Grant-fired, the D-I discriminator)
**Consumes:** [`research/2026-07-09_x33-clock-architecture_result.md`](2026-07-09_x33-clock-architecture_result.md) (merged #611 — the fork this
adjudicates: the walk PINS ∀ρ* via the Householder coin's ±1 eigenvalues; the CONTINUUM partner LIFTS 22×;
in-engine-undecidable AS TESTED), [`research/2026-07-09_srs-vector-band-survey_result.md`](2026-07-09_srs-vector-band-survey_result.md) (merged #607, the bracket
[5.441, 17.011] ω_C), Axiom 1's node definition (`manuscript/ave-kb/CLAUDE.md:70` — *"intrinsic LC oscillators at each
node ... modeled in continuum as a Trace-Reversed Chiral LC Network"*; the node resonance IS canonical).
**Adjudicates:** whether X33's "in-engine-undecidable architecture fork" collapses once Axiom 1's node is modelled
as an explicit shunt **LC tank** (not the mass-spring's node-as-inertia-only).

**Class (consistency-vs-emergence):** **CONSISTENCY / characterization.** A math+numerics typing of the substrate's
own node architecture. ω_C = c₀/ℓ_node is an **IDENTITY** (`OMEGA_C`; ℏω_C = m_e c² exactly); the elastic→ω_C
calibration R = √2 is a Class-B manifestation of the two velocity conventions (√eig vs arccos); ρ* is GR-imported
(ν=2/7). **No CODATA on any verdict path; this is an exact-spectrum computation, not an empirical vote.**

> **⚠ PROCESS CAVEAT (2026-07-09, post PR #613 adversarial review — annotation only, content below UNCHANGED,
> KEEP-BOTH).** This prereg, the driver, the result doc + JSON, and the verdict all landed in a **single commit**
> (`c2136718`); the "frozen expectations" in §4 and §5 match the run's results to 5 digits. There is no pre-run
> commit of this prereg preceding the driver output, so **the freeze cannot be claimed as pre-registered** (MINOR-12).
> The §4/§5 "frozen expectations" are therefore demoted to **post-hoc analytic cross-checks**: they are correct
> closed-form values, but they did not function as a pre-commitment that constrained the run. Two further items the
> review confirmed, which the reader should carry while reading below: (i) §2a's claim that the mass-in-mass topology
> is **forced** is FALSE — §2a itself and §3 list an equally passive/lossless/KCL-consistent **parallel-LC band-pass**
> shunt (line 85) that does NOT pin (→ Branch L); the topology is the P-vs-L *selector*, a choice (CRITICAL-1). (ii)
> The §4 "predicts … pinned at the node rate ~1 ω_C = m_e c²" is **calibration-in, calibration-out** (ω_C is the
> definitional `OMEGA_C` anchor), NOT an emergence-class prediction (CRITICAL-2). See the result doc's correction
> banner for the full restated verdict. **The prereg text is preserved verbatim below; nothing is rewritten.**

---

## 0. substrate-native-check (walked BEFORE any numerical code, per Operating Principle 1)

- **K4 / node:** Axiom 1 node = **intrinsic LC oscillator** (a shunt LC tank; `CLAUDE.md:70`,
  `translation-circuit.md:97`). The 6 DOF/node decompose 3 translational (E → **capacitive** storage) + 3
  microrotational (B → **inductive** flywheel). The node's translational response IS the tank capacitance.
- **What X33 got wrong (the reframe):** X33's continuum partner was a **mass-spring dynamical matrix** — nodes as
  **inertia only** (a bare mass m, no resonance). That is the translational-C truncation of the node with the tank
  **removed**. Axiom 1's node is an LC TANK with its own shunt resonance ω_C; every channel transacts through the
  same node hardware (channel-shared shunt admittance). **This prereg adds the tank back.**
- **Dynamics:** CONTINUOUS-time Bloch (Hamiltonian flow, NO tick) WITH an explicit shunt LC tank at each node. NOT
  Lagrangian-minimization, NOT gradient-descent, NOT energy-basin. The tank is a passive reactive DOF, rendered as a
  frequency-dependent **effective dynamical mass** the bonds see (boundary-style reactance, not a bulk force term —
  Checkpoint 10). Sector: TRANSLATIONAL / T2-vector (the γγ-carrier channel), cold / linear (A≪1), Op14 OFF.
- **Coords (A46):** the observable is a dispersion **ceiling** ω_top(k) — the same coordinate for all three
  architectures (bare continuum √eig D, node-tank, walk arccos are all ω(k) band tops). No phase-space vs
  real-space mismatch (`phase-space-coordinate-check` cleared: dispersion-top vs dispersion-top, as X33).
- **Clock:** the object UNDER TEST is whether the NODE (its LC tank), not the bond-tick, sets the ceiling.

## 1. pre-test-physics-check — one plumber/CIRCUIT question, surfaced to Grant BEFORE design

**Synchronous-backplane picture:** the shared clocked chip (the node) has ONE resonant frequency ω_C = c₀/ℓ_node
set by its own L and C. A fast backplane trace (a stiff bond, large ρ*) can slew faster than the chip, but the
signal still has to clock THROUGH the chip — so the whole bus should be pinned at the chip's clock, not the trace's
slew rate. **The question that sets the verdict scale:**

> **Where does the node's shunt LC tank resonate, relative to the bond band?** The identity says
> **ω_C = c₀/ℓ_node = 1 ω_C** (= m_e c²), which sits a factor **π√3 ≈ 5.44 BELOW** the per-bond Nyquist
> (π·ω_link = π√3 ω_C = the #604/walk ceiling). If the tank resonates at that base node rate, it is a
> **within-band** bottleneck → it pins the ceiling DOWN at **~1 ω_C = m_e c²**, BELOW the bond-tick walk's
> 2.78 MeV, **contradicting** the #604 time-stepped scalar top (which used a memoryless node, no tank). If instead
> the node tank resonates at the per-bond tick rate π√3 ω_C, it reproduces the walk. **AND:** is ALL bond current
> forced through the shared tank (η = 1, everything pinned = Branch P), or does part of the node inertia bypass the
> tank rigidly (η < 1, the stiff channel pokes through a node stop-band = Branch M)?

**This is surfaced, not resolved by fiat.** The prereg FREEZES the identity value ω_C = c₀/ℓ_node = 1 ω_C (a
DERIVED substrate number, not tuned) and the Axiom-1-pure η = 1 (node IS the tank) as the canonical reading, and
REPORTS the full η-sweep and the ω_C-placement sensitivity so Grant/substrate can anchor the fork.

---

## 2. THE DECIDABLE QUESTION (frozen exactly this way)

Extend the X33 CONTINUOUS-time Bloch problem (1D two-channel zig-zag chain — primary, tractable; and the srs cell)
with an **explicit shunt LC tank at each node**, resonance ω_C, coupled to **all channels** through the shared node.
Compute the coupled spectrum's ceiling ω_top(ρ*) and compare against (a) the **bare continuum** (X33, tank removed —
the control that LIFTS 22×) and (b) the **walk** (X33, arccos — PINS at π√3 ω_C). Does the node tank pin the ceiling
at the node rate for every channel (deriving effective synchrony with NO tick postulate)?

### 2a. Node-tank construction (frozen — the coupling is DERIVED from the junction, not tuned)

The node's Axiom-1 LC tank is a shunt resonator the through-signal must drive to cross the node. Because the tank is
**channel-shared** (one scalar reactive admittance × I on all D translational channels — "every channel transacts
through the same node hardware"), it presents the bond network a **frequency-dependent effective dynamical mass**

    m_eff(ω) = (1−η)·m  +  η·m·ω_C² / (ω_C² − ω²),     η = μ_tank/m ∈ (0, 1],   ω_C² = γ_tank/μ_tank,

with m the node's total (X33-fixed) low-frequency inertia, μ_tank the tank's inertial store, γ_tank its restoring
reactance, and η the fraction of the node inertia that is the tank vs a bond-rigid bypass. The coupled dispersion is

    eig(D(k)) = ω² · m_eff(ω)       [ per D-eigenvalue λ_b(k); the tank is isotropic ⇒ D's eigenvectors are unchanged ].

**Topology choice + justification (stated, alternatives flagged, per Grant):** the tank is a **series** reactive
store the bonds see (mass-in-mass / locally-resonant-network form) — FORCED by (i) shunt KCL through the shared node
and (ii) losslessness (a passive LC store). **η = 1** ("the node IS the tank"; Axiom 1: the node's translational
storage is the tank capacitance, no separate rigid inertia) is the canonical Axiom-1 reading. **Alternatives
flagged:** (a) η < 1 (a bond-rigid bypass inertia — Branch M, an upper polariton branch pokes through a node
stop-band); (b) a **parallel-LC band-pass** shunt (transparent AT ω_C — would NOT pin, → Branch L); (c) the
microphysical **Cosserat translational-C ⊗ rotational-L** tank (the deep model — the mass-in-mass is its
translational-sector reduction with the microrotational DOF integrated out; a NAMED follow-on).

### 2b. The closed-form consequences (frozen BEFORE the run)

- **η = 1** ⇒ m_eff = m·ω_C²/(ω_C²−ω²) ⇒ **1/ω²(k) = m/eig(D(k)) + 1/ω_C²** (the reciprocal / series-reactance
  **bottleneck law**: the slower of {bond network, node tank} binds). Single pinned manifold, no upper branch.
- **η < 1** ⇒ quadratic per λ_b: `m(1−η)·x² − (m·ω_C² + λ_b)·x + λ_b·ω_C² = 0`, `x = ω²` ⇒ TWO branches (lower
  pinned + upper lifting), gap **[ω_C, ω_C/√(1−η)]** (D-INDEPENDENT — a pure node-resonance stop-band).

---

## 3. THREE BRANCHES (fork-record-all, frozen)

- **Branch P (NODE-PINS):** ω_top^tank(ρ*) is ρ*-independent (~node rate) for all channels ⇒ effective synchrony
  DERIVED from the shared node bottleneck, NO tick postulate ⇒ D-I resolves single-scale-by-mechanism ⇒ the
  longitudinal-only window CLOSES ⇒ the fork-A floor narrative simplifies. (The Axiom-1 η=1 reading predicts this.)
- **Branch L (LIFT SURVIVES):** the stiff channel's band still rises past the node resonance (e.g. the tank is a
  band-pass transparent at ω_C, or ω_C ≫ the bond band) ⇒ the architecture fork REMAINS open, sharpened to the
  junction-topology question.
- **Branch M (MIXED):** partial pinning / hybridization gaps (avoided crossings between the channel bands and ω_C).
  Report the **gap structure** [ω_C, ω_C/√(1−η)]; a node-resonance stop-band is itself a **new spectral feature**
  worth first-class reporting. (The η<1 bypass reading predicts this.)

## 4. ADJUDICATION RULE (frozen — decision rule fixed before the verdict is read; no post-hoc drop, Rule 11)

Compute ω_top^tank(ρ*) at ρ* ∈ {1, 9.77337 (canonical), 100, 1000} for the canonical model (η = 1, ω_C = 1 ω_C):

- **Branch P** iff **lift ratio ω_top^tank(1000)/ω_top^tank(1) < 1.3** (bounded, ≤ 30 %, vs the bare continuum's
  22.4×) — i.e. the tank has removed the stiffness lift.
- **Branch L** iff **lift ratio > 3** (comparable to the bare continuum's lift — the tank failed to bind).
- **Branch M** iff **1.3 ≤ lift ratio ≤ 3** OR a hybridization stop-band + an upper branch that lifts is present at
  the canonical model (report the gap and which sector pins vs lifts).

**Frozen expectation (from the X33 continuum + the closed-form tank law, R = √2):** the bare continuum tops
(elastic) 2.4495 → 5.5846 → 17.3734 → 54.789 map to ω_C units (×R=√2) 3.464 → 7.898 → 24.570 → 77.483; the η=1
node-tank at ω_C=1 pins these at **0.9608 → 0.9921 → 0.9992 → 0.99992 ω_C** (lift ratio **1.041×**) ⇒ **Branch P**,
pinned at the node rate ~1 ω_C = m_e c². This is BELOW the walk's π√3 = 5.441 ω_C — see §6.

## 5. GATES (analytic expectations frozen — ALL must pass for the verdict to stand)

| Gate | Condition (frozen) | Analytic expectation |
|---|---|---|
| **G1 low-k UNCHANGED** | the node tank decouples at ω→0 ⇒ acoustic velocities are the X33 velocities | ω→√(eig D/m), ω_C-independent; walk/node-tank/bare-continuum low-k slope ratio = R = √2 to < 1e-5 |
| **G2 tank-removed control** | ω_C → ∞ (or η → 0) recovers X33's LIFTING bare continuum | node-tank top → bare-continuum top for every ρ*; lift ratio → 22.4× to < 1e-6 |
| **G3 scalar reduces + walk leg reproduces #604** | single channel (ρ*=1): the WALK leg gives π√3; the node-tank leg gives its ω_C=1 pin (recorded + FLAGGED vs #604) | walk scalar top = π√3 = 5.4414 (< 1e-4); node-tank scalar top = 0.9608 ω_C (record — the #604 tension, §6) |
| **G4 band-count bookkeeping** | DOF = channels + node-tank DOF | η=1: N_DOF branches (srs 12, 1D 4); η<1: 2·N_DOF (lower+upper); verify exactly |
| **G5 enantiomorph parity** | the isotropic tank preserves R/L handedness identity (cold spectra parity-symmetric) | node-tank R vs L spectra identical to the survey roundoff floor (< 1e-6) |
| **G6 hybridization / gap structure** | η<1 opens a D-INDEPENDENT node stop-band [ω_C, ω_C/√(1−η)]; η=1 has none (gap→∞) | gap edges match ω_C, ω_C/√(1−η) to < 1e-6; ρ*-independent (pure node feature) |

**Driver-honesty (Rule 10):** no dead-actuator / PML (closed spectral solve); the tank law is applied to the
diagonalized D per-eigenvalue (isotropic tank ⇒ D-eigenvectors preserved — verified, not assumed, by G4 count and by
a literal augmented-DOF eigensolve cross-check on the 1D chain); reactance-pair N/A (spectral, not time-domain).

## 6. WHERE THE CEILING LANDS (the convergence-to-walk question, to be REPORTED not tuned)

The node tank pins (Branch-P property) but at its OWN resonance ω_C, NOT the walk's bond-tick Nyquist. With the
identity ω_C = 1 ω_C:

- **node-tank ceiling ≈ 1 ω_C = m_e c² = 0.511 MeV** (the node rate),
- **walk ceiling = π√3 ω_C = 5.441 ω_C = 2.781 MeV** (the bond-tick Nyquist),
- **bare continuum = lifts 3.46 → 77 ω_C** (no clock).

⇒ **the node-tank does NOT numerically reproduce the walk's arccos band** (different law — rational vs arccos; and a
factor π√3 tighter ceiling). Both PIN, by DIFFERENT mechanisms: the walk by the bond tick, the node tank by the node
resonance — and the **node tank is the TIGHTER binding clock**. **Flag (surface to Grant, do not silently
reconcile):** IF the node tank is a series bottleneck at ω_C = c₀/ℓ_node, it predicts the vector band tops at the
NODE RATE m_e c², BELOW and in TENSION with #604's time-stepped bond-tick top of π√3 ω_C = 2.78 MeV (the #604
scatter+connect engine uses a memoryless node and omits the tank, so it would OVER-read the ceiling). Which clock is
binding — node-tank (tighter, ~1 ω_C) or bond-tick (#604, π√3 ω_C) — is the plumber question of §1, surfaced to
Grant. Convergence-to-walk gate result: **NO** (both pin; different ceilings) UNLESS Grant anchors ω_C(tank) = π√3.

## 7. D-I DISCRIMINATOR IMPLICATION (frozen consequence of the verdict)

- **Branch P ⇒** effective synchrony is DERIVED from Axiom-1's node tank with NO tick postulate — reconciling
  Axiom-1's continuous LC language with the walk map's operational success. The bond-tick walk is then the
  discrete-tick SHADOW of the continuous node-tank bottleneck; both pin, and the node tank is the binding one.
- **Branch M ⇒** the node tank pins the shared acoustic manifold but the stiff channel pokes through a node
  stop-band; effective synchrony holds below ω_C only; the architecture fork survives above the gap.
- **Branch L ⇒** the node tank does not bind; X33's in-engine-undecidable fork stands unchanged.

## 8. Deliverables

prereg (this, FROZEN) → derivation note + numeric driver `x33_clock_architecture.py` **EXTENDED** (Rule 14, reuse
the validated srs vector + walk pipeline) → result doc + JSON + WHITE figure (three spectra overlaid: bare continuum
/ node-tank continuum / walk, + ceiling-vs-ρ*). `make verify`. Commit `[REVIEW: pending-orchestrator]`. PR
(DO-NOT-MERGE).

**FROZEN 2026-07-09. No adjudication axis is dropped or relaxed post-hoc (Rule 11).**
