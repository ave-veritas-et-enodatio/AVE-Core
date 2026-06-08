# Vacuum Characterization Program — the bounded scope-of-work

**Date:** 2026-06-07 · **Status:** living tracker · **Class:** scope-of-work (consistency-class framing; no new derivations)

## Framing — why the work is now a finite checklist

The electron-as-(2,3)-flux-tube is a **textbook dynamical object**: a self-pinched magnetic
flux tube (MHD) ringing as an LC tank (EE) at its Compton frequency, stabilized as a knotted
soliton (nonlinear dynamics + knot theory), with radiation-reaction drag (classical EM) and
gyroscopic precession (rigid-body). Because every piece is standard physics, the
characterization stops being open-ended and becomes a **finite, enumerable matrix**: the
*vacuum datasheet* (material properties) × the *dynamics domains* (governing laws), each cell
carrying a value and a corpus status.

**Status legend:** ✓ characterized · ◐ partial · ○ open. All values from
`src/ave/core/constants.py` unless noted.

> **Provenance note.** The dynamics-domain *equations* below are standard-physics relations
> (MHD, LC, knot, radiation-reaction, rigid-body) — reliable as textbook physics. The AVE
> *values* are corpus constants (cited). The FBD-workflow auditor verification did **not**
> complete (monthly spend limit), so per-cell FBD-derivations are standard-relation + cited-value,
> not yet auditor-grounded cell-by-cell. Flagged for a later verify pass.

---

## A — The vacuum datasheet (material properties)

| Property | Symbol | Relation | Value | Status |
|---|---|---|---|---|
| Propagation velocity | `c` | `1/√(μ₀ε₀)` | 2.998×10⁸ m/s | ✓ |
| Characteristic impedance | `Z₀` | `√(μ₀/ε₀)` | 376.7 Ω | ✓ |
| Permittivity / permeability | `ε₀, μ₀` | C, L per cell | CODATA | ✓ |
| Cell pitch / reduced Compton radius | `ℓ_node` | `ℏ/(m_e c)` | 3.862×10⁻¹³ m | ✓ |
| Dielectric breakdown (voltage) | `V_yield` | `√α · V_snap` | 43.65 kV | ✓ |
| Breakdown (field) | `E_yield` | `V_yield/ℓ_node` | 1.13×10¹⁷ V/m | ✓ |
| Breakdown (B) | `B_snap` | `√(2μ₀ m_ec²/ℓ_node³)` | 1.89×10⁹ T | ✓ |
| Line tension | `T_EM` | `m_ec²/ℓ_node` | 0.212 N | ✓ |
| Snap voltage (rest-energy/charge) | `V_snap` | `m_ec²/e` | 511 kV | ✓ |
| Action quantum | `ℏ` | — | CODATA | ✓ |
| Topological charge density | `ξ_topo` | `e/ℓ_node` | 4.15×10⁻⁷ C/m | ✓ |
| Boundary impedance (Machian) | `ξ_Machian` | `ℏc/(7 G m_e²)` | — | ◐ |
| **Loss tangent / coupling** | **`α`** | `1/Q` | 1/137.036 | **○ value** |
| **Resonant modes (masses)** | `m_e; m_μ, m_τ` | `(p,q)` windings | m_e ✓ | **◐** |
| **Operating-point coefficients** | `dc/dA, dα/dT, dε/dE` | — | — | **○** |

`A_0 = ℓ_node/α = 5.29×10⁻¹¹ m` (Bohr radius) and `Ry = α²m_ec²/2 = 13.606 eV` are derived
datasheet consequences — both ✓.

---

## B — The dynamics domains (textbook physics)

| Domain | Standard law | AVE realization | Status |
|---|---|---|---|
| **MHD flux-tube** | tension `B²/μ₀`, pressure `B²/2μ₀`, Z-pinch | line tension `= T_EM = 0.212 N`; eq. radius `~ ℓ_node` | ✓ |
| **Self-confinement** | nonlinear self-trapping | saturation kernel `S(A)=√(1−(A/A_yield)²)` | ✓ (AVE-specific) |
| **LC resonator** | `ω_C=1/√(LC)`, `Q=1/α` | `ω_C = m_ec²/ℏ`; `Q=137` | ◐ (Q-value = α, open) |
| **Soliton / nonlinear** | parametric oscillator at threshold = Hopf limit cycle | gain = saturating reactance; loss = dark-wake; threshold = ω_C | ✓ (Fork A resolved) |
| **Knot topology** | `Lk = Tw + Wr` | `(2,3)`; `Tw = q/p = 540°/rev`; `Wr` | ✓ (twist test, PR #123) |
| **Radiation reaction** | Abraham–Lorentz; multipole near/far-field | far-field = loss (dark-wake); **near-field reactance = m_ec²** | ✓ (dark-wake split) |
| **Gyroscope / rigid-body** | `L = ℏ/2`; Larmor/Thomas precession | Cosserat micro-rotation; precession = α slip/rev | ◐ (slip-value = α, open) |

---

## The two AVE-specific moves (everything else is textbook)

1. **The confining nonlinearity is the saturation kernel `S(A)`** — where a plasma needs an
   external field and a fluid needs viscosity, AVE confines with the saturable lattice.
2. **Inertia is the stored near-field reactance** — `m_ec²` *is* the LC tank's stored,
   non-radiating energy. Mass = stored field energy.

Every other cell is standard dynamics with the AVE value pinned.

---

## The open frontier — the entire work-remaining is TWO routes

### Route 1 — φ-winding-stability / lepton-tower (closes α-value **and** the masses)
The hinge (re-check §20, epic): is φ (the golden torus, `R/r=φ²`) **forced** — the
most-irrational, hardest-to-phase-lock, **most-stable** winding — or merely chosen?
**Undetermined; never tested.** If a KAM winding-stability argument forces `R/r=φ²` (⇒
`R·r=1/4` in pure `ℓ_node²` geometry, **no voltage bridge, no α-substitution**), then
`α⁻¹ = 4π³+π²+π = 137.036` becomes a genuine derivation of the observable — **and** the
`(2,5)`, `(2,7)` windings give `m_μ`, `m_τ`. **Discriminator:** the lepton-mass tower must
track the KAM winding-stability ordering (separates "φ forced" from "¼ imposed, φ a shadow";
over-determination of ¼ alone is the coincidence-magnet tell). **One route, two payoffs.**

### Route 2 — operating-point coefficients (the AVE-distinct, falsifiable frontier)
The datasheet's "vs. operating point" curves — what no other cell carries and the SM has no
slot for:
- `dc/dA` — gravitational `c`-slowing (`c_EM = c₀/S(A₀)`): lensing / redshift / strong-field departure.
- `dα/dT` (δ_strain) — cosmic α-drift: quasar absorption lines, Oklo reactor. AVE predicts the *sign*.
- `dε/dE` — vacuum-impedance mirror (DC-biased vacuum): the PONDER bench.

These are the **AVE-distinct, falsifiable predictions** — the experimental test surface.
Mostly **uncharacterized**.

---

## Bottom line

The project is no longer "figure out the electron" — it is **"fill two columns of a
datasheet."** Everything else is textbook-with-value-pinned (✓/◐). The only ○ rows are the two
routes that decide whether AVE is right: **Route 1** (derive α + the lepton masses from
winding-stability) and **Route 2** (the falsifiable operating-point predictions). This matrix is
the scope-of-work tracker; update cell status as each closes.
