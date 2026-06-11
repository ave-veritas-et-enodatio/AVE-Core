# PREREG — S11 DE-NOVO: does the v6 MAIN *made* product (rebuilt to T1 convergence, then settled drive-off) present a characterizable resonance to its own ring-down self-spectrum and to a small-signal S11 probe — and what are its f₀ / linewidth / Q / BVD?

**Date (frozen):** 2026-06-11
**Branch:** `analysis/2026-06-11-s11-de-novo` (worktree `/tmp/ave-s11denovo`, off `origin/analysis/2026-06-10-genesis-v6-transducer` @ `7484dd0b`; do NOT push/merge — review-gated; do NOT touch `/tmp/ave-v6` or `/tmp/ave-v7`).
**Engine lineage (subclassed, inherited physics unchanged):** the *made* product is `UnifiedGenesisEngine` (`src/ave/core/unified_genesis_engine.py:67`) ← `CrystalGraftV4` (`crystal_graft_v4.py:74`) ← V3 (`crystal_graft_v3.py:55`) ← V2 (`crystal_graft_v2.py:54`) ← `CrystalEngine` (`crystal_engine.py:51`). The canonical S11 instrument is `S11Probe(CrystalGraftV2)` (`src/ave/core/s11_probe.py`, PR #166 / commit `7d11c518`).
**Governing discipline:** `ave-apparatus-floor-attribution` — the PROBE is the instrument; it is validated on a KNOWN resonator FIRST **in THIS engine config**, and the bins are ORDERED so the probe-capability floor-check GATES any f₀/Q claim about the unknown *made* state. No Q is reported for the made product until the probe has recovered a known f₀ AND known Q within tolerance.
**Skills fired at design time:** `ave-prereg` (corpus anchors §9, frozen bins §6, committed ALONE before any run artifact; dimensional Step-3.5 §7); `substrate-native-check` (CP1 dynamical-not-minimization, CP6 reactance pair, CP7 PML-excluded read, CP9 integrated-field-not-painted-Lorentzian, CP10 boundary-not-bulk — §2.1; and the **re-layer-on-a-different-engine** trigger — §3); `phase-space-coordinate-check` (the charge/winding identity is phase-space; ring-down and S11 are real-space frequency-domain observables — §2.2); `ave-apparatus-floor-attribution` (probe-capability gate + ORDERED bins, governing); `ave-representation-capability-check` (does a small-signal probe channel even COUPLE to the *made* object? — the NO-RESPONSE bin exists precisely because it may not — §6); `ave-driver-script-honesty` (every number FROM the evolved field; the Lorentzian/BVD fit reported with its residual; NO comparison to α⁻¹ unless the number genuinely emerges); `consistency-vs-emergence` (f₀/Q/BVD are MEASURED-IN-ENGINE in engine-natural α-free units — §8); `verify-before-cite` (every anchor grep-confirmed live in this worktree, §9).

---

## 0. THE NAMED QUESTION (forward-registered; Rule 11)

This prereg is the *de-novo* sibling of the #166 electron-S11 sweep. #166 characterized a **PLANTED** test article — a hand-seeded known-positive (2,3) ω-winding + a trapped bulk-V breather on `CrystalGraftV2` via `seed_omega_known_2_3` — and returned **MULTI-MODE (low-contrast dispersive), Measured-Q UNTESTED, no α⁻¹** (`research/2026-06-10_electron-s11-sweep_result.md:0`). This prereg asks the same instrument's question of the **MADE** product instead: the object that `genesis_v6_transducer_run.py`'s MAIN recipe *actually builds* — `seed_lane1(frac=0.85)` + `energize_rotation_column(M=1.8)` + `freeze_wall_window` + `drive_chiral_photon(helicity=1)` on `UnifiedGenesisEngine` (N=48), evolved to T1 (mass) convergence (N_BUILD=3200), THEN settled with the drive off.

**The named question:** rebuilt to T1 convergence and settled drive-off, does the v6 *made* object present (a) a ring-down self-spectrum with a resolvable f₀ + linewidth (its own free "song"); (b) an S11 small-signal driven resonance (net susceptibility above floor, by the #166 drive-off-subtraction method); (c) a fittable BVD/Q — **IF** a resonance exists at all? Reported **in engine-natural units, forward, before any α comparison.**

**Forward-registration (Rule 11, hard / anti-137-retrofit):** the run reports the MEASURED (f₀, linewidth, Q) FIRST. The ring-down self-spectrum (a) is acquired **un-driven** (it cannot be a driven artifact) and it **SETS the S11 band** — so the band is not a post-hoc retrofit around a pretty driven peak. Only AFTER (a)+(b)+(c) are reported, as a separate post-hoc line, is any dimensionless Q compared to α⁻¹ ≈ 137. **The α⁻¹ comparison is not an adjudication criterion for any bin.** A near-137 Q is reported with its floor, NOT headlined as α-emergence (which would require a de-novo (2,3) that the v6 panel verdict says does not exist — §1). **No debugging toward a pretty resonance.**

**Prior expectation (recorded, NOT a target):** the inherited v6 panel verdict is **NOT-ELECTRON — T1 detonates in v5; v6 builds the missing transducer primitive + fixes hygiene, and does NOT reopen the electron claim** (`research/2026-06-10_genesis-v6-transducer_prereg.md:11`, "NOT-ELECTRON (T1 detonates) — STANDS"). The made object is a *rotating-column + chiral-boundary-transducer assembly*, not a certified self-bound electron. The #166 PLANTED article — a deliberately favourable test piece — already returned only low-contrast multi-mode dispersive structure. So the honest prior for the MADE object is **NO-RESPONSE** (the near-perfect-mirror reading) **or UNRESOLVED**, with **MULTI-MODE** as the next most likely, and **RESONANCE-CHARACTERIZED** the least likely. This prereg is designed to RETURN any of those cleanly, including the near-perfect-mirror null, which is itself a datasheet entry.

---

## 1. WHY "DE-NOVO" — THE PLANTED-vs-MADE DISTINCTION (the load-bearing design axis)

| | #166 (PLANTED) | THIS prereg (MADE / de-novo) |
|---|---|---|
| engine | `CrystalGraftV2` | `UnifiedGenesisEngine` (← V4 ← V3 ← V2) |
| object origin | hand-seeded `seed_omega_known_2_3(R,r)` + planted bulk-V breather | the genesis MAIN recipe's *own* output (column + chiral-photon transducer), evolved to T1 convergence then settled drive-off |
| (2,3) winding | present BY CONSTRUCTION (planted, r=4 cells > extractor floor) | whatever the recipe makes — per the v6 verdict, a de-novo (2,3) does NOT self-assemble; `w_pol` emergence is the open §7-genesis question, NOT assumed here |
| what S11 reads | the planted article's bulk trap | the made object's bulk trap (if any) |
| outcome already known | MULTI-MODE low-contrast | **UNKNOWN — this run** |

The discriminating value of de-novo: #166 showed even a *favourably planted* article gives no clean Q. If the *made* object gives MORE structure than the planted one, that is a positive surprise to be reported honestly (not chased); if it gives LESS (NO-RESPONSE / near-perfect mirror), that confirms the made object does not host a small-signal-couplable resonator — the honest-prior datasheet entry. **The planted-vs-made comparison (§5) is run on the SAME instrument with floors either re-used or recalibrated (decided in §5), so the two are directly comparable.**

---

## 2. PHYSICAL PICTURE (substrate-native, before code)

The v6 made object is (per the recipe): a longitudinal bulk-V field held at the `c_eff` Γ=−1 acoustic wall (the dilatation added-mass, "3"-as-MASS, `crystal_graft_v2.py:16-18`); a rotating column carrying bulk circulation `Γ`/`L_bulk` (the D-PERM motion-lock — conserved circulation, `genesis-v6-transducer_prereg:14`); a micro-rotation ω carrier with a mass-gap LC tank (`omega_gap`, the "3"-as-WINDING channel); and a chiral-boundary transducer coupling photon helicity ↔ ω/bulk circulation per bounce. A resonator is characterized by (a) striking it once and listening to it ring (the free ring-down self-spectrum → f₀, linewidth), and (b) injecting a small steady sinusoid and watching how the energy is returned frequency-by-frequency (the S11 driven sweep → net susceptibility, peak, π phase swing). Q = f₀/Δf (FWHM); BVD (L_m, C_m, R_m) is the motional equivalent-circuit fit to the resonance shape.

### 2.1 substrate-native-check (walked at design time)
- **CP1 (dynamics):** both (a) and (b) are time-domain FDTD field responses — NOT eigensolves, NOT a prescribed Lorentzian. The ring-down is the free field's own decay; the driven spectrum is integrated; the Lorentzian/BVD is FIT post-hoc to the measured data.
- **CP6 (reactance pair):** the lock-in records BOTH quadratures (I = in-phase ↔ C-state, Q = quadrature ↔ L-state) every step over the read window (`s11_probe.py:lockin`); |resp|=√(I²+Q²), phase=atan2(Q,I). The ring-down likewise records the full field time series (both reactances implicit in the complex FFT). A single-phase snapshot cannot distinguish a resonant absorber from an oscillator caught at peak (A-Rule 10).
- **CP7 (PML-excluded read):** the source and read masks sit in the interior; the read integral excludes PML cells (`interior_mask`, `crystal_engine.py`). For the made object the read is at an energy-density peak of the settled field, NOT at a centroid offset (density-peak sampling discipline; the column/shell centroid is the empty axis).
- **CP9 (heuristic-vs-dynamical):** LOAD-BEARING. The S11 drive enters the ACCELERATION (a physical force density, `s11_probe.py` PROBE TERM 1); the ring-down is the integrated free field. No Γ is painted on a circle, no transmission is assumed, no algebraic susceptibility formula is read in place of the dynamics.
- **CP10 (boundary-not-bulk):** the drive is a localized interior source density, not a global bulk forcing; the Γ=−1 wall is the engine's own `c_eff` trap, untouched. The probe ADDS only the two #166 terms (drive force + gate-only linear damping) — nothing in the bulk EOM is altered.

### 2.2 phase-space-coordinate-check
The **charge/winding** identity (the (2,3) winding integer in the (V_inc, V_ref) Clifford-torus phase-space) is a **PHASE-SPACE** claim and is **NOT** what ring-down or S11 measure. **Ring-down and S11 measure REAL-SPACE frequency-domain observables** — a free-field FFT peak (a) and a driven-response amplitude/phase vs real angular frequency ω (b). f₀, linewidth and Q are real-space frequency-domain quantities. The two coordinate systems are not compared across each other (A46): the winding is read by the genesis extractor (`extract_2_3_omega_fast`), never inferred from the S11 spectrum, and the S11 spectrum is never compared to a φ² phase-space prediction. **PASS** — same coordinate discipline as #166 §1.2.

---

## 3. ENGINE-COMPATIBILITY FLAGS (flag-don't-fix — surfaced, NOT silently resolved)

Two load-bearing preconditions for the Phase-2 RUN are surfaced here, not silently patched. Both are for Grant/auditor adjudication.

**FLAG-A — the canonical `s11_probe.py` is NOT present at the pinned base `7484dd0b`.** PR #166 (which introduced `src/ave/core/s11_probe.py` + `electron_s11_sweep.py`) merged into `main` at `f6ffd98d` on **2026-06-10 17:29:39**. The v6-transducer base commit `7484dd0b` (PR #180) merged a snapshot of `main` at `09b4d995` (PR #179, **2026-06-10 17:02:26**) — i.e. **27 minutes BEFORE #166 landed**. Verified: `git merge-base --is-ancestor f6ffd98d 7484dd0b` → **NO**; `git ls-tree -r 7484dd0b | grep s11_probe` → **empty**. So the task framing "(7484dd0b … contains, via the merged main, the canonical s11_probe.py from #166)" is **FALSE as stated** — the merged-in main was too old by ~27 min. **Phase-2 precondition:** before any S11 run, bring #166 into the worktree (rebase `analysis/2026-06-11-s11-de-novo` onto current `origin/main`, which DOES contain #166; OR cherry-pick `7d11c518`'s `s11_probe.py`). This prereg (Phase 1) is committed ALONE on the pinned base and does NOT require the file present; it records the precondition rather than auto-rebasing (which would silently move the pinned base the task specified).

**FLAG-B — the canonical `S11Probe` subclasses `CrystalGraftV2`, but the made object is `UnifiedGenesisEngine(CrystalGraftV4)`; the probe must be RE-LAYERED, not reused as-is.** `S11Probe.step()` reproduces `CrystalGraftV2.step()` **verbatim** + two probe terms (`s11_probe.py`, "the ``step`` below reproduces the parent 3-sector leapfrog verbatim and ADDS exactly two probe terms"). That V2 step has NO bulk-density ρ̄/u_adv sector, NO self-limiting snap, NO chiral transducer — the entire v6 physics. Instantiating `S11Probe` directly would probe a V2 object, not the v6 made product. **Phase-2 implementation requirement:** the S11 instrument must be re-instantiated as `S11ProbeUnified(UnifiedGenesisEngine)` that reproduces `UnifiedGenesisEngine.step()` (= `CrystalGraftV4.step()` + the unified sectors) **verbatim** and ADDS the SAME two #166 probe terms (PROBE TERM 1: drive force into the chosen sector's acceleration; PROBE TERM 2, gate-only: uniform linear `−γ·velocity` damping), plus the identical `read_signal` / `lockin` I/Q machinery and the driver's drive-off NET-subtraction. This is a `substrate-native-check` operator-re-derivation-on-a-different-engine trigger; the re-layer changes NO inherited physics (every probe term is additive and behind a probe flag that defaults OFF). **Because the engine changed, the probe-capability gate (§4) MUST be re-run in THIS engine config — a gate PASS inherited from the V2 #166 run does NOT transfer.** Confirmed the gate's primitives exist in the lineage: `c_omega`/`omega_gap`/`omega_sector_on` are CrystalGraftV2 attributes (`crystal_graft_v2.py:93,95,96`, inherited by `UnifiedGenesisEngine`); `c_eff_squared` is `CrystalEngine:197`; `seed_omega_known_2_3` is `crystal_graft_v4.py:296`.

---

## 4. THE PROBE-CAPABILITY GATE (FIRST; gates everything; re-run IN THIS engine — FLAG-B)

Per `ave-apparatus-floor-attribution` + the m-even/keeper discipline, the probe is validated on a KNOWN resonator **in the `UnifiedGenesisEngine` config** BEFORE it is pointed at the unknown made object.

- **Known resonator (analytic):** the ω-sector mass-gap oscillator with **`c_omega = 0`** (each cell an independent local oscillator, no spatial dispersion) + a driver-injected uniform linear damping `γ_probe`. A spatially-broad (low-k) ω drive realizes the textbook driven-damped oscillator `ω̈ = −ω₀²ω − γ_probe·ω̇ + F·sin(ω_d t)` with **EXACT analytic** `f₀,known = ω₀/(2π)` (ω₀ = `omega_gap`) and `Q,known = ω₀/γ_probe`. At the MAIN default `omega_gap = 1.0` ⇒ **f₀,known = 1/(2π) = 0.15915 cyc/time** (this is the SAME analytic anchor the #166 V2 gate recovered to 0.16%, confirming the gate is realizable identically in the unified engine).
- **Gate PASS criterion (FROZEN):** the lock-in sweep + Lorentzian fit must recover **f₀ within ±5%** AND **Q within ±20%** at **≥2** distinct (ω₀, γ_probe) settings (a low-Q and a high-Q known, e.g. Q=5 and Q=10 as in #166). If the probe cannot recover a KNOWN f₀/Q **in this engine config**, the entire run returns **UNRESOLVED** and NO f₀/Q is reported for the made object.
- **Linearity sub-gate (FROZEN):** at fixed ω near f₀,known, sweep drive amplitude A over **≥4 values spanning ×8**; the steady response must be **linear in A** (slope-fit R² > 0.99, intercept ≈ 0). This fixes the small-signal band for the unknown run. **Auditor WARN inherited from #166 §1, honored here:** the linearity sub-gate validates the channel it is swept on. The unknown is probed on the **bulk-V channel** (through the saturating `c_eff(V)` wall). Therefore the V-channel amplitude linearity is swept **directly** here (≥4 A-values ×8 on `drive_sector="V"`), converting #166's indirect (subtraction-ratio) V-argument into a swept one — closing #166 FLAG-5.

---

## 5. THE UNKNOWN — THE MADE OBJECT (only run if the gate PASSES) + THE PLANTED-vs-MADE COMPARISON

**Build the made object (FROZEN recipe — `genesis_v6_transducer_run.py` MAIN, verbatim):** `make_cfg("MAIN", helicity=1)` → `build_engine` (N=48, M=1.8, frac=0.85, snap=True, transducer_on=True, chi_exch=0.02, omega_frac=0.5, meissner=0.05, lock_eta=0.08, seed=20260610) → step to **T1 convergence (N_BUILD=3200)**, asserting T1 mass converged (`spec_T1_mass_converges`, E_V_cons drift < 5e-2 — if T1 does NOT converge / detonates, the run STOPS and reports NOT-CONVERGED; no S11 on a detonating object). **Then settle drive-off:** kill the chiral-photon drive (`e.w[:]=0; e.w_prev[:]=0`; `e.drive_helicity=0` — the F-CLOSE/D11 drive-off convention, `genesis_v6_transducer_run.py:331-332,480`) and settle for the convergence-checked settle window. This settled, free object IS the de-novo subject.

**(a) Ring-down self-spectrum (the free object's own song):** from the settled object, record the interior (PML-excluded), density-peak read-point field time series over a long free window; subtract the mean; FFT; report the dominant angular frequency `w_est` (→ f₀,ringdown in cyc/time) and the spectral linewidth (FWHM of the dominant peak → an independent Q_ringdown = f₀/Δf). This is acquired BEFORE the driven sweep and **SETS the S11 band** (≥3× around f₀,ringdown).

**(b) S11 small-signal sweep (the canonical s11_probe machinery — drive-off leakage subtraction, the #166 method):** drive a small-signal **bulk-V** probe at the V-linearity-gated amplitude; sweep ω_d across the ring-down-set band (≥20 points). Record driven (I,Q) at each ω_d. Separately record the **drive-off reference** (same settled object, `drive_amp=0`) read series ONCE and project at every ω_d. **NET susceptibility = (driven I,Q) − (drive-off I,Q), complex** (`electron_s11_sweep.py:326-329`); `net = |net_I + i·net_Q|`. Floor = **median + 3·robust-σ (MAD)** of the NET off-resonance level (`:332-335`). Subtraction-meaningful gate: `subtraction_ratio = median(net)/median(driven)` must be small (background cancelled). Count distinct local maxima above floor (`:344-348`).

**(c) BVD/Q extraction (IF a resonance exists):** only if (b) shows a single clean net peak above floor inside the band, fit a single Lorentzian (`fit_driven`) → f₀, Q, residual; AND extract the BVD motional parameters (L_m, C_m, R_m in engine-natural units) from the resonance shape + off-resonance baseline. If ≥2 peaks, report ALL peaks + their Q's (no cherry-pick toward 137). If no peak clears floor, NO BVD is reported.

**Planted-vs-made comparison (the de-novo payoff):** re-run the SAME instrument on the #166-style PLANTED article (`seed_omega_known_2_3(R, r=4)` + planted breather) **in the SAME `UnifiedGenesisEngine` config** (NOT the V2 #166 config), so the only difference is planted-vs-made. **Floor decision (FROZEN):** floors are **RECALIBRATED per object** (each object's own NET MAD floor and own ring-down-set band), because the planted and made objects have different breather backgrounds and dispersion — a floor carried from one to the other is invalid (`ave-apparatus-floor-attribution`: a floor from a different config is invalid). The comparison is reported as a paired table (planted vs made: f₀,ringdown, n_modes, peak/floor contrast, Q_fit or "no clean Q", bin), with each object floored on its own.

---

## 6. FROZEN BINS (ORDERED — the floor-check gates the rest)

**GATE (first):** probe-capability + V-channel linearity, re-run in THIS engine (§4). **FAIL ⇒ entire run = UNRESOLVED**, no made-object f₀/Q reported.

If the gate PASSES, the made-object run lands in exactly one bin (the SAME four frozen bins as #166, applied to the de-novo subject):

- **RESONANCE-CHARACTERIZED** — a single clean net Lorentzian peak above the median+3σ floor, fit residual small (< 0.35), peak inside the band (not at an edge). Report f₀, linewidth, Q (forward), and the BVD motional parameters — **with NO comparison to α⁻¹ in the bin verdict** (the α⁻¹ comparison is the separate forward-registered post-hoc line, §0). **Rule 11 anti-137-retrofit:** f₀/Q reported FIRST, THEN compared.
- **MULTI-MODE** — ≥2 resolved net peaks above floor (subtraction meaningful, not band-edge). Report the spectrum honestly (all peaks, their Q's); do NOT cherry-pick the one nearest 137.
- **NO-RESPONSE** (the near-perfect-mirror reading — *itself a datasheet entry*) — the made object does not couple a resolvable resonance to the small-signal bulk probe (net ≈ flat / never clears the floor across the band) AND/OR the ring-down shows no resolvable peak (the free object does not ring). This is the honest-prior outcome (§0): the made object reads as a near-perfect mirror to the probe — no internal small-signal-couplable resonator. Recorded as such, a positive datasheet fact (`ave-representation-capability-check`: the probe channel may not couple), **NOT a failure to be debugged**.
- **UNRESOLVED** — the response exists but does not clear the apparatus floor (peak below the noise band, or the fit does not converge, or the peak sits on a band edge, or the drive-off subtraction is not meaningful / background-dominated). The honest floor bin.

**Rule 11 / honest-closure commitment:** NO-RESPONSE or UNRESOLVED is the expected-prior result (§0) and CLOSES the de-novo characterization as "the v6 made object presents no clean small-signal resonance"; it is NOT a trigger to tune the seed, the wall, the band, the settle, or the read location toward a peak. A single mechanism (the made object is not a self-bound high-Q resonator — NOT-ELECTRON inherited) explaining a null is the discipline working, not a result to rescue (Rule 11). Apparatus redesign, if warranted, is SURFACED for Grant/auditor — not auto-pivoted (Rule 16).

---

## 7. STEP-3.5 — DIMENSIONAL ANALYSIS (engine-natural primitives; mandatory)

**Dimensional ingredients (canonical, grep-confirmed in this worktree):** `dx = 1.0` (`crystal_engine.py:58`), `c0 = 1.0` (`:60`), `cfl_safety = 0.30` (`:61`), `A_cap = 0.99` (`:63`), `S_min = 0.05` (`:64`); `omega_gap = 1.0` (`crystal_graft_v2.py:63`, default; MAIN does NOT override → `self.omega_gap` `:96`); `c_omega = c_T` by default (`:95`, set to 0 for the gate). MAIN passes no `omega_gap`/`c_omega`/`S_min` override (`genesis_v6_transducer_run.py` `build_engine`), so the defaults govern.

**Derived time-step (the frequency unit):**
- `c_eff_max = c0/√S_min = 1/√0.05 = 4.4721`.
- `dt = cfl_safety · dx / (c_eff_max · √3) = 0.30 / (4.4721 · 1.73205) = 0.30 / 7.7460 = 0.03873` time-units/step (`crystal_engine.py:100`).
- Engine-natural frequency unit: **cyc/time**, where 1 "time" = 1 engine time-unit. Sampling interval `dt` ⇒ **Nyquist f = 1/(2·dt) = 1/(0.07746) = 12.91 cyc/time**. Everything physical here sits far below Nyquist.

**Gate anchor (exact, dimensionless-in, dimensionless-out):**
- `f₀,gate = omega_gap/(2π) = 1.0/6.2832 = 0.15915 cyc/time` (c_omega=0 ⇒ the spatial term vanishes, f₀ is purely the ω-tank LC reactance — independent of dx, S_min, the wall). Period `T = 2π/omega_gap = 6.2832 time = 162.2 steps/cycle`. A settle/window of ~2200 steps ≈ **13.6 cycles** — several periods, satisfying the settle/window discipline.
- `Q,gate = omega_gap/γ_probe` — for Q=5, γ_probe=0.20; for Q=10, γ_probe=0.10. Q is **dimensionless** (a ratio of frequencies).

**Made-object scale (NOT pre-dicted — set empirically by the ring-down):** the made object's resonance scale is NOT predictable a priori; it is bounded between the ω mass-gap (`omega_gap/2π = 0.159 cyc/time`, the fast LC reactance) and the slower bulk-breather ring-down (the #166 *planted* article rang at `f_est ≈ 0.052 cyc/time`, a lower dispersion-set scale, `electron-s11-sweep_result.md:§2`). The ring-down self-spectrum (a) measures whichever the made object actually presents and SETS the band there — so the band cannot be a retrofit. **Pre-frozen band rule:** band = [0.33·f₀,ringdown, 3·f₀,ringdown] angular-equivalent, ≥20 points; a dominant peak at a band edge ⇒ band widened once and re-noted, else UNRESOLVED.

**Q is dimensionless and α-free:** f₀ and Q carry engine-natural units only; no α-bearing input enters (κ̃=6/5 topology, V_yield≡1, `omega_gap`/`c_omega` are geometry/engineering knobs). A dimensionless Q near 137 would be a **consistency-class coincidence** (§8), not an emergence — there is no SI/CODATA substitution anywhere in the chain.

---

## 8. consistency-vs-emergence TAG

f₀, linewidth, Q, and the BVD motional parameters (if measured) are **MEASURED-IN-ENGINE** quantities in **engine-natural (α-free) units** — **`consistency`-class** apparatus readings, NOT emergence claims. The engine takes no α-bearing input. A dimensionless Q near 137 would be a `consistency`-class coincidence UNLESS a de-novo (2,3) self-assembles — which the v6 panel verdict says it does NOT (`genesis-v6-transducer_prereg:11`, NOT-ELECTRON STANDS; the genesis/T1 electron arm "remains NOT run"). In that (absent) case the joint-ledger guard, not this S11 sweep, would adjudicate emergence. **No emergence headline is licensed by this prereg.**

---

## 9. CORPUS ANCHORS (verify-before-cite — re-grepped live in this worktree 2026-06-11)

- **The canonical S11 instrument (the #166 machinery):** `src/ave/core/s11_probe.py` — `S11Probe(CrystalGraftV2)`; PROBE TERM 1 = small-signal drive force into the sector acceleration; PROBE TERM 2 (gate-only) = uniform linear `−γ·velocity` damping; `lockin` records BOTH I/Q quadratures (CP6). Present in commit `7d11c518` / `f6ffd98d`; **NOT present at the pinned base `7484dd0b`** (FLAG-A, §3).
- **The drive-off NET-subtraction method (#166):** `src/scripts/vol_9_device/electron_s11_sweep.py:314-348` — drive-off reference (`drive_amp=0`) recorded once; `net_I = Is − off_IQ[:,0]`; `net = hypot(net_I, net_Q)`; floor = `median + 3·MAD·1.4826`; `subtraction_ratio` gate; local-maxima count for MULTI-MODE.
- **The #166 result (the planted baseline):** `research/2026-06-10_electron-s11-sweep_result.md:0` — GATE PASS (f₀ 0.16%, Q ≤5%); UNKNOWN bulk channel MULTI-MODE low-contrast (2 weak maxima, contrast 1.1–1.5× floor, Q_fit≈0.73 overdamped); Measured-Q UNTESTED; no α⁻¹.
- **The made-object recipe (MAIN):** `src/scripts/vol_1_foundations/genesis_v6_transducer_run.py` — `make_cfg("MAIN", helicity=1)`, `build_engine` (`:68`), N_MAIN=48, M_MAIN=1.8, N_BUILD=3200 (T1), drive-off convention `e.w[:]=0; e.w_prev[:]=0` (`:331-332, :480`).
- **The inherited v6 verdict (NOT-ELECTRON; the honest prior):** `research/2026-06-10_genesis-v6-transducer_prereg.md:11` — "NOT-ELECTRON (T1 detonates) — STANDS … the genesis/T1 arm remains NOT run."
- **Engine lineage + gate primitives:** `unified_genesis_engine.py:67` (`UnifiedGenesisEngine(CrystalGraftV4)`); `crystal_graft_v4.py:74`; `crystal_graft_v2.py:54,93,95,96` (`omega_sector_on`, `c_omega`, `omega_gap`); `crystal_engine.py:51,197` (`c_eff_squared`); `crystal_graft_v4.py:296` (`seed_omega_known_2_3`).
- **Canonical primitives for §7:** `crystal_engine.py:58,60,61,63,64,100` (`dx`, `c0`, `cfl_safety`, `A_cap`, `S_min`, `dt`); `crystal_graft_v2.py:63,95,96` (`omega_gap=1.0` default, `c_omega=c_T`, `self.omega_gap`).

## 10. WHAT THIS PREREG DOES NOT DO
- It does NOT promote any candidate-claim; it does NOT promise a 137; it does NOT reopen the electron/NOT-ELECTRON verdict.
- It does NOT test phase-space charge (the genesis extractor's job, §2.2).
- It does NOT silently rebase the pinned base or silently re-layer the probe — both are SURFACED (FLAG-A, FLAG-B, §3) for Grant/auditor.
- It does NOT redesign the apparatus to chase a peak (Rule 11). If the made object reads NO-RESPONSE / UNRESOLVED, that is the honest datasheet entry (the near-perfect mirror), and any apparatus redesign is surfaced for Grant/auditor, not auto-pivoted (Rule 16).
