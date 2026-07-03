# RESULT — Axiom-4 DP-3: the cross-sector combine rule is PER-YIELD-NORMALIZED (single-radius-L2 falsified); L∞-vs-normalized-L2 across grades is UNDERDETERMINED by the electron

**Date:** 2026-07-02
**Lane:** derivation (DP-3 follow-on to the Axiom-4 reduction epic). Analysis + engine-read + adversarial verification.
**Branch:** `analysis/axiom4-combine-rule` (off `origin/main` @ `c9a1188c`)
**Prereg:** [`2026-07-02_axiom4-combine-rule_prereg.md`](2026-07-02_axiom4-combine-rule_prereg.md) (frozen @ `e390d32b`)
**Parent:** Axiom-4 reduction epic (PR #455 MERGED). **Disciplines:** `ave-prereg`, `substrate-native-check`, `pre-test-physics-check`, `consistency-vs-emergence`.
**Method:** 3 derive lenses (coupling-char via engine read / combine-rule derivation / electron acceptance test) → per-lens perspective-diverse adversarial verify → L2-recovery adversary (10 agents). Load-bearing arithmetic + engine combine rule re-verified independently against `origin/main` + `ave.core.constants`.

---

## 0. VERDICT (one line)

**Outcome A directional — but WEAKER than a clean "L∞ wins," and it refines the epic's over-read.** The combine
rule is **per-yield-NORMALIZED** (each sector normalized to its *own* yield) — the **single-radius-L2 sphere**
(`trampoline-framework.md:249`, one shared `V_SNAP²`) is **FALSIFIED** by both the electron (68× short) and the
operative engine. The engine's actual rule is **per-yield-normalized L2-sum *within* a grade, separate kernels
(L∞) *across* grades** — neither `trampoline:249`'s single-radius-L2 nor pure three-mode L∞. **But the electron
does NOT uniquely force L∞** over a per-sector-normalized L2-sum: at the electron's α-suppressed operating point
they are degenerate to O(α) (0.73%). And **`√α` is imported, not derived** (definitional, `constants.py:464`;
α-echo). So: the combine's *normalization structure* is settled (per-yield, single-radius dead); its
*cross-grade aggregation* (L∞ vs normalized-L2) is **underdetermined by the electron** and needs a
non-α-suppressed discriminator. **NOT Outcome C** (coupling doesn't pump, no shared phasor — established);
**NOT Outcome B** (nothing forces joint co-saturation).

---

## 1. What is SETTLED

### 1.1 The coupling ontology survives (D-1)

Grant's "the latter, but coupled" holds. The inter-grade coupling's three load-bearing properties are
**established** (Outcome C not triggered):
- **Conservative / no-pump** — the only allowed inter-grade coupling is a conserved (energize-lock) Hamiltonian
  pair; the realized skew-Hermitian circulator generator (`da/dt=−iHa`, PR#321) conserves norm to machine
  precision (drift 1.9e-11 over 40k steps). `device-circuit-models.md:201`; `2026-06-20_node-circulator-coupling.md:83`.
- **Grade-orthogonal / no-shared-phasor** — A1⊥T2; the grades are two independent amplitudes coupled
  off-diagonally, **never** wired into one `(V_inc,V_ref)` phasor (genesis-24 guard, `master-equation.md:20`).
- **Energy-transferring** — 100% bulk→shear sloshing at fixed total (vs the failed graft-v3 ~2%).
- **Caveat (do-not-overclaim):** the coupling's *form* is a live candidate, not canonical; the trilinear buckle
  **pumps/detonates** in discrete dynamics (demoted B→C); the skew circulator is PARTIAL (2-mode is reciprocal;
  non-reciprocity *magnitude* is imposed = echo). The combine rule rests on the coupling's **properties**
  (conservative + grade-orthogonal + no-shared-phasor), which are established, **not** on any single form.

### 1.2 Single-radius-L2 is DEAD; the combine is per-yield-normalized (D-2, D-3, engine, electron)

The corpus's CEILING-1 as literally written — `trampoline:249` "S(A) acts on the total `A²=ε²+κ²+V²`… at A=1
the wall forms," with the **single shared `V_SNAP²` normalization** of `substrate-perspective-electron.md:56`
— is **falsified on two independent grounds**:
- **The electron:** at confinement, single-radius `A²_total = (V_T2²+V_A1²)/V_SNAP² = 2α = 0.0146` — **68× short**
  of the `=1` wall. It cannot confine at `√α`. (verified: `/tmp` + `ave.core.constants`, `V_SNAP`=511.00 kV,
  `V_YIELD`=43.65 kV, ratio `=√α` to rtol 1e-12.)
- **The engine (operative ground truth):** `cosserat_field_3d.py:411,600` computes
  `A² = ε²/ε_yield² + κ²/ω_yield²` (+ `V²/V_SNAP²`) — a **per-yield-normalized L2-sum** (each term to its *own*
  yield), with **separate kernels `S_mu`, `S_eps` per grade** (`:612-613`). The wall is whichever grade reaches
  `S→0` first → **L∞ across grades, L2-sum within a grade**. The engine does **not** implement a single shared
  radius.

**Settled content:** the combine is **per-yield-NORMALIZED**. Each sector saturates against its own yield;
there is no single shared `V_SNAP²` radius. This is a real reduction of the residual (and a corpus repair — §4).

## 2. What is NOT established (the honest walk-back of "electron leans L∞")

The epic (PR #455) said "the corpus's own confinement physics **leans L∞**." **The DP-3 adversary shows that was
an over-read**, and I confirmed it. The electron kills single-radius-L2 but **cannot discriminate L∞ from a
per-sector-normalized L2-sum**:

| Rule (at the electron: `n_T2=1`, `n_A1=√α≈0.0854`) | fires? | value |
|---|---|---|
| **L∞** = `max(n_T2, n_A1)` | ✅ | 1.000 |
| **per-sector-normalized L2** = `n_T2² + n_A1²` | ✅ | **1+α = 1.0073** (0.73% excess) |
| **single-radius L2** = `(V_T2²+V_A1²)/V_SNAP²` | ❌ | 2α = 0.0146 (**68× short**) |

Because one sector sits at `√α≈0.085`, **`max_i` and quadrature-`sum` differ by only O(α)** — the electron is an
α-suppressed operating point where L∞ and normalized-L2 are degenerate. The engine *codes* L∞-across-grades
(separate kernels), but that is a **modeling commitment**, not independently forced by the electron. The
epic's L∞ lean was directionally right (single-radius-L2 dies; the engine does code L∞-across-grades) but
**overstated the electron's discriminating power**. Retract-don't-refill: the honest claim is
**"per-yield-normalized; cross-grade aggregation underdetermined at O(α)."**

## 3. Classification (consistency-vs-emergence)

- **DERIVED (structure):** the combine is per-yield-normalized (single-radius-L2 falsified) — a **Class-B /
  consistency** structural result of (conservative coupling + per-sector rupture at distinct yields +
  no-shared-phasor), corroborated by the engine implementation. No emergence claimed.
- **IMPORTED (value):** `√α = V_yield/V_snap` is a **definitional α-echo** (`constants.py:464`; `def-vyvsn1`
  "both CALIBRATION, not derived"; Class-C). Every candidate rule *consumes* `√α`; none derives it. The
  structural result must NOT lean on the value — consistent with the corpus-wide FORM-derived/VALUE-imported
  finding.
- **UNDERDETERMINED:** the cross-grade aggregation (L∞ vs normalized-L2). Not resolvable at the electron.

## 4. Corpus repairs surfaced (flag-don't-fix — Grant resolves)

- **(R1) `trampoline-framework.md:249` single-radius-L2 is falsified.** "S(A) acts on the total `A²=ε²+κ²+V²`…
  at A=1" implies one shared normalization; the engine (`cosserat_field_3d.py:411,600`) and the electron both
  reject it. Should be reconciled to **per-yield-normalized** (each mode to its own yield). This is the concrete
  resolution of the epic's flagged **C2**.
- **(R2) `substrate-perspective-electron.md:68` carries the genesis-24 double-count** (the epic's **C1**,
  re-confirmed by D-2's substrate-native verifier): `A²_V=(V_inc²+V_ref²)/V_SNAP²` wires `V_ref` — a read-only
  projection of `V`, NOT an independent DOF (`master-equation.md:20`) — into an additive strain-energy sum. The
  "raw energies add" ground partly rests on this forbidden pair; the correct raw energy is the `(V_inc,Φ_link)`
  conjugate pair. Needs repair.

## 5. Answer to DP-3 (for Grant)

**"L2-sum vs L∞-first?"** resolves as: **neither, as originally posed.** The operative rule (what the engine
computes, and what the electron is consistent with) is:
- **per-yield-NORMALIZED** (each sector/grade to its own yield) — *single-radius-L2 is dead*;
- **L2-sum WITHIN a grade** (`ε²/ε_yield² + V²/V_SNAP²`);
- **L∞ ACROSS grades** (separate `S_mu`, `S_eps` kernels — first grade to `S→0`) — **but this cross-grade L∞ is
  the engine's coded choice, NOT forced by the electron** (a normalized-L2-across-grades is degenerate at O(α)).

So the electron *confirms* per-yield-normalization and *kills* the single-radius-L2, but the cross-grade
aggregation stays a **modeling commitment pending a discriminating test** at an operating point where a sector
is **not** α-suppressed (so `max` and quadrature-sum diverge by O(1), not O(α)).

## 6. Recommended DP-2 axiom-register `residual_content` (HELD — now resolvable)

Recommend Axiom 4 **stays `SHAPE-DERIVED (conditional)`, count 4**, with `residual_content`:

> The L2 norm is **FORCED within each dynamical reactance tank** (Ax1+Ax3). The cross-sector combine is
> **per-yield-NORMALIZED** (the single-radius-L2 total is falsified by the electron + engine). The residual
> axiomatic content is: **(i)** the **cross-grade aggregation rule** — the engine codes L2-within-grade /
> L∞-across-grade, but L∞-vs-normalized-L2 across grades is **underdetermined by the electron** (a non-α-
> suppressed discriminator is needed); **(ii)** the **hard-radius** character (epic F-c); **(iii)** the
> per-sector yield **ratio `√α`** (imported α-echo). Content reduction, not count reduction.

## 7. Decision points → Grant

1. **A new discriminator test** for the cross-grade aggregation (L∞ vs normalized-L2): design at a
   **non-α-suppressed** operating point (symmetric/both-sectors-driven loading, or a non-electron particle,
   where `max` and quadrature-sum diverge O(1)). Recommend as a follow-on; Grant's call whether to pursue.
2. **Corpus repairs R1 (`trampoline:249` → per-yield-normalized)** and **R2 (`:68` `V_ref` double-count)** —
   recommend, Grant rules.
3. **The DP-2 register re-pin** (§6 wording) — recommend, Grant ratifies.

## 8. Outputs

This result + the frozen prereg, landed via a branch + PR (research doc, **NOT a canon change**). No edit to
`axiom-definitions.md`, `eq_axiom_4.tex`, the engine, or the axiom-register.
