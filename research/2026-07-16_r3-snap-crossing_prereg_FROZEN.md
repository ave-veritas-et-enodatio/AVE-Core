# R3 — the destructive test: drive one cell past V_snap (past-A=1) — prereg FROZEN

**Date:** 2026-07-16
**Charter:** [`_orchestration/2026-07-15_hardware-ratings-map.md`](../_orchestration/2026-07-15_hardware-ratings-map.md) §2 **R3** — *"★ Absolute maximum (snap) — `V_snap = m_ec²/e`; rectification past it … THE DESTRUCTIVE TEST (new charter): drive one cell past snap; watch for rectification."* Status there: **UNRUN** ("the most hardware-shaped test the program owns has never been run in-engine").
**Corpus prediction under test:** pair production ≙ vacuum-avalanche breakdown — past-snap overflow rectifies AC→DC winding (the Miller-row / translation-circuit mapping; the FPB past-snap-overflow walk; `manuscript/vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex:85` — *"the blocked longitudinal kinetic energy shatters sideways into two contra-rotating Beltrami vortices"*).
**Class:** prereg — **freeze-by-push BEFORE any driver code exists** (ave-prereg Step 3.11). This file is committed AND pushed before the first line of `r3_snap_crossing.py`.

> ★ **FROZEN.** §0–§4 (identity, hypothesis, verdict classes, adjudication thresholds, method) are locked before any RESULT is read. No retune after fire (Rule 11). A falsified prediction retracts via Rule 12, it does not refill the slot (Rule 12 / A47 v11b).

---

## §0 Test identity + sector header (mandatory, before any standard-physics word)

**Which sector is driven / which carries the predicted product?**
- **DRIVE = E-sector** (the longitudinal scalar substrate potential `V` — the "3"/V-sector, Heaviside-excised longitudinal scalar; NOT a Maxwell transverse photon).
- **PREDICTED PRODUCT = T2 / Cosserat winding** (the micro-rotation grade `ω`; rectified DC winding = a persistent, non-decaying net micro-rotation `Φ_ω`).
- **The observable IS the cross-sector transfer E→T2.** Sub-snap the two sectors are decoupled (`coupling_strength = α₀(1−S(V)) → 0` as `S→1`); the coupling engages only as `A→1` (`S→S_min`). So a persistent T2 winding produced by an E-sector drive, absent in a sub-snap control, is the engine-scale signature the corpus predicts.

**Does the chosen engine carry those DOF?** Yes — `ave.core.cosserat_master_equation_fdtd.CosseratMasterEquationFDTD` (`coupling_mode="shared_flux"`, the Phase-2b canonical bidirectional Op14 flux-trade):
- E-sector field `V(r,t)` with the Ax-4 kernel `S(V)=√(1−(V/V_yield)²)` (`saturation_kernel`, `master_equation_fdtd.py:156`).
- T2 field `ω(r,t)` (scalar Cosserat micro-rotation) with source term `−α(V)·V̇` (`cosserat_master_equation_fdtd.py:189`) — the E→T2 pump.
- Reactance pair registers: C-state `Sigma_V_sq` (`:227`) and L-state `Sigma_Phi_link_sq` (Φ_link inductive proxy, `:235`).

**Cold-vs-saturated:** the test RAMPS a single cell from the cold linear regime (`A≪1`, `S≈1`) through the knee (`A²=2α`), avalanche (`A≥√3/2`), wall-adjacent (`A→1⁻`), to **past** (`A≥1`, `S→S_min`). Surroundings held sub-yield.

**Regime / phase-state declaration (per stage; per the regime-discipline memory):**
MODE = *driven* (not free-relaxation). REGIME = *ramped I→II→III→IV at one cell*. PHASE-STATE = *cold-start → local wall-adjacent → past-crossing → post-drive relaxation*. A null in a regime where the effect cannot exist would be ARTIFACT not falsification — hence the regime is instrumented explicitly (§4).

