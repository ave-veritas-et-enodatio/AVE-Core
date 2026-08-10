# LC-1 — ONE-SPEED (multi-messenger) — FROZEN pre-registration

**Date:** 2026-08-06 · **Branch:** `research/lc1-one-speed` · **Arc:** Lorentz-compliance (Grant GO
2026-08-04; resequenced to LEAD by ruling R15, `_orchestration/docket-entries/2026-08-06-rulings-final-batch.md`)
**Arc brief:** [`_orchestration/2026-08-04_lorentz-compliance-arc-brief.md`](../_orchestration/2026-08-04_lorentz-compliance-arc-brief.md)
(including its DATED CURRENCY UPDATE 2026-08-06 EOD).
**Base:** `origin/main` @ `d129e7ac` (the PR #910 LC-brief currency merge).
**Class:** DERIVATION-ONLY (Tier-2 at adjudication). No simulation campaign. Engine `src/ave`
byte-untouched and imported READ-ONLY for constants. Mints no `clm-`/`def-`; propagates to no
KB/manuscript leaf; edits no register, no falsification ledger, no docket ruling.
**SVA pilot pass** (this leaf runs the `standard-vacuum-analysis.md` v0.2 §0 header; it does NOT
canonize the SVA leaf).

**This document is frozen ALONE and pushed BEFORE any derivation text, any driver code, and any
number produced by this lane exists** (`ave-prereg` v1.8 Step 3.11 — the freeze is a git fact
claimable only by commit/push ordering).

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot)

```markdown
 1. SECTOR / OWNERSHIP:      per-channel, below; cross-wiring check RUN
 2. REGIME / PHASE-STATE:    MODE = far-field linear wave propagation between two events;
                             REGIME = Regime-I cold-linear vacuum, small-signal;
                             PHASE-STATE = cold, unsaturated, A << 1, S(A) = 1 on the whole
                             propagation path. The SOURCE is NOT cold — see the split in row 5.
 3. CIRCUIT STATEMENT:       a two-terminal delay measurement between one launch event and two
                             receivers, on a lossless multi-channel transmission medium: how many
                             independent propagating channels does the medium present between the
                             two events, what is each channel's phase/group velocity, and which of
                             them terminates into a real detector impedance.
 4. PLANE & PROJECTION:      reference plane = the far-field (source region excluded); projection =
                             the Christoffel eigen-decomposition of the medium's acoustic tensor
                             on a plane-wave ansatz, i.e. the plane-wave EIGENVALUE basis, not the
                             modulus basis. This distinction is load-bearing (see FLAG-LC1-A).
 5. CONSTITUTIVE PROVENANCE: G (shear) = DEFINITIONAL-IDENTITY at the constants module
                             (G_VAC := rho c^2); rho_bulk = DERIVED-from-topological-primitives;
                             K = 2G = IMPORTED (GR-imported, PR #261, re-attributed at
                             constants.py:769-773); G_c, I_omega, gamma = ENG-CHOICE placeholders;
                             the rotational gap E_g = hbar omega_m = 2 m_e c^2 = IMPORTED (CODATA
                             m_e) with the FACTOR derived (A-008).
 6. ENERGY LEDGER:           the only ports in this lane are (i) the far-field radiative ports of
                             the medium's own propagating channels and (ii) the detector
                             terminations that read them. No bulk resistor is invoked anywhere; all
                             propagation is Axiom-3 lossless-reactive. "Sourced" means a
                             boundary-crossing arrow exists from the merger into the channel;
                             "read" means a second arrow exists from the channel into a detector's
                             real impedance.
 7. CALIBRATABILITY:         the target is a DIMENSIONLESS RATIO (v_channel / c_EM) and a PORT
                             PHASE/ARRIVAL DIFFERENCE between two receivers. Both are
                             self-calibratable from inside the medium. No unit bridge is crossed.
 8. DISCRIMINATION CLASS:    PURE-AC. Wave speeds and arrival times are shared observables with
                             the competitor framework; GR + SM also predict c_GW = c exactly. A
                             PASS here is EXPECTED CONSISTENCY, not a discriminating survival.
                             Only the FAIL direction carries information. Tautology filter and SM
                             counterfactual run in §1.2.
 9. CERTIFICATION PLAN:      bins and gates frozen in §7/§9 before any number exists; negative
                             controls named; UNRUN != PASSED; every load-bearing numeral in the
                             result doc machine-gated against a shipped JSON with a mutation
                             receipt.
10. ADJUDICATION ROUTING:    §12. This lane's own comparator settles ONE axis (does the GW170817
                             dataset read a non-c channel). The inherited-corpus-state axis is
                             declared ENTAILED at freeze and is reported, NOT adjudicated here.
11. NUMERICAL CONDITIONING:  no iterated map, no cancellation-sensitive subtraction. All quantities
                             are closed-form algebraic functions of the moduli evaluated once in
                             IEEE double; the one long accumulation (post-Newtonian inspiral time
                             to frequency) is a single power law evaluated in log space. Regex
                             engine for every doc scan: Python `re`, named per the two-method
                             discipline.
```

### §0.1 — Sector / ownership, per channel (row 1 expanded; cross-wiring check RUN)

| object | OWNER sector | never cross-wired to |
|---|---|---|
| mass / inertia / the gravitational source moment | **A1 dilatation** (the longitudinal V-sector scalar grade, `def-9a4f07`) | not the Cosserat winding, not the T2 photon |
| charge / spin-1/2 | **Cosserat (2,3) micro-rotation winding** (couple-stress $\gamma$-grade) | not A1; not the massless EM-inductive B-rotation |
| the photon | **T2 transverse-translational $u$** (the G2 relabel, `k4-port-irrep-decomposition.md` G2 note) | not the micro-rotational $\omega$ |
| the observed gravitational wave | **T2 transverse shear** | not the A1 bulk channel |

The cross-wiring hazard specific to THIS lane is the A1/T2 one: it is tempting to say "the bulk
channel is confined by the same wall that confines the shear channel." That is a cross-owner
claim and it is NOT asserted here; the wall's channel-scoping is exactly the open cross-grade
question fenced in §0.4.

**A second, subtler ownership question this lane must NOT silently resolve:** the port register
carries channel 1 (EM-transverse, $Z_{EM} = Z_0$) and channel 2 (mechanical shear / GW,
$Z_{shear} = \rho c_{shear}$) as two rows, both $T_2$, both transverse-$u$, both at $c$. Whether
they are two branches of one operator or **one branch read in two conjugate variable pairs** is
load-bearing for LC-1(a) and is raised as FLAG-LC1-C, not decided.

### §0.2 — Substrate-native walk (`substrate-native-check`, fired BEFORE the first line of code)

- **K4 / lattice:** the medium is a discrete K4/Cosserat network, not a continuum. Every speed
  quoted here is an $O(k^2)$ long-wave limit of a band structure with a real Brillouin zone; the
  dispersion curvature is LC-3's business and is fenced out of this lane.
- **Cosserat:** the medium carries an independent micro-rotation DOF with its own modulus and its
  own gap. It is a FOURTH channel, not a polarization of the other three, and it must appear in
  the enumeration on its own row.
- **Op14 / saturation:** OFF on the propagation path by construction (cold-linear). Declared, not
  assumed — see §0.4.
- **Phase-space vs real-space:** the observable here is a REAL-SPACE arrival time and a REAL-SPACE
  propagation speed. It is not a phase-space claim, so A46 does not bind; the check is run
  explicitly in §0.3 rather than skipped.
- **SM/QED default that would leak in if this walk were skipped:** "the vacuum has one speed
  because Lorentz invariance is a symmetry of the Lagrangian." That is the wrong register
  entirely. The substrate-native statement is: **a material medium has as many speeds as its
  acoustic tensor has distinct eigenvalues**, and one-speed-ness is a statement about that
  eigenvalue spectrum plus which eigenvalues have open ports.

