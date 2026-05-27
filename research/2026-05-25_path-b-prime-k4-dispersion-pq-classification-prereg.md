# Path B-prime Entry-Gate Pre-Registration — K4-TLM Transverse-Mode (p,q) Band-Splitting Test

**Date**: 2026-05-25
**Workstream**: clm-0ktpcn Golden Torus α Strengthening — Path B-prime exploration (alternative to Path B Faddeev-Skyrme variational)
**Branch target**: TBD per Grant adjudication (candidate: `analysis/path-b-prime-k4-dispersion-pq`)
**Author lane**: orchestration session (Grant + Claude Opus 4.7)
**Status**: PRE-RUN — frozen at draft for Grant adjudication before driver build

---

## §0 — One-paragraph framing

Path B-prime is an alternative route to deriving why the electron has $(2,3)$ phase-space winding. Path B (original) requires a Faddeev-Skyrme variational analysis showing $E[(2,3)] < E[(p,q)]$ for all other $(p,q)$ — multi-session physics work. Path B-prime claims a simpler argument: **if the K4 substrate's linear-regime transverse modes are already $(p,q)$-classified by K4 geometry, then $(2,3)$ as the electron's winding follows mechanically from coprimality + minimality + pinch-off topology-preservation, without requiring an energy-minimum argument.** This pre-reg tests the load-bearing premise: do K4-TLM transverse-mode dispersion bands split by $(p,q)$ topological label in the linear regime, or are they just $\mathbf{k}$-classified?

The test outcome decisively gates Path B-prime as a viable workstream. CONFIRMED → Path B-prime is the cheaper road. FALSIFIED → fall back to Path B (Faddeev-Skyrme). Either result is high-signal per Rule 11.

---

## §1 — Background

### §1.1 What Grant proposed (2026-05-25 dialogue)

> "if a photon is limited to an unclosed (2,3) phase space due to its allowed propagation path due to node compliance, doesn't that just mean an electron occurs when a photon hits a high impenetrable density in terms of nodal voltage and it can't transfer its charge to the node in front of it, reflecting back on itself? and a (2,3) phase space is the definition of a torroid that has 1/2 spin, therefore self cancelling flux intersecting at the classically defined 'point particle' of the soliton?"

The framing stacks five claims:
1. Photons propagating on K4 are constrained to $(p,q)$-classified modes by node compliance (linear-regime claim — **the load-bearing novelty**)
2. The lightest mode = $(2,3)$ trefoil winding on the Clifford-torus phase space
3. "High impenetrable density in nodal voltage" = local $A^2 \to 1$ saturation (canonical Axiom 4 mechanism)
4. "Can't transfer charge forward → reflects" = $\Gamma = -1$ TIR wall (canonical pair-production mechanism)
5. Closure preserves the $(p,q)$ winding the photon was already carrying → $(2,3)$ electron

Claims 3, 4, 5 are corpus-canonical (`pair-production-axiom-derivation.md` + `mass-closure-theorem.md` + `electron-identification.md` "self-trapped photon" framing). Claim 2 is canonical with coprimality + minimality already derived (`torus-knot-uniqueness.md`, clm-8c3yhs). **Claim 1 is the novel piece.** This prereg tests claim 1.

### §1.2 Trampoline-language mapping

In trampoline-primer language, claim 1 says: the K4 trampoline isn't just a buckled-bond lattice; locally it carries a Hopf-fiber bundle structure ($S^3 \to S^2$, $U(1)$ fiber) inherited from the chiral $I4_132$ symmetry. Transverse EM modes propagating on this trampoline don't just have $\mathbf{k}$-classification — they ARE Hopfions, parameterized by $(p,q)$ winding labels on the local Clifford-torus structure. When the wave hits saturation (bubble-wand stage C pinch-off), the $(p,q)$ label is FROZEN by topology-preservation: the bubble cannot unwrap without unwinding $(p,q)$. The smallest stable closed bubble = smallest non-trivial coprime $(p,q)$ = $(2,3)$ electron.

### §1.3 What the corpus has

