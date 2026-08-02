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

**Five** distinct statements of the electron's rest-energy budget exist in canon, plus a restatement family that propagates them. **Every one of them is a two-term-or-fewer sum, and not one of them contains a Cosserat-rotational / couple-stress ($\gamma_c$) term.**

> **⚠ COUNT CORRECTED 2026-08-02 (repair pass; Rule 12 — prior wording quoted, not deleted).** This section originally opened: *"**Four** independent statements of the electron's rest-energy budget exist in canon."* **That was an under-count.** It missed [`l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — the single most explicit budget site in the corpus, and the only one that supplies a closed form for **every symbol** in the sum. Added below as **T5**, with a **two-method sweep receipt in §9.3.4** enumerating every hit and its classification. **The correction EXTENDS the §2.2 finding rather than softening it** — see §2.2b.

### 2.1 The five budget statements

| # | Statement | Terms in the sum | Any $\gamma_c$ / couple-stress term? | Class |
|---|---|---|---|---|
| **T1** | [`mass-closure-theorem.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md):52 — $E_{\text{reactive}} = \tfrac12 L_{\text{tube}} I_{\max}^2 = \tfrac12 C_{\text{tube}} V_{\text{peak}}^2$ | **1** (one reactive store, stated twice in its two conjugate faces) | **NO** | **A — identity** (see 2.2) |
| **T2** | [`mass-closure-theorem.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md):54 — the LC-tank virial: peak-amplitude equality $\tfrac12 LI^2_{\max} = \tfrac12 CV^2_{\text{peak}}$, *"the two stores are in phase quadrature"* | **2** (magnetic ⊕ electric reactance) | **NO** | **A — identity** |
| **T3** | [`relativistic-inductor-newtonian-limit.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md):24 — $E_L = E_C = \tfrac{m_ec^2}{2},\ \ E_L + E_C = m_ec^2$ | **2**, and **explicitly closed** — the two halves are each exactly $\tfrac12 m_ec^2$ and they **sum to the whole** | **NO** — and no slot remains | **A — identity** |
| **T4** | [`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):48 — $U_{AVE} = \oint_{C_{loop}} T_{EM}\,ds = T_{EM}\cdot \ell_{node} = 1.0\,m_ec^2$ | **1** (a 1-D line integral of the string tension along the loop) | **NO** — a 1-D scalar-tension integral carries no rotational DOF at all | **A — identity** (see 2.2) |
| **T5** *(added 2026-08-02 repair pass)* | [`l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md):90 — the **boxed** Virial sum $\boxed{E_e = m_ec^2 = \hbar\omega_C = T_{EM}\cdot\ell_{node} = \tfrac12 L_0I_{\max}^2 + \tfrac12 C_eV_{\text{peak}}^2}$, with a **closed form for every symbol** at :98-105, the per-half split at :114-116, and the closure claim at :118 | **2** (inductive ⊕ capacitive), and it is the **only site that writes the sum AND supplies every symbol's closed form** — so it is the only one whose arithmetic can actually be executed | **NO** | **A — identity, demonstrably so.** Substituting :98-105 gives $\tfrac12 L_0I^2_{\max}/m_ec^2 = 0.5$ and $\tfrac12 C_eV^2_{\text{peak}}/m_ec^2 = 0.5$ **exactly**, with $\xi_{topo}$ and $e$ cancelling identically (§2.2b, receipt §9.4) |

**T3 is the load-bearing one for this audit.** It is the only statement that writes the budget as an explicit *closed sum over named sectors*, and it closes at **two**: inductive ⊕ capacitive, $\tfrac12 + \tfrac12 = 1$. There is **no third slot**. The [`vol4/simulation/ch14`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md) and [`electron-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md):165 restatements ("*the soliton's total energy decomposes 50/50 inductive/capacitive by virial equipartition*") propagate the same two-term closure.

### 2.2 The load-bearing finding: the sum was never evaluated as a sum

Canon's own claim-quality entry for the mass-closure theorem — [`vol2/claim-quality.md`](../manuscript/ave-kb/vol2/claim-quality.md):1256, `clm-ka5zdx`, **confidence 0.50 / solidity 0.50, "use as input only, don't build deeper"** — states the situation exactly:

> *"the load-bearing final identity $E_{reactive}=mc^2$ is reached by **identifying** the closed-loop standing-wave invariant with the rest energy (**no quantity computed**) — honestly labeled 'a statement about what mass IS, not a computational program.'"*

and its own open strengthen-by item, [`vol2/claim-quality.md`](../manuscript/ave-kb/vol2/claim-quality.md):1258, is *the unbuilt ledger*:

> *"Compute $E_{reactive}=\frac12 L_{tube}I_{max}^2$ for the unknot and show it equals $m_ec^2$ **numerically**, closing the identification."*

**Consequence for the twist question, stated precisely.** The mass-closure chain is a **one-term identification**, not a ledger. There is therefore **no enumerated sum for the $\gamma_c$ term to be inside of or excluded from**. The question "is the twist energy absorbed?" cannot be answered ABSORBED, because nothing was ever added up.

The same holds for T4: $T_{EM} \equiv m_ec^2/\ell_{node}$ is *defined from* $m_e$ ([`constants.py`](../src/ave/core/constants.py):493, `T_EM: float = (M_E * C_0**2) / L_NODE`), so $U_{AVE} = T_{EM}\cdot\ell_{node} = 1.0\,m_ec^2$ is **algebraically forced** — verified numerically to 1.000000 in §6. It is a **Class-A definitional identity**, not a computation that could have come out ≠ 1 and thereby left or refused room for a twist term. The "1.0" is not evidence of exhaustion; it is evidence of tautology.

> **Consistency-vs-emergence tag for §2 as a whole: Class A (definitional identity) throughout.** No term in the five budget statements is a Class-D emergence result. This is not a criticism of the chain — canon labels it honestly at :1256 — but it is decisive for the ledger question: *a tautology has no residual, so it can neither absorb nor exclude a physical term.*

### 2.2b ★T5 EXTENDS the Class-A finding — `clm-ka5zdx`'s strengthen-by is TRIVIALLY SATISFIABLE, therefore vacuous (added 2026-08-02 repair pass)

T5 is the **fifth** budget site and the **sharpest confirmation** of §2.2, not a counterexample to it. It is the only site that supplies a closed form for every symbol in the sum ([`l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md):98-105, verbatim rows): $\xi_{topo} = e/\ell_{node}$; $L_0 = \xi_{topo}^{-2}\cdot m_e$; $I_{\max} = \xi_{topo}\cdot c$; $C_e = e/V_{\text{SNAP}} = e^2/(m_ec^2)$; $V_{\text{SNAP}} = m_ec^2/e$. Substituting them:

