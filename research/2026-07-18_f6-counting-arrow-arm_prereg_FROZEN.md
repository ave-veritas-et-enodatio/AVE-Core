# F6 counting-arrow arm — recurrence-sweep — prereg FROZEN

**Date:** 2026-07-18
**Charters (frozen taxonomy consumed, not redefined):**
[`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md) §4 bins + §5b gate;
[`2026-07-16_f6-circuit-map-fill-PROTOCOL.md`](2026-07-16_f6-circuit-map-fill-PROTOCOL.md) (§5b fill rule);
[`2026-07-16_f6-bath-meter_CHARTER.md`](2026-07-16_f6-bath-meter_CHARTER.md) §A/§B + §B-post-review addendum (the meter certificate + ★SCOPE CAVEAT R-1).
**Ruling:** `_orchestration/2026-07-10_rulings-docket.md` RULING 19 (tare rule) + ENTRY 17 (this arm opened).
**License under test:** [`manuscript/ave-kb/common/retention-transition-split.md`](../manuscript/ave-kb/common/retention-transition-split.md) — the *TRANSITION* crossing-arrow, "licensed **only** from counting … mode-spread with reconvergence ≈ 0 … never a valve."
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler`) — **byte-untouched**. §5b probe: `src/scripts/vol_1_foundations/f6_counting_arrow_probe.py`.
**Class:** prereg — **freeze-by-push BEFORE any driver exists** (ave-prereg Step 3.11). Grant ratified in-chat 2026-07-17/18: Q1 = the ladder (Phase-1 sub-yield first); Q2 = sparse-vs-dense recurrence sweep as the kill-shape; 377-Ω framing adjudicated FORM-derived / VALUE-instrument-calibrated.

> ★ **FROZEN.** §0–§7 locked before any RESULT. No retune after fire (Rule 11); deviations from this prereg are **findings**, disclosed. R_return(x) was **NOT** measured before this freeze — the prediction is derived from recurrence physics, not fitted.

---

## §0 Sector header + MODE / REGIME / PHASE-STATE (mandatory before any substrate claim)

