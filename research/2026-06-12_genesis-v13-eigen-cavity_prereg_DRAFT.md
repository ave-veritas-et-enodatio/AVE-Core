# Genesis v13 — OP-2 eigen-cavity / bulk-wall confinement (pre-registration DRAFT)

**Status:** DRAFT — Grant freeze pending  
**Platform:** discrete srs vector-TLM (v11 memristive kernel)  
**Parent:** LOOP GAP rank-1 (OP-2 container)  
**Charter:** `_orchestration/2026-06-12_loop-gap-v13-charter.md`

---

## 1 — Motivation

v12 production closed with **ENGINE-GAP**: comoving transport rails work in smoke but **width_ratio ≈ 3.9×** on open srs — localized defect disperses without a bounded resonator. LOOP GAP plumber rank **1** is **OP-2**: bulk $\Gamma_{\mathrm{bulk}}\to -1$ confinement at Compton scale, not EM $S_{11}$ at $Z_0$.

v13 tests whether a **discrete bulk-wall ansatz** on the srs platform can localize energy in a tubular Compton pocket **without** comoving transport (transport deferred to v14 stack).

---

## 2 — Engine hypothesis

| Piece | Discrete analogue |
|:---|:---|
| Bulk TIR wall | Exterior nodes: $z_{\mathrm{local}}\to Z_{\mathrm{bulk,wall}}$ in Op3 bond mixing |
| Hard container | Post-scatter exterior field attenuation ($\times\varepsilon_{\mathrm{leak}}$) |
| Compton pocket | Tubular mask along srs axis: $|z-z_0|\le f_z\cdot L_{\mathrm{box}}$, $r\le r_0+f_r\cdot L_{\mathrm{box}}$ |
| Seed | Localized `(2,3)` ansatz (`plant_23_ansatz`) centered in pocket |

**Not in scope (v13):** full coupled K4⊗Cosserat $V_{\mathrm{inc}}$ bulk branch; Compton ring-up drive sweep; v12 comoving stack.

---

## 3 — Primary falsifier: P13

**P13 — eigen-cavity localization** (confinement under passive evolution, no Galilean advection):

| Metric | Threshold | Role |
|:---|:---:|:---|
| `E_frac_interior` | $\ge 0.55$ | Energy remains in pocket |
| `width_ratio` | $\le 2.0$ | No runaway dispersion along axis |
| `peak_retention` | $\ge 0.40$ | Amplitude not fully radiated |

**Ablation:** `bulk_wall=OFF` must **fail** P13.

**Discrimination:** `width_ratio(wall-OFF) / width_ratio(wall-ON) ≥ 1.20` **or** `ΔE_frac ≥ 0.15`.

**Controls:**
- Linear packet + wall (non-(2,3) apparatus)
- Wall + memristive-OFF (wall mechanism isolated from Level-2 lag)

---

## 4 — Verdict taxonomy

| Verdict | Condition |
|:---|:---|
| **LOCALIZATION-LANDED** | P13 wall-ON pass + ablation fail + discrimination pass |
| **PARTIAL** | Discrimination pass + partial metrics (E_frac ≥ 0.45 or width ≤ 2.5) |
| **ENGINE-GAP** | Wall does not localize; open srs dispersion persists |

---

## 5 — Classification

| Test | Class |
|:---|:---|
| Op3 + $z_{\mathrm{wall}}$ stiffening | **Consistency** (discrete Γ_bulk routing) |
| P13 wall-ON vs OFF | **Emergence candidate** (bounded resonator on lattice) |
| v11 P11 regression cell | **Regression** (no remanence claim from v13) |

---

## 6 — Deliverables

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v13.py` |
| Tests | `src/tests/test_chiral_lattice_v13.py` |
| Driver | `chiral_lattice_v13_genesis.py` |
| JSON | `assets/sim_outputs/genesis_v13_eigen_cavity.json` |

```bash
pytest src/tests/test_chiral_lattice_v13.py -q
python src/scripts/vol_1_foundations/chiral_lattice_v13_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v13_genesis.py
```

---

## 7 — Relation to cross-sector layer

GAP-1 (`cross_sector_coupling.py`) populates bulk $V_{\mathrm{inc}}$ on **CoupledK4Cosserat** — orthogonal engine class. v13 is the **discrete srs OP-2 pocket** path; full two-sector adjudication (A44) remains open for unified container.