**Coordinate discipline (phase-space-coordinate-check, A46):** the crossing is measured in the engine-native dimensionless **`A = V/V_yield`** coordinate and in the engine-native **T2 registers (`ω`, `Φ_ω`, `Φ_link`)** — NOT against an SI 511 kV target. In this engine's macroscopic normalization the kernel's rupture root `S=0` sits at `A=1` i.e. `V=V_yield` (the macroscopic-solver default); the physical `V_snap = 511 kV = V_yield/√α` and `V_yield = 43.65 kV` are the two SI anchors of the SAME dimensionless `r=1.0` rupture boundary (abs-max chapter: *"all five ratings correspond to the Regime III/IV boundary r = A/A_c = 1.0"*, `02_absolute_maximum_ratings.tex:18`). "Cross A=1" = "drive the kernel to its rupture root," normalization-independent.

**Consistency-vs-emergence tag (A47 family):** **CONSISTENCY-class.** The test asks whether the engine's frozen dynamics *manifest* the corpus-asserted rectification when driven to the kernel-rupture root. It is NOT an emergence claim (no CODATA target is recovered; no value is derived). The rupture scale `V_yield`/`V_snap` are DERIVED-from-`{m_e,c,α,ℓ_node}` pins, used here only to locate `A=1`.

**Bench-∅ honesty rail:** this probes the **MODEL's absolute-maximum behavior**. The real vacuum's snap is Schwinger-scale (`E_S≈1.32e18 V/m`; largest lab `E/E_S∼10⁻⁸`); nothing here touches the actual machine. Model-first, bench-∅.

**Explicitly NOT this test:** not a claim that pair production is confirmed; not an SI-value emergence; not the genuine (2,3) *integer* topological winding (that lives in the srs vector engine `crystal_graft_v4` / the S1 gate `compute_Q_link` — a heavier, separately-frozen harness; the scalar-`ω` DC component here is the engine-scale *rectified-micro-rotation* register, an honest proxy for "DC winding," and this scope-limit is declared not hidden); not a retune-to-cross exercise (the A_cap/S_min clamp is reported as-is, §4).

---

## §1 Hypothesis + the surfaced physics question (pre-test-physics-check)

**H (corpus):** driving one cell's amplitude across `A=1` produces a **persistent DC component in the T2 winding register** (`Φ_ω`), absent in an otherwise-identical sub-snap ramp. This is the pair-production-as-avalanche-rectification signature at engine scale.

**Pre-test plumber-physical question surfaced to Grant (NOT resolved by me — flagged):**
> In this harness rectification = a *latched* DC winding that survives after the drive stops. But (i) the canonical Ax-4 kernel `S(A)=√(1−A²)` is **anhysteretic** (zero enclosed loop area ⇒ no remanence — this is the known **R10 loop gap**, `engine-capability-map.md §3.3`), and (ii) the `ω`-equation is **linear in ω** given `V`. A closed `V`-path (ramp up, ramp down) has `∮α(V)dV = 0` because `α` depends only on instantaneous `|V|`; a linear oscillator fed a zero-net-impulse source relaxes back to `ω=0`. **So is "pair-production-as-rectification" physically a REMANENCE claim — gated on the R10 loop — rather than a clipping claim the anhysteretic engine can carry?** If so, the honest expectation is CLIPS-ONLY on THIS engine, and RECTIFIES would require the loop primitive the frozen kernel deliberately lacks. This is registered as the analytic prior; **the run adjudicates, not the prior.**

**No claim that any particular class is expected.** Fork-record-both: CLIPS-ONLY (anhysteretic prior) and STALLS (the wall reflects the soft drive) are both live; RECTIFIES would be the surprising, load-bearing positive; NUMERICAL guards the instrument.

---

## §2 Frozen verdict classes + adjudication thresholds (locked; no post-hoc drop, Rule 11)

Let, over PML-excluded interior cells only (`pml_thickness ≤ {i,j,k} ≤ N−pml−1`):
- `A_src(t) = |V_src(t)|/V_yield` — driven-cell field strain (the crossing coordinate).
- `S_ker(t) = saturation_kernel(V_src)` — the kernel feedback (clamped ≥ `S_min`).
- `Φ_ω(t) = Σ_interior ω(t)` — net micro-rotation content = the **DC-winding register**.
- `AC_peak = max_t |Φ_ω(t)|` over the DRIVE window; `DC_post = |mean_t Φ_ω(t)|` over the POST-drive relaxation window `[t_off+settle, t_end]`.
- `R_rect = DC_post / AC_peak` — rectification fraction (0 = no DC latched; ~1 = fully rectified).
- `persist = |mean(Φ_ω, 2nd half of post window)| / |mean(Φ_ω, 1st half of post window)|` — non-decay of the DC component.
- Harmonic content: FFT of `V_src` and `ω_src`; `clip_ratio = Σ(odd-harmonic power ≥ 3f) / (fundamental power)`.