$$\tfrac12 L_0 I_{\max}^2 \;=\; \tfrac12\,\big(\xi_{topo}^{-2}m_e\big)\big(\xi_{topo}c\big)^2 \;=\; \tfrac12 m_ec^2, \qquad \tfrac12 C_e V_{\text{SNAP}}^2 \;=\; \tfrac12\,\frac{e^2}{m_ec^2}\cdot\frac{(m_ec^2)^2}{e^2} \;=\; \tfrac12 m_ec^2.$$

**$\xi_{topo}$ cancels identically in the first; $e$ cancels identically in the second; the sum is $1.000000\,m_ec^2$ by construction** — numeric receipt in §9.4 (driver block 1b), and canon writes the first cancellation out longhand itself at [`relativistic-inductor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md):28, verbatim: *"the rest energy stored in the inductor's self-field is $E_0 = \tfrac{1}{2} L_0 I_{max}^2 = \tfrac{1}{2} (\xi_{topo}^{-2} m_0)(\xi_{topo} c)^2 = \tfrac{1}{2} m_0 c^2$."*

**Consequence: `clm-ka5zdx`'s open strengthen-by is vacuous.** [`vol2/claim-quality.md`](../manuscript/ave-kb/vol2/claim-quality.md):1258 asks to *"Compute $E_{reactive}=\frac12 L_{tube}I_{max}^2$ for the unknot and show it equals $m_ec^2$ **numerically**, closing the identification."* **That is already trivially satisfiable from canon's own closed forms and therefore carries no information** — executing it produces `0.5 + 0.5 = 1.0` with the only free symbol cancelling out, and closes nothing. The `clm-ka5zdx` solidity-0.50 hedge cannot be lifted by running an arithmetic that is an identity before it is run.

**The sharpest counter-text in the corpus to any "the budget is exhausted" reading is this same leaf**, [`l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md):118, verbatim:

> Given Axiom 1 (LC network with fixed $Z_0$) + Axiom 4 (saturation kernel with $V_{\text{yield, macro}} = \sqrt{\alpha} \cdot V_{\text{SNAP}}$) + the bond-pair smallest-coupled-oscillator scale, the energy at saturation onset MUST equal $m_e c^2$ by the Virial sum identity. There is no remaining empirical question about the energy magnitude.

**Read against §2.2 this EXTENDS the Class-A verdict.** A budget declared to have *"no remaining empirical question about the energy magnitude"* — reached by substituting definitions that cancel — is **exactly** a ledger that cannot detect a physical term it never enumerated. Canon's own vol-4 claim-quality entry says the same thing in the same words, [`vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md):200, verbatim: *"The 'particle as resonant LC tank, $E = m_e c^2 = \tfrac{1}{2}LI^2 + \tfrac{1}{2}CV^2$' mapping is **structural (Virial decomposition), not an independent rest-mass derivation** — $m_e$ is taken as given."*

**Rule 12 note: the `clm-ka5zdx` slot is NOT refilled here.** The finding is that the *existing* strengthen-by is vacuous. It is **not** a proposal that a twist term belongs in that slot; that stays exactly as canon wrote it (§8.1).

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

**This is the sharpest available answer, and it is neither ABSORBED nor ZERO.** Canon (i) asserts a **nonzero** mechanical mass on the winding sector, sourced by the couple-stress stiffness, and (ii) declares it **outside** the electron's rest-energy store. The exclusion is by **grade-orthogonality declaration**, not by a computation showing the quantity vanishes.

