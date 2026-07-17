# F1 V-active consumer audit — who consumed the wrong bond-Γ, and does it matter

**Date:** 2026-07-16 · **Class:** Consumer audit (docs-only; engine untouched by
this doc). · **Lane:** F1 implementer. · **Supersedes-scope-of:**
[`_orchestration/2026-07-15_f1-consumer-audit.md`](../_orchestration/2026-07-15_f1-consumer-audit.md)
r7–r10 NEEDS-TRIAGE bucket (this doc closes it with a mechanism, not a per-file guess). ·
**Companion:** [`2026-07-16_f1-materiality-report_NOTE.md`](2026-07-16_f1-materiality-report_NOTE.md).

## 0 · Status up front (flag-don't-fix)

**The F1 code fix is ALREADY BANKED on main** — it did not need re-implementing
in this lane. Both commits are ancestors of the audited HEAD:

- `79435ee3` *fix(f1)+feat(f6): Grant DEFECT fix for shared front* — adds
  `external_z_local` to `K4Lattice3D`, sets it `True` under `CoupledK4Cosserat`,
  and adds `src/tests/test_f1_shared_front_ordering.py`.
- `20395fe2` *fix(f1): advance S_field under external_z_local without overwriting
  shared front* — the follow-up so memristive `S_field` still evolves under the
  external-owned path (CI regression).

So the deliverable of *this* lane is **not** the fix (banked) but: (STEP 1) a
mechanism-grounded consumer audit that closes the r7–r10 survey debt, (STEP 2)
verification of the banked fix + a strengthened regression, and (STEP 3) the
materiality report (companion doc). No banked doc is edited. No banked gate is
re-run.

## 1 · Sector / regime declaration (before any standard-physics word)

- **Which sector?** The defect lives in the **K4 U(1) V-sector** ("the 3",
  `(V_inc, Φ_link)`) bond-reflection short. It does **not** touch the Cosserat
  (2,3) ω-shear sector directly.
- **Does the engine carry the DOF?** Yes — `z_local_field` is a live per-site
  field on `K4Lattice3D`; the shared front `√(S_μ/S_ε)` is written into it every
  outer step (`k4_cosserat_coupling.py:881`, `_update_z_local_total`).
- **Cold vs saturated?** The fix only changes bond Γ where the **shared front
  differs from the V-only kernel** — i.e. where the Cosserat sector is loaded
  (A²_μ via curvature, A²_ε via strain, or the helicity asymmetry). Cold-Cosserat
  ⇒ the two kernels coincide identically (§3, proven to 1e-14).
- **Phase-space vs real-space (A46):** the bond-Γ short acts on the real-space
  lattice V-pulse routing; the observable it moves is real-space V localization,
  not a phase-space quantity. No coordinate mismatch introduced.

## 2 · Mechanism (two-method verified on the audited HEAD)

**Method A — read the shipped ordering.** In `CoupledK4Cosserat.step()`:

1. `_update_z_local_total()` writes `z_local_field = √(S_μ/S_ε)` (asymmetric,
   default) — `k4_cosserat_coupling.py:881`, `:576–607`.
2. `k4.step()` → `_scatter_all()`. Under `external_z_local=True` it calls
   `_integrate_s_field_from_v()` (advances `S_field` only) and **does not**
   overwrite `z_local_field` — `k4_tlm.py:324–329`. (Pre-fix / `external_z_local=False`
   it called `_update_z_local_field()` which overwrote with the V-only
   `1/√S(V)` — `k4_tlm.py:298–320`.)
3. `_connect_all()` consumes the surviving shared front for bond Γ —
   `k4_tlm.py:432–454`.

**Method B — run the toggle.** `external_z_local` is a live boolean; setting it
`False` restores the pre-fix overwrite. The regression
`test_f1_shared_front_ordering.py::test_defect_control_overwrite_without_external_flag`
exercises exactly this and shows the V=0 Cosserat-loaded front collapsing to
`z≡1` under the defect. Reproduced independently in this lane (§4).

## 3 · The materiality kernel — why "V-active" is necessary but not sufficient

Two structural facts sharpen the naive "V-active ⇒ affected" rule:

**(a) The shared front reduces EXACTLY to the V-only kernel when Cosserat is
quiet.** With `use_asymmetric_saturation=True` and Cosserat cold
(κ=ε=0, h=0): `A²_μ=0 ⇒ S_μ=1`, `A²_ε = V²/V_SNAP² ⇒ S_ε=√(1−A²_V)`, so
`z_shared = √(S_μ/S_ε) = (1−A²_V)^(−1/4)`, which is *identically* the legacy
V-only `1/√S(V)` (`_update_saturation_kernels`, `cosserat_field_3d.py:680–692`
vs `_update_z_local_field`, `k4_tlm.py:315–318`). **Measured: z_local identical
to 6.97e−14 between fixed and defect on a V-active + Cosserat-quiet config**
(§4 Config C). ⇒ materiality requires **V-active AND Cosserat-active** at
overlapping sites; the helicity `h` is a property of the ω-field, not V
(`_beltrami_helicity(omega,…)`, `cosserat_field_3d.py:683`), so chiral **V**
drive alone does not break the symmetry.

