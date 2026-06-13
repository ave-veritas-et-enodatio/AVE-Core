# Genesis v12 — boost-covariant transport pre-registration (DRAFT 2026-06-12)

> **STATUS: DRAFT** — awaiting Grant freeze.
> **Charter:** `_orchestration/2026-06-12_loop-gap-v12-charter.md`
> **Baseline:** v11 memristive + P11 (`chiral_lattice_v11.py`); moving-defect ENGINE-GAP (`moving_defect_transport_gate.py`).

**Tier:** discrete srs transport build — first run whose **primary falsifier** is **P12 comoving transport** (bounded-spread translating defect), not CVR-SET or P11 alone.

---

## 0. Corpus-grep (ave-prereg Step 1)

| Prior item | Relevance | v12 relation |
|---|---|---|
| `moving_defect_transport_gate.py` | 4× ENGINE-GAP: ME disperses, VacuumEngine3D pins | **Target gap** |
| `2026-06-11_next-step-fundamentality-plan.md` R5 | Master-unblocker for dynamics | **Scope anchor** |
| `chiral_lattice_v11.py` | Memristive + P11 on srs | **Platform base** |
| DCVE spec §Exact Lattice Operators | $\hat{T}_x=\exp(ia\hat{p}/\hbar)$ on voxel array | **Discrete analogue** |
| LOOP GAP doctrine rank 1 (OP-2) | Bulk container still open | **v12b** — not v12a |

**Genuinely open on srs:** semi-Lagrangian comoving transport of localized saturation pocket with ablation contrast.

---

## 1. Physical picture

- **Substrate:** v11 discrete srs TLM + per-node $S(t)$ lag.
- **Transport:** after each scatter step, **Galilean field remap** $\Delta z = v_{\mathrm{boost}}$ along lattice axis (semi-Lagrangian; DCVE discrete translation operator flavour).
- **Defect:** localized `(2,3)` plant or Gaussian-enveloped packet — the **payload** the voxels carry.
- **Not claiming:** full multi-channel CoupledK4Cosserat boost covariance (v12b); double-slit fork (downstream of P12 PASS).

---

## 2. P12 — primary gate

| Metric | Definition | PASS (proposed) |
|:---|:---|:---|
| `transport_gain` | $\Delta z_{\mathrm{comoving}} - \Delta z_{\mathrm{pinned}}$ | $\ge 0.08 \times (N_{\mathrm{steps}}/100) \times L_{\mathrm{box}}$ |
| `width_ratio` | $w_{\mathrm{end}}/w_0$ (comoving) | $\le 2.0$ |
| `peak_retention` | $A_{\mathrm{peak,end}}/A_{\mathrm{peak,0}}$ (comoving) | $\ge 0.50$ |

**P12 PASS:** all three on comoving vs pinned pair; **ablation** = pinned gain $<$ comoving.

**C4 apparatus:** linear comoving centroid $>$ linear pinned (boost live, not dead apparatus).

**Discrete hop:** $v_{\mathrm{boost}}=1$ node per scatter step (sorted-axis roll).

---

## 3. Verdict ladder

| Verdict | Condition |
|:---|:---|
| **TRANSPORT-LANDED** | P12 PASS + ablation FAIL + C4 linear advances |
| **PARTIAL** | comoving disp > pinned disp but P12 incomplete |
| **ENGINE-GAP** | no bounded translating defect |

---

## 4. Deliverables

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v12.py` |
| Tests | `src/tests/test_chiral_lattice_v12.py` |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_v12_genesis.py` |
| JSON | `assets/sim_outputs/genesis_v12_boost_transport.json` |

---

## 5. Out of scope (v12a)

- CoupledK4Cosserat multi-channel transport (v12b).
- Double-slit fork (`moving-defect-doubleslit` prereg).
- LOOP GAP LANDED / matrix promotion.
