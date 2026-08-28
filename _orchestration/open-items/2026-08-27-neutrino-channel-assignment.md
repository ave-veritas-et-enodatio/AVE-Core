---
id: neutrino-channel-assignment
title: "Does canon assign the neutrino to the scalar (1/7) matter channel? It gates the SN1987A falsifier"
status: OPEN
owner: unassigned
opened: 2026-08-27
source: manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md
anchor: "A fast-moving massive particle is an isotropic 3D volumetric wave packet"
---

Surfaced by the `L1-group-vs-phase` lane; the arithmetic was redone independently
by the `two-knob-gravity-repair` lane with a different method.

**The falsifier this gates.** From `ω² = c_eff²k² + Ω²`, the gap drops out as
`ω ≫ Ω`, so an ultrarelativistic massive packet must asymptote to its own
channel's massless ray. In closed form,
`α·b/(GM/c²) = 2a₁ + 2b₁(1/β² − 1) → 2a₁`. **Canon's matter channel has `a₁ = 1`
and its light channel `a₁ = 2`, so a massive packet deflects at exactly HALF the
photon value forever** — `2.000400` vs `4.000400` (GR) at `v = 0.9999c`. This
depends on `a₁` alone: not on `b₂`, not on the two-knob repair, not on the
missing photoelastic map.

**The observational test, with the method stated.** Using a flat rotation curve
(`v_c = 220 km/s`), the index argument `U = GM(<r)/(c²r) = (v_c/c)² = 5.385e-7` is
**constant along the path** — so the estimate needs no enclosed-mass guess. Over
51.4 kpc: photon potential-delay excess `65.95 d`, AVE-matter excess `32.97 d`,
**predicted ν-vs-γ differential `32.97 d = 791 h` against an observed offset of
~3 h.** The model-free version, which is the one to quote: AVE predicts a **50%**
fractional difference in the two species' gravitational delay; SN1987A bounds it
at `3h / 65.9d ≈ 2e-3`. **The mass model cancels out of the fraction.**

**The open question.** The coupling-selection rule is canon's, verified verbatim
at `double-deflection.md`:20: *"A fast-moving massive particle is an isotropic 3D
volumetric wave packet carrying finite rest energy. It couples to the *scalar*
(isotropic bulk) component of the lattice strain via the 1/7 volumetric
projection."* A neutrino has rest mass, so by that rule it takes `n = 1 + U`.
**But no leaf found assigns the neutrino to a specific AVE channel.**
`neutrino-flavor-mixing.md`:12 treats MSW as *"impedance-dependent mode coupling
between propagation channels"* without naming which channel carries the free
neutrino. *(Method: two independent searches over the worktree at `a3f4fef7`;
blind spot — single-line regex, sibling repos not searched.)*

**Why it matters, and why it does not rescue anything.** If AVE's neutrino is not
an A1-massive packet, SN1987A stops being the cheap data point. **The structural
defect survives regardless**, because the theorem is about any massive packet —
the same factor of 2 applies to a `0.9999c` electron or proton, and the same
`n_matter/n_light = 1/2` applies to the Shapiro-class delay of any of them.

**Corpus state:** two independent search methods return **0 files** for `1987A`
and `sn1987` anywhere in AVE-Core at `a3f4fef7`. This test appears nowhere in the
corpus.
