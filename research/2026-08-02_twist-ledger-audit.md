# The twist-energy ledger audit — does $m_ec^2$ account for the (2,3) winding's Cosserat twist energy? (2026-08-02)

**Class: READ-ONLY CORPUS AUDIT. IMPLEMENTER-LANE output. NOT adversarially reviewed. Mints no `clm-`/`def-`/`exp-`/`sup-`. Ratifies nothing. Banks no verdict Grant has not called. Engine byte-untouched — no solver written, no driver run; the one arithmetic in §6 is a paper-ballpark on canon-supplied constants, not a simulation.** All criteria herein DRAFT-NOT-FROZEN. Nothing below is Grant-ratified except the verbatim `[sic]` quote marked as his.

**Provenance.** Item 13 of the standing frontier queue, sharpened, on Grant's GO (2026-08-02, verbatim `[sic]`: *"10, GO"*). Base: `origin/main` @ `ac165cf2`.

**Discipline applied:** `verify-before-cite` (v1.6 ship-time currency — all 19 load-bearing cites re-verified two-method at the tip, ledger in §9), `consistency-vs-emergence` (per-term class tags throughout), `phase-space-coordinate-check` (§3.4 — the load-bearing coordinate question), `ave-dimensional-provenance-check` shape (§6.1 — a live units defect found), flag-don't-fix (§7 — five flags surfaced, zero repaired), Rule 11 / Rule 12 (no post-hoc criterion drops; no slot refills).

---

## §0 The walk frame (Grant's physical picture — carried with attribution, verbatim `[sic]`)

> *"the twist feels like stored negative tension. Almost like a paperclip unfolded and the two ends pulled apart, then you bend them together until they just barely catch eachother and form a closed shape, but could unsnap at anytime, there's spring tension in the clip still?"*

Orchestrator refinements, recorded as **walk-level, NOT canon**:

- The **catch is a linking number** — the clip cannot unsnap without its antiparticle. Annihilation is the topologically-gated release; **charge conservation ≡ electron stability** is the same statement twice.
- The **stored energy is positive**; "negative tension" names the **direction of the pre-load**, not a negative energy.

The frame's testable content is a **ledger** question, and it is sharp: *a pre-loaded clip stores energy in the pre-load.* If the substrate's (2,3) winding is a pre-loaded twist on the Cosserat couple-stress grade, that pre-load has an energy. Either $m_ec^2$ already counts it, or canon says it costs nothing, or it is unbooked.

---

## §1 The question, and why it is the SAME question as the generation spectrum

**The question.** Does canon's mass-closure chain account for the (2,3) winding's Cosserat twist energy **inside** $m_ec^2$, **count it zero**, or **leave it unaccounted**?

**The enrichment that makes it one question, not two.** Canon says the muon is the electron's *same* $(2,3)$ plus **one quantum of Cosserat torsional excitation** — verified verbatim at [`manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md):43:

> *"A heavy fermion, such as a **Muon**, possesses the same real-space unknot topology and the same $(2, 3)$ phase-space winding pattern as the electron, but with **one quantum of Cosserat torsional excitation** added on top"*

and the generation ladder is the **Cosserat-torsion ladder on fixed (2,3)** — [`torus-knot-uniqueness.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md):110:

> *"Higher-mass leptons stay at (2,3) topology — they don't climb the (p,q) torus-knot ladder; they climb the Cosserat-torsion excitation ladder."*

So the twist ledger and the generation ledger are **the same ledger**. If the ground-state twist term is unbooked in $m_ec^2$, then $m_\mu - m_e$ is that same unbooked ledger's **first excited rung** — and Grant's paperclip is *generations as more pre-load in the same clip*. This is the doc's spine: **§2 audits the $n=0$ rung, §4 audits the $n=0\to1$ rung, §5 shows they fail together.**

The sector identification carrying the ladder is canon's own flagged weak point — [`vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md):544 (`clm-zw6mut`, solidity 0.60, *"use as input only, don't build deeper"*):

> *"the three-Cosserat-sector-to-three-lepton-generation identification (translation/torsion/curvature-twist) is **asserted, not derived** from the four axioms"*

---

## §2 TRACE — the mass-closure sum, end to end, every term enumerated

Four independent statements of the electron's rest-energy budget exist in canon. **Every one of them is a two-term-or-fewer sum, and not one of them contains a Cosserat-rotational / couple-stress ($\gamma_c$) term.**

### 2.1 The four budget statements

| # | Statement | Terms in the sum | Any $\gamma_c$ / couple-stress term? | Class |
|---|---|---|---|---|
| **T1** | [`mass-closure-theorem.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md):52 — $E_{\text{reactive}} = \tfrac12 L_{\text{tube}} I_{\max}^2 = \tfrac12 C_{\text{tube}} V_{\text{peak}}^2$ | **1** (one reactive store, stated twice in its two conjugate faces) | **NO** | **A — identity** (see 2.2) |
| **T2** | [`mass-closure-theorem.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md):54 — the LC-tank virial: peak-amplitude equality $\tfrac12 LI^2_{\max} = \tfrac12 CV^2_{\text{peak}}$, *"the two stores are in phase quadrature"* | **2** (magnetic ⊕ electric reactance) | **NO** | **A — identity** |
| **T3** | [`relativistic-inductor-newtonian-limit.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md):24 — $E_L = E_C = \tfrac{m_ec^2}{2},\ \ E_L + E_C = m_ec^2$ | **2**, and **explicitly closed** — the two halves are each exactly $\tfrac12 m_ec^2$ and they **sum to the whole** | **NO** — and no slot remains | **A — identity** |
| **T4** | [`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):48 — $U_{AVE} = \oint_{C_{loop}} T_{EM}\,ds = T_{EM}\cdot \ell_{node} = 1.0\,m_ec^2$ | **1** (a 1-D line integral of the string tension along the loop) | **NO** — a 1-D scalar-tension integral carries no rotational DOF at all | **A — identity** (see 2.2) |

