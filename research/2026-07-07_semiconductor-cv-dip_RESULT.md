# RESULT — Semiconductor device-analysis techniques mapped onto the vacuum cell + network

**Arc:** analysis/semiconductor-cv-dip · Task #17 · **Date:** 2026-07-07
**Prereg:** [`2026-07-07_semiconductor-cv-dip_prereg_FROZEN.md`](2026-07-07_semiconductor-cv-dip_prereg_FROZEN.md) (frozen commit `04734a68`)
**Driver:** `src/scripts/verify/semiconductor_cv_dip.py` · **Tests:** `src/tests/test_semiconductor_cv_dip.py` (13 green)
**Figure:** `manuscript/vol_9_vacuum_datasheet/figures/semiconductor_cv/vacuum_cv_datasheet.{pdf,png}`

> **CLASSIFICATION (consistency-vs-emergence): CONSISTENCY-class throughout.** This arc re-expresses
> the Axiom-4 kernel + the varactor/VCA canon in device-physics (BJT/MOSFET/GaN) vocabulary. It
> originates NO new dimensionful number; every value is imported from `ave.core.constants`. The
> $\sqrt\alpha$ ratio $V_{yield}/V_{snap}$ is an **$\alpha$-echo** (Class-C). No emergence headline
> (prereg F4). The one AVE-distinct categorical prediction that this mapping *touches* — the exact
> static-$\mathbf B$ transparency — is already canon (`node-up`:147, the Letter Eq. staticB); this arc
> adds no new chord, it organizes the existing one in device language.

---

## REGIME HEADER (mandatory)

Cold lattice ($A=0\Rightarrow S=1$), driven to a **quasi-static HELD bias** (a DC operating point),
probed with a **weak small-signal** wave. **Ax3-LOSSLESS below threshold.** Every device technique
resting on carrier statistics, doping, or recombination/generation RATES transfers ONLY at/above the
pair-production threshold, where carriers become real (Regime IV). Below threshold there are no
carriers to count — those techniques DO-NOT-TRANSFER, with the Ax3-lossless reason named (table g).

**The two critical voltages (the whole point):**
- **A1 longitudinal bond compliance** — $C_{eff}=C_0/S(V/V_{snap})$, DIVERGES at $V_{snap}=m_ec^2/e
  \approx511$ kV (`nonlinear-vacuum-capacitance.md`:16). Device reading: **turn-on / channel-inversion
  capacitance** — pair production IS channel formation; the diverging $C$ approaching $V_{snap}$ is the
  device signature of imminent carrier injection (forward-bias diffusion capacitance / MOS
  approach-to-threshold).
- **T2 transverse dielectric** — $\varepsilon_{eff}=\varepsilon_0\,S(V/V_{yield})$, ROLLS OFF to zero
  at $V_{yield}=\sqrt\alpha\,V_{snap}\approx43.65$ kV. Reading: **reverse-biased depletion varactor**
  (polarization runs out).
- The pair $(V_{snap}:V_{yield})$ maps to a MOSFET's $(V_{th}:V_{BD,ox})$ — two critical voltages,
  different physics, in one device. $V_{yield}/V_{snap}=\sqrt\alpha$ EXACTLY (driver-confirmed).

---

## (a) OPERATIONAL DEFINITIONS — pin each capacitance BY THE MEASUREMENT

Device physics never pins a nonlinear capacitance by a formula alone — it pins it by the *measurement*:
the large-signal **chord/secant** $C=Q/V$ vs the small-signal **tangent** $C_{ss}=dQ/dV$ at the held
bias. The C-V *definition* crowns the **tangent** as "the small-signal capacitance." Both sectors carry
the pair; we state both and crown the tangent, keeping the chord named as the large-signal secant.

### A1 longitudinal bond compliance (keyed $V_{snap}$)

