# Electrostatic-sector fork memo — the atomic static-field exposure of the SVE elliptic kernel [FROZEN]

> ## 🔒 FROZEN — Grant ratification (2026-07-05), recorded verbatim
> **Grant ruling (2026-07-05, verbatim):** *"The fork memo is FROZEN — Grant's ratification is the
> freeze act; Problem 3 fires on it."*
>
> This memo is FROZEN as of this commit. The three pre-registered outcome bins ([A-CONSISTENT] /
> [B-AVE] / [C-EXCLUDED]) and the rejection of Keith's "radiative-not-static" arm are now **IMMUTABLE**:
> any later change is an **ERRATA BANNER ONLY** (append-only; the frozen body below is a record, NOT
> edited). **This freeze GATES Problem 3** — the muonic-hydrogen 2S–2P adjudicator (§1 Problem 3, §3
> [A]/[B]/[C], §4) fires on this freeze. The commit-time ordering (this freeze committed before any
> Arm-2 edit in the same PR) is the proof that Problem 3 was gated, not run, at freeze time.

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/letter-v2-arm2`
**Status:** **FROZEN (Grant-ratified 2026-07-05).** Was `[GRANT-RATIFY]` DRAFT; the ratification above is
the freeze act. The frozen body is a RECORD; changes are errata-banner-only.
**The freeze gates Problem 3 — the muonic-hydrogen ADJUDICATOR — only.** Problems 1–2 (the
no-solution radius and the Z-table of Coulomb fields) are pure kinematic reconnaissance; they are
DISCLOSED as already-run inputs to this memo (the tables in §1, verified this session) — they are what
MAKES the fork real and are stated up front so the pre-registration is honest about what is known.
Problem 3, the µeV-scale muonic-H comparison that adjudicates [A] vs [B] vs [C], fires on this freeze.
**Class:** PRE-REGISTRATION of a fork the substrate adjudicates. No claim minted; no number retracted.

> This memo states an exposure and PRE-REGISTERS three outcomes so the Problem-3 computation cannot be
> rationalized after the fact. Problems 1–2 (reconnaissance) are already run and disclosed in §1; the
> memo does NOT run Problem 3 (the adjudicator). The consonance noted in §2 is flagged with the knife
> armed: it is suggestive only, adjudicated exclusively by the frozen Problem-3 computation.

---

## 1. The exposure, stated plainly

The birefringence Letter (`papers/2026_birefringence_letter/main.tex`) presents a **continuum
constitutive law** — the vacuum permittivity `eps_eff = eps0 * sqrt(1 - (E/E_c)^2)` with
`E_c ~ 1.13e17 V/m` — **with no regime boundary**. The Letter validates it only in the deep-cold,
weak-field pump--probe sector (`A^2 = (E/E_c)^2 ~ 6e-7`, far below the yield knee). But **atomic
static electric fields are measured to sub-µeV precision**, and those fields are NOT weak against
`E_c`. A continuum saturating law with no floor makes a definite, checkable prediction in the atomic
static sector, and that sector is exquisitely constrained. If the kernel as written violates those
constraints, the Letter's constitutive law is exposed unless a regime boundary enters.

Keith's three problems, stated verbatim from the review context:

- **Problem 1 — `D_max` / no-solution radius for the elliptic kernel.** The elliptic kernel
  `S = sqrt(1 - (E/E_c)^2)` is real only for `E <= E_c`; the displacement `D = eps0 S E` turns over at
  `E = E_c/sqrt(2)` and has no single-valued continuation above it. Compute the radius, around a point
  charge, at which a Coulomb field reaches `E_c/sqrt(2)` (D-turnover) and `E_c` (no real `S`), i.e. the
  radius inside which the continuum kernel has no solution.

- **Problem 2 — the Z-table of Coulomb fields vs the landmarks.** Tabulate the Coulomb field
  `E = Ze/(4 pi eps0 r^2)` at the three physical landmarks: **muonic hydrogen** (Bohr-radius scale,
  ~285 fm), **U91+** (the 1s radius scale, ~575 fm), and the **Cu K-edge** (inner-shell, ~1.8 pm),
  and compare each against `E_c` (and against the no-solution radius of Problem 1).

- **Problem 3 — the muonic-hydrogen 2S–2P shift.** Compute the SVE kernel's contribution to the
  muonic-hydrogen Lamb shift and compare against the measured **2S–2P splitting 202.3706(23) meV**
  (Pohl et al./CREMA). This is the sharpest constraint: a µeV-scale continuum-kernel correction to a
  meV-scale measured splitting either fits under the error bar or it does not.

**Preview of the Problem-1/2 arithmetic (VERIFIED this session; the numbers that MAKE the fork real):**

| landmark | Z | r | `E_coul` (V/m) | `A^2 = (E/E_c)^2` | `r / ell_node` |
|---|---|---|---|---|---|
| muonic-H | 1 | 285 fm | `1.77e16` | `0.0246` | `0.738` |
| U91+ | 92 | 575 fm | `4.01e17` | **`12.6`** (`A^2 > 1`: kernel has NO real solution) | `1.489` |
| Cu K-edge | 29 | 1.8 pm | `1.29e16` | `0.0130` | `4.661` |

| no-solution radius (E = E_c) | Z=1 | Z=29 | Z=92 |
|---|---|---|---|
| `r_ns` (fm) | `112.9` | `607.8` | `1082.6` |
| `r_ns / ell_node` | `0.292` | `1.574` | `2.803` |

The exposure is real and unavoidable: at U91+ the continuum elliptic kernel has **no real solution**
(`A^2 = 12.6 > 1`); at muonic-H and Cu-K it is a percent-level correction to a static field, which at
µeV precision is enormous. **A continuum kernel with no floor is falsified in the atomic sector as
written** — UNLESS a regime boundary enters.

## 2. The AVE-native regime fact the memo turns on (each number verified vs `constants.py`)

**`ell_node = hbar/(m_e c) = 386.16 fm`** (the reduced Compton wavelength; `constants.py:282`
`L_NODE = HBAR/(M_E*C_0)`, live `3.8616e-13 m`). This is the **lattice pitch** — the founding
discreteness scale of the substrate (Axiom 1 Nyquist resolution, `constants.py:187`), NOT a
post-hoc hatch invented to escape Problem 3. It is the same `ell_node` that fixes `E_c` itself
(`E_c = V_yield/ell_node`, `constants.py:500`).

**Every landmark sits at or below a few lattice cells** (`r/ell_node` column above: 0.74, 1.49,
4.66), and **every no-solution radius sits at or below ~3 cells** (0.29, 1.57, 2.80). A continuum
constitutive kernel **has no meaning below the pitch** — the medium is discrete there, and a
smooth `eps(E)` is the wrong description by construction. This is not special pleading: the pitch
is the substrate's founding scale, present before this Letter existed.

**The consonance, stated HONESTLY with the knife armed.** Keith's data-derived floor — the radius
below which the continuum law would have to stop to protect the atomic-sector windows — comes out at
**~300 fm**. That sits **just under `ell_node = 386 fm`** (ratio `300/386 = 0.78`). This is
**suggestive**: the scale at which the continuum law must break, derived purely from atomic data, is
within ~20% of the substrate's own founding pitch, which the Letter never invoked for this purpose.
**It is NOT a result.** It is adjudicated ONLY by the Problem-3 computation: whether scoping the
kernel to `r >> ell_node` actually protects the muonic-H 2S–2P window at 202.3706(23) meV, with the
CORRECT cutoff-dependent coefficients, is what the frozen computation decides. A near-miss consonance
is exactly the kind of seductive pattern the discipline exists to guard against; the memo records it
as a flag, not a finding.

## 3. Pre-registered outcomes (FROZEN by Grant; Problems 1–3 fire only after)

- **[A-CONSISTENT] — the continuum kernel is already safe.** The kernel's atomic-sector shifts (the
  Problem-3 muonic-H contribution, and the Problem-2 Cu-K / muonic-H percent-level fields treated
  perturbatively) come in **under the µeV windows even without any regime scoping**. ⟹ The Letter is
  *stronger*: the same continuum law that predicts the pump--probe birefringence also survives the
  atomic static sector with no new structure. No regime boundary needed. (Note: this outcome must
  survive the U91+ no-real-solution point — [A-CONSISTENT] requires an honest account of why
  `A^2 = 12.6` at U91+ does not falsify, e.g. that the U91+ 1s density does not sample the near-nucleus
  field the way the naive point-Coulomb estimate suggests. If it cannot, [A] fails and [B] or [C]
  applies.)

- **[B-AVE] — the shifts violate the windows UNLESS the kernel is scoped to `r >> ell_node`.** The
  atomic-sector shifts exceed the µeV windows when the continuum kernel is run to `r -> 0`, but are
  protected once the kernel is scoped to `r >> ell_node = 386 fm` — **the lattice scale, NOT a new
  fitted parameter** (it is the founding pitch, `constants.py:282`, with canon provenance in the
  Axiom-1 Nyquist-resolution chain). ⟹ The regime boundary enters the Letter as the lattice scale.
  **Falsifiable bonus:** scoping to `r >> ell_node` produces **cutoff-dependent effective coefficients
  across the three probe energies** (8766 / 9835 / 12914 eV), DERIVED from `ell_node`, not fitted.
  Expected FORM (to be derived, not tuned): the leading cutoff correction to each probe's coefficient
  scales as `(q ell_node)^2` where `q` is the probe momentum transfer — i.e. the higher-energy probe
  carries a larger fractional correction, in a fixed ratio set by `ell_node` alone. The three
  coefficients are then over-determined by one scale, a distinct forward prediction.

  **Tension with clm-k4d4ph, and why the SCALAR channel can still be quadratic (derivation sketch).**
  The corpus's cubic-point-group result (`manuscript/ave-kb/vol4/claim-quality.md:520`, clm-k4d4ph)
  states that the K4/diamond-cubic Bloch dynamical matrix `D(k)` has its **first DIRECTIONAL
  ANISOTROPY at order `(q ell_node)^4`** — the cubic harmonic `Xi(q_hat) = q_x^4 + q_y^4 + q_z^4`,
  **quartic not quadratic, symmetry-protected by the `Fd-3m` point group** (a random bond set breaks
  it to quadratic). This looks like it forbids my `(q ell_node)^2` form. It does NOT, because the two
  are DIFFERENT channels — the same claim's own note (`:526`) records it: "the temporal cutoff
  `omega_C = c0/ell_node` is separate from this spatial quartic." Concretely:
  - The `(q ell_node)^2` correction I name is the **ISOTROPIC / scalar** cutoff term — the
    direction-AVERAGED leading Taylor coefficient of the lattice dispersion `omega^2(q) = c^2 q^2 [1 -
    a (q ell_node)^2 + ...]`. The scalar (angle-independent) piece is generically **quadratic**; there
    is no symmetry that forbids an isotropic `(q ell)^2` term (it is the trace part, present for ANY
    lattice).
  - clm-k4d4ph's quartic is the **first ANISOTROPIC (direction-dependent) invariant** — the cubic
    harmonic `Xi(q_hat)`, whose quadratic angular term is symmetry-KILLED by `Fd-3m` (the only
    invariant quadratic in `q_hat` is the isotropic `|q_hat|^2 = 1`, a constant, i.e. no angular
    dependence). So anisotropy first appears at quartic; isotropy appears at quadratic. No conflict.
  - **The Problem-3-relevant coefficient is the SCALAR one** (a birefringence coefficient magnitude
    per probe energy is a scalar per `q`, set by `|q|`, not by `q_hat` direction), so its leading
    cutoff correction is `(q ell_node)^2`. The anisotropic quartic is a SEPARATE, higher-order
    directional signature (and a distinct forward prediction in its own right).

  **HONEST HEDGE:** this is a derivation SKETCH, not the derivation. If the Problem-3 computation finds
  that the load-bearing correction is not the scalar dispersion term but a genuinely anisotropic one
  (e.g. because the near-nucleus Coulomb field probes a preferred lattice direction), the quartic
  `(q ell_node)^4` of clm-k4d4ph governs and the form is quartic. **Pending Problem 3, the [B-AVE]
  bonus FORM is stated as: scalar-channel `(q ell_node)^2` if the correction is isotropic (expected),
  anisotropic `(q ell_node)^4` per clm-k4d4ph if it is directional — the computation adjudicates
  which channel is load-bearing.** Either way the form is DERIVED from `ell_node`, not fitted; the
  over-determination-by-one-scale prediction holds in both channels.

  [B-AVE] is the outcome that turns the exposure into a strength: the same `ell_node` that sets `E_c`
  also sets the regime floor, and the floor makes a new, testable prediction.

- **[C-EXCLUDED] — the lattice-scale scoping fails to protect the windows.** Even with the kernel
  scoped to `r >> ell_node`, the atomic-sector shifts violate the µeV windows (e.g. the muonic-H
  contribution still overshoots 202.3706(23) meV by more than the error bar, or the cutoff cannot be
  placed at `ell_node` without an independent free parameter). ⟹ **The static-E sector of the SVE
  kernel is excluded as written.** Ledger the cost honestly:
  - **What dies:** the *continuum static-E constitutive law* as a universal claim — the `sqrt(1-(E/E_c)^2)`
    permittivity cannot be the vacuum's response to arbitrary static fields down to atomic scales.
  - **What survives (SEPARATE SECTORS, explicitly):** (i) the **pump--probe AC birefringence** of the
    Letter is a DIFFERENT sector — a deep-cold, weak-field (`A^2 ~ 6e-7`), *dynamic* (`d/dt != 0`)
    ε-varactor response read at optical/X-ray frequencies, NOT the atomic static-DC sector; its
    falsifier (the `~10^-3` flip-prob at HIBEF) is untouched by a static-sector exclusion. (ii) The
    **µ-sector / circulation keying** (`clm-pvlas1`, static-B transparency) is a DIFFERENT sector
    again — keyed on `partial_t B`, not on static flux, and not implicated by a static-E exclusion.
    A [C] verdict excludes the *continuum static-E extrapolation*, not the registered birefringence
    prediction and not the magnetic-sector side-prediction.

**Also recorded — Keith's original Outcome-B framing is REJECTED as the AVE fork arm.** Keith framed
his Outcome-B as *"the saturable response is radiative-not-static"* — i.e. the saturation lives in the
AC/radiative sector and the static sector is unsaturated. **This inverts the merged AVE Q-point
canon** and is NOT the AVE-native fork arm. The canon (Grant Reading-A; the AC/DC epistemological
carve) is that **matter's static DC bias IS what saturates**: the electron/matter is a self-biased LC
circuit sitting at a self-set Q-point (`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md`;
the merged birefringence prereg states it plainly, `research/2026-07-03_birefringence-hibef-prediction_registered.md:37`:
"The optical pump provides the DC operating point; the X-ray probe reads the AC differential index").
The DC operating point — the static bias — is precisely the saturating quantity; the AC probe reads a
*differential* about it. So the AVE fork arm is the OPPOSITE of Keith's: the static sector is where
saturation is MOST active (matter's own DC field biases the vacuum varactor hard), which is exactly
why the atomic static sector is the sharp constraint. Keith's "radiative-not-static" would put
saturation in the AC sector and leave the static sector free — that is the inversion. [B-AVE] above,
the lattice-scoping arm, is the AVE-native fork; Keith's radiative-not-static framing is not adopted.
(Honest caveat, flagged: the pump-probe-tslot result `research/2026-07-05_pump-probe-tslot_result.md:411`
notes a traveling wave DOES deposit a rectified 2nd-order bias the slow probe feels — the DC-only
scope is nuanced at 2nd order — but this refines *how* the DC bias is set, it does not move the
saturation into the radiative sector; the Q-point-is-the-saturating-bias canon stands.)

## 4. What freezes, and when Problem 3 fires

- This memo carries **[GRANT-RATIFY]** status. The three outcomes in §3 (including the U91+ caveat on
  [A], the scalar-vs-anisotropic FORM fork on [B] — `(q ell_node)^2` scalar / `(q ell_node)^4`
  anisotropic per clm-k4d4ph, computation-adjudicated — and the sector-survival ledger on [C]) are the
  pre-registered adjudication criteria.
- **Problems 1–2 are ALREADY RUN and disclosed (§1); Problem 3 is what the freeze gates.** The
  Problem-1/2 kinematics (no-solution radii; the Z-table of Coulomb fields) are verified in §1 and are
  the disclosed inputs that make the fork real — they are NOT held. Problem 3 (the muonic-H 2S–2P
  µeV-scale computation that adjudicates [A] vs [B] vs [C]) is the frozen computation, held until Grant
  ratifies this memo.
- On freeze, Problem 3 runs against these criteria; the substrate picks the arm; the result doc
  records the verdict without dropping or adding criteria post-hoc (Rule 11 honest closure).

## 5. Discipline tags + provenance
- **substrate-adjudicates-forks:** the fork is pre-registered; the engine/computation resolves it, not
  fiat. This memo freezes the criteria; it does not pick the arm.
- **flag-don't-fix:** the ~300-fm/`ell_node` consonance is surfaced as suggestive-only with the knife
  armed; not booked as a result.
- **regime/phase-state discipline:** the exposure is a MODE/REGIME statement — the Letter's validated
  regime (deep-cold, weak-field, dynamic AC pump--probe) vs the untested regime (atomic static DC,
  strong-field near-nucleus). A continuum kernel run outside its validated regime is the exposure.
- **sector-ownership:** [C]'s survival ledger keeps the ε-route (birefringence), µ-route (circulation
  keying), and static-E sectors DISTINCT; a static-E exclusion does not cross-wire into the AC or
  magnetic sectors.
- **verify-before-cite:** `ell_node = 386.16 fm`, `E_c = 1.13e17 V/m`, all Coulomb fields, `A^2`
  values, and no-solution radii live-derived vs `ave.core.constants` this session; muonic-H 2S–2P
  202.3706(23) meV is the Pohl/CREMA landmark (external, standard).
- **Anchored v1 untouched:** no birefringence-Letter number is edited by this memo; it concerns the
  UNvalidated static sector, disjoint from the anchored pump--probe prediction.
