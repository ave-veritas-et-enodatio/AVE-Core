# PRE-REGISTRATION — Finkelstein–Rubinstein two-loop BRAID spin-statistics gate

**Date:** 2026-06-20 · **Lane:** implementer (carrier-sector) · **Status:** FROZEN
**Branch:** `carrier-sector/fr-braid-spin-statistics`
**Charter:** [`_orchestration/2026-06-20_carrier-sector-charter.md`](../_orchestration/2026-06-20_carrier-sector-charter.md) §3(b), §5 THE BAR
**Prerequisite operator (on `origin/main` via #312):** `src/ave/topological/k4_lattice_holonomy.py` (signed-Frank, homotopy-invariant, 19/19)

**Discipline applied (this prereg):** `ave-prereg` (corpus-grep BEFORE design — §0) ·
`substrate-native-check` (A4 port-permutations on the connect-map, NOT Cartesian-FD on a
parity-mask — §4) · `phase-space-coordinate-check` (the braid is in REAL-SPACE coords; the
(2,3) winding is PHASE-SPACE — §3) · `consistency-vs-emergence` (the verdict is tagged — §6) ·
`ave-discrimination-check` (the generic-FR-vs-lattice-forced chord-vs-peer call — §2) ·
`verify-before-cite` (every file:line grepped on HEAD — §0).

---

## 0 — VERIFY-BEFORE-CITE ANCHOR LEDGER (all grepped on this worktree off `origin/main` @ `c6950a29`)

| Claim used in this design | Anchor (file:line) | Status |
|---|---|---|
| Electron = real-space `$0_1$` unknot LOOP (min ropelength 2π on K4); the (2,3) is the PHASE-SPACE winding, "NOT a real-space trefoil knot" | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:22-24` (Canonical 4-property def, properties 1-2) | verified verbatim |
| FM / Dirac belt-trick: a single extended closed defect under a 2π rotation reaches a topologically distinct state; 4π returns. Classical topology, no QM. | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md:26-34` (§2.1) | verified verbatim |
| FM derivation does NOT yet address two-particle exchange / spin-statistics ("exchange" appears 0× in that leaf; §8 scope-correction) | `finkelstein-misner-spin-half-derivation.md:165-178` (§8) | verified (absence) |
| FM mechanism lives in REAL-SPACE coords; the (2,3) winding lives in PHASE-SPACE (Clifford torus) — different coordinate systems | `finkelstein-misner-spin-half-derivation.md:176-178` (§9 coordinate-system discipline) | verified verbatim |
| K4 → A4 → 2T ⊂ SU(2); a 2π SO(3) rotation lifts to −I, only 4π to +I | `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md:125-136` (§6) | verified verbatim |
| The RETIRED-for-the-exchange line: "To get an A↔B SWAP (needed for the **bipartite-spinor argument**) … we need reflections (full T_d = S₄)" — SCOPED TO A SUBLATTICE SWAP | `k4-rotation-group.md:121-123` (§5) | verified verbatim — see §4 guard (2) for why it is a CATEGORY ERROR for the carrier |
| The operator refuses ODD/improper perms (reflections in T_d\T) loudly | `src/ave/topological/k4_lattice_holonomy.py:102-107` | verified verbatim |
| The operator self-reports `uses_analytic_qbody: False` (AST proof; never imports the OP_B rotor) | `k4_lattice_holonomy.py:499`, `:628-662` | verified verbatim |
| Single-particle 2π −I = encircle a disclination 3× (C3³, net 2π SO(3), R³=I → −I); signed `net_winding` is the topological invariant | `k4_lattice_holonomy.py:213`, `:573-580`, `:428-493` | verified verbatim |
| The achiral diamond control net (Fd-3m), Grant-ruled correct rotation-topology net for the chirality-INDEPENDENT spin-statistics question | `src/ave/core/chiral_lattice.py:227-275` (`build_diamond_net`) | verified verbatim |
| Charter §5 BAR: discriminator = "was a reflection needed?"; A4-only −1 = CHORD, T_d-reflection-needed = ECHO; the build lands only the single-particle prong, exchange is the OPEN gate | `_orchestration/2026-06-20_carrier-sector-charter.md:124-145` | verified verbatim |

**Anchor corrections recorded (flag-don't-fix, do not silently propagate stale prose):**
- The charter (`charter.md:96-102`, `:144`) cites `k4-rotation-group.md:123` as the EXCHANGE-gate discriminator. That line is scoped to an **A↔B sublattice swap for the bipartite-spinor argument** (`k4-rotation-group.md:121-123` verbatim), which is a **category error** for the carrier exchange — see §4 guard (2). This prereg RE-SCOPES it and SALIENCE-GUARDS against re-citing it as the exchange bar.

---

## 1 — THE QUESTION

Does the AVE substrate **derive**, via Finkelstein–Rubinstein (FR, 1968) configuration-space
topology, the **spin-statistics connection** — that an exchange of two identical carriers
carries a `−1` (Fermi sign) **iff** they are spin-½ (2π-rotation `−1`) — using **A4-only,
reflection-free** lattice transport? Or does the exchange `−1` require an **odd/improper
permutation** (a reflection in `T_d \ T`) that the chiral `I4₁32` net (and its achiral diamond
rotation-topology control) cannot supply?

**Why this is GENUINELY OPEN (not already-closed).** A prior close attempt (orchestration
thread `w257o33nz`) canonized the carrier spin-statistics question as "structurally EXCLUDED"
by reading `k4-rotation-group.md:123` as decisive. A double-check (`wkg5zfrai`, all four
assumption-checks returned FALSE) showed that line is scoped to a **sublattice A↔B swap** for
the bipartite-spinor argument — a **category error** for the carrier. The electron is a
real-space `$0_1$` unknot LOOP (`electron-identification.md:22`), and the exchange of two
identical solitons is a **real-space BRAID**, NOT a permutation of the lattice's A/B
sublattices. Per FR (1968), soliton exchange is **homotopic to a 2π rotation of one soliton**,
so the exchange `−1` flows from configuration-space `π₁(SO(3)) = ℤ₂ → SU(2)` — **rotations
only, no reflection**. The corpus's own FM belt-trick
(`finkelstein-misner-spin-half-derivation.md` §2) + the #312 holonomy operator
(`k4_lattice_holonomy.py`, which **refuses** odd perms at `:102` yet produces `−I` from a pure
A4 `C3³`) already establish the **rotation-only single-particle 2π `−I`**. This gate tests
whether that **transfers to the two-loop EXCHANGE `−1`**, A4-only and reflection-free — the
exact prong the charter (`charter.md:135-145`) names as the open discriminator.

---

## 2 — THE DISCRIMINATOR (PASS / FAIL) + chord-vs-peer sub-discriminator

### 2.1 The primary discriminator (derived-vs-imported)

- **PASS** — the **two-loop exchange holonomy = `−I`** (the `2T` central element, sign `< 0`)
  in `SU(2)`, produced by **A4-only port-permutation transport** of one carrier's worldline
  **around the partner** and back to the exchanged configuration, with **ZERO odd/improper
  (`T_d \ T`) permutations** in the transport (the operator refuses them at
  `k4_lattice_holonomy.py:102`, and the path must never trigger that refusal).
  ⇒ The substrate **DERIVES**, via FR configuration-space topology, the spin-statistics
  connection the SM **IMPOSES** by Lorentz-invariance + microcausality axiom — i.e.
  **ahead-of-SM-axiom** (the SM never derives this from a microscopic substrate; it is an
  axiom-level input — `charter.md:112-115`).

- **FAIL** — the exchange `−1` **requires an odd/improper permutation** (an element of
  `T_d \ T`) that the A4 connect-map cannot supply (the transport HALTS at the `:102`
  refusal, or only a `+I` is reachable A4-only).
  ⇒ **ECHO** — but now **earned on the RIGHT object** (the real-space two-loop braid), not
  the retired sublattice-swap red herring. The structure was imported, not forced by the
  chiral/rotation substrate.

### 2.2 The chord-vs-peer SUB-discriminator (registered HONESTLY, pre-result)

**FR is GENERIC to soliton theories.** *Any* extended-object (topological-soliton) field
theory derives the spin-statistics connection from configuration-space topology — Finkelstein
& Rubinstein (1968), Skyrme model, Sorkin, Balachandran et al. This is textbook soliton
physics. Therefore:

- A **PASS** is **"derived, ahead-of-SM-axiom"** — a real result against the SM's axiom-level
  posit. **BUT** it is **generic-soliton-class = PEER-ahead**, **NOT an AVE-distinct chord**,
  *unless* the **discrete lattice forces the connection in a way a continuum FR leaves free.*

- **What AVE-distinct lattice-forcing would have to look like** (pre-named, so we cannot
  invent it post-hoc):
  1. the exchange `−1` is forced specifically by the **discrete A4 connect-map** (the 12
     tetrahedral rotations / the `2T` cocycle of the *finite* group), such that it **FAILS on
     a non-A4 control** — e.g. a degree-matched but non-tetrahedral connectivity, or an
     A4-subgroup-restricted transport, that **cannot** reach the `−I`; **and/or**
  2. the lattice **selects** the antisymmetric sector rather than merely **admitting** it
     (a dynamical-forcing prong — explicitly out of scope for THIS gate, which is a
     topological-holonomy gate, not a dynamics gate; flagged so the ceiling is honest).

- **If we cannot exhibit (1) or (2), the honest ceiling is PEER-ahead** ("generic-FR,
  derived-ahead-of-SM-axiom, not AVE-distinct") and the result will be reported as such —
  **no chord inflation.** A PASS that is generic-FR is a *peer-level* re-derivation of the
  double-cover→antisymmetry chain shared by every spin-½ formalism (`charter.md:119-122`).
  This gate **does run the non-A4 control** (a degree-matched random-rewire and an
  A4-only-vs-improper comparison) so the (1) prong is *testable* here, not deferred.

**Net pre-registered chord-vs-peer logic:**
`PASS ∧ non-A4-control-fails ⇒ candidate AVE-distinct (lattice-forced)`;
`PASS ∧ non-A4-control-also-passes ⇒ PEER-ahead (generic-FR, not a chord)`;
`FAIL ⇒ ECHO (earned on the braid)`;
`HALT ⇒ tautological/ill-posed setup (see §7)`.

---

## 3 — COORDINATE DISCIPLINE (phase-space-coordinate-check)

The braid is measured in **REAL-SPACE lattice coordinates** — and that is the **correct**
coordinate system, per the corpus's own discipline:

- The carrier exchange is a **real-space** transport of two extended `$0_1$` unknot LOOPS past
  each other on the diamond net (`electron-identification.md:22`, property 1). The braid
  generator `σ` is "worldline of defect-1 encircles defect-2 in real space and returns."
- The FM/`2T` `SU(2)` structure **lives in real-space coordinates** by the corpus's explicit
  ruling: `finkelstein-misner-spin-half-derivation.md:176-178` (§9) — "this derivation lives
  in **real-space coordinates**." The `SU(2)` holonomy is the lift of a **real-space `SO(3)`
  rotation loop**, not a phase-space winding.
- The **(2,3) Clifford-torus winding is PHASE-SPACE** (`(V_inc, V_ref)` Clifford torus —
  `electron-identification.md:23`, property 2; "the (2,3) 'trefoil' is the phase-space
  winding pattern, **NOT a real-space trefoil knot**"). This gate does **NOT** measure the
  (2,3) winding and does **NOT** transport in phase-space coordinates. The holonomy invariant
  read by the operator (`net_winding`, the signed real-space encirclement count —
  `k4_lattice_holonomy.py:428,493`) is a **real-space** winding of a worldline around a defect
  line, which is the FR braid coordinate, **not** the phase-space `(V_inc, V_ref)` winding.

**Coordinate-match assertion (A46):** corpus claim (FR exchange ≅ real-space 2π rotation) and
test measurement (real-space lattice encirclement holonomy in `SU(2)`) are in **matching
coordinates**. No real-space-vs-phase-space mismatch.

---

## 4 — ANTI-TAUTOLOGY GUARDS (mandatory; from `wnyo1z138`)

All six guards are pre-registered as **build requirements** and will be implemented as pytest
assertions (Part B). A guard violation ⇒ HALT (§7), not a silent pass.

1. **WINDING-AROUND-THE-OTHER, not per-defect `C3³`.** The `−1`, if it appears, MUST come from
   **defect-1's worldline winding around DEFECT-2** (the braid `σ` generator: particle-1
   encircles particle-2 and returns to the exchanged config). It MUST NOT come from a per-defect
   `C3³` self-encirclement (which merely re-derives the **single-particle** rotation `−1` of
   `probe_lattice_doublecover` and relabels it "exchange"). **Operationalized:** the braid path's
   `net_winding` around defect-1 (the particle being transported) is **0** (no self-encirclement),
   while its `net_winding` around defect-2 (the partner) is the braid encirclement. The metric is
   the **partner-encirclement** holonomy, never the self-encirclement.

2. **LABEL-FREE.** No reference to the A/B sublattice anywhere (the retired
   `k4-rotation-group.md:123` framing). The verdict is a **topological invariant of the
   two-winding configuration** (`net_winding` of the worldline around the partner defect line),
   computed from node positions + connect-map only. **SALIENCE-GUARD:** `k4-rotation-group.md:123`
   is RETIRED for the exchange question — it must NOT be re-cited as the exchange discriminator
   (it is scoped to a bipartite-spinor **sublattice** swap, `k4-rotation-group.md:121-123`).

3. **REFLECTION-FREE path (ZERO `T_d \ T`).** The transport asserts **zero odd/improper
   permutations**. The operator already refuses them at `k4_lattice_holonomy.py:102-107`; this
   gate KEEPS that refusal armed and additionally **asserts** that every `link_perm` along the
   braid path is an **even** permutation (an A4 element). A reflection appearing anywhere ⇒ FAIL
   (the structure was imported), reported, not worked around.

4. **`uses_analytic_qbody == False`.** No baked `SU(2)` half-angle rotor anywhere. The braid
   holonomy is composed from the connect-map via `rotation_from_port_permutation` (read the
   permutation, never `cos(φ/2)`). The AST self-report (`k4_lattice_holonomy.py:628-662`) is
   asserted `False`. `True` ⇒ HALT (convention-baked).

5. **POSITIVE CONTROL (the metric discriminates, not blind).** A **symmetric / non-braiding**
   two-loop transport — two carriers brought near and returned **without** one encircling the
   other (the trivial / contractible two-particle path) — MUST give **`+I`**. If the symmetric
   control ALSO gives `−I`, the metric is blind (it is firing on something other than the braid)
   ⇒ HALT.

6. **ACHIRAL DIAMOND net (Grant-ruled).** Spin-statistics is **chirality-INDEPENDENT**; the
   correct rotation-topology net is the **achiral diamond** (`build_diamond_net`, Fd-3m —
   `chiral_lattice.py:227`). The gate runs on the diamond. (A chiral `I4₁32` cross-check is
   optional/secondary, not the headline — the chirality is not the carrier of the exchange sign.)

---

## 5 — VALIDATE-ON-KNOWN

The braid operator must reproduce the **braid-group / FR homotopy ladder** before its verdict
on `σ` is admissible:

| Path | Expected | Meaning |
|---|---|---|
| **Contractible** two-particle path (defects far, no encirclement) | `+I` | trivial config-space loop |
| **`σ`** (defect-1 worldline encircles defect-2 once, returns to exchanged config) | **THE TEST** (`−I` predicted by FR) | the single exchange |
| **`σ²`** (double exchange / full loop, defect-1 encircles defect-2 twice) | `+I` | the `4π`-equivalent / identity return |
| **Self-encircle defect-1 3×** (the single-particle `C3³`) | `−I` | the FR cross-check: exchange `−1` must be the **SAME `2T` element** as the single-particle 2π `−I` |

**FR consistency assertion:** IF `σ` gives `−I`, the gate asserts it is the **SAME central
`2T` element** (`q = −1` in `SU(2)`) as the single-particle 2π `−I` from
`probe_lattice_doublecover` — the FR homotopy "exchange ≅ 2π-rotation of one soliton" made
explicit. A `−I` on `σ` that is a *different* `2T` element than the single-particle 2π would
violate the FR homotopy ⇒ HALT (the setup is not actually realizing the FR braid).

---

## 6 — CONSISTENCY-VS-EMERGENCE TAG + symmetric-standard framing

**Classification (pre-registered):** this is a **MANIFESTATION / structural-derivation** gate,
NOT an emergence-of-a-number gate. There is **no CODATA input, no fitted constant, no SI
substitution** — the holonomy reads `sign(q_w)` from integer port-permutation combinatorics
(`k4_lattice_holonomy.py:40` SIGN-only, α-free; `:480`). So the consistency-vs-emergence trap
(headlining emergence when inputs are CODATA-derived) **does not apply** — there are no
dimensionful inputs to launder.

- A **PASS** is tagged **DERIVATION (structural)**: the spin-statistics *connection* is derived
  from the substrate's configuration-space topology, not imported as an axiom.
- The **chord-vs-peer** axis (§2.2) is **orthogonal** to consistency-vs-emergence: even a clean
  structural derivation is **PEER-ahead (generic-FR)** unless the lattice-forcing prong (§2.2.1)
  fires. "Derived" ≠ "AVE-distinct."

**Symmetric-standard framing (consensus-bias guard).** Apply the same yardstick to the SM:
- The SM does **NOT derive** spin-statistics from a microscopic substrate. The spin-statistics
  theorem **assumes** Lorentz invariance + microcausality + energy-positivity and shows
  consistency *requires* the connection — it is an **axiom-level** result, not a mechanism
  (`charter.md:112-115`). So a PASS here is **genuinely ahead of the SM's posture** on this
  specific question — that is the honest peer-mapped framing, not an AVE comedown.
- **BUT** the SM gets no special pass that AVE is denied: if AVE's PASS is *generic-FR*
  (true of any soliton theory), then the honest statement is "AVE, like any soliton theory,
  derives what the SM imposes" — **peer-with-the-soliton-literature**, ahead-of-SM-axiom,
  **not AVE-distinct.** The knife stays symmetric: we do not inflate a generic-soliton result
  to an AVE chord, and we do not discount it below what it is (a real ahead-of-SM-axiom
  derivation).

---

## 7 — HALT CONDITION

**HALT (report honestly; do NOT force a tautological build) IF ANY of:**

1. **Circular setup.** The braid setup must POSIT the (2,3) carrier pair in a way that
   **re-imports the premise** — e.g. the only way to "seed two carriers" bakes in the `2T`
   structure, or the exchange `−1` is structurally identical to the per-defect `C3³`
   (guard 1 fails: `net_winding` around the partner is 0 while the self-encirclement carries
   the sign) — the result is the **single-particle** `−1` relabeled, not the exchange. ⇒ HALT.
2. **Ill-posed exchange.** "Exchange of two identical windings" **cannot be defined label-free**
   (guard 2 fails) — i.e. the only available exchange operator is the A/B sublattice swap
   (the retired framing) and no real-space braid of two distinct defect lines can be
   constructed on the diamond at accessible `L`. ⇒ HALT.
3. **Baked convention.** `uses_analytic_qbody == True` (guard 4). ⇒ HALT.
4. **Blind metric.** The positive control (guard 5) also returns `−I`. ⇒ HALT.
5. **FR homotopy violated.** A `σ` `−I` that is a *different* `2T` element than the
   single-particle 2π `−I` (§5 FR consistency). ⇒ HALT.

A **HALT is a SUCCESSFUL gate outcome** — it means the question is not yet answerable without
re-importing the premise, which is itself the honest finding. A **FAIL (ECHO on the braid)** is
also a successful gate. The only *failure* of this gate is forcing a tautological PASS.

---

## 8 — DELIVERABLES (this prereg freezes the design; Part B builds it)

- `src/ave/topological/fr_braid_exchange.py` — the FR two-loop braid holonomy, extending the
  #312 signed-Frank operator (no new analytic rotor; A4 port-permutation transport only).
- `src/tests/test_fr_braid_exchange.py` — validate-on-known (§5) + the six anti-tautology
  guards (§4) as pytest assertions.
- `research/2026-06-20_fr-braid-spin-statistics_result.md` — the verdict, guard statuses,
  chord-vs-peer call.

**This prereg is FROZEN at the commit that adds it. The discriminator (§2), guards (§4),
validate-on-known (§5), and HALT conditions (§7) are not re-openable post-result (Rule 11 / no
post-hoc criterion-dropping).**
