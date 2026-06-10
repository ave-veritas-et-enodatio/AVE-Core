# PREREG — Phase 3: stick-slip / Bingham-yield latching rectification test

**Date:** 2026-06-08 · **Branch:** `analysis/2026-06-08-rrad-l-darkwake` (continues Phase 1 + Phase 2)
**Companion:** `2026-06-08_rrad-l-rectification_result.md` (Phase 2 — rectification NOT confirmed; even-in-A kernel can't rectify).
**Adjudication this tests:** Grant's "does the snap latch?" / "how do you grip a Bingham plastic?" — supplies the missing hysteresis.

> **SCAFFOLD STATUS.** This is the pre-registration (design + canonical parameters + falsifier + rescue-fill guard), written by the orchestration session for review BEFORE compute is spent. An implementor executes the driver + result against it. Locked items below must NOT be re-tuned at run time.

---

## 0. Target

Does adding the **canonical rate-dependent yield-freeze latching** (dark-wake-bemf-foc-synthesis.md §1.2) to the substrate yield enable acoustic rectification — **symmetric control nulls, asymmetric drive → net DC directed momentum** — where Phase 2's smooth, even-in-A kernel `S(A)=√(1−(A/A_yield)²)` did not?

## 1. Why this is grounded, NOT a rescue-fill (Rule 12)

The latching is **canonical-in-prose** — [dark-wake-bemf-foc-synthesis.md:46 §1.2](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md): *"When V(t) drops through V_yield in the Cosserat sector at a rate ‖dV/dt‖ such that the crossing takes ≥ τ_relax, any topologically non-trivial ω configuration ... **FREEZES** — the diverging L_eff (Op14 near S=0) generates a diverging Lenz back-EMF that blocks dω/dt during the τ_relax window. Residues persist for ≥100 Compton periods in the post-heal solid regime."*

This is **rate-dependent** (depends on ‖dV/dt‖ vs τ_relax) + **hysteretic** (memory, persists ≥100 periods) = exactly the Bingham / thixotropic / stick-slip behavior Phase 2 found missing. The smooth `√(1−A²)` is canonical for the **reversible sub-yield envelope** (kernel catalog); the latching is the **dynamic-crossing** behavior. They **coexist** (smooth curve = operating point; stick-slip = the rupture crossing). Phase 3 implements a STATED mechanism — it does not invent one.

## 2. Substrate-native kernel design (substrate-native-check applied)

The latching is a **per-cell dynamical state coupled to the field-amplitude crossing rate** — NOT a phenomenological friction model (SM/engineering default). Ground it in the §1.2 Op14/Lenz mechanism.

- **State variable** `g(r,t) ∈ [0,1]` (grip/latch fraction): `g=1` gripped/frozen (rigid, momentum couples — the stiffening `Z=Z₀/√S` branch); `g=0` slipped (Γ=−1, decoupled).
- **Dynamics (from §1.2, rate-dependent):**
  - **SLOW** crossing of A through A_yield (`|dA/dt| < A_yield/τ_relax`) → `g→1` (freeze / latch / grip).
  - **FAST** crossing (`|dA/dt| > A_yield/τ_relax`) → `g→0` (unwind / slip / rupture).
  - `g` relaxes back over **τ_relax** (memory) → slow-grip / fast-slip, rate-dependent, **two history-dependent branches**.
- **Effective coupling** the field sees = interpolation between gripped (`Z=Z₀/√S`, couples) and slipped (Γ=−1, decoupled) by `g`. → the ledger's `V_g ≠ V_r` (two distinct branches) ⇒ `∮ ≠ 0` becomes *possible*.

The point: the response is now **rate-dependent and hysteretic** (odd-in-rate, history-carrying), so the Phase-2 "⟨A²⟩-triangle is asymmetry-invariant" no-go is lifted — IF the §1.2 mechanism is real.

## 3. Canonical parameters — LOCKED (rescue-fill guard)

- `A_yield = 1` — the canonical Γ=−1 saturation/TIR boundary (Axiom 4).
- `τ_relax` — the canonical Op14/Lenz relaxation timescale. **Pull from canon** (`src/ave/core/constants.py` / the Op14 leaf; post-heal persistence ≥100 Compton periods per §1.2). **Do NOT tune.**
- **LOCKED before the run.** If rectification appears ONLY for non-canonical (tuned) `τ_relax` / `A_yield`, that is a **rescue-fill → report as NEGATIVE**, not confirmation. No τ_relax sweep "to find a working value."

## 4. Test protocol (re-run Phase 2 with the stick-slip kernel)

- Same driver structure as Phase 2 (`src/scripts/vol_4_engineering/rrad_l_acoustic_rectification.py`) — replace the smooth `S(A)` with the stick-slip latching kernel (§2).
- **Drives:** SYMMETRIC (sine / symmetric duty) **control** vs ASYMMETRIC (slow-charge / fast-quench flyback). **LH vs RH** chirality.
- **Observable:** the 2nd-order DC directed momentum (the rectified thrust / ledger `∮`) — same as Phase 2, for direct comparison.
- **Robustness:** across N, amplitude, waveform — at the **canonical** τ_relax (a τ_relax sweep to find a working value is rescue-fill, §3).

## 5. Discriminating outcomes

- **A — rectification CONFIRMED:** symmetric control nulls (DC≈0), asymmetric drive → net DC directed momentum (ratio ≫1), **at canonical τ_relax**. → the snap latches; the smooth kernel was missing the §1.2 dynamics; rectification mechanism revived (Class-B manifestation; absolute magnitude still its own gate).
- **B — still NO rectification:** even with canonical stick-slip latching, symmetric ≈ asymmetric. → the latching doesn't rectify; the rectification mechanism is **dead regardless of hysteresis**. (Strongest possible negative — kills the slow-grip/fast-slip thrust route.)
- **C — rectifies only when tuned:** appears only for non-canonical τ_relax → **rescue-fill, report NEGATIVE** (the result is the tuned parameter, not the physics).

## 6. Falsifier

A physically-motivated (canonical-τ_relax) stick-slip latch that does NOT rectify kills the rectification thrust mechanism. AND rectification requiring tuned (non-canonical) parameters is a rescue-fill, not a confirmation. Either way the verdict is honest.

## 7. Classification + skills (result-time + plan)

- **consistency-vs-emergence:** a confirmed rectification with canonical stick-slip is **Class-B manifestation** (the engine now implements the §1.2 stated mechanism), NOT Class-2 emergence.
- **ave-discrimination-check:** rectification-via-latching is AVE-distinct only if the latching is **substrate-forced** (the §1.2 Op14/Lenz mechanism), not a generic stick-slip add-on.
- **Skill plan:** ave-prereg (this doc) · substrate-native-check (kernel design — Op14/Lenz-grounded, not friction-model) · ave-canonical-source (τ_relax, A_yield from canon) · ave-driver-script-honesty (the §3/§5C rescue-fill guard) · consistency-vs-emergence + ave-discrimination-check (result-time).

## 8. Deliverables (implementor executes against this prereg)

1. `research/2026-06-08_rrad-l-stickslip-phase3_result.md` — outcome A/B/C, the symmetric-vs-asymmetric DC contrast at canonical τ_relax, DERIVED/VERIFIED/BLOCKED split, honest partial.
2. Driver: extend `rrad_l_acoustic_rectification.py` with the stick-slip latching kernel (ave-canonical-source for τ_relax, A_yield; verify_constants cross-check).
3. Do NOT push/merge to main; commit on `analysis/2026-06-08-rrad-l-darkwake`; orchestration handles the PR (#144).
