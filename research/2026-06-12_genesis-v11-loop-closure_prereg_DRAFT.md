# Genesis v11 — LOOP GAP closure pre-registration (DRAFT 2026-06-12)

> **STATUS: DRAFT** — awaiting Grant freeze. Rename to `_FROZEN` before implementor execution.
>
> **Charter:** `_orchestration/2026-06-12_loop-gap-v11-charter.md`
> **Synthesis + audit:** `research/2026-06-12_loop-gap-electron-resonator-synthesis.md`
> **KB doctrine:** `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md`
> **Baseline:** v10 production (`research/2026-06-12_genesis-v10-cvr-convergence_result.md`) — LOOP GAP **open**.

**Tier:** v11 convergence build — first run whose **primary falsifier** is **zero-drive persistence** (P11), not CVR-SET under drive.  
**Lane:** implementor. Extend v10 platform; do not reopen v10 Decisions 1–5 without Grant.

---

## 0. Corpus-grep (ave-prereg Step 1)

**Target:** Under **memristive $\tau_{\mathrm{relax}}$ saturation** on discrete srs, does the lattice show **P11 zero-drive persistence** that **fails** when Level-2 dynamics are ablated — without claiming mass until **matched-baseline 2×** passes?

| Prior item | Relevance | v11 relation |
|---|---|---|
| `chiral_lattice_v10.py` + v10 result | Snap + IC partial CVR-SET; ablations not isolating | **Platform base** |
| `k4_tlm.py` `use_memristive_saturation` | $\mathrm{d}S/\mathrm{d}t$ backward-Euler lag | **Port to srs** (primary new code) |
| `tau-relax-derivation.md` §3–§4 | $\tau_{\mathrm{relax}}=\ell_{\mathrm{node}}/c$ | Canonical $\tau$ |
| `substrate-hysteresis-index.md` §5b | LOOP GAP vs Ω_freeze | Success criterion |
| `loop-gap-electron-resonator-closure-doctrine.md` | Plumber order + fool modes | Gate design |
| genesis-23 result | Bulk $V\equiv 0$ from transverse | **v11b** only (gated) |
| R2 prereg FROZEN | Ferrite bench | **Sibling** — not blocking v11a sim |

**Genuinely open:** First discrete srs run with **integrated $S(t)$ lag** and **P11 quiescence gate**.

---

## 1. Grant decisions (proposed — freeze at ratification)

| ID | Proposed ruling | v11 implementation |
|---|---|---|
| D1 | Inherit v10 B-primary / A-partial | srs cells + diamond null; no change |
| D2 | **Add Level-2 memristive leg** alongside snap | `vector_tlm_step_v11` with per-node $S(t)$; snap **retained** but ablation-required |
| D3 | **P11 primary**; P6 secondary | Promotion requires P11 PASS + structure_driven_2× |
| D4 | Inherit tri-channel χ + $H_*$ readout | Unchanged from v10 |
| D5 | Ω_freeze IC ON + ablation | Unchanged; must not satisfy P11 alone |
| D6 | Compton ring-up arm | Sweep `n_drive` in units of $\tau_{\mathrm{relax}}$ steps |
| D7 | v11b bulk container | **BLOCKED** until A44 two-sector adjudication |

---

## 2. Physical picture (Step 1.5)

- **Substrate:** periodic srs net, vector scatter+connect (v10 inheritance).
- **Level-2 medium:** per-node saturation state $S_i(t)$ evolves
  $\mathrm{d}S/\mathrm{d}t=(S_{\mathrm{eq}}(A_i)-S_i)/\tau_{\mathrm{relax}}$ with backward Euler per scatter step; $z_{\mathrm{local},i}=1/\sqrt{S_i}$.
  At $\omega\tau\ll 1$ reduces to v10 Op14; near yield, $S$ lags $S_{\mathrm{eq}}$ → **pinched hysteresis loop** (consistency-class target).
- **Snap:** retained from v10; **hypothesis:** snap + lag **together** may yield P11; **falsifier:** P11 PASS with memristive ON but snap OFF would demote snap as necessary.
- **Drive:** inherit linear packet; **D6 arm** scales `n_drive` ∈ `{0.25, 0.5, 1.0, 2.0} × N_{\tau}` where $N_{\tau}=\lceil \tau_{\mathrm{relax}}/\Delta t\rceil$ (discrete analogue of ring-up).
- **Quiescence:** after drive-off, continue **$N_{\mathrm{quiet}}=4\,N_{\tau}$** steps with **no** `add_drive` — P11 reads here only.

---

## 3. Platform specification

### 3.1 New module

**`src/ave/core/chiral_lattice_v11.py`** extending v10:

1. `SatState` array `S_lag` shape `(n_nodes,)`, init $S_{\mathrm{eq}}(A)$ at $t=0$.
2. `vector_tlm_step_v11`: after amplitude update, backward-Euler $S$ lag; use $S_lag$ for $z_{\mathrm{local}}$ in Op3 connect.
3. `memristive_ablation` flag: when False, instant $S_{\mathrm{eq}}$ (reverts to v10 Op14 path).
4. `run_p6_cell_v11`: adds quiescence segment; computes P11 metrics.

