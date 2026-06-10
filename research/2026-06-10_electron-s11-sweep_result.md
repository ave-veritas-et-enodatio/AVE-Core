# RESULT — Electron S11 resonance sweep: probe VALIDATED; the bulk channel is MULTI-MODE (low-contrast dispersive), NOT a single high-Q resonator — measured Q stays UNTESTED, no α⁻¹

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-electron-device-datasheet`
**Prereg (FROZEN, committed alone first):** [`2026-06-10_electron-s11-sweep_prereg.md`](2026-06-10_electron-s11-sweep_prereg.md) (commit `df146283`, before any run artifact)
**Engine:** [`src/ave/core/s11_probe.py`](../src/ave/core/s11_probe.py) `S11Probe(CrystalGraftV2)` ·
**Driver:** [`src/scripts/vol_9_device/electron_s11_sweep.py`](../src/scripts/vol_9_device/electron_s11_sweep.py) ·
**Data:** `src/scripts/vol_9_device/_output/electron_s11_results.json` · **Figures:** `electron_s11_gate.png`, `electron_s11_unknown.png`
**Governing discipline:** `ave-apparatus-floor-attribution` (probe-capability gate + ORDERED bins). Skills: substrate-native-check, ave-prereg, phase-space-coordinate-check, ave-representation-capability-check, ave-driver-script-honesty, consistency-vs-emergence, verify-before-cite.

---

## 0. VERDICT (ordered: GATE first, then the unknown bin)

> **GATE — PASS.** The lock-in probe recovers KNOWN omega mass-gap resonators (c_omega=0 ⇒ analytic f₀=ω₀/2π=0.1592 cyc/time, controllable Q=ω₀/γ) to **f₀ within 0.2% and Q within 5%** at two settings (Q=5 and Q=10), and the response is **linear in drive amplitude** (R²=1.00000). The probe is a validated instrument.
>
> **UNKNOWN bulk channel — MULTI-MODE (low-contrast).** With the probe validated, the small-signal BULK-V probe on the locked (2,3)+trapped-breather state returns a net susceptibility (driven − drive-off, background cancelled to 2.2%) with **two weak local maxima above the median+3σ floor** (f≈0.026 and f≈0.057 cyc/time, contrast only ~1.1–1.5× floor) and a **FAILED single-Lorentzian fit** (Q_fit≈0.73, residual 0.19). There is **NO single clean high-Q resonance.** Per the frozen bins this is **MULTI-MODE**; reported honestly, it is low-contrast multi-mode dispersive structure — exactly what the apparatus-floors verdict predicted ("the bulk leak is dispersion-contaminated, FLAT across the knob sweep, set by breather dispersion not a wall-transmission Q").
>
> **Consequence: the datasheet MEASURED-Q row STAYS UNTESTED.** There is no single Q to report; the only fitted number (Q≈0.73) is a failed single-mode fit to a multi-mode spectrum, **not** a wall-transmission Q. **α⁻¹≈137 is NOT measured, NOT approached, and is NOT copied into any measured cell** (Rule 11 / forward-registration).

**Plumber-physical one-liner:** the validated network analyzer, pointed at the electron's bulk trap, sees not one sharp tank but a smear of weak, overlapping dispersive modes — the breather rings at many nearby pitches at once, none of them a clean Q. You cannot read a single 1/Q=α leak off a smear.

---

## 1. THE GATE (probe-capability, FIRST — gates everything; `ave-apparatus-floor-attribution`)

KNOWN resonator = the ω mass-gap driven-damped oscillator (c_omega=0 ⇒ each cell an independent oscillator at ω₀; injected linear damping γ_probe). Analytic f₀=ω₀/2π, Q=ω₀/γ_probe.

| known (f₀ cyc/time, Q) | recovered f₀ | f₀ err | recovered Q | Q err | gate |
|---|---|---|---|---|---|
| (0.1592, 5.0) | 0.1594 | **0.16%** | 4.86 | **2.7%** | PASS (≤5% / ≤20%) |
| (0.1592, 10.0) | 0.1594 | **0.13%** | 9.52 | **4.8%** | PASS |

**Linearity sub-gate:** drive amplitude swept ×16 (2.5e-4 … 4e-3); response slope-fit **R²=1.00000**, intercept 0.0% → LINEAR. The small-signal band is validated; the unknown was probed at A=6e-4 (inside the linear regime).

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
- **single-Lorentzian fit FAILS:** w0_fit=0.285 angular, **Q_fit=0.73**, residual 0.185 — a driven-damped-oscillator model does NOT describe the spectrum. There is no single high-Q resonance to characterize.

## 3. FROZEN BIN ASSIGNMENT (no debugging toward a peak — Rule 11)

| bin | criterion | this run |
|---|---|---|
| RESONANCE-CHARACTERIZED | single clean Lorentzian above floor, inside band, fit-ok | ✗ (fit fails, Q_fit=0.73 resid 0.19) |
| **MULTI-MODE** | ≥2 net peaks above floor, subtraction meaningful, not edge | **✓ (2 maxima; sub_ratio 0.022)** |
| NO-RESPONSE | net never clears floor | ✗ (it clears, weakly) |
| UNRESOLVED | clears but band-edge / fit-fail / background-dominated | (near-boundary; see honesty note) |

**Honesty note (near the MULTI-MODE/UNRESOLVED boundary):** the bin is MULTI-MODE by the frozen logic, but the contrast is only 1.1–1.5× the floor and the single-mode fit fails — so the substantive reading is "**low-contrast multi-mode dispersive structure, NOT a clean resonator.**" The two readings agree on the load-bearing point: **the bulk channel does NOT present a single high-Q (∼137) resonance.** Reported as MULTI-MODE per the frozen criterion; the low contrast is stated, not hidden. **No band/seed/wall was re-tuned to sharpen a peak.**

## 4. FORWARD-REGISTERED α COMPARISON (post-hoc; NOT a bin criterion)

Per the prereg §0 forward-registration: the measured spectrum is reported FIRST (§2). Only now, separately: there is **no single measured Q** (MULTI-MODE); the only fitted Q≈0.73 is a *failed* single-mode fit and is **nowhere near α⁻¹=137.036**. **No α⁻¹ emergence is claimed, approached, or implied.** The joint-ledger guard's precondition (a de-novo (2,3)) is also absent (graft-v2 gives w_pol=0), so emergence was never on the table here.

## 5. CONSISTENCY WITH THE STANDING APPARATUS-FLOORS VERDICT (no conflict)

This result is **consistent with** `research/2026-06-10_apparatus-floors_note.md` (read-only, `analysis/2026-06-10-apparatus-floors`): "the bulk leak is FLAT across the entire sweep … set by the bulk breather's dispersion (shape-driven, scale-invariant) … a leak-derived α at this config would be reading breather dispersion dynamics, not a regularization-set wall property." The S11 sweep adds the frequency-resolved picture: the dispersion shows up as **multiple weak overlapping modes**, not a single wall-transmission Q. Same conclusion from the spectroscopy side: **this config cannot measure the α⁻¹ leak; an apparatus redesign is required.**

## 6. consistency-vs-emergence tag

f₀ candidates and the failed Q are **MEASURED-IN-ENGINE** in engine-natural (α-free) units — consistency-class apparatus readings, NOT emergence. No α-bearing input (κ̃=6/5 topology, V_yield≡1, c_omega/omega_gap engineering knobs). No emergence headline.

## 7. DERIVED / VERIFIED / BLOCKED (honest split)

**VERIFIED (this run):**
- The lock-in probe recovers KNOWN f₀ (≤0.2%) and Q (≤5%) and is linear (R²=1.0) — the instrument is validated (gate PASS).
- The planted (2,3) sits above the r≥3 extractor floor (r=4 cells); the drive-off subtraction cancels the breather background to 2.2%.
- The bulk channel returns LOW-CONTRAST MULTI-MODE dispersive structure; a single high-Q resonance is absent; the single-Lorentzian fit fails.

**BLOCKED / out of scope:**
- A single measured Q for the electron self-impedance → **UNTESTED** (multi-mode, dispersion-contaminated). The datasheet Measured-Q row stays UNTESTED; apparatus redesign required (a probe that isolates wall transmission from bulk dispersion).
- The phase-space charge winding (not what S11 measures — the graft-v2 extractor's job; §1.2 of the prereg).
- Absolute SI units (engine-natural throughout).

## 8. CORPUS-STATE DELTAS TO QUEUE (auditor LANDS; implementer SURFACES)

1. **NEW capability:** `S11Probe` — a validated small-signal lock-in network-analyzer layered on the crystal-graft carrier (drive force + controllable damping + I/Q lock-in; probe-gated on a known resonator). First S11/VNA-style instrument in the graft family.
2. **NEW result (apparatus-class):** the electron bulk channel is MULTI-MODE / low-contrast dispersive to a small-signal probe — **no single high-Q (∼137) resonance**; the datasheet Measured-Q row stays UNTESTED. Consistent with (does not conflict) the apparatus-floors dispersion-contamination verdict; sharpens it with the frequency-resolved spectrum.
3. **FLAG (surfaced, not resolved):** an apparatus that could measure the 1/Q=α wall-transmission leak must separate wall transmission from bulk breather dispersion — a redesign (e.g., a boundary-localized reflection read at the Γ=−1 front, not a bulk-volume response). Surfaced for Grant/auditor; NOT auto-pivoted (Rule 16).
