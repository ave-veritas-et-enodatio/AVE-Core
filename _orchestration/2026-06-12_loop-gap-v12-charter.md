# LOOP GAP — v12 charter: boost-covariant transport (2026-06-12)

**Epic:** genesis voxel translation / dynamical program  
**Status:** CHARTER ACTIVE — prereg DRAFT; implementor in-session  
**Parent:** v11 charter `_orchestration/2026-06-12_loop-gap-v11-charter.md`  
**Prereg:** `research/2026-06-12_genesis-v12-boost-transport_prereg_DRAFT.md`

---

## Phase 0 — Scope (2026-06-12)

v12 closes the **4×-confirmed ENGINE-GAP** on the **discrete srs platform**:

> Converged reactive trap cannot **translate** covariantly — voxel payload does not surf node-to-node.

**v12a deliverable:** semi-Lagrangian comoving advection + P12 gate on v11 kernel.

**v12b (deferred):** CoupledK4Cosserat multi-channel + bulk OP-2 container.

---

## Phase 1 — Implementor (IN PROGRESS)

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v12.py` |
| Tests | `src/tests/test_chiral_lattice_v12.py` |
| Driver | `chiral_lattice_v12_genesis.py` |

```bash
python src/scripts/vol_1_foundations/chiral_lattice_v12_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v12_genesis.py
pytest src/tests/test_chiral_lattice_v12.py -q
```

---

## Phase 2 — Grant freeze (PENDING)

- [ ] Ratify P12 thresholds
- [ ] Rename prereg `_FROZEN`

---

## Related

- Fundamentality plan **R5** — boost-covariant transport master-unblocker
- `moving_defect_transport_gate.py` — capability baseline (ENGINE-GAP)
