# Vacuum-Birefringence Coefficient — the Bankable AVE-Distinct Falsifier (facility proposal)

**Date:** 2026-06-21
**Status:** PROPOSAL (facility-grade). Coefficient result LOCKED + validate-on-known PASS. OQ-1 (field→cavity-phase coupling) now **PARTIALLY CLOSED** (adversarial-verify verdict `partially-closed`): the coupling is **DERIVED** from the Axiom-4 kernel and the geometry factor *g* is **PINNED per apparatus config** — see the derivation [`research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md). Named residuals carried (R-1 differential-vs-leaf observable, R-2 single-invariant modeling choice, R-3 detector-floor validate-on-known owed); §5, §8 below superseded with the pinned per-config numbers (Rule-12).
**Canonical claim:** `clm-pp3qwf` (Vol-4 Ch.12 `vacuum-birefringence-e4.md`; solidity 0.8) — this doc is its **strengthen-by**.
**Drivers:** `src/scripts/vol_9_device/vacuum_birefringence_facility_sweep.py` (this branch); `AVE-Bench-Birefringence/scripts/birefringence_coefficient_bench.py` (R1–R8); shared `ave.bench.{sweep,apparatus,snr,validate}` + `ave.bench.birefringence`.
**Worktree provenance:** `/tmp/biref-harden`, branch `analysis/birefringence-hardening`, on `origin/main` 5f91d1af; sweep commit ec9b9830.

> **Bench-repo mirror (open item).** The canonical long-term home for this proposal is
> `AVE-Bench-Birefringence/docs/design/`. It lands here in the AVE-Core `research/`
> tree because the reviewed PR for this work targets AVE-Core `main`; copying it into
> the sibling bench repo's `main` is a separate, separately-reviewed commit (cross-repo
> promotion is a different session per workspace discipline). See OPEN ITEMS.

---

## 0. Bottom line (one paragraph)

**Yes — this is a peer-or-better, fully-specified, AVE-distinct bankable falsifier, with one
remaining gate.** AVE predicts a vacuum-birefringence index-shift coefficient $4.14\times10^6$
(at $a_{EH}=7/45$; physical band $[4.14,\,9.65]\times10^6$) above QED's Euler-Heisenberg value —
**field-independent** (both responses are $E^2$-leading; the discriminator is the coefficient, not
the exponent), resting on the **exact** substrate identity $(E_{crit}/E_{yield})^2=1/\alpha$ and
validate-on-known PASS (PVLAS $A_e$ recovered to 0.35%). The instrument is the ratified linear-pump
→ polarimeter (PVLAS/BMV lineage): the scalar-$|E|$ kernel under a linearly-polarized pump yields a
uniaxial probe-response tensor $\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$ → birefringence →
ellipticity readout. A facility sweep (1728 points) finds an 841-point divergence window enclosing
the $g\sim10^{-3}$ worst-case, with AVE 5σ-detectable in $<1\,\mu$s at PW-class fields and a modest
finesse, while QED sits a factor $4.14\times10^6$ below throughout (a $\sim10^{13}\times$
integration-time gap — an unambiguous AVE-sized-vs-QED-sized call). The **chord** (the bankable
content) is the *structural* tree-$O(1)/4$-saturation-vs-$\alpha^2$-loop FORM, present at every field;
the *magnitude* $4.14\times10^6$ is honestly an **α-echo** at the value level (symmetric standard:
QED's coefficient is equally α-rooted).

> 🔴 **SUPERSEDED (Rule-12, 2026-06-21 OQ-1 close).** The first-cut text read: *"The single remaining
> gate is OQ-1: the field → cavity-phase coupling $g$ is here derived only to leading order … and
> asserted as a Gaussian-beam overlap parameter rather than derived as an Axiom-4 coupling."* That
> first-cut leading-order/asserted framing is now superseded — see the replacement immediately below.
> Body preserved for audit-trail continuity.

**OQ-1 is now PARTIALLY CLOSED (verify verdict `partially-closed`).** The field → cavity-phase coupling
is **DERIVED** through the chain focal-E → uniaxial probe tensor $\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$
(the exact differential of the scalar Axiom-4 kernel) → cavity round-trip birefringent phase →
ellipticity, and the geometry factor $g$ is **PINNED per apparatus config** as an explicit
Gaussian-focus ($g_{spatial}=(2z_R/L)\arctan(L/2z_R)$, exact Lorentzian integral) × cavity-timing
($g_{temporal}$, pump-gated coherent-pass count) overlap (derivation:
[`2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)).
Three **named residuals** remain (verdict honesty — do **not** over-state "closed"): **R-1** the
DERIVED par−perp *differential* ($-\tfrac12 A^2$) is a NEW observable, not the canonical leaf's scalar
single-arm ($-\tfrac14 A^2$, `clm-pp3qwf` :12,:14) — whether to promote it is an auditor/Grant call;
**R-2** $u=|E|^2$ as THE invariant is an AVE modeling choice vs QED's two invariants ($E^2-B^2$,
$E\cdot B$, which split 7/45 vs 4/45); **R-3** the polarimetry/detector floor is still owed a
validate-on-known against a published cavity. **The coefficient depends on none of R-1/R-2/R-3.**
**Do not headline "$10^4\times$ QED at $g\sim10^{-3}$": $g$ cancels in the ratio (always
$4.14\times10^6$, or $1.93\times10^7$ at the matched differential observable, FLAG-A §6/§10); $g$
sets only the absolute realized signal-vs-floor margin.**

---

## 1. The prediction — what AVE says and where the chord lives

AVE's vacuum is a chiral LC string network whose permittivity saturates under the
Axiom-4 universal kernel $S = \sqrt{1-(E/E_{yield})^2}$. The refractive index follows
the wave-speed identity $n = \sqrt{\varepsilon_{eff}/\varepsilon_0} = \sqrt{S}$ (only
$\varepsilon$ strained, $\mu = \mu_0$), so the AVE index shift is

