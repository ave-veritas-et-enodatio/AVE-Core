# Walk record — the common-mode/operating-point layer carve, its four corrections, and the repaired 2×2 (2026-08-12)

**Class:** walk record. **Grade: CHAT-WALK, UN-AUDITED**, except where a line is tagged
**[RECEIPTED]** — those rest on a read-only two-engine corpus sweep run the same day (`git grep -F`
+ python `str.find` over an explicit `git ls-files` list; the box `grep` is ugrep and was not used
for any receipt). **Mints nothing. Edits no leaf, axiom, register, ruling, or engine file. Moves no
solidity. Rules nothing.**

**Provenance.** Grant + orchestrator, in chat, 2026-08-12, following R51 (#958), R52 (#960), R53
(#961). Grant's ask, verbatim: *"lets define exactly what the common mode shift/dlation is, and look
at what all the axioms say at once now that we can step back and challenge them with a new lens on
the K=2G and the modes/regimes/boundaries of the vacuum material and waves/projevtions"*, then
*"bring first principled thinking and fight the sm and qed creepage"*, then *"make sure to document
the chats/walks"*.

**Why this record leads with its own corrections.** The walk proposed a three-layer carve. A receipt
sweep was then run against it **with an explicit instruction to hunt for what contradicts it**. It
returned eleven contradictions, four of which break claims the orchestrator had asserted to Grant in
chat. Those are §1. What survived is §2, and it is stronger than what was proposed, because most of
it turned out to be canon's own text rediscovered.

---

## §1 — THE FOUR CORRECTIONS (orchestrator claims, withdrawn or repaired)

**C-A. "The GR import is inside Axiom 1" — WITHDRAWN. [RECEIPTED]**
Axiom 1 (`manuscript/common_equations/eq_axiom_1.tex:37`) says only: *"In the macroscopic continuum
limit, the lattice is a **Trace-Reversed Chiral LC Network** supporting intrinsic spin and trace-free
transverse EM wave propagation."* Two engines plus a full-file read: **zero** occurrences of `K`,
`2G`, `ν`, `Poisson`, or `bulk modulus` anywhere in the file. The axiom carries the compound noun,
already scoped to *the macroscopic continuum limit*, and never links it to `K = 2G`. The
identification is asserted in five other files (per R52 §6). **Axiom 1 is clean on this; the walk
put the import into it.**

**C-B. "The axiom set has no discrete dynamics" — WITHDRAWN. [RECEIPTED]**
`eq_axiom_3.tex:24` states: *"the bond-LC tank conserves `E = ½CV² + ½Φ²/L` exactly."* That is a
per-bond dynamical statement inside the continuum-limit axiom. The same axiom labels its density
*"the **per-node** electromagnetic vector potential `A_n`"* (`:16`) while integrating it as
`∫ℒ_node d⁴x` (`:18-19`). The structural claim was too strong: **the axioms do carry discrete
content; what they do not carry is a discrete equation of motion for the A₁ coordinate.** That
narrower statement is what survives, and it is walk-level, not receipted.

**C-C. The conjugacy claim (`V` and `θ = ∇·u` as one tank's two halves) — NOT SUPPORTED, and a
competing canonical reading exists. [RECEIPTED]**
`k4-port-irrep-decomposition.md:25` maps the A₁ port amplitude to *"Translational `u` (isotropic,
longitudinal)"*. If A₁ **is** the longitudinal projection of `u`, then `V` and `θ` are one sector's
field and its divergence, not conjugates. Two engines found **no canonical statement identifying**
the node scalar `V` with `θ = ∇·u`, and **none distinguishing them as conjugate**. Canon writes both
objects — `kirchhoff-network-method.md:18,19,34-41` (nodes are capacitors holding a scalar `V_i`;
struts are inductors carrying `I_ij`; `V_new = V_old + (Δt/C)(ΣI_in − ΣI_out)`) and
`vacuum-varactor-scatter-operator.md:64-65` (`V_i = V_i^inc + V_i^ref = V` shunt, alongside a
separate KCL equation) — **and never relates them.** See §5: this is now a stated fork, not a
finding.

**C-D. The three-layer carve — SUPERSEDED by §3's 2×2. [RECEIPTED]**
The proposed Layer 3 ("continuum readout — θ, ε₁₁, K, G, ν — model only") is contradicted by
ratified text using those objects as *state*: clause Q writes `∇·π = 0, θ = 0, ε₁₁ = 0` and `:75`
calls it *"a statement about the substrate's **state**"*; ε₁₁ is Axiom 5's *"THE BIAS"* (`:61`,
header `:37`) **and** the Axiom-4 kernel argument (`saturating-modulus-and-backreaction.md:51`:
`A = ε₁₁/ε_yield`); and the CI-enforced falsification net (`ave-kb/.index/SCHEMA.md:276`) states
*"the substrate has **ONE degree of freedom** (the operating point u₀\*)"* — the very object the walk
called "not a coordinate."

**One further correction, to the record rather than to the walk. [RECEIPTED]** A "routed ε₁₁-vs-A
item at `eq_axiom_4.tex:56-59`" has been carried in orchestrator working notes. **It is not in that
file.** A full-file read finds the only open marker at `:47` (the exponent sign/ontology selector,
`PENDING Grant`); `:56-59` is the four-line Gravity bullet with no marker. The ε₁₁-vs-A question is
real (it is C-3 above) but it is **not routed in the axiom text**, and should not be cited there.

---

## §2 — WHAT SURVIVES, AND WHOSE IT ACTUALLY IS

**S-1. The mode-vs-operating-point carve is CANON'S OWN, verbatim. [RECEIPTED]**
`manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:111`:

> *"The A₁ breathing MODE ≠ the saturation STATE A. The breathing mode … is a genuine kinematic
> coordinate the Master Equation integrates. The saturation-amplitude state A … is 'not a seventh
> spatial DOF' … **A mode is a coordinate; A is an operating point. Distinct objects.**"*

and `:45`: *"These are kinematic coordinates; the saturation-amplitude operating point A is a
separate object."* **The walk rediscovered a ratified carve and then bolted a third layer onto it.**
The two-object split needs no new record; it needs propagation (§6).

**S-2. Axiom 5 IS a DC circuit analysis — confirmed five ways, including by clause S naming
Kirchhoff. [RECEIPTED]** Title (`:51`) *"Axiom 5 — Substrate DC Bias (deposit · grade ·
quiescence)"*; `:52` *"Axiom 5 is that missing specification: the substrate's **DC operating
point**"*; `:70` *"Q (quiescence — the **DC operating point**)"*; `:75` *"the **quiescent reference
(Q-point)** that makes the potentials defined and clause G's elliptic solve well-posed"*; header
`:34` *"canonical operating-point noun: 'DC operating point / quiescent point (Q-point)'"*. And
clause S itself, `:59`: *"**Mass is an enclosed compression charge BY LAW** … and **Kirchhoff's
current law** / the derived conservation leg `∂ₜ(∇·π) = −∇·j_m` preserves it thereafter."*

