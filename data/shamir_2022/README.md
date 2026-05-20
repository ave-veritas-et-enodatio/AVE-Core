# Shamir 2022 DESI Legacy Spin Directions — Canonical Data Cache

External research data reference for AVE-Core C5 cross-catalog validation. This catalog is **NOT** in the AVE-Core workspace as a downloadable file: per the Shamir 2022 data-availability statement, the full annotated catalog of ~1.287 million spiral galaxies is provided "upon reasonable request" from the corresponding author only — there is no public mirror at MNRAS supplementary materials, Zenodo, OSF, or the author's institutional page.

This README captures the catalog metadata + paper-quoted load-bearing results that the cross-catalog validation analysis depends on.

## Source paper

**Shamir, L., 2022, "Analysis of spin directions of galaxies in the DESI Legacy Survey", MNRAS 516(2):2281-2291. DOI: 10.1093/mnras/stac2372.**

- Online publication: <https://doi.org/10.1093/mnras/stac2372>
- Journal URL: <https://academic.oup.com/mnras/article/516/2/2281/6678564>

## Methodology

- **Classification algorithm**: Ganalyzer — a deterministic image-processing pipeline that converts galaxy images to radial intensity plots, applies peak detection to identify galaxy arms, then uses linear regression on peak positions to determine spin direction. Positive slope -> clockwise; negative slope -> counterclockwise. No machine learning, no crowdsourcing.
- **Imaging dataset**: DESI Legacy Imaging Surveys (DECaLS + BASS + MzLS), accessed via <https://www.legacysurvey.org/>. The DECaLS DR8 component is the largest contributor.
- **Sample size**: ~1.287 million spiral galaxies (Shamir 2022 abstract + §2).
- **Statistical method**: chi-square fit of the per-galaxy chirality signs against cos(gamma) for every integer (RA, Dec) grid point; significance sigma established via 1000 Monte Carlo randomizations of the sign assignment.
- **Chirality convention**: clockwise/counterclockwise as viewed from Earth (galaxy image orientation). Matches Galaxy Zoo 1 convention.

## Paper-quoted results (Table 3, Shamir 2022)

The paper reports a single best-fit dipole axis per survey, with asymmetric 1sigma uncertainty boxes derived from chi-square contours on the (RA, Dec) integer grid:

| Data set | RA (deg) | Dec (deg) | sigma | RA 1sigma range | Dec 1sigma range | Galactic (l, b) |
|---|---|---|---|---|---|---|
| DESI Legacy Survey | 63 | -39 | 8.8 | -2 to 118 | 6 to -90 | (242.10, -46.91) |
| DECam | 57 | -10 | 4.7 | 22 to 92 | -39 to 56 | (199.19, -45.09) |
| SDSS | 69 | 56 | 4.6 | 19 to 107 | 25 to 77 | (150.75, 5.78) |
| Pan-STARRS | 47 | -1 | 1.9 | 4 to 117 | -73 to 40 | (180.12, -48.11) |

Galactic conversion verified via astropy.coordinates.SkyCoord ICRS->galactic with default frame definitions.

## Catalog access — structural blocker for live-fire re-analysis

The Shamir 2022 data availability statement reads (paraphrasing): "Annotated DESI Legacy Survey data will be provided upon reasonable request" (corresponding author: lshamir@mtu.edu). The paper does **NOT** redistribute the per-galaxy CW/CCW classifications via a public URL.

Surveyed public sources (this session, 2026-05-19):
- MNRAS supplementary materials (DOI 10.1093/mnras/stac2372): no supplementary data files.
- Zenodo: no Shamir 2022 DESI catalog record.
- Author's institutional page <https://people.cs.ksu.edu/~lshamir/data/>: only `assym_72k/` (SDSS dataset for Iye et al. 2021 reproduction, not the DESI Legacy 1.287M catalog).
- GitHub: no `lshamir/desi_legacy` or similar repository identified.