### §0.3 — Phase-space coordinate check (A46)

The corpus claim under test ("all inter-event energy travels at $c$") is stated in REAL-SPACE
propagation coordinates, and the comparator (GW170817 arrival-time difference) is measured in
REAL-SPACE arrival time. Coordinates MATCH. A46 does not bind this lane and no $\varphi^2$ /
Clifford-torus / impedance-plane translation is required. Recorded rather than omitted.

### §0.4 — Cross-grade combine-member declaration (the #905/#907 rescope-v2 fence)

Per the mandatory input: the kernel-collapse rescope v2 ruling
(`_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2.md`, PR #905, with
the post-merge correction #907) fences its channel carve-out to the **per-grade
(L∞-across-grades) combine member**, and states verbatim that *"The cross-grade combine rule is
open in canon"*. **Declared here as a header row rather than assumed:**

- **Every propagation leg of this lane runs cold-linear**, $A \ll 1$, and therefore evaluates
  every saturation kernel at $S(A) = 1$. At $S = 1$ the per-grade member, the
  normalized-L2-across-grades member, and the sym-only/`V^2/V_SNAP^2` amplitude definition are
  **numerically identical** (each is a product of unit kernels). The propagation verdict is
  therefore predicted to be **combine-member-INSENSITIVE**, and G-MEMBER (§9) tests exactly that
  by re-evaluating every derived speed under both members.
- **The SOURCE-COUPLING leg is NOT cold and is NOT member-insensitive.** A neutron star is a
  saturated region; whether the merger drives the bulk channel is inherited from #761/#765 and
  rides the envelope lane's OPEN constituent-knot-core fork. This split is stated in advance so
  that a member-insensitive propagation result is not mis-read as a member-insensitive verdict.

### §0.5 — Pre-test physics check (Rule 16 — one plumber-physical question to Grant, BEFORE design locks)

**Q(LC-1).** *A neutron-star merger is a mass quadrupole shaking a medium that has both a shear
modulus and a bulk modulus. In any real elastic solid that launches BOTH an S-wave and a faster
P-wave, and an earthquake seismologist reads the P-arrival first. AVE's medium has $K \neq 0$,
so it has a P-wave, and it is faster than $c$. The question is not whether the P-wave exists —
Christoffel says it does for any $K > 0$. The question is: **when the P-wave from a chirping
binary arrives at your detector, what frequency is it at?** Because a channel that runs at
$1.83c$ hands you the source's PAST, and a chirping source's past is at LOWER frequency. Is the
right reading of "observability" for this lane (i) the channel exists and is sourced, or (ii) the
channel lands inside a detector's band at the coincidence time? Those give different verdicts and
LC-1's frozen kill condition can be read either way.*

**Routed to Grant BEFORE the design locked.** This lane does not pick; it freezes BOTH readings as
separate bin axes (§7) and reports both, per KEEP-BOTH.

## §1 — The target, and the explicit non-claims

### §1.1 The target

Two derivations and one adjudication.

- **(a)** The provenance of cold $c_{shear} = c$. Is $G_{vac} = \rho c^2$ a DERIVATION or a MATCHING
  CONDITION? Classify per `consistency-vs-emergence` (definitional identity / axiom manifestation /
  consistency check / emergence) with the derivation path traced to file:line.
- **(b)** The observability of the bulk $\sqrt{10/3}\,c$ P-wave. Enumerate **every** energy-carrying
  inter-event channel the substrate supports, using the port register's channel inventory as the
  enumeration frame, with each channel's speed and its observability status. Re-derive
  $\sqrt{10/3}$ from the moduli rather than quoting it, and carry the $K = 2G$ import provenance.
- **The adjudication:** does an energy-carrying inter-event channel at speed $\neq c$, that a
  GW170817-class event sources and a detector reads, exist? Bins in §7.

### §1.2 The non-claims, written in advance and binding

1. **This lane does not claim AVE-distinctness on any PASS outcome.** The observable is PURE-AC
   (SVA row 8). GR predicts $c_{GW} = c$ exactly; SM predicts $c_\gamma = c$ exactly. A compliant
   outcome is EXPECTED CONSISTENCY. `ave-discrimination-check` is run in advance here rather than
   after: the tautology filter asks whether "AVE's GW travels at $c$" reduces to a known identity
   restated — and if the photon and the GW turn out to be the same $T_2$ transverse-$u$ branch,
   **it does**, exactly and trivially. In that case the word "STRONG" is forbidden in the result
   doc and the honest label is IDENTITY-class compliance. The SM counterfactual is that a
   framework which builds $c$ in by construction gets the same PASS for free.
2. **This lane does not re-litigate the banked pulsar exclusion.**
   `genesis-chord-falsification-ledger.md` entry `q1-reading-A-radiative-bulk-port` is a PRIOR on a
   DIFFERENT comparator class (binary-pulsar orbital-decay timing). It is cited, its conditionals
   are carried, and it is not re-derived, re-graded, or re-argued.
3. **This lane does not edit the port register.** Whatever it finds about Q1 or FLAG-A is stated as
   a narrowing with receipts and routed to the auditor lane. KEEP-BOTH: no row is redefined in
   place.
4. **This lane does not resolve the A1-radiativity contradiction it surfaces** (FLAG-LC1-B). Both
   sides are quoted verbatim with paths and routed.
5. **This lane does not claim any statement about the electron, the rest mass, the value of $c$,
   or the Q1 ruling's correctness.**
6. **This lane does not derive dispersion, anisotropy, birefringence, or form factors.** Those are
   LC-2..LC-5 and are fenced out even if this lane's channel table touches their inputs.

### §1.3 What "one-speed" is being read to mean, stated before the derivation

The claim under test is NOT "the substrate has exactly one wave speed" — the corpus openly carries
four channels at three or four distinct speeds and says so in a table titled *"three speeds, do not
fuse"*. The claim under test is the **multi-messenger** claim: *every channel that actually carries
energy from one astrophysical event to a detector runs at $c$*. A medium may carry a hundred
eigen-speeds and still be multi-messenger-compliant if the non-$c$ ones are gapped, non-propagating,
unsourced, or unread. That is why (b) is an ENUMERATION with a per-channel mechanism, not a
speed-counting exercise.

## §2 — The comparator, re-retrieved from source

**Rule zero (arc brief): pointers-not-values. Nothing numeric in the brief is load-bearing; every
published bound is re-retrieved from source at lane time.** Retrieval performed 2026-08-06 via the
external-retrieval pipeline against the arXiv abstract pages.

### §2.1 The primary comparator — the joint GW/GRB paper

**Citation as retrieved:** LIGO Scientific Collaboration, Virgo Collaboration, Fermi Gamma-Ray
Burst Monitor, and INTEGRAL, *"Gravitational Waves and Gamma-rays from a Binary Neutron Star
Merger: GW170817 and GRB 170817A"*, **The Astrophysical Journal Letters, 848:L13 (27pp), 2017
October 20**; arXiv:1710.05834.

**Verbatim from the retrieved abstract** `[sic]`:

> "On 2017 August 17, the gravitational-wave event GW170817 was observed by the Advanced LIGO and
> Virgo detectors, and the gamma-ray burst (GRB) GRB 170817A was observed independently by the
> Fermi Gamma-ray Burst Monitor, and the Anticoincidence Shield for the Spectrometer for the
> International Gamma-Ray Astrophysics Laboratory. The probability of the near-simultaneous
> temporal and spatial observation of GRB 170817A and GW170817 occurring by chance is
> $5.0\times 10^{-8}$. We therefore confirm binary neutron star mergers as a progenitor of short
> GRBs... We use the observed time delay of $(+1.74 \pm 0.05)\,$s between GRB 170817A and GW170817
> to: (i) constrain the difference between the speed of gravity and the speed of light to be
> between $-3\times 10^{-15}$ and $+7\times 10^{-16}$ times the speed of light..."

**The comparator interval, as retrieved:** the difference between the speed of gravity and the
speed of light is constrained to lie between $-3\times 10^{-15}$ and $+7\times 10^{-16}$ times the
speed of light. **Observed time delay:** $(+1.74 \pm 0.05)$ s.

### §2.2 The source parameters — the discovery paper

**Citation as retrieved:** LIGO Scientific Collaboration and Virgo Collaboration, *"GW170817:
Observation of Gravitational Waves from a Binary Neutron Star Inspiral"*, **Phys. Rev. Lett. 119,
161101 (2017)**; arXiv:1710.05832.

**Verbatim from the retrieved abstract** `[sic]`, the two quantities this lane consumes:

> "...with the total mass of the system $2.74^{+0.04}_{-0.01}\,M_\odot$. The source was localized
> within a sky region of 28 deg$^2$ (90% probability) and had a luminosity distance of
> $40^{+8}_{-14}$ Mpc, the closest and most precisely localized gravitational-wave signal yet."

**Consumed:** total mass $2.74\,M_\odot$; luminosity distance $40$ Mpc.

**The chirp mass is NOT quoted verbatim** (it does not appear in the retrieved abstract). Rather
than import an unretrieved number, this lane **derives** the chirp mass from the verbatim total
mass under an explicitly-declared equal-mass assumption,
$\mathcal{M} = M_{tot}\,(1/4)^{3/5}$, and tags it DERIVED-FROM-QUOTED-TOTAL-MASS. The frequency
result of §4 is checked for sensitivity to that assumption (G-CHIRP, §9).

### §2.3 The detector band — the one comparator input that is NOT verbatim-retrieved

The LIGO low-frequency analysis cutoff is required by §4's derivation. It is **not** present in
either retrieved abstract. It is therefore entered as a BRACKETED ENGINEERING INPUT with an
explicitly conservative value: the ground-based network's low-frequency wall is taken as
$f_{low} = 20$ Hz, and the derivation's conclusion is required to be robust across
$f_{low} \in [10, 30]$ Hz (G-BAND, §9). If the conclusion is not robust across that bracket, the
band leg is NOT-CERTIFIED and the corresponding bin is unreachable. **This is the lane's weakest
comparator input and it is flagged here rather than in the result.**

## §3 — The derivation plan

### §3.1 Leg (a) — provenance of cold $c_{shear} = c$

**Step a1 — read the constants-module chain at file:line and classify it.** `constants.py:757-766`
defines $\rho_{bulk}$ from topological primitives and then defines $G_{VAC} := \rho_{bulk} c^2$.
The classification question is whether $G$ is fixed independently and $c = \sqrt{G/\rho}$ then
falls out, or whether $G$ is assigned the value that makes $\sqrt{G/\rho} = c$ true. Verdict
recorded with the verbatim comment text.

**Step a2 — separate the FORM from the VALUE.** Consume the two-band k·p result
(`research/2026-08-05_two-band-kinematics_result.md` §3, KB row `clm-2bkp7v`): the
transverse-translational branch has $v^2 = G/\rho$ **identically for all moduli**, obtained as the
direct micropolar stiffness $(G+G_c)/\rho$ minus the k·p level repulsion $G_c/\rho$. Re-derive
this cancellation independently from the isotropic micropolar constitutive law rather than quoting
it (G-KP, §9). The FORM statement and the VALUE statement get separate
`consistency-vs-emergence` tags.

**Step a3 — the identity question.** Determine whether the port register's channel 1 (EM
transverse) and channel 2 (mechanical shear / GW) are the same Christoffel eigenbranch. If they
are, $c_{GW} = c_{EM}$ is an IDENTITY (one branch, one speed) and the GW170817 bound is satisfied
at arbitrary precision with zero free parameters. If they are two branches, the corpus owes a
mechanism for their exact degeneracy and the bound becomes a live constraint on that mechanism.
This step reports what canon says and FLAGS the gap; it does not decide (FLAG-LC1-C).

