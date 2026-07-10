# PREREG (FROZEN) — srs 3D band survey (Bloch/Ybus eigenvalue analysis)

**Task:** #31 Fork B (Grant-fired 2026-07-09). **Branch:** `analysis/x31-srs-band-survey` (off main @ #602).
**Driver:** `src/scripts/vol_1_foundations/srs_band_survey.py`
**Class (consistency-vs-emergence):** **CONSISTENCY / characterization.** This is a *measurement of the
substrate's own linear band structure* (generic power-network eigenvalue math), NOT a falsification test
and NOT an emergence claim. The band scale ω_C = c₀/ℓ_node is an IDENTITY (imported symbol `OMEGA_C`); the
1/√3 network factor is a known geometric OUTPUT of the tetrahedral-network dynamics (Class-B manifestation,
imported symbol `ANALYTIC_NETWORK_FACTOR`); the band top / gaps are substrate re-statements of standard
Bloch-network facts. No CODATA fit, no new primitive.

## 0. What is computed (frozen)

The **scalar channel** linear band structure of the chiral srs (Laves / (10,3)-a / Sunada-K4, I4₁32) vacuum
net, as a **Bloch/Ybus eigenvalue analysis** of the **4-site BCC primitive cell** — NO engine time-stepping.

- **Real-space object:** srs Bravais lattice = **body-centred cubic** (I-centred), 4-site basis (the first
  four Wyckoff-8a positions; the other four are the +(½,½,½) body-centre images). Bonds = the degree-3 srs
  NN bonds from `build_srs_net`, each of length ℓ_node.
- **Bloch matrix:** 4×4 Hermitian Bloch **adjacency** A(k), A_ij(k) = Σ_bonds e^{i k·δ} over the directed
  NN bonds i→j with minimum-image displacement δ. Graph **Laplacian** L(k) = 3·I − A(k) (the periodic Ybus
  in its lumped limit). μ_n(k) = eigenvalues of A(k) ∈ [−3,3]; λ_n(k) = 3 − μ_n(k) ∈ [0,6].
- **Substrate-native dispersion (the load-bearing model choice — see §4):** the srs vacuum is a **distributed
  LC transmission-line network** (Op5 shunt junctions on ℓ_node lines), whose scatter+connect (TLM) dynamics
  is the coined-quantum-walk of A(k). Its dispersion is
  **ω_n(k) = ω_link · arccos(μ_n(k)/3)**, ω_link = c_link/ℓ_node = ω_C / `ANALYTIC_NETWORK_FACTOR` = √3·ω_C.
  Equivalently **ω_n(k)/ω_C = arccos(μ_n(k)/3) / (1/√3)**. The bare lumped map ω=√λ is the ω→0 limit ONLY
  and is *rejected* by gate (i) (it gives 1/√2, not 1/√3). See §4 for the pilot that established this.
- **BZ sampling:** (a) high-symmetry BCC path Γ–H–N–Γ–P–H (–P–N); (b) dense volumetric sample over one
  reciprocal primitive cell (FCC reciprocal, b_i=2π{(0,1,1),(1,0,1),(1,1,0)}) for global extrema + gaps.

**Deliverables:** 4-band diagram; global band top (ω_C units + k-point); complete gap inventory (full
stop-bands between branches; "no gap" reported as first-class); Γ-point acoustic structure.

## 1. Validation gates (pre-stated — ALL must pass or the survey is VOID)

| # | Gate | Pass condition |
|---|---|---|
| **(i)** | acoustic 1/√3 | low-k acoustic velocity factor v(k→0)/c_link (computed from the arccos dispersion's slope, spherically averaged) equals imported `ANALYTIC_NETWORK_FACTOR` = 1/√3 within **1e-4**. Isotropic (spread < 1e-3). |
| **(ii)** | λ_max cross-check | k-summed / global max of λ_n(k)=3−μ_n(k) over the dense BZ reproduces the **direct** `build_srs_net` graph-Laplacian λ_max = **6.000** within **1e-3**. |
| **(iii)** | band count | exactly **4** eigenvalues at every k (no spurious / missing modes); both enantiomorphs identical spectra. |

## 2. Deliverable read-outs (frozen list; values filled by the run only)

- **Band top:** ω_top/ω_C and its k-point (report the high-symmetry label); band top in MeV (× 0.511 MeV/ω_C).
- **Gap inventory:** per-band [ω_min, ω_max] envelopes over the dense BZ; any full stop-band (band n max <
  band n+1 min) reported with its ω-window; explicit "NO full gap" if the manifold is connected.
- **Γ structure:** acoustic (ω=0) + optical multiplet (value + degeneracy).

## 3. The three consumers (stated now; filled by the run)

- **(a) FORK A tone placement:** the two-tone difference-frequency drive tones must sit ABOVE the true band
  top. Recommend ω_a, ω_b (in ω_C) with ω_a−ω_b in-band.
- **(b) FPB-corner marker #1 revision:** band edge in MeV; report the ORDERING vs pair threshold 2ω_C =
  1.022 MeV (does AC→DC / pair conversion open while smooth modes still propagate?).
- **(c) gap-breather flag:** if any full gap exists, gap-localized modes are carrier candidates (flag only,
  no claim). If no gap, report the mechanism is unavailable.

## 4. Substrate-native model decision (pilot record — frozen BEFORE the survey run)

A pilot (`scratchpad/proto*.py`, this session) established the load-bearing model choice:
- The **bare graph-Laplacian** dispersion ω=√λ gives srs acoustic velocity factor **1/√2 = 0.7071** — it
  **FAILS gate (i)**. It is the *lumped* limit and is NOT the substrate-native vacuum dynamics.
- The **actual srs TLM** (Op5 scatter+connect, `chiral_lattice_dynamics.network_velocity_factor`) gives
  **0.5778 ≈ 1/√3** — the canonical `ANALYTIC_NETWORK_FACTOR`. Its dispersion is the coined-walk spectral
  map ω = ω_link·arccos(μ/3), which recovers 1/√3 exactly in the k→0 limit (arccos(1−λ/3) → √(2λ/3)).
- **Therefore the survey uses the transmission-line / arccos dispersion.** This is flagged (not silently
  chosen): the task brief sketched "graph Laplacian ω=√λ"; the substrate-native fix is the arccos map, and
  it is the ONLY model consistent with gate (i). λ_max=6 (gate ii) is preserved (λ=3−μ). Surfaced to Grant
  as the one pre-test-physics question (§5).

## 5. Pre-test-physics question surfaced to Grant (one)

**Which speed is the physical c₀?** The emergent light speed c₀ = ω_C·ℓ_node is the LONG-WAVELENGTH acoustic
branch velocity (= c_link/√3), NOT the microscopic bond/link speed c_link (= √3·c₀, super-luminal, sub-lattice,
unobservable). The survey adopts c₀ = acoustic-branch continuum limit (the definition that makes ℏω_C = 511 keV
and keeps the 1D chain band top = π·ω_C in the same transmission-line model). If instead c_link were taken as
c₀ (R1 reading), every ω_C band figure divides by √3. **Adopted: R2 (c₀ = emergent acoustic speed).** Flagged
for Grant adjudication; does not change the k-space band SHAPE or the gap inventory, only the ω_C scale label.

## 6. Disciplines

Constants imported by SYMBOL (`OMEGA_C`, `L_NODE`, `C_0`, `ANALYTIC_NETWORK_FACTOR`); forward computation
only (no fitted targets — gate (i)/(ii) compare to independently-derived canonical numbers); both enantiomorphs;
figure in WHITE house style (`ave.viz.style.apply`, Okabe-Ito, units on axes, no on-figure title).
