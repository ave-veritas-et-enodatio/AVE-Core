# CMB Axis Alignment Driver — Design + Phase-1 Verification

**Branch:** `analysis/cmb-axis-alignment-driver` (off `research/l3-electron-soliton` at `317faf3`)
**Goal:** Build the executable observer for the framework's **sharpest empirical commitment** — the 3-route framework commitment (foreword line 121-129) that requires α + G + 𝒥_cosmic to converge on the same magic-angle operating point $u_0^*$. This is rank #1 in the operational triage at [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — more leverage than HOPF-02a, LIGO ringdown, or CLEAVE-01.

Tests matrix row **C5-CMB-AXIS** + the 𝒥_cosmic cascade meta-test that affects C4-THREE-ROUTE.

---

## §1 Target — 7 observables that should all align with $\hat{\Omega}_{freeze}$

Per [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) (frozen 2026-05-15, extended 2026-05-16 with observables 6 + 7):

| # | Observable | Predicted alignment with $\hat{\Omega}_{freeze}$ | Primary data source |
|---|---|---|---|
| 1 | CMB axis-of-evil | $\hat{\Omega}_{freeze} \approx (l=174°, b=-5°)$ in galactic coords | Planck PR3 quadrupole-octupole alignment |
| 2 | Hubble flow anisotropy | Aligns with $\hat{\Omega}_{freeze}$ | Pantheon+ supernova dipole |
| 3 | LSS galaxy rotation | Aligns with $\hat{\Omega}_{freeze}$ | SDSS DR17 spiral-galaxy chirality |
| 4 | Matter asymmetry | Aligns with $\hat{\Omega}_{freeze}$ | Galactic plane / antimatter survey direction |
| 5 | CMB E/B polarization decoupling | Anomalous decoupling along $\hat{\Omega}_{freeze}$ if parent K/G ≠ 2 | Planck PR3 polarization + BICEP/Keck |
| 6 | Orbital-plane alignment | Solar-system ecliptic + binaries + galactic disks + LIGO inspirals all align | JPL + Gaia DR3 + SDSS + LIGO GWTC |
| 7 | CODATA G anisotropy | $P_2(\cos\theta)$ residual; amplitude $A \approx 4.4 \times 10^{-5}$ at $\alpha^2$-suppression | CODATA 2022 G compilation |

**Pass criterion (4-axis):** all 4 primary axes align to within combined error margins, at $> 3\sigma$ vs isotropic null.

**Fail criterion (sharpest):** **CMB axis vs Hubble flow misaligned by $> 20°$ at $> 3\sigma$ kills A-034 cosmic-scale claim and the 3-route framework commitment.**

## §2 Why this is the highest-leverage test in the framework

Per the master synthesis at [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) "Master Cross-Cascade Synthesis" section:

> The CMB+SDSS axis-alignment driver closes the 3-route framework commitment (foreword line 121-129). A single test simultaneously falsifies (or strengthens) the entire single-cosmological-parameter theory. Pre-reg already frozen 2026-05-15. Free public data. **More leverage than any single-anchor test.**

Specifically: a misalignment fail doesn't just kill one row's prediction — it kills the framework's claim that one cosmological IC parameter $\Omega_{freeze}$ generates α, G, and 𝒥_cosmic via the same magic-angle operating point. The framework would degrade from "one-cosmological-parameter theory with 3 observational windows" to "multi-parameter EFT."

## §3 Phases of driver work

### Phase 1 — Angular-separation computation against literature axes (this session)

**Scope:** Numpy-only. Build the canonical machinery:
- Galactic-coord → Cartesian unit-vector conversion
- Angular separation between two galactic-coord vectors (arccos of dot product)
- Compare $\hat{\Omega}_{freeze} = (l=174°, b=-5°)$ against literature-cited published axis positions for each of observables 1-4
- Print alignment matrix + flag which alignments are < 20° (PASS), 20-45° (AMBIGUOUS), > 45° (FAIL)
- Honest TBD-pin-source flags for each observable's axis citation

**Substrate:** [`src/scripts/vol_3_macroscopic/cmb_axis_alignment_driver.py`](../src/scripts/vol_3_macroscopic/cmb_axis_alignment_driver.py)

**Acceptance:** computes mutual angular separations of all 7 observable axes vs $\hat{\Omega}_{freeze}$ + cross-pair separations. Surfaces honest assessment of which literature values are well-pinned vs disputed.

### Phase 2 — Raw-data fetch + statistical analysis (next session)