**S-3. The standing debt is the AC small-signal step, in the axiom's own words. [RECEIPTED]**
Clause (c1), `:86`: *"Clause G's elliptic law is the **static abstraction of underived finite-speed
bias dynamics**: **an elliptic solve is instantaneous by construction, and the axiom does not write
what replaces it when the source moves.**"* The walk's contribution here is only the **restatement**:
in circuit practice this is the ordinary second step — solve DC, linearize, do AC — and naming it
that way makes the debt a well-posed engineering task rather than an open field-theory question.
**Walk-level framing on a receipted gap.**

**S-4. The first-principles node argument, offered as reasoning and not as a finding.** Drive all
four ports of a K4 node in phase: by tetrahedral symmetry the net vector sum is zero, so **A₁ does
not displace the node** — which is why it is orthogonal to the T₂ triplet. What it is instead is a
net flux at the node, and Axiom 1 makes every node an intrinsic LC oscillator, so that flux has
somewhere to go. **Un-receipted; and see §5, where C-C makes the follow-on step a fork rather than a
conclusion.**

---

## §3 — THE REPAIRED STRUCTURE: a 2×2, not three layers

The walk conflated *kinds of object* with *kinds of description*. Canon carries **two objects** and
**two descriptions of each**:

| | **discrete statement** | **continuum statement** |
|---|---|---|
| **coordinate** | the A₁ common mode, `(1,1,1,1)/2` port amplitude (`k4-port-irrep-decomposition.md:11,:22`) | `u∥`, and `θ = ∇·u` |
| **operating point** | `u₀*`, the bond ratio `ρ = k_a/k_s` | `ε₁₁`, `K/G` |

