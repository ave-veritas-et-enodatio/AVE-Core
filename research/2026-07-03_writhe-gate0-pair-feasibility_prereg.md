# FROZEN PRE-REG — Writhe arc GATE-0: pair feasibility

**Status:** FROZEN. Committed BEFORE any driver code (Chern-arc discipline).
**Arc charter:** [`_orchestration/2026-07-02_writhe-force-ratio-build-brief.md`](../_orchestration/2026-07-02_writhe-force-ratio-build-brief.md) (Gate-0 = brief §3 step 0).
**Scope cap:** Gate-0 ONLY. The four-configuration T⁰ⁱ campaign (brief steps 1–5) is HELD pending Grant's review of this gate's result.
**Classification (`consistency-vs-emergence`):** CONSISTENCY-class. Gate-0 asks *can the engine host a winding pair and does each knot conserve its S1 DOF* — an engine-capability check, NOT an emergence claim. **No |F| ratio of any kind is claimed, measured, or implied here.** The ratio is the held campaign.

---

## 0. Sector header + regime declaration (mandatory, per discipline)

- **SECTOR.** The pair interaction is carried by the **T2 / Cosserat micro-rotation ω-sector**. Charge = Beltrami helicity `H_bel = ∫ ω·(∇×ω)` read off the real-space ω micro-rotation grade (S1 axiom chain, `s1_winding_conservation_gate.py:9-16`). The (2,3) winding = toroidal "2" (ω polarization-direction) × poloidal "3" (the ω-tank LC quadrature phase). Mass (A1 dilatation) is NOT the carrier here (sector-ownership discipline: mass=A1, charge=Cosserat-winding — never cross-wire).
- **REGIME.** Gate-0 runs on the **S1 isolated-knot host** (`s1_winding_conservation_gate._build_isolated_knot`): ω-carrier ON (own wave eq + own momentum + mass-gap LC reactance), **buckle OFF**, photon OFF, Woltjer/Taylor helicity-LOCK ON (`CrystalGraftV4`, `crystal_graft_v4.py:74`). This is the exact host the S1 gate used and passed — reused, not reinvented (mission spec).
- **PHASE-STATE.** Seeded quasi-stationary breathing knots (LC quadrature: C-state in ω, L-state in ω_prev via `seed_omega_known_2_3`, `crystal_graft_v4.py:296`), evolved under the engine's real `step()`. **substrate-native-check CP8:** precursors seeded, dynamics let evolve — NOT a frozen template.
- **WALL vs MEDIUM regime labels.** The knots' own T2 self-trap walls are at Γ=−1 by definition (Grant sectoral ruling fc680254, pair-production leaf §4). The inter-knot medium is **cold / parity-even** by construction. **substrate-native-check CP10:** the saturation walls are boundary conditions of each soliton, not bulk force terms in the cold medium.

### 0.1 Coordinate declaration (`phase-space-coordinate-check`, A46)

- The **(2,3) winding label is PHASE-SPACE**: toroidal "2" = winding of `arg((ω·ê_R)+i(ω·ê_z))` around the major circle; poloidal "3" = winding of the ω-tank LC phase `arg((ω·d̂)+i(π_ω·d̂))` around the minor circle (`fast_winding_extractor.py:165-234`). It is read in its native phase-space coordinates by `extract_2_3_omega_fast`.
- The **pair separation d is REAL-SPACE**: lattice-Cartesian x-displacement between the two torus centers, in cells.
- **These two coordinate systems are NEVER cross-compared.** Each knot's winding is read in matching phase-space coords (per-knot, in the knot's local frame — see §3.3). The separation is tracked in real-space cells. No real-space-Cartesian measurement is compared against a phase-space φ² prediction anywhere in Gate-0.

---

## 1. The pair-feasibility question (Gate-0)

**Can the engine host TWO winding solitons at controlled real-space separation d, such that each individually conserves its S1 (2,3) DOF and the pair neither merges nor disperses over a measurement window?**

