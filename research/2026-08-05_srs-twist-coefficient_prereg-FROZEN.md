# PREREG (FROZEN) — the srs compression→twist coefficient and the L–C lockstep

**Date:** 2026-08-05 · **Lane:** implementer (`research/srs-twist-coefficient`) · **SVA pilot case 6**
**Fired by:** Grant ruling 2026-08-05 (`_orchestration/docket-entries/2026-08-05-ruling-squeeze-twist.md`,
on PR #889's branch `orchestration/ruling-squeeze-twist-0805`), verbatim `[sic]`: *"of course, the
squeeze twists, until a point, the twist is how L and C scale uniformly with a relative offset in
the strain regime right?"* → *"1 and 2, go"*.

**This document is FROZEN before any derivation code exists.** It is pushed as its own commit with
nothing else in the tree (the freeze-alone receipt). Bins, gates, predictions and the adjudication
map below are read afterwards exactly as written. UNRUN ≠ PASSED.

---

## §0 — Standard Vacuum Analysis header (SVA v0.1-pilot)

Per [`manuscript/ave-kb/common/standard-vacuum-analysis.md`](../manuscript/ave-kb/common/standard-vacuum-analysis.md)
§0 (PILOT, not canonical; binds lanes the core orchestrator dispatches). Eleven rows: the ten
declarations plus **row 11 numerical conditioning**, added by this lane's dispatch.

```markdown
## §0 — Standard Vacuum Analysis header (SVA v0.1-pilot)
 1. SECTOR / OWNERSHIP:      <which channel owns each observable; cross-wiring check done>
 2. REGIME / PHASE-STATE:    <MODE + REGIME + PHASE-STATE; small- vs large-signal; DC bias point>
 3. CIRCUIT STATEMENT:       <the observable in circuit terms BEFORE any framework word; total-vs-slot>
 4. PLANE & PROJECTION:      <reference plane + series/shunt projection for every Γ or Z claim>
 5. CONSTITUTIVE PROVENANCE: <each grading law: DERIVED | IMPORTED | FORKED(fork-id) | ENG-CHOICE>
 6. ENERGY LEDGER:           <rim (within-system reactive) vs port (boundary-crossing); no loss word without a port>
 7. CALIBRATABILITY:         <is the target a dimensionless ratio or a port phase difference?>
 8. DISCRIMINATION CLASS:    <pure-AC | DC→AC coupling | DC-internal; tautology filter run; SM counterfactual>
 9. CERTIFICATION PLAN:      <gates frozen before numbers; unrun ≠ passed; negative controls named>
10. ADJUDICATION ROUTING:    <which run settles which fork; what propagates on which outcome>
```

**FILLED, row by row:**

**1. SECTOR / OWNERSHIP.** Three observables, three owners, declared before any circuit word and
not cross-wired:

| Observable | Owner (substrate) | Circuit grade | Canon |
|---|---|---|---|
| dilatation strain `ε_sym` | **A1 translational** (3 translational node DOF) | **CAPACITIVE — the C-side** | `translation-circuit.md`:35 *"three translational (E-field origin → capacitive storage)"* |
| micro-rotation `φ` / wryness `κ=∇φ` | **Cosserat micro-rotational** (3 microrotational node DOF) | **INDUCTIVE — the L-side** | `translation-circuit.md`:35 *"three microrotational (B-field origin → inductive flywheel)"* |
| bond couple-stress `γ` | Cosserat, inter-node | mutual-inductance gradient | `translation-circuit.md`:35 |

Cross-wiring check **DONE**: mass = A1 (PR #260/#311) and charge = Cosserat (2,3) winding are
**not** invoked. The "twist" of this lane is the **mechanical micro-rotation coordinate** `φ`, i.e.
the Cosserat rotational DOF of Axiom 1 — it is **NOT** the Cosserat (2,3) winding *charge*, and it
is **NOT** the "T2 bow" mechanical coordinate of the Axiom-4 buckling kernel. The T2-homonym guard
(`axiom-register.md`:193) is read and applied verbatim: *"the 'T2 bow' here is the mechanical bow
COORDINATE of the strut …, NOT the Cosserat (2,3) micro-rotation charge winding."* This lane adds a
third member to that homonym family and keeps it separate: **A1 dilatation (load) → Cosserat φ
(response under test) ⟂ T2 bow (Axiom-4 kernel coordinate) ⟂ (2,3) winding (charge)**.

**2. REGIME / PHASE-STATE.** MODE = **static** (no time stepping, no driven port). REGIME =
**cold linear, sub-yield, saturation OFF** — the same regime line as the parent arcs
(`2026-07-04_srs-elastic-tensor_result.md` § SECTOR HEADER). PHASE-STATE = **unsaturated cold
lattice**, `S(A)=1`. Signal class = **small-signal about the cold bias point**; the DC bias point is
the gravitational A1 grading `ε(r)`, entered here as an *imposed macroscopic strain*, not as a
solved gravity field. **The near-yield large-signal regime is entered ONLY through the canon-forced
swapped-spring composition `ρ_eff = ρ_cold·(S_axial/S_shear)`** (`2026-07-04_matter-stiffening-rho_result.md`,
`2026-07-04_saturated-elastic-tensor_result.md`) — a **cold tensor with per-channel-softened
springs at FIXED geometry**, whose MODEL SCOPE (pre-stress and bias-induced geometry change
OMITTED) is inherited verbatim and is a declared fence on the roll-off deliverable, not a silent
extension.

**3. CIRCUIT STATEMENT (before any framework word; total-vs-slot declared).** The substrate cell is
a two-reactance node: a capacitive branch (translational store, graded by `S_ε`) and an inductive
branch (micro-rotational store, graded by `S_μ`). *"Does the squeeze twist?"* is, in circuit terms:
**when a DC bias loads the capacitive branch, does the SAME bias load the inductive branch?**
The **LOCKSTEP** is the statement that the two branches' fractional reactance changes are equal at
leading order:

$$\frac{\delta L}{L}\Big/\frac{\delta C}{C} = 1 \quad\Longleftrightarrow\quad S_\mu = S_\varepsilon .$$

Both quantities are **TOTAL branch reactances of the cell**, not series slots: `L ∝ μ_eff = μ_0 S_μ`
and `C ∝ ε_eff = ε_0 S_ε` are the *transverse T2* constitutive pair that sets `Z=√(μ/ε)`. **Declared
non-use:** the *other* canon object named "capacitance", the A1 longitudinal bond compliance
`C_eff = C_0/S` (INVARIANT-S2 sector split), is **NOT** the C of this ratio — identifying them is
the genesis-24 double-count and is refused here by declaration.

**4. PLANE & PROJECTION.** The only Γ this lane touches is `Γ_EM`, at the **cell-boundary reference
plane** of the graded medium (the same plane the engine's `Γ ≈ ¼[∇S_μ/S_μ − ∇S_ε/S_ε]` uses,
`cosserat_field_3d.py`:590-605). Projection: **shunt-graded** (the grading is a bulk constitutive
modulation of the medium, not a series discontinuity). **This lane computes NO Γ number** — it
computes the *input* to Γ (the `S_μ`-vs-`S_ε` loading ratio) and reports Γ only as the frozen
`S_μ = S_ε ⇒ Γ_EM = 0` implication already in the engine. No signed Γ claim is minted.

**5. CONSTITUTIVE PROVENANCE.** Every constant, tagged:

| Input | Value | Provenance |
|---|---|---|
| carrier net | srs-z3, `I4₁32` Wyckoff-8a, both enantiomorphs | **DERIVED** — Axiom 1 object; **D1 RATIFIED** (Grant 2026-07-03, `_orchestration/index.md`:185); handedness convention `chiral_lattice.py`:45 *"Native = right-handed enantiomorph"*, `srs_motif('left')` = `I4₃32` mirror `x→−x` (`chiral_lattice.py`:66-72) |
| bond model | Born `Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)` | **DERIVED-as-engine-native** (Stage-1 `srs_elastic_tensor.py`; the FLAG-4 absolute-frame-rotation objection at `2026-08-02-biased-tensor-scoping.md`:8 is inherited OPEN and gated by G3) |
| lever arm | `lever = 1` (bond-midpoint attachment) | **DERIVED (geometry-fixed)** — `micropolar_bloch.py`:77-87; Poisson-disk `r_node=ℓ_node`, NN bond `=ℓ_node` |
| couple-stress | `γ = 6·k_s` | **IMPORTED-from-canon** — `ℓ_c²=γ/G=6`, `ℓ_c=√6·ℓ_node` at `constants.py`:**338** (`ELL_C: float = np.sqrt(6.0) * L_NODE`). ⚑ **STALE-CITE FLAG (surfaced, not fixed):** `research/2026-07-04_srs-chiral-micropolar_result.md`:93 cites this as `constants.py:298`; line 298 at HEAD is inside the **`OMEGA_C`** comment block and carries no `ℓ_c` content. Pure line-drift class; the source result doc is a frozen record and is **not edited by this lane** |
| stiffness ratio | `ρ_bond = k_a/k_s = 1` primary; `ρ=9.7734` reported alongside | `ρ=1` **DERIVED** (Ax-3 match point, `clm-mfb2ax`, `parent-condition-match-forces-balance.md`); `ρ*=9.7734` **GR-IMPORTED** (K=2G, PR #506/#261) |
| `ε_yield`, `ω_yield` | **NO canonical value** | ⚑ **CANON-ABSENT.** `ω_yield` has **no `constants.py` symbol and no KB home** (two-method receipt in §5). Engine literals disagree: `1.0` (`lattice_decoration_discriminator.py`:113) vs `π` (`rrad_l_counterprop_chiral.py`:144). **Consequence, declared in advance:** the *dimensionless* leak ratio is derivable; its *absolute* value is normalization-gated, and any absolute claim would be UNDERDETERMINED |

**6. ENERGY LEDGER.** Entirely **RIM**. This is a lossless static elastic-energy minimization on a
closed periodic cell: no port, no radiation, no detector, no topology change. Every energy quantity
is reactive storage redistributed among branches. **No "loss", "dissipated" or "damping" word appears
in this lane's result** — if the derivation needs one, that is a STOP-and-flag, not a fix.

**7. CALIBRATABILITY.** The two headline targets are **dimensionless ratios**:
(i) `τ ≡ φ̄/ε` — net micro-rotation per unit strain, **radians per unit strain** (dimensionless);
(ii) `c_twist ≡ lim_{q→0} (κ/ε)/q` — dimensionless; and
(iii) the lockstep ratio `(δL/L)/(δC/C)` — dimensionless by construction.
No CODATA, no SI substitution, no α on any verdict path. **α-CLEAN by construction** (the whole
computation is in units of `k_s` and `a_cell`; `ℓ_node` enters only when converting `c_twist` into
the `A_μ/A_ε` budget ratio, and that conversion is reported as a separate, explicitly-normalized
line — never folded into the coefficient).

**8. DISCRIMINATION CLASS.** **DC-internal.** The object is a property of the substrate's static
constitutive response; nothing here is measured at a port. It becomes DC→AC coupling only via the
downstream `Γ_EM`-in-a-gravitational-gradient statement, which this lane does **not** headline.
**Tautology filter, run in advance:** the risk is that "compression twists a chiral lattice" is the
known chiral-metamaterial phenomenon restated. It is — at the *existence* level (bench anchor
below). What is NOT a restatement, and is what this lane computes, is the **coefficient's size, its
k-order, and whether it is large enough to co-load the μ budget**. **SM counterfactual:** classical
Cauchy elasticity (the SM-equivalent default here) forbids a homogeneous compression→rotation
coupling in ANY medium, because `C_ijkl` is inversion-even; a micropolar continuum with a chiral
point group permits it. So a **nonzero** result is carrier-distinct; a **zero** result is the
Cauchy default and buys nothing.

**9. CERTIFICATION PLAN.** Gates G1–G8 (§4) frozen below with pass/fail thresholds and named
negative controls (the achiral **diamond-z4 instrument** as the symmetry null, and the **purely
central `k_s=0`** model as the mechanism null). Bins (§6) frozen. **UNRUN ≠ PASSED**: every gate is
reported with its literal state, and a gate not run is reported as `UNRUN`, never folded into a
pass. **No number of any kind has been computed at freeze time** — §3.4's rank-2 independence argument
is ANALYTIC (derived from a canon quote) and is turned into gate **G7**, which runs after freeze.

**10. ADJUDICATION ROUTING.** §6 maps each frozen bin to exactly what it settles and what it does
NOT license. **Nothing propagates from this lane**: no manuscript edit, no KB edit, no `src/ave/`
edit, no claim-id minted, no solidity moved. Canonical propagation (wall-taxonomy §10, the
SYM-mechanism cross-refs, the FLAG-CANON repair, the ch15 fourth-channel row) is **GATED** on
Tier-2 review + Grant, per the dispatching ruling.

**11. NUMERICAL CONDITIONING** *(row added by this lane's dispatch; not in the v0.1-pilot ten).*
The static solve is a linear system on the internal DOFs at fixed macroscopic load. Declared in
advance: (a) the internal Hessian is **rank-deficient by exactly 3** (uniform translations) and the
solve is done on the **orthogonal complement**, never by naive inversion; (b) the **condition
number** of the reduced Hessian is reported for every configuration; (c) at the ratified `ρ_bond=1`
the **bulk modulus is `K<0`** (`parent-condition-match-forces-balance.md`:71,74 — the Ax-3
zero-reflection point is *"NOT a stable static elastic solid"*), so the reduced Hessian may be
**indefinite**; this is a KNOWN canon state, is reported as an eigenvalue receipt, and the ρ-family
is run so no conclusion rests on `ρ=1` alone; (d) every headline number is recomputed at
**`mpmath` ≥ 50 dps** and the float64-vs-mp deviation reported; (e) the **regex engine** used for
every scan/absence claim in this lane is named at each use (Python `re`, POSIX ERE via `grep -E`,
and Perl-compat via `grep -P` where available) — no absence claim rests on one engine.

---

## §1 — The question, stated so it can come back negative

Grant's picture: a squeeze on a chiral lattice **twists** it, and the twist is how the L branch
takes its share of the squeeze — so L and C scale together (lockstep) *until a point*, near yield,
where a relative offset opens. The ruling promotes this to: *the DC bias is two-component,*
`ε₁₁(r)` *plus a* `κ(r)` *profile riding it, so both kernel budgets load under a "pure" squeeze.*

The falsifiable content is a **number**: the micro-rotation induced per unit compressive strain by
the srs carrier's chirality, at cold linear order, with its sign tied to handedness. If that number
is zero, or is suppressed by a factor that makes the μ budget's loading negligible against the ε
budget's, the walk is wrong and this lane says so plainly.

## §2 — Bench anchor (retrieval-pointer class; NO values imported)

Chiral mechanical metamaterials that convert axial compression to twist are an established
experimental class (Frenzel–Kadic–Wegener 2017; acoustical activity measured 2019 — both already in
the corpus at `physics-lineage-map.md`:338,347). **Cited for the EXISTENCE of the phenomenon and
for nothing else.** No coefficient, no scaling law, no sign convention and no magnitude is taken
from that literature; every number in this lane comes from the canon lattice. The corpus's own
lineage note also carries the standing caveat that bench-scale mechanical couple-stress signatures
are hopeless in AVE's parameter regime (`physics-lineage-map.md`:347) — that caveat is inherited,
not re-litigated.

---

## §3 — Method (frozen before code)

### §3.1 What is computed, and in what coordinates

**Static unit-cell lattice mechanics on the D1-ratified chiral srs-z3 carrier under periodic
boundary conditions — a DIRECT STIFFNESS computation.** Per node, 6 DOF `q_n = (u_n, φ_n)`, per
Axiom 1. Per undirected bond `(i,j,d)` the energy is the engine-native micropolar bond form already
certified in `src/ave/core/micropolar_bloch.py` §1:

```
U_bond = ½ Δ·Φ_b·Δ  +  ½ γ |φ_j − φ_i|²
Δ      = (u_j + φ_j × b_j) − (u_i + φ_i × b_i),   b_i = +½·lever·d,  b_j = −½·lever·d
Φ_b    = k_a·d̂⊗d̂ + k_s·(I − d̂⊗d̂)
```

**Rule-14 anti-rebuild: the bond block is IMPORTED from `micropolar_bloch.bond_6dof_block`, not
reimplemented.** What this lane adds is a **static** load path that module does not have.

**A46 coordinate declaration:** real-space / spatial-Brillouin throughout. The claim under test
(*"the squeeze twists"*) is a real-space mechanical statement about a real-space lattice; the
readouts (`φ̄/ε`, `κ/ε`) are real-space. **Coordinates match.** No phase-space (`V_inc`/`V_ref`,
Clifford-torus) quantity appears, and none is compared against.

### §3.2 Load path A — the k=0 affine squeeze (the primary object)

Impose a macroscopic displacement gradient `H`; carry it affinely and relax the cell-periodic
internal fields:

```
u_n = H·r_n + ũ_n ,      φ_n = φ̃_n           (ũ, φ̃ cell-periodic, unknown)
minimise  E(H; ũ, φ̃)  over (ũ, φ̃),  with the 3 uniform-ũ translations projected out
```

Two loads, both **compressive**, per the dispatch:
- **A-ISO:** `H = −ε I` (isotropic / hydrostatic squeeze), `ε > 0`.
- **A-UNI:** `H = −ε ẑ⊗ẑ` (uniaxial-radial squeeze along `[001]`), and the same along `[111]`.

**Readouts.** (i) the **net micro-rotation** `φ̄ ≡ N⁻¹ Σ_n φ̃_n` and the **twist coefficient**
`τ ≡ |φ̄|/ε` with its sign along the load axis; (ii) the **staggered / internal-only** rotation
`τ_rms ≡ rms_n|φ̃_n|/ε` (a nonzero `τ_rms` with `τ=0` is an internal-strain pattern, NOT a
macroscopic twist — the two are reported separately and never summed); (iii) the induced internal
displacement's antisymmetric part.

### §3.3 Load path B — the gradient (finite-`q`) squeeze

Because a *uniform* wryness is not a homogeneous bulk state (a uniform `κ` carries a
position-growing micropolar strain), the wryness channel is loaded the only way it can be: with a
**gradient**. Bloch-phased direct stiffness on the same 8-node cell, `K(q)` complex `48×48`:

```
clamp   the uniform-translation-along-q̂ amplitude A   (this IS the macroscopic longitudinal strain, ε = i q A)
solve   K_ff(q) ψ_f = − K_fd(q) A                      (all other DOF free)
read    Φ  = the uniform-micro-rotation-about-q̂ component of ψ_f
report  κ/ε = Φ/A   and   c_twist(q) ≡ (κ/ε)/q         (dimensionless)
```

`q` swept over ≥ 6 decades toward `q→0` along `[001]`, `[111]`, `[110]`; the leading power of `q` in
`κ/ε` is **fitted, not assumed**, and reported as the twist law.

### §3.4 Independence from the rank-2 srs bond-tensor blocker (ANALYTIC at freeze; gated by G7)

PR #884's disclosed pre-reg deviation reads, verbatim: *"the srs re-run is **BLOCKED-STRUCTURAL**,
blocker measured: every srs site's bond tensor is rank 2, spectrum {0, 1.5, 1.5}."* (PR #884 body;
the PR's numbered **FLAG-3** is a different item — *"the canonical Cosserat operator runs on the z=4
diamond CONTROL net … not the D1-ratified srs-z3 carrier"* — and the dispatch brief's phrase
"PR #884's FLAG-3" is read here as **the rank-2 blocker item**, with the numbering discrepancy
flagged, not silently reconciled.)

**Why it does not apply to a direct stiffness assembly, stated as a checkable claim, not an
assertion.** The rank-2 object is the *site-summed central-force* tensor `Σ_b d̂_b⊗d̂_b`, which for
the srs trivalent star is `(3/2)(I − n̂⊗n̂)` because the three bonds at an srs node are **coplanar**
(`2026-07-04_srs-chiral-micropolar_result.md` §3: *"the single srs node … is COPLANAR (det of the
3 bond directions = 0 exactly)"*). It is rank 2 **only for the purely central model** `k_s = 0`.
The engine-native Born bond tensor carries the non-central `k_s` term, so the site sum is
`(3/2)k_a(I−n̂n̂) + k_s(3n̂n̂ + (3/2)(I−n̂n̂))`, full rank for `k_s > 0`. **G7 turns this into a
gate**: it (a) reproduces the `{0, 1.5, 1.5}` spectrum literally, and (b) asserts the *global*
reduced stiffness has exactly the expected nullity — the property the direct solve actually needs.
**If G7(b) fails, this lane STOPS and flags; it does not switch nets, does not switch bond models,
and does not fall back on the diamond instrument.**

### §3.5 Handedness

Every readout is computed on **both** enantiomorphs via `chiral_lattice.srs_motif('right'|'left')`
(`I4₁32` / `I4₃32`, `chiral_lattice.py`:45,63-75). **Frozen falsifier:** any nonzero twist
coefficient MUST flip sign exactly; any parity-even quantity (moduli, condition numbers) MUST
match. **A twist coefficient that does not flip sign with handedness is a FINDING, reported as
such** (it would mean the measured rotation is not sourced by chirality) — not debugged into
flipping.

### §3.6 The roll-off toward yield

Entered only through the canon-forced swapped-spring composition
`ρ_eff = ρ_cold·(S_axial/S_shear)` with `ρ_cold = 1` (`2026-07-04_matter-stiffening-rho_result.md`;
`2026-07-04_saturated-elastic-tensor_result.md`), sweeping the wall amplitude `A → 1`. The
**inherited MODEL SCOPE fence** is carried verbatim: *initial/residual (pre-)stress from bias
pre-loading and bias-induced geometry change are OMITTED and remain OPEN*. Consequence declared in
advance: **if the cold twist coefficient is zero by symmetry, it is zero at every `ρ`, hence at
every `A` in this model, and the roll-off deliverable degenerates** — that degeneracy is a result to
report, not a gap to paper over with a different model.

---

## §4 — Gates (FROZEN; UNRUN ≠ PASSED)

| # | Gate | Threshold | Kind |
|---|---|---|---|
| **G1** | Carrier + bond-list rebuild reproduces `chiral_lattice.build_srs_net` adjacency: 8 nodes, degree 3, girth 10, NN bond `√2/4` cell units | exact / `<1e-12` | regression |
| **G2** | **Stage-1 regression.** With `lever=0, γ=0, φ` clamped, the u-block long-wave `C_ij` reproduce `2026-07-04_srs-elastic-tensor_result.md` (`C11=0.72786, C44=0.24876` at `ρ*=9.7734`) | `<1e-6` relative | regression on a certified predecessor |
| **G3** | **Objectivity.** The global rigid mode `(u_n = θ×r_n, φ_n = θ)` is an exact zero mode at `lever=1`; and is NOT at `lever≠1` | `E < 1e-20` at `lever=1`; `E>0` otherwise | physics correctness — this is the FLAG-4 absolute-frame-rotation objection turned into a gate |
| **G4** | **Rotational gap.** State whether a uniform `φ` with `u=0` is a zero mode of the `k=0` stiffness. Reported as a literal number either way | report `E_uniform-φ`; declare GAPPED or GAPLESS | instrument characterization; **either outcome is a pass**, and a GAPPED outcome contradicts the docstring of `micropolar_bloch._acoustic_rotational_subspaces` and is FLAGGED, not fixed |
| **G5** | **Achiral null control.** Diamond-z4 instrument: `τ` and `c_twist` identically zero | `<1e-12` | negative control (symmetry) |
| **G6** | **Mechanism null control.** Purely central `k_s=0`: chiral coupling vanishes (no transverse force ⇒ no moment arm) | `<1e-12` | negative control (mechanism) |
| **G7** | (a) srs site central tensor spectrum = `{0, 1.5, 1.5}`; (b) reduced internal stiffness nullity = **3** (uniform translations only) at `lever=1, γ=6k_s, k_s>0` | (a) `<1e-12`; (b) exact | **feasibility / STOP-gate** — (b) failing halts the lane |
| **G8** | **Conditioning.** `cond(K_red)` reported for every configuration; every headline number recomputed at `mpmath ≥ 50 dps`; float64-vs-mp deviation reported; deterministic double-run digest identical | digest byte-identical; deviation reported (no threshold — it is a receipt) | conditioning receipt (Rule 10) |

**Negative-control ordering (frozen):** G5 and G6 are run and reported **before** any srs number is
read.

---

## §5 — Absence / completeness claims and their two-method receipts

Every absence claim this lane makes is backed by **two independent scans with the regex engine
named**. Pre-declared list:

1. **`ω_yield` has no canonical value.** Method 1: Python `re` walk of `src/ave/core/constants.py`
   for `(?i)omega_?yield`. Method 2: `grep -REn 'omega_?yield|ω_yield' manuscript/ave-kb src/ave/core/constants.py`
   (POSIX ERE). Both reported with hit counts and the disagreeing engine literals.
2. **No prior corpus computation of a k=0 compression→twist coefficient on srs.** Method 1:
   `grep -REn 'compression.?twist|twist.per.strain|squeeze.*twist'` over `manuscript/ research/ _orchestration/`.
   Method 2: Python `re` walk over the same trees with `re.IGNORECASE` and a widened alternation.
   Known prior art that IS found is cited, not re-derived: `clm-acgyr1`
   (`chiral-mechanical-gyrotropy.md`) and the two 2026-07-04 srs elastic-tensor arcs.

---

## §6 — Frozen bins and adjudication routing

The bins are the dispatching ruling's, verbatim in intent, with the operational test for each
stated **now**:

| Bin | Fires when | What it settles | What it does NOT license |
|---|---|---|---|
| **LOCKSTEP-EXACT** | `(δL/L)/(δC/C) = 1` to the numerical floor, forced by geometry, at k=0 | canon's SYM gravity class becomes a **theorem of the carrier's chirality** | still no VALUE derivation; still no headline without Tier-2 |
| **LOCKSTEP-APPROX** | ratio ≠ 1 by a **named and sized** residual | a residual `Γ_EM ≠ 0` in gravitational gradients exists with a derivable size — **DISCRIMINATOR-CLASS** | ⚠ **fenced per mechanism-claims discipline; headline NOTHING.** Report the size, route it, do not surface it as a prediction from a first lane |
| **NO-TWIST** | `τ = 0` at the numerical floor and the gradient channel too small to load the μ budget | the chirality does not couple compression to rotation **at the order the ruling needs** — the walk is falsified honestly and reported plainly | does NOT falsify canon's SYM class (which rests on a *different*, source-side mechanism); does NOT retract `clm-acgyr1` |
| **ROLL-OFF-EARLY** | a nonzero twist that saturates **before** strain yield | the lockstep's break point, with `S_κ(wall)` reported | nothing about the cold-regime lockstep |
| **UNDERDETERMINED** | canon lacks a needed constitutive input | the exact missing inputs, enumerated | no verdict on the physics |

**Compound bins are allowed** (e.g. NO-TWIST at k=0 compounded with a sized gradient residual);
inventing a *new* bin post-result is not.

**Routing.** Whatever fires: this lane writes `research/2026-08-05_srs-twist-coefficient_result.md`
and `_orchestration/docket-entries/2026-08-05-srs-twist-coefficient.md`, and **nothing else**. The
relationship to `axiom-register.md`:189 (the load-response-bifurcation wording) and to the
FLAG-COMBINE-SPLIT counter-receipts (`trampoline-framework.md`:255, `axiom-register.md`:232) is
stated as a **RELATIONSHIP ONLY** — no leaf edited, no reconciliation text minted, no claim-id
touched.

## §7 — Pre-registered predictions (so the result can contradict me)

Stated before any code runs, with reasoning, so that a wrong prediction is visible:

- **P1.** `τ = 0` **exactly** for A-ISO. Reason: the srs nodes occupy Wyckoff **8a of `I4₁32`, a
  fixed special position with ZERO free positional parameters**, so a symmetry-preserving load
  admits no internal relaxation at all.
- **P2.** `τ = 0` **exactly** for A-UNI as well. Reason: a uniform micro-rotation induced by a
  homogeneous strain would require a non-vanishing **rank-3 axial** coupling tensor `d_ijk ε_ij φ_k`.
  Point group **432 is the one non-centrosymmetric class that is NOT piezoelectric**, and because
  432 contains only proper rotations, its axial rank-3 tensor vanishes with its polar one.
- **P3.** `τ_rms ≠ 0` for A-UNI (internal-strain relaxation exists once the load lowers the
  symmetry) but `τ_rms = 0` for A-ISO (P1).
- **P4.** `c_twist ≠ 0`, parity-odd, diamond-null — i.e. the chirality DOES show up, but at
  **`O(q)`**: `κ/ε ∝ q`. This is the same object canon already carries as `clm-acgyr1`.
- **P5.** Therefore `A_μ/A_ε ∝ (q ℓ_node)` and the lockstep **fails by orders of magnitude** for any
  gravitational gradient scale, i.e. **`S_κ(wall) → 1`** (the μ branch does not collapse with the ε
  branch). Expected bin: **NO-TWIST**, compounded with a sized `O(q)` residual.
- **P6.** G4 returns **GAPPED** (uniform micro-rotation costs energy at `lever=1`), contradicting
  the `micropolar_bloch._acoustic_rotational_subspaces` docstring claim that it is *"an exact
  zero-eigenvector of Phi0"*. If so, that is a **FLAG** on a merged, canonized result, surfaced
  with both file:line and verbatim content, and **not fixed here**.

**If P1–P6 are wrong, the result doc says so in the first paragraph.**

