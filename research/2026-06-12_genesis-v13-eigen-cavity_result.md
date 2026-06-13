# Genesis v13 — OP-2 Eigen-Cavity Result (PRODUCTION — 2026-06-12)

> **Prereg:** `research/2026-06-12_genesis-v13-eigen-cavity_prereg_DRAFT.md` (DRAFT — freeze pending)
> **Engine class:** discrete srs TLM + v11 memristive + **bulk-wall OP-2 pocket**
> **Run class:** **PRODUCTION** — P13 L=10, 220 scatter steps; smoke L=8, 60 steps.
> **Driver:** `python src/scripts/vol_1_foundations/chiral_lattice_v13_genesis.py`
> **Wall time:** ~2.5 min (production).

## Implementation

| Artifact | Path |
|----------|------|
| v13 integrator | `src/ave/core/chiral_lattice_v13.py` |
| Tests | `src/tests/test_chiral_lattice_v13.py` (4/4 PASS) |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_v13_genesis.py` |
| JSON (local, gitignored) | `assets/sim_outputs/genesis_v13_eigen_cavity.json` |
| Charter | `_orchestration/2026-06-12_loop-gap-v13-charter.md` |

**Platform notes:** Compton tubular pocket (`z_half_frac=0.14`, `r_max_frac=0.18`, ~22.5% of nodes).
Exterior `z_local → Z_bulk_wall=12` in Op3 + post-step exterior leak `ε_leak=0.04`.
No Galilean advection. Memristive τ_steps=50 (discrete apparatus floor).

---

## P13 — eigen-cavity localization (production)

| Cell | E_frac | width× | peak | total E ratio | P13 |
|------|--------|--------|------|---------------|-----|
| **bulk-wall ON** | **1.000** | **0.98** | 0.606 | 0.078 | **PASS** |
| bulk-wall OFF (ablation) | 0.417 | **3.15** | 0.833 | 0.405 | FAIL |
| wall + memristive-OFF | 1.000 | 0.98 | 0.630 | 0.076 | PASS |
| linear packet + wall | 1.000 | 1.02 | 0.941 | 0.133 | PASS |

**Wall discrimination:**
- `width_ratio(OFF)/width_ratio(ON)` = **3.23** (threshold ≥ 1.20) — PASS
- `ΔE_frac` = **0.583** (threshold ≥ 0.15) — PASS

**P13 any PASS:** **True**
**P13 ablation FAIL:** **True** (open srs reproduces v12-class dispersion)
**VERDICT:** **LOCALIZATION-LANDED**

---

## Smoke cross-check (L=8, 60 steps)

| Cell | width× | P13 |
|------|--------|-----|
| wall ON | 0.85 | PASS |
| wall OFF | 3.68 | FAIL |

Smoke and production agree on verdict and discrimination direction.

---

## v11 regression (same net, P6 cell)

| Metric | Production |
|--------|------------|
| Bin | **DISPERSES** |
| P11 | **FAIL** |

v13 closes rank-1 (OP-2 container) **without** claiming rank-4 remanence. P11 remains open on the discrete srs platform at production scale.

---

## Comparison to v12 (open srs, no wall)

| Engine | width× (comoving / open) | Transport |
|--------|--------------------------|-----------|
| v12 production | 3.86× | ENGINE-GAP (no gain) |
| v13 wall-OFF | 3.15× | N/A (no comoving) |
| v13 wall-ON | **0.98×** | N/A |

v12 transport failure is **consistent with** missing OP-2 container: defect disperses on open srs before centroid differential can be read as covariant surfing.

---

## Classification

| Observation | Class | LOOP GAP implication |
|:---|:---|:---|
| Exterior z_wall stiffening + leak clamp | **Consistency** (discrete Γ_bulk routing) | Channel-tagged confinement analogue |
| P13 wall-ON vs OFF discrimination | **Emergence candidate** | Bounded resonator on lattice at Compton pocket scale |
| E_frac=1.0 on wall-ON | **Apparatus note** | Hard leak clamp contributes; ablation is load-bearing falsifier |
| Memristive-OFF still P13 PASS | **Falsifier** | Wall mechanism not memristive-dependent |
| Linear packet + wall P13 PASS | **Control** | Confinement not (2,3)-exclusive |
| v11 P11 FAIL at production | **Regression** | Remanence (rank 4) still open |

---

## Honest caveats

1. **Leak clamp vs Op3 TIR alone** — `E_frac≈1.0` partly reflects exterior field zeroing (`ε_leak=0.04`), not pure bond reflection. v14 prereg includes **Op3-only wall ablation** (no leak) to separate mechanisms.
2. **Not full bulk $V_{\mathrm{inc}}$ branch** — discrete srs transverse-only; coupled K4⊗Cosserat GAP-1 path remains orthogonal.
3. **Total energy loss** — wall-ON `total_energy_ratio≈0.08` vs OFF `≈0.41`; confinement trades against radiative/leak dissipation. Peak retention 0.61 still above P13 floor.

---

## Cascade implications

| LOOP GAP rank | Status after v13 |
|:---|:---|
| **1 — OP-2 container** | **PARTIAL→LANDED (discrete srs ansatz)** — P13 LOCALIZATION-LANDED |
| **2 — Compton ring-up** | NOT TESTED |
| **3 — Energize-lock** | OPEN (genesis-24 pump falsified) |
| **4 — Remanence** | OPEN (P11 FAIL at production) |

**Next:** v14 stacks v12 comoving transport on v13 cavity; dual-gate P13+P12 (`research/2026-06-12_genesis-v14-cavity-transport_prereg_DRAFT.md`).

---

## Commands to reproduce

```bash
pytest src/tests/test_chiral_lattice_v13.py -q
python src/scripts/vol_1_foundations/chiral_lattice_v13_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v13_genesis.py
```
