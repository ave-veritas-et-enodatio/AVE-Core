# Epic: Path B-prime — K4-TLM (p,q) Band-Splitting Entry-Gate Experiment

**Status**: **GREENLIT 2026-05-27 — Q-PBP-1 ADJUDICATED via canonical corpus survey** (foundational Hopf-on-substrate IS canonical per L3 doc 06 + AVE-HOPF + project-hopf-02.md; chiral $I4_132$ substrate carries Hopf-fiber-bundle structure $S^3 \to S^2$ at framework level via the L3 derivation chain). Path B-prime's specific extension claim (linear-regime K4-TLM transverse-mode (p,q)-classification BEFORE saturation pinch-off) is genuinely-novel and is the substrate-mechanical claim the test designs. Pre-reg committed; implementor session in scope.
**Origin**: Grant insight 2026-05-25 during clm-0ktpcn close-out session — proposed alternative framing to Path B (Faddeev-Skyrme variational) for deriving why electron has (2,3) winding. Reconnaissance + trampoline-analogy synthesis + AVE-HOPF deep dive performed; prereg drafted but parked uncommitted per Grant Option-1 scope-discipline adjudication. Adjudicated 2026-05-27 via vocabulary-broadened pre-survey grep (per `ave-canonical-leaf-pull` v1.3 Trigger 17 discipline-extension landed same session): grepping for "Hopf" / "fibration" / "(p,q)" / "winding-index projection" / "I4_132 + chiral" surfaced L3 archive doc 06 (canonical Hopf-fibration projection $SU(2) \to S^2$ with explicit $(w_1=2, w_2=3)$ identification) + AVE-HOPF sibling repo (canonical hardware expression assuming substrate IS Hopf-structured) + project-hopf-02.md (canonical KB leaf assuming substrate IS Hopf-structured). The framework-level Hopf-on-substrate question Q-PBP-1 framed as "needs Grant adjudication" was already settled by canonical content; only the linear-regime extension is novel. 5th session-time instance of the vocabulary-narrow-pre-survey-miss pattern that Trigger 17 closes; retroactive validation of v1.3 amendment.

## Why this workstream

If the K4 substrate's linear-regime transverse modes are intrinsically $(p,q)$-classified (Hopf-bundle structure on chiral $I4_132$), then deriving why the electron is $(2,3)$ reduces to:
1. (2,3) is the lightest K4-allowed propagation mode (coprimality + minimality on K4-allowed (p,q)-bands)
2. Closure at saturation preserves (p,q) topology via bubble-wand pinch-off (canonical AVE pair-production mechanism)
3. Electron = closure of the lightest mode

This is **substantially cheaper than Path B (Faddeev-Skyrme variational)** because it bypasses the variational analysis entirely — (p,q) becomes a propagation-mode label, not an energy-minimum result.

**HOWEVER**: this hinges on whether the K4 lattice actually carries the Hopf-fiber bundle structure. The chiral $I4_132$ space group has the symmetry; the question is whether the K4 graph specifically inherits a $S^3 \to S^2$ bundle with $U(1)$ fiber compatible with EM propagation. **AVE-HOPF does not formalize this** (per 2026-05-25 deep dive); it would be a new theoretical contribution.

## The pre-reg (parked uncommitted)

Pre-reg draft exists locally at:

[`research/2026-05-25_path-b-prime-k4-dispersion-pq-classification-prereg.md`](../research/2026-05-25_path-b-prime-k4-dispersion-pq-classification-prereg.md)

**Parked status**: per Grant Option-1 adjudication 2026-05-25, the prereg is NOT committed to keep the Golden Torus close-out branch's topical scope clean. When a Path B-prime workstream is formally opened, the prereg should be staged + committed to its own branch (`analysis/path-b-prime-k4-dispersion-pq`) as part of the workstream opening.

The prereg covers:
- 5 frozen metrics (M1-M5) covering band-splitting + ordering + null corollaries + α-decoupling self-check
- 4-outcome verdict map (A CONFIRMED / B PARTIAL / C FALSIFIED / D TAUTOLOGY UNRESOLVED)
- 5 open Grant-adjudication Q's (Q-PBP-1 through Q-PBP-5) — see below
- ~5-9 hour single-session deliverable scope

## Open Q's adjudication status (post 2026-05-27 corpus survey)