- **Sector:** **E-sector ε-store** — the reactive lattice field energy that is the F6 ε→T2 transfer candidate. **NOT** A1 dilatation-mass, **NOT** Cosserat (2,3) winding/charge. The bath is a **T2 dissipation-sink DOF** (external oscillator comb), carrying no winding and no mass; sector-ownership respected (bath does not confine/hold charge).
- **Mode:** classical reactive TLM lattice (K4, z=3 srs, 4 ports) coupled to an **external Foster comb bank** (Caldeira–Leggett independent-oscillator bath) via a collar port. Symmetric-leapfrog integrator (the meter's `LatticeBathCoupler.step`).
- **Regime:** **Regime I sub-yield (Phase 1)** — cold, `A_max ≈ 0.10` (`A² ≈ 2.5e-3 ≪ 2α = 1.46e-2`; measured §5b). Op14 saturation carried only weakly through op3's bond Γ(A) (second-order at this amplitude); no `|Γ|→1` yield wall; no memristive hysteresis (`use_memristive_saturation=False`); no node mint. **Phase 2 (near-knee A≈0.5) is a SEPARATE fire**, gated on Phase-1 banking (see §3), within the W-certified band `A ≤ 0.5`, and is **not run in this lane**.
- **Phase-state:** driven-then-source-off in a **closed cavity** (`pml_thickness=0`, energy-conserving); the scaled broadband seed is the drive impulse, the source is off for the whole recording window.
- **Plant scope (★cite the caveat):** the plant is a **STANDALONE-K4** lattice — **within the meter certificate** (`2026-07-16_f6-bath-meter_CHARTER.md` §B-post-review addendum **R-1 ★SCOPE CAVEAT**: the certificate is scoped to standalone-K4 plants; energy conservation is an **algebraic identity** on this junction, not an empirical outcome). No `CoupledK4Cosserat`, no ε→T2 depletion primitive is introduced here (either would break the identity ⇒ W-battery re-validation per the caveat). This arm consumes the meter **as certified**.
- **CHANNEL-BOUNDED alignment (cite #721 R-1):** the door charter's **CHANNEL-BOUNDED** bin is *defined* energy-conserving, so the identity-enforced ledger of the standalone-K4 plant is **consistent with** (not a blocker for) the counting-arrow design — the caveat is about *which plant the certificate covers*, not the arm's target (R-1 alignment note, verbatim-close).
- **Coordinate discipline (A46 / phase-space-coordinate-check):** the corpus claim (mode-count irreversibility) lives in the bath's **modal/spectral** phase-space. The headline observable `R_return` is a **scalar energy-ledger** read (coordinate-free), and the collapse variable `x = T·Δω/2π` is a **spectral** coordinate — matched to the claim's coordinate. No real-space Cartesian φ² surrogate is compared against a phase-space prediction. `N_occ` is read per-mode over `{ω_m}` (spectral).
- **Consistency-vs-emergence tag:** the **FORM** (irreversibility born from a lossless comb; the `2π/Δω` recurrence collapse in `x`; transition at `x≈1`) is a **substrate-mechanism manifestation** of the mode-count license — Class-B/manifestation on the mechanism, **FORM-derived**. The **VALUE** of the emergent input resistance (κ-, weight-, density-set) is **Class-4 consistency / calibration** — *not* an emergence of `Z₀ = 377 Ω`. No CODATA input reaches a headline target through SI substitution; `Z₀` enters **only** the companion-leg consistency comparison (§6), tagged.

---

## §1 THE QUESTION + FORM/VALUE declaration

**The question (the only load-bearing one):**

> Does **irreversibility-by-counting** exist in this engine — does energy leaving the ε-store through a **genuinely-coupled** port fail to **RETURN** when (and only when) the **return horizon** exceeds the observation window?

The mechanism under test is the corpus's licensed one: *mode-spread with reconvergence ≈ 0 within the window* (`retention-transition-split.md:33`; tier-1 "the arrow comes from **mode-count or a click, never a valve**", `2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256`). A finite comb of `M` equally-spaced oscillators (spacing `Δω`) has an **exact Poincaré recurrence** at `T_rec = 2π/Δω` (all phases `ω_m t = ω_min t + mΔω t` re-cohere when `Δω t = 2πℤ`, independent of `M` and `ω_min`). Energy transferred out **returns** at `T_rec`. So the arrow is a **horizon-crossing**: irreversible *iff* the observation window `T_window < T_rec`, i.e. iff the comb is dense enough (small `Δω`) that the recurrence outruns the window.

**FORM/VALUE declaration (verbatim-close, frozen):** *the arm derives the **FORM** (real input resistance born from a **lossless comb** at the recurrence crossing); the **VALUE** of that resistance is **instrument-calibrated** (κ, weights, density) — this is **not** a derivation of `Z₀ = 377 Ω`; the companion leg (secondary) makes the mechanism-identity with the lattice's own characteristic impedance explicit at **consistency-class**.*

---

## §2 THE OBSERVABLE + COLLAPSE VARIABLE + frozen PREDICTION

### The ledger read (defined exactly)

Per step record `E_lat(t) = lat.total_energy()` and `E_bath(t) = bath.energy()` (both-field: `E_lat = Σ_p V_inc² + V_ref²`; `E_bath = Σ_m ½p_m² + ½ω_m²x_m²` — C-state `x_m` AND L-state `p_m`, the reactance pair). `E0 = E_lat(post-first-step)` (on-shell; bath empty ⇒ `Etot0 = E0`). Conservation `E_lat(t) + E_bath(t) = E0` is identity-enforced (#721 R-1) and is **audited** (see §4·5), so `E_lat` recovery and `E_bath` residual are the **same** ledger read tared consistently: energy back in the lattice ⇔ energy out of the bath.

- `t_peak = argmax_t E_bath(t)` (transfer-complete time; the first/global transfer peak).
- `E_bath_peak = E_bath(t_peak)` = the **transferred energy** (the return reference).
- **R_return(t)** `= 1 − E_bath(t)/E_bath_peak` for `t ≥ t_peak`, else `0` (transfer not complete ⇒ nothing has returned). Fraction of the transferred energy back in the lattice ledger.
- **Cumulative return** `R_ret_cum(t) = max_{t_peak ≤ t' ≤ t} R_return(t')` (monotone; "has the energy returned by `t`").

### THE COLLAPSE VARIABLE

> **`x = T_window · Δω / (2π) = T_window / T_rec`.**

### PREDICTION (frozen)

1. **Collapse.** All `R_ret_cum(x)` curves — swept over comb density `Δω` (§3) — **collapse onto one universal curve in `x`** (the `Δω`-dependence divides out because `T_rec = 2π/Δω` exactly).
2. **Transition at `x ≈ 1`.** Each qualifying curve crosses `R_ret_cum = 0.5` at `x_50(Δω)`, and:
   - **transition-location gate (DERIVED):** `mean(x_50) ∈ [0.7, 1.5]` (the first full recurrence is exactly at `x=1`; the cumulative-0.5 crossing may precede `1` by the partial-pre-return width `≈ x_dephase = Δω/band` and may follow `1` up to the 2nd recurrence at `x=2` if the first recurrence returns `<50%` — so `[0.7,1.5]` brackets the physically-allowed first-substantial-return window).
   - **collapse-quality metric + gate (DERIVED):** `spread(x_50) = max(x_50) − min(x_50) < 0.30`. Derivation: the only `Δω`-systematic in `x_50` is the dephasing offset `x_dephase = Δω/band` (band `≈ 0.70`), which spans `0.014 (Δω=0.01) … 0.114 (Δω=0.08)`, plus the sampling floor `≈ Δω_max/2π ≈ 0.013`; the systematic spread bound is `≈ 0.13`, and `0.30` is `≈ 2.3×` that bound — comfortably above the physical spread yet **far below** a non-collapse (a transition tracking `T_window` rather than `x` would spread `x_50` by the full `Δω` factor `8×`, i.e. `≫ 1`).
3. **Sparse end = full return (built-in positive control).** The **two-tank control** (`M=2`, §3) and the **sparsest sweep comb** (`Δω=0.08`) at `x ≫ 1` **MUST** show `R_ret_cum > 0.7` — reproducing the banked two-reservoir reversibility (`2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md`; #674). Threshold `0.7` (DERIVED): a finite comb recurs exactly ⇒ return `→ 1`; `0.7` allows for lattice-internal-mode leakage that does not recur on this timescale.
4. **Dense/short-window end pins low.** For the dense combs (`Δω ≤ 0.03`, so `x_dephase = Δω/band < 0.043 ≪ 0.3`), `R_return(x = 0.3) < 0.30` — energy has transferred (`x > x_dephase`) but not returned (`x < 1`). DERIVED: in the plateau the return fraction is `≈ 0`; `0.30` allows partial early returns.
5. **Mode-count fingerprint.** `N_occ(dense comb) > N_occ(sparse comb)` (dense combs populate more modes across the driven band), and `N_occ` at the dense end tracks the **driven bandwidth**, not the array size (the meter's M-invariance certificate).

If (1)+(2) hold and (3)+(4)+(5) hold with energy conserved and OFF recovering Ax3 → **COUNTING-ARROW** (§4). Any other pattern maps to a fail-closed bin (§4).

---

## §3 THE GRID (every value declared; frozen)

**Fixed** across the whole sweep (ENGINEERING CHOICES — tagged; inherited from the meter's frozen pins): grid `N=12³`, center `(6,6,6)`, collar `[r_in,r_out]=[2.0,4.0]`, coupling `κ=0.012`, `ω_min=0.30`, `dt=1.0`, `pml_thickness=0`, seed `SEED=1`, seed scale `0.6` (Phase-1 mild, `A_max≈0.10`), `nonlinear=True` + `op3_bond_reflection=True` + `V_SNAP=1.0`. **Drive protocol:** the scaled broadband seed (meter `_seed_lattice`) is the impulse; `E0` captured post-first-step (on-shell); source off for the whole window (free coupled evolution).

**Knob 1 — comb density `Δω`** (band top held at `ω_max ≈ 1.0`, so `M` adjusts with `Δω`; `dt` need not be reduced — `ω_max·dt < π` holds for every row):

| `Δω` | `M` | `ω_max = ω_min+(M−1)Δω` | `T_rec = 2π/Δω` (steps) | run horizon `T_max = 11·T_rec` | role |
|---|---|---|---|---|---|
| 0.010 | 71 | 1.000 | 628 | 6908 | densest (deepest irreversible) |
| 0.015 | 48 | 1.005 | 419 | 4607 | dense |
| 0.020 | 36 | 1.000 | 314 | 3455 | dense |
| 0.030 | 24 | 0.990 | 209 | 2304 | production comb |
| 0.050 | 15 | 1.000 | 126 | 1382 | sparse |
| 0.080 | 10 | 1.020 | 79 | 869 | sparsest (positive control edge) |

**Knob 2 — `T_window`.** Read off each single trajectory (one run per `Δω`, `R_ret_cum(x)` sampled every step). For the RESULT table, report `R_return` and `R_ret_cum` at the frozen window points **`x ∈ {0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0}`** (11 points over 2 decades = ≥3/decade; `T_window = x·T_rec` interpolated to the nearest recorded step). Every `Δω` run reaches `x = 11 > 10`; the densest reaches `x=0.1` at step 63 (fine sampling resolves the plateau).

**Positive control (declared separately):** **two-tank** `M=2`, `ω = {0.50, 0.70}` (`Δω=0.20`, `T_rec=31.4`), horizon `T_max = 12·T_rec = 377` steps — the cleanest sloshing reservoir (reproduces two-reservoir reversibility).

**Phase 2 (SEPARATE fire; NOT run here).** Same frozen grid + criteria at seed scale `2.9` (`A_max≈0.50`, near-knee, mid-upper Regime II), gated on Phase-1 **banking**, and carrying the **5.3% tare budget** on **any spatial read** (`2026-07-16_f6-bath-meter_CHARTER.md` §B-post-review R-4: near-knee W5 residual `0.0526`). Phase-1's headline `R_return` is a scalar ledger read (not spatial), so the tare budget gates only the §4·8 protected-core spatial check.

---

## §4 FROZEN VERDICT CLASSES (map onto the door taxonomy + arm-specific)

Rule-11: no retune after any fire; a single mechanism that explains all failures is the discipline working (honest closure). Blow-up = INSTRUMENT.

| Verdict | Door bin | Fire condition (all frozen) |
|---|---|---|
| **COUNTING-ARROW** | **CHANNEL-BOUNDED** (i) | (1) collapse holds: `spread(x_50) < 0.30`; (2) transition at `x≈1`: `mean(x_50) ∈ [0.7,1.5]`; (3) sparse-control returns: two-tank + `Δω=0.08` at `x≫1` `R_ret_cum > 0.7`; (4) dense-end pins low: `R_return(x=0.3) < 0.30` for `Δω ≤ 0.03`; (5) energy conserved `|E_lat+E_bath−E0|/E0 < 1e-3`; (6) OFF recovers Ax3 (`κ=0` closed cavity drift `< 1e-10`); (7) mode-count rises at the dense end (`N_occ` dense `>` sparse, bandwidth-tracking); (8) protected-core bias within tol **after the tare** (`|A_max^ON − c·A_max^OFF|/A_max^OFF < 0.05`, `c=√(1−E_bath/E0)`) |
| **NO-ARROW** | — | `R_ret_cum` high across ALL `x` (echo always home) — counting alone does not produce the arrow in this engine; **route to the click mechanism** (X40), do not rescue |
| **FOREIGN-EATER** | — | irreversibility at **sparse** combs, or return failure **NOT tracking `x`** (e.g. sparse control fails to return) — something else eats the echo; **INSTRUMENT-first** investigation; **fail closed** |
| **BIAS-MOVED** | (iii) | protected-core bias moves ON vs OFF beyond tol **after the tare** (criterion 8 fails) — fail closed |
| **FRICTION-RENAMED** | (vi) | energy leaves but `N_occ`/mode-count does **not** rise (criterion 7 fails) — Ax3-illegal class; fail closed |
| **NUMERICAL / DETONATE** | (ii) | NaN / energy blow-up / conservation-identity broken (`|E_lat+E_bath−E0|/E0 ≥ 1e-3`) — INSTRUMENT; fail closed |
| **NULL** | (v) | no transfer (`E_bath_peak/E0 < E_BATH_MIN = 1e-2`) — build incomplete |

Decision rule (consumed frozen from the door charter §4): **(ii)/(iii)/(vi) fail closed**; only **COUNTING-ARROW** licenses the successor gates (thermometer / spatial-F6). **NO-ARROW** and **FOREIGN-EATER** are honest negative closures, routed (click / instrument), **not** retuned.

---

## §5b Circuit map (§5b) — FROZEN

**Object:** **F6 occupancy chord** (one taxonomy object; kept separate from frontier crystallization and from the finished-A1 wall — fill-PROTOCOL Step 0). Probe: `f6_counting_arrow_probe.py` (Phase-1 mild plant, `A_max≈0.10`).

| Question | Claim | Cite | Observable / null (measured value + `probe.py:line`) |
|---|---|---|---|
| Ports | collar shell of K4 tetrahedral bond sites, all 4 ports `p0..p3` read via `mean_p(V_inc+V_ref)`; the coupling port is **collar → Foster comb bank** | `f6_bath_meter.py:make_collar_mask` + `read_q`; `k4_tlm.py` 4-port `V_inc[...,p]` | `collar_sites=56`, `ports_read=all_4_K4_bonds`, `collar_subset_of_mask_active=True`, `pml_thickness=0` (`probe.py:85`) |
| Regime | **cold sub-yield** (Regime I) | envelope-anatomy / Ax-4 kernel; `A²≪2α` | `A_max(collar)=0.0744`, `⟨A²⟩=2.47e-3 ≪ 2α=1.46e-2`, `⟨S=√(1−A²)⟩=0.99877` (`probe.py:94`) |
| Port behavior (cold baseline) | **matched pass** at the op3 bond front (cold); the `Γ`-vs-`x` **transition is the FROZEN HYPOTHESIS**, deliberately unmeasured | translation-circuit cold≈matched; op3 `z_local=(1−A²)^(−1/4)` | `z_local(collar)∈[1.00005,1.00155]` spread `1.50e-3` (~1.00 = matched, cold) (`probe.py:104`) |
| Port behavior (predicted vs `x`) | **sparse: reactive `|Γ|≈1` phase-rotating** (energy reflects back = recurrence within window); **dense: matched-line `Re(Z)` emergent** (energy stays out = counting) | recurrence identity `T_rec=2π/Δω`; §1 | *frozen prediction, tested by §2 — NOT a probe read* |
| Energy fate | **in-network reactive, reversibly exchanged with a lossless comb; total conserved** (identity, #721 R-1). Return-vs-window is the arm's observable (§2), unmeasured here | circuit-first "reflection ≠ T2 leave"; #721 R-1 identity | closed-cavity `\|ΔE_lat\|/E0=1.87e-15`; comb-on `\|Δ(E_lat+E_bath)\|/E0=2.28e-15` (`probe.py:124`) |
| A1 protection | interior reversibility protected by **losslessness** (same mechanism as the port: lossless comb + on-shell global rescale); **no `CORE_R` mask, no siphon** — reversibility is the recurrence, not a valve | Ax3 lossless interior; bias≠release | closed-cavity drift `1.9e-15` = the bias≠release control (`probe.py:130`) |
| Forbidden costumes | **not** Re(Z)-dump (`friction=False, β=0`), **not** PML sponge (`pml=0`), **not** face-`V`-scale siphon (back-reaction = global energy-matched rescale), **not** dump-R; the comb is **lossless** — any real impedance is **EMERGENT from counting** | mode-count charter §5b costume row; killed classes | `friction=False, β=0.0, pml_thickness=0` (`probe.py:136`) |

**★The no-valve rail (frozen):** **no `Re(Z)` element exists anywhere in the arm** — the comb is lossless (`bath.damp` is production-OFF), the coupling is a symplectic Caldeira–Leggett kick + exact free rotation, and the back-reaction is a phase-preserving energy-matched rescale. Any real input resistance the port sees is **EMERGENT from mode-counting** (reconvergence outrunning the window), not a dissipative primitive.

**Pre-freeze consistency pass: PASS (1)–(6) dated 2026-07-18** — cite `f6_counting_arrow_probe.py:85,94,104,124,130,136` and its printed values above. (1) object = F6 occupancy chord (exactly one). (2) regime measured cold (`A²=2.47e-3`) matches the "cold" label. (3) port behavior cold = matched (`z_local≈1.001`) matches the label; the wall/`|Γ|→1` claim is **not** made cold — it is the frozen `x`-prediction. (4) energy fate = in-network conserving (`2.28e-15`) matches "reflected/reversibly-exchanged." (5) A1 protection = losslessness, same mechanism (closed-cavity `1.9e-15`), no parallel `CORE_R` costume. (6) no killed class in the sketch (`friction=False, pml=0`, global rescale not siphon).

---

## §6 THE COMPANION LEG (SECONDARY — non-gating; clearly fenced)

**Its outcome CANNOT change the arm verdict** (§4 rests only on the primary comb-bath sweep). This leg makes the mechanism-identity with the lattice's own characteristic impedance explicit at **consistency-class**.

**The self-termination sweep.** A **local port driven INTO the lattice** (single-cell impulse at the center), using the **lattice's own modes** as the reservoir (no external comb). **Lattice-size sweep** `N ∈ {8, 10, 12, 16}`.
- Measure `Δω_lattice` = the lattice's own mode spacing (FFT of the center-cell field timeseries on a long closed run; mean spacing of the dominant spectral lines / first-revival of the field autocorrelation).
- Measure the **local return** `R_in(t)` = fraction of the injected local energy back in the **port region** (the central cell block) at `t`; the **emergent input resistance** proxy `Re(Z_in)/Z_char = 1 − max_{window} R_in` (the fraction that dispersed into the bulk and did not return within the window = the matched-line "absorption").
- **The SAME `x`-collapse:** `x = T · Δω_lattice / (2π)`; `R_in(x)` (and `Re(Z_in)(x)`) collapse across `N`, transition at `x≈1`.

**FORM observables (testable):** the `x`-collapse across `N`, and the `Re(Z_in)/Z₀` ratios vs port geometry. **Consistency target (VALUE = calibration, stated):** `Z₀ = √(L_bond/C_bond)` (the K4 bond characteristic impedance). **This is NOT a derivation of `Z₀`** — the ratio is reported at consistency-class; `Z₀` and `Δω_lattice` are instrument-calibrated. A larger `N` (finer `Δω_lattice`, longer recurrence) should make `Re(Z_in)` more clearly "born" (approach the matched `Z₀`) over a fixed `x`-window — the same counting-arrow, self-terminated.

---

## §7 Honesty flags (frozen)

1. **Window-relative irreversibility (Poincaré).** A finite comb is **reversible in principle** — the recurrence at `T_rec` always returns the energy. The arrow measured here is a **horizon-crossing** (`T_window < T_rec`), the **same epistemic status as radiation resistance** (a matched line looks resistive only until the reflection returns). This arm does **not** claim thermodynamic irreversibility in the `N,T → ∞` limit; it claims the counting-arrow **exists and collapses in `x`**.
2. **Mechanism-existence rung, NOT the rate rung.** This tests *whether* counting produces the arrow, not the depletion **rate**. `Γ = 3Hρ_latent` (the DE-tracks-matter rate) is **untouched**.
3. **Plant = standalone-K4 (certificate valid).** The meter certificate covers this plant (identity-enforced conservation, #721 R-1). **Any future ε→T2 primitive or `CoupledK4Cosserat` front BREAKS the identity ⇒ W-battery revalidation** per the §B-post-review R-1 SCOPE CAVEAT.
4. **Meter tare (RULING 19).** The back-reaction is ~90% uniform amplitude attenuation + ~10% spatial (amount-not-phase). The headline `R_return` is a **scalar energy ledger** (not spatial) ⇒ the tare does not gate it. The only spatial read (§4·8 protected-core bias) is tared by `c=√(1−E_bath/E0)` before comparison, budget = the mild W5 residual (`≈0.026`; Phase-2 near-knee = `0.053`).
5. **FORM-derives / VALUE-imports.** Consistent with the corpus meta-finding: the arm forces the **FORM** (counting-arrow, collapse, emergent Re(Z)); the **VALUE** (`Z₀=377Ω`) is calibration, made explicit only at consistency-class in the companion leg (§6).

---

*Prereg only. Nothing here banks COUNTING-ARROW; §2 predictions are derived from recurrence physics and were not measured before this freeze. The RESULT (with Rule-11 honesty on any fail) follows in `2026-07-18_f6-counting-arrow-arm_result.md`.*

---

## POST-FREEZE AMENDMENTS (dated; the §0–§7 body above is byte-untouched)

> These amendments are appended below the frozen line per the freeze rail (frozen body byte-untouched; amendments dated here). They **flag** contradictions/misfires root-caused post-fire — they do **not** edit the frozen body or retune the classifier (Rule 11).

### 2026-07-18 — AMENDMENT 1 (PR #722 review R-6): §4 FRICTION-RENAMED row REDEFINED the charter bin it claimed to consume

**Header contradiction, flagged (flag-don't-fix).** The header (above) states the taxonomy is *"frozen taxonomy **consumed, not redefined**."* But the frozen **§4 FRICTION-RENAMED row** maps *criterion-7* (`N_occ dense > sparse` — a **dense-vs-sparse fingerprint**) onto **door bin (vi)**, whereas the door charter's bin (vi) FRICTION-RENAMED (`2026-07-15_f6-mode-count-door_CHARTER.md` §4) requires **`N_occ` NOT rising from zero + dissipation (Q-drop / damping, Ax3-illegal)**. Substituting a dense-vs-sparse fingerprint for the charter's no-mode-count-rise + dissipation condition **REDEFINED bin (vi) in place** — contradicting the header's "consumed, not redefined." This misfire was **frozen-in** (present at freeze); it is **root-caused here**, not silently fixed: it is exactly why the shipped tree returned `FRICTION-RENAMED` on data where the bath **does** gain modes and returns energy reversibly (no dissipation). The frozen body is left untouched; the correct disposition (honest frozen reading = **FOREIGN-EATER**; `NULL-OF-REGIME` = routed regime-interpretation) is carried in the RESULT §4/§7 and routed to Grant.

### 2026-07-18 — AMENDMENT 2 (pointer): RESULT-doc repairs

The Phase-1 RESULT was re-banked under PR #722 review (R-1…R-10): FALSIFIED scoped to the **frozen `κ=0.012` recurrence-sweep PREDICTION** (the counting-arrow QUESTION **remains open**); `NULL-OF-REGIME` demoted from banked class to routed interpretation; regime-diagnosis numbers (`ω_d`, `n_pop`, `τ_transfer/T_rec`) given shipped provenance (RESULT §8, `…_result.json["diagnostics"]`). See `2026-07-18_f6-counting-arrow-arm_result.md`. **This prereg's frozen §0–§7 predictions are unchanged.**
