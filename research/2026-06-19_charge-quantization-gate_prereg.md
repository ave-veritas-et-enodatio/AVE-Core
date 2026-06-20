# Pre-registration — Carrier-sector GATE #2 (#43): Charge-quantization structural gate

**Frozen:** 2026-06-19 (BEFORE running the rigorous 𝒬 read — discriminating test, bins fixed first)
**Branch:** `analysis/2026-06-19-charge-quantization-gate`
**HEAD at freeze:** `bb206fa2` (PRs #296/#297/#298/#299 merged — GATE #1 spin double-cover PASS landed)
**Lane:** implementer
**Class (consistency-vs-emergence):** **D / representability + structural-protection** — reads a
topological invariant (an integer winding/linking) from substrate primitives. NO CODATA-derived
number is read. **VALUE-ECHO IMMUNITY**: only the integer 𝒬 and its sign are read; the dimensionful
`-e` (`constants.py:100`) and `α` are NEVER imported or read in this gate.

---

## The framing (what is at stake)

QED does **not** explain charge quantization. Integer charge is put in by hand via the hypercharge
assignment; the only "explanations" on offer require **unobserved** physics (magnetic monopoles —
Dirac quantization; or GUT embedding). Separately, QED renders the point-charge self-energy finite
**only by renormalization** (subtracting an infinity from the bare self-energy).

AVE's claim — **charge = a topological winding/linking integer** — is, IF it holds:
- **FINITE** (a counted integer, no divergent self-energy to subtract),
- **EXACT** (an integer, not an asymptotic series),
- **quantized BY CONSTRUCTION** (no renormalization step; the integer is forced by the field topology),
- and it **EXPLAINS** the quantization (the integer is a property of the field configuration's topology,
  not an external input).

So a **PASS is a structural advance over QED** on a problem QED cannot solve.

**HONEST SCOPE (load-bearing, carried into the result):**
1. This gate is **CONDITIONAL on the [Q] ≡ [L] identification** (charge ≡ the topological
   winding/linking integer of the Cosserat ω micro-rotation grade). That identification is **asserted,
   not derived-from-nothing** — it is the TKI (Topological Knot Identification) axiom-level posit. The
   gate tests whether, GIVEN that posit, the quantization is structurally forced. It does NOT derive
   the posit.
2. This gate is **SEPARATE from self-formation / genesis**. It tests STRUCTURAL quantization on a
   **PLANTED** winding. It does **NOT** claim the winding self-forms (that is the genesis/keystone
   question, which **LEANS-FALSIFIED** per the keystone-energize-LOCK negative). The result is
   *"IF a (2,3) winding exists, its charge is a topologically-forced integer"*, **NOT** *"the electron
   self-forms"*. Do not conflate; do not headline emergence.

---

## Question (plumber-physical)

If you plant a (2,3) winding on the Cosserat micro-rotation field ω and read its boundary charge 𝒬,
do you get a **clean integer** that is **the winding number** — and, crucially, does that integer
**stay put** when you wiggle the field around (smoothly, without cutting the knot)? A real topological
invariant is a number that **cannot drift** under continuous deformation — it can only **jump** when
you actually change the topology (unwind the knot). If 𝒬 holds its integer through arbitrary smooth
wiggles and jumps only when the knot is cut/unwound, the quantization is **forced by the topology**,
not by the way we planted it. That deformation-robustness is the whole demonstration.

This is a **kinematic / static** test: no time-stepping, no energy budget, no frequency-vs-timestep,
no genesis. The Nyquist / energy / CFL gates do NOT bind at this diagnostic scale. 𝒬 is a **boundary**
observable → **no sub-cell interior resolution is required** (the #39 sub-cell dodge: the canonical
electron is 2× past the cell Nyquist, so we do NOT try to resolve the interior; we read the boundary
integer at a lattice-resolved diagnostic scale R ≥ 4 cells).

---

## Substrate-native construction of 𝒬 (resolves the corpus C.3 reconciliation gap)

The corpus carries **two** definitions of 𝒬, flagged OPEN at
[`electron-bound-resonator-coverage.md:169`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md)
(coverage row C.3):

- **1D linking number** `𝒬 = Link(∂Ω, F_substrate) ∈ ℤ`
  ([`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md):20 — dimensionality "1D line/loop"),
- **3D Beltrami helicity** `𝒬 = H_bel = ∫ ω·(∇×ω)`
  ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 — the two-"3"s disambiguation: *"charge = Beltrami helicity H_bel = ∫ω·(∇×ω)"*).

The corpus says these are *"almost certainly two projections of ONE charge via helicity = linking
(Moffatt 1969); that identity is NOT written for the AVE case."* This gate **writes that identity for
the AVE case**, computing BOTH and showing they agree on the same integer:

1. **F = curl ω** (the substrate flux field; `_tetrahedral_curl` already exists,
   `cosserat_field_3d.py:514`).
2. **𝒬_link** = the **real-space Gauss linking integer** between the boundary loop ∂Ω (the |ω|
   level-set's major circle) and the F = curl ω flux line threading it. This replaces the
   connected-component **PROXY** named DEFERRED at `boundary_invariants.py:146-151`.
3. **𝒬_hopf** = the **Chern–Simons / Hopf self-linking integer**
   `Q_H = (1/4π²) ∫ A·B` with `B = curl-of-director`, `A` the Coulomb-gauge inverse-curl (the existing
   `_hopf_density`, `cosserat_field_3d.py:319`, integrated and normalized). For a (p,q) torus knot
   `Q_H = p·q` ([`torus-knot-uniqueness.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md):23).
4. **𝒬** is reported as the integer + sign read from these. The **sign** is the chirality (handedness)
   of the winding (the charge sign). Helicity = linking (Moffatt) is the identity that ties 𝒬_hopf to
   the helicity integral; agreement of 𝒬_link with 𝒬_hopf's expected `p·q` closes C.3 for this case.

**Distinct-coordinate note (GUARD 4):** the (2,3) is fenced as a PHASE-SPACE winding portrait
(`def-kn0t01` SOLID). The flux/linking HERE is a **REAL-SPACE field-line topology** on the Cosserat ω
micro-rotation grade. The two coordinate systems are kept distinct; this gate is a real-space ω-field
linking read, NOT a phase-space `(2,3)` Clifford-torus measurement.

---

## VALIDATE-ON-KNOWN anchors (MANDATORY, wired FIRST — the Build-A lesson)

The de-novo 𝒬 read is built BETWEEN two anchored poles. No build is interpreted without both.

- **KNOWN-NEGATIVE (ω ≡ 0 null):** the unstrained vacuum. `F = curl 0 = 0`, no flux line, no boundary
  winding → **𝒬 = 0**. If the null does not return 0, the instrument is broken → **HALT**.
- **KNOWN-POSITIVE (planted (p,q) winding recovers its winding integer):** a planted winding whose
  field-line topology is known by construction recovers 𝒬 → its winding integer (cf. the existing
  plant-and-recover `_planted_2_3_field` / `spec_T2_charge_winding` and the `_hopf_density` (2,3) test
  `test_cosserat_field_3d.py:490`). For the (2,3): 𝒬_hopf → the (p,q) self-linking `p·q = 6` (sign =
  chirality). If the known-positive does not recover its known integer, the instrument is broken →
  **HALT**.

---

## Frozen bins (set BEFORE running)

| Verdict | Signature | Meaning |
|---|---|---|
| **PASS** (topologically-FORCED integer quantization) | 𝒬 is (a) an **INTEGER** (within tolerance of the nearest integer), (b) equal to the planted winding's integer / sign, (c) **ROBUST** — invariant (same integer) under a sequence of continuous, topology-preserving ω-deformations, and (d) **INDEPENDENT of α / m_e** (no value-echo). AND the topology-CHANGING (unwind) operation makes 𝒬 **jump** to a different integer / 0. | Charge quantization is a topological invariant **forced by the substrate**: finite, exact, quantized-by-construction. Structural advance over QED (which puts integer charge in by hand and renders self-energy finite only by renormalization). **Scope: conditional on TKI [Q]≡[L]; NOT a self-formation claim.** |
| **ECHO / FAIL** | ANY of: 𝒬 **non-integer**; OR 𝒬 **deformation-SENSITIVE** (drifts continuously under topology-preserving wiggles → not topologically protected → not a real invariant); OR 𝒬 **α-dependent** (a value leak); OR 𝒬 merely **counts the planted amplitude** without topological forcing (drifts with amplitude, or does not jump on unwind). | The quantization is NOT structurally forced — it is an artifact of the planting / a non-topological count. **A clean negative — report honestly, name the failing condition, do NOT debug toward PASS.** |
| **HALT** (solver bug) | A known-anchor misbehaves: ω≡0 null does not give 𝒬=0, OR the planted known-positive does not recover its known winding integer. | The instrument is broken; the discriminator is uninterpretable. Fix, re-freeze, re-run. |

**Discriminator that distinguishes structural from plant-and-recover:** the load-bearing test is
**STAGE 2 (topological protection)** — invariance under continuous deformation + jump-only-on-
topology-change. Plant-and-recover alone (recovering the planted integer) is NECESSARY but NOT
SUFFICIENT for PASS; it is the known-positive anchor, not the verdict. PASS requires the
deformation-robustness.

**Honest-closure clause (Rule 11):** an ECHO/FAIL is recorded as a clean negative with its failing
condition named; the branch closes with the mechanism. No debug-toward-PASS, no post-hoc bin-dropping
to convert ❌→✅. **Substitution-not-retraction (Rule 12):** if [Q]≡[L] is implicated, the hypothesis
is retracted with a 🔴 header, not silently refilled.

---

## GUARDS (non-negotiable)

1. **VALUE-ECHO IMMUNITY:** read ONLY the integer 𝒬 and its sign. NEVER import or read the dimensionful
   `-e` (`constants.py:100`), `α` (`ALPHA`), or `Q_TANK`. The module asserts `ALPHA`, `Q_TANK`,
   `e_charge` are ABSENT from its globals (import-guard). The integer-ness is the chord; the value `-e`
   is the echo. (`α`-echo keystone, memory `project_alpha_keystone_echo_resolved.md`.)

2. **TWO-3s ORTHOGONALITY** (`master-equation.md:20`, Grant-ratified 2026-06-10): 𝒬 lives in the
   Cosserat **micro-rotation (ω) grade** (T2 couple-stress, the Axiom-1 intrinsic-spin/charge DOF). It
   is **NEVER** wired into the A1 `(V_inc, V_ref)` dilatation-MASS phasor — that is the genesis-24
   double-count (`V_ref` is a read-only projection of the same scalar `V`, not an independent DOF).
   This gate touches ONLY ω.

3. **SELF-FORMATION SEPARATION** (critical): this gate tests STRUCTURAL quantization on a PLANTED
   winding. It does NOT claim the winding self-forms (the genesis/keystone question, which
   LEANS-FALSIFIED — keystone-energize-LOCK). Do NOT conflate; do NOT claim emergence. The result is
   *"IF a (2,3) winding exists, its charge is a topologically-forced integer"*, not *"the electron
   self-forms"*.

4. **PHASE-SPACE-COORDINATE-CHECK** (A46; `def-kn0t01` SOLID): the (2,3) is a PHASE-SPACE winding
   portrait on the Clifford torus. The flux/linking HERE is a REAL-SPACE field-line topology on ω. The
   two coordinate systems are kept distinct. This gate is real-space ω-field linking, NOT a
   phase-space (2,3) measurement.

---

## Substrate-native walk (recorded at freeze)

- **K4 / Cosserat:** uses the existing `CosseratField3D` SO(3) micro-rotation ω-field on the K4 diamond
  lattice and the existing tetrahedral operators (`_tetrahedral_curl` `:514`, `_hopf_density` `:319`,
  `_beltrami_helicity` `:533`). NOT a new solver — a new sibling read-out module that imports them.
- **Op14 / saturation:** N/A — this is a kinematic/static topological read on a planted configuration;
  no saturation/confinement rendering, no Γ wall. 𝒬 is a topological integer of the bare ω field.
- **Phase-space-vs-real-space:** real-space ω field-line linking (GUARD 4); the (2,3) phase-space label
  is kept separate.
- **CP8 (emergence/hosting):** N/A — structural-quantization gate on a PLANTED winding, explicitly NOT
  an emergence/self-formation test (GUARD 3).
- **CP9 (dynamical-vs-heuristic):** honored — the linking integer is a genuine topological observable
  (Gauss linking integral + Chern–Simons Hopf invariant), not an algebraic heuristic standing in for
  topology. The connected-component PROXY it replaces WAS a heuristic; this is the dynamical-grade
  replacement.
- **CP10 (boundary-not-bulk):** honored — 𝒬 is a BOUNDARY observable (no interior sub-cell resolution),
  consistent with the substrate-observability rule.
