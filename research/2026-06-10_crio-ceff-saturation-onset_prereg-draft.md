# Prereg (DRAFT): cRIO C_eff(V) Saturation-Onset Discriminator — the program's first real-hardware bench

**Status:** `DRAFT-FOR-GRANT-REVIEW` (2026-06-10). **NOT FROZEN.** This document freezes
only when Grant schedules bench time. DOC-ONLY: no hardware acquired, no execution. The
genesis-v7 simulation run closes the sim arc; this is the staged first-hardware prereg that
becomes live when Grant says "build it."
**Lane:** implementer (per Grant 2026-05-01 cross-authorization where applicable). Real-hardware
falsification-instrument design — the program's first one.
**Origin:** the deferred cRIO benchtop bench (memory: `project_crio_benchtop_falsification_bench.md`).
Grant owns NI cRIO-9014 controller + NI-9263 (4ch AO, ±10 V, 100 kS/s) + NI-9215 (4ch AI, ±10 V,
100 kS/s) = a DC–40 kHz 4×4 phase-coherent lock-in bench. First experiment = the C_eff(V)
saturation-onset discriminator, with the validation-ladder discipline FIRST (this bench's plan is
where `ave-apparatus-floor-attribution` was encoded from).

**Skills fired at draft time:** `pre-test-physics-check` (T6 draft-moment — one plumber question to
Grant, §0), `ave-prereg` (corpus-grep + Step-3.5 dimensional, §3), `ave-canonical-source` (every
number imported/verified from `src/ave/core/constants.py`, §3), `substrate-native-check` (the C_eff
form is derived from the Ax-4 kernel, not an SM nonlinear-optics analogy, §1), `ave-discrimination-check`
(SM/standard-phenomenology counterfactual, §2), `phase-space-coordinate-check` (§9 — the kernel's
amplitude `A` is a per-node operating-point coordinate, not the lab voltage), `consistency-vs-emergence`
(§9 class tags), `ave-regime-phase-state-check` (§9 mode/regime/phase declaration), `verify-before-cite`
(file:line citations grepped this session).

---

## §0 — Pre-test physics check: the ONE plumber question to Grant (BEFORE freeze)

Per Rule 16 strengthening, surfaced at DRAFT time, not after 30+ commits.

**The question (sign-of-slope — load-bearing for the discrimination bin, §2):**

> Grant — does the AVE bench prediction say a DC-biased capacitor's measured **small-signal
> capacitance** should **RISE toward a divergence** as bias climbs, or **FALL / soften**? The corpus
> gives me two canonical leaves with **opposite signs of slope**, and which one is right decides
> whether a Class-2 derating MLCC (which *falls*) **supports** or **contradicts** the AVE form — i.e.
> it sets the entire AVE-FORM / STANDARD-FORM bin boundary.