$$\delta n_{AVE} = \sqrt{S}-1 = (1-(E/E_{yield})^2)^{1/4}-1 \;\approx\; -\tfrac14\left(\tfrac{E}{E_{yield}}\right)^2 - \tfrac{3}{32}\left(\tfrac{E}{E_{yield}}\right)^4 + \cdots$$

negative (the vacuum softens), and **$E^2$-leading** — the *same leading power* as QED's
Euler-Heisenberg $\delta n_{QED} = a_{EH}\,\alpha^2 (E/E_{crit})^2$.

**The discriminator is the COEFFICIENT, not the exponent** (the historical "$E^4$ falsifies
AVE" framing was a $\sqrt\varepsilon$ conflation — retracted Rule-12, `vacuum-birefringence-e4.md:20`,
and the vol4-ch11 LaTeX re-scope box at `11_experimental_falsification.tex:58-64`). The
field-independent ratio collapses on the **substrate identity** $(E_{crit}/E_{yield})^2 = 1/\alpha$
(exact by construction: $E_{YIELD}=\sqrt\alpha\,E_{CRIT}$, `constants.py:438` vs `:432`;
`substrate_identity_holds()` → `True`, reproduced this branch = 137.0360):

$$\boxed{\;\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1}{4\,a_{EH}\,\alpha^2}\left(\frac{E_{crit}}{E_{yield}}\right)^2 = \frac{1}{4\,a_{EH}\,\alpha^3} = 4.1358\times10^{6}\;\;(a_{EH}=7/45)\;}$$

reproduced from live `ave.core.constants`: `1/(4·(7/45)·α³) = 4135790.14`.

**Chord-vs-echo split (the load-bearing honesty).**
- **CHORD (the AVE-distinct FORM):** the index shift is **tree-level $O(1)/4$ saturation**
  of a real medium, present at *every* field, un-suppressed against the *yield* field
  $E_{yield}\approx1.13\times10^{17}$ V/m. QED's same-power response is a **one-loop**
  effect suppressed by $\alpha^2$ against the *Schwinger* field $E_{crit}\approx1.32\times10^{18}$
  V/m. Tree-saturable-medium vs loop-polarizable-vacuum is the structural distinction —
  it is what produces a field-*independent* ~6-OOM coefficient gap. This is the bankable
  content.
- **ECHO (the magnitude, honestly tagged):** the *number* $4.14\times10^6$ is rooted in
  $\alpha^{-3}$ (via the substrate identity). It rides the α-echo family at the value level
  — AVE does not *derive* α, so the precise prefactor is a calibration echo, not an emergent
  number (`consistency-vs-emergence`: the ratio FORM is a MANIFESTATION of Axiom 4; the
  MAGNITUDE is value-echo). **Symmetric standard holds:** QED's own $a_{EH}\alpha^2$ is
  equally α-rooted and QED does not derive α either. The discriminator's force is therefore
  the **field-independence + ~6-OOM size of the gap**, not the third significant figure of
  the prefactor.

There is a strictly-cleaner companion channel — the parity-odd **optical-activity rotation**
($\theta\neq0$, sign-flips between lattice enantiomorphs, zero on the achiral control;
`birefringence.py:222-262`), against which QED is **identically zero**. That zero-vs-nonzero
channel is the strongest discriminator AVE owns here, but it is **not** the subject of this
proposal — this doc specs the retardance/ellipticity polarimeter for the COEFFICIENT channel.
The rotation-channel apparatus is a flagged follow-up (§10).

## 2. The instrument — linear-pump → polarimeter (ratified)

The retired DC-electrode / gap-voltage framing (inherited from the VacuumMirror EE bench)
does not apply to an optical-focus drive; the **ratified instrument is a linear-pump →
polarimeter** of the PVLAS/BMV lineage (rotating-magnet + Fabry-Perot ellipsometer,
achieved ~$10^{-10}$–$10^{-11}$ rad/$\sqrt{\text{Hz}}$ ellipticity sensitivity).

**Why a *linearly*-polarized pump still produces birefringence (the uniaxial-tensor reasoning).**
The AVE kernel keys off the scalar field magnitude $|E|$: $n=(1-A^2)^{1/4}$, $A=|E|/E_{yield}$.
For an isotropic / *circular* pump this gives a purely scalar phase — no preferred transverse
axis — so $\Delta\phi_\parallel - \Delta\phi_\perp = 0$ (the corpus zero-ellipticity statement;
see the `:146` reconciliation in §10 and the mirror leaf). But a **linearly-polarized** pump
breaks that transverse isotropy: the probe sees the *local anisotropy of the index response to
the pump's polarization direction* $\hat E_0$. Expanding the scalar kernel about the pump
operating point, the small-signal probe-response tensor is **uniaxial**:

$$\varepsilon_{ij}(\text{probe}) = \varepsilon\,\delta_{ij} + 2\varepsilon'\,E_{0i}E_{0j}, \qquad \varepsilon' = \tfrac{\partial \varepsilon}{\partial(E_0^2)}\Big|_{\text{pump}}$$

i.e. an **optic axis parallel to the pump polarization**. The probe phase velocity differs
between the parallel and perpendicular probe-polarization components by $\delta n \sim
O(\delta n_{iso})$ — this is birefringence proper, and a probe launched at $45^\circ$ to the
pump axis acquires an **ellipticity** $\psi$, which is the polarimeter's readout. This is
structurally identical to the QED Euler-Heisenberg birefringence the PVLAS/BMV ellipsometers
were built to measure — the AVE physics enters **only** through the index-shift coefficient.

**Coordinate discipline (`phase-space-coordinate-check`, PASS):** the corpus prediction here
is a real-space optical index/path observable, and the instrument measures real-space optical
path / ellipticity. The probe-response tensor $\varepsilon\delta+2\varepsilon'E_0E_0$ is a
real-space Cartesian tensor; there is **no** phase-space ($V_{inc}/V_{ref}$, Clifford-torus,
impedance-plane) claim being compared against a real-space measurement. No $\phi^2$-vs-Cartesian
mismatch. (This is in contrast with the optical-activity *rotation* channel, whose chirality
sign rides the phase-space writhe — out of scope here.)

