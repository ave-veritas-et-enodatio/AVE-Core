# LOOP GAP — v15 charter: nucleation from latent heat (Lane A) (2026-06-12)

**Epic:** genesis three-lane program  
**Status:** CHARTER ACTIVE — Phase 1 COMPLETE (HEAL-CONFIRMED); Phase 1b ablation PENDING  
**Program ledger:** `research/2026-06-12_genesis-program-status.md`  
**Parameter audit:** `research/2026-06-12_genesis-parameter-provenance-audit.md`  
**Context doc:** `research/2026-06-12_three-lane-genesis-context.md`  
**Prereg:** `research/2026-06-12_genesis-v15-nucleation-from-latent_prereg_DRAFT.md`  
**Parent:** v14 charter `_orchestration/2026-06-12_loop-gap-v14-charter.md`

---

## Phase 0 — Scope (2026-06-12)

Grant session reframed genesis as **three lanes** (cosmic / manufacture / emission). v9–v14 = **Lane B** (photon-in). v15 = **Lane A**:

> **Nucleation from latent heat + saturation seed on crystallized lattice — no photon precursor.**

**Unblocks:** constitutive "condensed phase" obligations (`the-abandoned-interior.md`); genesis-23 heal vs seeded discrimination; OP-4 latent-heat hypothesis surface.

**Does not claim:** electrons ur-particle; $m_ec^2$ derived from latent; single-electron without partner (optional P15-P arm).

---

## Phase 1 — Implementor (COMPLETE — 2026-06-12)

**Production verdict:** **HEAL-CONFIRMED** — native derived budget ($9.5\,m_e c^2$ over 50 latent steps) deposited on pair; $r_{\mathrm{yield}}^*\approx 0.36$ vs floor 1.34; photon control $r_{\mathrm{yield}}^*\approx 2.9$ without latent.  
**Result:** `research/2026-06-12_genesis-v15-nucleation-latent_result.md`  
**JSON:** `assets/sim_outputs/genesis_v15_nucleation_latent.json`  
**Tests:** 6/6 PASS

**Retracted:** pre-native `q_latent` knob and ENGINE-GAP read — replaced by `genesis_lane_a_provenance.py` (vacuum native units).

### v15a — discrete srs (shipped)

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v15.py` |
| Native provenance | `src/ave/core/genesis_lane_a_provenance.py` |
| Tests | `src/tests/test_chiral_lattice_v15.py` |
| Driver | `chiral_lattice_v15_genesis.py` |

**Primitives (no free knobs):**

```python
# genesis_lane_a_provenance.py — derived budget in vacuum native units
def lane_a_injection_schedule(...) -> LaneAProvenance

# chiral_lattice_v15.py
def inject_latent_pair_ramp_native(V, pair_nodes, schedule) -> None
def seed_saturated_node_pair(net, *, r_yield_seed: float = 1.0) -> np.ndarray
def run_p15_nucleation_cell(...) -> V15P15Result
```

## Phase 1b — v15a-ablation (PENDING)

**Hypothesis:** χ-snap + memristive scatter during latent window dissipates the 9.5 native deficit.

**Derived ablation switches** (not tuning):

- `chi_shock=0` during latent phase only
- `snap=False` during latent phase only
- optional `memristive=False` during latent phase only

**Pass criterion:** cell A cosmic IC reaches P15-N floor ($r_{\mathrm{yield}}^*\geq 1.342$) with ablation ON and heal cell B still cold.

## Phase 2 — v15b K4 TLM ($V_{\mathrm{inc}}$ read) (PENDING)

| Artifact | Path |
|:---|:---|
| Driver | `k4_tlm_v15_nucleation.py` or extend `cross_sector_gap1_closure.py` |

**Read:** `max|V_inc|`, persistence after pulse; compare to genesis-23 null.

```bash
pytest src/tests/test_chiral_lattice_v15.py -q
python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py --smoke
python src/scripts/vol_1_foundations/chiral_lattice_v15_genesis.py
python src/scripts/vol_1_foundations/chiral_lattice_v15_figures.py
```

**Estimated wall time:** v15a smoke ~2 min; production ~5 min; v15b TBD (FDTD budget).

---

## Phase 3 — Grant freeze (PENDING)

- [x] Native unit injection path resolved — `genesis_lane_a_provenance.py` (Grant ratification pending freeze)
- [ ] Ratify P15 thresholds + srs-proxy sufficiency for NUCLEATION-LANDED
- [ ] Adjudicate v15b engine choice (`k4_tlm` vs `CoupledK4Cosserat`)
- [ ] Rename prereg `_FROZEN`

---

## Phase 4 — Expected outcomes

| Outcome | Implication |
|:---|:---|
| **NUCLEATION-LANDED** | Lane A viable — cosmic IC can nucleate without photon; proceed OP-4 latent mechanism |
| **PARTIAL** | Saturation localizes; $V_{\mathrm{inc}}$ still zero on srs — v15b required |
| **HEAL-CONFIRMED** | Only photon lane works — strengthens manufacture program |
| **ENGINE-GAP** | No discrimination A vs C |

---

## Inputs (frozen context)

| Doc | Role |
|:---|:---|
| Three-lane context | `research/2026-06-12_three-lane-genesis-context.md` |
| v13 result | OP-2 container — `research/2026-06-12_genesis-v13-eigen-cavity_result.md` |
| v14 result | Transport partial — `research/2026-06-12_genesis-v14-cavity-transport_result.md` |
| Manufacturing traveler | Lane B OP map — `research/2026-06-10_electron-manufacturing-process-flow.md` |
| Vapor-lock framing | Lane A ontology — `research/2026-06-10_matter-as-vapor-locked-pump_framing.md` |
| genesis-23 null | `max|V_inc|=0` — heal baseline |
| Pair nucleation | C1+C2+C3 — `pair-production-axiom-derivation.md` |

---

## Parallel tracks (not blocked on v15)

| Track | Status |
|:---|:---|
| v14b pocket-frame peak metric | OPEN |
| v11 P11 production result doc | OPEN |
| R2 ferrite bench | Sibling repo |
| Compton ring-up (rank 2) | After v15 or v14b |

---

## Related

- Doctrine §6e + §7 three lanes
- Program ledger — `research/2026-06-12_genesis-program-status.md`
- LOOP GAP synthesis audit — §5b v15 row
