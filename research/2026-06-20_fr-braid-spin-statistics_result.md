# RESULT — Finkelstein–Rubinstein two-loop BRAID spin-statistics gate

**Date:** 2026-06-20 · **Lane:** implementer (carrier-sector) · **Status:** COMPLETE
**Prereg (frozen):** [`research/2026-06-20_fr-braid-spin-statistics_prereg.md`](2026-06-20_fr-braid-spin-statistics_prereg.md) (SHA `1250bb33`)
**Operator:** [`src/ave/topological/fr_braid_exchange.py`](../src/ave/topological/fr_braid_exchange.py) · **Tests:** [`src/tests/test_fr_braid_exchange.py`](../src/tests/test_fr_braid_exchange.py) (14, + 19 #312 holonomy = 33, no regressions)

**Discipline applied:** `substrate-native-check` · `phase-space-coordinate-check` · `consistency-vs-emergence` · `ave-discrimination-check` · `verify-before-cite`.

---

## VERDICT

> **PASS — derived, ahead-of-SM-axiom — BUT chord-vs-peer = PEER-ahead (generic-FR), NOT an AVE-distinct chord.**

The two-loop exchange holonomy is **`−I`** (the `2T` central element, `q_w = −1.0`,
`so3_is_identity = True`) produced by **A4-only, reflection-free** port-permutation transport
of one carrier's worldline **around its partner** and back. It is the **SAME `2T` central
element** as the single-particle 2π `−I`. So the substrate **derives**, via Finkelstein–
Rubinstein (1968) configuration-space topology, the spin-statistics connection the SM
**imposes** by Lorentz-invariance + microcausality axiom.

**But this PASS is generic-soliton-class.** The non-A4 control (a 2π loop about a generic,
non-tetrahedral axis) **ALSO reaches `−I`**. The `double-cover → −1` chain is a property of
`π₁(SO(3)) = ℤ₂` shared by **every** double-cover / soliton framework — it is **not forced
specifically by the discrete A4 connect-map**. Per the prereg's pre-registered chord-vs-peer
sub-discriminator (§2.2), the honest ceiling is **PEER-ahead** (ahead-of-SM-axiom, but
peer-with-the-soliton-literature), **NOT an AVE-distinct chord.** No chord inflation.

---

## THE NUMBERS (raw operator output, `probe_fr_braid_exchange(L=10)`)

| Quantity | Value | Meaning |
|---|---|---|
| `verdict` | **PASS** | exchange −I, all guards, FR consistency |
| `chord_vs_peer` | **PEER-ahead (generic-FR; non-A4 control ALSO reaches −I)** | the honest ceiling |
| `sigma_sign` / `sigma_q_w` | **−1.0** / **−1.0000000000000002** | the exchange σ holonomy = −I |
| `sigma_so3_is_identity` | **True** | σ is a genuine 2π SO(3) loop |
| `sigma1_sign` / `sigma1_q_w` | +1.0 / **+0.5** | a SINGLE C3 partner-encircle = **120°**, NOT −I |
| `sigma2_sign` / `sigma2_so3_is_identity` | +1.0 / True | σ² (double exchange / 4π) → +I |
| `fr_same_2T_element_as_single_particle_2pi` | **True** | exchange ≅ 2π rotation (the FR theorem) |
| `single_particle_2pi_q_w` | −1.0000000000000002 | the C3³ self-encircle −I it matches |
| `non_a4_control.q_w` / `.reaches_minus_I` | −1.0 / **True** | generic-axis 2π loop also gives −I ⇒ PEER |

**The physics crux (recorded transparently, no fudge):** a C3 wedge disclination is a
**1/3-rotation source** — a single partner-encirclement rotates the dragged frame by the
partner's Frank angle (120°, `q_w = +0.5 = cos 60°`), **not** 2π. The FR exchange ≅ 2π
rotation is therefore realized as the **3-fold partner-encirclement** (`C3³ = 360°`), exactly
mirroring how the single-particle 2π −I is built (`k4_lattice_holonomy.py:213`). The `−I` lives
in the **cover** and is reached only by **composition along the path** (continuity-tracked),
never by a single finite A4 link rotation — which is why both the single-particle 2π and the
exchange σ are 3-fold encirclements.

---

## GUARD STATUSES (prereg §4, all SIX HOLD)

| Guard | Status | Evidence |
|---|---|---|
| **(1) winding-around-the-OTHER, not self-C3³** | ✅ HOLD | `partner_winding_around_carrier2 = 3` (≠0); `self_winding_around_carrier1 = 0`. The sign is the **partner-encirclement** holonomy of a DISTINCT defect line, not a single-particle self-encircle relabeled "exchange." |
| **(2) label-free** | ✅ HOLD | the verdict is `net_winding` of the worldline around the partner defect line — a topological invariant of the two-winding configuration. Zero reference to A/B sublattice. **SALIENCE-GUARD honored:** `k4-rotation-group.md:123` (the sublattice-swap reflection line) is NOT used as the discriminator. |
| **(3) reflection-free (zero `T_d \ T`)** | ✅ HOLD | `reflection_free = True`; every braid `link_perm` is an even (A4) permutation. The operator's odd-perm refusal (`k4_lattice_holonomy.py:102`) was never triggered. |
| **(4) `uses_analytic_qbody == False`** | ✅ HOLD | AST self-report `False`; the FR module imports no `cosserat_field_3d`, calls no `q_body` rotor. Composed from `rotation_from_port_permutation` (read the perm, never `cos(φ/2)`). |
| **(5) positive control → +I** | ✅ HOLD | `positive_control_sign = +1.0`, `positive_control_net_winding = 0`. The symmetric / non-braiding (there-and-back) transport gives +I — the metric **discriminates**, it is not blind. |
| **(6) achiral diamond (Grant-ruled)** | ✅ HOLD | `net.name == "diamond"` (Fd-3m); spin-statistics is chirality-independent, so the achiral rotation-topology net is correct. |

**FR homotopy consistency (prereg §5):** the σ `−I` is the SAME `2T` element as the
single-particle 2π `−I` (both `q_w = −1.0`) — the Finkelstein–Rubinstein theorem "exchange ≅
2π rotation of one soliton" realized on the lattice. ✅

**Validate-on-known ladder:** contractible → +I ✅; σ → −I ✅ (the test); σ² → +I ✅
(4π / identity return); single partner-encircle → 120° (not −I) ✅ (ladder transparency).

---

## CHORD-VS-PEER CALL (ave-discrimination-check, prereg §2.2)

**Generic-FR caveat applied. Honest ceiling = PEER-ahead. NOT inflated to a chord.**

- FR (1968) is **generic to soliton theories**: any extended-object field theory derives the
  spin-statistics connection from configuration-space topology. The PASS is a real result
  **against the SM's axiom-level posture** (the SM never derives spin-statistics from a
  microscopic substrate — it assumes Lorentz + microcausality + positivity), but it is
  **peer-with-the-soliton-literature**, not AVE-distinct.