## 3. The apparatus — fields, cavity, probe, noise (DERIVE-3)

**MODE / REGIME (`ave-regime-phase-state-check`):** EM-transverse mode, **LINEAR** regime
($A=E/E_{YIELD}\ll1$, deep sub-yield), reactive-lossless. The whole proposal lives where
$\delta n$ is well-defined; reaching the AVE knee $A=1$ needs $E=E_{YIELD}\Rightarrow
I\sim1.7\times10^{27}$ W/cm² (unreachable, far above any optical regime), so we never leave
the linear regime — and that is fine, because the discriminator is field-*independent*.

**(a) Apparatus.** Linearly-polarized PW/ELI-class pump focus; Fabry-Perot probe cavity at
$\lambda_{probe}=1064$ nm (Nd:YAG), finesse $F=10^2$–$10^5$, $L\sim$ cm, probe at $45^\circ$
to the pump. Ellipticity readout $\psi = \tfrac12\,(2\pi/\lambda)\,|g\cdot\delta n|\,L\cdot(2F/\pi)$,
structurally identical to `induced_ellipticity()` in the bench (`birefringence_coefficient_bench.py:172-187`):
single-pass phase $(2\pi/\lambda)|\delta n|L$, finesse build-up $\approx 2F/\pi$, $\psi\approx\delta\phi/2$.

**(b) Field reachability (W/cm² → E_peak).** Plane-wave peak $E=\sqrt{2I/(c\varepsilon_0)}$:

| Intensity $I$ [W/cm²] | $E_{peak}$ [V/m] | $A=E/E_{YIELD}$ | regime |
|---|---|---|---|
| $10^{20}$ | $2.74\times10^{13}$ | $2.4\times10^{-4}$ | deep-linear |
| $10^{22}$ (PW-class focus) | $2.74\times10^{14}$ | $2.4\times10^{-3}$ | deep-linear |
| $10^{23}$ (ELI flagship) | $8.68\times10^{14}$ | $7.7\times10^{-3}$ | deep-linear |
| $5\times10^{25}$ (ELI-extreme) | $1.94\times10^{16}$ | $0.17$ | linear (knee far off) |

**(c) Shot-noise floor + time-to-Nσ.** Probe photon energy $E_{ph}=\hbar\omega=1.867\times10^{-19}$ J
(1.165 eV at 1064 nm); flux $\Phi=P/(\hbar\omega)$ (`probe_photon_flux()`). Shot-limited
polarimetry sensitivity $S_\psi = 1/(2\sqrt\Phi)$:

| Probe power | $\Phi$ [/s] | $S_\psi$ [rad/$\sqrt{\text{Hz}}$] |
|---|---|---|
| 1 mW | $5.36\times10^{15}$ | $6.83\times10^{-9}$ |
| 1 W | $5.36\times10^{18}$ | $2.16\times10^{-10}$ |
| 10 W | $5.36\times10^{19}$ | $6.83\times10^{-11}$ |
| 100 W | $5.36\times10^{20}$ | $2.16\times10^{-11}$ |

A 1–10 W probe sits **at the PVLAS/BMV achieved floor** ($\sim10^{-10}$–$10^{-11}$ rad/$\sqrt{\text{Hz}}$).
Time-to-Nσ (`snr.time_to_n_sigma`, signal $\gg$ floor): $t_{N\sigma} = (N_\sigma/\psi)^2/\Phi$.

**(d) Empirical-driver finding (Rule-10).** The as-specified cm-path + high-$F$ + facility-field
combination drives AVE **far out of small-angle** — $\psi_{AVE}$ from tens of rad up to $\sim10^7$
rad, 2–7 OOM past the 0.1-rad linearization validity. **The fix IS the dominant systematic, the
geometry factor $g$** (§5): the honest interaction length is not the cm cavity but the pump
Rayleigh range; with the realistic $g$ the signal lands cleanly in-band. The bench's
`small_angle_valid` guard gates any reported $\psi$; the headline regime is **overlap-limited
modest-$F$**, not high-$F$.

**Validate-on-known (HALT gate, PASS).** $A_e = 2\alpha^2\hbar^3/(45\mu_0 m_e^4 c^5) = 1.3247\times10^{-24}$ T⁻²
vs PVLAS textbook $1.32\times10^{-24}$ T⁻² (rel-err 0.35%, = exact-CODATA vs rounded-textbook;
`birefringence.py:197`). $c\,B_{crit}=E_{CRIT}$ holds. If this anchor failed the model would be
wrong and the run HALTs — it passes.

## 4. The sensitivity — divergence window, SNR, time-to-Nσ (sweep)

The facility-scale sweep (`vacuum_birefringence_facility_sweep.py`, 1728 points over
$E\times F\times\lambda\times L\times g$) extracts the **divergence window**: where realized
$\psi_{AVE}$ BOTH clears the polarimetry floor AND exceeds its co-computed QED counterpart AND
stays inside small-angle. (`make verify` PASS; validate-on-known HALT-gate PASS.)

**Divergence window (841 / 1728 points in-window):**

| Axis | In-window range |
|---|---|
| $E$ | $[7.6\times10^{9},\,3.0\times10^{16}]$ V/m ($A=[6.7\times10^{-8},\,0.27]$, deep-linear) |
| finesse | $[10^2,\,10^5]$ |
| $g$ | $[10^{-8},\,10^{-3}]$ — **includes the $g=10^{-3}$ worst-case the brief required** |
| $\psi_{AVE}$ | $[1.06\times10^{-9},\,9.11\times10^{-2}]$ rad |
| AVE/QED ratio | **field-INDEPENDENT $[4.136\times10^{6},\,4.250\times10^{6}]$** (median $4.136\times10^{6}$; the ~2.8% drift = exact-kernel curvature past leading order) |
| time-to-5σ | $[7.4\times10^{-16},\,8.35]$ s; **fastest $7.4\times10^{-16}$ s** at $E=5.2\times10^{14}$ V/m, $F=10^3$, $g=7.9\times10^{-4}$ (the sweet spot) |

