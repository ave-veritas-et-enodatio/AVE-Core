# Pantheon+SH0ES Canonical Data Cache

External research data tracked here for AVE-Core reproducibility. NOT simulation output — these are canonical observational catalogs from the Pantheon+SH0ES collaboration.

## Files

| File | Size | MD5 | Source |
|---|---|---|---|
| `Pantheon+SH0ES.dat` | 579 KB | `2049b142e6aad384470b3364aa10f3fa` | [PantheonPlusSH0ES/DataRelease](https://github.com/PantheonPlusSH0ES/DataRelease) main catalog |
| `Pantheon+SH0ES_STAT+SYS.cov` | 33 MB | `041bdb6638841794fc2d7caa88dd66eb` | Same repo, full STAT+SYS covariance matrix |

The `.cov` file is routed through git-LFS per `.gitattributes` (filter=lfs).

## Sources

- Primary catalog: [Scolnic et al. 2022, ApJ 938:113](https://iopscience.iop.org/article/10.3847/1538-4357/ac8b7a) — 1701 Type Ia supernovae with calibrated distance moduli, peculiar-velocity corrections (zHEL, zCMB, zHD), and SH0ES Cepheid anchors.
- Covariance: STAT+SYS uncertainty matrix combining photometric, calibration, MW-dust, peculiar-velocity, and SN-population systematics.

## Used by

- `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py` — E1b-prime Pantheon+ raw-SN bulk-flow tightening (Outcome Marginal-D, audit tag `audit/2026-05-19_c5-pantheon-tightening`)
- Future SDSS DR17 spin-orientation cross-check (queued epic `_orchestration/c5-sdss-dr17-spin-orientation.md`)

## Re-download instructions

If the LFS objects are inaccessible (LFS bandwidth quota, etc.), re-fetch via:

```bash
cd data/pantheon_plus/
curl -L -o Pantheon+SH0ES.dat "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat"
curl -L -o Pantheon+SH0ES_STAT+SYS.cov "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov"
# Verify checksums
md5 Pantheon+SH0ES.dat Pantheon+SH0ES_STAT+SYS.cov
```

Expected MD5 hashes per table above.

## Why tracked here (not external download)

E1b-prime session surfaced that the `.cov` file was NOT in canonical cache when the driver tried to load it; chi²/dof = 0.47 (over-conservative diagonal-only) surfaced the missing dependency. Tracking via LFS ensures future driver re-runs don't re-trigger the download step + allows reproducibility from a single checkout.

The `data/*` gitignore broadly excludes simulation outputs (which can be re-generated from the engine). External research catalogs are NOT in that category and merit explicit allowlist + LFS routing.
