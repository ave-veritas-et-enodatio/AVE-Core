# PREREG — Electron S11 resonance sweep: does the locked (2,3)+trapped-breather state present a characterizable resonance to a small-signal probe, and what are its f₀ / Q / BVD parameters?

**Date (frozen):** 2026-06-10
**Branch:** `analysis/2026-06-10-electron-device-datasheet` (worktree `/tmp/ave-edatasheet`, off `origin/analysis/2026-06-09-crystal-graft-v2` = PR #155; do NOT push/merge — review-gated)
**Engine lineage (subclassed, inherited physics unchanged):** `CrystalGraftV2` (`src/ave/core/crystal_graft_v2.py`) ← `CrystalEngine` (`src/ave/core/crystal_engine.py`). The S11 driver ADDS a small-signal sinusoidal drive force + a lock-in read + (gate-only) a controllable linear damping; it makes **no** change to the inherited bulk-V / shear-w / micro-rotation-ω / buckle dynamics.
**Governing discipline:** `ave-apparatus-floor-attribution` — the PROBE is the instrument; it is validated on a KNOWN resonator FIRST, and the bins are ORDERED so the probe-capability floor-check GATES any f₀/Q claim about the unknown locked state. No Q is reported for the electron state until the probe has recovered a known f₀ AND known Q within tolerance.
**Skills fired at design time:** `ave-prereg` (corpus anchors §7, frozen bins §5, committed alone before any run artifact); `substrate-native-check` (CP1 dynamical-not-minimization, CP6 reactance-pair recorded, CP7 PML-excluded read, CP9 the resonance is the integrated field response not a painted Lorentzian — §1.1); `ave-apparatus-floor-attribution` (probe-capability gate + ORDERED bins, governing); `phase-space-coordinate-check` (the charge/winding identity is phase-space; the S11 RESONANCE is a real-space driven-response observable measured in real-space frequency — each in its own coordinate, §1.2); `ave-representation-capability-check` (does the small-signal probe channel even COUPLE to the planted winding? — the NO-RESPONSE bin exists precisely because it may not, §5); `ave-driver-script-honesty` (every number from the evolved field; lock-in fit reported with its residual; NO comparison to α⁻¹ unless the number genuinely emerges); `consistency-vs-emergence` (f₀/Q are MEASURED-IN-ENGINE quantities in engine-natural units, not emergence claims — §6); `verify-before-cite` (every anchor grep-confirmed live in this worktree, §7).

---

## 0. THE NAMED QUESTION (forward-registered; Rule 11)

The electron datasheet (`research/2026-06-10_electron-device-datasheet_draft.md`) carries a canonical-DERIVED claim — **Q = α⁻¹ ≈ 137, with 1/Q = α the per-cycle leak fraction** (`theorem-3-1-q-factor.md:81`, "this IS α in its original Sommerfeld meaning … seen from the LC-tank side"). That row's MEASURED cell is currently **UNTESTED**. This prereg freezes the instrument and the bins to ASK — not assume — whether the locked state presents a characterizable resonance to a small-signal probe, and if so, what its f₀ and Q are **in engine-natural units**.

**Forward-registration (Rule 11, hard):** the driver reports the MEASURED (f₀, Q) FIRST. Only THEN, as a separate post-hoc line, is the dimensionless Q compared to α⁻¹. The comparison is **not** an adjudication criterion for any bin; a near-137 Q would be reported as such with its floor, NOT headlined as α-emergence (that would require the joint-ledger guard's de-novo (2,3), which the graft-v2 full run does NOT produce — `2026-06-09_crystal-graft-v2_result.md:30`). **No debugging toward a pretty resonance.**

**Prior expectation (recorded, NOT a target):** the apparatus-floors characterization (`analysis/2026-06-10-apparatus-floors`, `research/2026-06-10_apparatus-floors_note.md`, read-only) found the bulk-trap leak is **FLAT across the whole knob sweep** (mean 0.544, CV 1.5%) and is set by **breather dispersion, not a wall-transmission Q** — "a leak-derived α at this config would be reading breather dispersion dynamics, not a regularization-set wall property." So the honest prior is that the bulk channel may land **UNRESOLVED** or **NO-RESPONSE**, and the datasheet's Q row stays UNTESTED. This prereg is designed to be able to RETURN that null cleanly.

## 1. PHYSICAL PICTURE (substrate-native, before code)

The locked electron state is a trapped longitudinal bulk-V breather (the "3"-as-MASS, held at the `c_eff` Γ=−1 acoustic wall — `crystal_graft_v2.py:16-18`) carrying a micro-rotation ω winding (the "3"-as-WINDING / charge — `crystal_graft_v2.py:20-24`). A resonator is characterized by injecting a **small** disturbance and watching how the energy rings: the cavity returns a frequency-selective response (a peak in driven amplitude + a π phase swing) whose center is f₀ and whose sharpness is Q = f₀/Δf (FWHM). This is a network-analyzer / lock-in measurement: drive at ω, read the in-phase (I) and quadrature (Q) response over a settled window, sweep ω.

### 1.1 substrate-native-check (walked at design time)
- **CP1 (dynamics):** the response is the time-domain FDTD field reacting to the drive — NOT a prescribed Lorentzian, NOT an eigensolve. The Lorentzian is FIT to the measured spectrum, post-hoc; the spectrum itself is integrated.
- **CP6 (reactance pair):** the lock-in records BOTH quadratures (I = in-phase ↔ C-state, Q = quadrature ↔ L-state) every step over the read window; |resp|=√(I²+Q²), phase=atan2(Q,I). A single-phase snapshot cannot distinguish a resonant absorber from an oscillator caught at peak — both quadratures are mandatory (A-Rule 10).
- **CP7 (PML-excluded read):** the read location and the response integral exclude PML cells (`interior_mask`); the source sits in the interior, the read at a separate interior location.
- **CP9 (heuristic-vs-dynamical):** LOAD-BEARING. The drive enters the ACCELERATION (a physical force density), the response is the integrated field — no Γ is painted on a circle, no transmission is assumed.
- **CP10 (boundary-not-bulk):** the drive is a localized source density, not a global bulk forcing; the Γ=−1 wall is the engine's own `c_eff` trap, untouched.

### 1.2 phase-space-coordinate-check
The **charge** identity (winding integer in the (V_inc,V_ref) Clifford torus) is a PHASE-SPACE claim and is NOT what S11 measures. **S11 measures a REAL-SPACE driven-response spectrum** — amplitude/phase vs real frequency ω. f₀ and Q are real-space frequency-domain observables. The two are not compared across coordinates (A46). This prereg's resonance is the real-space frequency observable; the phase-space winding is read separately (the graft-v2 extractor). PASS.

## 2. THE PROBE-CAPABILITY GATE (FIRST; gates everything downstream)

Per `ave-apparatus-floor-attribution`, the probe is validated on a KNOWN resonator in the SAME engine BEFORE it is pointed at the unknown locked state.

- **Known resonator:** the ω-sector mass-gap oscillator with **`c_omega = 0`** (each cell an independent local oscillator — no spatial dispersion) and a driver-injected uniform linear damping `γ_probe`. A spatially-broad (low-k) ω drive then realizes the textbook driven-damped oscillator `ω̈ = −ω₀²ω − γ_probe·ω̇ + F·sin(ω_d t)`, with **EXACT analytic** `f₀,known = ω₀/(2π)` (ω₀ = `omega_gap`) and `Q,known = ω₀/γ_probe`.
- **Gate pass criterion (FROZEN):** the lock-in sweep + Lorentzian fit must recover **f₀ within ±5%** of `ω₀/2π` AND **Q within ±20%** of `ω₀/γ_probe`, at **≥2** distinct (ω₀, γ_probe) settings (a low-Q and a high-Q known). If the probe cannot recover a KNOWN f₀/Q, the entire run returns **UNRESOLVED** and NO f₀/Q is reported for the electron state.
- **Linearity sub-gate (FROZEN):** at fixed ω near f₀,known, sweep drive amplitude A over ≥4 values spanning ×8; the steady response must be **linear in A** (slope-fit R² > 0.99, intercept ≈ 0). This fixes the small-signal amplitude band for the unknown run. A drive that is not in the linear regime is OUT OF SPEC.

## 3. THE UNKNOWN (only run if the gate PASSES)

Plant the known-positive configuration: the validated (2,3) ω winding via `seed_omega_known_2_3(R, r, …)` with **minor radius r above the r ≥ 3-cell extractor floor** (the graft-v4 `F0b` floor, `genesis-v5 prereg:150`) — confirmed by re-reading `(w_tor,w_pol)` before probing — AND a trapped bulk-V breather (the `c_eff` wall cavity = the mass). Then:
1. drive a small-signal **bulk-V** probe at the linearity-gated amplitude, sweep ω_d across the band;
2. lock-in read |resp|(ω_d) and phase(ω_d) at an interior read location;
3. fit the Lorentzian → f₀, Q, and the BVD motional parameters (L_m, C_m, R_m in engine-natural units) from the resonance shape + off-resonance baseline.

## 4. APPARATUS INVENTORY (every knob swept or bounded — `ave-apparatus-floor-attribution`)

| knob | gate/bound | role |
|---|---|---|
| probe amplitude A | linearity sub-gate, ≥4 values ×8 span | must be in the linear small-signal regime; OUT OF SPEC otherwise |
| frequency band [ω_lo, ω_hi] | ≥3× around the expected f₀; ≥20 points | must bracket the peak; a peak at a band edge ⇒ band widened or UNRESOLVED |
| settle time t_settle | ≥ several/γ (gate) / ≥ several cavity periods (unknown); convergence-checked | transient must decay before the lock-in window opens |
| lock-in window t_win | ≥ several drive periods | the I/Q integral averaging window |
| read location | interior, PML-excluded, ≠ source location | CP7 |
| source location / mask | interior, PML-excluded | CP10 |
| γ_probe (gate only) | ≥2 known values | sets the KNOWN Q for the gate |

## 5. FROZEN BINS (ORDERED — the floor-check gates the rest)

**GATE (first):** probe-capability + linearity. **FAIL ⇒ entire run = UNRESOLVED**, no electron f₀/Q reported.

If the gate PASSES, the unknown run lands in exactly one bin:

- **RESONANCE-CHARACTERIZED** — a single clean Lorentzian peak above the read-noise/baseline floor, fit residual small, peak inside the band (not at an edge). Report f₀, Q (with the linewidth), and the BVD motional parameters — **with NO comparison to α⁻¹ in the bin verdict**. (The α⁻¹ comparison is a separate forward-registered post-hoc line per §0.)
- **MULTI-MODE** — ≥2 resolved peaks above floor. Report the spectrum honestly (all peaks, their Q's); do NOT cherry-pick the one nearest 137.
- **NO-RESPONSE** — the planted state does not couple a resolvable resonance to the small-signal bulk probe (response ≈ flat / at the baseline floor across the band). This is itself informative (`ave-representation-capability-check`: the probe channel may not couple to the winding) and is recorded as such — NOT a failure to be debugged.
- **UNRESOLVED** — the response exists but does not clear the apparatus floor (peak below baseline-noise band, or the fit does not converge, or the peak sits on a band edge). The honest floor bin.

**Rule 11 / honest-closure commitment:** a NO-RESPONSE or UNRESOLVED outcome is the expected-prior result (§0) and CLOSES the row as UNTESTED-pending-apparatus; it is NOT a trigger to tune the seed, the wall, or the band toward a peak.

## 6. consistency-vs-emergence tag

f₀ and Q (if measured) are **MEASURED-IN-ENGINE** quantities in **engine-natural (α-free) units** — `consistency`-class apparatus readings, NOT emergence claims. The engine takes no α-bearing input (κ̃=6/5 topology, V_yield≡1, `c_omega`/`omega_gap` geometry/engineering knobs — `crystal_graft_v2.py:41-43`). A dimensionless Q near 137 would be a `consistency`-class coincidence UNLESS a de-novo (2,3) self-assembles (it does not, per the graft-v2 verdict) — in which case the joint-ledger guard, not this S11 sweep, would adjudicate emergence.

## 7. CORPUS ANCHORS (verify-before-cite — re-grepped live in this worktree 2026-06-10)

- **Q = α⁻¹, 1/Q = α per-cycle leak (Sommerfeld):** `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:81` — "only a fraction 1/Q = α ≈ 0.0073 of the stored energy leaks per cycle through the TIR boundary — this IS α in its original Sommerfeld meaning ('coupling strength'), seen from the LC-tank side."
- **leak is dispersion-contaminated / flat (the prior):** `research/2026-06-10_apparatus-floors_note.md` Leak-attribution section (`analysis/2026-06-10-apparatus-floors`, read-only) — "leak is FLAT across the entire sweep … set by the bulk breather's dispersion (shape-driven, scale-invariant) … a leak-derived α at this config would be reading breather dispersion dynamics, not a regularization-set wall property."
- **graft-v2 does NOT self-assemble a de-novo (2,3):** `research/2026-06-09_crystal-graft-v2_result.md:28,30` — full run `(w_tor,w_pol)=(0,0)`; α "REFUSED by joint-ledger guard."
- **known-positive (2,3) carrier reads back:** `research/2026-06-09_crystal-graft-v2_result.md:25` (SMOKE-3a, rel (0.80,0.59)); seeder `crystal_graft_v2.py:321` `seed_omega_known_2_3`.
- **extractor floor r ≥ 3 cells:** `genesis-v5 prereg:150` (`/tmp/ave-v5`, read-only) — "the winding read (T2) requires `r_meas ≥ 3 cells`."
- **ω-sector mass-gap oscillator (the known resonator):** `crystal_graft_v2.py:201-208` (`∂²_tω = c_ω²∇²ω − ω_0²ω`), `:76-79` (`omega_gap` = the ω-tank LC reactance), `:95` (`c_omega` default = c_T; set to 0 for the gate).
- **PML-excluded read:** `crystal_engine.py:134-139` `interior_mask`.

## 8. WHAT THIS PREREG DOES NOT DO
- It does NOT promote any candidate-claim. It does NOT promise a 137.
- It does NOT test phase-space charge (that is the graft-v2 extractor's job, §1.2).
- It does NOT redesign the apparatus to chase a peak (Rule 11). If the bulk channel is dispersion-floored, the honest output is NO-RESPONSE / UNRESOLVED and the datasheet Q row stays UNTESTED — apparatus redesign surfaced for Grant/auditor, not auto-pivoted.