- Install `healpy` + `astropy`
- Fetch Planck PR3 CMB temperature + polarization maps from PLA (`pla.esac.esa.int`)
- Fetch Pantheon+ supernova dipole catalog
- Fetch SDSS DR17 spiral-galaxy chirality catalog
- Re-derive each axis independently from raw data (Bayesian fit or quadrupole-octupole alignment statistic)
- Statistical significance vs isotropic null at $> 3\sigma$

### Phase 3 — CODATA G anisotropy P_2 fit (Observable 7)

- Pull CODATA 2022 G compilation + underlying ~15-20 publications
- Extract lab coordinates + apparatus orientation + measurement time
- Convert to galactic-coord measurement-direction $\hat{n}_{measurement}$
- Chi-squared fit $G(\hat{n}) = G_0 [1 - A P_2(\cos\theta)]$
- Predicted $A \approx 4.4 \times 10^{-5}$ ($\alpha^2$-suppression) per [`research/_archive/L3_electron_soliton/118_omega_freeze_tensor_extension_vol3ch1.md`](_archive/L3_electron_soliton/118_omega_freeze_tensor_extension_vol3ch1.md)
- Distinguishes 6 outcomes (A through F) per prereg §1.7

### Phase 4 — Outcome propagation

- Update [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) C5-CMB-AXIS row:
  - Outcome: TBD → PASS / AMBIGUOUS / FAIL based on Phase 2/3 results
  - Substrate: MISSING → this driver
  - Comparison source: TBD pin → specific Planck/Pantheon+/SDSS/CODATA datasets pinned
- Update C4-THREE-ROUTE row (foreword commitment status)
- Update D4-A034 cosmic-instance row

## §4 Branching decision

This branch is `analysis/cmb-axis-alignment-driver` off `research/l3-electron-soliton`. Same rationale as `analysis/ligo-ringdown-driver`:
- main lacks the prereg + the canonical 𝒥_cosmic cascade content
- This branch is code-bearing (Python + astropy/healpy); separate from docs-only `analysis/divergence-test-substrate-map`

When driver lands outcomes, C5/C4 row updates can cherry-pick or merge-after.

## §5 References

- Prereg: [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) (515 lines, 7 observables, 6 outcome categories A through F)
- Canonical AVE axis prediction: [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) line 88
- 𝒥_cosmic cascade context: [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)
- 3-route framework commitment: `manuscript/frontmatter/00_foreword.tex` lines 121-129
- G anisotropy P_2 derivation: [`research/_archive/L3_electron_soliton/118_omega_freeze_tensor_extension_vol3ch1.md`](_archive/L3_electron_soliton/118_omega_freeze_tensor_extension_vol3ch1.md)
- A-031 cosmic-parameter horizon: [`manuscript/ave-kb/common/cosmic-parameter-horizon-a031-refinement.md`](../manuscript/ave-kb/common/cosmic-parameter-horizon-a031-refinement.md)
- Planck Legacy Archive: https://pla.esac.esa.int
- LIGO Open Science Center (for Observable 6e): https://www.gw-openscience.org

## §6 Phase-1 run report (2026-05-16)

### §6.1 Mechanical infrastructure works

Angular-separation computation (galactic → Cartesian → arccos) + classification thresholds (PASS < 20°, FAIL > 45°, AMBIGUOUS between) functional. Cross-pair separation matrix between all 6 observable axes computes correctly.

### §6.2 Vs AVE-predicted Omega_freeze axis (l=174°, b=-5°)

| Axis | (l, b) deg | sep vs AVE | Verdict |
|---|---|---|---|
| CMB axis-of-evil (Land+Magueijo 2005 WMAP) | (237, 63) | **82.67°** | **FAIL** |
| CMB axis-of-evil (AVE prereg-cited) | (174, -5) | 0.00° | PASS (self-cite) |
| Hubble dipole (Watkins+ 2009 bulk flow) | (295, 14) | 58.74° | FAIL |
| LSS rotation chirality (Longo 2011 SDSS) | (145, -65) | 63.43° | FAIL |
| Matter asymmetry proxy (CMB rest-frame dipole) | (264, 48) | 86.29° | FAIL |
| Ecliptic pole | (96.4, 29.8) | 81.82° | FAIL |

5 of 6 literature axes FAIL alignment with AVE prediction; only AVE's self-citation matches (tautologically).

### §6.3 Cross-pair separations (do observed axes mutually align, regardless of AVE?)

The 6 literature axes don't mutually align either — most cross-pair separations are 35-90°. **The 4-axis alignment claim is not visible in literature-best-guess values.**

One partial alignment cluster: Land+Magueijo CMB axis is 35.5° from LSS rotation chirality and 21.1° from matter asymmetry proxy — both AMBIGUOUS, not clean PASS. So there's a hint of a 3-axis loose cluster around (l≈237°, b≈63°) — but **this is 82° away from the AVE-cited (174, -5)**.

