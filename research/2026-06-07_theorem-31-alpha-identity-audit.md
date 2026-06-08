# Audit: what is α under AVE first principles? (Theorem 3.1' + cross-scale)

**Status:** FROZEN analysis before native-K4 ceiling test.
**Branch:** `analysis/2026-06-07-two-node-alpha-projection`.
**Drivers:** `alpha_identity_discriminator.py`, `native_k4_gamma_ceiling.py` (complete).
**Question:** Under AVE first principles — is α **derived**, **definitional**, or **operating-point projected**? What cross-scale problems share the same structure?

---

## §1 Executive answer (Grant-facing)

**Most likely under AVE (corpus-weighted):**

α is the **per-cycle reactive leak fraction** `1/Q` at a **Γ = −1 TIR boundary** on the electron LC tank — Sommerfeld "coupling strength" seen from the circuit side.

**Not** the node's torque constant in `(V_inc,V_ref)` complex projection (discriminator dead).

**Classification:**

| Layer | Status |
|-------|--------|
| **Identity of α** | **Class B** substrate-mechanism + **Class E** operating-point projection at `u₀*` |
| **Path A (LC tank)** | **Class A circular** — uses `α = e²Z₀/(4πℏ)` to prove `Q = 1/α` |
| **Path B (Golden Torus Λ-sum)** | **Class B** — geometry at one identification; independent of Path A numerically |
| **Dynamic readout (projection lane)** | **Class D OPEN** — MasterEquationFDTD+PhasorBridge stalls at `Γ ≈ −0.63`, `ε ≈ 0.6` |
| **Dynamic readout (native K4 lane)** | **Class D PARTIAL** — `VacuumEngine3D` reaches `Γ ≤ −0.99` at `V_SNAP ≥ 1`; `ε ≈ 0.0126` (~1.7× α), not exact |

So: **AVE names α correctly; the projection lane does not yet sit at the configuration where the name becomes a measurement. Native coupled K4 can reach near-TIR but still misses α numerically and only at wall amplitude, not rest-energy scale.**

---

## §2 Theorem 3.1' derived-vs-asserted (the fundamental gate)

### Path A — LC-tank (Vol 4 Ch 1)

```text
ω_C L_e = Z₀/(4π α)     [uses SI definition of α]
Q = (ω_C L_e) / (Z₀/4π) = 1/α
```

**Verdict:** **Class A identity** if α is imported. Path A **identifies** Q with 1/α; it does not **derive** α from substrate primitives without α entering.

The corpus is honest: `electron_tank_q_factor.py` Method 1 uses CODATA α.

### Path B — Multipole / Op21 (Vol 1 Ch 8 + op21-multi-mode-mode-counting)

```text
α⁻¹ = Λ_vol + Λ_surf + Λ_line = 4π³ + π² + π   (Golden Torus, Class B)
```

**Verdict:** **Class-B closed form** at named identification (`R·r = 1/4`, phasor-area = Nyquist cell). It evaluates to 137.036 from geometry without α as a *computational* input — but `R·r = 1/4` is **unproven-forced** (forced-vs-fitted undetermined; the `R=φ/2`, `r=(φ−1)/2` Golden-Torus identification is asserted, not derived — see session §18/§25). So this is a **Class-B closed-form consistency identity contingent on a forced `R·r = 1/4`**, not an unconditional "produces 137.036 cold from geometry" derivation. Until `R·r = 1/4` is shown forced (not fitted), the cold-derivation framing overstates it.

### Bridge Q_i = Λ_i

Op21 (Phase 3-A4) derives mode-count = reactance at **Γ = −1** boundary. Strengthens Path B; does not close Path A circularity.

### Leak interpretation (line 81)

> `1/Q = α` per cycle through TIR boundary

This is a **physical identification** contingent on:
1. Full TIR (`Γ → −1`, `Z_core → 0`)
2. Radiation load `R = Z₀/(4π)` per Compton cycle
3. Q from Op21 mode-count = 137

