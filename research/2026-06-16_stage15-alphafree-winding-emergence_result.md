# RESULT — Stage-1.5 α-FREE two-sector convergence engine (winding-emergence lane)

**Date:** 2026-06-16 · **Lane:** implementer · **Branch:** `analysis/2026-06-16-boundary-mqj-stage15-alphafree-emergence`
**Prereg (FROZEN, Rule-11):** [`2026-06-16_stage15-alphafree-winding-emergence-prereg.md`](2026-06-16_stage15-alphafree-winding-emergence-prereg.md) (commit `6e5529a1`)
**Engine (NEW):** [`src/ave/core/a1_cosserat_convergence_engine.py`](../src/ave/core/a1_cosserat_convergence_engine.py)
**Drivers:** `stage15_layer_a_a1_selftrap.py`, `stage15_layer_b_coupled_stability.py`, `stage15_layer_c_emergence_probe.py`
**Success criterion (inherited, FROZEN):** `reconciliation-handoffs/2026-06-16_electron-existence-discrimination-prereg.md` §"success criterion".

---

## §0 — VERDICT: built layers (a)+(b); (c) = EMERGENCE-NEGATIVE with a precisely-localized mechanism

**Build LAYER reached: (c) — all three layers RAN.** Honest per-layer status:

| Layer | Status | What it showed |
|---|---|---|
| **(a)** α-free A1 c_eff(V) self-trap | **PASS** | the INDEPENDENT α-free longitudinal cage self-traps; longitudinal **Z_tank=√S formation_floor=0.376** (the stiffening wall FORMS) — the confinement the Stage-1 coupled VacuumEngine3D could NOT show |
| **(b)** two-grid coupled stability | **STABLE** (CP10 front coupling); **🔴 INERT-claim RETRACTED 2026-06-16 (Rule-12) → loop-closure UNTESTED** | coupled system bounded (|ω|max/seed=1.00, no blow-up); ~~the energize-LOCK loop is **INERT** on the winding~~ — **the f_V=0 / loop-INERT read was a Cartesian-stencil ARTIFACT**: the inherited `_cosserat_axial_curl` (np.roll±1) placed Ξ entirely on the K4 DEAD sublattice (alive \|Ξ\|=0) while the front window g is alive-masked, so g·Ξ≡0 for ANY field. With the substrate-native `_tetrahedral_curl` + the `adjoint_tetrahedral_divergence` back-reaction (two-sided fix, `analysis/2026-06-16-stage16-rerun-amendments`), the coupling fires on alive (f_V, f_ω_alive > 0). **Loop-closure is therefore UNTESTED here, not falsified** — re-scoped to Stage-1.6 under the corrected stencil + the H-ledger / K_wall gates. See §3 retraction header below. |
| **(c)** α-free emergence probe | **EMERGENCE-NEGATIVE** | the (2,3) does NOT self-form (bulk w_tor=w_pol=0 on reliable contours; Cosserat ω radiates out); no α-free Q; α NOT inserted. Seed-audit non-circular (CP8) |

**The chord (FORM-emergence) does NOT appear in this engine layer.** The negative is
**clean, with a named mechanism**, and the magnitude readout was **NOT forced**
(m_e/e/ℏ/2 not read; α not inserted — the α-free discipline held end-to-end).

---

## §1 — The α-free emergence read (the four-part success criterion)

1. **(2,3) winding + Γ=−1 self-form from generic IC?** **NO.** Bulk reactance
   phase-space on reliable contours (rel=0.63/0.59): `w_tor=0.0, w_pol=0.0` — zero
   winding (a pure breathing mode has no spatial phase winding). Cosserat ω-winding:
   `w_tor=−1.0` but on unreliable contours (rel=0.0, the photon radiated out, amp 0.3→0.016).
   Seed-audit PASS: `t0_closes_23=False` (no planted (2,3), CP8 non-circular).
2. **α inserted anywhere?** **NO** — α-free held end-to-end. Zero `ALPHA`/`KAPPA_CHIRAL`/
   `V_yield=√α·V_snap`/`delta_lock_fraction=α` in any update equation. Inputs:
   `κ̃=6/5=pq/(p+q)` (the (2,3) topology), `V_yield=1.0`, `ω_yield=π`, `NU_VAC=2/7`,
   `R_II=√3/2` — all geometric/topological. `ALPHA` asserted for provenance only.
