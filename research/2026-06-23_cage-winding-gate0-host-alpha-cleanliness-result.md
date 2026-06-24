# GATE 0 RESULT — cage⊗winding-engine host α-cleanliness: **HARD STOP**

**Date:** 2026-06-23 · implementer lane · branch `analysis/cage-winding-gate0`
**Prereg:** [`2026-06-23_cage-winding-gate0-host-alpha-cleanliness-prereg.md`](2026-06-23_cage-winding-gate0-host-alpha-cleanliness-prereg.md)
**Charter:** [`_orchestration/2026-06-23_cage-winding-engine-charter.md`](../_orchestration/2026-06-23_cage-winding-engine-charter.md)
**Probe:** [`src/scripts/vol_1_foundations/cage_winding_gate0_alpha_cleanliness_probe.py`](../src/scripts/vol_1_foundations/cage_winding_gate0_alpha_cleanliness_probe.py)

---

## VERDICT: 🔴 HARD STOP — the Cosserat host is α-CONTAMINATED on the Q-readout path

The build approach as literally chartered — *"run the A1 mass-cage on the Cosserat winding host
`cosserat_field_3d.py`, reproduce the cold-Q≈30.8 with the Q-slot EMPTY"* — **fails Gate 0**. Two of the three STOP
conditions fire (the guard trips AND 137 reappears). Per the prereg adjudication and honest-closure (Rule 11), this is
recorded as a clean negative; the failure mechanism is named; the branch closes. **No patch-around was applied — the
137 IS the failure signal.**

The α-free cold-Q≈30.8 known-negative is REAL and reproduces (Q_ringdown=30.754 ≠ 137) — but it lives on the
**Master-Equation scalar engine** (`_bulk.py` / `MasterEquationFDTD`), **NOT** on the Cosserat winding host. The host
the charter names cannot, as built, deliver that number with the Q-slot empty.

---

## EVIDENCE (refute-by-default; three independent α-contamination vectors)

All from the probe, reproducible from a clean import. All file:line refs grep-verified at build time
(verify-before-cite).

### V1 — the α-leak import-guard TRIPS on the host module globals  → STOP condition (1)

The canonical guard (verbatim, `src/ave/solvers/vacuum_varactor_scatter.py:110-112`):

```python
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported into the varactor scatter"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
```

Applied to the host module globals (`vars(ave.topological.cosserat_field_3d)`):

```
reachable: {'ALPHA': True, 'Q_TANK': False, 'ELECTRON': False}
GUARD TRIPS? True  (tripped on: ['ALPHA'])
```

Root: `cosserat_field_3d.py:56` — `from ave.core.constants import ALPHA, V_SNAP` imports ALPHA into the module
globals at load time; `:131` — `KAPPA_CHIRAL_ELECTRON: float = ALPHA * KAPPA_TILDE_ELECTRON` bakes α into a
module-level constant (= 0.00875682308316 = α·1.2). **The guard cannot be placed in this module without tripping** —
which is exactly its job. This is not a fixable import-ordering nit: the host's chirality coupling is defined α-baked.

### V2 — the cage Γ-field default routes through κ_chiral = α·κ̃  → α-baked cage mechanism

The moving-Γ=−1 cage wall is the relu(−Γ) clamp weight (`_freeze_clamp_weight`, `:1957`), frozen from the Γ-field
`_impedance_gamma_field()` (`:1824`). That Γ-field is computed (`:1842-1853`):

```python
S_mu, S_eps = _update_saturation_kernels(u_j, w_j, V_sq, self.dx, V_SNAP,
                                         self.omega_yield, self.epsilon_yield,
                                         KAPPA_CHIRAL_ELECTRON)          # <-- α-baked default
Z_eff = jnp.sqrt(S_mu / jnp.maximum(S_eps, 1e-12))
gamma = (Z_eff - 1.0) / (Z_eff + 1.0)
```

and the asymmetric split (`_reflection_density_asymmetric`, `:605-606`) is
`A²_μ = (1 + κ_chiral·h_local)·A²_μ_base`, `A²_ε = (1 − κ_chiral·h_local)·A²_ε_base`. Probe:

