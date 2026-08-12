# Walk record — DoF vs PORT: is the longitudinal bulk scalar a degree of freedom? (2026-08-11)

> ## 🔴 ADJUDICATED 2026-08-12 — **M1 IS REFUTED. ONTOLOGY-DEAD.**
>
> **Rule 12: everything below this header is PRESERVED UNEDITED.** No new hypothesis is substituted
> into M1's slot. The walk was built to be killed and it was killed **on its own frozen criterion**;
> that is the record, and the record is what this document is for.
>
> **The killing fact.** M1's own membership test was *"no independent initial condition, no conjugate
> momentum."* The scalar `V` has **both**: `src/ave/core/master_equation_fdtd.py`:112–113 allocates
> `self.V` **and** `self.V_prev` as state arrays; `:219` steps them as a leapfrog pair
> (`V_new = 2·V − V_prev + dt²·c_eff²·L`, so `V_prev` **is** the conjugate momentum); `:265–267`
> sets `self.V_prev = self.V.copy()` under the comment *"Set V_prev = V to give zero initial time
> derivative (stationary initial state)"* — **an explicit initial condition on that momentum.**
> `V` is identified as the **A₁ dilatation** by the Grant-ratified
> [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20,
> and `03_pin_port_configuration.tex`:111 states it outright: *"The breathing mode … **is a genuine
> kinematic coordinate the Master Equation integrates.** … A mode is a coordinate; `A` is an operating
> point. Distinct objects."*
>
> **Second, independent refutation.** `k4-port-irrep-decomposition.md`:11,:21,:22 (clm-j550uh) derives
> `V_4-port = A₁ ⊕ T₂` — **four ports = 1 + 3**. M1's three-wire common-mode analogy (§2) was run on a
> **four-port node**, so the analogy's premise was wrong independently of the state-vector question.
>
> **Authority:** the #957 adjudication, executing this document's own frozen brief. **The walk-level
> stuck-point it surfaced (ring-or-sit) is RESOLVED by R51**,
> [`2026-08-12-ruling-r51-a1-two-objects-carve.md`](../_orchestration/docket-entries/2026-08-12-ruling-r51-a1-two-objects-carve.md)
> — the bias **sits**, the common-mode tank **rings defect-locally**, and the engine's vacuum-wide
> gapless `V` is **phantom-in-form**. That carve is now the standing frame; this record is closed
> beneath it.
>
> **What this means for Grant's 3+3+1.** It **stands** — `vol9/ch3-pin-port-configuration/index.md`:17
> counts *"seven per-cell kinematic modes — 3 translational **u** … 3 microrotational **ω** … 1
> volumetric **A₁** breathing."* The lane's category error was the reverse of the one it alleged:
> **it demoted a real coordinate to a port.** See §9 for the per-row verdicts and §10–§12 for what
> survives.

**Class:** records / **chat-walk transcript, ⚑ UN-AUDITED — now ADJUDICATED, see header.** No corpus
file is edited. Nothing is minted, no solidity moves, no axiom is amended. **This document exists to
be adjudicated, not to be believed.**

**Adjudication brief:** [`_orchestration/2026-08-11_dof-port-adjudication-brief.md`](../_orchestration/2026-08-11_dof-port-adjudication-brief.md)
**Receipts:** [`research/drivers/dof_port_ontology_check.py`](drivers/dof_port_ontology_check.py) — 14 checks, incl. an anti-tautology leg.
**Base:** `origin/main` @ `a23a044b`.

**Provenance, stated plainly.** This is a live conversational walk between Grant and the
gravity-linearity lane on 2026-08-11, following PR #955's §1–§8 review. **Its central claim (M1) is
the lane's, produced in chat, with no second reader.** Grant supplied the challenges (Q1–Q5) and two
of the framings; the lane supplied the vocabulary proposal and two retractions. **Who said what is
recorded per-row below, because that matters for how much each row is worth.**

> **⚑ WHY THIS IS NOT A SIDE NOTE.** It reaches an **axiom**. `eq_axiom_1.tex`:37 states *"six
> intrinsic degrees of freedom"*; `mode-counting-heat-capacity.md`:14–18 states **seven**, and uses
> that 7 to derive `g_* = 7³/4 = 85.75`, the offered substrate replacement for the Standard Model's
> `g_* = 106.75`. **If M1 is right, the two are not in contradiction — they are counting different
> kinds of object — and the `g_*` derivation loses its basis.** If M1 is wrong, Axiom 1 is
> undercounting and needs amendment. **Either way an axiom-level statement moves**, which is why this
> goes to an auditor and not into a leaf.

---

## §1 — The claim ledger

Grammar: **C** = corpus fact (grep-verified, quotable) · **D** = defect found · **M** = the lane's own
claim · **R** = the lane's retraction · **G** = Grant's proposal. Only **M** and **G** rows require
adjudication; **C** rows need re-verification only; **D** rows need routing.

| id | claim | origin | status | receipt |
|---|---|---|---|---|
| **C1** | Axiom 1 states **six intrinsic DoF per node**, node is *"micropolar (Cosserat-type)"* — 3 translational (→ε₀/**E**) + 3 microrotational (→μ₀/**B**) | corpus | verified | `eq_axiom_1.tex`:37 |
| **C2** | Axiom 1 places the continuum as a **limit**: *"In the macroscopic continuum limit, the lattice is a Trace-Reversed Chiral LC Network … trace-free transverse EM"* | corpus | verified | `eq_axiom_1.tex`:37 |
| **C3** | `n = 7` is stated to count *"independent compliance modes per node"* = 3 translational + 3 rotational + **1 volumetric (radial breathing / compression)**; `d = 2` = the two transverse polarizations | corpus | verified | `mode-counting-heat-capacity.md`:14–20 |
| **C4** | The same `2/7` is derived with **no mode counting**: `ν = (3K−2G)/(2(3K+G)) = 4/14 = 2/7` at `K = 2G` | corpus | verified | `vacuum-poisson-ratio.md`:13 |
| **C5** | `ν = 2/7` is the **Voigt–Reuss–Hill isotropic average**; the lattice is anisotropic (Zener `A ≈ 1.23`); *"an averaging choice, not a per-direction lattice output"* | corpus | verified | `vacuum-poisson-ratio.md`:18–24 |
| **C6** | *"The value ν=2/7 is **GR-imported** via K=2G (PR#261) … the crystalline srs Cauchy tensor is a **one-parameter family**, ν=2/7 only at an externally-supplied ρ*≈9.77 … **not** crystalline/network-derived … the 1/7 boundary is a projection of a GR-imported ratio, **not a first-principles lattice output**"* | corpus | verified | `one-seventh-impedance-projection.md`:18 (PR#506) |
| **C7** | Deleting the longitudinal branch forces `λ = −2μ` ⇒ `K = −4μ/3 < 0` ⇒ runaway implosion. **The corpus's own argument FOR micropolarity** | corpus | verified | `implosion-paradox.md`:10–16 |
| **C8** | The biquaternion is *"canonized-to-nothing **AS A PRIMITIVE**"*; *"**never** mint it as a substrate primitive or **read a new number off it**"* | corpus | verified | `unified-engine-design-doctrine.md`:282–290 |
| **C9** | Chirality is frozen in at crystallization; mirror-image freeze-in gives *"identical magnitude \|u₀\| and **identical physics**"* | corpus | verified | `trampoline-framework.md`:101–105 |
| **D1** | **Dead cite.** The 6-DoF claim is sourced to *"INVARIANT-S2 verbatim, `ave-kb/CLAUDE.md` line 55."* **`:55` is blank**; INVARIANT-S2 is at `:66` and concerns **axiom numbering**, not DoF. Claim true, pointer wrong on both counts | lane | verified | `delta-strain-cosmic-tcc.md`:32 |
| **D2** | **Equivocation in four lines.** `:14` says *"compliance **modes**"* (port language); `:16`,`:17`,`:18` each say *"**degrees of freedom**"* (state language) — for the same seven | lane | verified | `mode-counting-heat-capacity.md`:14–18 |
| **D3** | **The `7` is not invariant.** `(3K+G)/G` = 4 at `K=G`, **7** at `K=2G`, 8 at `K=7G/3`, 10 at `K=3G`. **A count cannot slide with a stiffness ratio** | lane | receipted | driver family **A** |
| **★ M1** | **The longitudinal bulk scalar (dilatation) is a PORT, not a DoF.** `θ = ∇·u` is built from the gradients of the three translational coordinates: **no independent initial condition, no conjugate momentum.** It is an irreducible *channel* with its own modulus (`K`), not a state variable | **lane** | **UN-AUDITED — adjudicate** | §2, driver **C** |
| **M2** | Therefore `3 + 3 + 1 = 7` adds **6 state variables to 1 port** — a category error — and C3's `n=7` is not a DoF count | **lane** | **UN-AUDITED — adjudicate** | follows from M1 + D2 |
| **M3** | The **pseudoscalar is a formation parameter**, not a DoF: it is the centre of `Cl(3,0)`, a handedness marker with no independent kinematics — and C9 makes it explicitly a frozen-in manufacturing artifact | **lane** | **UN-AUDITED — adjudicate** | C8, C9 |
| **M4** | The four-category vocabulary ladder (§2) — state variable / port / constitutive coefficient / formation parameter | **lane** | **UN-AUDITED — adjudicate** | §2 |
| **M5** | The regime-dynamic split should be: **DoF count is a PHASE property** (invariant within a phase); **port grading and port connectivity are REGIME properties**. *Not* "6 at low strain, 7 near yield" | **lane** (answering G2) | **UN-AUDITED — adjudicate** | §4 |
| **R1** | ⚑ **RETRACTED: "microstretch."** Imported by the lane from **Eringen's micromorphic/microstretch continuum mechanics**; **zero hits in the corpus** (`micropolar`/Eringen *are* native). The term *is by definition* the 7-DoF theory with an independent microdilatation field — **naming it presupposed the disputed answer** | lane | withdrawn | §5 |
| **R2** | ⚑ **RETRACTED: "a biquaternion has 8 components, so discard the pseudoscalar to get 7."** This counted **algebraic grades as state variables** — the same category error M1/M2 criticize | lane | withdrawn | §5 |
| **G1** | Axiom 1 **does not state the status of the longitudinal/scalar channel.** It declares 6 DoF and a *"trace-reversed … trace-free"* continuum limit, but never says whether the trace is a live port | **Grant** | **open — adjudicate** | C1, C2 |
| **G2** | Axiom definitions should be **dynamic w.r.t. vacuum phase / regime of strain** | **Grant** | **open — adjudicate** | §4 |
| **G3** | **Framing challenge:** a medium reproducing physics 1:1 in-regime is the hypothesis *working*, not an echo; the discriminator lives at the boundary. The lane's license map conflated *"imported"* with *"deficient"* | **Grant** | **open — adjudicate** | §6 |
| **G4** | *"Why do you keep saying continuum?"* — the substrate is discrete; continuum is emergent | **Grant** | **sustained by C2** | §3 |

---

## §2 — M1 stated precisely, in EE terms (the thing to attack)

Four objects have all been called *"modes"* in this corpus. The walk's proposal is that they are
distinct and must never be summed:

| # | object | membership test | EE term | count here |
|---|---|---|---|---|
| 1 | **DoF / state variable** | has an **initial condition** and a **conjugate momentum**; sets system order | independent **capacitor voltage / inductor current** | **6** (3 C→**E**, 3 L→**B**) |
| 2 | **Port / channel** | somewhere energy can be injected and an **impedance measured**; *built from* the states | a **branch**, or a **mode of a set of wires** | bulk + shear |
| 3 | **Constitutive coefficient** | a number setting a port's stiffness | the **L or C value** | `K`, `G`, `ν` |
| 4 | **Formation parameter** | a sign/offset **locked at manufacture**; no dynamics | **winding sense**, sign of `k` | chirality |

> **★ M1, in one sentence.** *Take three wires. Decompose into one **common mode** and two
> **differential modes**. The common mode is not a fourth wire.*

Dilatation is the **common mode of the three translational branches**. It earns its own impedance
(`Z_cm ≠ Z_dm`, exactly `K ≠ G`) and needs its own return path — both of which make it a genuine
**port**. Neither makes it a **state**. You cannot give it an initial condition without moving `u`.

**The corpus forbids deleting it** (C7): killing the longitudinal branch drives `K < 0` and the
vacuum implodes. **So the bulk port must exist, must be live, and must have positive stiffness — and
is still not a state variable.** Port-hood and DoF-hood are independent properties; the walk's claim
is that canon has been treating them as one.

**Machine-checkable adjudicator (driver family C).** The operative node model
`src/ave/core/vacuum_node_circuit.py` (`class PerDOFVacuumNode`) exposes **3 `L` slots + 3 `C` slots
= 6** per-node storage slots and no seventh; `src/ave/topological/cosserat_field_3d.py`:4–5 carries
*"the translational displacement u(r) and the Cosserat microrotation omega(r) as **independent
fields**"* — two 3-vectors, no scalar field. Dilatation appears in that module as the *"A1 (V_inc,
V_ref) dilatation-**MASS phasor**"* (`vacuum_node_circuit.py`:17) — **a port object, not a state
slot.** ⚑ **A seventh independent slot anywhere in the operative state vector REFUTES M1**, and the
driver's family-D leg proves the detector reports 7 when handed a synthetic 7-slot node, so the
check is falsifiable rather than vacuous.

⚠ **What driver family C does NOT establish.** Green means *the engine does not contradict M1*. The
engine is an implementation; it could be under-modelling. **It cannot promote M1 to canon** — only
an adjudication can, and that is not this document's to make.

## §3 — On "continuum" (G4) — sustained, and it is load-bearing

The lane used *"continuum mechanics"* throughout as if it named the substrate. **It does not.**
Axiom 1 (C2) makes the continuum a **limit** of a discrete chiral Laves K4 crystal.

This is not vocabulary hygiene; it decides C3-vs-C4:

- The **scalar + deviatoric** decomposition is an **SO(3)** statement (driver family B: 6 = 1 + 5,
  hence exactly **two** moduli).
- **The srs/K4 lattice does not have SO(3)** — it is cubic-chiral and anisotropic, Zener `A ≈ 1.23`
  (C5, PR#506).
- Therefore **the entire `7` lives in the emergent continuum**, inside an **isotropic average** (C5's
  own words), of an **anisotropic** lattice, at a **GR-imported** `K = 2G` (C6).

**So the `7` could not have been a lattice mode count even in principle.** C3's reading is a
continuum-limit coefficient described in discrete-substrate language. *(This sharpening is Grant's —
the lane's own grep did not reach it.)*

## §4 — G2: the regime-dynamic axiom, and the lane's counter-proposal (M5)

Grant's proposal: axiom definitions should track vacuum phase / regime of strain.

**M5 (the lane's response — adjudicate, do not assume).** The natural reading — *"6 DoF at low
strain, 7 near yield"* — should be rejected, because **a state variable cannot be grown by pushing
harder**: system order is fixed by kinematics, not by amplitude. The defensible split:

| property | what it is | varies with |
|---|---|---|
| **DoF count** | number of state variables per node | **PHASE** — fixed within a phase; changes only across a phase transition (crystallization / genesis) |
| **Port grading + connectivity** | which channels are graded, and whether a port still transmits | **REGIME** — this is where `S(A)`, the SYM/ASYM loading split, and the `Γ = −1` walls live |

M5 is **stronger** than adding a 7th DoF: it makes a falsifiable claim in **both** directions —
DoF-count invariance *within* a phase, and port-structure variation *across* regimes. **G1's gap
survives M5 untouched:** the axiom still does not say whether the trace is a live port, and on M5's
reading that is a *port-structure* statement the axiom is entitled to make.

## §5 — Retractions (R1, R2) — recorded, not buried

**R1 — "microstretch."** The lane introduced it to name a 7-DoF continuum with an independent
microdilatation field. **It is absent from the corpus** (verified: zero hits repo-wide outside this
lane's own documents; `micropolar` and Eringen *are* native, incl. Axiom 1 itself). Importing it
imported **Eringen's theorems** — specifically the premise that the volumetric mode *can* be an
independent state variable, which is exactly the disputed question. **A vocabulary-cage instance: the
word carried the conclusion.**

**R2 — "8 components, discard the pseudoscalar to get 7."** The lane counted **algebraic grades** of
`Cl(3,0)` (1 scalar + 3 vector + 3 bivector + 1 trivector) as though they were state variables.
**Grades are not DoFs.** This is the identical category error M1/M2 allege against C3 — committed by
the lane, one turn before alleging it. Recorded because it is evidence about **how easy this error
is**, which is itself relevant to adjudicating M2.

## §6 — G3: the framing challenge, and what the lane concedes

Grant's challenge: *a physical vacuum medium that reproduces existing physics 1:1 until the boundary
conditions of material/phase/regime is the hypothesis working — reproduction in-regime is the
prediction, not a failure.*

**The lane concedes the framing defect.** PR #955's license map used **IMPORT** as though it were an
indictment, and never separated:

- **FORM forced by the medium, value reproduced** → the hypothesis working.
- **FORM chosen to match, value fitted** → an echo with no content.

**But the concession does not rescue this coefficient**, and the corpus is what says so: the test that
separates those two readings is *"does the coefficient fall out of the geometry"*, and **PR#506 ran
exactly that test on the srs lattice and it came back negative** (C6) — the Cauchy tensor is a
one-parameter family and `ν = 2/7` appears only at a hand-supplied `ρ* ≈ 9.77`.

**So the honest localization:** everything downstream of `ρ*` is forced continuum mechanics. **The
unfixed content of the whole `/7` chain is one number — `ρ* = k_a/k_s ≈ 9.77`, the axial-to-shear bond
stiffness ratio.** Whether that is geometry or a free parameter is the question G3 actually turns on,
and **this walk does not answer it.**

## §7 — Blast radius (what moves if M1/M2 are sustained — none of it actioned here)

| downstream | dependency | consequence if M1/M2 sustained |
|---|---|---|
| `g_* = n³/N_K4 = 343/4 = 85.75` (`vol3/claim-quality.md`:504–514) — the offered replacement for the SM's `106.75` | needs `n = 7` to be a **count** | loses its basis; `n` is a coefficient, and `n³` of a coefficient is not a mode count |
| `mode-counting-heat-capacity.md`:14–20 | states `n=7` as DoF | needs the port/state relabel (D2) |
| **PR #955 §4.1** — restated as *"(channel MODE-COUNT fraction) × (channel strain)"* | the §1–§8 review **instructed** that restatement | **wrong as written**; the fractions are coefficients, not mode-counts. ⚑ **The review's instruction and the corpus disagree — the lane did not improvise a fix** |
| PR #955 §9 review brief, lens **L3** | asks whether `m = 1 + ε₁₁/7` is derived or back-fitted | C6 already answers: the `1/7` is a projection of an import ⇒ **back-fit charge stands** |
| `eq_axiom_1.tex`:37 | silent on the scalar channel (G1) | candidate amendment — **Grant's call, not an auditor's** |

## §8 — Explicitly NOT done

No corpus file edited. No axiom amended. No claim-id minted. No solidity moved. **M1–M5 are not
asserted as findings** — they are entered so they can be killed. `ρ*` is not derived or estimated.
PR #955 is untouched by this branch. The `Γ`-sign fence (`backreaction.md`:194, wall-taxonomy §10)
is not entered.

---

# ADJUDICATION CLOSURE (2026-08-12) — appended below the preserved body

## §9 — M-row verdicts (from the #957 adjudication; §1's ledger rows stand as written)

| row | verdict | basis |
|---|---|---|
| **M1** | **REFUTED** | Failed **its own** membership test. `master_equation_fdtd.py`:112–113, :219, :265–267 — `V` carries an independent IC **and** a conjugate momentum (`V_prev`). Second, independent refutation: `k4-port-irrep-decomposition.md`:11,:21,:22 — `V_4-port = A₁ ⊕ T₂`, **four** ports, so §2's three-wire analogy had the wrong node. |
| **M2** | **refuted as stated** | `3+3+1` is **not** a category error — the volumetric A₁ breathing **is** a coordinate (`03_pin_port_configuration.tex`:111). ⚑ **The underlying defect survives, but on D3 alone**: the ν-denominator 7 is K-conditional. The *arithmetic* complaint stands; the *ontological* one does not. |
| **M3** | **MOOT** | R2's retraction dissolved its premise. Nothing to adjudicate. |
| **M4** | **DOWNGRADED** | The state-vs-operating-point carve is **already canon, verbatim**: `01_general_description.tex`:18 (*"which is **not** a seventh spatial DOF"*, of the saturation state `A`) and `03_pin_port_configuration.tex`:111 (*"A mode is a coordinate; `A` is an operating point. Distinct objects."*). The four-category ladder is a **useful consolidation, not a new distinction.** |
| **M5** | **DOWNGRADED — unfalsifiable as posed** | Two engines found **zero** corpus sites stating a before/after DoF count across a phase transition. With no site to check against, *"DoF count is a PHASE property"* cannot currently be failed. |

## §10 — ⚑ THE DRIVER IS **NOT CITABLE** as a receipt for anything about DoF counts

`research/drivers/dof_port_ontology_check.py` is quarantined. **Three independent reasons, all
confirmed at the adjudication:**

1. **It declares a match between two DIFFERENT sixes.** Check `C2` reads *"3 L + 3 C = 6 storage slots
   … matches `eq_axiom_1.tex`:37 'six intrinsic degrees of freedom'."* It does not. The engine's six is
   **3 translational DoF × 2 phase-space slots (an L and a C per direction)**; Axiom 1's six is
   **3 translations + 3 microrotations.** The module says so itself at `vacuum_node_circuit.py`:12–25
   — the per-DOF `(L_i, C_i)` is *"the MECHANICAL displacement-direction constitutive layer of the
   TRANSVERSE / EM-translation sector (the cell's three translational u → E modes)"* and explicitly
   **"is NOT … the A1 (V_inc, V_ref) dilatation-MASS phasor."** The check was a coincidence of the
   integer 6.
2. **Three of its fourteen checks cannot fail** — `B1` (hardcoded `1+5 == 6`), `B2` (literal `2 == 2`),
   `B3` (literal `True`). Unfireable gates dressed as receipts.
3. **It is PLACEMENT-BLIND.** A live probe injected a genuine seventh slot (`theta` + `pi_theta` +
   `K_bulk`) into the **real engine** and the driver still reported *"all receipts GREEN"* — including
   **`C3 NO seventh storage slot`**. It only ever read one function signature in one file, so the
   family-D anti-tautology leg proved the *parser* could count to seven, **not** that the *check* could
   find a seventh slot where one actually lives.

> **The lesson worth keeping.** The driver had an anti-tautology leg and still could not fire. A probe
> that validates the parser is not a probe that validates the gate — the injection has to land where
> the real object lives. This is the self-referential-gate class again, one layer deeper.

## §11 — Standalone defects: ROUTED, all M1-independent, all confirmed

| id | defect | scope correction from the adjudication |
|---|---|---|
| **D1** | Dead cite at `delta-strain-cosmic-tcc.md`:32 | ⚑ **UNDER-SCOPED as this record wrote it.** `ave-kb/CLAUDE.md`:55 is blank ✓ and INVARIANT-S2 is at `:66` ✓ — **but the correct target is `:70`** (the Axiom-1 bullet, which does carry the 6-DoF text), and the quoted pointer also **drops the `manuscript/` prefix**. **And there is a SECOND instance of the same dead cite**: `manuscript/vol_9_vacuum_datasheet/chapters/06_temperature_characteristics.tex`:29 — *"Per Axiom~1 (CLAUDE.md INVARIANT-S2 verbatim), the substrate K4 lattice carries six degrees of freedom per node"*. Two sites, one bad pointer. |
| **D2** | Four-line equivocation, `mode-counting-heat-capacity.md` | Confirmed, with the reading tightened: `:14` *"compliance **modes**"* · `:16`,`:17` *"degrees of freedom"* (plural) · `:18` *"degree of freedom"* (**singular**). |
| **D3** | The sliding 7 | Confirmed and **independently re-derived**. ⚑ **Extended: the NUMERATOR slides too.** At `K = G`, `ν = 1/8` — which on C3's reading would have to be read as *"1 transverse polarisation, 8 modes."* Both halves of the fraction move with the moduli, so neither is a count. **D3 is the surviving core of M2.** |

## §12 — Routed, NOT repaired

**(e) `g_*` — flag only, no solidity moves.** `g_* = n³/N_{K4} = 7³/4 = 85.75`
(`vol3/claim-quality.md`:504–514, value at `:507`) is sourced **through the ν route** — i.e. the seven
that slides (D3). ⚑ Its claim-id `clm-uu6dl5` is the **same** id carried in
`mode-counting-heat-capacity.md`'s frontmatter: **one node, not two.** The claim already caveats
itself at `:513` (*"a multi-factor formula with several lat…"*) and `:514` (*"Does NOT claim
`g_* = 85.75` is a separately measurable cosmological observable; the validation is via the
downstream baryon ratio"*). **Flagged. No repair, no solidity change.**

**(f) FLAG for Grant — ⚑ but the pairing in the closing relay does not hold, and the lane will not
reproduce a mis-paired contradiction.** The relay poses
`vol9/ch3-pin-port-configuration/index.md`:17 (*"seven per-cell kinematic modes"*) against
`01_general_description.tex`:18 (*"not a seventh spatial DOF"*) as a 6-vs-7 contradiction inside one
volume. **Those two phrases are about different objects, and the same volume says so.** At `:18` the
*"not a seventh spatial DOF"* clause attaches to **the saturation state `A`** (*"an operating point —
the saturation state `A`, a DC bias on the node's own nonlinearity … which is not a seventh spatial
DOF"*), **not** to the volumetric breathing mode; `03_pin_port_configuration.tex`:111 draws exactly
that line, and `index.md`:17's own clause (i) cites the same disambiguation. **What DOES survive as a
real flag, stated accurately:** `01_general_description.tex`:18 says nodes carry *"six degrees of
freedom"* and **never mentions the A₁ breathing mode at all**, while `index.md`:17 counts it as the
seventh kinematic mode. **That is the live question — an omission, not a contradiction — and it is
Grant's.** *(Reported this way per the frozen-criteria-travel-verbatim discipline: a paraphrase that
becomes the pivot is the failure mode this lane has already been bitten by.)*

**(g) G1 — RE-FRAMED before it goes to Grant.** Axiom 1's silence on the scalar channel is real, **but
the axiom SET is not silent.** `manuscript/common_equations/eq_axiom_5.tex`'s preamble names exactly
that gap: *"never write the source coupling that pins the bound (A1 dilatation) sector's absolute
state."* **So G1 is not "the axioms don't cover this" — it is "Axiom 5 is the specification, and
Axiom 1 does not point at it."** A cross-reference question, not a gap. **G2 unchanged, still Grant's.**

## §13 — What this closure does NOT do

No corpus file edited. No axiom amended. `g_*` untouched. D1/D2/D3 routed, not fixed. The `Γ`-sign
fence not entered. **M1's slot is not refilled** — the body above stands as written, wrong, and dated.
