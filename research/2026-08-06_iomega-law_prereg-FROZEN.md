# PRE-REGISTRATION (FROZEN) — the I_ω(A) law (FLAG-IOMEGA): derive, or bound, the amplitude dependence of the rotational micro-inertia

**Date:** 2026-08-06 · **Branch:** `research/iomega-law`
**Written against `origin/main` =** `d129e7ac` (the lane base; also the pinned scan surface, §3).
**Dispatch:** [`_orchestration/2026-08-06_iomega-law-brief.md`](../_orchestration/2026-08-06_iomega-law-brief.md) — the FLAG-IOMEGA lane, ruled R6 (`_orchestration/docket-entries/2026-08-06-rulings-decision-batch.md`, *"two derivation lanes briefed"*).
**Class:** DERIVATION prereg (research-doc; **mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates
to no KB/manuscript leaf; changes no solidity; edits no falsification ledger; engine `src/ave`
byte-untouched and never imported — engine reads are receipts about the CODE, not the substrate**).
**SVA v0.2 header (11 rows) below; pilot-family numbering left to the orchestrator's ledger.**

> **THIS FILE IS FROZEN AND PUSHED ALONE**, before any driver code exists and before any scan,
> classification, or derivation output produced by this lane exists. No gate, tolerance, bin
> boundary, pattern-battery entry, receipt-checklist item, verdict wording or method element of
> §1–§6 may be changed after any result of this lane is seen. **UNRUN ≠ PASSED.**

**WHAT THIS LANE MAY AND MAY NOT DO.** It derives, or bounds, the amplitude dependence of the
Cosserat rotational micro-inertia `I_ω` — the law canon does not state (FLAG-IOMEGA,
[`2026-08-05_approach-leak_result.md`](2026-08-05_approach-leak_result.md):475–482, *"canon
states no `I_ω(A)` grading law."*). It may NOT touch the approach-leak knife (Rule 11 — the
brief's wording is operative: *"the knife's frozen criterion is untouched by this lane; you
deliver the law, the knife's verdict follows mechanically"*), may NOT adjudicate FORK-3, may NOT
promote the engine's coded `a = 2` to canon (the v2 fence,
[`2026-08-06_approach-leak-v2_result.md`](2026-08-06_approach-leak-v2_result.md):379 names the
hinge *"while the engine's `a = 2` stands"*), and may NOT edit any predecessor artifact.

---

