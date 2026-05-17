# 126 — Q-G47 19+ Standing-Wave Eigenmode Verification: FIRST-PASS scope discovery

**Date:** 2026-05-16 late evening
**Branch:** `research/l3-electron-soliton`
**Status:** **FIRST-PASS SCOPE DISCOVERY** — r7_k4tlm_scattering_lctank.py as-is tests electron-soliton bound-state (Mode III FAIL per cached run 2026-05-16 12:19), NOT the K=2G magic-angle operating point. Different physics. Doc 125 §5 1-2 session estimate UNDERESTIMATED scope. Need to either (a) extend r7 with K=2G seed configuration, OR (b) build new K=2G operating-point eigenmode script.
**Per Grant directive 2026-05-16 late evening**: "A" — execute Option A.

---

## §0 TL;DR

Ran Option A per doc 125 §5 (extend r7_k4tlm_scattering_lctank.py with operating-point eigenmode extraction). Honest finding: r7 as-currently-implemented is tuned for the **electron-soliton bound-state question** at Golden Torus geometry (R = 10.0, r = φ²·10/φ²), NOT the **K=2G magic-angle operating point question** at substrate scale.

**r7 cached results (2026-05-16 12:19)**:
- V-block: 20 eigenvalues clustered at phase 0.7158 rad (1.2% off target 0.7071 = ω_C·dt)
- Cos-block: eigenvalues in 0.038-0.15 range (NOT at ω_C² = 1.0)
- Adjudication: **Mode III** — "No eigenmode at ω_C at any tested seed. (2,3) representation needs structural rework OR bound state hybrid V≠0∧ω≠0 (Round 8)"

**This is the ELECTRON-SOLITON eigenmode result, not the K=2G magic-angle result.** The two questions are different physics:
- Electron-soliton question: does a bound (2,3) state exist on K4-TLM at ω_C? (Mode III FAIL → bound-state requires Master Equation FDTD per A-027 two-engine architecture)
- K=2G magic-angle question: does the substrate's standing-wave eigenmode amplitude equal u_0* = 0.187 at the K=2G operating point? (UNTESTED — different seed configuration needed)

**Scope correction**: doc 125 §5's "1-2 session" estimate underestimated. The work requires either:
- (a) **Extend r7 with K=2G operating-point seed configuration** (1-2 sessions) — uses existing infrastructure but with substrate-scale (not bound-state) seed
- (b) **Build new K=2G eigenmode script** (2-3 sessions) — clean implementation specifically for K=2G operating-point question

---

## §1 What r7 actually tests (electron-soliton bound state)

Per `r7_k4tlm_scattering_lctank.py:36-50, 91-95`:

- Builds VacuumEngine3D with `temperature=0.0, amplitude_convention="V_SNAP"`, Cosserat self-terms enabled
- Seeds with `seed_2_3_hedgehog(R=10.0, r=3.82)` — Golden Torus geometry for electron-soliton (2,3) trefoil
- Builds K4-TLM scatter+connect operator T = C·S(z_local) per Op14 z_local from Cosserat A²
- Eigsolves V-block (target eigenvalue at unit circle phase 0.7071 = ω_C·dt)
- Eigsolves Cos-block (K_cos · δψ = ω²·M_cos · δψ; target eigenvalue ω² = 1)

**This tests**: does the K4-TLM substrate (sub-saturation engine per A-027) host the (2,3) electron-soliton bound state at ω_C?

**Per A-027 two-engine architecture** (canonical 2026-05-16): K4-TLM is sub-saturation; bound states need Master Equation FDTD. So r7's Mode III FAIL is EXPECTED — the bound-state belongs in the other engine.

**This is NOT what the Q-G47 19+ verification is asking.**

---

## §2 What the Q-G47 19+ verification actually needs

Per doc 124 §1.1 + doc 125 §1:
- Compute the standing-wave eigenmode of the K4 substrate at the **K=2G magic-angle operating point** (u_0 = 0.187)
- Verify amplitude = 0.187 (matching A-029)
- This is a SUBSTRATE-SCALE eigenmode question, NOT a bound-state-soliton question