- The **pre-registered AVE-distinct prong** (§2.2.1) — "the `−1` is forced specifically by the
  discrete A4 connect-map, FAILS on a non-A4 control" — **DID NOT FIRE.** The non-A4 control
  (a 2π loop about a generic, non-tetrahedral axis) also reaches `−I`. The double-cover sign is
  a property of `π₁(SO(3)) = ℤ₂`, not of the A4 group structure specifically.
- The second AVE-distinct prong (§2.2.2, **dynamical SELECTION** — the substrate must *select*
  the antisymmetric sector, not merely *admit* it) is **out of scope** for this gate (a
  topological-holonomy gate, not a dynamics gate). It remains the open interior item
  (charter §3(a)). Spin-statistics here is established at **representability + topological-
  derivation** grade, NOT dynamical-forcing grade.

**Conclusion:** the carrier spin-statistics connection is **derived (structural), ahead-of-
SM-axiom, generic-soliton-class (PEER).** It is a genuine result and it **closes the
spin-statistics question the `w257o33nz` "structurally excluded" close got wrong** — but it is
**not** the AVE-distinct chord the charter §5 BAR was hoping for, because no A4-lattice-forcing
was found and dynamical selection is untested.

---

## CONSISTENCY-VS-EMERGENCE TAG + SYMMETRIC-STANDARD (prereg §6)

- **Tag: DERIVATION (structural / manifestation-class).** No CODATA input, no fitted constant,
  no SI substitution — the holonomy reads `sign(q_w)` from integer port-permutation
  combinatorics (`k4_lattice_holonomy.py:40` SIGN-only, α-free). The consistency-vs-emergence
  trap (headlining emergence on CODATA-laundered inputs) **does not apply**: there is nothing
  dimensionful to launder.
- **Symmetric-standard (consensus-bias guard):** applied both ways. The SM gets **no special
  pass** — it imposes spin-statistics at the axiom level, so "AVE derives it" is genuinely
  ahead **on this question**. But AVE gets **no special inflation** — a generic-soliton
  derivation is peer-with-the-soliton-literature, not an AVE chord. The object-level knife
  stays sharp: the result is exactly "derived-ahead-of-SM-axiom, generic-FR, not AVE-distinct,
  dynamical-selection untested."

---

## WHAT THIS CLOSES, WHAT IT LEAVES OPEN

- **CLOSES:** the spin-statistics-exchange gate (charter §3(b), §5 THE BAR "was a reflection
  needed?"). **Answer: NO reflection needed** — the exchange `−1` is A4-only and
  reflection-free, transferring the single-particle 2π result to the two-loop exchange. The
  `w257o33nz` "structurally excluded" close (which mis-cited the sublattice-swap line
  `k4-rotation-group.md:123`) is **corrected**: the carrier exchange is a real-space braid, the
  reflection-bar was a category error.
- **CEILING:** PEER-ahead (generic-FR), not an AVE-distinct chord.
- **OPEN:** dynamical SELECTION (charter §3(a)) — the substrate must *select* the antisymmetric
  sector, not merely *admit / topologically-derive* it. Untested here. If the chord-hunt
  continues, the live AVE-distinct candidates are the **standing forward predictions** (the
  optical-activity sign-flip + achiral-null #195; the `(q·ℓ_node)⁴` dispersion; the GW-echo;
  the birefringence coefficient ~10⁶× QED — see the synthesis doc), not the spin-statistics
  derivation, which is now closed at PEER-grade.
