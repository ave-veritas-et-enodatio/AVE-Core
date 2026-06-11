# Genesis v9 — Phase-2 Pre-Registration (DRAFT — PROPOSED FREEZE 2026-06-12)

> **STATUS: DRAFT — returned for Grant freeze.** Supersedes the P5/P6 stubs in
> `research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md` (Phase-2 scope only).
>
> **Arms from (must be on `main` or merged PR before implementor runs):**
> - Phase-1 FROZEN + P1–P4 PASS (`chiral_lattice_vector.py`, PR #201)
> - R3 decoration discriminator result (D1 partial bin D1-A)
> - CVR framing bins (`research/2026-06-11_chiral-vacuum-reactor-framing.md` §1.3)
> - A1–A4 amendments (ratified at Phase-1 freeze)
>
> **NOT at freeze:** §0 D1 framing (A) substrate vs (B) decoration — adjudication memo
> after Phase-2 bins land (`_orchestration/2026-06-11_lattice-d1-test-gated.md`).

---

## Corpus-grep (ave-prereg Step 1 — 2026-06-12)

**Target:** Does the **bare srs lattice net** host a `(2,3)` standing mode (P5) and
**genesis-by-linear-precursor** under **Op14 saturation** (P6), without injected
`κ_chiral`?

**Prior work found (do not reinvent):**

| Corpus item | Relevance | Phase-2 relation |
|---|---|---|
| `unified_genesis_engine.py` (v5–v8) | CP8 precursor seed + D2 trap on **cubic** bulk | **Different platform** — Phase-2 is discrete **srs net + vector-TLM** |
| `photon_propagation_saturated.py` | Op14 cusp confinement on **K4 grid** | Arms P6 saturation observable discipline; not srs geometry |
| `r10_v8_t_st*.py` | Circular-pol photon self-trap on K4 | **Confounds P6** (A1 forbids CP seed); historical, not v9 |
| `chiral_lattice_vector.py` | Vector-TLM P1–P4 PASS | **Platform base** — extend with Op14 + drive |
| Genesis v6–v9 session record | **No mass retention without lock** | LOOP GAP context; P6 tests precursor trap, not lock |
| `genesis-v9-chiral-lattice_design.md` §CP Op14 | Saturation OFF in Phase-0 | **Op14 ON is new in Phase-2** |
| `two-engine-architecture-a027.md` | K4-TLM has $Z(V)$, lacks full $c_{\text{eff}}(V)$ | **Engine-class ceiling** on P6 BIN-D reading |
| `lattice-impedance-decomposition.md` §3 | Axiom 4 → Op14 $Z_{\text{eff}}$ + **Op3** bond $\Gamma$ | **Canonical discrete trap path** |
| `2026-06-09_substrate-temporal-values-definition.md` | $c_{\text{EM}}$ vs $c_{\text{shear}}$ split | Photon precursor = EM/impedance trap, not shear bond-delay |
| `chiral_lattice.py` `scatter_matrix` | Uniform $z_{\text{local}}$ **cancels** on shunt junction | Op14 on scatter alone is **inert** at srs degree-3 |

**Genuinely open:** First Op14 + Op3 + genesis run on **trivalent srs** with geometry-only
chirality (writhe-driven rotation channel, `κ_chiral = 0`).

---

## Physical picture (ave-prereg Step 1.5)

- **Substrate:** periodic srs net (z=3), scatter+connect vector-TLM on ports.
- **P5 (hosting):** Plant a **finished** `(2,3)` phase-space standing ansatz on the
  net; ask whether the lattice **carries** it (energy bounded, charge stable). This is
  **consistency-class hosting**, NOT genesis (substrate-native-check CP8).
- **P6 (genesis):** Launch a **linear-polarized transverse packet** (zero injected
  helicity) along a screw direction with **Op14 accessible** (`A² → √(2α)` cusp
  reachable). Ask whether **spatial $Z_{\text{eff}}$ gradients** (Op14) plus **bond
  impedance mismatch** (Op3) **self-trap** a localized state whose chirality tracks
  **enantiomorph × launch-direction** (geometry rotation from Phase-1, separate channel).
- **Γ boundary:** At high $A^2$, $S \to 0$, $Z_{\text{eff}} \to \infty$, $\Gamma \to -1$
  TIR — reactive (no dissipation), per Axiom 4 + `photon-identification.md`. The trap
  discriminator is **impedance / reflection**, not an injected `κ_chiral` knob.
- **Engine-class honesty (A-027):** This Phase-2 integrator is **discrete srs TLM +
  Op14/Op3**. It does **not** implement Master-Equation FDTD $c_{\text{eff}}(V)$
  bound-state physics. BIN-D with Op14 engaged is consistent with an **engine-class
  gap** as well as a substrate miss — report which observables fired.
- **LOOP GAP:** Op14 is reactive; genesis v6–v9 found **no mass retention without
  lock**. BIN-T / SET-ACHIRAL remain physically plausible even with saturation working.
- **Controls:** enantiomorph pair, diamond null, `κ_chiral = 0`, reversed direction
  (A2 four-cell grid).

---

## Hypotheses

**H3 (P5 — hosting):** The bare srs net supports a **stable closed-system eigenmode**
when a `(2,3)` ansatz is planted — topological charge conserved, energy bounded over
≥500 steps. *Does not imply genesis.*

**H4 (P6 — genesis):** A **linear** transverse precursor self-traps under Op14 ON,
producing a **CVR-SET** outcome (formed + set + geometry-handed) on srs, null on
diamond, absent under `κ_chiral` injection if geometry is doing the work.

---

## Platform specification (implementor MUST document)

Extend `chiral_lattice_vector.py` (or sibling module) with:

### Op14 + Op3 — **FROZEN implementation choice (2026-06-12 KB adjudication)**

**Primary coupling (AVE-native per `k4_tlm.py` + `lattice-impedance-decomposition.md` §3):**

1. **Op14 amplitude → local impedance** (per node, each step):
   - `A_node = |V|_rms / V_SNAP` (vector energy over ports+components; `V_SNAP` tagged
     apparatus-floor, same three-regime convention as `k4_tlm._update_z_local_field`).
   - `S = √(max(0, 1 − A_node²))` (Axiom 4 / Op2 kernel).
   - `z_local = 1/√S = (1 − A²)^(−1/4)` in natural units (canonical Op14; matches engine).

2. **Scatter step — unchanged shunt form at srs degree-3:**
   - `S_ij = 2/3 − δ_ij` **even when** `z_local ≠ 1` if all ports share uniform admittance
     (`chiral_lattice.scatter_matrix` — uniform shunt cancellation). **Do not claim
     Op14 entered via scatter retune alone** on the srs net.

3. **CONNECT step — Op3 bond reflection (load-bearing):**
   - For each directed bond $(u \to v)$: $\Gamma = (z_v - z_u)/(z_v + z_u)$,
     $T = \sqrt{1 - \Gamma^2}$ (mirror `k4_tlm._connect_all`, `op3_bond_reflection=True`).
   - Mix reflected/transmitted port amplitudes at endpoints. **Power-conserving** (unitary
     bond map). This is how spatial $Z_{\text{eff}}$ gradients produce trap physics on
     discrete TLM.

4. **Optional:** memristive Op14 (`S(t)` lags `S_eq` via `τ_relax`) — tag if used;
   default instantaneous Op14 for Phase-2 v1.

5. **Diagnostics (required every run):** `max(A²)`, fraction with `A² ≥ √(2α)`, spatial
   `std(z_local)`, peak $|\Gamma|$ on bonds, and whether trap sites show $\Gamma \to -1$.

**Explicitly NOT primary (deprioritized at freeze):**

- **Bond-delay / local-clock on CONNECT** as $\propto \sqrt{1-A^2}$ — not canonical in
  `k4_tlm`; conflates EM-phase speed ($c_{\text{EM}}$) with matter clock ($c_{\text{shear}}
  \propto (1-A^2)^{1/4}$ per `2026-06-09_substrate-temporal-values-definition.md`).
- **Scatter-step rotation tied to $A^2$** — that is Phase-1 geometry chirality, not Op14.

**Temporal-values discipline:** P6 precursor is **transverse EM-class**; trap observables
are impedance / $\Gamma$ / TIR / localization. Do **not** headline shear-clock slowdown
$(1-A^2)^{1/4}$ as the P6 mechanism (matter-clock sector). Report it as diagnostic only.

### Other platform rules

- **P6 drive chain (A3 audit):** No `κ_chiral`, no CP injection, no parity-odd numerical
  seed, no handed boundary forcing. External drive = **linear packet launch only** (+ taper
  to zero for drive-off / P6-D).

- **Topological charge proxy (discrete):** Window-weighted mean `ring_writhe` in the
  trapped region (or implementor-documented Op10 crossing count if Cosserat sector is
  coupled in Phase-2b). **Same proxy** for P5 and P6.

---

## Pre-registered predictions — PROPOSED FREEZE

### P5 — soliton hosting (consistency-class, NOT genesis)

A **planted** `(2,3)` standing ansatz on srs-right:

| Criterion | Threshold | Falsifier |
|---|---|---|
| **P5-E** Energy bounded | `E(t)/E(0) ∈ [0.5, 1.5]` over all steps | Monotonic blow-up or decay to `<1%` |
| **P5-Q** Charge conserved | `\|Q(t) − Q(0)\|/|Q(0)| ≤ 5%` | Charge drifts or sign-flips |
| **P5-T** Persistence | **≥ 500** scatter steps, closed system | Unbinds / disperses |
| **P5-G** Grid | `L ≥ 8` srs cells/side (document `n_nodes`) | — |

**Seed discipline:** Implementor documents the `(2,3)` phase-space ansatz construction
in the result doc (toroidal/poloidal winding on transverse components along screw orbit).
**Auto-VOID** if seed certificate shows pre-planted nonzero ω / Beltrami helicity inconsistent
with a pure V-mode ansatz (CP8 inverse — P5 is *allowed* to plant composite; certificate
tags it as HOSTING not GENESIS).

*Checkpoint-8 binding:* P5-pass alone ≠ genesis. Must pair with P6 for CVR-SET claim.

---

### P6 — genesis-by-precursor (emergence-class, PRIMARY)

Launch via `launch_linear_packet` (A1) on **srs-R, srs-L, diamond** × **{+z, −z}** (A2).

| Criterion | Threshold | Falsifier |
|---|---|---|
| **P6-A** Amplitude sweep | `{0.25, 0.5, 1.0} × E_ref`; `E_ref` = energy of unit default launch | — |
| **P6-S** Steps | **≥ 800** post-launch; plateau judged on last **100** steps | — |
| **P6-L** Localization (CVR formed leg) | RMS radius `r_rms` change **< 5%** over last 100 steps at **any** sub-rupture amp | BIN-D |
| **P6-C** Chirality (CVR formed leg) | Trapped-region `sign(Δθ_pol)` tracks `sign(writhe × direction)`; diamond **≤ 5%** of srs; survives `κ_chiral = 0` | SET-ACHIRAL |
| **P6-D** Drive-off (CVR set leg) | After drive taper to 0 at `t = N_drive` (**N_drive = 400**), persistence **≥ 200** steps with `E_loc ≥ 50%` peak and `r_rms` not doubling | BIN-T |
| **P6-G** Grid | `L ≥ 10` srs (document memory); CI smoke may use `L = 8` tagged **SMOKE-ONLY** | — |

**Outcome bins (frozen):**

| Bin | Label | Assignment rule |
|---|---|---|
| **BIN-G** | **CVR-SET** | P6-L + P6-C + P6-D all pass on srs (any amp in sweep) |
| **BIN-T** | **TRANSIENT** | P6-L pass then fails P6-D |
| **BIN-D** | **DISPERSES** | P6-L fail at all three amps |
| **SET-ACHIRAL** | **SET-ACHIRAL** | P6-D pass but P6-C fail (persists but not geometry-handed) |

**Matched baseline (CP8):** Same `E_ref` and envelope statistics on **diamond** and on
**srs with Op14 OFF** — localization on srs with Op14 ON must exceed both by **≥ 2×**
(energy retention ratio) to count as structure-driven, not amplitude artifact.

**Honest combinations (Rule 11):**

| Outcome | Report as |
|---|---|
| P5-pass + BIN-D | Hosting OK, **no genesis** |
| P5-pass + SET-ACHIRAL | Persistent but **not chiral genesis** |
| P5-fail + BIN-D | Structural hit on srs substrate (H3) |
| BIN-G on diamond | **VOID** — investigate achiral artifact |

---

## Controls (inherit Phase-1 + Phase-2)

| Control | Applies to |
|---|---|
| srs-R / srs-L enantiomorph pair | P5, P6 |
| Diamond achiral | P6 (P5 optional on diamond — record, not gate) |
| `κ_chiral = 0` ablation | P6-C |
| Reversed launch direction (A2) | P6-C four-cell |
| Op14 OFF ablation | P6 matched baseline |
| Op3 OFF ablation (CONNECT permutation only) | P6 — isolates bond-reflection trap channel |
| Matched-distribution baseline (CP8) | P6 |

---

## Op14 / driver discipline

- **Op14 canonical:** $S(A)=\sqrt{1-A^2}$, $z_{\text{local}}=1/\sqrt{S}$; trap via **Op3**
  at bonds when $z_{\text{local}}$ varies spatially (KB `op14-local-clock-modulation.md`
  matter-clock exponent $(1-A^2)^{1/4}$ is **shear-sector** — stale $\sqrt{1-A^2}$ rows
  flagged; do not use stale form as P6 headline).
- **A-027 tag:** Result doc must state engine class = **discrete srs TLM + Op14/Op3**;
  BIN-D does not auto-imply srs substrate failure without Op3-ablation comparison.
- No single global σ eigsolve (spatially-varying $A^2$ invalidates uniform-σ modes per
  `op14-local-clock-modulation.md` §3).
- PML / interior mask: density and `r_rms` use `net.interior_mask` only.
- Phase-space coordinate (A46): `(2,3)` = phase-space winding on `(V_⊥1, V_⊥2)`, not
  real-space Cartesian φ².
- **ave-driver-script-honesty:** Report measured bins; no fit-as-prediction on `Δθ` or
  `r_rms`.

---

## Kill conditions (Rule 11)

- P6-C fail at all four cells with P6-L pass ⇒ **SET-ACHIRAL** ladder; do not promote
  to genesis.
- BIN-D at all amps on both enantiomorphs ⇒ H4 falsified for framing (A) **if Op3-ablation
  shows Op3 was load-bearing**; if BIN-D with Op14+Op3 but Op3-OFF also disperses, tag
  **A-027 engine-class gap** and defer substrate adjudication to D1 memo + optional
  Master-Equation follow-on. Do not rescue toward injected κ.
- P5-fail + BIN-D ⇒ srs may not host electron ansatz — structural hit; triggers D1 memo
  input but does not auto-pick (B).

---

## What Grant decides at freeze

1. Ratify or amend thresholds above (P5/P6 tables, `L`, `N_steps`, `N_drive`).
2. **Op14 implementation — PROPOSED RATIFIED:** Op14 $z_{\text{local}}(A^2)$ + **Op3 at
   CONNECT** (not bond-delay clock; not scatter retune on uniform shunt). Amend only if
   Grant overrides KB adjudication 2026-06-12.
3. Approve topological-charge proxy (ring writhe window vs Op10 crossing if Phase-2b).
4. Approve optional memristive Op14 (`τ_relax`) as Phase-2b extension vs instantaneous v1.
5. **NOT at freeze:** D1 framing (A)/(B).

---

## Implementor deliverables (post-freeze)

| Artifact | Path (proposed) |
|---|---|
| Op14 vector-TLM extension | `src/ave/core/chiral_lattice_vector_sat.py` (or extend existing) |
| P5 seed + persistence | `src/ave/core/chiral_lattice_soliton_host.py` |
| P6 precursor genesis | `src/ave/core/chiral_lattice_genesis.py` |
| Keeper tests | `src/tests/test_chiral_lattice_phase2_p5.py`, `..._p6.py` |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_phase2_genesis.py` |
| Result doc | `research/2026-06-12_genesis-v9-phase2_result.md` |

**Branch:** `analysis/2026-06-12-genesis-v9-phase2-implementor` (off `main` after PR #201 merge).

---

## Cross-refs

- Phase-1 FROZEN: `research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md`
- Design: `research/2026-06-11_genesis-v9-chiral-lattice_design.md`
- CVR bins: `research/2026-06-11_chiral-vacuum-reactor-framing.md` §1.3
- Epic: `_orchestration/2026-06-11_lattice-d1-test-gated.md`
- D1 partial: `research/2026-06-11_lattice-decoration-discriminator_result.md`
- Two-engine: `manuscript/ave-kb/common/two-engine-architecture-a027.md`
- Op14 clock: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md`
- Impedance map: `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`
- Temporal split: `research/2026-06-09_substrate-temporal-values-definition.md`
- Engine ref: `src/ave/core/k4_tlm.py` (`_update_z_local_field`, `op3_bond_reflection`)
