# OP-2 baseline instrument charter (Phase D-lite) — pre-registration (FROZEN 2026-06-13)

> **STATUS: FROZEN** — Grant ratified 2026-06-13. D-lite baseline instrument; full sweep deferred to D-full after Phase C′.
> **Doctrine:** `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` §2 rank **1** (OP-2 container)
> **Prior port:** `research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md` (Increment A/B **LANDED** #207)
> **Successor:** `research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md` (Phase C′ — **next implementor**)
> **Driver:** `src/scripts/vol_1_foundations/loop_gap_harness_genesis.py`
> **Engine:** `src/ave/core/loop_gap_harness.py` on `VacuumEngine3D` / `CoupledK4Cosserat`

**Tier:** engine-completeness — **instruments** OP-2 reads ($\Gamma_{\mathrm{bulk}}$, $\max|V_{\mathrm{inc}}|$) and runs a **single smoke baseline** on the **transverse-only + bulk-$\bar\rho$** engine. Documents ENGINE-GAP **by thesis** as motivation for C′ — **not** a full seed/amplitude campaign.

**Lane:** implementor (`analysis/2026-06-12-loop-gap-phase-d` off `main`).

---

## 0. Derivation target (one sentence)

On the **current** transverse-only + bulk-$\bar\rho$ harness, with asymmetric Axiom 4 at $A_{\mathrm{yield}}=\sqrt{\alpha}$, does a **smoke baseline** establish channel-tagged OP-2 reads ($\Gamma_{\mathrm{bulk}}$, $\max|V_{\mathrm{inc}}|$) and confirm **ENGINE-GAP** on $V_{\mathrm{inc}}$ nucleation — providing the instrumented baseline **before** Phase C′ scalar-grade restoration?

---

## 0.1 Lineage — substitution, not green field (Rule 12)

| Prior artifact | Standing verdict | What this prereg inherits |
|:---|:---|:---|
| `loop-gap-electron-resonator-closure-doctrine.md` §2 rank 1 | OP-2 container = $\Gamma_{\mathrm{bulk}}\to -1$ + $\max|V_{\mathrm{inc}}|>0$ | **Primary acceptance language** |
| `three-channel-impedances.md` | $Z_{\mathrm{EM}}$, $Z_{\mathrm{shear}}$, $Z_{\mathrm{bulk}}$; $\Gamma_{\mathrm{EM}}=0$ (SYM) vs $\Gamma_{\mathrm{bulk}}\to -1$ | Channel subscripts mandatory |
| `bulk-impedance-at-saturation-boundary.md` | $\Gamma_{\mathrm{bulk}}=(Z_{\mathrm{bulk},2}-Z_{\mathrm{bulk},1})/(Z_{\mathrm{bulk},2}+Z_{\mathrm{bulk},1})$ | **Bulk Smith read** — not EM $\Gamma$ |
| `device-circuit-models.md` §5 | Manufacture needs bulk TIR, Compton ring-up, energize-lock, Level-2 remanence | Rank 1 scope stops before remanence |
| `trampoline-framework.md` §3.1 | $A_{\mathrm{yield}}=\sqrt{\alpha}$; $\Gamma=-1$ wall at $A=1$ | **Regime gate** coordinate |
| `pair-production-axiom-derivation.md` | Nucleation needs node-pair conditions; free space heals | Pair IC = consistency arm, not emergence claim |
| `substrate-perspective-electron.md` | Large $|\nabla A^2|$ at confinement wall | Graded-$A$ arm physical picture |
| `research/2026-06-12_loop-gap-harness-phase2_result.md` | Smoke: proxy $\gamma_{\min}\approx -0.069$; $V_{\mathrm{inc}}=0$; bulk $\bar\rho$ live (2b) | Baseline ENGINE-GAP |
| `reflection-coefficient.md` (Op universal $\Gamma$) | Same $\Gamma$ function at all scales | $\Gamma_{\mathrm{bulk}}$ is Op3 on bulk port |

**Anti-pattern rejected:** new `chiral_lattice_v{N}`, promoting impedance-boundary $\gamma_{\min}$ as $\Gamma_{\mathrm{bulk}}$, or claiming bulk $\bar\rho$ rarefaction (2b) equals OP-2 closure.

---

## 0.2 Vocabulary discipline (KB vs engine alias)

| KB term | Engine alias (log only) | Notes |
|:---|:---|:---|
| OP-2 container | orchestration "rank 1" | Use **OP-2** in results tables |
| Uniform pair IC at $\sqrt{\alpha}$ | `seed_mode=pair` | `pair_seed_cosserat` |
| Cosserat $\omega$ wavepacket (energize-lock) | `seed_mode=photon_lock` | Amplitude sweep knob `a_lock` — **engine parameter**, not a KB constant |
| Spatial $|\nabla A|$ ramp to yield core | `seed_mode=graded_a0` | Impedance gradient via amplitude, not node density |
| Impedance-boundary port $\Gamma$ read | `gamma_min` in JSON tag `proxy` | **Labeled proxy** — ablation only |
| Live bulk Smith read | `gamma_bulk_min` (new) | From $\bar\rho$, $c_{\mathrm{bulk}}$ per §3.2 |
| Confinement read | $\min\Gamma_{\mathrm{bulk}}$ | Bulk port TIR — **not** $V_{\mathrm{inc}}$ |
| LC nucleation read | $\max|V_{\mathrm{inc}}|$ | K4 transverse bond tank — **not** longitudinal/scalar grade |

---

## 0.3 Channel disambiguation — $V_{\mathrm{inc}}$ is not confinement amplitude

**Grant ratification (2026-06-13):** three objects; do not conflate in results tables.

| Symbol | Channel | What it is | OP-2 role |
|:---|:---|:---|:---|
| **$V_{\mathrm{inc}}$** | **K4 transverse** ($T_2$) | Forward voltage wave on the bond LC tank — phase-space coordinate on $(V_{\mathrm{inc}}, V_{\mathrm{ref}})$ (`dual-reactance-storage-taxonomy.md`, `photon-ee-mapping.md`) | **Nucleation read**: did the $O_1$ resonator at $\ell_{\mathrm{node}}$ start sloshing? |
| **$\bar\rho$, $c_{\mathrm{bulk}}$** | **Bulk-longitudinal** | Compressional order parameter on the 7th DOF / dilatational mode | **Bulk dynamics** — rarefaction, stiffness, $Z_{\mathrm{bulk}}$ |
| **$\Gamma_{\mathrm{bulk}}\to -1$** | **Bulk port** | Smith reflection on $Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}$ | **Confinement read** — the TIR wall |