3. **α-free Q emerges (~137 without being told)?** **NO** — joint-ledger guard: with
   no (2,3) resonator there is nothing for an α-free leak Q to be. α NOT emergent.
4. **Z→0 longitudinal confinement (necessary, not sufficient)?** **The gate IS met
   in Sector A** (Z_tank=√S formation_floor=0.376 → toward 0) — but it is necessary,
   NOT sufficient: the cage stiffens, yet the winding does not self-form. Confirms
   the criterion's "necessary but NOT sufficient" framing.

**Magnitude readout NOT taken (ECHO, explicitly avoided):** m_e/e/ℏ/2 not read off
the region; the α=𝓜+𝓙+𝓠 decomposition (Class-B / (R·r)-collinear / echo) not invoked.

---

## §2 — The engine (the substrate-complete-engine §4 spec's first two sectors, α-free)

Per `engine-capability-map.md` §3.1 firewall (irrotational A1 cage ↮ winding → TWO
coupled sectors), `a1_cosserat_convergence_engine.py`:

- **Sector A — the A1 cage (continuum-scalar FDTD):** the validated v14 Mode-I
  `MasterEquationFDTD` kernel as a STANDALONE integrated longitudinal field (NOT a
  projection), `c_eff(V)=c₀·(1−A²)^(−¼)→∞`, **V_yield=1.0 generic** (α-FREE). This is
  the independent A1 field the Stage-1 coupled `VacuumEngine3D` lacked (it has only
  the read-only projection `v_scalar_from_v_inc`, `cross_sector_coupling.py:226`;
  `engine-capability-map.md:45,79`).
- **Sector B — the winding (K4-tetrahedral Cosserat):** the VECTOR `CosseratField3D`
  (u, ω) micro-rotation on the K4 diamond A/B sublattice (`ω_yield=π`, `k_hopf=π/3`)
  — the multi-component U(1)-fibre carrier the scalar-bulk arc named as **missing**
  (`crystal_engine_result.md` §5).
- **Shared-front coupling:** ONE conservative Hamiltonian term `H_c=κ̃∫g·V·Ξ`,
  `Ξ=(∇×ω)·ẑ` — reciprocal functional-derivative forces on each sector's own Verlet
  acceleration (the `crystal_engine` ADD-2 energize-LOCK structure). α-FREE `κ̃=6/5`.

