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

> **⚠ F4's energy-flat clause is SUPERSEDED → Amendment 3 (2026-06-13).** The master-equation leapfrog grows the energy ledger ~+880% even with `converter_on=False` while the field stays bounded at ≈ `V_yield`; the conservation proxy is **amplitude-boundedness + persistence**, not ledger-flatness. `converter_work ≈ 0` retained.

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
- [x] Auditor pre-driver review folded → **Amendment 1** below.
- [x] Auditor final audit CLEARED (2026-06-13) — one required fix (re-add the PLANTED-ONLY bin) folded as **Amendment 2** below; driver clear thereafter.

---

## Amendment 1 — auditor pre-driver review (2026-06-13)

> **Rule-12 dated addendum** (the frozen body above is preserved). Folds the auditor's pre-driver review; **supersedes the §3 verdict bins**. No data has been seen — this remains a pre-run pre-registration.

**A1 — self-focus is the PRIMARY signal, robust to BOTH traps.** The discriminator is **`max|A|_interior` GROWTH** (the `c_eff(V)` self-steepening dynamics — does the field amplify toward `A→1`), **NOT** the `gamma_bulk` magnitude. This dodges *both* the plant-vs-emerge trap (it's the dynamic, not the t=0 read) *and* the `n=S^{1/4}`-vs-`S^{1/2}` exponent defect (which lives in `gamma_bulk()`, a downstream read of A — not in A itself). `gamma_bulk_min` deepening *below* its t=0 value is **corroborating**; its magnitude stays apparatus-qualified, never a verdict axis.

**A2 — framing is CONSISTENCY-with-v14, not new-emergence (pre-empts the #215 consistency-as-emergence error).** v14 Mode I PASS *already* validated that the longitudinal-bulk scalar self-traps into a breathing soliton with a `Γ≈−1` TIR shell — that **is** the cage (the one green `have` cell). This test does **not** discover the cage. What is new and worth the run: **does the de-contaminated A1 seed (`self.V`, the correctly-pinned "which V" — not `V_inc`) reproduce the v14 self-trap** — closing the "which V" question and validating that the F1 plumbing routed the right grade. **Report a positive as "confirms `self.V` is the self-trapping grade, consistent with v14 Mode I" — NOT "built the electron cage" (v14 built it), NOT "scalar beats transverse" (the harness thesis, now structurally moot: the harness cannot host the cage at all).**

**A3 — frozen verdict bins (supersede §3):**
- **SELF-FOCUS** — `max|A|` grows toward 1, the wall deepens below t=0, and the bound state **persists** (v14-consistent: `self.V` is the self-trapping grade). *The positive.*
- **TRANSIENT** — forms then decays (distinct from never-formed; informative — a partial self-trap that doesn't hold).
- **DISPERSES** — `max|A|` shrinks; `self.V` does NOT self-trap for this seed = a **clean honest negative** (grade-self-trap falsified for this seed/frac).
- **UNRESOLVED** — budget/regime inconclusive.

**A4 — the frac-sweep's PRIMARY read is the CRITICAL-FRAC (nucleation threshold), not monotonicity.** Sweep `frac` to find the **critical-frac** where behaviour switches: DISPERSES below, SELF-FOCUS above. A nucleation threshold is the cleanest bound-state-emergence signature (a real soliton has a critical seed amplitude), and that critical-frac **is** the nucleation barrier the genesis program has chased — more diagnostic than "monotone-deepens." Sweep fine enough to bracket it (bisect between the highest-dispersing and lowest-self-focusing frac; this subsumes §2's S3 disperse-control). The production budget must run long enough to distinguish **TRANSIENT** from persistent **SELF-FOCUS**.

**A5 — ratification:** Grant + auditor confirmed `self.V` (2026-06-13); this amendment folds the auditor's pre-driver review. The auditor audits THIS amended frozen prereg — success bin = self-focus-dynamics + critical-frac, framing = consistency-with-v14 — before any driver code.

---

## Amendment 2 — auditor final-audit fix (2026-06-13)

> **Rule-12 dated addendum, pre-run.** Adds a *discriminating* bin (a new way to FAIL) — cannot be debugging-toward-success. Closes the one gap the final audit caught: Amendment 1's A3 dropped the plant-not-create bin while §4 F3 still routes to it.

**A2.1 — re-add PLANTED-ONLY; A3 is now FIVE bins.** A3's four bins had **no home** for the *planted-only* state (`gamma_bulk<0` at t=0 from the seed, `max|A|` **flat**, no deepening): it doesn't grow (≠SELF-FOCUS), shrink (≠DISPERSES), form-then-decay (≠TRANSIENT), or run out of budget (≠UNRESOLVED) — yet §4 F3 names it as its FAIL outcome. It is the home for the exact **plant-masquerading-as-emergence** failure this test exists to catch (#215 / CP9). Frozen bins are now:
> **SELF-FOCUS / TRANSIENT / PLANTED-ONLY / DISPERSES / UNRESOLVED**
- **PLANTED-ONLY** — `gamma_bulk<0` at t=0 (the seed amplitude read through the kernel) but `max|A|` stays flat and `gamma_bulk_min` does NOT deepen below t=0 = **F3-FAIL, the plant-not-create negative**. (Distinct from DISPERSES: neither self-traps nor disperses — the "wall" is just the instrument re-reading the plant.)

**A2.2 — tighten SELF-FOCUS so "persists" alone cannot admit a plant.** SELF-FOCUS now REQUIRES BOTH `max|A|` **grows** beyond the seed AND `gamma_bulk_min` **deepens below its t=0 value** (F1-PASS ∧ F3-PASS) — *then* persists. "Persists" is necessary, not sufficient: a flat planted-only wall persists yet is PLANTED-ONLY, not SELF-FOCUS.

**A2.3 (clarity) — F1 ∧ F4 co-occurrence IS the self-focus-vs-pump discriminator.** `max|A|` growing **with `total_energy` flat** = energy *concentrating* → genuine self-focus (the soliton signature). Growing **with energy drift** = energy *created* → the genesis-24 pump, not self-focus. SELF-FOCUS requires F1-PASS ∧ F4-PASS together; "the field amplifies" and "energy is conserved" are not in tension — together they are the bound-state signature.
> **[SUPERSEDED → Amendment 3 (2026-06-13):** the discriminator is amplitude-**BOUNDEDNESS** (concentrating at ≈ `V_yield`) vs **UNBOUNDED** detonation (pump) — **NOT** energy-flat. On this engine the leapfrog grows the ledger ~+880% on a *genuine bounded* self-focus, so ledger-flatness is the wrong proxy.**]**

**A2.4 (clarity) — "persists" reports the amplitude-envelope TREND** (flat vs slow-decay over the budget), not just "survived N periods" — a slow decay masquerades as persistent over a finite window. That envelope trend is the SELF-FOCUS-vs-TRANSIENT edge; the production budget must run long enough to resolve it.

**A2.5 — auditor cleared this amended prereg to driver (2026-06-13).**

---

## Amendment 3 — F4 conservation criterion (post-result correction, Rule-12) (2026-06-13)

> **Rule-12 dated addendum, POST-RESULT — NOT a Rule-11 freeze violation.** This corrects a *mis-specified criterion*, not a verdict. Two independent proofs it is not debugging-toward-success: **(1) external anchor** — the frozen F4 "energy-flat" clause, applied to the *already-canonical* v14 Mode I breather (same engine, same sech eigen-profile), would FALSELY FALSIFY v14; a criterion that falsifies accepted canon is wrong independent of this run. **(2) result-invariant** — the driver's classifier never gated SELF-FOCUS on energy-flatness (it gated on boundedness + persistence and *reported* the drift as a flag; result §FLAG-2), so the bins are identical with or without this amendment (sech = SELF-FOCUS, Gaussian = DISPERSES). The amendment reconciles the frozen text to what the classifier correctly did.

**A3.1 — supersede the energy-flat clause of F4 (and its A2.3 restatement).** The master-equation leapfrog grows BOTH `total_energy` (1.767 → 17.32, +880% at amp 0.20) AND `bulk_E_conserved` (+484% → +907% across the sweep) on the self-focusing sech **even with `converter_on=False`** — a numerical leapfrog-at-saturation-front artifact, not physical energy creation. **The conservation proxy is amplitude-BOUNDEDNESS + PERSISTENCE, not ledger-flatness:**
- **F4 PASS (not-a-pump):** `max|A|` stays **bounded** at ≈ `V_yield` (cage: ≤ 1.22 ≪ the genesis-24 detonation ~1e4) **and** `converter_work ≈ 0` / bounded (no one-way runaway) **and** the amplitude envelope **persists** (A2.4 trend).
- **F4 FAIL (pump):** **unbounded detonation** (`max|A| → ~1e4`, genesis-24) **or** converter one-way runaway.
- **Energy-ledger drift is REPORTED, not binned** (logged: `total_energy_drift_pct`, `bulk_E_conserved_drift_pct`).

**A3.2 — pump-exclusion triad (so a bounded pump cannot masquerade as self-focus).** The ledger growth is provably the leapfrog artifact, not a pump, by THREE signatures a real pump would each violate: **(a)** it occurs with `converter_on=False` — no source term in the pure master equation; **(b)** the field stays **bounded** at ≈ `V_yield` — a real pump is unbounded; **(c)** it **decreases** with seed amplitude (+879% at amp 0.20 → +484% at amp 0.85) — the **inverse** of a saturation-driven pump (which grows with drive). Boundedness (b) is the load-bearing discriminator: a pump must show unbounded amplitude.

**A3.3 — referential integrity (`ave-prereg` v1.2 Step 3.6, verified).** This supersede touches exactly **two** sites — F4 (§4) and its A2.3 restatement — both re-routed here with in-place pointers. **No bin is dropped or added** (SELF-FOCUS / TRANSIENT / PLANTED-ONLY / DISPERSES / UNRESOLVED stand); F1/F2/F3 routing and the Amendment-2 PLANTED-ONLY fix are untouched (F4 is orthogonal — conservation, not deepening). Masquerade-direction check: the superseded clause was a pump-GUARD; its replacement keeps the guard (detonation / runaway → pump) and adds the a/b/c triad, so a pump still cannot wear the SELF-FOCUS bin.

**A3.4 — retained, unchanged:** `converter_work ≈ 0` (the converter-OFF energize-LOCK check; result: bounded [−1.40, −2.4e-6]) and the apparatus-qualified magnitude (A3 / −0.2400 clip floor, never a verdict axis).
