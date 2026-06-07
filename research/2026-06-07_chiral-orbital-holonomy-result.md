# Chiral Orbital Holonomy — does a loop orbiting a host K4 node accumulate a ½-twist (π) per orbit?

**Status:** RESULT (standalone geometric diagnostic, no genesis sim).
**Date:** 2026-06-07.
**Branch:** `analysis/2026-06-07-chiral-holonomy-half-twist`.
**Driver:** [`src/scripts/vol_1_foundations/chiral_orbital_holonomy.py`](../src/scripts/vol_1_foundations/chiral_orbital_holonomy.py).
**Viz:** `src/scripts/vol_1_foundations/_output/chiral_orbital_holonomy.png` (viz-candidate #1/#6).
**Classification (`consistency-vs-emergence`):** EMERGENCE test as framed; result lands **CONSISTENCY-class** (see §6).
**Verdict:** **(II) — suggestive, not topological.** A clean π half-twist (SU(2) `-I`) is realizable and *requires* the chiral port structure, but it is **path-dependent** (conditional on the orbit encircling a chirality-induced orientation degeneracy), not a robust topological invariant of "orbiting the host."

---

## §1 Claim under test (Grant's picture)

The electron loop orbits ONE host K4 node (host = the loop's axis). The loop body is interstitial (Meissner-expelled, radius `r`). The host's chiral K4 neighbours impart a *differential* tension that sets the loop's preferred orientation. As the loop orbits (azimuth 0→2π) its frame is parallel-transported in the chiral neighbour field. **Claim: holonomy per orbit = π (a ½-twist) → 720° to return → spin-½ emerges geometrically from crystal chirality.** Secondary: the real-space orbit+twist path, projected from the host, looks like a `(2,3)` trefoil.

This fills the gap explicitly flagged open in the corpus:
- [`finkelstein-misner-spin-half-derivation.md` §8](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) (clm-salw2h): "**Does NOT** provide a discrete-lattice computation of the Finkelstein-Misner kink on K4 … flagged as open work for a future Phase."
- [`k4-rotation-group.md` §5](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) (clm-7pvh9i): "if we restrict to rotations only (T = A₄), A and B sublattices are preserved separately. To get an A↔B SWAP (needed for the bipartite-spinor argument leading to spin-½), we need to include reflections (full T_d) **or some other physical mechanism**." Orbital encircling is a candidate for that "other mechanism."

## §2 Method (substrate-native — `substrate-native-check`: this is HOLONOMY / parallel transport, NOT energy-min)

- **Canonical geometry (not invented).** Host's four neighbours sit along the canonical port vectors `p₀=(+1,+1,+1) p₁=(+1,−1,−1) p₂=(−1,+1,−1) p₃=(−1,−1,+1)` ([`k4_tlm.py:359-362`](../src/ave/core/k4_tlm.py) `_connect_all` A→B directions; same basis as `k4-rotation-group.md`). These four form a **regular tetrahedron** — geometrically **achiral** at a single node (`k4-rotation-group.md` §1). Port handedness ([`k4_tlm.py:542`](../src/ave/core/k4_tlm.py) `get_helicity_density`): ports {0,2} right-handed, {1,3} left-handed → handedness signs `s = (+1,−1,+1,−1)`.
- **The connection.** At azimuth φ the loop sits at `p(φ) = r·ê(φ)` (host at origin). Its preferred orientation is the rotation `R(φ) ∈ SO(3)` that best-aligns the canonical reference tetrahedron `{p_j}` to the bond directions `{b_j(φ)}` seen from the loop (Wahba/Kabsch attitude from vector observations). This is "the orientation set by the local neighbour directions" — **no energy functional, no free parameter**.
- **Parallel transport = continuous SU(2) lift.** `R(φ)` is lifted to a unit quaternion `q(φ)` with the sign chosen to stay continuous. After one orbit the frame returns geometrically (`R(2π)=R(0)`); the lift returns to `+q(0)` (holonomy 0) or `−q(0)` (holonomy π = ½-twist). The `±` sign is the Z₂ homotopy invariant of π₁(SO(3)) = Z₂.
- **Chirality knob.** Handedness anisotropy `w_j = 1 + ε·s_j` in the alignment; `ε=0` is the achiral regular-tetrahedron control, `ε>0` injects the engine's port-pair handedness (Σ s_j p_j = (0,4,0) ⇒ a chiral axis along ŷ).
- **Sweeps:** orbit radius `r`, orbit-plane normal, chirality `ε`, and `n_steps` (resolution), plus a 400-orbit random scan.

## §3 Primary result — the holonomy number(s)

| Probe | Result |
|---|---|
| Holonomy value, when present | **clean SU(2) `−I` (dot(q(2π),q(0)) = −1.0000 to 4 d.p.)** — i.e. exactly π. Never a fractional angle. |
| `n_steps` robustness (256→4096) | `−I` stable; step-jump → 0 (0.21→0.013). The π is a **genuine smooth-transport Z₂ holonomy**, not a discretization artifact. |
| Double-cover (2 orbits = 4π) | `q(4π) = +q(0)` everywhere ✓ — 720° returns, consistent with spin-½. |
| Achiral regular tetrahedron (ε=0), 400 random orbits | **−I fraction = 0/400 (0%).** A half-twist NEVER appears without chirality. |
| Chiral (ε=0.6), 400 random orbits | **−I fraction = 127/400 (32%);** 123/400 with clean smooth transport. |
| Radius sweep, non-encircling plane (chiral-ŷ, ε=0 & 0.6) | `+I` for ALL r (no twist), robust. |
| Radius sweep, z-plane, ε=0.6 | `+I` for r<~0.95, `−I` for r>~0.95 (orbit crosses the degeneracy locus). |
| ε sweep at z-plane, r=1.0 | ε=0,0.3 → `+I`; ε=0.6,0.9 → `−I`. Chirality threshold flips the sign. |

**Reading:** the loop's orientation field has **degeneracy points** (Wahba singular-value gap → 0) sitting near the neighbour/port directions (lowest-gap direction has cos 0.93 to a port vertex at r/bond=1.0). Orbits that **encircle** a degeneracy pick up `−I` (π); orbits that don't pick up `+I` (0). The +I↔−I boundary is exactly where an orbit passes *through* a degeneracy (tilt 45°: gap 0.68→0.13, a 2.34-rad branch jump). This is the **generic Berry-phase-by-encircling / Dirac-monopole mechanism**, instantiated on the canonical K4 neighbour geometry.

**Is it π? Robust/topological or path-dependent?**
- The value, when it appears, is **exactly π** (clean Z₂ `−I`, n_steps-robust) — not some tuned fractional angle. The SU(2) double-cover is genuinely realized.
- **Chirality is NECESSARY:** the achiral regular tetrahedron yields a half-twist for *zero* of 400 orbits. This is real support for the qualitative "chirality enables spin-½" picture.
- **It is NOT robust/topological across orbits:** with chirality on, only ~32% of orbits give π; the rest give 0. Which one is set jointly by orbit plane + radius + ε (whether the orbit encircles the chirality-induced degeneracy). There is **no plateau where every orbit gives π**.

## §4 Secondary result — projected path / winding (the `(2,3)` trefoil claim)

Real-space marked-point trajectory (orbit + accumulated frame twist), traced over 2 orbits, measured winding `(p, q)`:

| Orbit plane | twist / orbit | measured (p, q) |
|---|---|---|
| chiral-ŷ (+I) | +0.0001 π | (2, 0.00) |
| z-axis (−I) | **+1.30 π** | (2, **1.30**) |
| x-axis (−I) | **+1.42 π** | (2, **1.42**) |

The twist winding is **non-integer and plane-dependent (~1.3–1.4)**, NOT 3. **The projected path is NOT a `(2,3)` torus knot.** The continuous twist rate is set by the geometric-phase rate (path-dependent), not pinned to a topological 3. What sets the (non-)winding numbers: `p=2` is the orbital cycle count over the 4π closure; the second number is the *continuous* geometric-phase twist, which is not quantized and not 3.

**Coordinate-discipline note (`phase-space-coordinate-check`):** the canonical `(2,3)` winding is **phase-space** (Clifford torus in `(V_inc, V_ref)`, seeder Layer 3). This test measures the **real-space** projected path. A real-space non-`(2,3)` therefore does **NOT** contradict the canonical phase-space `(2,3)` winding — they are different coordinate systems. The real-space `(2,3)`-trefoil secondary claim (a real-space claim) is **not supported** by this diagnostic.

## §5 What this does and does not say about the corpus (flag-don't-fix)

- **No contradiction with the canonical spin-½ (FM / gyroscopic-isomorphism).** That mechanism is a **real-space rotation of the extended unknot** (clm-salw2h), not orbital encircling; it is untouched. This diagnostic addresses the *separate, explicitly-open* discrete-lattice/orbital question.
- **Consistent with — and sharpens — the corpus's own caveats.** `k4-rotation-group.md` §5 says pure rotation needs "reflections or some other physical mechanism" for the A↔B/spinor swap. Finding: orbital encircling is a *candidate* "other mechanism" that **can** produce the `−I` sign, **but only conditionally** (encircling), so it does not by itself convert the open caveat into a clean unconditional derivation. The corpus caveat stands.
- **Chirality dependence is the substantive new datum:** the half-twist is *necessary*-on-chirality (0/400 achiral) yet *path-dependent* even with chirality — a more precise statement than the corpus currently carries.

## §6 Verdict + classification

**Verdict (II): suggestive, not topological.** The chiral K4 neighbour geometry **can** host a clean π half-twist (SU(2) `−I`, n_steps-robust, double-cover consistent), and that half-twist **requires the chiral port structure** (achiral → 0/400). But the π is **path-dependent** — the generic Berry-phase-by-encircling, conditional on the orbit encircling a chirality-induced orientation degeneracy (~32% of orbits). It is **not** the path-independent "every orbit returns π / 720° to close" topological invariant that verdict (I) requires.

**`consistency-vs-emergence` → CONSISTENCY-class.** The geometry is *consistent* with hosting a chirality-required π half-twist; spin-½ does **not robustly/inevitably emerge** from orbiting per se. The strong emergence headline ("spin-½ emerges geometrically from crystal chirality, for every orbit") is **not supported**; the weaker, honest statement — "chiral K4 geometry can host a chirality-required π half-twist for encircling orbits" — **is**.

## §7 Load-bearing limitation / the open physics question (`pre-test-physics-check`)

The single-host neighbour set is a **regular tetrahedron — geometrically achiral** (`k4-rotation-group.md` §1). The chirality injected here (`w_j = 1+ε·s_j`) is a **reflection-even scalar anisotropy** along the port-pair axis ŷ, NOT a manifestly reflection-odd I4₁32 handedness. The *true* crystal chirality of the chiral Laves/K4 net lives in the **second shell** — the screw relation between the A- and B-sublattice tetrahedra — which a single-host model does not capture. So this diagnostic establishes:
- the orbital-encircling mechanism is real and produces a clean π,
- it requires the engine's port-pair handedness construct,

but it **cannot** decide whether a *true* 2nd-shell I4₁32 screw would make the π **robust/topological** (path-independent) rather than encircling-conditional. **That is the next test** (and the one that would actually adjudicate verdict I vs II for the chirality claim): repeat the holonomy on a 2nd-shell screw geometry, not a single achiral host tetrahedron + anisotropy knob. This echoes the `substrate-native-check` flag already raised in [`research/2026-06-03_spinning-chiral-coupling-prereg.md`](2026-06-03_spinning-chiral-coupling-prereg.md) (internal-chirality vs the modelled quantity — "a genuine cross-term vs an SM-imported geometric phase?").

## §8 Files

- Driver: [`src/scripts/vol_1_foundations/chiral_orbital_holonomy.py`](../src/scripts/vol_1_foundations/chiral_orbital_holonomy.py)
- Visualisation: `src/scripts/vol_1_foundations/_output/chiral_orbital_holonomy.png`
- Numbers (JSON): `src/scripts/vol_1_foundations/_output/chiral_orbital_holonomy.json`
- Canonical sources cited: [`k4_tlm.py:359-362,542`](../src/ave/core/k4_tlm.py); [`k4-rotation-group.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) §1/§5/§6; [`finkelstein-misner-spin-half-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) §8/§9.
