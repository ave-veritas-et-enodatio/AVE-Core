# WALK RECORD — the G2 walk: scaffold-as-gradient, the √2 fork, the electron's boundary, and what g = 2 actually costs (2026-08-25)

**Status: WALK-GRADE except where a receipt is quoted.** Dated record of the
2026-08-25 adjudication walk. Two of Grant's answers are RULINGS (recorded as
such); the rest are physical pictures and CANDIDATES, each tagged. The
6-question sweep gate has NOT run on any candidate here. Mints no `clm-`, no
`def-`, moves no solidity.

**Grant's questions, verbatim:**
- *"A1. how does this map to the gradient needed for making the boundary
  project?"*
- *"A2: include"* — **RULING**
- *"A3. give me the physical picture here"*
- *"B1. i need a physical picture here. what type of wave would the boundary of
  the electron live within, longitudinal? and whats the transduction of that
  from transverse em waves"*
- *"B2: reopen"* — **RULING**
- *"B3. what does the behavioral empirical observations of the electron tell
  us?"*
- *"B4. what makes most sense?"*
- *"what is so unique about the electron being the lightest fundamentally
  charged particle and how does that plan into this effort think critically
  through what g=2 means physically for what we are trying to show"*

---

## §1 — A1: the scaffold IS a gradient specification [WALK]

