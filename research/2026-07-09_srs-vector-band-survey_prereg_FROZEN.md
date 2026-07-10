# PREREG (FROZEN) — srs 3D VECTOR/Cosserat-translational band survey (12-band Bloch)

**Task:** x31-B2 (Grant-fired 2026-07-09) — the deferred half of PR #604 (scalar §5), now the **FORK-A gate**
and the direct answer to Grant's "is the √3 longitudinal?" question.
**Branch:** `analysis/x31-vector-band-survey` (stacked on `analysis/x31-srs-band-survey`; retargets to main when #604 merges).
**Driver:** `src/scripts/vol_1_foundations/srs_vector_band_survey.py`
**Stacks on:** the scalar survey (`srs_band_survey.py`, `research/2026-07-09_srs-band-survey_result.md`), whose §5
deferred exactly this ("the transmission-line arccos correction plus a shear/longitudinal velocity gate are needed").

## Substrate-first sector header (stated before any standard-physics term)

- **SECTOR:** the **translational (Cauchy-grade) vector sector** of the chiral srs-z3 net (`build_srs_net`,
  I4₁32, Wyckoff-8a, z=3). 4-site BCC primitive × **3 translational DOF/site = 12 bands**. Each z=3 bond
  carries the **substrate-native RANK-2 bond tensor** Φ_b = k_a·(d̂⊗d̂) + k_s·(I−d̂⊗d̂), k_a = axial STRETCH
  (longitudinal along the bond), k_s = transverse SHEAR/bend. NOT a Cartesian Laplacian (the disabled-flag
  stencil bug). Cosserat couple-stress (microrotation) = **Stage 2, NOT invoked** — this is the Cauchy
  translational level; the true photon (T2 Cosserat microrotation) is a **named follow-on**, so the transverse
  S-branch here is its **PROXY only** (do not overclaim S = photon).
- **REGIME:** cold linear, sub-yield, **saturation OFF**. Handedness is saturation-only ⇒ cold spectra are
  parity-symmetric (both enantiomorphs identical). No Op14 local-clock modulation (no load-bearing sites).
- **READOUT COORDS (A46):** real-space / spatial-Brillouin (acoustic slopes → C_ij → per-branch velocities;
  band ω(k) over the BCC zone). The velocity-factor and band-top claims are real-space; coordinates match.
- **CLASS (consistency-vs-emergence): CONSISTENCY / characterization.** ω_C = c₀/ℓ_node is an IDENTITY
  (imported `OMEGA_C`); 1/√3 is a Class-B geometric MANIFESTATION (imported `ANALYTIC_NETWORK_FACTOR`);
  ν=2/7 is **GR-imported** (imported `N_NU`/`NU_VAC`, K=2G; PR#261/#506); √(10/3) is a manifestation of K=2G
  elasticity. NOT a falsification, NOT an emergence claim, NO CODATA fit on any verdict path. α-CLEAN.

## 0. What is computed (frozen)

The **vector (3-DOF) linear band structure** of the srs vacuum net, as a Bloch eigenvalue analysis of the
**4-site BCC primitive cell × 3 DOF (12×12)** — NO engine time-stepping. Two dispersion maps, both reported:

1. **Lumped mass-spring** ω = √eig(D(k)): the elastic-limit model (rejected for the scalar velocity by gate (i),
   retained as the low bound / shape reference).
2. **Transmission-line / normalized-arccos** (the substrate-native generalization of the scalar §4 map):
   ω/ω_C = (1/FACTOR)·arccos(1 − λ̃(k)), where λ̃ = eigenvalues of the **symmetric-normalized dynamical
   Laplacian** S_i^{-1/2} D(k) S_i^{-1/2} ∈ [0,2] (S_i = Σ_b Φ_b, the per-site self-block). This **reduces
   exactly to the scalar map** when k_a=k_s (there S_i = z·I, λ̃ = 1 − μ/z, and ω/ω_C = √3·arccos(μ/3)).

**The canonical bond ratio is IMPORTED, never hard-coded.** ρ* = k_a/k_s is DERIVED by bisection to the point
where ν_Hill(ρ) = `N_NU` = 2/7 (imported symbol) using the VALIDATED Born-Huang elastic pipeline
(`srs_elastic_tensor.py`, PR#506). Prior runs place ρ*≈9.7734 but the driver re-derives it from the symbol.

## 1. ANALYTIC EXPECTATIONS (M6 / ave-prereg v1.6 Step 3.9 — frozen WITH NUMBERS, first-class criteria)

**A run that cannot state its analytic expectations is not ready to run.** These are the frozen expected
observables. Fork-record-both is the default shape where a model choice is open.

### (i) Long-wavelength acoustic velocity family — THE √3-LONGITUDINAL ANSWER (frozen before run)

Three √-factors are in play; they are **distinct objects** and the prereg commits to which is which:

| factor | value | what it is | longitudinal? |
|---|---|---|---|
| **√3** | 1.732 | **network/coordination projection** c_link → c₀ (D=3 isotropic average over z=3), the emergent light-speed factor. Applies to **ALL** branches equally (overall scale). | **NO — universal network factor** |
| **√(10/3)** | 1.826 | **P-wave (longitudinal) acoustic** stiffness-speed ratio c_P/c_S in the **isotropic K=2G** limit: c_P²/c_S² = (K+4G/3)/G = (2G+4G/3)/G = **10/3**. Includes the 4G/3 shear stiffening. | **YES — the longitudinal branch factor** |
| **√2** | 1.414 | **A1-scalar BULK-SOUND** v_bulk = √(K/ρ) = √(2G/ρ) (`V_LONG`), the PURE-dilatation port mode that **DROPS** the 4G/3 shear term. A **scalar-sector port**, NOT a translational Bloch branch. | **NO — different sector (A1 dilatation)** |
| **1 (unity)** | 1.000 | **S/transverse (shear)** branch = c_S = √(G/ρ) = c₀ = **light-like PROXY** (true photon = T2 Cosserat, follow-on). | transverse |

**RESOLVED (before run): the vector translational P-branch should give √(10/3)·c₀, NOT √2·c₀.** The discrete
Christoffel longitudinal eigenvalue is ρc_P² = C11-family = K + 4G/3 (isotropic Hill), the FULL compressional
stiffness. The √2·c₀ bulk-sound drops the 4G/3 shear term and is the A1 scalar PORT mode (clm-uu1qbo,
cosserat-mass-gap.md) — it does not appear as a translational acoustic Bloch branch. This is exactly the
KEEP-BOTH distinction in `constants.py:764-770`.

**Frozen numeric gate (i):** at ρ*, the **isotropic (Voigt-Reuss-Hill) longitudinal/transverse eigenvalue
ratio** c_P²/c_S² = **10/3 = 3.333** (within 3% — the lattice is Zener-anisotropic A≈1.23, so per-direction
values SPREAD; e.g. [100] gives C11/C44 ≈ 2.93 → 1.71, not √(10/3); only the Hill-average recovers √(10/3)).
The **shear (S) branch velocity factor vs c_link = 1/√3** (light-like), matching the scalar acoustic.

### (ii) Scalar-limit reduction (frozen numeric)

At **k_a = k_s** the 12 vector bands = **4 scalar bands ⊗ 3** (each scalar band 3-fold degenerate), because
D(k) = L_scalar(k) ⊗ I₃. The normalized-arccos map then reproduces the scalar spectrum exactly, so the
**band top = π√3 = 5.4414 ω_C** (×3 degenerate) and the Γ-optical multiplet = 3.3093 ω_C. Gate: max
|vector_arccos_band − scalar_band⊗3| < 1e-6 at k_a=k_s.

### (iii) Band count (frozen)

Exactly **12** real ω(k) at every k (4-site × 3 DOF; no spurious/missing modes). 3 acoustic (ω→0 at Γ) + 9 optical.

### (iv) Enantiomorph identity (frozen)

Right (I4₁32) and left (I4₃32) spectra **identical to ≤1e-9** (cold parity-symmetric; a nonzero difference = bug).

### (v) ★ Band top — frozen BRACKET (fork-record-both; the model choice is open, so bound both ways)

The scalar top is π√3 = 5.441 ω_C. For the vector channel the arccos correction does **NOT cleanly generalize**
(3 acoustic branches, 2 distinct speeds, anisotropic per-site self-block ⇒ no single ω_link) — so the top is
BRACKETED (frozen expectation, computed value lands inside):
- **LOWER — normalized-arccos (substrate-native, shape-preserving):** if the srs vector normalized Laplacian is
  bipartite (λ̃_max = 2, as the scalar is), the arccos top is **pinned at π√3 = 5.441 ω_C independent of ρ**
  (the normalization absorbs stiffness into SHAPE). Expected λ̃_max ≤ 2 ⇒ top ≤ 5.441.
- **UPPER — per-channel link speed (raw stiffness):** the stiff longitudinal channel's Bragg half-wave cutoff
  scales as c_l/c_s = √(k_a/k_s) = √ρ*, giving π√3·√ρ* ≈ 5.441·√9.77 ≈ **17.0 ω_C**.
- **MIDDLE — P-wave-scaled (the #604 review's worst-case):** π√3·√(10/3) ≈ 5.441·1.826 ≈ **9.9 ω_C**.
- **MIDDLE — lumped-eigenvalue-scaled:** 5.441·√(λmax(D@ρ*)/λmax(D@ρ=1)); computed by the run.

The **owning branch/channel** is expected to be the **longitudinal (k_a-dominated) optical branch** at a BCC
zone corner (H- or P-type), NOT the shear branches.

### (vi) Gap inventory (frozen expectation)

Expected: the k_a≫k_s split may OPEN a full stop-band between the shear-dominated lower manifold and the
longitudinal-dominated upper band(s) (unlike the scalar, which had NO gap). **Fork-record-both:** any full
stop-band = **gap-breather revival territory** (first-class either way — a full gap RESTORES the gap-pinned
carrier candidate that the scalar no-gap result had killed; no gap = same as scalar). Reported whatever it is.

### (vii) Discreteness-vs-artifact pre-declaration

This is a survey-class eigenvalue analysis (NO integrator, no time-stepping), so integrator/ramp artifacts do
not arise. The only "discreteness effects" are physical Bloch band folding and the zone-edge Bragg cutoff
(π·ω_link) — these are PHYSICS (the half-wave-line resonance), not artifact. The normalization-choice ambiguity
in (v) is a **modeling** bracket, not a numerical artifact, and is reported as a bracket.

## 2. Validation gates (pre-stated — ALL must pass or the survey is VOID)

| # | Gate | Pass condition |
|---|---|---|
| **G1** | band count | exactly **12** ω(k) at every sampled k; both enantiomorphs. |
| **G2** | scalar reduction | at k_a=k_s, arccos 12-band = scalar 4-band⊗3 (band top 5.441; Γ-optical 3.309) within 1e-6. |
| **G3** | primitive-cell consistency | the 4-site BCC vector Christoffel C_ij at ρ* reproduce the VALIDATED 8-site `srs_elastic_tensor` ν_Hill = 2/7 / K=2G within 1e-3 (confirms the 4-site primitive carries the vector problem). |
| **G4** | isotropic P/S ratio | Hill c_P²/c_S² = 10/3 within 3% (the √(10/3) longitudinal expectation). |
| **G5** | enantiomorph identity | R/L spectra identical ≤1e-9. |
| **G6** | ρ* import | ρ* derived by bisection to ν_Hill=`N_NU` (NOT hard-coded); the imported-symbol path is exercised. |

## 3. Deliverables (frozen list; values filled by the run only)

(a) the **12-band diagram** (WHITE house style, BCC Γ–H–N–Γ–P–H path);
(b) ★ **the vector band top** (value, k-point, owning channel/branch) + the frozen bracket from §1(v);
(c) **per-branch long-wavelength velocity table** — the √3-longitudinal answer (which branch carries √3 vs √2
    vs √(10/3));
(d) **which acoustic branch is light-like** (S/shear = c₀ proxy) + the T2-Cosserat follow-on caveat;
(e) **full gap inventory across 12 bands** (any full stop-band = gap-breather territory, first-class);
(f) the final **fork-A tone-placement** recommendation (both tones ABOVE the TRUE/worst-case vector top;
    difference in-band).

## 4. Pre-test-physics question surfaced to Grant (one, per Rule 16 — asked BEFORE design)

**Is the vacuum's linear vector band top a SINGLE-SCALE object or stiffness-lifted?** Under the normalized-TLM
map the top is pinned at π√3·ω_C by ℓ_node + c₀ alone (stiffness only reshapes the band); under per-channel
link speeds the stiff longitudinal channel lifts the Bragg cutoff to π√3·√ρ*. The former makes the fork-A floor
IDENTICAL to the scalar (5.441); the latter pushes it to ~17. **Adopted for this survey:** report the BRACKET,
survey at the cold-vacuum ρ* (ν=2/7, K=2G matter-Poisson point), and recommend the **conservative
(stiffness-lifted) fork-A floor** so tones clear the worst case. Flagged for Grant adjudication; does not change
the band SHAPE or the gap inventory, only the fork-A tone floor.

## 5. Disciplines

Constants by SYMBOL (`OMEGA_C`, `L_NODE`, `C_0`, `HBAR`, `e_charge`, `N_NU`/`NU_VAC`, `ANALYTIC_NETWORK_FACTOR`,
`V_LONG`, `G_VAC`, `RHO_BULK`); ρ* DERIVED from `N_NU` (not hard-coded); Born-Huang elastic pipeline REUSED from
the validated `srs_elastic_tensor.py` (Rule 14); both enantiomorphs; forward computation only (gates compare to
independently-derived canonical numbers). Figure WHITE house style (`ave.viz.style.apply`, Okabe-Ito, units on
axes, legend outside data, no on-figure title). α-CLEAN — no α/Q_TANK/CODATA on any verdict path.