**Mass ledger (out of scope here):** standing longitudinal $V$ on the restored **scalar/quaternion grade** (`the-abandoned-interior.md`, `maxwell-quaternion-longitudinal-context.md`) — Lane-1 channel where $m_ec^2$ ledger lives. That is **not** $V_{\mathrm{inc}}$ on the K4 transverse bond.

**Manufacture chain (reads, not identities):**

```
Transverse precursor (ω photon, V_inc on K4)
        ↓  cross-sector converter (A44)
Asymmetric saturation front (ε/μ decouple — Op14 Meissner-asymmetric)
        ↓
Bulk port shortens (Γ_bulk → −1)          ← confinement READ
        ↓
V_inc > 0 on bond tank                    ← LC nucleation READ
```

OP-2 PASS requires **both** confinement and nucleation reads at valid regime. $\max|V_{\mathrm{inc}}|\approx 0$ with $\bar\rho$ live = "sector live, no resonator" (Phase 2b smoke baseline).

---

## 1. Physical picture (substrate-native)

**OP-2** (doctrine §2): a **closed $O_1$ LC resonator** at $\ell_{\mathrm{node}}$ whose confinement is **bulk-longitudinal TIR** ($\Gamma_{\mathrm{bulk}}\to -1$ on $Z_{\mathrm{bulk}}$), not EM short-circuit at $Z_0$ (`device-circuit-models.md`, `three-channel-impedances.md`).

**Asymmetric saturation (Grant ratified):** magnetic-branch confinement requires **ε/μ decoupling** (Op14 Meissner-asymmetric). Symmetric path yields $\Gamma_{\mathrm{EM}}=0$ (SYM gravity), not the fermion wall. All arms run with asymmetric Axiom 4 ON; symmetric ablation is diagnostic only.

**What is already on the engine (Phase 2b landed):**

