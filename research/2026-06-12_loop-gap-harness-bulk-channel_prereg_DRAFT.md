# LOOP GAP harness — bulk-channel port pre-registration (DRAFT 2026-06-12)

> **STATUS: DRAFT** — corpus-grounded; awaits Grant ratification before FROZEN.
> **Epic:** `_orchestration/2026-06-12_loop-gap-unified-harness.md` Phase 2b
> **DAG:** `_orchestration/2026-06-12_loop-gap-engine-dag.md` § Rank 1b
> **Harness:** `src/ave/core/loop_gap_harness.py` (no new `chiral_lattice_v{N}`)

**Tier:** engine-completeness — closes synthesis audit row “Bulk $V_{\mathrm{inc}}$ container / $\Gamma_{\mathrm{bulk}}$ boundary” (`research/2026-06-12_loop-gap-electron-resonator-synthesis.md` §3.1) on the **active** K4 platform.

**Lane:** implementor (branch off `main` / current harness branch).

---

## 0. Derivation target (one sentence)

Port the **existing** `UnifiedGenesisEngine` rarefaction bulk-density sector (GAP-A: $\bar\rho$, $u_{\mathrm{adv}}$, candidate EOS, exact pressure ledger) into `VacuumEngine3D` behind `bulk_density_on=False` (KEEP-BOTH), then extend `loop_gap_harness` with **channel-tagged** rank-1 observables so $\Gamma_{\mathrm{bulk}}$ confinement is tested on the **bulk-longitudinal** branch — not conflated with EM $S_{11}$ at $Z_0$ or the impedance-boundary **proxy** alone.

---

## 0.1 Lineage — substitution, not green field (Rule 12)

| Prior artifact | Standing verdict | What this prereg inherits |
|:---|:---|:---|
| `UnifiedGenesisEngine` (`unified_genesis_engine.py`) | GAP-A/B documented; `bulk_density_on=False` ⇒ byte-identical to `CrystalGraftV4` | **Port target** — do not re-derive EOS or continuity |
| `research/2026-06-10_genesis-v5-seeded-snap_prereg.md` | Bulk sector discipline (CP9/CP10, clip suspects, candidate $\bar\rho_{\mathrm{cav}}$) | Apparatus-floor + substrate-native checkpoints |
| `research/2026-06-12_cross-sector-engine-integration_prereg_FROZEN.md` | GAP-1 converter **LANDED** on CoupledK4Cosserat | Converter stays on harness; **orthogonal** to bulk $\bar\rho$ |
| `loop-gap-electron-resonator-closure-doctrine.md` §3 | Bulk-longitudinal **absent** in srs; EM implemented | Channel routing mandate |
| `test_vacuum_moduli_and_channels.py` | $c_{\mathrm{EM}}$, $c_{\mathrm{shear}}$, $c_{\mathrm{bulk}}$ at $K/G=2$ | Constants gate only — dynamics still open |
| Harness Phase 2 smoke | `photon_lock`: $\Gamma\approx -0.069$; $V_{\mathrm{inc}}=0$ | Rank-1 partial; bulk proxy insufficient |

**Anti-pattern rejected:** new engine file, new gate ID without doctrine rank, or “enable all waves” master flag without increment boundaries.

---

## 0.2 Held contentions (not resolved by this prereg)

| ID | Tension | This prereg scope |
|:---|:---|:---|
| C1 (`synthesis.md` §1.3) | μ-channel R2 bench vs bulk confinement | Observables **channel-tagged**; R2 not promoted as electron closure |
| C4 | Single-sector flip vs two-branch $\omega\to V$ | A44 **closed** for converter; **GAP-C** ($V\leftrightarrow\bar\rho$) remains **out of scope** until Increment C adjudication |

---

## 1. Physical picture (substrate-native, before code)

- **EM-transverse:** K4 $V_{\mathrm{inc}}$ on T₂ ports — already on harness; fool mode #4 if used alone.
- **Shear / GW:** Cosserat $(u,\omega)$ + trilinear converter — GAP-1 path; feeds $V_{\mathrm{inc}}$ from $\omega$ at saturation front.
- **Bulk-longitudinal:** compressional $\bar\rho$ with rarefaction EOS $c_{\mathrm{bulk}}^2(\bar\rho)=c_0^2(1+\bar\rho/(1-\bar\rho^2))$ — **missing** on `VacuumEngine3D`; rank-1 confinement in doctrine is **$\Gamma_{\mathrm{bulk}}\to -1$**, not $\Gamma_{\mathrm{EM}}=0$.

