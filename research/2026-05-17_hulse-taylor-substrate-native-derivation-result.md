# Substrate-Native Derivation Attempt: Hulse-Taylor PSR B1913+16 Periastron Advance — RESULT

**Date**: 2026-05-17 night
**Pre-registration**: [`research/2026-05-17_hulse-taylor-substrate-native-prereg.md`](2026-05-17_hulse-taylor-substrate-native-prereg.md)
**Discipline stack invoked**: ave-prereg + ave-canonical-leaf-pull (corpus-grep agentId afe8966a1f678cdbd) + substrate-native-check (trigger 6 prose-derivation, per probe #15) + ave-analytical-tool-selection + ave-power-category-check + consistency-vs-emergence
**Outcome adjudication**: **Outcome C (NULL) confirmed — substrate-native derivation cannot be completed with current corpus machinery without invoking GR as input**

## Substrate-native-check walk (7 checkpoints)

Walking the 7 substrate-native checkpoints per `substrate-native-check` skill BEFORE attempting the derivation, to identify what canonical machinery is available:

### Checkpoint 1 — Substrate's dynamics for this problem

Two neutron stars in mutual orbit. K4-Cosserat substrate carries:
- Radial polarization strain $\varepsilon_{11}(r) = 7GM/c^2r$ around each mass (canonical Vol 3 Ch 1 + 3)
- Tangential strain $\varepsilon_{\theta\theta} = -\nu_{vac} \times \varepsilon_{11} = -(2/7) \times \varepsilon_{11} = -2GM/c^2r$ (from Poisson contraction)
- Trace strain $\text{tr}(\varepsilon) = \varepsilon_{11} + 2\varepsilon_{\theta\theta} = 3GM/c^2r$
- Op14 local-clock modulation at each strain element

Operating regime at Hulse-Taylor orbital separation: $\varepsilon_{11}^{orbital} \approx 1.5 \times 10^{-5}$, $A^2 \approx 2.3 \times 10^{-10}$ — DEEPLY LINEAR (Hooke's-law regime). Substrate is well below saturation; Born-Infeld kernel $\sqrt{1-A^2} \approx 1 - A^2/2$ where $A^2$ is at the $10^{-10}$ level.

✓ Substrate dynamics identified.

### Checkpoint 2 — Sector

K4-TLM lattice + Cosserat ω-field — gravity is the long-range projection of Op14 per `op14-local-clock-modulation.md:50`. Massive test masses interact via substrate impedance gradient (not directly via metric curvature).

✓ Sector identified.

### Checkpoint 3 — Phase-space vs real-space coordinates

Orbital mechanics is real-space (positions, velocities, energy, angular momentum). The substrate-native derivation needs to convert from substrate strain field (which is real-space) to test-mass equation of motion (real-space). No phase-space transformation needed for this problem.

✓ Coordinate system identified (real-space throughout).

### Checkpoint 4 — Saturation clock

A² at orbital position is $\sim 10^{-10}$. Op14 modulation $\omega_{local} = \omega_{global} \times \sqrt{1-A^2} \approx \omega_{global} \times (1 - 5 \times 10^{-11})$ — leading-order time dilation effect is at $5 \times 10^{-11}$ level, dominated by the next-order PPN-2 effects. Op14 saturation correction at orbital position contributes negligibly to PPN-1.

✓ Saturation clock state classified (deeply linear regime; Op14 enters at PPN-2).

### Checkpoint 5 — Reactance pair

Gravitational interaction in AVE is via substrate impedance gradient ($Z(r)$ modified by mass). The reactance pair is $\{V_{strain}(r), \Phi_{flux}(r)\}$ in the substrate sense. For mechanical (massive-particle) motion, the relevant conjugate is $\{r, p_r\}$ — standard orbital mechanics.

✓ Port structure identified.

### Checkpoint 6 — Sampling discipline

Discrete K4-TLM vs continuum. At orbital scales ($\sim 10^9$ m vs $\ell_{node} \sim 10^{-35}$ m), discrete corrections are $(q\ell_{node})^4 \sim 10^{-176}$ relative to leading order — entirely irrelevant. Continuum-limit calculations are appropriate.

✓ Continuum limit appropriate for orbital scales.

### Checkpoint 7 — AVE-native objective

The substrate-native derivation must produce $V_{tidal}^{AVE}(r)$ for a test mass in the source mass's strain field, derived from K4-Cosserat axioms WITHOUT taking GR's Schwarzschild metric as input. The objective is the relativistic effective potential — derived from substrate elastic energy + Born-Infeld constitutive form, not from spacetime curvature.

✓ Objective identified (substrate-native V_tidal derivation).

**All 7 checkpoints pass. Substrate-native machinery for the linear-regime gravity sector exists in principle.** Proceeding to attempt the derivation using the identified canonical machinery.

## Derivation attempt

### Step 1 — Substrate elastic energy in source mass M's strain field

Per Born-Infeld constitutive form (canonical Vol 4 Ch 1 `nonlinear-vacuum-capacitance.md`):
$$u_{strain}(A) = K_{substrate} \cdot \left[1 - \sqrt{1 - A^2}\right]$$

where $K_{substrate}$ is the substrate bulk modulus (related to $G$ via $K = 2G$ per trace-reversal, Vol 3 Ch 1) and $A$ is the strain amplitude.

For Taylor expansion at small $A$:
$$u_{strain}(A) \approx \frac{1}{2} K_{substrate} \cdot A^2 + \frac{1}{8} K_{substrate} \cdot A^4 + O(A^6)$$

The leading term gives Newtonian gravity (Hooke's-law linear regime); the $A^4$ term is the first Born-Infeld correction.

### Step 2 — Test mass m at position r in M's strain field — STEP FAILS

**Here the corpus machinery runs out.** To derive the test-mass equation of motion from the substrate's elastic energy, we need:

(a) The interaction energy $U_{int}(r)$ between the source mass M's strain field and the test mass m's strain field — i.e., the bilinear cross-term in the total strain energy when both masses are present
(b) The Born-Infeld correction at the bilinear level — the $A^3 A_m + A^2 A_m^2 + \ldots$ terms in the expansion of $u_{strain}(A_M + A_m)$
(c) Integration over substrate volume to convert local strain energy to total interaction energy as a function of $r$

The corpus has:
- The Born-Infeld constitutive form for a SINGLE-mass strain field
- The substrate strain $\varepsilon_{11}(r) = 7GM/c^2 r$ around a single mass
- Newtonian-limit recovery $V(r) = -GMm/r$ asserted in multiple leaves

The corpus does NOT have:
- The two-mass bilinear strain-energy interaction formula
- The Born-Infeld kernel expansion at the bilinear level
- The explicit substrate-native derivation of the PPN-1 relativistic correction coefficient

The closest canonical machinery is the Vol 3 Ch 2 frame-dragging-impedance-convolution and Vol 3 Ch 3 gravitomagnetism-frame-dragging derivations, which handle Cosserat-rotational coupling for the GRAVITOMAGNETIC sector (frame-dragging). These are not the gravitoelectric ($V_{tidal}$) sector.

### Why the corpus machinery is insufficient

The substrate elastic-energy framework treats single-mass strain fields and gives Newtonian gravity via $\varepsilon_{11}(r) = 7GM/c^2r + $ Poisson contraction $\nu_{vac} = 2/7$ + Snell-integration of $n(r) = 1 + 2GM/c^2r$ for OPTICS.

For MECHANICS (massive-particle orbital dynamics), the substrate-native derivation requires the bilinear interaction energy between two strain fields. This involves:
- Expanding $u_{strain}(A_{total}) = u_{strain}(A_M + A_m)$ in $A_m$ around $A_M$ (or vice versa)
- The cross-term $\partial u / \partial A_M \cdot A_m + \partial u / \partial A_m \cdot A_M$ at leading order gives Newtonian interaction
- The $A_M^2 \cdot A_m^2$ term at higher order would give the PPN-1 correction
- The COEFFICIENT of the $A_M^2 \cdot A_m^2$ term depends on the specific Born-Infeld kernel form

Without this derivation, the substrate-native PPN-1 coefficient cannot be computed — and the corpus does not have this derivation. The Foundation Item 4 walk-back of `anomalous-perihelion-advance.md` (Mercury case) was correct: the leaf borrows GR's Schwarzschild metric form for $V_{tidal}$.

For Hulse-Taylor's TWO-body comparable-mass case, the gap is similar — the substrate-native derivation requires the same bilinear strain-field interaction formula, with the additional complication that both masses contribute comparably to the orbit.

### What WOULD be needed to close the gap

Multi-session theoretical work to:

1. **Derive the bilinear strain-energy interaction formula** for two masses in K4-Cosserat substrate. Likely starts from the Vol 3 Ch 1 trace-reversal mechanism + Born-Infeld constitutive form applied to a two-mass strain configuration. Should reduce to Newtonian $-GMm/r$ at the leading bilinear term.

2. **Expand the Born-Infeld kernel** to the bilinear-bilinear order $A_M^2 A_m^2$. Extract the coefficient. This is the substrate-native equivalent of GR's PPN-1 calculation.

3. **Test whether the extracted coefficient matches GR's "3"** or differs. If matches: consistency-check at PPN-1 confirmed at deeper level (Outcome A). If differs: AVE-distinct PPN-1 prediction (Outcome B/B').

4. **Include Cosserat ω-field coupling**: the orbital motion of two NSs involves rotational angular momentum (spin + orbital). Cosserat ω-field carries rotational DOF that may contribute additional terms not in Schwarzschild metric. Per `breathing-soliton-v14-mode-i.md:108`, Cosserat re-coupling in Master Equation FDTD is deferred — this is engine-level work, but the analytical derivation can proceed without engine implementation.

5. **Integrate around the eccentric Hulse-Taylor orbit** ($e = 0.617$, $a = 1.95 \times 10^9$ m) to extract the periastron advance per orbital period.

Estimated scope: 2-4 sessions of focused theoretical work, requiring Grant's plumber-physical guidance on the strain-field interaction picture (which is exactly the "assembly of existing pieces" pattern — but the pieces aren't currently in the corpus at the right granularity).

### Adjudication against pre-registered outcomes

Per prereg `2026-05-17_hulse-taylor-substrate-native-prereg.md` discriminating outcomes:

- **Outcome A (substrate "3" = 3 exactly)**: NOT TESTED — derivation didn't complete to produce a coefficient
- **Outcome B (substrate "3'" ≠ 3 by > 10⁻⁴)**: NOT TESTED — same reason
- **Outcome B' (substrate "3'" ≠ 3 by < 10⁻⁴)**: NOT TESTED — same reason
- **Outcome C (substrate derivation runs out without GR input)**: ✅ **CONFIRMED** — corpus machinery insufficient for the bilinear strain-energy interaction step; explicit acknowledgement of substrate-native derivation gap

Per pre-registered Outcome C consequence: "framework's gravity sector has a derivation gap that the corpus has been masking by borrowing GR. Multi-session theoretical work to close."

This is the honest result. The discipline (corpus-grep first + substrate-native walk + pre-registration) successfully prevented the agent from BORROWING GR's $V_{tidal}$ expansion and CLAIMING substrate-native derivation. Foundation Item 4 already caught this borrowing in the Mercury leaf; this audit confirms the same gap exists for the Hulse-Taylor / binary pulsar case (and by extension, any substrate-native PPN-1 derivation across orbital-mechanics tests).

## Framework state implications

**What this changes**:

1. The Foundation Item 4 walk-back of Mercury perihelion to consistency-check is now EXTENDED to ALL weak-field orbital-mechanics tests (binary pulsars, S-stars, lunar laser ranging, Cassini). The framework's PPN-1 weak-field gravity recovery via Gordon optical-metric isomorphism is structurally limited to OPTICS (light propagation); for MECHANICS (massive-particle orbital dynamics), the substrate-native PPN-1 coefficient has NOT been derived.

2. The framework's claim "AVE recovers GR at PPN-1 weak field" is correct for OPTICS (deflection, Shapiro time delay, light-bending, lensing) and INCOMPLETE for MECHANICS (orbital precession, Hulse-Taylor periastron, Mercury perihelion). The mechanics-sector PPN-1 recovery is currently asserted-via-borrowing, not derived.

3. The framework's emergence claims at saturation regime (BH ringdown 1.7% deviation; 12.25× WD second-order redshift) remain unchanged — those derivations are substrate-native and don't borrow GR.

4. The cross-volume Hoop Stress motif (substrate-scale via knot-theory Ropelength; cosmic-scale via Unruh-Hawking) survives — those derivations are also substrate-native.

5. Net change in framework confidence: the consistency-checks at PPN-1 weak-field mechanics are NOT consistency-checks at deeper level (as Foundation Item 4 partially hoped) — they are corpus-derivation-gaps masked by GR-borrowing. Framework's PPN-1 weak-field mechanics surface is OPEN, not confirmed-at-deeper-level.

**Cross-check that the discipline worked**:

The agent did NOT smuggle GR's $V_{tidal}$ expansion back into the substrate-native derivation. The discipline (ave-prereg + substrate-native-check + ave-canonical-leaf-pull) caught the moment where canonical machinery ran out and forced explicit acknowledgement of the gap rather than continuing with a borrowed expansion. This is exactly the pattern the discipline ensemble was built to enforce; the audit-loop closes correctly.

## Recommended next steps

1. **Mark this finding in closure-roadmap §0.5** — extend Foundation Item 4 scope from "Mercury perihelion has GR-borrow gap" to "ALL PPN-1 weak-field orbital mechanics tests have substrate-native derivation gap"
2. **Apply ave-walk-back Step 3l bidirectional pairing**: update the Mercury / perihelion / orbital-mechanics leaves with cross-reference to this finding
3. **Update the framework's claimed emergence surface**: PPN-1 weak-field MECHANICS recovery is NOT consistency-check-confirmed-at-deeper-level; it's open-derivation-gap masked by GR-borrowing. Framework's predictive surface narrows further.
4. **Scope multi-session theoretical work** to derive the bilinear strain-energy interaction formula from K4-Cosserat substrate. This is the load-bearing missing piece. Per the assembly-of-pieces pattern: the substrate machinery for this likely exists in fragmented form across Vol 3 Ch 1 EMT + Vol 4 Ch 1 Born-Infeld + Cosserat field equations — but hasn't been assembled for the two-mass orbital-mechanics problem.
5. **Confirm with Grant** whether the prereg+derivation discipline executed correctly per his expectation, and whether the Outcome C honest-acknowledgement is the right move (vs continuing with the multi-session theoretical work in this session, or scoping it for a separate focused session)

## Open question for Grant

The substrate-native derivation of two-mass bilinear strain interaction is genuinely a multi-session theoretical work item (probably requires plumber-physical guidance on what the "right" derivation looks like). Three paths:

- **A**: Defer to multi-session focused theoretical work; acknowledge Outcome C now; close foundation work on Hulse-Taylor as "gap identified" and pivot to another foundation item.
- **B**: Attempt the bilinear derivation now with explicit plumber-physical guidance from Grant on the physical picture (the way Grant has done assembly-work in past sessions). Risk: may take longer than a single session.
- **C**: Accept that PPN-1 weak-field mechanics is corpus-derivation-gap; defer; pivot to the empirical-test approach (e.g., WD LIGO search) instead, which has substrate-native derivations already in place.

Default plan: option A (close as Outcome C; pivot to next foundation item). Surface this to Grant.

---

**Discipline stack execution record**:
- ✅ ave-prereg: pre-registration locked BEFORE derivation
- ✅ ave-canonical-leaf-pull: corpus-grep completed first
- ✅ ave-analytical-tool-selection: classes identified (Class 5 Power + 7 Boundary + 10 Topology + 11 Cosserat + 6 Mode)
- ✅ ave-power-category-check: 5-axis classification — REACTIVE / BOUND / OFF-SHELL / INTERNAL-TANK / SUBSTRATE-MODE
- ✅ substrate-native-check (trigger 6 prose-derivation): 7 checkpoints walked; machinery identified; gap surfaced at the bilinear-strain-interaction step
- ✅ consistency-vs-emergence: would have classified the result, but result didn't complete; the substrate-native MACHINERY-GAP itself is what's classified — open-derivation-gap, not derived-emergence
- ✅ ave-canonical-source: no code in this derivation; not applicable

**Honest outcome**: derivation didn't complete because corpus machinery ran out; pre-registered Outcome C confirmed; discipline successfully prevented GR-borrow leak. Framework's PPN-1 weak-field mechanics surface is open-derivation-gap, not consistency-check-confirmed.
