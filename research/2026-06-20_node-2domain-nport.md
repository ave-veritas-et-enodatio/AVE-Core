# Two-Domain N-Port Equivalent Circuit of ONE Vacuum Node

> **Tracked artifact** for the `feat/node-2domain-nport` branch.
> Scope: an explicit, runnable equivalent-circuit netlist for a single graded-vacuum
> node, with the electrical (EM, Ω) sub-network and the mechanical (shear + bulk,
> Rayl) sub-network joined by an explicit ideal-transformer two-port — plus the
> resolution of the bulk/shear ratio seam (Part 1). Realizes Grant's "draw up the
> circuit + do actual analysis" request. **This is a HYGIENE + disambiguation
> artifact, not a new derivation. α stays an echo.** Driver:
> `src/scripts/vol_9_device/node_2domain_nport.py` (run: `make verify` PASS;
> numbers below are the live driver output). All numbers import from
> `ave.core.constants` — zero hardcoded canonical literals.
>
> **Verify-before-cite:** anchors re-grepped on this worktree (base `origin/main`
> `b8119e15`). `three-channel-impedances.md:22-24`, `constants.py:664,674-676,400`,
> `_bulk.py:102-110`, `crystal_engine.py:27,96`, `graded_vacuum_network.py:67-75,120-124`,
> `node_scattering_multiplicity.py:81`, `vacuum_node_circuit.py:38`,
> `master-equation.md:20`, `device-circuit-models.md:139,195` confirmed.

---

## 0. The one-line answer

| Object | Speed | Ratio | What it IS |
|---|---|---|---|
| **bulk PORT** (canonical) | `c_bulk = √(K/ρ) = √(2G/ρ) = V_LONG` | **√2 = 1.41421** | the A1 **pure-dilatation** CONFINED **MASS** mode (a breathing common-mode), symmetry-decoupled from shear |
| medium **P-wave** | `c_L = √((K+4G/3)/ρ)` | √(10/3) = 1.82574 | the freely-**propagating** longitudinal wave of the medium, which **mixes** A1 dilatation + deviatoric shear |
| prereg compound | `c_bulk·c_L/c₀²` | 2.58199 | **double-count** — multiplies the two distinct longitudinal speeds against one transverse reference; **erroneous** |