**Impedance boundary (current):** moving $\Gamma$ wall on coupled K4+Cosserat ports = **CP10 boundary proxy**, not propagating bulk wave (substrate-native-check CP9). This prereg adds the **dynamical** $\bar\rho$ sector; proxy remains for ablation.

---

## 1.1 substrate-native-check (design-time)

| CP | Verdict |
|:---|:---|
| CP1 | Time-domain FDTD/RK2 — no minimization |
| CP2 | Coupled K4 $V$ ⊗ Cosserat $\omega$ ⊗ **bulk** $\bar\rho,u_{\mathrm{adv}}$ — port from `UnifiedGenesisEngine`, not `lbm_3d` / static srs |
| CP4 | $\bar\rho_{\mathrm{min}}$ in **real-space** bulk density; $\Gamma$ in port/Smith chart; do not mix |
| CP9 | $\bar\rho$ **dynamically** integrated (continuity), not algebraic centrifugal formula |
| CP10 | Snap machine **OFF** in Increment A; confinement from EOS stiffness + optional impedance wall, not bulk potential well |

---

## 2. Phased increments (mandatory — no monolithic “all waves” landing)

### Increment A — GAP-A port only (this prereg’s implementor deliverable)

| Knob | Default | Role |
|:---|:---:|:---|
| `bulk_density_on` | **False** | KEEP-BOTH: False ⇒ harness byte-identical to pre-port |
| `snap_on` | **False** | Snap is genesis-v5 D1 — **not** rank-1 container |
| `cross_sector_bulk_coupling` (GAP-C) | **False** | New physics surface; explicit Grant gate for Increment C |
| `use_impedance_boundary` | True (rank ≥1) | Proxy wall — ablation arm retained |

**Port scope:** $\bar\rho$, $u_{\mathrm{adv}}$, `pressure()` ledger, clip floors (`c2_floor`, `rho_floor`) from `UnifiedGenesisEngine` — **extract/module**, not rewrite.

### Increment B — Channel-tagged harness reads (same PR or follow-up)

Extend `LoopGapResult` / `snapshot_rank()` with:

| Tag | Observable | Coordinate |
|:---|:---|:---|
| `EM` | `max|V_inc|`, `max_A_sq_k4` | K4 port / T₂ |
| `shear` | `max|ω|`, `max_tau_zx` (optional `DarkWakeObserver`) | Cosserat / shear strain |
| `bulk` | `min(rho_bar)`, `min(c_bulk2)`, `bulk_stiffness_crossing` | Real-space $\bar\rho$ |
| `proxy` | `gamma_min` (impedance boundary) | Port $\Gamma$ proxy — **labeled proxy** |

### Increment C — OUT OF SCOPE (separate prereg)

- GAP-C seed-$V\leftrightarrow\bar\rho$ couplings
- D1 snap state machine + latent tally
- Rank 3–4 promotion on bulk sector alone

---

## 3. Primary falsifiers — rank 1b (channel-tagged)

### F0 — Regression (KEEP-BOTH)

| Metric | PASS |
|:---|:---|
| `bulk_density_on=False`, 200 harness smoke steps | `max|Δ|` vs pre-port baseline = 0 on K4 $V$, Cosserat $\omega$, existing harness scalars |

### F1 — Bulk sector live (Increment A)

| Metric | PASS | FAIL |
|:---|:---|:---|
| `bulk_density_on=True`, converter ON, seed `pair` | `min(rho_bar)` < 0 OR `c_bulk2_min` crosses 0 band without $|H|$ blow-up | detonation / NaN / $|H|$ runaway |
| Ablation `bulk_OFF` vs `bulk_ON` | bulk scalars differ at $t_{\mathrm{end}}$ | bulk_ON ≡ bulk_OFF |

### F2 — Proxy vs bulk discrimination (Increment B)