The K=2G operating point is per Vol 3 Ch 1:17-23: $p^* = 8\pi\alpha \approx 0.183$ bond occupation fraction, $z_0 \approx 51.25$ amorphous coordination, K=2G trace-reversal operating point.

The relevant eigenmode is the **substrate's natural standing wave at K=2G** — not the electron-soliton's (2,3) trefoil bound state.

**Different seed needed**: instead of `seed_2_3_hedgehog(R=10.0, r=3.82)` (electron Golden Torus geometry), need a uniform-K4-substrate seed at the K=2G operating point. The substrate has bonds at the over-bracing length $r_{\text{secondary}}/d = 1.187$; the eigenmode of THIS configuration is what should give u_0* = 0.187.

---

## §3 Three paths forward

### §3.1 Path A — Extend r7 with K=2G operating-point seed (~1-2 sessions)

**What**: take r7's existing T = C·S construction + Cos-block Hessian-of-W, but seed with a uniform-K4 configuration at K=2G operating point (NOT the electron-soliton (2,3) seed). Compute eigenmodes, extract K, G from eigenmode-perturbed state per Session 12-15 uniform-strain protocol, identify eigenmode at K=2G.

**Estimated effort**: 1-2 sessions
- ~2 hr: write `seed_uniform_K2G(engine)` function (uniform Cosserat configuration at substrate K=2G operating point)
- ~2 hr: extend `eigsolve_V_block` + `eigsolve_Cos_block` outputs with K/G ratio extraction per eigenmode
- ~2 hr: identify eigenmode at K=2G, read off amplitude, compare to 0.187

**Risk**: r7's T = C·S operator may be tuned to bound-state regime (Op14 z_local from Cosserat A² assumes the (2,3) seed structure). May need to also re-implement build_T_operator with K=2G operating-point assumptions.

### §3.2 Path B — Use Q-G47 Sessions 12-15 discrete K4 scaffold + add eigenmode (~1-2 sessions)

**What**: take Sessions 12-15's existing discrete K4 scaffold (computes K_0, G_0 via uniform-strain protocol), ADD eigenvalue computation of the mass-stiffness matrix M⁻¹·K, identify standing-wave eigenmode at K=2G, read off amplitude.

**Estimated effort**: 1-2 sessions
- ~2 hr: re-instantiate Session 12-15 scaffold (existing code in AVE-QED `src/scripts/q_g47_*`)
- ~2 hr: add scipy.linalg.eigh on mass-stiffness matrix
- ~2 hr: extract eigenmode at K=2G operating point, compare to 0.187

**Risk**: Session 16 explicit flag that Sessions 12-15 scaffolds have discretization artifacts ("K_0 = 12 baseline, central-force instability, Keating ratio as free piece"). The eigenmode result may inherit these artifacts.

### §3.3 Path C — Build new analytical K=2G eigenmode (continuous-field per Session 17, ~2-3 sessions)

**What**: write the continuous Cosserat micropolar field equations on K4-symmetric geometry per Session 17. Solve analytically for standing-wave eigenmodes. Identify the one at K=2G operating point. Read off amplitude.

**Estimated effort**: 2-3 sessions
- ~3 hr: set up continuous Cosserat PDE on unit K4 cell with periodic boundary conditions
- ~3 hr: separate variables / Floquet analysis to find eigenmodes
- ~2 hr: identify K=2G eigenmode + amplitude extraction

**Risk**: PDEs may not separate cleanly; analytical closed form might require simplifying assumptions that lose the magic-angle physics (same risk as doc 125 §3.2 Option B).

---

## §4 Recommendation

