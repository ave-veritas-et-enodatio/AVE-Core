# Genesis v15 — nucleation from latent heat / crystallization (pre-registration DRAFT)

**Status:** DRAFT — Grant freeze pending  
**Context:** `research/2026-06-12_three-lane-genesis-context.md` (§7 — Lane A)  
**Charter:** `_orchestration/2026-06-12_loop-gap-v15-charter.md`  
**Parent:** v13 LOCALIZATION-LANDED (container); v14 CAVITY-BREAK (manufacture transport)

---

## 1 — Motivation

Session 2026-06-12 reframed genesis as **three lanes** (cosmic nucleation, photon-in manufacture, emission). The v9–v14 discrete srs program tests **Lane B** only. Corpus Lane A claims:

- Lattice **crystallizes** first; **latent heat** injects into the radiation/order-parameter budget (`cmb-thermal-attractor.md`, generative cosmology).
- Matter is a **condensed phase** of transverse content; A1 standing-V is the **order parameter** (`photon-identification.md` R1; vapor-lock framing §11).
- **Free-space heals** — lone propagating photon does not nucleate defect (genesis-23 `max|V_inc|=0`).
- **Seeded** saturation at node pair with C1+C2+C3 is the pair-production nucleation picture (`pair-production-axiom-derivation.md`).

**v15 hypothesis:** a defect can nucleate from **latent heat injection + saturation seed** on an already-crystallized lattice **without** a `plant_23` photon precursor — the cosmic/crystallography lane made falsifiable on-engine.

**Not claimed:** latent heat $= m_ec^2$ numerically; single electron without partner; electrons as ur-particle.

---

## 2 — Two-platform strategy

| Arm | Platform | What it tests | Longitudinal / $V_{\mathrm{inc}}$ |
|:---|:---|:---|:---|
| **v15a** | Discrete srs + v13 pocket | Latent injection as **local energy deposit** + saturation ramp at node-pair; **no photon plant** | Proxy: pocket $E$, $A^2$, width — no true $V_{\mathrm{inc}}$ |
| **v15b** | `k4_tlm.py` (or CoupledK4 + GAP-1) | Same IC on engine with **$V_{\mathrm{inc}}$ array** | **Primary** for OP-2 longitudinal population read |

**Prereg rule:** v15a can **PARTIAL**-pass without v15b; **NUCLEATION-LANDED** requires v15b $V_{\mathrm{inc}}$ gate OR Grant adjudication that srs proxy is sufficient.

---

## 3 — Initial condition (Lane A analogue)

Replace OP-0 photon packet with:

1. **Crystallized cell** — srs net + `apply_omega_freeze_ic` ON (operating-point bias).
2. **Compton pocket** — v13 `compton_pocket_mask` (container pre-placed OR self-generated wall later).
3. **Node-pair seed** — two interior nodes at minimum separation satisfying C1 amplitude threshold (not a propagating wavepacket).
4. **Latent heat pulse** — volumetric energy injection per scatter step:
   $$\Delta E_{\mathrm{latent}}(t) = \dot q_{\mathrm{latent}}\,\Delta t \cdot \mathbf{1}_{\mathrm{pocket}}(r)$$
   discrete analogue of $3H\rho_{\mathrm{latent}}$ source (cosmology continuity equation).
5. **Saturation ramp** — drive local $A^2 \to A_{\mathrm{yield}}^2 = 2\alpha$ at seed pair (crystallization-front analogue).

**Explicitly OFF:** `localized_plant_seed` / `plant_23_ansatz`; linear packet launch; external plane-wave drive.

---

## 4 — Primary falsifiers

### P15-N — nucleation without photon precursor

| Metric | Threshold | Role |
|:---|:---:|:---|
| `A2_seed_peak` | $\ge A_{\mathrm{yield}}^2 \cdot 0.9$ | Saturation reached at seed without photon IC |
| `E_localized` | pocket fraction $\ge 0.55$ after quiescence | Defect stays bounded (reuse P13 floor) |
| `photon_ablation` | photon-IC arm **fails** P15-N when latent-OFF | Discriminates lanes |

### P15-V — longitudinal branch (v15b only)

| Metric | Threshold | Role |
|:---|:---:|:---|
| `max|V_inc|` | $> 10^{-12}$ (machine floor) | genesis-23 null reversed |
| `V_inc` persistence | nonzero after latent pulse ends | Order parameter survives drive-off |

### P15-H — heal ablation (genesis-23 regression)