Frozen thresholds: `RECT_FRAC = 0.10`, `RECT_RATIO = 10`, `PERSIST_MIN = 0.5`, `CLIP_TOL = 1e-2`, `STALL_GAP = 0.05` (A-units), `ENERGY_DRIFT_TOL = 5e-2` (fractional, over a source-off conservation window), `CONV_TOL = 0.20` (fractional metric change under dt/2 or grid refine).

| Verdict | Fires when (past-snap run vs its sub-snap twin) |
|---|---|
| **RECTIFIES** | `A_src` crosses 1 AND `R_rect(past) ≥ RECT_FRAC` AND `R_rect(past)/max(R_rect(control),ε) ≥ RECT_RATIO` AND `persist ≥ PERSIST_MIN` AND the metric survives the dt/2 + grid-refine convergence pair (`|Δ| < CONV_TOL`). The persistent DC winding is the crossing's product, not a transient or a numerical artifact. |
| **CLIPS-ONLY** | `A_src` crosses 1 AND `clip_ratio(past) − clip_ratio(control) > CLIP_TOL` (clipping harmonics appear at the crossing) BUT `R_rect(past) < RECT_FRAC` (no latched DC winding). The register oscillates + radiates; no remanence. |
| **STALLS** | Soft-source primary: commanded `A_peak > 1` but the self-consistent field ceilings at `A_ceil` with `1 − A_ceil > STALL_GAP` (the wall reflects the drive; the engine enforces `A=1` as an asymptote). Report `A_ceil` and `S_ker_min` vs the ideal `A=1 / S=0`. |
| **NUMERICAL** | NaN/Inf before the physics window closes, OR energy-drift `> ENERGY_DRIFT_TOL` in the source-off conservation window, OR the key metric FAILS the dt/2 or grid-refine convergence pair (`|Δ| ≥ CONV_TOL`). Report the failure amplitude + the convergence table. A blow-up is INSTRUMENT, not physics. |
| **MIXED** | Verdict differs across drive shape (A vs B) or across resolution in a way not cleanly one class — report every sub-verdict, no single-headline. |

**Entailed-branch liveness (ave-prereg 3.10):** each class must be *reachable*. RECTIFIES is reachable — a plant that imposes a hysteretic `α` (loop) or a one-signed source-integral would fire it; the production run uses the anhysteretic canonical kernel and both a symmetric and a unipolar drive so the class is not entailed-never by construction. STALLS is reachable via soft-source self-consistency. NUMERICAL is reachable by the singularity-adjacent regime. The sub-snap control is what makes RECTIFIES/CLIPS *discriminating* (it removes the "any nonlinearity clips" triviality).

**Decision rule:** the past-snap verdict is read against its sub-snap twin AND the convergence pair; a positive (RECTIFIES) is only banked if it survives BOTH controls. STALLS and CLIPS-ONLY are as informative as RECTIFIES — the engine refusing to cross, or crossing without remanence, are real datasheet entries (they close the R3 cell with a REFUSED/DRIVEN status + a named mechanism).

---

## §3 Method (harness, drive, controls — locked)

1. **Harness:** `CosseratMasterEquationFDTD(N, dx=1.0, V_yield=1.0, c0=1.0, coupling_mode="shared_flux", alpha_0=1.0)` — natural units; the kernel rupture root `A=1` sits at `V=V_yield=1.0`. `A_cap`/`S_min` left at engine defaults (0.99 / 0.05) and REPORTED as the regularization floor (§4) — **not** retuned to force a crossing.
2. **Grid:** `N=48` (primary), `pml_thickness=6`. Source at the box center (deep interior, PML-excluded by construction). Surroundings start cold (`V=ω=0`).
3. **Drive shapes** (both run past-snap and sub-snap):
   - **Shape A — bipolar AC carrier + rising envelope:** `V_src(t) = env(t)·A_peak·V_yield·sin(2π f t)`, `env` a `tanh` ramp 0→1 over `N_ramp`, hold `N_hold`, then source OFF for `N_relax` (relaxation). Carrier `f` set to `≈20` samples/cycle (well-resolved), recorded in output. Tests clipping harmonics + any spontaneous-symmetry-breaking rectification.
   - **Shape B — unipolar ramp-hold-release (the literal "charge one cell past V_snap"):** `V_src(t) = env(t)·A_peak·V_yield` (one-signed DC push), ramp up over `N_ramp`, hold `N_hold`, ramp down / source OFF over `N_relax`. The most rectification-favorable input (non-zero source integral during ramp).
