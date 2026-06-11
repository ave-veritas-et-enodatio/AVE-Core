# RESULT — Electron S11 resonance sweep: probe VALIDATED; the bulk channel is MULTI-MODE (low-contrast dispersive), NOT a single high-Q resonator — measured Q stays UNTESTED, no α⁻¹

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-electron-device-datasheet`
**Prereg (FROZEN, committed alone first):** [`2026-06-10_electron-s11-sweep_prereg.md`](2026-06-10_electron-s11-sweep_prereg.md) (commit `df146283`, before any run artifact)
**Engine:** [`src/ave/core/s11_probe.py`](../src/ave/core/s11_probe.py) `S11Probe(CrystalGraftV2)` ·
**Driver:** [`src/scripts/vol_9_device/electron_s11_sweep.py`](../src/scripts/vol_9_device/electron_s11_sweep.py) ·
**Data:** `src/scripts/vol_9_device/_output/electron_s11_results.json` · **Figures:** `electron_s11_gate.png`, `electron_s11_unknown.png`
**Governing discipline:** `ave-apparatus-floor-attribution` (probe-capability gate + ORDERED bins). Skills: substrate-native-check, ave-prereg, phase-space-coordinate-check, ave-representation-capability-check, ave-driver-script-honesty, consistency-vs-emergence, verify-before-cite.

---

## 0. VERDICT (ordered: GATE first, then the unknown bin)

> **GATE — PASS.** The lock-in probe recovers KNOWN omega mass-gap resonators (c_omega=0 ⇒ analytic f₀=ω₀/2π=0.1592 cyc/time, controllable Q=ω₀/γ) to **f₀ within 0.2% and Q within 5%** at two settings (Q=5 and Q=10), and the response is **linear in drive amplitude on the ω readout channel** (R²=1.00000). The probe is a validated instrument.
>
> **UNKNOWN bulk channel — MULTI-MODE (low-contrast).** With the probe validated, the small-signal BULK-V probe on the locked (2,3)+trapped-breather state returns a net susceptibility (driven − drive-off, background cancelled to 2.2%) with **two weak local maxima above the median+3σ floor** (f≈0.026 and f≈0.057 cyc/time, contrast only ~1.1–1.5× floor) and a single-Lorentzian fit that returns a **non-resonant, overdamped Q_fit≈0.73** (w0=0.285, resid 0.185 — *under* the 0.35 frozen fail-threshold; fit_ok=True). There is **NO single clean high-Q resonance.** Per the frozen bins this is **MULTI-MODE** — set by the 2-peak count (n_modes≥2), NOT by a residual exceedance; reported honestly, it is low-contrast multi-mode dispersive structure — exactly what the apparatus-floors verdict predicted ("the bulk leak is dispersion-contaminated, FLAT across the knob sweep, set by breather dispersion not a wall-transmission Q").
>
> **Consequence: the datasheet MEASURED-Q row STAYS UNTESTED.** There is no single Q to report; the only fitted number (Q≈0.73) is a non-resonant (overdamped) single-mode fit forced onto a multi-mode spectrum, **not** a wall-transmission Q. **α⁻¹≈137 is NOT measured, NOT approached, and is NOT copied into any measured cell** (Rule 11 / forward-registration).

**Plumber-physical one-liner:** the validated network analyzer, pointed at the electron's bulk trap, sees not one sharp tank but a smear of weak, overlapping dispersive modes — the breather rings at many nearby pitches at once, none of them a clean Q. You cannot read a single 1/Q=α leak off a smear.

---

## 1. THE GATE (probe-capability, FIRST — gates everything; `ave-apparatus-floor-attribution`)

KNOWN resonator = the ω mass-gap driven-damped oscillator (c_omega=0 ⇒ each cell an independent oscillator at ω₀; injected linear damping γ_probe). Analytic f₀=ω₀/2π, Q=ω₀/γ_probe.

| known (f₀ cyc/time, Q) | recovered f₀ | f₀ err | recovered Q | Q err | gate |
|---|---|---|---|---|---|
| (0.1592, 5.0) | 0.1594 | **0.16%** | 4.86 | **2.7%** | PASS (≤5% / ≤20%) |
| (0.1592, 10.0) | 0.1594 | **0.13%** | 9.52 | **4.8%** | PASS |

**Linearity sub-gate:** drive amplitude swept ×16 (2.5e-4 … 4e-3) on the **ω readout channel** (`drive_sector="omega"`, linear by construction); response slope-fit **R²=1.00000**, intercept 0.0% → the lock-in READOUT is linear. *Scope (auditor WARN, honored):* the unknown is driven on the **V channel** (`drive_sector="V"`, through the saturating c_eff(V) wall), which this sub-gate does NOT directly sweep; V-channel small-signal operation at A=6e-4 is supported INDIRECTLY by the drive-off subtraction cancelling the breather background to 2.2% (subtraction_ratio=0.022), not by a swept V-amplitude linearity. A direct V-amplitude sweep is queued (§8.5).

**Gate conclusion:** probe-capability=True ∧ linearity=True → the probe recovers known f₀/Q and is linear. Any failure to find a clean resonance downstream is the SAMPLE, not the instrument.

## 2. THE UNKNOWN (only run because the gate PASSED)

**Apparatus inventory (every knob bounded/swept):**

| knob | value | role |
|---|---|---|
| N | 40 | grid (PML thickness 5; interior read PML-excluded) |
| S_min, A_cap | 0.0125, 0.999 | wall config (deepest non-clip wall ≈ −0.37, per apparatus-floors) |
| drive sector / amp | bulk V / **6e-4** (linearity-gated small-signal) | probe |
| source / read | center Gaussian σ=2.5 / single interior point (ic+6, ic, ic) | CP10 / CP7 |
| planted (2,3) | R=10.4, **r=4.0 cells (> r≥3 extractor floor)**, max\|ω\|=0.234 | known-positive winding |
| band | ring-down-set: [0.114, 0.844] angular ([0.018, 0.134] cyc/time), 16 pts | brackets f_est |
| settle / window | 2200 / 2200 steps | transient decay / lock-in window |
| drive-off reference | same seed, drive_amp=0, recorded once, projected at all ω_d | the breather background to SUBTRACT |

**Ring-down pre-scan (independent band-setting estimate):** dominant angular w_est=0.3245 (f_est=0.0516 cyc/time). The driven sweep was centered on it.

**Net susceptibility (driven − drive-off; background subtracted to 2.2%):**

| f (cyc/time) | net \|χ\| | vs floor 2.98e-3 |
|---|---|---|
| 0.0258 | 4.36e-3 | **1.46×** (peak 1) |
| 0.0336 | 3.43e-3 | 1.15× (shoulder) |
| 0.0568 | 3.39e-3 | **1.14×** (peak 2) |
| (all others) | < floor | — |

- **subtraction_ratio = 0.022** — the drive-off subtraction cancelled the breather background to 2% of the raw driven amplitude, so the net IS the small-signal probe susceptibility (not breather leakage).
- **two local maxima above the median+3σ floor** (f≈0.026, f≈0.057) → MULTI-MODE by the frozen criterion. **Contrast is LOW** (1.1–1.5× floor): these are weak dispersive features, not sharp tanks.
- **single-Lorentzian fit returns a non-resonant, overdamped Q:** w0_fit=0.285 angular, **Q_fit=0.73**, residual 0.185 (*under* the 0.35 frozen fail-threshold; fit_ok=True). The MULTI-MODE bin is set by the **2-peak count** (n_modes≥2, `assign_bin` line 385), reached BEFORE the fit-quality branch (line 388) — the residual gate was NOT the deciding criterion. A driven-damped-oscillator model does not describe the spectrum (overdamped Q≈0.73, nowhere near a high-Q resonance).

## 3. FROZEN BIN ASSIGNMENT (no debugging toward a peak — Rule 11)

| bin | criterion | this run |
|---|---|---|
| RESONANCE-CHARACTERIZED | single clean Lorentzian above floor, inside band, fit-ok | ✗ (2 peaks ⇒ not single-mode; fit non-resonant/overdamped Q_fit=0.73, resid 0.185) |
| **MULTI-MODE** | ≥2 net peaks above floor, subtraction meaningful, not edge | **✓ (2 maxima; sub_ratio 0.022)** |
| NO-RESPONSE | net never clears floor | ✗ (it clears, weakly) |
| UNRESOLVED | clears but band-edge / fit-fail / background-dominated | (near-boundary; see honesty note) |

**Honesty note (near the MULTI-MODE/UNRESOLVED boundary):** the bin is MULTI-MODE by the frozen logic, but the contrast is only 1.1–1.5× the floor and the single-mode fit is non-resonant (overdamped Q≈0.73) — so the substantive reading is "**low-contrast multi-mode dispersive structure, NOT a clean resonator.**" The two readings agree on the load-bearing point: **the bulk channel does NOT present a single high-Q (∼137) resonance.** Reported as MULTI-MODE per the frozen criterion; the low contrast is stated, not hidden. **No band/seed/wall was re-tuned to sharpen a peak.**

> **Caveat on the POSITIVE 2-peak structure (auditor FLAG, surfaced — NOT a new run):** the two net maxima sit at f≈0.0258 ≈ f_est/2 and f≈0.0568 ≈ f_est — i.e. the breather ring-down frequency (f_est=0.0516 cyc/time) and its exact subharmonic. The unknown ran at a SINGLE config (band-center, settle=2200, read-location all fixed), so a coincidence with incomplete subtraction cannot be excluded for the positive structure without a band-recenter + settle/read-location sweep (queued §8.4, NOT run — Rule 16). **Only the NULL (no single high-Q resonance) is robust to this caveat;** the load-bearing datasheet consequence (Measured-Q stays UNTESTED) rests on the NULL, not on the 2-peak count.

## 4. FORWARD-REGISTERED α COMPARISON (post-hoc; NOT a bin criterion)

Per the prereg §0 forward-registration: the measured spectrum is reported FIRST (§2). Only now, separately: there is **no single measured Q** (MULTI-MODE); the only fitted Q≈0.73 is a *failed* single-mode fit and is **nowhere near α⁻¹=137.036**. **No α⁻¹ emergence is claimed, approached, or implied.** The joint-ledger guard's precondition (a de-novo (2,3)) is also absent (graft-v2 gives `(w_tor,w_pol)=(0,0)`), so emergence was never on the table here.

## 5. CONSISTENCY WITH THE STANDING APPARATUS-FLOORS VERDICT (no conflict)

This result is **consistent with** `research/2026-06-10_apparatus-floors_note.md` (read-only, `analysis/2026-06-10-apparatus-floors`): "the bulk leak is FLAT across the entire sweep … set by the bulk breather's dispersion (shape-driven, scale-invariant) … a leak-derived α at this config would be reading breather dispersion dynamics, not a regularization-set wall property." The S11 sweep adds the frequency-resolved picture: the dispersion shows up as **multiple weak overlapping modes**, not a single wall-transmission Q. Same conclusion from the spectroscopy side: **this config cannot measure the α⁻¹ leak; an apparatus redesign is required.**

## 6. consistency-vs-emergence tag

f₀ candidates and the failed Q are **MEASURED-IN-ENGINE** in engine-natural (α-free) units — consistency-class apparatus readings, NOT emergence. No α-bearing input (κ̃=6/5 topology, V_yield≡1, c_omega/omega_gap engineering knobs). No emergence headline.

## 7. DERIVED / VERIFIED / BLOCKED (honest split)

**VERIFIED (this run):**
- The lock-in probe recovers KNOWN f₀ (≤0.2%) and Q (≤5%) and is linear (R²=1.0) — the instrument is validated (gate PASS).
- The planted (2,3) sits above the r≥3 extractor floor (r=4 cells); the drive-off subtraction cancels the breather background to 2.2%.
- The bulk channel returns LOW-CONTRAST MULTI-MODE dispersive structure; a single high-Q resonance is absent; the single-Lorentzian fit is non-resonant (overdamped Q≈0.73, resid 0.185 < the 0.35 frozen fail-threshold — the MULTI-MODE bin is set by the 2-peak count, not the residual gate).

**BLOCKED / out of scope:**
- A single measured Q for the electron self-impedance → **UNTESTED** (multi-mode, dispersion-contaminated). The datasheet Measured-Q row stays UNTESTED; apparatus redesign required (a probe that isolates wall transmission from bulk dispersion).
- The phase-space charge winding (not what S11 measures — the graft-v2 extractor's job; §1.2 of the prereg).
- Absolute SI units (engine-natural throughout).

## 8. CORPUS-STATE DELTAS TO QUEUE (auditor LANDS; implementer SURFACES)

1. **NEW capability:** `S11Probe` — a validated small-signal lock-in network-analyzer layered on the crystal-graft carrier (drive force + controllable damping + I/Q lock-in; probe-gated on a known resonator). First S11/VNA-style instrument in the graft family.
2. **NEW result (apparatus-class):** the electron bulk channel is MULTI-MODE / low-contrast dispersive to a small-signal probe — **no single high-Q (∼137) resonance**; the datasheet Measured-Q row stays UNTESTED. Consistent with (does not conflict) the apparatus-floors dispersion-contamination verdict; sharpens it with the frequency-resolved spectrum.
3. **FLAG (surfaced, not resolved):** an apparatus that could measure the 1/Q=α wall-transmission leak must separate wall transmission from bulk breather dispersion — a redesign (e.g., a boundary-localized reflection read at the Γ=−1 front, not a bulk-volume response). Surfaced for Grant/auditor; NOT auto-pivoted (Rule 16).
4. **FLAG (auditor, surfaced — NOT run):** the POSITIVE 2-peak structure coincides with the breather ring-down subharmonic (peak1≈f_est/2, peak2≈f_est) and was probed at a single config; a **band-recenter + settle/read-location sweep** is needed before any downstream citation of the 2-mode structure as intrinsic. The NULL (no single high-Q) stands regardless. Surfaced, NOT run (Rule 16).
5. **FLAG (auditor, surfaced — NOT run):** the linearity sub-gate validated the **ω readout channel** (linear by construction), not the **V channel** actually probed; a direct **V-amplitude sweep** would convert the indirect (subtraction_ratio=0.022) V small-signal argument into a swept one. Surfaced, NOT run.
