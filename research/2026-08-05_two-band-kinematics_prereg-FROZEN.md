# Two-band / k·p kinematics of the K4 carrier sector — FROZEN pre-registration

**Date:** 2026-08-05 · **Lane:** two-band kinematics (Grant GO 2026-08-05)
**Branch:** `research/two-band-kinematics` · **Status:** FROZEN — pushed alone, before any driver code exists.
**SVA pilot case:** 4 (Standard Vacuum Analysis v0.1-pilot, `manuscript/ave-kb/common/standard-vacuum-analysis.md`).
**Companion:** Lorentz-compliance arc LC-1 (`_orchestration/2026-08-04_lorentz-compliance-arc-brief.md:44`).

**North star (one line).** Does the K4 carrier sector's near-gap dispersion take the relativistic
massive form $E(k)^2 = (E_g/2)^2 + (\hbar v k)^2$, and is the carrier limiting velocity $v$ equal to
the EM-channel speed $c_{EM}=\sqrt{G/\rho}$?

---

## §0 — Standard Vacuum Analysis header (SVA v0.1-pilot)

```markdown
 1. SECTOR / OWNERSHIP:      Carrier = Cosserat micro-rotation (ω) sector — the winding/charge owner
                             (carrier-sector arc; `cosserat-mass-gap.md` §4 Rule-12 re-scope: the ω-gap
                             is the FLYWHEEL CLOCK gap, NOT the rest-mass store, which is A1 dilatation).
                             The comparison speed c_EM = √(G/ρ) is the massless transverse-TRANSLATIONAL
                             u-pair (G2 ruling 2026-07-03, `cosserat-mass-gap.md`:158). Cross-wiring check:
                             the gap is read on ω; the speed is read on u; mass (A1) is NOT invoked. The
                             ONLY sector claim made is about the ω-branch's own kinematics.
 2. REGIME / PHASE-STATE:    MODE = cold linear (small-signal) Bloch band structure. REGIME = sub-yield,
                             Axiom-4 saturation OFF (k_op10=k_refl=k_hopf=0, κ_chiral inactive — it is
                             saturation-only, `cosserat_field_3d.py`:562). PHASE-STATE = unbroken free-wave;
                             no load-bearing saturated site, no Op14 local-clock modulation. DC bias point:
                             flat (A=0). Small-signal is EXACT here by construction.
 3. CIRCUIT STATEMENT:       Two coupled reactive ladders share every node. Ladder-u (translational) is a
                             plain LC line: no shunt-to-ground ⇒ passes DC ⇒ gapless, phase velocity
                             √(G/ρ). Ladder-ω (micro-rotation) has a SHUNT SPRING TO GROUND at every node
                             (the G_c micropolar restoring torque) ⇒ a high-pass line with cutoff ω_m ⇒
                             gapped. The two ladders are cross-coupled through the same G_c element (it
                             appears once as the shunt and once as a mutual-coupling transformer). QUESTION:
                             does the gapped ladder's cutoff line have the SAME characteristic velocity as
                             the plain ladder? TOTAL-vs-SLOT: v is read as the TOTAL branch curvature of
                             the exact 12×12 eigenproblem, not as the γ-slot's own √(2γ/I_ω) label — the
                             slot value and the total can differ by the cross-coupling (k·p) term, and
                             separating them is the whole point.
 4. PLANE & PROJECTION:      No Γ or Z claim is made in this lane. Reference plane for the dispersion is the
                             Bloch cell boundary (per-bond phase k·p_ℓ); the projection is the eigen-branch
                             decomposition of D(k) by eigenvector CHARACTER (u-weight vs ω-weight), not by
                             sort order (the sectors interleave in energy — the P-wave at √(10/3) sits above
                             the gap). Declared so the "which branch is the carrier" read is a computed
                             projection, not a chosen index.
 5. CONSTITUTIVE PROVENANCE: G (shear)        — natural-unit normalization, sets c_EM ≡ 1 ...... ENG-CHOICE (normalization)
                             G_c (micropolar) — engine default 1.0 (`cosserat_field_3d.py`:941) .. ENG-CHOICE (phase-I placeholder)
                             γ (curvature)    — engine default 1.0 ................................ ENG-CHOICE (phase-I placeholder)
                             ρ, I_ω           — engine defaults 1.0 (`:954` "phase-I placeholder") . ENG-CHOICE
                             m² = 4G_c/I_ω    — the FACTOR 4 ..................................... DERIVED (operator convention, `clm-jz0xaw`)
                             gap VALUE ~1 MeV — see the VALUE-PROVENANCE axis, §1 ................ [BRACKETED — resolved as a required output]
                             ω_C = c_0/ℓ_node — IDENTITY (`constants.py`:294) given ℓ_node ≡ ħ/(m_ec) IMPORTED (CODATA m_e)
                             c_EM = √(G/ρ)    — the massless transverse-u branch ................. DERIVED (V1 gate, `clm-j550uh`)
 6. ENERGY LEDGER:           Rim-only. Every quantity here is a within-system REACTIVE exchange between the
                             u and ω storage elements of one lossless Hermitian quadratic form. NO port is
                             crossed; no radiation, no detector, no topology change. Therefore NO loss word
                             is used anywhere in this lane — no "damping", no "dissipated", no Q. D(k) is
                             Hermitian and its eigenvalues ω²(k) are real by construction; a complex ω would
                             be a BUG, not physics, and is gated as such (G4).
 7. CALIBRATABILITY:         The target IS a dimensionless ratio: v/c_EM. It is measured entirely inside the
                             same operator with the same length and time units, so it is self-calibratable
                             and immune to the ℓ_node / ω_C unit bridge. The gap VALUE (MeV) is NOT
                             self-calibratable and is therefore NOT on any verdict path — it is reported on
                             the separate VALUE-PROVENANCE axis only.
 8. DISCRIMINATION CLASS:    pure-AC (cold linear band structure of an undriven medium) ⇒ DEAD ON ARRIVAL as
                             a discriminator, and declared so up front. SM counterfactual: the Dirac equation
                             POSTULATES E²=(mc²)²+(pc)² with v≡c; Wilsonian universality says any gapped
                             two-band lattice yields the same form near the gap. So a PASS is emergence-class
                             FORM-derivation at peer-with-SM strength, NOT a chord. Tautology filter: the
                             identity m*=E_g/(2v²) is ALGEBRAICALLY FORCED by the form ω²=ω_0²+v²k² and is
                             therefore reported as an internal-consistency check, NOT as a result. The only
                             non-tautological content is (a) whether the exact lattice dispersion HAS that
                             form and (b) the NUMBER v/c_EM.
 9. CERTIFICATION PLAN:      Gates G1–G8 (§4) frozen below before any number exists; tolerances derived from
                             the expansion's own truncation order (§3 NUMERICAL CONDITIONING), not chosen for
                             convenience. UNRUN ≠ PASSED — every gate reports RUN/UNRUN explicitly. Negative
                             control: reproduce the certified predecessor (PR #392 V1–V4: c_EM=1, c_R=√2,
                             m²=4, 6 gapless translational branches) on the imported canonical operator
                             BEFORE any new number is read. Second negative control: G_c→0 must close the gap
                             AND collapse the branch splitting (G6).
10. ADJUDICATION ROUTING:    This run settles ONLY the FORM + the v/c_EM ratio for the ω-sector carrier of the
                             canonical Cosserat operator. On FORM-REPRODUCED-v=c → LC-1 gains a constructive
                             one-speed result for the carrier channel. On FORM-REPRODUCED-V-MISMATCH → report
                             plainly as a kill-condition-class input to LC-1; it does NOT by itself fire LC-1's
                             kill (that needs the branch to be an energy-carrying INTER-EVENT channel, which
                             this lane does not establish). FENCE — what this lane does NOT license: (i) any
                             statement about the electron's rest-mass VALUE; (ii) any claim that the ω-branch
                             IS the electron (the corpus's own re-scope says the ω-gap is the clock, not the
                             mass store); (iii) any Zitterbewegung claim — §6 is a documented consequence,
                             mints nothing; (iv) any propagation to the manuscript beyond the single fenced
                             KB leaf named in the trigger-6 condition.
```