**Q-PBP-1** (foundational): **CLOSED GO 2026-05-27 via canonical corpus survey** — Hopf-bundle structure on chiral $I4_132$ substrate is canonical at framework level per L3 archive doc 06 [`research/_archive/L3_electron_soliton/06_winding_index_projection.md`](../research/_archive/L3_electron_soliton/06_winding_index_projection.md) (canonical Hopf-fibration projection $SU(2) \to S^2$ derivation with explicit $(w_1=2, w_2=3)$ Clifford-torus winding identification at Level 1 → Level 2). Cross-references: AVE-HOPF sibling repo (canonical hardware assumes substrate IS Hopf-structured); [`project-hopf-02.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) (canonical KB leaf: "Hopf Coil ((p,q) Torus Knot) forces $\mathbf{A} \parallel \mathbf{B}$... Anomalous Chiral Impedance Match"). The framework-level Hopf-on-substrate is canonical; **only the Path-B-prime-specific extension claim is novel**: linear-regime K4-TLM transverse modes carrying (p,q) labels BEFORE saturation pinch-off (as opposed to canonical L3 doc 06 Hopf-as-projection-between-non-linear-levels). The test gates the novel extension claim, not the foundational Hopf structure.

**Q-PBP-2** (methodology): Is using the existing `kappa_tilde_torus(p,q) = pq/(p+q)` infrastructure (cosserat_field_3d.py:30-100 + test_kappa_tilde_topology.py) the right way to probe (p,q) band-splitting? Or does the (p,q) label need to live on the wave's geometric structure (curve winding on Clifford torus), not on a per-run modulation parameter? Risk: by externally feeding $\tilde\kappa(p,q)$ into the simulator, we may be measuring how the simulator responds to a $\tilde\kappa$ input, not how the substrate naturally classifies modes.

**Q-PBP-3** (scope): Is the falsification of Path B-prime (outcome C, FALSIFIED) a HARD KILL for the Grant-framing intuition, or just "this specific test doesn't show it"?

**Q-PBP-4** (sequencing): Run BEFORE or AFTER fixing the AVE-HOPF crib sheet:25 "K4-TLM simulator has α hardcoded, making verification tautological" finding? The $\tilde\kappa$ refactor partially addresses it but `k4_tlm.py` may not yet consume the refactored path.

**Q-PBP-5** (commit): If outcome is A or C (decisive), commit to `analysis/path-b-prime-k4-dispersion-pq` branch with audit tag? If B or D (inconclusive), how do we want to scope the follow-on?

## Reconnaissance findings (background)

### AVE-HOPF deep dive (2026-05-25)

Net verdict: **AVE-HOPF does NOT have the K4-Hopfion linear-regime mode framework**. It's an experimental wire-antenna falsification platform, not a theoretical framework for K4-Hopfion modes. "Hopfion" in AVE-HOPF = a torus-knot-shaped physical wire antenna, NOT a substrate-mode classification. Mode-ID and "what (p,q) means on the K4 substrate" are explicitly deferred to HOPF-02 bench run (open_questions.md Q7, Q8). The K4-TLM simulator has unresolved α-tautology flaws (crib sheet:25). Building a linear-regime Hopfion mode framework would be a NEW theoretical contribution, not excavation of existing HOPF work.

### Trampoline-analogy synthesis (2026-05-25)

The trampoline-primer's bubble-wand pinch-off (Step 4.5) IS the mechanical closure mechanism Grant's framing requires. The piece beyond the canonical trampoline picture is the claim that propagating waves carry (p,q) labels DURING propagation (Stage B) due to local Hopf-torus geometry, not just AT closure (Stage C). If true: closure freezes whatever (p,q) was instantaneously present; lightest stable (p,q) by knot theory is (2,3); therefore (2,3) electron. The trampoline picture provides the mechanical scaffolding but not the Hopf-bundle formalization.

### Existing infrastructure (2026-05-02 work)

- `kappa_tilde_torus(p,q) = pq/(p+q)` lives in `src/ave/core/cosserat_field_3d.py:30-100`, tested at `src/tests/test_kappa_tilde_topology.py`
- Dispersion driver: `src/scripts/vol_1_foundations/test_lattice_layer_1_dispersion.py` (Phase 1 emergence drivers, 2026-05-02)
- Doc 108 Phase 1 (Layers 0+1) DONE; Phase 3 (Layer 5 α-emergence) NOT EXECUTED — gated by α-tautology concern
- Doc 107 (validate_photon_modeling.py, 2026-05-02) returned FAIL on all 3 doc-30 photon properties — flagged 3 open Q's (Q-A/B/C) that this workstream potentially answers if outcome is A

## Branch + sequencing

- **Recommended branch**: `analysis/path-b-prime-k4-dispersion-pq` off `main` (only after Grant Q-PBP-1 adjudication is positive)
- **NOT to land on**: the closed `analysis/golden-torus-alpha-strengthen` branch — that workstream is done
- **Prereq for kickoff**: Grant Q-PBP-1 adjudication (positive answer required)

## Cross-references

- **Parked prereg**: [`research/2026-05-25_path-b-prime-k4-dispersion-pq-classification-prereg.md`](../research/2026-05-25_path-b-prime-k4-dispersion-pq-classification-prereg.md) (local-only, uncommitted)
- **Origin epic**: [`clm-0ktpcn-golden-torus-alpha-strengthen.md`](clm-0ktpcn-golden-torus-alpha-strengthen.md) — Grant insight surfaced during Phase 2 sub-item 1 work
- **Trampoline primer**: [`manuscript/ave-kb/common/trampoline-analogy-primer.md`](../manuscript/ave-kb/common/trampoline-analogy-primer.md) — mechanical scaffolding for substrate-native picture
- **Doc 108 Phase 1 infrastructure**: [`research/_archive/L3_electron_soliton/108_lattice_fundamentals_emergence_plan.md`](../research/_archive/L3_electron_soliton/108_lattice_fundamentals_emergence_plan.md) — §4.3 Phase 3 (the test infrastructure that already exists, never executed)
- **Doc 107 photon-modeling FAIL**: [`research/_archive/L3_electron_soliton/107_ave_axiom_compliant_rifled_photon.md`](../research/_archive/L3_electron_soliton/107_ave_axiom_compliant_rifled_photon.md) — Q-A/B/C open, this workstream potentially closes Q-A
- **κ̃ refactor**: `src/ave/core/cosserat_field_3d.py:30-100` + `src/tests/test_kappa_tilde_topology.py`

## Status note

If Q-PBP-1 returns negative (no Hopf-bundle structure on $I4_132$), this epic doc + the parked prereg can be archived to `_orchestration/_archive/` with a "FRAMEWORK-EXTENSION ABANDONED, FALLS BACK TO PATH B" header. Path B (Faddeev-Skyrme variational) remains the canonical route to deriving the lightest-coprime selection from energy-ordering.
