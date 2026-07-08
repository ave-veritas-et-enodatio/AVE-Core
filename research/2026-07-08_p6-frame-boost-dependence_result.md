# P6-FRAME — does the birefringence response reference a preferred frame? RESULT

**Status:** RESULT. Adjudicates the three-corner fork frozen in
`research/2026-07-08_p6-frame-boost-dependence_prereg_FROZEN.md`.
**Date:** 2026-07-08 · **Lane:** implementer.
**Class (consistency-vs-emergence):** **CONSISTENCY.** Determines the
Lorentz-transformation property of an EXISTING kernel argument and the boost-order of an
EXISTING observable. No new claim-id / constant / axiom. Q=137 stays empty. The 4.9e-3 rides
the external ratio β = v_CMB/c — NOT an AVE emergence.
**Driver:** `src/scripts/vol_9_device/p6_frame_boost_dependence.py`
(run: `PYTHONPATH=src python3 src/scripts/vol_9_device/p6_frame_boost_dependence.py`).
**Tests (14, all green):** `src/tests/test_p6_frame_boost_dependence.py`.
**Artifact + figure (driver-regenerable, gitignored):**
`src/scripts/vol_9_device/_output/p6_frame_boost_dependence.{json,png}`.
**Builds on:** PR #574 `analysis/p6-sidereal-boost` (order settled O(β) *given* the CMB premise).
**Loci audited (NOT edited here — auditor/orchestrator integrates):**
`papers/2026_birefringence_letter/main.tex:402-432`, `.../provenance.md:40-43`.

---

## VERDICT BOX

