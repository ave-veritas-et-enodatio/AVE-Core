# Dark-wake feedback → α: does the α-FREE loss give Q = 1/α (emergence) or need α (calibration)?

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-07-darkwake-feedback-alpha` (off `analysis/2026-06-07-swept-gamma-omega-A2`)
**Lane:** implementer · **Session type:** implementor (single deliverable)
**Status:** §0–§5 are the **FROZEN PREREG** (frozen before any driver run). §6+ are post-run results.
**Base:** extends `research/2026-06-07_swept-gamma-omega-A2-parametric-characterization.md` §7 (the named immediate-next driver) + `src/scripts/vol_1_foundations/swept_gamma_omega_A2.py` (reuses its Floquet monodromy).

---

## §0 Frame (Grant, electron-synthesis epic) — THE genuine α test

The swept-Γ characterization (PR #118) established the parametric-oscillator-at-threshold picture and split it cleanly:

- the **GAIN** (parametric tongue: pump depth `¼A²`, ridge `2ω_C√(1−¼A²)`) is **α-free geometry** — computed with zero α input, the good non-circular half;
- but **`Q = 1/α`** was demonstrated to be **α-ENCODED**: the swept-Γ stretch had to **set `γ = α·ω_C` by hand**, and the canonical route (`theorem-3-1-q-factor.md:21-40` Path A) lands `Q = 1/α` only by **substituting the SI definition `α = e²Z₀/(4πℏ)`** into the reactance. That is α-in → α-out — the A47 `p_c = 8πα` structural-circularity failure mode (a Class-A/C identity), **not** a derivation of 137.

**This driver feeds the REAL, α-free dark-wake loss in** and re-measures `Q`. The make-or-break:

- **If the α-free dark-wake geometry gives `Q = 1/α ≈ 137` → the first non-circular α route this program has had.** Headline it, with the full input-trace as proof.
- **If `α` (or its SI chain `e, ε₀, ℏ, Z₀, c`) is anywhere in the loss magnitude, or the magnitude is a free knob → CALIBRATION.** Say so as plainly as a positive. A *false* positive is the only failure mode.

**The honest classification IS the deliverable.** This tests α (loss/scale) + the genesis threshold ONLY. The `(2,3)` topological closure (Fork D, phase-space) is SEPARATE — **genesis is NOT closed by this.**

---

## §1 Substrate-native re-walk (`substrate-native-check`) — how `τ_zx` becomes a damping `γ`

The swept-Γ §1 already closed the substrate-native walk for the parametric kernel (bond LC + Op14 → Mathieu/Hill oscillator). This section walks the **new** physics: how the `DarkWakeObserver` `τ_zx` (`vacuum_engine.py:1457`) enters the reduced bond-LC EOM as a damping `γ`, **derived from the shear-wake geometry + lattice, never parameterized.**

**CP1 — the dark-wake is a RADIATION resistance (far-field), not a reactance.** Load-bearing disambiguation, corpus-canonical per [`dark-back-reaction-taxonomy.md:21,29,43`](../manuscript/ave-kb/common/dark-back-reaction-taxonomy.md) (the 2026-05-31 FT-darkwake-crossscale split):
- **dark WAKE = far-field radiated shear stress `τ^far_zx`** — the radiation-reaction analogue; `∫τ dA = F`, propagates backward at `c₀`, carries the Newton-3rd-law reaction momentum, `P_wake = F·c₀`. **This is the LOSS** (energy leaves the oscillator into the substrate behind it). The `DarkWakeObserver`'s real-space `τ_zx = z_local·∂(A²)/∂x` IS this far-field species.
- **dark RESONANCE = near-field reactive self-energy `Σ_near ∝ V²`** — the QED self-energy analogue; internal, at rest, in the `(2,3)` phase space; produces the g-2 saliency. **This is the REACTANCE / mass** (`M_inertial ≡ L_drag`).

**FLAG (for Grant), flag-don't-fix:** the task names the loss as "`M_inertial ≡ L_drag`; the dark wake IS the mutual-inductance back-EMF." Per the canonical taxonomy (post-dating that framing), the **mutual-inductance back-EMF `M_inertial ≡ L_drag` is the NEAR-field reactive piece (dark *resonance*, the mass/reactance)**, while the **dark *wake* proper is the FAR-field radiated piece (the loss)**. They are different substrate objects. This driver feeds the **far-field radiation resistance** (the genuine loss) — which is the correct object for a Q-factor — and the split turns out to be exactly why the answer is what it is (the α-encoding lives in the near-field reactance/mass, never in the far-field loss). Surfaced, not silently reframed.

**CP2 — which sector.** V-sector bond LC, `(V_inc, Φ_link)` conjugate pair. The loss is the bond's radiation resistance `R(A²)` set by the local saturation-modulated impedance `z_local = Z_node/Z₀` (`k4_tlm.py:73-74`, normalized; unstrained `z_local = 1`). Real-space (Γ, A², ω) — the matching coordinate for the loss/gain-ratio question (CP4).

**CP3 — AVE-native objective.** NOT energy minimization. The damped Floquet multiplier `|λ_max|(A², ω, γ)`: `|λ| > 1` gain, `|λ| = 1` the gain=loss locus (self-oscillation), `|λ| < 1` damped. The loss `γ` is the per-cycle radiation through the boundary (Axiom 3 minimum-reflection: at the `Γ = −1` TIR boundary the leak → 0).

**CP4 — the reduction `τ_zx → γ` (the load-bearing derivation).** The bond rings at `A(t)`; the far-field wake radiates power `P_wake` backward at `c₀`. For a damped LC oscillator `q̈ + γq̇ + ω_C²S(A)q = 0`, the radiation resistance `R` gives `γ = R / L_bond`, and `Q = ω_C L_bond / R = ω_C / γ`. The dark-wake radiation resistance is, by construction (`τ_zx ∝ z_local·∇A²`, the local impedance through which the wake escapes):

```
R(A²) = z_local(A²) · R_geom ,   R_geom = Z₀ / (4π)
```

- `R_geom = Z₀/(4π)` is the **canonical radiation impedance per observable Compton cycle** (`theorem-3-1-q-factor.md:75-79`): `Z₀` = the vacuum impedance through which radiated energy escapes; `4π` = K4 bipartite-lobe temporal-phase closure (2 sublattices × 2π phasor rotation, Ax 1 geometry). **Pure geometry — the SAME `R` theorem-3-1 uses; this is the apples-to-apples loss.**
- `z_local(A²)` is the **Op14 saturation modulation** (Ax 4): `S(A) = √(1−A²)`; **low-Z / TIR-short branch** (canonical Meissner μ, `Γ → −1`) `z_local = √S = (1−A²)^{1/4} → 0` at saturation (radiation chokes off → TIR confinement, `Q → ∞`); **high-Z / engine-default branch** (`k4_tlm.py:291`) `z_local = 1/√S = (1−A²)^{−1/4} → ∞`.
- `L_bond` (engine-natural): the bond reactance `ω_C·L_bond = √(L/C) = Z_LC = Z₀ = 1` (the lattice's own characteristic impedance — the bare bond, NOT the electron's calibrated `L_e`).

So, engine-natural (`Z₀ = 1`, `ω_C = 1`):

```
γ(A²)/ω_C  =  z_local(A²) · R_geom / (ω_C L_bond)  =  z_local(A²) / (4π)   [× ρ_Op14]
```

with `ρ_Op14 = 0.990` the canonical bond-pair trade efficiency (`op14-cross-sector-trading.md:11`) — optional ≈1 prefactor. **Every factor — `z_local`, `Z₀`, `4π`, `S(A²)`, `ρ_Op14` — is α-free** (CP traced in full at §3).

**CP5 — saturation-modulated local clock.** Same as swept-Γ: ridge follows `2ω_C√(1−¼A²)` (Op14 down-bend). The loss `γ(A²)` inherits the same `S(A²)` modulation through `z_local`. Both gain and loss bend with the local clock — consistent.

**CP6 — reactance pair.** The Floquet monodromy tracks the full 2-D `(q, q̇)` (C-state `V_inc` + L-state `Φ_link`); the damped multiplier is read on both. Reused unchanged from swept-Γ.

**CP7 — sampling discipline.** Reduced single-bond Floquet — no PML, no lattice extraction. (A future full-engine cross-check would exclude PML per Rule 10; the `DarkWakeObserver` already does, `vacuum_engine.py:1544-1558`.)

**CP8 — generative process.** Characterizes the self-selected operating point (gain=loss) of the saturating bond — the generative precursor's self-bounding amplitude — not a planted `(2,3)`.

**Walk verdict:** the loss is a **substrate-native far-field radiation resistance** `R(A²) = z_local(A²)·Z₀/(4π)`, derived from the shear-wake's escape impedance + the K4 temporal-phase geometry. **No `α·ω_C`, no SI α-definition** — the magnitude is geometry-set. The pump depth `¼A²` and ridge `2ω_C√(1−¼A²)` are pure `S(A)` geometry (swept-Γ §1). The α-classification (§3) is therefore well-posed: trace every input to `γ`.

---

## §2 Phase-space coordinate check (`phase-space-coordinate-check`)

- **Corpus claim under test:** "the dark-wake loss bounds the parametric gain; `Q = ω_C/γ` at the operating point" — a **real-space** statement about the bond's radiation resistance vs its reactance. Coordinates: **real-space (Γ, A², ω)**, the loss/gain ratio. The Floquet multiplier `|λ|` is the per-period reflection gain (impedance-plane native). **MATCH.** ✓
- **Separate axis explicitly NOT addressed:** `α⁻¹_cold = 4π³ + π² + π` (`theorem-3-1` Path B / Golden-Torus mode-count) is a `(V_inc,V_ref)` phase-space multipole observable — a **different mechanism** from the parametric loss/gain ratio. Per the task caveat: **do NOT conflate the parametric `Q` with the multipole `α⁻¹`.** The `(2,3)` topological closure is untouched (genesis NOT closed).

---

## §3 Consistency-vs-emergence pre-classification (`consistency-vs-emergence`) — THE HEADLINE, pre-registered

**Step 1 — target:** `Q = ω_C/γ` at the gain=loss operating point, compared to `1/α = 137.036` (COMPARISON ONLY; α is never an input).

**Step 2 — trace EVERY input to `γ`** (the make-or-break; pre-registered before the run):

| Input to `γ(A²)` | Value / form | Class | α present? |
|---|---|---|---|
| `z_local(A²)` | `(1−A²)^{±1/4}` (Op14 kernel `S=√(1−A²)`) | Axiom-derived (Ax 4) | **NO** |
| `Z₀` (in `R_geom`) | `√(μ₀/ε₀)` (engine-natural → 1) | Identity (Class A; **not** a function of `e,ℏ,α`) | **NO** |
| `4π` (in `R_geom`) | K4 bipartite-lobe temporal-phase closure (2×2π) | Axiom-derived (Ax 1 geometry) | **NO** |
| `ω_C·L_bond = Z_LC` | `√(L/C) = Z₀` (bare-bond reactance, engine-natural) | Engine-natural primitive | **NO** |
| `ρ_Op14` | `0.990` (Pearson trade efficiency, empirical) | Engine-measured (≈1) | **NO** |
| `A²` (operating point) | dimensionless strain, self-selected by gain=loss | Engine-natural state | **NO** |

**Result of the trace: `γ` contains NO `α`, `e`, `ε₀`, `ℏ`, `Z₀`-via-SI, or `c`. The loss is pure geometry of the shear-wake escape impedance + the K4 lattice.** This is the *necessary precondition* for an emergence claim — and it is satisfied (the loss is genuinely α-free, exactly as the gain was). The classification therefore turns entirely on **the magnitude**:

- **`γ(A²→0)/ω_C = 1/(4π) ≈ 0.0796` → `Q_bare = 4π ≈ 12.57`.** Geometry, α-free.
- **`1/α = 137.036`.** The ratio `137/(4π) = 10.905 = 1/(4πα)`.

**Pre-registered classification (fixed before the run — the run measures, cannot move it):**

- **Outcome EMERGENCE (`Q ≈ 137` from α-free `γ`):** would be the first non-circular α route. **Pre-registered as NOT expected**, because `Q_bare = 4π` and there is no geometric reason for the dark-wake radiation-to-reactance ratio of the *bare bond* to equal `137`. To reach `137` the *reactance* must be enhanced `×1/(4πα)` over the bare `Z₀` — and that enhancement is `L_e = (ℓ_node/e)² m_e`, `ω_C L_e = ℏ/e² = Z₀/(4πα)` (`theorem-3-1:32`), **which is α-encoded via the SI definition** (`e, ℏ` CODATA). The 137 lives in the **near-field reactance / mass** (`M_inertial ≡ L_drag → L_e`, CP1), **never in the far-field loss.**
- **Outcome CALIBRATION (`Q ≈ 4π`, NOT 137):** the α-free dark-wake loss gives a geometric `Q ~ O(4π)`; landing `Q = 1/α` requires α-encoding (set `γ = α·ω_C`, OR the α-encoded reactance `Z₀/4πα`). **Pre-registered as EXPECTED.** This confirms `Q = 1/α` is the A47 `p_c = 8πα` / theorem-3-1 Path A consistency-class identity, **not** an emergence of 137. **A clean negative — reported as plainly as a positive.**

**The honest split (pre-registered):** the parametric **LOSS** (`γ`, this driver) is α-free geometry, magnitude `~1/(4π)` → `Q ~ 4π`. The parametric **SCALE** that would make `Q = 1/α` is the α-encoded reactance enhancement (the near-field mass), NOT the loss. **An α-encoded reactance must not masquerade as the loss deriving α.** If the run shows `Q ≈ 4π`: CALIBRATION, the genuine route needs an α-free *reactance* (which the bare bond does not provide — only the geometric Golden-Torus multipole `4π³+π²+π` does, on the SEPARATE phase-space axis).

---

## §4 PREREG block (`ave-prereg`) — frozen

```
PREREG (target: feed the REAL α-free dark-wake loss γ into the bond-LC Floquet EOM;
        measure Q = ω_C/γ at the gain=loss operating point; classify Q→α as
        emergence vs calibration with the FULL input-trace of γ).

