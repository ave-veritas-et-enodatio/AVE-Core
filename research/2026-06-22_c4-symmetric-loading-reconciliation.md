# RESULT — C4 "DC bias scales both grades": ALREADY closed in-corpus (symmetric-internal-loading) + the regime taxonomy

**Date:** 2026-06-22 · **Lane:** implementer · **Branch:** `docs/birefringence-arc-2026-06-22`
**Scope:** resolve the C4 residual that appeared to collide with the static-field asymmetry (INVARIANT-S2):
is the canonical "a DC bias scales BOTH μ and ε symmetrically" a genuine collision, or is it a different
regime? Companion to the FORK-1 resolution
([`2026-06-22_node-up-small-large-signal_result.md`](2026-06-22_node-up-small-large-signal_result.md)).
**Class:** **CONSISTENCY.** No new constant; a scoping/citation reconciliation plus the R1/R2/R3 taxonomy.
**Workflow:** `w8d8hyhvz` (C4 location + derivation + regime sweep + adversarial verify).

---

## 0. TL;DR

**C4 is NOT a global claim and there is NO live collision.** "C4" is a **doc-local label** in the
2026-06-05 gravity-sign prereg/result pair (the only globally-numbered canonical invariants are
INVARIANT-S1..S10 in `CLAUDE.md`). The apparent collision with the static-field asymmetry was a
**stale-citation artifact**: the gravity-sign result cited `CLAUDE.md`:58,:60 (pre-W6 layout); the live
content is at `CLAUDE.md`:75, and the **W6 scope commit `e5307e53`** (an ancestor of origin/main, verified
`git branch -r --contains`) already wrote the resolution in verbatim. C4's "both sectors scale" is the
**R1 symmetric-internal-loading** regime (a self-sustained soliton carrying internal `E` AND `B`), NOT a
claim that *any* DC bias scales both. The discriminator is **internal-AC-drive vs external-static**, not
large-vs-small-signal.

## 1. Where "C4" lives and what it says

- The `[C4]` label is defined only at `research/2026-06-05_gravity-sign-frequency-modulation-prereg.md`:38-39,
  scoping itself to "Op14 small-signal varactor-bias modulation at operating point `A₀`" — i.e. the per-node
  **symmetric** operating-point shift, NOT an external static field.
- The compressed gloss "a DC operating-point bias scales BOTH μ and ε symmetrically" appears at
  `..._result.md`:91.
- Every *other* "both-sector" site in the corpus is gravity / symmetric-scaling-scoped (achromatic-lens,
  GW leaves) or is the sector-symmetry-of-the-kernel-form statement (`vol4/claim-quality.md`:132,
  `relativistic-inductor.md`:18: "both are projections of the single Axiom-4 kernel onto the electric and
  magnetic sectors"). The "C4" token elsewhere (`vocabulary-register.md`, `divergence-test-substrate-map.md`,
  loop-gap docs) are **unrelated homonyms** — different C4s.

## 2. The collision dissolves (already reconciled in-corpus)

`CLAUDE.md`:75 (W6 clarification, verbatim) already carries the resolution:

> "this symmetric both-sectors-scale form (S_ε = S_μ = S … Z = Z_0 invariant → reflectionless) is the
> SYMMETRIC-loading operating point — realized when both sectors are driven, e.g. a mass-soliton carrying
> internal E and B (Symmetric Gravity)… **It does NOT follow that any DC bias scales both sectors.** A
> static-E-only drive is ASYMMETRIC: a static field has no ∂B/∂t to load the μ / microrotational (Cosserat-B)
> sector, so it loads the ε / capacitive sector only (S_ε<1, S_μ=1)."

