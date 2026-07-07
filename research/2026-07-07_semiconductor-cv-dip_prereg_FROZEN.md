# PREREG (FROZEN) — Semiconductor device-analysis techniques mapped onto the vacuum cell + network

**Arc:** analysis/semiconductor-cv-dip · Task #17 (Grant-fired after an in-chat physical walk)
**Repo:** AVE-Core (PUBLIC) · **Branch:** analysis/semiconductor-cv-dip off origin/main (tree-proof: HEAD @ `cb38c9b9`)
**Date frozen:** 2026-07-07 · **Status:** PRE-REGISTRATION — expectations + deliverable bins + falsifiers, frozen BEFORE the RESULT/driver/figure.

> This document is frozen in its own commit. The RESULT doc, driver, figure, and tests land in
> subsequent commits and are adjudicated against the bins below. No bin is redefined post-hoc to
> convert a ❌ to a ✅ (Rule 11).

---

## REGIME HEADER (mandatory — read before any technique claim)

- **Substrate state:** COLD lattice ($A=0\Rightarrow S=1$ on every port), driven to a **quasi-static
  HELD bias** (a DC operating point), then probed with a **weak small-signal** wave.
- **Ax3-LOSSLESS below threshold:** the substrate is a lossless reactive network below the
  pair-production / rupture threshold. **Every device technique whose physics rests on carrier
  statistics, doping profiles, recombination/generation RATES, or thermal carrier populations
  transfers ONLY at/above the pair-production threshold**, where carriers become real (Regime IV
  onset). Below threshold those techniques have no carriers to count — they DO-NOT-TRANSFER, with the
  Ax3-lossless reason named.
