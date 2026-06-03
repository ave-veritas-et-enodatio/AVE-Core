# Prereg: Spinning Chiral Impedance-Matched Antenna — rotation × chirality cross-term

**Status:** SCOPING (2026-06-03). Corpus-grep dispatched (`ave-corpus-grep`, AVE-Core + AVE-HOPF + AVE-PONDER).
**Lane:** experimental-protocol revamp — the chiral pivot off the retired density-coupled Sagnac-RLVE.
**Origin (Grant 2026-06-03):** the density-coupled rotor-Sagnac retired (achiral, GR-shared, RLG-excluded). The live question: does a **chiral** impedance-matched coupler — which touches the substrate's AVE-distinct chirality, not its GR-shared density — gain a *discriminating frequency-domain signature* when spun?

## Target (precise)
Derive whether a spinning chiral (torus-knot) impedance-matched antenna hosts an AVE-native **rotation-rate × chiral-coupling cross-term** — a sideband at (chiral resonance ± ω_spin) — that (a) exists in the K4-Cosserat substrate AND (b) classical rotating-antenna EM cannot reproduce. If both, it is a new frequency-domain chiral discriminator, extending HOPF's static enantiomer-sign + medium-independence legs into the frequency domain.

## Physical picture (mechanical, pre-math)
- A chiral torus-knot antenna couples to the substrate's chiral mode (K4→A4→2T⊂SU(2); chiral Meissner κ_chiral) — the parity-odd, AVE-distinct channel. GR/classical EM have no parity-odd vacuum coupling. (The HOPF principle.)
- "Impedance-matched" = Op3 Γ→0: dump energy *into* the chiral lattice mode rather than reflect it. Observable = the chiral resonance shift/loss.
- Spinning the antenna at ω_spin rotates its helicity-projection axis → modulates the chiral coupling at ω_spin → a sideband at (chiral-resonance ± ω_spin).
- Candidate AVE source of a *rotation-dependent* term: the chiral-Meissner helicity h = ω·(curl ω); a mechanically rotating chiral structure sweeps h, feeding a cross-term.
- **Discriminator bar:** a *classical* rotating chiral antenna ALSO throws sidebands (rotating-frame / geometric-phase). The AVE term must DIFFER — in scaling, sign-under-spin-reversal, or magnitude.

## Corpus-grep (DISPATCHED 2026-06-03 — results fill this section)
Inventory prior work on: (1) rotation × chirality coupling in K4-Cosserat; (2) the chiral Meissner (κ_chiral, S_μ/S_ε) under mechanical rotation; (3) spinning/rotating chiral solitons or antennas, geometric/Berry phase, spin-modulated coupling; (4) the HOPF chiral-coupling derivation (Δf = α·pq/(p+q)) and any rotating-frame extension; (5) Cosserat micro-rotation (ω) coupling to mechanical rotation; helicity h = ω·(curl ω) under spin; (6) any "rotating antenna" / "modulated chiral" / "parity chopper" treatment. [PENDING.]

## Discriminating outcomes
- **A (LIVE):** AVE rotation×chirality cross-term exists AND differs from the classical rotating-chiral-antenna baseline (sign-flip under spin-reversal, or AVE-specific scaling) → new frequency-domain chiral discriminator. Scope a bench (spin-modulated HOPF).
- **B (READOUT-ONLY):** cross-term exists but matches the classical baseline → spinning is only a parity-chopper readout enhancement for the static HOPF chiral signal; no new discriminator.
- **C (NULL):** the chiral coupling picks up no rotation-dependent term → spinning adds nothing beyond modulation.

## Falsifier
If the AVE rotation×chirality term equals the classical rotating-chiral-antenna sideband (same scaling + sign), it is not AVE-distinct (Outcome B). The chirality *channel* is AVE-distinct; the open question is whether ROTATING it adds a discriminator or merely a chopper.

## Discipline
`ave-prereg` (this doc) · `substrate-native-check` (K4-Cosserat rotating-frame — a genuine cross-term vs an SM-imported geometric phase?) · `ave-discrimination-check` (the classical rotating-chiral-antenna counterfactual is the bar) · `ave-canonical-leaf-pull` (chiral Meissner, Op3 matched-coupling, HOPF antenna-Q leaves) · `ave-ee-intuition-summary` (the deliverable gets a 5-beat summary).
