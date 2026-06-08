# Prereg: electron genesis observer bridge

**Status:** FROZEN PREREG before running the new observer harness.
**Branch:** `analysis/2026-06-07-two-node-alpha-projection`.
**Driver to be written:** `src/scripts/vol_1_foundations/electron_genesis_observer_bridge.py`.
**Prompt from Grant:** fix the electron genesis simulations; do we have to insert `alpha`? Is the missing object the tiny E/B power-conversion gear in the many-neighbor envelope?

---

## §0 Question

Can the current AVE engines expose the substrate-native observables needed for an alpha-free electron genesis test?

The target is not yet "derive alpha." The target is the prerequisite observer bridge:

1. bound-state trapping / breathing in the correct nonlinear saturation engine;
2. bond phasor observables `V_inc`, `V_ref`;
3. inductive/reactive state `Phi_link`;
4. local saturation / impedance trace `S(A)` or `z_local`;
5. first/second-neighbor envelope covariance;
6. measured leakage/Q, compared to non-fitted scales (`4π`, `137`) only after the run.

## §1 Physical framing

Working picture:

- Local K4/Cosserat geometry permits spinor structure.
- The electron envelope is a many-neighbor dressed reactive object, not a single-node scalar shadow.
- Fine structure, if it emerges dynamically, should appear as a tiny conversion/leakage gear between trapped translational E-sector reactance and rotational/magnetic/Cosserat-sector reactance.
- Inserting `alpha` into the emergence lane would convert the simulation into a calibration model. That lane is allowed only if separately labeled `alpha-in`.

## §2 Corpus constraints

- Per A-027 two-engine architecture, **K4-TLM** is the sub-saturation / bench-style engine: it has `V_inc`, `V_ref`, `Phi_link`, and `z_local`, but prior bound-state tests on K4-TLM return Mode III and are not framework failures.
- **MasterEquationFDTD** is the scalar bound-state engine: it contains saturation-modulated local wave speed and produces the breathing soliton, but it does not expose `V_inc/V_ref/Phi_link`.
- Therefore a full electron genesis test is not possible until one engine carries both classes of observables or a validated bridge exists between them.

## §3 Layered criteria

### Alpha-free emergence lane

Inputs allowed:

- K4 geometry and A/B neighbor shells.
- Axiom-4 saturation kernel.
- Existing engine state variables (`V`, `V_prev`, `V_inc`, `V_ref`, `Phi_link`, `z_local`).
- Non-fitted seed amplitudes expressed in `V_SNAP` / `V_yield` natural units.

Inputs forbidden:

- `alpha` as a damping coefficient, Q target, kernel coefficient, threshold, or tuned normalization.
- Any fitted screening coefficient chosen to land on `1/137`.

Layer outcomes:

| Layer | Required signal | Failure meaning |
|---|---|---|
| L1 trapping | Master scalar bound-state remains localized / breathing after transient | no bound-state substrate support |
| L2 phase-space | K4 observer supplies rank-2 `V_inc/V_ref` phasor at canonical bond | current run lacks phase-space observable |
| L3 reactance | `Phi_link` trace anti-correlates / exchanges with capacitive `V_inc` energy | no C/L reactive gear visible |
| L4 envelope | first/second-neighbor covariance is stable, non-random, and not single-node artifact | no many-neighbor envelope |
| L5 leakage/Q | measured Q/leakage is finite and alpha-free | no Q channel to classify |

### Calibration lane

Allowed only after the alpha-free lane is classified. `alpha` may be inserted as a known Q/loss for morphology comparison, but all outputs must be labeled `alpha-in calibration`. Calibration cannot count as an emergence result.

## §4 Prediction before run

Prediction: **ARCHITECTURE-SPLIT negative / incomplete.** The scalar bound-state engine should pass L1 but fail L2/L3 because it lacks bond phasors and `Phi_link`. The K4 observer lane should pass L2/L3 instrumentation but fail L1 because K4-TLM is not the bound-state engine. This would not falsify the physics; it would identify the next implementation target: a unified bound-state engine with bond-phasor/reactance observers or an explicitly validated projection bridge.

## §5 Classification rules

- If the run reports `Q≈137` only in the alpha-in lane, classify as **calibration**, not emergence.
- If alpha-free output gives `Q≈4π`, classify as **geometry/loss scale**, not fine structure.
- If alpha-free output gives `Q≈137` and passes L1-L5, classify as **emergence candidate** requiring auditor review.
- If the engines split by observable class, classify as **observer-architecture gap**.

## §6 Result

