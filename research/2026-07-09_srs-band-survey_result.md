# RESULT — srs 3D band survey (Bloch/Ybus): **band top = π√3 ω_C ≈ 5.441 ω_C, NO full gap**

**Date:** 2026-07-09 · **Branch:** `analysis/x31-srs-band-survey` (off main @ #602) · **Task:** #31 Fork B
**Prereg (FROZEN):** [`research/2026-07-09_srs-band-survey_prereg_FROZEN.md`](2026-07-09_srs-band-survey_prereg_FROZEN.md)
**Driver:** [`src/scripts/vol_1_foundations/srs_band_survey.py`](../src/scripts/vol_1_foundations/srs_band_survey.py)
**Data:** [`research/2026-07-09_srs-band-survey_result.json`](2026-07-09_srs-band-survey_result.json) (= driver `_output/srs_band_survey.json`) · **Figure:** `src/scripts/vol_1_foundations/_output/srs_band_survey.png`
**Class (consistency-vs-emergence):** **CONSISTENCY / characterization.** A measurement of the substrate's
own linear band structure (generic power-network eigenvalue math). NOT a falsification, NOT an emergence
claim. Band scale ω_C = c₀/ℓ_node is an IDENTITY; 1/√3 is a known geometric OUTPUT (Class-B manifestation).

---

## 0. TL;DR

The scalar-channel Bloch survey of the 4-site BCC primitive cell of the chiral srs (I4₁32, z=3) vacuum net
resolves the band top the x29 settle-result left open:

- **GLOBAL BAND TOP = π√3 ω_C = 5.4414 ω_C = 2.781 MeV**, at the **H point** (2π/a)(1,0,0) of the BCC zone
  (μ = −3, λ = 6). Closed form: `π / ANALYTIC_NETWORK_FACTOR`.
- **GAP INVENTORY: NO full stop-band.** The four scalar bands form a single connected manifold
  0 → 5.441 ω_C (all adjacent envelopes overlap). "No gap" is the first-class result.
- **Γ-point acoustic structure:** one acoustic branch (ω = 0) + a **triply-degenerate optical multiplet at
  3.3093 ω_C** (= √3·arccos(−1/3)).
- **All three validation gates PASS** (velocity factor 1/√3 to 3e-9; λ_max = 6.000000 vs direct
  `build_srs_net`; band count = 4; both enantiomorphs identical).

**The load-bearing finding (flag-don't-fix):** the naive "graph-Laplacian ω=√λ" band model — which the task
brief sketched and which the x29 review's three quick methods implicitly assumed — gives the **wrong
velocity factor (1/√2)** and is NOT substrate-native. The substrate-native srs vacuum is a **distributed LC
transmission-line network**; its dispersion is `ω = ω_link·arccos(μ/3)` (the coined-quantum-walk spectral
map of the Op5 scatter+connect), which recovers the canonical **1/√3** exactly. Under it the true global
band top is **π√3 ω_C ≈ 5.44**, notably **above** the prior "≈3.3–3.5 ω_C" estimate — because that estimate
was the **Γ-optical / [001]-zone-edge fold** (arccos(−1/3)·√3 = 3.309), not the global maximum (at H).

---

## 1. Gate ledger (all PASS — survey VALID)

| Gate | Condition | Result (right enantiomorph) | Pass |
|---|---|---|---|
| **(i) acoustic 1/√3** | low-k velocity factor v/c_link = `ANALYTIC_NETWORK_FACTOR` (1e-4), isotropic | **0.5773503** vs 1/√3 = 0.5773503 (err **3.0e-9**); dir-spread < 1e-9 | ✅ |
| **(ii) λ_max cross-check** | global max of λ_n(k)=3−μ_n(k) = direct `build_srs_net` λ_max = 6.000 (1e-3) | Bloch **6.000000** = direct **6.000000** (mean degree 3.000) | ✅ |
| **(iii) band count** | exactly 4 bands ∀k; both enantiomorphs identical | 4 everywhere; R/L spectra identical to 1e-9 | ✅ |

Gate (i) is not decorative: it *selects the model*. The bare graph Laplacian (ω=√λ) fails it (gives 1/√2,
see §4); only the transmission-line arccos map passes, and it is that map which fixes the ω_C normalization.

---

## 2. Band structure (the deliverable)

Bands are ω_n(k) = ω_link·arccos(μ_n(k)/3), ω_link = ω_C/(1/√3) = √3·ω_C, μ_n = eigenvalues of the 4×4
Bloch adjacency A(k). Envelopes over a dense sample of one reciprocal (FCC) primitive cell:

| band | ω range (ω_C) | note |
|---|---|---|
| 0 (acoustic) | [0.000, 2.132] | linear from Γ, v=c₀ (factor 1/√3 vs c_link) |
| 1 | [1.655, 3.309] | |
| 2 | [2.132, 3.787] | |
| 3 | [3.309, **5.441**] | reaches the global top at H |

**High-symmetry values (ω_C):** Γ = {0, 3.309×3}; H = {2.132×3, **5.441**}; N = {1.264, 2.132, 3.309, 4.178};
P = {1.655×2, 3.787×2}. Band diagram: `_output/srs_band_survey.png` (Γ–H–N–Γ–P–H path, white house style).

**GAP INVENTORY (complete):** band0↔1, band1↔2, band2↔3 all **OVERLAP** → **no full stop-band anywhere**.
The manifold is connected 0 → 5.441 ω_C. The spectrum is symmetric in λ about λ=3 (bipartite srs graph:
μ↔−μ), but the arccos map makes ω asymmetric; the top (μ=−3, the "π-mode") sits at H.

---

## 3. The three consumers

- **(a) FORK A tone placement.** The two-tone difference-frequency drive tones must sit **ABOVE 5.441 ω_C**
  (the true 3D srs band top), with ω_a − ω_b in-band. **Recommended: ω_a ≈ 6.94 ω_C, ω_b ≈ 5.94 ω_C**
  (both clear 5.441; difference 1.0 ω_C is well in-band). ⚠ The old superband run placed tones above
  **2 ω_C** (the 1D-chain *lumped* band top) — that is **≈2.7× too low** for the real 3D srs net. Any FORK-A
  two-tone protocol on the actual scatter+connect engine must clear 5.441 ω_C, not 2 ω_C.
- **(b) FPB-corner marker #1 revision.** Band edge = **2.781 MeV**. Pair threshold 2ω_C = **1.022 MeV**.
  **Measured ordering: 2ω_C (1.022 MeV) < band-top (2.781 MeV).** ⇒ the AC→DC / pair-production channel opens
  **BELOW** the band top: propagating scalar lattice modes **coexist** with the pair channel in the
  **1.022 – 2.781 MeV** window. (Smooth modes do NOT stop where pair conversion begins.)
- **(c) gap-breather flag.** **NO full gap exists** ⇒ gap-localized (gap-breather) carrier candidates are
  **UNAVAILABLE** in the scalar srs channel. First-class negative for the mobile-carrier search: srs cannot
  host a gap-pinned-vs-mobile discriminator because it has no gap.

---

## 4. Substrate-native model finding (the headline flag — flag-don't-fix)

Two distinct scalar band models exist on the srs net; they agree at k→0 velocity to first order for a 1D
chain but **disagree for the srs multi-band cell**:

| model | operator | srs velocity factor | 1D-chain band top | srs band top |
|---|---|---|---|---|
| **lumped** (mass-spring / tight-binding) | ω = √λ, λ = eig(3I−A) | **1/√2 = 0.7071** ✗ | 2 ω_C | √12 = 3.464 ω_C |
| **distributed** (transmission-line / TLM) | ω = ω_link·arccos(μ/3) | **1/√3 = 0.5774** ✓ | π ω_C | **π√3 = 5.441 ω_C** |

- The **actual srs vacuum dynamics** is the Op5 scatter+connect TLM (`chiral_lattice_dynamics.py`), which
  measures **0.5778 ≈ 1/√3** (`network_velocity_factor` on `build_srs_net`). Its dispersion is exactly the
  distributed transmission-line one: at a shunt node, KCL on ℓ_node lines gives A(k)V = 3cos(βℓ)V ⇒
  ω = (c_link/ℓ)·arccos(μ/3), and near the band bottom arccos(1−λ/3) → √(2λ/3) = kℓ/√3 ⇒ v = c_link/√3 = c₀.
- The **bare graph Laplacian ω=√λ** (the model the x29 review's three quick methods and the task brief
  sketched) gives **1/√2** for srs — a genuine geometric fact (the srs acoustic Laplacian curvature is
  C = 1/2, not 1/3). It is only the ω→0 *lumped* limit and is **not** the substrate-native vacuum.
- **Decision (flagged, not silent):** the survey uses the transmission-line arccos map. λ_max = 6 (gate ii)
  is preserved (λ = 3−μ). This deviates from the task brief's literal "graph Laplacian ω=√λ"; the deviation
  is forced by gate (i) and is the substrate-native repair. Surfaced to Grant (§6).

This also revises the x29 note ([`2026-07-09_superband-carrier-fork_result.md`](2026-07-09_superband-carrier-fork_result.md):167–170):
its "≈3.3–3.5 ω_C … √6 ≈ 2.449 raised by the 1/√3-network factor" conflated two things. The **√6 = 2.449**
is the *lumped* √λ_max (wrong model). The **3.3–3.5** is the **Γ-optical / [001]-zone-edge value**
arccos(−1/3)·√3 = **3.309** — matching the settle-result's [001] `band_top_omega = 1.9105 rad/step`
([`2026-06-16_k4-zone-edge-nyquist-settle_result.json`](2026-06-16_k4-zone-edge-nyquist-settle_result.json):25;
1.9105·√3 = 3.309). Neither is the **global** top; the H-point global top is **π√3 = 5.441 ω_C**. The settle
verdict "K4-CUTS-AT-~π/ℓ_node" (line 14) is the *k-space* zone-edge cutoff; the corresponding **ω** cutoff is
π·ω_link (the first Bragg / half-wave-line resonance) — physical, not a temporal-Nyquist artifact.

---

## 5. Vector / Cosserat channel — STRETCH, scoped (secondary)

Attempted: the 12×12 primitive-cell dynamical matrix (4 sites × 3 DOF), RANK-2 bond tensor
Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂) at the isotropic-bond (photon) point. **Band count = 12** everywhere (3 acoustic
+ 9 optical), acoustic structure isotropic. **NOT completed as a band-top survey:** this elastic matrix is the
*lumped* mass-spring model (ω=√eig); the transmission-line arccos correction that the SCALAR channel required
for the canonical 1/√3 (§4) is **not** applied here. **Deferred** — the vector band-top in ω_C units needs its
own acoustic-velocity gate (the shear vs longitudinal c_s/c_l network factors) plus the arccos map derived for
the 3-DOF port scatter. What's needed to finish: (i) the per-branch (longitudinal/transverse) velocity gate
against the canonical shear-network factor; (ii) the coined-walk spectral map for the 3-DOF Op5 node; (iii)
the BCC-path 12-band diagram. Estimate: a full follow-on arc, not a within-session addendum.

---

## 6. Flags surfaced to Grant (one physics question + one model deviation)

1. **Which speed is the physical c₀?** (pre-test-physics question). Adopted **R2**: c₀ = the long-wavelength
   acoustic-branch velocity (= c_link/√3), the emergent measured light speed, so ω_C = c₀/ℓ_node = 511 keV.
   The microscopic bond/link speed c_link = √3·c₀ is super-luminal, sub-lattice, unobservable. Under R2 the
   1D chain and srs share one formula and the 1D top stays a clean π ω_C in the transmission-line model. If
   instead c_link were called c₀ (R1), every ω_C band label divides by √3 (band top → π = 3.142 ω_C). R2 is
   the physically-defensible reading; **only the ω_C *scale label* changes under R1**, not the k-space band
   SHAPE or the gap inventory. Flagged for adjudication.
2. **Model deviation from the task brief** (§4): brief said "graph Laplacian ω=√λ"; gate (i) forces the
   transmission-line arccos map. Adopted the arccos map (substrate-native, passes 1/√3). Flagged.

---

## 7. Consistency-vs-emergence + corpus-state consequence

Per the frozen classification: **CONSISTENCY / characterization.** ω_C = c₀/ℓ_node is an IDENTITY (`OMEGA_C`,
constants.py:294); 1/√3 is a Class-B geometric MANIFESTATION (`ANALYTIC_NETWORK_FACTOR`,
chiral_lattice_dynamics.py:48). Every gate is COMPUTED vs an independently-derived canonical number (velocity
factor vs the imported symbol; λ_max vs the direct `build_srs_net` graph Laplacian), not asserted. No α/Q_TANK
on any verdict path; constants by SYMBOL; forward computation only.

**Corpus-state consequence (for the auditor to land, not this lane):** the x29 superband result's band-top
note (§5, lines 167–170) — "true 3D srs top ≈ 3.3–3.5 ω_C, √6 raised by the 1/√3 factor" — is **superseded**:
(a) the 3.3–3.5 value is the Γ-optical/[001] fold (arccos(−1/3)·√3 = 3.309), not the global top; (b) the
global top is **π√3 = 5.441 ω_C = 2.781 MeV** at H; (c) the "√6 raised by 1/√3" reasoning used the lumped
√λ model, which fails the 1/√3 gate. This is a **ledger row + a correction to the superband §5 note**, surfaced
to the auditor's manuscript / COLLABORATION_NOTES queue; the manual entry is the auditor's to land (lane
discipline). No leaf edit from this lane.