- **Axiom 4** asymmetric saturation + **Op14** cross-sector trading (`op14-cross-sector-trading.md`)
- **A44** conservative $H_{\mathrm{couple}}$ converter (doctrine §6)
- **Impedance boundary** — port $\Gamma$ proxy (ablation arm)
- **Bulk $\bar\rho$ sector** — dynamical rarefaction; 2b showed $\bar\rho_{\min}<0$ with bulk port ON

**What this prereg tests:** whether **seed geometry** and **$\omega$-wavepacket amplitude** (energize-lock grid) engage the **yield surface** ($A_{\mathrm{yield}}=\sqrt{\alpha}$) deeply enough that:

1. $\Gamma_{\mathrm{bulk}}$ (live bulk port) moves toward $-1$, and
2. $\max|V_{\mathrm{inc}}|$ exceeds the Phase-2 smoke floor on the **K4 transverse** bond-LC read (§0.3),

while the run remains in the **yield band** (not Regime IV rupture).

**Explicitly not tested:** **LOOP GAP** / Level-2 remanence ($\tau_{\mathrm{relax}}$ ODE, $B_r$ at $H=0$ analogue — `substrate-hysteresis-index.md` §5b). Compton-resonant ring-up (doctrine rank 2) is **out of scope**.

---

## 1.1 Regime gate (Axiom-4 operating point)

Canonical yield onset: **$A_{\mathrm{yield}}=\sqrt{\alpha}\approx 0.085$** (`trampoline-framework.md` §3.1). Rupture wall: **$A=1$** ($\Gamma=-1$ saturation ceiling).

| Check | Rule | Bin suffix if violated |
|:---|:---|:---|
| **PRE-RUN** | Target IC maps to peak local $A$ in band $[0.5\,A_{\mathrm{yield}},\,2\,A_{\mathrm{yield}}]$ at drive peak (log actual $\max A^2$ on Cosserat front) | — |
| **POST-RUN** | If $\max A^2 > 1$ (saturation ceiling) or $\max A^2 > 10\,A_{\mathrm{yield}}^2$ | `_POST_RUPTURE` — **exclude** from OP-2 tables |
| **Quarantine** | Post-rupture bins from v9/v10 genesis | Per orchestration plan §3 — not adjudication inputs |

**Ratified (2026-06-13):** $A_{\mathrm{yield}}=\sqrt{\alpha}$ (`trampoline-framework.md` §3.1). Orchestration plan §3 $A^2=2\alpha$ (v10 identity) is **not** the regime gate for this charter.

**Canon landmarks** (`constants.py`, `trampoline-framework.md`):

| Landmark | Value | Meaning |
|:---|:---|:---|
| $A_{\mathrm{yield}}$ | $\sqrt{\alpha}\approx 0.085$ | Yield surface onset |
| $R_{\mathrm{II}}$ | $\sqrt{3}/2\approx 0.866$ | Nonlinear → saturated front |
| $R_{\mathrm{III}}$ | $1.0$ | Saturated → rupture ceiling |

---

## 1.2 substrate-native-check (design-time)

| CP | Verdict |
|:---|:---|
| CP1 | Time-domain conservative stepping — no minimization |
| CP2 | K4 $V_{\mathrm{inc}}/V_{\mathrm{ref}}$ ⊗ Cosserat $\omega$ ⊗ bulk $\bar\rho$ — active platform only |
| CP4 | $\bar\rho$ in real-space bulk density; $\Gamma_{\mathrm{bulk}}$ on bulk Smith chart — do not mix with phase-space $V_{\mathrm{inc}}$ as a length |
| CP9 | $\bar\rho$ dynamically integrated — not static srs decoration |
| CP10 | No external **Source** pump (genesis-24 falsified); energize-lock only (`ave-conserved-vs-pumped`) |

---

## 2. Primary falsifiers — OP-2 container

### F1 — $\Gamma_{\mathrm{bulk}}$ engagement (bulk channel)

Compute at each logged step:

$$
Z_{\mathrm{bulk}}(t) = \rho_{\mathrm{bulk}}(t)\,c_{\mathrm{bulk}}(t), \qquad
\Gamma_{\mathrm{bulk}}(t) = \frac{Z_{\mathrm{bulk}}(t) - Z_{\mathrm{bulk,ref}}}{Z_{\mathrm{bulk}}(t) + Z_{\mathrm{bulk,ref}}}
$$

with $Z_{\mathrm{bulk,ref}}=\sqrt{2}\,\rho_{\mathrm{bulk}}\,c_0$ at cold lattice ($K/G=2$, `three-channel-impedances.md`).