- **Canonical**: photon = transverse Cosserat shear wave (single sector, ω only, u=0 per doc 30 §3.1)
- **Canonical**: K4 port-space decomposes A₁ ⊕ T₂ with A₁ longitudinal at $c\sqrt{2}$, T₂ transverse at $c$
- **Canonical**: (2,3) torus knot is the smallest non-trivial coprime knot (clm-8c3yhs)
- **Canonical**: photon → electron via pinch-off closure (`pair-production-axiom-derivation.md`)
- **Canonical**: $\kappa_\chi = \alpha \cdot \tilde\kappa$ with $\tilde\kappa(p,q) = pq/(p+q)$ refactor (doc 108 §11.5, `cosserat_field_3d.py:30-100`, tested at `src/tests/test_kappa_tilde_topology.py`)
- **GAP**: whether T₂ modes split into $(p,q)$-labeled bands in the linear regime — NOT tested in corpus

### §1.4 What was already attempted (doc 108)

Doc 108 Phase 1 (2026-05-02) ran K4 dispersion analysis but only checked Layer 0 (port decomposition) + Layer 1 (cardinal vs diagonal kinematics). It established A₁ at $c\sqrt{2}$, T₂ at $c$ — symmetry-irrep splitting only. It did NOT enumerate dispersion bands by $(p,q)$ topological winding. Doc 108 Phase 3 (Layer 5 α-emergence) was gated by an unresolved circularity concern (Q-4) and **not executed**. The $\tilde\kappa$ refactor was completed but not used in a $(p,q)$-band-splitting test.

This prereg picks up exactly where doc 108 Phase 1 left off: extend the dispersion analysis to enumerate $(p,q)$-bands using the existing $\tilde\kappa$ infrastructure.

### §1.5 Doc 107 empirical context (2026-05-02)

`validate_photon_modeling.py` driver established that the `CosseratBeltramiSource` doesn't produce a doc-30-compliant photon — u/ω = 0.354 (corpus says u=0), A²_max = 71× linear-regime threshold, helicity sign bug. Three open Q's were flagged (Q-A: is u=0 realizable; Q-B: real amplitude threshold; Q-C: helicity sign convention).

**This prereg potentially answers Q-A**: if K4 transverse modes are intrinsically $(p,q)$-classified and the "photon = Cosserat ω only" framing is interpretive overreach, then u≠0 isn't a bug — it's what photons actually are in K4-Cosserat-coupled dynamics. The (p,q) label lives on the COUPLED mode, not the pure ω sector.

---

## §2 — Hypothesis

**H1 (LOAD-BEARING)**: K4-TLM transverse-mode dispersion $\omega(\mathbf{k}, p, q)$ in the linear regime exhibits discrete band-splitting indexed by torus-knot winding number $(p,q)$, with band-energy ordering:

$$\omega_{(2,3)}(\mathbf{k}) < \omega_{(2,5)}(\mathbf{k}) < \omega_{(3,4)}(\mathbf{k}) < \omega_{(3,5)}(\mathbf{k}) < \omega_{(3,7)}(\mathbf{k}) \ldots$$

with the ordering matching the knot-theoretic crossing-number sequence ($c=3, 5, 8, 10, 14, \ldots$) at fixed $\mathbf{k}$.

**H1-corollary (NULL)**: Modes with $\gcd(p,q) > 1$ (e.g., $(2,2), (2,4), (3,6)$) do NOT form stable bands (they are multi-component links, not knots).

**H1-corollary (NULL)**: $(1, q)$ modes are unknots and degenerate with the trivial $\mathbf{k}$-classified continuum (no distinct band structure).

**H0 (NULL HYPOTHESIS)**: K4-TLM transverse modes are $\mathbf{k}$-classified only. No discrete $(p,q)$ band-splitting in the linear regime. The $(p,q)$ topology is a closure-stage label assigned at pinch-off, not a propagation-stage label.

---

## §3 — Pre-registered discriminating outcomes

| Outcome | Probability | Diagnostic |
|---|---|---|
| **A (CONFIRMED)** | ~30% | Discrete $(p,q)$-band-splitting observed with knot-theoretic ordering. $(2,3)$ at lowest energy. $(1,q)$ and $\gcd>1$ pairs do NOT form distinct bands. **Path B-prime alive.** |
| **B (PARTIAL)** | ~25% | Some $(p,q)$ labeling appears but ordering wrong, OR labeling holds only at certain $\mathbf{k}$, OR null corollaries violated. Framework incomplete; needs further theoretical work before commitment. |
| **C (FALSIFIED)** | ~30% | T₂ modes are $\mathbf{k}$-classified only. No $(p,q)$ splitting. **Path B-prime dead. Fall back to Path B (Faddeev-Skyrme).** |
| **D (TAUTOLOGY UNRESOLVED)** | ~15% | The α-tautology in K4-TLM simulator (per AVE-HOPF crib sheet:25) cannot be cleanly decoupled even with $\tilde\kappa$ refactor — test inconclusive. Need engineering fix before re-test. |