### §3.2 Leg (b) — the channel enumeration and the $\sqrt{10/3}$ re-derivation

**Step b1 — re-derive the longitudinal speed from the moduli, from scratch.** Build the acoustic
(Christoffel) tensor of an isotropic linear-elastic medium,
$\Gamma_{ik}(\hat n) = C_{ijkl}\,\hat n_j \hat n_l$ with
$C_{ijkl} = \lambda\,\delta_{ij}\delta_{kl} + G(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$
and $\lambda = K - \tfrac{2}{3}G$. Diagonalize. Report the FULL eigenvalue spectrum with
multiplicities. Then substitute $K = 2G$ and report $v_L/v_T$. Independently cross-check against
the Poisson ratio $\nu = (3K-2G)/(2(3K+G))$ and against the corpus `NU_VAC` symbol.

**Step b2 — the import-provenance separation, and the $K$-independence of the KILL-relevant
statement.** $K = 2G$ is GR-IMPORTED (PR #261; re-attributed verbatim at `constants.py:769-773`),
so the VALUE $\sqrt{10/3}$ inherits that import. But the statement the kill condition actually
needs is weaker: derive the condition on $K$ under which $v_L > v_T$. If $v_L > c$ follows from
$K > 0$ alone, then the existence of a superluminal longitudinal channel is **axiom-forced** (the
medium has a bulk modulus because it carries A1 dilatation-mass) and no re-choice of $K$ rescues
it. Report which.

**Step b3 — adjudicate the two channel-3 columns (FLAG-A).** The port register carries channel 3
with TWO speed columns, a PORT/impedance $\sqrt2\,c$ and a RADIATIVE $\sqrt{10/3}\,c$. Step b1's
eigenvalue spectrum settles, without any new physics, whether $\sqrt2\,c$ is a plane-wave
eigenvalue of the medium at all. This is a NARROWING of FLAG-A, executed as a derivation and
routed to the auditor lane; **no register edit is made.**

**Step b4 — the gapped channel's numbers.** Take the rotational gap
$E_g = \hbar\omega_m = 2 m_e c^2$ as pinned by A-008
(`research/2026-08-05_a008-factor-propagation_note.md`, BIN `FACTOR-CLOSED-BY-A008`), evaluate the
merger's drive quantum $\hbar\omega_{drive}$ at the GW170817 band, and form the ratio. Evaluate the
Yukawa reach $\ell_{node}$ against the 40 Mpc path length. Both from `ave.core.constants`.

**Step b5 — the observability determination for each channel, against THIS comparator.** For every
channel, answer three questions with a named mechanism: is it a propagating plane wave at all; is
it SOURCED by a GW170817-class event; is it READ by the GW170817 detector network. The third
question requires the arrival-kinematics derivation of §3.3.

### §3.3 Leg (c) — the arrival kinematics of a superluminal channel from a chirping source

**Derived here, from first principles, because it is the leg that this lane's own comparator
actually decides.**

A channel at speed $v > c$ from a source at distance $D$ delivers, at a fixed reception epoch, the
radiation emitted at retarded time $t_e = t_{obs} - D/v$, while the $c$-channel delivers
$t_e' = t_{obs} - D/c$. The superluminal channel therefore shows the source EARLIER by

$$\Delta t \;=\; \frac{D}{c} - \frac{D}{v} \;=\; \frac{D}{c}\left(1 - \frac{c}{v}\right).$$

For a **chirping** source the retarded epoch fixes the frequency. Using the quadrupole inspiral
time-to-coalescence relation (leading order),

$$f_{GW}(t_c) \;=\; \frac{1}{\pi}\left(\frac{5}{256\,t_c}\right)^{3/8}\left(\frac{G\mathcal{M}}{c^3}\right)^{-5/8},$$

evaluate $f_{GW}$ at $t_c = \Delta t$. **The physical content:** a superluminal channel is a
kinematic DETUNER — it hands the observer the source's deep past, and a monotonically-chirping
source's deep past is at far lower frequency. The faster the channel, the deeper the past, the
lower the frequency.

**Both directions must be reported honestly.** This mechanism can only ever move a
superluminal channel DOWN in frequency at a fixed coincidence epoch. It therefore cannot rescue
any comparator whose readout is a secular energy budget rather than an arrival time — and the
banked pulsar exclusion is exactly such a readout. Stated in advance so that a band-mismatch
finding is not mis-sold as a rescue.

### §3.4 What is NOT in the plan

No band-structure computation, no engine run, no eigensolve, no lattice sweep, no dispersion
extraction, no antenna-pattern derivation from first principles (the interferometer's scalar-mode
response is entered as an IMPORTED standard-instrument fact in §10 and is deliberately kept OFF
the load-bearing chain; the arrival-kinematics leg carries the verdict on its own).

## §4 — Analytic expectations, with numbers

**`ave-prereg` v1.8 Step 3.9 — a run that cannot state its analytic expectations is not ready to
run. Every number below is PREDICTED here, before any code exists, and each is checked against the
lane's own computation in the result doc. A prediction that misses is reported as a miss.**

### §4.1 Predicted eigenvalue spectrum (leg b1)

The isotropic Christoffel tensor is predicted to have exactly **two distinct eigenvalues** for any
propagation direction: one longitudinal with multiplicity 1 at $\rho v_L^2 = K + \tfrac{4}{3}G$,
and one transverse with multiplicity 2 at $\rho v_T^2 = G$. **Predicted: there is no eigenvalue at
$K/\rho$.** If a third distinct eigenvalue appears, the derivation is wrong and the lane is
NOT-CERTIFIED.

### §4.2 Predicted numbers

| quantity | predicted value | basis |
|---|---|---|
| $v_L/v_T$ at $K=2G$ | $\sqrt{10/3} \approx 1.826$ | $(2G + 4G/3)/G = 10/3$ |
| $v_T/c_{EM}$ | exactly $1$ | $G_{VAC} := \rho c^2$ |
| Poisson ratio $\nu$ | $2/7 \approx 0.2857$ | $(3K-2G)/(2(3K+G))$ at $K=2G$; must equal the corpus `NU_VAC` |
| condition for $v_L > v_T$ | $K > 0$ | $K + \tfrac43 G > G \iff K > -\tfrac13 G$ |
| $1 - c/v_L$ | $\approx 0.452$ | $1 - \sqrt{3/10}$ |
| light-travel time over 40 Mpc | $\approx 4.12\times10^{15}$ s $\approx 130$ Myr | $D/c$ |
| **retarded offset $\Delta t$ of the P-channel** | $\approx 1.86\times10^{15}$ s $\approx 59$ Myr | $(D/c)(1-c/v_L)$ |
| derived chirp mass from $M_{tot}=2.74\,M_\odot$ | $\approx 1.19\,M_\odot$ | $M_{tot}(1/4)^{3/5}$ |
| **$f_{GW}$ at $t_c = \Delta t$** | $\approx 2.5\times10^{-4}$ Hz | leading-order inspiral chirp |
| **band shortfall vs $f_{low} = 20$ Hz** | $\approx 8\times10^{4}$, i.e. $\approx 4.9$ decades BELOW the band | ratio |
| rotational gap $E_g$ | $2 m_e c^2 = 1.022$ MeV | A-008 pin |
| merger drive quantum at 100 Hz | $\approx 4\times10^{-13}$ eV | $\hbar\omega$ |
| **drive/gap ratio** | $\approx 4\times10^{-19}$ | ratio |
| Yukawa reach $\ell_{node}$ | $\approx 3.9\times10^{-13}$ m | `L_NODE` |
| **path length in Yukawa reaches over 40 Mpc** | $\approx 3\times10^{36}$ | $D/\ell_{node}$ |

### §4.3 Predicted qualitative outcomes, stated so they can miss

1. **Predicted:** $G_{VAC} = \rho c^2$ is a **matching condition**, i.e. the VALUE $c$ is a
   definitional identity at the constants module; but the **FORM** $v_T = \sqrt{G/\rho}$ with the
   gap modulus $G_c$ cancelling exactly is an **axiom manifestation** (a theorem of the micropolar
   energy functional's long-wave reduction). Split verdict predicted, not a single tag.
2. **Predicted:** the $\sqrt2\,c$ column of FLAG-A is **not** a plane-wave eigenvalue — the
   register's own two-column split is between a genuine wave and an impedance/modulus quantity,
   not between two waves. If instead $\sqrt2\,c$ appears in the spectrum, this prediction is wrong
   and the result says so.
3. **Predicted:** the superluminal-channel existence is **$K$-forced, not import-forced** — the
   $K=2G$ import moves the number $1.826$ but cannot move the inequality $v_L > c$.
4. **Predicted:** the Cosserat channel is DEAD for this comparator by two independent margins
   (drive/gap $\sim 10^{-19}$; path/reach $\sim 10^{36}$), i.e. over-determined, so the conclusion
   is robust to large errors in either.
5. **Predicted:** the bulk P-channel is **sourced** (inherited, conditional) and **out-of-band at
   arrival by roughly five decades**, so this lane's own comparator does NOT read it.
6. **Predicted:** bin (i) COMPLIANT as literally worded in the dispatch (*"all inter-event energy
   channels at c, or non-c channels shown gapped/confined/sourceless"*) is **UNREACHABLE**, because
   merged canon has already falsified all three of gapped, confined, and sourceless for channel 3b.
   See §8.

### §4.4 Predictability disclosure — what this lane already knows at freeze

Honesty requires stating this before the run rather than discovering it at review. At freeze, the
lane has already READ (as mandated by the dispatch) the merged corpus state that makes prediction 6
above nearly certain: the port-register Q1 row is **REVERTED to Reading-A LIVE** (not
"explicitly-OPEN" as the dispatch describes it), and the falsification-ledger entry
`q1-reading-A-radiative-bulk-port` is a **LIVE closed-negative against the framework's
gravitational-radiation sector**. Therefore:

- The **inherited-state axis** of §7 is very largely known at freeze. It is declared ENTAILED in
  §8 and is NOT counted as an adjudicated result of this lane.
- The **genuinely unknown quantities at freeze** are: the full eigenvalue spectrum (§4.1), the
  $K$-independence result (§4.3 prediction 3), the retarded-offset frequency (§4.2), and the
  band-robustness bracket. Those, and only those, are what this lane's own comparator decides.

## §5 — The channel-enumeration frame and the observability vocabulary

### §5.1 The enumeration frame

Per the dispatch, the enumeration frame is the port register's channel inventory
(`manuscript/ave-kb/common/port-register.md` §1, four channel rows). **Frozen scope of the frame:**
a CHANNEL is an inherent, axiom-level propagating capability of the MEDIUM. A messenger that is a
bound excitation riding a channel (a neutrino, a cosmic ray, a photon) is enumerated under the
channel it rides, not as a channel of its own. Any messenger this lane cannot assign to a channel
is enumerated on its own row and tagged **UNDERIVED**, and the lane does not guess.

The enumeration must additionally SPLIT channel 3 into its two FLAG-A columns, because the register
itself carries them as distinct objects and the whole of leg (b) turns on whether both are waves.

### §5.2 The observability vocabulary — the dispatch's four mechanisms, plus one this lane adds

The dispatch's frozen mechanism vocabulary for a non-$c$ channel is: **gapped** (below what
energy), **confined/evanescent**, **sourceless** (no astrophysical source term couples), or
**radiative**. Freezing an addition, with the reason stated in advance:

- **NOT-A-WAVE** — the speed in question is a modulus/impedance combination, not an eigenvalue of
  the medium's acoustic tensor, so no plane wave propagates at it and it cannot carry inter-event
  energy at all. Needed because FLAG-A's $\sqrt2\,c$ column is a candidate for exactly this status
  and the four-item vocabulary has no slot for it.
- **OUT-OF-BAND-AT-ARRIVAL** — the channel is radiative, sourced, and in-principle readable, but
  its content arriving coincident with the $c$-channel signal is at a frequency outside the
  comparator detector's band, by the arrival-kinematics mechanism of §3.3. Needed because it is a
  distinct physical status from all four dispatch items: it is not gapped (the channel is
  gapless), not confined (it propagates to the detector), not sourceless (the source drives it),
  and calling it simply "radiative" would suppress the comparator-power fact that decides this
  lane.

**These two additions are declared as an incompleteness finding against the dispatch's frozen
mechanism list, not as a redefinition of it.** KEEP-BOTH: the original four are retained verbatim
and used wherever they apply, and every channel row reports its status in the six-item vocabulary
with the addition flagged.

**A status of OUT-OF-BAND-AT-ARRIVAL is explicitly NOT a compliance mechanism in the physics
sense.** It is a statement about THIS comparator's power. The result doc must say so on the same
line, every time, and must name which comparator class does retain power (§3.3 second paragraph).

### §5.3 The three questions each channel row must answer

1. **Is it a wave?** Does a real-$k$ propagating branch exist (band structure / Christoffel
   eigenvalue)? — port-register §0 radiativity condition (i).
2. **Is it sourced?** Does a GW170817-class event's source tensor couple into it (multipole content
   + impedance match)? — condition (ii). Answers inherited from #761/#765 carry their conditionals.
3. **Is it read?** Does a detector in the GW170817 multi-messenger dataset terminate it into a real
   impedance, in band, at the coincidence epoch?

A channel is COMPLIANT-CLEAN only if it runs at $c$, or fails 1, or fails 2. A channel that passes
1, 2 and 3 at $v \neq c$ fires the kill.

## §6 — Conditionals carried from the four mandatory inputs

Each input is re-derived, not trusted; its conditionals carry into any verdict this lane returns.

### §6.1 Two-band k·p (#884, CLEARED) — `research/2026-08-05_two-band-kinematics_result.md`, `clm-2bkp7v`

**Consumed:** the transverse-translational branch sits at $v^2 = G/\rho \equiv c_{EM}^2$ identically
for all moduli, via the cancellation $(G+G_c)/\rho - G_c/\rho$; the longitudinal branch at
$10G/(3\rho)$; the carrier branches at $2\gamma/I_\omega$ and $2\gamma/I_\omega + G_c/\rho$; and
$v^2_\perp - v^2_\parallel = G_c/\rho$.

**Conditionals carried, explicitly:**

- **C1 — scale separation.** That lane's §6 records that the relativistic form's validity window
  closes before its own relativistic regime opens ($k_{break}/k_{rel} \approx 0.39$, $0.42$), and
  the review softened the attribution: the "no scale separation" statement holds only under the
  ADDITIONAL identification gap = Compton. **Consequence for LC-1:** every speed this lane quotes
  is an $O(k^2)$ long-wave coefficient, valid at the astrophysical wavelengths in play
  ($k\ell_{node} \sim 10^{-18}$ at 100 Hz) but NOT a statement about zone-edge transport.
- **C2 — gap identification.** The carrier's gap is the Cosserat sector's own gap; FLAG-1's
  factor-2 tension is closed by A-008 (§6.2) but the identification of that gap with a physical
  pair-threshold remains a corpus reading, not an LC-1 result.
- **C3 — connectivity.** The $O(k^2)$ closed forms are connectivity-INDEPENDENT (G7b: identical on
  $z=6$ cubic, $z=8$ bcc, anisotropic $z=4$), and the review corrected the stated REASON (the
  least-squares gradient's asymmetric piece enters eigenvalues only at $O(k^3)$; `TETRA_OFFSETS` is
  NOT centrosymmetric). **The $O(k^4)$ coefficients and all band-top statements ARE diamond-specific
  and this lane uses none of them.**
- **C4 — the operator runs on the $z=4$ diamond CONTROL net, not the ratified $z=3$ srs production
  carrier** (that lane's FLAG-3; G7a `BLOCKED-STRUCTURAL`, srs bond tensor rank 2). LC-1's $O(k^2)$
  usage is covered by C3; nothing else is.
- **C5 — the 0.612 full-BZ group-velocity figure is a LOWER BOUND** ($\geq 0.6133$ on the audit's
  denser scan), not a point value. LC-1 cites it only as "the carrier manifold's group velocity is
  measured below $c_{EM}$ over the sampled BZ," never as a number.

### §6.2 A-008 factor propagation (#895, CLEARED) — `research/2026-08-05_a008-factor-propagation_note.md`

**Consumed:** BIN `FACTOR-CLOSED-BY-A008` — $E_g = \hbar\omega_m$ (not $2\hbar\omega_m$), numerically
$2m_ec^2 = 1.022$ MeV; and $G_c/I_\omega = 1$ stands (the $1/4$ re-pin is a corpus path closed by
name on the 2026-04-27 adjudication).

**Conditionals carried:**

- **C6 — the single hinge.** That note names one live residue: `l3-electron-soliton-synthesis.md:132`
  states the half-cover direction the other way, against a 14-site witness set. If Grant ruled that
  clause canonical, the A-008 verdict inverts. **Consequence for LC-1:** the gap value would move
  by a factor of 2 or 4. LC-1's use of the gap is a $\sim10^{-19}$ over-determination margin, so
  the Cosserat-channel conclusion is robust to that entire factor range — stated in advance, and
  checked numerically (G-GAPMARGIN, §9).
- **C7 — placeholder moduli.** $G_c$, $I_\omega$, $\gamma$ have no `constants.py` symbols; they are
  engine placeholders. **Consequence:** every carrier-branch speed this lane quotes is
  ENG-CHOICE-conditioned and is reported as a ratio-with-placeholder-tag, never as a substrate
  value.

### §6.3 Kernel-collapse v2 + correction (#905/#907) — the cross-grade combine fence

Handled as an SVA header row in §0.4 rather than buried here. **Declared, not assumed:** the
propagation legs are predicted combine-member-insensitive because every kernel is evaluated at
$S=1$; G-MEMBER tests it; the source-coupling leg is NOT member-insensitive and is inherited.

### §6.4 NO-TWIST (#890) — `research/2026-08-05_srs-twist-coefficient_result.md`

**Does it bind LC-1?** The srs 432 result kills homogeneous strain→rotation coupling, and the arc
brief routes it to LC-2's rotational-channel suppression derivation. **For LC-1 it binds in exactly
one place and is cited there only:** it removes a candidate mechanism by which a merger's
homogeneous strain field could pump the gapped Cosserat channel. That candidate was already dead
by the $\sim10^{-19}$ energy margin, so NO-TWIST is a SECOND, independent reason for the same row —
recorded as over-determination, not as the load-bearing reason.

### §6.5 The banked pulsar exclusion — a PRIOR on a different comparator

`manuscript/ave-kb/common/genesis-chord-falsification-ledger.md`, entry
`q1-reading-A-radiative-bulk-port`, PROMOTED LIVE 2026-07-20. Cited, conditionals carried, **not
re-litigated** (§1.2 non-claim 2). Its own diagnostic already states, verbatim `[sic]`, *"why pulsar
timing is the sharp kill, not the LIGO single event"* — an input this lane must reckon with rather
than rediscover.

## §7 — The bins (frozen, two axes) and the arc-termination rule

The dispatch's frozen kill condition is:

> *an energy-carrying inter-event channel at speed $\neq c$ that a GW170817-class event sources and
> a detector reads $\Rightarrow$ KILL.*

Its phrase **"a detector reads"** admits two readings that give DIFFERENT verdicts on the same
physics, and the pre-test physics check (§0.5) surfaced this to Grant BEFORE the design locked.
This lane does not pick. **Two axes are frozen; both are reported; the arc-termination trigger is
defined explicitly so that no post-hoc reading can move it.**

### §7.1 PRIMARY AXIS — comparator-scoped (LC-1's OWN content; genuinely fireable)

Reading: *"a detector"* = a detector in the GW170817 multi-messenger dataset, in band, at the
coincidence epoch.

| bin | criterion | consequence |
|---|---|---|
| **`A-COMPLIANT-AT-COMPARATOR`** | Every channel the GW170817 detector network can read runs at $c$, AND every $\neq c$ channel is unread by that network with its blocking mechanism NAMED per channel from the six-item vocabulary of §5.2. | The multi-messenger timing bound is satisfied. Classification is EXPECTED CONSISTENCY (§1.2 non-claim 1), not a discriminating survival. **Not arc-terminating.** |
| **`B-KILL-AT-COMPARATOR`** | A $\neq c$ channel is (1) a wave, (2) sourced by this event class, and (3) in-band and antenna-coupled for the GW170817 network at the coincidence epoch. | **ARC-TERMINATING** for LC-2..LC-5 per the arc brief. |
| **`C-NOT-CERTIFIED`** | Any derivation step fails its own self-test (§9), or the $f_{low}$ bracket robustness fails, or a channel row cannot be filled. | Bins become diagnostics; nothing propagates; no arc consequence either way. |

### §7.2 SECONDARY AXIS — inherited-corpus-state (declared ENTAILED at freeze; reported, not adjudicated)

Reading: *"a detector"* = any detector, on any comparator class.

| bin | criterion | consequence |
|---|---|---|
| **`S1-NO-INHERITED-KILL`** | No standing merged corpus state carries a sourced, readable, $\neq c$ inter-event channel. | — |
| **`S2-KILL-INHERITED`** | A standing merged corpus state already carries one, established by a prior lane on a different comparator. | **Recorded for arc bookkeeping. NOT arc-terminating by this lane's own act** — see §7.3. |

### §7.3 The arc-termination rule, frozen

**LC-1 terminates the arc if and only if `B-KILL-AT-COMPARATOR` fires.** `S2-KILL-INHERITED` does
NOT terminate the arc by this lane's action, for a stated reason and not as a softening:

- `S2` is ENTAILED by already-merged inputs (§8). An entailed branch firing is DEMONSTRATED, not
  ADJUDICATED (`ave-prereg` Step 3.10). A lane cannot terminate a five-test arc by re-reading a
  merged ruling.
- Whether a standing exclusion on the pulsar comparator should terminate a multi-messenger arc is a
  FRAMING-level decision about arc scope, which is Grant's, not the implementer lane's (lane
  discipline; `walk-before-execute-on-fence-reach`).
- **Therefore:** if `S2` fires, the result doc states it plainly, at full strength, with receipts,
  and routes the arc-scope question to Grant as an explicit decision — it does not answer it, and
  it does not bury it.

**This is not a rescue clause.** If `S2` fires the framework carries a live closed-negative on its
gravitational-radiation sector, and the result doc must say exactly that in its headline, without
hedging, whatever the primary axis returns.

### §7.4 Reachability audit (frozen; run honestly in §8)

| bin | reachable at freeze? |
|---|---|
| `A-COMPLIANT-AT-COMPARATOR` | **YES** — reachable, and its reachability depends on the §3.3 arrival-kinematics result, which is not known at freeze. |
| `B-KILL-AT-COMPARATOR` | **YES** — fires if the retarded-offset frequency lands inside the detector band, or if any other channel is found in-band at $\neq c$. |
| `C-NOT-CERTIFIED` | **YES** — three named self-tests can fail (§9). |
| `S1-NO-INHERITED-KILL` | **NO — foreclosed by merged inputs at freeze.** Declared, §8. |
| `S2-KILL-INHERITED` | **YES, and ENTAILED.** Declared, §8. |

### §7.5 The dispatch's bin (i) as literally worded — declared UNREACHABLE at freeze

The dispatch's bin (i) reads *"COMPLIANT (all inter-event energy channels at c, or non-c channels
shown gapped/confined/sourceless — state WHICH mechanism per channel)"*. **That bin cannot be
reached**, because merged canon (#761, `research/2026-07-20_mechanical-commonmode-derivation_result.md`
§5, via the Q1 revert) has already FALSIFIED all three of its escape mechanisms for channel 3b:
mode-absence FALSIFIED, derived-cold-emptying FALSIFIED, derived-source-decoupling FALSIFIED.
`A-COMPLIANT-AT-COMPARATOR` is therefore NOT a renaming of the dispatch's bin (i); it is a
comparator-scoped bin with a strictly weaker criterion, and the difference is exactly the
`OUT-OF-BAND-AT-ARRIVAL` mechanism §5.2 adds. **Stated here, at freeze, so that landing
`A-COMPLIANT-AT-COMPARATOR` can never be read as having landed the dispatch's bin (i).**

## §8 — Entailed-branch check, run at freeze

**`ave-prereg` v1.8 Step 3.10.** Before freezing a bin set, flag any branch the model class
MATHEMATICALLY ENTAILS — a monotone objective, an adjudication rule consuming already-merged
inputs, a detector that structurally cannot report one branch. An entailed branch "firing" is
DEMONSTRATED, not ADJUDICATED. Run honestly:

### §8.1 `S2-KILL-INHERITED` is ENTAILED — by an adjudication rule consuming already-merged inputs

Three merged facts on `origin/main` at `d129e7ac`, verified at this worktree HEAD:

1. `manuscript/ave-kb/common/port-register.md` §3, Q1 row: **"★REVERTED 2026-07-20 → Reading-A
   LIVE"**, with standing physics *"Reading A (independent far-field bulk radiative port + O(1)
   coupling)"*.
2. `manuscript/ave-kb/common/genesis-chord-falsification-ledger.md`, entry
   `q1-reading-A-radiative-bulk-port`: **"🔴 PROMOTED LIVE 2026-07-20 — banked-conditional → LIVE
   closed-negative against the gravitational bulk sector"**.
3. `research/2026-07-20_envelope-sector-reduction_result.md`: BIN-1-CONDITIONAL, *"the standing
   Reading-A exclusion + the reverted Q1 ruling STAND on this analysis."*

Given those three, the secondary axis's adjudication rule ("does a standing merged corpus state
carry a sourced, readable, $\neq c$ inter-event channel?") has its answer BEFORE this lane computes
anything. `S2` fires by demonstration. **`S1` is correspondingly unreachable.** Both are declared
here rather than presented as findings.

**This is why §7.3 exists.** A bin that is entailed at freeze cannot be the trigger that terminates
a five-test arc.

### §8.2 What is genuinely fireable

The primary axis is genuinely fireable, and the reason is specific: **its verdict turns on a
quantity nobody in the corpus has computed** — the retarded-epoch frequency of a superluminal
channel from a chirping source at the comparator's distance (§3.3). At freeze that number is
unknown to this lane except as the §4.2 prediction, and the two bins straddle it: if
$f_{GW}(\Delta t)$ lands above $f_{low}$, `B-KILL-AT-COMPARATOR` fires; if below,
`A-COMPLIANT-AT-COMPARATOR` fires. Neither is entailed by any merged input.

The other genuinely fireable items, none of which are entailed:

- The **full Christoffel eigenvalue spectrum** and the multiplicities (§4.1). Predicted two distinct
  eigenvalues; a third would falsify the derivation and land `C-NOT-CERTIFIED`.
- The **$K$-independence** of the superluminal-channel existence (§4.3 prediction 3). This could
  have come out the other way — if $v_L > c$ required $K > G/3$ or similar, the import would be
  load-bearing for the kill and the kill would be import-conditional.
- Whether **$\sqrt2\,c$ is a plane-wave eigenvalue** (§4.3 prediction 2). Its answer NARROWS the
  register's FLAG-A either way.
- The **$f_{low}$ robustness bracket** (G-BAND).

### §8.3 Entailed-branch check on the dispatch's own bin set

The dispatch's bins (i)/(ii)/(iii) also get the check, and the finding is reported rather than
silently worked around:

- **Bin (i) COMPLIANT: NOT FIREABLE** — its three escape mechanisms are all falsified by merged
  inputs (§7.5). A bin whose only route to firing has been closed on `main` is not an adjudicable
  branch.
- **Bin (ii) KILL: FIREABLE, but under the broad reading it is ENTAILED** (§8.1); under the
  comparator-scoped reading it is genuinely fireable (§8.2). This ambiguity is precisely why §7
  splits the axis.
- **Bin (iii) NOT-CERTIFIED: FIREABLE.**

**Consequence, stated at freeze:** the dispatch's three-bin set, taken literally, has exactly one
genuinely-adjudicable bin and one entailed bin. The two-axis structure of §7 is the minimum repair
that leaves a real adjudication for this lane to perform, and it is added ALONGSIDE the dispatch's
bins (which are retained verbatim in §7.5 and scored) rather than replacing them.

## §9 — Gates and self-tests

**UNRUN $\neq$ PASSED. Every gate below is frozen here, before any number exists. A gate that cannot
fail is not a gate, so each carries its own fireability note.**

| # | gate | criterion | can it fail? |
|---|---|---|---|
| **G-SPEC** | the isotropic Christoffel tensor's eigen-spectrum | exactly TWO distinct eigenvalues, multiplicities 1 (long.) and 2 (trans.), for every sampled direction; symbolic result cross-checked numerically on at least five directions including non-axis | YES — a third eigenvalue, or direction-dependence, fails it |
| **G-NU** | Poisson-ratio cross-check | $\nu$ computed from $(3K-2G)/(2(3K+G))$ at $K=2G$ equals the corpus `NU_VAC` symbol to machine precision | YES — a mismatch means the moduli chain is inconsistent with canon |
| **G-KP** | independent re-derivation of the two-band photon cancellation | $v_T^2 = G/\rho$ recovered with $G_c$ cancelling exactly, derived here and matching `clm-2bkp7v`'s closed form | YES — a residual $G_c$ term fails it |
| **G-MEMBER** | combine-member insensitivity (the #905/#907 fence) | every derived propagation speed identical under the per-grade (L∞) member and the normalized-L2-across-grades member, at $S=1$ | YES — any difference fails it and the propagation verdict becomes member-conditional |
| **G-BAND** | $f_{low}$ bracket robustness | the in-band/out-of-band verdict is unchanged for $f_{low} \in [10, 30]$ Hz | YES — a flip inside the bracket lands `C-NOT-CERTIFIED` |
| **G-CHIRP** | chirp-mass assumption robustness | the in-band/out-of-band verdict is unchanged across component-mass ratios spanning the paper's quoted range, i.e. $\mathcal{M}$ varied by at least $\pm15\%$ | YES |
| **G-DIST** | distance robustness | verdict unchanged across the quoted $40^{+8}_{-14}$ Mpc interval | YES |
| **G-GAPMARGIN** | gap-margin over-determination (C6) | the Cosserat-channel DEAD verdict survives multiplying the gap by $1/4$, $1/2$, $2$, $4$ | YES in principle; predicted to pass by $\sim18$ orders of margin, and that margin is REPORTED so the pass is legible as over-determination, not as a tight call |
| **G-CONST** | canonical-source discipline | every physical constant consumed is imported from `ave.core.constants`; zero hard-coded substrate values; asserted by the checker | YES |
| **G-NEG** | negative control | recompute the transverse speed with $K$ set to zero and confirm $v_L \to \sqrt{4/3}\,c \neq \sqrt{2}\,c$, and with $G_c \to 0$ confirm the carrier splitting vanishes — i.e. the instrument reproduces the two known limits before it is trusted on the new one | YES |
| **G-DET** | determinism | double-run digest identical | YES |
| **G-DOC** | number gate | every load-bearing numeral in the result doc re-derived from the shipped JSON by `research/drivers/lc1_one_speed_number_check.py`, with a mutation receipt | YES |

### §9.1 Fireability self-tests (each MUST be demonstrated in the result)

1. **G-SPEC fires** if fed a deliberately anisotropic stiffness tensor (must report more than two
   distinct eigenvalues).
2. **G-BAND fires** if fed a fictitious detector with $f_{low} = 10^{-6}$ Hz (must flip the verdict
   to in-band).
3. **G-DOC fires** under the mutation receipt (perturb each JSON source value; the checker must
   FAIL).

A self-test that does not fire means the corresponding gate is decorative and the lane reports
`C-NOT-CERTIFIED` on that leg rather than claiming the gate passed.

## §10 — Import ledger

Every number this lane consumes, tagged before it is used (`substrate-first-for-numbers`).

| quantity | source | provenance tag |
|---|---|---|
| $c_0$ | `ave.core.constants.C_0` | SI-DEFINITIONAL |
| $\hbar$, $m_e$ | `ave.core.constants.HBAR`, `M_E` | CODATA IMPORT |
| $\ell_{node}$ | `ave.core.constants.L_NODE` | DERIVED from CODATA ($\hbar/m_ec$) |
| $\rho_{bulk}$ | `ave.core.constants.RHO_BULK` | DERIVED from topological primitives ($\xi$, $\mu_0$, $p_c$, $\ell_{node}$) |
| $G_{vac}$ | `ave.core.constants.G_VAC` | **DEFINITIONAL IDENTITY** — assigned as $\rho c^2$; this is leg (a)'s subject |
| $K = 2G$ | `constants.py:769-773` note | **GR-IMPORTED** (PR #261); NOT crystalline, NOT constitutively forced |
| $V_{LONG} = \sqrt{2G/\rho}$ | `ave.core.constants.V_LONG` | derived from the imported $K$; its STATUS as a wave is leg (b3)'s subject |
| $\nu_{vac} = 2/7$ | `ave.core.constants.NU_VAC` | DERIVED from $K=2G$, hence import-conditioned |
| $G_c$, $I_\omega$, $\gamma$ | `cosserat_field_3d.py` pinning | **ENG-CHOICE placeholders**; no `constants.py` symbols exist |
| $E_g = 2m_ec^2$ | A-008 (#895) | FACTOR DERIVED / VALUE IMPORTED (CODATA $m_e$) |
| $M_{tot} = 2.74\,M_\odot$, $D_L = 40$ Mpc, $\Delta t_{obs} = 1.74$ s, the speed interval | §2, retrieved verbatim | **EXTERNAL OBSERVATION IMPORT** |
| $\mathcal{M}$ (chirp mass) | derived in-lane from $M_{tot}$ | DERIVED-FROM-QUOTED-TOTAL-MASS, equal-mass assumption declared |
| $f_{low} = 20$ Hz | §2.3 | **BRACKETED ENGINEERING INPUT** — the lane's weakest comparator input; bracket $[10,30]$ Hz gated by G-BAND |
| interferometer scalar-mode antenna response | standard instrument theory | **IMPORTED, and deliberately OFF the load-bearing chain** — cited as supplementary only |
| $M_\odot$, Mpc, yr | `astropy`-free explicit SI definitions in the driver, printed in the JSON | UNIT-DEFINITIONAL, stated explicitly |

**No substrate value is hard-coded anywhere in this lane** (G-CONST).

## §11 — Flag-don't-fix: raised at freeze, routed, not resolved

All four flags below are raised BEFORE any derivation runs, with both sides quoted, and are routed.
None is resolved here.

### FLAG-LC1-DISPATCH — the dispatch's description of the Q1 row is STALE against `main`

**Dispatch text:** *"the explicitly-OPEN Q1 'does the A1/bulk channel open an independent far-field
radiative port for gravitating sources?'"*

**`manuscript/ave-kb/common/port-register.md` at this worktree HEAD**, frontmatter, verbatim
`[sic]`: *"Q1 is a RULED row — REVERTED 2026-07-20 to Reading-A-live: the make-or-break mechanical
common-mode derivation returned NONE-DERIVES (#761 merged @ caa51c17), firing the row's own clause,
so the RULED-CONDITIONAL Reading-B reverts and the independent-radiative-port exclusion is live
against the framework (was: explicitly-OPEN, adjudication-pending)."*

**Q1 has been ANSWERED (against the framework) since 2026-07-20.** The dispatch, and the arc brief's
LC-1 row (*"bulk $\sqrt{10/3}c$ P-wave observability — gapped, confined, or sourceless?"*), both
presuppose an open question with three available answers. All three were falsified by #761 before
the arc brief was written on 2026-08-04, and the 2026-08-06 dated currency update did not catch it.
**Raised, not fixed. Routed to Grant + auditor lane as an arc-brief currency finding.**

### FLAG-LC1-A — the FLAG-A two-column split may be a wave-vs-not-a-wave split, not two waves

The register resolves the channel-3 speed confusion structurally by carrying two columns and states,
verbatim `[sic]`: *"**Both superluminal** ⇒ the causality/observability consequences are robust to
the fork; only the exact flux prefactor moves."* If step b1 finds the isotropic acoustic tensor has
no eigenvalue at $K/\rho$, then the two columns are not two waves and the "both superluminal" gloss
is describing one wave and one impedance quantity. **This would NARROW FLAG-A, not overturn it** —
and the register's own §4 already records *"Owed: an auditor-lane band-map channel-3 speed-label
reconciliation."* Routed there. **No register edit by this lane** (KEEP-BOTH).

### FLAG-LC1-B — a live corpus contradiction on A1 free-space radiativity, on this lane's crux channel

Two canon leaves make opposite claims about whether the A1 / V-sector longitudinal grade radiates in
cold free space:

- `manuscript/ave-kb/common/physics-lineage-map.md:63`, verbatim `[sic]`: *"AVE evades by sector
  assignment, claiming **no longitudinal photon** (the A1 grade is non-radiative in free space,
  re-engaging only inside saturation ...). The gapped/confined status is simultaneously the evasion
  and the exposure: any mechanism coupling the A1 bulk mode to EM detectors below saturation walks
  back into these bounds."*
- `manuscript/ave-kb/common/port-register.md` §3 Q1 (standing), via #761 §5: the A1-dilatation rides
  the **gapless** P-branch, the binary drives it at quadrupole order, and the port is **OPEN** —
  Reading-A LIVE.

**These cannot both be read at face value.** The most likely reconciliation is that "A1" names TWO
objects — the EM-scalar grade (Gauss-constrained; no propagating longitudinal EM wave, which is the
Goldhaber–Nieto-relevant statement) and the MECHANICAL A1 dilatation (the elastic P-wave, which is
what radiates) — but the corpus's own vocabulary node `def-9a4f07` currently IDENTIFIES them,
reading the V-sector scalar as *"'the 3' in its A1 dilatation-MASS sense."* **This lane surfaces the
contradiction with both paths and does not pick.** It is directly LC-1-relevant because an
interferometer reading a scalar GW polarization is a mechanical channel read out optically — the
exact configuration `physics-lineage-map.md:63` warns about. Routed to Grant (sector-ownership
adjudication) + auditor lane. **No leaf edited.**

### FLAG-LC1-C — are port-register channels 1 and 2 the same branch?

Both are $T_2$, both transverse-$u$, both at $c$, but they carry different impedances
($Z_{EM} = Z_0$ vs $Z_{shear} = \rho c_{shear}$) in different unit systems. If they are ONE
Christoffel eigenbranch read through the TKI transducer in two conjugate variable pairs, then
$c_{GW} = c_{EM}$ is an IDENTITY and LC-1(a)'s answer is trivially exact — which is the strongest
possible compliance statement AND the weakest possible discrimination statement, simultaneously. If
they are two branches, the corpus owes a degeneracy mechanism. **Raised; the result reports what
canon says and routes the question. This lane does not decide it, and its verdict is constructed so
as not to depend on the answer** (either way, both channels are at $c$).

### FLAG-LC1-D — the messenger this lane cannot assign to a channel

Neutrinos. A BNS merger is a copious neutrino source; the GW170817 neutrino searches returned nulls,
so nothing moves for THIS comparator. But the enumeration frame (§5.1) requires every messenger to
be assigned to a channel, and **the corpus does not establish the limiting speed of a bound matter
excitation in a medium whose longitudinal eigenspeed exceeds its transverse one.** If matter is
A1-dilatation-owned (canon) and the A1 channel's wave speed is $1.83c$, the question "what is a
free-streaming massive soliton's limiting speed" is live and UNDERIVED. **Enumerated as its own row,
tagged UNDERIVED, routed as a follow-on lane.** It is NOT folded into this lane's verdict, and no
speed is guessed for it.

## §12 — Adjudication routing, and what this lane does NOT license

### §12.1 What propagates on which outcome

| outcome | what propagates |
|---|---|
| `A-COMPLIANT-AT-COMPARATOR` | Nothing to canon automatically. The result doc records the compliance at EXPECTED-CONSISTENCY grade and the per-channel mechanism table. LC-2..LC-5 proceed. |
| `B-KILL-AT-COMPARATOR` | Nothing to canon automatically. Grant is handed an arc-termination decision with the full derivation and the comparator citation. |
| `C-NOT-CERTIFIED` | Nothing. Bins become diagnostics; the failing self-test is named and the repair specified. |
| `S2-KILL-INHERITED` (in any combination with the above) | Nothing to canon. The standing state is REPORTED verbatim with receipts, and the arc-scope question is routed to Grant per §7.3. |

### §12.2 The fence on this lane's own result — what it does NOT license

1. **No register edit, no ledger edit, no ruling edit, no claim-card edit, no solidity change, no
   `clm-`/`def-` mint.** Whatever this lane finds about Q1, FLAG-A, or the A1-radiativity
   contradiction is a routed finding for the auditor lane to land, per lane discipline.
2. **No re-opening or re-closing of Q1.** LC-1 may NARROW Q1 by supplying derived facts; the row's
   status is Grant's.
3. **No arc termination by this lane's own act** unless `B-KILL-AT-COMPARATOR` fires (§7.3).
4. **No LC-2..LC-5 content.** Dispersion, anisotropy, birefringence and form-factor statements are
   out of scope even where this lane's channel table is their input.
5. **No "AVE-distinct", "STRONG", "chord", or "discriminating" language on any compliant outcome**
   (§1.2 non-claim 1; `ave-discrimination-check` pre-run).
6. **No statement about the electron, the rest mass, the value of $c$, or the correctness of the
   K=2G import.**
7. **No claim that the arrival-kinematics mechanism rescues anything.** It is a comparator-power
   statement and must be labelled as one every time it appears (§5.2).

### §12.3 Where this lane's questions go

- **Grant:** the §0.5 plumber question (which reading of "observability" the frozen kill condition
  takes); the §7.3 arc-scope decision if `S2` fires; FLAG-LC1-B's sector-ownership adjudication;
  FLAG-LC1-DISPATCH's arc-brief currency.
- **Auditor lane:** FLAG-LC1-A (the FLAG-A narrowing + the owed band-map channel-3 speed-label
  reconciliation); FLAG-LC1-B's leaf-level repair once adjudicated; FLAG-LC1-C.
- **A follow-on lane:** FLAG-LC1-D (limiting speed of a bound matter excitation).

### §12.4 SVA pilot log (this lane's per-row fill experience)

To be completed in the result doc §-final, per `standard-vacuum-analysis.md` §3: each of the eleven
rows scored FILLED / FILLABLE-BUT-MISSING / NOT-APPLICABLE, with any gap logged as a dated
amendment candidate. **This lane does NOT canonize the SVA leaf.**

---

**FREEZE.** This document is committed and pushed ALONE, before any derivation text, any driver
code, any JSON, and any number produced by this lane exists.