---

## §1 — STEP 0: VALUE-PROVENANCE of the Cosserat rotation-sector gap (frozen finding, pre-derivation)

This axis is settled by corpus READING, before any computation, and is reported independently of the
form derivation. Re-located per the brief's instruction (the cite has line-shifted).

**Re-location.** The brief cites `trampoline-framework.md:188`. At HEAD (`773fe007`) line 188 is the
Cosserat microrotation EOM $I_\omega\ddot{\boldsymbol\omega}=\nabla\cdot\boldsymbol\mu+2\sigma^A+\mathbf g$;
the gap statement is now at **`manuscript/ave-kb/common/trampoline-framework.md:192`**, verbatim:

> **Mass gap in the rotation sector:** $m_\omega^2 = 4 G_c / I_\omega$ where $G_c$ is the Cosserat
> couple-stress modulus. Period $T = 2\pi/\omega_m = \pi$ in natural units. **Verlet-validated** at
> doc 41 §2-§3; E-046 canonical.

Pure line-shift, correct-when-written class. Canonical home is
`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md` (`clm-jz0xaw`,
`clm-dhvhwi`).

**No MeV value is stated at either site.** A repo grep for a MeV-tagged Cosserat-gap value returns
nothing; the "~1 MeV" in the brief is an inference, and the prereg treats it as such. The arithmetic
that produces it is: the driver's frequency unit is $c_0/\ell_{node} \equiv \omega_C$ (bond length set
to $\ell_{node}$, `cosserat_band_structure_two_sublattice.py`:90; $c_0=\sqrt{G/\rho}=1$ by the V1 gate),
so $\omega_m = 2 \Rightarrow \hbar\omega_m = 2\,m_ec^2 = 1.022$ MeV.

