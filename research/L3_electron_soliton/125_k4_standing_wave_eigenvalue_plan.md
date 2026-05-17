# 125 — K4 Standing-Wave Eigenvalue Derivation Plan (Sessions 19+ rigorous closure)

**Date:** 2026-05-16 late evening
**Branch:** `research/l3-electron-soliton`
**Status:** **PLAN + RESEARCH** — explicit u_0* = 0.187 as standing-wave eigenmode amplitude on K4 lattice. Substantial existing infrastructure (Option A leverages r7_k4tlm_scattering_lctank.py + doc 73 methodology). Estimated 1-2 sessions to execute per doc 124 §1.1.
**Per Grant directive 2026-05-16 late evening**: "let's proceed with 1, fully plan out and research."

---

## §0 TL;DR

The Q-G47 19+ verification per doc 124 needs explicit derivation that the K4 standing-wave eigenvalue equation produces $u_0^* = 0.187$ at the K=2G operating point. Per Grant's LC-cavity-eigenmode reframe (primer Step 2.5-6.5 + doc 122 Picture A): the substrate IS an LC resonant cavity with $u_0^*$ as the stored reactance amplitude of its standing-wave eigenmode.

**Existing infrastructure** (corpus research, this doc §2):
- `src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py` — discrete K4-TLM scatter+connect transmission operator $T = C \cdot S(z_{\text{local}})$, V-block + Cosserat (u, ω) LC-tank Hessian-of-W for Cos-block (active methodology per doc 73)
- `src/scripts/vol_1_foundations/coupled_engine_eigenmode.py` — coupled K4+Cosserat eigenmode finder on VacuumEngine3D
- `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py` — K4-only eigenmode finder (AVE-native methodology per doc 66 §17)
- `src/scripts/vol_1_foundations/r10_path_alpha_v9_discrete_eigenmode_results.json` — discrete eigenmode results from v9 path-α work
- Q-G47 Sessions 12-15 — discrete K4 scaffolds compute $K_0, G_0$ but not standing-wave eigenmodes
- AVE-QED `docs/analysis/2026-05-15_Q-G47_session17_continuous_lc_from_axioms.md` — continuous-field Cosserat recasting per Grant's "the springs are actually continuous" framing

**Recommended approach (Option A)**: extend `r7_k4tlm_scattering_lctank.py` to compute the standing-wave eigenmode at the K=2G operating point and verify amplitude = 0.187. Smallest delta from existing infrastructure. ~1-2 sessions.

---

## §1 Goal (precise)

**Derive explicitly**: the K4 lattice's standing-wave eigenvalue equation has an eigenmode at $u_0^* = 0.187$ (within tolerance, matching A-029 magic angle), and this eigenmode is the one whose amplitude balances the K=2G trace-reversal operating point.

