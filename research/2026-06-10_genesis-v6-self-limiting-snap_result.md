# RESULT — Genesis-v6 JOB 2 (D10): the self-limiting snap, BOTH renderings

**Date:** 2026-06-10
**Prereg (frozen, committed alone):** `research/2026-06-10_genesis-v6-transducer_prereg.md` @ `fa4420c6`
**Driver:** `src/scripts/vol_1_foundations/genesis_v6_self_limiting_snap.py` (serial, deterministic, seed `20260610`)
**Raw numbers:** `research/2026-06-10_genesis-v6-self-limiting-snap_results.json` (read FROM it — ave-driver-script-honesty)
**Engine:** the v6 D10 additions (`vent_mode="absorbed"`, `meissner_harden`); v5 path byte-identical by default.

---

## 0. HEADLINE

**Both self-limiting renderings BUILT and demonstrated on the v5 cascade config; both PRESERVE the D6
birth-flash.** The run also isolates a load-bearing structural fact: **the v5 "deflagration" is TWO coupled
failures on TWO channels** — the POCKET cascade (bulk ρ̄) and the E_V detonation (the seed-V breather) —
and **each rendering bounds a DIFFERENT channel.** The full self-limiting object combines them.

---

## 1. THE TWO CHANNELS + THE TWO RENDERINGS — REAL NUMBERS (F-EV = 13; deflagration = ≥ 10×)

| arm | vent | meissner | pocket_max | E_V_max | max\|V\| | E_V bounded? |
|---|---|---|---|---|---|---|
| **BASELINE_v5_cascade** | kick | 0 | **5968** | **50 339** | 5.55 | ❌ (3 870×) |
| **(a) A_vent_absorbed** | absorbed | 0 | 5256 | **13.1** | 0.32 | ✅ |
| **(b) B_meissner_0.02** | absorbed | 0.02 | 1912 | 13.1 | 0.32 | ✅ |
| **(b) B_meissner_0.05** | absorbed | 0.05 | **1704** | 13.1 | 0.32 | ✅ |
| **(b) B_meissner_0.10** | absorbed | 0.10 | 1704 | 13.1 | 0.32 | ✅ |
| B_meissner_0.00 (keeper) | absorbed | 0 | 5256 | 13.1 | 0.32 | ✅ (= (a), no hardening) |
| **DIAG_meissner_0.05_kick** | kick | 0.05 | **1704** | **11 558** | 2.69 | ❌ |

- **Rendering (a) VENT-ABSORBED bounds E_V (the breather channel).** The vented latent goes to a
  conservative store (`E_vent_absorbed`) instead of a `∂_tV` kick → no breather → `E_V` flat at 13.1,
  `max|V|` 0.32. The POCKET cascade still runs (5256) — (a) does not address the bulk-ρ̄ channel.
- **Rendering (b) MEISSNER-HARDENING bounds the POCKET (nucleates-and-stops).** Each snapped cell lowers
  its neighbors' snap threshold; the cascade front needs ever-deeper deficits and STALLS — pocket
  `5256 → 1704` (a 3× containment; saturates by increment 0.05). Paired with the absorbed vent, BOTH
  channels are bounded (E_V 13.1 AND pocket 1704). `meissner_harden=0` reproduces the full pocket (the
  keeper / known-different reference).
- **CHANNEL SEPARATION (diagnostic, reinforces D11):** Meissner WITH the kick vent bounds the pocket
  (→ 1704) but **E_V STILL detonates (→ 11 558)**. The deep-saturated seed breather is hypersensitive to
  ANY vent kick — the E_V channel is the VENT (JOB-1 finding), not the pocket. **Meissner alone cannot
  bound E_V; it must be paired with the vent-absorbed fix.** (This is why the directive's two renderings
  are complementary, not redundant.)

## 2. THE BIRTH-FLASH IS PRESERVED (the known-positive — F-BURST gate)

F-BURST floor (free-run, no-snap scatter, inherited F0d) = `3.84e-5`; gate = floor×3 = `1.15e-4`.
A single hand-snap emits a burst clearing the gate by **4–5 OOM** under EVERY rendering:

| rendering | released | clears floor×3 |
|---|---|---|
| A_vent_absorbed | `3.47` | ✅ |
| B_meissner_0.05_absorbed | `3.47` | ✅ |
| legacy_v5 | `7.53` | ✅ |

The deflagration fix does NOT over-correct: the D6 birth flash (the snap's certified role) survives intact.

## 3. VERDICT

- **(a) vent-absorbed:** bounds the **E_V** (breather) channel. ✅
- **(b) Meissner-hardening (+ absorbed vent):** bounds the **POCKET** channel (and E_V via the absorbed
  vent). ✅ Best increment 0.05 (pocket 1704, saturated).
- **Both preserve the birth flash.** ✅
- **The self-limiting snap = (a) ⊕ (b):** the vent-absorbed kills the energy pump; Meissner makes the
  condensation nucleate-and-stop. Each is necessary for a DIFFERENT failure mode; together the cascade is
  contained on both channels with the birth flash intact.

## 4. FLAGS (flag-don't-fix)

1. **The pocket still reaches 1704 (≈ 33 % of the v5 5256) even at high hardening.** Meissner contains, it
   does not eliminate, the bulk-ρ̄ cascade at this M=1.8 reach — a finite nucleation radius, not a point
   snap. Reported, not tuned away. (The hardening increment is the control knob, swept; its value is
   engineering, not physics — ave-apparatus-floor-attribution.)
2. **This is hygiene, not an electron claim.** The renderings make the snap a well-behaved birth-flash
   mechanism (D-PERM: the snap is NOT the lock; the circulation is). The NOT-ELECTRON verdict is unchanged.
3. **Corpus-state delta (auditor lands):** the v5 "E_V 3 870× cascade / deflagration" is now resolved into
   two channels with two complementary self-limiting fixes; the genesis arm's D10 gate is satisfiable.