**This resolves every contradiction that killed the three-layer version:**
- **C-10 (A₁ ↔ translational u):** that table row is the **mapping between columns** for the
  coordinate row — not an identity, and not a category error.
- **C-3 (ε₁₁ is both bias and kernel argument):** ε₁₁ is the operating point's **continuum**
  statement. That is exactly why Axiom 5 owns it as THE BIAS *and* Axiom 4 consumes it as `A`.
- **C-1 / C-2 (clause Q and `def-l0ngdu` use θ as state):** in the continuum column the state **is**
  the field; no conflict with the discrete column.
- **C-5 (the CI-enforced "one degree of freedom" is the operating point):** a **vocabulary
  collision, not a physics contradiction** — a free parameter of the substrate versus a per-node
  kinematic coordinate. Two senses of "DOF" in one corpus. Worth a vocabulary ruling; not a defect.

**Status: walk-level.** The 2×2 is offered as the structure that survives the contradicts-hunt, not
as a ruling. Its own kill-check is §5.

---

## §4 — THE EE DICTIONARY READING (walk-level, and it fits clause G as written)

Reading the DC sector with the standard network dictionary rather than by field-index matching:

| substrate object | EE reading | consequence |
|---|---|---|
| `u` | the flux / displacement field (a **D**-like object) | clause S's `∮u·n̂` is a flux integral |
| `θ = ∇·u` | the **source density** | Gauss/KCL: net flux out = enclosed source |
| `ε₁₁` | the **potential** | clause G is **Poisson's equation** |
| clause S, `∮_S u·n̂ = 4πB(M)` (`eq_axiom_5.tex:56`) | Gauss's law with `B(M)` the enclosed charge | **mass = a node where the flux does not balance** |
| clause G (`:63-65`) | the **DC operating-point solve** | instantaneous *by construction*, not by a causality claim |
| node `C` + bond `L` | the reactances the DC solve sets aside | restoring them **is** the owed AC analysis (S-3) |

This is a better fit than the withdrawn conjugacy reading (C-C) and it is **what clause G already
writes**; the walk's contribution is the naming, not the physics. One consequence worth holding
loosely: if mass is a source term, it is not a *thing in* the lattice but a **boundary condition on
it** — reconcilable with the trapped-resonance picture because a topological winding presents as a
monopole source in the far field. **Un-receipted; flagged, not banked.**

---

## §5 — THE OPEN FORK (this walk's actual deliverable)

**Is the A₁ common mode's continuum image the longitudinal displacement `u∥`, or the node
potential `V`?** [RECEIPTED that canon asserts both and reconciles neither.]

- **Arm A — `u∥`:** `k4-port-irrep-decomposition.md:25`, *"A₁ Cosserat mapping | Translational `u`
  (isotropic, longitudinal)"*. Under this arm `θ = ∇·u` is the A₁ sector's own divergence and
  `master-equation.md:26` / `def-l0ngdu` read straight through.
- **Arm B — the node potential:** `kirchhoff-network-method.md:18,34-41` builds the entire network
  on a node-local scalar `V_i` updated by net branch flux; `vacuum-varactor-scatter-operator.md:64-65`
  writes `V_i = V_i^inc + V_i^ref = V` (shunt) **and** KCL as two separate equations at one node.

**Canon never relates them** (two engines, zero hits either way). The arms are not obviously
equivalent: one makes A₁ a displacement component, the other makes it a potential whose *rate*
tracks the flux. **This is the question the walk stumbled into and could not settle, and it has a
clean discrete calculation waiting behind it** — which is why it is recorded as a fork rather than
resolved by preference.

---