```
cage Γ default κ_chiral = 0.008756823083 (α-baked)
α-free κ̃               = 1.2
κ_chiral / κ̃ = 0.007297352569  is exactly α? True
```

**Partial mitigation (honest):** κ_chiral only multiplies `h_local` (the Beltrami helicity of ω). With the winding
OFF (cage-only, h_local≈0) the α-term vanishes and the split degenerates to the symmetric, α-free
`Z_eff=√(S_μ/S_ε)` route. So the cage *mechanism* could in principle be run α-free on this host by (a) swapping the
default to `KAPPA_TILDE` per charter requirement #2 AND (b) keeping the winding off. **But this does not rescue the
gate** — V3 is the independent, unconditional contamination.

### V3 — `extract_quality_factor()` is a baked golden-torus α⁻¹, NOT an empty cold-Q slot  → STOP condition (2)

`cosserat_field_3d.py:2422-2425`:

```python
def extract_quality_factor(self) -> float:
    R, r = self.extract_shell_radii()
    d = 1.0
    return 16.0 * np.pi**3 * (R * r) + 4.0 * np.pi**2 * (R * r) + np.pi * d
```

This is the **golden-torus Q form**. It is algebraically `4·(4π³)(R·r) + 4·(π²)(R·r) + π·d`, so at the canonical
normalization `R·r = 1/4, d = 1` it equals `4π³ + π² + π` **EXACTLY**:

```
formula 16π³(R·r)+4π²(R·r)+π  at R·r=1/4  = 137.036304
cold α⁻¹ = 4π³+π²+π                       = 137.036304
Q(R·r=1/4) == α⁻¹ EXACTLY? True  <-- 137 LEAK
```

The host's Q-slot is **not empty — it is pre-filled with the 137 golden-torus echo by formula construction**,
independent of any ring-down dynamics. It is a closed-form geometric readout (`is_ringdown_measurement = False`), not
a cold-Q measured from the cavity's envelope decay + −3dB linewidth. This is precisely the strict-anti-substitution
violation the charter named: *"do NOT let anything refill 137"*. (On a real seeded (2,3) state R·r=8.52 gives
Q=4568 — i.e. the value floats with the geometry, but the FORM is the α⁻¹ golden-torus expression at every
normalization, and it lands on 137 at the canonical R·r=1/4.)

### V4 — the α-FREE cold-Q≈30.8 known-negative is REAL but lives on a DIFFERENT engine

The L3 mass-cage cold ring-down (T3.4b) is genuinely α-free and reproduces the known negative:

```
engine: MasterEquationFDTD/_bulk (NOT the Cosserat host)
α-guard trips on _bulk? False  (α-clean: imports only C_0, G_VAC, RHO_BULK, V_LONG)
ω_cutoff=2.8679  Q_ringdown=30.754  Q_linewidth=3.750
Q ≈ 137? False  → Q≈30.8 ≠ 137 (clean α-free negative)
```

`src/tests/engine_acceptance/test_l3_mass_cage.py` **passes 4/4 on HEAD** (live-fire this session, 112.8 s):
T3.4b reports `Q_ringdown=30.754, Q_linewidth=3.750`, guards clean. **But that test runs on `_bulk.py`'s
`MasterEquationFDTD`/`CrystalEngine`, measuring Q from an rfft-linewidth + Hilbert-envelope ring-down — it never
touches `cosserat_field_3d.py` and never calls `extract_quality_factor()`.** The charter's premise that the cage is
already validated *on the winding host* does not hold: the green validation is on a separate scalar engine.

---

## CONFLICT SURFACED (flag-don't-fix) — for orchestrator + Grant adjudication

The charter (`:21,:33,:65`) states the host already carries the cold-cage known-negative and Gate 0 is "wiring +
live-fire on the existing host, NOT new derivation." The engine disagrees on two points; surfaced verbatim, not
silently reconciled:

