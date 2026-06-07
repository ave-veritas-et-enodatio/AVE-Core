# Saturation TIR as a moving Γ=−1 impedance boundary (SCOPE / PREREG)

**Date:** 2026-06-06 · **Branch:** `analysis/2026-06-06-saturation-tir-moving-boundary` (off `origin/main` `fc303233`)
**Status:** SCOPE — engine-mechanism design, **build pending Grant's greenlight**. Session: orchestration (Grant in-session).
**Origin:** Grant 2026-06-06, after the four-arm genesis triangulation. Arm C (III) isolated the gap: the engine renders Axiom-4 saturation as a **non-convex energy** `γ(κ²−κ⁴/ω_yield²)` (`cosserat_field_3d.py:661`) → Hamiltonian dynamics **collapse/disperse, never confine**. The corpus mechanism (`photon-identification.md:25`) is an **impedance boundary**: `V→V_yield ⇒ Z→0 ⇒ Γ=−1` — a *reflective TIR wall*. Scope the fix.

---

## §0 The goal

Implement Axiom-4 saturation as a **moving `Γ=−1` reflective boundary** (the wave reflects off its own `Z→0` wall), not an energy minimum — so the **charged ω-shear photon** (Arm C confirmed `charge=helicity` is carried, `chirality_flips_helicity=True`) **self-traps into the standing (2,3)** = the electron. *The electron is a self-trapped photon — via the impedance wall.*

**Why energy collapses but the boundary confines:** the non-convex energy has **no wall** — the field falls inward without limit (collapse). The impedance boundary **is the wall** — the wave reflects (Γ=−1, TIR), so focusing is balanced by reflection → a stable self-made cavity. The missing ingredient is the *reflective stop*, not more energy.

## §1 Canonical anchors (`ave-canonical-leaf-pull` — the boundary/cavity canon)

- **Op3** Universal Reflection `Γ = (Z₂−Z₁)/(Z₂+Z₁)` (`operators.md:43`, CANONICAL). Engine: `_reflection_density` at `cosserat_field_3d.py:266` — **present but used as a diagnostic, not a propagation BC.**
- **Op14** Dynamic Impedance `Z_eff = Z₀/√S` (`operators.md:54`; engine `cosserat_field_3d.py:337`). The **asymmetric-Meissner** specialization `Z_eff = Z₀·√(S_μ/S_ε)` → **Z→0 → Γ=−1** when the **μ-side** saturates (`pair-production-axiom §6`) — *this is the electron's short.*
- **Op21** Quality Factor Phase Transition: `Q = ℓ` for the **Nyquist-cell-resolved confined mode at the `Γ=−1` saturation/TIR boundary** (`operators.md:61`, `op21-multi-mode-mode-counting.md`).
- **Cavity class** (`ave-cavity-class-identification`): the electron = a **self-made TIR cavity** — `Γ=−1` walls, `Q=ℓ`, the (2,3) = the cavity standing-wave mode. Framework: `vacuum-impedance-mirror.md` (saturation-reflection = impedance mirror) + `leaky-cavity-particle-decay/theory.md` + `leaky-cavity-decay.md`.

**Key:** the engine already computes both `Γ` (Op3, `:266`) and `Z_eff` (Op14, `:337`). The mechanism gap is purely that these feed a **diagnostic + an energy term**, never a **reflective boundary condition** in the wave step.

## §2 EE picture (`ave-ee-first-mapping`)

Saturation = a **varactor reaching breakdown** → `Z→0` (a **short**) → `Γ=−1`. A wave hitting a short-circuit termination reflects with `Γ=−1` (TIR). The electron is the ω-wave **bouncing between its own saturation-shorts** — a self-made resonant cavity, `Q=ℓ`. As the wave focuses, its peak hits `V_yield`, the local cell *shorts*, the energy reflects — focusing balanced by reflection → the stable soliton. (Op17 `T²=1−Γ²`: at `Γ=−1`, `T=0`, total confinement.)

## §3 The mechanism (substrate-native — `substrate-native-check` CP1)

