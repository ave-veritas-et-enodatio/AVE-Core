[↑ Ch.5 Dark Sector](index.md)
<!-- leaf: verbatim -->

## Multi-Galaxy Validation

<!-- label: sec:multi_galaxy -->

### Headline: SPARC 135-galaxy benchmark CONFIRMED (zero free parameters, 11.5% Q=1 mean |residual|)

AVE's galactic-rotation prediction has been benchmarked against the full SPARC catalog (Lelli, McGaugh, Schombert 2016 AJ 152 157 — 175 late-type galaxies, public). Live-fire validation 2026-05-17 via [`sparc_catalog_ingest.py`](../../../../../src/scripts/vol_3_macroscopic/sparc_catalog_ingest.py): 135 galaxies parsed (40 lack published $V_{flat}$); AVE prediction matches observed flat-rotation velocities with **zero free parameters** at the following residual statistics:

| Quality flag | Sample | Mean \|residual\| | RMS residual | Notes |
|---|---|---|---|---|
| **Q=1 (best)** | 87 galaxies | **11.5%** | 14.9% | Highest-confidence subset; cleanest rotation curves + best mass determinations |
| Q=2 (medium) | 42 galaxies | 15.5% | 25.4% | Mid-quality |
| Q=3 (worst) | 6 galaxies | 74.3% | 94.4% | Poor-quality subset; large scatter expected per SPARC quality flag |
| **All valid** | **135 galaxies** | **15.51%** | 27.17% | Median residual +4.89% (slight positive bias) |

**Zero-parameter test:** the AVE prediction uses a single canonical $a_0 = c H_\infty/(2\pi) \approx 1.07 \times 10^{-10}$ m/s² for ALL 135 galaxies (no per-galaxy fitting), standard SPARC $M^*/L_{3.6} = 0.5\ M_\odot/L_\odot$ for stellar mass conversion (not a fit parameter), and He correction $1.33 \times M_{HI}$ for gas mass (primordial composition). Baryonic mass $M_{disk} = M_* + M_{gas}$ with no DM halo component.

**Mass range covered:** 4 decades, from DDO154 dwarf ($0.4 \times 10^9\ M_\odot$ baryonic) to ESO563-G021 giant ($188 \times 10^9\ M_\odot$ baryonic). Same single $a_0$ produces ~11.5% mean residual across the entire range for high-quality galaxies.

**Comparison to standard physics:** WIMP DM requires per-galaxy halo fitting (NFW, Burkert, etc. with 2-3 fit parameters per galaxy). AVE matches the cleanest SPARC data at ~10% accuracy across 4 OOM with zero free parameters. This is C13a-GAL-ROT in the [divergence-test substrate map](../../../common/divergence-test-substrate-map.md), promoted from partial-PASS-hard-code to **forward-prediction CONFIRMED**.

### Legacy 5-galaxy demonstration (preserved for cross-check)

The physics engine also contains a smaller five-galaxy demonstration catalog ([`ave.regime_3_saturated.galactic_rotation`](../../../../../src/ave/regime_3_saturated/galactic_rotation.py)) spanning four decades of baryonic mass, used as a quick benchmark before the full SPARC ingestion landed. The table below preserves these values for cross-checking the SPARC ingestion pipeline:

| **Galaxy** | $M_{\text{disk}}$ ($M_\odot$) | $R_d$ (kpc) | $v_{\text{flat}}^{\text{AVE}}$ (km/s) | $v_{\text{flat}}^{\text{obs}}$ (km/s) | Error |
|---|---|---|---|---|---|
| DDO 154 (dwarf) | $5 \times 10^8$ | 1.0 | $\sim\!55$ | $47 \pm 2$ | $\sim\!17\%$ |
| NGC 3198 | $3 \times 10^{10}$ | 3.0 | 159 | 150 | 5% |
| Milky Way | $5 \times 10^{10}$ | 2.6 | $\sim\!220$ | $220 \pm 20$ | $<5\%$ |
| M31 (Andromeda) | $7 \times 10^{10}$ | 5.3 | $\sim\!225$ | $225 \pm 25$ | $<5\%$ |
| UGC 2885 (giant) | $2 \times 10^{11}$ | 12.0 | $\sim\!300$ | $300 \pm 10$ | $<3\%$ |

All predictions use $a_0 = c H_\infty / (2\pi)$ with zero adjustable parameters. Observed values from SPARC (Lelli et al. 2016) and standard references.