**(b) Bond reflection is power-conserving, so the V-sector ENERGY is an exact
invariant of the fix.** `_connect_all` mixes each bond unitarily
(`Γ = (z_B−z_A)/(z_B+z_A)`, `T = √(1−Γ²)`, `Γ²+T²=1` exactly —
`k4_tlm.py:440–441`), and the coupled engine scatters *linearly*
(`nonlinear=False`, `k4_cosserat_coupling.py:304`), so `V_ref = ½ΣV_inc − V_inc`
is itself z_local-independent (`k4_tlm.py:376`). Changing `z_local` therefore
**re-routes V spatially but cannot change Σ|V_inc|²**. **Measured: E_V final
identical to ≤3e−14 %, and E_V constant over the whole run, across passive /
converter-on / impedance-on configs** (§4). The fix's first-order effect is on
**V spatial distribution only** (peak position, localization, density-peak core
fraction) — `max|V_inc|` moved ≤0.20 % at the strongest loading tested.

**Corollary buckets — most consumers are immaterial by construction, not by luck:**

| Bucket | Why immaterial to the F1 fix |
|---|---|
| **Standalone `K4Lattice3D(op3_bond_reflection=True)`** | `external_z_local=False` (default) — path unchanged, and *correctly* so (no Cosserat front exists). ~20 drivers + 3 tests. |
| **Coupled eigenmode / spectral** (`r7_cos_block_*`, `r7_helmholtz_*`, `r7_*_shift_invert`, `r7_k4tlm_scattering_lctank`, `r7_lattice_resolution_sweep`, `r7_n64_topology_check`) | Build a **static operator**; `.step()` count = 0 → the scatter/connect *ordering* is never exercised. N/A. |
| **Coupled, V-quiet** | V≈0 ⇒ bond Γ acts on ~zero pulses ⇒ V-observable ≈0 either way. |
| **Coupled, V-active + Cosserat-quiet** | shared front ≡ V-only (§3a; z_local identical to 1e−14). |
| **Coupled, V-active + Cosserat-active, ENERGY observable** | power-conserving ⇒ E_V exact invariant (§3b). |
| **Coupled, V-active + Cosserat-active, SPATIAL observable** | **← the only first-order materiality class.** |

## 4 · Empirical before/after (fixed = `external_z_local=True` vs defect = `False`)

Harness: synthetic seeds on `CoupledK4Cosserat(N=12, pml=0,
disable_cosserat_lc_force=True)`, V planted on 3 active interior sites,
40 steps. Report-only.

| Config | V | Cosserat | z_local range (shared front) | E_V rel Δ | traj L2 reldiff | max\|V\| rel Δ |
|---|---|---|---|---|---|---|
| A · V-quiet + ω-active | 0 | ω=0.35 | 0.999 (dev ~1e−3) | V≡0 both | — | V≡0 both |
| C · V-active + Cosserat-quiet | 0.4 | 0 | z **identical to 6.97e−14** | +2e−14 % | 3e−14 % | 0.0000 % |
| B1 · V-active + ω=2.5 | 0.4 | ω-curv | 0.909 – 0.958 | +2e−14 % | 1e−14 % | −0.07 % |
| B2 · V-active + u-strain=1.0 | 0.4 | ε-strain | 1.000 – 1.045 | +2e−14 % | 3e−14 % | −0.17 % |
| B3 · V-active + ω=2.5 + u=1.0 | 0.4 | both | loaded | −2e−14 % | 2e−14 % | −0.20 % |
| passive/converter/impedance sweep | 0.4 | ω=2.0 | loaded | ≤3e−14 % | ≤2e−14 % | −0.07 % → −0.20 % |

**Read (not interpreted):** in every configuration the V-sector **energy** is
invariant to machine precision; only `max|V|` (a spatial peak) moves, and at
≤0.20 % for these loadings. The converter/impedance channels did not fire in the
synthetic seeds (A² did not localize at the `R_II` wall), so the runaway/pumped
regime (genesis-24, 1e4 V-growth) is **under-sampled** here — that regime is the
materiality candidate and is left to a gated re-run (companion report), not run
in this lane.

**"1.045-class" reconciliation (flag).** The briefing's "1.045-class" survives-value
maps to the **electric-loaded** shared front (u-strain → A²_ε → z>1; u=0.8 gives
z_max = 1.0446). The banked regression config uses an **ω-Beltrami** seed, which
loads the **magnetic** sector (A²_μ → z<1 → 0.999). Both are valid V-quiet +
Cosserat-active fronts; they exercise opposite sectors of `√(S_μ/S_ε)`. The
strengthened regression (§ STEP 2) pins **both**.