### §6.4 SURFACED FINDING — AVE corpus axis citation provenance gap

**The (l=174°, b=-5°) value cited in the AVE corpus** ([`universal-saturation-kernel-catalog.md` line 88](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md), [`omega-freeze-cosmic-grain-cascade.md` line 26](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)) **does not match the canonical CMB axis-of-evil literature value** (Land+Magueijo 2005, Phys.Rev.Lett.95:071301 → (237, 63) for WMAP quadrupole-octupole alignment).

The 82° discrepancy is too large to be measurement uncertainty. Possible explanations:
1. **AVE uses a different CMB statistic** (not Land+Magueijo's quadrupole-octupole alignment). The corpus needs to cite which one explicitly.
2. **AVE cites a coordinate-system error** — (174, -5) might be antipodal to (237, 63) under a sign convention difference. **Check:** (237+180, -63) = (417, -63) = (57, -63), not (174, -5). So not antipodal flip.
3. **The AVE value is AVE-derived** (not from CMB measurement directly) — e.g., a Cosserat-axis projection or parent-BH spin-axis estimate. If so, the comparison-to-CMB is non-trivial and the prereg's "CMB axis-of-evil at (174, -5)" wording is misleading.

**This is a load-bearing corpus citation gap** that affects the framework's sharpest empirical commitment. The 3-route framework commitment test depends on this axis being well-defined; if the AVE-cited (174, -5) is not actually the canonical CMB axis-of-evil literature value, the prereg needs revision.

### §6.5 Phase 2 action items

Before raw-data fetch, the corpus citation gap must be resolved:

1. **Pin the canonical AVE axis source** — find the paper or AVE-internal derivation that gives (l=174°, b=-5°) for the CMB axis-of-evil. If AVE uses a non-standard statistic, cite which.
2. **Decide:** does the 3-route framework commitment require alignment with Land+Magueijo (237, 63), with the AVE-cited (174, -5), with both, or with some other CMB anomaly axis?
3. **THEN** install healpy + astropy and fetch Planck PR3 maps for raw re-derivation under the chosen statistic.

For Observables 2-4 (Hubble dipole, LSS rotation, matter asymmetry):
- Each has multiple competing literature axes; raw-data refit is essential
- LSS rotation (Observable 3) may need to be dropped if modern SDSS DR17 replication of Longo 2011 is null

For Observables 5-7 (E/B, orbital, G anisotropy):
- Observable 5 (E/B): Phase 3 — needs full Planck PR3 polarization analysis
- Observable 6 (orbital): Phase 3 — needs JPL ephemeris + Gaia + LIGO aggregation; partially testable Phase 1 (ecliptic pole already done above)
- Observable 7 (G anisotropy): Phase 3 — needs CODATA G publication compilation + lab-coordinate metadata

### §6.6 Phase-1 outcome summary

- **Driver infrastructure: WORKS** (angular separations, classification, pairwise matrix all functional)
- **Literature-axis vs AVE: 5 of 6 FAIL** (using best-guess literature values)
- **Cross-pair alignment of observable axes: weak** (one 3-axis loose cluster at ~(237, 63), but no tight 4-axis alignment in current data)
- **Load-bearing finding:** AVE corpus citation gap for the (l=174°, b=-5°) value. Phase 2 cannot run a fair test until the AVE-cited axis has explicit literature provenance OR is reframed as an AVE-derived prediction (not a CMB measurement).

### §6.7 Status of matrix rows C4-THREE-ROUTE + C5-CMB-AXIS after Phase 1

**C4-THREE-ROUTE** (the foreword's framework commitment):
- Status unchanged: Route 3 (𝒥_cosmic) remains the bottleneck. Phase 1 reveals **Route 3 has an upstream corpus-gap (axis citation provenance) that must close before Route 3 driver can even run fairly**.

**C5-CMB-AXIS**:
- `Substrate` cell: MISSING → `src/scripts/vol_3_macroscopic/cmb_axis_alignment_driver.py` (this driver, Phase 1)
- `Outcome` cell: TBD → **TBD-pending-corpus-citation-resolution** (cannot move to PASS/FAIL until §6.4 gap closed)
- `Confounders` cell: add "AVE-corpus axis citation (l=174°, b=-5°) does not match canonical literature CMB axis-of-evil values (Land+Magueijo 2005 gives 237°, 63°). Phase 2 cannot fairly test until provenance pinned."

Row updates happen when this branch merges back to L3 / analysis branch.