**Two-grid reconciliation (the brief's core challenge):** Sector A lives on every
cell (continuum FDTD); Sector B lives only on the K4 alive sublattice. TEMPORAL
reconciliation = Cosserat sub-cycled at its own stable dt; SPATIAL reconciliation =
the coupling forces front-localized + alive-masked (CP10).

---

## §3 — The two-grid coupling: what worked, what didn't (honest, flag-don't-fix)

**WORKED — the conservative force coupling is stable.** An earlier velocity-rotation
coupling PUMPED (|ω| 0.3→276 at N=24 — the genesis-24 detonation class), traced to
rotating leapfrog (½-step) `∂_tV` against Verlet (full-step) `ω̇` at mismatched
time-centering. Replaced with the position-coupled Hamiltonian force (both coupled
quantities position-like → forces on each sector's own Verlet) → NO blow-up
(|ω|max/seed=1.00, = the Sector-B-alone floor).

> ### 🔴 RETRACTED 2026-06-16 (Rule-12, substitution-not-retraction) — the "loop is INERT" claim below was a **Cartesian-stencil discretization ARTIFACT**, not a substrate finding. Re-scope: **loop-closure UNTESTED here.**
>
> **Mechanism of the retraction** (the `coupling_curl_sublattice` / two-sided-stencil diagnostic, `analysis/2026-06-16-stage16-rerun-amendments`, engine-rerun-preflight `ww8x96sci`): the `f_V=0` read below was produced by the **inherited Cartesian `_cosserat_axial_curl` (np.roll±1)**, which straddles the K4 diamond's DEAD cells and places the winding curl Ξ **entirely on the dead sublattice** (alive \|Ξ\|=0, dead \|Ξ\|≈1.6). The front window `g` is **alive-masked**, so `g·Ξ ≡ 0` for **ANY** ω-field — confined or not, co-located or not. The "disjoint support" / "extended-vs-compact" sub-findings below are **downstream of this zero**, not independent causes: they were measured against a coupling that was already identically zero by discretization. With the substrate-native `_tetrahedral_curl` forward operator AND the exact `adjoint_tetrahedral_divergence` reciprocal back-reaction (two-sided fix), the coupling **fires on the alive sublattice** (f_V_alive≈2.0, f_ω_alive≈0.6, overlap_cells 128 vs 0). **The energize-LOCK loop was never tested here** — it was disabled by a substrate-native-check Ckpt-2 violation in the inherited stencil. Re-scoped to Stage-1.6 under the corrected stencil + the H-ledger / two-sided-fire / K_wall-sweep gates (which then surfaced a *separate*, genuine bounded-wall-pump finding — see the Stage-1.6 result). **The body below is preserved verbatim per Rule-12; do NOT read it as a live falsification of loop-closure.**

**DID NOT — the energize-LOCK loop is INERT on the winding (the localized obstruction).**
The bulk source `f_V=−κ̃·g·Ξ` is **0 over the entire run** (`fV_source_live_max=0.0`,
active 0% of steps). Diagnosis (two co-located sub-findings):
- **Spatial:** the saturation FRONT shell (where the cage's stiffening wall lives,
  A_V≈√3/2; CP10 boundary-localized = the correct anti-pump discipline) and the
  winding curl Ξ (at the trap interior) have **disjoint support**.
- **Extended-vs-compact / temporal:** even a `saturated_interior` coupling variant
  stays inert — a generic transverse **propagating** ω-photon's winding curl is an
  EXTENDED, axially-distributed structure, while the cage deep-saturation core is
  COMPACT/centered; they never co-locate, and the UNTRAPPED photon radiates out
  (|ω| 0.3→0.029) before/while the cage breathes deep.

**The known-positive discipline localizes this to the coupling, NOT the integrator:**
Sector A alone HELD (Layer a); Sector B alone is rock-stable (seeded photon
|ω|max/seed=1.00, H decays 18→1, radiates cleanly). Both sectors individually stable
⇒ the inertness is the cross-sector co-location, a physics/design finding.

---

## §4 — The localized obstruction, named (extends the prior arc's gap by one level)

| arc | carrier | obstruction |
|---|---|---|
| genesis-23/24 | K4 4-port `V_inc` | toroidal "2" only; poloidal "3" absent; source dead OR detonates |
| crystal_engine→graft-v4 (CLOSED NEGATIVE) | scalar bulk + shear curl | **no U(1)-fibre carrier** — shear carries CHARGE not WINDING; w_tor=w_pol=0 |
| **Stage-1.5 (this work)** | **vector Cosserat ω (the U(1)-fibre carrier ADDED)** | **carrier present + two-grid-stable, but the energize-LOCK loop is INERT** — a generic untrapped transverse photon's winding does not co-locate with / get trapped by the cage core to close the loop |

**The design fork this surfaces (for Grant/auditor — NOT an implementer pivot, Rule 16):**
**CP10 front-localization (anti-pump)** vs **the winding co-locating with the trap
(transfer)**. A bulk-volume coupling would overlap but risks the pump CP10 forbids;
a front coupling is anti-pump but spatially decoupled from the interior winding. The
deeper question the fork raises: does the winding need to be **trapped + co-located**
with the cage core FIRST (a confined, not propagating, ω-precursor), before the
gyrotropic loop can close? That is a precursor-class + coupling-support decision that
needs Grant/corpus adjudication.

---

## §5 — Witnesses + the 4 Stage-1 corrections (panel `wvvx6y6zb`)

**Witnesses (Rule 10 empirical-driver discipline):**
- Full-Hamiltonian witness = Cosserat `total_hamiltonian()` (kinetic + gradient
  potential) + bulk conserved energy — NOT `sum(ω²)`.
- Reactance pair recorded: |ω| (C-state) AND |ω̇| (L-state) every sample (A-Rule 10).
- The full-H ramp is dominated by the bulk breather's INTRINSIC excursion (7.6×,
  IDENTICAL ON vs OFF — the known cage-alone floor, `crystal_engine_result.md` §1.2);
  the coupling-attributable pump is the ON-minus-OFF excess (≈0 — no coupling pump).
- PML-excluded interior sampling (A-Rule 10 corollary); density-peak sampling (top-|V|²
  / top-|ω|², not centroid).

**The 4 corrections, dispositions:**
1. **run N labeled explicitly** — all three drivers report `run_N_explicit` (N=28 layer a;
   N=24 layers b/c) + `long_window_periods` (12) in the JSON + console.
2. **long-window persistence (≥10P)** — 12 Compton periods (not a truncated short window).
3. **S_μ/S_ε split AND longitudinal Z_tank=√(L/C_comp)** — `S_mu_S_eps_split()` emits
   both: longitudinal `Z_tank=√S` FALLS (formation_floor 0.376) while transverse
   `Z_eff=√(S_μ/S_ε)` RISES (1.21) — the orthogonal reactances (INVARIANT-S2 Q1=B).
4. **Z_long floor = A_cap=0.99 numerical CLAMP** — annotated in the JSON
   (`A_cap_clamp_note`): `Z_tank=√S`, S clamped at `√(1−A_cap²)=0.1411`, NOT
   asymptotic Z→0 (which needs A_V→1 exactly).

---

## §6 — Checkpoint status + skills fired

- **CP8 (generative precursor, not planted):** seed-audit PASS (`t0_closes_23=False`);
  generic transverse ω-photon + sub-yield bulk, NO planted (2,3). The CP8
  structural-capability finding: the carrier is present but the loop is inert.
- **CP10 (Op17-bounded BC, not bulk force):** the coupling is front-localized
  (g_front at A_V≈√3/2), no bulk V→ω runaway channel; |ω| bounded (no blow-up). The
  CP10 anti-pump discipline is exactly what spatially decouples the winding (§3-4).
- **substrate-native-check** (CP8/CP10), **consistency-vs-emergence** (the
  emergence-vs-echo line IS the test; emergence REFUSED; Z_tank=manifestation,
  magnitudes=echo-NOT-read), **phase-space-coordinate-check** (A46 — winding measured
  in (V_inc,V_ref)/(ω_x,ω_y) phase-space, NOT real-space), **ave-conserved-vs-pumped**
  (full-H witness; the velocity-rotation pump named + fixed), **ave-canonical-source**
  (κ̃, V_yield, NU_VAC, R_II from constants; α NOT inserted), **verify-before-cite**
  (the crystal_engine→graft-v4 CLOSED-NEGATIVE arc + its §5 surfaced synthesis greped
  this session — this build IS that synthesis, executed).

---

## §7 — Corpus-state queued (auditor LANDS; implementer SURFACES)

- **engine-capability-map.md §4 (DESIGN PROPOSAL):** the first two sectors of the
  substrate-complete engine are now BUILT + two-grid-stable (α-free). The §5
  build-order DAG's "seed photon precursor → self-trap (cage AND winding emerge
  together)" node returns a localized obstruction: the cage self-traps, but the
  winding does not co-form from a generic untrapped photon (the energize-LOCK loop
  is inert). Auditor decides whether to annotate §4/§5 with this finding.
