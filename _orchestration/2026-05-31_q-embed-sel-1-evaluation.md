# Epic: Step (c) — Substrate Derivation of $\Lambda_{\text{surf}} = \pi^2$

**Opened**: 2026-05-31 (orchestration session, Grant).
**Refocused**: 2026-05-31 (Grant directive: *"Let's adjust our epic to focus on the one issue, step C. Let's be exhaustive and pedantic with mapping/planning/skills applied to it."*).
**Branch**: `analysis/q-embed-sel-1-investigation` (off main).
**Draft PR**: [#59](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/59).
**Skill discipline applied at scoping**: `ave-prereg` (corpus-grep across 10 repos via agent `ab2555d4`), `pre-test-physics-check` (Q1+Q2+Q3 plumber questions to Grant in §3 below), `verify-before-cite` v1.4 (all citations grep-confirmed), `phase-space-coordinate-check` (load-bearing), `ave-handoff-canonical-locale` (this locale), `ave-evidence-framing-discipline` (precision on what's proven vs asserted vs ambiguous).

---

## §0 What step (c) actually claims

The framework's $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ derivation has three regime equations. The contested step is regime (c) — the source of the $\pi^2$ in $\Lambda_{\text{surf}}$.

**ch8 verbatim statement** of regime (c):

> **(c) Screening (substrate spinor half-cover)** — **Ax 3 minimum-reflection principle + K4-derived spinor structure**: spin-½ on the substrate emerges from the K4 rotation group chain $T = A_4 \to 2T \subset SU(2) \to SO(3)$; the 2-to-1 cover forces the electron's physically-distinct observable surface to be half of the standard Clifford-torus surface area on $S^3$ → $(2\pi R)(2\pi r) = \pi^2 \Rightarrow R \cdot r = 1/4$

**ch8 verbatim derivation of $\pi^2$**:

> The standard Clifford torus $(z_1, z_2) = (r_1 e^{i\theta_1}, r_2 e^{i\theta_2})$ at $r_1 = r_2 = 1/\sqrt{2}$ on $S^3$ has total surface area $A_{\text{standard}} = 2\pi^2$ (a complex-geometry theorem on $S^3$, framework-external mathematics). The electron's substrate spinor structure forces only half of the Clifford torus to correspond to physically distinct observable amplitudes — the other half is the spinor-conjugate image identified to the first by the substrate's 2-to-1 cover. Therefore $\Lambda_{\text{surf}} = \tfrac{1}{2} A_{\text{standard}} = \pi^2$.

**ch8 four-step chain** for this derivation:

| Step | Claim | Status |
|---|---|---|
| 1 | K4 rotation group $T = A_4$ (order 12) | Derived from Ax 1 substrate topology — canonical leaf `k4-rotation-group.md` (rigorous) |
| 2 | Double cover $2T \subset SU(2)$ | Standard math identity |
| 3 | Spin-½ via Finkelstein-Misner kink mechanism on the extended $0_1$ unknot defect — 4π rotation returns to original state, classical topology of extended objects in SO(3) | Derived — canonical leaf `finkelstein-misner-spin-half-derivation.md` |
| **4** | **$\pi^2$ half-cover area: substrate-distinct observable surface = $\tfrac{1}{2} A_{\text{standard}} = \pi^2$** | **Claimed derived "definitional given step 3"** — the contested step |

## §1 What's pedantically clear

**Solid (substrate-derived)**:

1. **K4 rotation group $T = A_4$.** `k4-rotation-group.md` proves this from K4 tetrahedral port basis $\{p_0, p_1, p_2, p_3\}$ with pairwise dot products $-1$ giving the tetrahedral group of order 12. Action on substrate state is a faithful representation. Rigorous.
2. **$A_4 \to 2T \subset SU(2)$ double cover.** Standard math; binary tetrahedral group $2T$ has order 24, sits in $SU(2)$, exact sequence $1 \to \mathbb{Z}_2 \to 2T \to A_4 \to 1$.
3. **FM kink mechanism on extended unknot (the rotational behavior).** The extended $0_1$ unknot embedded in K4 substrate, under 2π rotation, picks up a topological twist that unwinds only after another 2π (total 4π). This is the Dirac belt-trick — classical topology of extended objects in SO(3) manifolds, no QM postulate. The Cosserat microrotational DOF per K4 node provides the SO(3) substrate geometry; the unknot's continuous geometric extension generates the FM kink. Derived in `finkelstein-misner-spin-half-derivation.md` §2.
4. **The algebra of $(2\pi R)(2\pi r) = \pi^2 \Rightarrow R \cdot r = 1/4$.** This is just stating that a 2-torus parameterized by $(\theta_1, \theta_2) \in [0, 2\pi]^2$ with radial coords $R, r$ has surface area $4\pi^2 R r$, set equal to $\pi^2$.

**Solid (framework-external math, used as identity)**:

5. **The standard Clifford torus on $S^3$ at $r_1 = r_2 = 1/\sqrt{2}$ has surface area $2\pi^2$.** Complex-geometry theorem on $S^3 \subset \mathbb{C}^2$. ch8 cites this as framework-external math.

## §2 What's pedantically ambiguous — the three load-bearing identifications

Three things are claimed but not pedantically anchored. Each one needs either Grant's intuition or substrate-derivation work.

### §2.1 Ambiguity Q1 — What surface is $\Lambda_{\text{surf}}$ the area integral over?

ch8 writes "the substrate-distinct observable surface" — phrase with multiple plausible referents:

| Candidate | What it means physically |
|---|---|
| (a) **Substrate cells the soliton occupies** | 2D Nyquist-resolved spatial cells on the K4 lattice; surface integral counts cells crossed by the extended unknot's flux-tube envelope. Real-space picture. |
| (b) **Complex-geometry Clifford torus** | The abstract 2-torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ — surface integral on this complex manifold. Mathematical-coordinates picture. |
| (c) **$(V_\text{inc}, V_\text{ref})$ phasor swept area** | The 2D phase-space area the bond's phasor traces over a period. Phase-space picture per doc 28. |
| (d) **Cosserat-rotation manifold** | The 2-surface in micropolar-rotation-state space the soliton accesses. Substrate-rotation picture. |
| (e) **Something else** | Different substrate-mechanism the agent hasn't identified. |

**The answer pins down**: what the "half-cover" actually halves, what coordinate system the framework's $R, r$ live in, and which derivation path (§4 below) is the right target.

**Cannot resolve from corpus alone** — ch8 uses the phrase "substrate-distinct observable surface" without unambiguous physical referent. Doc 28 §5.4 has the explicit open question about the real-space-to-phase-space relationship; doc 29 F5 flags the spatial reading as importing standard spinor-T² algebra. Grant's intuition needed.

### §2.2 Ambiguity Q2 — How does the FM rotational double-cover translate to a surface-area halving?

The FM mechanism (per `finkelstein-misner-spin-half-derivation.md` §2.2) is a **rotational** topological property of the extended unknot: under 2π rotation in 3D, the loop's embedding twists relative to environment; under 4π, the twist unwinds. That's a property of HOW THE LOOP ROTATES.

The half-cover claim in ch8 is about a **surface area**: the substrate-distinct observable surface = $\tfrac{1}{2} A_{\text{standard}}$.

These are not obviously the same statement. Plausible bridges:

| Bridge | Claim |
|---|---|
| (a) **Direct rotational-to-spatial identification** | The surface integrated over the soliton's full rotational period traverses 4π in observable space, but the substrate-distinct observable only counts 2π of that (since states differing by 2π rotation are identified via the FM mechanism). Halving rotational integration range → halving surface area. |
| (b) **Spatial-region identification** | The Clifford torus has two physically-distinct "halves" identified by the FM kink (one is the substrate-distinct observable; the other is its spinor-conjugate image, physically equivalent under the FM identification). Halving is a spatial-region identification, not a rotational-range one. |
| (c) **Spectral / mode-count identification** | The full Clifford torus carries two substrate modes; the FM kink identifies them as one observable; mode count goes from 2 to 1 → effective area halves. |
| (d) **Something else** | Identifying-step the agent hasn't identified. |

**Cannot resolve from corpus alone** — ch8 step 4 says only "definitional given step 3 substrate-spinor identification of the two cover sheets." Which "two cover sheets" — rotational halves of the period, spatial halves of the torus, or substrate modes — isn't pinned. FM leaf §2.2 describes the rotational behavior but doesn't explicitly identify surface halves.

### §2.3 Ambiguity Q3 — Is $R \cdot r = 1/4$ the input or the output?

There's a subtle circularity in the published ch8 derivation:

- **As ch8 writes it**: Standard Clifford torus has $A = 2\pi^2$. Half-cover halves it. Therefore $\Lambda_{\text{surf}} = \pi^2$. Set $(2\pi R)(2\pi r) = \pi^2$. Solve $R \cdot r = 1/4$. → $R \cdot r$ is the **output**.
- **Geometric alternative**: For the Golden Torus mapped to Clifford coords $(r_1, r_2)$, doc 38 §3 finds $r_1 r_2 = 1/4$. Surface area on $S^3$ for such an embedding is $4\pi^2 \cdot r_1 r_2 = \pi^2$ — without invoking any half-cover. → $\pi^2$ surface area is the **consequence of** $r_1 r_2 = 1/4$ (which is by assumption).

**The two readings give the same $\pi^2$ value but different load-bearing structure**. Reading 1 has half-cover as the substrate-mechanism that derives the value; Reading 2 has the value emerging from whatever fixes $r_1 r_2 = 1/4$ (which is back to embedding-selection).

**Cannot resolve from corpus alone** — ch8 frames Reading 1. But doc 38 §3 algebraically demonstrates Reading 2 is consistent with the geometry. The two readings need disambiguating before we know which mechanism we're substrate-deriving.

## §3 Plumber-physical questions for Grant (per `pre-test-physics-check`)

Before locking the epic's investigation paths, three plumber questions need calling. Per the skill: one sentence each, expects one-paragraph answer, asks about substrate / framing.

**Q1**: When ch8 step 4 says *"the substrate-distinct observable surface is half of $A_{\text{standard}} = 2\pi^2$"*, what physical surface is the integral over — substrate cells the soliton occupies (real-space), the complex-geometry Clifford torus on $S^3$ (mathematical-coordinates), the $(V_\text{inc}, V_\text{ref})$ phasor's swept area (phase-space), the Cosserat-rotation manifold (substrate-rotation), or something else? **(§2.1)**

**Q2**: The FM kink mechanism gives the extended unknot a $4\pi$ rotational double-cover — that's about how the loop rotates relative to environment. How does that rotational property translate into halving a surface-area integral: by direct rotational-to-spatial identification (period 4π → half-period counts), by spatial-region identification (one half of the torus is the spinor-conjugate image of the other), by spectral/mode-count identification, or something else? **(§2.2)**

**Q3**: When ch8 writes the equation $(2\pi R)(2\pi r) = \pi^2$ and concludes $R \cdot r = 1/4$, is the $\pi^2$ on the LHS *derived from* the half-cover argument and $R \cdot r = 1/4$ is the *consequence* (ch8 framing), OR is $R \cdot r = 1/4$ *assumed/given by embedding-selection* and the $\pi^2$ surface area is just the *natural Clifford-coord product of that embedding* (geometric alternative per doc 38 §3)? **(§2.3)**

These pin down which §4 path is the right substrate-derivation target.

## §4 Six paths to derive $\Lambda_{\text{surf}} = \pi^2$ from substrate primitives

Each path is contingent on a different answer to Q1/Q2/Q3. I'll keep all six on the board until Grant calls.

### §4.A — Phase-space empirical (Path α v(latest+1)-phasor)

**Fires if Q1 = (c) phasor-swept-area**.

Re-run the (V_inc, V_ref) phasor extraction from doc 28's two-node test, with 4 A59 methodology fixes (persistence pre-characterization, Hilbert-transform chirality, per-cluster bipolar R/r adjudication, sampling strategy). Adjudicate whether $R/r = \varphi^2$ in dominant cluster. If pass: phase-space framing gets empirical support; $\Lambda_{\text{surf}} = \pi^2$ is the phasor's natural swept area at the (2,3) eigenmode.

**State**: existing v1 driver `r9_canonical_phase_space_phasor.py` + A59 fixes documented in doc 78 §7. v1 ran 2026-04-27, FAILED with caveats.

**Time estimate**: 1-2 sessions to build + run.

### §4.B — Analytical: substrate-primitive surface integral

**Fires if Q1 = (a) substrate cells OR (d) Cosserat-rotation manifold**.

Derive $\pi^2$ as a substrate-mechanical surface integral over whatever Q1 identifies — Nyquist-resolved spatial cells crossed by the extended unknot's flux tube, OR the Cosserat-rotation manifold the soliton's micropolar DOF accesses. From K4 lattice primitives + Cosserat field + Op operators only (no standard spinor-T² algebra).

**State**: doc 28 §5.4 explicit open question; not attempted analytically.

**Time estimate**: open. 1-N sessions depending on how cleanly substrate primitives produce $\pi^2$.

### §4.C — Discrete-lattice FM kink simulation

**Fires for any Q1 answer; especially valuable if Q1 = (a)**.

Build the extended-defect simulation on K4-TLM that the FM leaf line 167 explicitly says doesn't exist: *"Does NOT provide a discrete-lattice computation of the FM kink on K4 — would require full extended-defect simulation, not currently in the K4-TLM or Master Equation FDTD engines."* Once built, compute the half-cover surface integral directly from the discrete lattice. Closes the FM mechanism + the surface area at full discrete-lattice rigor.

**State**: infrastructure does not exist. Significant build.

**Time estimate**: large (≥ 3-5 sessions of engine work, possibly more).

### §4.D — Real-to-phase-space transformation derivation

**Fires for any Q1 answer; settles Q1 (c) vs other**.

Doc 28 §5.4 explicit verbatim open question: *"What's the precise relationship between real-space $R_\text{real} \approx 2.27$ and phase-space $R_\text{phase} = \varphi/2 = 0.809$? Is there a transformation? Does the phase-space Golden Torus correspond to a SCALED-DOWN version of the real-space envelope?"* If a clean substrate transformation exists, the framework has a coherent dual-picture; if not, one reading is the wrong description.

**State**: not attempted; sits as an open analytical question in archive.

**Time estimate**: 1-2 sessions of analytical work.

### §4.E — Alternative substrate mechanism for $\pi^2$

**Fires if Q2 indicates the half-cover isn't the right mechanism**.

Replace the FM-half-cover identification with a different substrate process that produces $\pi^2$ — candidates: Cosserat-rotation-sector boundary integral (the $\pi^2$ as integral over the rotation manifold), saturation-boundary cross-section (the $\pi^2$ as the soliton's boundary geometry at $\Gamma = -1$), SU(2) action on substrate state vector (the $\pi^2$ as group-theoretic invariant). Doc 39 implicitly suggests this when arguing the FM half-cover is the SU(2) projective-ray postulate.

**State**: open analytical question. Multiple candidate mechanisms; no canonical attempt.

**Time estimate**: open. Initial scoping ~1 session per candidate mechanism.

### §4.F — Cross-particle consistency (muon, proton, baryons)

**Fires independently — falsification check for any Q1 answer**.

Does the same regime (c) derivation work for muon ($e^- + $ Cosserat torsion quantum), proton ($(p,q) = (3,5)$ trefoil), Δ baryon ($(p,q) = (3,7)$), etc.? If the half-cover argument is electron-specific, the framework has an electron-postulate. If the same algebra works across spin-½ particles with their respective (p,q) windings, that's strong evidence the substrate-mechanism is real (whatever the analytical-derivation status of regime (c)).

**State**: corpus has separate Λ derivations for each particle in Vol 2; cross-check hasn't been done as a discipline pass.

**Time estimate**: 1-2 sessions of corpus analysis.

## §5 Skill matrix (path-by-path, full suite)

| Skill | §4.A | §4.B | §4.C | §4.D | §4.E | §4.F |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `ave-prereg` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `pre-test-physics-check` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `phase-space-coordinate-check` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-canonical-source` | ✅ | — | ✅ | — | — | — |
| `ave-driver-script-honesty` | ✅ | — | ✅ | — | — | — |
| `ave-canonical-leaf-pull` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-discipline-translate` | — | ✅ | — | ✅ | ✅ | ✅ |
| `ave-ee-first-mapping` | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `substrate-native-check` | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `consistency-vs-emergence` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-discrimination-check` | ✅ | — | — | — | — | ✅ |
| `ave-fundamental-ground-up-implementation` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-analytical-tool-selection` | ✅ Time-domain+Mode | ✅ Boundary+Mode | ✅ Numerical | ✅ Coupling | ✅ Mode+Boundary | — |
| `ave-power-category-check` | — | — | — | — | ✅ | — |
| `ave-independence-check` | ✅ per-cluster | — | — | — | ✅ candidate mechanisms | ✅ per-particle |
| `ave-multi-falsifier-triangulation-discipline` | ✅ C1+C2+persistence | ✅ multiple regimes | ✅ multi-observable | ✅ multi-route | ✅ multi-mechanism | ✅ multi-particle |
| `ave-cavity-class-identification` | — | — | ✅ | — | ✅ | — |
| `ave-worktree-paths` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-audit` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-audit-of-audit` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `verify-before-cite` v1.4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-evidence-framing-discipline` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-directory-enumeration-discipline` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-walk-back` | ⚠️ if reframes claim | ⚠️ if reframes claim | ⚠️ if reframes claim | ⚠️ if reframes claim | ⚠️ if reframes claim | ⚠️ if reframes claim |
| `ave-newly-created-skill-self-audit` | ⚠️ if new skill | ⚠️ if new skill | ⚠️ if new skill | ⚠️ if new skill | ⚠️ if new skill | ⚠️ if new skill |
| `ave-sweep-audit` | — | — | — | — | — | ⚠️ if N>10 particles |
| `ave-handoff-canonical-locale` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-ip-divide-discipline` | — | — | — | — | — | — |

Routing per memory v2 (`feedback_branch_discipline_colleagues`): every phase that lands commits goes via PR.

## §6 Sequencing (PENDING Q1/Q2/Q3)

```
[Grant Q1/Q2/Q3 plumber-call] ← LOAD-BEARING (gates everything else)
        ↓
   ─────┴───────┬─────────────┬─────────────┐
   ↓            ↓             ↓             ↓
[§4.A          [§4.B          [§4.C          [§4.D
 phasor]        analytical]    sim]           transform]
   ↓            ↓             ↓             ↓
   └──────┬────────────────────────┘
          ↓
[Joint synthesis: which path closed (c) substrate-derivation?]
          ↓
[Optional §4.E alternative mechanism if A/B/C/D all open]
          ↓
[Optional §4.F cross-particle consistency check]
          ↓
[(c) substrate-derivation status declared]
```

Phases are mostly parallelizable once Q1/Q2/Q3 are called. §4.A and §4.D can run independently; §4.B and §4.E are analytical-track; §4.C is engine-build; §4.F is cross-corpus.

## §7 Cross-references

- **Walkback epic** (parent, paused awaiting evaluation): [`_orchestration/2026-05-28_parameter-count-framing-walkback.md`](2026-05-28_parameter-count-framing-walkback.md) §Phase 3
- **Routing-convention retrospective**: [issue #58](https://github.com/ave-veritas-et-enodatio/AVE-Core/issues/58)
- **This epic's draft PR**: [#59](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/59)

### Canonical KB leaves
- [`manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) (three-regime canonical anchor; step-4 contested step)
- [`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) (K4 → A4 substrate derivation — solid)
- [`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) (FM mechanism, §2.2 rotational behavior, §5 K4-native-vs-imported decomposition, line 167 missing-discrete-lattice-computation note)
- [`manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-half-paradox.md`](../manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-half-paradox.md) (spin-½ from extended-defect topology, no QM postulate)
- [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) (Theorem 3.1 §Op21 mode-counting)
- [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) (Op21 PARTIAL closure; embedding remains canonical INPUT)

### Canonical research/archive docs
- [`research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md`](../research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md) §5.4 (open question: real-to-phase-space relationship)
- [`research/_archive/L3_electron_soliton/29_ch8_audit.md`](../research/_archive/L3_electron_soliton/29_ch8_audit.md) F4-F9 (ch8 structural audit), §2.4 (spatial reading falsified; phase-space surviving)
- [`research/_archive/L3_electron_soliton/36_pathB_trefoil_z2_investigation.md`](../research/_archive/L3_electron_soliton/36_pathB_trefoil_z2_investigation.md) §3.1 (original symmetric-Clifford hypothesis)
- [`research/_archive/L3_electron_soliton/38_ropelength_minimality.md`](../research/_archive/L3_electron_soliton/38_ropelength_minimality.md) §2-§3 (numerical refutation of spatial-ropelength-minimality; Golden Torus in Clifford coords (0.966, 0.258))
- [`research/_archive/L3_electron_soliton/39_alpha_is_calibration.md`](../research/_archive/L3_electron_soliton/39_alpha_is_calibration.md) (calibration-input dissent; SU(2) projective-ray postulate critique)
- [`research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md`](../research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md) §7 (Path α v1 result + A59 4 methodology fixes verbatim)
- [`research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md:3713`](../research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md) (Grant 2026-04-27 adjudication: R, r as phase-space)

### Existing infrastructure (extends, doesn't rebuild)
- `src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py` (v1 driver) + results JSON
- `src/scripts/vol_1_foundations/r9_path_alpha_bond_pair_phasor.py`, `phasor_discovery.py`, `phasor_trajectory_test.py`
- `src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py`, `tlm_electron_soliton_eigenmode.py`, `k4tlm_dispersion_analytical.py`
- `src/scripts/vol_1_foundations/ropelength_trefoil_golden_torus.py` (existing ropelength composite; STAGE B imposes R·r=1/4, doesn't derive it)
- `src/scripts/vol_1_foundations/verify_clifford_half_cover.py` (5-step half-cover derivation — needs re-audit against Q1/Q2/Q3 answers)

### Cross-repo
- [`AVE-HOPF/docs/glossary.md:32`](../../AVE-HOPF/docs/glossary.md) — Grant 2026-04-30 bracketing of Golden Torus as "post-IP-separation patch-attempt"

## §8 Status

- [x] **Epic scoping refocused on step (c)** (2026-05-31) — three ambiguities Q1/Q2/Q3 + six paths §4.A-§4.F + skill matrix
- [ ] **Grant Q1/Q2/Q3 plumber adjudication** — load-bearing for path selection
- [ ] **§4.A phase-space empirical** (gated on Q1 = c or D path-§4.D positive)
- [ ] **§4.B analytical substrate-primitive surface integral** (gated on Q1 = a/d)
- [ ] **§4.C discrete-lattice FM kink simulation** (open; large infrastructure build)
- [ ] **§4.D real-to-phase-space transformation derivation** (open, independent)
- [ ] **§4.E alternative substrate mechanism for $\pi^2$** (gated on Q2 indicating half-cover not the mechanism)
- [ ] **§4.F cross-particle consistency check** (independent, falsification-counterpart)
- [ ] **(c) substrate-derivation status declared** — gated on which §4 paths close
- [ ] **Resolves walkback §3.3 framing choice** — gated on the above
- [ ] **AVE-HOPF cross-repo reconciliation** — gated on resolution