**Recommendation (flagged for Grant's ratification — this doc edits no canonical leaf):**
keep the canonical bulk-PORT speed `c_bulk = √(K/ρ) → √2` (already the
`three-channel-impedances.md:22` value); add a one-line disambiguation note that
**√2 is the confined bulk-PORT impedance ratio** while **√(10/3) is the unconfined
medium's P-wave/S-wave propagation ratio** — both correct, for different objects;
**retire 2.582 everywhere** as the flagged double-count. Seam 4
(`device-circuit-models.md:195`, "1.826-vs-2.582 ratio … OPEN pending Grant") is the
exact call this resolves.

---

## 1. The ratio seam — physics (Part 1)

### 1.1 Three conflicting ratios in the corpus

- **√2 = 1.41421** — `three-channel-impedances.md:22-24`: `c_bulk = √2·c₀` labeled
  "bulk dilatational speed, not full P-wave"; `constants.py:674-676` `V_LONG = √(2G/ρ)`
  "Longitudinal wave speed" from `K=2G`; `_bulk.py:102-110` `c_bulk/c₀ = √(K/G) = √2`.
- **√(10/3) = 1.82574** — `graded_vacuum_network.py:120-122` (the solver's α-free
  "primary"): `c_L/c_T = √(2(1−ν)/(1−2ν)) = √(10/3)` at ν=2/7; `crystal_engine.py:27,96`
  `c_L²/c_T² = (K+4G/3)/G |_{K=2G} = 10/3`.
- **√2·√(10/3) = 2.58199** — `prereg:82` headline `Z_bulk/Z_shear = 2.581989`;
  already flagged erroneous in `graded_vacuum_network.py:67-75`.

### 1.2 What each ratio physically IS (verified, not assumed)

**√2 = the bulk PORT.** The bulk port is the **A1 dilatation** = the **CONFINED
internal MASS mode**. In the K4 node's irrep/mode structure it is the **symmetric
breathing common-mode** — the `+1` eigenvector of the node scattering matrix
(`node_scattering_multiplicity.py:81`: "the COMMON MODE = symmetric breathing
channel"). It is **symmetry-decoupled** from the deviatoric shear: the shear lives
on a **separate, differential/deviatoric axis** (`vacuum_node_circuit.py:38`: a
deviatoric strain *splits* the pairs `L_x C_x ≠ L_y C_y`; it is "a SEPARATE axis"
from the common-mode dilatation). A *pure volume change* (the A1 breathing mode)
involves **no shear distortion**, so its restoring stiffness is the **bulk modulus
K alone**:

```
c_bulk = √(K/ρ),   K = 2G   ⇒   c_bulk = √(2G/ρ) = √2·√(G/ρ) = √2·c₀.
```

The transverse photon/shear speed is `c₀ = √(G/ρ)` on the LC lattice
(`constants.py:670-672`), so the bulk-PORT impedance ratio is

```
Z_bulk/Z_shear |_port = (ρ·c_bulk)/(ρ·c_shear) = c_bulk/c₀ = √(K/G) = √2.
```

This is the object the three-channel leaf, the device leaf, `constants.V_LONG`,
`_bulk.py`, and `bulk_rarefaction_sector.py:63` (`z_ref = √2·ρ·c₀`) all wire. The
electron mass-cage IS this confined A1 dilatation (`master-equation.md:20,85`:
`Z_bulk → 0 ⇒ Γ_bulk = −1`).

**√(10/3) = the medium P-wave (a DIFFERENT object).** The *freely propagating*
longitudinal wave of an unconfined isotropic medium is **not** a pure volume change:
a plane longitudinal wave produces uniaxial strain, which **necessarily carries a
deviatoric (shear) component**. Its speed is therefore the **P-wave speed**

```
c_L = √((K + 4G/3)/ρ),   c_T = √(G/ρ) = c₀   (S-wave / shear speed),
c_L/c_T = √((K+4G/3)/G) |_{K=2G} = √(10/3) = 1.82574.
```

The `+4G/3` term is exactly the deviatoric-shear admixture that the **confined A1
breathing mode does not have**. So √(10/3) is the medium's **P-wave-to-S-wave
propagation ratio** — the correct object for `graded_vacuum_network.py`'s
two-mechanical-channels *propagation* gap location, **not** the confined bulk-PORT
impedance. This is standard isotropic elasticity: the dilatational/breathing modulus
is K, the P-wave modulus is `M = K + 4G/3`; they are different moduli for different
modes.

### 1.3 The 2.582 double-count — diagnosed

The prereg formed `Z_bulk/Z_shear = √2·√(10/3) = (c_bulk/c₀)·(c_L/c_T)`. Because
`c_T = c_shear = c₀` on the LC lattice, this product is `c_bulk·c_L/c₀²` — it
multiplies **two distinct longitudinal speeds** (the pure-dilatation `c_bulk` AND
the P-wave `c_L`, which itself already contains the dilatation) against the **same**
transverse reference. That is a physically meaningless compound: you cannot stack a
PORT impedance ratio on top of a propagation speed ratio when both numerators encode
"the longitudinal/bulk speed." `graded_vacuum_network.py:67-75` already caught this
("COMPOUNDS two distinct transverse references") and demoted 2.582 to a non-physical
sensitivity probe, keeping √(10/3) as its α-free primary for the propagation gap it
computes. Both √2 and √(10/3) are α-free, so the double-count never moved a
chord/echo bin — but it is wrong as a *bulk-PORT impedance*.

### 1.4 Recommendation (Grant ratifies)

- **Canonical bulk-PORT speed** = `c_bulk = √(K/ρ) → √2` ratio. This is **already
  the `three-channel-impedances.md:22` value** — no change to the canonical number.
- **KEEP-BOTH-DISAMBIGUATE**: add a one-line note (in the three-channel leaf and/or
  the device leaf) stating: *√2 = the confined A1-dilatation bulk-PORT impedance
  ratio; √(10/3) = the unconfined medium's P-wave/S-wave propagation ratio (`c_L/c_T`,
  the `graded_vacuum_network.py` propagation object) — different physical objects,
  not interchangeable.*
- **Retire 2.582** everywhere as the flagged double-count (it is `c_bulk·c_L/c₀²`,
  not any port or propagation ratio).
- This driver and doc **edit no canonical leaf** — the seam ruling is Grant's.

---

## 2. The explicit 2-domain netlist

ONE vacuum node, three substrate grades on one K4 cell, **two impedance domains**.

```
  ELECTRICAL sub-network (Ω)            MECHANICAL sub-network (Rayl = Pa·s/m)
  ─────────────────────────            ──────────────────────────────────────
                                          ┌──────────── bulk-A1-dilatation ──────────┐
   EM-transverse PORT                     │  Z_bulk = ρ·c_bulk = √2·ρ·c₀ = 3.353e15  │
   ┌───────────────────┐                  │  c_bulk = √(K/ρ) = V_LONG = √2·c₀         │
   │  L_cell = μ₀·ℓ     │   ideal          │  CONFINED: z_core(A)=Z_ref√S → 0 ⇒ Γ→−1  │
   │  C_cell = ε₀·ℓ     │═════════════════▷│      MASS-"3" (A1 Heaviside scalar)       │
   │  √(L/C)=Z₀=376.730 │  TRANSFORMER     │                                          │
   │  ω_LC = c₀/ℓ       │  turns²=ξ_topo²  │              ╳ chiral circulator         │
   │  Γ_EM = 0 (matched │  · (1/p_c, α-leak│              (S ≠ Sᵀ, non-recip)         │
   │   radiative — SOLE │   VISIBLE)       │                                          │
   │   external port)   │                  │  ┌──────────── shear-Cosserat ──────────┐│
   └───────────────────┘                  │  │  Z_shear = ρ·c_shear = ρ·c₀ = 2.371e15││
        1-port S = [Γ_EM]                  │  │  c_shear = √(G/ρ) = c₀                ││
                                           │  │  CONFINED: Γ_shear → −1               ││
                                           │  │      CHARGE-"3" (Cosserat (2,3) wind) ││
                                           │  └──────────────────────────────────────┘│
                                           └──── 2-port S = [[Γ_bulk,t],[−t,Γ_shear]] ─┘
                                              (bulk ⊗ shear, SAME Rayl domain,
                                               coupled via H_couple / circulator)
```

**Live driver numbers** (`src/scripts/vol_9_device/node_2domain_nport.py`):

| Port | domain | Z (cold) | Γ (cold) | confinement | grade |
|---|---|---|---|---|---|
| EM-transverse | electrical (Ω) | 376.730 Ω | **0** (matched) | open radiative — SOLE external | EM transverse photon (2 DOF) |
| shear-Cosserat | mechanical (Rayl) | 2.371×10¹⁵ | 0 (cold match) | **Γ→−1** at sat | Cosserat (2,3) CHARGE-"3" |
| bulk-A1-dilatation | mechanical (Rayl) | 3.353×10¹⁵ | 0 (cold match) | **Γ→−1** at sat | A1 dilatation MASS-"3" |

EM cell: `L_cell = 4.853×10⁻¹⁹ H`, `C_cell = 3.419×10⁻²⁴ F`, `ω_LC = 7.763×10²⁰ rad/s`.

### 2.1 Why per-DOMAIN S-matrices, not one 3×3

The corpus explicitly forbids collapsing the three channels into one homogeneous
3×3 S-matrix (`device-circuit-models.md:139`: "do NOT collapse to one unit" — only
`Z_EM` is electrical Ω; `Z_shear`, `Z_bulk` are mechanical ρ×speed, off by ~12.8 OOM
AND a unit change). So the model carries:

- **electrical 1-port** `S_EM = [Γ_EM] = [0]` (matched radiative).
- **mechanical 2-port** `S = [[Γ_bulk, t_bs],[t_sb, Γ_shear]]` (bulk ⊗ shear, same
  Rayl domain). Isolation leg (H_couple OFF): off-diagonals vanish. Saturated: both
  diagonals → −1.
- **chiral circulator** (inter-sublattice coupling) `S = [[0, e^{+iθ}],[−e^{−iθ}, 0]]`
  — **non-reciprocal** (`S ≠ Sᵀ`, driver-confirmed True) and **unitary** (lossless
  routing; driver-confirmed True). Chirality sign selects matter vs antimatter
  (`crystal_engine.py:41`). It is a **circulator** (lossless routing), not a gyrator.

### 2.2 Confinement = reactive short (Axiom 3, lossless)

Driving `A: 0 → 1` on a confined port: `z_core(A) = Z_ref·√S(A)`, `S(A)=√(1−A²)`
(Axiom 4). `Γ = (z_core − Z_ref)/(z_core + Z_ref) → −1` **monotonically** as A→1
(driver sweep: Γ = 0 → −0.205 → −0.454 → −0.651 → −0.787 → −0.875 → −0.928 at
A = 0.9 … 0.999999). This is a **lossless reactive SHORT** (R=0; the μ-load wall,
PR#260), **never** resistive loss. Consequently **Q → ∞ on the confined ports**;
finite Q enters **only** via the EM matched radiative port (Γ_EM=0 ⇒ energy leaves).

---

## 3. The domain bridge — a TRANSFORMER, not a gyrator; α localized to it

The EM (Ω) and mechanical (Rayl) sub-networks do **not** share a numeric axis (Z_EM
≈ 377 Ω vs Z_mech ≈ 2–3×10¹⁵ Rayl — ~12.8 OOM **and** a unit change). Joining them
needs a **transducer**. AVE uses the **impedance/Maxwell analogy** (across↔across,
through↔through: mass → inductance, `constants.py:389-390`
`EE_TO_TOPO_INDUCTANCE = ξ_topo²`), so the transducer is an **ideal TRANSFORMER**
(a turns-ratio scaling of an across/through pair) — **NOT a gyrator** (which would
swap across↔through, the *mobility* analogy AVE does not use).

The transformer carries **two factors, kept SEPARATE so the α-leak is VISIBLE**:

| Factor | Value | Character |
|---|---|---|
| honest turns² = ξ_topo² | 1.721×10⁻¹³ | **α-FREE** — the honest Ω → kg/s electromechanical map (`constants.py:389-390`) |
| residual p_c = 8πα | 0.183402 | **the α-LEAK** — the lumped↔specific reconciliation factor (`constants.py:400`) |

`Z_referred(Rayl) = Z_EM(Ω)·ξ_topo²/(p_c·ℓ_node²)`. The identity
`(ξ_topo²·μ₀)/(p_c·ℓ²) = RHO_BULK` (`constants.py:664`) makes the α-leak in the
transducer **exactly** the RHO_BULK α-leak — and **only** there. The
mechanical-INTERNAL ratios (`Z_bulk/Z_shear = √2`, bulk/shear) are **α-FREE** (ρ
cancels identically). So **α localizes to EXACTLY this transducer turns-ratio**:
the electron-α-echo is a property of the EM↔mechanical PORT bridge, not of the
mass/charge internal structure.

---

## 4. Honest negatives (no over-claim; α stays an echo)

1. **K = 2G is GR-imported, not forced.** The bulk modulus `K = 2G` (hence the √2
   port ratio) rides on `ν_vac = 2/7`, which is the EMT operating point set by
   `P_C = 8πα` — a calibration input, not a substrate-forced geometry (the K=2G
   crystalline-provenance lane closed: NOT crystalline-geometric, NOT constitutively
   forced; merged PR#261). The √2 ratio is **conditional on K=2G**.

2. **Mass and charge are REPRESENTED, not DERIVED, by this circuit.** The bulk port
   *hosts* the A1 dilatation MASS-"3" and the shear port *hosts* the Cosserat
   CHARGE-"3"; the model wires them as distinct reactive branches and recovers their
   impedances. It does **not** derive `m_e` or `e` — those enter through
   `ℓ_node = ℏ/(m_e c)` and `ξ_topo = e/ℓ_node`. This is a **consistency-class /
   hygiene** re-expression (consistency-vs-emergence), not an emergence claim.

3. **α stays an echo.** The unified 2-domain network buys **HYGIENE** (it makes the
   EM↔mechanical domain boundary explicit, localizes the α-leak to one visible
   transducer factor, and disambiguates the ratio seam) — it does **not** make α
   fall out. The α-localization is a *diagnosis* of where the echo lives, not a
   derivation that turns it into a chord (`device-circuit-models.md:195`: "the
   unified network buys HYGIENE, not a derivation; α stays echo").

4. **The bulk-PORT vs medium-P-wave disambiguation is a units/physics correction,
   not new physics.** Both √2 and √(10/3) already existed in the corpus, correctly,
   for their respective objects; the contribution here is naming which is which and
   retiring the 2.582 compound. Grant ratifies the canonical-leaf wording.

---

## 5. Validate-on-known (the gate)

The driver HALTs unless the cold node recovers all three known anchors (hard
asserts):

| Anchor | Recovered from | Value | const | ✓ |
|---|---|---|---|---|
| Z₀ | cell `√(L_cell/C_cell)` | 376.730313 Ω | 376.730313 | ✓ |
| c₀ | shear `√(G/ρ)` | 2.997925×10⁸ m/s | 2.997925×10⁸ | ✓ |
| Compton clock | `ω_LC = c₀/ℓ_node` | 7.763441×10²⁰ rad/s | `m_e c²/ℏ` | ✓ |

`make verify` PASS. Driver output JSON:
`src/scripts/vol_9_device/_output/node_2domain_nport.json`.

---

## 6. Pointers (verify-before-cite)

| Anchor | Content |
|---|---|
| `three-channel-impedances.md:22-24` | `c_bulk = √2·c₀` "bulk dilatational, not full P-wave" (the canonical bulk PORT) |
| `constants.py:664,674-676,400` | `RHO_BULK`, `V_LONG = √(2G/ρ)`, `P_C = 8πα`, `XI_TOPO` |
| `_bulk.py:102-110` | A1 dilatation MEDIUM extension; `c_bulk/c₀ = √(K/G) = √2` |
| `crystal_engine.py:27,96` | `c_L²/c_T² = (K+4G/3)/G = 10/3` — the medium P-wave object |
| `graded_vacuum_network.py:67-75,120-124` | the 2.582 compound flag + √(10/3) primary |
| `node_scattering_multiplicity.py:81` | A1 = "COMMON MODE = symmetric breathing channel" (+1 eigenvector) |
| `vacuum_node_circuit.py:38` | deviatoric (shear) = SEPARATE differential axis (splits pairs) |
| `master-equation.md:20,85` | A1 ⊥ T2; electron mass-cage = A1 dilatation `Z_bulk→0 ⇒ Γ=−1` |
| `device-circuit-models.md:139,195` | mixed-domain discipline; seam 4 OPEN pending Grant |