**If any fail, `1/Q = α` is naming, not measurement.**

---

## §3 First-principles challenge (what would falsify the corpus identity)

| # | Challenge | If true → |
|---|-----------|-----------|
| C1 | Native K4 never reaches `Γ < −0.99` at any amplitude | **FALSIFIED on native lane** (Outcome A); **still holds on projection lane** — dual-lane calibration crux |
| C2 | `ε = 1−Γ²` approaches α only at `Γ² = 1−α` | Confirms H1; our scalar lane plateaus at `Γ ≈ −0.63` |
| C3 | Fine-structure tidal scales **α²** not α | Torque-constant picture wrong order |
| C4 | Dark-wake / reactive loss gives **Q ~ 4π** not 137 | Competing loss channel at sub-yield (PR #119 thread) |
| C5 | Three-route `u₀*` mismatch | Class E operating-point falsified (cosmic) |

**Session evidence:** C2 confirmed on projection lane; C1 **split** — native K4 reaches TIR, projection does not; ε at native wall ~1.7× α.

---

## §4 Cross-scale KB — related problems (A-034 / TIR / Q / leak)

Same kernel `S(A) = √(1−A²)`; same **Γ = −1** wall vocabulary at rupture. α appears as **leak/coupling**, not torque, across scales:

| Scale | A-034 row | α or Q role | Relation to electron α |
|-------|-----------|-------------|------------------------|
| **Atomic EM** | Pair creation at `V_yield = √α V_snap` | Yield onset | **Same α**; rupture threshold |
| **Electron tank** | Op21 + Theorem 3.1' | `Q = 1/α` leak | **Definition locus** |
| **BH horizon** | Row 13 | `Γ = −1` shear wall | Same TIR vocabulary; no α number |
| **Parametric kernel** | DAMA / α-slew | `ε_det ∝ 4π/N²`, leak `α m_e c²`/cycle | **Inherits** Theorem 3.1' 4π |
| **Water LLCP** | Row 5 | `r_crit = √(2α)` | **Same α** in yield ratio |
| **Pd shatter** | Row 4 | `√(2α)` volumetric bound | Consistency-class |
| **Cosmic DE** | Row 14b | ε-sector saturation at `R_H` | Operating-point cousin of `u₀*` |
| **Engineered quartz** | Row 21 | Per-node `A₀` tiny at bench V | **Conflation warning** — not vacuum α test |

**Cross-scale throughline:** α enters as **yield/leak ratio** at saturation boundaries, not as **gradient torque stiffness**.

**Open cross-scale problems (same structure as electron calibration crux):**

1. **Rest-energy vs rupture amplitude** — atomic pair creation wants `V_yield`; wall wants `V_snap` (~4× in energy).
2. **SYM vs ASYM-N** — BCS/plasma/cosmic-ε saturate one sector only; electron needs asymmetric Meissner (`S_μ → 0`).
3. **z_local double-write** (genesis audit C3) — bond Γ may read wrong sector.
4. **CAST vs TUNE** — lossless engine lacks equilibration channel (entrainment deep-dive); pumps instead of leaking at α.

---

## §5 Order of operations (fundamental → applied)

1. **This audit** — what α *is* in corpus (§1–2) ✓
2. **Native K4 Γ ceiling** — can engine reach `Γ → −1`? (C1) ✓ **native yes; projection no**
3. **Theorem 3.1' + Op21 consistency** — already corpus-green; no re-derive
4. **Fine-structure tidal α²** — emergence teeth (rotor §7c); later
5. **Ω_freeze three-route** — cosmic Class E; separate arc

---

## §6 Links to session discriminators

- `alpha_identity_discriminator` → H1 mechanism wins; short-term images dead
- `unified_l5_q_leakage` → ε never → α on projection lane
- `two_node_alpha_projection` → projector ≠ α
- `unified_amplitude_gamma_sweep` → calibration crux (rest vs wall amplitude)
