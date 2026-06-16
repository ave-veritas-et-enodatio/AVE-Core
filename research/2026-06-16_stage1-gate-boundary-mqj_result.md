# Stage-1 GATE result — boundary-MQJ self-trap integrator + Z-at-wall

**Date:** 2026-06-16
**Stage:** Stage-1 GATE (boundary-MQJ self-trap integrator + Z-at-wall discriminator)
**Branch:** `analysis/2026-06-16-boundary-mqj-selftrap-integrator-zwall`
**Source data:** [`src/scripts/vol_1_foundations/boundary_mqj_selftrap_zwall_gate_results.json`](../src/scripts/vol_1_foundations/boundary_mqj_selftrap_zwall_gate_results.json) (this branch)
**Adjudication:** verify panel `wvvx6y6zb`; tracker Phase 9
**Doc class:** thin gate-result MD (Q2 — gate-class steps get a standalone result so the corpus carries the verdict + corrections, not just the tracker).

---

## VERDICT

**GATE_VERDICT = `c_eff(V)-STRUCTURAL-GAP` — NOT echo (panel-verified).**

- **Bucket-1 (numerical adequacy) CLEARED.** The standalone known-positive cage held
  (`step1_known_positive.instrument_adequate = true`). The MasterEquationFDTD v14 cage —
  the engine that actually carries `c_eff(V)` — produces the stiffening-confinement signature
  ($Z_{\text{long}}/Z_0 = \sqrt{S} \to 0$ at core). Any coupled-engine reading is therefore
  **not a numerical artifact**: bucket-1 is cleared by construction of the gate.

- **Bucket-2 (the coupled run) = `c_eff(V)-STRUCTURAL-GAP`, NOT echo.**
  The coupled `VacuumEngine3D` $\Gamma=-1$ wall forms, but **Z does not collapse to 0**.
  What the wall reads is the **TRANSVERSE Meissner impedance**
  $Z_{\text{eff}} = \sqrt{S_\mu/S_\varepsilon} \approx 1.003\,Z_0$
  (`Z_wall_post_median = 1.003109686793587`; floor `0.8468217735138248`).
  The electron-confinement object is the **orthogonal LONGITUDINAL A1 tank**
  $Z_{\text{tank}} = \sqrt{L/C_{\text{comp}}} \to 0$ — and **this engine has no independent
  field for it.** Per `INVARIANT-S2 Q1 = (B)` and `engine-capability-map.md` (`:45`/`:79`),
  `VacuumEngine3D` is **softening-only**: its scalar is the projection
  `v_scalar_from_v_inc(V_inc)` (def `cross_sector_coupling.py:226`, used at
  `k4_cosserat_coupling.py:499`), not an independent A1 degree of freedom. So
  $Z \approx Z_0$ is the **PREDICTED no-A1-field reading** — exactly what an engine with
  no stiffening cage must report. It is **not** a no-trap result, and therefore **not an echo**.

  This bin is **resolution-stable**: the coupled apparatus-floor sweep
  (`apparatus_floor_sweep`, cfl 0.25 → 0.125, n_sub 127 → 253) returns
  `c_eff(V)-STRUCTURAL-GAP` at both resolutions (`bin_resolution_stable = true`,
  `Z_wall_resolution_stable = true`). The PUMP control bins separately as `PUMPS`
  (full-Hamiltonian ledger ramp = 163.18 ≫ 2.0), confirming the discriminator separates
  passive-confinement from energy-injection.

**Plumber reading:** the wall is a *transverse Meissner skin* (~$Z_0$), not a *longitudinal
voltage-node short* (→0). The coupled engine has the transverse channel but is **missing the
load-bearing scalar reactance** — the gap is structural (a missing field), not a falsification
of the trap and not a calibration echo. A true confinement test needs a coupled engine with an
**independent c_eff(V) / A1 field** (a bounded build) — the missing physics named in
`engine-capability-map.md` §6.

---

## THE 4 CORRECTIONS (panel `wvvx6y6zb` — carried durably HERE)

Panel `wvvx6y6zb` flagged four points where the committed/headline numbers do not say what
they appear to say. These ride **here** so the corpus carries them, not just the tracker.

1. **Headline geometry is `N=18` "fast artifact", NOT the `N=24` driver default.**
   The committed JSON headline run is `geometry.N = 18` (`note: "N=18 fast artifact; PUMP control
   lightened ..."`). The `N=24` is the *known-positive bucket-1* configuration
   (`step1_known_positive.base.N = 24`), not the coupled headline grid. Do not read the
   headline LOCK/PUMP numbers as N=24-converged.

2. **Long-window cos persistence is `11.9P` (panel full-window re-run), NOT the committed `3.94P`.**
   The committed JSON has `cos_confined_persist_periods = 3.938883883187337` — this is a
   **truncated-window artifact**. The panel's full-recording-window re-run gives **11.9 periods**.
   The committed `3.94P` understates persistence; the durable figure is **11.9P**.

3. **The `S_μ = 0.915 / S_ε = 0.830` micro-numbers are auditor-illustrative, NOT in the committed JSON.**
   These specific saturation values do **not** appear anywhere in
   `boundary_mqj_selftrap_zwall_gate_results.json` (verified absent). They are an
   auditor-supplied illustration of the $Z_{\text{eff}} = \sqrt{S_\mu/S_\varepsilon}$ mechanism,
   not committed measurements. Do not cite them as engine output. (The committed engine
   output is `Z_wall_post_median ≈ 1.003`; the $\sqrt{S_\mu/S_\varepsilon}$ form is the
   *interpretation* of why it sits at ~$Z_0$.)

4. **The standalone known-positive `Z_long = 0.376` is the `A_cap = 0.99` numerical CLAMP floor,
   NOT an asymptotic `Z → 0`.**
   `step1_known_positive.Z_long_core_min = 0.37558934995105875`. The *direction* is genuine
   (stiffening drives $Z_{\text{long}}$ down), but the *magnitude* is **clip-set** by the
   `A_cap = 0.99` numerical clamp: $\sqrt{1 - 0.99^2} = 0.141$. The cage approaches the clamp
   floor, not a physical asymptotic $Z \to 0$. Read 0.376/0.141 as "clamp-limited downward",
   not "measured asymptote".

---

## CROSS-REFERENCE

The **same** `c_eff(V)-STRUCTURAL-GAP` verdict is also filed — under the INVARIANT-S2 lane
filename — in
[`research/2026-06-15_ceff-epsilon-monotonicity_result.md`](2026-06-15_ceff-epsilon-monotonicity_result.md).
That doc carries the `INVARIANT-S2 Q1 = (B)` resolution (longitudinal/A1/mass reactance
$C_{\text{comp}} = C_0/S$ is **orthogonal** to the transverse/T2/charge reactance
$\varepsilon_{\text{eff}} = \varepsilon_0 S$ — the same-wall coincidence is not a same-object
identity) that **grounds** why $Z \approx Z_0$ here is the no-A1-field reading rather than a no-trap.

This note exists so a `stage1` / `boundary-mqj` grep resolves to the gate verdict even though the
underlying physics lives under the monotonicity filename. **Same verdict, two filenames** —
both point at the structural gap: the coupled engine lacks an independent c_eff(V)/A1 field.

**Engine-capability provenance:** `manuscript/ave-kb/common/engine-capability-map.md` (`:45`/`:79`)
— `VacuumEngine3D / loop_gap_harness` is softening-only; its scalar is the
`v_scalar_from_v_inc` projection with no independent A1 field, so it structurally cannot host
the stiffening cage.
