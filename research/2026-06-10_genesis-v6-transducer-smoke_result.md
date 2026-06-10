# RESULT — Genesis-v6 PHASE 2 (D9): the CHIRAL-BOUNDARY TRANSDUCER smoke — THE GATE

**Date:** 2026-06-10
**Prereg (frozen, committed alone):** `research/2026-06-10_genesis-v6-transducer_prereg.md` §6 (the D9 smoke mini-prereg, frozen before this run)
**Driver:** `src/scripts/vol_1_foundations/genesis_v6_transducer_smoke.py` (serial, deterministic, seed `20260610`)
**Raw numbers:** `research/2026-06-10_genesis-v6-transducer-smoke_results.json` (read FROM it — ave-driver-script-honesty)
**Engine:** the v6 D9 additions (`transducer_on`, `chi_exch`, `transduce_axis`, `_transducer_step`); the inherited V/w/ω + bulk + snap path is byte-identical with `transducer_on=False` (default).
**Keepers:** `src/tests/test_unified_transducer_v6.py` (6 tests, incl. the F-PROBE m-even keeper); full unified suite 36/36 green.

---

## 0. HEADLINE — **TRANSDUCER-LIVE**

The component that blocked six architectures is BUILT and LIVE. The chiral wall couples the photon's
handedness into the bulk circulation — the channel v5 measured as **NEVER** coupling (four arms byte-identical).
Implemented as a **chiral boundary condition** on the `g_wall` shell (CP10 — ON the boundary, no bulk term):
per step it shuttles axial angular momentum from the photon's spin `S_φ=∫(w×∂_tw)·n̂` to the bulk orbital
circulation `L_bulk=∫ρ(r×u_adv)·n̂`. Every frozen gate criterion (§6.6 L1–L5 + D12) passes:

| gate check (frozen §6.6) | result |
|---|---|
| **L1** exchange above floor | ΔL_bulk(RH) = **−1.3008** vs F-EXCHANGE = **0** (structural zero) → ∞× floor ✅ |
| **L2** helicity-odd (sign reversal) | RH −1.3008 / LH **+1.3008**, **odd-fraction = 1.000** ✅ |
| **L3** depleting 1:1 + no pump | AM ratio **1.0** (exact); measured \|ΔS_φ\| = **1.301** ≫ F-DRIFT 1.6e-7; E_absorb **+0.319 ≥ 0** (passive) ✅ |
| **L4** achiral null + probe | achiral ΔL_bulk **= 0**; F-PROBE separates ±h (RH_seed −2.99 / LH_seed +2.99 / achiral 0) ✅ |
| **L5** coefficient/sharpness-robust | sign invariant across χ̃∈{9e-4…0.08} and wall_width∈{0.06,0.12,0.20}; total ΔL invariant to bounce_thresh ✅ |
| **D12(i)** RH≠LH within 200 steps | max\|u_RH−u_LH\|@200 = **2.7e-3 > 0** (live) ✅ |
| **D12(ii)** achiral known-null | \|ΔL_bulk(achiral)\| = 0 at floor ✅ |

---

## 1. THE OPERATOR (substrate-walked; derivation stated)

D9 = the **polar-conjugate of the snap reflector**. The snap makes the wall reflect the RADIAL pair
(`Z_bulk→0`); D9 makes the SAME wall **chiral** so it torques the ANGULAR pair per traversal (the ADD-2
compression→rotation buckle class, `crystal_engine.py:33-37`: a chirality-signed velocity-space rotation
conserving the conjugate pair — here applied to (photon spin ↔ bulk orbital) instead of (∂_tV, ∂_tw)).

- **CP10 (the load-bearing constraint):** the exchange acts ONLY on the `_wall_window()` g_wall shell,
  interior-masked, in `step()` AFTER the inherited substeps — NOT a term in any field's EOM. No bulk trilinear
  potential (the indefinite-Hamiltonian pump that detonated `photon_deplete=True` cannot recur).
- **Conservation BY CONSTRUCTION (ave-representation-capability-check (C)):** per step the wall (1) extracts
  per-cell spin `Δs=χ̃·g_wall·s_density` by scaling `π_w←π_w·(1−χ̃·g_wall)` — `s_density=(w×π_w)·n̂` is LINEAR
  in π_w so the removed spin is EXACTLY `δL=Σ Δs·dV`; (2) deposits exactly δL into `u_adv` as a wall-localized
  azimuthal `δu=Ω_add·(n̂×r)·g_wall`, `Ω_add=δL/I_wall`. **AM ledger closes 1:1 (ratio = 1.0, exact)** —
  bounded, depleting, no refilled source.
- **The derived coefficient:** the FORM ∝ κ̃·h·g_wall·spin is ADD-2; the residual magnitude is the swept χ̃.
  The κ̃-anchored value `χ̃_κ = κ̃·dt·(c_T·k) = 9.0e-4` is run as a sweep point (it transduces cleanly too,
  ΔL = −0.310). The verdict is **coefficient-robust** (sign/oddness/null invariant; small-χ̃ early-window
  rate ∝ χ̃; cumulative saturates as the finite photon depletes — the bounded-source signature).

---

## 2. THE FIVE MEASUREMENTS — REAL NUMBERS (N=40, 600 steps, seed 20260610)