---

## §4 — Methodology

### §4.1 Substrate + driver

- **Substrate**: K4-TLM only (no Cosserat continuum overlay; staying in port-space-mode regime). `src/ave/core/k4_tlm.py` engine.
- **Driver candidate name**: `src/scripts/vol_1_foundations/test_lattice_pq_dispersion_classification.py`
- **Build basis**: extend existing `test_lattice_layer_1_dispersion.py` infrastructure (doc 108 Phase 1, 2026-05-02) — DO NOT build new dispersion solver from scratch.
- **Domain**: $N = 64$ K4 cube, PML = 8, linear regime (amp_factor = 0.001·V_yield), 480 steps minimum (sample ~30 periods for clean FFT).

### §4.2 $(p,q)$ enumeration

Test the following $(p,q)$ candidates per `kappa_tilde_torus(p,q) = pq/(p+q)`:
- **Stable knot candidates** (coprime, both ≥ 2): $(2,3), (2,5), (2,7), (3,4), (3,5), (3,7)$ — 6 modes
- **Null candidates (must NOT band-split)**: $(1,1), (1,2), (1,3)$ — unknots; $(2,2), (2,4), (3,6)$ — links

For each, inject a sub-yield transverse mode with $\tilde\kappa$-modulated chiral coupling using the `kappa_tilde_torus(p,q)` function. Measure the resulting dispersion $\omega(\mathbf{k})$ via FFT of `V_inc(x, y, z, port, t)` time-domain data.

### §4.3 Decoupling α from the simulator

Per AVE-HOPF crib sheet:25 the K4-TLM simulator has α hardcoded into κ_chiral, making any (p,q)-coupling test tautological. The $\tilde\kappa$ refactor (cosserat_field_3d.py:30-100) decouples α — but `k4_tlm.py` may not yet use the refactored code path. The first build step is to **verify the dispersion driver uses `kappa_tilde_torus(p,q)` as the topology input, NOT a pre-multiplied α·$\tilde\kappa$ constant**.

If `k4_tlm.py` doesn't expose $\tilde\kappa$ as a per-run free parameter, the prereg outcome is automatically D (TAUTOLOGY UNRESOLVED) and the driver build expands to "refactor k4_tlm.py to use $\tilde\kappa$ as a free input" before the actual test runs.

### §4.4 Data analysis protocol (frozen pre-run)

Per A47 v11b discipline — these metrics are FROZEN before any driver runs:

```python
PREREG_METRICS = {
    # Band-splitting test
    "M1_distinct_bands_required": 6,  # one per stable knot candidate
    "M1_band_separation_threshold": 0.05,  # ≥5% ω spacing between adjacent bands at fixed k
    "M1_pq_label_assignment_via": "match peak omega to kappa_tilde_torus(p,q) modulation frequency",

    # Ordering test (knot-theoretic c-number prediction)
    "M2_ordering_required": ["(2,3)", "(2,5)", "(3,4)", "(2,7)", "(3,5)", "(3,7)"],
    "M2_ordering_match_threshold": "exact (all 6 in correct order)",

    # Null corollary 1: (1,q) unknots degenerate with k-continuum
    "M3_unknot_band_separation_max": 0.01,  # (1,q) bands < 1% separated from baseline T₂ continuum

    # Null corollary 2: gcd>1 pairs not stable bands
    "M4_gcd_gt1_band_stability_max": 0.1,  # (2,2), (2,4), (3,6) bands < 10% amplitude of (2,3) baseline

    # Tautology check
    "M5_alpha_independence": "vary kappa_tilde input ±20%; band positions must scale linearly with kappa_tilde, NOT remain pinned to alpha-hardcoded value",
}
```

### §4.5 Verdict mapping

- **A (CONFIRMED)**: M1 ✓ AND M2 ✓ AND M3 ✓ AND M4 ✓ AND M5 ✓
- **B (PARTIAL)**: M1 ✓ but at least one of M2/M3/M4 fails
- **C (FALSIFIED)**: M1 fails (no $(p,q)$ band-splitting)
- **D (TAUTOLOGY UNRESOLVED)**: M5 fails (bands pinned to α-hardcoded value)

---