Constitutive charge on the A1 bond $Q_{A1}(V)=C_0\,V/S(V/V_{snap})$. Then, per
`device-circuit-models.md`:60 (verbatim, A1-scoped, $A\equiv V/V_{snap}$: *"the large-signal
chord/secant varactor $C_{\mathrm{eff}}=C_0/S$ vs the small-signal differential
$C_{\mathrm{ss}}=\mathrm{d}Q/\mathrm{d}V=C_0/S^3$"*):

| Object | Formula | Small-field expansion | Role |
|---|---|---|---|
| **A1 large-signal chord** (secant) | $C_{chord}/C_0 = 1/S(V/V_{snap})$ | $1+\tfrac12(V/V_{snap})^2$ | the constitutive compliance $Q/V$ |
| **A1 small-signal tangent** (crowned) | $C_{ss}/C_0 = dQ/dV = 1/S^3(V/V_{snap})$ | $1+\tfrac32(V/V_{snap})^2$ | **THE small-signal compliance** ($dQ/dV$) |

Driver spot-check (live-fire, from constants): at the electron's A1 bias $A=\sqrt\alpha$ (i.e.
$V=V_{yield}$ on the A1 axis) the tangent is $C_{ss}/C_0=1.01105$, matching `device-circuit-models.md`:60's
stated $\approx1.011$. Both DIVERGE as $V\to V_{snap}$ (the tangent faster, via $1/S^3$).

### T2 transverse permittivity (keyed $V_{yield}$)

Constitutive displacement $D(V)\sim\varepsilon_0 S(V/V_{yield})\,V$. Per the round-3 KEEP-BOTH
(`research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`:292-299):

| Object | Formula | Small-field expansion | Role |
|---|---|---|---|
| **T2 large-signal chord** (secant) | $\varepsilon_{chord}/\varepsilon_0 = S(V/V_{yield})$ | $1-\tfrac12(V/V_{yield})^2$ | constitutive permittivity $\varepsilon_0 S$ |
| **T2 small-signal tangent** (crowned) | $\varepsilon_{ss}/\varepsilon_0 = dD/dV = S - A_V^2/S$ | $1-\tfrac32(V/V_{yield})^2$ | **THE small-signal permittivity** ($dD/dV$) |

Both ROLL DOWN under held bias. The T2 tangent $S-A_V^2/S$ loses real support past $A_V=1/\sqrt2$
(where $S^2=A_V^2$) — this is not a bug: it is exactly the birefringence Letter's parallel eigenindex
$n_\parallel$ going imaginary at $A^2>1/2$ (see (c)). Both coefficients ($\tfrac12$ chord, $\tfrac32$
tangent) are sympy-traced and test-pinned; neither is crowned as "the answer to the corpus convention
tangle" — that stays a Grant call (`node-up`:229; see the merged flag in (h)).

**Anti-cross-wire (the discipline this arc enforces):** the A1 divergent form $C_0/S$ is keyed on
$V_{snap}$; the T2 rolloff form $\varepsilon_0 S$ is keyed on $V_{yield}$. Never $C_0/S$ keyed on
$V_{yield}$ (that is the node-up cross-wire, (h)) and never $\varepsilon_0 S$ keyed on $V_{snap}$.

---

## (b) THE VACUUM C-V DATASHEET CURVE

Analytic, from `ave.core.constants` (no hardcoding), both branches on one log-V figure. House style:
WHITE via `ave.viz.style.apply("print")`, Okabe-Ito, honest axes+units, legend outside data, no
on-figure title, `strict=True` (a baked title would raise). Vol-9-datasheet register.

**Pinned curve values (driver JSON; test-locked):**

| Bias point | Quantity | Value |
|---|---|---|
| $0.5\,V_{yield}$ | T2 chord $\varepsilon/\varepsilon_0$ | $0.86603$ ($=\sqrt3/2$) |
| $0.5\,V_{yield}$ | T2 tangent $\varepsilon_{ss}/\varepsilon_0$ | $0.57735$ ($=1/\sqrt3$) |
| $V_{yield}$ | T2 chord $\varepsilon/\varepsilon_0$ | $0.0$ (rolloff complete) |
| $0.5\,V_{snap}$ | A1 chord $C/C_0$ | $1.15470$ ($=2/\sqrt3$) |
| $0.5\,V_{snap}$ | A1 tangent $C_{ss}/C_0$ | $1.53960$ ($=(2/\sqrt3)^3$) |
| $V_{yield}$ (A1 axis, $A=\sqrt\alpha$) | A1 tangent $C_{ss}/C_0$ | $1.01105$ (corpus $\approx1.011$) |
| $0.99\,V_{snap}$ | A1 chord / tangent $C/C_0$ | $7.089$ / $356.2$ (diverging) |
| — | $V_{yield}$ / $V_{snap}$ | $43.65$ kV / $511.0$ kV |
| — | $V_{yield}/V_{snap}$ | $0.0854245 = \sqrt\alpha$ exactly |