Executed with:

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/electron_genesis_observer_bridge.py
```

Output:

- `src/scripts/vol_1_foundations/_output/electron_genesis_observer_bridge_results.json`

Console summary:

```text
Electron genesis observer bridge
  verdict: OBSERVER_ARCHITECTURE_GAP
  L1 master trapping: True
  L2 K4 phasor observer: True
  L3 K4 Phi_link observer: True
  L4 K4 neighbor envelope: True
  K4 retained energy fraction of peak: 0.1507
  K4 C/L proxy corr: None
  alpha: comparison-only; not inserted
```

## §7 Adjudication

**Verdict: OBSERVER_ARCHITECTURE_GAP.** The alpha-free first-pass run confirms the split predicted in §4:

- `MasterEquationFDTD` passes the scalar trapping/breathing layer: post-transient peak remains finite (`mean=0.198`, `min=0.0738`, `max=0.533`), and FWHM variation stays bounded (`CV=0.301`). This is the bound-state lane.
- `K4Lattice3D` exposes the needed phasor/reactance/envelope observables: `V_inc/V_ref` are populated, `Phi_link` is nonzero, `z_local` is available, and first/second neighbor shell covariance is measurable. This is the observer lane.
- No current run has all layers in the same dynamical object. The bound-state engine has no `V_inc/V_ref/Phi_link`; the phasor/reactance engine does not form the bound state (`energy_retained_fraction_of_peak=0.1507`, not a trapped electron).

The neighbor-envelope screened variance values in this instrumentation run are tiny (`~1e-8`) and are not promoted as an alpha result. They are seed/observer diagnostics only because the K4 lane is not the bound-state lane.

## §8 Calibration lane

**Not executed.** The blocker is not morphology calibration; it is that no current engine simultaneously carries the bound-state dynamics and bond-phasor/reactance observables. Inserting `alpha` now would only produce an `alpha-in` consistency morphology on the wrong architecture. That would not repair the emergence test.

The correct next implementation target is therefore:

1. add bond-phasor / `Phi_link`-equivalent observers to the bound-state lane, or
2. add saturation-local-clock bound-state dynamics to the K4 phasor lane, or
3. construct a validated projection bridge between `MasterEquationFDTD.V/V_prev` and K4 bond observables.

Until one of those exists, `Q≈137` cannot be claimed or falsified by genesis simulation.

---

## §9 Projection bridge follow-up (2026-06-07)

Implemented option (3): `src/ave/core/master_fdtd_phasor_bridge.py` projects the scalar Master Equation field onto K4 four-port phasors after each leapfrog step using the TLM traveling-wave split at Z₀ = 1. The driver now runs a third lane, `master_unified_projection_lane`, on the same sech seed as the scalar L1 test.

Re-executed with:

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/electron_genesis_observer_bridge.py
```

Console summary:

```text
Electron genesis observer bridge
  verdict: PROJECTION_BRIDGE_INSTRUMENTED
  unified L1 trapping: True
  unified L2 phasor: True
  unified L3 Phi_link: True
  unified L4 envelope: True
  unified bond gamma min: -0.00563
```

## §10 Adjudication (projection bridge)

**Verdict: PROJECTION_BRIDGE_INSTRUMENTED.** The observer-architecture gap is closed for instrumentation:

- The unified lane passes L1–L4 on one dynamical object (`MasterEquationFDTD` + projected observers).
- Post-transient phasor activity is strong (`v_inc_std=0.104`, `v_ref_std=0.100`), not a null channel.
- `Phi_link` accumulates to O(1) magnitude (`phi_abs_max_local=1.28`), with high `V_inc` ↔ `dPhi/dt` correlation (`0.979`).
- Neighbor-shell covariance is rank ≥ 2 on both shells.
- Bond Γ remains near matched bulk (`Γ_min ≈ −0.006`), consistent with A ≈ 0.53 peak strain — no emergent short wall at this seed amplitude.

**What this does NOT claim:**

- Not alpha emergence (`Q≈137` was not measured; alpha remains comparison-only).
- Not native K4-TLM bond dynamics — the projection is read-only post-processing on scalar `V`.
- Not electron genesis closure — the sech blob is a given bound-state seed, not a rupture→pair-production chain.

**Next physics targets (still open):**

1. ~~Run L5 leakage/Q on the unified lane~~ → **DONE** (`research/2026-06-07_unified-l5-q-leakage-prereg.md`, verdict `L5_NEGATIVE_BOTH`).
2. Drive from rupture/precursor rather than planted sech blob (genesis chain).
3. Resolve the calibration crux (rest-energy vs saturation amplitude) before expecting Γ → −1.