> **⚠ CORRECTED 2026-08-02 (repair pass; Rule 12 — the prior sentence is quoted here in full, not deleted).** This paragraph originally ended: *"…not by a computation showing the quantity vanishes **and not by a mechanism for where a nonzero rest-frame energy goes if not into the invariant mass**."* **The bolded clause was OVER-STRONG and is retracted.** Canon *does* carry such a mechanism, inside the **Grant-ratified 2026-06-20 mass-sector ruling block** (block header at [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):30, *"MASS = A1 DEPRESSION / FLYWHEEL = T2 ($\omega$) FREQUENCY-REGULATOR — the clean split … Grant-ratified mass-sector ruling"*), and this audit's first pass never engaged it. The bullet, [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):34, verbatim:
>
> > **Lepton tower:** more Cosserat torsion → faster flywheel → higher regulated frequency → (Compton $f = mc^2/\hbar$) deeper A1 depression → more mass. The flywheel regulates the frequency that *sets* the mass; the mass stays A1.
>
> **That is a TRANSDUCTION account, not a silence.** The twist is priced as a **frequency-setter**, not as an additive store: torsion sets the flywheel rate $f$; $m=\hbar f/c^2$ lands the energy on **A1**; nothing is double-booked, and $A_1\perp T_2$ survives because T2 supplies a *frequency* to the A1 ledger, not a *joule*. On this reading, "where does the energy go" has canon's own answer — **into A1, via $f$.**
>
> **Verdict impact: NONE. UNACCOUNTED stands.** Two narrow reasons: **(i) :34 quantifies nothing.** It is a monotone chain (*more* torsion → *more* mass) with no $E(\mathrm{Tw})$, no coefficient, and no statement that the transduction is *lossless* — i.e. it never says the couple-stress store is **zero**, only that it is not where the mass label lands. **(ii) A flywheel that regulates $f$ still stores $\tfrac12 I_\omega\omega^2$ in the rest frame.** A real rotor turning at a real rate, on a grade canon calls **massive** (:41) and **costly** ([`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559), has kinetic-reactive energy in the electron's rest frame whatever else it also regulates. §2's closure still has no slot for it. **What :34 *does* change is FLAG-4** — see §4.1, where it is load-bearing.

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

**So: WHERE is $m_\mu-m_e$ stored, physically?** Three candidate stores appear in canon:
1. **rotational DOF / Cosserat torsion** (q-g27 §Sign; the whole "torsion ladder" framing),
2. **dielectric saturation density / impedance modulation, explicitly NOT node displacement** ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17) — an $\varepsilon$-sector, not a couple-stress store,
3. **A1, by the standing `mass = A1` ruling** (PR#260) — the extra $205.8\,m_ec^2$ is A1 dilatation.

> **⚠ CORRECTED 2026-08-02 (repair pass; Rule 12 — the prior sentence is quoted here in full, not deleted).** This passage originally read: *"Canon gives **three mutually inconsistent answers** and adjudicates none"*, and §7 FLAG-4 was raised on that basis. **That is FALSE as stated.** **(1) and (3) ARE adjudicated — against each other, Grant-ratified** — inside the 2026-06-20 mass-sector ruling block ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):30 header; bullet at :34), verbatim:
>
> > **Lepton tower:** more Cosserat torsion → faster flywheel → higher regulated frequency → (Compton $f = mc^2/\hbar$) deeper A1 depression → more mass. The flywheel regulates the frequency that *sets* the mass; the mass stays A1.
>
> **(1) is the frequency-setter; (3) is the store.** They are two links of one ratified transduction chain, not two rival answers to one question. The audit's first pass never engaged :34 — **recorded as an audit failure, not silently dropped.**
>
> **FLAG-4 is DEMOTED accordingly** (§7, row updated): the live inconsistency is **store (2) vs the ratified (1)→(3) chain.** [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17 books the generation increment on the **$\varepsilon$ / impedance** sector — *"a pattern of **dielectric saturation density** … The nodes themselves remain fixed at $l_{node}$ spacing (Axiom 1) … **Neither involves physical displacement of lattice nodes**"* — which is neither the T2 flywheel that :34 makes the setter nor the A1 depression that :34 makes the store. **One two-way contradiction, not a three-way one.**
>
> **Verdict impact: NONE.** :34 quantifies nothing (§3.3) and this demotion narrows a *supporting* flag. UNACCOUNTED rests on §2.2 (the sum was never evaluated as a sum) and §3.1/§3.2 (a geometrically nonzero $\mathrm{Tw}=3/2$ on a grade canon calls massive and costly) — neither of which :34 touches.

**Consistency-vs-emergence tag for the whole lepton table: canon's own, verbatim** ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):84): *"**matched closed-form CONSISTENCY — NO solver** … evaluated from the CODATA-input $\alpha$ and $p_c$ with $m_e$ as the input scale — **not** 'derived' or 'emergent', and **not** solver-backed."* **Class C.** Plus the standing `clm-zw6mut` finding that the sector→generation identification *"is asserted, not derived"* ([`vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md):544) and the **live 🔴 OPEN FLAG** that $\sqrt{3/7}=\sqrt{1-2\nu_{vac}}$ is the **bulk/dilatational** elastic signature wearing a *"PAT torsion-shear"* label ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):29, Grant adjudication pending).

**★Note the coherence between two independent open flags.** The $\sqrt{3/7}$-is-bulk-not-shear flag (:29) and booking-#3 (`mass = A1`) point the **same way**: the muon's excess reads as **dilatational/A1**, not couple-stress/T2 — which would make the "Cosserat torsion ladder" a **mislabel** of an A1 ladder. That is a *possible resolution*, and it is **NOT adopted here**: it is an unadjudicated inference, and adopting it would silently refill a slot Rule 12 says stays empty. Recorded as a Grant walk question (§8, Q4).

**★2026-08-02 repair-pass note on the above — :34 partially pre-empts it.** The ratified transduction chain **already** routes the muon's excess *energy* to A1 as the store, while keeping **torsion** as the frequency-setter. So "the excess is A1" is not a rival to canon; it is canon. What the :29 flag would additionally claim is that even the **setter** is bulk/dilatational rather than torsional-shear — a strictly narrower and still-live question. **Q4 (§8.2) is re-scoped to that narrower form** and does not turn on the store.

### 4.2 Is the muon booking consistent with the electron's own closure? — NO, in two independent ways

**(a) The energy-arithmetic inconsistency.** If the ladder is real and physical, an $n=0$ ground state on a **massive, costly** grade with a geometrically nonzero $\mathrm{Tw}=3/2$ carries a nonzero ground-rung energy $E_0$ (the zero-point of any real oscillator ladder is not zero). Canon's electron closure has **no slot for $E_0$** (§2, T3's $\tfrac12+\tfrac12$ is closed) and canon's ladder declares $n=0$ excitation-free ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):21). **These are compatible only if the ground-state (2,3) twist costs exactly zero — which no site derives, and which §3.3 + §3.2 + [`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559 all contradict.**

