# PREREG — Genesis-v7: the QUADRATURE DEPOSIT (a poloidal-projecting δπ_ω) + the LOCK-SURVIVAL discriminator

**Date (frozen):** 2026-06-10
**Branch:** `analysis/2026-06-10-genesis-v7-quadrature` (worktree `/tmp/ave-v7`, off `origin/analysis/2026-06-10-genesis-v6-transducer` @ `d11b0923` — INHERIT EVERYTHING at the v6 FINAL commit; do NOT push/merge — the orchestrator PRs at the end only).
**Engine lineage (subclassed, inherited physics UNCHANGED by default):** `UnifiedGenesisEngine` (`src/ave/core/unified_genesis_engine.py`) ← `CrystalGraftV4` ← V3 ← V2 ← `CrystalEngine`. Every v7 engine addition is behind a NEW parameter that DEFAULTS to the v6 byte-identical path (the inherited keeper ladder `src/tests/test_unified_transducer_v6.py` 10/10 + `test_unified_snap_machine.py` must stay green — the D-INHERIT regression gate).
**Governing discipline:** `ave-apparatus-floor-attribution v1.1` — ORDERED BINS (floor-check gates every positive; the floors §4 are evaluated FIRST); PROBE-CAPABILITY keepers (§9, every discriminating probe validated on a known-different reference + a known-positive plant-at-scale); every new knob inventoried + swept (§5). **§210-COMPLIANCE GATE: the run phase executes every sweep this prereg mandates, or states the deviation explicitly BEFORE running and re-bins. A positive whose governing knob was unswept is CLIP by this prereg's own law.**
**THE GROSS-VS-FIELD RULE (the v6 panel lesson, now STRUCTURAL — §10):** a deposit ACCUMULATOR is never a measurement. Every transducer-effect claim in v7 is the NET FIELD quantity (MAIN − OFF), measured ON the field, above its floor. The v6 numbers to beat are explicit: v6's net field ω-axial deposit was **−3.6e-5** (≈4 OOM under its by-construction accumulator ∓0.539; LOCK-DRAINED because the deposit was rigid-azimuthal — exactly the mode `_lock_relax` removes). v7's survival gate (D14): the net field deposit into the **poloidal target mode** is NOT drained — gap to its accumulator ≲ 1 OOM, OR the drain is explicitly measured and bounded.
**Skills fired at design time:** `substrate-native-check` (CP1/CP2/CP9/CP10 walked §1 — the deposit is a per-cell BOUNDARY operation on the g_wall shell, NOT a bulk EOM term); `pre-test-physics-check` (the ONE plumber-physical question surfaced to Grant — §2.4, the swirl-vs-ripple AM-conservation flag, asked BEFORE design per Rule 16 strengthening); `phase-space-coordinate-check` (A46 — the winding claim is read in PHASE-SPACE: w_pol = Park-along-contours = the LC-quadrature winding `arg((ω·d̂)+i(π_ω·d̂))` around the minor circle ψ; the extractor floor r≥3 cells; the DEPOSIT is derived in MATCHING coordinates §3); `ave-representation-capability-check v1.1` incl. (C) conservation-by-channel + the carrier/engine DOF-capability lens (the deposit must have the WINDING-CAPABLE structure — a poloidal-phased pattern on the shell, NOT a rigid mode, NOT a random stir — §3.3); `ave-conserved-vs-pumped` (the deposit DEPLETES the photon and lands in a passive sink — never pumps standing-V; §2.3); `ave-driver-script-honesty` (every number in the result phase must come FROM the evolved field / the dumped JSON — the accumulator is logged but is NOT the headline); `verify-before-cite` (every v6 anchor below grep/JSON/line-confirmed this session — §0); `flag-don't-fix` (the AM-conservation reconciliation §2.4 and the §10 net-field/accumulator gap are SURFACED, not silently resolved); `ave-prereg v1.1` (the Step-3.5 dimensional subsection §3.5 is mandatory — the survival gate is a magnitude claim).

---

## 0. INHERITED VERDICTS (from the v6 DEMOTED-PARTIAL FINAL VERDICT, recorded verbatim-class — `research/2026-06-10_genesis-v6-transducer_result.md` §10 @ `d11b0923`; verify-before-cite, every number re-confirmed against the run JSON this session)