- **Two critical voltages, two sectors (the whole point of this arc):**
  - **A1 longitudinal bond compliance** — $C_{eff}=C_0/S(V/V_{snap})$, DIVERGES at
    $V_{snap}=m_ec^2/e\approx 511$ kV (`nonlinear-vacuum-capacitance.md`:18 verbatim: "reaches
    $A^2=1$ ($C_{eff}\to\infty$) at $V_{snap}=m_ec^2/e\approx511$ kV"). Blessed device reading:
    the vacuum's turn-on / channel-inversion capacitance (pair production IS channel formation).
  - **T2 transverse dielectric** — $\varepsilon_{eff}=\varepsilon_0\,S(V/V_{yield})$, ROLLS OFF to
    zero at $V_{yield}=\sqrt\alpha\,V_{snap}\approx 43.65$ kV. Reading: reverse-biased depletion
    varactor (polarization runs out).
  - The pair $(V_{snap}:V_{yield})$ maps to a MOSFET's $(V_{th}:V_{BD,ox})$ — two critical voltages,
    different physics, one device.

## SECTOR HEADER + HOMONYM GUARD

- **Which sector?** Two orthogonal reactances ($A1\perp T2$, `master-equation.md`:20): the A1
  dilatation-MASS longitudinal bond compliance and the T2 transverse-field permittivity. They share
  the EE noun "capacitance"; identifying them is the genesis-24 double-count (`CLAUDE.md`:73).
- **Does the engine carry the DOF?** Yes — both are Axiom-1 spatial-DOF reactances modulated by the
  Axiom-4 kernel; no new solver is scaffolded (analytic, from `ave.core.constants`).
- **Cold or saturated?** Cold base, held to a DC operating point, small-signal-probed.
- **Five "A²" senses, named distinctly** (never cross-wired): (i) generic Ax4 kernel arg $A/A_{yield}$;
  (ii) the Letter's $(E/E_c)^2$; (iii) mechanical bond strain; (iv) **T2** $A_V=V/V_{yield}$;
  (v) **A1** $A=V/V_{snap}$. Homonym discipline is load-bearing: **this arc exists because of a
  cross-wire** (node-up writes the A1 divergent FORM $C_0/S$ but keys it on the T2 key $V_{yield}$).

## VERIFY-BEFORE-CITE — line-number drift FLAG (surfaced, not silently reconciled)

The Grant brief cites `node-up-small-large-signal.md`:104 / :360 for the ε-grade varactor line
($C_0/S(A_V=V/V_{yield})$). At branch tip `cb38c9b9` those are at **:105** (the keyed-argument
resultbox) and **:370** (the derived-vs-asserted ledger row). Re-grepped two ways (grep + Read). Both
are cited below; the drift is a revision offset, not a content change (verbatim content identical).

---

## CORPUS GROUNDING (re-grepped verbatim at branch tip — the load-bearing anchors)

| Anchor | Verbatim content (load-bearing) | Role in this arc |
|---|---|---|
| `CLAUDE.md`:73 | "$C_{eff}=C_0/S$ (↑) is the **longitudinal-A1 bond compliance** … a DISTINCT object from the **transverse-T2 permittivity** $\varepsilon_{eff}=\varepsilon_0 S$ (↓ …)" | The ratified sector split (Grant 2026-06-15). |
| `nonlinear-vacuum-capacitance.md`:18 | "reaches $A^2=1$ ($C_{eff}\to\infty$) at $V_{snap}=m_ec^2/e\approx511$ kV" with $S(V)=\sqrt{1-(V/V_{snap})^2}$ | A1 branch: divergence at $V_{snap}$. |
| `nonlinear-vacuum-capacitance.md`:20 (`def-vyvsn1`) | "$V_{yield}$ is the **transverse Cosserat ($T_2$) self-trap wall** … NOT the A1 compliance bound" | T2 keyed on $V_{yield}$; A1 on $V_{snap}$; the anti-cross-wire ruling. |
| `node-up`:105 (brief:104) | "$C_{eff}(V) = \frac{C_0}{S(A_V)}, \quad A_V = \frac{V}{V_{yield}}$ … $\varepsilon$-grade: VARACTOR, keyed on VOLTAGE" | **THE CROSS-WIRE**: A1's divergent form $C_0/S$ keyed on T2's key $V_{yield}$. R1 supersession target. |
| `node-up`:370 (brief:360) | "$C_{eff}=C_0/S(A_V)$, varactor keyed on $V$ \| **DERIVED** \| Axiom 4 dielectric specialization (`CLAUDE.md`:73)" | Same cross-wire in the ledger. |
| `device-circuit-models.md`:60 | "the large-signal chord/secant varactor $C_{\mathrm{eff}}=C_0/S$ vs the small-signal differential $C_{\mathrm{ss}}=\mathrm{d}Q/\mathrm{d}V=C_0/S^3$" (A1-scoped, $A\equiv V/V_{snap}$) | The chord/tangent operational pair (A1 side). Crown the **tangent** as the small-signal C. |
| `node-up`:229 | "the three-way varactor-convention tangle (surfaced for Grant, NOT resolved here)" | The OPEN Grant-adjudication item this arc composes into (a). |
| round-3 RESULT `:292-299` | T2 chord `C₀·S(A₀)`→`1−½A₀²` vs dQ/dV tangent `C₀·(S−A₀²/S)`→`1−(3/2)A₀²` (KEEP-BOTH, neither crowned) | The T2 chord/tangent pair for (a). |
| Letter `main.tex` Eq. (A5-A7) | $n_\perp=\sqrt S=(1-A^2)^{1/4}$; $n_\parallel=\sqrt{S-A^2/S}=\sqrt{(1-2A^2)/\sqrt{1-A^2}}$; $\delta n_{bir}=-\tfrac12 A^2$ | The eigenmode-check (c) target: are $n_\parallel,n_\perp$ the tangent and chord of the T2 kernel? |
| `graded-network-response.md`:50,:53 | "series $L$ per bond, shunt $C$ per node"; $\omega(q)=(2c_0/\ell_{node})|\sin(q\ell_{node}/2)|$ | K4 z=3 loaded-line ladder for (d). |
| `z0-derivation.md`:133-136 | "periodic chain of identical cells … Bloch/Floquet condition on the cell ABCD $\cos(q\ell_{eff})=(A+D)/2$" | ABCD/Bloch composition for (d). |
| round-2 prereg `:75-78,:119-121` | "the slow-drive limit … an unconstrained crossover is a declared open scale"; `𝒲_beat=(ω/ω_C)²·𝒲_var` | The OPEN slow-drive band for (f). |

---

## EXPECTATIONS (pre-committed)

1. **The C-V datasheet curve (b)** will show, on one log-V figure from canonical constants:
   - T2 branch $\varepsilon(V)/\varepsilon_0 = S(V/V_{yield})$ rolling off from 1 to 0 as $V\to V_{yield}=43.65$ kV.
   - A1 branch $C/C_0 = 1/S(V/V_{snap})$ (chord) and $1/S^3$ (tangent) diverging as $V\to V_{snap}=511$ kV.
   - The two features separated by the factor $1/\sqrt\alpha\approx11.7$ in voltage.
2. **The eigenmode check (c)** will confirm (sympy) that the Letter's $n_\perp$ is the **chord** $\sqrt S$
   of the T2 kernel and $n_\parallel$ is the **tangent** $\partial D/\partial E$ (the longitudinal
   eigenvalue $\sqrt{S-A^2/S}$), so the KEEP-BOTH chord/tangent fork is **corpus-resolved as the two
   polarization eigenmodes** (both real; the split IS the birefringence $\delta n_{bir}=-\tfrac12A^2$).
   PREDICTION: YES. If NO, report exactly what the Letter's two indices are and bin the fork still-open.
3. **The technique-transfer table (g)** will bin each device technique TRANSFERS / TRANSFERS-WITH-CAVEAT
   / DOES-NOT-TRANSFER with the Ax3 reason; carrier-statistics-dependent techniques bin
   DOES-NOT-TRANSFER below threshold.
4. **CONSISTENCY-class throughout.** The mapping re-expresses the Ax4 kernel + varactor + VCA canon in
   device-physics vocabulary. It originates NO new dimensionful number. The $\sqrt\alpha$ ratio
   $V_{yield}/V_{snap}$ is an $\alpha$-echo (Class-C). No emergence headline. Any claim beyond
   consistency-class is FLAGGED, not asserted.

## DELIVERABLE BINS

- **(a)** OPERATIONAL DEFINITIONS — chord (secant, large-signal) vs tangent ($dQ/dV$, small-signal) for
  BOTH A1 and T2; crown the tangent as "the small-signal compliance" per the C-V definition; keep the
  chord named as the large-signal secant.
- **(b)** the vacuum C-V datasheet curve (analytic, house-style figure) + shipped script + a test
  pinning curve values at named bias points.
- **(c)** the ⊥/∥ eigenmode check (R2 confirmation) verified against the Letter's actual $\Delta n$
  derivation; STAGE (do not land) the ruling text if YES.
- **(d)** COMPOSITION across the K4 z=3 series-L / shunt-C ladder (loaded-line + gradient-bias rider).
- **(e)** SPLIT C-V — separating T2 polarization from A1 compliance by "terminal-pair" selection.
- **(f)** FREQUENCY DISPERSION — POSE the properly-posed question (do not force an answer).
- **(g)** TECHNIQUE-TRANSFER TABLE.
- **(h)** STAGED R1 node-up:105/:370 supersession text (written in the RESULT for Grant; NO KB edit).

## WHAT WOULD FALSIFY THE MAPPING (pre-committed kill conditions)

- **F1 (kills c):** if the Letter's $n_\parallel$ is NOT the tangent $\partial D/\partial E$ of the T2
  kernel (i.e. the sympy identity $n_\parallel=\sqrt{S-A^2/S}$ fails, or $n_\perp\ne\sqrt S$), the
  chord/tangent = polarization-eigenmode identification is FALSE. Then (c) is binned still-open and the
  staged ruling is NOT written.
- **F2 (kills the sector-clean mapping):** if any C-V value at a named bias point requires a hardcoded
  number (not derivable from `ave.core.constants`), the "no new number" consistency claim is broken.
- **F3 (kills the anti-cross-wire discipline):** if the A1 divergence is found keyed on $V_{yield}$ or
  the T2 roll-off keyed on $V_{snap}$ anywhere in the shipped driver, the homonym guard has failed and
  the arc has reproduced the very cross-wire it exists to repair.
- **F4 (kills a spurious emergence claim):** if the mapping is headlined as deriving $V_{snap}$,
  $V_{yield}$, or $\alpha$ (rather than importing them), the consistency-vs-emergence tag is violated.

## LANE DISCIPLINE

Implementer lane. The R1 supersession text (h) is STAGED in the RESULT for Grant's adjudication — the
node-up cross-wire is a corpus-consistency call across (a)/(b)/(c) of the `node-up`:229 three-way
tangle, NOT an engine bug; the auditor lands any KB manual. Flag-don't-fix: surface both file paths +
verbatim content, do not reframe one to match the other.
