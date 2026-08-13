# R54 — The node has SIX degrees of freedom. The dilatation is a MODE, not a DOF. "Breathing" is retired. (2026-08-13)

**Grant, in chat, 2026-08-13:** *"6 makes sense and we should clarify what the dilation is, and deprecate the breathing language as it conflates continuous SM and QED with ee native/vacuum native language."*

**Class:** ruling — a DOF-count ruling plus a vocabulary retirement. Settles the standing 6-vs-7 question.

---

## §1 — THE COUNT: SIX

**A vacuum node carries six intrinsic degrees of freedom** — three translational **u** (→ E, capacitive) and three microrotational **ω** (→ B, inductive) — exactly as Axiom 1 states (`manuscript/common_equations/eq_axiom_1.tex:37`). **There is no seventh.**

**The evidence that decides it** (`research/2026-07-20_mechanical-commonmode-derivation_result.md:46`, merged 2026-07-20, and adopted **verbatim** into `manuscript/ave-kb/common/vocabulary-register.md:594` where it is called *"load-bearing and not a gloss"*):

> the A1-dilatation `θ = ∇·u` is the **longitudinal polarization of the vector displacement field** … It is **NOT a separate scalar DOF; it is a projection of the same 3-vector `u`**.

A projection of the three translational coordinates is not a fourth independent coordinate. **The seven-count double-counts.** The two sides were never symmetric in provenance: one is a ratified adoption with a derivation behind it, the other is an inventory line.

## §2 — WHAT THE DILATATION IS

Stated once, in three dialects, so no site has to guess:

| dialect | the object |
|---|---|
| **port / circuit (primary)** | the **A₁ common mode** — the in-phase pattern across a node's bond ports, the trivial irrep of the site symmetry |
| **mechanical** | the **dilatation** `θ = ∇·u` — the longitudinal projection of the displacement field |
| **network** | the node's own scalar state; the only pattern that carries net flux into the node (a differential pattern sums to zero and cannot) |

**The carve that resolves the confusion: a MODE is a pattern; a DOF is an independent coordinate.** The common mode is a *mode of the three translational DOF*, not a seventh DOF. This is the same distinction canon already draws one level over at `manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:111` — *"A mode is a coordinate; A is an operating point. Distinct objects."* — now applied to the mode/DOF pair as well: **operating point ≠ mode ≠ degree of freedom, three distinct things.**

## §3 — VOCABULARY: "BREATHING" IS RETIRED

**"Breathing" / "breathing mode" is RETIRED as a load-bearing noun**, per Grant's stated reason: it conflates continuum-field (SM/QED) language with EE-native / vacuum-native language. It also carries soliton-theory freight — an oscillating solution of a nonlinear field equation — which is not what this object is.

- **Canonical:** **the A₁ common mode** (or *the common mode* where the sector is unambiguous).
- **Mechanical dialect:** *the dilatation*, `θ = ∇·u`.
- **Retired:** *breathing*, *breathing mode*, *radial breathing*, *the breather* (the last already retired at R51 §2 — this extends the retirement to the whole family).

Existing occurrences are **preserved per Rule 12**; this governs new text and any re-derivation of an old passage.

## §4 — WHAT THIS RULING DOES *NOT* DECIDE

**It does not touch the energy ledger.** The Pythagorean store split `A² = ε² + κ² + V²` (`vol9/ch18-experimental-prints/index.md:43` and siblings) is an **energy** statement, not a DOF count. A projection can still carry its own storage term if the node's scalar state is stored somewhere the translational springs are not — and **where the reactances actually sit is an open question**: `eq_axiom_3.tex:24` puts the LC tank in the **bond**, `eq_axiom_1.tex:37` puts an LC oscillator at the **node**, and `kirchhoff-network-method.md` splits them (C at the node, L in the strut). **The sweep implementing this ruling must correct DOF counts and must NOT touch the store split**, which needs its own adjudication once the reactance placement is settled.

**It does not re-open** the A₁ ⊥ T₂ sector fence (`master-equation.md:20`), the mode-vs-operating-point carve, or the carrier question (z=3 srs ratified, engine on z=4 — unchanged).

## §5 — PROPAGATION (routed to the doc lane; nothing edited here)

Roughly **17 sites count seven** and **35+ count six**. The seven-counting sites take a dated correction, not a rewrite. Known seven-counting sites: `vol9/ch3-pin-port-configuration/index.md:17`; `vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:42,:45,:56,:59`; `18_experimental_prints.tex:61,:72`; `vol9/ch18-experimental-prints/index.md:43,:144`; `common/trampoline-framework.md:204`; `common/trampoline-analogy-primer.md:325,:410`; `vol3/condensed-matter/ch11-thermodynamics/mode-counting-heat-capacity.md:18`; `vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex:149`; `vol6/appendix/geometric-inevitability/g-star-derivation.md:18`; `backmatter/03_geometric_inevitability.tex:417,:495`; `src/scripts/vol_1_foundations/kit_core_diamond.py:27`; `common/historical-precedents.md:22`; `assets/3d_models/kit/README.md:43`.

**Two known hazards for that sweep.** (i) `src/tests/engine_acceptance/test_facade_p0_validate_on_known.py:118` labels six and enumerates seven in one comment — it is both a seven-site and a six-site. (ii) Two six-counting sites say *"not a seventh spatial DOF"* about the **saturation state A**, a different object — do not read those as denials of the dilatation (`01_general_description.tex:18`, `07_saturation_characteristics.tex:45`).

**Carries with it:** the mode-count sites that derive `ν_vac = 2/7`'s denominator from a seven-mode count are separately unlicensed per R52 §2, and that propagation is already owed. The two items should ride together — they touch the same lines.

## §6 — FENCES

Nothing here mints, edits a leaf or axiom, or moves a solidity; §5 is routing. Rule 12 applies to every corrected site. The store split (§4) is explicitly out of scope.