The two device features are separated by $1/\sqrt\alpha\approx11.7$ in voltage. The figure shows the T2
chord (vermillion) rolling to zero at $V_{yield}$ and the A1 chord (solid blue) + tangent (dashed blue)
diverging toward $V_{snap}$.

---

## (c) THE ⊥/∥ EIGENMODE CHECK (R2 confirmation) — VERDICT: **YES, corpus-resolved**

**Question (orchestrator candidate resolution of the chord-vs-tangent fork):** a weak probe polarized
PARALLEL to a held bias samples the tangent $\partial D/\partial E$; PERPENDICULAR samples the chord
$\varepsilon(A_0)$; their difference IS the birefringence. Verified against the Letter's actual $\Delta n$
derivation (`papers/2026_birefringence_letter/main.tex`, Appendix A).

**Derivation summary (sympy, `eigenmode_check()`; the Letter's Appendix A is the same algebra):**

The Letter's kernel `eq:kernel` is $\varepsilon_{eff}(E)=\varepsilon_0\,S(E)$, $S=\sqrt{1-(E/E_c)^2}$ —
the **same** kernel as the T2 permittivity, with $E_c=\sqrt\alpha\,E_{crit}=E_{yield}=1.130\times10^{17}$
V/m (the field image of $V_{yield}$; driver-confirmed $E_c\equiv E_{YIELD}$). The probe permittivity
tensor is $\varepsilon_{ij}=\varepsilon_0 S\,\delta_{ij}+2\varepsilon_0 S'E_{0i}E_{0j}$ (Letter
Eq. app-tensor). Its two eigenvalues, and their probe indices:

- **transverse (twofold) eigenvalue** $\varepsilon_0 S$ → $n_\perp=\sqrt{S}=(1-A^2)^{1/4}$
  (Letter Eq. app-nperp). This is the **CHORD / constitutive** value $\varepsilon_0 S$ evaluated at the
  pump — the PERPENDICULAR polarization samples the T2 **chord**.