4. **Amplitudes (frozen):** past-snap `A_peak = 1.3` (clear crossing); sub-snap control `A_peak = 0.8` (per charter; `A²=0.64`, deep Regime III but never crosses). Same drive shape, envelope, and timing between a past/sub twin — ONLY `A_peak` differs.
5. **Source mode:** primary = **soft** (`source_mode="soft"`, current-injection-like) so the STALLS question is real (the field builds self-consistently and the wall may reflect it). A **hard**-source companion (`source_mode="hard"`, field imposed) is run for Shape B past-snap to GUARANTEE a crossing and isolate the T2-register response conditional-on-crossing (reported as a sub-result; it cannot STALL by construction).
6. **Controls (frozen):**
   - **Sub-snap twin** — `A_peak=0.8`, identical otherwise. The RECTIFIES/CLIPS discriminator.
   - **Convergence pair** at the crossing (Shape B past-snap): (a) **dt/2** via `cfl_safety/2`; (b) **grid refine** `N=64` same physical box. The key metrics (`A_src` max, `S_ker` min, `R_rect`) must be stable within `CONV_TOL`; else NUMERICAL.
7. **Compute cap:** ≤ 3 concurrent runs; the 6-run matrix batched.

---

## §4 Instruments + numerical-health guards (Rule-10 empirical-driver discipline)

Recorded every `probe_every` steps over the FULL run (drive + relaxation):
- **S trajectory:** `A_src(t)`, `S_ker(t)`; report `A_src_max` (field crossing) AND `S_ker_min` (kernel feedback floor). **Honesty:** `S_ker` is clamped at `S_min=0.05` and `A` at `A_cap=0.99` in the *c_eff/coupling feedback* — the FIELD `A_src` is unclamped (leapfrog `V` is free), so the field can cross `A=1` while the kernel feedback is regularized. Both are reported; `S_min` is the engine's singularity-regularization = an INSTRUMENT limit, not the physical `S=0`.
- **Local energy ledger:** `Sigma_V_sq` (E/capacitive), `H_cosserat` (T2), `Sigma_Phi_link_sq` (L/inductive Φ_link), `H_total`. **Reactance-pair tracking (Rule-10 corollary):** BOTH the C-state (`Sigma_V_sq`) and the L-state (`Sigma_Phi_link_sq`) recorded at EVERY probe step over the whole window — never a single-phase snapshot (a one-phase read is consistent with both static and oscillator-at-peak).
- **Φ_link / winding register before/during/after:** `Φ_ω(t)=Σ_interior ω`, `Sigma_Phi_link_sq(t)`, at pre-drive (≈0), during-drive (AC), post-drive (the DC test). PML cells excluded from all interior sums.
- **Harmonic content:** FFT of `V_src`, `ω_src` over the hold window; `clip_ratio` (odd-harmonic power fraction) = the clipping-products readout.
- **Density-peak sampling (Rule-10 corollary):** in addition to the known source cell, a top-K `|ω|²` interior extraction (PML-excluded `argpartition`) each snapshot, to catch whether any rectified winding lands OFF the source cell (a shell would hide at the source-centroid).
- **Numerical-health guards:** per-step `max|V|`, `max|ω|`, `isfinite` check (abort+flag on NaN/Inf, record the step + amplitude); fractional energy drift over the source-off window; the dt/2 + grid-refine convergence table. A blow-up is reported as NUMERICAL (instrument), never as a physics rupture.

---

## §5 Outputs