## §0 — Standard Vacuum Analysis header (SVA v0.2, 11 rows)

 1. **SECTOR / OWNERSHIP:** the object is the **kinetic coefficient of the Cosserat micro-rotation
    sector** — `I_ω`, the coefficient of `½·I_ω·|ω̇|²` in the canonical Lagrangian
    (`src/ave/topological/cosserat_field_3d.py`:953,
    `L = ½·rho·|u_dot|² + ½·I_omega·|omega_dot|² − W(u, omega)`), the
    channel-4 flywheel inertance. **Cross-wiring check done:** the rest-MASS store is A1
    dilatation and is NOT this object (the Lenz-inertia re-scope guard: the stored inductive
    energy is the T2/ω flywheel, the rest-mass store is A1 — no cross-wire); charge is the
    Cosserat winding INTEGER and is not in this lane. **The lane's core question IS a sector
    question:** whether a **foreign-sector static bias** (the A1/ε-sector strain amplitude
    `A_ε`) re-values a **rotational-sector** kinetic coefficient — so the sector carve is the
    derivation's subject, not only its header.
 2. **REGIME / PHASE-STATE:** **MODE** — constitutive-law derivation: a DC operating-point
    statement about a coefficient, consumed downstream by the approach-leak small-signal AC
    scattering instrument. **REGIME** — sub-yield lossless-reactive on `r > r_sat`; the `A ≥ 1`
    interior is Regime IV and **is not in the domain**. **PHASE-STATE** — cold crystalline
    lattice, Op14 ON as a static constitutive grade, `A(r) = r_sat/r`; the delivered law's domain
    of validity is exactly this static sub-yield approach, and **no phase boundary is crossed**
    (any candidate law whose mechanism requires collapse dynamics, rupture, or the de-bonded
    phase is out-of-domain here and must say so).
 3. **CIRCUIT STATEMENT (before any framework word):** `I_ω` is the **series inertance (the
    inductance-analog) of the rotational transmission line**; `G_c` is the shunt stiffness whose
    ratio to it sets the line's cutoff — the gap `ω_m² = 4G_c/I_ω`
    (`manuscript/ave-kb/common/trampoline-framework.md`:192,
    `$m_\omega^2 = 4 G_c / I_\omega$`). The question in circuit
    terms: **does a DC bias on the OTHER line's capacitive sector re-value this line's series
    L?** Total-vs-slot: the knife consumes only the RATIO (the cutoff), never either slot alone —
    which is why provenance-consistent pairing of the two slots' gradings is part of the
    deliverable (§2.3).
 4. **PLANE & PROJECTION:** no signed `Γ` and no `Z` at any wall plane is claimed by this lane;
    the primary deliverable is a **dimensionless exponent** (plane-invariant). Spectral
    convention: the gap is the rotational optical-branch bottom, **frame-side** per the A-008
    canonical convention, with the field-side image one application of the ruled half-cover —
    this lane inherits that convention and re-derives nothing about it.
 5. **CONSTITUTIVE PROVENANCE (every law consumed, tagged):** `S(A) = √(1−A²)` DERIVED (Ax 4);
    `A(r) = r_sat/r` DERIVED-FORM / VALUE-IMPORTED; `G_c/I_ω = ω_C²` **RULED-AT-COLD-POINT**
    (A-008, PR #895; the record's own fence — the check *"does not reach into the saturated
    regime"* — is consumed as scope, §2.4); engine `a = 2` **CODE-NOT-CANON**; **RHO-B
    `ρ_eff = ρ_0/S³` IMPORTED-BY-ANALOGY** (its manuscript source derives nothing:
    `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`:445,
    *"longitudinal inertia scales with the Lorentz factor"* — the SR γ transplanted with
    `γ ↔ 1/S`), **matter-scoped** and **FORKED(FORK-3) OPEN**
    (`manuscript/ave-kb/common/wall-taxonomy.md`:433, *"the fork is still OPEN"*); the μ-sector
    keying **RULED** (the Grant-ratified 2×2, `manuscript/ave-kb/common/operators.md`:135–140,
    *"the canonical μ-kernel is slew-KEYED"*); the relativistic inductor CANONICAL with the
    amplitude-vs-rate refinement **BRACKETED(pending-ruling)**
    (`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`:171, *"pending A4"*);
    the archived kinetic co-saturation prescription **ARCHIVE-STAGED-CANCELED**
    (`research/_archive/L5/axiom_derivation_status.md`:313, *"cleanliness only, NOT
    load-bearing for closure"* — E-073); lattice pitch under strain
    **BRACKETED(pending-ruling)** (FLAG-PITCH — handled by the §2.2 cancellation lemma, not
    resolved). **The delivered `b`: target provenance DERIVED, else honestly CONDITIONAL or
    BOUNDED.**
 6. **ENERGY LEDGER:** **RIM.** Every mechanism this lane touches is within-system reactive
    exchange; no port is crossed and no loss word is used anywhere in this lane. The one
    energy-honesty receipt consumed (the loaded-μ conservation check of the circulation-keyed
    inductor) is cited as a CODE-class receipt, not as substrate evidence.
 7. **CALIBRATABILITY:** the primary deliverable is a **dimensionless exponent** `b` and the
    composed dimensionless `p`; no absolute modulus is shipped (the A-008 pin is a RATIO; the
    absolute `I_ω` stays the ENG-CHOICE placeholder canon says it is,
    `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`:151,
    *"placeholders calibrated to"*).
 8. **DISCRIMINATION CLASS:** the downstream knife physics is DC→AC coupling (a static DC bias
    modulating an AC transport property); **this lane's own deliverable is internal constitutive
    bookkeeping and is NOT surfaced as an AVE-vs-competitor discriminator.** Tautology filter:
    `b = 0` is contentful against the live `b = 3` alternative (the v2 hinge), not a restated
    identity. SM counterfactual: GR + matter carries no saturating rotational-gap modulus — the
    question does not arise there, so no discriminator claim is available or made.
    **Walk fence:** the rotation-substance walk (UN-AUDITED) predicts `I_ω` strain-independent;
    per the brief this is context, NOT a target. Symmetric reporting is frozen: a RIDES outcome
    is reported as a walk-falsifier; a CONST outcome is reported as walk-CONSISTENT and
    explicitly **NOT** walk-validating (the walk's counter-arms C1–C6 are untouched by either
    outcome — an ontology-neutral crystal can produce the same law).
 9. **CERTIFICATION PLAN:** gates §4 frozen here before any scan or derivation output exists;
    this prereg lands as its own pushed commit; negative controls named in advance (§3: the v1
    `P3`/`P4` battery is reproduced byte-identically as the reproduction control; a present- and
    an absent-sentinel fireability pair is mandatory); derived gate constants get pre-freeze
    second-method checks (§4.4); the scan instrument **excludes its own artifacts by
    construction** (the scan surface is the pinned base tree `d129e7ac`, which contains no lane
    artifact). All comparisons in this lane are exact (integers, strings, rationals) — no
    float tolerances exist to size wrongly.
10. **ADJUDICATION ROUTING:** BIN-CONST-DERIVED or BIN-RIDES → the exponent feeds the
    already-certified v2 bin table mechanically (consumption contract §1.2) and the routing is
    to the ORCHESTRATOR'S DOCKET, not to any edit by this lane; BIN-RIDES additionally flags the
    walk-falsifier to the residence lane (E1) via the docket; BIN-SUPERSEDED-BY-CANON → the
    found law is quoted in the headline and this lane defers to it; STOP-A008 → the lane stops
    and routes (frozen consequence §5.3). **Fence on this lane's own result:** the result doc
    propagates nothing to KB/manuscript without an adjudication ruling; FORK-3 remains exactly
    as open as it was regardless of bin.
11. **NUMERICAL CONDITIONING:** the only arithmetic is exact rational exponent composition —
    computed independently by `fractions.Fraction` and `sympy.Rational` (two engines, named);
    no cancellations, no iterated maps, no floats. Scan determinism: file set = the pinned
    commit's tracked blobs, `LC_ALL=C` sort, digest over canonicalized JSON excluding runtime
    fields. **Regex engines NAMED** (git grep `-P` = PCRE2 as shipped with the installed git;
    CPython `re` with the interpreter version recorded in the output JSON); **no pattern in the
    battery uses `\b`** (the FLAG-UNIWB rule); the ASCII-vs-Unicode `omega`/`ω` divergence that
    false-negatived the archive sites is closed by DUAL pattern forms per class (§3).

---

## §1 — The question and the frozen deliverable interface

### §1.1 The question (prove-or-disprove level, from the brief)

Does `I_ω` depend on the local strain amplitude `A_ε`, on the rotational amplitude `A_κ`, on
neither, or on both — and with what functional form? Derive from the substrate's own structure
(the srs control net, Wyckoff 8a, the A-008-pinned gap identity), not by convention import.

### §1.2 The consumption contract (what the knife takes, verbatim from the freeze that defined it)

The predecessor parameterization is FROZEN at
[`2026-08-05_approach-leak_prereg-FROZEN.md`](2026-08-05_approach-leak_prereg-FROZEN.md):191–197:
`G_c^eff(r) = G_c·S(r)^a` and `I_ω^eff(r) = I_ω·S(r)^{−b}`, `p = (a + b)/2`, and *"`a` and `b`
are the two numbers canon does not state."* **Sign convention therefore: `b > 0` means `I_ω`
GROWS toward the wall.** The v2 table is already adjudicated member-by-member (GAP-CLOSED on
`p ∈ {0.5, 1.0, 1.5}`; CHANNEL-OPENS on `p ∈ {2.0, 2.5, 3.0}`), so a delivered `b` that reduces
on the sub-yield approach to a pure power of `S(A_ε)` is consumed mechanically. **A delivered law
that is NOT a pure power of `S(A_ε)` on this approach, or that keys on an amplitude the approach
does not carry, maps onto NO frozen member and is reported as requiring successor adjudication —
it is not silently coerced onto the sweep.**

### §1.3 The deliverables (frozen list)

- **D1 (primary, knife-facing):** the exponent `b` w.r.t. `S(A_ε)` on the static sub-yield
  approach — derived, conditional, or bounded per §5's bins.
- **D2 (pairing rule):** the provenance-consistent pairing statement for `(a, b)` (§2.3's
  lemma): the knife's `p` is well-defined only when the two slots' gradings are drawn from the
  same provenance decomposition; the lane states which pairings are legal and why.
- **D3 (own-sector statement):** what canon's ratified keying structure implies for `I_ω`'s
  dependence on rotational-sector amplitudes (`A_κ`; own rate), with the A4
  amplitude-vs-rate bracket carried, NOT resolved.
- **D4 (A-008 consistency):** the delivered law evaluated at the cold point against the pinned
  ratio (gate §4.3; STOP-A008 on contradiction).
- **D5 (archive surfacing):** the E-073 staged-canceled kinetic co-saturation prescription
  surfaced with its cancellation receipt and its DOWN-vs-UP sign conflict with the
  diverging-inertia precedents — reported, not adjudicated.

---

## §2 — The frozen derivation protocol

### §2.1 The three-channel decomposition (frozen structure of the argument)

Any `I_ω(A_ε)` dependence must arrive through one of exactly three channels, and the lane must
adjudicate each with the receipts named in §2.5:

- **CH-G (geometric):** the node population per volume changes under the grade (lattice pitch /
  cell compression). Canon receipt state: no corpus site grades `ℓ_node` by `S` or `A`
  (re-receipted at §3, `P-I5`); strain-grading of the pitch is the OPEN FLAG-PITCH — this
  channel is handled by the §2.2 cancellation lemma WITHOUT resolving FLAG-PITCH.
- **CH-K (constitutive per-node, foreign-keyed):** the per-node rotor inertance re-values under
  the ε-sector static bias. This is the channel the ratified keying structure speaks to
  (slew-μ canonical; swing-μ *"PREDICTED EMPTY for the vacuum"*; W6 static-drive asymmetry;
  the A-034 catalog's zero inertial swing rows).
- **CH-R (imported transfer):** the RHO-B `1/S³` grading transferred to `I_ω` by analogy (the
  v1 flag's `b = 3` scenario). The lane audits the transfer chain's provenance link-by-link
  (§2.5 R6); it does NOT adjudicate FORK-3 itself.

### §2.2 The density-cancellation lemma (to be proven, then machine-checked)

On one crystal, `G_c` (per-volume stiffness) and `I_ω` (per-volume inertance) host on the SAME
lattice: `G_c = g_c·n_host`, `I_ω = j·n_host'` with `n_host/n_host'` a topological constant of
the net (srs `z = 3`, Wyckoff 8a — zero free positional parameters, so a homogeneous squeeze is
exactly affine and changes no count ratio). Therefore any COMMON population factor `n(A) ∝ S^{−d}`
enters both slots identically and cancels in the gap: `(a, b) → (a_c − d, b_j + d)` leaves
`p = (a_c + b_j)/2` invariant. **Consequences frozen as claims-to-check:** (i) the knife's `p` is
invariant to any geometric density grading, so FLAG-PITCH cannot move the knife whichever way it
resolves; (ii) a pairing that applies a density factor to ONE slot only (the `b = 3`-with-`a = 2`
scenario read as density) asserts that node density grades while bond density does not — on a
fixed-topology net that is not a live physical reading, so the `b = 3` scenario must stand or
fall as CH-R (constitutive transfer), not as CH-G. The arithmetic half is gate `G-PAIR`; the
hosting-ratio half must be argued from the net's ratified graph facts in the result doc.

### §2.3 The pairing rule (D2, frozen statement to be proven)

`p` is well-defined only for `(a, b)` drawn from one consistent decomposition (both totals, or
both constitutive with the common factor cancelled). Mixed pairings (one slot's constitutive
exponent with the other slot's total) are ILLEGAL and the lane must say so wherever the corpus
currently juxtaposes them.

### §2.4 The A-008 boundary condition (consumed as constraint)

The pin `G_c/I_ω = ω_C²` (given `ℓ_node ≡ ħ/(m_ec)`) is RULED at the COLD POINT — the record's
own regime fence keeps it there, and the propagation note's algebra
([`2026-08-05_a008-factor-propagation_note.md`](2026-08-05_a008-factor-propagation_note.md):175,
`G_c/I_\omega = \omega_C^2 = 1`) reaches `1` only through the cold calibration `ω_C = 1`.
**Frozen use:** every candidate law must reproduce the pinned ratio at `S = 1` exactly (gate
`G-A008-COLD`); NO candidate law may be justified BY the pin away from the cold point (that
would be an unsupported all-A extension — reader-of-record scope, §0 row 5); if a derivation
CONTRADICTS the pin at the cold point, the lane STOPS and routes (§5.3) — it does not re-tune.

### §2.5 The receipt checklist (frozen; BIN-CONST-DERIVED requires ALL of R1–R6 to verify)

| id | receipt | verification (each cite with its verbatim excerpt) |
|---|---|---|
| **R1** | the ratified keying 2×2: μ-kernel slew-keyed; the swing-μ cell empty for the vacuum | `manuscript/ave-kb/common/operators.md`:135–140, *"the canonical μ-kernel is slew-KEYED"*; `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`:161–173, *"PREDICTED EMPTY for the vacuum"* |
| **R2** | W6 static-drive asymmetry: a static ε-sector-only drive leaves the μ/rotational sector unloaded (`S_μ = 1`) | quote in `manuscript/ave-kb/CLAUDE.md` (INVARIANT-S2 block), *"loads the $\varepsilon$ / capacitive sector only ($S_\varepsilon < 1$, $S_\mu = 1$)"* |
| **R3** | the approach bias point carries ZERO rotational-sector own-amplitude: static ⇒ `ω̇ = 0`; the static gravitational grading carries no micro-rotation, and the homogeneous squeeze converts none (srs-twist 432 theorem, exactly affine) | `research/2026-08-05_last-bond-kernel-collapse_result.md`:146–155, *"carries no micro-rotation at all"*; `_orchestration/docket-entries/2026-08-05-srs-twist-coefficient.md`:22, *"zero free positional parameters"* |
| **R4** | the A-034 catalog grades NO inertial quantity in any of its 26 swing rows (all constitutive-side) | `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`:145–151, *"All 26 catalog instances are SWING-typed."* — plus the §3 `P-CAT` two-method re-scan |
| **R5** | every kinetic-side grading precedent in canon keys on the element's OWN rate/velocity: relativistic inductor (own current); sonoluminescence (own Mach); RHO-B's source (own collapse γ) | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md`:15–17, `I_{max} = \xi_{topo}\, c \approx 124.4`; `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md`:29–30, *"ideal relativistic inductor keyed on the circulating current"*; `manuscript/ave-kb/vol3/claim-quality.md`:451, *"longitudinal inertia in 3D spherical collapse"*; `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`:445, *"longitudinal inertia scales with the Lorentz factor"* |
| **R6** | the CH-R transfer chain carries ≥3 independent un-derived links (substance: matter→lattice, with FORK-3(c) LEADING; sector: translational→rotational; keying: own-velocity→foreign-static-strain), each link receipted | `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md`:16–21, *"Topo-Relativistic Impedance Divergence"*; `research/2026-07-31_qlaw-framing-challenge_walk.md`:1201, *"two different substances, and canon must say so"*; `manuscript/ave-kb/common/wall-taxonomy.md`:433, *"the fork is still OPEN"* |
| **R7** | (CODE-class context, not substrate evidence) the engine's kinetic side is bare — `I_ω` a constant placeholder; kernels multiply stiffness terms only | `src/ave/topological/cosserat_field_3d.py`:761–768, `S_eps_sq = jnp.clip(1.0 - eps_sq / epsilon_yield**2, 0.0, 1.0)`; :953–954, *"phase-I placeholder"*; :967, `self.I_omega = float(I_omega)` — plus §3 `P-I6` code scan |
| **R8** | the archive's staged kinetic co-saturation (`ρ→ρS`, `I_ω→I_ωS`) surfaced with its cancellation and its sign conflict with R5's diverging precedents | `research/_archive/L5/axiom_derivation_status.md`:313, *"cleanliness only, NOT load-bearing for closure"* — plus §3 `P-I3` Unicode battery hit-classification |

**Frozen expectation (declared per discipline, not steering):** the lane EXPECTS
BIN-CONST-DERIVED — `b = 0` w.r.t. `S(A_ε)` — because R1–R5 converge on one structure: static
amplitude kernels are constitutive-side only, inertia grades only on its own rate, and the
approach bias carries zero rotational own-amplitude. **What would discriminate against the
expectation:** a CANON-LAW battery hit (§3) stating an `I_ω(A)` law; a canon-grounded
zero-un-derived-link chain forcing `∂I_ω/∂A_ε ≠ 0` at the static bias (BIN-RIDES — reported as
a walk-falsifier); an A-008 all-A extension ruling; a FORK-3 resolution re-scoping `ρ_eff` onto
the lattice's own kinetic constants WITH a ruled sector transfer.

---

## §3 — The scan battery (two methods, engines named, pinned surface)

**Scan surface (frozen):** the tracked blobs of the base commit `d129e7ac` (`git ls-files` at
that tree; contents via `git show d129e7ac:<path>`), which **contains no artifact of this lane
by construction** (SVA row-9 self-reference rule). `research/_archive/**` is INCLUDED in the
surface and handled by the classification rule below — the v1 receipt's ASCII-only patterns
could not see the archive's Unicode `I_ω` sites, and this battery closes that hole.

**Methods (both, per pattern):** METHOD A = `git grep -P` against the pinned tree (PCRE2 as
shipped with the installed git; version recorded in the output JSON); METHOD B = CPython `re`
(interpreter version recorded) over the same blob set. **No pattern uses `\b`.** Frozen: `the
two methods must return the SAME hit set per pattern; if they disagree the DISAGREEMENT is the
reported result, the UNION is used, and nothing is reconciled silently.`

### §3.1 The patterns (frozen)

| id | pattern (PCRE2 = re form) | purpose |
|---|---|---|
| `P-NC3` | `I_\\?omega\s*\(\s*A\s*\)\|I_\{?\\?omega\}?\s*\(\s*A\s*\)` | v1 `P3` reproduced byte-identically — reproduction control |
| `P-NC4` | `(I_\\?omega\|micro.?inertia)[^\n]{0,40}(S\^\|/\s*S\|S\(A\))` | v1 `P4` reproduced byte-identically — reproduction control |
| `P-I3a` | `I_ω\s*(→\|->)` | the archive's Unicode prescription-arrow form (`I_ω → I_ω·S`) |
| `P-I3b` | `I_ω\s*[·*]\s*S` | the archive's Unicode product form |
| `P-I3c` | `I_ω\s*\(\s*A` | Unicode functional form — the discourse-vs-law classifier's main feed |
| `P-I4` | `(per.?node\|node.?level)[^\n]{0,60}(moment of inertia\|gyration)` | per-node rotor moment / gyration definition |
| `P-I5` | `(ell_\{?node\}?\|l_\{?node\}?\|ℓ_\{?node\}?)[^\n]{0,60}(S\(\|saturat\|grade)` | `ℓ_node` graded by `S`/saturation (CH-G receipt) |
| `P-I6` | `(self\.I_omega\|self\.rho)\s*[*/]\s*S\|I_omega\s*\*\s*S` (over `src/ave/**/*.py` only) | kinetic-side kernel in landed engine code |
| `P-CAT` | `(inerti\|kinetic\|mass densit)[^\n]{0,60}(S\(A\)\|√(1\|\\sqrt\{1\|kernel)` (over `universal-saturation-kernel-catalog.md` only) | inertial row in the A-034 catalog |

### §3.2 The classification rule (frozen; applied per hit, each hit quoted verbatim)

Every hit is quoted verbatim in the result doc with file:line and classified with a one-line
rationale into exactly one of:

- **CANON-LAW** — the content STATES an `I_ω`-amplitude functional form as physics in a KB
  leaf, manuscript volume, or landed engine code. **Frozen consequence: any CANON-LAW hit
  supersedes every absence-based receipt, the result headline says so, and the bin is
  BIN-SUPERSEDED-BY-CANON.**
- **ARCHIVE-STAGED** — the hit lies under `research/_archive/**` or its content is the
  E-073-canceled prescription. Reported (D5), never treated as canon.
- **DISCOURSE** — the content POSES the law's absence or reports on it (the FLAG-IOMEGA
  discourse: the approach-leak/last-bond docs, briefs, docket entries, this lane's dispatch).
- **NON-LAW** — mentions with no functional form (e.g. protein gyration radii, flux-tube
  moments).

### §3.3 Fireability (mandatory; a gate that cannot fail is not a gate)

- **FT-SCAN-ABS:** an absent sentinel string (`IOMEGA_SENTINEL_ABSENT_2026_08_06`) must return
  `0`/`0` on both methods.
- **FT-SCAN-PRES:** a present sentinel (a string verified to exist in the pinned tree, chosen
  and named in the driver before first run) must return identical non-empty hit sets on both
  methods.

---

## §4 — The gates (frozen; all comparisons exact)

| gate | what it certifies | frozen criterion |
|---|---|---|
| **G-SCAN** | two-method agreement | identical hit sets per pattern, both engines named in the JSON |
| **G-NC-P34** | reproduction control | `P-NC3`/`P-NC4` regexes byte-identical to the v1 prereg §5.1 battery rows (string equality against the quoted forms) |
| **G-A008-COLD** ★ | the delivered law preserves the cold-point pin | symbolic: `I_ω^eff(S=1) = I_ω` exactly, hence `G_c^eff/I_ω^eff` at `S=1` = the pinned ratio, via sympy substitution — for EVERY delivered branch (D1 and every conditional member) |
| **G-PAIR** ★ | the cancellation-lemma arithmetic | sympy: `simplify( (a_c − d + b_j + d)/2 − (a_c + b_j)/2 ) == 0` as a symbolic identity in `(a_c, b_j, d)` |
| **G-KNIFE-ARITH** ★ | the composed `p` per delivered branch | `p = (a + b)/2` computed independently by `fractions.Fraction` and `sympy.Rational` for the delivered `b` × `a ∈ {1, 2}`; each `p` mapped against the v2-adjudicated member table `{0.5: GC, 1.0: GC, 1.5: GC, 2.0: CO, 2.5: CO, 3.0: CO}`; a `p` outside the member set reports `NOT-A-FROZEN-MEMBER` |
| **G-CITE** | every load-bearing quote in the result doc | quote-registry entries `(file, line, excerpt)` re-verified at lane HEAD: excerpt must occur within ±2 lines of the registered line |
| **G-DET** | determinism | two full driver runs, identical canonical-JSON digest excluding runtime fields |

### §4.2 Fireability self-tests (each MUST fire)

| self-test | injection | must produce |
|---|---|---|
| **FT-A008** | a law with `I_ω^eff(S=1) = 2·I_ω` | `G-A008-COLD` FAIL |
| **FT-PAIR** | the broken shift `(a_c − d, b_j + 2d)` | nonzero symbolic residual |
| **FT-KNIFE** | `b = 3` injected against `a ∈ {1, 2}` | `p ∈ {2.0, 2.5}`, both mapping `CO` — the verdict-relevant flip is visible |
| **FT-CITE** | one registry entry with line perturbed by +7 and excerpt perturbed by one character | `G-CITE` FAIL |
| **FT-SCAN** | §3.3's sentinel pair | absent `0`/`0`; present identical non-empty |

### §4.4 Derived-constant second-method checks (pre-freeze, per SVA row 9)

| derived item | method 1 | method 2 |
|---|---|---|
| the v2 member table `{0.5,1.0,1.5}→GC, {2.0,2.5,3.0}→CO` | quoted from the v2 result headline/§ bins | re-derived from the v1 frozen `p_crit = 2` + the p = 2 knife-edge award note (`p = 2` awarded v1's frozen CHANNEL-OPENS) |
| sign convention `b > 0 ⇔ I_ω grows toward the wall` | the v1 §1.3 parameterization `I_ω^eff = I_ω·S^{−b}` | the v1 flag arithmetic: `(a, b) = (2, 3) ⇒ p = 2.5` reproduced exactly |

---

## §5 — The bins (frozen verdict vocabulary)

- **BIN-CONST-DERIVED** — ALL of R1–R6 verify AND no CANON-LAW hit: the lane delivers
  **`b = 0`** as DERIVED-from-canon-structure (a convergence of independently receipted
  mechanisms, each quoted); D2–D5 ship alongside.
- **BIN-RIDES** — a canon-grounded chain with ZERO un-derived links forces
  `∂I_ω/∂A_ε ≠ 0` at the static sub-yield bias: the lane delivers the derived form/exponent,
  and the result headline reports it as a **walk-falsifier** in those words.
- **BIN-SUPERSEDED-BY-CANON** — a CANON-LAW battery hit exists: the found law is quoted in the
  headline and the lane defers to it (its exponent, if power-law, is delivered as `b`).
- **BIN-CONDITIONAL** — receipts partially verify, or the only nonzero-`b` chains carry
  un-derived links: the lane delivers the conditional law with EVERY antecedent link
  enumerated (`b = 0` on the receipted members; the alternative exponent only on its named
  antecedent chain).
- **BIN-UNDERDETERMINED** — neither the CONST receipt set nor any RIDES chain completes: the
  lane delivers bounds only, and FLAG-IOMEGA stays minted.
- **STOP-A008** — any surviving candidate law fails `G-A008-COLD`: the lane STOPS, adjudicates
  nothing, and routes to the orchestrator (frozen: no re-tune, no re-derivation in this lane).

### §5.3 Global consequence clause (frozen)

`Any gate in §4 FAILS (outside its fireability injection) ⇒ this lane reports LAW-NOT-CERTIFIED,`
`adjudicates NO bin, ships its diagnostics in full, and routes to a successor with a new version`
`number. The fireability self-tests must each FIRE; a non-firing self-test is itself a gate`
`failure under this clause.`

---

## §6 — Fences (restated, binding)

1. **Rule 11:** the knife's frozen criterion (`p_crit = 2`, `Ω < 4θ`, the bins, the sweep) is
   untouched; this lane delivers the law only.
2. **Engine reads are receipts about the CODE** — the engine carries `I_ω` as a constant
   parameter; that is the gap being filled, not evidence of constancy (brief fence, honored in
   R7's CODE-class tag).
3. **FORK-3 is not adjudicated here** — only the provenance of the CH-R transfer is audited.
4. **The walk is context, not target** — symmetric reporting frozen at §0 row 8.
5. **No propagation:** result doc is research-class; mints nothing; edits no leaf; engine
   byte-untouched; `Regime IV` out of domain; pure-physics corpus rule observed.
6. **Freeze-first:** this prereg is committed and pushed ALONE before any driver code exists.

## §7 — Routing (post-result, all via the orchestrator's docket)

- The result doc + driver + number-check land on this branch; PR opens
  `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
- The delivered `b` (or conditional/bounds) is routed to the approach-leak successor via the
  docket; the pairing rule (D2) is routed wherever the corpus juxtaposes mixed-provenance
  `(a, b)` pairs; D5's archive surfacing is routed to the auditor lane.