**T3 is the load-bearing one for this audit.** It is the only statement that writes the budget as an explicit *closed sum over named sectors*, and it closes at **two**: inductive ⊕ capacitive, $\tfrac12 + \tfrac12 = 1$. There is **no third slot**. The [`vol4/simulation/ch14`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md) and [`electron-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md):165 restatements ("*the soliton's total energy decomposes 50/50 inductive/capacitive by virial equipartition*") propagate the same two-term closure.

### 2.2 The load-bearing finding: the sum was never evaluated as a sum

Canon's own claim-quality entry for the mass-closure theorem — [`vol2/claim-quality.md`](../manuscript/ave-kb/vol2/claim-quality.md):1256, `clm-ka5zdx`, **confidence 0.50 / solidity 0.50, "use as input only, don't build deeper"** — states the situation exactly:

> *"the load-bearing final identity $E_{reactive}=mc^2$ is reached by **identifying** the closed-loop standing-wave invariant with the rest energy (**no quantity computed**) — honestly labeled 'a statement about what mass IS, not a computational program.'"*

and its own open strengthen-by item, [`vol2/claim-quality.md`](../manuscript/ave-kb/vol2/claim-quality.md):1258, is *the unbuilt ledger*:

> *"Compute $E_{reactive}=\frac12 L_{tube}I_{max}^2$ for the unknot and show it equals $m_ec^2$ **numerically**, closing the identification."*

**Consequence for the twist question, stated precisely.** The mass-closure chain is a **one-term identification**, not a ledger. There is therefore **no enumerated sum for the $\gamma_c$ term to be inside of or excluded from**. The question "is the twist energy absorbed?" cannot be answered ABSORBED, because nothing was ever added up.

The same holds for T4: $T_{EM} \equiv m_ec^2/\ell_{node}$ is *defined from* $m_e$ ([`constants.py`](../src/ave/core/constants.py):493, `T_EM: float = (M_E * C_0**2) / L_NODE`), so $U_{AVE} = T_{EM}\cdot\ell_{node} = 1.0\,m_ec^2$ is **algebraically forced** — verified numerically to 1.000000 in §6. It is a **Class-A definitional identity**, not a computation that could have come out ≠ 1 and thereby left or refused room for a twist term. The "1.0" is not evidence of exhaustion; it is evidence of tautology.

> **Consistency-vs-emergence tag for §2 as a whole: Class A (definitional identity) throughout.** No term in the four budget statements is a Class-D emergence result. This is not a criticism of the chain — canon labels it honestly at :1256 — but it is decisive for the ledger question: *a tautology has no residual, so it can neither absorb nor exclude a physical term.*

### 2.3 The one named sub-leading term canon DOES carry — and it is not the twist

[`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):41 names a $\approx\tfrac{\alpha}{2}m_ec^2$ piece: *"bounding this integral purely at the 3D spherical geometry of the topological perimeter ($\ell_{node}$) captures only the $\approx\frac{\alpha}{2}m_ec^2$ linear-field component residing in the non-saturated surrounding vacuum space (Regime I)."* That is the **exterior linear far-field** of the $\varepsilon$/EM sector — a different object from an interior couple-stress store on the mechanical $\omega$ grade. It is recorded here so the audit cannot be answered with "the $\alpha/2$ term is the twist term." It is not.

### 2.4 Where the A1 ⊥ T2 ruling puts the twist — and what it does NOT say