- `research/2026-07-16_r3-snap-crossing_results.json` — full metric matrix (per run: `A_src_max`, `S_ker_min`, `R_rect`, `persist`, `clip_ratio`, energy-drift, verdict inputs) + convergence table.
- `research/2026-07-16_r3-snap-crossing_result.md` — the frozen verdict, the key trajectories (S_min reached, winding register before/after, control comparison), the numerical-health statement, and the mechanism named (esp. if CLIPS/STALLS — link to the R10 loop gap).
- Figures (house style: WHITE, `ave.viz.style.apply`): S-trajectory + Φ_ω(t) past-vs-sub overlay; reactance-pair (C/L) time series; harmonic spectrum.

---

*Rule-of-this-prereg: §0–§4 do not change after the first RESULT byte is read. If H falls, it retracts via Rule 12 (🔴 header, body preserved) and the R3 cell closes with a DRIVEN/REFUSED status + named mechanism — the slot is not refilled with a rescue (Rule 12 / A47 v11b). Honest closure (Rule 11): a clean STALLS or CLIPS-ONLY with the anhysteretic mechanism named is the discipline working, not a failure to debug around.*

---

## POST-FREEZE AMENDMENTS (2026-07-17, post-review — the frozen body above is untouched)

These amendments are appended below the frozen §0–§5 body (which is byte-untouched). They flag — they do **not** rewrite — prereg items surfaced by the PR#718 adversarial review (12 findings, all EVIDENCE-VOID / repair-and-bank; no physics verdict flips). Full re-adjudication lives in `2026-07-16_r3-snap-crossing_result.md`.

**A-1 (R-2) — the STALLS entailed-branch liveness row is RETRO-VACUOUS.** §2 line 67 (STALLS class) and §2 line 71 ("STALLS is reachable via soft-source self-consistency") presume a stiffening wall that the soft self-consistent field runs into. But in the shipped harness the kernel feedback is floored at `S=0.141` by the `A_cap=0.99` clamp (`√(1−0.99²)=0.1411`), so **the wall never forms** — and the soft source **never calibrated amplitude** (the sub-snap soft control commanded `A=0.8` but reached `A=6.728`, `e_growth≈145`, itself in the blow-up bin). STALLS was therefore **not reachable as instrumented** — the liveness claim was retro-vacuous. The result doc reclassifies STALLS as **UNADJUDICABLE in this harness** (not "falsified"): a null where the effect cannot exist is ARTIFACT not falsification (the frozen §0 rail's own words). This does **not** flip any physics verdict; it corrects a verb/scope claim.

**A-2 (R-8 / R-3) — "6-run matrix" is a count slip; the shipped matrix is 5 runs.** §3 line 89 says "the 6-run matrix batched", and the driver docstring inherited "6-run". The frozen method §3.3–§3.5 defines exactly **five** runs: 2× Shape-A soft (past + sub), 2× Shape-B soft (past + sub), and 1× Shape-B hard companion. `build_matrix()` returns 5 configs; the count word "6" is a slip with no effect on the frozen design. Corrected to "5-run" in the driver docstring; flagged here.

**A-3 (R-3) — the frozen `ENERGY_DRIFT_TOL=5e-2` NUMERICAL trigger was never wired in the original driver.** §2 line 61 froze `ENERGY_DRIFT_TOL = 5e-2` (fractional source-off energy drift) as a NUMERICAL trigger. The original driver did not implement it and instead minted `stable ⇔ e_growth < 0.5` and `BLOWUP_FACTOR=100`, both **post-charter**. The repair adds the frozen constant, discloses the two post-charter instruments, and re-adjudicates every stable-labeled cell against the frozen `5e-2` bar using already-banked numbers (no re-runs; no threshold retuning — Rule 11). Consequence banked in the result doc: **the AC (Shape-A) case is instrument-blocked everywhere at the frozen tolerance** (the AC null is unreadable at `5e-2`); the Shape-B crossing at `cfl≤0.1` (`e_growth=0.031`) is the only frozen-stable crossing cell; the requires-BOTH mechanism (`8.378` vs `0.073`, ~114×) survives either bar.

*These amendments are flag-only. No frozen threshold was loosened; no verdict was flipped; the RECTIFIES-not-supported physics and the named mechanism bank unchanged. The frozen §0–§5 body above remains the locked pre-registration.*