## §6 — ROUTED (flag-don't-fix; nothing edited by this record)

1. **★ R52's ruling has not propagated, and the move it declares unlicensed is live at five-plus
   sites. [RECEIPTED]** R52 §2 rules the "ν-denominator 7 = a mode count" reading **not licensed**
   and says *"do not merge the two sevens."* Unedited at `origin/main`:
   `mode-counting-heat-capacity.md:14` (*"The denominator n = 7 **counts the independent compliance
   modes per node**"*), `vol6/appendix/geometric-inevitability/g-star-derivation.md:18`,
   `alpha-s-derivation.md:21,35`, `manuscript/backmatter/03_geometric_inevitability.tex:417,475,495`,
   `manuscript/vol_3_macroscopic/chapters/11_thermodynamics_and_entropy.tex:149`. A docket ruling is
   not propagation. **Doc-lane item.**
2. **The "gauge" epistemic-grade split in a SOLID node. [RECEIPTED]** `vocabulary-register.md:870`
   (`def-l0ngdu`, status *SOLID, Grant-ratified 2026-07-20*) carries one sentence with two grades:
   the ∇·u half is asserted as a lattice fact (*"rides the gapless lattice-computed P-branch"*),
   while the ∇·A half is explicitly grounded in *the written Lagrangian's* curl-only form (*"the
   curl-only EM Lagrangian gives it no restoring force"*). **Creepage note:** QED's word *gauge*
   carries the theorem *unphysical / unobservable / removable*; *"no term was written in this
   action"* does not establish that theorem. Per the standing no-QED-garbage rule, the longitudinal
   scalar is real and "gauge" is the word that deletes it. **Adjudication item, not a fix.**
3. **The 6-vs-7 enumeration seam is corpus-wide, not vol9-local. [RECEIPTED]** ~17 sites count seven
   (including `vol9/ch3-pin-port-configuration/index.md:17`, and three that call the volumetric mode
   a *degree of freedom*); ~35+ count six (including `eq_axiom_1.tex:37`, `ave-kb/CLAUDE.md:70`, and
   engine code). One shipped test carries both at once: `test_facade_p0_validate_on_known.py:118`,
   *"# 6 DOF/node: u (3) + omega (3) + the A1 node-field scalar (+1)"* — arithmetically seven,
   labelled six. **This is Grant's standing open question** (does the breathing mode belong inside
   Axiom 1's enumeration, or does Axiom 1's six count only the LC stores with Axiom 5 owning the
   scalar?) and it is **one question at many sites**, already cross-linked with #957's G1 re-frame
   and D1.
4. **Cite drift. [RECEIPTED]** `03_pin_port_configuration.tex:45` cites the 7-mode compliance to
   `common/trampoline-framework.md:200`; the cited sentence is at **`:204`** (4-line drift).
5. **Minor:** the withdrawn-narrowing block in `eq_axiom_3.tex` runs **`:75-81`**, not `:77-81` as
   carried in orchestrator notes.

---

## §7 — FENCES AND KILL-CHECKS

**Fences.** Nothing here is ratified. The 2×2 (§3), the EE dictionary reading (§4), and the node
argument (S-4) are **walk-level**; §1's corrections and the §2/§6 receipts rest on the two-engine
sweep. No axiom is amended, no vocabulary retired, no solidity moved, nothing minted. The sector
fences stand (R51 §7; `master-equation.md:20`'s winding/scalar fence). Per R53, this walk is
**interior structure** — it is recorded because it corrects the record and surfaces a fork, not
because it is chartered work.

**Kill-checks.** (i) **§5's fork decides §3 and §4** — if Arm A holds, the coordinate column is a
displacement and the potential reading in §4 needs re-derivation; if Arm B holds,
`k4-port-irrep-decomposition.md:25`'s mapping row needs a scoping note. (ii) **If the 2×2's
"vocabulary collision" reading of C-5 is wrong** — i.e. if canon means the same sense of "DOF" in
both places — the 2×2 fails and the operating point is a coordinate after all. (iii) **§4 is
un-receipted and must not be cited as canon**; clause G's Poisson structure is canon, the dictionary
gloss around it is this walk's.