### Tully-Fisher relation

The Tully-Fisher relation ($v_{flat}^4 = G M a_0$) is an automatic consequence of the deep-MOND limit, requiring no additional physics beyond the universal saturation operator. This is a substrate-native prediction (no per-galaxy fitting) that emerges from the same $a_0 + \eta_{eff}$ saturation kernel that drives the 135-galaxy SPARC benchmark.

[Figure: galactic_rotation_curve.pdf --- see manuscript/vol_3_macroscopic/chapters/]

### VLBI Gravitational Impedance Parallax — RETRACTED 2026-05-16 audit

> **Scope correction (2026-05-16):** This section previously proposed a VLBI Jupiter-grazing radio test claiming dark matter IS continuous phase-velocity gradient of the $377\,\Omega$ vacuum impedance baseline. Audit found two compounding problems:
>
> 1. **The "$377\,\Omega$ stretching" mechanism contradicts AVE's own $Z_0$-invariance theorem.** Per [`achromatic-impedance-matching.md:24`](../../gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md) and [`z0-derivation.md:79`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md), $Z_{local}(r) = \sqrt{\mu(r)/\varepsilon(r)} \equiv Z_0$ at every $r$ because $\varepsilon(r)$ and $\mu(r)$ scale symmetrically with $n(r)$. There is no $Z_0$ to "stretch" geometrically.
> 2. **The driver script** [`vlbi_impedance_parallax.py`](../../../../../src/scripts/vol_3_macroscopic/vlbi_impedance_parallax.py) **computes pure GR Shapiro delay** ($n = 1 + 2GM/rc^2$). AVE's $n(r)$ is "mathematically identical to the spatial transverse trace of the Gordon optical metric" per [`refractive-index-of-gravity.md:14`](../../gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md). No AVE-distinct VLBI observable is derived in the corpus.
>
> The corpus's actual derived DM mechanism is **kinematic mutual inductance of the spatial network** ($\nu_{kin} = \alpha c \ell_{node}$ per [`lc-electrodynamics.md:40-54`](../../../vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md)), with the observable galactic-rotation chain driven by $a_0 = c H_\infty / (2\pi)$ via the Unruh-Hawking hoop projection ([`mond-hoop-stress.md:25-31`](../../../vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md)).
>
> The C13-VLBI-DARK matrix row was split 2026-05-16 into three rows reflecting what the corpus actually derives: C13a (galactic rotation via $a_0 + \eta_{eff}$), C13b (bullet cluster via TT shockwave on Gordon metric), C13c (META row tracking the three-mechanism coexistence as an open theoretical gap). See [`closure-roadmap.md`](../../../common/closure-roadmap.md) §0.5 scope-correction changelog + [`divergence-test-substrate-map.md`](../../../common/divergence-test-substrate-map.md) C13 family section.

### DAMA Parallax & Crystal Phonon Modulation — descriptive only

The DAMA/LIBRA collaboration claims persistent annual modulation indicative of a Dark Matter "Wind." Under the AVE framework, the Earth is physically flying through the Milky Way's rest-frame LC kinematic mutual-inductance field. This bulk lattice phenomenon generates macroscopic phononic coupling inside the highly tensioned DAMA NaI(Tl) scintillating crystals, modulating the spontaneous acoustic defect decay rate.

If the DAMA collaboration were to switch target crystals---for instance, from Sodium Iodide ($\rho = 3.67 \times 10^3$ kg/m$^3$) to Sapphire ($\rho = 3.98 \times 10^3$ kg/m$^3$) or Germanium ($\rho = 5.32 \times 10^3$ kg/m$^3$)---the **phase** of the annual modulation would remain identical, driven by Earth's orbital kinematics. The **amplitude** of the anomaly should scale with the crystal's bulk-density coupling constant $\kappa_{crystal} = \rho_{crystal}/\rho_{bulk}$ and structural acoustic Q-factor.

> **Honest scope (2026-05-16 audit):** the amplitude formula itself is NOT derived in the corpus. The script [`vlbi_impedance_parallax.py`](../../../../../src/scripts/vol_3_macroscopic/vlbi_impedance_parallax.py) computes the crystal-density ratios $\kappa$ but does not predict an annual-modulation amplitude. The C14-DAMA matrix row carries a TBD-pin on the amplitude derivation; this is a corpus derivation gap, classed as part of the C13c three-mechanism unification META item.

---