This is also logged below as a **flagged corpus tension** (flag-don't-fix, Operating-principle 6).
I did NOT pick a branch; both are quoted verbatim with file:line, and the discrimination section (§2)
is written to carry BOTH until Grant adjudicates.

### Flagged corpus tension — C_eff(V) sign of slope (DO NOT silently resolve)

- **Branch R (rising / diverging):** [`nonlinear-vacuum-capacitance.md:21`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md)
  — verbatim:
  > `C_eff(V) = C_0 / sqrt(1 - (V/V_yield)^2) = C_0/S(V)`
  with the table at `:32-39` showing `C_eff/C_0 = 1.005 / 1.155 / 2.294 / 7.089 / ∞` at
  `V/V_yield = 0.10 / 0.50 / 0.90 / 0.99 / 1.000`. Capacitance **rises and diverges** at V_yield. The
  leaf's own claim-quality marker `clm-8nkvwy` (`:17`) states: *"Asymmetric saturation case: only ε
  scales by S → C_eff → ∞, Z_asym = Z_0/√S → ∞."*

- **Branch F (falling / softening):** `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 — verbatim:
  *"Dielectric specialization … `C_eff = C_0/S, ε_eff = ε_0 S, μ_eff = μ_0 S`."* and the predecessor
  prereg [`2026-06-03_yield-knee-map-prereg.md:8,44`](2026-06-03_yield-knee-map-prereg.md):
  *"ε_eff(V) = ε₀√(1−(V/V_yield)²)"* and *"AVE: δε/ε₀ = −A²/2 — the vacuum dielectric **softens**
  (negative V² coefficient)."* The small-signal **permittivity falls** with bias.

**Why this is a genuine tension, not my confusion:** `C ∝ ε` for a fixed-geometry capacitor, so
`ε_eff = ε_0·S` (falling) and `C_eff = C_0/S` (rising → ∞) cannot both describe the same measured
parallel-plate capacitance. Physically they look like two *different observables* sharing the name
"capacitance": (a) the small-signal **differential permittivity** `ε_diff = dD/dE`, which a saturating
polarization drives toward `ε_0` (falls — the ferroelectric-derating picture), versus (b) a bulk
**compliance / displacement-per-force** that *diverges* at rupture (the medium flows). The bench
measures (a) — the quadrature-current small-signal C (§5). **Grant's call:** which sign should the
bench see, and is Branch R describing a rupture-compliance observable the bench does NOT measure?
The auditor lane should NOT land a manual entry on this until Grant adjudicates; I surface it only.

---

## §1 — The frozen forward prediction (derived from the canonical Ax-4 kernel)

**Class tag (per `consistency-vs-emergence`, full classification in §9): the FORM is a Class-B axiom
manifestation; any bench match on a real material is Class-C consistency.** Not an emergence test.

### §1.1 Substrate-native derivation chain (not an SM analogy)

The prediction is NOT "capacitors are varactors, fit a varactor curve." It descends from the Axiom-4
universal saturation kernel:

1. **Kernel (Axiom 4, canonical):** `S(A) = sqrt(1 - A^2)` where `A = A/A_yield` is the **per-node
   saturation operating-point amplitude** (`manuscript/ave-kb/CLAUDE.md` INVARIANT-S2; dielectric
   specialization `A = Δφ/α`). This is a **phase-space / operating-point** coordinate, NOT the lab
   voltage — see §9 phase-space note. The dielectric specialization sets `A = V/V_yield` **per node**.
2. **Op14 wave-speed modulation (canonical):** [`op14-local-clock-modulation.md:29`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)
   `c_eff = c_0·sqrt(S)`; and the Maxwell phase velocity `c_EM = c_0/S` (`manuscript/ave-kb/CLAUDE.md`
   INVARIANT-S2, clm-8nkvwy:111).
3. **Lumped constitutive form (canonical):** holding the inductive (μ / Cosserat-B) sector fixed — the
   correct choice for a **static-E-only DC bias**, which is the **ASYMMETRIC** load per INVARIANT-S2
   (`S_ε < 1, S_μ = 1`) — the capacitance follows the kernel. **The two canonical branches (§0):**
   - Branch R: `C_eff(V)/C_0 = 1 / sqrt(1 - (V/V_yield)^2)` (`nonlinear-vacuum-capacitance.md:21`)
   - Branch F: `ε_eff(V)/ε_0 = sqrt(1 - (V/V_yield)^2)` → `C_eff(V)/C_0 = sqrt(1 - (V/V_yield)^2)`
     (INVARIANT-S2 + yield-knee prereg)

### §1.2 The frozen-form summary (both branches, small-A Taylor)

Let `x ≡ V/V_yield` (the per-node operating-point ratio). The canonical Taylor expansions:

| Branch | Closed form | Small-x Taylor | Sign of leading V² coeff |
|---|---|---|---|
| **R** (rising) | `C/C_0 = (1 − x²)^(−1/2)` | `1 + ½x² + ⅜x⁴ + …` (`nonlinear-vacuum-capacitance.md:27`) | **+½** (stiffens) |
| **F** (falling) | `C/C_0 = (1 − x²)^(+1/2)` | `1 − ½x² − ⅛x⁴ − …` (yield-knee prereg:44) | **−½** (softens) |

**The frozen forward prediction the bench would test:** the small-signal `C_eff(V)/C_0` follows a
**quarter-arc kernel** with leading **V² coefficient of magnitude ½** (in per-node units `x = V/V_yield`),
**sign per Grant's §0 adjudication.** The second-harmonic (2ω) generation coefficient is the canonical
companion observable: `δC/C = ¼ x²` at 2ω (yield-knee prereg:48, `parametric-coupling-kernel.md:70-78`).

**The AVE-distinct fingerprint vs standard phenomenology (§2):** (i) the specific `(1−x²)^(±1/2)`
**quarter-arc shape** (a √-form, with a vertical-tangent **knee** at `x→1`), not a power-law or
tanh/Devonshire form; (ii) the **single yield field V_yield** sets the knee location at zero free
parameters *for the vacuum* (but is a FIT parameter for any real material — §6 honest scope); (iii)
the 2ω even-harmonic with the canonical ¼ coefficient.