## §5 — What we WILL NOT do (scope discipline)

- **NOT** formalize the K4 Hopf-fiber bundle structure theoretically — that's downstream of this test (only fired if outcome A)
- **NOT** run nonlinear / saturation tests (linear regime only — Axiom 4 not engaged)
- **NOT** extend to Cosserat-coupled dynamics (K4-TLM port-space only)
- **NOT** address doc 107 Q-A/Q-B/Q-C (separate workstream; outcome A would inform Q-A but not solve it)
- **NOT** write new KB leaves until the test result lands
- **NOT** integrate with AVE-HOPF wire-antenna physics (HOPF-02 territory)
- **NOT** validate the result against PDG-2024 mass spectrum (this is a substrate-mode-classification test, not a particle-mass prediction)
- **NOT** rebuild the K4-TLM simulator (use existing infrastructure; refactor only if needed for M5)

---

## §6 — Acceptance criteria (pre-frozen)

- **PASS to commit**: all 5 metrics evaluated honestly per Rule 11; outcome A/B/C/D classification reported decisively; no post-hoc threshold redefinition
- **FAIL to commit**: ANY of (a) thresholds adjusted after seeing data, (b) verdict reframed to avoid honest classification, (c) driver code includes hardcoded α anywhere it shouldn't (M5 self-check)
- **Engineering bug acceptable**: if a bug is found during driver build (e.g., k4_tlm.py doesn't expose $\tilde\kappa$), fix it and re-document under §4.3; the prereg's HYPOTHESIS isn't redefined
- **Outcome D path forward**: if α-decoupling can't be completed in single session, lift D to its own engineering workstream and reschedule the (p,q) test for after

---

## §7 — Skills compliance check (firing schedule)

| Skill | Firing | Rationale |
|---|---|---|
| `ave-prereg` | ✓ (this doc) | Workstream-level prereg before any driver build |
| `substrate-native-check` | At driver design | K4 substrate dynamics only; no SM/QED imports |
| `phase-space-coordinate-check` | CRITICAL | Three coordinate systems must stay separated: (i) Bloch $\mathbf{k}$ on K4 lattice, (ii) $(p,q)$ topological winding labels on Clifford torus, (iii) port-space irrep label (A₁ vs T₂) |
| `consistency-vs-emergence` | At result interpretation | Outcome A would establish $(p,q)$ as Class 2 axiom-manifestation (emerging from K4 substrate geometry); outcome C would falsify the emergence and route back to Class 1 (Path B variational) |
| `ave-canonical-source` | At driver build | Import α, $\tilde\kappa$, $V_{snap}$, $V_{yield}$, $\ell_{node}$ from `src/ave/core/constants.py` and `src/ave/core/cosserat_field_3d.py` — never hardcode |
| `ave-canonical-leaf-pull` | NOT FIRING | No new derivation; test extends existing infrastructure |
| `verify-before-cite` | Continuous | Every file:line cited in §1.3 / §1.4 / §4.3 directly verified via Read or Bash grep before landing in this doc |
| `ave-discrimination-check` | At result framing | Path B-prime alive vs dead is a clean SM-counterfactual-independent discriminator (the test doesn't compare to QED; it tests AVE substrate-internal classification) |
| `ave-evidence-framing-discipline` | At result writeup | "Bands split by $(p,q)$" is a Class 2 emergence claim; framing must distinguish from "we INPUT $(p,q)$ and observed it" tautology (M5 catches this) |
| `ave-discipline-translate` | NOT FIRING | No classical-physics borrowed concepts; pure K4 substrate physics |
| `ave-handoff-canonical-locale` | ✓ | Prereg lands in `research/` not `~/.claude/plans/`; result will land in `research/2026-MM-DD_path-b-prime-k4-dispersion-result.md` |
| `ave-audit` | At driver completion | Auditor pass on driver code (verifying M5 self-check, verifying no hardcoded α leaks) before run |
| `ave-walk-back` | NOT FIRING | Single-test prereg; nothing to walk back |

---

## §8 — Open Q's for Grant adjudication (BEFORE driver build)

**Q-PBP-1** (foundational): Is the claim "K4 transverse modes are $(p,q)$-classified in the LINEAR regime" a physically reasonable position given the K4 lattice's chiral $I4_132$ symmetry? Specifically: does $I4_132$ space group carry the Hopf-fiber bundle structure $S^3 \to S^2$ that would allow $(p,q)$ labels to live on substrate eigenmodes? If yes, the test is meaningful. If you read the chiral $I4_132$ symmetry as NOT carrying this structure, the test's null hypothesis is essentially guaranteed and the prereg should be abandoned without running.

**Q-PBP-2** (methodology): Is using the existing `kappa_tilde_torus(p,q)` infrastructure (which assigns $\tilde\kappa = pq/(p+q)$ per topology) the right way to probe $(p,q)$ band-splitting? Or does the $(p,q)$ label need to live on the WAVE'S geometric structure (curve winding on Clifford torus), not on a per-run modulation parameter? The risk is: by externally feeding $\tilde\kappa(p,q)$ into the simulator, we may be measuring how the simulator responds to a $\tilde\kappa$ input, not how the substrate naturally classifies modes.

**Q-PBP-3** (scope): Is the falsification of Path B-prime (outcome C) a HARD KILL for the Grant-framing intuition, or just a "this specific test doesn't show it" result? I.e., if K4-TLM doesn't show $(p,q)$ band-splitting, does that decisively kill the picture, or might $(p,q)$ structure live elsewhere (full K4-Cosserat coupled engine, full continuum Master Equation, etc.)? Determines how much we lean on this single test.

**Q-PBP-4** (sequencing): Should we run this BEFORE or AFTER addressing the AVE-HOPF crib sheet:25 "K4-TLM simulator has α hardcoded, making verification tautological" finding? The tautology is a known concern; running this test on a tautological simulator wastes the run. The $\tilde\kappa$ refactor (`cosserat_field_3d.py:30-100`) partially addresses it but `k4_tlm.py` may not yet consume the refactored path. Single-session test may need to expand scope to include the k4_tlm.py refactor.

**Q-PBP-5** (commit): If outcome is A or C (decisive), commit to `analysis/path-b-prime-k4-dispersion-pq` branch with audit tag? If outcome is B or D (inconclusive), how do we want to scope the follow-on?

---

## §9 — Honest scope per A47 v18

This test is a **substrate-internal-consistency test** of a Grant-proposed framing. It does NOT test:
- Whether the framing is correct in the limit of full continuum Cosserat dynamics (K4-TLM only)
- Whether photons SI-empirically have $(p,q)$ structure (engineering test, not empirical-physics test)
- Whether the AVE corpus's larger photon-→-electron mechanism is correct (single piece of it)

What it DOES test: whether the AVE-Core K4-TLM engine reproduces $(p,q)$ band-splitting under controlled $\tilde\kappa$ modulation in the linear regime. If yes, Path B-prime has substrate-internal-consistency support and warrants downstream theoretical formalization. If no, Path B-prime is substrate-empirically inconsistent at the K4-TLM level and Path B (Faddeev-Skyrme variational) is the only remaining road.

---

## §10 — Expected total scope (single-session deliverable)

- **Driver build** (extending `test_lattice_layer_1_dispersion.py`): 2-4 hours
- **k4_tlm.py refactor if needed** (Q-PBP-4): +2-3 hours
- **Run** (12 modes × 480 steps × N=64 K4 cube): 10-30 minutes
- **FFT analysis + band classification**: 1 hour
- **Result doc + outcome classification**: 1 hour
- **Auditor pass + commit**: 1 hour

Total: **single session, 5-9 hours of build + run + analysis + commit**

---

## §11 — Result template (to be populated post-run)

```
[STATUS: PRE-RUN — empty until first run lands]

## §11.1 Run configuration
[N, PML, amp, steps, knot enumeration]

## §11.2 PREREG_METRICS evaluation (verbatim)
M1: [PASS / FAIL] — [observed value vs threshold]
M2: [PASS / FAIL] — [observed ordering vs predicted]
M3: [PASS / FAIL] — ...
M4: [PASS / FAIL] — ...
M5: [PASS / FAIL] — ...

## §11.3 Verdict classification
Outcome: [A / B / C / D]
Path B-prime status: [alive / partial / dead / inconclusive]

## §11.4 Honest interpretation per Rule 11
[Decisive call, no post-hoc threshold redefinition]

## §11.5 Forward direction
[Whatever the result indicates — next workstream]
```

---

*Pre-reg written 2026-05-25. Per A47 v11b: this doc + the corresponding driver script will be landed together so any post-hoc rule redefinition is detectable. Per Rule 12: future amendments to this doc preserve body via header-update retraction notation.*
