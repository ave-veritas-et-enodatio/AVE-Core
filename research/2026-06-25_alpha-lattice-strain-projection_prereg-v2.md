# PRE-REG v2 ADDENDUM — lattice-native strain-projection chain (Open A rescope)

**Date frozen:** 2026-06-25 · **Supersedes functional definition only** in [`2026-06-25_alpha-variational-strain-projection_prereg.md`](2026-06-25_alpha-variational-strain-projection_prereg.md) (v1 EMT-abstract routes retained as legacy comparison). **Driver:** `src/scripts/verify/alpha_variational_strain_projection.py`

**Motivation:** v1 treated `p` and `K/G` as abstract EMT knobs. v2 anchors the solve on the corpus lattice chain:

```
T_EM  →  ε_11 on primary bond  →  γ on secondary links (u/(1+u))
      →  θ = ε_11(1−2ν)  →  Π = (1/3)θ = (1/7)ε_11 at K/G=2
      →  s_grav = Π·γ   (local bulk-gravity strain amplitude, T_EM=1)
```

**α enters only as packing readout:** `α_pred = p/(8π)` **after** the forward solve. **G (Newton)** and **ξ (Machian)** are **post-solve diagnostics only** — never on the verdict path.

---

## Frozen lattice-native setup

| Symbol | Meaning | Verdict path |
|---|---|---|
| `T_EM` | 1D EM string tension at defect | normalized to **1** (dimensionless) |
| `u` | over-bracing dilution knob | **solve variable** |
| `p(u)` | `p_cauchy/(1+u)³` | derived |
| `K/G(p)` | FTG-EMT amorphous ratio at `z₀=52` | derived |
| `ν(p)` | `(3K/G−2)/(2(3K/G+1))` | derived |
| `Π(p)` | isotropic bulk projection `(1−2ν)/3 = 1/(3K/G+1)` | derived |
| `ε_11` | axial strain from unit tension, `1/E_eff`, `E/G=9(K/G)/(3K/G+1)` | derived |
| `γ` | secondary-link shear, `(u/(1+u))·ε_11` | derived |
| `s_grav` | **`Π·γ`** — projected bulk gravitational strain amplitude | **functional** |
| `α_pred` | `p/(8π)` | readout only |

**Inputs unchanged from v1:** `z₀=52`, `p_cauchy=0.3068`, `p_G=6/z₀`.

**α-hiding guard:** unchanged — no `constants.py`, no CODATA α on verdict path.

---

## Frozen routes (v2 primary)

### B1 — unconstrained max `s_grav(u)`

Argmax `s_grav(u) × admissibility` on `u ∈ [0, 0.6]`, where admissibility = rigidity margin × Cauchy clearance (zero outside `(p_G, p_cauchy)`).

### B2 — trace-reversal constraint (K/G = 2)

Same as v1 A1: solve `K/G(p(u))=2`; report full chain at `u*`. **Physical read:** gravity-stable projection requires trace-reversal lock; α is packing at that lock.

### B3 — max secondary engagement at K/G = 2

At the B2 crossing only, report `γ`, `Π`, `s_grav` — checks whether secondary-link factor `u/(1+u)` adds selection beyond the constraint (expect: **no**, fixed point).

### B4 — marginal stability (floppy/Cauchy bracket)

Argmax `s_grav(u) × exp(−|ln(K/G/2)|)` — v1 A2 relabeled in lattice units; compare landing to B2.

**Legacy (v1):** A1–A3 retained in driver output for relabel audit.

---

## Post-solve diagnostics (NOT verdict)

After forward solve, optionally report (labeled **DIAGNOSTIC**):

- CODATA `p_c = 8πα` and implied `u_codata`
- If `G`, `m_e`, `ℏ`, `c` imported: `G_pred_form = ℏc/(7ξ_local m_e²)` is **NOT computed** (ξ requires α in horizon integral — circular). Report only **`α_G_local ∝ s_grav`** as dimensionless lattice-side coupling proxy.

---

## Outcome map (unchanged from v1)

| Outcome | Condition |
|---|---|
| **CHORD** | B2 (or B1 if distinct) forward `α_pred` within δ_strain |
| **PARTIAL** | within 1.5% |
| **ECHO** | requires α-circular input or >1.5% off |
| **FORK-for-Grant** | B4 ≡ B2 (variational relabel) OR B1 ≠ B2 but B1 lands at floppy edge (unphysical) |

## Expected stance

**Expect B4 ≡ B2 and B1 at floppy/Cauchy edge** — unconstrained max of `Π·γ` favors low `K/G` (high Π) + high `u`, i.e. toward `p_G`, not trace-reversal. **Informative if B1 ≠ B2:** shows gravity-stable projection is a **constraint** (K/G=2), not an unconstrained extremum of `s_grav`.
