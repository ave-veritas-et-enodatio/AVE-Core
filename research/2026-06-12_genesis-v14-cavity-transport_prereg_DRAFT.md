# Genesis v14 — cavity + comoving transport stack (pre-registration DRAFT)

**Status:** DRAFT — Grant freeze pending  
**Platform:** discrete srs vector-TLM (v13 bulk-wall + v12 Galilean hop)  
**Parent:** v13 LOCALIZATION-LANDED + v12 ENGINE-GAP (open srs)  
**Charter:** `_orchestration/2026-06-12_loop-gap-v14-charter.md`

---

## 1 — Motivation

| Prior run | Verdict | Key read |
|:---|:---|:---|
| v12 production | ENGINE-GAP | width ~3.9× open srs; no comoving−pinned gain |
| v13 production | LOCALIZATION-LANDED | width ~0.98× wall-ON; ~3.15× wall-OFF |

**Hypothesis:** v12 transport read failed because the defect **dispersed** on an open lattice before centroid differential could be interpreted as covariant voxel surfing. v13 provides the **bounded eigen-cavity**; v14 tests whether **comoving advection** (v12 rails) produces measurable **transport gain** *while* P13 confinement holds.

This is the first **dual-gate** genesis run: localization **and** translation on the same localized payload.

---

## 2 — Engine stack

```
v14_step = v13_bulk_wall_step(…) → translate_field_along_axis(…, n_nodes_shift=v_boost)
```

| Layer | Source | Role |
|:---|:---|:---|
| Memristive Op14/Op3/snap | v11 | Constitutive kernel |
| Bulk-wall pocket | v13 | OP-2 Γ_bulk analogue |
| Integer node roll | v12 | Boost-covariant hop per scatter step |

**Not in scope:** Compton ring-up drive sweep; CoupledK4Cosserat unified bulk; P11 remanence closure.

---

## 3 — Primary falsifiers

### P13 (retained from v13)

Must still pass on the **comoving** arm — transport must not re-open dispersion:

| Metric | Threshold |
|:---|:---:|
| `E_frac_interior` | ≥ 0.55 |
| `width_ratio` | ≤ 2.0 |
| `peak_retention` | ≥ 0.40 |

### P12 (retained from v12)

Transport gain on **cavity-confined** defect:

| Metric | Threshold |
|:---|:---:|
| `transport_gain` = comoving_disp − pinned_disp | ≥ `P12_MIN_GAIN_PER_100 × (n/100) × box` |
| `width_ratio` | ≤ 2.0 (with wall ON) |
| `peak_retention` | ≥ 0.50 |

### P14 — composite (new)

**P14 PASS** iff **both** P13 and P12 pass on the same `wall-ON + comoving-ON` cell.

**P14 PARTIAL** iff P13 passes + `transport_gain > 0` but below P12 threshold.

**P14 ENGINE-GAP** iff P13 fails on comoving arm **or** transport_gain ≤ pinned (v12 recurrence inside cavity).

---

## 4 — Ablation matrix (production)

| Cell | wall | comoving | Purpose |
|:---|:---:|:---:|:---|
| **A — full stack** | ON | ON | Primary P14 |
| B — pinned cavity | ON | OFF | v13 regression |
| C — open transport | OFF | ON | v12 failure mode inside cavity context |
| D — open pinned | OFF | OFF | double-null |
| E — Op3-only wall | ON (no leak) | ON | Separate TIR from leak clamp |
| F — linear + cavity + comoving | ON | ON | Apparatus control |

---

## 5 — Sensitivity arms

### E — Op3-only wall (no exterior leak)

Set `exterior_leak=1.0` (no post-step clamp). If P13 still passes with P12 gain, leak clamp is not load-bearing for the composite verdict.

### v_boost sweep (smoke only)

`v_boost ∈ {0.5, 1.0, 2.0}` nodes/step — check gain monotonicity without production budget blow-up.

---

## 6 — Verdict taxonomy

| Verdict | Condition |
|:---|:---|
| **TRANSPORT-IN-CAVITY-LANDED** | P14 PASS (P13 + P12 on full stack) |
| **PARTIAL** | P13 pass + positive transport_gain < threshold |
| **CAVITY-BREAK** | P13 fails when comoving ON (transport re-opens dispersion) |
| **ENGINE-GAP** | P13 pass but no transport gain (pinned ≈ comoving) |

---

## 7 — Classification

| Test | Class |
|:---|:---|
| v13 step + v12 roll composition | **Consistency** (stacked discrete analogue) |
| P14 dual-gate on same run | **Emergence candidate** (localized + translating defect) |
| Op3-only ablation | **Discriminator** (leak vs TIR) |
| P11 regression | **Regression** (no remanence claim) |

---

## 8 — Deliverables

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v14.py` |
| Tests | `src/tests/test_chiral_lattice_v14.py` |
| Driver | `chiral_lattice_v14_genesis.py` |
| JSON | `assets/sim_outputs/genesis_v14_cavity_transport.json` |

```bash
pytest src/tests/test_chiral_lattice_v14.py -q
python src/scripts/vol_1_foundations/chiral_lattice_v14_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v14_genesis.py
```

---

## 9 — Success criteria vs failure modes

**Success (TRANSPORT-IN-CAVITY-LANDED):** Centroid advances with comoving ON inside a pocket whose width stays ≤2× — the voxel payload **surfs** without **melting**.

**Failure mode A (CAVITY-BREAK):** Comoving re-opens width >2× despite wall — advection and confinement incompatible at current parameters.

**Failure mode B (ENGINE-GAP):** Cavity holds but pinned ≈ comoving displacement — same as v12 on confined background; transport rails need richer physics (multi-channel bulk, Compton ring-up).

**Failure mode C (leak artifact):** P14 passes only with leak clamp; Op3-only arm fails P13 — confinement not physically routed.
