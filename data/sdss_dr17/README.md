# SDSS DR17 Spin-Orientation Canonical Data Cache

External research data tracked here for AVE-Core reproducibility. NOT simulation output — this is a canonical observational catalog from the SDSS / Galaxy Zoo 1 collaboration.

## Files

| File | Size | MD5 | Source |
|---|---|---|---|
| `GalaxyZoo1_DR_table2.csv.gz` | 19.4 MB (gzipped, ~64 MB uncompressed) | `766cb56d64f936e00d26699a55f0669b` | [Galaxy Zoo 1 Data Release Table 2](https://data.galaxyzoo.org/) — Lintott et al. 2011 |

## Naming rationale ("sdss_dr17" not "galaxy_zoo_1")

The directory is named `sdss_dr17` to match the orchestration brief at `_orchestration/c5-sdss-dr17-spin-orientation.md`. The actual catalog is **Galaxy Zoo 1 Table 2**, which is the crowdsourced morphological classification of SDSS galaxies. The relevant point for the C5-CMB-AXIS LSS-spin-orientation test:

- GZ1's source imaging is **SDSS DR7** (Lintott+2011 §2.1).
- SDSS DR17 (2021 release) **includes the full DR7 photometric footprint unchanged** — additions in DR17 are spectroscopic (BOSS / eBOSS) and infrared (APOGEE-2), neither of which produces galaxy chirality labels.
- Therefore the largest available galaxy-chirality catalog with SDSS DR17 footprint coverage IS the Galaxy Zoo 1 catalog (~667k galaxies). The "DR17" naming is footprint-currentness; the catalog is canonical for any SDSS DR ≥ 7.

Alternative catalogs considered but not used this session:
- **Galaxy Zoo 2 (Hart+2016)**: 239k galaxies, finer morphology features but smaller spiral sample. Available at `data.galaxyzoo.org` if needed for future sub-analysis.
- **Galaxy Zoo DECaLS (Walmsley+2022)**: 314k galaxies, CNN-derived predictions from DECaLS DR8 imaging. Larger angular footprint than SDSS (DECaLS covers SDSS + extends). Available on Zenodo `10.5281/zenodo.4196266`. Defer to a follow-up session if cross-catalog cross-check is needed.
- **Shamir 2020 Ganalyzer algorithmic catalog (~170k galaxies)**: derived from SDSS DR8 imaging. Not publicly redistributed in a clean machine-readable form; partial tables in the published paper.

## Columns

The catalog is comma-separated with one header row. Per the Galaxy Zoo 1 data release documentation:

| Column | Description |
|---|---|
| `OBJID` | SDSS unique object identifier (long integer) |
| `RA` | Right ascension, sexagesimal `hh:mm:ss.s`, J2000 |
| `DEC` | Declination, sexagesimal `±dd:mm:ss.s`, J2000 |
| `NVOTE` | Number of Galaxy Zoo volunteer votes for this galaxy |
| `P_EL` | Probability elliptical (raw vote fraction) |
| `P_CW` | Probability **clockwise spiral** (raw vote fraction) |
| `P_ACW` | Probability **anticlockwise spiral** (raw vote fraction) |
| `P_EDGE` | Probability edge-on disk |
| `P_DK` | Probability "star or don't know" |
| `P_MG` | Probability merger |
| `P_CS` | Probability "combined spiral" (= P_CW + P_ACW + P_EDGE) |
| `P_EL_DEBIASED` | Debiased elliptical probability per Bamford+2009 / Lintott+2011 |
| `P_CS_DEBIASED` | Debiased combined-spiral probability |
| `SPIRAL` | Binary classification flag (1 = clean spiral by GZ1 criteria) |
| `ELLIPTICAL` | Binary classification flag (1 = clean elliptical) |
| `UNCERTAIN` | Binary classification flag (1 = neither clean) |

Total rows: 667,944 galaxies.

## Sources

- Primary catalog DR paper: [Lintott et al. 2011, MNRAS 410:166](https://academic.oup.com/mnras/article/410/1/166/1032478) — Galaxy Zoo 1 data release, 893k Galaxy Zoo classifications, 667k objects in this Table 2.
- Original methodology: [Lintott et al. 2008, MNRAS 389:1179](https://academic.oup.com/mnras/article/389/3/1179/977333) — Galaxy Zoo initial release.
- Bias correction reference: [Hayes, Davis, Silva 2017, MNRAS 466:3928](https://academic.oup.com/mnras/article/466/4/3928/2733974) — Sparcfire-based correction for SDSS clockwise/anticlockwise vote bias in GZ1.
- Cosmic spin dipole prior art:
  - [Longo 2011, Phys. Lett. B 699:224](https://www.sciencedirect.com/science/article/pii/S0370269311003224) — 15,158 SDSS DR6 spirals, hand-classified by 5 scanners, dipole at galactic `(l, b) = (52°, 68.5°)` (equatorial (α, δ) = (217°, 32°)), p = 7.9 × 10⁻⁴.
  - [Shamir 2020, ApJ 891:97](https://iopscience.iop.org/article/10.3847/1538-4357/ab6b54) — ~170k SDSS DR8 + ~33k Pan-STARRS, Ganalyzer algorithmic classification, quadrupole at ~6.9σ.

## Used by

- `src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py` — C5 SDSS DR17 spin-orientation re-analysis (this session: `analysis/c5-sdss-dr17-spin-orientation` branch)

## Re-download instructions

If the local file is corrupt or missing, re-fetch via:

```bash
cd data/sdss_dr17/
curl -L -o GalaxyZoo1_DR_table2.csv.gz "https://static.zooniverse.org/data.galaxyzoo.org/data/gz1/GalaxyZoo1_DR_table2.csv.gz"
# Verify checksum
md5 GalaxyZoo1_DR_table2.csv.gz
# Expected: 766cb56d64f936e00d26699a55f0669b
```

## Why tracked here (not external download)

The driver `c5_sdss_spin_orientation.py` runs the live-fire dipole fit + bootstrap + randomization-null on this catalog. Tracking the file ensures reproducibility from a single checkout (matches Pantheon+ canonical-cache pattern). 19 MB compressed is well within the regular-git size budget — no LFS routing needed.

The `data/*` gitignore broadly excludes simulation outputs (which can be re-generated from the engine). External research catalogs are NOT in that category and merit explicit allowlist override.

## License

Galaxy Zoo 1 data is publicly released for scientific use. Cite Lintott et al. 2011 (MNRAS 410:166) when using.