Corpus state: PARTIAL — swept-Γ (PR #118) proved gain α-free + Q=1/α α-ENCODED-by-hand;
  named THIS driver as the genuine emergence test (swept-Γ §7). DarkWakeObserver coded +
  observed-not-fed-back (vacuum_engine.py:1457). theorem-3-1 Path A: Q=1/α via SI α-def
  (the route to AVOID). dark-back-reaction-taxonomy: wake=far-field LOSS, resonance=near-field
  REACTANCE. NOT YET DONE: feed the real geometry-set γ in and re-measure Q. This driver does that.

Prior work cited:
  - research/2026-06-07_swept-gamma-omega-A2-parametric-characterization.md §6-§7 (base + the call)
  - src/scripts/vol_1_foundations/swept_gamma_omega_A2.py (Floquet monodromy, reused)
  - src/ave/topological/vacuum_engine.py:1457 (DarkWakeObserver τ_zx = z_local·∂(A²)/∂x)
  - manuscript/.../theorem-3-1-q-factor.md:32,75-79 (R=Z₀/4π geometric; ω_C L_e=Z₀/4πα α-encoded)
  - manuscript/.../dark-back-reaction-taxonomy.md:21,29,43 (far=loss / near=reactance split)
  - manuscript/.../op14-cross-sector-trading.md:11 (ρ_Op14=0.990)
  - src/ave/core/constants.py (ALPHA, Z_0, V_YIELD; ω_C=1, Z₀=1 engine-natural; α COMPARISON ONLY)

Dimensional analysis (Step 3.5 — the magnitudes, engine-natural Z₀=ω_C=1):
  - R_geom = Z₀/(4π) = 1/(4π) = 0.07958.
  - γ(A²→0)/ω_C = z_local(0)·R_geom/Z_LC = 1·0.07958/1 = 0.07958 (×ρ=0.990 → 0.0788).
  - Q_bare = ω_C/γ(0) = 4π = 12.566 (÷ρ → 12.70). NOT 137.
  - 1/α = 137.036; 1/α_cold = 4π³+π²+π = 137.036; 137/(4π) = 10.905 = 1/(4πα). The α-encoding factor.
  - Self-consistent (analytic, low-Z TIR): gain=loss at ε=¼A²=2γ/ω_C ⟹ γ/ω_C=A²/8; dark-wake
    γ/ω_C=(1−A²)^{1/4}/(4π); intersect ⟹ A²_self≈0.53, Q_self=8/A²_self≈15. (Floquet-measured in driver.)
  - To FORCE Q=137: γ=α·ω_C=0.00730 — 10.9× SMALLER than the geometric 0.0796 (α-IN, the toy).

My prediction:
  1. CALIBRATION. The α-free dark-wake γ gives Q_bare = 4π ≈ 12.6 and self-consistent Q_self ≈ 15,
     NOT 137. Every input to γ is α-free (trace §3); the magnitude is geometry-set ~1/(4π).
  2. The loss BOUNDS the pump: dark-wake γ>0 lifts the lossless tongue off the ω-axis; a finite
     gain=loss operating point A²_self exists (low-Z/TIR branch). YES, Fork A's window is real.
  3. The 137 lives in the α-ENCODED reactance (L_e via SI α-def), NOT the loss. Feeding the real
     loss does NOT derive α; it shows Q=1/α is α-in→α-out (theorem-3-1 Path A consistency identity).
  4. Genesis threshold: with the real α-free loss A²_self≈0.5 (low-Z), ABOVE the m_ec² point 0.23 —
     the swept-Γ "0.23/0.057≈4.0" coincidence DISSOLVES (it was an artifact of the α-encoded toy
     loss γ=α giving the tiny A²_self=8α=0.057).

Discriminating outcomes:
  - Outcome CAL (expected): Q_self = O(4π)≈12-20, α-free trace clean, 137 needs α-encoding. →
    Q=1/α is CALIBRATION (consistency identity); the loss is geometry but ~10.9× too large for 137.
  - Outcome EMERGE (the prize): α-free γ gives Q_self = 137.0 to <1%. → FIRST non-circular α route.
    Would require the dark-wake radiation-to-bare-reactance ratio to BE 1/α by geometry (no reason to).
  - Outcome UNBOUNDED: dark-wake γ fails to bound the tongue (no finite A²_self) → loss too weak /
    wrong polarity; reframe (high-Z over-damps, low-Z self-oscillates — characterize both).
  - Outcome KNOB: Q_self depends sensitively on the O(1) reduction coefficient (the 1/4π) → the
    magnitude is a free knob, not geometry-pinned → CALIBRATION by the knob route. (Sensitivity-swept.)

Falsifier (of the CALIBRATION call): if Q_self lands 137.0 ± a few % from the α-free γ AND is robust
  to the O(1) coefficient sweep, the CALIBRATION pre-registration is WRONG and this is EMERGENCE.
  Conversely if Q_self ≈ 4π robustly, EMERGENCE is refused and CALIBRATION holds.
```

**`pre-test-physics-check`:** the framing (dark-wake = loss, feed into bond-LC) is **Grant's**, supplied in the task and named in swept-Γ §7 — pre-collapsed. The one genuinely-open substrate question the walk surfaced — *is the dark-wake a radiation resistance (loss) or a mutual inductance (reactance)?* — is **answered by the corpus** (`dark-back-reaction-taxonomy.md`: the wake is far-field radiation = loss; the `M_inertial≡L_drag` is near-field reactance). Surfaced as a FLAG (CP1) for Grant, not blocked. The remaining modeling choice (the O(1) coefficient in the `τ_zx → γ` reduction) is a numerical detail, not a framing question, and the classification is made **robust to it** via the §6.4 sensitivity sweep.

---

## §5 Driver design (`darkwake_feedback_alpha.py`)

*(frozen design; results in §6+)*

Extends `swept_gamma_omega_A2.py` (imports its `floquet_max_multiplier`, `S_kernel`). Adds:

1. **`darkwake_gamma(A², polarity)`** — the traced α-free loss `γ(A²)/ω_C = z_local(A²)·R_geom·ρ_Op14`, `R_geom = 1/(4π)`, both polarities (low-Z TIR-short / high-Z engine). Emits the full input-trace.
2. **Bounding test** — `|λ_max|` at the Op14 ridge `2ω_C√(1−¼A²)` with `γ = darkwake_gamma(A²)` vs lossless: does the dark-wake lift the tongue off the axis?
3. **Self-consistent operating point** — Floquet bisection `γ_threshold(A²)` (where `|λ|=1`) reused from swept-Γ; intersect with `darkwake_gamma(A²)` → `A²_self`; read `Q_self = ω_C/darkwake_gamma(A²_self)`.
4. **★ α-classification** — `Q_self` vs `1/α`; full input-trace; the α-encoded contrast (`γ=α·ω_C` toy + theorem-3-1 reactance `Z₀/4πα`) shown explicitly as α-in→α-out.
5. **Sensitivity** — sweep `R_geom` coefficient over `[1/(8π), 1/(2π)]` (×4 around `1/4π`); show `Q_self` stays `O(5–30)`, never 137 without α.
6. **Genesis threshold** — `A²_self` vs the m_ec² point `0.23`; does the real loss dissolve the swept-Γ "4×"?

**Outputs:** `darkwake_feedback_alpha_results.json` + `darkwake_feedback_alpha_map.png`.
**Discipline:** `ave-canonical-source` (ALPHA, Z_0 imported; α COMPARISON ONLY; ω_C=Z₀=1 engine-natural) · `consistency-vs-emergence` (§3 trace fixed pre-run) · `substrate-native-check` (§1) · KEEP-BOTH (new driver, no engine mutation).

---