**VERDICT (frozen, pre-derivation): the gap VALUE is IMPORTED / placeholder-set; the FACTOR is DERIVED.**

| component | provenance | receipt |
|---|---|---|
| the factor **4** in $m^2=4G_c/I_\omega$ | **DERIVED** (2×2: antisymmetric-pair $\Sigma_{ij}$ doubling × Lagrangian→EOM Hessian) | `cosserat-mass-gap.md`:61 |
| $G_c = 1$, $I_\omega = 1$ | **ENG-CHOICE placeholder** — verbatim `cosserat_field_3d.py`:12 *"Moduli pinning (natural units, ell_node = 1): G = G_c = gamma = rho_vac = 1"*; `:954` *"Defaults rho = I_omega = 1 in natural units (phase-I placeholder;"* | no `constants.py` symbol exists for either |
| the resulting $\omega_m = 2$ | **forced by the placeholder choice**, not by the substrate | $2\sqrt{G_c/I_\omega}$ |
| the MeV scale | **IMPORTED from CODATA $m_e$** via $\ell_{node}\equiv\hbar/(m_ec)$ | `cosserat-mass-gap.md`:143 verbatim: *"the substrate parameters $\rho, I_\omega, G_c$ **calibrated to** $\ell_{node} = \hbar/(m_ec)$"* |
| corpus's own tag | **"placeholders … rather than measured-from-substrate"** | `cosserat-mass-gap.md`:151 verbatim |

This is the corpus's own FORM-deriving / VALUE-importing meta-finding
(`manuscript/ave-kb/common/form-deriving-value-importing.md`), one more instance. It is recorded and
**quarantined**: no gate in §4 and no bin in §5 reads the MeV value, and the form derivation is run
entirely in dimensionless modulus ratios so the provenance verdict cannot contaminate it in either
direction.

**⚠ FLAG-1 (carried, NOT resolved here) — a factor-2 tension between the gap's two readings.** If the
$\omega$-branch is read relativistically, the branch bottom is the REST frequency ($\hbar\omega_0 = E_g/2$)
and the $\pm\omega$ interband splitting is $E_g = 2\hbar\omega_0$. With the placeholder moduli
$\omega_0 = \omega_m = 2\omega_C$, giving $E_g = 4m_ec^2 = 2.044$ MeV — **not** the 1.022 MeV the
Zitterbewegung/pair-threshold identification wants. To land $E_g = 2m_ec^2$ the branch bottom must be
$\omega_C$, i.e. $G_c/I_\omega = 1/4$, not 1. Either the placeholder is off by 4 in $G_c/I_\omega$, or
$\omega_m$ is being read as the FULL gap rather than the branch bottom, or the two "2"s (A-008's
frame-vs-field double cover, `trampoline-framework.md`:226-227, and the KG $\pm$ splitting) are being
double-counted. Surfaced verbatim per flag-don't-fix; **not adjudicated in this lane**, and no gate
depends on it.

## §2 — Sector-ownership carve + two flags raised against the brief (RULE ZERO)

