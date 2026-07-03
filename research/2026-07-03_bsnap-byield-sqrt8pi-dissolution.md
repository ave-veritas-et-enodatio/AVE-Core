# B_SNAP vs the E_yield/c duality scale — the √(8π) bridge, KEEP-BOTH ratified

**Date:** 2026-07-03
**Adjudication:** Grant, 2026-07-03 — option (a): DISSOLVED-BY-DERIVATION, KEEP-BOTH.
**Scope:** A2 adjudication of the ⚑ FLAG at
`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md`
(flag block, previously lines 56–64). Records the adjudication; does **not** touch
the Route-C / R3 static-B μ-kernel verdict (that verdict is untouched by design —
the flag itself already says so).
**Classification:** consistency-class / definitional-identity. This is
convention bookkeeping made explicit — **a naming collision dissolved by
derivation**, NOT a chord, NOT an emergence claim, NOT headlined as a discovery.
**Skills applied:** verify-before-cite, ave-canonical-source, consistency-vs-emergence,
substrate-native-check (light — no new physics object), KEEP-BOTH.

---

## 1 — The flag's history (what was flagged, and why it was deferred)

The PVLAS/BMV static-B verdict leaf (`pvlas-static-b-verdict.md`) records that a
static external **B** leaves the μ-grade unloaded (`I_vac = 0 ⇒ A_I = 0 ⇒ S_μ = 1
⇒ δn_μ = 0` exactly; clm-pvlas1, clm-vca7r1, clm-p5cf3t). En route it noted two
DIFFERENT magnetic yield-scales the corpus carries, and flagged that they
"disagree by ~5×", surfacing the tension per flag-don't-fix rather than picking a
scale:

- **B_SNAP = 1.89×10⁹ T** — the **energy-density-matched** scale, defined by
  `B_SNAP²/(2μ₀) = m_ec²/ℓ_node³` (one electron rest energy per K4 unit cell).
  Canonical in `src/ave/core/constants.py` as the symbol `B_SNAP`.
- **E_yield/c ≈ 3.77×10⁸ T** — the **duality image** of the T2 electric yield
  wall, i.e. the `cB ↔ E` duality applied to `E_yield ≈ 1.13×10¹⁷ V/m`.

The flag was explicit that this is a **labeling tension, not a physics defect**
of the static-B verdict: `A_I = 0 ⇒ δn_μ = 0` holds regardless of which B-scale is
adopted, because a static **B** never enters the μ-kernel as an amplitude (the
kernel argument is `I/I_max`, a circulation-rate, not a flux-density). The flag
deferred picking a scale "pending Grant adjudication."

