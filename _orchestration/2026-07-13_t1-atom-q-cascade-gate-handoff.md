# Handoff brief — T1 atom-Q cascade gate (the discriminating gate on the cascade-filter framing)

**Date:** 2026-07-13 · **Grant GO:** 2026-07-13 · **Class:** satellite-session derivation +
consistency driver (self-contained). **Role:** T1 is the **cheapest discriminating test** the
cascade-filter framing owes — derive ONE intermediate rung's loss-Q from substrate.

**Sector header (mandatory).** MODE: derivation-from-canon + numerical consistency solve, NOT
engine-fire. REGIME: cold lattice, sub-yield (no saturation dynamics). PHASE-STATE: a **bound
standing mode** trapped in the **off-line Coulomb-dress mismatch walls** of the atomic
eigencavity. The quantity is the **loss-Q of that bound mode against its mismatch walls** — see
the WHICH-Q declaration under Rails (this is NOT the electron tank's loaded/intrinsic Q).

---

## Mission

Derive the **atom's loss-Q** (the ~10⁷ walk-estimate rung) **from first principles** — as the
**insertion loss of the graded Coulomb-dress impedance-mismatch walls** of the atomic
eigencavity, using the **existing x42 eigencavity machinery** (driver
`src/scripts/vol_2_subatomic/x42_atomic_eigencavity.py`; result
`research/2026-07-10_x42-atomic-eigencavity_RESULT.md`).

The atom is canonically **a wave trapped between its own reflections in a well made of
mismatch**: the electron is a **permanent macroscopic Impedance Mismatch (Γ = −1)** to the
linear vacuum (`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:52`),
and **the atomic orbital is "the precise radius where this trapped bulk-modulus acoustic wave
achieves a lossless resonant impedance match with itself"** (same leaf `:54`, quoted verbatim
in x42 at `research/2026-07-10_x42-atomic-eigencavity_RESULT.md:89`). *(Cite-note: the compact
gloss "a well made of MISMATCH" is a synthesis paraphrase; the verbatim canon is the two
clauses at `:52` + `:54`.)* The off-line dress is already rendered in x42 as an impedance /
mismatch profile `Z(r)` (`RESULT.md:84`).

---

## Stakes (kill-shape — state verbatim)

**This is THE discriminating gate on the cascade-filter framing.** Kill-shape: **if the
framework cannot produce a DISTINCT intermediate rung value, "cascade filter" is the
homogeneous vacuum line relabeled — a vocabulary echo.** A **derived distinct Q kills the
relabel-echo**; a failure to get a distinct value **IS the kill-shape firing.**

The cascade picture only has content if the nested envelopes are **not** the same cell tiled at
different span-lengths. A per-stage cutoff that is genuinely distinct from the endpoints
(electron Q→∞, horizon Q~few) is the first evidence the stages are real filter sections and not
one homogeneous line renamed.

---

## Frozen bins (freeze the tolerance PRE-RUN)

- **(i) DISTINCT-Q-DERIVED.** The machinery returns a **first-principles value within a
  pre-named tolerance of the observed atomic linewidth-class Q** (the ~10⁷ rung). **The
  tolerance must be frozen pre-run** (part of the freeze-by-push prereg) — no post-hoc
  tolerance widening. This bin **kills the relabel-echo.**
- **(ii) NO-DISTINCT-VALUE.** The machinery runs but returns **only endpoint-class or
  degenerate values** (Q→∞ intrinsic, or Q collapsing onto an endpoint, or a value with no
  distinct intermediate structure). **The kill-shape FIRES** — the cascade is a vocabulary echo
  on this rung.
- **(iii) MACHINERY-INSUFFICIENT.** An **honest instrument gap**: x42's eigencavity **cannot
  express the loss channel** (it is a **consistency-class, spectrum-focused Op6 eigencavity with
  NO new primitive**, `RESULT.md:47`; it renders `Z(r)` but was not built to evaluate a
  loss-Q). This is **artifact-class, NOT a physics verdict**: regime discipline — **a null where
  the instrument cannot exist = ARTIFACT**, not a falsification. If (iii), the deliverable is a
  named instrument gap (what the loss channel needs that x42 lacks), not a kill.

---

## Rails (binding)

- **NEVER seed or normalize from α⁻¹ = 137.036.** That is the **electron tank's LOADED /
  radiative Q** — a **Class-B echo, citable as identity only**, never as a seed
  (`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:164`;
  intrinsic-vs-loaded amendment `:145-147`). Baking α into the atom-Q would manufacture the
  distinct value the gate is supposed to test for.
- **The middle rungs are FRAMING, not canon.** The Q-ladder middle rungs (**muon ~3.5×10¹⁷**,
  **atom ~10⁷**) are **FRAMING-tagged walk-estimates** — "walk estimate; order-of-magnitude
  only" at
  `research/2026-07-11_keying-register-walk_framing.md:116` (muon) and `:117` (atom); table
  header `:111-118`. **Only the endpoints are canon** (electron Q→∞, `:115`; BH QNM Q~few,
  `:118`). **The brief's job is to upgrade-or-kill the atom rung**, not to reproduce the
  walk-estimate.
- **Declare WHICH Q — the Q-glyph guards four non-interchangeable electron objects.** The
  Q-glyph ownership row (`theorem-3-1-q-factor.md:158-170`) guards **≥4 non-interchangeable
  electron-scale Qs** (loaded 137.036 `:164`; intrinsic ∞ `:165`; cold-cage ring-down 30.8
  `:166`; structural radiative floor 29.98 `:167`; per-mode Q=ℓ `:168`). The Q being derived
  here is **NONE of these**: it is the **loss-Q of the bound atomic standing mode against its
  off-line Coulomb-dress mismatch walls** — a distinct object (the cavity's insertion loss),
  and the brief must name it as such in the prereg so no downstream cite conflates it with the
  electron tank's Q.
- **Freeze-by-push.** The prereg (with the frozen tolerance) is **its own commit, PUSHED BEFORE
  the driver runs.**
- **Adversarial review wrapper.** ALWAYS use a `scriptPath` wrapper that inlines ARGS and calls
  `workflow({scriptPath: '.claude/workflows/ave-adversarial-pr-review.js'}, ARGS)` — the
  **named-workflow args path silently drops args.**
- **DO-NOT-MERGE.** PR opens `[DO-NOT-MERGE]`; **only Grant merges.**

---

## References (grep-verified anchors — 2026-07-13, at this PR's base d0037d8f)

- `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:52,54`
  — electron = permanent macroscopic Impedance Mismatch (Γ=−1); atomic orbital = the precise
  radius of lossless resonant impedance match. *(Path note: the leaf lives under vol2, not
  common/.)*
- `research/2026-07-10_x42-atomic-eigencavity_RESULT.md:40,47,84,89,198-203` +
  `src/scripts/vol_2_subatomic/x42_atomic_eigencavity.py` — the existing eigencavity machinery;
  consistency-class, no new primitive; `Z(r)` mismatch rendering; Op6-eigencavity owns Q,
  distinct from the (2,3) winding.
- `research/2026-07-11_keying-register-walk_framing.md:111-118` — the Q-ladder;
  muon/atom rungs FRAMING walk-estimates (`:116`, `:117`), endpoints canon (`:115`, `:118`).
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:145-147,158-170`
  — α⁻¹=137 is the LOADED (not intrinsic) Q; Q-glyph ownership guards ≥4 non-interchangeable
  electron Qs.