The Grant-ratified grade split is at [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 — **mass = A1 dilatation; charge/spin = the Cosserat (2,3) micro-rotation winding on T2; A1 ⊥ T2, never cross-wire** (PR#260). Two things follow, and they must not be run together:

- **(a) What it DOES say.** Mass is *booked on* A1. The (2,3) winding is *booked on* T2. Grade orthogonality is the genesis-24 no-double-count guard.
- **(b) What it does NOT say — verified absence.** It does **not** say the T2 grade **stores zero energy**. A two-method sweep for any statement of the form *"T2 stores no / zero rest energy"* returns **0 hits** across `manuscript/` + `research/` (commands in §9). *Which sector mass is booked on* and *whether the other sector stores energy* are different propositions. **The corpus asserts the first and is silent on the second.**

This is the crux. Under (a) alone, an auditor may slide to "mass is A1, so T2 energy is irrelevant to $m_ec^2$" — but that is a **sector-ownership claim doing an energy-ledger job it was never derived to do**. If the T2 couple-stress grade stores a nonzero $E_{\text{twist}}$ and the electron is a single object of rest energy $m_ec^2$, that energy is *in the object's rest frame* and must appear in its invariant mass, whichever grade hosts it. Nothing in canon closes that gap.

---

## §3 SWEEP — every $\gamma_c$ / couple-stress / torsional-energy site in canon

Patterns swept (two-method, `git grep` on `origin/main` ⊕ worktree `grep -rn`; commands in §9): `gamma_c` · `γ_c` · `couple.stress` · `torsion.*energy|energy.*torsion` · `twist energy` · `E_twist|U_twist|E_\{tw\}` · `Călugăreanu|Lk *= *Tw|Tw *\+ *Wr|writhe`. **39 KB files carry a `γ_c` / couple-stress token** (excluding the generated `.index/`).

### 3.1 The energy-bearing sites — and what each computes

| Site | What it is | Is it the ground-state (2,3) twist energy? |
|---|---|---|
| [`weak-coupling.md`](../manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/weak-coupling.md):15 — $E_{\text{twist}} = \dfrac{T_{EM}^2}{4\pi\varepsilon_T r_0}$ | **The only closed-form "torsional self-energy" in canon.** A Coulomb-analog $\nabla^2\theta=0$, $\theta\propto1/r$ integral with a **torsional permittivity $\varepsilon_T$** and UV cutoff $r_0=\ell_{node}/2\pi$ | **NO.** It is the **$W$-boson chirality-MISMATCH** self-energy — the cost of a twist that *opposes* lattice chirality (:20). It is parameterized by $\varepsilon_T$, **not by $\gamma_c$**, and it is a **two-vertex $\alpha^2$ transient** (:30-35), explicitly contrasted against the leptons' single-vertex static defect at [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):68 |
| [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py):713 — `W = (2/3)G(tr eps)^2 + G eps_sym·eps_sym + G_c eps_antisym·eps_antisym + gamma kappa·kappa + …` | **The engine HAS the term.** `gamma kappa·kappa` **is** the couple-stress twist-energy density, and the module *"Supports the electron topological sector (c = 3) via a Sutcliffe-style (2,3)-torus-knot initial ansatz, relaxes to the ground state by gradient descent on the Cosserat energy functional"* (:6-9) | **The capability exists; the number was never booked against $m_ec^2$.** Moduli are pinned `G = G_c = gamma = rho_vac = 1` in **natural units** (:12, `self.gamma = 1.0` at :942) — a dimensionless decree, not the canonical $\xi_{K2}$ calibration. No result doc converts a relaxed-(2,3) `gamma kappa·kappa` integral into MeV or into a fraction of $m_ec^2$. **Two-method absence-check in §9.** |
| [`genesis-chord-falsification-ledger.md`](../manuscript/ave-kb/common/genesis-chord-falsification-ledger.md):47 — $E_{curv}(\kappa)=\gamma(\kappa^2-\kappa^4/\omega_{yield}^2)$ | The Axiom-4-**saturated** curvature energy, used to prove the ω-sector self-trap is non-convex and disperses | **NO** — it is a *stability* argument about dynamics class, not a rest-energy magnitude. Its own diagnostic notes the coupled engine *"routes saturation only to the K4 V-sector, never the ω dynamics"* |
| [`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559 — *"This $\omega_B$ is **COSTLY** (couple-stress energy via $G_c$)"* | Canon's plainest statement that **microrotation costs energy** | Affirms the term is real and positive; assigns it no magnitude and does not enter it into any mass budget |
| [`gauge-boson-masses.md`](../manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39 — $l_c=\sqrt{\gamma_c/G_{vac}}$ = weak-force range | The **only place $\gamma_c$'s VALUE is fixed** | Fixes $\gamma_c$ **by identification with $r_W\sim10^{-18}$ m** — see §6.2, this is the magnitude gate |
| [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41 | The rotational band gap $m^2=4G_c/I_\omega$ = *"the **GAPPED mechanical Cosserat mass** — … the winding's mechanical mass"* | **See §3.3 — this is the decisive site.** |

**Two-method absence result (the negation, with its commands shown in §9.3): there is NO site in `manuscript/` or `research/` that computes a $\gamma_c$-parameterized twist energy for the electron's ground-state (2,3) configuration and expresses it in units of $m_ec^2$.** Zero hits, both methods. The `E_twist` symbol exists in canon exactly once as a physics formula (plus its index row and LaTeX mirror), and **it belongs to the $W$**.

### 3.2 The Călugăreanu leg — the ground-state twist is geometrically NONZERO

$\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}$ is canonical and **Grant-adjudicated (2026-07-09, R1)** at [`chirality-and-antimatter.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md):10:

> *"by the **Călugăreanu relation** $\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}$, the internal twist $\mathrm{Tw}$ (the charge-defining LH Beltrami helicity) and the real-space loop **writhe** $\mathrm{Wr}$ are two lawful readings of the one conserved linking number $\mathrm{Lk}$ (= charge)."*

and quantified at [`research/2026-06-07_vacuum-characterization-program.md`](2026-06-07_vacuum-characterization-program.md):59:

> `| **Knot topology** | `Lk = Tw + Wr` | `(2,3)`; `Tw = q/p = 540°/rev`; `Wr` | ✓ (twist test, PR #123) |`

So for the **electron's own ground state**, $\mathrm{Tw} = q/p = 3/2$ turns per revolution $= 540°$/rev. **The ground-state twist is not zero. It is one-and-a-half turns.** That is exactly the pre-load in Grant's clip, and canon quantifies it — geometrically. It has never been priced.

(PR #123 verified: *"α-as-twist test: (2,3) flux-tube cross-section TWIST is α-free but ≠ 1/137 (Rule 11 negative)"*, merged 2026-06-08 — a **geometry** test on whether the twist rate equals $\alpha$; it computed no energy.)

### 3.3 ★The decisive site — canon books a NONZERO winding-sector mass and EXCLUDES it from $m_ec^2$ by declaration

[`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41-42, the **Grant-adjudicated G2-dissolution ruling** (`research/2026-07-03_g2-photon-relabel_note.md`), verbatim:

> *"- the **rotational BAND gap** $m^2 = 4G_c/I_\omega$ (the $\omega$ sector) is the **GAPPED mechanical Cosserat mass** — the Yukawa-screened, short-range mass of the *static winding* sector (`clm-wcoul2`), i.e. the couple-stress stiffness that makes the node micro-rotation massive. This is the flywheel/spin **clock gap** and the winding's mechanical mass, **NOT the electron's rest-energy store**.*
> *- the **electron's REST-ENERGY store** is the **A1 breather / dilatation depression** … Orthogonal ($A_1 \perp T_2$) to the rotational band gap."*

**This is the sharpest available answer, and it is neither ABSORBED nor ZERO.** Canon (i) asserts a **nonzero** mechanical mass on the winding sector, sourced by the couple-stress stiffness, and (ii) declares it **outside** the electron's rest-energy store. The exclusion is by **grade-orthogonality declaration**, not by a computation showing the quantity vanishes and not by a mechanism for where a nonzero rest-frame energy goes if not into the invariant mass.

The ruling is *correct as far as it goes*: a band-gap **frequency** of the ω sector and an **energy store** are genuinely different questions (:43), and the ruling was made to dissolve a different tension (the Verlet driver's ω-gap vs `mass = A1`). **But the twist-ledger question it does not answer is: the electron's ω sector is not in its ground state — it carries a static $\mathrm{Tw}=3/2$ winding on a grade canon calls massive and costly. That configuration's stored couple-stress energy sits in the electron's rest frame.** Grade-orthogonality says which sector *owns the label "mass"*; it does not say the other sector's stored energy is absent from the invariant. Flagged, not resolved — §7 FLAG-1.

### 3.4 Phase-space vs real-space — the coordinate check, and why it does NOT dissolve the question

Per A46 / `phase-space-coordinate-check`, the first defense is: *the (2,3) is a **phase-space** winding on the Clifford torus in $(V_{inc},V_{ref})$; the real-space body is the $0_1$ **unknot**; so a real-space couple-stress integral $\int\gamma_c|\nabla\omega|^2 d^3x$ is a coordinate-category error.* That defense is **live and correct as a caution** (INVARIANT-N1; [`electron-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md):31, *"The $(2,3)$ 'trefoil' is the phase-space winding pattern, NOT a real-space trefoil knot"*).

**It does not dissolve the question, because canon itself puts the (2,3) on the real mechanical couple-stress grade.** [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):24, the 2026-07-03 rotation-flavor tag, verbatim:

> *"the `(2,3)` WINDING rotation named above is the **GAPPED mechanical Cosserat micro-rotation ω** (couple-stress / curvature grade; the Yukawa-screened `clm-wcoul2` field; carries the *static* (2,3) Link on the shear sector). It is **NOT** the **massless EM-inductive rotation**…"*

So the (2,3) has a **real-space mechanical-ω image on the couple-stress/curvature grade**, by canon's own un-conflation tag. A $\gamma_c|\nabla\omega|^2$ energy of that image is **well-posed in matching coordinates** — it is an integral over the same mechanical ω field canon says carries the static Link. The Călugăreanu $\mathrm{Wr}$ face (§3.2) is likewise explicitly the **real-space** reading of the same conserved budget. **Coordinate check: PASSES. The question survives it.**

---

## §4 THE GENERATION SIDE — how canon books $m_\mu - m_e$, and whether that booking is consistent with the electron's own closure

### 4.1 What canon actually does with the muon

| Statement | Cite | What it books |
|---|---|---|
| *"The electron is the $0_1$ unknot ground state. **No torsional excitation is present**"* then $m_e = T_{EM}\ell_{node}/c^2 = \hbar/(\ell_{node}c)$ | [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):21,24 | **The $n=0$ rung, declared torsion-free.** But the $m_e$ formula it introduces is the **same Class-A definitional identity** as T4 (§2.2) — $T_{EM}\equiv m_ec^2/\ell_{node}$ |
| *"the muon is the $0_1$ unknot absorbing exactly **one quantum of chiral torsional coupling**"*; $m_\mu = m_e/(\alpha\sqrt{3/7})$ | [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):33,39 | **The $n=1$ rung as a multiplicative closed form on $m_e$** |
| Electron = *"(2,3) trefoil + **0** Cosserat torsion quanta"* / Muon = *"(2,3) trefoil + **1** Cosserat torsion quantum"* | [`torus-knot-uniqueness.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md):106-107 | The **ladder-quantum count**, $n=0$ and $n=1$ |
| *"the helical spiral **adds energy** to the rotational DOF"* | [`q-g27-muon-cosserat-saliency.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md) §Sign | **Canon's own statement that torsion energy is ADDITIVE and lives on the rotational DOF** |
| *"the geometric deformation (twist, curvature) describes a pattern of **dielectric saturation density** … The muon's 'twist' is a **helical modulation of impedance density** … **Neither involves physical displacement of lattice nodes**."* | [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17 | **A THIRD, incompatible booking** — see §4.3 |
| Muon's extra helical twist $\Phi_{\text{twist}} = 2\pi\sqrt{3/7}\approx236°$ per unknot traverse | [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):51 | The $n=1$ rung's **geometric** twist increment |

**So: WHERE is $m_\mu-m_e$ stored, physically?** Canon gives **three mutually inconsistent answers** and adjudicates none:
1. **rotational DOF / Cosserat torsion** (q-g27 §Sign; the whole "torsion ladder" framing),
2. **dielectric saturation density / impedance modulation, explicitly NOT node displacement** ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17) — an $\varepsilon$-sector, not a couple-stress store,
3. **A1, by the standing `mass = A1` ruling** (PR#260) — which, applied to the muon, says the extra 205.8 $m_ec^2$ is A1 dilatation, contradicting (1).

**Consistency-vs-emergence tag for the whole lepton table: canon's own, verbatim** ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):84): *"**matched closed-form CONSISTENCY — NO solver** … evaluated from the CODATA-input $\alpha$ and $p_c$ with $m_e$ as the input scale — **not** 'derived' or 'emergent', and **not** solver-backed."* **Class C.** Plus the standing `clm-zw6mut` finding that the sector→generation identification *"is asserted, not derived"* ([`vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md):544) and the **live 🔴 OPEN FLAG** that $\sqrt{3/7}=\sqrt{1-2\nu_{vac}}$ is the **bulk/dilatational** elastic signature wearing a *"PAT torsion-shear"* label ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):29, Grant adjudication pending).

**★Note the coherence between two independent open flags.** The $\sqrt{3/7}$-is-bulk-not-shear flag (:29) and booking-#3 (`mass = A1`) point the **same way**: the muon's excess reads as **dilatational/A1**, not couple-stress/T2 — which would make the "Cosserat torsion ladder" a **mislabel** of an A1 ladder. That is a *possible resolution*, and it is **NOT adopted here**: it is an unadjudicated inference, and adopting it would silently refill a slot Rule 12 says stays empty. Recorded as a Grant walk question (§8, Q4).

### 4.2 Is the muon booking consistent with the electron's own closure? — NO, in two independent ways

**(a) The energy-arithmetic inconsistency.** If the ladder is real and physical, an $n=0$ ground state on a **massive, costly** grade with a geometrically nonzero $\mathrm{Tw}=3/2$ carries a nonzero ground-rung energy $E_0$ (the zero-point of any real oscillator ladder is not zero). Canon's electron closure has **no slot for $E_0$** (§2, T3's $\tfrac12+\tfrac12$ is closed) and canon's ladder declares $n=0$ excitation-free ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):21). **These are compatible only if the ground-state (2,3) twist costs exactly zero — which no site derives, and which §3.3 + §3.2 + [`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559 all contradict.**

**(b) The spacing inconsistency (quantitative, §6).** The $n=0\to1$ rung costs $205.8\,m_ec^2$ (CODATA anchors) / $208.3\,m_ec^2$ (canon's closed form). The ground-rung twist energy, priced from canon's own $\gamma_c$ inputs on the **lattice-scale** normalization, lands at $\mathbf{O(10)-O(10^2)}\,m_ec^2$ (§6.3). **A ladder whose ground rung is within one order of magnitude of its first spacing is not a small perturbation on a torsion-free ground state** — it means the electron's own mass is *substantially* the twist energy the closure omits, and $m_e$ would not be the "torsion-free" anchor the whole ladder is built on. On the **weak-scale** normalization it is $\sim10^{-11}\,m_ec^2$ and the problem evaporates entirely. **The two readings are 12 orders apart and canon has not chosen — §6.2.**

### 4.3 What "no torsional excitation is present" does and does not zero — the precise scope

This is the closest thing canon has to a **ZERO** answer, so its scope must be exact.

- **It DOES zero:** the **excitation-ladder quantum count**, $n_{\text{torsion}}=0$ for the electron. Confirmed by the parallel wording at [`torus-knot-uniqueness.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md):106 (*"+ **0** Cosserat torsion quanta"*).
- **It does NOT zero:** the **couple-stress energy of the ground-state (2,3) winding itself**. The muon carries the *same* (2,3) (theory.md:43), so the (2,3)'s own twist is **common-mode across all three generations** — it **cancels identically out of every mass DIFFERENCE** and therefore is invisible to the entire ladder. The ladder can be exactly right about $m_\mu-m_e$ and say nothing whatsoever about whether the common-mode ground twist is priced into $m_e$.

**That is the whole finding in one sentence: the ground-state twist is the common-mode term the difference-ladder is structurally blind to, and the electron's own closure is a definitional identity with no ledger to catch it.**

---

## §5 CLASSIFICATION

> ### VERDICT: **UNACCOUNTED.**
> Not ABSORBED — §2.2: the mass-closure sum was **never evaluated as a sum** (`clm-ka5zdx` rationale, verbatim: *"no quantity computed"*), so there is no ledger for a $\gamma_c$ term to be inside of; and the two sites that *do* write a closed sum (T3's $\tfrac12+\tfrac12$; T4's 1-D $\oint T_{EM}ds$) are **Class-A definitional identities** that are algebraically forced to $1.0\,m_ec^2$ and therefore neither absorb nor exclude anything physical.
> Not ZERO — §4.3: the only zero canon states ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):21) zeroes the **ladder quantum count**, not the ground (2,3)'s couple-stress energy; and canon separately affirms that the (2,3) rides the **couple-stress/curvature grade** ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):24), that microrotation is **"COSTLY"** ([`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559), that the ground-state twist is geometrically $\mathrm{Tw}=3/2$ turns (§3.2), and that the winding sector carries a **nonzero** gapped mechanical mass ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41).
> **The sharpest canon statement is an EXCLUSION-BY-DECLARATION of a nonzero quantity** (§3.3): the winding sector's mechanical mass is asserted real and asserted *"NOT the electron's rest-energy store"*, on grade-orthogonality grounds, with no computation that it vanishes and no account of where a rest-frame energy goes if not into the invariant mass.

**Honest size of the hole (the two-sided answer, §6):** the magnitude is **gated on an already-flagged, unadjudicated symbol collision** — canon carries **two** Cosserat lengths, both written $\ell_c=\sqrt{\text{couple-stress}/\text{shear}}$, **6 orders of magnitude apart** ([`constants.py`](../src/ave/core/constants.py):331-337, *"Surfaced for auditor adjudication … not silently merged"*). Since $E_{\text{twist}}\propto\gamma_c\propto\ell_c^2$, the ballpark spans **12 orders**:
- **lattice-scale $\ell_c=\sqrt6\,\ell_{node}$ → $E_{\text{twist}}\sim 2\times10^{1}$ to $2\times10^{2}\ m_ec^2$** — the hole is *larger than the particle*, and the ledger is broken.
- **weak-scale $\ell_c\approx10^{-18}$ m → $E_{\text{twist}}\sim2\times10^{-11}\ m_ec^2$** — the hole is negligible and "UNACCOUNTED" is a bookkeeping nit, not a physics problem.

**So the twist-ledger question REDUCES TO an already-open corpus adjudication.** That is the most useful thing this audit produces: it converts a new open question into a **decision that was already on the board** and shows that decision is load-bearing for the electron's mass ledger and the entire generation spectrum — not just for naming conventions in Vol 9.

---

## §6 The ballpark — canon-supplied inputs only

**Class: paper arithmetic, order-of-magnitude only. NOT a simulation, NOT a prediction, mints nothing.** Driver: `research/drivers/twist_ledger_ballpark.py` (added by this doc; pure-constants, no solver, no lattice). Re-runnable: `PYTHONPATH=src .venv/bin/python research/drivers/twist_ledger_ballpark.py`.

### 6.1 ★A dimensional defect found in the canonical $\xi_K$ relation (FLAG-2, not repaired)

Canon states, identically in three places — [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py):28, [`k4_cosserat_coupling.py`](../src/ave/topological/k4_cosserat_coupling.py):34, [`q-g47-substrate-scale-cosserat-closure.md`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md):58 —

```
  μ + κ = ξ_K1 · T_EM            (Cauchy + micropolar moduli, [Pa])
  β + γ = ξ_K2 · T_EM · ℓ_node²  (couple-stress moduli, [N])
```

With the canonical `T_EM = 0.212 N` ([`constants.py`](../src/ave/core/constants.py):493), **both lines contradict their own unit brackets**: $\xi_{K1}T_{EM}$ is N, not Pa; $\xi_{K2}T_{EM}\ell_{node}^2$ is N·m², not N. The relations are unit-consistent **only** if the symbol `T_EM` in them denotes the **stress** $\sigma_0 \equiv m_ec^2/\ell_{node}^3 = 1.4218\times10^{24}$ Pa rather than the 1-D tension. **Independent confirmation that this is the intended reading:** under it, and only under it, the canonical cross-check reproduces exactly — $\ell_c^2=(\beta+\gamma)/[2(\mu+\kappa)] = \xi_{K2}/(2\xi_{K1})\,\ell_{node}^2 = 6\,\ell_{node}^2$, i.e. $\ell_c = 2.4495\,\ell_{node}$ vs $\sqrt6 = 2.4495$. Verified numerically in the driver. **Surfaced, not fixed** — repairing a symbol overload inside a Grant-era closed derivation (Sessions 19) is an auditor/Grant call, not an implementer edit.

### 6.2 The magnitude gate — the $\ell_c$ collision, already flagged in canon

[`constants.py`](../src/ave/core/constants.py):331-337, verbatim:

> *"⚠ DISAMBIGUATION (two-objects-one-symbol — flag-don't-fix): this ELL_C (≈ 9.46e-13 m, the K4 LATTICE-scale Cosserat coupling length, ≈ 2.45 node spacings) is **NOT** the weak-force-range "l_c = √(γ_c/G_vac) ≈ 1e-18 m" used in vol9 ch9/ch10 + gauge-boson-masses.md:39. Same symbol and same formula STRUCTURE (√(couple-stress/shear)), but **~6 orders of magnitude apart** and a different physical referent. **Surfaced for auditor adjudication** … not silently merged."*

And the provenance of the weak-scale value, [`physics-lineage-map.md`](../manuscript/ave-kb/common/physics-lineage-map.md):220: *"$\gamma_c$ VALUE **imported by identification** with $r_W \sim 10^{-18}$ m — FORM-deriving/VALUE-importing, honestly booked."*

Since $\gamma_c = G_{vac}\ell_c^2$, the two readings differ in $\gamma_c$ by $\sim10^{12}$.

### 6.3 The two-sided number

Geometry, all canon: $C_{loop}=\ell_{node}$ ([`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):28), $r_0=\ell_{node}/2\pi$ (:11), $V_{tube}=\pi r_0^2 C_{loop}=\ell_{node}^3/4\pi$, twist rate $\kappa = 2\pi\,\mathrm{Tw}/C_{loop}$ with $\mathrm{Tw}=q/p=3/2$ ([`2026-06-07_vacuum-characterization-program.md`](2026-06-07_vacuum-characterization-program.md):59). Energy form $E=\int\gamma_c|\kappa|^2dV$ ([`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py):713 `gamma kappa·kappa`).

| Route | $\gamma_c$ | $E_{\text{twist}}$ | in $m_ec^2$ |
|---|---|---|---|
| **R1a** lattice-scale via $G_{vac}\ell_c^2$, $\ell_c=\sqrt6\ell_{node}$ | $6.360\times10^{-1}$ N | $1.736\times10^{-12}$ J | **$2.12\times10^{1}$** |
| **R1b** lattice-scale via $\xi_{K2}\sigma_0\ell_{node}^2$, $\xi_{K2}=32$ (upper: $\gamma=\beta+\gamma$) | $6.784$ N | $1.852\times10^{-11}$ J | **$2.26\times10^{2}$** |
| **R2** weak-scale, $\ell_c\approx10^{-18}$ m | $7.109\times10^{-13}$ N | $1.940\times10^{-24}$ J | **$2.37\times10^{-11}$** |

R1a vs R1b differ by $32/3=10.67$ — internal slop *within* the lattice-scale reading (two canon stress scales, $G_{vac}=\rho_{bulk}c^2 = 7.109\times10^{23}$ Pa vs $\sigma_0=1.422\times10^{24}$ Pa; and $\gamma$ alone vs $\beta+\gamma$, which canon never separates). **Honest lattice-scale bracket: $2\times10^1$ – $2\times10^2\ m_ec^2$.**

### 6.4 ★The muon-rung near-coincidence — recorded, and explicitly NOT claimed

R1b's closed form is $E_{\text{twist}}/m_ec^2 = \xi_{K2}(2\pi\mathrm{Tw})^2/4\pi = 32\cdot 9\pi/4 = 72\pi = 226.19$, against the muon rung $205.77$ (CODATA anchors, `constants.py`:131/:159) / $208.33$ (canon's $1/(\alpha\sqrt{3/7})-1$). **8% apart. This is NOT a match and is NOT offered as one.**

**Discrimination note (why the near-agreement is weak evidence, applying `ave-discrimination-check` against my own finding):** because $T_{EM}\ell_{node}\equiv m_ec^2$ **by definition**, *any* energy of the form (O(1) geometry)$\times\xi_{K2}\times T_{EM}\ell_{node}$ is **forced** to be (O(1)$\times$32)$\,m_ec^2$ — i.e. forced into the $10^1$–$10^3$ band before any physics enters. Landing near 206 requires only that the geometric factor be $\approx6.5$, which is not a tight target. The R1a/R1b spread (10.67×) already brackets 206 from both sides. **Treat as: the lattice-scale twist energy is the same ORDER as the generation spacing. That is a structural statement about the ladder's shape, not a numerical chord.** It is exactly the shape Grant's paperclip predicts (ground pre-load and first rung comparable), which is why it is recorded — as a walk question (§8 Q3), not a result.

---

## §7 FLAG-DON'T-FIX register — five items surfaced, ZERO repaired

| # | Flag | Both sides, verbatim | Routed to |
|---|---|---|---|
| **1** | ★**Nonzero winding-sector mass excluded from $m_ec^2$ by declaration.** | [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41 *"the couple-stress stiffness that makes the node micro-rotation **massive** … **NOT the electron's rest-energy store**"* **vs** [`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559 *"This $\omega_B$ is **COSTLY** (couple-stress energy via $G_c$)"* + [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):24 *"the `(2,3)` WINDING rotation … is the **GAPPED mechanical Cosserat micro-rotation ω** (couple-stress / curvature grade)"*. A costly, massive grade carrying a static $\mathrm{Tw}=3/2$ configuration in the electron's rest frame, declared outside the electron's rest energy. | **Grant** — the physics adjudication. |
| **2** | **Dimensional defect in the canonical $\xi_K$ relations.** | §6.1. `μ+κ = ξ_K1·T_EM  [Pa]` and `β+γ = ξ_K2·T_EM·ℓ_node²  [N]` at [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py):28 / [`k4_cosserat_coupling.py`](../src/ave/topological/k4_cosserat_coupling.py):34 / [`q-g47-substrate-scale-cosserat-closure.md`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md):58 disagree with their own unit brackets under `T_EM = 0.212 N` ([`constants.py`](../src/ave/core/constants.py):493). Consistent only reading `T_EM` as $\sigma_0=m_ec^2/\ell_{node}^3$; that reading is confirmed by the $\ell_c=\sqrt6$ cross-check. | **Auditor lane** — a symbol overload inside a closed derivation; three sites, one repair. |
| **3** | **The $\ell_c$ 6-OOM collision is load-bearing far beyond naming.** | [`constants.py`](../src/ave/core/constants.py):331-337 already flags it *"for auditor adjudication"* as a naming/referent issue. **This audit shows it gates the electron's mass ledger and the whole generation ladder** — 12 OOM on $E_{\text{twist}}$ (§6.3). Its priority should reflect that. | **Grant / auditor** — re-prioritize an existing open item. |
| **4** | **Three incompatible stores for $m_\mu-m_e$.** | rotational-DOF ([`q-g27-…`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md) §Sign *"the helical spiral adds energy to the rotational DOF"*) **vs** dielectric-saturation-density, node-displacement-free ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17 *"a pattern of **dielectric saturation density** … **Neither involves physical displacement of lattice nodes**"*) **vs** A1 (`mass = A1`, PR#260). | **Grant** — same sector-of-storage family as charter **D1**; see §8. |
| **5** | **The engine can price this and never has.** | [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py) relaxes a **(2,3)** ansatz on an energy functional containing `gamma kappa·kappa` (:713) — but with `G = G_c = gamma = rho_vac = 1` natural units (:12, :942), never the $\xi_{K2}$/$\gamma_c$ calibration, and no result doc converts the relaxed integral to $m_ec^2$ units. Two-method absence-check in §9. | **Implementer follow-on** — §8 T1. |

**Not repaired, not reframed, not reconciled.** Per flag-don't-fix: both sides quoted verbatim with paths; no side edited to match the other.

---

## §8 The falsifiable follow-on shape, and the Grant walk questions

### 8.1 Follow-on shape, per classification — verdict is UNACCOUNTED, so:

**T1 — the cheapest decisive test (no new physics, no new axiom, no new engine).** [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py) already relaxes a **(2,3)** ansatz on an energy functional whose `gamma kappa·kappa` term (:713) **is** the twist store. The test: relax the ground-state (2,3), **calibrate the moduli off natural units onto the canonical $\gamma_c$** (both readings, R1 and R2 — the collision is the independent variable, not a nuisance), and report $E_{\gamma\kappa\kappa}/m_ec^2$. **Pre-registrable, falsifiable, and it forces the §6.2 adjudication empirically rather than by fiat.** This is Rule-10 empirical-driver discipline applied to a question that has so far only been argued on paper. Requires the `substrate-native-check` walk before a line is written (the relaxation is a **gradient-descent energy-basin** move, which is exactly the SM-default the check exists to catch — and canon has *already* falsified basin-trapping for this object: [`electron-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md):64 *"held **topologically** … **not** trapped in an energy basin"*. **The driver must be written as an energy READOUT on a topologically-imposed configuration, not a relaxation-to-minimum**, or it will re-run a closed negative).

**T2 — the discriminator that does not need the engine.** The two $\gamma_c$ readings make **opposite** predictions about the generation ladder's shape, and the ladder is already measured:
- **R1 (lattice-scale):** ground rung $\sim10^1$–$10^2\,m_ec^2$, first spacing $\sim2\times10^2\,m_ec^2$ ⇒ **ground rung comparable to the spacing** ⇒ $m_e$ is *substantially* twist energy ⇒ the "torsion-free electron anchor" that the whole ladder is built on is **false**, and $m_\mu/m_e$ should NOT be a clean $1/(\alpha\sqrt{3/7})$ multiple of a torsion-free base.
- **R2 (weak-scale):** ground rung $\sim10^{-11}\,m_ec^2$ ⇒ the torsion-free anchor is **fine** ⇒ the closed-form ladder is undisturbed.
**Adjudication criterion, frozen here before any run:** if the lattice-scale $\gamma_c$ is the electron's, the existing $m_\mu = m_e/(\alpha\sqrt{3/7})$ closed form is **inconsistent with its own stated mechanism** (though it may survive as a numerological match — which is exactly what [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):84 already labels it, Class C). **Do not drop this criterion post-hoc** (Rule 11).

**T3 — the honest null branch.** If Grant adjudicates the electron's $\gamma_c$ to the **weak-scale** reading, then: $E_{\text{twist}}\sim10^{-11}m_ec^2$, the hole is real but negligible, and the correct closure is **a one-line scope note on `clm-ka5zdx`** stating that the couple-stress store is a $10^{-11}$ correction — **not** a new claim, **not** a new axiom, **not** a lift of anything. Branch closed clean. **That is a perfectly good outcome and must not be debugged toward a more interesting one.**

**What this audit does NOT license.** No new axiom candidate. Per A44 (missing-axiom-vs-engine-bug), the diagnosis here is **an unbuilt ledger plus an unadjudicated symbol collision** — both engine/bookkeeping-class, neither axiom-class. Do not draft an Ax 5. Do not refill `clm-ka5zdx`'s open strengthen-by slot with a twist hypothesis (Rule 12) — that slot stays exactly as canon wrote it.

### 8.2 Grant walk questions — plumber-physical, four, in priority order

**Q1 (the one that decides everything).** *Two Cosserat lengths wear the same name, six orders apart: $\sqrt6\,\ell_{node}\approx9.5\times10^{-13}$ m (lattice) and $\approx10^{-18}$ m (weak-force range). Which one is the stiffness the **electron's own (2,3) twist** feels?* — Plumber form: **when you twist the clip, over what distance does the metal notice?** If the couple-stress reach is a couple of node-spacings, the electron's twist is stiff and expensive ($10^1$–$10^2\ m_ec^2$). If it is the weak-force range — a million times shorter — the twist is nearly free ($10^{-11}$). Canon already flags the collision *"for auditor adjudication"* ([`constants.py`](../src/ave/core/constants.py):331-337); this audit shows the electron's mass ledger rides on it.

**Q2 (the paperclip question, direct).** *Your clip stores spring tension in the pre-load. Canon says the electron's ω-grade is **massive** and that microrotation is **costly**, and it says that store is **"NOT the electron's rest-energy store"** — an exclusion by grade-orthogonality, not by a computation showing it is zero. **Where does that energy live, if not in $m_ec^2$?*** In a lossless reactive substrate at rest there is no radiation channel to carry it away, and Ax 3 forbids a dissipative one. Options as I read them: (a) it IS in $m_ec^2$ and `mass = A1` is a **labelling** convention over a total that A1 and T2 both feed; (b) it is genuinely zero for the ground (2,3) and something forces $\kappa_{\text{eff}}=0$ that canon hasn't stated; (c) the grade-orthogonality guard is doing more work than it was derived to do. **Which?**

**Q3 (the ladder-shape question).** *If the ground twist is $O(10^1$–$10^2)\,m_ec^2$ and one torsion quantum is $\sim206\,m_ec^2$ — is that a ladder, or is $m_e$ itself mostly the same thing the muon has more of?* Grant's paperclip says the second: generations = more pre-load in one clip. That reading is **physically coherent and structurally destructive** — it makes $m_e$ non-anchor and the torsion-free ground state a fiction. **I am recording the 8%-apart near-coincidence ($72\pi=226$ vs $206$) as a walk observation and explicitly NOT as evidence** (§6.4 — any term of that shape is forced into the band). Does the picture want the ladder, or the continuum?

**Q4 (the mislabel candidate — surfaced, deliberately not adopted).** *$\sqrt{3/7}=\sqrt{1-2\nu_{vac}}$ is the **bulk/dilatational** elastic signature, and canon's own live 🔴 flag says so ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):29). `mass = A1` (PR#260) also says the muon's excess should be **A1 dilatation**. Both point the same way: is the "Cosserat **torsion** ladder" actually an **A1 dilatation** ladder wearing a torsion label?* If yes, §7 FLAG-4's three-way contradiction collapses to one store (A1), the twist ledger becomes a genuinely separate and possibly small question, and Q1 loses its teeth. **Not adopted here** — it is an unadjudicated inference and adopting it would silently refill a slot.

---

## §9 Cite ledger + verification receipts (the checkability requirement)

### 9.1 Two-method cite verification — 19 load-bearing cites, ALL PASS at ship tip

Method A: `sed -n "<N>p" <file>` on the worktree. Method B: `git show origin/main:<file> | sed -n "<N>p"`. Byte-compared. Run at `origin/main` @ `ac165cf2` (ship time, per `verify-before-cite` v1.6 — the brief's stated base `e72d18f6` had already advanced; **re-verified at the tip, not at brief time**).

| # | Cite | Verdict |
|---|---|---|
| 1 | `vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md`:52 | OK |
| 2 | `…/mass-closure-theorem.md`:54 | OK |
| 3 | `…/ch01-topological-matter/electron-unknot.md`:48 | OK |
| 4 | `vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md`:21 | OK |
| 5 | `vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md`:43 | OK |
| 6 | `…/ch01-topological-matter/torus-knot-uniqueness.md`:106 | OK |
| 7 | `vol2/claim-quality.md`:1256 (`clm-ka5zdx` rationale) | OK |
| 8 | `vol2/claim-quality.md`:1258 (the open strengthen-by) | OK |
| 9 | `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`:24 (rotation-flavor tag) | OK |
| 10 | `common/q-g47-substrate-scale-cosserat-closure.md`:58 ($\xi_{K1}{=}8/3$, $\xi_{K2}{=}32$) | OK |
| 11 | `vol2/particle-physics/ch05-electroweak-mechanics/weak-coupling.md`:15 ($E_{\text{twist}}$) | OK |
| 12 | `vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md`:24 | OK |
| 13 | `common/genesis-chord-falsification-ledger.md`:47 ($E_{curv}$) | OK |
| 14 | `vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md`:10 (Călugăreanu) | OK |
| 15 | `research/2026-06-07_vacuum-characterization-program.md`:59 (`Tw = q/p = 540°/rev`) | OK |
| 16 | `vol1/claim-quality.md`:544 (`clm-zw6mut` *"asserted, not derived"*) | OK |
| 17 | `src/ave/topological/cosserat_field_3d.py`:28 ($\beta{+}\gamma$ relation) | OK |
| 18 | `src/ave/topological/cosserat_field_3d.py`:713 (`gamma kappa·kappa`) | OK |
| 19 | `src/ave/core/constants.py`:493 (`T_EM = M_E*C_0**2/L_NODE`) | OK |

Additionally verified in-body (same two methods): `master-equation.md`:41-42 (the G2-dissolution bullets), `constants.py`:331-337 (the $\ell_c$ collision flag), `trampoline-framework.md`:559, `physics-lineage-map.md`:220, `electron-unknot.md`:41, `electron-identification.md`:64, `lepton-spectrum.md`:17/29/39/51/84, `torus-knot-uniqueness.md`:110, `cosserat_field_3d.py`:12/942, `k4_cosserat_coupling.py`:34.

### 9.2 ★Cite CORRECTION against the dispatch brief (recorded as a failure, not silently fixed)

The brief cited **`vol1/claim-quality.md:544`** for `clm-zw6mut`'s *"asserted, not derived"*. **Both parts check out but the anchor is split:** the `<!-- id: clm-zw6mut -->` marker is at **`:521`**; the *"asserted, not derived"* rationale text is at **`:544`**. A reader grepping `:544` for the claim ID finds nothing. Cited above as **`:544` for the rationale text** (which is what the audit uses), with the ID home at `:521` recorded here. No file edited.

### 9.3 The absence claims, with their commands (per `verify-before-cite` trigger 6)

Both run from the worktree root at `ac165cf2`; each cross-checked with a second method (`git grep` on `origin/main` ⊕ filesystem `grep -rn`), per the grep-completeness discipline.

**A1 — "no site computes a $\gamma_c$ twist energy for the electron's ground-state (2,3) in $m_ec^2$ units."**
```
git grep -n -I -E '(gamma_c|γ_c|couple.stress)' -- manuscript/ave-kb | grep -v '\.index/' \
  | grep -i -E 'energ|E_|store|\bwork\b'
```
→ **12 hits.** The energy-bearing ones are enumerated in §3.1 (`master-equation.md`:20/:41, `trampoline-framework.md`:559, `physics-lineage-map.md`:212/:220/:338); the remaining six are $\delta_{\text{strain}}$ / thermal-mechanism, saturation-rim, and closure-roadmap contexts (`claim-quality-closure-roadmap.md`:102, `saturation-rim-inversion.md`:23, `vol1/claim-quality.md`:127, `vol3/claim-quality.md`:1222, `delta-strain-cosmic-tcc.md`:15, `vol9/ch6-temperature-characteristics/index.md`:40) carrying **no electron energy computation**. **None of the 12** is an electron ground-state (2,3) twist energy in $m_ec^2$ units.

Second method — `grep -rn -E 'E_\{?\\?text\{?twist|U_twist|E_twist' manuscript/ research/ src/` → **exactly four source sites** outside this audit's own files: `weak-coupling.md`:15 (the **W boson** formula), its chapter index row `vol2/particle-physics/ch05-electroweak-mechanics/index.md`:20, its LaTeX mirror `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex`:79, and `src/scripts/vol_4_engineering/simulate_gw_impedance.py`:105 (an unrelated GW-bench `0.5*k_twist*sum(d_phi**2)` spring term). **Absence confirmed, two methods.**

**A2 — "canon nowhere states that the T2 grade stores zero rest energy."**
```
git grep -n -I -E 'T2 (sector )?(stores|carries) (no|zero)|zero rest energy|no rest energy|T2.*zero energy' \
  -- manuscript/ research/
```
→ **0 hits**, both methods. What canon *does* say is the **exclusion-by-declaration** at `master-equation.md`:41 (§3.3), which is a different proposition.

**A3 — "the engine's (2,3) `gamma kappa·kappa` integral was never booked against $m_ec^2$."**
`git grep -l -I -E 'cosserat_field_3d|CosseratField3D' -- research/ manuscript/` cross-read against every result doc citing the module; none reports a couple-stress energy in MeV or as a fraction of $m_ec^2$. The module's own moduli are `G = G_c = gamma = rho_vac = 1` natural units (`cosserat_field_3d.py`:12, `:942`), so no such conversion is even available without the calibration step T1 proposes. **Absence confirmed.**

### 9.4 Numeric receipts (banked; re-runnable via `research/drivers/twist_ledger_ballpark.py`)

```
U_AVE = T_EM * l_node                      = 8.187106e-14 J = 1.000000 m_e c^2   (Class A, forced)
sigma_0 = m_e c^2 / l_node^3               = 1.4218e+24 Pa
beta+gamma = xi_K2 * sigma_0 * l_node^2    = 6.784439e+00 N     [N] OK
l_c cross-check                            = 2.4495 * l_node   vs sqrt(6) = 2.4495   REPRODUCES
kappa = 2 pi Tw / l_node,  Tw = 3/2        = 2.4406e+13 1/m
V_tube = l_node^3 / (4 pi)                 = 4.5824e-39 m^3
R1a  gamma_c = G_vac * ELL_C^2 = 6.3604e-01 N  -> E_twist = 2.1206e+01 m_e c^2
R1b  gamma_c = xi_K2*sigma_0*l^2 = 6.7844 N    -> E_twist = 2.2619e+02 m_e c^2   (= 72 pi)
R2   gamma_c = G_vac * (1e-18 m)^2 = 7.1089e-13 N -> E_twist = 2.3701e-11 m_e c^2
R1b/R1a = 10.6667 (= 32/3, internal slop)  |  R1a/R2 = 8.9471e+11 (the 12-OOM gate)
(m_mu - m_e)/m_e = 205.77 (CODATA anchors) ; 1/(alpha*sqrt(3/7)) - 1 = 208.33 (canon) ; 72 pi = 226.19
```

### 9.5 What this doc changes in the corpus

**Nothing.** Zero KB edits, zero manuscript edits, zero claim-quality edits, zero `clm-`/`def-`/`exp-`/`sup-`/`ilk-` ids minted, zero solidity flips, zero status changes, engine byte-untouched. Two files added: this doc and `research/drivers/twist_ledger_ballpark.py`, plus one docket fragment. The five §7 flags are **routed**, not repaired.

---

> **Reading discipline for anyone citing this doc.** The verdict (**UNACCOUNTED**) is a statement about the **corpus's bookkeeping**, not a claim that AVE is wrong about mass. The magnitude of the hole is **undetermined by 12 orders** and reduces to one already-open adjudication (§6.2). The §6.4 near-coincidence with the muon rung is **recorded and disclaimed** — do not headline it. Nothing here is Grant-ratified.
