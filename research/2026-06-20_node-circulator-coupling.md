# Node circulator coupling — Fork-A as a NORM-PRESERVING ROTATION (RESULT)

**Date:** 2026-06-20 · **Branch:** `feat/node-circulator-coupling` · **Lane:** implementer
**Driver:** [`src/scripts/vol_9_device/node_circulator_coupling.py`](../src/scripts/vol_9_device/node_circulator_coupling.py) ·
**Results:** [`src/scripts/vol_9_device/_output/node_circulator_coupling.json`](../src/scripts/vol_9_device/_output/node_circulator_coupling.json)
**Grounds in:** [`research/2026-06-10_graft-v4-photon-helicity_result.md`](2026-06-10_graft-v4-photon-helicity_result.md) §6,§9 (the escape spec) ·
[`research/2026-06-09_crystal-graft-v3_result.md`](2026-06-09_crystal-graft-v3_result.md) (the pump evidence) ·
[`device-circuit-models.md`](../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md):159-165,201-217 (Fork-A + chiral circulator) ·
`node_2domain_nport.py`:376 (the idealized S≠Sᵀ circulator — PR #320, branch `feat/node-2domain-nport`, NOT yet on main)

## HEADLINE VERDICT — **PARTIAL** (a bounded helicity-transferring coupling EXISTS; its non-reciprocity is an ECHO at the magnitude level)

A BOUNDED, lossless, helicity-transferring shear↔bulk coupling **EXISTS** and passes
all four gates — a genuine advance over the trilinear potential's pump/inert dead-end.
But the realization is **PARTIAL**: the 2-mode skew coupling is a *reciprocal Rabi flop*
(chirality drops out of the energy flow); genuine non-reciprocity requires the 3-port
ring (the EM port), where it is recovered but small; and the non-reciprocity *magnitude*
is **imposed by hand**, not derived from the lattice (the chiral-crystal engine that
would derive it averages chirality out). **Fork-A does NOT close as isolation, and it
does NOT close as a derived-circulator coupling — it sits at PARTIAL.**

## §0 — The escape, and what it replaces

Fork-A ([`device-circuit-models.md`](../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md):210-215)
asks: does the mass channel (bulk / A1 dilatation) couple to the charge channel
(shear / Cosserat micro-rotation) via a conserved `H_couple`, or is it galvanic
**isolation**? Every *potential-energy* coupling tried so far hit a wall:

- The **trilinear potential** `H = κ̃ ∫ g·V·[w·(∇×ω)]` (cross_sector_coupling.py:122,
  graft-v3/v4) is **INDEFINITE** — linear in each of `V, w, ω` ⇒ unbounded below. The
  conserve-and-transfer arm (`photon_deplete=True`) **DETONATES** (`H_bel −4107`,
  graft-v4 §6); the bounded arm transfers **~2 %** and is **inert**.
- graft-v4 named the escape (§9, 2nd bullet): *"a BOUNDED, helicity-TRANSFERRING
  coupling — norm-preserving `H_photon↔H_bel` exchange ... an orthogonal field-space
  rotation à la the crystal_engine converter, rather than a trilinear potential."*

This driver builds that escape: the coupling as a **skew-Hermitian GENERATOR**, not a
potential. Where the trilinear `H` is a number (an energy that can go to −∞), the
generator is a **rotation** — norm-preserving by construction, so it cannot pump.

## §1 — The circulator formulation (the skew generator)

The two physical modes (pinned in **phase-space** coordinates, A46 discipline):

| amplitude | substrate grade | observable | corpus anchor |
|---|---|---|---|
| `a_bulk`  | A1 dilatation / bulk-compression | `\|a_bulk\|²` ∝ trapped bulk energy `E_V` = **latent MASS** | crystal_engine.py:354 |
| `a_shear` | Cosserat micro-rotation / poloidal circulation | `\|a_shear\|²` + winding-phase = the LOCAL `(ω,π_ω)` LC quadrature = the poloidal **CHARGE "3"** | crystal_graft_v4.py:46-47 |

`a = q + i·p/ω` is the analytic signal of an LC reactance pair (`q`=displacement,
`p`=momentum); `|a|²` = mode energy / ω. **Crucially**, `a_shear` is the LC-quadrature
amplitude — the phase-space winding, NOT the orthogonal real-space rigid rotation `L_ω`
the previous inert lock mistakenly targeted (graft-v4 §5).

The dynamics:

```
d/dt [a_bulk; a_shear] = -i H [a_bulk; a_shear],     H Hermitian,

    H = [[ ω_b              ,  Ω·e^{+i·χ·θ_χ} ],
         [ Ω·e^{-i·χ·θ_χ}   ,  ω_s            ]]
```

- `Ω` = circulator rate (magnitude from the α-free topological converter `κ̃ = 6/5`).
- `χ ∈ {+1,−1,0}` = I4₁32 handedness (matter / antimatter / achiral, crystal_engine.py:41).
- `θ_χ = 2π·ν_vac` (ν_vac = 2/7, **α-free**) = the chirality phase — the SAME gyrotropic
  phase as `node_2domain_nport.py`:473 (PR #320, not yet on main).

`H = H†` ⇒ `e^{-iHt}` is **unitary** ⇒ `|a_bulk|² + |a_shear|²` conserved **EXACTLY** for
any `ω_b, ω_s, Ω`. This driver builds the **time-domain generator** whose frequency-domain
S-matrix shadow is `node_2domain_nport.py`:376 (PR #320, not yet on main)
`S = [[0, e^{+iθ}],[−e^{−iθ},0]]`. **α-freedom CI-style guard** (`assert_alpha_free`):
κ̃ verified = 6/5 (not 1.2α), ν_vac = 2/7, no α-literal in any rate/energy/amplitude.

## §2 — The four-gate table

**validate-on-known** (HALTs on fail): unitarity ✅, Rabi formula `Ω²/(Ω²+Δ²/4)` ✅,
norm conservation ✅ — the analytic anchors the gates rest on hold independently of the
integrator.

| Gate | What it tests | Result | Number | Pass |
|---|---|---|---|---|
| **A CONSERVE** | norm/energy conserved, no pump (Axiom-3 lossless) | norm drift `1.1e-12` over 40k steps; late-time pump slope `2.7e-17`/step; `\|j\|/N` bounded `0.60` | machine-precision conservation, no pump | ✅ |
| **B TRANSFER** | energy FLOWS bulk↔shear, ≫ the failed 2 % | seed bulk only (shear EMPTY) → **100 % transfer** at resonance, **80 %** detuned; matches analytic Rabi exactly; shear oscillates (191 crossings) | **50× the failed 2 %**, measured flow | ✅ |
| **C LOCK-ON-WINDING** | coupling acts on the POLOIDAL WINDING; ON ≠ OFF | winding rate `−1.300` (OFF, = −ω_s bare LC) → `−0.814` (ON); Δrate `0.486 ≈ Ω`; shear-energy ON-vs-OFF differs by `0.55`; **inert = False** | not the inert-lock failure | ✅ |
| **D MOTION→MASS** | trapped bulk (mass) scales with circulation rate, winding fixed | trapped-bulk-vs-detuning **corr `0.994`**; matches analytic `1−f_rabi/2`; monotone in `\|ω_b−ω_s\|` | clean relation, **see §3 caveat** | ✅ (with caveat) |

**All four gates pass.** Gate A is conservation *by construction* — Gate B proves it is
not VACUOUS (energy genuinely sloshes: shear starts empty and fills to 100 %). Gate C is
the discriminator that the previous lock **failed**: this coupling moves the winding-rate
observable (in phase-space coordinates), where the old lock only touched the orthogonal
`L_ω`. Gate D's `0.994` correlation is real but carries a self-skeptical caveat (§3).

## §3 — The reciprocal-Rabi finding (the load-bearing negative) + the Gate-D caveat

Two honest negatives temper the four green gates:

**(1) The 2-mode skew coupling is RECIPROCAL — the chirality drops out of the energy
flow.** `non_reciprocity_test` measures forward (bulk→shear) vs reverse (shear→bulk),
and RH vs LH, on the SAME generator:

| | RH (χ=+1) | LH (χ=−1) | asymmetry |
|---|---|---|---|
| fwd bulk→shear | `0.80000` | `0.80000` | — |
| rev shear→bulk | `0.80000` | `0.80000` | reciprocity asym **`8.8e-15`** |
| chirality (RH vs LH, fwd) | | | **`1.0e-13`** |

The transfer fraction is `\|Ω\|²/(\|Ω\|²+Δ²/4)` — it depends on `\|Ω\|²`, so the chirality
**PHASE** `e^{±iχθ_χ}` **cancels out of the energy transfer entirely**. A 2-port lossless
skew rotation is a **Rabi flop**, not a one-way router: energy sloshes back and forth
symmetrically. This is the plumber-physical fact a circulator needs ≥3 ports — a 2-mode
coupling carries a chirality *phase* but no chirality-*dependent* energy routing.

**(2) The 3-PORT ring RECOVERS genuine non-reciprocity** (but small). Adding the EM port
([bulk, shear, EM] ring with a uniform chirality phase) gives a **gauge-invariant loop
phase `3χθ_χ`** — a real chirality flux (Aharonov-Bohm-like) the 2-port cannot carry:

| χ | net directional (shear−EM) |
|---|---|
| +1 (RH) | `−8.76e-4` |
| −1 (LH) | `+8.76e-4` (flips with χ ✅) |
| 0 (achiral) | `1.6e-12` (symmetric ✅) |

`genuine_nonreciprocity_3port = True` — the routing IS chirality-dependent once the EM
port is present. But the directional asymmetry (`1.75e-3`) is small at this rate, and its
magnitude is still the plugged `θ_χ` (§4).

**(3) Gate-D caveat (self-skeptical — FLAGGED).** The trapped-bulk-vs-circulation
correlation is real (`0.994`), but the relation is **symmetric in sign(Δ)**: `ω_s = 0.4`
and `ω_s = 1.6` (both `\|Δ\| = 0.6`) give **identical** trapped bulk `0.7501`. So it is the
Rabi *off-resonance retention* — "detuning throttles how much the circulator pulls out of
the bulk" — NOT a unidirectional *"more circulation ⇒ more mass"*. Reported as-is, not
inflated to a mass-generation mechanism.

## §4 — FORCED-vs-IMPOSED (chord-vs-echo)

Tracing where the antisymmetry / non-reciprocity comes from, honestly:

1. **The SKEW STRUCTURE is FORCED only trivially.** *Any* lossless linear coupling
   between two oscillators is `e^{-iHt}` with `H` Hermitian — the skew off-diagonal is the
   generic two-mode-coupling form, NOT AVE-distinct. "Realize the coupling as a rotation"
   is forced by losslessness (Axiom-3), nothing more.
2. **The non-reciprocity SIGN is LATTICE-sourced.** `χ` = I4₁32 handedness
   (crystal_engine.py:41, "chirality sign h selects matter vs antimatter"). That sign is
   real and lattice-derived. The χ→−χ flip in the 3-port net-directionality (§3) traces it.
3. **The non-reciprocity MAGNITUDE is IMPOSED.** `θ_χ = 2π·ν_vac` and the rate `κ̃` are
   topological converter constants **we plug in**. The lattice does not hand us a derived
   non-reciprocity magnitude: the cubic-FDTD chiral-crystal engine **averages chirality
   out** ([`device-circuit-models.md`](../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md):163,
   the chiral circulator is **STATED-pending-engine**, magnitude not computed).

> **VERDICT: IMPOSED-AT-MAGNITUDE (ECHO).** A bounded, helicity-transferring coupling
> EXISTS and works — but it does NOT derive its non-reciprocity from the lattice. The skew
> form is forced trivially; the non-reciprocity sign is lattice-sourced; the non-reciprocity
> magnitude is plugged by hand. **Flagged for Grant** (§5): deriving the magnitude is the
> STATED-pending-engine frontier — it needs the chiral-crystal engine that does not average
> chirality out.

## §5 — Honest closure + corpus-state queue

**This is a clean PARTIAL, not a manufactured success and not a flat isolation.**

- **NOT ISOLATION-WINS.** All four gates pass; a bounded, winding-acting, energy-
  transferring shear↔bulk coupling demonstrably exists. The trilinear potential's
  pump/inert dead-end is genuinely escaped: the skew generator cannot pump (norm conserved
  to `1e-12`), and Gate C confirms it acts on the *winding*, not the orthogonal `L_ω` the
  previous inert lock targeted. So Fork-A's coupling leg is **NOT dead**.
- **NOT COUPLING-CLOSES.** The 2-mode realization is a reciprocal Rabi flop (chirality
  drops out of energy flow, §3.1); genuine non-reciprocity needs the 3-port ring (§3.2);
  and the non-reciprocity magnitude is imposed, not derived (§4). The coupling *works* but
  its circulator character is an **echo** at the magnitude level.
- **Self-skeptical guards (the previous efforts fooled themselves — these were tested):**
  - *INERT-LOCK:* Gate C ON ≠ OFF on the winding (Δrate `0.486`, energy-diff `0.55`) — NOT
    the inert failure. ✅
  - *TAUTOLOGICAL-TRANSFER:* Gate B seeds shear EMPTY, so the fill is a measured flow, not
    a closure identity. ✅
  - *VACUOUS-CONSERVATION:* Gate B (100 % sloshing, 191 oscillation crossings) proves the
    conservation is non-trivial — energy genuinely exchanges. ✅
  - *FORCED-vs-IMPOSED:* traced and reported as ECHO-at-magnitude (§4) — not narrated as a
    chord. ✅
  - *DO-NOT-MANUFACTURE-SUCCESS:* the reciprocal-Rabi negative and the Gate-D sign-symmetry
    caveat are headlined, not buried.

**Corpus-state updates queued (implementer SURFACES; auditor LANDS):**

- **`device-circuit-models.md`:201 / Fork-A** — the graft-v3 χ-source is no longer the only
  live candidate: a **skew-generator circulator coupling** exists, passes the four gates,
  and is bounded/conserving (escapes the pump/inert dead-end). But it is **PARTIAL** — the
  non-reciprocity is reciprocal at 2 modes and imposed-at-magnitude. The Fork-A "coupling
  leg" status should move from "demoted/unimplemented" to "**partial — bounded coupling
  exists, non-reciprocity imposed**." Auditor decides annotation.
- **`device-circuit-models.md`:159-165 / chiral circulator (Fork-B)** — this driver
  confirms the corpus statement that the circulator is **≥3-element** (the 2-mode coupling
  is reciprocal; the 3-port ring is where non-reciprocity lives). The STATED-pending-engine
  magnitude is now sharpened: it is specifically the **3-port loop-phase flux** that needs
  the chiral-crystal engine.
- **No new axiom drafted** (A44 / Rule 16): the residual is an engine coupling-family gap
  (the non-reciprocity magnitude needs a chirality-resolving engine), surfaced for Grant —
  not a missing postulate.

**Flagged for Grant (the one place I had to impose rather than derive):** the
non-reciprocity *magnitude* (`θ_χ`, `κ̃`) is plugged, because the chiral-crystal engine that
would derive it averages chirality out (device-circuit-models.md:163). Whether the 3-port
loop-phase flux can be derived from the I4₁32 net is the open frontier.

**Skills fired:** `substrate-native-check` (CP K4/Cosserat grade-pinning; CP A46
phase-space-vs-real-space — the modes are phase-space LC amplitudes, NOT real-space
Cartesian moments; CP not-a-potential/not-gradient-descent — unitary rotation, lossless);
`phase-space-coordinate-check` (the winding measured on the complex amplitude phase, the LC
quadrature, matching the corpus charge="3"=LC-quadrature claim); `ave-conserved-vs-pumped`
(the skew generator is the bounded energize-lock the trilinear potential could not be);
`ave-discrimination-check` (FORCED-vs-IMPOSED traced; the reciprocal-Rabi finding is the
SM-counterfactual that a 2-mode coupling cannot be a one-way router); `consistency-vs-
emergence` (the non-reciprocity is ECHO-at-magnitude, not emergence); `ave-canonical-source`
(κ̃, ν_vac from constants; α-free guard); `verify-before-cite` (graft-v3/v4 §6/§9, device-
circuit-models Fork-A, node_2domain_nport circulator all re-read this session); `flag-don't-
fix` (the imposed magnitude + the Gate-D sign-symmetry + the 2-mode reciprocity surfaced for
Grant, not silently resolved); `pre-test-physics-check` (the ≥3-port question surfaced
BEFORE the build, then measured rather than assumed).