**PASS criteria**:
- Compute eigenvalues of K4 scattering operator $T = C \cdot S$ (or equivalent K4 elastic-network mass-stiffness matrix)
- Identify the standing-wave eigenmode with K4 cubic symmetry (per v14 cubic anisotropy empirical, Grant's "cubic rebound")
- Read off this eigenmode's amplitude $u_0^{\text{eigenmode}}$
- Compare to A-029's $u_0^* = 0.187$ within ≤10% tolerance

**FAIL criteria**:
- Eigenmode amplitude differs from 0.187 by >10% → diagnostic: either the K4 scaffold model is incomplete (missing physical ingredients) or A-029's 0.187 isn't the K4 standing-wave eigenvalue (would require reframing)
- No eigenmode with K4 cubic symmetry → K4-TLM scattering operator isn't capturing the K=2G operating mode → would need different operator construction

**PARTIAL** (most likely outcome based on Session 6 §5.2):
- Eigenmode in 0.13-0.24 ballpark (matching the structural-PASS bracket from doc 124 §3) — confirms framework structurally but requires shape-function tuning for exact 0.187 match

---

## §2 Corpus research findings

### §2.1 Existing K4 eigenmode scripts

| Script | What it does | Relevance to this plan |
|---|---|---|
| `r7_k4tlm_scattering_lctank.py` | Discrete K4-TLM scatter+connect transmission operator T = C·S; eigenvalues on unit circle for V-block; Cosserat (u, ω) LC-tank Hessian-of-W for Cos-block; Op14 cross-coupling decoupled at V=0 | **Most relevant** — active methodology per doc 73, computes the LC-tank eigenmode that's the substrate's natural standing wave |
| `coupled_engine_eigenmode.py` | Coupled K4+Cosserat eigenmode finder on full VacuumEngine3D; handles energy runaway diagnostics | Backup if r7 doesn't have the right operator |
| `tlm_electron_soliton_eigenmode.py` | K4-only eigenmode finder; AVE-native methodology per doc 66 §17 | Backup; K4-only may miss the Cosserat-coupled mode |

### §2.2 Existing K4 scaffolds (Q-G47 Sessions 12-15)

Per `2026-05-15_Q-G47_session12_k4_cosserat_numerical.md`:
- Discrete K4 lattice with 4 primary bond directions + 12 secondary A→B→A' paths via shared B-nodes
- Cosserat-rod bond model (each bond has translational + microrotational DOFs)
- Computes $K_0 = 4 k_a + 8 k_s$ and $G_0 = (4/3) k_a + (8/3) k_s$ (Session 13 analytical)
- **Doesn't compute standing-wave eigenmodes** — measures effective moduli via uniform-strain protocol
- Session 12 §2.4 explicitly flags: "$\chi_K$ extraction failed because uniform strain doesn't probe the cross-coupling modes the dressing modifies"

### §2.3 Continuous-field framework (Q-G47 Sessions 16-17)

Per `2026-05-15_Q-G47_session16_continuous_field_recasting.md` and `session17_continuous_lc_from_axioms.md`:
- "Springs are actually continuous" per Grant directive
- Cosserat micropolar field equations: $\mu + \kappa = \xi_{K1} \cdot T_{EM}$, $\beta + \gamma = \xi_{K2} \cdot T_{EM} \cdot \ell_{\text{node}}^2$
- $\xi_{K2}/\xi_{K1} = 12$ from $|T|=12$ universality
- $\ell_c/\ell_{\text{node}} = \sqrt{6}$ from dimensional analysis

This gives an analytical alternative (Option B in §3) but doesn't have explicit standing-wave eigenmode computation either.

### §2.4 Master Equation FDTD (per A-027 two-engine architecture)

`src/ave/core/master_equation_fdtd.py` — bound-state engine with $c_{\text{eff}}(V)$ modulation. Doesn't currently have eigenmode-extraction capability; would need addition. Per K4-TLM canonical, the K4-TLM is the sub-saturation engine; Master Equation FDTD is the bound-state engine. For the standing-wave eigenmode AT the magic-angle operating point (which IS at saturation boundary), Master Equation FDTD is the right engine — but adding eigenmode capability to it is more work than extending r7.

---

## §3 Three candidate approaches

### §3.1 Option A — extend `r7_k4tlm_scattering_lctank.py` (RECOMMENDED)

**What it is**: add operating-point-eigenmode extraction to the existing r7 script. The discrete K4-TLM scatter+connect operator T = C·S already has the right structure; just need to identify the K4 standing-wave eigenmode with the right symmetry and read off its amplitude.

**Effort**: ~1-2 sessions
1. Read r7's existing T = C·S operator construction
2. Compute eigenvectors with K4 cubic symmetry (filter by symmetry analysis)
3. For each candidate eigenmode, compute the corresponding K/G ratio
4. Identify the eigenmode at K/G = 2 (the magic-angle operating point)
5. Read off the eigenmode amplitude $u_0^{\text{eigenmode}}$
6. Compare to A-029's 0.187

**PASS evidence**: eigenmode amplitude = 0.187 ± 10%

**Strength**: smallest delta from existing infrastructure; r7 is already validated per doc 73 methodology.

**Risk**: r7 may be set up for V-block only (not Cosserat-coupled); may need supplementing with Cosserat Hessian-of-W eigenmode from the script's other half.

### §3.2 Option B — Continuous-field analytical eigenmode (Sessions 16-17 extension)

**What it is**: solve the continuous Cosserat micropolar field equations analytically on K4-symmetric geometry. The eigenvalue equation is a PDE with known coefficients ($\xi_{K1}, \xi_{K2}, \ell_c, \nu_{\text{vac}} = 2/7$); find the standing-wave eigenmodes analytically.

**Effort**: ~2-3 sessions
1. Set up the continuous Cosserat micropolar wave equation on a unit cell with K4 symmetry
2. Identify eigenmode boundary conditions (periodic with K4 symmetry)
3. Solve eigenvalue equation analytically (possibly via separation of variables or Floquet)
4. Identify the standing-wave eigenmode at K=2G operating point
5. Read off amplitude

**Strength**: pure analytical → exact answer, no numerical artifacts.

**Risk**: continuous Cosserat micropolar field equations on K4-symmetric geometry are PDEs that may not separate cleanly; analytical closed form might require simplifying assumptions that lose the magic-angle structure.

### §3.3 Option C — Extend Q-G47 Sessions 12-15 discrete scaffolds

**What it is**: take the existing discrete K4 scaffolds (Sessions 12-15 computed $K_0, G_0$ via uniform-strain protocol) and ADD eigenvalue computation of the mass-stiffness matrix. Identify standing-wave eigenmodes and check amplitude at K=2G.

**Effort**: ~1-2 sessions
1. Re-instantiate the Session 12-15 discrete K4 scaffold (existing code)
2. Build the elastic mass-stiffness matrix M⁻¹·K explicitly
3. Compute eigenvalues + eigenvectors
4. Identify standing-wave eigenmode at K=2G operating point
5. Read off amplitude

**Strength**: leverages Sessions 12-15 existing scaffold + standard numpy eigenvalue solver.

**Risk**: per Session 16, the discrete scaffolds have discretization artifacts ("K_0 = 12 baseline, central-force instability, Keating ratio as free piece"). The continuous-field is the right physics; eigenmode of discretized version may inherit artifacts.

---

## §4 Recommendation: Option A

**Why Option A**:
1. **Smallest delta from existing code**: r7 already implements the right K4-TLM operator (T = C·S) with V-block eigenvalue problem on unit circle (per doc 73 methodology)
2. **AVE-native methodology**: doc 73 + doc 66 §17 established this as the canonical approach for substrate standing-wave fixed points
3. **Operating-point structure already there**: r7's Cosserat (u, ω) LC-tank Hessian-of-W is the right object for the magic-angle eigenmode
4. **Validated foundation**: r7 has Grant's "confirmed 6.1" approval per doc 73 §6.1 catastrophic-error carve-out

**Option B (analytical)** is cleaner but higher-risk — continuous Cosserat PDEs on K4 symmetric geometry might not yield analytical closed forms without simplifying assumptions that lose the magic-angle physics.

**Option C (Session 12-15 extension)** has known discretization artifacts (Session 16 explicit flag); fixing those is roughly as much work as Option A but with less existing validation.

---

## §5 Specific calculation steps for Option A (1-2 sessions)

### §5.1 Session-1 work (~3-4 hours)

1. **Read `r7_k4tlm_scattering_lctank.py` in detail** (~30 min): understand the T = C·S construction, the Cosserat Hessian-of-W, the eigenvalue output format
2. **Identify symmetry filter** (~1 hour): which eigenmodes have K4 cubic symmetry? (Should be a small subset — probably $|T| = 12$ rotational orbits of a base mode)
3. **Operating-point identification** (~1 hour): for each candidate eigenmode, compute the effective K/G ratio (use the existing Session 12-15 effective-moduli extraction protocol applied to the eigenmode-perturbed state)
4. **Read off amplitude** (~30 min): the eigenmode at K/G = 2 has some amplitude $u_0^{\text{eigenmode}}$; extract and compare to 0.187

### §5.2 Session-2 work (~3-4 hours) — depending on Session-1 result

**If Session-1 PASS** (amplitude = 0.187 ± 10%): 
- Document the result in research/L3 doc 126 "Q-G47 19+ standing-wave eigenmode verified"
- Update doc 122, 124 status to "CLOSED PASS"
- Update primer Q-G47 section + Step 6.5 to reflect rigorous closure
- Propagate to omega-freeze + CODATA G prereg (note framework's K=2G now rigorously closed)

**If Session-1 PARTIAL** (in 0.13-0.24 bracket but not exactly 0.187): 
- Document the partial-PASS in doc 126
- Diagnose discrepancy: is it shape-function specifics? Symmetry-filter wrong? Cosserat coupling normalization?
- Decide whether to iterate Session-1 or move to Option B/C as backup

**If Session-1 FAIL** (no eigenmode in the expected ballpark):
- Document FAIL in doc 126 with full diagnostic
- Reframe: either r7's operator doesn't capture the right substrate physics, OR A-029's 0.187 isn't the standing-wave eigenvalue
- Adjudicate next step with Grant

### §5.3 Required inputs (already in corpus per §2)

- $\chi_K = 12$ (Q-G47 Session 9, A-032)
- $\chi_G = 3$ (Session 11, T_t triplet)
- $\xi_{K2}/\xi_{K1} = 12$ (Session 17)
- $\ell_c/\ell_{\text{node}} = \sqrt{6}$ (Session 9 §5.3)
- $r_{\text{secondary}}/d = 1.187$ (A-029)
- $K_0/G_0 = 5/3$ (Cauchy baseline, Session 1+2)
- $K_0 = 4 k_a + 8 k_s$, $G_0 = (4/3)k_a + (8/3)k_s$ (Session 13 analytical)
- A-029 target: $u_0^* = 0.187$

### §5.4 Output spec

Doc 126 (NEW): "Q-G47 19+ standing-wave eigenmode verification result" with:
- PASS/PARTIAL/FAIL status
- Computed eigenmode amplitude vs A-029's 0.187
- Symmetry-class identification of the eigenmode
- Effective K/G ratio at the eigenmode operating point
- Diagnostic if PARTIAL or FAIL

---

## §6 PASS/FAIL implications

### §6.1 If PASS

- Q-G47 closure status: STRUCTURAL PASS (doc 124) → RIGOROUS PASS (this work)
- Trampoline-analogy primer §Q-G47 + Step 6.5 + "What this primer is NOT" can be updated to remove all "pending Sessions 19+" qualifications
- omega-freeze-cosmic-grain-cascade.md note that framework's K=2G is rigorously closed → δ_χ derivation can proceed independently with full substrate-physics grounding
- doc 117 §10 K_phys ~ α² conjecture can be revisited with cavity-eigenmode structure as foundation
- L5 entry: A-032 ($\chi_K = 12$) status migrates from structural-hypothesis to canonical

### §6.2 If PARTIAL

- Q-G47 status remains STRUCTURAL PASS with numerical-precision DIAGNOSED (specific discrepancy identified)
- Primer notes the partial closure with diagnostic
- Iterate Option A or move to Option B/C

### §6.3 If FAIL

- Q-G47 status DOWNGRADED to "buckling picture not the right substrate model" — framework needs reframing
- Major adjudication required: is the LC-cavity-eigenmode reframe wrong, or is A-029's 0.187 not the eigenvalue?
- doc 124 STRUCTURAL PASS may need re-examination

---

## §7 What this would close

If PASS: closes the multi-week deferred work flagged at:
- Session 5 §5.2 "explicit values of f_Cosserat, f_buckling, f_Cauchy as functions of operating-point parameters"
- Session 17:49 "individual ξ_K1, ξ_K2 values via multi-week K4 lattice integration"
- doc 122 §1 "Sessions 19+ verification calculation"
- doc 124 §5 "numerical-precision closure"

The framework's central claim — K=2G at the magic-angle operating point IS a standing-wave eigenmode of the K4 substrate (with α as the cavity weave density) — becomes rigorously established.

---

## §8 Recommended next move

Execute Option A (extend r7_k4tlm_scattering_lctank.py with operating-point eigenmode amplitude check). Session-1 (~3-4 hours): read script, identify symmetry filter, extract eigenmode amplitudes, compare to 0.187. Session-2 (~3-4 hours): document result + diagnostics.

If Grant wants Option B (analytical) or Option C (Session 12-15 scaffold extension) instead, those are viable but higher-risk per §3.

---

## §9 Cross-references

- [doc 124 — Q-G47 19+ verification attempt (STRUCTURAL PASS)](124_q_g47_19_verification_attempt.md) — defines what numerical-precision PASS means
- [doc 122 — Q-G47 19+ scope adjudication (a)+(b)](122_q_g47_sessions_19_plus_scope_adjudication.md) — Mode A construction-given, Mode B verification
- [trampoline-analogy-primer.md Q-G47 section (LC-cavity reframe)](../../manuscript/ave-kb/common/trampoline-analogy-primer.md) — Picture A confirmed via standing-wave eigenmode
- AVE-QED Q-G47 Sessions 1-17 — substrate-physics framework + discrete scaffolds + continuous-field recasting
- `src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py` — Option A foundation (existing K4-TLM scatter+connect transmission operator)
- `research/L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md` — doc 73 methodology referenced by r7
- `research/L3_electron_soliton/66_*.md` — doc 66 §17 AVE-native eigenmode methodology
- Vol 3 Ch 1:17-23 — EMT operating point $p^* = 8\pi\alpha$, $z_0 \approx 51.25$
- Vol 4 Ch 1 Theorem 3.1 — $\alpha^{-1} = Q$-factor of electron LC tank (canonical framing)