A **uniform** boundary specification is gauge — by the relational-cancellation
identity (`clm-relcnc`, PR #1014) it projects nothing and the interior cannot
detect it. A scaffold does work only by imposing a **differential**: a phase
gradient across the boundary ports.

**The winding is exactly that and nothing more.** A (2,3) specification is a
statement of *relative* phase advance around a loop. Its common-mode part is
the tube phase ϖ — which epic guard 8 forbids imposing.

| scaffold | what it imposes | guard-8 status |
|---|---|---|
| source-terminated | absolute port phasors = differential **+** common mode | imposes ϖ unless explicitly quotiented |
| injection-lock | relative phase only | **imposes only the differential, by construction** |

**Orchestrator recommendation (revised at this walk; the earlier lean was
source-terminated alone):** solve **source-terminated with the common mode
explicitly projected out**, injection-lock as the physics-honest cross-check —
and make the projection itself a receipt: *if projecting out the common mode
changes the solution, the scaffold was doing illegitimate work.*

**The source-idle criterion in this frame:** at the solution the scaffold's
*differential* drive → 0, i.e. **the state's own gradient has become the source
of its boundary projection.** That is the self-clamp stated in one sentence.

## §2 — A3: the √2 envelope fork, physically [WALK + a CANDIDATE]

The two canon forms differ by **what is counted**:

- **C-state** (DP-1 K4-V projection): `A² = Σ_ports V_inc²/V_SNAP²` — how hard
  the incident waves drive the port.
- **Full tank** (DP-3 R2-fix): `A² = (V_inc² + Φ²/LC)/V_SNAP²` — the total
  stored LC energy, electric plus magnetic.

For a standing wave the identity `|v_f+v_b|² + |v_f−v_b|² ≡ 2(|v_f|²+|v_b|²)`
makes stored energy exactly twice the incident-only reckoning — **√2 in
amplitude**. Plainly: **counting the waves that hit vs counting the energy
that is stored.**

**Which does the kernel want?** `S(A) = √(1−A²)` measures how close the medium
is to yield, and yield is a property of the medium's *state* (its strain), not
of the flux arriving at a port — which argues for the full-tank form. Against
it: DP-1's C-state row is what canon writes for the K4-V sector, and the
electron's operating point `A=√α` was computed in *some* convention.

**★ CANDIDATE — the two forks may be ONE fork [WALK, computable, un-run].**
If `A_full = √2·A_C` then `A²` doubles — and canon already carries two criteria
exactly a factor of 2 apart in `A²`: the **storage-α** criterion (`A² = α`,
`|Γ| = √(1−α) = 0.996345`) and the **response-α knee** (`A² = 2α`,
`(1−2α)^{1/4} = 0.996331`), which canon's own Ruling-12 contour tag flags as
*"near-colliding, Δ = 1.4×10⁻⁵ … two readings of one kernel one Taylor order
apart"* (`cvr-reflection-smith.md`:49-55). **The check:** express both criteria
in both envelope conventions and see whether they map onto each other. If they
do, ruling the envelope fork rules the contour fork too. *A factor-of-2-in-A²
coincidence between two independently-recorded forks is exactly the
identity-collapse tell AND exactly the shape of a coincidence — hence
CANDIDATE, and hence cheap to settle before ruling.*

## §3 — B1: the electron's boundary, and the transduction [WALK + a CANDIDATE resolution]

**The wall is transverse; what it confines is longitudinal.** `def-vyvsn1`
(SOLID): `V_yield` is the **transverse-T2 self-trap wall**; the A1 core operates
sub-saturated at `A=√α`, `S≈0.996`, inside it. So the electron is **a
longitudinal compression resonator inside a mirror made of transverse
saturation** — trapped acoustic-like compression energy (that is `m_ec²`)
bouncing off walls made of micro-rotation saturation.

**The transduction from transverse EM is PARAMETRIC, not mode conversion.**
Op14 couples the sectors through the shared saturation state
(`A²_total = A²_V + A²_ω`): an incident transverse field raises the ω-sector
amplitude → raises total saturation → lowers `S` → changes the **longitudinal**
impedance `Z = Z₀√S`. **Transverse field = the bias; longitudinal wave = the
signal; the kernel = the varactor.** (This is why the EE register keeps being
the right language: the object is literally a varactor-modulated tank.)

**★ CANDIDATE resolution of the INVARIANT-S2 / master-equation split
[WALK — proposed, not ruled; the adjudication is Grant's, open item
`2026-08-25-invariant-s2-sector-split.md`].** Canon carries two saturation
branches with opposite boundary phase:

- **magnetic-first** (`μ_eff→0`): a transverse wave sees `Z=√(μ_eff/ε₀)→0` →
  **short, Γ=−1**
- **electric-first** (`ε_eff→0`): a transverse wave sees `Z=√(μ₀/ε_eff)→∞` →
  **open, Γ=+1**

while the **A1 longitudinal tank shorts in BOTH** cases, because
`C_eff = C₀/S → ∞` whenever `S→0` regardless of which constitutive parameter
drove it. **Proposed reading: INVARIANT-S2's "A1 shorts / T2 opens" is the
electric-first branch; master-equation's μ-first Γ=−1 is the magnetic-first
branch, where T2 also shorts. Both are transverse-wave statements differing by
BRANCH, not by sector; A1 shorts either way.**

**The check this proposes (cheap, un-run):** the longitudinal channel should
behave the SAME under both loadings while the transverse channel mirrors —
which is the shape Stage 1 measured on the transverse side (mirror-antisymmetric
to 0.45%, PR #1012). The longitudinal half is unrun.

**★ A striking reading, flagged not asserted [WALK].** PR#260 ruled the μ-vs-ε
fork is the **spin sign-selector** (*"μ-first ⇒ Γ=−1 vs ε-first ⇒ Γ=+1 are the
spin-conjugate signs"*), degenerate on equilibrium observables. If that holds,
**Stage 1 measured the two spin-conjugate boundary conditions**, and the mirror
antisymmetry is spin conjugacy at response-map level. **This owes a
discrimination check before it is anything:** is that content, or the |Γ|=1
degeneracy restated? Any real content lives in the 0.45% *departure* from
perfect antisymmetry, not in the antisymmetry itself.

## §4 — B3: what the electron's measured behaviour constrains [WALK, on external data]

1. **No structure to ~10⁻¹⁸ m** — five orders BELOW `ℓ_node` (= the reduced
   Compton wavelength, 3.9×10⁻¹³ m). Any real-space impedance profile — step or
   taper — must be invisible to probes far finer than the node scale. The
   framework's answer is the phase-space/real-space carve (structure in phase
   space; real-space body is the `0₁` unknot) — consistent, but it means the
   J/B/taper question, being about a real-space grading profile, inherits this
   constraint directly.
2. **g = 2 exactly (leading)** — the sharpest: it says charge and mass are not
   measurably separated. Any boundary assignment that spatially divorces the T2
   winding from the A1 core must answer why g does not move.
3. **Absolute stability, with `|Γ|² = 1−α` leaking at the wall** — not a
   contradiction: the leak is the radiative coupling (the electron radiates when
   accelerated), not a decay channel. The Link cannot unwind and nothing lighter
   carries it.

**Net for the J/B/taper fork:** the empirical record does not discriminate J vs
B (both are phase-space-side constructions) but imposes a hard downstream
constraint — *whatever the answer, it must not move g off 2 and must not print a
real-space form factor.*

## §5 — B4: the two small dispositions [orchestrator recommendations; Grant's call]

- **Frozen Class-C driver wrap blind-spot → dated surface note on the frozen
  file.** Frozen-text discipline says dated note, never rewrite; and "leave the
  PR record as the pointer" fails read-don't-grep — a future auditor greps the
  driver, not the PR archive.
- **B(M) glyph → rename now**, by the same reasoning that carried ϖ (cheapest
  before consumers accumulate; B is the most sector-loaded glyph in the corpus —
  it *is* the A1⊥T2 fence). Method: the ϖ derivation lane (reserved-glyph map →
  notation-derived candidates → double sweep with independently-constructed
  patterns → Grant picks).

## §6 — ★ THE CAPSTONE: g = 2, and an orchestrator error caught by grepping first

**THE ERROR, RECORDED.** The orchestrator was about to hand Grant the reading
*"g=2 is the winding-2 / SU(2) double cover"* as the walk's punchline. **Canon
retracted exactly that argument.** `electron-identification.md`:92 (Rule-12
re-scope, 2026-06-21), verbatim: the prior status *"✅ axiom-derived | ratio
falls out of the double-cover structure"* was **"a non-sequitur"** and is
retracted, with a **decisive falsifier**: *"the proton (g_p ≈ 5.586) and neutron
(g_n ≈ −3.826) are also spin-½ and also carry the same 4π double-cover — yet
g ≠ 2. A ratio that equals 2 for every spin-½ particle cannot select g = 2 for
the electron."* Canon's honest line (`translation-circuit.md`:637): **"g = 2 is
POSITED, not derived."** The error was caught by grepping canon before
asserting — the core-canon-collision discipline firing as designed, on the
orchestrator.

**What the falsifier teaches (the shape a real derivation must have).** g=2
cannot come from spin-½ topology, because every spin-½ object has it. It must
come from what the electron has and the proton does not: **the proton is
composite, with charge and mass distributions that differ.** Classically that is
the entire content of g — the ratio of how charge is distributed to how mass is
distributed.

**Therefore g = 2 is a statement about the A1↔T2 relationship.** The magnetic
moment comes from the T2 winding; the angular momentum from the Cosserat
microrotation (Axiom 1: the microrotational DOF *is* the substrate-native origin
of intrinsic spin); the mass in the denominator is A1. **g is a cross-sector
ratio whose value is fixed by how the solved state distributes those two
sectors** — which is precisely what the static-existence solve computes.

**★ THE CONSEQUENCE FOR THE EFFORT (the walk's operative output):**

> **If the harmonic-balance solve produces a self-consistent railed-core state
> carrying Link = 1, then μ and S are computable from that solution — and g
> falls out as an OUTPUT. Not an input, not a posit: a prediction.**

Three reasons it is the right verdict observable:

1. **It is currently POSITED.** Deriving it would move a genuinely unearned
   number to earned — one of very few electron observables that is not
   calibration (`m_e`), definitional (Compton), or echo (α).
2. **It is a pure dimensionless ratio — immune to every normalization fork.**
   By `clm-relcnc`, a ratio taken against a co-transforming reference cannot be
   moved by the √2 envelope choice, the R1/R2 convention, or the yield
   normalization. **g = 2 is the one verdict criterion that cannot be argued
   into or out of by convention.**
3. **It is a kill either way.** g≠2 from a converged solve falsifies the
   identification (or the imposition, or the machinery) — and *how* it misses
   says which.

**The lightest-charged-particle fact = the uniqueness handle.** The electron is
stable because it is the lightest thing carrying the Link — charge conservation,
nothing dynamical. So it is **the ground state of the Link=1 sector**: the
minimum-energy self-consistent state carrying one unit of winding. Canon puts
its A1 core at `A=√α≈0.085`, `S≈0.996` — **the least-strained charged state the
vacuum admits**, barely perturbing the medium; that is *why* it is light. Two
consequences for the solve: (i) if harmonic balance finds a FAMILY of Link=1
solutions, the electron is the lightest member — a selection criterion the solve
can apply itself; (ii) the heavier charged leptons should sit at deeper `A` on
the same ladder — **the mass hierarchy as a saturation-depth ladder** [WALK,
un-checked, and the kind of claim that owes a discrimination check before it
travels].

**Status of the anomalous part, stated so it is not over-read.** `a_e = α/2π`
has a claimed substrate derivation (`preferred-frame-and-emergent-lorentz.md`:131
— Axiom-4 saturation back-reaction + a `1/π²` spin-orbit projection) **and** a
canon flag that the 50 ppm closure is *"postulate-dependent (n_q-additivity =
1-point fit, not derivable)"* (`translation-circuit.md`:529). **Contested/partial
— nothing in this walk builds on it.** The adjacency between the wall's `α` leak
(`|Γ|²=1−α`) and the anomaly's `α` is NOT asserted here: the coefficient `1/2π`
would have to come from somewhere structural, and "α appears in both" is the
echo pattern, not a mechanism.

## §7 — Routing (every item from this walk, with its durable home)

| item | disposition | home |
|---|---|---|
| A2 — projected M/Q on two representatives | **RULED: include** | `open-items/2026-08-25-g2-freeze-decisions.md` |
| B2 — the ℂP¹ Smith-chart park | **RULED: reopen** | `open-items/2026-08-18-smith-chart-cp1-canonization.md` (status flipped) |
| A1 — scaffold form | Grant-pending, recommendation revised (§1) | G2 item, decision 1 |
| A3 — envelope fork + the collapse candidate | Grant-pending; **HOLD until the collapse check runs** | G2 item, decision 3 + its gating sub-task |
| **g as a frozen verdict observable** | orchestrator recommendation, NEW (§6) | G2 item, decision 4 |
| B1 — the sector split | Grant adjudication; candidate resolution + the longitudinal check | `open-items/2026-08-25-invariant-s2-sector-split.md` |
| the spin-conjugate reading of Stage-1's mirror | WALK; owes a discrimination check | same item, §"flagged not asserted" |
| B3 — the empirical constraints | recorded as constraints on the fork | this record §4; consumed by the J/B/taper item |
| B4 — frozen-driver note / B(M) rename | recommendations, Grant's call | this record §5; B(M) in `2026-08-24-axiom5-b-glyph.md` |
| the g=2 retraction finding | recorded (§6) | this record; consumed by the G2 item's decision 4 |

---

## §8 — Grant's boundary/Pauli description, checked against canon (2026-08-25, same walk)

**Grant, verbatim:** *"a physical boundary is implied to be impossible by what
ave predicts. the pauli exclusion principle would manifest as a transverse EM
wall thats saturated by an entrained longitudinal core"*

**Verdict: two of three parts match canon; one is inverted; and the most
interesting part lands on a hole canon states explicitly.**

### (a) "A physical boundary is impossible" — RIGHT in the operative regime [CANON]

The wall is an **impedance condition, not a surface**. Canon says this in
operator form, twice:

- **Op9 Universal Steric Reflection** (`operators.md`:49): *"Γ_steric → −1
  (Pauli-level overlap → impedance divergence)"*, described as *"Pauli-level
  repulsion mapping overlap to an impedance divergence Γ → −1"*.
- **Op4 Universal Pairwise Potential** (`operators.md`:44):
  `Z(r) = Z_0/(1−(d_sat/r)²)^{1/4}` with a three-regime table
  (Coulomb / nuclear-H-bond / **Pauli**).

The "wall" is a **divergence in a continuous function of separation** — no
material surface anywhere. **Scope caveat:** this holds in the sub-yield
lossless regime. Past `V_snap` the medium ruptures, and rupture IS a
discontinuity — so "impossible" is regime-scoped, not universal.

### (b) "A transverse EM wall" — MATCHES CANON

`def-vyvsn1` (SOLID): `V_yield` is the **transverse-T2 self-trap wall**.

### (c) "saturated by an entrained longitudinal core" — INVERTED [correction]

Canon runs the causation the other way, and the ratified combine rule forbids
the proposed direction:

1. The T2 winding **self**-traps — *"the mirror is made of the thing it
   confines"*; the T2 field's own amplitude pins the shell at the rail.
2. The A1 core is the **sub-saturated occupant**: `A = √α ≈ 0.085`,
   `S ≈ 0.996` — **0.7 % of yield**. It is not saturating anything.
3. **DP-3 (Grant-ratified 2026-07-02, `trampoline-framework.md`:255) makes this
   structural, not incidental:** the combine is per-yield-normalized with
   **separate `S_μ`, `S_ε` kernels — L2-sum WITHIN a grade, L∞ (first grade to
   `S→0`) ACROSS grades.** Under L∞-across-grades an A1 contribution does not
   add into the T2 kernel at all. **The longitudinal core cannot saturate the
   transverse wall by construction of the ratified combine rule.**

**Corrected form of the sentence:** *a transverse-T2 self-trapped wall, holding
an entrained longitudinal core that sits far below its own yield.*

### (d) ★ The valuable part: this lands on a hole canon states explicitly

`form-deriving-value-importing.md`:220, verbatim: spin-statistics is *"the
exchange = antisymmetric **connection** (σ = −I, FR two-loop braid, #315) —
DERIVED at PEER-ahead"*, but *"**the dynamical selection of the antisymmetric
sector (exclusion enforcement) stays OPEN**."*

**Canon derives the braid's sign; it does NOT derive the enforcement.** Grant's
capacity reading is therefore **not a competitor to the FR-braid treatment — it
is a candidate for the open enforcement half**, and Op9/Op4 already supply the
repulsion side of it in canonical operator form.

**The obstacle it must clear [the sharp one]:** Pauli is **spin-dependent and
state-based**, not spatial. Opposite-spin electrons overlap *completely* in one
orbital and are allowed; same-spin are not. A spin-blind capacity mechanism
excludes both, so capacity alone cannot be Pauli.

**★ CANDIDATE repair, canon-supported [WALK, un-swept]:** DP-3's **separate
per-grade kernels with L∞ across grades** is exactly the structure that would
make capacity spin-dependent — two excitations loading the SAME grade sum (L2
within grade) and compete for one yield; two loading DIFFERENT grades do not sum
and do not compete. If spin maps to grade, "two per orbital" falls out of the
ratified combine rule. **The obstacle to THAT:** PR#260 ruled the μ-vs-ε fork
**DEGENERATE on equilibrium observables** (a sign selector), which cuts against
the two spin states loading different grades. **That tension is the walk this
candidate owes** — and note DP-3 itself records the cross-grade combine
(L∞ vs normalized-L2) as an **open discriminator, degenerate to O(α) at the
electron**, so a non-α-suppressed operating point is what would settle it.

**Routing:** recorded here at WALK grade; owes the 6-question sweep gate and the
#260-degeneracy walk before any part of it travels as a claim. Nothing in this
section mints, and no solidity moves.