S1's scope was single-knot (`2026-06-24_engine-s1-winding-dof_result.md`). The engine has never hosted two winding solitons at controlled separation. Dispersal is the engine's demonstrated default failure mode (brief §3 step 0: Stage-2 native cage DISPERSES; S3 DISPERSE-FALSIFIED). Gate-0 is the cheapest decisive computation, run before the expensive T⁰ⁱ campaign (the Cleave lesson applied forward).

### 1.1 Seed method (reuse S1 machinery — do NOT invent a new host)

- **Host:** `CrystalGraftV4` via `_build_isolated_knot` config (`_CFG` frozen: `source_mode="abc", lam_sign=1, p=2, q=3, S_min=2e-3, A_cap=0.999, omega_gap=1.0, wall_center=0.62, wall_width=0.30, kappa_tilde=6/5, pml_thickness=6`). The κ̃=6/5 literal is **α-clean** (no ALPHA on the readout path — `s1_winding_conservation_gate.py:41-44`).
- **Single-knot seed:** `seed_omega_known_2_3(R, r, amplitude, p=2, q=3)` — the canonical (2,3) breathing knot the S1 gate uses. VERIFIED this session: the S1 reader reads (w_tor, w_pol) = (2, 3) on this seed.
- **PAIR seed = two single-knot seeds at offset centers.** The canonical seed hard-centers the torus at grid center `c=(N-1)/2` (`crystal_graft_v4.py:306`) with NO offset parameter. Off-center placement is done by **rigid translation** (`np.roll`) of a single centered seed to each target center, then superposing the two ω-fields (and their ω_prev LC-partners). A rigid translation preserves the winding topology exactly (VERIFIED this session: roll +6 then read → (2,3); roll is lossless). This reuses the S1 seed verbatim — the only new machinery is the lossless translation, not a new host or a new seed construction.
  - **NOTE (flag-don't-fix, structural):** the canonical `seed_omega_known_2_3` uses `+=` for ω but `=` for ω_prev (overwrite). For a pair, ω_prev must be assembled by superposing each knot's ω_prev contribution — the driver builds each knot's (ω, ω_prev) contribution independently and sums, then assigns, so neither knot overwrites the other's LC partner.

### 1.2 The pair configurations for Gate-0

- **PRIMARY: RR pair** (both knots seeded with the same handedness = identical seed, translated to two centers). This is the brief's mandated Gate-0 starting configuration.
- **OPTIONAL (labeled, budget-permitting): LL pair** (both enantiomorph = mirror-imaged seed at both centers). A cheap symmetry check: LL feasibility should mirror RR feasibility (both are like-handed pairs; the pair-feasibility physics is handedness-agnostic at this gate). If LL feasibility diverges from RR, that is a red flag surfaced to Grant, not silently resolved.
- **Handedness encoding (recorded, not load-bearing for the Gate-0 verdict):** the enantiomorph (R vs L) is the SIGN of the poloidal winding — implemented as a z-reflection (mirror) of the seed. The S1 reader `extract_2_3_omega_fast` returns winding MAGNITUDES (w_tor, w_pol) = (2, 3) for both R and L (VERIFIED). The signed handedness is a step-1+ observable; Gate-0's stability verdict rests on the magnitude conservation + separation tracking, NOT on the sign.

---

## 2. The d-sweep (pre-stated) and measurement window

### 2.1 Knot core scale (the sweep unit)

The single knot occupies a torus of major radius R=11 cells, tube radius r=4 cells (the S1 gate default N=48/R=11/r=4). The knot's real-space extent is ≈ R+r ≈ 15 cells (outer diameter ≈ 2(R+r) ≈ 30 cells). To host two knots at controlled separation without initial hard overlap AND with a PML-excluded interior between them, Gate-0 uses a **larger domain** than the single-knot N=48 so both knots + a cold mid-region + PML fit. Domain and scale are frozen here.

- **Knot core scale L_core := 2R = 22 cells** (the toroidal diameter — the natural real-space size of one knot). The separation d is the center-to-center distance between the two torus centers, reported in both cells and in units of L_core.

### 2.2 Frozen d-sweep (≥ 3 separations, small / medium / large)

Domain **N = 96** (large enough for two R=11 knots + cold gap + pml=6 each side). Both knots on the x-axis, symmetric about the true grid center XC=(N−1)/2=47.5 (the T⁰ⁱ true-center discipline, `mass_sector_field_momentum_T0i.py:82-95`), at XC ∓ d/2.

| bin | d (cells) | d / L_core | regime | rationale |
|---|---|---|---|---|
| SMALL | 24 | 1.09 | near-contact | ~1 core-diameter gap; tori nearly touch (2R=22); tests whether close pairs merge |
| MEDIUM | 34 | 1.55 | intermediate | ~1.5 core; a clear cold gap between tube surfaces (surface gap ≈ 34−2·4 = 26 > 0) |
| LARGE | 44 | 2.00 | well-separated | ~2 core; both knots comfortably inside interior, large cold mid-region |

d chosen EVEN so both centers land on integer cells symmetric about XC=47.5 (the momentum-conservation true-center discipline). All three are FROZEN. If additional intermediate d are needed to map a stability window (§4 mini-bin 3), they are recorded as such, not used to move a verdict.

### 2.3 Measurement window (frozen, with rationale)

- **Warmup:** 50 steps (past the at-rest LC turning point, matching the S1 gate `gate_c` warmup, `s1_winding_conservation_gate.py:329`).
- **Recording window:** **600 steps** after warmup (matching the S1 `gate_c_conservation_continuity` n_steps=600 — the same window the single-knot conservation PASSED on). Rationale: the pair verdict must be measured over the SAME window the single-knot S1 conservation was certified on, so a pair failure is attributable to the pair (not to a longer/shorter window than S1 used). At dt≈7.7e-3 this is ≈ 4.6 time units, ≈ 4.6 ω-tank LC periods (omega_gap=1.0 ⇒ LC period 2π ≈ 6.3 time units — so ~0.74 LC periods; the S1 gate certified conservation on exactly this step count, so it is the calibrated window).
- **Readout cadence:** the per-knot winding + separation are read every 100 steps (7 reads over the window, matching the S1 `chk = n_steps//6` cadence).

---

## 3. Stability criteria — numerically pre-committed (NO post-hoc thresholds)

A pair is **STABLE at separation d** iff ALL of the following hold over the measurement window. Every threshold is frozen here.

### 3.1 Per-knot winding conservation (the S1 DOF, per knot)

- **CRITERION S:** each knot individually reads `(w_tor, w_pol) = (2, 3)` at every readout checkpoint (7 reads), measured by `extract_2_3_omega_fast` in the knot's LOCAL frame (roll-to-center — see §3.3).
  - Threshold: **7/7 reads = (2,3) for BOTH knots** (0 tolerance on the integer — a topological integer either holds or breaks).
- **CRITERION A (alias canary):** the S1 alias-fraction on the raw winding trajectory ≤ **ALIAS_TOL = 0.34** (the frozen S1 tolerance, `s1_winding_conservation_gate.py:62`) for both knots. Alias ≥ 0.95 ⇒ INCONCLUSIVE (field detonated), reported not rescued (Rule 11).

### 3.2 Separation trackable + no merger / dispersal

- **CRITERION T (trackable):** the two knots remain resolvable as two distinct ω-energy-density peaks throughout. Measured as: the top-2 peaks of the PML-excluded interior ω-energy density `|ω|²` (density-peak sampling per Rule 10, NOT centroid) remain separated by ≥ **0.5·d_initial** at every checkpoint. If the two peaks merge into one (separation < 0.5·d_initial) ⇒ MERGER (unstable at that d).
- **CRITERION D (no dispersal):** the total PML-excluded interior ω-energy `∫|ω|²` retains ≥ **50%** of its post-warmup value at the end of the window. If it drops below 50% ⇒ DISPERSAL (energy radiated out / knot dissolved). Threshold rationale: S1 single-knot conservation held with the knot intact; a 50% interior-energy loss is a decisive dispersal signal well above numerical noise.
- **CRITERION E (separation drift bound):** the center-to-center separation drift `|d(t_end) − d_initial| / d_initial` ≤ **0.30** over the window. A drift beyond 30% means the knots are strongly accelerating toward each other (pre-merger) or apart (pre-dispersal) — either way the "controlled separation d" premise fails at that d. (This is a stability bound, NOT a force measurement — Gate-0 makes no force claim.)

### 3.3 Per-knot local-frame readout (roll-to-center)

Both winding readers (`extract_2_3_omega_fast`, `compute_Q_link`) hard-center the readout torus at grid center `c=(N-1)/2` (VERIFIED: `fast_winding_extractor.py:174`, `charge_quantization.py:496`). To read knot-A (at XC−d/2) and knot-B (at XC+d/2), the driver rigidly rolls the ω (and ω_velocity) field so the target knot sits at grid center, then reads. Roll is lossless for the winding integer (VERIFIED this session). Each knot is read in matching phase-space coords (per §0.1) — no cross-frame comparison.

### 3.4 Validate-on-known FIRST (the honest floor — mandatory)

Before ANY pair verdict counts, the driver runs the S1 single-knot validate-on-known IN THE GATE-0 SETUP: a single seeded (2,3) knot in the N=96 domain must reproduce `(w_tor, w_pol)=(2,3)` and the S1 `validate_on_known` static floor (Q_link=3, w_tor=2, null=0). If the single-knot floor does not reproduce in the Gate-0 domain, the pair result is VOID (the setup itself is broken) — reported, not rescued.

---

## 4. FROZEN mini-bins (exactly per the brief's Gate-0)

The verdict falls into exactly one bin. Committed here; not redefinable post-hoc.

1. **[PAIRS STABLE]** — at the tested d (all three, or a d-window), both knots individually pass their S1 conservation checks (Criterion S ∧ A) AND separation is trackable (Criterion T ∧ E) AND no merger/dispersal (Criterion T ∧ D) over the measurement window. → **The arc proceeds** to steps 1–5 (HELD for Grant's review). Record which d are stable.
2. **[UNSTABLE at all tested d]** — at every tested d, the pair fails at least one stability criterion (merges, disperses, or loses the winding integer). → **The pair-force observable is ILL-DEFINED at current engine capability.** Named blocker (the specific failing criterion + d), arc stops at ~10–15% of cost, register §2.4 gets the honest status. This is a legitimate Gate-0 outcome (Rule 11 honest closure), NOT a failure to debug.
3. **[STABLE ONLY IN A d-WINDOW]** — stable for some d but not others. → **The stable-d window IS the measurement domain** for the held campaign; record it exactly (which d stable, which not, and the failing criterion at the unstable ends).

**INCONCLUSIVE** (separate from all three, Rule 11 — report, do NOT rescue): the integrator cannot carry the dynamics to a clean verdict (alias canary ≥ 0.95 / detonation / NaN in the energy ledger). This says the integrator failed, not that the pair is ill-defined; reported as-is.

---

## 5. THE TRANSMISSION QUESTION (brief §3 step 0 amendment — the un-derived gap)

The brief traces the "near-yield" prerequisite to its provenance: κ_chiral enters ONLY as a multiplicative bias on saturation strain, so parity-odd dynamics vanish cold BY CONSTRUCTION. The knots' own T2 walls are AT V_yield by definition (Grant ruling fc680254), so the parity-odd saturation is **wall-supplied by the solitons themselves**; the inter-knot medium is cold/parity-even. **The un-derived gap is TRANSMISSION: can a parity-even linear medium carry the wall-generated handedness-dependent stress to a mid-plane T⁰ⁱ, or must the inter-knot region itself be driven near-yield?**

### 5.1 Candidate answer — analytical (pre-stated)

**Load-bearing architectural finding surfaced this session (flag-don't-fix), which reshapes the transmission analysis:**

> The κ_chiral term `_reflection_density_asymmetric` (`A²_μ = (1 + κ_chiral·h_local)·A²_μ_base`) lives in the **JAX `CosseratField3D` engine** at `src/ave/topological/cosserat_field_3d.py:554` — **NOT** in the S1 seed host `CrystalGraftV4`. (The brief cites the path as `src/ave/core/cosserat_field_3d.py`; the actual path is `src/ave/topological/…` — a citation-path discrepancy in the brief, flagged, not silently corrected in the brief.) In the S1 isolated-knot host the **buckle is OFF** (`_build_isolated_knot`: `buckle_on=False`), so there is NO κ_chiral saturation-bias term active at all. In this host, handedness is a purely geometric/kinematic property of the seeded ω-winding SIGN, evolving under the ω wave equation `a_ω = c_ω²∇²ω − ω_gap²ω` (`crystal_graft_v4.py:240-243`).

**Consequence for the transmission question (pre-stated candidate answer):** In the Gate-0 host, the handedness-dependent stress that could cross the cold mid-region is NOT the κ_chiral-biased saturation stress (that engine is not running). It is the **ω-field-momentum flux `T⁰ⁱ_ω = (∂_t ω)·(∂_i ω)`** — the winding carrier's OWN momentum flux, the direct ω-sector analogue of the mass-sector scalar `T⁰ⁱ = (∂_t V)(∂_i V)` (`mass_sector_field_momentum_T0i.py:137`). The candidate analytical answer: a handedness-dependent mid-plane signal exists in the Gate-0 host **iff** the two knots' ω-fields overlap in the mid-region with a parity-odd (handedness-dependent) component of the momentum-flux tensor. Because the ω wave equation is LINEAR (Beltrami + mass-gap, no saturation), the two knots' overlap is a linear superposition, and the momentum-flux `(∂_tω)(∂_iω)` is QUADRATIC in ω — so a cross-term between the two knots' fields exists and CAN carry handedness (the cross-term flips sign under mirroring one knot). **So the candidate answer is: wall-supplied saturation is NOT required for a handedness-imprint in THIS host — the linear ω overlap already carries a handedness-dependent quadratic momentum-flux cross-term, which does not require driving the cold medium near yield.** This must be TESTED, not assumed (below).

### 5.2 The transmission numerical probe (inside Gate-0 budget) + its own mini-bin

**IF and ONLY IF the RR pair is STABLE (mini-bin 1 or 3 fires),** the driver reads the mid-plane ω-sector T⁰ⁱ on the stable pair and checks it against floor. This is cheap (it reuses the already-evolved stable-pair state; no extra evolve).

- **Observable:** `T⁰ⁱ_ω = (∂_t ω)·(∂_i ω)` — the ω-sector field-momentum density, ∂_tω = `omega_velocity()` (`crystal_graft_v2.py:238`), ∂_iω central-difference along the pair axis. Mid-plane flux `Φ_mid` = mean of the two planes adjacent to XC, PML-excluded (Rule 10; reusing the `mass_sector_field_momentum_T0i.py:169` face-flux construction, ported to the ω vector field).
- **Floor:** the single-knot ω-T⁰ⁱ mid-plane value (one knot's own breathing radiation at the mid-plane) — the two-knot signal must EXCEED this to count as a real inter-knot transmission.
- **SYMMETRY CAVEAT (load-bearing, pre-stated).** The mass-sector result established that the mid-plane transported flux is **SYMMETRY-FORCED to zero for any mirror-symmetric head-on pair** (`mass_sector_field_momentum_T0i.py:269-279`, result §2). For the RR pair, the two knots are like-handed; whether the configuration is mirror-symmetric about the mid-plane depends on the seed. A parity-EVEN observable (|Φ| magnitude) may be symmetry-zeroed. **This is exactly why the transmission signal, if present, is a mirror-symmetry-BREAKING flux** — a nonzero handedness-dependent Φ_mid above floor is the transmission signal; a symmetry-forced zero is NOT informative about transmission and is recorded as such (not booked as a null).

**Transmission mini-bin (its own):**
- **[T-IMPRINTED]:** `|Φ_mid|` for the stable RR pair is **> 3× the single-knot floor** AND finite → a handedness-carrying stress reaches the mid-plane in the cold medium; **wall-supplied saturation suffices** (the cold medium need NOT be driven near-yield). Answer: transmission YES in this host.
- **[T-SYMMETRY-ZEROED]:** `|Φ_mid| ≈ 0` at floor for the RR pair AND the zero is traceable to mirror symmetry (verified by the field mirror-symmetry check, `mass_sector_field_momentum_T0i.py:42`) → the parity-EVEN mid-plane observable is symmetry-forced to zero; this is NOT a transmission null (the handedness signal is parity-ODD and needs the RL/LR configs, which are in the HELD campaign). Documented-open, NOT booked as wrong-regime, NOT booked as a cold-medium null (the brief forbids booking a cold-medium null as wrong-regime).
- **[T-DOCUMENTED-OPEN]:** the RR pair is stable but the ω-T⁰ⁱ probe is inconclusive (floor comparison ambiguous, or the pair is stable only in a window too narrow to probe cleanly) → transmission question documented-open, answered analytically only (§5.1), for the HELD campaign to resolve with the full four-config RL/LR set.

**The transmission question is answered at one of three grades in the result: answered-analytically (§5.1 always) / probed-numerically (if stable, one of T-IMPRINTED / T-SYMMETRY-ZEROED / T-DOCUMENTED-OPEN) / documented-open.**

---

## 6. What Gate-0 does NOT establish (honest scope, pre-stated)

- **NO |F| ratio claim of any kind.** Gate-0 measures pair feasibility + winding conservation + (if stable) a mid-plane ω-T⁰ⁱ presence/floor check. It does NOT measure `R = |F|_co / |F|_anti`, does NOT compare RR vs RL/LR forces, does NOT touch the four-configuration campaign. That is the HELD arc (brief steps 1–5).
- **NO emergence claim.** CONSISTENCY-class only (can the engine host the pair?).
- **NO handedness-force claim.** Even a nonzero T-IMPRINTED transmission signal establishes only that a handedness-carrying stress *reaches* the mid-plane — it does NOT establish a force ratio ≠ 1 (that needs the co-vs-anti contrast, HELD).
- **Scope of the host.** All results are on the S1 isolated-knot host (`CrystalGraftV4`, buckle OFF). The κ_chiral saturation engine (`CosseratField3D`) is a DIFFERENT code path not exercised here; Gate-0 says nothing about that engine's pair behavior.

---

## 7. Reproduce plan

- **Driver:** `src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility.py`.
- **Constants:** canonical only (`ave.core.constants`); the S1 host is α-clean (κ̃=6/5 literal). No hard-coded physics constants; every printed number computed in-run (`ave-driver-script-honesty`).
- **Order (frozen):** (1) validate-on-known single knot in the N=96 setup → (2) RR pair at d ∈ {24, 34, 44} → bin per §4 → (3) if stable, the mid-plane ω-T⁰ⁱ transmission probe → bin per §5.2 → (4) OPTIONAL LL pair symmetry check (labeled).
- **Heavy evolves:** routed to the engine_sim CI lane per the existing test-routing pattern (the pair evolves are S1/Chern-class cost).
- **Result doc:** `research/2026-07-03_writhe-gate0-pair-feasibility_result.md` (committed-verdict gates, S3/Chern pattern).