### 3.2 P11 — zero-drive persistence (PRIMARY)

Measured after quiescence window:

| Metric | Definition | PASS threshold (proposed) |
|:---|:---|:---|
| `E_persist_ratio` | $E_{\mathrm{loc}}(t_{\mathrm{end}})/E_{\mathrm{loc}}(t_{\mathrm{driveoff}})$ | $\ge 0.85$ |
| `A_persist_ratio` | $\max A^2$ quiescent / $\max A^2$ during drive | $\ge 0.80$ |
| `theta_persist` | $|\Delta\theta|_{\mathrm{quiet}}/\|\Delta\theta\|_{\mathrm{drive}}$ | $\ge 0.75$ |
| `loop_proxy` | $\sum |S_{\mathrm{eq}}-S_{\mathrm{lag}}|$ over quiescence | $>0$ (Level-2 active) |

**P11 PASS:** all four, on **≥1** srs +z cell, with **memristive ON**, and **P11 FAIL** on memristive-OFF ablation at matched amp.

**Not sufficient alone:** P6 CVR-SET, snap ledger, $e_{\mathrm{driveoff}}$ without quiescence.

### 3.3 Inherited gates (secondary)

- P6 bins (v10 logic) — report, do not promote on P6 alone.
- Matched-baseline 2× (`_matched_baseline_ok`) — **required** for any LANDED verdict.
- Snap / Ω-free / Op3 / Op14 / memristive ablations — full grid.
- χ sweep — inherit v10 values.

### 3.4 Controls

| Arm | Purpose |
|:---|:---|
| memristive-OFF | Level-1 null — must fail P11 |
| snap-OFF | Test snap necessity given lag |
| Ω-free | IC not remanence |
| v10 replay cell | Regression — same bins as v10 result doc |

---

## 4. Hypotheses

**H1 (LOOP GAP — primary):** Level-2 $\tau_{\mathrm{relax}}$ lag on discrete srs yields **P11 persistence** not achievable with Level-1 Op14 alone.

**H2 (snap synergy):** Rate-gated snap **enhances** P11 when paired with lag; snap alone (v10) is insufficient — already supported by v10 ablations.

**H3 (ring-up):** P11 retention maximized near `n_drive ~ N_{\tau}` (Compton-scale analogue); off-resonance drive underperforms.

**H4 (emergence):** P11 PASS is **emergence-class** only if memristive-OFF fails and no new fit parameters beyond canon $\tau_{\mathrm{relax}}$, $\alpha$, lattice geometry.

**H5 (discrimination):** Persistence with $\theta$ wrong sign (−z) or diamond cells does **not** count toward electron claim (geometry filter).

---

## 5. Verdict ladder

| Verdict | Condition |
|:---|:---|
| **LANDED** | P11 PASS + memristive ablation FAIL + structure_driven_2× PASS + ≥1 +z srs |
| **PARTIAL** | P11 PASS but 2× FAIL or only −z |
| **LOOP GAP OPEN** | P11 FAIL on all cells (default prior) |
| **CLIP** | P11 tracks only `n_drive` with no loop_proxy — apparatus |

---

## 6. Deliverables

| Artifact | Path |
|:---|:---|
| Engine | `src/ave/core/chiral_lattice_v11.py` |
| Tests | `src/tests/test_chiral_lattice_v11.py` |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_v11_genesis.py` |
| Result | `research/2026-06-12_genesis-v11-loop-closure_result.md` |
| JSON | `assets/sim_outputs/genesis_v11_loop_closure.json` |

---

## 7. Run workflow

```bash
# Smoke (~2 min)
python src/scripts/vol_1_foundations/chiral_lattice_v11_genesis.py --smoke

# Production (budget ~45–90 min — document wall time at run)
python src/scripts/vol_1_foundations/chiral_lattice_v11_genesis.py
```

**Update protocol after each run:**

1. Write result doc with verdict ladder outcome.
2. Update `substrate-hysteresis-index.md` §5b one-liner.
3. If LANDED: open discrimination pass (`ave-discrimination-check`) before matrix promotion.
4. If FAIL: queue v11b only if Grant unblocks D7.

---

## 8. Out of scope (v11a)

- R2 ferrite bench execution (sibling implementor).
- Bulk $V_{\mathrm{inc}}$ source / genesis-23 converter (v11b).
- Matrix row promotion without 2× + discrimination.
- Reopening v9/v10 D1 substrate ruling.

---

## 9. Discrimination (pre-declared)

SM-null: persistence is **any** nonlinear hysteresis — report whether linear Op14-only control fails.

AVE-distinct: persistence correlates with **canon** $\tau_{\mathrm{relax}}=\ell_{\mathrm{node}}/c$ scaling when lattice spacing refined (smoke grid optional).

Interpretive alternative: persistence is **numerical artifact** of backward Euler — ablation with $\tau\to 0$ instant limit must recover v10.
