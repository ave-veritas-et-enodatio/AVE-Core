[↑ Ch.17 Engine Requirements](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Derivation-support wiring leaf for the ground-up engine-acceptance suite (src/tests/engine_acceptance/). Hosts one sup- node per acceptance test that strengthens a clm-/def- beneficiary's DERIVATION confidence (INVARIANT-S9: a simulation is a sup-, never an exp-). No new substrate-physics claim — every sup- wires an already-canonical claim, authoring quality + on-point fraction as *pending* (INVARIANT-S10: a pending support contributes nothing and never drags a beneficiary to pending)."
sup-id: sup-uiny42
supports:
  - clm-hd9bee: *pending*
sup-id: sup-zf5d1t
supports:
  - def-7c3f9e: *pending*
sup-id: sup-u7r3vu
supports:
  - clm-dfaiwj: *pending*
sup-id: sup-l2ah0k
supports:
  - clm-8nkvwy: *pending*
sup-id: sup-2qja9z
supports:
  - clm-gz7ryg: *pending*
  - clm-8nkvwy: *pending*
sup-id: sup-su0h1a
supports:
  - clm-3npynp: *pending*
  - clm-djpx2v: *pending*
sup-id: sup-iryl5d
supports:
  - clm-djpx2v: *pending*
sup-id: sup-xn9y6c
supports:
  - clm-3npynp: *pending*
  - clm-j550uh: *pending*
sup-id: sup-xey8a8
supports:
  - clm-yr6tu4: *pending*
sup-id: sup-w6tjvs
supports:
  - def-7c3f9e: *pending*
  - def-0pt1ac: *pending*
sup-id: sup-oicgzy
supports:
  - clm-crbl60: *pending*
  - clm-8nkvwy: *pending*
sup-id: sup-1sq5c1
supports:
  - clm-8nkvwy: *pending*
sup-id: sup-lorxuk
supports:
  - clm-k9up5c: *pending*
  - clm-07kd5v: *pending*
sup-id: sup-874l1g
supports:
  - clm-8nkvwy: *pending*
  - clm-5s5b0d: *pending*
sup-id: sup-ftxwil
supports:
  - clm-3zz0f6: *pending*
  - clm-8nkvwy: *pending*
sup-id: sup-evhfcd
supports:
  - clm-sysqaf: *pending*
  - clm-m7qd0w: *pending*
-->

# Engine-Acceptance Suite — Derivation-Support Map (L0–L2 + Op/scale tier)

This leaf wires the ground-up engine-acceptance suite (`src/tests/engine_acceptance/`)
into the KB claim-DAG. The suite is a pytest regression gate built from the medium
up, one excitation-layer at a time, each test a falsifiable physics claim with a
frozen pre-registered pass/fail bin (the orchestration plan
`_orchestration/2026-06-16_groundup-engine-acceptance-plan.md`). Per the §8
STANDING PER-LAYER COMPLETION RITUAL step 1.5 (MAP-TO-SPINE), each green test that
**strengthens** an already-canonical `clm-`/`def-` is materialized here as a `sup-`
derivation-support node.

**Sims register as `sup-`, never `exp-` (INVARIANT-S9).** A simulation is not an
experiment: it feeds a claim's *derivation* confidence (the min-branch), never its
*experimental* solidity. `exp-` is reserved for a physical apparatus AVE designs,
originates, and controls. Each `sup-` here lifts the DERIVATION branch of its
beneficiary.

**Every fraction is `*pending*` (INVARIANT-S10).** The local rigor `quality` and
every `supports:` on-point fraction are authored `*pending*` — this leaf WIRES the
graph; it does not SCORE it. A `*pending*` support contributes nothing to a
beneficiary's `local_quality` and **must never drag a beneficiary with otherwise-valid
quality to pending** (CRITICAL clause, `manuscript/ave-kb/CLAUDE.md:235`). Back-solving
a fraction is forbidden.

**Tests with NO clm-/def- target get NO sup- node** (a `sup-` with no beneficiary is
malformed). Five green tests are medium-validity checks or honest gap-findings with no
positive claim to strengthen — tracked by test-id in the plan §9, not wired here:

- **T0.2** (Z₀ = √(μ₀/ε₀)) and **T0.3** (isotropy) — Class-A identity / medium-validity,
  no `clm-` beneficiary (plan §9 Spine: "— (medium-validity, no clm-)").
- **A1a** (6-DOF/node + srs connectivity) — a STRUCTURE check whose load-bearing output
  is the HONEST DOF-capability FINDING (`carried_dof == 2` vs `axiom_dof == 6`); it
  records a gap, it does not strengthen a positive claim.
- **T1.7** (longitudinal-bulk wave) and **T1.8** (Cosserat micro-rotation wave) —
  STOP-and-report MEDIUM-EXTENSION FINDINGS (the mode is NOT carried). A finding that a
  mode is absent records the precise L3/L4 medium-extension gap; it does not strengthen
  the precursor's derivation. Wiring a `sup-` to a precursor from an absence-finding
  would mis-credit the precursor. Tracked by test-id; not wired.

The matching `### Quality` entries (one per `sup-` above) live in the Vol 9 register
`../claim-quality.md`. The frozen pre-registered bins and the substrate-native-check
walk live in each test's docstring.

## Layer index

| Layer | Test (file) | sup- node | beneficiaries |
|---|---|---|---|
| L0-medium | T0.1 (`test_l0_medium.py`) | sup-uiny42 | clm-hd9bee |
| L0-axioms | A1b (`test_l0_axioms.py`) | sup-zf5d1t | def-7c3f9e |
| L0-axioms | A2 (`test_l0_axioms.py`) | sup-u7r3vu | clm-dfaiwj |
| L0-axioms | A3b (`test_l0_axioms.py`) | sup-l2ah0k | clm-8nkvwy |
| L0-axioms | A4 (`test_l0_axioms.py`) | sup-2qja9z | clm-gz7ryg, clm-8nkvwy |
| L1-photon | T1.1 (`test_l1_photon.py`) | sup-su0h1a | clm-3npynp, clm-djpx2v |
| L1-photon | T1.2 (`test_l1_photon.py`) | sup-iryl5d | clm-djpx2v |
| L1-photon | T1.3 (`test_l1_photon.py`) | sup-xn9y6c | clm-3npynp, clm-j550uh |
| L1-photon | T1.4 (`test_l1_photon.py`) | sup-xey8a8 | clm-yr6tu4 |
| L1-photon | T1.5 (`test_l1_photon.py`) | sup-w6tjvs | def-7c3f9e, def-0pt1ac |
| L1-multiwave | T1.6 (`test_l1_multiwave.py`) | sup-oicgzy | clm-crbl60, clm-8nkvwy |
| L2-em-media | T2.1 (`test_l2_em_in_media.py`) | sup-1sq5c1 | clm-8nkvwy |
| L2-em-media | T2.2 (`test_l2_em_in_media.py`) | sup-lorxuk | clm-k9up5c, clm-07kd5v |
| L2-em-media | T2.3 (`test_l2_em_in_media.py`) | sup-874l1g | clm-8nkvwy, clm-5s5b0d |
| L2-em-media | T2.4 (`test_l2_em_in_media.py`) | sup-ftxwil | clm-3zz0f6, clm-8nkvwy |
| Op/scale tier | Op-primitive + scale-invariance (`test_operators.py`) | sup-evhfcd | clm-sysqaf, clm-m7qd0w |

> **Figures:** each test emits a `<test-id>_debug.png` at
> `research/figures/engine_acceptance/` (KF_VIZ=1; regen via
> `python -m tests.engine_acceptance.regen`), mirrored into
> `manuscript/vol_9_vacuum_datasheet/figures/engine_acceptance/` for the Vol 9 build.
> Figures carry no spine id (§1.5: no `fig-` prefix); each inherits its test's `sup-`
> provenance through this leaf.

---
