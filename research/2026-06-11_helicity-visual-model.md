# Helicity visual model — metaphor map, corpus anchors, test hooks

**Date:** 2026-06-11  
**Lane:** orchestration / framing (not canon)  
**Status:** Grant visual-intuition capture — **hypothesis-class** where marked  
**Companion:** `research/2026-06-11_chiral-vacuum-reactor-framing.md` §3; D1 epic `_orchestration/2026-06-11_lattice-d1-test-gated.md`

---

## Purpose

Lock Grant's physical picture of **how a photon gets helicity** into testable language: what is metaphor, what is corpus, what is already measured, what needs a prereg.

---

## The cartoon (one glance)

```
Launch:  linear pol (h=0)  +  direction only
              │
              ▼
Cold lattice "slats" — bond LC tanks, scatter+connect at each ℓ_node pitch
              │
              ▼  conjugate reflection each hop
Transverse frame rotates along path  →  acquired helicity
              │
              ▼  (optional) saturation Op14
Local ε, μ warp; S_μ ≠ S_ε if ω helical
              │
              ▼  (separate story)
Bound CVR traps (electron) vs Γ=−1 horizons (particle/BH class)
```

**Identity (Grant-ratified, consistency-class):**

> **helicity sign ∝ enantiomorph × launch-direction**

---

## Metaphor map — keep / tighten / defer

| Visual image | Tight corpus read | Tag |
|--------------|-------------------|-----|
| **Diamond-ish voxel walls** | One ℓ_node cell; **engine** = 4-port tetrahedral junction (~109°). **D1 open:** srs = 3-port, 120°, girth-10 rings. "Walls" = bond stubs, not solid facets spinning. | [mixed — engine cartoon / D1 open] |
| **Slats + conjugate reflection** | Scatter+connect TLM; each bond event rotates transverse frame (Bishop / vector-TLM in Phase-1). | [Grant-ratified §3 CVR doc] |
| **Walls spin on corners** | **Do not read literally.** Split: (1) Cosserat **ω** at node, (2) **T** tetrahedral symmetry on ports, (3) **polarization frame** transport. | [metaphor → three objects] |
| **Warp / deflect under saturation** | Op14 `S(A)=√(1−A²)`; local-clock modulation; asymmetric `S_μ,S_ε` with `κ·h_local`. Cubic 6/8/12 at saturation (T_d). | [corpus — vol1 cubic anisotropy] |
| **Electron = mirror / well** | CVR floor: reactive trap, **Z_eff→0**, **Γ→−1** at core (Meissner/dielectric snap). α = leakage per cycle. Phase-space **(2,3)** winding — not a real-space screw crushed shut. | [corpus EE register] |
| **BH = opposite — melt / flip handedness** | **Defer.** Both electron core and horizon class can show **Γ=−1**, but **different mechanisms**. Gravity well = **symmetric** strain, **Z=Z₀** (stealth). Not "LH-only valve into inverted crystal." | [hypothesis-class — see T4 prereg] |
| **Inverted crystal** | Candidate meanings: (a) **mirror enantiomorph** (matter/antimatter), (b) **excited κ decoration** on achiral net (D1-B arm). Must not merge without a gate. | [open — test-gated] |

---

## What is already measured

| Observable | Result | Class |
|------------|--------|-------|
| Ring writhe srs-R/L | ±4.09×10⁻²; diamond 0 | Phase-0 geometric source |
| Bishop Δθ/L along srs screw | ±75.46°/unit; mirror-odd; diamond 0 | Phase-0 **kinematic** (not dynamical packet) |
| R3 decoration vs srs | κ flips sign; ρ≈0.057% of srs Bishop | D1 **partial A** |
| Dynamical photon helicity | **Not measured** | Phase-1 P2/P4/P6 |
| BH changes photon helicity sign | **Not measured** | T4 prereg DRAFT |

---

## Test hooks (linked work)

| ID | Question | Vehicle |
|----|----------|---------|
| **T1** | Does a **linear** launch acquire signed dynamical rotation? | v9 Phase-1 **P2, P4, A2** (reversed direction) |
| **T2** | Does precursor **self-trap** chiral + persistent (CVR-SET)? | v9 Phase-1 **P6** bins |
| **T3** | Does saturation warp rotation rate vs `√(1−A²)`? | Phase-1 Op14 amplitude sweep (named, not separate prereg yet) |
| **T4** | At **Γ=−1** boundaries, is helicity **reflected/absorbed** vs **sign-flipped**? | `research/2026-06-11_electron-mirror-vs-bh-helicity_prereg_DRAFT.md` |
| **T5** | Structural vs decoration lattice | R3 done (partial); Phase-1 completes |

---

## Honest limits (do not upgrade)

1. Phase-0 Bishop is **kinematic** — frame along fixed helix, not vector-TLM packet (`CVR` §3.3).
2. Single screw-ray is **handedness-ambiguous**; signed channel = **writhe** or **enantiomorph-pair × direction**.
3. Helicity **quantization** is Phase-1 open (`Δθ_pol/L` spectrum vs launch).
4. This doc is **not** a D1 ruling and **not** axiom text.

---

## Proposed default Phase-1 thresholds (delegated from Phase-0 floors)

For Grant ratification at freeze — same numbers as v9 DRAFT placeholders unless amended:

| Gate | Threshold |
|------|-----------|
| P1 energy drift | ≤ 1e-8 relative |
| P2 enantiomorph sum | \|sum\| ≤ 10% of \|srs\| |
| P2 diamond control | ≤ 5% of \|srs\| |
| P5 persistence | N_steps ≥ 500, N_grid ≥ 32³ (implementor may use srs scaffold grid first) |
| P6 localization plateau | RMS radius change \< 5% over last 100 steps after transient |

Framing (A) vs (B) **excluded** from freeze per D1 test-gated epic.