| Metric | Expected |
|:---|:---|
| Latent-OFF + no seed | $V_{\mathrm{inc}}\approx 0$; energy disperses |
| Matches genesis-23 | **HEAL-PASS** |

### P15-P — pair seed (optional arm)

| Metric | Role |
|:---|:---|
| Single-node seed vs node-pair | Pair-production canon: pair seed required for stable nucleation |
| Classification | Consistency check, not full e⁺e⁻ dynamics |

### P15-L — latent discontinuity (hypothesis-class)

| Metric | Role |
|:---|:---|
| Energy ledger jump at $A^2$ crossing | FLASH analogue; may fail (cavprobe LOCK) — report honestly |

---

## 5 — Ablation matrix

| Cell | latent pulse | photon plant | pair seed | wall | Purpose |
|:---|:---:|:---:|:---:|:---:|:---|
| **A — cosmic IC** | ON | OFF | ON | ON | Primary P15 |
| B — heal | OFF | OFF | OFF | OFF | genesis-23 regression |
| C — photon compare | OFF | ON | OFF | ON | Lane B control |
| D — latent no wall | ON | OFF | ON | OFF | container necessity |
| E — single-node | ON | OFF | single | ON | pair canon probe |

---

## 6 — Verdict taxonomy

| Verdict | Condition |
|:---|:---|
| **NUCLEATION-LANDED** | P15-N pass + P15-H pass + (P15-V pass on v15b OR Grant srs-proxy ratification) |
| **PARTIAL** | Localized saturation without $V_{\mathrm{inc}}$ (v15a only) |
| **HEAL-CONFIRMED** | B passes; A fails — cosmic IC insufficient (expected if hypothesis wrong) |
| **ENGINE-GAP** | No discrimination between A and C |

---

## 7 — Classification

| Test | Class |
|:---|:---|
| Latent injection kernel | Consistency (cosmology continuity discrete analogue) |
| P15-N vs photon ablation | Emergence candidate (lane discrimination) |
| P15-V $V_{\mathrm{inc}}$ | Emergence candidate (OP-2 longitudinal population) |
| P15-H heal | Regression (genesis-23) |
| P15-L latent jump | Hypothesis-class (vapor-lock payoff-if-true) |

---

## 8 — Deliverables

| Artifact | Path |
|:---|:---|
| Engine v15a | `src/ave/core/chiral_lattice_v15.py` |
| Engine v15b | `src/scripts/vol_1_foundations/k4_tlm_v15_nucleation.py` (or extend GAP-1 driver) |
| Tests | `src/tests/test_chiral_lattice_v15.py` |
| Driver | `chiral_lattice_v15_genesis.py` |
| Figures | `chiral_lattice_v15_figures.py` |
| JSON | `assets/sim_outputs/genesis_v15_nucleation.json` |

```bash
pytest src/tests/test_chiral_lattice_v15.py -q
python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py
python src/scripts/vol_1_foundations/chiral_lattice_v15_figures.py
```

---

## 9 — Relation to LOOP GAP ranks

| Rank | v15 role |
|:---|:---|
| 1 OP-2 container | Reuse v13 pocket; test **nucleation-into** container vs photon-closure |
| 2 Compton ring-up | Latent pulse duration sweep (secondary) |
| 3 Energize-lock | Deferred |
| 4 Remanence | P15 persistence after latent-OFF (weak remanence probe) |

---

## 10 — Figures (characteristic curves)

Mirror v14 figure set with Lane-A-specific panels:

- Latent injection rate vs $A^2$ at seed
- $V_{\mathrm{inc}}$ field snapshot (v15b)
- Comparison: cosmic IC vs photon IC final profiles
- Energy ledger: latent partition vs dispersive loss

---

## 11 — Grant adjudication queue (before freeze)

- [x] **Latent injection rate units (resolved 2026-06-12):** vacuum native units via `src/ave/core/genesis_lane_a_provenance.py`. Local path = `local_pair_ramp_native` ($\Delta E_{\mathrm{native}}=0.095$/step/pair, $9.5\,m_e c^2$ total over 50 steps). Cosmic $3H\rho_{\mathrm{latent}}$ / cell / τ logged at $\sim 5.8\times 10^{-71}\times$ yield kinetic — **not injected** (scale separation). Audit: `research/2026-06-12_genesis-parameter-provenance-audit.md`.
- [ ] Ratify P15-V floor and srs-proxy sufficiency
- [x] **Single-electron vs pair scope for v15a (resolved):** pair canon primary; cell E single-node probe only
- [ ] v15b engine choice: `k4_tlm` vs `CoupledK4Cosserat` GAP-1 replay
