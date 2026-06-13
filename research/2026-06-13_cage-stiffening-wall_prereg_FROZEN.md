# Cage stiffening-wall self-focus test (A1 dilatation) — pre-registration (FROZEN 2026-06-13)

> **STATUS: FROZEN** — Grant + auditor ratified 2026-06-13. Tests whether the standing **A1-dilatation scalar V** (the master-equation field) self-focuses into the `c_eff→∞` stiffening cage on the longitudinal-bulk engine — where the C′ harness run structurally could not (its scalar was a `v_scalar_from_v_inc` projection; no independent A1 channel).
> **Engine:** `src/ave/core/crystal_engine.py` (bulk branch = the v14-Mode-I-validated `master_equation_fdtd.py`). **DRIVER job on the existing validated engine — NOT a new build** (`ave-loop-gap-harness-discipline` v1.1: stiffening-cage branch → master-eq/crystal_engine).
> **Lane:** implementor (`analysis/2026-06-13-cage-stiffening-wall` off `main`).
> **Lineage:** `manuscript/ave-kb/common/engine-capability-map.md` (the cage = stiffening A1 wall, firewalled from softening ρ̄; the harness cannot host it) · `research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md` (the C′ thesis, ran SCALAR-PARTIAL on the wrong engine) · `two-engine-architecture-a027.md` (master-eq = bound-state engine, v14 Mode I PASS).

---

## 0. Derivation target (one sentence)