- **NOT-ELECTRON (the v5 panel) STANDS.** v7 does NOT reopen the electron claim. It tests ONE structural hypothesis the v6 panel surfaced (and did NOT adjudicate): that helicity→winding is blocked by DEPOSIT GEOMETRY, not by a missing coupling family.
- **T1 = a CONVERGED dilatation mass (`E_V^cons ≈ 12.9`, drift 0.86 %, N- and stop-time-robust) — SURVIVES the v6 panel UNCHANGED**, attributable to the D11 pump-fix + D10 deflagration hygiene, NOT the transducer. **This is the v7 D-INHERIT regression baseline (§2.1).**
- **The v6 transducer = a LIVE, passive, helicity-odd, depleting CHIRAL BOUNDARY COUPLING whose net field deposit (∓3.6e-5, RIGID-azimuthal) is DRAINED BY THE LOCK** (`_lock_relax`, `crystal_graft_v4.py:186-226`, removes precisely the rigid-rotation mode the deposit lands in — `unified_genesis_engine.py:513-514` deposits `dpi ∝ Ω_om·(n̂×r)·g_wall`, a rigid azimuthal rotation). The headline accumulator ∓0.539 is the by-construction per-step tally, ≈4 OOM above the net field effect (DEMOTION 1).
- **The `H_bel` "charge" attribution is the BUCKLE's, not the transducer's (DEMOTION 2):** `Hbel` invariant to 6 sig-figs across `omega_recipient_frac` {0,0.5,1.0} while the deposit scaled 0→−1.8e-3; `Hbel_OFF(RH) = −0.119` = 86 % of MAIN. v7 carries this forward — the buckle's pre-existing helicity-oddness is a CONTAMINANT of any RH−LH contrast, so the clean v7 contrast is **MAIN − transducer-OFF at the SAME handedness** (the D9-increment isolation), AND the lock-ON vs lock-OFF contrast (§2.2 D14).
- **`w_pol ≡ 0` at EVERY swept point (the night's answer, panel-confirmed):** helicity did NOT become winding at the v6 architecture. The lone `w_pol=1` at the MAIN 3200-build sat AT the reliability floor (rel 0.109 vs the 0.1 gate), did NOT track the coupling, AND appeared in the achiral arm — a floor-grazing read, not a coupling-driven `(2,3)`. The poloidal "3" never formed.
- **D-PERM = MOTION-LOCKED PHYSICS (ν_art-invariant over 50×, deficit −0.0365 to 4 sig-figs, persists better WITHOUT the snap); the snap-channel = CLIP.** Both inherited unchanged; v7 does NOT re-litigate them.
- **THE STRUCTURAL-BLOCK HYPOTHESIS (panel-surfaced, NOT adjudicated — the v7 question, Rule 12, no slot refilled):** the v6 deposit geometry is rigid-azimuthal and `_lock_relax` removes precisely the rigid-rotation mode WHILE PRESERVING the local LC quadrature where the poloidal `(2,3)` lives — so helicity→winding may be **structurally blocked by deposit geometry (rigid mode → lock sink)**, not by a missing coupling family. **v7 is that discriminator and ONLY that discriminator.**

---

## 1. SUBSTRATE-NATIVE CHECKPOINTS WALKED (before the first line of v7 numerical code)

- **CP1 (dynamical, no minimization):** UNCHANGED — FDTD leapfrog (V/w/ω) + RK2 (ρ̄/u) + the helicity-conserving lock substep. No energy-basin descent. The v7 deposit is a per-step BC, not a relaxation toward a minimum.
- **CP2 / representation-capability (C) conservation-by-channel — the load-bearing check.** The ω-sector master equation is `∂_t²ω = c_ω²∇²ω − ω_0²ω + f_ω` (a massive wave; the ω-tank's LC reactance pair is `(ω, π_ω≡∂_tω)`, restoring `ω_0²`). The poloidal "3" is a winding of the LC PHASE `arg((ω·d̂)+i(π_ω·d̂))` around the minor circle — it is a property of the (C-state, L-state) QUADRATURE, not of ω alone. **The v7 deposit therefore acts on the L-state π_ω with poloidal-phased spatial structure (§3); the lock's net-L removal does NOT touch this quadrature (`_lock_relax` docstring + code, `crystal_graft_v4.py:186-204`: "removes the rigid-body rotation … leaving the local LC quadrature — hence the poloidal winding — intact").** The energy ledger is TRACKED (passive lossy mirror E_absorb ≥ 0), never assumed conservative.
- **CP9 (dynamical integration, not algebraic):** ρ̄ integrated by continuity; the bulk deficit EMERGES. Whether the planted-L-state poloidal pattern self-organizes into a quantized `(2,3)` is the open T2/WINDING-TAKES question — it must EMERGE from the LC dynamics, not be algebraically asserted (the deposit plants winding-CAPABLE L-state structure; the LC tank + buckle must complete and quantize it, or it does not).
- **CP10 (boundary, not bulk) — THE constraint that detonated every v5 bulk-coupling architecture.** The v7 deposit acts ONLY on the `_wall_window()` g_wall shell (A≈`wall_center`=R_II=√3/2, the Γ=−1 saturation front), interior-masked, applied in `step()` AFTER the inherited V/w/ω + bulk substeps — NOT a term added to any field's acceleration/EOM. No bulk trilinear potential is introduced (the indefinite-Hamiltonian pump that detonated `photon_deplete=True` cannot recur). The ONLY v7 change vs v6 is the SPATIAL SHAPE of the on-shell δπ_ω increment.

---

## 2. THE V7 DESIGN — D-INHERIT / D13 / D14 (verbatim-class from the directive; FROZEN, Rule 11; the design INTENT does not change post-run)

### 2.1 D-INHERIT — the v6 engine EXACTLY as committed at `d11b0923`

The v6 engine, unchanged: T1-converging (D10 self-limiting snap + D11 conservative vent); the lock as-is (`lock_on`, `lock_eta`, `_lock_relax`); the buckle as-is (`_buckle_forces`, director = photon w); the D9 boundary-transducer machinery as-is (extraction π_w←π_w·(1−χ̃·g_wall), the AM ledgers, the ω-recipient split). **T1 MUST REMAIN converged in every v7 arm** — the regression gate: `E_V^cons → ~12.9-class`, drift < 1 %-class. **If the new deposit breaks T1, that is a FINDING (the T1-BROKEN bin §6), not a tweak target** (Rule 11: do not debug toward a rescue).

### 2.2 D13 — THE QUADRATURE DEPOSIT (the ONE change)

The wall's extracted photon spin δL is deposited **NOT as a rigid-azimuthal δu/δπ_ω but as a POLOIDAL-PROJECTING δπ_ω on the wall shell** — structured so its Park-along-contours projection (the LC quadrature `(ω·d̂, π_ω·d̂)` read around the minor circle ψ — the SAME coordinate the extractor reads w_pol in, A46) has NONZERO POLOIDAL CONTENT (the mode the lock does NOT drain and the `(2,3)` lives in). The spatial structure is DERIVED from the poloidal contour geometry around the core (§3). Constraints, all BY CONSTRUCTION:
- **conservation exactly as v6:** extract LINEARLY from π_w (the extraction is the inherited D9 op, unchanged), deposit exactly δL — the AM ledger must close 1:1 (the deposit magnitude/sign is set by the extracted photon spin; the photon pays exactly what lands). The reconciliation of "deposit exactly δL" with "a poloidal mode the lock preserves" is the load-bearing design question §2.4, resolved by the deposit-SHAPE sweep §5 and surfaced to Grant.
- **boundary-local (CP10):** on the g_wall shell only, a post-substep BC, no bulk EOM term.
- **helicity-odd:** the deposit sign reverses RH↔LH (the extraction `s_density=(w×π_w)·n̂` is helicity-odd; achiral → structurally zero).
- **passive:** the energy removed from the photon ≥ the energy deposited; remainder is a lossy-mirror sink (E_absorb ≥ 0), H_total not increased.

**Any shape parameter of the deposit pattern is a GOVERNING KNOB: MANDATED SWEEP (§5).**

### 2.3 D14 — THE LOCK-SURVIVAL ARM (the discriminator)

**lock-ON vs lock-OFF arms measuring the NET FIELD deposit into the target (poloidal) mode.** The structural-block hypothesis predicts:
- the RIGID-mode deposit (the v6 deposit, reproduced as a CONTROL) **dies under lock-ON** (drained to the v6 −3.6e-5-class, ≈4 OOM under accumulator);
- the QUADRATURE deposit (the v7 poloidal δπ_ω) **SURVIVES lock-ON** (net field poloidal deposit NOT drained, gap to accumulator ≲ 1 OOM).
- the lock-OFF arms are the positive control that the deposit geometry CAN land content in each mode at all (isolating the lock as the drain mechanism).

**If the quadrature deposit is ALSO drained under lock-ON, FIND AND NAME the new sink (the DEPOSIT-DRAINED-AGAIN bin §6)** — that would FALSIFY the deposit-geometry hypothesis and relocate the block (candidate sinks to instrument: the `damping` array, the PML, the `ω_0²` mass-gap dispersion, the buckle f_ω back-reaction, the global I-tensor coupling in `_lock_relax` leaking the poloidal mode into net-L). Naming it is the Rule-11 honest closure, not a rescue.

### 2.4 THE ONE PLUMBER-PHYSICAL QUESTION (pre-test-physics-check; SURFACED to Grant BEFORE design, Rule 16 strengthening — flag-don't-fix)

> **A real chiral mirror torquing the angular pair per bounce — does it deposit a net SWIRL (a flywheel spin-up of the ω-tank, carrying net axial AM, what v6 did and the lock bleeds off) or a zero-net-swirl POLOIDAL RIPPLE (a standing phase-pattern around the tube cross-section, carrying the poloidal winding the lock ignores)?**
>
> The tension, stated honestly: the extracted quantity from the photon is AXIAL SPIN δL (a net-axial-AM scalar, helicity-odd). A pure poloidal-winding pattern carries ~ZERO net axial AM (the ψ-winding averages out). So enforcing BOTH "deposit exactly δL of net axial AM (1:1 AM closure, no AM created/destroyed)" AND "deposit a zero-net-axial-AM poloidal mode the lock cannot see" is OVER-CONSTRAINED — one must give. **Where does the photon's axial AM go if the deposit carries none?** This is an angular-momentum-conservation gut-check, not a knob.
>
> **The design does NOT pre-resolve it — it brackets it as the deposit-SHAPE sweep `α_pol ∈ [0,1]` (§5) and lets the discriminator + Grant adjudicate:**
> - **α_pol = 0 (S-rigid):** the v6 deposit reproduced — net axial AM = δL, fully lock-drained CONTROL.
> - **α_pol = 1 (S-poloidal / "pure ripple"):** a zero-net-axial-AM poloidal pattern, amplitude ∝ δL, sign = handedness — the photon's HELICITY (not its net axial AM) is imprinted; the axial AM is depleted into the passive sink rather than transferred as net swirl. Fully lock-surviving by construction.
> - **0 < α_pol < 1 (S-blend, AM-closing):** the poloidal-phased pattern carries net axial AM = δL via a minimal rigid component; the lock drains the rigid part (reproducing v6's drain as the built-in control) while the poloidal-phased part survives. Keeps axial-AM conservation strictly honest.
>
> **The WINDING-TAKES bin (§6) is ROBUST to this choice** — it requires w_pol ≠ 0 de novo, above floor, helicity-odd, OFF-absent, sweep-robust, REGARDLESS of which sub-design produced it. The honest flag for Grant: which of S-poloidal / S-blend is the physical chiral-mirror torque, and whether depositing a zero-net-axial-AM pattern (S-poloidal) is AM-conservation-legitimate (the axial AM going to the passive sink) or a hidden non-conservation. **Surfaced; not silently fixed.**

---

## 3. THE DEPOSIT'S SPATIAL-STRUCTURE DERIVATION PLAN (phase-space-coordinate-check A46: derived in the SAME coordinate w_pol is read in)

### 3.1 The coordinate the winding is READ in (the target — verify-before-cite, `src/ave/utils/fast_winding_extractor.py:137-176`)

The poloidal "3" is the winding of the ω-tank LC phase `arg(Z)`, `Z = (ω·d̂) + i·(π_ω·d̂)`, around the MINOR circle ψ, where:
- `φ = arctan2(y,x)` = the toroidal/major angle; `ψ = arctan2(z, ρ−R)` = the poloidal/minor angle (ρ=√(x²+y²)); the torus sits at major radius R, minor radius r around the core.
- `d̂` = the principal transverse axis from the ω covariance (`cov = OᵀO`, `eigh`, max-eigenvalue eigenvector — `extractor:162-164`); the C-state is `ω·d̂`, the L-state is `π_ω·d̂` (the INDEPENDENT reactance partner).
- `w_pol` = the amplitude-weighted unwrapped winding of `arg(Z)` as ψ goes 0→2π, modal-voted over n_walks=12 toroidal start angles, reliability gate `w_pol_rel > 0.1` (`extractor:198`); the extractor floor requires ≥16 valid contour samples and r-radius ≥ 3 cells (F0b).

**THE DEPOSIT MUST PROJECT INTO THIS COORDINATE.** The v6 rigid-azimuthal δπ_ω ∝ (n̂×r) has, by construction, a poloidal projection `π_ω·d̂` that does NOT wind in ψ (a rigid rotation is ψ-independent in the LC phase) → w_pol = 0 capability. The v7 deposit is built to wind q=3 times in ψ.

### 3.2 The winding-capable template (from the canonical planted-(2,3), verify-before-cite, `crystal_graft_v4.py:296-324 seed_omega_known_2_3` and the stand-alone twin `fast_winding_extractor.py:220-252`)

The canonical (p,q) ω-knot that the extractor reads as w_tor=p, w_pol=q:
```
β = p·φ ;  Θ = q·ψ ;  dR = cos β ;  dz = sin β ;  base = amp·env(rtube)
ω      = base·cos(Θ)   ·[ dR·cosφ , dR·sinφ , dz ]        (C-state)
ω_prev = base·cos(Θ+δ) ·[ dR·cosφ , dR·sinφ , dz ] ;  δ = ω_gap·dt   (L-state offset)
π_ω   = (ω − ω_prev)/dt  ⇒  the (C,L) pair winds Θ = q·ψ around the minor circle.
```
The **poloidal phase advance lives in `Θ = q·ψ`**; the quadrature partner is the δ=ω_gap·dt LC offset (the natural ω-tank phase advance per step). **The v7 deposit imprints this `q·ψ`-phased structure onto the L-state π_ω on the g_wall shell**, with amplitude set by the extracted δL (the 1:1 ledger) and sign set by the photon handedness (helicity-odd).

### 3.3 The deposit (representation-capability (C): winding-CAPABLE, not rigid, not random)

Plan for `δπ_ω(r)` on the g_wall shell, the ONE engine change vs v6 (`_transducer_step`, the ω-deposit branch `unified_genesis_engine.py:515-528`):
```
g_wall(r)        = the inherited Gaussian shell window (A≈wall_center, width wall_width)   [CP10, unchanged]
ψ_loc(r), φ_loc(r) = the poloidal/toroidal angles about the core's torus axis (R from the pocket geometry)
δπ_ω(r) = A_dep · g_wall(r) · [ (1−α_pol)·(n̂×r̂)               # rigid component (carries net axial AM)
                              + α_pol · ê_pol(r)·cos(q·ψ_loc + s_h·δ_φ) ]   # poloidal-phased ripple
```
where `ê_pol` = the poloidal unit director (tangent to the minor circle, in the d̂-plane), `s_h = ±1` = the photon handedness (helicity-odd sign), `q = 3` (the target poloidal winding; q is a swept structure param §5), `α_pol ∈ [0,1]` = the deposit-SHAPE knob (§2.4 / §5), and `A_dep` fixed by the 1:1 AM-ledger closure exactly as v6 (`A_dep` is the v6 Ω-amplitude analog; the photon pays `pay_scale·extract_frac` of π_w so S_photon_removed ≡ L_transferred by construction — `unified_genesis_engine.py:536-546`). **The torus geometry (R, the core axis, ψ_loc/φ_loc) is read FROM the planted-pocket field at deposit time** (the saturated seed defines the major radius; the g_wall shell defines the minor-circle locus) — derived from the field, not hand-set (ave-driver-script-honesty / CP9).

**Representation-capability (C) keeper (§9, the PROBE-CAPABILITY plant-at-scale gate):** the v7 deposit pattern δπ_ω at α_pol=1, planted ONCE into a clean ω field at the run's own scale (N, R, r) and read by `extract_2_3_omega_fast`, MUST return `w_pol = q` (the designed winding) with rel > 0.1. A deposit that cannot produce its own designed read is DISQUALIFIED (the WINDING-TAKES verdict is CLIP — the deposit is not winding-capable). This is the v7 analog of the v6 F-PROBE m-even keeper. **The plant-at-scale gate runs BEFORE the de-novo read** (the de-novo w_pol is only credible once the extractor is shown known-positive at the run's own scale).

### 3.4 Why the lock should preserve it (the structural-block mechanism, made explicit)

`_lock_relax` (`crystal_graft_v4.py:207-226`) computes the SINGLE global net angular momentum `L = Σ r×π_ω` over the interior, solves the rigid `Ω = I⁻¹L`, and subtracts `η·(Ω×r)` — contracting `L_ω ← (1−η)L_ω` exactly while leaving any zero-net-L pattern untouched. The α_pol=1 poloidal ripple `ê_pol·cos(q·ψ)` integrates to ~zero net axial AM over the shell (the q·ψ winding cancels) ⇒ the lock's `Ω` is ~unchanged by it ⇒ it is NOT drained. The α_pol=0 rigid component is exactly `Ω×r` ⇒ fully drained at rate η/step (the v6 behavior). **D14 measures which prediction holds; DEPOSIT-DRAINED-AGAIN (§6) is the honest exit if the poloidal ripple is drained anyway (the global I-tensor solve could couple a nonzero residual net-L of the ripple back into the drain — instrument it).**

### 3.5 EXPLICIT DIMENSIONAL ANALYSIS (ave-prereg v1.1 Step-3.5 — MANDATORY: the survival gate §10 is a magnitude claim)

**Dimensional ingredients (canonical, probed live from the assembled engine `UnifiedGenesisEngine(N, bulk_density_on=True, omega_sector_on=True, buckle_on=True)` this session — NOT round-number estimates):**

| primitive | symbol | canonical value | role |
|---|---|---|---|
| node spacing | `dx` = ℓ_node | **1.0** | lattice unit |
| CFL timestep | `dt` | **1.732e-3** (= 0.30·dx/(c_eff,max·√3), assembled bulk config) | integrator step |
| bulk speed | `c0` = c_L | **1.0** | longitudinal |
| shear/ω speed | `c_T`=`c_ω` | **0.5477** (= √(3/10)) | transverse / micro-rotation |
| ω-tank mass-gap | `ω_0` = `omega_gap` | **1.0** | LC restoring frequency |
| converter coupling | `κ̃` = `kappa_tilde` | **1.2** (= 6/5 = pq/(p+q)) | buckle strength |
| lock fraction | `η` = `lock_eta` | **0.08** | per-step rigid-rotation removal |
| wall shell center | `R_II` = `wall_center` | **0.866** (= √3/2, the Γ=−1 front, A-amplitude units) | g_wall locus |
| wall shell width | `wall_width` | **0.12** (A-units) | shell sharpness |
| extraction fraction | `χ̃` = `chi_exch` | **0.02** (default; swept {0,9e-4,…,0.08}) | per-step wall spin-extraction |

**(1) The LC quadrature completes within the build window (the deposit CAN become a quadrature winding):** the ω-tank LC phase advances `δ = ω_0·dt = 1.0·1.732e-3 = 1.732e-3 rad/step`. A quarter-period (L-state→C-state rotation, needed to turn a planted L-state poloidal pattern into a full `arg(Z)` quadrature winding) is `(π/2)/δ ≈ 907 steps` ⟪ `n_build = 3200` (and ⟪ the full 4400-step window). **CONCLUSION: dimensionally, the LC tank has ~3.5 quarter-periods to rotate the planted poloidal L-state into a read-able quadrature winding before persistence begins.** (Falsifier: if w_pol only ever reads the planted L-state and never the rotated quadrature, the LC rotation is being suppressed — instrument ω·d̂ growth vs π_ω·d̂.)

**(2) The lock-drain dimensional argument (WHY v6's net field was −3.6e-5, ≈4 OOM under accumulator):** the lock removes fraction η=0.08 of the net-L (rigid) mode PER STEP. A rigid deposit added at rate `δl/step` and drained at `η/step` reaches steady state `L_ss ≈ δl/η`, NOT the accumulated `Σδl`. With the v6 accumulator |L_transferred_ω| ≈ 0.539 over ≈3200 transduce events ⇒ `δl ≈ 1.68e-4/step` ⇒ `L_ss ≈ 1.68e-4/0.08 ≈ 2.1e-3` (and the measured net field ω-axial was even smaller, −3.6e-5, the residual after the u_adv split + interior masking). **The accumulator/net-field gap ≈ 0.539/3.6e-5 ≈ 1.5e4 ≈ 4 OOM is the `(N_steps·η)`-class drain-suppression — dimensionally the signature of a deposit landing in the η-drained rigid mode.**

**(3) The v7 survival prediction (the magnitude the gate §10 freezes):** the α_pol=1 poloidal ripple carries ~zero net axial AM ⇒ it is NOT subject to the η/step drain ⇒ its net field deposit accumulates against only the OTHER sinks (`damping` ~1−ε/step, PML edge loss, ω_0² dispersion) which are 2–3 OOM weaker per step than η. **Frozen prediction: the v7 poloidal net field deposit's gap to its OWN accumulator is ≲ 1 OOM** (vs v6's 4 OOM) — that 3-OOM improvement IS the structural-block discriminator. If instead the v7 poloidal gap is also ≈4 OOM, the drain is NOT the lock (DEPOSIT-DRAINED-AGAIN: name the new sink, §6). **Power-counting the exponent:** net-field/accumulator ratio `~ 1/(N_steps · k_sink)` where `k_sink` = per-step fractional drain of the mode; v6 `k_sink = η = 8e-2` (lock) ⇒ ratio ~`1/(3200·8e-2)·O(1) ~ 4e-3`–`1e-4` (with masking); v7 `k_sink ≈ (1−damping)+PML ~ 1e-3`–`1e-4` (NO lock term) ⇒ ratio `~ 1/(3200·1e-3) ~ 0.3` to `~1/(3200·1e-2)~0.03` ⇒ **gap 0.5–1.5 OOM** — the ≲1 OOM survival gate. (Sanity anchor: the v6 ν_art-invariant deficit −0.0365 and the F0e L_bulk drift −0.05 % confirm the non-lock sinks operate at the 1e-3–1e-4/step level claimed here — the assembled-config known-null drift.)

**(4) Cross-check against the canonical empirical anchor:** the inherited v6 figure plots the FIELD `L_ω,axial` (not the accumulator) at −3.6e-5; the F-EXCHANGE structural floor is 5.3e-18; v6's net field sat ~7e12× above floor. The v7 poloidal net field at the ≲1-OOM gate would be O(0.1·accumulator) ~ O(1e-2)–O(1e-1) (accumulator scales as the v6 ∓0.539-class) ⇒ ~12–13 OOM above F-EXCHANGE — comfortably above floor, so the SURVIVAL question is decidable, not floor-limited. The magnitude is NOT the headline (gross-vs-field §10): the headline is the GAP and the w_pol read.

---

## 4. FLOORS (ORDERED BINS — floor-check FIRST, gates every positive; ave-apparatus-floor-attribution v1.1; the floors are RE-MEASURED at the v7 run config by their own known-null run BEFORE any binning — a floor carried over from a different config is invalid)

- **F-T1 (the D-INHERIT regression gate — evaluated FIRST of all).** The inherited converged mass `E_V^cons ≈ 12.9`, drift < 1 %-class, N-robust, stop-time-robust. **GATE: every v7 arm must keep T1 converged; an arm that breaks T1 is binned T1-BROKEN (§6), and its winding/survival reads are VOID (a winding on a detonating object carries no weight — the v5/v6 caveat).**
- **F-WPOL (the extractor floor + known-positive — gates every WINDING-TAKES read).** (a) the structural floor: `w_pol_rel > 0.1` AND r-radius ≥ 3 cells AND ≥16 valid contour samples (`fast_winding_extractor.py:53-58,198`; F0b). (b) the KNOWN-POSITIVE plant-at-scale gate (§3.3 keeper): the extractor returns `w_pol = q` on the v7 deposit pattern planted at the run's OWN scale BEFORE the de-novo read; a de-novo w_pol read on an extractor not shown known-positive at scale is UNRESOLVED.
- **F-NETFIELD (the GROSS-VS-FIELD floor — gates every DEPOSIT-SURVIVES read; the v6 panel lesson, structural §10).** The net field deposit into the target mode = MAIN − transducer-OFF at the SAME handedness (the D9-increment isolation, NOT RH−LH which the buckle contaminates — DEMOTION 2). The floor = the transducer-OFF run's residual in the same channel (the buckle/seed background + numeric). **GATE: the net field poloidal deposit must clear F-NETFIELD AND its gap to the accumulator must be ≲ 1 OOM (the survival gate) — else DEPOSIT-DRAINED-AGAIN.** The accumulator is logged but is NEVER the headline.
- **F-EXCHANGE (the transducer known-null).** The `chi_exch=0` (transducer-OFF) run's |deposit| (= structural zero + numeric noise; v6: 5.3e-18). Every positive deposit is gated on ≥ 100× F-EXCHANGE.
- **F-DRIFT (the free-spin baseline).** The `chi_exch=0` run's |ΔS_φ| over the window (photon axial-spin drift from propagation/dispersion/PML alone). A photon-depletion claim must show |ΔS_φ(on)| > F-DRIFT with the depletion sign.
- **F-ACHIRAL (the helicity-odd structural null).** The `helicity=0` (linear-pol) arm's transducer deposit ≡ 0 (the extraction `s_density` is structurally zero for an achiral photon). Re-confirmed, not re-measured. (Note the inherited BUCKLE sources ω for an achiral drive on its own — that contaminant is the transducer-OFF background, isolated by the MAIN−OFF contrast, not a transducer pump; the §0 DEMOTION-2 / v6 §8-flag-1 carry-forward.)
- **F-CLOSE (the D11 pump pre-gate, inherited).** The MAIN-config drive-off `H_total^cons` must show NO positive excursion above F-CLOSE (re-measured at the v7 config); else the genesis arm does NOT run (honest block).

---

## 5. THE MANDATED-SWEEP LIST (§210-COMPLIANCE GATE — every knob the bins depend on, EXPLICITLY ENUMERATED; FROZEN. The run executes EVERY sweep, OR states the deviation explicitly BEFORE running and re-bins. A positive whose governing knob was unswept is CLIP by this prereg's own law.)

**The v7-specific sweeps (the deposit-geometry knobs — the new physics):**

| # | knob | swept grid | which bin it gates | CLIP / falsifier telltale |
|---|---|---|---|---|
| 1 | **deposit shape** `α_pol` (rigid↔poloidal mix; §2.4) | {0 (=v6 rigid CONTROL), 0.25, 0.5, 0.75, 1.0 (pure poloidal)} | WINDING-TAKES vs DEPOSIT-SURVIVES; the whole v7 thesis | the survival/winding verdict tracks α_pol AS EXPECTED (this IS the control axis) — but w_pol≠0 must appear at α_pol>0 and be ABSENT at α_pol=0 (the v6 rigid control); a w_pol that appears at α_pol=0 is a floor-grazer, not the deposit |
| 2 | **lock** `lock_on` (D14 discriminator) | {ON (default), OFF} × {α_pol=0, α_pol=1} | DEPOSIT-SURVIVES vs DEPOSIT-DRAINED-AGAIN | the net field poloidal deposit dies under lock-ON at α_pol=1 (⇒ DEPOSIT-DRAINED-AGAIN, name the sink) while the rigid α_pol=0 dies as the v6 control (expected) |
| 3 | **deposit winding** `q_dep` (target poloidal order) | {2, 3 (default, the "3"), 4} | WINDING-TAKES (de-novo w_pol must track the DESIGNED q, else it is not the deposit's winding) | de-novo w_pol does NOT track q_dep ⇒ the read is not reading the deposit's structure (floor-grazer / geometric) |
| 4 | **extraction** `chi_exch` (χ̃) | {0, 9e-4 (κ̃-anchored), 0.005, 0.02 (default), 0.08} | the coupling magnitude; the net-field ∝ structure | the VERDICT (sign/oddness/null/winding) tracks χ̃ magnitude — it must NOT; only the deposit MAGNITUDE may scale (the §210 invariance) |
| 5 | **lock fraction** `lock_eta` (η) | {0, 0.05, 0.08 (default), 0.12} | the drain rate of the rigid mode (T3 spin η-invariance carried in too) | the SURVIVAL of the poloidal deposit tracks η (it must NOT if it is genuinely zero-net-L — a tracking ⇒ the ripple leaks net-L into the drain, a DEPOSIT-DRAINED-AGAIN mechanism) |
| 6 | **ω-routing** `omega_recipient_frac` (f_ω) | {0, 0.5, 1.0} | how much extracted δL routes to the ω carrier (where the winding can live) vs u_adv | w_pol≡0 across f_ω (as v6) ⇒ the residual is robust to ω-wiring strength up to 100 % |
| 7 | **shell sharpness** `wall_width` | {0.06, 0.12 (default), 0.20} | the deposit-locus geometry (does the poloidal projection survive a blurrier shell) | sign/oddness/winding tracks shell sharpness |

**The inherited regression / attribution sweeps (carried from v6 §7.6 so the D-INHERIT gate and the apparatus attribution stay §210-clean):**

| # | knob | swept grid | gates | CLIP telltale |
|---|---|---|---|---|
| 8 | **`N` resolution** | {40, 48 (primary), 56} (budget §12) | T1 / winding read (the under-resolved torus) | the T1 or w_pol verdict tracks N |
| 9 | **K3 stop-time** `n_build`/`n_persist` | build {2400, 3200, 4000}; persist {300, 600, 1200} | T1 convergence + whether the LC quadrature has rotated (the §3.5(1) 907-step argument) | the "converged" mass or the w_pol read tracks when the run STOPS |
| 10 | **`ν_art`** artificial viscosity | {1e-4, 5e-4, 1e-3, 2e-3, 5e-3} (50× span) | D-PERM / the F0e known-null drift floor used in §3.5(3) | the persistence/drift tracks ν_art ⇒ apparatus |
| 11 | **K4 seed `frac`** (saturation depth) | {0.30, 0.60, 0.85 (default), 0.95} | the regime gate (a winding only at shallow frac = sub-saturation artifact) | w_pol≠0 ONLY at shallow frac |

**§210 DEVIATION POLICY (the v5/v6 lesson, structural):** the per-bounce metric is degenerate at the CFL dt (continuous spin-drain, not ballistic bounces — the v6 honest deviation); the v7 headline is the CUMULATIVE net field deposit into the poloidal mode and the de-novo w_pol, NOT a per-bounce count. Any further deviation is stated BEFORE the run and re-binned.

---

## 6. THE FROZEN BINS (ORDERED, floors first; Rule 11 — no post-hoc criterion drop, no debugging toward a rescue, no dropping an adjudication criterion to convert ❌→✅)

**The floor gate (evaluated FIRST, before any positive bin): F-T1 (D-INHERIT regression) → F-WPOL (extractor floor + known-positive at scale) → F-NETFIELD (gross-vs-field, MAIN−OFF same-handedness) → F-EXCHANGE / F-DRIFT / F-ACHIRAL / F-CLOSE.** A signal below its own calibrated floor → UNRESOLVED. A positive that TRACKS a §5 knob (other than the designed control axes α_pol / q_dep / magnitude) → CLIP, named by the knob.

- **WINDING-TAKES** iff ALL: **w_pol ≠ 0 DE NOVO** (the de-novo read on the assembled object, NOT a planted seed) AND above the extractor floor (F-WPOL: rel > 0.1, r ≥ 3, known-positive-calibrated at scale) AND **helicity-odd across RH/LH** (w_pol sign or the chiral-twin signature reverses) AND **ABSENT in transducer-OFF** (and absent at α_pol=0, the v6 rigid control) AND **robust across the mandated sweeps** (tracks q_dep as designed, appears at α_pol>0, invariant in sign/oddness across χ̃ / wall_width / N / frac). → run the FULL spec sheet on the product (§8).
- **DEPOSIT-SURVIVES-NO-QUANTIZATION** iff: the net field LC-quadrature (poloidal) deposit SURVIVES lock-ON above F-NETFIELD with gap-to-accumulator ≲ 1 OOM (the structural-block hypothesis CONFIRMED — the deposit geometry was the block), BUT **w_pol stays 0** (the winding does not QUANTIZE — the deposit lands poloidal content but the LC tank + buckle do not self-organize it into an integer `(2,3)`). → localize WHAT CLOSURE IS MISSING (candidate: the quantization needs the buckle's nonlinear lock-in, or a second `(p,φ)` toroidal phase the deposit does not supply, or a topological threshold in amplitude/time — name the missing closure, A44 refined; do NOT auto-draft an Ax-5, the diagnosis is engine-coupling-family).
- **DEPOSIT-DRAINED-AGAIN** iff: the net field poloidal deposit is ALSO drained under lock-ON (gap-to-accumulator ≈ v6's 4 OOM) → **the deposit-geometry hypothesis is FALSIFIED; FIND AND NAME the new sink** (instrument: lock global-I-tensor net-L leakage of the ripple, `damping`, PML, ω_0² dispersion, buckle f_ω back-reaction — §2.3). A clean falsification with a named relocated block is the discipline at full strength (Rule 11); the v7 branch closes on the named sink.
- **T1-BROKEN** iff: the deposit destabilizes the inherited converged mass (F-T1 fails — `E_V^cons` detonates / still-rising / tracks seed amplitude) → an HONEST regression finding (the poloidal deposit is not passive in the full assembly despite the boundary-locality + E_absorb≥0 construction — surface the conservation leak, do NOT tune α_pol to rescue T1). Its winding reads are VOID.
- **UNRESOLVED**: anything else (above a floor but not separable into physics-vs-knob; a probe that fails its known-positive/known-null keeper; the net-field/accumulator gap indeterminate between the ≲1-OOM and 4-OOM regimes; floors not cleared).

---

## 7. FAIL-FAST ASSERTIONS (D12 class — cheap, early; run BEFORE the full matrix; do not burn the full run on a dead coupling)

1. **D12(i) — handedness alive:** after the deposit is enabled (MAIN, α_pol=1), RH-drive and LH-drive must NOT be byte-identical within **200 steps** in the ω/π_ω channel — else the deposit is DEAD: ABORT, report (TRANSDUCER-DEAD class).
2. **D12(ii) — achiral null:** the `helicity=0` arm's transducer deposit ≡ 0 (F-ACHIRAL) within the same window (the structural known-null; the buckle background is isolated by MAIN−OFF, §4).
3. **D12(iii) — transducer-OFF null:** with `transducer_on=False`, the deposit channel ledgers stay exactly 0 and the ω-deposit field is unsourced by D9 (the inherited byte-identical path — the D-INHERIT keeper).
4. **D12(iv) — RH≠LH winding sign within 200 steps:** if a w_pol forms, its handedness signature must NOT be byte-identical RH vs LH (a helicity-EVEN "winding" is geometric — the v6 GEOMETRIC false-positive lesson).
5. **F-WPOL known-positive plant-at-scale (the de-novo gate):** the extractor must read `w_pol = q_dep` on the deposit pattern planted at the run's own scale BEFORE the de-novo read is trusted (§3.3) — a de-novo read on an uncalibrated extractor is UNRESOLVED.
6. **F-T1 fail-fast:** if `E_V^cons` is diverging (> 2× the v6 12.9 baseline) by the 200-step gate in any arm, flag T1-BROKEN early.

---

## 8. THE FULL-SPEC-SHEET CONDITIONAL (IF WINDING-TAKES — the complete electron acceptance test; FROZEN, Rule 11)

This section is GATED: it runs ONLY if §6 returns WINDING-TAKES. It does NOT run for DEPOSIT-SURVIVES / DEPOSIT-DRAINED-AGAIN / T1-BROKEN / UNRESOLVED (those close the v7 branch with the named mechanism — Rule 11). If WINDING-TAKES, run the FULL spec sheet on the product:

- **T2 charge — quantized + SIGNED, with the buckle SEPARATED via OFF arms.** The de-novo `(w_tor, w_pol)` integer `(2,3)` (or `(3,2)`), reliability > 0.1, r ≥ 3; sign = handedness, FLIPS RH↔LH; and the **buckle-vs-transducer separation**: the charge attribution must track the DEPOSIT (scale with α_pol / χ̃ and vanish at transducer-OFF), NOT be invariant like the v6 `H_bel` (the DEMOTION-2 contaminant) — the OFF arms isolate the transducer's own charge contribution. Phase-space Park-along-contours read (NOT lattice-Cartesian), A46.
- **T3 spin — re-tested; STATE WHAT THE LOCK DOES IN v7.** The v6 lock DRAINED the carrier mode (rigid); IF the v7 deposit is the lock-surviving poloidal mode, the lock NO LONGER needs to drain the carrier to stabilize — so the v7 T3 must STATE explicitly what `_lock_relax` now does to the winding-bearing mode (does the locked `L_ω` still track `lock_eta`, the v6 CLIP — or is the spin now in the η-invariant poloidal quadrature?). Report the reactance pair (C-state ω, L-state π_ω) every step (F0c) + CP5 local-clock `A²_local`.
- **T5 chiral twin — SHARPENED.** The counter-rotating partner / pocket-split asymmetry PRESENT in MAIN & C-LH, FLIPS sign RH↔LH, ABSENT/symmetric in C-achiral (the m-even keeper); separated into the charge-ledger sign-flip vs a genuine spatial vorticity twin (the v6 split: chiral in charge, geometric in vorticity — does the v7 winding finally give a SPATIAL twin?).
- **T6 de Broglie — weight-bearing ONLY if T1 passes (which it must, D-INHERIT).** Translate the locked winding state at ≥2 momenta; `λ ∝ 1/p` (exponent −1) within fit-floor.
- **T1 is RE-AFFIRMED by D-INHERIT** (the converged mass is the inherited baseline; the spec sheet adds the winding the v6 object lacked).

**SPEC-SHEET verdict bins (inherited from v6 §7.5):** ELECTRON-CLASS (T1 + ≥4 of T2–T6 at floor, no clip-valued positive) / PARTIAL (a named residual survives) / NOT-ELECTRON (T1 fails — impossible under D-INHERIT unless the deposit broke T1 = T1-BROKEN) / VOID (a forbidden seeder, a non-null OFF, a winding below F-WPOL, an OFF not byte-identical across handedness). **A positive at a clip value is APPARATUS; a clean negative with a named mechanism is the discipline at full strength.**

---

## 9. APPARATUS / PROBE-CAPABILITY KEEPERS (ave-apparatus-floor-attribution v1.1 — every discriminating probe validated on a known-different reference + a known-positive; encoded as `src/tests/test_unified_quadrature_v7.py`, the v7 keeper file)

| keeper | known-reference | assertion |
|---|---|---|
| **K-OFF byte-identical (D-INHERIT)** | `α_pol`/`quadrature_deposit` defaults OFF | the v7 engine reproduces the v6 path bit-for-bit (the `test_unified_transducer_v6.py` 10/10 + snap ladder stay green); no v7 knob perturbs the inherited dynamics when off |
| **K-PLANT-AT-SCALE (the de-novo gate, F-WPOL known-positive)** | the v7 deposit pattern δπ_ω(α_pol=1, q_dep) planted ONCE into a clean ω field at the run scale | `extract_2_3_omega_fast` returns `w_pol = q_dep`, rel > 0.1 — the deposit IS winding-capable in the read coordinate (else WINDING-TAKES is CLIP) |
| **K-RIGID-NULL (representation-capability contrast)** | the deposit at α_pol=0 (pure rigid) planted at scale | the extractor returns `w_pol = 0` on the rigid pattern — proving the read DISTINGUISHES poloidal from rigid (the v6 rigid mode is correctly read as non-winding) |
| **K-HELICITY-ODD (m-even keeper)** | a fresh RH vs LH vs achiral deposit, 200 steps | the deposit reverses sign RH↔LH and is exactly 0 achiral (the helicity-odd extraction is from the field, not dialed) |
| **K-AM-LEDGER (conservation-by-channel)** | the run's own ledger | `S_photon_removed ≡ L_transferred` to 1e-9; `E_absorbed ≥ 0` (passive); H_total not increased (the D11 discipline on the v7 deposit) |
| **K-LOCK-PRESERVES (the D14 mechanism keeper)** | the α_pol=1 poloidal pattern planted, then ONE `_lock_relax` substep | the poloidal-mode amplitude is preserved (the lock's net-L removal does NOT contract it), while a planted rigid `Ω×r` pattern contracts by exactly `(1−η)` — the structural-block mechanism is real at the substep level (else the survival prediction §3.4 is wrong before the full run) |

**The keepers run + pass BEFORE the matrix.** A probe that fails its known-positive/known-null keeper DISQUALIFIES the corresponding verdict (CLIP), per the m-even lesson.

---

## 10. THE GROSS-VS-FIELD RULE — STRUCTURAL (the v6 panel lesson, binding on every v7 transducer-effect claim)

**A deposit ACCUMULATOR is never a measurement.** The engine logs `L_transferred_omega` (the by-construction per-step deposit tally) — this is BOOKKEEPING, used ONLY to compute the gap-to-net-field, NEVER as a headline. **Every transducer-effect claim is the NET FIELD quantity (MAIN − transducer-OFF at the SAME handedness), measured ON the field, above its floor (F-NETFIELD).**

- **The v6 numbers to beat (explicit, verify-before-cite §0):** v6 net field ω-axial deposit = **−3.6e-5** (≈4 OOM under its accumulator ∓0.539; LOCK-DRAINED, rigid-azimuthal). The accumulator's odd-fraction 1.000 and the 1:1 AM ledger were bookkeeping identities, not field measurements.
- **v7's survival gate (D14, the headline test):** the net field deposit into the **poloidal target mode** is NOT drained — **gap to accumulator ≲ 1 OOM** (the §3.5(3) power-counting prediction), OR the drain is explicitly measured and bounded (the gap quantified and the sink named). The poloidal "net field" is measured in the matching coordinate (the LC-quadrature amplitude `|Z| = |(ω·d̂)+i(π_ω·d̂)|` poloidal content, MAIN−OFF) AND as the de-novo w_pol read — NOT a lattice-Cartesian L_ω,axial (A46; the axial AM is the WRONG coordinate for a poloidal-winding claim, that was the v6 mode).
- **The headline sentence the result MUST be able to write:** "the v7 poloidal net field deposit is X above floor with gap Y OOM to its accumulator" — with X the field number and Y the survival metric, NOT the accumulator.

---

## 11. CORPUS STATE + ADJUDICATION DISCIPLINE

- **OPEN.** v7 does NOT promote any candidate-claim and does NOT reopen NOT-ELECTRON (the v5 panel) — it tests ONE structural hypothesis (deposit-geometry block) the v6 panel surfaced and did not adjudicate. T1 is inherited (D-INHERIT), not re-claimed.
- **Rule 11 (honest closure):** the bins (§6) are frozen pre-run; floor-checks gate every positive; a clip-valued positive is APPARATUS; DEPOSIT-DRAINED-AGAIN / DEPOSIT-SURVIVES-NO-QUANTIZATION with a NAMED mechanism is the discipline working, not a failure. No post-hoc criterion drop, no debugging toward a rescue, no tuning α_pol to save T1.
- **Rule 12 (substitution-not-retraction):** v7 is the structural-block hypothesis's OWN chain — a NEW version number with its own verification chain (this prereg + the run result). It does NOT refill the v6 slot; the v6 DEMOTED-PARTIAL record + the v5 NOT-ELECTRON / SNAP-LOCKED 🔴 demotions stand unchanged. A v7 WINDING-TAKES (should it survive) is a NEW positive with its own tracked entry.
- **Lane discipline:** the auditor lands any manual / manuscript / `COLLABORATION_NOTES` entry; this prereg + the run result SURFACE the empirical finding only. Do NOT draft the auditor's manual; do NOT draft Ax-5 candidates (the diagnosis is engine-coupling-family / deposit-geometry, A44, NOT a missing axiom). The §2.4 plumber-physical AM-conservation question is surfaced to Grant (the framing source of truth), not self-resolved.

---

## 12. SCALE / BUDGET (the N³ cost law governs; N frozen at 48 primary)

Inheriting the v6 cost model (verified live, v6 §7.9): `~9.4e-8·N³ s/step`; at N=48 ≈ 10.4 ms/step, ≈46 s per full 4400-step arm, ~20 MB/engine. The `genesis_parallel_runner.py` (ProcessPool, ~5× effective, `serial==parallel` bit-identical) fans the matrix; `fast_winding_extractor.py` (25.8×, float64-mandatory) accelerates the de-novo + plant-at-scale w_pol reads.

The v7 mandated matrix: the core deposit-geometry arms (α_pol 5 × lock 2 × handedness {RH,LH,achiral} ≈ 30 build-equivalents for the discriminator) + the inherited regression/attribution sweeps (q_dep 3, χ̃ 5, lock_eta 4, f_ω 3, wall_width 3, N 3, K3 9, ν_art 5, frac 4) ≈ **~70 build-equivalents**. At N=48: ~70 × 46 s ≈ 3220 s serial / 5× ≈ **~11 min wall**; at N=56 ≈ 18 min — within a single-session budget.

**FROZEN: N=48 primary** (the disciplined "largest N the budget allows that keeps the inherited N=40 keepers within one resolution step"); the K2 sweep {40, 48, 56} brackets the headline so any N-tracking is binned CLIP. **EXCLUDED (honesty):** f32 dtype — physically forbidden (the conservation canaries operate at 1e-3, the winding gate needs 1e-12; f32 desyncs the ledger and misses the extractor equivalence gate). The BINDING constraint is NOT budget — it is the hard floor-recalibration + keeper-revalidation rule (§4, §9), which N=48 keeps cheap.

---

*Prereg committed ALONE (this commit) before any v7 engine line or run artifact. The deposit derivation §3 is a PLAN; the engine change (the `_transducer_step` ω-deposit branch §3.3) is built + smoke-gated in a SEPARATE Phase-2 commit. Skills fired recorded in the front matter. verify-before-cite: every v6/engine anchor grep/line/JSON-confirmed this session.*