## 5 · Consumer enumeration (two-method: `rg` + `grep -rn`, cite file:line)

**Affected surface = the coupled path only.** `external_z_local=True` is set at
exactly one site (`k4_cosserat_coupling.py:312`); every other
`op3_bond_reflection=True` construction is standalone `K4Lattice3D`
(external_z_local False) and is N/A.

**Coupled-path entry points:**

- Direct `CoupledK4Cosserat(...)`: `genesis_v18_coupled.py:93`,
  `vacuum_engine.py:1687`, and drivers `coupled_coupling_test.py`,
  `coupled_pair_creation.py`, `coupled_self_saturation.py`,
  `cross_sector_gap1_closure.py`, `cross_sector_pump_confirmation.py`,
  `f6_field_channel.py`, `k4_tlm_v15_nucleation.py`, `saturation_heatmap.py`;
  tests `test_cross_sector_coupling.py`, `test_f1_shared_front_ordering.py`.
- `VacuumEngine3D` (wraps `CoupledK4Cosserat`, `vacuum_engine.py:1687`): 9 direct
  + 67 of the 80 r7–r10 files (via `VacuumEngine3D.from_args`, e.g.
  `r10_path_alpha_v14_single_cell_boundary.py:65,140`). The 13 non-users run
  fdtd3d / master-equation / srs engines → N/A.
- `genesis_v18_coupled` (wraps `CoupledK4Cosserat`, `genesis_v18_coupled.py:93`,
  converter+impedance on): `loop_gap_harness.py`, `loop_gap_seeds.py`,
  `blob_ablation_kernel_off.py`, `genesis_node_birth_discriminator.py`,
  `genesis_npersist_battery.py`, `gpersist_localization_observable.py`; tests
  `test_l3_mass_cage.py`, `test_genesis_node_birth_discriminator.py`.

### 5.1 · r7–r10 bucket — TRIAGED (closes the first-pass NEEDS-TRIAGE)

Partition of the 80-file family by mechanism (§3 buckets), not per-file guess:

| Sub-bucket | Count | Disposition |
|---|---|---|
| Non-coupled engine (fdtd3d / master-eq / srs) | 13 | **N/A** — not the coupled path |
| Coupled **eigenmode/spectral** (`.step()`=0, static operator) | r7 family (7 cited + siblings) | **N/A** — ordering never exercised |
| Coupled time-domain, **energy / dispersion / topology** observable | majority of r8–r10 cited | **immaterial by §3b** — power-conserving; E_V, wave-speed, winding invariant |
| Coupled time-domain, **V-spatial** observable (self-trap, localization, phasor/Φ_link, DC characterization) | small subset (`r10_v8_t_st_self_trap`, `r9_path_alpha_v2_phi_link_sector`, `r10_vacuumengine3d_transverse_2_3_emergence`, `r10_v8_v_dc_*`) | **candidate** — but no *standing banked verdict* keyed on absolute V-localization beyond the six HIGH rows already tracked; sub-% spatial shift expected |

Verification samples: `r7_cos_block_n64_c_eigvec.py` `.step()`=0 (eigen);
`r10_v8_foundation_audit_t2_dispersion_v2.py` measures wave-speed (Cosserat);
`r10_v8_t_st_self_trap.py` time-domain V-plant (spatial candidate).

## 6 · V-ACTIVE consumer table (banked results with standing verdicts)

Carries forward the six HIGH rows from the first pass, re-keyed to the §3
materiality kernel. Full verdict-movement analysis in the companion report.

| Consumer (banked doc) | V-class | Cosserat-active? | Load-bearing quantity | First-order materiality class |
|---|---|---|---|---|
| `2026-07-14_gpersist-localization-observable_RESULT.md` | V-active (√α pump) | yes | **localization meter / density-peak core fraction** (spatial) | **§3b spatial — candidate** |
| `2026-06-09_genesis-24-saturated-seed_result.md` | V-active (runaway →1e4) | yes | `max|V_inc|`, source-channel-FIRES | spatial + pumped runaway — candidate |
| `2026-07-12_genesis-node-birth-discriminator_result.md` | V-active | yes | `v_inc_peak`, D1–D4 persist gates | spatial peak — candidate |
| `2026-07-13_genesis-npersist-n14-battery_RESULT.md` | V-active (family) | yes | E/φ persist (G-PERSIST family) | energy-class → §3b invariant-leaning |
| `2026-06-04_full-electron-option-B-discrete-emergence-result.md` | V-active | yes | (V_inc,V_ref) retention trajectory | spatial trajectory — candidate |
| `2026-06-09_cross-sector-pump-confirmation_result.md` | V-active (drive-to-yield) | yes | **null**: V does *not* source ω (VERDICT B) | V→ω reads V_sq not z_local → **null robust** |

---
*Docs-only. Engine untouched by this document. Grant adjudicates any re-run
scheduling or ruling reopening. Materiality verdict-movement in the companion report.*