The K4-TLM **scatter+connect IS a reflection process** (bonds scatter with impedance-set coefficients) — so imposing `Γ=−1` at saturated sites is **native to the substrate's own dynamics**, NOT a foreign BC. Per cell, per step:
1. Compute the local saturation `S(A)` and `Z_eff` (existing Op14, `:337`); on the μ-side near yield, `Z_eff→0`.
2. Where `A→1` (a moving **saturation front**), set the bond reflection to `Γ=−1` (Op3) — the incident wave **reflects** instead of transmitting. (Wave dynamics — scatter+connect with the saturated Γ — **NOT** the gradient-descent settle `:1384`, **NOT** the non-convex energy term.)
3. The front **moves** as the field evolves; the reflected energy builds the standing wave inside the self-made `Γ=−1` envelope.

## §4 Implementation sketch (KEEP-BOTH)

- New flag `use_impedance_boundary=True` (default OFF → the current energy-saturation behaviour is **unchanged**; audit-trail KEEP-BOTH).
- In the propagation step: where `S(A) < S_thresh` (saturation front), replace the energy-multiplier update with an **Op3 Γ=−1 reflective scatter** at those bonds (total reflection of the incident T₂/ω amplitude).
- Reuse `_reflection_density` (`:266`) for the Γ field and `Z_eff` (`:337`) for the short detection — both already computed.
- Validity: at `A≪1`, `Γ≈0` everywhere (matched, photon propagates — recovers the photon limit); at `A→1`, `Γ→−1` (confined). The mechanism must **smoothly interpolate** matched→reflective across `V_yield`.

## §5 The test (genesis re-run on the new mechanism)

Seed the **ω-shear photon** (Arm C's seeder, `cosserat_field_3d:1600-1643`; charge=helicity confirmed). Drive it; the moving `Γ=−1` boundary reflects it. Checks (forward, no fit):
1. **Self-trap** — does the ω-photon reflect into a **stable standing wave** (vs disperse/collapse)?
2. **(2,3) cavity mode** — extractor `w1→2, w2→3`?
3. **sub-V_yield core + `Γ=−1` skin** — the drop structure (per-phasor `V/V_yield`)?
4. **`Q=ℓ`** (Op21 mode-count at the TIR boundary)?
5. **charge=helicity retained** (Cosserat-ω sector)?
6. **mass=½LI², size≈ℓ_node, ring at ω_C** + matched baseline.

## §6 Outcomes (pre-committed)

- **(I)** the moving `Γ=−1` boundary **confines the ω-photon → standing (2,3), Q=ℓ, charge=helicity** → **the genesis WORKS** — the electron is a self-trapped photon via the impedance wall. Render the animation.
- **(II)** confines (skin forms) but **no (2,3) cavity mode** → the boundary is right, the mode-assembly isn't (localize).
- **(III)** doesn't confine (reflection doesn't stabilize) → the gap is deeper than the energy-vs-boundary choice (re-open).

## §7 Risks + honest scope

- **A real engine-mechanism addition**, not a sim re-run — a moving reflective discontinuity in the propagation (numerically non-trivial: a dynamic Γ=−1 wall can ring/alias if not smoothed across `V_yield`).
- The scatter+connect being natively a reflection process makes this **substrate-native** (CP1-clean), but the moving-front detection + the matched→reflective interpolation are the implementation risk.
- KEEP-BOTH: energy-saturation stays default; the impedance-boundary is the new opt-in. No existing result changes.

## §8 Discipline + deliverable

`ave-canonical-leaf-pull` (Op3/Op14/Op21 + leaky-cavity + impedance-mirror — §1) · `ave-cavity-class-identification` (electron = self-made TIR cavity) · `ave-ee-first-mapping` (varactor-short/reflection — §2) · `substrate-native-check` CP1 (scatter+connect reflection = wave dynamics, NOT energy-min/gradient-descent) · `ave-analytical-tool-selection` (Boundary: Op3/Op17; Mode: Op21) · `ave-prereg` · `ave-evidence-framing` (honest I/II/III; KEEP-BOTH).

**Deliverable (on greenlight):** the `use_impedance_boundary` engine mechanism (`cosserat_field_3d.py` / `vacuum_engine.py`, KEEP-BOTH) + the genesis re-run driver + result. Reviewed PR; no merge. **Build pending Grant's greenlight on the mechanism.**