**Consequence**: the cross-catalog validation cannot run a live-fire re-fit on the Shamir 2022 catalog under this brief's scope (single-session, ~3 hr). The analysis falls back to **paper-quoted-axis comparison** — taking Shamir's published best-fit axis + 1sigma box as the cross-catalog datum, comparing to SDSS DR17 (l=129, b=79) sigma=6.83. This is the same epistemic class as the original Longo 2011 / Shamir 2020 literature-pin path that the C5 driver `cmb_axis_alignment_executable_observer.py` already used before E1c empirically refit it.

The brief's outcome E classification ("CATALOG-METHODOLOGY: Catalogs incomparable") is partially triggered by this structural surface — but **not in the same way as GZ-DECaLS Outcome E** (which had no chirality observable at all). Shamir 2022 DOES have chirality direction with a convention matching GZ1; the blocker is access not measurement.

This Outcome-E surface is documented in the result doc + surfaced for orchestration adjudication.

## Comparison to GZ1 / SDSS DR17

The brief's empirical question: "Does Shamir 2022 (Ganalyzer on DECaLS DR8) independently recover the SDSS DR17 spin axis at (l=129, b=79), sigma=6.83 within combined uncertainty?"

Loadbearing inputs (verified 2026-05-19):
- AVE SDSS DR17 (this corpus, E1c at `cmb_axis_alignment_executable_observer.py` corpus pin + `c5_sdss_spin_orientation_results.json`): (l=129.00, b=79.00), sigma=6.83. Method: Longo 2011 cos-gamma axial dipole on Galaxy Zoo 1 (Lintott+2011) crowdsourced +/-1 chirality, ~63k SDSS DR7 spirals post-Q-cuts (delta_clear=0.4).
- Shamir 2022 DESI Legacy: (l=242.10, b=-46.91), sigma_proxy ~ 42 (1sigma-box-radius in galactic).
- Methodological independence (per brief): different catalog (DESI Legacy vs SDSS DR7), different methodology (Ganalyzer vs crowdsourced GZ1), different imaging (DECaLS DR8 + BASS + MzLS vs SDSS DR7). All three independence axes hold.
- Convention compatibility: BOTH catalogs use clockwise/counterclockwise from Earth's image-plane perspective. No convention flip.

## Cross-checked alternative sources

| Catalog | Available? | Sample size | Verdict |
|---|---|---|---|
| **Shamir 2022 DESI Legacy** (this README) | NO — upon-request | 1.287M | Paper-quoted-axis fallback |
| **Shamir 2020 ApJ SDSS DR8 + Pan-STARRS** | partial | ~170k SDSS + ~33k Pan-STARRS | Smaller; SDSS DR8 imaging overlap (not the brief's "different imaging" requirement) |
| **GZ DECaLS Walmsley+2022** | YES (Zenodo 4573248) | 314k | No chirality observable (see `research/2026-05-19_c5-gz-decals-spin-orientation-scoping.md`) |
| **Shamir's `assym_72k/` SDSS** | YES (author's page) | ~72k | Iye et al. 2021 reproduction dataset, not the brief's "different imaging" requirement |

## Sources

- Primary paper: Shamir, L., MNRAS 516(2):2281-2291 (2022), <https://doi.org/10.1093/mnras/stac2372>
- DESI Legacy imaging portal: <https://www.legacysurvey.org/>
- Ganalyzer methodology paper: Shamir, L., 2011, ApJ 736:141 (radial intensity peak detection algorithm)

## Used by

- `src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation.py` — C5 Shamir 2022 cross-catalog validation
- `research/2026-05-19_c5-shamir-2022-cross-catalog-prereg.md` — pre-registration
- `research/2026-05-19_c5-shamir-2022-cross-catalog-result.md` — result + cross-catalog matrix

## License

Shamir 2022 DESI Legacy results are published under MNRAS scientific use license. Cite Shamir 2022 (MNRAS 516:2281) when using paper-quoted values in derived work.