**Carve.** The carrier lives on the Cosserat micro-rotation / winding sector. The gap used is THAT
sector's own gap ($m^2 = 4G_c/I_\omega$, the on-site micropolar restoring torque), read off the
$\omega$-character eigenbranches by computed eigenvector projection. The comparison speed $c_{EM}$ is
read off the $u$-character massless transverse branches of the SAME operator at the SAME $k$ — one
operator, one unit system, so the ratio is unit-free.

**⚠ FLAG-2 — the brief's dispersion-model instruction contradicts the corpus for THIS sector.**
The brief directs: *"the canon-adjudicated dispersion model (`srs-band-structure.md`, the
arccos/coined-quantum-walk map, `clm-bnd5rq` — the graph-Laplacian map is canon-REJECTED; do not use
it)"*. The corpus scopes that adjudication to the SCALAR channel only. Verbatim,
`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`:88-89:

> because the scalar arccos map does **NOT** cleanly generalize to the vector channel (3 acoustic
> branches, 2 distinct speeds $c_P\neq c_S$, anisotropic per-site self-block ⇒ no single
> $\omega_{\text{link}}$).

The canonical VECTOR/Cosserat band model in the corpus is the elastic dynamical-matrix eigenproblem
$\omega^2 = \mathrm{eig}(D)$ — used by the canonical vector survey itself
(`src/scripts/vol_1_foundations/srs_vector_band_survey.py`) and by the canonical Cosserat two-sublattice
operator (`src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py`, PR #392,
CI-gated at `src/tests/test_cr_rotational_curvature_sqrt2.py`). **RESOLUTION TAKEN (declared, not
silent):** this lane uses the canonical Cosserat dynamical-matrix operator, because it is the
adjudicated model *of the sector that owns the gap*, and because it is the only operator in the corpus
that CARRIES a $G_c$ gap term at all — the arccos map has no micropolar DOF to gap. The brief's
instruction is flagged as scope-overreach, not followed, and not silently reframed.