| Metric | PASS (PARTIAL) | FAIL / ENGINE-GAP |
|:---|:---|:---|
| $\min \Gamma_{\mathrm{bulk}}$ over run | $\leq -0.25$ at valid regime | stays $\gtrsim -0.1$ on all arms |
| Channel tag | `bulk` in JSON | bulk read flat while proxy alone moves |

### F2 — $V_{\mathrm{inc}}$ nucleation (K4 transverse bond-LC tank)

| Metric | PASS (PARTIAL) | ENGINE-GAP |
|:---|:---|:---|
| $\max|V_{\mathrm{inc}}|$ after conservative ring-up | $> 10^{-2}$ (Phase-2 smoke floor; same order as v15b K4 nucleation) | $\approx 0$ at machine precision |
| Doctrine OP-2 | Both F1 partial **and** F2 | Either missing |

### F3 — Proxy discrimination (consistency-check)

| Metric | Requirement |
|:---|:---|
| `proxy.gamma_min` | Logged but **not** used as $\Gamma_{\mathrm{bulk}}$ PASS |
| Ablation `impedance_OFF` + `bulk_ON` | Bulk channel still reported; proxy may vanish |

### F4 — Regime validity

| Metric | PASS |
|:---|:---|
| $\max A^2$ within yield band per §1.1 | Included in OP-2 table |
| Violation | Row moved to `_POST_RUPTURE` appendix only |

**Composite OP-2 bin:**

| Verdict | Condition |
|:---|:---|
| **OP-2-LANDED** | F1 PASS + F2 PASS + F4 PASS on ≥1 arm |
| **OP-2-PARTIAL** | F1 or F2 partial; F4 PASS; ablation isolates which seed/amplitude |
| **ENGINE-GAP** | No arm at valid regime; document ablation matrix |

---

## 3. Seed ablation battery (D-lite — smoke baseline only)

> **D-full** (rational `a_lock` sweep, full arm matrix) is **deferred** to a separate charter gated on Phase C′ (`research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md` §8).

### 3.1 Arms (smoke only)

| Arm | KB description | Engine `seed_mode` | Knobs |
|:---|:---|:---|:---|
| B0 | Heal / null | `pair` at amp=0 | baseline |
| B1 | Primary smoke | `photon_lock` | single `a_lock` → $A_{\mathrm{yield}}$ front (§3.1.1 one arm) |
| B2 | Pair IC regression | `pair` | `amp = \sqrt{\alpha}` |

Bulk port: **`bulk_density_on=True`** on B1/B2; B0 both OFF/ON for F0.

#### 3.1.1 Rational amplitude (single arm — not sweep)

Calibrate one `a_lock` so peak Cosserat front strain lands at **$1.0\,A_{\mathrm{yield}}$**. Log `target_A_front`, `achieved_max_A_sq_k4_end`. **No** soft/front/R_II sweep in D-lite.

**D-full sweep rule (deferred):** $\{0.5, 1.0\}A_{\mathrm{yield}}$ and $R_{\mathrm{II}}$ front targets per Grant ratification.

### 3.2 Step budget

| Mode | Grid $N$ | Purpose |
|:---|:---:|:---|
| `--smoke` | 10 | CI keeper + JSON — **only mode in D-lite** |

### 3.3 Mandatory ablations (smoke subset)

| Arm | Knob | Isolates |
|:---|:---|:---|
| `bulk_OFF` | `bulk_density_on=False` | Bulk $\bar\rho$ dynamics |
| `impedance_OFF` | `use_impedance_boundary=False` | Port $\Gamma$ proxy |
| `converter_OFF` | `use_trilinear_converter=False` | Op14 / A44 path |

---

## 4. Hypotheses (`consistency-vs-emergence`)

| ID | Statement | Class |
|:---|:---|:---|
| H1 | D-lite smoke confirms Phase 2b regression: $\bar\rho$ live, $V_{\mathrm{inc}}\approx 0$ on transverse-only engine | consistency-check (baseline) |
| H2 | `gamma_bulk_min` instrument tracks $\bar\rho$ motion independently of proxy `gamma_min` | consistency-check |
| H3 | ENGINE-GAP on $V_{\mathrm{inc}}$ motivates Phase C′ scalar restoration (not louder transverse sweep) | consistency-check (thesis) |