**Path B** is now my recommended approach (replacing doc 125's Path A recommendation):

1. **Session 12-15 scaffolds are RIGHT physics**: they're substrate-scale K4 elastic-network calculations (NOT bound-state soliton like r7)
2. **Adding scipy.linalg.eigh** to the existing scaffold is incremental (~50 lines of code)
3. **Session 16 discretization-artifact concerns are real BUT manageable**: the artifacts are KNOWN (K_0/G_0 = 3 not 5/3 in scaffold; need sublattice relaxation or Keating bond-bending per Session 14-15), and can be addressed by using the Session 15 stabilized scaffold

**Path A** would require substantial re-implementation of r7's build_T_operator for K=2G seed; not significantly less work than Path B.

**Path C** is cleanest analytically but riskiest (PDE separation may not close).

---

## §5 Why doc 125 §5's "1-2 session" estimate was wrong

Doc 125 §5 said: "extend r7 with operating-point eigenmode amplitude check, ~1-2 sessions." This assumed r7's existing infrastructure was directly extensible to the K=2G question. After actually inspecting r7:

- r7 IS for electron-soliton bound state (different question)
- r7's T = C·S operator uses Op14 z_local from Cosserat A² (which assumes (2,3) seed structure)
- For K=2G substrate-scale eigenmode, need uniform-substrate seed (NOT bound-state seed)

**The scope discovery is**: r7's existing infrastructure is more specialized than I read from its docstring. The "eigenmode finder" framing is true but specifically for bound-state-at-(2,3)-Golden-Torus, not for substrate-scale-K=2G-operating-point.

This is the ave-prereg discipline working as designed — corpus-grep revealed the actual scope of existing tooling, which differs from initial estimate.

---

## §6 Next move

**For Grant adjudication**:

(a) Execute Path B — extend Q-G47 Sessions 12-15 discrete scaffold with scipy.linalg.eigh eigenmode extraction. 1-2 sessions. Uses substrate-scale physics (not bound-state) and existing scaffold code.

(b) Execute Path A — adapt r7 with K=2G operating-point seed configuration. 1-2 sessions but requires re-implementing build_T_operator. Higher risk.

(c) Execute Path C — build continuous-field analytical eigenmode. 2-3 sessions. Cleanest if it works.

(d) Reconsider — maybe the verification question itself needs reframing per the LC-cavity standing-wave reframe (Picture A): if u_0* IS the standing-wave eigenmode amplitude tautologically (per the K4 cavity geometry), then there's nothing to "verify" beyond the geometric identity r_secondary/d - 1 = u_0* = 0.187 = p*/8π (or however these connect). Sessions 19+ work might be confirming the IDENTITIES rather than computing an independent eigenmode.

My read: **Path B + Path D framing concurrently**. Do Path B as the concrete computation (~1-2 sessions), but frame the result per Picture A — the eigenmode amplitude SHOULD be 0.187 by cavity geometry; the computation verifies the K4 standing-wave actually has that amplitude (not as an independent prediction, but as a structural-consistency check).

---

## §7 Status of doc 125 + doc 124

**Doc 125 plan needs §5 update**: the 1-2 session Path A estimate underestimated scope; Path B is now recommended.

**Doc 124 verification status**: STRUCTURAL PASS (per LC-cavity standing-wave reframe in primer Q-G47 section) stands. Picture A interpretation (one physical quantity expressed multiple ways) means the verification is PASS by structural identity at the framework level. The concrete numerical computation of u_0* = 0.187 from K4 standing-wave eigenmode is what Path B would deliver — confirming the identity holds quantitatively.

---

## §8 Cross-references

- [doc 124 — Q-G47 19+ verification attempt (STRUCTURAL PASS)](124_q_g47_19_verification_attempt.md)
- [doc 125 — K4 standing-wave eigenvalue derivation plan](125_k4_standing_wave_eigenvalue_plan.md) — needs §5 update per this doc's scope discovery
- `src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py` — tested electron-soliton bound state (Mode III FAIL, expected per A-027)
- `src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank_results.json` — cached run 2026-05-16 12:19 (electron-soliton seed, NOT K=2G operating point)
- AVE-QED `docs/analysis/2026-05-15_Q-G47_session12_k4_cosserat_numerical.md` — discrete K4 scaffold reference for Path B
- AVE-QED `docs/analysis/2026-05-15_Q-G47_session15_stabilized_scaffold.md` — stabilized scaffold with Keating bond-bending
- AVE-QED `docs/analysis/2026-05-15_Q-G47_session17_continuous_lc_from_axioms.md` — continuous-field framework for Path C
- [trampoline-analogy-primer.md Q-G47 section (LC-cavity reframe)](../../manuscript/ave-kb/common/trampoline-analogy-primer.md) — Picture A framing