The tension had also been noted in the engine audit chain
(`research/2026-06-22_node-up-small-large-signal_result.md`:276–277,
`research/2026-06-22_vca-r01-mu-keying-derivation.md`:175: "B_SNAP vs E_YIELD/c
are not energy-density duals, differ by ~5.01×"), in
`research/2026-06-24_e4-im3-vacuum-distortion.md`:201, and carried forward in
`research/2026-07-03_historical-exposure-audits_synthesis.md` §Y2 as
"still Grant-deferred". The interlock register
(`common/interlock-register.md`:113–114) records it as Grant-deferred in its
yield consumer-map pointer.

---

## 2 — The derivation: the ratio is EXACTLY √(8π), analytically forced

The "~5×" is not an approximate coincidence. It is `√(8π) = 5.013257`, with **zero
free parameters** and **α cancelling in the bridge**. Every value below is imported
from `src/ave/core/constants.py` per ave-canonical-source; nothing is hard-coded
except the analytic target √(8π). The full numeric re-verification is in §3.

Definitions (all canonical):
- `B_SNAP = √(2 μ₀ m_ec² / ℓ_node³)` — its defining energy-density match
  (`constants.py` `B_SNAP`; equivalently `B_SNAP²/(2μ₀) = m_ec²/ℓ_node³`).
- `E_snap ≡ V_snap/ℓ_node = m_ec²/(e ℓ_node)`. This is the **electric snap
  field-scale**; it is IDENTICALLY the Schwinger field `E_S = m_e²c³/(eℏ) ≈
  1.32×10¹⁸ V/m` (using `ℓ_node ≡ ℏ/(m_ec)`), so `E_snap` here = `E_S` = `constants.py`
  `E_CRIT`. (Named `E_snap` in this derivation to parallel `V_snap` / `B_SNAP`; do
  not coin `E_snap` as a symbol — the canonical name is `E_S` / `E_CRIT`.)
- `E_yield = √α · E_snap = √α · E_S` — the T2 electric yield wall
  (`constants.py` `E_YIELD = V_YIELD/L_NODE`, `V_YIELD = √α · V_SNAP`;
  `E_S/E_yield = 1/√α`, the same √α ladder that separates `V_snap` from `V_yield`).

Chain:

1. `B_SNAP² = 2 μ₀ m_ec² / ℓ_node³`  — the energy-density definition.
2. Multiply by `c²` and use `c² = 1/(μ₀ε₀)`:
   `(c·B_SNAP)² = 2 m_ec² / (ε₀ ℓ_node³)`.
3. `E_snap = V_snap/ℓ_node = m_ec²/(e ℓ_node)`  — the snap field-scale (= E_S).
4. Divide (2) by `E_snap²`:
   `(c·B_SNAP / E_snap)² = 2 e² / (ε₀ ℓ_node · m_ec²)`.
   Substitute `ℓ_node = ℏ/(m_ec)` ⇒ `= 2 e² / (ε₀ ℏ c) = 8π α`
   (using `α = e²/(4πε₀ℏc)`).
   So **`c·B_SNAP / E_snap = √(8π α)`** — this half carries the α.
5. `E_yield = √α · E_snap`, so
   **`c·B_SNAP / E_yield = √(8πα)/√α = √(8π)`** — **α CANCELS.**

Therefore:

```
B_SNAP / (E_yield/c) = c·B_SNAP / E_yield = √(8π) = 5.013257   (exact, α-free)
```

The `8π` is the geometric factor from the energy-density definition (the `2` of
`B²/2μ₀` combined with the `4π` in `α`'s denominator); the α-cancellation is the
key structural point — the bridge between the two scales is a **pure geometric
constant**, independent of the fine-structure calibration.

**Why the two scales are BOTH correct (KEEP-BOTH).** They answer DIFFERENT
questions and neither is the static-B μ-kernel argument:

- **B_SNAP** answers *"what magnetic field stores the cell's rest energy in
  field-energy-density form?"* — the energy-budget question. Used in
  energy-density / node-destruction / Regime-IV arguments (`B²/2μ₀ = m_ec²/ℓ³`).
- **E_yield/c** answers *"what is the duality image of the T2 electric yield
  wall?"* — the field-scale / duality question. Used in
  birefringence-facility / duality arguments (`cB ↔ E_yield`).
- **Neither** is the Route-C static-B μ-kernel argument (circulation-keying,
  `I_vac = 0`). The R3 verdict `A_I = 0 ⇒ δn_μ = 0` is untouched: a static **B**
  never enters the μ-kernel as an amplitude, whichever B-scale a downstream
  argument nominally references.

The two live on a `√(8π)` bridge because one is energy-density-matched (a `B²`
budget) and the other is field-amplitude-matched (a `cB ↔ E` duality). An
energy-density scale and a field-amplitude scale of the same substrate cell are
NOT equal — they differ by exactly the geometric factor the energy integral
introduces. Expecting them to coincide was the naming collision; deriving the
bridge dissolves it.

---

## 3 — Numeric re-verification (canonical constants, < 1e-8)

Script (scratchpad) imports every value from `src/ave/core/constants.py`; run
output:

```
B_SNAP      = 1.890320e+09 T
E_YIELD     = 1.130411e+17 V/m
E_YIELD/c   = 3.770644e+08 T

numeric ratio  B_SNAP/(E_yield/c) = 5.013256549
sqrt(8*pi)                        = 5.013256549
rel err vs sqrt(8*pi)             = 3.26e-11        (< 1e-8 ✓)

step [1] B_SNAP^2 = 2 μ₀ m_ec²/ℓ³      rel 0.0e+00
step [2] (cB_SNAP)² = 2 m_ec²/(ε₀ℓ³)   rel 0.0e+00
step [3] E_snap = V_snap/ℓ = m_ec²/(eℓ) rel 1.9e-16   (= E_S = E_CRIT = 1.323e18 V/m)
step [4] (cB_SNAP/E_snap)² = 8πα       rel 6.5e-11    (= 0.183402)
step [5] cB_SNAP/E_yield = √(8π)       rel 3.3e-11
```

The ratio is **5.013257**, sharper than the flag's stated "~5.0" — the flag
rounded; the exact value is `√(8π)`. Every intermediate step matches to machine
precision or the 1e-8 gate.

---

## 4 — Classification (consistency-vs-emergence)

Tagged **consistency-class / definitional-identity**. Justification:

- Both scales are **algebraic faces of the single imported lattice scale** `m_e`
  (via `ℓ_node ≡ ℏ/(m_ec)`), exactly like the five-face economy at
  `vol1/claim-quality.md`:1399 (frame-checked `claim_survives = false` there —
  a one-import economy, NOT a prediction, NOT a chord). `B_SNAP` inserts `m_ec²`
  by hand in its numerator (`single-substrate-scale.md`:74); `E_yield` is `√α`
  times the snap field. The `√(8π)` bridge between them is therefore a
  **relationship between two definitions**, not a derived observable.
- The `√(8π)` is a **pure geometric constant** with α cancelled — it buys **no
  parameter reduction** and predicts nothing measurable. It is the honest
  book-keeping that the two named scales are consistent (related by a fixed
  geometric factor), not that the substrate independently selects either value.
- **NOT a chord.** No SM-counterfactual is beaten; no forward prediction rides on
  it. This is the same posture as the α-echo and the `E_S = E_yield/√α`
  identities: a consistency match made explicit, not an emergence.

The honest one-line framing for the KB: **"a naming collision dissolved by
derivation — the two magnetic yield-scales are the energy-density face and the
duality face of the same cell, on a fixed √(8π) bridge."**

---

## 5 — Naming ruling (KEEP-BOTH) + the B_yield collision (SURFACED, not forced)

Per the KEEP-BOTH discriminator pattern (add a named axis alongside; never
redefine-in-place):

- **B_SNAP keeps its name and its energy-density definition.** Already canonical
  in `constants.py`. No change.
- **The duality scale gets a DISTINCT name.** The brief proposed `B_yield ≡
  E_yield/c`. **`B_yield` is NOT clean — it is already overloaded in the corpus
  in two CONFLICTING senses**, so per INVARIANT-S12 (a coinage requires 0 prior
  corpus hits, NEVER seeded SOLID) it must not be forced:
  - **Sense A — `B_yield = B_SNAP`** (the energy-density scale): the fdtd engine
    parameter `b_yield` **defaults to `B_SNAP`**
    (`src/ave/core/fdtd_3d_jax.py`:81, `src/tests/test_vca_r01_static_b_mu_keying.py`:26,
    `src/tests/test_vca_node_regime_sweep.py`:18); prose "b_yield = B_SNAP" at
    `vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md`:370;
    `research/2026-05-18_phase3-architectural-pivot.md`:60 ("B_yield = B_SNAP");
    `constants.py`:520 comment ("r = V/V_yield (or B/B_yield)").
  - **Sense B — `B_yield = E_yield/c = 3.77×10⁸ T`** (the duality scale): the
    birefringence facility survey
    `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`:27,140,162.
  - Because `B_yield` already means B_SNAP in the engine/test/prose lane AND
    E_yield/c in the survey lane, adopting `B_yield` for the duality scale would
    **entrench the exact collision this ruling dissolves.**
- **Coinage adopted (collision-free): `B_dual ≡ E_yield/c`** — the duality image
  of the T2 electric yield wall. **VERIFIED 0 prior corpus hits** for `B_dual` /
  `B_DUAL` / `b_dual` across `manuscript/`, `research/`, `src/`. Status:
  **proposed** (per INVARIANT-S12, a coinage is never seeded SOLID; gated on
  auditor + Grant). Added as a `def-` node in `common/vocabulary-register.md`
  with the two-scales/two-questions semantics and the √(8π) bridge cross-link,
  carrying an **open-ambiguity flag against the `B_yield` overload** so the
  mis-use watch-list captures it.

**Surfaced for the PR (not forced):** the `B_yield` surface form is overloaded
(Sense A / Sense B above). The facility-survey doc uses `B_yield` in Sense B; a
follow-on hygiene pass may retag it to `B_dual`, but that is out of this bounded
arc's scope and is flagged rather than swept.

---

## 6 — What changes, what does not

- **No number changes.** `B_SNAP = 1.89×10⁹ T` and `E_yield/c = 3.77×10⁸ T` are
  both unchanged; the ruling is **labeling only** — it names the second scale
  `B_dual`, records that the two are related by the derived `√(8π)` bridge, and
  tags each treatment with the scale it uses. Verified: no site keys a physics
  number on "the two scales being equal"; every site uses one scale or the other
  for its own argument.
- **R3 / Route-C static-B verdict untouched.** `A_I = 0 ⇒ δn_μ = 0` holds
  regardless of B-scale; not edited beyond the flag block. μ-kernel physics not
  expanded.
- **The two treatments** (§ locate):
  - **Treatment keying on B_SNAP (energy-density):** `pvlas-static-b-verdict.md`
    "Not B_SNAP" note (previously :51–54); Vol-9 datasheet
    `chapters/02_absolute_maximum_ratings.tex`:88 and `chapters/14_phase_diagrams.tex`:185.
  - **Treatment keying on E_yield/c (duality, = B_dual):**
    `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`:27,140,162.

---

## 7 — Grant's ruling (verbatim)

> "Yup I agree with a"

Option (a) = ratify KEEP-BOTH with names, record the derived √(8π) bridge, tag
the treatments, close the flag as **DISSOLVED-BY-DERIVATION**.

---

## Deliverables landed by this arc

- KB leaf `pvlas-static-b-verdict.md`: flag block → **RESOLVED (Grant 2026-07-03,
  KEEP-BOTH)** with the √(8π) bridge + two-questions split + pointer here.
- `common/vocabulary-register.md`: `def-` node for `B_dual` (proposed, 0 prior
  hits, open-ambiguity vs `B_yield`).
- `vol4/claim-quality.md`: `clm-` node for the bridge identity
  `cB_SNAP/E_yield = √(8π)` (definitional-identity / consistency).
- Named-scale tags on the two treatments (each cites the def-/clm- ids).
- Manuscript propagation: Vol-9 datasheet clarification where the B_SNAP usage is
  co-located with a duality/yield context (KB-leaf-first lockstep).