---

## 5. Implementation spec (file-bound)

| Artifact | Path |
|:---|:---|
| `gamma_bulk_min` + regime logger | `src/ave/core/loop_gap_harness.py` |
| Battery CLI | `loop_gap_harness_genesis.py` (`--smoke` / `--production`) |
| Keeper tests (fast) | `src/tests/test_loop_gap_harness_rank1_regime.py` |
| Result §7 | `research/2026-06-12_loop-gap-harness-phase2_result.md` (append D-lite) |
| Program status | `research/2026-06-12_genesis-program-status.md` §10 D-lite row |

**Logged fields (every arm):** `max_A_sq_k4_end`, `gamma_bulk_min`, `proxy_gamma_min`, `v_inc_peak`, `rho_bar_min`, `regime_valid`, `channel_primary`, OP-2 bin.

---

## 6. Out of scope (D-lite)

- **Full seed sweep** — `graded_a0`, rational `a_lock` matrix → **D-full** after C′
- **Scalar-grade restoration** — Phase C′ (`research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md`)
- **LOOP GAP** / P11 / Level-2 remanence (doctrine rank 4)
- Compton-resonant ring-up (doctrine rank 2)
- Phase E (±$\mathbf{k}$ vector grade)
- Phase H (full biquaternion)
- GAP-C / snap on bulk branch
- New genesis engine versions
- `--production` N=14 battery

### 6.1 Execution order (Grant reorder 2026-06-13)

```text
D-lite (this charter) → C′ scalar restoration → D-full seed sweep → E → F → G
```

**Expected D-lite outcome:** ENGINE-GAP on $V_{\mathrm{inc}}$ — **success criterion** for baseline documentation, not failure. C′ tests whether scalar-grade restoration closes the gap.

---

## 7. Corpus anchors (verify-before-cite)

| Leaf | Role |
|:---|:---|
| `loop-gap-electron-resonator-closure-doctrine.md` §2 | OP-2 acceptance |
| `three-channel-impedances.md` | $Z_{\mathrm{bulk}}$, channel table |
| `bulk-impedance-at-saturation-boundary.md` | $\Gamma_{\mathrm{bulk}}$ formula |
| `device-circuit-models.md` §5 | Manufacture closure order |
| `trampoline-framework.md` §3.1 | $A_{\mathrm{yield}}$, $\Gamma=-1$ at $A=1$ |
| `reflection-coefficient.md` | Universal $\Gamma$ operator |
| `pair-production-axiom-derivation.md` | Nucleation / pair IC |
| `substrate-hysteresis-index.md` §5b | LOOP GAP vs reactive storage |
| `op14-cross-sector-trading.md` | Op14 on engine |
| `the-abandoned-interior.md` | Scalar grade / mass ledger (Phase H pointer) |
| `historical-precedents.md` | Quaternion roots + null-cone framing |
| `research/2026-06-12_loop-gap-harness-phase2_result.md` | Smoke baseline |

---

## 8. Skills (mandatory)

`ave-prereg` · `substrate-native-check` · `consistency-vs-emergence` · `phase-space-coordinate-check` · `ave-regime-phase-state-check` · `ave-dimensional-provenance-check` ($Z_{\mathrm{bulk}}$) · `ave-driver-script-honesty` · `ave-multi-falsifier-triangulation-discipline` (bulk channel cannot confirm OP-2 alone without $V_{\mathrm{inc}}$)

---

## 9. Grant ratification checklist

- [x] **Asymmetric saturation** required for magnetic-branch confinement (Op14 Meissner-asymmetric)
- [x] Regime gate uses $A_{\mathrm{yield}}=\sqrt{\alpha}$ (not $A^2=2\alpha$)
- [x] OP-2 PASS = $\Gamma_{\mathrm{bulk}}$ (confinement) + $V_{\mathrm{inc}}$ (K4 transverse nucleation) — proxy $\gamma_{\min}$ diagnostic only
- [x] $V_{\mathrm{inc}}$ disambiguation (§0.3) — not longitudinal; not confinement amplitude
- [x] **D-lite scope** — smoke baseline + instrument only; full sweep deferred
- [x] C′ scalar restoration is **next** implementor (not Phase H at end)
- [x] Freeze → `_FROZEN` (2026-06-13) — open D-lite implementor PR