Polarimetry floors used: realistic $10^{-9}$ rad (window gate), optimistic $10^{-11}$ rad.

**No-strawman compliance (ave.bench R1).** At every point the QED Euler-Heisenberg baseline is
co-computed through the **identical** `induced_ellipticity(g,F,L,λ)` machinery as the AVE √S leg;
the two legs differ **only** in the index-shift coefficient. There is no pre-baked SM array
anywhere — the QED side is the real E-H literature curve on the same E-grid.

**The discriminator does NOT degrade with $g$ in ratio terms.** The coefficient ratio is
$g$-independent (verified constant $4.136\times10^6$ at every swept $g$ from $10^{-3}$ to
$10^{-8}$ — $g$ multiplies $\delta n_{AVE}$ and $\delta n_{QED}$ equally, so it cancels in the
ratio). What $g$ degrades is the **absolute** signal-vs-floor margin: AVE stays detectable down
to $g\sim5\times10^{-9}$ (optimistic floor) / $5\times10^{-7}$ (realistic floor), with QED
$4.14\times10^6$ below throughout. The discriminating window in $g$ is therefore
$[\sim5\times10^{-9},\,1]$ — **enclosing the realistic $g\sim10^{-3}$**.

**Figures** (committed alongside the sweep JSON `src/scripts/vol_9_device/_output/`):
- `vacuum_birefringence_facility_sweep_signal_vs_field.png` — realized polarimeter ellipticity
  $\psi$ vs peak field at the sweet-spot geometry ($g=7.9\times10^{-4}$, $F=10^3$, $\lambda=1064$ nm,
  $L=1$ cm); AVE and QED co-computed through the identical `induced_ellipticity` machinery, AVE a
  field-independent $4.14\times10^6$ above QED, both polarimetry floors drawn.
- `vacuum_birefringence_facility_sweep_window_E_vs_g.png` — the divergence window in the
  $(E,\,g)$ plane at $F=10^3$; coloured cells in-window (clear realistic floor, exceed QED, inside
  small-angle); cell colour = the field-independent AVE/QED ratio (uniform — $g$ cancels);
  the window includes the $g=10^{-3}$ worst-case.
- `vacuum_birefringence_facility_sweep_time_to_5sigma.png` — shot-noise-limited time-to-$5\sigma$
  vs peak field across the $g\in[10^{-8},10^{-3}]$ tiers (1 W probe); $g$ sets the absolute
  integration time, **not** the AVE/QED ratio.

## 5. The geometry factor *g* — PINNED per config (OQ-1 partially closed)