On the longitudinal-bulk engine, does a **standing, sub-saturation A1-dilatation scalar V** (`∂_tV=0` at t=0), driven by its **own** `c_eff(V)=c0·(1−A²)^(−1/4)→∞` saturation, **self-focus** into the `Γ→−1` stiffening wall (the electron mass-cage) — with the wall **deepening dynamically BEYOND the seeded amplitude** (self-create, not the seed's amplitude re-read) — where the C′ harness run could not?

---

## 0.1 Which V — PINNED (load-bearing; the noun the whole arc kept slipping)

**V := the master-equation longitudinal-bulk scalar field** = `crystal_engine.self.V` ([`crystal_engine.py:104`](../src/ave/core/crystal_engine.py)) = `master_equation_fdtd.self.V`. The **A1 dilatation**, **the MASS "3"** (NO-QED directive, `crystal_engine.py:11-18`). It is explicitly **NONE** of:

| NOT this | Why |
|:---|:---|
| `V_inc` (K4 transverse port voltage) | the transverse **readout** — does not exist in this engine; the channel C′ wrongly seeded |
| `V_ref` / `v_scalar_from_v_inc` projection | the harness's **derived** scalar (`cross_sector_coupling.py:226`) — the C′ contamination |
| `self.w` (`crystal_engine.py:106`) | the transverse-shear **photon** (speed c_T) |
| `Ω_w=(∇×w)·x̂` (`crystal_engine.py:213`) | the Cosserat micro-rotation = the **CHARGE "3"** (winding/helicity) — a *different* "3" than the mass dilatation |
| `ρ̄` (softening rarefaction) | a *different* engine (`bulk_rarefaction_sector`); firewalled from the stiffening cage (`cavitation_flow.py:28`) |

**Normalization (engine's own, α-free natural units):** `A=|V|/V_yield`, kernel `S(A)=√(1−A²)` saturating at `A=1` (`crystal_engine.py:191-200`); `V_yield=1`, `c0=1`. The seed `frac` is the **saturation fraction A∈(0,1)** — NOT the loop-gap `√α` units.

---

## 1. Physical picture (substrate-native)

The cage is the V's **own self-saturation**: as the seed's core saturates (`A→1`), `c_eff→∞` self-creates the `Γ=−1` TIR wall — THE BULK-TRAP (`crystal_engine.py:18-20`). Rest mass = the trapped longitudinal-bulk reactive energy. The `c_eff(V)=c0/√S` nonlinearity is **self-steepening** (faster in the saturated core), so a sub-saturation seed either **self-focuses** into the saturated bound state (the v14 Mode I breathing soliton) **or disperses**. That fork is the test.

---

## 1.1 substrate-native-check (design-time)

| CP | Verdict |
|:---|:---|
| CP1 | Time-domain leapfrog wave eq `∂²V/∂t²=c_eff²∇²V` — no minimization, no pump |
| CP8 | **Seed the GENERATIVE PRECURSOR** — a *sub-saturation, bare* standing V; the wall must **EMERGE**. NOT a pre-walled/pre-saturated cage (that's plant-not-create). THE load-bearing checkpoint. |
| CP9 | **`gamma_bulk()` is ALGEBRAIC in the instantaneous A** (`crystal_engine.py:434`) — so a seeded V yields `gamma_bulk<0` *at t=0* from the seed amplitude alone. The self-create read is therefore the **DYNAMIC growth of A** (the field `step()`-evolves), i.e. `gamma_bulk_min` deepening *below* its t=0 value — NOT the t=0 read. |
| CP10 | The wall = the `Γ=−1` boundary (Smith Γ at the `c_eff→∞` surface), Op17-bounded — NOT a bulk force |

**Note (dual-wall H4 is a harness framing — not applicable here):** crystal_engine has *only* the stiffening V-wall; no softening-ρ̄ sector to disambiguate against. With no ρ̄ to confound it, `V→V_yield` tracking is unambiguous on its own; the discriminator is the self-focus-vs-disperse dynamic + the bare-seed CP8 guard. The softening ρ̄ stays the **firewalled control** (a different engine, referenced, not co-run).

---

## 2. Seed + ablation battery

**Seed:** `seed_bulk(center, sigma, frac, helical=False)` — the bare standing A1-dilatation V, `∂_tV=0` (stationary). **No** `seed_photon`, **no** pre-walling, **no** planted (2,3).

**`frac` sweep (sub-saturation, for the monotone-trend read):** `{0.30, 0.50, 0.70}` — well below `A=1`, so the t=0 wall is shallow and any deepening is dynamical.

| Arm | Config | Isolates |
|:---|:---|:---|
| **S0** | `frac=0`, no seed | baseline — no wall (F0) |
| **S1** | `seed_bulk(frac)`, `converter_on=False` | **the bare V self-trap** — does the A1 dilatation self-focus from V alone (pure master-equation), no chiral coupling? (the narrow emergence arm) |
| **S2** | `seed_bulk(frac)`, `converter_on=True` | + the ADD-2 chiral converter — does it sharpen/deepen the wall? |
| **S3** | sub-saturation seed expected to disperse (small frac / wide σ) | disperse control — the negative the self-focus must beat |

**Step budget:** `--smoke` (short, CI keeper); `--production` (≥3 breathing periods, or until `A` clearly grows/decays).

---

## 3. Self-create discriminator + success bins

**Discriminator (CP8/CP9):** does `max|A|_interior` **GROW** dynamically beyond the seeded `frac` (self-focus → deeper wall), or **SHRINK** (disperse)? Track `gamma_bulk_min` over the run: SELF-CREATE = `gamma_bulk_min` **deepens below its t=0 (seeded) value**; DISPERSE = `gamma_bulk_min → 0`.

**Success bin — `CAGE-SELF-CREATED`:**
- **SIGN** — `gamma_bulk_min < 0` (reflective short), AND
- **SELF-CREATE** — `max|A|_end > max|A|_t0` and `gamma_bulk_min_end < gamma_bulk_min_t0` (the wall deepens *beyond* the seed; the seed self-traps), AND
- **MONOTONE-DEEPENS-with-frac** — deeper `gamma_bulk_min` at higher seeded `frac` across the sweep.

**Magnitude REPORTED but APPARATUS-QUALIFIED — do NOT bin on `Γ=−1`.** The wall depth is **doubly bench-capped**: (1) graft-v2's `−0.849` sat *exactly* on the `A_cap`/`S_min` clip floor (corr 1.0, resid 0.0 across 10 cells); (2) the `n=S^{1/4}`-vs-`S^{1/2}` exponent defect *understates* depth (`crystal_engine.py:421-432` flag). A genuine cage reaching only `−0.37→−0.65` dynamically is a **PASS**, not a falsification. Report whether `gamma_bulk_min` sits on the clip floor; if so, the magnitude is bench-limited, not physics.

**Verdict bins:**
- `CAGE-SELF-CREATED` — sign + self-create + monotone (magnitude apparatus-qualified).
- `CAGE-PLANTED-ONLY` — `gamma_bulk<0` at t=0 but does NOT deepen (the seed amplitude, not self-focus). *Not* a cage.
- `DISPERSE` — `gamma_bulk_min→0`, `max|A|` shrinks. No cage.
- `APPARATUS-LIMITED` — depth pinned to the clip floor; report, do not falsify.

---

## 4. Primary falsifiers

| ID | PASS | FAIL |
|:---|:---|:---|
| **F0** baseline | `frac=0` ⇒ `gamma_bulk≈0` (no wall) | wall without a seed → harness/code artifact |
| **F1** self-focus | `max|A|_end > max|A|_t0` (S1/S2) | `max|A|` shrinks → DISPERSE |
| **F2** monotone-trend | `gamma_bulk_min` deepens monotonically with `frac` | non-monotone / flat |
| **F3** created-not-planted | `gamma_bulk_min_end < gamma_bulk_min_t0` | only the t=0 seeded read → `CAGE-PLANTED-ONLY` |
| **F4** conservation | `total_energy` flat; `converter_work ≈ 0`; `bulk_energy_conserved` flat (energize-LOCK) | secular drift / detonation → pump (genesis-24 failure) |

---

## 5. Hypotheses (`consistency-vs-emergence`)

The master-equation bulk-V self-trap is **v14-Mode-I-VALIDATED** (`two-engine-architecture-a027.md:32-37`). So this is a **regime-valid CONSISTENCY-confirmation** of the C′ scalar-grade thesis on the engine that can host the A1 channel — closing the C′ harness confounded-null — **not** a wide-open emergence frontier. New value: (a) the de-contaminated A1-V seed pinned to the master-equation field; (b) the honest self-create discriminator + apparatus-qualified magnitude; (c) the converter-OFF ablation. The genuinely-OPEN emergent frontier — **retention / R10 / the loop** (does the cage PERSIST at zero drive) — is DOWNSTREAM and out of scope.

| ID | Statement | Class |
|:---|:---|:---|
| H1 | The master-equation bulk V self-focuses into the cage (de-contaminated seed) | consistency-check (v14 re-confirmation) |
| H2 | The cage self-creates (deepens beyond the seed) with `converter_on=False` — the bare V self-trap | **emergence-test (narrow)** |
| H3 | The ADD-2 chiral converter deepens/sharpens the wall vs S1 | consistency-check |

---

## 6. Out of scope

- The **winding / (2,3) / charge "3"** (the photon→converter genesis path; Cosserat micro-rotation). This is the **MASS dilatation cage only.**
- **Retention / R10 / the loop** (zero-drive persistence) — the deeper frontier, downstream.
- The V→ω source (the inert C′ source); the harness (`VacuumEngine3D`); ρ̄ softening; GAP-C.
- Full genesis (photon→electron).

---

## 7. Implementation spec (file-bound)

| Artifact | Path |
|:---|:---|
| Driver | `src/scripts/vol_1_foundations/cage_stiffening_wall.py` (new) — `CrystalEngine` + `seed_bulk` + `gamma_bulk` + `strain_field` + `total_energy` + `converter_work` + `field_intensity` |
| Keeper test | `src/tests/test_cage_stiffening_wall.py` |
| Result | `research/2026-06-13_cage-stiffening-wall_result.md` |

**Logged fields:** `frac`, `converter_on`, `max_A_t0`, `max_A_end`, `gamma_bulk_min_t0`, `gamma_bulk_min_end`, `self_focus`(=`max_A_end>max_A_t0`), `monotone_deepens`, `total_energy_drift`, `converter_work`, `on_clip_floor`, VERDICT bin.

---

## 8. Skills (mandatory)

`ave-prereg` · `substrate-native-check` (CP8/CP9/CP10) · `ave-conserved-vs-pumped` · `phase-space-coordinate-check` · `ave-apparatus-floor-attribution` · `consistency-vs-emergence` · `ave-evidence-framing-discipline`

---

## 9. Ratification checklist

- [x] Standing-V seed; **V = the A1-dilatation master-equation scalar** (`crystal_engine.self.V`) — Grant + auditor confirmed 2026-06-13 (not `V_inc`, not `V_ref`/projection).
- [x] Self-create discriminator = the self-focus **dynamic** (`max|A|` grows beyond seed; `gamma_bulk_min` deepens below t=0) — NOT the t=0 `gamma_bulk`.
- [x] Success bin = sign + self-create + monotone-trend; **magnitude apparatus-qualified (NOT `Γ=−1`)** — auditor #1.
- [x] crystal_engine is stiffening-only here (no ρ̄ dual-wall); softening ρ̄ = firewalled control.
- [x] Fork off a clean `origin/main` worktree (auditor #3); driver-not-build; Rule-11 prereg frozen before code.
- [ ] Grant + auditor review of this frozen prereg **before** any driver code.