| Metric | PASS | FAIL |
|:---|:---|
| Rank-1 bin | Document **which channel** satisfied `P18_GAMMA_MAX` or $V_{\mathrm{inc}}$ floor | PASS claimed on EM-only read while bulk $\bar\rho$ flat |
| `impedance_OFF` + `bulk_ON` | Still report bulk channel; do not require $\gamma_{\min}$ proxy | — |

**Existing gates unchanged:** `P18_VINC_FLOOR`, `P18_GAMMA_MAX` (`genesis_v18_coupled.py`) — but rank-1 PASS requires **bulk tag** present in result JSON when `bulk_density_on=True`.

---

## 4. Hypotheses

**H1:** Impedance-boundary $\gamma_{\min}\approx -10^{-4}$ (Phase 2) reflects **proxy** engagement; live $\bar\rho$ rarefaction lowers bulk stiffness toward $\bar\rho_{\mathrm{cav}}$ band with stronger **bulk-channel** confinement signature than proxy alone.

**H2:** `bulk_density_on=True` does not restore $V_{\mathrm{inc}}$ for `photon_lock`-only seed without converter/pair path — channel separation holds (converter = shear→EM; bulk = container).

**H3:** KEEP-BOTH regression passes — bulk port does not break GAP-1 converter arms.

---

## 5. Mandatory ablation arms (extends DAG)

| Arm | Knob | Isolates |
|:---|:---|:---|
| `bulk_OFF` | `bulk_density_on=False` | GAP-A dynamics |
| `impedance_OFF` | `use_impedance_boundary=False` | $\Gamma$ proxy wall |
| `converter_OFF` | `use_trilinear_converter=False` | GAP-1 (existing) |
| `bulk_ON_impedance_OFF` | bulk on, wall off | bulk vs proxy |
| `heal` | zero seed (existing) | false positive |

---

## 6. Implementation spec (file-bound — no ad-hoc drivers)

| Artifact | Path |
|:---|:---|
| Bulk sector module or mixin | Port from `unified_genesis_engine.py` → `src/ave/topological/` or `src/ave/core/bulk_rarefaction_sector.py` |
| `VacuumEngine3D` hook | `EngineConfig.bulk_density_on` + step integration |
| Harness | `engine_config_for_rank()` + `LoopGapResult` bulk fields |
| Keeper | `src/tests/test_loop_gap_harness_bulk_channel.py` — F0 regression + F1 smoke |
| Driver | **Same** `loop_gap_harness_genesis.py` with `--bulk` flag (no new genesis driver) |
| Result | `research/2026-06-12_loop-gap-harness-bulk-channel_result.md` |

**Clip suspects (inherited from v5):** `c2_floor`, `rho_floor`, `nu_art_bulk` — swept in production, not tuned to PASS.

---

## 7. Out of scope

- `chiral_lattice_v19+`, new P19 gate IDs
- Snap / FLASH / D1–D8 genesis-v5 assembly
- Rank 4 P11 remanence (epic Phase 3 — unchanged)
- Promoting candidate $\bar\rho_{\mathrm{cav}}=-1/\varphi$ to canonical
- Full tri-channel FDTD with independent $H_{\mathrm{EM}}$, $H_{\mathrm{shear}}$, $H_{\mathrm{bulk}}$ saturation ride in one step (readout exists; dynamics merge is Increment A/B only)

---

## 8. Corpus anchors (verify-before-cite)

| Anchor | Role |
|:---|:---|
| `manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md` | $Z_{\mathrm{EM}}$, $Z_{\mathrm{shear}}$, $Z_{\mathrm{bulk}}$ definitions |
| `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` §3 | Three-channel routing + fool modes |
| `unified_genesis_engine.py` header GAP-A/B/C | Port boundaries |
| `_orchestration/2026-06-12_loop-gap-engine-dag.md` | Capability prerequisites |

---

## 9. Skills fired at design time

`ave-prereg` · `substrate-native-check` (CP1–CP10) · `consistency-vs-emergence` (rank-1 bulk = emergence candidate; constants = Class C) · `phase-space-coordinate-check` · `ave-apparatus-floor-attribution` (clip grid) · `ave-driver-script-honesty` (harness-only entry)