1. **The cold-Q≈30.8 known-negative is hosted on `_bulk.py` (MasterEquationFDTD), not `cosserat_field_3d.py`.** The
   green `test_l3_mass_cage.py` measures a ring-down on the scalar engine. The Cosserat host's only Q method
   (`extract_quality_factor`, `:2422`) is a closed-form golden-torus α⁻¹ form, not a ring-down — and it returns 137
   at canonical normalization.
2. **The host imports α at module load and bakes κ_chiral = α·κ̃ as the cage Γ-field default.** Swapping to
   `KAPPA_TILDE` (charter req #2) addresses the Γ-field default, but the `extract_quality_factor` golden-torus α⁻¹
   form (V3) is an independent, unconditional 137-leak that a κ swap does not touch.

This is a **substrate-native / capability-map question, not a missing-axiom or engine-bug question** (per A44
missing-axiom-vs-engine-bug). I am NOT drafting an Ax-5 candidate, an engine patch, or a methodology pivot. The clean
finding: the named host is the wrong validate-on-known surface for the α-free cold-Q; the α-clean route is the
`_bulk.py` MasterEquationFDTD cage. Whether the unification should EXTEND `_bulk.py` (the proven-α-clean cage) with
the Cosserat winding rather than EXTEND `cosserat_field_3d.py` (the proven-α-contaminated Q-readout) with the cage is
a framing-level architecture decision for Grant + the orchestrator — NOT an implementer call.

---

## WHAT WOULD A PASS REQUIRE (not done here — flagged for the re-scope decision)

For a future Gate-0 retry to PASS on a Cosserat-hosted cage, ALL of:
1. the host's α-import (`:56`) + the module-level `KAPPA_CHIRAL_ELECTRON = α·κ̃` (`:131`) refactored so the
   cage-dynamics path is α-free (κ̃ topological factor only; α reachable nowhere in the cage globals);
2. a **measured** cold-Q on the host — a ring-down (rfft linewidth + envelope decay of the bound breathing mode),
   NOT the `extract_quality_factor()` golden-torus closed form. The geometric `16π³(R·r)+…` formula must NOT be the
   Q-readout (it bakes 137);
3. the cage mechanism (the moving-Γ=−1 boundary) demonstrated to ring with a finite α-free Q ≈ 30.8 ≠ 137 on the
   host's own dynamics.

None of these are implementer-discretionary; they touch the host's load-bearing constants + Q-definition and a
build-architecture choice. Held for Grant + orchestrator.

---

## PRE-REGISTERED-BIN OUTCOME TABLE

| Bin | Prereg criterion | Outcome |
|---|---|---|
| PASS-1 | α-leak guard does NOT trip on the host cage path | ❌ TRIPS (V1: ALPHA in host globals) |
| PASS-2 | cage mechanism survives on the winding-host | ⚠ mechanism present but Γ-field default α-baked (V2) |
| PASS-3 | cold-Q ≈ 30.8 NOT 137, Q-slot EMPTY | ❌ host Q-slot = golden-torus α⁻¹ = 137 (V3) |
| STOP-1 | guard trips | ✅ FIRES (V1) |
| STOP-2 | 137 reappears / Q-slot not empty | ✅ FIRES (V3) |
| STOP-3 | cage mechanism breaks | — not reached (stopped at V1/V3) |

**Two independent STOP conditions fire ⇒ HARD STOP.**

---

## DISCIPLINE TAGS

- honest-closure (Rule 11): pre-registered prediction failed decisively; single mechanism (α baked into the host's
  constants + Q-form) explains both failures; branch closed; no rescue-debug.
- substitution-not-retraction (Rule 12): no new hypothesis refilled into the Q-slot; the α-free cold-Q≈30.8 result
  is preserved as belonging to the `_bulk.py` route.
- flag-don't-fix: the charter↔engine conflict surfaced with both verbatim sources; not silently reconciled; no host
  patch, no Ax-5 draft, no methodology pivot — held for Grant + orchestrator.
- consistency-vs-emergence: the 137 in `extract_quality_factor` is an instance-baked geometric ECHO (golden-torus
  form), not a cage-emergent chord — consistent with the corpus α-keystone-echo adjudication.
