# PREREG — FROZEN — Reciprocal-loading pulse reflection Γ(A) on the 2-component transverse vector-TLM carrier (static-existence Stage 1 / epic P1)

**Status:** FROZEN at commit. No run has been executed and no driver code existed when
this document was authored; no measured number from THIS test appears here. This
prereg is never edited after its freeze commit — every departure is a dated DEVIATION
entry in the result doc.
**Authoring arrangement (declared delta from the Class-C template):** the Class-C
prereg (`research/2026-08-24_engine-gamma-meanstest_prereg_FROZEN.md`) was written by
a prereg-author agent firewalled from a run executed by a separate run agent. This
lane is a single-implementer build session (the Stage-1 satellite of the
static-existence build brief), so the firewall here is CAUSAL, not organizational:
the prereg is committed before the first line of driver code is written, and the
freeze commit hash is the receipt. **Provenance of the expectations, stated
honestly:** the T-ELEC expectations (§6) are derived from canon receipts + lumped
algebra only; the apparatus parameters (E1/E2/E4/E5/E6) are adopted verbatim from
the merged Class-C run's MEASURED receipts, cited per row; and the T-MAG expectation
is NOT blind — T-MAG is mathematically a replay of the merged Class-C G-J
measurement (§2.4) and is frozen here as a REPRODUCTION gate, not a prediction.
**Pre-freeze adversarial check (disclosed):** a 3-lens adversarial review
(citation-verification / gate-fireability / physics-and-sector) ran on the DRAFT of
this document before freeze; its confirmed findings were repaired in the draft. No
run existed at any point of that loop.
**Date frozen:** 2026-08-24
**Spec (Grant-launched):** `_orchestration/2026-08-24_static-existence-build-brief.md`
Stage 1, verbatim: *"Build the transverse per-directed-bond graded scatter (the named
extension — no T2 grading hook exists in-tree; `vacuum_varactor_scatter`'s per-bond
form + cancellation gate is the template to generalize), port the pulse/probe
pipeline, and measure the transverse Γ(A) locus"* … *"Run BOTH loadings as separate
declared configurations; the prereg freezes each config's expectations separately."*
Epic P1 (`_orchestration/2026-08-24_static-existence-epic.md` §3): *"The P1 prereg
must declare WHICH constitutive parameter the frozen transverse grading loads"* —
discharged in §2.2/§2.5 with the machinery's actual reach declared (impedance-ratio
projection only).
**Result lands as:** its own research pair (`..._result.md`) via one reviewed PR
opened `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`, with the ≥3-lens adversarial
verify downstream of the run and the repairs-need-reaudit loop run to convergence
before the lane presents anything. Only Grant merges.

---

## §0 — SECTOR / REGIME / MODE DECLARATION (house table)

| Axis | Declaration |
|---|---|
| **MODE** | Numerical measurement: impose-and-probe scattering. A passive linearly-polarized pulse is launched in a closed lattice and its reflection off an IMPOSED, STATIC, kernel-shaped per-bond grading is measured. Reflection-coefficient (Op3) observable, read in (V_inc, V_ref) TLM port coordinates on the launch polarization component (§4.4). |
| **SECTOR** | The 2-component transverse vector-TLM container on the D1-ratified `srs-z3` carrier (`chiral_lattice_vector.vector_tlm_step`, `src/ave/core/chiral_lattice_vector.py:35-62`; net `build_srs_net`, `src/ave/core/chiral_lattice.py:206`). **Honest carrier-gap declaration** (`engine-capability-map.md:54`): `carried_dof==2` (transverse polarization pair) vs `axiom_dof==6` — NOT the full Cosserat micro-rotation. The def-0pt1ac object (optical-activity/gyrotropy) is the per-node polarization-plane TWIST, which is OFF in this run (E8); the 2-component space itself is just the polarization pair. No winding, charge, or spin content anywhere in this run. **Honest channel declaration (§2.4):** with the twist off and a component-scalar loading, the container's dynamics are two decoupled copies of the scalar TLM — no observable in this run distinguishes "transverse" from "scalar" at the Γ-locus level; the transverse content of the deliverable is the MACHINERY (the graded vector scatter + its structure gates), not a channel-distinct locus. |
| **ENGINE-DOF receipt** | The engine carries the DOF under test: `vector_tlm_step` propagates 2 transverse components per directed port on the srs net; the ground-up L0–L2 acceptance suite runs on this grid and is GREEN (lossless transverse propagation, dispersionless band, transversality, causality — `engine-capability-map.md:54`), with that line's own rider carried: *"The suite forces ZERO chords"* — medium-validity is a different axis than chord-DOF coverage. The P0 capability report (`_orchestration/2026-08-24_static-existence-p0-capability-report.md` V1) confirms no graded junction-scatter primitive exists for this channel — the graded scatter is the NEW build item (§4.1). |
| **REGIME** | LINEAR probe on a statically graded medium. The scatter matrices depend on the imposed grading field A(x) and NOT on the propagating field V — dynamics are amplitude-independent by construction. Op14 dynamic saturation OFF (`chiral_lattice_vector_sat` NOT used — its z_local is self-consistent/amplitude-dependent, the opposite of a frozen grading). Optical activity OFF (achiral measurement, E8). **Fixed-delay declaration (load-bearing):** CONNECT is the fixed-delay permutation — one step per bond transit regardless of Y — so the graded region's refractive index is UNGRADED (μ_eff·ε_eff = const is forced by the machinery). The grading is an IMPEDANCE-RATIO grading only (§2.5). The Axiom-4 kernel S(A)=√(1−A²) enters ONLY through the two imposed impedance maps (§4.2). |
| **PHASE-STATE** | Cold lattice everywhere except the FROZEN-IMPOSED grading region, A ∈ [0, 0.99]. The grading is imposed-and-probed: never self-consistent, never pumped, never evolving. Closed system, no drive after t=0, no loss terms. |
| **CLASS** | Response-map measurement + machinery validation: (i) the Γ(A) locus under the ELECTRIC-FIRST impedance loading z=1/√S — **never measured before, on any channel** — and (ii) a REPRODUCTION gate: the MAGNETIC-FIRST loading z=√S replays the merged Class-C G-J measurement on the new 2-component machinery and must reproduce its banked locus. Adjudicates whether the two reciprocal loadings draw opposite boundary phases at response-map level. Nothing minted; no canonical leaf edited by the run. |

**consistency-vs-emergence tag:** a **consistency/response-map** measurement of the
engine's linear scattering off imposed gradings, compared against lumped forms, plus
an **implementation-verification** reproduction gate. NOT an emergence test, NOT a
bound-state test, NOT a CODATA fit, NOT a chord claim (epic §8; and the
capability-map rider above).

## §0.5 — Epic §5 guard discharge (by name, per the epic's header requirement)

| guard | binds P1? | discharged at |
|---|---|---|
| 1 — existence-not-emergence carve | P2-scoped (nothing is imposed as a finished texture here), but its forbidden-conclusions clause travels | §1 |
| 2 — challenge-canonical-negative config-grep | YES | §3 |
| 3 — phase-space-coordinate-check / transduction hazard | YES | §4.4 coordinate map |
| 4 — structural-null stencil lens (cancellation trap) | YES | §4.0 + the module gates T1(a)/T1(b) + the run gate CS-6b (VOID-linked, §8 V1) |
| 5 — sector-ownership A1 ⊥ T2 | YES | §0 SECTOR + §2.3 (the flagged two-reading split; no sector-ownership claim is made or adjudicated) |
| 6 — R40-B2a stamp adjacency | YES | §4.1 (both stamps: `vacuum_varactor_scatter.py:72` AND `srs-vertex-scattering.md:24`) |
| 7 — regime/phase-state declaration | YES | §0 house table |
| 8 — α-agnostic imposition | P2-scoped (no winding is imposed here; no tube phase exists in this run) | recorded as not-applicable |

