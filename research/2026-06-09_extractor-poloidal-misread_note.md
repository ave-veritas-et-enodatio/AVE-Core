# Extractor poloidal-read characterization — when does a planted (2,3) read back wrong?

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-crystal-graft-v3` · **Lane:** implementer
**Probe:** [`src/scripts/vol_1_foundations/extractor_misread_probe.py`](../src/scripts/vol_1_foundations/extractor_misread_probe.py) (reads only; no fix)
**Why load-bearing:** a future TRUE (2,3) could be misread as a FAILURE. This is the
**instrument-side `ave-representation-capability-check`**: can `extract_2_3_omega` REPRESENT a
planted q=3 poloidal fibre across the configuration space, separated from the physics?

## Symptom
graft-v3's independence smoke plants a KNOWN (2,3) (`seed_omega_known_2_3`, R=0.22N=9.68, r=R/φ²=3.70)
and reads back **(2,1)** — the poloidal "3" collapses to 1. graft-v2's carrier-gate planted the SAME
(2,3) and read (2,3) at rel 0.80/0.59; the perf-utils fast extractor (bit-identical to the slow one)
also read planted-(2,3) correctly. The brief's premise was an EXTRACTOR misread at the planted read.

## Sweep (FRESH plant, real reads, no templated answer)
| config | R_plant | r_plant | R/r | amp | steps | read@ | (w_tor,w_pol) | rel(t,p) | pol_raw | is(2,3) |
|---|---|---|---|---|---|---|---|---|---|---|
| v2_path_findshell | 9.68 | 3.70 | 2.62 | 0.30 | 0 | findshell(9.72,3.71) | (2,**3**) | (0.80,0.59) | [2.99 ×12] | True |
| v3_path_planted_fresh | 9.68 | 3.70 | 2.62 | 0.30 | 0 | planted(9.68,3.70) | (2,**3**) | (0.75,0.61) | [2.99 ×12] | True |
| amp_lo_0.15 | 9.68 | 3.70 | 2.62 | 0.15 | 0 | planted | (2,**3**) | (0.75,0.61) | [2.99 ×12] | True |
| amp_hi_0.60 | 9.68 | 3.70 | 2.62 | 0.60 | 0 | planted | (2,**3**) | (0.75,0.61) | [2.99 ×12] | True |
| aspect_fat_Rr2.0 | 9.68 | 4.84 | 2.00 | 0.30 | 0 | planted | (2,**3**) | (0.77,0.62) | [2.99 ×12] | True |
| aspect_thin_Rr3.5 | 9.68 | 2.77 | 3.50 | 0.30 | 0 | planted | (2,**3**) | (0.76,0.59) | [2.99 ×12] | True |
| scale_mid_R6.6 | 6.60 | 2.52 | 2.62 | 0.30 | 0 | planted | (2,**3**) | (0.76,0.61) | [2.99 ×12] | True |
| **scale_small_fullrun_R2.9** | 2.92 | 1.11 | 2.62 | 0.30 | 0 | planted | (2,**2**) | (0.53,0.33) | [-1.0, 1.52, 1.52, …] | False |
| **v3_smoke_stepped500** | 9.68 | 3.70 | 2.62 | 0.30 | **500** | planted | (2,**1**) | (0.94,0.59) | [0.98 ×12] | False |

## Localized parameter (data-derived, FLAG: NOT the brief's premise)
Two DISTINCT effects, neither is an extractor misread of the FRESH planted (2,3) at the smoke geometry:

1. **The independence-smoke (2,1) is the 500-step DYNAMICS product, not the instrument.** At the
   IDENTICAL geometry, fresh read = **(2,3)** (poloidal raw ≈2.99); only after 500 live-buckle steps does
   it read **(2,1)** (poloidal raw ≈0.98). The live buckle overwrites the planted q=3 fibre into a q=1
   field; the extractor reads that EVOLVED field honestly. So graft-v3's SMOKE-4 "(2,1) robust" is the
   dynamics' product, **not** the planted (2,3) surviving — and **not** an extractor bug. (This refutes
   the brief's "EXTRACTOR-MISREAD at the planted read" framing — surfaced per flag-don't-fix.)
2. **The extractor's GENUINE capability limit is absolute contour-radius / SCALE.** Amplitude and R/r
   aspect are irrelevant (all read (2,3)); only when the minor radius drops to **r≈1.1 cells (the de-novo
   full-run torus R=2.9, r=1.1)** does the poloidal minor circle become under-resolved and the read
   collapses to (2,2)/garbage (rel 0.33, poloidal raw [-1.0, 1.52, …]). **This is the load-bearing one:**
   the full-run de-novo arms (which reported w_pol=0) are sampled at exactly this scale, so a TRUE (2,3)
   there could NOT have been resolved — the w_pol=0 read at R=2.9/r=1.1 is partly representation-limited,
   not purely physical.

## Follow-up spec (own gate; do NOT fix here)
- **Read the de-novo arms at a RESOLVED scale** (larger host torus or finer grid so r ≳ 3 cells, where the
  probe shows clean (2,3)), before concluding w_pol=0 is physical. Re-run the de-novo arms at scale_mid or
  larger and re-read.
- **Re-pose the independence test** to read the field BEFORE the buckle overwrites the fibre, or to measure
  fibre-SURVIVAL explicitly — the current SMOKE-4 conflates "ω independent of V" with "the planted fibre
  decayed under its own dynamics."
- Both the slow extractor and the bit-identical perf-utils fast extractor inherit the small-scale
  resolution floor; any fix must pass a **plant-(2,3)-at-de-novo-scale → read-(2,3) gate** (plant at
  R=2.9/r=1.1, require (2,3)) before it is trusted on the full-run arms.

**Skills fired:** `ave-driver-script-honesty` (every row a real read; the only printed "conclusion" is the
data-derived list of which configs read w_pol≠3); `ave-representation-capability-check` (instrument-side:
the extractor's q=3-representation capability is scale-bounded, r≳3 cells); `verify-before-cite` (v2
planted-read 0.80/0.59 + v3 planted geometry re-derived from the run, not session memory); `flag-don't-fix`
(the dynamics-vs-instrument divergence from the brief's premise surfaced, not silently reframed).
