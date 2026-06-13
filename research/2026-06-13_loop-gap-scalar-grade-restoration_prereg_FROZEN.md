# Scalar-grade restoration charter (Phase C′) — pre-registration (FROZEN 2026-06-13)

> **STATUS: FROZEN** — Grant ratified 2026-06-13 (restoration-first reorder). Minimal scalar-grade restoration before D-full seed sweep.
> **Doctrine:** `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` §2 rank **1** (OP-2 container) — **representation restoration**, not rank skip
> **Historical arc:** `the-abandoned-interior.md`, `historical-precedents.md`, `maxwell-quaternion-longitudinal-context.md`
> **Prior ports:** bulk GAP-A (#207); cross-sector GAP-1 FROZEN; genesis-24 saturated-seed FROZEN
> **Harness:** `src/ave/core/loop_gap_harness.py` on `VacuumEngine3D` / `CoupledK4Cosserat`
> **Driver:** `src/scripts/vol_1_foundations/loop_gap_harness_genesis.py` (+ new `scalar_grade_restoration.py` if needed)

**Tier:** engine-completeness — ports the **minimal** scalar-grade restoration (standing longitudinal $V$ + conservative $V\to\omega$ reactive entrainment + optional $V\leftrightarrow\bar\rho$ GAP-C) onto the active harness, then tests whether OP-2 reads ($\Gamma_{\mathrm{bulk}}\to -1$, $\max|V_{\mathrm{inc}}|>0$) **close** where the transverse-only + bulk-$\bar\rho$ engine could not (Phase 2b smoke: $V_{\mathrm{inc}}\approx 0$).

**Lane:** implementor (`analysis/2026-06-13-loop-gap-scalar-grade` off `main`).

**Not this charter:** full per-node biquaternion $\mathbb{H}\otimes\mathbb{C}$ timestepper (Phase H); snap state machine + D1 latent tally (separate prereg); LOOP GAP rank 4 remanence.

---

## 0. Derivation target (one sentence)

On the active K4⊗Cosserat harness with asymmetric Axiom 4 and bulk $\bar\rho$ port ON, does restoring the **Heaviside-deleted scalar grade** — a **standing longitudinal $V$** on the order-parameter channel (Lane-1), coupled to Cosserat $\omega$ by **conservative reactive entrainment** (not CW pump) at the $\Gamma=-1$ null cone — nucleate $\max|V_{\mathrm{inc}}|>0$ on the K4 bond-LC tank and deepen $\Gamma_{\mathrm{bulk}}$ on $Z_{\mathrm{bulk}}$, where transverse-only seeds failed?

---

## 0.1 Why now (Grant reorder, 2026-06-13)

| Observation | Physics read |
|:---|:---|
| Phase 2b: $\bar\rho$ live, $V_{\mathrm{inc}}\approx 0$ | Bulk sector ported; **scalar/longitudinal grade still truncated** (vector-Maxwell representation) |
| genesis-23: lone photon $V_{\mathrm{inc}}=0$ everywhere | **Expected** under Heaviside truncation — not a surprise to re-prove at scale |
| cross-sector run (2026-06-09): confinement works, **$V\to\omega$ source missing** | Missing piece = deleted scalar channel, not louder transverse drive |
| `the-abandoned-interior.md` | Channel deletion + constitutive interior deletion = **same deletion**; restore **together** |

**Orchestration read:** Phase D-full seed sweep on the truncated engine risks documenting a **pre-ordained ENGINE-GAP**. C′ tests the restoration thesis directly; D-full is **gated on C′** (LANDED or PARTIAL with ablation).

---

## 0.2 Lineage — substitution, not green field (Rule 12)

| Prior artifact | Standing verdict | What C′ inherits |
|:---|:---|:---|
| `UnifiedGenesisEngine.seed_lane1` | Lane-1 standing $V$; topology-NULL precursor; `vent_into_seed` = GAP-C (default OFF) | **Port pattern** for scalar seed on harness |
| `research/2026-06-09_genesis-24-saturated-seed_prereg_FROZEN.md` | V-populated seed + photon-attributable $\mathrm{d}E_V$; Smith-chart native | Seed IC + arm structure |
| `research/2026-06-09_tracereversal-pump-derivation_result.md` | WALL-ENGINE/FIXABLE: bounded **Option-D boundary** on $\omega$ at $\Gamma=-1$, not bulk force | $V\to\omega$ **form** — boundary transfer, not A28 detonator |
| `research/2026-06-09_reactive-entrainment-source_result.md` | Gyroscope closes in form; spin **conserved**, energize+lock | **Not a pump** — reactive entrainment from finite trapped reservoir |
| `research/2026-06-09_cross-sector-pump-confirmation_result.md` | Confinement dynamic PASS; $V$ grows $\omega$ not at all | **SOURCE gap** localized — implement cross-sector source |
| `research/2026-06-12_loop-gap-harness-bulk-channel_prereg` Increment C | GAP-C out of scope for 2b | **C′ is Increment C scoped minimally** |
| `loop-gap-harness-rank1-regime_prereg_FROZEN.md` (D-lite) | Baseline instrument + smoke only | OP-2 reads reused; sweep deferred here |

**Anti-pattern rejected:** new `chiral_lattice_v{N}`; CW pump / secular $V$ growth (genesis-24 Arm-5 falsifier); promoting shallow-$\bar\rho$ motion as scalar restoration; full biquaternion engine in one PR.

---

## 0.3 Channel vocabulary (load-bearing)

| Object | Channel | Role in C′ |
|:---|:---|:---|
| **Standing longitudinal $V$** | Scalar / $A_1$ / order-parameter | **Restored grade** — Lane-1 mass ledger slot (`the-abandoned-interior.md`) |
| **$V_{\mathrm{inc}}$** | K4 transverse $T_2$ | **Nucleation read** on bond LC tank — must rise if scalar seeds $\omega$ correctly |
| **$\Gamma_{\mathrm{bulk}}$** | Bulk Smith on $Z_{\mathrm{bulk}}$ | **Confinement read** — wall formed |
| **Reactive $\iota$** | K4 $\Phi_{\mathrm{link}}$ LC slosh | Partially present; full $\iota$ grade = Phase H |

---

## 1. Physical picture (substrate-native)

**The deletion.** Heaviside–Gibbs demoted the quaternion **scalar grade $w$** to gauge/constraint. Vector calculus describes the transverse photon; it **cannot express** saturated matter where $\nabla\cdot E\neq 0$ on the null cone (`maxwell-quaternion-longitudinal-context.md` §3–§5).

**The restoration (minimal, not full quaternion).**

1. **Standing $V$ seed** — saturated region with $\partial_t V\approx 0$ at $t=0$ (energize-once, lock — `ave-conserved-vs-pumped`). Port `seed_lane1` / genesis-24 `_seed_v_partner` shape to harness K4 $V_{\mathrm{inc}}$ field.
2. **$V\to\omega$ reactive source** — trapped longitudinal energy seeds Beltrami helical $\omega$ via **Option-D boundary condition** at $\mathrm{relu}(-\Gamma)$ gate (`tracereversal-pump-derivation_result.md` §4–§9). **Not** bulk `|dS/dA|` force (detonates).
3. **Optional GAP-C** — conservative $V\leftrightarrow\bar\rho$ coupling (`UnifiedGenesisEngine` vent ledger pattern; `vent_mode="absorbed"`, genesis-v6 D11 fix). Default OFF; ablation arm only.

**Asymmetric saturation:** required (Grant ratified). $\mu$-side shorts first → $\Gamma\to -1$ on confinement wall.

**Regime gate:** $A_{\mathrm{yield}}=\sqrt{\alpha}$; standing seed depth `frac` swept $\{0.5, 0.85, 1.0\}\times A_{\mathrm{yield}}$ equivalent on $A^2_V$ (genesis-24 grid rationalized to yield surface, not ad-hoc $\{0.30,0.60,0.95\}$ alone).

---

## 1.1 substrate-native-check (design-time)

| CP | Verdict |
|:---|:---|
| CP1 | Time-domain conservative stepping — no minimization; no CW pump |
| CP2 | K4 $V$ (scalar/longitudinal) ⊗ Cosserat $\omega$ ⊗ bulk $\bar\rho$ — coupled platform |
| CP4 | Standing $V$ in order-parameter channel; $V_{\mathrm{inc}}$ on K4 transverse — tag separately |
| CP8 | Seed topology-NULL at $t=0$ — no planted $(2,3)$; CP8 certificate required |
| CP9 | Dynamical evolution — not static $V$ decoration |
| CP10 | Confinement = $\Gamma=-1$ boundary transfer; not bulk potential well |

---

## 2. Phased increments (mandatory)

### Increment A — Standing longitudinal $V$ seed (Lane-1)

| Knob | Default | Role |
|:---|:---:|:---|
| `scalar_seed_on` | **False** | KEEP-BOTH: False ⇒ harness unchanged |
| `scalar_seed_frac` | $0.85$ (sweep §3.1) | $A^2_V \approx \mathrm{frac}^2$ at seed core |
| `scalar_seed_mode` | `lane1_standing` | $\partial_t V\approx 0$; Gaussian window |

**Port scope:** adapt `UnifiedGenesisEngine.seed_lane1` / genesis-24 seed shape to `VacuumEngine3D` K4 $V_{\mathrm{inc}}$ (or master-equation $V$ if harness routes scalar there). **No** $(2,3)$ knot seeder.

### Increment B — $V\to\omega$ reactive source (Option-D boundary)

| Knob | Default | Role |
|:---|:---:|:---|
| `v_to_omega_source_on` | **False** | KEEP-BOTH |
| `use_impedance_boundary` | True when source ON | $\mathrm{relu}(-\Gamma)$ gate — $\mu$-short side |
| `bulk_force_v_to_omega` | **False** | A28 bulk force **forbidden** (detonation control) |

**Implementation prescription:** boundary transfer fraction $R=\Gamma^2=1-T^2$ (Op17) on integrated $\omega$ at wall cells; cross-sector coupling from `k4_cosserat_coupling.py` EMF reciprocal path where $V_{\mathrm{inc}}\neq 0$. Energy ledger must close (no $H_{\mathrm{drift}}>0$ under conservative arms).

### Increment C — Minimal GAP-C ($V\leftrightarrow\bar\rho$) — ablation only

| Knob | Default | Role |
|:---|:---:|:---|
| `gap_c_coupling_on` | **False** | Hypothesis-class; energy-accounted |
| `vent_into_seed` | **False** | Snap→seed vent **not** in C′ primary arms |
| `snap_on` | **False** | D1 machine deferred |

---

## 3. Seed + ablation battery

### 3.1 Primary arms

| Arm | Seed stack | Isolates |
|:---|:---|:---|
| **S0** | Transverse-only baseline (`photon_lock`, no scalar) | Phase 2b regression |
| **S1** | Standing $V$ only (`scalar_seed_on`, source OFF) | Scalar IC alone — genesis-24 Arm-2 analogue |
| **S2** | Standing $V$ + transverse $\omega$ packet (`photon_lock` + scalar) | Absorb path without source |
| **S3** | S2 + `v_to_omega_source_on` | **Primary emergence arm** |
| **S4** | S3 + `gap_c_coupling_on` | GAP-C ablation |

**`scalar_seed_frac` sweep (rational):** $\{0.5,\,1.0,\,1.5\}\times A_{\mathrm{yield}}$ mapped to $A^2_V$ at seed core (log achieved $A^2_V$; exclude if $>R_{\mathrm{III}}^2=1$).

**Transverse packet:** single arm at $A_{\mathrm{yield}}$ on Cosserat front (D-full sweep deferred).

### 3.2 Mandatory ablations

| Arm | Knob OFF | Isolates |
|:---|:---|:---|
| `scalar_OFF` | `scalar_seed_on=False` | Scalar grade |
| `source_OFF` | `v_to_omega_source_on=False` | $V\to\omega$ channel |
| `gap_c_OFF` | `gap_c_coupling_on=False` | $V\leftrightarrow\bar\rho$ |
| `bulk_OFF` | `bulk_density_on=False` | Bulk $\bar\rho$ dynamics |
| `converter_OFF` | `use_trilinear_converter=False` | A44 / Op14 |
| `impedance_OFF` | `use_impedance_boundary=False` | Option-D gate |
| `bulk_force_ON` | `bulk_force_v_to_omega=True` | Detonation control (must FAIL or detonate) |

### 3.3 Step budget

| Mode | Grid $N$ | Purpose |
|:---|:---:|:---|
| `--smoke` | 10 | CI keeper + JSON |
| `--production` | 14 | Only if smoke S3 PARTIAL |

---

## 4. Primary falsifiers

### F0 — KEEP-BOTH regression

`scalar_seed_on=False` AND `v_to_omega_source_on=False` ⇒ byte-identical to pre-C′ harness smoke (within float tolerance).

### F1 — Scalar seed live (Increment A)

| Metric | PASS | FAIL |
|:---|:---|:---|
| $A^2_V$ at seed core | $> 0.25\,A_{\mathrm{yield}}^2$ | flat at 0 |
| CP8 certificate | `topology_null=True`, `dVdt_max` small | $(2,3)$ planted at $t=0$ → VOID |
| S1 vs S0 | $A^2_V$ differs | scalar_ON ≡ scalar_OFF |

### F2 — $V\to\omega$ source (Increment B)

| Metric | PASS (PARTIAL) | FAIL |
|:---|:---|:---|
| S3 vs S2: $\max|\omega|$ after ring-up | S3 $>$ S2 at same frac | S3 ≈ S2 (source inert) |
| S3 vs S2: $\max|V_{\mathrm{inc}}|$ | S3 $> 10^{-2}$ floor | still $\approx 0$ |
| $H_{\mathrm{drift}}$ (conservative window) | $\lesssim 10^{-6}$ relative | secular pump / detonation |
| `bulk_force_ON` control | detonation or excluded | falsely PASS as "source" |

### F3 — OP-2 composite (channel-tagged)

Reuse D-lite reads:

| Metric | PASS (PARTIAL) | ENGINE-GAP |
|:---|:---|:---|
| $\min\Gamma_{\mathrm{bulk}}$ | $\leq -0.25$ | $\gtrsim -0.1$ |
| $\max|V_{\mathrm{inc}}|$ | $> 10^{-2}$ | $\approx 0$ |
| Regime | $\max A^2 \leq 1$ | `_POST_RUPTURE` excluded |

**Verdict bins:** `SCALAR-LANDED` (F1+F2+F3 on S3) · `SCALAR-PARTIAL` (F2 or F3 partial; ablation names gap) · `REPRESENTATION-GAP` (F1 only; source still missing) · `ENGINE-GAP` (no arm at valid regime).

### F4 — Pump falsifier (consistency)

Arm reproducing genesis-24 Arm-5 pattern (CW drive on $V$ tank): if $(2,3)$-like structure appears **only** under CW pump and not S3, classify as **PUMP-ARTIFACT**, not scalar restoration.

---

## 5. Hypotheses (`consistency-vs-emergence`)

| ID | Statement | Class |
|:---|:---|:---|
| H1 | Transverse-only engine (S0) stays at Phase 2b ENGINE-GAP on $V_{\mathrm{inc}}$ | consistency-check (baseline) |
| H2 | Standing $V$ alone (S1) populates order-parameter channel but does not close OP-2 without source | consistency-check |
| H3 | S3 (scalar + source) nucleates $V_{\mathrm{inc}}$ and deepens $\Gamma_{\mathrm{bulk}}$ vs S0 | **emergence-test** (restoration) |
| H4 | GAP-C (S4) moves $\bar\rho_{\min}$ independently of F2 — channel separation | consistency-check |
| H5 | Option-D boundary source passes; bulk-force path detonates | consistency-check (representation) |

---

## 6. Implementation spec (file-bound)

| Artifact | Path |
|:---|:---|
| Scalar seed + source hooks | `src/ave/core/loop_gap_harness.py`, `vacuum_engine.py` / `CoupledK4Cosserat` |
| Port helpers | `src/ave/core/scalar_grade_seed.py` (new) or extend `bulk_rarefaction_sector.py` |
| Battery CLI | `loop_gap_harness_genesis.py` (`--smoke-scalar` / flags) |
| Keeper tests | `src/tests/test_loop_gap_harness_scalar_grade.py` |
| Result §8 | `research/2026-06-12_loop-gap-harness-phase2_result.md` (append C′) |
| Program status | `research/2026-06-12_genesis-program-status.md` new C′ row |

**Logged fields:** `scalar_seed_on`, `v_to_omega_source_on`, `gap_c_on`, `A2_V_peak`, `gamma_bulk_min`, `v_inc_peak`, `omega_peak`, `H_drift_rel`, `cp8_topology_null`, OP-2 bin, SCALAR bin.

---

## 7. Out of scope

- Full biquaternion $\mathbb{H}\otimes\mathbb{C}$ per-node algebra (Phase H)
- D1 snap state machine + latent tally
- LOOP GAP / P11 remanence (rank 4)
- Compton ring-up sweep (rank 2 — Phase F, after C′)
- Rational `a_lock` full sweep (Phase D-full)
- Partner vent / pair production OP-0
- Promoting S1 $V>0$ alone as OP-2 LANDED (circular — seed supplies $V$)

---

## 8. Downstream gates

| Phase | Gate |
|:---|:---|
| **D-full** | C′ `SCALAR-LANDED` or `SCALAR-PARTIAL` with F2 ablation doc |
| **E** (±$\mathbf{k}$) | Parallel if seed module isolated |
| **F** (Compton) | After D-full or honest ENGINE-GAP on restored engine |
| **H** (full quaternion) | Only if C′ PARTIAL — representation upgrade |

---

## 9. Corpus anchors

| Leaf | Role |
|:---|:---|
| `the-abandoned-interior.md` | Two deletions, one restoration |
| `historical-precedents.md` | Quaternion / null-cone framing |
| `maxwell-quaternion-longitudinal-context.md` | Scalar re-engages at saturation |
| `loop-gap-electron-resonator-closure-doctrine.md` §2–§3 | OP-2 + channel routing |
| `research/2026-06-09_genesis-24-saturated-seed_prereg_FROZEN.md` | Lane-1 seed + arms |
| `research/2026-06-09_tracereversal-pump-derivation_result.md` | Option-D boundary form |
| `research/2026-06-09_reactive-entrainment-source_result.md` | Conserved spin / no pump |
| `research/2026-06-06_biquaternion-node-algebra-result.md` | Scalar grade forced by product |
| `research/2026-06-12_loop-gap-harness-phase2_result.md` | 2b baseline |

---

## 10. Skills (mandatory)

`ave-prereg` · `substrate-native-check` · `consistency-vs-emergence` · `phase-space-coordinate-check` · `ave-regime-phase-state-check` · `ave-conserved-vs-pumped` · `ave-driver-script-honesty` · `ave-multi-falsifier-triangulation-discipline` · `ave-dimensional-provenance-check`

---

## 11. Grant ratification checklist

- [x] C′ before D-full — restoration-first order accepted
- [x] Minimal scope: standing $V$ + Option-D source + optional GAP-C ablation (not full quaternion)
- [x] `$V_{\mathrm{inc}}$` = K4 transverse nucleation read; standing $V$ = scalar grade (§0.3)
- [x] No CW pump arms in primary battery (F4 control only)
- [x] `frac` sweep tied to $A_{\mathrm{yield}}$ rational multiples
- [x] Freeze → `_FROZEN` (2026-06-13) — **primary implementor** after D-lite