- **longitudinal eigenvalue** $\varepsilon_0(S+2S'E^2)=\varepsilon_0(S-A^2/S)$ →
  $n_\parallel=\sqrt{S-A^2/S}=\sqrt{(1-2A^2)/\sqrt{1-A^2}}$ (Letter Eq. app-npar). This is the
  **TANGENT** $dD/dE=\partial_E(\varepsilon_0 S\,E)$ along the field — the PARALLEL polarization samples
  the T2 **tangent**.

sympy MATCH (both `True`): $n_\perp-(1-A^2)^{1/4}=0$ and $n_\parallel-\sqrt{(1-2A^2)/\sqrt{1-A^2}}=0$.
Their difference is the polarimeter observable:
$$\delta n_{bir}=n_\parallel-n_\perp\;\to\;-\tfrac12 A^2 \quad\text{(driver: } -E^2/(2E_c^2)\text{)},\qquad
\delta n_{iso}=n_\perp-1\;\to\;-\tfrac14 A^2.$$

> **[Resultbox — VERDICT] The KEEP-BOTH chord/tangent fork is CORPUS-RESOLVED as the two polarization
> eigenmodes.** The T2 **chord** $\sqrt S$ IS the perpendicular index $n_\perp$; the T2 **tangent**
> $\sqrt{S-A^2/S}$ IS the parallel index $n_\parallel$. BOTH are real, physical probe eigenmodes — the
> "which one is *the* small-signal C" question dissolves at the tensor level: they are two *different
> polarization channels of the same tensor*, and **their split IS the observable** ($\delta n_{bir}=
> -\tfrac12 A^2$, the Letter's registered birefringence). Perpendicular reads the chord; parallel reads
> the tangent; the birefringence is the difference. (The T2 tangent's loss of real support past
> $A_V=1/\sqrt2$ is exactly $n_\parallel$ going imaginary at $A^2>1/2$ — the same physics, consistently.)

**Scope + discrimination (`ave-discrimination-check`):** this identification is NOT itself AVE-distinct
— that a uniaxial saturable dielectric has a chord (⊥) and a tangent (∥) eigenmode is the generic
structure of any nonlinear-optics birefringence (Born–Infeld has it too). What is AVE-distinct is
already-canon and unchanged: (i) the specific elliptic ($p=2$, energy-norm) kernel, and (ii) the exact
static-$\mathbf B$ transparency. This arc's contribution is *organizational*: it shows the corpus's
chord/tangent KEEP-BOTH and the Letter's ⊥/∥ eigenmodes are the SAME two objects, so the fork was never
a contradiction — it was two polarization channels. **STAGED ruling text below (h §ruling); not landed.**

---

## (d) NETWORK COMPOSITION — the biased loaded-line

The two-branch cell composes across the canonical srs/K4 ladder: **series-$L$ per bond, shunt-$C$ per
node** (`graded-network-response.md`:50, $z=3$ mutual inductive struts; K4 $z=3$), a periodic chain of
identical cells with the Bloch/Floquet condition on the cell ABCD ($\cos(q\ell_{eff})=(A+D)/2$,
`z0-derivation.md`:133-136). The cold dispersion is the sine law $\omega(q)=(2c_0/\ell_{node})
|\sin(q\ell_{node}/2)|$.

- **Where each capacitance lives.** The **T2 permittivity** is the **shunt-$C$ per node** (the LCR-cell
  capacitance $C_{diel}=\varepsilon_{eff}A/d\propto S$, `CLAUDE.md`:73) — it loads the ladder's shunt
  admittance. The **A1 bond compliance** is a **longitudinal (bond-level) reactance** — the $1/k_a$
  stretch-compliance of the series bond, orthogonal to the shunt path ($A1\perp T2$). So a **NETWORK
  C-V sweep on the shunt admittance reads the T2 branch**; the A1 branch lives on the series-bond DOF
  and is read by a longitudinal (bulk-channel) probe, not the shunt LCR.
- **Loaded-line C-V.** A held T2 bias loads the shunt-$C$ through the small-signal (tangent)
  permittivity, pulling the band edge by $1/\sqrt{\varepsilon_{ss}/\varepsilon_0}$. Driver band-edge
  pull ($q\ell=\pi$): cold $=1.0$, $0.5\,V_{yield}\to1.316$, $0.7\,V_{yield}\to5.976$ (the tangent
  shrinking as the bias approaches the rolloff).
- **Uniform vs gradient bias (the round-3 gauge rider, honored).** A spatially-**uniform** bias parks a
  real local deficit that **self-cancels on readout** (gauge-relative $A$, INVARIANT-S2; a co-located
  wave-made ruler rides the same offset). So a network-level C-V must be a **DIFFERENTIAL / gradient**
  measurement: the readable observable is $\Gamma\ne0$ at an $\varepsilon$-gradient boundary via the
  **Op14 Meissner-asymmetric impedance mirror** $Z_{eff}=Z_0\sqrt{S_\mu/S_\varepsilon}$
  (`CLAUDE.md`:75 / `operators.md`:54). *This is the network analog of "a MOS C-V is meaningless without
  a reference terminal" — the vacuum needs a gradient, not an absolute bias.*

---

## (e) SPLIT C-V — separating T2 polarization from A1 compliance by terminal selection

The device technique **split C-V** separates channel charge from bulk charge by terminal selection:
gate-to-channel capacitance $C_{gc}$ (gate + source/drain tied) reads the **inversion/channel** charge;
gate-to-body $C_{gb}$ (gate + body) reads the **depletion/bulk** charge. Two terminal pairs, two charge
populations, one device.

**Vacuum-cell map — the anti-cross-wire MEASUREMENT discipline.** The two "terminal pairs" an engine
measurement would use, keyed by which channel the probe couples to (the three-channel boundary port,
`device-circuit-models.md`:91-105):

| Split-C-V terminal pair (device) | Vacuum "terminal pair" (engine) | Reads | Sector |
|---|---|---|---|
| gate ↔ channel ($C_{gc}$, inversion) | **transverse-EM port ↔ shunt node** ($Z_{EM}=Z_0$, the $\varepsilon$ shunt admittance) | T2 permittivity rolloff (small-signal $\varepsilon_{ss}$, keyed $V_{yield}$) | **T2** |
| gate ↔ body ($C_{gb}$, depletion/bulk) | **longitudinal-bulk port ↔ series bond** ($Z_{bulk}$, the A1 stretch-compliance DOF) | A1 bond-compliance divergence (small-signal $C_{ss}=C_0/S^3$, keyed $V_{snap}$) | **A1** |

Concretely, an engine split-C-V would: (1) hold a gradient bias; (2) drive a weak **transverse-polarized**
probe on the EM channel and read $\partial D/\partial E$ (the T2 tangent $\varepsilon_{ss}$) via the
$S_{11}$-at-$Z_0$ shunt admittance; (3) *separately* drive a weak **longitudinal (bulk-channel)** probe
and read the A1 series-bond compliance via $Z_{bulk}$. Because $Z_{EM}$ (transverse, $\Omega$) and
$Z_{bulk}$ (longitudinal, mechanical $\rho c$) live in **different impedance domains**
(`device-circuit-models.md`:143), the two terminal pairs cannot cross-couple — **that domain separation
IS the anti-cross-wire guarantee**: a transverse-EM readout can NEVER pick up the A1 compliance, and a
longitudinal-bulk readout can NEVER pick up the T2 permittivity. Split C-V is thus the engine's
built-in defense against the genesis-24 double-count.

---

## (f) FREQUENCY DISPERSION — the properly-posed question (POSED, not forced)

In a MOS capacitor the **inversion branch** of the C-V curve is frequency-dependent: at low frequency
minority carriers can be generated/recombined fast enough to follow the small-signal swing (high-$C$
inversion branch); at high frequency they cannot, and $C$ stays at the depletion floor. The crossover
is set by the ratio of the drive rate to the minority-carrier **generation rate**.

**The map to the A1 turn-on branch, posed precisely:**

> **[Posed question — deliverable (f), NOT answered here]** *Near $V_{snap}$, does the A1 branch's
> small-signal response depend on the drive rate $\omega$ relative to the pair-generation rate — so that
> a SLOW probe sees the diverging turn-on (inversion-like, carriers/pairs follow) while a FAST probe sees
> only the sub-threshold compliance (depletion-like, pairs cannot follow)? Equivalently: is there an
> $\omega_{gen}(V)$ — a bias-dependent pair-generation rate — below which $C_{ss}^{A1}(\omega)\to C_0/S^3$
> (the full slow-drive turn-on) and above which $C_{ss}^{A1}(\omega)\to$ the frozen sub-threshold value?*

**Connection to the OPEN slow-drive band (round-2 prereg).** The round-2 prereg
(`2026-07-05_em-keying-round2-worked-cell_prereg_FROZEN.md`:75-78) already carries an **unconstrained
slow-drive crossover** as a *declared open scale* (verbatim: *"an unconstrained crossover is a declared
open scale, not a free parameter to hide"*), with the $\mathbf B$-sector rate suppression
$\mathcal{W}_{beat}=(\omega/\omega_C)^2\mathcal{W}_{var}$ (`:119-121`). The A1 frequency-dispersion
question is the **$\varepsilon$/A1-side twin** of that same slow-drive band: the pair-generation rate
$\omega_{gen}$ is the A1-turn-on analog of the round-2 $\mathbf B$-side circulation rate.

**What computation would decide it (NOT run here):** a **reactance-pair time-domain** run near $V_{snap}$
recording BOTH the C-state ($V_{inc}$/$\omega$) AND the L-state ($\Phi_{link}$/$\dot\omega$) at every
step over the recording window (per the empirical-driver reactance-pair discipline), swept in
drive-rate $\omega$ from adiabatic ($\omega\ll\omega_{gen}$) to sudden ($\omega\gg\omega_{gen}$), to see
whether $C_{ss}^{A1}(\omega)$ exhibits a MOS-inversion-like dispersion step and at what $\omega_{gen}(V)$.
**We do NOT claim an answer** — a snapshot at one phase is consistent with both a static turn-on and an
oscillator caught at peak; only the reactance-pair sweep distinguishes them. This is posed for a future
driver, tied to the round-2 open slow-drive band. **No derivation, no answer asserted.**

---

## (g) TECHNIQUE-TRANSFER TABLE

Each device technique tagged TRANSFERS / TRANSFERS-WITH-CAVEAT / DOES-NOT-TRANSFER, with the Ax3 reason
and the deliverable that uses it.

| Technique | Transfer | Ax3 reason | Deliverable |
|---|---|---|---|
| **C-V profiling** (chord vs $dQ/dV$ tangent; feature at a critical voltage) | **TRANSFERS** | Pure reactive small-signal on a lossless saturating capacitor; no carriers needed below threshold. The vacuum C-V IS the Ax4 kernel read as $C(V)$. | (a),(b) |
| **Split C-V** (terminal-pair selection separates two charge populations) | **TRANSFERS** | Reactive; the two "terminals" are the transverse-EM shunt vs longitudinal-bulk series ports — different impedance domains, guaranteed non-cross-coupling. No carrier statistics. | (e) |
| **C-V frequency dispersion** (inversion branch follows/doesn't follow the drive) | **TRANSFERS-WITH-CAVEAT** | The *mechanism* (carriers follow a slow drive, not a fast one) transfers ONLY at/above threshold where pairs are real; the *question* is posable below threshold but its answer is the OPEN slow-drive band. Ax3-lossless holds below threshold, so any true dispersion step implies a rate-limited (non-instantaneous) process = a generation channel, which is a threshold-sector phenomenon. | (f) |
| **Charge-control ($Q/\tau$)** (stored charge / transit or recombination time) | **DOES-NOT-TRANSFER (below threshold)** | $\tau$ here is a recombination/transit **rate** — dissipative, carrier-statistics-based. Ax3-LOSSLESS forbids a real-power loss channel below threshold; there is no stored *carrier* charge to control, only reactive displacement. Transfers only at/above threshold (real pairs). *(N.B. the substrate's own $\tau_{relax}=\ell_{node}/c$ is a lossless remanence timescale, NOT a recombination rate — do not conflate.)* | — (excluded) |
| **Gummel / threshold-voltage extraction** ($I$-$V$ knee, transconductance) | **DOES-NOT-TRANSFER (below threshold); the threshold ITSELF transfers** | A Gummel plot needs a real **current** ($I$-$V$), i.e. dissipative carrier transport — Ax3-forbidden below threshold. But the *concept* of a threshold voltage maps exactly: $V_{snap}$ IS the vacuum's turn-on threshold (pair-injection). So threshold-*extraction-by-current* does-not-transfer; the *threshold voltage* is canonical ($V_{snap}$). | (a) [threshold identity only] |
| **GaN polarization-induced 2DEG** (dopant-free channel from spontaneous/piezo polarization) | **TRANSFERS-WITH-CAVEAT (closest sibling)** | This is the closest device analog: the 2DEG forms from a *polarization discontinuity* with NO doping — carriers appear from a built-in field gradient, not from dopants. The vacuum analog is a **gradient-bias** ($\nabla A\ne0$) producing a readable $\Gamma\ne0$ at the $\varepsilon$-boundary (the Op14 mirror) — a dopant-free, gradient-sourced channel. CAVEAT: the 2DEG carriers are real (above-threshold); below threshold the vacuum has only the reactive gradient (readable but carrier-free). The *dopant-free, gradient-sourced* mechanism transfers in FORM; real carriers need threshold. | (d),(e) |
| **Avalanche / snapback** (breakdown $I$-$V$ negative resistance) | **DOES-NOT-TRANSFER as $I$-$V$; the threshold transfers** | Avalanche is impact-ionization — a carrier-multiplication **rate**, dissipative, above-threshold only. Below threshold Ax3-lossless forbids it. The *breakdown voltage* concept maps to $V_{yield}$ (T2 rupture wall) / $V_{snap}$ (A1 completion); the negative-resistance $I$-$V$ does not. | (a) [threshold identity only] |

**Pattern:** every technique whose physics is a *rate* on *real carriers* (charge-control $\tau$, Gummel
$I$-$V$, avalanche, C-V frequency dispersion's answer) DOES-NOT-TRANSFER below threshold by Ax3-lossless;
every technique that is a *reactive small-signal on a saturating capacitor* (C-V profiling, split C-V) or
a *gradient-sourced field structure* (GaN 2DEG in FORM) TRANSFERS. The *threshold voltages themselves*
($V_{snap}$, $V_{yield}$) are canonical in all cases — the vacuum HAS the turn-on knees; what it lacks
below threshold is the dissipative carrier machinery to read them by current.

---

## (h) STAGED — the R1 node-up supersession text (for Grant; NOT landed — no KB edit in this arc)

The node-up leaf `node-up-small-large-signal.md` (branch tip `cb38c9b9`) writes the **A1 divergent
form** $C_0/S$ but keys it on the **T2 key** $V_{yield}$ — the exact cross-wire this arc exists to
repair. Two sites, re-grepped verbatim two ways (grep + Read):

- **`node-up`:105** (brief cited :104 — a revision offset; content identical) verbatim:
  *"$C_{eff}(V) = \frac{C_0}{S(A_V)}, \quad A_V = \frac{V}{V_{yield}}$ … $\varepsilon$-grade: VARACTOR,
  keyed on VOLTAGE"*.
- **`node-up`:370** (brief cited :360) verbatim: *"$C_{eff}=C_0/S(A_V)$, varactor keyed on $V$ \|
  **DERIVED** \| Axiom 4 dielectric specialization (`CLAUDE.md`:73)"*.

The cross-wire: $C_0/S$ (the *diverging* form) is **A1's** form (the bond compliance that diverges at
$V_{snap}$, `nonlinear-vacuum-capacitance.md`:16); $A_V=V/V_{yield}$ is **T2's** key. So `node-up`:105
labels an A1-shaped divergence as the "$\varepsilon$-grade" (T2) and keys it on $V_{yield}$ — T2's key on
A1's form. Per `CLAUDE.md`:73 the T2 permittivity ROLLS OFF ($\varepsilon_0 S$, ↓), it does not diverge;
the diverging $C_0/S$ (↑) is A1. Per `def-vyvsn1` (`nonlinear-vacuum-capacitance.md`:18) $V_{yield}$ is
the T2 self-trap wall and $V_{snap}$ is the A1 compliance bound.

> **⚑ FLAG (surfaced for Grant, NOT resolved here) — this composes into the `node-up`:229 three-way
> varactor-convention tangle.** This supersession is a **corpus-consistency call**, not an engine bug
> (per A44 missing-axiom-vs-engine-bug and the lane discipline): `node-up`:229 already carries the (a)/
> (b)/(c) three-way tension around $C_0/S(A_V)$ and what "small-signal C" means. The staged text below
> corrects the **sector-keying** cross-wire specifically; the "which object is *the* small-signal C"
> convention question stays the OPEN `node-up`:229 Grant item. The auditor lands the KB manual — this
> arc only stages the text.

### STAGED SUPERSESSION TEXT (verbatim, for Grant to adjudicate then the auditor to land)

> 🔴 **SECTOR-KEYING SUPERSESSION (2026-07-07, `analysis/semiconductor-cv-dip`; Rule-12 — body below
> preserved, git is the trail).** The `node-up`:105 keyed-argument resultbox and the `node-up`:370 ledger
> row label $C_{eff}(V)=C_0/S(A_V)$, $A_V=V/V_{yield}$ the "$\varepsilon$-grade varactor." This
> **cross-wires A1's form onto T2's key**: the diverging $C_0/S$ (↑) is the **longitudinal-A1 bond
> compliance** and is keyed on **$V_{snap}$** ($m_ec^2/e\approx511$ kV, where $C_{eff}\to\infty$;
> `nonlinear-vacuum-capacitance.md`:16, `CLAUDE.md`:73), NOT the "$\varepsilon$-grade." The
> **transverse-T2 permittivity** is $\varepsilon_{eff}=\varepsilon_0 S$ (↓, ROLLS OFF), keyed on
> **$V_{yield}$** ($\sqrt\alpha\,V_{snap}\approx43.65$ kV, the Cosserat self-trap wall; `def-vyvsn1`,
> `nonlinear-vacuum-capacitance.md`:18). **The corrected split (Grant-ratified sector split, `CLAUDE.md`:73):**
> - **A1 longitudinal bond compliance:** $C_{eff}=C_0/S(V/V_{snap})$, DIVERGES at $V_{snap}$; small-signal
>   tangent $C_{ss}=dQ/dV=C_0/S^3$ (`device-circuit-models.md`:60). *Operational (this arc, deliverable a):*
>   the small-signal compliance is the **tangent** $C_0/S^3$ (crowned); the **chord** $C_0/S$ is the
>   large-signal secant. Device reading: turn-on / channel-inversion capacitance.
> - **T2 transverse permittivity:** $\varepsilon_{eff}=\varepsilon_0 S(V/V_{yield})$, ROLLS OFF at
>   $V_{yield}$; small-signal tangent $\varepsilon_{ss}=dD/dV=\varepsilon_0(S-A_V^2/S)$ (round-3 RESULT).
>   *Operational (deliverable a):* chord $\varepsilon_0 S$ (leading $1-\tfrac12 A_V^2$) = the perpendicular
>   probe eigenmode $n_\perp=\sqrt S$; tangent $\varepsilon_0(S-A_V^2/S)$ (leading $1-\tfrac32 A_V^2$) = the
>   parallel eigenmode $n_\parallel$ — the **chord/tangent split IS the birefringence** $\delta n_{bir}=
>   -\tfrac12 A_V^2$ (corpus-resolved, `analysis/semiconductor-cv-dip` (c); Letter Appendix A).
> The `node-up`:229 three-way "which is *the* small-signal C" convention question is UNCHANGED by this
> correction and stays OPEN for Grant; this note fixes only the **sector-keying** (A1 form ↔ T2 key)
> cross-wire. Provenance: `research/2026-07-07_semiconductor-cv-dip_RESULT.md` (a)/(c)/(h).

---

## VERIFY / DISCIPLINE LEDGER

- **Every number from canonical constants** (`ave.core.constants`): $V_{SNAP}$, $V_{YIELD}$, $ALPHA$;
  $V_{yield}/V_{snap}=\sqrt\alpha$ exactly (driver + test). $E_c=\sqrt\alpha E_{crit}=E_{YIELD}=1.130
  \times10^{17}$ V/m (driver-confirmed). No hardcoding (prereg F2 clean).
- **ERRATUM (frozen-prereg citation offset, surfaced not silently fixed):** the FROZEN prereg cites
  `nonlinear-vacuum-capacitance.md`:18 for the A1 $C_{eff}\to\infty$-at-$V_{snap}$ line and :20 for the
  `def-vyvsn1` T2-keying ruling. On re-grep at branch tip the A1 divergence line is at **:16** and the
  `def-vyvsn1` ruling at **:18** (the verbatim CONTENT is correct at both; only the line numbers were
  off by a leaf-context offset). The prereg is left frozen (freeze integrity); this RESULT uses the
  corrected :16 / :18. No content claim changes.
- **Every canon quote verbatim, two methods** (grep + Read at branch tip `cb38c9b9`): `CLAUDE.md`:73,
  `nonlinear-vacuum-capacitance.md`:16,:18, `node-up`:105,:229,:370, `device-circuit-models.md`:60,
  round-3 RESULT:292-299, Letter Appendix A, `graded-network-response.md`:50,:53, `z0-derivation.md`:133-136,
  round-2 prereg:75-78,:119-121. **verify-before-cite FLAG:** `node-up` line drift :105/:370 (this rev) vs
  brief :104/:360 — revision offset, content identical; both cited.
- **Gates prove can-fire:** the eigenmode-check tests assert the sympy identity holds AND (implicitly) the
  form would fail if $n_\parallel\ne\sqrt{S-A^2/S}$ (prereg F1 kill wired). The anti-cross-wire tests would
  RED if A1 were keyed $V_{yield}$ or T2 keyed $V_{snap}$ (prereg F3 kill wired).
- **Consistency-vs-emergence:** CONSISTENCY-class throughout (prereg §4 held); $\sqrt\alpha$ ratio = echo;
  no emergence headline (F4 clean). The eigenmode identification is NOT AVE-distinct (generic
  nonlinear-optics eigenmode structure); the static-$\mathbf B$ transparency it touches is already-canon.
- **Homonym discipline:** five "$A^2$" senses named distinctly (Ax4 arg / Letter $(E/E_c)^2$ / bond strain
  / T2 $A_V=V/V_{yield}$ / A1 $A=V/V_{snap}$); A1 keyed $V_{snap}$, T2 keyed $V_{yield}$, never cross-wired.
- **flag-don't-fix:** the node-up cross-wire is surfaced with both file paths + verbatim content; the
  correction is STAGED (h §ruling), NOT written to the KB. The `node-up`:229 convention tangle is composed
  into, not resolved.
- **Lane discipline:** implementer lane; the auditor lands the KB manual entry; the sector-keying
  supersession is a corpus-consistency call for Grant (A44), not an Ax-5 draft or an engine-bug fix.