The W6 commit `e5307e53` (titled "W6: scope INVARIANT-S2 'DC bias scales both eps and mu' → symmetric-loading
vs static-E asymmetric") landed ~2.7h AFTER the gravity-sign result and IS the reconciliation. The result
doc was never back-updated, so its line-99 "Not reconciled in this session" and line-138 "R-b open" flags are
**stale** (A43-v2 stale-belief mode — exactly what verify-before-cite exists to catch). The C4 residual is a
stale research-doc flag, not a live open question.

## 3. Why both sectors load internally (the ∂B/∂t mechanism, derived)

The μ-grade does not load on `|B|` — it loads on the circulating current `I` (`relativistic-inductor.md`:15),
and `I` exists only if an EMF drives it, which needs `∂B/∂t ≠ 0` (Faraday).

- **Internal (soliton) case:** the electron is a Beltrami standing wave / resonant LC loop
  (`∇×A = kA`, `electron-unknot.md`:13) ringing at `ω_node`. Internal `B` oscillates ⟹ `∂B/∂t ≠ 0` ⟹ a
  sustained internal EMF ⟹ `I_circ > 0` ⟹ `S_μ < 1`. The orthogonal internal `E` loads the varactor
  ⟹ `S_ε < 1`. Via `∇×A = kA` the two are ONE co-resonant object → they load TOGETHER at `S_ε = S_μ = S`
  → `Z_eff = Z_0` invariant → Γ = 0 reflectionless (op14 cross-sector trading `ρ = −0.990`). This is R1.
- **External static case:** `∂B/∂t = 0` (the `B` is held by the magnet's current) ⟹ no EMF ⟹ no `I_circ`
  ⟹ `S_μ = 1` exactly. Same kernel, opposite verdict — entirely because of `∂B/∂t` internal-vs-zero.

**Derived, not a rescue:** the scope distinction follows from two independently-canonical primitives that
predate the C4 question — (1) μ keyed on `I` not `|B|` (`relativistic-inductor.md`:15), and (2) the soliton
is a standing AC oscillator (`electron-unknot.md`:13) — plus Faraday. Symmetric-standard: standard EM gets
the same pass for DC-vs-AC susceptibility / Pockels-vs-Kerr regime scoping.

## 4. The regime taxonomy (R1/R2/R3) — the operative axis

The clean axis is **internal-AC vs external-static**, NOT the gravity-sign doc's older large-vs-small-signal
(R-a) framing. Numbers are the same as the FORK-1 companion §3 (direct-kernel sweep,
`src/tests/test_vca_node_regime_sweep.py`).

| Regime | Drive | `S_ε` | `S_μ` | `Z_eff` | `δn` | Interpretation |
|---|---|---|---|---|---|---|
| **R1** | symmetric internal soliton (internal `E` AND `B`) | `S` | `S` | `Z_0` invariant | `1/S − 1` | C4 / Symmetric Gravity; reflectionless, clock slows |
| **R2** | external static `E` (∂B/∂t = 0) | `<1` | `1` | `Z_0/√S_ε` (Γ≠0) | `≈ −¼(E/E_yield)²` | the E-route (HIBEF), the REAL test |
| **R3** | external static `B` (∂B/∂t = 0) | `1` | `1` | `Z_0` | `0` exactly | transparent; PVLAS does NOT test AVE |

C4 is scoped to R1. INVARIANT-S2 / static-E is R2. They are each correct in their own regime; the collision
dissolves. The PVLAS verdict (R3) is settled by the node analysis regardless of the C4 framing.

## 5. Propagation item (auditor-lane, surfaced not edited)

The 2026-06-05 gravity-sign **result** and **prereg** docs still carry stale annotations that should point at
the resolution — flag-don't-fix, surfaced for the auditor to land (Rule 12 preserve body, add resolution
back-reference; git-only trail, no in-doc banners per Grant 2026-06-22):

- `...result.md`:99 — "Not reconciled in this session" → resolved by `e5307e53` / `CLAUDE.md`:75 (W6 scope).
- `...result.md`:96-97 — annotate that the winning axis is the **internal-AC vs external-static** re-scope,
  not the large-vs-small-signal R-a reading; mark R-a superseded, don't delete.
- `...result.md`:138 — H3-FLAG → H3-RESOLVED (cite `e5307e53`).
- `...prereg.md`:38-39, :35 — fix stale `CLAUDE.md`:58,:60 → `CLAUDE.md`:75.

These are research-doc-level stale flags, not canonized-claim contradictions; the canonical leaves
(`clm-vca7r1`, `clm-pvlas1`) already carry the resolved taxonomy.

---

### Provenance

C4 reconciliation workflow `w8d8hyhvz`. Companion: the FORK-1 resolution
[`2026-06-22_node-up-small-large-signal_result.md`](2026-06-22_node-up-small-large-signal_result.md).
Canonicalized via PR #357 (`clm-vca7r1`, `clm-pvlas1`). Arc record:
[`_orchestration/2026-06-22_birefringence-vca-bench-arc.md`](../_orchestration/2026-06-22_birefringence-vca-bench-arc.md).