**(i) exchange / per-bounce.** ΔL_bulk(RH) = **−1.3008**, infinitely above the **structural-zero** F-EXCHANGE
(with χ̃=0 the transducer no-ops and nothing else sources `u_adv` ⇒ ΔL_bulk ≡ 0 bit-exactly).
**§210 DEVIATION (stated, not papered over):** at the CFL dt = 1.73e-3 the photon is quasi-static over the
window (travels < 1 cell), so `I_wall(t)` **monotone-DECREASES** (0.290 → 0.0053, a 55× drain — the
continuous-depletion signature) with **no discrete bounce-peaks ⇒ n_bounce = 0 at every swept threshold**.
The interaction is CONTINUOUS spin-extraction from the co-located packet, not ballistic bounces; the headline
is the continuous analog **d(L)/d(step) = −2.17e-3** and the total ΔL = −1.3008. The bounce_thresh sweep still
serves its §210 purpose: total ΔL is **threshold-INVARIANT** (the count knob is cosmetic, as predicted).

**(ii) RH-vs-LH sign reversal (helicity-odd).** RH = −1.30084, LH = +1.30084 → **odd-fraction 1.000**, exact
sign reversal. Quantitatively perfect because `s_density ∝ −h` flips with handedness and the deposit is linear.

**(iii) photon helicity ledger depleting 1:1.** AM ledger ratio (removed/transferred) = **1.0** (exact, by
construction). Independently, the photon's MEASURED axial spin depletes \|ΔS_φ\| = **1.301**, ≫ the F-DRIFT
free-propagation floor (1.6e-7) — genuine field depletion, not a ledger artifact. **No pump:** the photon pays
`E_photon_loss = 0.3197`, the bulk gains `E_bulk_gain = 2.4e-4`, the remainder `E_absorb = +0.3195 ≥ 0` goes
to the passive lossy-mirror sink (the wall absorbs, never creates — ave-conserved-vs-pumped on the transducer).

**(iv) achiral null.** helicity=0 (linear-pol) ⇒ `S_φ ≡ 0` structurally ⇒ ΔL_bulk = **0** exactly (no transfer,
no events). The known-null is from the FIELD, not dialed.

**(v) knob sweeps (§210 — every D9 knob inventoried + swept).**

| knob | sweep | finding |
|---|---|---|
| `chi_exch` | {0, 9e-4(κ̃), 0.005, 0.02, 0.08} | ΔL = {0, −0.310, −0.912, −1.301, −1.580}; **sign invariant**, monotone, saturating (depletion). |
| `wall_width` | {0.06, 0.12, 0.20} | ΔL = {−0.693, −1.301, −2.075}; **sign invariant** (broader shell → more transfer — reported). |
| `bounce_thresh` | {1.2, 1.5, 2.0} | n_bounce = {0,0,0}; **total ΔL identical** across all → the count is cosmetic. |
| `axis` (n̂) | {x, y, z} | ΔL = −1.3008 for all three — operator is axis-isotropic (sanity). |

---

## 3. PROBE-CAPABILITY + KEEPERS (ave-apparatus-floor-attribution v1.1)

- **F-PROBE (the m-even keeper):** the spin probe `photon_spin_axial` separates ±helicity on a KNOWN seed
  BEFORE any dynamics — RH_seed = −2.994, LH_seed = +2.994 (opposite sign), achiral = 0. A probe that could
  not distinguish ±h would have DISQUALIFIED the smoke (CLIP). Encoded as
  `test_v6_transducer_probe_separates_helicity_m_even_keeper`.
- **Defaults-OFF keeper:** `transducer_on` defaults False ⇒ ledgers zero, `u_adv` unsourced (the inherited
  byte-identical path); the 30 inherited unified-engine tests stay green.
- **Floors are STRUCTURAL zeros:** F-EXCHANGE = 0 (χ̃=0 ⇒ no source) and F-DRIFT = 1.6e-7 (free spin drift).
  Every positive is gated against them; the signal is ∞× / 8e6× above floor respectively.

---

## 4. SCOPE + DISCIPLINE

- **This is the GATE.** PHASE 2 TRANSDUCER-LIVE → the Run phase (the full T1–T6 spec-sheet matrix) is
  UN-gated. The smoke does NOT promote the electron claim — **NOT-ELECTRON stands** (v5 panel ruling). It
  builds + certifies the missing PRIMITIVE only (A44: an engine coupling-family gap, not a missing axiom).
- **CP10 honored throughout:** the coupling lives ON the boundary. No bulk term was added (the v5 detonation
  lesson). The transducer is bounded + depleting + passive — the depleting coupling the BEMF smoke demanded,
  achieved at a boundary not in the bulk.
- **phase-space-coordinate-check:** S_φ and L_bulk are REAL-SPACE axial angular momenta (the native coordinate
  for an AM-transfer claim); no winding/φ² claim is made here, so no Park-along-contours extractor is invoked.
- **Open items surfaced (flag-don't-fix; the auditor lands any manual entry):**
  1. The per-bounce metric (i) is degenerate at CFL dt (continuous drain, not ballistic bounces) — a discrete-
     bounce demonstration would need ~100× more steps or a larger-dt config; not required for the gate.
  2. The recipient here is the advective `u_adv` bulk circulation; the Cosserat-ω recipient (the canonical
     winding/charge) is left as the natural next channel (the Run phase wires ω back on).
  3. The energy ledger is passive (E_absorb ≥ 0) but NOT conservative — the lossy chiral mirror absorbs the
     photon's residual energy beyond the transferred AM; tracked, bounded, never a pump (D11 discipline holds).