## §1 — BINDING SCOPE (forbidden conclusion-shapes)

The following conclusion-shapes are FORBIDDEN in the result doc regardless of what
the run shows:

- "therefore a bound state / electron can (or cannot) form" — out of scope by construction;
- "therefore the energize-LOCK negative is explained away / reopened" (§3.1);
- "therefore an eigenmode exists / does not exist" (that is P2's question, behind G2);
- any charge-sector, winding, spin, or chirality statement (§0 SECTOR; achiral by construction);
- any adjudication of WHICH branch "the electron uses" — the branch fork is the RULED
  sign/spin selector (#260 B3-DEGENERATE; the `master-equation.md:106` banner,
  quoted with its parenthetical intact: *"the magnetic-vs-electric fork is DEGENERATE
  on the equilibrium observables ($Z=Z_0\sqrt{S}$, $|\Gamma|=1$ both ways) and the
  asymmetry is chirality-set, not substrate-forced"*. Flag, not fixed here: that
  parenthetical's $Z=Z_0\sqrt{S}$-both-ways reading is in tension with the two
  reciprocal Z conventions the same banner's body implies and
  `universal_operators.py:788-800` pins — the fork is degenerate in |Γ|, not in Z.
  The result doc must not silently inherit either reading);
- any adjudication of the SECTOR-OWNERSHIP question flagged in §2.3 (which channel
  canon assigns the Γ=−1 short to) — this run measures declared impedance maps and
  cannot settle it;
- any claim that a measured locus is TRANSVERSE-DISTINCT (vs the scalar channel) —
  structurally impossible in this design (§2.4);
- any claim that the transverse VERTEX behavior is now verified — CT-1 is an
  implementation identity, not a vertex measurement (§2.6).

The ONLY claims the run may produce: (i) the measured Γ(A) locus per loading,
(ii) the frozen classification of each locus (§6), (iii) the per-loading and
pair verdicts strictly via §6.3/§6.4, (iv) the recorded non-adjudicating
diagnostics (MIRROR, FLOOR, shape labels, δ-level sign profile, CT-1,
window-convergence receipts) as reported numbers.

## §2 — What is being measured, and the comparison targets

### §2.1 — The branch carve (receipts, corrected line numbers)

Canon's Axiom-4 saturation carve on the wave channel
(`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`):

- `:105` — electric-only saturation: *"only ε_eff → 0 while μ_eff remains intact,
  drives Z = √(μ₀/ε_eff) → ∞ — the medium becomes electromagnetically opaque
  (evanescent, no energy transport). This is the dielectric-rupture branch"*;
- `:107` (clm-lv3uw1, under the `:106` sign-selector banner) — the magnetic branch:
  *"the field B saturates μ_eff first, driving Z = √(μ_eff/ε₀) → 0 and Γ → −1
  (short-circuit)"*;
- `:114` — *"Both branches are governed by the same kernel S(A) = √(1−(A/A_yield)²);
  they differ in which constitutive parameter saturates first."*
  (`envelope-anatomy.md:94` attributes this third sentence to ":103-112", two
  lines short — a cite slip flagged for a downstream cite-repair, not fixed here.
  The epic's own ":103-112" pointer is attached to the branch PAIR at :105/:107,
  which is inside the range and correct.)

The kernel-to-parameter assignments (ε_eff = ε₀S, μ_eff = μ₀S, C_eff = C₀/S) are
pinned at `manuscript/ave-kb/CLAUDE.md:73-75`; the two reciprocal impedance
conventions are pinned in-tree at
`src/ave/core/universal_operators.py:788-800` (load="electric": Z₀/√S → ∞, Γ=+1;
load="magnetic": Z₀·√S → 0, Γ=−1; the sign-lock w35sn2bq3).

### §2.2 — The two loadings (declared impedance maps; continuum motivation only)

| loading (config) | continuum motivation | normalized bond impedance z_b(A) | bond admittance Y_b(A) | two-port lumped form (z−1)/(z+1) | isolated-vertex form (this geometry, §2.5) |
|---|---|---|---|---|---|
| **T-MAG** | magnetic-first direction (μ_eff saturates, `master-equation.md:107`) | z = √S | Y₀/√S | Γ = (√S−1)/(√S+1): 0 → −1 | Γ_J = (√S/2−1)/(√S/2+1): −1/3 → −1 (the MAG-VERTEX form — algebraically ave_chart's Form-J curve, `ave_chart.py:126-150`) |
| **T-ELEC** | electric-first direction (ε_eff saturates, `master-equation.md:105`) | z = 1/√S | Y₀·√S | Γ = (1−√S)/(1+√S): 0 → +1 | Γ_B = (1/2−√S)/(1/2+√S): −1/3 → +1, with ONE −→+ crossing at √S = 1/2, i.e. **A\* = √15/4 ≈ 0.96825** (`A_MATCHED_B`, `ave_chart.py:79`) (the ELEC-VERTEX form — algebraically ave_chart's Form-B curve) |

The "continuum motivation" column is a DIRECTION label, not what the machinery
imposes (§2.5). The two two-port forms are exact mirrors (Γ_elec ≡ −Γ_mag); the two
VERTEX forms are NOT mirrors — both start at the bare-vertex −1/3 (the two vertex forms
share their A=0 intercept), which is the actual mechanism behind any measured MIRROR
defect (§6.2), not "multiple scattering inside the slab": with a constant A over the
slab, every interior slab node has all three ports at equal Y and its scatter
collapses to the bedrock EXACTLY (the §4.0 cancellation), so the entire response
comes from the mixed-admittance boundary node layers.

**LABEL NOTE (collision fence):** ave_chart's Form J / Form B model the SCALAR
J/B SIDE-ASSIGNMENT fork — junction-side vs bond-side bias, where the Class-C G-B
config was a *crossing-bond* geometry. Here BOTH vertex forms arise from the SAME
far-side geometry under the two loadings; only the ALGEBRA coincides with those
curves. The Class-C G-B INVALID-EXTRACTION verdict concerns that other
construction and is untouched by anything here.

**μ-side fork flag (travels with any reuse; verbatim,
`manuscript/ave-kb/common/saturation-rim-inversion.md:70`):** *"The vacuum μ-grade
keys on **circulation** A_I, not on swing: μ_eff = μ₀/√(1−A_I²) … (the INCREASING
relativistic inductor …). **What A_I actually does AT the knot core is not pinned by
canon** … A **second, unreconciled** corpus reading exists: the wall-fork magnetic
route has μ_eff → 0 (Meissner onset …) — a **decreasing** μ, opposite to the
increasing relativistic inductor … This μ-at-core reconciliation is the **one open
detail** of this claim; graded accordingly and routed for adjudication."* The T-MAG
map's swing-keyed decreasing-μ label is therefore ONE HORN of a routed-open corpus
fork; this run does NOT adjudicate it, and the map functions here purely as the
declared reciprocal of the T-ELEC map (E9).

### §2.3 — The sector question (flagged, NOT adjudicated — epic guard 5)

Canon carries TWO readings of where the Γ=−1 short lives, and this prereg does not
resolve them:

- **The Grant-ratified INVARIANT-S2 sector split** (`resonant-lc-solitons.md:41`;
  restated `saturation-rim-inversion.md:65-68`): the Z→0 short is the
  **longitudinal-A1 bond compliance** (C₀/S), the Z→∞ open is the **transverse-T2
  permittivity** (ε₀S) — *"Orthogonal reactances, both |Γ|=1, differing only in
  boundary phase"* is a split BETWEEN sectors. Under this reading the transverse
  channel's own saturation branch is the OPEN one.
- **The master-equation in-channel branch fork** (`:105`/`:107` under the `:106`
  banner): both ε-first (open) and μ-first (short) live on the wave channel as the
  ruled spin/sign selector (#260 B3-DEGENERATE).

The epic's P0 CORRECTION (merged, `_orchestration/2026-08-24_static-existence-epic.md`
§3 P1) states canon holds BOTH branches with opposite boundary phase and requires
the prereg to declare WHICH constitutive parameter the grading loads (discharged
§2.2/§2.5); the RUN-BOTH-as-separate-declared-configurations order is the build
brief's (Stage 1, quoted verbatim in the header) — this prereg executes that
merged spec. To keep guard 5
clean, T-MAG is framed throughout as a DECLARED IMPEDANCE MAP (the reciprocal
control + reproduction gate), never as "the transverse magnetic branch": no result
sentence may assign the measured Γ→−1 locus to a sector. The two-reading split is
surfaced here per flag-don't-fix and travels to the result doc verbatim.

### §2.4 — The T-MAG replay identity (stated plainly; the reproduction gate)

With optical activity OFF, a component-scalar loading, and the launch polarized in
component 0, the vector step is S_u ⊗ I₂ + permutation ⊗ I₂: component 1 is
identically zero and component 0 obeys EXACTLY the scalar TLM equations. T-MAG
additionally adopts the Class-C G-J run's net, geometry, grading rule, A-grid,
launch, and estimator verbatim (E1–E6) with the same map z=√S. Therefore
**Γ_TMAG(A) equals the merged Class-C G-J locus to numerical roundoff, and its §6
classification is known before the run** (the banked record:
`research/2026-08-24_engine-gamma-meanstest_result.md` §8 — monotone deepening
negative, no crossing, no measurable floor, quantitatively the two-port core locus
to ~1 %, window-converged). T-MAG is accordingly frozen as a **REPRODUCTION gate**
(R-1/R-2/R-3, §5) validating the NEW graded 2-component machinery against a banked
measurement (the `ave-reproduction-gate` discipline) — agreement is a machinery
receipt, NEVER evidence about the transverse channel and NEVER an independent
confirmation of the locus. **All of this run's new physics content lives in
T-ELEC** (z = 1/√S has never been run on any channel) and in the cross-loading
MIRROR diagnostic. A genuinely transverse-DISTINCT measurement would need optical
activity ON or a non-component-scalar loading — both deliberately fenced out here
(§4.0 T2/T3); this run does not claim one.

### §2.5 — What the machinery can and cannot impose (epic P1's "which parameter" ask)

A per-bond admittance grading with CONNECT an untouched fixed-delay permutation
changes L/C at fixed LC: it grades the impedance ratio z(A) at CONSTANT propagation
speed. Both constitutive statements of §2.1 imply c_slab = c₀/√S as well — NOT
realized here (that would be a CONNECT-side delay/Op3 change, a different declared
config). The run therefore adjudicates the **boundary-phase (impedance-sign)
content** of the carve only; it cannot distinguish which parameter saturates, and
"the medium becomes electromagnetically opaque" (`:105`) is structurally unreachable.
This is the same limitation the Class-C scalar run had; it is declared here rather
than discovered later. (§6.5 carries it as a non-adjudicator.)

### §2.6 — The transverse vertex (honesty)

The −1/3 bare-vertex floor is a counting fact, Γ=(2−z)/z at z=3
(`srs-vertex-scattering.md:13`), whose leaf is scoped *"scalar / compression
channel"* with vector/torsion channels scoped out — and that sector-header line
carries an inline 🔴 R40-B2a DEMOTED stamp (`srs-vertex-scattering.md:24`), which
travels here per guard 6. CT-1 (§5) verifies the implemented vector scatter applies
the bedrock 3-port matrix per component — an IMPLEMENTATION IDENTITY (the formula
S_ij = 2Y_j/ΣY − δ_ij at equal Y is (2/3)J − I algebraically). It does NOT
discharge the epic's "transverse vertex behavior is unverified" item, because the
counting fact has no channel content and this machinery gives it none by
construction. That item remains OPEN after this run.

**DECLARED DEPARTURE from one build-brief sentence**
(`_orchestration/2026-08-24_static-existence-build-brief.md`: *"The transverse
vertex behavior (the −1/3 counting fact is scalar-scoped) is measured for free in
the cold gate"*): CT-1 is an implementation identity and does not MEASURE
transverse vertex behavior; the epic's own *"the transverse vertex behavior is
unverified on either branch"* (epic §3 P1) is the reading adopted here. Surfaced
for the orchestrator with this freeze.

### §2.7 — Expected loci (frozen, per loading)

- **T-MAG:** the banked Class-C G-J locus, reproduced (R-2 bound, §5). Shape class:
  monotone deepening negative, no crossing (core/J-class — the two forms are the
  same qualitative class on this geometry).
- **T-ELEC (the new measurement):** TWO canon-compatible candidate shapes, both
  drawing the OPEN boundary phase (SIGN_top = +):
  - **ELEC-CORE (homogenized mirror):** monotone increasing positive locus tracking
    (1−√S)/(1+√S), no crossing — favored by the scalar precedent (the Class-C
    far-side slab homogenized its vertex counting away and drew the two-port core
    form to ~1 %);
  - **ELEC-VERTEX:** the vertex-form shape — negative at low/mid A, exactly ONE −→+
    crossing near A\* = √15/4 ≈ 0.968, positive endpoint — favored if vertex
    counting survives homogenization at this loading. At full vertex strength the
    negative region reaches Γ_B(0.5) ≈ −0.30 (θ-detectable); homogenization-scale
    suppression (~×0.12, the T4-fork homogenization close, `translation-circuit.md:189`,
    inherited via the Class-C prereg §2) would
    put it near −0.036 — below θ but above δ, hence the δ-level sign profile
    diagnostic (§6.2).
  Which shape the lattice draws (or neither) is the measurement. NEITHER shape is
  privileged by the freeze; both count as "draws the open phase" (§6.3).
- **No floor is expected on the two-port forms; the vertex forms share a −1/3
  intercept.** FLOOR (§6.2) is computed and recorded; it adjudicates nothing.

## §3 — CONFIG-GREP (challenge-canonical-negative, MANDATORY; epic guard 2)

Prove at CONFIG level that no closed negative's path is reconstructed. The Class-C
prereg's §3 is the template; the same three closed negatives are in this
neighborhood.

### §3.1 — The energize-LOCK / keystone-pump closed negative

| config key | CLOSED energize-LOCK path | THIS test |
|---|---|---|
| initial state | FREE PRECURSOR seeded to self-form | a passive probe pulse; nothing seeded that could bind |
| drive / pump | convergence-engine coupling; H PUMPED; probed at dt→0 | ZERO drive for t>0; closed system; E_Y conservation is a run GATE (§8 V2), not a casualty |
| dt→0 limit | load-bearing | DOES NOT EXIST here: the TLM step IS the discrete bond transit; no tunable integrator dt |
| medium↔field coupling | SELF-CONSISTENT (field builds its own cage) | NONE: scatter coefficients are PRECOMPUTED CONSTANTS from the frozen A(x); no A-update, no V-dependence of S (structural; drift- and checksum-gated, §8 V2) |
| claim scope | electron formation route | static linear response map; formation conclusions FORBIDDEN (§1) |

Genesis requires (precursor ∧ pump ∧ self-consistency); this config has none of the
three conjuncts. Result-doc grep obligations (run on the ACTUAL driver, word-bounded,
reported with counts): `pump|drive|driven|inject|source_term` → 0; `dt|dt0|timestep`
→ 0; plus a read of the step function body confirming no A-update and no
V-dependence of S.

### §3.2 — #415 (static coupled eigensolve bound-state negative)

| config key | #415 closed path | THIS test |
|---|---|---|
| operation | eigensolve of the coupled static operator | time-domain pulse scattering; NO eigensolve |
| object sought | bound eigenstate (mass + winding) | none — no bound-state search, no mode-existence claim |

Grep: `eig[a-z]*\(|linalg\.(eig|eigh|eigsh)` → 0 on the driver.

### §3.3 — #417 (phase-space winding / two-carrier ratio negative)

The two transverse POLARIZATION components of this run are NOT #417's two coupled
carriers, and the config table proves it rather than asserts it:

| config key | #417 closed path | THIS test |
|---|---|---|
| channels | TWO COUPLED carriers (ω_b, ω_s) with an inter-carrier coupling; phase-space winding readout θ = 2φ+3ψ | two transverse polarization components with NO inter-component coupling (optical activity OFF; scatter = S_u ⊗ I₂; connect = permutation ⊗ I₂). Component 1 is identically zero for the whole run (launch is component-0 linear; gated §8 V5) |
| observable | winding ratio (toroidal/poloidal turns) | signed reflection amplitude Γ on component 0; no winding, no ratio, no phase-space orbit is constructed |

Grep: `omega_b|omega_s|winding|poloidal|toroidal` → 0 on the driver.

### §3.4 — Over-determination tell (privileged constants, enumerated)

Privileged constants consumed: 1/√3 (cold network factor — a sanity GATE, not an
adjudicator); −1/3 (the CT-1 implementation identity — recorded, not adjudicating);
**√15/4 ≈ 0.96825** (the Form-B vertex-crossing location A\*, `ave_chart.py:79` —
the report-against location for a possible T-ELEC −→+ crossing, NON-BINDING: the
crossing's PRESENCE feeds §6.3, its LOCATION adjudicates nothing). No adjudication
threshold in §6 lands on any closed negative's number; all thresholds are declared
engineering choices with stated rationale (§7).

## §4 — Measurement design

### §4.0 — The transverse cancellation-trap walk (epic guard 4, identified BEFORE code)

The scalar trap, in-tree receipt (`vacuum_varactor_scatter.py:52-57`): a per-NODE-
UNIFORM admittance CANCELS at the shunt junction — a common factor Y in every Y_j
cancels in 2Y_j/Σ_k Y_k, reducing to (2/n)J − I regardless of S. The P0 receipt
extends it: per-node-uniform grading is invisible at scatter AND at connect. The
transverse analogs, identified here before any code is written:

- **T1 (inherited port-space cancellation).** The transverse graded junction is the
  same admittance-weighted shunt form per component, so the identical cancellation
  exists — and with a constant A over the slab it makes every INTERIOR slab node
  bedrock exactly (the response is boundary-layer-only; §2.2). GATES (module pytest,
  VOID-linked via §8 V1):
  (a) a GLOBAL-UNIFORM A (any value) must collapse the full graded operator to the
  bedrock, max abs deviation ≤ 1e-13;
  (b) for the ACTUAL slab A-field at A = 0.9 (each loading), the set of nodes whose
  per-node scatter differs from bedrock by > 1e-13 must EQUAL the computed
  mixed-admittance boundary-node set (count printed), be NON-EMPTY, and the max
  deviation over that set must be ≥ 1e-3 (the positive half now has a floor and can
  fail).
- **T2 (component-space trap, NEW to the transverse channel):** the bond has ONE
  impedance; the loading must be COMPONENT-SCALAR — one Y_b applied to BOTH
  polarization components (S_u ⊗ I₂). A per-component (polarization-anisotropic)
  loading would smuggle un-owned birefringent structure into the medium; a
  component-common-mode amplitude factor is a gauge scaling, not an admittance, and
  tests nothing. GATE (§5 CS-6b): global SO(2) polarization equivariance of the
  GRADED step — verified under BOTH loading maps (T-MAG and T-ELEC, each at
  A = 0.9), since an anisotropy present in only one map would otherwise pass.
- **T3 (observable blindness):** because the graded scatter is S_u ⊗ I₂ and commutes
  with global SO(2) on components, EVERY polarization-angle observable is blind to
  the grading — a null read on a polarization observable would be a structural
  artifact. DESIGN CONSEQUENCE (§4.4): Γ is extracted from port amplitude sums on
  the launch component only; no polarization-angle observable appears anywhere in
  the extraction.
- **T-CONN (bond-end equality at connect; renamed from "T4" so it can never be
  confused with the T4 homogenization-fork close cited in §2.7):** the Op3-style
  bond-mismatch connect
  (`chiral_lattice_vector_sat.connect_op3`) is blind to gradings equal at a bond's
  two ends. NOT APPLICABLE by design: CONNECT stays the untouched pure permutation
  (per component); the grading lives ONLY in the scatter. Declared so the trap
  cannot enter through a later "improvement".

### §4.1 — Machinery (the named extension, specified here; built after the freeze)

- **Net:** `build_srs_net(L=24, enantiomorph="right")` — periodic srs, degree 3,
  carrier `srs-z3`. L=24 adopts the Class-C DEVIATION D1 receipt (L=16 fails the V3
  timing budget on this exact geometry). [E1]
- **Field:** V_inc shape (N, 3, 2) — per node, per directed port, two transverse
  components.
- **The transverse per-directed-bond graded scatter (NEW module,
  `src/ave/solvers/transverse_graded_scatter.py` + pytest gates):** per-port
  admittances Y_u[p] from the per-bond grading via the CONFIG's loading map (§4.2);
  per-node scatter S_u = 2Y_j/(Σ_k Y_k) − δ_ij — the same Op5 shunt-junction KCL as
  the bedrock with per-port admittance retained (`vacuum_varactor_scatter.py:28-35`,
  the template) — applied IDENTICALLY to both transverse components (S_u ⊗ I₂, the
  ratified vector-TLM structure: *"Scatter uses the same Op5 shunt matrix on both
  components"*, `chiral_lattice_vector.py:4-5`). CONNECT = the lattice's own
  directed-edge permutation applied per component, UNTOUCHED. Losslessness is under
  the Y-weighted line-power norm **E_Y = Σ_{u,p} Y_{b(u,p)}·(V₀² + V₁²)[u,p]** —
  conservation GATED (§8 V2), not assumed.
- **The ε-load is built FRESH (SCOPE-ASSERTION compliance) and RECONCILED, not
  declared:** the electric-first map Y_b = Y₀·√S does NOT reuse `gamma_bulk`'s
  Z_eff form (the SCOPE ASSERTION / EPSILON-LOAD FORBID, `crystal_engine.py:471-474`:
  *"A future ε-load import MUST NOT reuse this method's Z_eff form"*). Load-type
  compliance is a COMPUTED gate, not a printed string: CS-7 (§5) reconciles the
  module's actual per-bond admittance array against
  `universal_operators.universal_dynamic_impedance(1.0, S(A), load=<declared>)` —
  the guarded reference implementation whose sign-lock raise (w35sn2bq3,
  `universal_operators.py:817-823`) is thereby actually in the path — at two
  non-trivial amplitudes, per config; and the module's pytest suite demonstrates the
  gate FAILS on a deliberately swapped label (both directions exercised).
- **R40-B2a stamps (epic guard 6, carried on reuse):** (i) the per-bond
  admittance-scatter reading of (V_inc, V_ref) as port phasor coordinates carries
  the in-file demotion stamp on the scalar template (`vacuum_varactor_scatter.py:72`:
  "[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead …]", family
  longitudinal-TLM-port, BIAS-DEBT) — scoped to the A1/longitudinal carrier reading;
  cited, never load-borne silently. (ii) the −1/3 counting fact's leaf carries its
  own inline stamp (`srs-vertex-scattering.md:24`, quoted in §2.6) — same
  treatment.

### §4.2 — The imposed grading (FROZEN map, per-bond, per-loading)

- Grading is **per-BOND**: one scalar A_b per undirected bond; both end-ports of a
  bond carry the same Y_b (enforced by construction, asserted at build time); both
  transverse components see the same Y_b (T2 fence, §4.0).
- Kernel: S(A) = √(1−A²), exact/unclipped (shared with the comparison forms —
  `ave_chart.saturation_kernel`, `src/ave/viz/ave_chart.py:92`).
- **CONFIG T-MAG:** Y_b = Y₀ / √(S(A_b))  (z_b = √S).
- **CONFIG T-ELEC:** Y_b = Y₀ · √(S(A_b))  (z_b = 1/√S).
- The A-field is computed ONCE before t=0 from the config geometry (§4.3), the
  per-node scatter coefficients are precomputed, and a SHA-256 checksum of the
  stacked per-node scatter array is taken at t=0 and re-verified at end-of-run.
  **Checksum scope, in the Class-C result's own words (quoted, with only the
  array/driver names generalized):** *"the t=0 hash … and the end-of-run hash … are
  both computed from the SAME in-memory [coefficient] array. The check can
  therefore detect in-place mutation of that array during the run, and nothing
  else; it is NOT evidence that the stepper read S from that array rather than from
  some copy or other source, and it cannot detect a leak that never writes back."*
  (`research/2026-08-24_engine-gamma-meanstest_result.md:314`.) The freeze is
  over-determined by three load-bearing things: the E_Y drift gate, CS-4, and the
  structural read of the step function (no A-update, no V-dependence of S) — all
  three reported. The same scope statement travels as a comment at the hash site in
  the driver.

### §4.3 — Geometry, launch, and the configuration matrix

Geometry: the far-side slab ONLY — the Class-C G-J geometry adopted verbatim with
its run-validated numbers (the crossing-bond geometry was INVALID-EXTRACTION on the
scalar channel — 16/16 discordant, sign window-selected — and the taper geometry
adjudicates an adiabaticity question not asked here). All coordinates in cells:
**x_s = 2, x_p = 6, x_I = 9, x_B = 15, W = 6, wrap margin 11, back monitor 15.5,
sentinel plane 19.5 at 1 % threshold, L = 24.** [E2] Bond membership by
endpoint/midpoint minimum-image x-coordinates, exactly as the Class-C driver's bond
tables.

- **Grading region (both configs):** A_b = A for every bond with BOTH endpoints in
  x_I < x < x_B; bonds crossing x_I stay cold. The incident wave arrives on a cold
  feed bond and sees graded far arms — whose isolated-vertex algebra is the
  MAG-VERTEX form (T-MAG) / the ELEC-VERTEX form (T-ELEC), §2.2.
- **Launch [E3]:** baseband Gaussian plane pulse, σ_x = 1.5 cells, +x̂-directional
  port weighting max(0, −x̂·b̂_{u,p}) (the Class-C DEVIATION-D2-corrected sign,
  adopted with its receipt), **linearly polarized in component 0; component 1
  identically zero at launch.**
- **Amplitude grid [E4]:** the identical 16-point grid of the Class-C run —
  A ∈ {0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.925, 0.95, 0.9682,
  0.98, 0.99} — shared for direct comparison against the banked scalar record
  (R-2), **with A = 0.9682 re-declared as the T-ELEC vertex-crossing probe: the
  grid point NEAREST A\* = √15/4 ≈ 0.968246 (offset 4.6e-5, §2.2/§3.4). The grid
  literal 0.9682 is FROZEN — banked-grid identity, required by R-2 — and must NOT
  be replaced by `ave_chart.A_MATCHED_B`** — the grid's density at
  0.95/0.9682/0.98/0.99 resolves a possible crossing there. A = 0.0 is the
  null-calibration point. **16 points × 2 loadings = 32 runs.**
- Run length T = 170 steps per graded run, cold gate T = 200, hard cap 6000 [E5].
- Because CONNECT is Y-independent (fixed delay, §2.5), both loadings carry the
  IDENTICAL timing budget as the Class-C run; the binding window close there was the
  grading-independent wrap sentinel (87.776 projected, close 78), so window
  constructibility transfers. Gated anyway (V3), never assumed.

### §4.4 — Γ extraction (DECLARED; phase-space-coordinate-check, epic guard 3)

**Coordinate map (explicit).** The TLM port variables ARE the phasor coordinates:
V_inc[u,p,c] is the incident amplitude arriving at node u on port p in transverse
component c; the scattered wave is V_ref = (S_u ⊗ I₂) V_inc. On a probe bond
crossing x_p, after CONNECT the port variable at the far endpoint facing the near
one carries the forward (+x̂) wave and vice versa — Op3's (V_inc, V_ref) split read
directly on the bond cross-section, on the launch component. No real-space field
proxies; per trap T3, NO polarization-angle observable enters the extraction.

- **Records (every step):** F(t), B(t) = forward/backward probe-plane port sums of
  component 0; Fb(t) = the forward sum at the back monitor; direction-resolved
  sentinel maxima at the wrap plane; **C1_leak(t) = max over the whole lattice of
  |V_inc[·,·,1]|** (the polarization-leak sentinel, §8 V5).
- **Windows:** derived exactly as the Class-C driver
  (`engine_gamma_meanstest.py:504-545` + `:892-905`, pinned verbatim as the rule):
  incident = cold transit centroid ± 2σ_t; reflected opens at incident close + 1
  and closes at the earliest of (a) the slab-back first-return bound from the
  MEASURED back-monitor transit of the GRADED runs — per-config back-monitor
  centroid via `pulse_moments` over [0, 1.8·expected transit], MINIMUM over the
  A > 0 grid points, converted centroid→front by −2σ_t, THEN the −2σ_t guard (two
  subtractions); if a config has no measurable back-monitor transit, branch (a) is
  dropped and (b) alone sets the close (the banked G-B precedent,
  `t_back_return = None`) — and (b) the cold run's wrap-sentinel projected probe
  arrival minus the 2σ_t guard [E6]. (The min-over-A reduction makes (a) robust to
  weak high-A transmission on T-ELEC: the strongest early-A transits set the
  bound.) **Gate-role naming (frozen):** the GUARDED bound
  (arrival − 2σ_t ≥ close) is the window-CONSTRUCTION rule; the STRICT bound
  (arrival > close), re-verified per run by the standalone checker, is the §8 V3
  VOID trigger. **Ordering (the Class-C D5 lesson adopted into the freeze):**
  because close-bound (a) consumes graded-run measurements, the graded runs execute
  as DATA COLLECTION ONLY after CS-1..CS-4, CS-6, CS-7, CT-1 and the module gates
  pass; windows are then derived (which is when R-1 becomes checkable); CS-5 and
  R-1 are adjudicated BEFORE any graded datum is interpreted.
- **Primary signed estimator:** the Class-C matched filter verbatim (template = F in
  the incident window; τ* = argmax |xcorr| over admissible lags with the
  25 %-template-energy-in-window admissibility floor and the window-restricted
  denominator — the two D7-disclosed operationalizations adopted as DECLARED spec).
  Sign convention: Γ < 0 = polarity-inverted echo (short-like, −1 rim); Γ > 0 =
  same-polarity echo (open-like, +1 rim) — matching Γ = (z−1)/(z+1).
- **Secondary unsigned cross-check:** |Γ|_E = √(E_B/E_F). Discordance
  |(|Γ_meas| − |Γ|_E)| / max(|Γ|_E, θ) > 0.2 marks the point UNRELIABLE (recorded
  per point). **INVALID-EXTRACTION (config level, informative points only):** the
  > 4-unreliable tally counts ONLY points with max(|Γ_meas|, |Γ|_E) > θ — the
  near-null region is a structural estimator-floor mismatch (the matched filter
  reads ~ε₀ while the energy estimator carries its own ~3× floor; measured in the
  Class-C record) and is excluded from the tally, with all near-null discordances
  reported separately as a diagnostic. [E12]
- **Window-convergence receipts (the Class-C AMD-1 lesson adopted into the freeze;
  computed, not asserted):** per config per grid point, the result doc reports
  (i) `tmpl_contained` at the locked τ*; (ii) the post-window tail-energy fraction
  of the reflected trace over steps [close+1, close+8]; (iii) a re-extraction sweep
  over reflected-window closes {60, 64, 70, 74, close_f} where close_f = that
  config's derived guarded close (expected 78; 60/64 are early-truncation probes)
  with the Γ deltas tabulated. **Stability rules (frozen; stated for T-ELEC — on
  T-MAG any of these firing contradicts the banked window-converged record and is
  an R-3 concordance failure ⇒ R-FAIL, §6.3):**
  (S1) if SIGN_top or the θ-crossing count of T-ELEC changes across its
  {70, 74, close_f} closes on valid points, the T-ELEC verdict is
  **INDETERMINATE-WINDOW** (reported; no branch claim).
  (S2) Point-level labels: any valid point with |Γ(close_f) − Γ(70)| > δ is
  WINDOW-SENSITIVE; any valid point whose tail-energy fraction (receipt ii)
  exceeds 0.02 is TRUNCATION-SUSPECT. Both reported; the verdict uses close_f.
  (S3) Magnitude escalation (the receipt-consuming rule the Class-C AMD-1
  pathology — sign-stable truncation — needs): if ≥ 3 valid T-ELEC points are
  TRUNCATION-SUSPECT, OR the median over valid points of
  |Γ(close_f) − Γ(70)| / max(|Γ(close_f)|, θ) exceeds 0.1, the T-ELEC verdict is
  **INDETERMINATE-WINDOW**, and a NON-adjudicating convergence probe is REQUIRED
  reporting: re-extraction at the largest close strictly below the earliest
  projected contaminant arrival (unguarded, the AMD-1-style probe; labeled
  convergence-probe, never a verdict input). [E11]
- **Per-run V3 re-verification is a standalone checker script**
  (`transverse_gamma_meanstest_check_sentinels.py`, built WITH the driver): it
  consumes the shipped per-run sentinel series, recomputes every projected
  contaminant arrival, applies the STRICT and GUARDED gates per run, and reconciles
  its earliest arrival against the driver's cold-run projection to 1e-9. Its full
  output is a REQUIRED appendix of the result doc.

## §5 — Gates (ordering per §4.4; the run is VOID on any failure)

**Pre-graded (before any graded configuration):**

- **CS-1 (closed-system conservation, cold vector):** uniform scatter on both
  components, the actual polarized launch; max relative energy drift over 200 steps
  < 1e-10.
- **CS-2 (velocity + band edge):** `network_velocity_factor` (axis = x, m = 1..4):
  the k→0 extrapolated factor within 2 % of ANALYTIC_NETWORK_FACTOR = 1/√3, AND the
  literal smallest-k reading recorded and gated at the same 2 % (the Class-C D8
  lesson, both readings shipped). Band edge: ≥ 95 % of pulse spectral energy
  (analytic erf + per-cell discrete FFT) below k_edge, where **k_edge = the largest
  SAMPLED k with c(k) within 5 % of c₀; if ALL sampled k qualify (the Class-C
  case), k_edge = k(m=4) and the gate is reported as a bound-from-below on the true
  band edge, not a measurement of it.** VALIDITY NOTE: this is the scalar-machinery
  measurement; it transfers because the vector step is two decoupled scalar copies
  — the decoupling is itself GATED at CS-6a, so the transfer is receipted.
- **CS-3 (time-of-flight):** cold pulse centroid velocity source→probe within 5 %
  of the CS-2 c₀.
- **CS-4 (graded-path regression):** the vector graded machinery with ALL bonds cold
  reproduces the uniform-scatter SCALAR trajectory on component 0 to ≤ 1e-12 over
  200 steps, with component 1 identically zero.
- **CS-6 (transverse structure gates — the §4.0 trap gates at run level):**
  (a) DECOUPLING: with the component-0 launch, max over 200 cold steps of
  max|V[·,·,1]| ≤ 1e-14; (b) SO(2) EQUIVARIANCE at a GRADED operator, under BOTH
  loading maps (T-MAG at A = 0.9 AND T-ELEC at A = 0.9): a launch rotated by
  0.7 rad in the polarization plane produces the identically rotated trajectory
  (max abs deviation ≤ 1e-12 over 100 steps). These probes use a graded OPERATOR
  but are structure-gate runs, not §4.3 measurement runs (V5 does not apply to
  them — their component-1 content is prescribed non-zero).
- **CS-7 (load-map reconcile; reconcile-don't-declare):** for EACH config, at
  A ∈ {0.5, 0.9}: the module's actual per-bond Y_b/Y₀ on graded bonds equals
  1 / `universal_dynamic_impedance(1.0, S(A), load=<the config's declared load>)`
  to ≤ 1e-12 — the guarded reference is in the path, and the module pytest
  demonstrates this gate FAILS on a deliberately swapped label (both directions).
- **CT-1 (implementation identity, demoted per §2.6):** the cold bare 3-port vertex
  matrix applied per component returns S_ii = −1/3 and S_ij = 2/3 to ≤ 1e-15 abs
  per entry on each component. An implementation receipt ONLY (it cannot carry
  channel content); recorded, never cited as a transverse-vertex verification.
- **Module gates T1(a)/T1(b)/CS-7-swap (pytest, §4.0/§4.1):** T1(a)/T1(b) per
  §4.0; CS-7-swap = the module-pytest demonstration that the CS-7 load-map
  reconcile FAILS on a deliberately swapped label, both directions (§4.1). All
  must be green before the driver runs; VOID-linked via §8 V1. (The T2 trap's
  gate is the RUN-level CS-6b, not a module gate.)

**Graded data collection (uninterpreted), then before interpretation:**

- **R-1 (reproduction, windows; binds T-MAG ONLY):** T-MAG's derived windows
  (checkable only after data collection — close-bound (a) consumes graded
  back-monitor transits, §4.4) must equal the banked Class-C G-J windows
  (incident [10, 29], reflected [30, 78], `engine_gamma_meanstest_results.json`);
  mismatch ⇒ machinery investigation, VOID. **T-ELEC's windows are derived by the
  same §4.4 rule and REPORTED; a T-ELEC window difference is never a VOID** — if
  its guarded close close_f differs from 78, the E11 sweep/stability sets adjust
  to closes ≤ close_f (recorded as a dated deviation), and "the frozen close"
  means each config's own derived guarded close throughout.
- **CS-5 (null calibration):** each loading config at A = 0 through the full
  extraction pipeline: |Γ| < 0.02; noise floor ε₀ = max over the two configs;
  **θ = max(3·ε₀, 0.05)**; δ = max(ε₀, 0.01).
- **R-2 (reproduction, locus):** max over the 16 grid points of
  |Γ_TMAG(A) − Γ_GJ,banked(A)| < 1e-6 against the banked table
  (`research/drivers/engine_gamma_meanstest_results.json`, table.GJ, matched-filter
  column). Failure ⇒ MACHINERY defect (the identity of §2.4 is mathematical) ⇒ VOID.
- **R-3 (reproduction, classifiers):** classifiers recomputed on T-MAG (with THIS
  run's flags) concord with the banked ones on {SIGN_top = −, θ-crossing count = 0,
  monotone direction = decreasing}. Per-point valid-flag differences vs the banked
  run are REPORTED (the closest banked point — G-J at A = 0.3, discordance
  0.19745 — sits 0.00255 inside the 0.2 bound in the frozen window and crossed it
  at the Class-C AMD-1 extended close; a valid-flag flip there is a foreseen
  extraction-sensitivity outcome, not an R-fail unless a classifier flips).

**Any gate failure ⇒ the ENTIRE run is VOID (V1/§8).** No graded data may be
interpreted.

## §6 — FROZEN EXPECTATIONS and ADJUDICATION RULES

### §6.1 — Expected loci

As frozen in §2.7 (T-MAG: the banked locus, reproduced; T-ELEC: ELEC-CORE or
ELEC-VERTEX, both drawing SIGN_top = +; no floor expected; FLOOR recorded only).

### §6.2 — Frozen classifiers (computed per loading from the valid grid points)

With θ and δ from CS-5; "valid" = the per-point §4.4 flag:

- **SIGN_top:** the sign of Γ_meas at the highest VALID grid point with
  |Γ_meas| > θ; if no valid point exceeds θ, SIGN_top = UNDEFINED (→ T-ELEC is
  INDETERMINATE per §6.3; on T-MAG an all-sub-θ locus contradicts the banked
  record — |Γ_GJ,banked| > θ from A = 0.6 up — and is an R-3 concordance failure
  ⇒ R-FAIL).
- **θ-CROSSING:** adjacent valid pair with opposite signs, BOTH |Γ_meas| > θ;
  direction and count recorded; a −→+ crossing's location is reported against
  A\* = √15/4 (non-binding).
- **δ-level sign profile (recorded, NON-adjudicating):** the signs of all valid
  points with |Γ_meas| > δ — the diagnostic that keeps a homogenization-suppressed
  vertex signature (sub-θ, supra-δ) visible in the record.
- **MONOTONE:** signed Γ_meas monotone across valid points within ±δ; direction
  recorded. (Recorded for both loadings; a draws-conjunct only where §6.3 says so.)
- **FLOOR:** linear fit over valid points with 0 < A ≤ 0.5; requires ≥ 3 valid
  points there, else NOT-COMPUTABLE (reported with the count); |intercept| > θ ⇒
  FLOOR. Recorded, not adjudicating.
- **SHAPE (T-ELEC, recorded):** ELEC-CORE-like (no θ-crossing ∧ monotone increasing
  within δ) / ELEC-VERTEX-like (exactly one −→+ θ-crossing) / OTHER (described).
- **MIRROR (recorded, NON-adjudicating):** over grid points valid in BOTH configs
  with max(|Γ_TMAG|, |Γ_TELEC|) > θ: max and median of
  |Γ_TELEC(A) + Γ_TMAG(A)| / max(|Γ_TMAG(A)|, |Γ_TELEC(A)|, θ) (symmetrized
  denominator). Requires ≥ 3 such points, else N/A (reported with the count); if
  either loading is INVALID-EXTRACTION, reported as NOT-COMPUTABLE with the reason.
  The expected mechanism of any nonzero MIRROR defect is the shared −1/3 vertex
  intercept of Form J/Form B (§2.2), not slab-interior multiple scattering.

### §6.3 — Per-loading outcomes (a PARTITION — no third state can exist)

**T-ELEC** (the adjudicated new measurement). Outcome space
{DRAWS-OPEN, NONE, INDETERMINATE, INDETERMINATE-WINDOW, INVALID-EXTRACTION} —
evaluated in this order, first match wins:

1. **INVALID-EXTRACTION** (§4.4 informative-point tally > 4).
2. **INDETERMINATE-WINDOW** (§4.4 stability rule fires).
3. **INDETERMINATE:** SIGN_top = UNDEFINED (no valid point above θ — the ε-side
   response is below the adjudication floor everywhere; reported; flags the
   geometry for redesign in a follow-on; no branch claim either way).
4. **DRAWS-OPEN:** SIGN_top = + ∧ no +→− θ-crossing ∧ at most one θ-crossing
   (if one, its direction is −→+ by the preceding conjunct; the SHAPE label is
   computed separately per §6.2 and is not part of this verdict).
5. **NONE** (defined as the complement — everything else): SIGN_top = − ∨ any +→−
   θ-crossing ∨ ≥ 2 θ-crossings. The measured locus itself is then the result,
   reported without a branch label.

**T-MAG** (the reproduction config). Outcome space {REPRODUCED, R-FAIL}:
REPRODUCED iff R-1 ∧ R-2 ∧ R-3 pass (its branch-phase content — the deepening
negative locus — is the banked Class-C measurement, reproduced on the new
machinery); R-FAIL ⇒ VOID (machinery defect, never physics). T-MAG has no
INDETERMINATE or INDETERMINATE-WINDOW state: the banked locus is
window-converged and above θ at high A, so window instability or an all-sub-θ
reading on T-MAG (§4.4/§6.2) is an R-3 concordance failure ⇒ R-FAIL by
construction.

### §6.4 — Pair adjudication (frozen outcome table; T-MAG must be REPRODUCED or the
run is already VOID)

| T-ELEC outcome | verdict |
|---|---|
| DRAWS-OPEN | **The two reciprocal impedance loadings draw opposite boundary phases at response-map level** — the ε-side (z = 1/√S) locus measured for the first time on any channel, the μ-side the banked scalar locus reproduced in the 2-component container. Scoped per §2.5 to boundary-phase content; NO sector-ownership claim (§2.3's flagged split stands); NO transverse-distinctness claim (§2.4); #260 untouched. SHAPE and MIRROR reported as diagnostics. |
| NONE | The ε-loading does not draw the open boundary phase in this geometry — a physics surprise: reported prominently with the measured locus, frozen-classifier language only, and a **STUCK-POINT report to Grant** before any interpretation beyond the frozen classifiers. |
| INDETERMINATE | The ε-side response is below the adjudication floor everywhere — reported as such; no branch statement in either direction; geometry-redesign follow-on flagged (not adjudicated). |
| INDETERMINATE-WINDOW | The verdict-driving classifiers are window-unstable — reported as such with the sweep table; no branch statement; window/geometry follow-on flagged. |
| INVALID-EXTRACTION | The loading is not adjudicated (reported with the discordance table); no branch statement; the T-MAG reproduction receipt still stands on its own. |

### §6.5 — Explicit non-adjudicators

Quantitative deviation from any lumped curve; the MIRROR defect magnitude; the
crossing LOCATION vs √15/4; the FLOOR intercept value; the δ-level sign profile;
CT-1's value; the SHAPE label (which candidate T-ELEC draws is recorded, not
pass/fail); the fixed-delay limitation (§2.5 — the run cannot distinguish which
constitutive parameter saturates, only the boundary phase); T-MAG's agreement with
the banked locus (it adjudicates MACHINERY only — the R-2 VOID gate — and is a
non-adjudicator of every physics question, §2.4). The overlay figure
(measured points on the four §2.2 forms) is published in the result doc regardless
of verdicts.

## §7 — Engineering-choice register (every non-lattice-derived parameter)

| # | parameter | value | tag rationale |
|---|---|---|---|
| E1 | L = 24 cells | net size | adopts the Class-C D1 MEASURED receipt (L=16 fails the V3 timing budget on this geometry); not lattice-derived |
| E2 | geometry x_s/x_p/x_I/x_B/W = 2/6/9/15/6, back monitor 15.5, sentinel 19.5 @ 1 %, wrap margin 11 | imposed-probe geometry | Class-C run-validated numbers adopted verbatim; not substrate-derived |
| E3 | pulse: baseband Gaussian, σ_x = 1.5 cells, weighting max(0, −x̂·b̂), polarization = component 0 | launch | probe design; band-content gated at CS-2; polarization choice immaterial by CS-6b equivariance (receipted under both maps) |
| E4 | A-grid (16 points, §4.3) | sweep resolution | shared verbatim with the banked scalar record (R-2 comparability); A = 0.9682 (the frozen grid literal, nearest-point probe of A\* — NOT equal to it, offset 4.6e-5) is the declared T-ELEC vertex-crossing probe; not tuned to any closed negative (§3.4) |
| E5 | T_run = 170, T_cold = 200, hard cap 6000 | budget | timing from the Class-C measured budget; cap is engineering |
| E6 | window guard 2σ_t; matched-filter estimator incl. the 25 % admissibility floor + window-restricted denominator; discordance 0.2 / 4 points | extraction | declared estimator (the Class-C D7 operationalizations adopted as spec); cross-checked |
| E7 | gate tolerances: 2 % (CS-2 both readings), 5 % (band / CS-3), CS-1 1e-10, CS-4 1e-12, V2 drift 1e-8, ε₀ cap 0.02, θ = max(3ε₀, 0.05), δ = max(ε₀, 0.01), CS-6a 1e-14, CS-6b 1e-12 @ 0.7 rad, CS-7 1e-12 @ A∈{0.5,0.9}, CT-1 1e-15, T1(a) 1e-13, T1(b) floor 1e-3 @ A=0.9, R-2 1e-6, V5 leak 1e-12, checker reconcile 1e-9 (VOID-linked via V3), CS-2 band containment ≥ 0.95 (smaller of analytic/discrete), FLOOR ≥ 3 valid pts in 0 < A ≤ 0.5, MIRROR ≥ 3 co-valid pts, tail-fraction 0.02, stability median fraction 0.1, TRUNCATION-SUSPECT count 3 | thresholds | all declared pre-run; none tuned to closed negatives |
| E8 | enantiomorph "right"; optical activity OFF | build choice | ACHIRAL measurement: with the twist off the vector step is two decoupled scalar copies (gated CS-6a) and the scalar channel is achiral per Phase-0 receipts; enantiomorph immaterial, recorded |
| E9 | the TWO impedance maps z = √S (T-MAG) and z = 1/√S (T-ELEC) on S(A) = √(1−A²) | the frozen A-parametrization of both sides | the kernel is canon (`CLAUDE.md:73`); the impedance conventions are the two named in-tree forms (`universal_operators.py:788-800`); the μ-side CONSTITUTIVE label is one horn of the routed-open μ-at-core fork (`saturation-rim-inversion.md:70`, quoted §2.2) — the map functions here as the declared reciprocal control, and the run adjudicates boundary phase at fixed maps, never the maps' exponents or the fork |
| E10 | loading is component-scalar: ONE Y_b per bond, applied to BOTH components | the T2 trap fence (§4.0) | substrate-derived in DIRECTION (a bond has one impedance), engineering in enforcement; gated CS-6b under both maps |
| E11 | window-convergence set: closes {60, 64, 70, 74, close_f} per config (close_f = that config's derived guarded close, expected 78); tail probe [close+1, close+8]; stability set {70, 74, close_f}; escalation thresholds tail 0.02 / median fraction 0.1 / count 3; the unguarded convergence probe fires only as REQUIRED reporting under §4.4 rule S3, never as a verdict input | convergence receipts | the Class-C AMD-1 lesson adopted into the freeze, WITH the magnitude escalation its sign-stable truncation pathology needs |
| E12 | INVALID-EXTRACTION tally counts only informative points (max(\|Γ_meas\|, \|Γ\|_E) > θ) | extraction validity | excludes the structural near-null estimator-floor mismatch (measured in the Class-C record) from a physics-validity tally; near-null discordances still reported |

## §8 — VOID conditions (the run is null and interprets NOTHING)

- **V1 — Gate fail:** any §5 failure (CS-1..CS-7, CT-1, the module pytest gates
  T1(a)/T1(b)/CS-7-swap, R-1/R-2/R-3).
- **V2 — Grading leaks into dynamics:** E_Y relative drift ≥ 1e-8 in any graded
  run; OR the SHA-256 checksum fails re-verification (scope as quoted in §4.2 — the
  freeze evidence is the drift bound + CS-4 + the structural step-function read,
  all three reported); OR CS-4 fails.
- **V3 — Wrap-around / contamination:** the reflected window must be constructible
  with positive width under the measured timing budget; the per-run STRICT bound
  (checker script) is the VOID trigger — any projected contaminant arrival ≤ any
  window close in any run ⇒ VOID; AND the checker's earliest per-run projected
  arrival must reconcile to ≤ 1e-9 against the driver's cold-run projection, else
  VOID (the reconcile is what gives STRICT independent fireability — the close is
  CONSTRUCTED from the cold projection, so STRICT can only fire through a per-run
  disagreement with it). (GUARDED is the construction rule, §4.4.) Not
  constructible ⇒ VOID and the geometry must be re-frozen in an amended prereg
  before any re-run.
- **V4 — Window sanity (constructional assert):** reflected-window width ≤ 0, or
  the reflected window opening earlier than the incident close + 1 — cannot occur
  if the §4.4 construction is implemented correctly; asserted so an implementation
  slip is caught rather than assumed away.
- **V5 — Polarization leak:** any of the 32 §4.3 configuration-matrix runs
  (component-0 launch) with max_t C1_leak > 1e-12 ⇒ the step is not
  S_u ⊗ I₂ + permutation ⊗ I₂ (implementation defect) ⇒ VOID. (The CS-6b
  equivariance probes are excluded by construction — their component-1 content is
  prescribed non-zero; they are structure-gate runs, not measurement runs.)
- Per-config **INVALID-EXTRACTION** (§4.4) voids that loading's adjudication only
  (§6.3 handles it as a named outcome).

## §9 — Reporting requirements (binding on the run)

1. RESULT doc = this prereg's pair
   (`research/2026-08-24_transverse-gamma-meanstest_result.md`): verbatim gate
   outcomes with numbers, the 32-point Γ_meas table (signed, both estimators,
   per-point flags), classifier outputs (§6.2, incl. SHAPE, MIRROR, δ-profile,
   FLOOR with computability), the window-convergence receipts (§4.4/E11), verdicts
   strictly via §6.3/§6.4, overlay figure (white house style via
   `ave.viz.style.apply`, Okabe-Ito, no title, legend outside the data, honest
   axes; the four §2.2 forms drawn, measured points overlaid).
2. Raw-series landing:
   `research/drivers/data/transverse_gamma_meanstest/raw_{TMAG,TELEC}.json`
   (full F/B/back-monitor/sentinel/C1_leak series per grid point) +
   `cold_sanity.json` + `run_log.txt`;
   `research/drivers/transverse_gamma_meanstest_results.json`; the driver prints
   every parameter it actually uses (driver-script honesty).
3. The standalone sentinel checker's full output is a REQUIRED appendix.
4. Any deviation from this document is an AMENDMENT logged in the result doc with
   its own dated entry; the prereg file itself is never edited.
5. The §1 forbidden-conclusion list AND the §2.3 flagged sector split AND the §2.4
   replay identity are restated in the result doc's scope block.
6. Adversarial verify (≥3 lenses: config-compliance re-grep on the actual driver;
   physics/coordinates incl. the sector-ownership read; independent numerics rerun)
   happens AFTER the result doc is drafted; the repairs-need-reaudit loop runs to
   convergence; verdict language stays frozen-criterion-only throughout.

— END OF FROZEN PREREG —
