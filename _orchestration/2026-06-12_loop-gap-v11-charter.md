# LOOP GAP — v11 charter + implementation audit (2026-06-12)

**Epic:** genesis loop closure (electron manufacture)  
**Status:** CHARTER ACTIVE — prereg DRAFT; implementor **PENDING** freeze  
**Parent synthesis:** `research/2026-06-12_loop-gap-electron-resonator-synthesis.md`  
**KB:** `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md`  
**Prereg:** `research/2026-06-12_genesis-v11-loop-closure_prereg_DRAFT.md`

---

## Phase 0 — Documentation landed (2026-06-12) ✅

Session-critical synthesis preserved in proper channels:

| Artifact | Path |
|:---|:---|
| KB routing aid | `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` |
| Full synthesis + audit matrix | `research/2026-06-12_loop-gap-electron-resonator-synthesis.md` |
| v11 prereg DRAFT | `research/2026-06-12_genesis-v11-loop-closure_prereg_DRAFT.md` |
| This charter | `_orchestration/2026-06-12_loop-gap-v11-charter.md` |

Cross-links updated: `substrate-hysteresis-index.md` §6, `device-circuit-models.md` §5, manufacturing traveler §8.

---

## Phase 1 — Grant freeze (PENDING)

- [ ] Grant reviews v11 prereg DRAFT (D1–D7, P11 thresholds)
- [ ] Rename prereg to `_FROZEN`
- [ ] Open implementor branch off `main` (not direct-to-main)

---

## Phase 2 — v11a implementor (PENDING)

**Deliverable:** `chiral_lattice_v11.py` + driver + tests + production run.

**Scope (frozen at Phase 1):**

1. Port memristive $S(t)$ from `k4_tlm.py` pattern to discrete srs step.
2. Implement P11 quiescence gate (distinct from v10 `e_driveoff`).
3. D6 Compton ring-up sweep in `n_drive`.
4. Full ablation grid: memristive, snap, Ω-free, Op3, Op14.
5. Retain matched-baseline 2× — **no LANDED without it**.

**Explicit non-goals (v11a):** bulk $V_{\mathrm{inc}}$ source, R2 bench, matrix promotion.

**Skills (mandatory):** `ave-prereg`, `substrate-native-check`, `consistency-vs-emergence`, `ave-driver-script-honesty`, `ave-discrimination-check`, `verify-before-cite`.

---

## Phase 3 — Result + corpus update (PENDING)

- [ ] `research/2026-06-12_genesis-v11-loop-closure_result.md`
- [ ] `substrate-hysteresis-index.md` §5b v11 one-liner
- [ ] If PARTIAL/LANDED: orchestration index priority update

---

## Phase 3b — Cross-sector engine integration (2026-06-12) ✅

| Artifact | Path |
|:---|:---|
| Core module | `src/ave/core/cross_sector_coupling.py` |
| Coupled hook | `k4_cosserat_coupling.CoupledK4Cosserat.use_trilinear_converter` |
| Tests | `src/tests/test_cross_sector_coupling.py` (6/6) |
| GAP-1 driver | `cross_sector_gap1_closure.py` — smoke **PASS** |
| Prereg DRAFT | `research/2026-06-12_cross-sector-engine-integration_prereg_DRAFT.md` |

**GAP-1 production:** direct seed $6.08\times 10^{-6}$; genesis-23 photon replay $3.60\times 10^{-7}$ (gyrotropic + interior inject). Prereg **FROZEN**.

---

## Phase 4 — v11b bulk container (PARTIAL — source landed, confinement open)

**Gate:** Grant A44 adjudication (single-sector vs two-branch ω→V source).

**If unblocked:** discrete or coupled engine arm testing $\max|V_{\mathrm{inc}}|>0$ from transverse seed with $\Gamma_{\mathrm{bulk}}$ boundary — genesis-23 closure criterion.

---

## Implementation audit summary (2026-06-12)

Full matrix: synthesis doc §3. Headline:

| Emerges from lattice today | Missing / not in srs v10 |
|:---|:---|
| Op14/Op3 reactive trap, writhe geometry, yield from $\alpha$ | $\tau_{\mathrm{relax}}$ ODE, P11 remanence, Compton ring-up, bulk container, 2× |
| Snap machinery (not isolating) | Conservative lock path (sibling engines only) |

**Classification discipline:** Only P11 PASS + ablation contrast counts as **emergence candidate** for remanence. v10 CVR-SET is **consistency/emergence under drive**, not mass.

---

## How to run + update v11 (operator card)

### Run

```bash
cd /Users/grantlindblom/AVE-staging/AVE-Core
python src/scripts/vol_1_foundations/chiral_lattice_v11_genesis.py --smoke   # after implement
python src/scripts/vol_1_foundations/chiral_lattice_v11_genesis.py             # production
pytest src/tests/test_chiral_lattice_v11.py -q
```

### After each production run

1. Result doc from template in prereg §6.
2. JSON → `assets/sim_outputs/genesis_v11_loop_closure.json` (gitignored).
3. KB §5b one-liner in `substrate-hysteresis-index.md`.
4. Verdict ladder from prereg §5 — no matrix promotion on PARTIAL.
5. PR with audit tag pattern per `CLAUDE.md` (orchestration merge gate).

### Regression

v11 driver must include **v10 replay** cell — bins should match `research/2026-06-12_genesis-v10-cvr-convergence_result.md` within documented tolerance.

---

## Open decisions for Grant

| ID | Question |
|:---|:---|
| G1 | P11 threshold values (proposed in prereg §3.2) — ratify or tighten |
| G2 | Freeze D7 block on v11b until A44? (recommended: yes) |
| G3 | R2 bench parallel track — same epic or sibling? |
| G4 | Promote LOOP GAP KB leaf to vol9 ch17 index entry? |

---

## Related epics

- v10 CVR convergence — **merged context** (PR #207 branch)
- R2 constitutive loop bench — sibling, not run
- Vol 9 KB discipline pass — `_orchestration/2026-06-12_vol9-kb-discipline-pass.md`
- Electron manufacturing traveler — `research/2026-06-10_electron-manufacturing-process-flow.md`