**(b) The spacing inconsistency (quantitative, §6).** The $n=0\to1$ rung costs $205.8\,m_ec^2$ (CODATA anchors) / $208.3\,m_ec^2$ (canon's closed form). The ground-rung twist energy, priced from canon's own $\gamma_c$ inputs on the **lattice-scale** normalization, lands at $\mathbf{O(10)-O(10^2)}\,m_ec^2$ (§6.3). **A ladder whose ground rung is within one order of magnitude of its first spacing is not a small perturbation on a torsion-free ground state** — it means the electron's own mass is *substantially* the twist energy the closure omits, and $m_e$ would not be the "torsion-free" anchor the whole ladder is built on. On the **weak-scale** normalization it is $\sim10^{-11}\,m_ec^2$ and the problem evaporates entirely. **The two readings are 12 orders apart and canon has not chosen — §6.2.**

### 4.3 What "no torsional excitation is present" does and does not zero — the precise scope

This is the closest thing canon has to a **ZERO** answer, so its scope must be exact.

- **It DOES zero:** the **excitation-ladder quantum count**, $n_{\text{torsion}}=0$ for the electron. Confirmed by the parallel wording at [`torus-knot-uniqueness.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md):106 (*"+ **0** Cosserat torsion quanta"*).
- **It does NOT zero:** the **couple-stress energy of the ground-state (2,3) winding itself**. The muon carries the *same* (2,3) (theory.md:43), so the (2,3)'s own twist is **common-mode across all three generations — IFF the ground-twist energy is generation-independent** (premise stated and forked immediately below) — in which case it **cancels out of every mass DIFFERENCE** and is invisible to the entire ladder. On that branch the ladder can be exactly right about $m_\mu-m_e$ and say nothing whatsoever about whether the common-mode ground twist is priced into $m_e$.

> **⚠ CORRECTED 2026-08-02 (repair pass; Rule 12 — the prior sentence is quoted here in full, not deleted).** The bullet above originally read, **unconditionally**: *"the (2,3)'s own twist is **common-mode across all three generations** — it **cancels identically out of every mass DIFFERENCE** and therefore is invisible to the entire ladder."* **The word "identically" and the unconditional form are RETRACTED: the cancellation needs a premise, and that premise is itself an open fork.** From §6.3's own energy form, with $\kappa = 2\pi\mathrm{Tw}/C_{loop}$ and $V_{tube}=\pi r_0^2C_{loop}=C_{loop}^3/4\pi$:
>
> $$E_{\text{twist}} \;=\; \gamma_c\,\kappa^2 V_{tube} \;=\; \gamma_c\Big(\frac{2\pi\mathrm{Tw}}{C_{loop}}\Big)^{\!2}\frac{C_{loop}^3}{4\pi} \;=\; \frac{\gamma_c\,(2\pi\mathrm{Tw})^2}{4\pi}\;C_{loop} \;\;\propto\;\; C_{loop}.$$
>
> **So the ground twist is common-mode iff the loop geometry $C_{loop}$ (with $\gamma_c$ and $\mathrm{Tw}$) is generation-independent.** Canon carries **both** readings and has adjudicated neither:
>
> - **Fixed-$\ell_{node}$ reading — the cancellation HOLDS.** [`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17, verbatim: *"In all three lepton generations, the geometric deformation (twist, curvature) describes a pattern of **dielectric saturation density** … **The nodes themselves remain fixed at $l_{node}$ spacing (Axiom 1).** The muon's 'twist' is a helical modulation of impedance density wound around the unknot loop … Neither involves physical displacement of lattice nodes."* Same loop, same $C_{loop}=\ell_{node}$, all three generations ⇒ $E_{\text{twist}}$ identical ⇒ **exact** cancellation in every difference.
> - **Compton-scaled reading — the cancellation FAILS.** [`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):28 sets the loop by the particle's own Compton length, $C_{loop} = \frac{\hbar/c}{m_e c^2} = \frac{\hbar}{m_e c}$; the standing precedent that this scales **per particle** is [`proton-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md):46 / :151 (Route A, verbatim: *"Charge radius $D_p = 4\lambda_p = 0.841$ fm | Ax4 (saturation transition radius); $\lambda_p = \hbar/(m_p c)$ = proton Compton wavelength | ✅ axiom-derived"*). On that reading $C_{loop}(\mu)=C_{loop}(e)/206.8$, hence $E_{\text{twist}}(\mu)=E_{\text{twist}}(e)/206.8$ — **the term does NOT cancel and the difference-ladder does see it.**
>
> **The premise fork is routed back into FLAG-4** (§7) — it is the same fixed-node-vs-scaled-geometry question that :17's dielectric-saturation booking already raises against the ratified (1)→(3) transduction chain (§4.1).
>
> **Verdict impact: NONE. "Identically" is weakened; UNACCOUNTED is not.** The verdict never rested on the cancellation. On the **fixed-$\ell_{node}$** branch the cancellation is exact and the ladder is blind to the term (the original argument, now conditioned). On the **Compton-scaled** branch the term *does* enter the difference — but as a $1/m$-scaling contribution **nowhere present** in canon's $m_\mu=m_e/(\alpha\sqrt{3/7})$ closed form, so the term is *still* unbooked, and the closed form additionally lands in tension with its own stated mechanism (§8.1 T2). **Both branches leave the electron's own closure — §2.2, a definitional identity with no sum — completely untouched, and that is what UNACCOUNTED rests on.**
>
> *(Convergence note: a sibling canonization lane working the same material independently reached the same iff-qualifier. Recorded as convergence only — that lane's leaf is unmerged and is **not** cited here as a source; the qualifier above stands on the two canon readings quoted above and on the $E\propto C_{loop}$ algebra, both re-derived in this lane.)*

**That is the whole finding in one sentence: on canon's fixed-$\ell_{node}$ reading the ground-state twist is the common-mode term the difference-ladder is structurally blind to; on the Compton-scaled reading it is a term the ladder's closed form has no slot for; and on both readings the electron's own closure is a definitional identity with no ledger to catch it.**

---

## §5 CLASSIFICATION

> ### VERDICT: **UNACCOUNTED.**
> Not ABSORBED — §2.2: the mass-closure sum was **never evaluated as a sum** (`clm-ka5zdx` rationale, verbatim: *"no quantity computed"*), so there is no ledger for a $\gamma_c$ term to be inside of; and the two sites that *do* write a closed sum (T3's $\tfrac12+\tfrac12$; T4's 1-D $\oint T_{EM}ds$) are **Class-A definitional identities** that are algebraically forced to $1.0\,m_ec^2$ and therefore neither absorb nor exclude anything physical.
> Not ZERO — §4.3: the only zero canon states ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):21) zeroes the **ladder quantum count**, not the ground (2,3)'s couple-stress energy; and canon separately affirms that the (2,3) rides the **couple-stress/curvature grade** ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):24), that microrotation is **"COSTLY"** ([`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md):559 — scope-qualified, §3.1), that the ground-state twist is geometrically $\mathrm{Tw}=3/2$ turns (§3.2), and that the winding sector carries a **nonzero** gapped mechanical mass ([`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41).
>
> **⚠ PREMISE MADE EXPLICIT 2026-08-02 (repair pass; §4.3).** The *common-mode-cancellation* leg — the argument that the generation ladder is structurally **blind** to this term — holds **IFF the ground-twist energy is generation-independent.** $E_{\text{twist}}=\gamma_c(2\pi\mathrm{Tw})^2C_{loop}/4\pi \propto C_{loop}$, so it holds on canon's **fixed-$\ell_{node}$** reading ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17, *"The nodes themselves remain fixed at $l_{node}$ spacing (Axiom 1)"*) and **fails** on the **Compton-scaled** reading ([`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):28; [`proton-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md):46/:151 precedent), where $E_{\text{twist}}(\mu)=E_{\text{twist}}(e)/206.8$. The prior unconditional wording *"cancels identically"* is retracted (§4.3, quoted in place). **The verdict does not depend on which branch wins** — on the fixed branch the term is invisible to the ladder; on the scaled branch it enters the difference with no slot in canon's closed form. Both leave §2.2 untouched.
> **The sharpest canon statement is an EXCLUSION-BY-DECLARATION of a nonzero quantity** (§3.3): the winding sector's mechanical mass is asserted real and asserted *"NOT the electron's rest-energy store"*, on grade-orthogonality grounds, **with no computation that it vanishes.**
>
> **⚠ CORRECTED 2026-08-02 (repair pass; Rule 12 — prior wording quoted, not deleted).** This line originally continued: *"…with no computation that it vanishes **and no account of where a rest-frame energy goes if not into the invariant mass**."* **That clause is retracted as over-strong.** Canon carries an account — the Grant-ratified transduction chain at [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):34 (block header :30): "more Cosserat torsion → faster flywheel → higher regulated frequency → (Compton $f = mc^2/\hbar$) deeper A1 depression → more mass. The flywheel regulates the frequency that *sets* the mass; the mass stays A1." The twist is priced as a **frequency-setter**, not an additive store. **The verdict is unchanged:** :34 **quantifies nothing** (no $E(\mathrm{Tw})$, no coefficient, no claim the transduction is lossless), and a flywheel that regulates $f$ still holds $\tfrac12 I_\omega\omega^2$ in the rest frame. See §3.3 and §8.2 Q2(d).

**Honest size of the hole (the two-sided answer, §6):** the magnitude is **gated on an already-flagged, unadjudicated symbol collision** — canon carries **two** Cosserat lengths, both written $\ell_c=\sqrt{\text{couple-stress}/\text{shear}}$, **6 orders of magnitude apart** ([`constants.py`](../src/ave/core/constants.py):331-337, *"Surfaced for auditor adjudication … not silently merged"*). Since $E_{\text{twist}}\propto\gamma_c\propto\ell_c^2$, the ballpark spans **12 orders**:
- **lattice-scale $\ell_c=\sqrt6\,\ell_{node}$ → $E_{\text{twist}}\sim 2\times10^{1}$ to $2\times10^{2}\ m_ec^2$** — the hole is *larger than the particle*, and the ledger is broken.
- **weak-scale $\ell_c\approx10^{-18}$ m → $E_{\text{twist}}\sim2\times10^{-11}\ m_ec^2$** — the hole is negligible and "UNACCOUNTED" is a bookkeeping nit, not a physics problem.

**So the twist-ledger question REDUCES TO an already-open corpus adjudication.** That is the most useful thing this audit produces: it converts a new open question into a **decision that was already on the board** and shows that decision is load-bearing for the electron's mass ledger and the entire generation spectrum — not just for naming conventions in Vol 9.

---

## §6 The ballpark — canon-supplied inputs only

**Class: paper arithmetic, order-of-magnitude only. NOT a simulation, NOT a prediction, mints nothing.** Driver: `research/drivers/twist_ledger_ballpark.py` (added by this doc; pure-constants, no solver, no lattice). Re-runnable: `PYTHONPATH=src .venv/bin/python research/drivers/twist_ledger_ballpark.py`.

### 6.1 ★A dimensional defect found in the canonical $\xi_K$ relation (FLAG-2, not repaired)

Canon states the relation at three sites. **The unit brackets exist at exactly TWO of them** — [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py):27-28 and [`k4_cosserat_coupling.py`](../src/ave/topological/k4_cosserat_coupling.py):33-34, verbatim:

```
  μ + κ = ξ_K1 · T_EM            (Cauchy + micropolar moduli, [Pa])
  β + γ = ξ_K2 · T_EM · ℓ_node²  (couple-stress moduli, [N])
```

The third site, [`q-g47-substrate-scale-cosserat-closure.md`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md):51-54, carries the **same relations as display math with NO unit brackets**:

$$\mu + \kappa = \xi_{K1} \cdot T_{EM}, \qquad \beta + \gamma = \xi_{K2} \cdot T_{EM} \cdot \ell_{\text{node}}^2$$

> **⚠ RE-ANCHORED 2026-08-02 (repair pass; Rule 12 — the prior anchor is recorded, not deleted).** This section originally read: *"Canon states, identically in three places — `cosserat_field_3d.py`:28, `k4_cosserat_coupling.py`:34, **`q-g47-substrate-scale-cosserat-closure.md`:58**"*. **The q-g47 anchor was WRONG.** `:58` is the ξ-**value** line (*"**Individual values closed (Sessions 19, 2026-05-18):** $\xi_{K1} = 8/3$ and $\xi_{K2} = 32$, both clean rationals."*) — correctly cited for the values in §9.1 row 10, and correctly cited in the driver's `XI_K1, XI_K2` comment. The **relations** live at `:51-54`, where they carry **no unit brackets at all**.
>
> **Restated correctly: brackets at two code sites; the same relation without brackets at the KB site — and the KB site is dimensionally wrong there too.** [`q-g47-…`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md):56 names the symbol explicitly, verbatim: *"with $T_{EM}$ the **lattice's electromagnetic string tension** and $\ell_{\text{node}}$ the lattice pitch."* A string tension is [N]. So `:52`'s $\mu+\kappa = \xi_{K1}\cdot T_{EM}$ equates a **modulus** to a **tension** at the KB site as well, brackets or no brackets. **FLAG-2 is a three-site defect, but only two sites state the units.**

With the canonical `T_EM = 0.212 N` ([`constants.py`](../src/ave/core/constants.py):493), **both lines contradict their own unit brackets**: $\xi_{K1}T_{EM}$ is N, not Pa; $\xi_{K2}T_{EM}\ell_{node}^2$ is N·m², not N. The relations are unit-consistent **only** if the symbol `T_EM` in them denotes the **stress** $\sigma_0 \equiv m_ec^2/\ell_{node}^3 = 1.4218\times10^{24}$ Pa rather than the 1-D tension. **The stress reading is therefore forced by DIMENSIONAL ANALYSIS ALONE** — no corroborating check is needed, and (see below) none is available. **Surfaced, not fixed** — repairing a symbol overload inside a Grant-era closed derivation (Sessions 19) is an auditor/Grant call, not an implementer edit.

> **⚠ CORRECTED 2026-08-02 (repair pass; Rule 12 — the prior sentence is quoted here in full, not deleted).** This paragraph originally continued: *"**Independent confirmation that this is the intended reading:** under it, **and only under it**, the canonical cross-check reproduces exactly — $\ell_c^2=(\beta+\gamma)/[2(\mu+\kappa)] = \xi_{K2}/(2\xi_{K1})\,\ell_{node}^2 = 6\,\ell_{node}^2$, i.e. $\ell_c = 2.4495\,\ell_{node}$ vs $\sqrt6 = 2.4495$. Verified numerically in the driver."*
>
> **That cross-check is a NULL TEST, and both the "and only under it" clause and all "independently confirmed" language are RETRACTED.** $T_{EM}$ **cancels identically** between numerator and denominator:
>
> $$\ell_c^2 \;=\; \frac{\beta+\gamma}{2(\mu+\kappa)} \;=\; \frac{\xi_{K2}\,T_{EM}\,\ell_{node}^2}{2\,\xi_{K1}\,T_{EM}} \;=\; \frac{\xi_{K2}}{2\xi_{K1}}\,\ell_{node}^2$$
>
> — **whatever $T_{EM}$ denotes and whatever its units.** Tension, stress, or an arbitrary scale: the check returns $\sqrt6$ either way. **Both readings give $\ell_c/\ell_{node} = 2.44949 = \sqrt6$. DEGENERATE.** Canon says exactly this in the same breath, at [`q-g47-substrate-scale-cosserat-closure.md`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md):56, verbatim: *"**Self-consistency forces** $\xi_{K2}/\xi_{K1} = 12$, which is **independent of $T_{EM}$** — the ratio is purely K4-symmetry-forced (route 4 above)."* The code comment restates it with no stress scale anywhere in it, [`constants.py`](../src/ave/core/constants.py):326: `ℓ_c² = (β+γ)/[2(μ+κ)] = ℓ_node² · ξ_K2/(2·ξ_K1) = 6·ℓ_node²`.
>
> **The cross-check confirms only that $\xi_{K2}/2\xi_{K1} = 6$. It discriminates nothing.** The driver's block-2 print is retitled accordingly (`T_EM-INVARIANT CONSISTENCY CHECK, NOT A DISCRIMINATOR`) and now evaluates **both** readings side by side to show the degeneracy explicitly.
>
> **FLAG-2's core is UNAFFECTED and stands:** the moduli come out in **N** rather than **Pa** under `T_EM = 0.212 N`, and the stress reading is forced by dimensional analysis. Only the *supporting* corroboration claim was over-strong.

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
| **2** | **Dimensional defect in the canonical $\xi_K$ relations.** | §6.1. `μ+κ = ξ_K1·T_EM  [Pa]` and `β+γ = ξ_K2·T_EM·ℓ_node²  [N]` at [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py):27-28 and [`k4_cosserat_coupling.py`](../src/ave/topological/k4_cosserat_coupling.py):33-34 disagree with their own unit brackets under `T_EM = 0.212 N` ([`constants.py`](../src/ave/core/constants.py):493). Consistent only reading `T_EM` as $\sigma_0=m_ec^2/\ell_{node}^3$ — **forced by dimensional analysis alone.** **⚠ CORRECTED 2026-08-02 (repair pass, Rule 12 — prior clause quoted not deleted):** this cell originally ended *"; that reading is **confirmed by the $\ell_c=\sqrt6$ cross-check**."* **Retracted — that cross-check is a NULL TEST**: $T_{EM}$ cancels between numerator and denominator, so **both** readings return $\ell_c/\ell_{node}=2.44949=\sqrt6$ (DEGENERATE). Canon says so itself at [`q-g47-…`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md):56 (*"which is **independent of $T_{EM}$**"*) and [`constants.py`](../src/ave/core/constants.py):326. **The flag's core — moduli in N not Pa under `T_EM = 0.212 N`; stress reading forced — is UNAFFECTED and stands.** | **Auditor lane** — a symbol overload inside a closed derivation; three sites, one repair. |
| **3** | **The $\ell_c$ 6-OOM collision is load-bearing far beyond naming.** | [`constants.py`](../src/ave/core/constants.py):331-337 already flags it *"for auditor adjudication"* as a naming/referent issue. **This audit shows it gates the electron's mass ledger and the whole generation ladder** — 12 OOM on $E_{\text{twist}}$ (§6.3). Its priority should reflect that. | **Grant / auditor** — re-prioritize an existing open item. |
| **4** | **⚠ DEMOTED 2026-08-02 (repair pass).** Was: *"Three incompatible stores for $m_\mu-m_e$."* **Now: ONE two-way inconsistency** — store (2) vs the **ratified** (1)→(3) transduction chain. | **Retracted leg (Rule 12, quoted not deleted):** stores (1) rotational-DOF and (3) A1 were flagged as mutually inconsistent. They are **not** — [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):34 (Grant-ratified 2026-06-20 block at :30) adjudicates them: "more Cosserat torsion → faster flywheel → higher regulated frequency → (Compton $f = mc^2/\hbar$) deeper A1 depression → more mass. The flywheel regulates the frequency that *sets* the mass; the mass stays A1." Torsion = setter, A1 = store. **Surviving leg:** dielectric-saturation-density, node-displacement-free ([`lepton-spectrum.md`](../manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/lepton-spectrum.md):17 *"a pattern of **dielectric saturation density** … The nodes themselves remain fixed at $l_{node}$ spacing (Axiom 1) … **Neither involves physical displacement of lattice nodes**"*) **vs** that ratified chain — an $\varepsilon$-sector booking against a T2-setter/A1-store booking. **Also routed here (§4.3, 2026-08-02):** the same :17 fixed-$\ell_{node}$ reading is the premise the common-mode-cancellation argument depends on, and the rival Compton-scaled loop geometry ([`electron-unknot.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md):28; [`proton-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md):46/:151 precedent) breaks it. | **Grant** — same sector-of-storage family as charter **D1**; see §8. |
| **5** | **The engine can price this and never has.** | [`cosserat_field_3d.py`](../src/ave/topological/cosserat_field_3d.py) relaxes a **(2,3)** ansatz on an energy functional containing `gamma kappa·kappa` (:713) — but with `G = G_c = gamma = rho_vac = 1` natural units (:12, :942), never the $\xi_{K2}$/$\gamma_c$ calibration, and no result doc converts the relaxed integral to $m_ec^2$ units. Two-method absence-check in §9. | **Implementer follow-on** — §8 T1. |

**Not repaired, not reframed, not reconciled.** Per flag-don't-fix: both sides quoted verbatim with paths; no side edited to match the other.

**⚠ 2026-08-02 repair pass — what changed here and what did not.** **FLAG-4 was DEMOTED and FLAG-2's supporting argument was CORRECTED.** Both are corrections to *this audit's own over-strong claims*, not repairs of canon: zero canon files were edited by the repair pass, and both prior forms are quoted verbatim in place per Rule 12. **Five flags still stand, ZERO canon repairs still made.** The corrections narrow supporting claims; **the §5 verdict (UNACCOUNTED) is untouched by all of them** and each correction states its verdict impact explicitly.

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

**Q2 (the paperclip question, direct).** *Your clip stores spring tension in the pre-load. Canon says the electron's ω-grade is **massive** and that microrotation is **costly**, and it says that store is **"NOT the electron's rest-energy store"** — an exclusion by grade-orthogonality, not by a computation showing it is zero. **Where does that energy live, if not in $m_ec^2$?*** In a lossless reactive substrate at rest there is no radiation channel to carry it away, and Ax 3 forbids a dissipative one. Options as I read them: (a) it IS in $m_ec^2$ and `mass = A1` is a **labelling** convention over a total that A1 and T2 both feed; (b) it is genuinely zero for the ground (2,3) and something forces $\kappa_{\text{eff}}=0$ that canon hasn't stated; (c) the grade-orthogonality guard is doing more work than it was derived to do; **(d) — added 2026-08-02 repair pass; canon's own answer, which this audit's first pass missed and which therefore belongs on the menu — TRANSDUCTION, not storage.** [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):34 (Grant-ratified block at :30): "more Cosserat torsion → faster flywheel → higher regulated frequency → (Compton $f = mc^2/\hbar$) deeper A1 depression → more mass. The flywheel regulates the frequency that *sets* the mass; the mass stays A1." On (d) the twist is priced as a **frequency-setter**, the energy lands on A1 via $m=\hbar f/c^2$, and there is **no second joule to place**. **The residue (d) still owes an answer to:** a rotor turning at rate $f$ carries $\tfrac12 I_\omega\omega^2$ in the rest frame *whatever it also regulates* — is that store exactly **zero**, or is it **real and merely not-labelled-mass**? Plumber form: *the governor on a flywheel sets the engine's speed — but the flywheel still has angular momentum and still has $\tfrac12 I\omega^2$ in it.* **Which — (a), (b), (c), or (d)?**

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

### 9.3.4 ★The budget-site sweep that corrected §2.1's count from FOUR to FIVE (added 2026-08-02 repair pass)

**Method A** — `git grep` against `origin/main`, pathspec by directory (not a `**` glob — those silently false-negative):

```
git grep -n -I -E '(tfrac|frac)\{?1\}?\{?2\}? *[LC]_' origin/main -- manuscript/ave-kb \
  | grep -v '\.index/' | grep -E 'm_ec\^2|m_e c\^2|m_0 ?c\^2'
```

**Method B** — filesystem `grep -rn`, orthogonal pattern (anchor on the equated rest energy, not on the fraction):

```
grep -rn -I -E '=[^|]*m_e ?c\^2' manuscript/ave-kb --include='*.md' | grep -v '/\.index/' \
  | grep -E 'tfrac\{1\}\{2\}|frac\{1\}\{2\}|tfrac12'
```

**Both methods independently return [`l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) at `:19`, `:90`, `:114`, `:115`** — the T5 site the original four-way enumeration missed. Full classification of the union of hits:

| Site | Class |
|---|---|
| `mass-closure-theorem.md`:52, :54 | **budget statement** — T1, T2 |
| `relativistic-inductor-newtonian-limit.md`:24 | **budget statement** — T3 |
| `electron-unknot.md`:48 | **budget statement** — T4 |
| `l3-electron-soliton-synthesis.md`:19, :90, :114-116, :118 | **budget statement — T5, ADDED** |
| `relativistic-inductor.md`:28 | **restatement family** — same closure as T3, and it writes the $\xi_{topo}$ cancellation out longhand (quoted in §2.2b) |
| `resonant-lc-solitons.md`:20, :23 | **restatement family** — $E_{mag}=\tfrac12(\xi_{topo}\dots)$ + the Virial split |
| `single-substrate-scale.md`:24, :75, :126 | **index / cross-reference rows** pointing at `relativistic-inductor.md`:28 |
| `electron-identification.md`:165 | **restatement family** — the 50/50 propagation already noted in §2.1 |
| `vol4/claim-quality.md`:200 | **canon self-label** — *"structural (Virial decomposition), not an independent rest-mass derivation — $m_e$ is taken as given"*; **independently confirms §2.2** |
| `vol1/claim-quality.md`:1408, `parametric-coupling-kernel.md`:54/:430, `higgs-mass.md`:44, `yang-mills-steps1-2.md`:35, `dielectric-rupture.md`:19, `cvr-phasor-reactance.md`:37, `vol4/claim-quality.md`:1615 | **not electron rest-energy budgets** — one-scale-import note, pump-kernel, Higgs/YM/rupture/phasor contexts |

**Result: five budget statements (T1–T5), a four-leaf restatement family that propagates them, and one canon self-label that confirms §2.2. Not one of them contains a $\gamma_c$ / couple-stress term.** The §2.1 count is corrected in place with the prior wording quoted (Rule 12).

### 9.4 Numeric receipts (banked; re-runnable via `research/drivers/twist_ledger_ballpark.py`)

```
U_AVE = T_EM * l_node                      = 8.187106e-14 J = 1.000000 m_e c^2   (Class A, forced)
--- T5 (l3-electron-soliton-synthesis.md:90/:98-105), added 2026-08-02 repair pass ---
xi_topo = e/l_node                         = 4.149005e-07 C/m  (= constants.py:356)
L_0 = xi_topo^-2 * m_e                     = 5.291772e-18 H
I_max = xi_topo * c                        = 1.243840e+02 A
C_e = e^2/(m_e c^2)                        = 3.135381e-25 F
V_SNAP = m_e c^2 / e                       = 5.109989e+05 V
1/2 L_0 I_max^2 / (m_e c^2)                = 0.500000
1/2 C_e V_peak^2 / (m_e c^2)               = 0.500000
SUM                                        = 1.000000   (Class A, forced)
xi_topo scaled x1 / x7 / x1e6 -> 1/2 L I^2 = 0.500000 / 0.500000 / 0.500000
   => xi_topo CANCELS IDENTICALLY; clm-ka5zdx:1258's strengthen-by is trivially
      satisfiable, hence vacuous (audit 2.2b)
--- end T5 ---
sigma_0 = m_e c^2 / l_node^3               = 1.4218e+24 Pa
beta+gamma = xi_K2 * sigma_0 * l_node^2    = 6.784439e+00 N     [N] OK
l_c | stress reading                       = 2.44949 * l_node
l_c | tension reading                      = 2.44949 * l_node    <- DEGENERATE (T_EM cancels)
canon sqrt(6)                              = 2.44949             T_EM-INVARIANT NULL CHECK
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
