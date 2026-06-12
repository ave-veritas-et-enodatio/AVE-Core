# Cross-sector engine integration — result (2026-06-12)

> **Prereg (FROZEN):** `research/2026-06-12_cross-sector-engine-integration_prereg_FROZEN.md`

## Implementation

| Artifact | Path |
|:---|:---|
| Coupling module | `src/ave/core/cross_sector_coupling.py` |
| Coupled hook | `CoupledK4Cosserat.use_trilinear_converter` |
| VacuumEngine hook | `EngineConfig.use_trilinear_converter`, `freeze_converter_wall()` |
| Tests | `src/tests/test_cross_sector_coupling.py` — **7/7 PASS** |

## GAP-1 — direct Cosserat seed (production)

**Driver:** `cross_sector_gap1_closure.py` (N=14, 80 steps)

| Arm | $V_{\mathrm{inc}}(t_{\mathrm{end}})$ |
|:---|:---:|
| CONVERTER-OFF | 0 |
| CONVERTER-ON | **6.08×10⁻⁶** |

**GAP-1 PASS:** True

## GAP-1 — genesis-23 photon replay (production)

**Driver:** `reflection_genesis_23_converter_replay.py` (N=24, 50 steps, **gyrotropic** mode)

| Arm | $V_{\mathrm{inc}}(t_{\mathrm{end}})$ | $\|L\|$ |
|:---|:---:|:---:|
| PHOTON+CONVERTER-OFF | 0 | 14.8 |
| PHOTON+CONVERTER-ON | **3.60×10⁻⁷** | 14.8 |

**GAP-1 lift (ON > OFF):** True  
**Bounded (no detonation):** True

### Genesis-23 replay notes

1. **Trilinear** mode fails for Beltrami photon IC: $w\cdot(\nabla\times\omega)=0$ when $u=0$.
2. **Gyrotropic** mode + `effective_shear_director` ($w\leftarrow\dot\omega$ when $u=0$) is the correct photon path.
3. **Interior injection** (not `k4.mask_active`): coupling peaks on B-sublattice sites.
4. Magnitude is **small** ($10^{-7}$) vs direct sinusoidal seed ($10^{-6}$) — apparatus floor; not promotion-grade V-sector closure.

## Classification

| Claim | Class |
|:---|:---|
| Conserved cross-sector source in coupled engine | **Consistency** (Axiom-1 consequence) |
| GAP-1 lift on photon replay | **Emergence candidate** (weak magnitude) |
| (2,3) self-assembly | **Still open** |

## Next

- v11 discrete srs + LOOP GAP P11 (separate epic)
- OP-2 sustained confinement with $\Gamma_{\mathrm{bulk}}$ (v11b)
- Optional: strengthen photon-path coupling via sublattice-aware injection