**⚠ FLAG-3 — the canonical Cosserat operator runs on the z=4 DIAMOND CONTROL net, not the ratified
z=3 srs production carrier.** `cosserat_band_structure_two_sublattice.py`:77-84 uses
`TETRA_OFFSETS` = the four tetrahedral $(\pm1,\pm1,\pm1)$ even-parity ports, i.e. diamond, $z=4$.
The corpus labels that net the **control**: `src/ave/core/chiral_lattice.py`:240 verbatim
*"Canonical diamond (engine-'K4', degree-4, achiral) **control** net"*, against
`:231` *`carrier="srs-z3",  # the D1-ratified production carrier (Axiom-1's object)`* and
`manuscript/ave-kb/common/lattice-model-register.md`:24 (*"the physical chiral srs net at pitch
$\ell_{node}$, $z=3$, right-handed $I4_132$"*). So the sector's own canonical gap + band structure
live on the CONTROL connectivity. **Mitigation taken (pre-registered):** the derivation is run on BOTH
connectivities — the canonical diamond operator (primary, so the result is comparable to the certified
V1–V4 receipts) AND the same micropolar energy functional re-assembled on the z=3 srs net (8-site
conventional cell, 48×48), as gate G7. If the FORM and the $v/c_{EM}$ ratio agree between them, the
connectivity flag is de-risked for this result; if they disagree, that disagreement is the headline.

## §3 — The derivation, frozen BEFORE computing

**D1 — canonical link map + independent rebuild.** Import
`dynamical_matrix_two_sublattice` (the CI-gated canonical operator) and, separately, rebuild the same
12×12 $D(k)$ from the engine energy functional
$W = \tfrac23 G(\mathrm{tr}\,\varepsilon)^2 + G|\varepsilon_{sym}|^2 + G_c|\varepsilon_{asym}|^2 + \gamma|\kappa|^2$
by an INDEPENDENT symbolic route (sympy, exact rationals + symbolic $k$). Assert the two agree at
random $k$ to machine precision (G1). This is the reproduction gate: no new number is read off an
operator that has not first reproduced the certified one.

**D2 — the two bands at $k=0$, exactly.** Both gradient symbols vanish at $k=0$
($G^{self}_j = -\tfrac14\sum_\ell p_\ell^j = 0$ identically, $G^{cross}_j(0)=\tfrac14\sum_\ell p_\ell^j = 0$),
so $D(0)$ is diagonal: a 6-fold $u$-manifold at $0$ and a 6-fold $\omega$-manifold at
$m^2 = 4G_c/I_\omega$. **Pre-registered structural statement:** the two-band split is
SECTOR-based ($u$ vs $\omega$, gap set by the ON-SITE $G_c$ term), NOT sublattice-based — the K4/diamond
bipartite doubling supplies a DEGENERATE PARTNER inside each manifold, not the gap. If the $k=0$
spectrum instead shows a sublattice-split gap, that expectation is wrong and gets reported as such.

**D3 — symbolic k·p to $O(k^2)$.** Write $D(k) = D_0 + D_1 + D_2 + O(k^3)$ with
$D_1 = O(k)$, $D_2 = O(k^2)$, from the exact expansion
$G^{cross}_j(k) = ik_j - \tfrac12|\epsilon_{jab}|k_ak_b + O(k^3)$ (using
$\sum_\ell p_\ell^jp_\ell^m = 4\delta^{jm}$, $\sum_\ell p_\ell^jp_\ell^ap_\ell^b = 4|\epsilon_{jab}|$).
Second-order degenerate perturbation theory on each manifold:
$$\lambda^{(\omega)}(k) = m^2 + P_\omega D_2 P_\omega + \frac{1}{m^2}P_\omega D_1 P_u D_1 P_\omega + O(k^4),$$
$$\lambda^{(u)}(k) = P_u D_2 P_u - \frac{1}{m^2}P_u D_1 P_\omega D_1 P_u + O(k^4).$$
Extract per-branch $v^2$ as a CLOSED FORM in $(G, G_c, \gamma, \rho, I_\omega)$ and direction $\hat k$.
This is the load-bearing step: $v^2$ is the TOTAL branch curvature, and it is NOT assumed equal to the
$\gamma$-slot label $2\gamma/I_\omega$ — the level-repulsion term is exactly what the k·p is for.

**D4 — full-dispersion verification, extended precision.** Diagonalize the EXACT $D(k)$ (no expansion)
with `mpmath` at 60 decimal digits, along $[100]$, $[110]$, $[111]$ and 8 pseudo-random directions, at
$k \in \{10^{-2},10^{-3},10^{-4},10^{-5},10^{-6}\}$. Report the residual
$R(k) = |\lambda_{exact}(k) - (m^2 + v^2_{sym}k^2)| / k^4$ and require it to CONVERGE to a finite
constant as $k\to0$ (that constant is the $k^4$ coefficient) — the sharp form of "the k·p is right".

**NUMERICAL CONDITIONING (declared, per the brief).** The $k^4$ extraction is a catastrophic-cancellation
problem of exactly the float64 $1-A^2$ class: at $k=10^{-6}$, $\lambda-m^2 \sim 2\times10^{-12}$ against
$m^2 = 4$ (relative $5\times10^{-13}$, already within 3 decades of float64 $\varepsilon m^2 \approx 9\times10^{-16}$),
and the second subtraction $\lambda - m^2 - v^2k^2 \sim k^4 = 10^{-24}$ is **fully below the float64
floor**. Mitigations, frozen: (i) all D4 arithmetic in `mpmath.mp.dps = 60`; (ii) the eigen-solve done
on the exact-rational-coefficient matrix, not a float64 down-cast; (iii) a float64 shadow run is
executed alongside and its DIVERGENCE from the mp result is REPORTED as the conditioning receipt (a
float64-only lane would have silently reported noise as the $k^4$ coefficient); (iv) $v^2$ itself is
taken from the SYMBOLIC D3 result, so the D4 residual is a genuine independent check, not a fit.

**D5 — the adjudication.** $c_{EM} = \sqrt{G/\rho}$ re-derived from the SAME operator (the $u$-manifold
transverse branch slope at the same $k$, same precision), never quoted. Compare $v/c_{EM}$ per
$\omega$-branch. **Frozen tolerance, derived not chosen:** the k·p truncation error at the extraction
point $k=10^{-6}$ is $O(k^2) = 10^{-12}$ relative; mp arithmetic at 60 dps contributes $\lesssim10^{-50}$.
Setting the tolerance three decades above the truncation floor gives
$$\boxed{\ \text{tol} = 10^{-9}\ \text{(relative, on } v^2/c_{EM}^2)\ }$$
$|v/c_{EM} - 1| \le \tfrac12\times10^{-9}$ ⇒ EQUAL; anything larger ⇒ MISMATCH, and the exact ratio is
reported in closed form.

**D6 — the $m^*$ identity.** Report $m^* = E_g/(2v^2)$ per branch. **Declared in advance as
TAUTOLOGICAL** (algebraically forced by $\omega^2 = \omega_0^2+v^2k^2$); it is run as an internal
consistency check on the numerics and is explicitly NOT counted as evidence.

**D7 — documented consequence, no claim minted.** The $\pm\omega$ interband oscillation frequency of a
gap excitation, $E_g/\hbar$, and its correspondence to Zitterbewegung; cross-referenced to
`research/2026-08-04_electron-ontology-walk_framing-note.md`, which this feeds and does NOT adjudicate.
FLAG-1's factor-2 tension rides along with it.

## §4 — GATES, frozen before any number exists (UNRUN ≠ PASSED)

| # | gate | criterion | class |
|---|---|---|---|
| G1 | independent symbolic rebuild == canonical `dynamical_matrix_two_sublattice` | max abs diff < 1e-12 at 5 random k | reproduction |
| G2 | negative control: reproduce PR #392 V1–V4 on the imported operator | $c_{EM}=1$ (rel<1e-3), $c_R=\sqrt2$ at $G_c{=}0$ (rel<5e-2), $m^2=4$ (rel<1e-2), 6 gapless $u$ branches (abs $\omega^2<$1e-6) | negative control |
| G3 | $D(0)$ block structure | exactly 6 eigenvalues $=0$ and 6 $=m^2$, and the eigenvectors are pure-$u$ / pure-$\omega$ (off-character weight < 1e-12) | structural |
| G4 | Hermiticity / reality | $\max|D-D^\dagger|<$1e-14 and all $\omega^2$ real ≥ 0 at every sampled k | lossless (SVA row 6) |
| G5 | k·p vs exact, extended precision | $R(k)=|\lambda_{exact}-(m^2+v^2k^2)|/k^4$ converges to a finite constant as $k\to0$ (ratio of successive decades → 1 within 1e-6) | verification |
| G6 | 2nd negative control: $G_c\to0$ | gap → 0 AND the $\omega$-branch $v^2$ splitting → 0 (all $\omega$ branches degenerate at $2\gamma/I_\omega$) | negative control |
| G7 | connectivity robustness (FLAG-3) | same micropolar functional on the z=3 srs net: FORM holds, and the $v/c_{EM}$ VERDICT (equal vs mismatch) is unchanged | robustness |
| G8 | float64 shadow diverges from mp | the float64 $k^4$ extraction is reported and shown to be noise-dominated at $k\le10^{-4}$ | conditioning receipt |

**Deterministic double-run digest.** The driver is run twice; the SHA-256 of the canonical-JSON result
must be byte-identical. Any RNG is seeded from a frozen constant.

## §5 — FROZEN BINS (verdict space, declared before the run)

| bin | fires when |
|---|---|
| **FORM-REPRODUCED-v=c** | $\omega^2=\omega_0^2+v^2k^2$ holds (G5 passes) AND $\lvert v/c_{EM}-1\rvert \le \tfrac12\times10^{-9}$ for the carrier branch(es) |
| **FORM-REPRODUCED-V-MISMATCH** | form holds, $v \ne c_{EM}$ beyond tol. **Reported plainly; NOT softened.** Kill-condition-class input to LC-1 |
| **GAP-SECTOR-MISMATCH** | the gap actually used turns out not to belong to the Cosserat/winding sector |
| **NO-TWO-BAND-STRUCTURE** | no gapped/gapless two-manifold structure exists at $k=0$ |
| **VALUE-PROVENANCE** | separate axis, ALWAYS reported (§1 — already frozen above, pre-derivation) |

Bins are not mutually exclusive across axes; VALUE-PROVENANCE is always reported alongside whichever
FORM bin fires.

## §6 — Classification (consistency-vs-emergence), declared

**Class: FORM-derivation / emergence-class, at PEER-WITH-SM strength. NOT a chord.** The SM
counterfactual is explicit: the Dirac equation POSTULATES this form, and Wilsonian universality says any
gapped bipartite lattice with a linear interband coupling reproduces it near the gap. The AVE-relevant
content is therefore (a) the constructive one-speed answer for LC-1 and (b) the NUMBER $v/c_{EM}$, which
is the only part that can come out "wrong". No AVE-distinct language is used anywhere in this lane.
Symmetric-standard note: the SM does not derive $v=c$ either — it builds it in — so a MISMATCH here is
informative and an EQUALITY here is peer, not superior.

---

**FREEZE.** No driver code exists at this commit. This document is pushed alone.