> **PRIMARY BIN: [SIDEREAL-REAL] — BULK corner (substrate-native reading).**
>
> The birefringence kernel argument A = |E|/E_YIELD is a frame-dependent field **MAGNITUDE**,
> not a Lorentz invariant. The saturating medium (the vacuum nodes) is at rest in the substrate
> = CMB rest frame, which the corpus commits to as **detectable in principle**. The node
> therefore saturates on the **substrate-frame** field magnitude, whose boost-Doppler is a
> **continuum, O(1)-in-(qℓ_node)** effect — NOT suppressed by the cubic-symmetry (qℓ_node)⁴
> channel. Result: the sidereal signal is **REAL at first order in β**,
> **P_flip 1st-harmonic amplitude 4β ≈ 4.94×10⁻³**, phased to the CMB dipole.
>
> **This is a strong Lorentz-violation prediction in the nonlinear photon sector.** It is NOT
> excluded by existing LINEAR cavity/Michelson bounds (which AVE suppresses to (qℓ_node)⁴ ≈
> 10⁻²² — a *different* channel), but it must be stated as a strong-LV claim and checked against
> any nonlinear/higher-dimension SME sidereal bound.
>
> **The LOCAL corner (sidereal ≈ 0) is reachable ONLY via `main.tex:404-406`'s lab-frame
> EVALUATION choice, which has no substrate mechanism and contradicts `main.tex:420-421`.**
> Flagged for Grant, both loci quoted verbatim below (flag-don't-fix). The registered
> falsifier `(v/c)² = 1.5×10⁻⁶` is wrong on BOTH counts: wrong order (should be O(β), not O(β²);
> PR #574) AND — under the substrate-native reading — the correct magnitude is 4.9×10⁻³.

---

## ★ THE LOAD-BEARING SUB-QUESTION — the kernel-argument Lorentz transform

**The kernel argument is a field MAGNITUDE, not a Lorentz invariant.** The Axiom-4 kernel
S(A)=√(1−A²) takes A = |E|/E_YIELD, a scalar field amplitude
(`src/ave/axioms/scale_invariant.py:107-156` `saturation_factor(amplitude, …)`;
`src/ave/bench/birefringence.py:193-212` `delta_n_ave_differential_exact` keys on E/E_YIELD;
the Letter states it outright at `main.tex:404-405`: *"S depends on the single quantity |E|²,
which is not a Lorentz invariant"*). The electric response keys on |E| and the magnetic on |B|
**separately** (`epsilon_eff`/`mu_eff`), i.e. NOT on the invariants B²−E², E·B.

**Corner (a) — covariant/invariant — is RULED OUT, two ways** (sympy in
`p6_frame_boost_dependence.py::symbolic_kernel_transform`):
1. It is not what the kernel computes (|E|² ≠ any invariant).
2. **Anti-test:** for a radiation pump both EM invariants vanish (B=E/c ⇒ F=B²−E²=0, E·B=0), so
   an invariant-keyed kernel gives **A=0 ⇒ ZERO pump birefringence** — contradicting the
   Letter's central prediction δn ≈ 6×10⁻⁷. A covariant nonlinear electrodynamics (Born–Infeld)
   likewise produces no self-birefringence for a single null field. **So covariance is already
   broken in the nonlinear sector by construction; the kernel is a preferred-frame
   photon-sector modification** (as `main.tex:412-414` itself states).

**Therefore the live fork is which frame's |E| the medium keys on:**

| Transform class | frame | boost-dependence | corner |
|---|---|---|---|
| invariant √\|F\| | — | none (and 0 pump birefringence) | LOCAL (ruled out for the pump) |
| lab-frame magnitude | source/lab | none (E_lab fixed by the laser) | **LOCAL** (`main.tex:404`) |
| substrate-frame magnitude | CMB rest | Doppler D, O(β) | **BULK** (`main.tex:420`) |
| substrate, discreteness-gated | CMB rest | (qℓ_node)⁴·β | LATTICE |

For a radiation pump the substrate-frame magnitude is |E_sub| = D·|E_lab|, D = γ(1−β·k̂) the
plane-wave Doppler factor. **The vector Lorentz transform of the real (E,B) 4-tensor reproduces
this closed form to machine precision** (`doppler_vector_crosscheck`, rel_err = 0.0). The
β-expansion of the field powers (sympy):

```
D^1 (|E|)               = 1 + β cosθ + …      linear coeff = cosθ   ≠ 0
D^2 (δn_bir ~ A^2)      = 1 + 2β cosθ + …      linear coeff = 2cosθ  ≠ 0
D^4 (P_flip ~ |E|^4)    = 1 + 4β cosθ + …      linear coeff = 4cosθ  ≠ 0
γ   (STATIC field)      = 1 + ½β^2             linear coeff = 0       (O(β^2) — the static branch)
```

**Which frame is physical (the determination):** the saturation is a LOCAL, PER-NODE property
(`scale_invariant.py` docstring: "local field amplitude … at the node"); E_YIELD is a
node-rest-frame property; the node is at rest in the substrate = CMB rest frame, which the
corpus identifies AND declares detectable
(`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md:16,32,36`
— *"NOT Maxwell-Lorentz ether … the CMB dipole IS the detection"*). A radiation field has no
rest frame of its own (it is null), so the only frame available to split F into (E,B) is the
substrate frame. **⇒ substrate-frame magnitude ⇒ BULK.**

**Why LATTICE does NOT apply here.** The emergent-Lorentz (qℓ_node)⁴ suppression
(same leaf §2, `:21-22`) protects the **rotational anisotropy of the LINEAR photon dispersion**
(a cubic-point-group fact about the ω(q) dispersion tensor). The pump-birefringence
boost-Doppler is a **boost** (not a spatial rotation) acting on a **continuum** amplitude
(survives qℓ_node→0). It is a different tensor channel and is NOT cubic-symmetry-suppressed.
Numerically the physical optical lattice signal would be 4β·(qℓ_node)⁴ ≈ 1×10⁻²⁴ (~21 OOM below
BULK, unobservable) — the LATTICE corner is *reachable* but is not where this observable lives.

## NUMERICAL BOOST-DEPENDENCE (magnitude sweep, log-log slope = order)

| response frame | order in β (P_flip) | frac_P at β_CMB | corner |
|---|---|---|---|
| lab | flat (nan) | 0 (exact) | LOCAL |
| invariant | flat (nan) + zero pump birefringence | 0 (exact) | LOCAL (ruled out) |
| **substrate** | **1.001** | **+4.949×10⁻³** | **BULK** |
| lattice (X-ray demo qℓ) | 1.001 | +1.7×10⁻⁹ (∝ (qℓ)⁴) | LATTICE |

**Sidereal (direction) sweep, BULK config, over one apparatus rotation vs the fixed CMB dipole:**

| harmonic | computed | order | reading |
|---|---|---|---|
| P_flip 1st (fundamental) | **4.937×10⁻³** | 4β | DOMINANT, one sidereal day, CMB-phased |
| δn_bir 1st | 2.468×10⁻³ | 2β | the coefficient modulation |
| P_flip 2nd (2×sidereal) | 4.57×10⁻⁶ | ~3β² | subdominant (PR #574's "5β²" was an order estimate; both O(β²)) |

These reproduce PR #574's radiation-Doppler numbers exactly under the CMB-frame config — the
present result supplies the UPSTREAM frame determination #574 deferred.

## LIVENESS (anti-tautology) — all three bins reachable

The harness boosts the REAL (E,B) field and keys the REAL Axiom-4 kernel through a configurable
`response_frame`; it reaches every corner:
`lab`/`invariant` → FLAT (LOCAL); `substrate` → order-1 unsuppressed (BULK); `lattice` → order-1
suppressed by (qℓ_node)⁴ (LATTICE). A planted-order guard recovers n=1, n=2, and flat→nan. All
green in the driver (`ALL THREE REACHABLE: True`) and locked in
`test_p6_frame_boost_dependence.py::test_all_three_bins_reachable`.

## RECOMMENDED STATUS FOR THE THIRD FALSIFIER

**KEEP, but re-state as [SIDEREAL-REAL] with the frame premise explicit and the strong-LV caveat**
(NOT retract). Concretely (auditor/orchestrator lands; do not edit the paper here):
1. Correct the registered magnitude `(v/c)² = 1.5×10⁻⁶` → **P_flip 1st-harmonic 4β ≈ 4.9×10⁻³**
   (δn 2β ≈ 2.5×10⁻³), attribute the DOMINANT signal to the **first** (fundamental) sidereal
   harmonic, keep the O(β²) second harmonic (~3β² ≈ 4.6×10⁻⁶) as the labeled subdominant term
   (this is PR #574's already-owed correction).
2. **Resolve the internal contradiction** `main.tex:404-406` (lab frame → 0) vs `main.tex:420-421`
   (CMB frame → O(β)). The substrate-native physics selects the CMB-frame reading; the lab-frame
   sentence should be re-scoped to "the field is *specified* in the lab frame" (a labelling
   statement) and NOT "the response frame is the lab frame" (a physics statement, which the
   substrate contradicts).
3. Add the strong-LV caveat: a 4.9×10⁻³ CMB-phased sidereal modulation of the *nonlinear*
   pump-probe birefringence is a large preferred-frame effect; state that it is not bounded by
   existing linear cavity/Michelson LV limits and flag an SME nonlinear-sector bound check as
   owed. **This is a Grant framing call** — surfaced, not landed.

## HONEST CAVEATS

1. **The verdict is substrate-native, and the fork is genuinely a physics-framing question.** The
   harness PROVES the three corners are distinct and reachable and pins the numbers; the CHOICE
   of corner rides on "does the nonlinear response reference the medium's rest frame (BULK) or
   lock to the source frame (LOCAL)." The substrate physics (local node saturation + detectable
   CMB rest frame + wrong-channel (qℓ)⁴) points to **BULK**. The counter-reading requires
   postulating that the response locks to the lab/source frame — a postulate with no substrate
   mechanism. Both are surfaced; the substrate-native lean is BULK.
2. **Deeper open question (flag-don't-fix, for Grant).** Whether |E|²-keying is FUNDAMENTAL (→
   BULK) or a weak-field APPROXIMATION to an underlying covariant response that keys on the
   pump-probe cross-invariants (→ LOCAL, QED-Euler-Heisenberg-like) is not settled by the
   corpus. If the true substrate response is covariant and |E|²-keying is only its weak-field
   face, the sidereal signal collapses to the LATTICE/(qℓ)⁴ residual (~10⁻²⁴). The Letter
   commits to |E|²-keying as fundamental (`main.tex:404-405`, `:412-414`), which is the BULK
   reading. This is the single load-bearing physics assumption; named here, not buried.
3. **The paper-hardening ledger is on `origin/analysis/paper-hardening-ledger`, NOT on
   `origin/main`** (verify-before-cite: `git cat-file -e origin/main:research/2026-07-08_paper-hardening-ledger.md`
   → absent). This result stands on the merged-HEAD kernel + Letter + KB; the ledger is read as
   the contention source only.
4. **Order-counting + magnitude, not a full cavity QFT.** The corner is fixed by the kernel
   argument (the pump |E| in the response frame); probe-side Doppler/aberration are O(β) and
   REINFORCE (PR #574), so they cannot rescue LOCAL. A complete pump-probe cavity treatment
   would refine the coefficient, not the corner or the order.

## PROVENANCE OF NUMBERS

β = v_CMB/c = 370×10³ / 299792458 = 1.234187×10⁻³ (c from `ave.core.constants.C_0`, CODATA-exact;
v_CMB an EXTERNAL astrophysical input). E_YIELD, L_NODE ride in from `ave.core.constants`.
4β = 4.937×10⁻³; 2β = 2.468×10⁻³; (qℓ_node,optical)⁴ = 2.2×10⁻²². All reproduced by the driver
and pinned in the tests.
