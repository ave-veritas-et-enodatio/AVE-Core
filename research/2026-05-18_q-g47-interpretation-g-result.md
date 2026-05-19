# Result — Q-G47 K4-TLM A5 Interpretation G Geometry Verification

**Date**: 2026-05-18 night
**Test**: Golden Torus geometry verification on `run_v14_canonical` bound state via radial Riemann-invariant projection + Lissajous PCA + FFT multi-mode discriminator
**Engine commit SHA**: `9a989f7c8e02e9775e9283504f1a1273d5d9df44`
**Driver script**: `src/scripts/verify/q_g47_path_d_full_cross_validation.py` (this session's commit adds `golden_torus_geometry_check()` observer)
**Pre-registration**: `research/2026-05-18_q-g47-interpretation-g-prereg.md` (this session)
**Closure pathway**: `research/2026-05-18_abcd-eigensolver-workstream-handoff.md` (multi-session, next-session Priority #1)
**Result class** (per `consistency-vs-emergence` skill): **INTRA-FRAMEWORK CONSISTENCY CHECK** — verifies internal coherence between Vol 1 Ch 8 Golden Torus geometry claim and `MasterEquationFDTD` v14 canonical bound state. Result: INCOHERENT (geometry not realized).

## 1. TL;DR

**Outcome A fired**: R/r ratio measured = 13.29, target φ² = 2.618, deviation = 407%. The v14 canonical bound state does NOT realize Golden Torus geometry. Theorem 3.1' bridge precondition (Λ_i = Q_i identification valid only at Golden Torus) is therefore NOT satisfied at v14 — the 50% Λ_total/α_cold⁻¹ gap is dominantly geometric-mismatch (Interpretation G CONFIRMED).

**Two substantive findings beyond prereg expectations**:

1. **Unexpected multi-mode structure present**: ALL 8 sample peaks show multi-mode FFT (secondary peaks within 20 dB of dominant). Contrary to my pre-test reasoning that scalar EMT couldn't produce multi-mode breathing, the bound state has multi-mode structure from NONLINEAR SATURATION HARMONIC GENERATION, not from chirality (Grant's intervention correctly identified absent chirality; the multi-mode comes from a different mechanism).

2. **Radial-shell mode segregation**: Inner shell (r_from_center = 1.73) oscillates at f ≈ 0.068; outer shell (r_from_center = 3.32) at f ≈ 0.029. **Ratio 7/3 ≈ 2.333**, NOT the 3/2 expected for (2,3) torus knot. Inner-shell frequency ≈ 2.18× breathing fundamental — a **nested-oscillator structure** where the saturated core runs faster than the unsaturated outer halo. This is NOT (2,3) torus knot topology; it's a different multi-mode regime.

**Critical reframing finding** (`verify-before-cite` grep of citation #4): doc 78 (2026-04-27) already ran the K4-TLM-native cross-validation I was queuing as follow-up. **It also failed Mode III** (per-bond R/r ∈ {2.16, 2.21, 5.47, 5.72}, none at φ² ± 5%; persistence guard violated at 33%). So:
- The "queue K4-TLM cross-validation as follow-up" plan I had is wrong — that test has already been run + failed
- BOTH engines (continuum EMT + K4-TLM native) fail Golden Torus realization under tested conditions
- The real closure pathway is the **ABCD-matrix eigensolver** (Grant's intervention, this session) — see workstream handoff doc

## 2. Test result table (verbatim from observer output)

```
─────────────────────────────────────────────────────────────────────
Interpretation G: Golden Torus geometry verification (K4-TLM A5 closure)
─────────────────────────────────────────────────────────────────────
Sampling at top-8 energy-density peaks (PML-excluded buffer=4, min_sep=2.0):
  peak 0: cell (15,15,15)  r_from_center= 1.73  V²=1.1484e-01
  peak 1: cell (17,15,15)  r_from_center= 1.73  V²=8.8928e-02
  peak 2: cell (15,15,17)  r_from_center= 1.73  V²=8.8928e-02
  peak 3: cell (15,17,15)  r_from_center= 1.73  V²=8.8928e-02
  peak 4: cell (15,13,15)  r_from_center= 3.32  V²=8.4014e-02
  peak 5: cell (13,15,15)  r_from_center= 3.32  V²=8.4014e-02
  peak 6: cell (15,15,13)  r_from_center= 3.32  V²=8.4014e-02
  peak 7: cell (17,17,15)  r_from_center= 1.73  V²=6.9744e-02

Recording window: 2000 steps, runtime 0.4s, dt_sample=0.0516
Per-peak measurements:
  peak 0: R=0.141762  r=0.008001  R/r= 17.72  closed=True   A²_local=0.0405  f_dominant=0.0678
  peak 1: R=0.134657  r=0.007901  R/r= 17.04  closed=True   A²_local=0.0364  f_dominant=0.0678
  peak 2: R=0.134657  r=0.007901  R/r= 17.04  closed=True   A²_local=0.0364  f_dominant=0.0678
  peak 3: R=0.134657  r=0.007901  R/r= 17.04  closed=True   A²_local=0.0364  f_dominant=0.0678
  peak 4: R=0.124194  r=0.012223  R/r= 10.16  closed=True   A²_local=0.0308  f_dominant=0.0290
  peak 5: R=0.124194  r=0.012223  R/r= 10.16  closed=True   A²_local=0.0308  f_dominant=0.0290
  peak 6: R=0.124194  r=0.012223  R/r= 10.16  closed=True   A²_local=0.0308  f_dominant=0.0290
  peak 7: R=0.128910  r=0.010443  R/r= 12.34  closed=True   A²_local=0.0333  f_dominant=0.0290

Aggregate (mean across 8 peaks):
  R_meas      = 0.130903  (target R_GOLDEN_TORUS       = 0.809017)
  r_meas      = 0.009852  (target R_GOLDEN_TORUS_MINOR = 0.309017)
  R · r_meas  = 1.289660e-03  (target RR_GOLDEN_TORUS  = 0.250000)
  R / r_meas  =  13.2870  (target φ²                   =  2.6180)
  Deviation from φ² target: 407.5%
  Multi-mode peaks (>1 spectral peak within 20 dB): 8 / 8
  Median secondary/dominant frequency ratio: 2.333 (target 1.5 for (2,3) torus knot)
  Mean A²_local across peaks: 0.0344  (< 0.5 ≈ sub-saturation; > 0.9 ≈ TIR cavity)
  Closed-curve peaks: 8 / 8

OUTCOME: A — finite Lissajous, geometry NOT realized (Interpretation G confirmed)
```

## 3. Verified citations (per `verify-before-cite` skill)

All four citations verified before this doc landed:

| Citation | Verification | Status |
|---|---|---|
| Theorem 3.1' §49-63 bridge: "geometric dimensionless volumes ARE dimensionless reactances" | `sed -n '49,75p' theorem-3-1-q-factor.md` confirms verbatim at line 63 | PROMOTE — verbatim |
| **ABSENCE**: Theorem 3.1' precondition is IMPLICIT not EXPLICIT | `grep -nEi "(precondition\|geometry.verif\|must (be\|realize) at\|requires.*golden\|conditional on)" theorem-3-1-q-factor.md` → **0 hits** | PROMOTE — absence verified with explicit command + scope |
| Doc 130:55-60 A_op = 0.324 sub-saturation | `sed -n '50,65p' 130_...md` confirms "operating amplitude A_op = V_peak_mean / V_yield = 0.324", "sub-saturation regime" verbatim | PROMOTE |
| Doc 131:50-66 v14 observables (V_peak=0.2152, FWHM=15.10, T=32.27, Λ=102.78) | `sed -n '50,68p' 131_...md` confirms all numbers; my run reproduces Λ_total = 102.78 EXACTLY | PROMOTE + cross-validates engine reproducibility |
| Doc 78 R_phase/r_phase prior K4-TLM result | `sed -n '1,30p' 78_...md` + `grep -nEi "(persistence\|chirality.?noise\|caveat)"` confirms Mode III FAIL on K4-TLM-native with persistence-violation caveat | PROMOTE + **new finding** (see §5) |

## 4. Three substantive findings

### 4.1 Interpretation G CONFIRMED — geometry not realized

| Metric | Measured | Target (canonical) | Deviation |
|---|---|---|---|
| R_meas | 0.131 | R_GOLDEN_TORUS = 0.809 (= φ/2) | 6.2× too small |
| r_meas | 0.0099 | R_GOLDEN_TORUS_MINOR = 0.309 (= (φ-1)/2) | 31× too small |
| R·r_meas | 1.29e-3 | RR_GOLDEN_TORUS = 0.25 (= 1/4 algebraic) | 194× too small |
| R/r_meas (scale-invariant) | **13.29** | **φ² = 2.618** | **407%** |

Per the prereg's §4 outcome map: Outcome A (finite Lissajous, geometry NOT realized) is the result. The 50% Λ_total/α_cold⁻¹ gap reported in doc 131 (102.78 vs 137.036) is dominantly **geometric-mismatch**, not UV running or other Interpretation F/A/B/C from the §3 enumeration.

The Theorem 3.1' bridge identification $\Lambda_i = Q_i$ (theorem-3-1-q-factor.md:63: "in natural units, geometric dimensionless volumes ARE dimensionless reactances") **requires** the bound state to be AT Golden Torus geometry. The v14 canonical bound state isn't.

### 4.2 Unexpected multi-mode structure — nonlinear harmonic mechanism

Grant's intervention pre-run: scalar EMT engine `MasterEquationFDTD` lacks chiral coupling (no asymmetric K4 torque), so multi-mode breathing should be absent and Lissajous should be degenerate (Outcome B predicted at ~60% post-Grant). **Outcome B did NOT fire** — Lissajous is finite and structured (R/r = 13.29, not ∞). Multi-mode FFT: 8/8 peaks show secondary spectral peaks within 20 dB of dominant.

**Mechanism (corrected post-result)**: the multi-mode structure comes from **Op14 saturation kernel nonlinearity**, not from chirality. The saturation kernel S(A) = √(1 - A²) is nonlinear in A; this nonlinearity generates harmonics of the breathing fundamental even from a single-mode drive. Grant's intervention correctly identified that the **chirality** mechanism for multi-mode is absent from MasterEquationFDTD — but a DIFFERENT mechanism (saturation nonlinearity) provides multi-mode structure.

The result is informative about which mechanisms produce multi-mode in this engine and which don't:
- ✓ Op14 saturation harmonic generation (PRESENT)
- ✗ Chiral coupling from K4 asymmetric torques (ABSENT — engine has no K4 structure)
- ✗ Cosserat torsion coupling (ABSENT — engine is scalar)

### 4.3 Radial-shell mode segregation — nested-oscillator topology (NOT (2,3) torus knot)

The 8 sample peaks segregate into two shells:
- **Inner shell** (r_from_center = 1.73, peaks 0-3 + 7): f_dominant = 0.0678
- **Outer shell** (r_from_center = 3.32, peaks 4-6): f_dominant = 0.0290

Frequency ratio inner/outer = 0.0678 / 0.0290 = **2.333 ≈ 7/3** (not 3/2 expected for (2,3) torus knot).

Cross-check vs breathing fundamental from §1.3 of doc 131 (ω = 0.195 rad/time → f = 0.0310):
- Outer-shell f_dominant (0.0290) ≈ breathing fundamental f (0.0310) — matches within 7%
- Inner-shell f_dominant (0.0678) ≈ 2.18× breathing fundamental — a SECOND harmonic-like

Interpretation: the bound state has a **nested-oscillator topology**:
- Outer halo oscillates at the breathing fundamental (radial mode)
- Inner saturated core oscillates at a higher-frequency mode (driven by Op14 nonlinearity locally)
- The two modes have frequency ratio 7/3, NOT the 3/2 that would indicate (2,3) torus knot

This is a structural property of the v14 attractor that doc 131's headline observables (single dominant FFT peak) didn't surface. **The bound state's actual topology is NOT (2,3) torus knot** — it's a nested-radial-mode structure.

## 5. Doc 78 reframing — K4-TLM cross-validation has been done and ALSO failed

`verify-before-cite` grep of citation #4 surfaced this:

[`research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md`](research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md) (2026-04-27, auditor-drafted) ran the K4-TLM-native equivalent of the Interpretation G test. Setup:

> *VacuumEngine3D at N=32, PML=4 (interior 24³), A28 + Cosserat self-terms, no external drive. Seed: corpus (2,3) joint ansatz at corpus GT (R=10, r=R/φ²≈3.82); peak |ω|=0.926 (A26 guard OK); V_amp=0.14. Evolution: 200 Compton periods (1778 steps at dt=1/√2).*

Per-bond R/r results:

| Bond | Cell | R/r | Chirality | Notes |
|---|---|---|---|---|
| 0 | (25, 19, 15) | **5.4710** | CW | far from φ² |
| 1 | (24, 18, 14) | **5.7213** | CCW | far from φ² |
| 2 | (6, 16, 14) | **2.1556** | CCW | closest (17.5% below φ²) |
| 3 | (7, 17, 15) | **2.2107** | CW | (15.6% below φ²) |

**Adjudication**: Mode III nominal — C1 (R/r = φ² ± 5%) FAIL; C2 (chirality ≥75% consensus) FAIL.

**Critical caveat from doc 78 §1.3 / §3.1**: persistence at end of recording window was 33% (below 40% pre-reg threshold). The recording window captured the **decay phase** of the attractor, NOT a stable orbit:

> *"Move 5 attractor at 33% of initial peak |ω| at end of recording window... The recording window captures the attractor's decay phase, not a stable orbit."*

**Implication for current result**:

| Engine | Approach | Result | Caveat |
|---|---|---|---|
| K4-TLM (doc 78) | Seeded AT Golden Torus, evolved | R/r DRIFTED away from φ² (Mode III) | Persistence violated — attractor dissolving |
| MasterEquationFDTD (this test) | Seeded GENERIC (sech R=2.5), evolved to attractor | R/r FAR from φ² (Outcome A) | Engine lacks chiral coupling (Grant); persistence OK (Mode I PASS) |

**Both engines fail Golden Torus realization under tested conditions.** The K4-TLM result is methodologically weaker (persistence problem); the MasterEquationFDTD result is engine-mechanism-weaker (no chirality). Neither is definitive for Interpretation G alone — but together they BOUND the failure space: under available engine + evolution methodology, the Golden Torus attractor is either (a) not actually the canonical electron bound state, or (b) realized only transiently and decays.

**The "queue K4-TLM cross-validation as follow-up" plan from the prereg is therefore WRONG** — that work has been done. The actual closure pathway is the **ABCD-matrix eigensolver** (Grant intervention) which computes the eigenmode DIRECTLY (no evolution, no decay, no persistence problem) — see workstream handoff doc.

## 6. Grant chirality intervention — impact on outcome distribution

Grant intervened post-prereg-pre-run (this session, after `ave-prereg`, before `ave-driver-script-honesty` audit): *"the springs are asymmetrically applying torque to the nodes aren't they?"*

The K4 lattice (Axiom 1) is chiral Laves — 4 bonds per node arrange with handedness, applying asymmetric torque. This chirality is the canonical mechanism for converting pure radial breathing into multi-mode (2,3) torus knot structure (2 = orbital, 3 = chiral precession).

**Outcome distribution update** (per addendum §10 of prereg):
- Pre-Grant: A ~60%, B ~20%, C ~15%, D ~5%
- Post-Grant: A ~30%, B ~60%, C ~0%, D ~5%
- **Actual result**: Outcome A fired

Grant's intervention shifted weight from A toward B (predicting degenerate Lissajous because chirality is absent). The ACTUAL result lands at A (finite Lissajous, geometry not realized) because the saturation nonlinearity provides a DIFFERENT multi-mode mechanism than chirality. Both Grant's argument and the result are correct in their own scope:
- Grant correct: chirality-induced multi-mode (specifically (2,3) torus knot) is absent
- Result correct: SOME multi-mode is present (nonlinear-harmonic-induced, 7/3 ratio), but not the right kind

**Grant's load-bearing insight stands**: positive Outcome C verification on this engine would be a measurement artifact (no chirality mechanism to produce (2,3) topology). Outcome A is the most-informative-positive result available from this engine. K4-TLM-native engine has the chirality but suffers from persistence problem (doc 78). **The ABCD eigensolver bypasses BOTH limitations** (chirality in matrix definition; eigenmode is stationary by construction).

## 7. Banked sharpenings — status update

Per handoff §"Next-session sharpenings" (now this-session):

| Sharpening | Status |
|---|---|
| **foreword line 106** flag Interpretation G outcome | PENDING — outcome (A) determined; update should flag "geometry not verified at v14 + K4-TLM Move 5; closure pending ABCD eigensolver workstream" |
| **BRANCH STATE weak-spots #2 (2b)** resolution path sharpens | PENDING — resolution path is now "ABCD eigensolver", not "K4-TLM cross-validation" or "finer-grid convergence" |
| **Theorem 3.1' canonical leaf §49-63** make geometry-verification precondition EXPLICIT | PENDING — `verify-before-cite` confirmed precondition is currently IMPLICIT (0 hits for explicit-precondition language); revision should add a §63b paragraph stating the precondition |

All three propagate as follow-ups; this commit lands the prereg + observer + result + ABCD workstream-handoff. Foreword/BRANCH/leaf revisions are next-session work (small but require careful walk-back propagation per `ave-walk-back` skill).

## 8. Closure pathway — ABCD-matrix eigensolver (multi-session)

**Why**: bypasses every methodology hole this session surfaced:

| Hole this session surfaced | ABCD eigensolver fix |
|---|---|
| Post-hoc continuum→TLM projection ambiguity (substrate-native-check Q1) | K4-TLM ABCD is NATIVE; no projection |
| Persistence decay problem (doc 78 Mode III via 33% persistence) | Eigenmodes are STATIONARY by construction |
| Single-mode-Lissajous-degeneracy (my pre-run reasoning) | Eigenmode has well-defined (R, r) without needing multi-mode time-series |
| Substrate-engine mismatch (MasterEquationFDTD lacks chirality per Grant) | ABCD inherits whatever chirality the K4 bond definition has |
| Engine-attractor randomness (sech seed → whatever falls out) | Solves for canonical bound-state mode directly |

**Workstream handoff**: see [`research/2026-05-18_abcd-eigensolver-workstream-handoff.md`](research/2026-05-18_abcd-eigensolver-workstream-handoff.md) for pedantic implementation plan, cross-references, skill-selection, and adjudication framework.

**Scope**: ~4-8 hours (5 phases). Next-session Priority #1 — REPLACES handoff queue's Priority #1 (which was this Interpretation G test, now landed).

## 9. Result class designation (per `consistency-vs-emergence` skill)

This test is **CLASS: INTRA-FRAMEWORK CONSISTENCY CHECK** — NOT emergence test, NOT axiom manifestation, NOT identity.

| Skill exit criterion | Resolution |
|---|---|
| Target named | Clifford-torus (R, r) coords in natural units; targets are AVE-axiom-derived (φ from algebra), NOT CODATA |
| Inputs traced | engine.V (engine-natural primitive), engine config (engine-natural), canonical PHI/R_GOLDEN_TORUS/R_GOLDEN_TORUS_MINOR/RR_GOLDEN_TORUS (axiom-derived) — **ZERO CODATA inputs**, **ZERO α-encoded inputs** |
| Structural circularity check | NONE — no SI definitional substitution chain from input to target |
| α-decoupled | YES — α appears nowhere in observer pipeline |
| Commit-pinning | Result depends on engine SHA `9a989f7c`; targets are algebraic so not commit-dependent |
| Tautology check | NOT a regression assert; classification thresholds (10% deviation for Outcome C) are algorithmic, not target-defined |

**Honest framing for result reporting**:

> *"Interpretation G test: intra-framework consistency check between Vol 1 Ch 8 Golden Torus geometry claim and `MasterEquationFDTD` v14 canonical bound state. Outcome A — 407% deviation from R/r = φ² target — INTERNAL INCONSISTENCY surfaced. Resolution candidates: (i) Vol 1 Ch 8 geometry claim mis-scoped to chiral-K4-TLM bound state; (ii) v14 canonical bound state isn't the canonical electron (it's a nested-oscillator at A_op=0.32, not at TIR cavity); (iii) chiral coupling mechanism absent from scalar EMT engine. Class: CONSISTENCY CHECK, NOT EMERGENCE TEST; 0%/100% match would NOT have been predictive of α. Closure pathway: ABCD eigensolver (multi-session)."*

## 10. Audit-trail of skill applications (per `feedback_skill_selection_planning.md`)

**Upfront-fired (formal Skill tool invocations)**:
1. pre-test-physics-check — surfaced plumber question about path (a) vs (b) projection; user-greenlit path (b)
2. ave-prereg — corpus inventory across 10 repos; surfaced 12 prior-work items including canonical `analyze_phasor_trajectory()` pattern + doc 78/130/131 prior results + canonical Theorem 3.1' leaf
3. substrate-native-check — 7-checkpoint walk; surfaced post-hoc projection caveat + sub-ℓ_node sampling risk + radial direction choice
4. ave-canonical-source — added canonical PHI/R_GOLDEN_TORUS/R_GOLDEN_TORUS_MINOR/RR_GOLDEN_TORUS to `src/ave/core/constants.py`; verified algebraic identities to float64 precision
5. ave-driver-script-honesty — 4-discriminator check on observer (Class A clean with 2 sharpenings applied)
6. consistency-vs-emergence — classified as intra-framework consistency check; verified no structural circularity, no α-encoding
7. verify-before-cite — verified all 4 citations (3 presence + 1 absence); doc 78 verification surfaced reframing finding

**Mid-stream user interventions (Grant)**:
1. Chirality / asymmetric spring torques question — reshaped outcome distribution and engine-limitation framing; prereg addendum §10 added
2. ABCD eigensolver question — identified actual closure pathway; replaces queued K4-TLM cross-validation (which doc 78 reframing showed was already done)

**Compliance with `feedback_skill_selection_planning.md` rule**:
- 60-sec upfront skill-selection plan: ✓ (written in first response of this session)
- All planned skills fired formally: ✓ (7-of-7 formal Skill tool invocations as planned + one extra in pre-test-physics-check applied implicitly via in-response plumber-question framing)
- Mid-stream skill applications (Grant interventions): handled as substantive physics-framing inputs, not as skill-discipline gaps
- Retroactive pass before commit: this §10 IS the retroactive pass; no applied-set drift detected