> 🔴 **SUPERSEDED-IN-PART (Rule-12, 2026-06-21 OQ-1 close).** This section was the FIRST-CUT
> "$g$ derived only to leading order, asserted as a Gaussian-beam overlap parameter" residual. It is
> now superseded by the DERIVED + PINNED per-config $g_{eff}$ in **§5.1** below (full derivation:
> [`2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)).
> The first-cut spatial/temporal/sweet-spot text is preserved verbatim below it for audit-trail
> continuity; read §5.1 for the landed numbers (the first-cut "$1.4\times10^{-8}$ worst credible"
> and "$g\approx7.9\times10^{-4}$ sweet spot" are correct as the spatial single-pass values but
> did not yet pin the coherent-pass/temporal-gate structure that §5.1 resolves).

### 5.1 The PINNED per-config coupling (DERIVED — the OQ-1 close)

$g_{eff}$ is now a DERIVED function of explicit apparatus-inputs, $g_{eff} = g_{spatial}\cdot
g_{temporal}\cdot n_{coherent}$, with $g_{spatial,axial}=(2z_R/L)\arctan(L/2z_R)$ the **exact**
Lorentzian path integral (numeric quad $==$ closed form to machine precision; CHECK-3 PASS sub-part),
and $n_{coherent}=\min(2F/\pi,\ \tau_{pump}/\tau_{rt})$ the pump-gated coherent-pass count
($\tau_{build}=FL/\pi c$ threshold). At the PW-class point ($E_{peak}=2.745\times10^{14}$ V/m,
$A=2.43\times10^{-3}$, $w_0=\lambda_{pump}=800$ nm, $L=1$ cm, $F=10^3$, $\lambda_{probe}=1064$ nm;
$z_R=2.51\,\mu$m, $g_{spatial}=3.95\times10^{-4}$):

| Config | mode | $n_{coherent}$ | **$g_{eff}$** | **$\psi_{AVE}$ [rad]** | $\psi_{QED}$ [rad] | small-angle |
|---|---|---|---|---|---|---|
| **(i) CW high-$F$ (RECOMMENDED)** | CW pump, full build-up | $2F/\pi=637$ | **0.251** | **$2.19\times10^{-2}$** | $1.13\times10^{-9}$ | OK |
| (ii) pulsed single-pass | co-timed pulse, 1 transit | 1 | $3.95\times10^{-4}$ | $3.44\times10^{-5}$ | $1.78\times10^{-12}$ | OK |
| (iii-fs) gated cavity, 30 fs pump | recirculated, fs pump | **1** | $3.95\times10^{-4}$ | $3.44\times10^{-5}$ | $1.78\times10^{-12}$ | OK |
| (iii-ns) gated cavity, 20 ns gate pump | recirculated, ns pump | 600 | **0.237** | **$2.06\times10^{-2}$** | $1.07\times10^{-9}$ | OK |

(AVE/QED $=1.930\times10^7$ at **every** config — the matched par−perp differential ratio (FLAG-A
§6/§10); $g_{eff}$ cancels in the ratio.)

**The DD1 gated-cavity lever, RESOLVED to a NULL for an fs pump.** For the finesse build-up to add
coherently the pump must be present each time the recirculating probe re-enters the focus (every
$\tau_{rt}=L/c=33.4$ ps). A **30 fs pump gates exactly ONE coherent pass** ($n_{pump}=30\,\text{fs}/33.4\,\text{ps}=9.0\times10^{-4}\ll1$):
the gated cavity recovers **nothing** beyond single-pass ($g_{eff}$(iii-fs) $=$ $g_{eff}$(ii) exactly) —
the pump is gone before the probe completes one round trip. Recovering BOTH finesse AND temporal
overlap requires a **ns-class gate pump** ($\geq\tau_{build}=FL/\pi c=10.6$ ns), i.e. a $\sim3.5\times10^5\times$
larger pulse energy at fixed peak field. **You do not get both from one fs pump** — the mutually-exclusive
lever flagged in the first-cut (§5, below) is a hard pump-duration × finesse-product constraint, not a
free knob.

**RECOMMENDED CONFIG (Grant/engineering decision): (i) CW high-$F$ polarimeter** — full coherent
finesse, $g_{eff}=0.251$, $\psi_{AVE}=2.19\times10^{-2}$ rad at PW-class field, in small-angle and
$\sim10^7\times$ above the realistic $10^{-9}$ rad polarimetry floor. The **ns-gated pulsed cavity
(iii-ns)** is the near-equal pulsed-pump alternative ($g_{eff}=0.237$) for facilities that can only
deliver the peak field in a pulse but can stretch the gate to ns. The pulsed single-pass / fs-gated
configs ($g_{eff}=3.95\times10^{-4}$) remain detectable ($\psi=3.4\times10^{-5}$ rad, $\sim10^4\times$
floor) but forgo the finesse lever.

*Figures (committed):* `oq1_field_to_cavity_phase_coupling_birefringence_arc.{png,pdf}` (the DERIVED
uniaxial-tensor birefringence arc, $\delta n_{bir}=-\tfrac12 A^2$ vs the scalar single-arm $-\tfrac14 A^2$);
`…_config_coupling.{png,pdf}` (realized $\psi$ per config from the pinned $g_{eff}$);
`…_gate_constraint.{png,pdf}` (the pump-duration × finesse gating constraint — DD1 resolved).

### 5.2 First-cut $g$ residual (superseded by §5.1 — preserved for audit trail)

$g$ is the **field → cavity-phase coupling residual** — the pump-probe overlap fraction that maps
the field *at the focus* to a *detected* cavity-phase. It is an **optics/engineering coupling
(consistency-class, correctly OUTSIDE the AVE constants gate)** — not AVE physics. $g = g_{spatial}\cdot
g_{temporal}$:

- **Spatial.** Probe phase is the path-integral of the local $E^2$-weighted anisotropy. For a
  diffraction-limited Gaussian pump focus ($w_0\sim\lambda$, Rayleigh range $z_R=\pi w_0^2/\lambda$)
  crossing a cm cavity, collinear on-axis: $g_{spatial}=(2z_R\arctan(L/2z_R))/L \to \pi z_R/L$ in the
  $L\gg z_R$ limit $= 7.9\times10^{-4}$ (800 nm) to $1.05\times10^{-3}$ (1064 nm); robust
  $8\times10^{-4}$–$4\times10^{-3}$ over $w_0/\lambda$. A finite probe waist $w_p$ adds transverse
  dilution $w_0^2/(w_0^2+w_p^2)$ (~25× cost when $w_p\gg w_0$); a crossed-90° geometry gives
  $g_{spatial}\sim1.0\times10^{-4}$.
- **Temporal.** $g_{temporal} = \tau_{pump}/(L/c) = 30\,\text{fs}/33.4\,\text{ps} = 9.0\times10^{-4}$
  for a CW free-running probe (an fs pump is a sub-ppm temporal gate); $g_{temporal}=1$ for a
  **co-timed fs pulsed probe co-propagating with the pump** (rides the pulse, single-pass only).

**Defensible sweet spot** (collinear, co-timed fs pulsed, diffraction-limited $w_0\sim\lambda$,
cm cavity): $g_{spatial}=\pi z_R/L = 7.9\times10^{-4}$, $g_{temporal}=1 \Rightarrow g\approx
7.9\times10^{-4}$ (range $8\times10^{-4}$–$4\times10^{-3}$, $\sim10^{-3}$). Realized
$\delta n = g\,\delta n_{iso} = -1.5\times10^{-10}$; single-pass $\psi=(\pi/\lambda)|\delta n|L
= 4.6\,\mu$rad, $\sim10^5\times$ above a $10^{-15}$ index-shift floor. Worst credible (collinear
trans-averaged, CW probe): $g\sim1.4\times10^{-8}$. Finesse $F=10^3$ lifts $\psi$ to $2.9\times10^{-3}$
rad (small-angle OK); $F=10^5\to0.29$ rad (out of small-angle — a reason to stay modest-$F$).

Grounded in `derive_g.py` / `derive_g_floor.py` (scratch); $E_{YIELD}$ from `constants.py:438`,
kernel $\delta n=(1-A^2)^{1/4}-1\approx-\tfrac14 A^2$ from `birefringence_coefficient_bench.py:135-144`.

**The mutually-exclusive lever (flag — now RESOLVED in §5.1).** The co-timed fs pulsed probe
($g_{temporal}=1$) forgoes cavity build-up (single-pass); the CW high-$F$ probe gets finesse
enhancement but pays $g_{temporal}\sim9\times10^{-4}$. A combined gated-build-up
pulsed-probe-in-resonant-cavity treatment is *not* modeled here and could recover both — a follow-up
lever (§10). **→ RESOLVED in §5.1: for an fs pump the gated cavity recovers a NULL (one pass only);
both finesse and temporal overlap need a ns-class gate pump.**

## 6. The a_EH convention lock (DERIVE-2)

**HEADLINE PICK: $a_{EH} = 7/45$** (single-mode parallel index shift). Precise meaning: $7/45$ is
the QED Euler-Heisenberg weak-field coefficient for the mode whose E-vector is **parallel** to
the applied field: $n_\parallel-1 = (7/45)\alpha^2(E/E_{crit})^2$. Companions: $n_\perp-1 =
(4/45)\alpha^2(\cdot)$; differential $n_\parallel-n_\perp = (3/45)\alpha^2(\cdot)$. These come
directly from the E-H weak-field Lagrangian's $\tfrac{2\alpha^2}{45}[(E^2-B^2)^2+7(E\cdot B)^2]$
structure (standard single-mode QED — PVLAS/BMV/Rizzo lineage).

**Why 7/45 is canonical here:** (a) it is a *single-mode* index, pairing with the AVE single-channel
scalar-$|E|$ kernel — the instrument is a uniaxial probe, one mode at a time; (b) it is the
*largest* single-mode coefficient → smallest, most conservative AVE/QED ratio (does not over-state
the gap); (c) it matches the weak-field E-H expansion `vacuum-birefringence-e4.md:12` already quotes.

| Convention | $a_{EH}$ | ratio $1/(4a_{EH}\alpha^3)$ |
|---|---|---|
| single-mode parallel $7/45$ **(headline)** | 0.15556 | $4.14\times10^{6}$ |
| single-mode perp $4/45$ | 0.08889 | $7.24\times10^{6}$ |
| differential $3/45$ | 0.06667 | $9.65\times10^{6}$ |

All reproduced from live constants. **Physical single-mode band $[4.14\times10^6,\,9.65\times10^6]$**
— a factor-2.33 (7/3) spread, **sub-decade**; the falsifier's adjudication margin is ~6 OOM, so the
band does not blur it.

**FLAG-DON'T-FIX (surfaced, NOT silently fixed) — the $a_{EH}\approx1.45$ artifact.** The module's
4th band entry `A_EH_LITERATURE["PVLAS A_e differential (~1.45)"]` (`birefringence.py:102-105`) is
**NOT** an independent E-H mode convention. It is the differential $3/45$ coefficient multiplied by
$1/(2\pi\alpha)=21.81$ — a **units-normalization mismatch** between the dimensional magnetic
$A_e[\text{T}^{-2}]\cdot B^2$ form and the dimensionless electric $a_{EH}\alpha^2(E/E_{crit})^2$
mode-index form (back-solving $a_{EH}=3A_e B_{crit}^2/\alpha^2$ mixes the two normalizations).
Verified: $(3/45)\cdot1/(2\pi\alpha) = 1.453997$ = the module entry exactly (`np.isclose` True), and
the resulting ratio $4.42\times10^5$ is reproduced. **The $A_e$ form itself is correct** (it recovers
PVLAS) — it is only the *back-solved effective $a_{EH}=1.45$* that is a category-mixed number. It
should not anchor the band's low end. The genuine physical band is the rational single-mode set
$[3/45,\,7/45]$. (This closes the open §5.2 flag-don't-fix from
`research/2026-06-04_birefringence-coefficient-prereg.md:122`.)

## 7. The falsification criterion

A measured vacuum index shift $\delta n(E)$ at facility fields adjudicates:

- **$\delta n$ at the AVE coefficient** ($|\delta n|\approx\tfrac14(E/E_{yield})^2$, i.e.
  $\sim4\times10^6\times$ the E-H value) → **confirms** AVE's saturable-vacuum (tree-$O(1)$ kernel),
  **falsifies** QED at this observable.
- **$\delta n$ at the QED coefficient** ($a_{EH}\alpha^2(E/E_{crit})^2$) → **falsifies** AVE's
  saturable-vacuum prediction. A QED-sized coefficient is decisive against AVE here.

**An $E^2$ slope does NOT falsify AVE** — both are $E^2$-leading; the discriminator is the
coefficient. The ~6-OOM, field-*independent* gap is what makes this a clean two-sided falsifier:
there is no parameter (including $g$, which cancels in the ratio) that moves AVE toward QED.

**Match-the-observable (per `phase-space-coordinate-check` / Grant adjudication item):** a
single-mode phase-retardance probe matches $a_{EH}=7/45$ (ratio $4.14\times10^6$); a *differential*
ellipticity (PVLAS/BMV-style par-minus-perp) instrument is properly compared against $a_{EH}=3/45$
(ratio $9.65\times10^6$). The bench-design lane must pick the $a_{EH}$ that matches the observable the
instrument records. Physics verdict (AVE-distinct at all fields, ~6-OOM gap) is identical either way.

## 8. The honest experimental ask (PINNED per config — supersedes the first-cut)

> 🔴 **SUPERSEDED (Rule-12, 2026-06-21 OQ-1 close).** The first-cut ask read "$\psi_{AVE}\sim
> 2\times10^{-4}$–$2\times10^{-2}$ rad → 5σ in $<1\,\mu$s" with a *modest-$F$, overlap-limited,
> calibrated-$g$* recommendation premised on "high-$F$ drives out of small-angle." That premise is
> superseded: the **pinned** §5.1 analysis shows $F=10^3$ at the PW-class field **stays in
> small-angle** ($\psi_{AVE}=2.19\times10^{-2}$ rad $<0.1$ rad), so the CW high-$F$ finesse lever is
> *recommended*, not avoided. The pinned ask + recommended config follow; first-cut table preserved
> below for audit trail.

**PINNED ask (the apparatus-config is an explicit Grant/engineering decision — 3 configs, §5.1):**

| Parameter | PINNED ask | Provenance / tag |
|---|---|---|
| Pump intensity | $I\sim10^{22}$ W/cm² ($E_{peak}=2.745\times10^{14}$ V/m, PW-class) | APPARATUS-INPUT; reachable (ELI/Apollon-class) |
| Pump pulse | linearly-polarized, diffraction-limited $w_0\sim\lambda_{pump}$ ($z_R=2.51\,\mu$m) | sets $g_{spatial}=3.95\times10^{-4}$ (exact integral) |
| Probe | 1–10 W at 1064 nm at the PVLAS-tier shot floor ($S_\psi\sim2\times10^{-10}$ rad/$\sqrt{\text{Hz}}$) | APPARATUS-INPUT (floor still owed validate-on-known, R-3) |
| Cavity / finesse | $L=1$ cm, $F=10^3$ | $F=10^3$ stays in small-angle at PW-class (pinned) |
| **Geometry-factor $g_{eff}$** | **PINNED per config** (DERIVED): (i) CW high-$F$ **0.251**; (ii)/(iii-fs) single-pass **$3.95\times10^{-4}$**; (iii-ns) ns-gated **0.237** | DERIVED, §5.1; $g$ cancels in the AVE/QED ratio |
| **Recommended config** | **(i) CW high-$F$** → $\psi_{AVE}=\mathbf{2.19\times10^{-2}}$ **rad**; alt (iii-ns) ns-gated pulsed → $2.06\times10^{-2}$ rad | Grant/engineering decision (3 configs traded, §5.1) |
| Integration | $\psi_{AVE}\sim2\times10^{-2}$ rad (recommended) / $3.4\times10^{-5}$ rad (single-pass) → **5σ in $\ll1\,\mu$s** | shot-floor SNR; AVE detection integration-trivial |

**The AVE signal margin is overlap($g_{eff}$)-set, and the AVE/QED ratio is $g$-INDEPENDENT.** The
recommended **CW high-$F$ polarimeter** delivers $\psi_{AVE}=2.19\times10^{-2}$ rad against
$\psi_{QED}=1.13\times10^{-9}$ rad — the matched-differential ratio $1.93\times10^7$ (FLAG-A §6/§10).
The QED-vs-AVE integration-time gap is $\sim(1.93\times10^7)^2\sim3.7\times10^{14}$ (matched differential)
/ $\sim(4.14\times10^6)^2\sim1.7\times10^{13}$ (corpus single-arm) — i.e. a QED-coefficient signal would
take $10^{13}$–$10^{14}\times$ longer to reach the same SNR, which is what makes "did we see AVE-sized
or QED-sized" an unambiguous experimental call. **Engineering caveat (honest residual R-3):** the
absolute margin rides the polarimetry/detector floor, which is still owed a validate-on-known against a
published cavity (§10). The **coefficient** does not.

**First-cut ask (superseded by the pinned table above — preserved for audit trail):**

| Parameter | Ask | Provenance |
|---|---|---|
| Pump intensity | $I\sim10^{22}$ W/cm² ($E_{peak}\sim2.7\times10^{14}$ V/m, PW-class) | reachable today (ELI/Apollon-class) |
| Pump pulse | linearly-polarized, $\sim30$ fs, diffraction-limited $w_0\sim\lambda$ | sets $g_{spatial}$, $g_{temporal}$ |
| Probe | 1–10 W CW at 1064 nm at the PVLAS-tier shot floor ($S_\psi\sim2\times10^{-10}$ rad/$\sqrt{\text{Hz}}$) | OR co-timed fs pulsed probe ($g_{temporal}=1$, single-pass) |
| Cavity | $L\sim$ cm, **modest** finesse $F\sim1$–$10^3$ over the pump-Rayleigh overlap | high-$F$ drives out of small-angle |
| Geometry | a **calibrated** $g$ (overlap), not more finesse | $g$ is the dominant systematic, §5 |
| Integration | $\psi_{AVE}\sim2\times10^{-4}$–$2\times10^{-2}$ rad → **5σ in $<1\,\mu$s** | sweep §4; AVE detection is integration-trivial |

## 9. Discipline tags (chord-vs-echo / consistency-vs-emergence / coordinate / symmetric-standard)

| Quantity | Tag | Rationale |
|---|---|---|
| $\delta n_{AVE}$ FORM ($E^2$-leading √S kernel) | **MANIFESTATION** of Axiom 4 | the saturating-permittivity index shift is the kernel's optical specialization |
| $\delta n_{AVE}$ COEFFICIENT ($-1/4$ tree-$O(1)$ vs $\alpha^2$ loop) | **CHORD** (AVE-distinct STRUCTURE) | tree-saturable-medium vs loop-polarizable-vacuum; field-independent ~6-OOM gap |
| ratio MAGNITUDE $4.14\times10^6$ | **ECHO** (α-rooted) | $1/(4a_{EH}\alpha^3)$; AVE does not derive α — value-echo. **Symmetric standard:** QED's $a_{EH}\alpha^2$ is equally α-rooted; QED does not derive α either |
| geometry factor $g$ | **consistency-class, OUTSIDE the constants gate** | optics/engineering coupling; cancels in the ratio |
| $a_{EH}$ band | **labeled non-AVE LITERATURE input** | Heisenberg-Euler 1936 / Rizzo-PVLAS; not fit, not AVE-derived |
| $A_e$ recovery $1.3247\times10^{-24}$ T⁻² | **VALIDATE-ON-KNOWN** (HALT on fail) | recovers PVLAS textbook or the model is wrong |
| coordinates | **real-space optical-path** matched to real-space probe tensor | `phase-space-coordinate-check` PASS, no $\phi^2$-vs-Cartesian mismatch |

**Net:** the proposal is a peer-or-better, fully-specified, AVE-distinct **bankable falsifier** —
*provided the headline language separates the $g$-independent coefficient ratio from the
$g$-dependent absolute-signal margin* (FLAG-(i), §10).

## 10. Open items

1. **FLAG-(i) (flag-don't-fix, headline language).** Do NOT headline "discriminator survives to
   $g\sim10^{-3}$, still $10^4\times$ QED" — that conflates the **$g$-independent coefficient
   ratio ($4.14\times10^6$ at ALL $g$, not $10^4$)** with the **$g$-dependent absolute-signal-vs-floor
   margin**. The manuscript/OQ-1 language should state explicitly: (i) coefficient ratio
   $4.14\times10^6$ is $g$-independent; (ii) $g$ sets only the absolute realized signal; (iii)
   detectability window $g\gtrsim\sim5\times10^{-9}$–$5\times10^{-7}$ depending on floor.
   *(Auditor lands the manuscript wording; surfaced here.)*

2. **FLAG-(ii) — the $a_{EH}\approx1.45$ module artifact (§6).** `birefringence.py:102-105` ships
   the back-solved $a_{EH}=1.45$ entry (ratio $4.42\times10^5$), and the published band in
   `research/2026-06-20_vacuum-birefringence-bench_result.md:62` currently states
   $[4.42\times10^5,\,9.65\times10^6]$. RECOMMEND (auditor lands, not me): re-scope the published
   band to the physical single-mode set $[4.14\times10^6,\,9.65\times10^6]$ and demote the 1.45 entry
   to an explicitly-labeled "$A_e$ magnetic-form back-solve, off by $1/(2\pi\alpha)$ — DO NOT use as
   an electric-mode $a_{EH}$" comment (or remove it). This is the open `prereg:122` §5.2 flag.

3. **OQ-1 — PARTIALLY CLOSED (this doc is the strengthen-by; verdict `partially-closed`).** The field
   → cavity-phase coupling is now **DERIVED** from the Axiom-4 kernel (focal-E → uniaxial probe tensor
   → cavity round-trip phase → ellipticity) and the geometry factor $g_{eff}$ is **PINNED per
   apparatus config** (§5.1; derivation
   [`2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`](2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md)).
   The **COEFFICIENT** ($4.14\times10^6$ single-arm / $1.93\times10^7$ matched differential) is robust
   and field-independent; the absolute $\psi$/integration numbers are now PINNED (no longer first-cut).
   Three **named residuals** keep this *partially*-closed, not closed: **R-1** the derived par−perp
   *differential* ($-\tfrac12 A^2$) is a NEW observable, not the canonical leaf's scalar single-arm
   ($-\tfrac14 A^2$, `clm-pp3qwf` :12,:14) — promoting it into the leaf is an **auditor/Grant call**
   (FLAG-A, §6/§10-#10); **R-2** $u=|E|^2$ as THE invariant is an AVE modeling choice (QED uses two
   invariants → 7/45 vs 4/45); **R-3** the detector floor is owed a validate-on-known (open-item #4).
   The OQ-1 entry in `AVE-Bench-Birefringence/docs/open_questions.md` should be updated to
   "**partially-closed: coupling DERIVED + $g$ PINNED; residuals R-1/R-2/R-3**"
   (auditor/implementer-commit, next session — that file lives in the sibling repo, not this PR's tree).

4. **validate-on-known still owed on the detector floor.** The $10^{-15}$ (optimistic) / $10^{-13}$
   (realistic) index-shift floor and the $10^{-9}$/$10^{-11}$ rad polarimetry floors are asserted from
   PVLAS/BMV-class lineage, **not** validated-on-known against a specific published cavity sensitivity.
   A validate-on-known against a real PVLAS/BMV ellipticity floor is owed before the SNR/integration
   numbers fully harden. (The COEFFICIENT result does not depend on this.)

5. **Mutually-exclusive lever (§5) — RESOLVED (§5.1).** Co-timed fs pulsed probe ($g_t=1$,
   single-pass) vs CW high-$F$ (finesse build-up). The gated-build-up combined treatment is now
   **modeled**: an fs pump gates only **one** coherent pass (it is gone $33$ ps before the recirculating
   probe returns), so the gated cavity recovers a **NULL** for an fs pump — both finesse and temporal
   overlap need a **ns-class gate pump** ($\geq\tau_{build}=10.6$ ns, $\sim3.5\times10^5\times$ larger
   pulse energy). The recommended configs are CW high-$F$ (full finesse, $g_{eff}=0.251$) or ns-gated
   pulsed cavity ($g_{eff}=0.237$).

6. **Transverse-overlap dilution (§5).** Mode-matching the probe waist toward $w_0$ (or multi-pass
   focal recycling) is an un-modeled $g_{spatial}$ lever (~25× at $w_p\gg w_0$).

7. **Rotation-channel apparatus (the strictly-cleaner discriminator).** This doc specs the
   retardance/ellipticity COEFFICIENT polarimeter. The parity-odd optical-activity **rotation**
   channel ($\theta\neq0$, sign-flips, achiral-null; QED $\theta\equiv0$) is the zero-vs-nonzero
   discriminator and is **not yet apparatus-spec'd**. It is the stronger make-or-break; flagged for
   the apparatus roadmap.

8. **Two-color probe (dispersion chord).** The $(q\cdot\ell_{node})^4$ dispersion forward-prediction
   is not exercised by a single-λ probe; a two-color probe adds an orthogonal AVE-distinct axis.
   Out of scope, flagged.

9. **Bench-repo mirror (cross-repo promotion).** Copy this proposal into
   `AVE-Bench-Birefringence/docs/design/` and update its `open_questions.md` OQ-1 in a separate,
   separately-reviewed commit on that repo (cross-repo promotion is a different session per workspace
   discipline). Tracked here so it is not lost.

10. **FLAG-A (flag-don't-fix) — matched-observable ratio + new-observable promotion (R-1; auditor/Grant
    lands, surfaced here, NOT silently fixed).** The OQ-1 derivation produced a NEW observable: the
    par−minus−perp **differential** $\delta n_{bir}=-\tfrac12 A^2$ (a factor 2 above the canonical leaf's
    scalar single-arm $-\tfrac14 A^2$). At the **matched** differential observable a PVLAS/BMV
    ellipsometer actually reads, the ratio is **AVE($-\tfrac12$)/QED($3/45$) $=7.5/\alpha^3=1.93\times10^7$**
    (closed form, verified) — NOT the corpus headline $4.14\times10^6$, which pairs AVE single-arm
    ($-\tfrac14$) with QED single-mode-parallel ($7/45$) — a **mismatched** pairing. RECOMMEND (auditor
    lands): state the headline observable-matched — single-arm-retardance probe → $4.14\times10^6$
    (AVE $-\tfrac14$ vs QED $7/45$); differential ellipsometer → $1.93\times10^7$ (AVE $-\tfrac12$ vs QED
    $3/45$). And decide whether to promote the differential observable into `clm-pp3qwf` (the canonical
    leaf currently headlines only the scalar single-arm; the differential framing entered via §2 of
    this proposal, not the leaf). The physics verdict (AVE-distinct at all fields, $\gtrsim6$-OOM gap) is
    identical either way; the chord-vs-echo split is unaffected (FORM = chord; magnitude = α-echo at
    either ratio). Surfaced verbatim, not reframed.