- **The front-vs-interior / trapped-vs-propagating-precursor DESIGN FORK** (§4) —
  surfaced for Grant/corpus adjudication, NOT pivoted-to.
- **crystal_engine_result.md §5 synthesis** ("graft the converter + c_eff trap onto
  the K4 4-port / vector Cosserat sector") — EXECUTED here; the result extends the
  named gap by one level (carrier present + stable; loop inert).
- **chord-vs-echo:** the implementer does NOT conclude chord/echo — the orchestrator
  adjudicates. This layer is an honest EMERGENCE-NEGATIVE; no chord, no forced echo.

---

## §8 — Honest closure (Rule 11)

Per the prereg's frozen bins, the verdict is **LAYER-C-EMERGENCE-NEGATIVE** with the
mechanism named (the inert energize-LOCK loop / winding-trap co-location obstruction).
This is the discipline working: the chord (FORM-emergence) does NOT appear in this
engine layer, and the negative was reached without dropping any adjudication criterion
(seed-audit non-circular, reliable-contour winding read = 0, joint-ledger guard
refuses any α). The magnitude readout was NOT forced — m_e/e/ℏ/2 not read, α not
inserted. The build advanced the framework by **building the first two sectors of the
substrate-complete engine (α-free, two-grid-stable)** and **localizing the residual
obstruction one level deeper than the prior arc**. The precondition for a meaningful
emergence positive — closing the energize-LOCK loop (the design fork) — is surfaced
for Grant/auditor, not auto-pivoted.
