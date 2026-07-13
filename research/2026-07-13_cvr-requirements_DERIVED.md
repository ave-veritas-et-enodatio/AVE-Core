# CVR Bench — Requirements / Derived Boundary-Conditions Datasheet

**Date:** 2026-07-13 · **Lane:** CVR dielectric-C-V bench (implementer) · **Status:** DERIVED requirements datasheet; NOT canonized. Requirements are physics-set; every design CHOICE lives in the sibling trade-study (STATUS:OPEN).

**Sibling docs.**
- `research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md` — the OPEN make-vs-buy + design-knob decision-space (STATUS:OPEN throughout; SELECTS NOTHING; cost out of scope). Derived physics is HERE; choices are THERE.
- Ratified prediction leaf this datasheet specs the bench against: `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:25-38` (the transverse-T2 roll-off / tangent / 1/√2 NDC; ruling chain PR#562/#558, Grant-ratified 2026-07-06/07).
- Structural template: the CLEAVE-01 doc set (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md`, `…/cleave-01-trade-study-decision-register.md`, `…/project-cleave-01.md`). This datasheet copies its single-source-of-truth REQ-ID discipline (`cleave-01-requirements-boundary-conditions.md:43`) and its corroborative-null rescope (`project-cleave-01.md`).

> **★ OPEN DECISION FOR GRANT — KB chapter home.** These CVR docs live in `research/` for now. The natural KB home is Vol-4 (either `vol4/falsification/ch11-experimental-bench-falsification/` alongside CLEAVE-01, or `vol4/circuit-theory/ch1-vacuum-circuit-analysis/` alongside `cvr-dc-operating-point.md`). Chapter placement + whether the requirements leaf becomes a `clm-*` claim vs a `no-claim` consolidation leaf is flagged OPEN — not decided here.

---

## PAGE ONE — the binding epistemic frame (`CVR-REQ-FRAME`)

**This frame BINDS every requirement below. Read it first; it decides what the bench can and cannot claim.**

The CVR (across-gap dielectric C-V) bench is honestly THREE things, and nothing more:

1. **A VALIDATION-LADDER + MATERIAL-ANALOG SHAPE BENCH.** It confirms the universal saturation-kernel SHAPE $S(A)=\sqrt{1-A^2}$ — the tangent roll-off, the $1/\sqrt2$ negative-differential-capacitance (NDC) snap-back, the flat-in-$f$ character — on a *known saturable material varactor* at the calibrated material scale (the cRIO prereg's own verdict, `research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md:165-170`: a "validation-ladder + material-analog consistency bench", "separable in shape only"; the "known saturable dielectric first" framing is `research/2026-07-08_sve-vacuum-network-ee-analysis.md:68`). It NEVER measures $\ell_{node}$ itself (that is a calibration import, circular by construction) and NEVER reaches the *vacuum's* own kernel at bench fields.

2. **A ONE-SIDED ANOMALY BOUND (corroborative-null class).** The form axes below classify any *resolved* $E^2$-even residual as fixture-vs-anomaly — CLEAVE-01-corroborative-null style (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md:40-61,131-151`, `clm-clvchn` NULL-CONFIRMED-FINAL → a positive REOPENS, never confirms). A clean null is the expected result and *bounds* an anomalous coefficient; it does not confirm AVE.

3. **NOT an AVE-confirming channel.** At bench fields the lattice's own conjunction-passing signal is $\delta C/C \sim 10^{-17}$ (see the magnitude verdict below) — unreachable. **Any conjunction-passing residual at bench magnitude falsifies AVE *and* QED alike** — both predict a flat, linear vacuum at these fields. A bench-magnitude {negative-sign ∧ $d^{-2}$ ∧ flat-in-$f$} residual is therefore a *falsifier for both frameworks*, not a discriminating chord for AVE.

**★ The magnitude route is DEAD — three independent verified ways (do not attempt a magnitude rescue):**

| # | Route | Verdict | Receipt (verified this branch) |
|---|---|---|---|
| 1 | Per-node conflation (the PONDER-05 invariant) | $A_0 = V_{DC}/V_{yield}$ is a PER-NODE ratio; across real 10–100 µm gaps $A_0 \sim 10^{-8}$–$10^{-10}$ → $\delta C/C \approx -\tfrac12 A_0^2 \sim 10^{-17}$, ~8 OOM below any lock-in floor | `manuscript/ave-kb/common/translation-tables/translation-circuit.md:111` ($V_{DC}/V_{yield}$ per-node, vacuum $A_0 \sim 10^{-7}$–$10^{-10}$); `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 |
| 2 | cRIO regime verdict | vacuum claim NOT separable — unreachable by **~20 OOM**; the bench sits **~9 OOM below** even the linear→nonlinear knee $R_I=\sqrt{2\alpha}=0.12$ (DEEP Regime I) | `research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md:165` (~20 OOM), `:193` (~9 OOM below $R_I=0.12$) |
| 3 | Vacuum tangent zero-crossing | the vacuum's own NDC zero-crossing is at **30.87 kV across a single $\ell_{node}$** = a Schwinger-scale field, NOT bench-reachable | `research/2026-07-08_sve-vacuum-network-ee-analysis.md:69` |

> **⚠ FLAG-DON'T-FIX (cite-verification, surfaced not fixed).** The walk card also listed a *"piezo fourth-transducer `:102-107`"* as a fourth magnitude-dead receipt. It **did NOT verify** at `project-cleave-01.md:102-107` (that range is the spatial/power/temporal regime-classification table, not a piezo-transducer analysis) nor anywhere in the cRIO prereg (no "piezo"/"fourth-transducer" string). **Substituted the verified per-node-conflation route (#1 above) so the "dead three ways" claim stands on three receipts that all verify.** Surfaced for the auditor lane.

**AC/DC-carve license (why this qualifies as a discriminating-test class at all).** CVR is the sibling instrument of the banked E-route vacuum birefringence (`clm-pp3qwf`, `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`): identical DC ε-varactor operating point, an LCR AC-capacitance channel instead of the laser-index channel — a DC→AC coupling-class test (`manuscript/ave-kb/common/claim-quality.md:1368` clm-acdc07, selection rule (iv) `:1378`). **Caveat (iii) `:1377`: AC agreement is consistency-only; the distinctive content is the SIGN + the $1/\sqrt2$ NDC snap-back, which the incumbent (QED) does not predict — and both are magnitude-dead at the bench, hence the corroborative-null / anomaly-bound framing above.**

**Discipline classification (per `consistency-vs-emergence`).** The kernel SHAPE the material-analog ladder confirms is CONSISTENCY-class (network-topology + Ax-4 kernel-argument identity; no new dimensionful number minted — mirrors `manuscript/ave-kb/vol4/claim-quality.md:1846` "FORM-level derivation / CONSISTENCY class"). The vacuum $E_{yield}=1.13\times10^{17}$ V/m scale is EMERGENCE-class but is *not measured here* (magnitude-dead). **No requirement below may be read as gating an emergence-class AVE-confirmation.**

---

## REQ-ID INDEX — the canonical CVR requirement identifiers

**These `CVR-REQ-<NAME>` identifiers are the canonical, stable CVR requirement IDs** (copying the CLEAVE-01 single-source-of-truth rule, `cleave-01-requirements-boundary-conditions.md:43`: descriptive, reorder-proof, each names the physics object it constrains — NOT a section number). Where a requirement *inherits* a CLEAVE-01 boundary condition, this datasheet **cites the `CLV-REQ-*` ID by reference and does NOT duplicate the derived number** (single-source-of-truth: the CLEAVE requirements leaf owns those). Stamping an ID changes no derived number and selects no design knob.

| REQ-ID | One-line requirement | Class |
|---|---|---|
| `CVR-REQ-FRAME` | The binding epistemic frame: validation-ladder + material-analog shape bench + one-sided anomaly bound; corroborative-null class; magnitude-dead three ways; NOT AVE-confirming | frame (binding) |
| `CVR-REQ-BIAS` | Bias/field: no achievable bias makes the vacuum bound bite → the requirement is CLASSIFIER-driven, kV-class across 10–100 µm gaps so every fixture systematic is fully resolved + the material-analog ladder has strong signal | physics-set + classifier |
| `CVR-REQ-STANDOFF` | HV C-V topology: sense node at virtual ground; DC never threads the sense path; the blocking/coupling element's own $C(V)$ is Class-I/vacuum/air-gap OR topologically excluded from the sense path; standoff-network calibration-stability | topology BC |
| `CVR-REQ-FIELDVOL` | Class-I / vacuum-spacer ONLY in the DC field volume; Class-II ceramic is the one sign-degenerate confound (its own negative-going $C(V)$) — excluded from the field volume | physics-set |
| `CVR-REQ-FIXTURE` | Fixture stiffness derived from the $d^{-3}$ subtraction requirement: pull-in characterized BEFORE data runs (knowing $k$ converts electrode attraction from confound to subtraction); gap sweep $\ge4\times$ at fixed $V$, holder unchanged; log-log $d$-power slope resolution $\sim0.1$ | physics-set + design |
| `CVR-REQ-ACQ` | Acquisition: in-phase/quadrature separation of the $E^2$-even response; 3–4 SIMULTANEOUS probe tones across DC–40 kHz in one acquisition (sequential runs let drift fake dispersion on the flatness axis); mandatory INCONCLUSIVE bin | acquisition BC |

**Inherited CLEAVE-01 requirements (cited by ID, NOT duplicated):** `CLV-REQ-VALIDATE` (validate-on-known / anti-false-null positive control, `cleave-01-requirements-boundary-conditions.md:62`) applies unchanged — inject a known even-in-$V$ residual and confirm the chain resolves it before trusting any null. The mandatory INCONCLUSIVE outcome bin is the bench-model-spine discipline (`src/ave/bench/model.py:355,372-374`), shared by every AVE bench prereg.

---

## §1 — `CVR-REQ-BIAS` — the bias/field requirement is CLASSIFIER-driven, not magnitude-driven

**The canonical scale (verified).** $E_{yield} = V_{yield}/\ell_{node} \approx 1.13\times10^{17}$ V/m (`src/ave/core/constants.py:516`, `E_YIELD = V_YIELD / L_NODE`; with `V_YIELD:505` $\approx43.65$ kV and `V_SNAP:496` $\approx511$ kV). This is the field at which the *transverse-T2* vacuum dielectric rolls off; it is a per-$\ell_{node}$ field and is unreachable at the bench (`CVR-REQ-FRAME`, magnitude route dead).

**Why no achievable bias makes the vacuum bound bite (reproduce the arithmetic).** Define an anomalous even-in-$V$ capacitance coefficient $\kappa$ via
$$
\frac{\delta C}{C} = \kappa\left(\frac{E}{E_{yield}}\right)^2 .
$$
A bench with a fractional-capacitance resolution floor $\Phi$ can only *bound* $\kappa$ to
$$
|\kappa| < \frac{\Phi}{(E/E_{yield})^2}.
$$
Take a representative strong bench point — $E = 10\ \text{kV}/100\ \mu\text{m} = 1\times10^{8}$ V/m — and a good lock-in fractional floor $\Phi = 1\times10^{-8}$:
$$
\frac{E}{E_{yield}} = \frac{1\times10^{8}}{1.13\times10^{17}} = 8.85\times10^{-10},
\qquad \left(\frac{E}{E_{yield}}\right)^2 = 7.83\times10^{-19},
$$
$$
|\kappa| < \frac{1\times10^{-8}}{7.83\times10^{-19}} \approx 1.3\times10^{10}.
$$
The lattice's own coefficient is $\kappa = -\tfrac12$ (chord) / $-\tfrac32$ (tangent) — see §6. The bench bound ($\sim10^{10}$) is **~10 orders of magnitude looser** than the lattice value it would need to detect. **No achievable DC bias closes that gap** (the deficit is $(E/E_{yield})^2$, quadratic in the unreachable field ratio). The vacuum bound does not bite at any bench field — confirming `CVR-REQ-FRAME`.

**Therefore the bias requirement is CLASSIFIER-driven, not magnitude-driven.** Since the vacuum kernel is unreachable, the bias is specified to serve the *material-analog ladder* + the *anomaly-bound classifier*:

- **kV-class DC bias across 10–100 µm gaps.** This (a) drives a real saturable-material varactor deep enough that the kernel SHAPE (roll-off, $1/\sqrt2$ NDC, flat-in-$f$) has strong signal for the validation ladder, and (b) makes every even-in-$V$ *fixture* systematic large enough to be fully resolved and CLASSIFIED rather than buried at the floor.

- **The dominant fixture systematic, reproduced honestly — electrode electrostatic attraction.** The plates attract, the gap closes, $C=\varepsilon_0 A/d$ rises. With gap-holder stiffness $k$ the fractional response is
$$
\frac{\delta C}{C} = +\frac{\varepsilon_0 A\,V^2}{2\,k\,d^{3}}.
$$
At $A = 1\ \text{cm}^2 = 1\times10^{-4}$ m², $d = 100\ \mu\text{m} = 1\times10^{-4}$ m, $k = 1\times10^{6}$ N/m:
$$
\frac{\varepsilon_0 A}{2 k d^{3}} = \frac{(8.854\times10^{-12})(1\times10^{-4})}{2(1\times10^{6})(1\times10^{-4})^{3}} = \frac{8.854\times10^{-16}}{2\times10^{-6}} \approx 4.4\times10^{-10}\ \text{per V}^2 .
$$
So $\delta C/C \approx 4.4\times10^{-10}\,V^2$ — i.e. $\approx4.4\times10^{-4}$ at 1 kV and $\approx4.4\times10^{-2}$ at 10 kV. At kV-class this is a **large, fully-resolvable, positive-sign, $d^{-3}$-scaling** term — exactly the property `CVR-REQ-FIXTURE` exploits: at kV-class the systematic is not a floor-level nuisance but a *characterized, subtractable, differently-signed, differently-gap-scaling* object.

**Bias requirement (stated):** DC bias tunable to **kV-class** (0.1–10 kV) across a **10–100 µm** gap, with polarity irrelevant to the physics (the response is $E^2$-even — see the route-asymmetry note in §5), chosen so that (i) the material-analog kernel SHAPE has strong signal and (ii) every $E^2$-even fixture systematic sits well above the acquisition floor for classification. **No bias target is set to "reach" the vacuum kernel — that is physics-dead.**

## §2 — `CVR-REQ-STANDOFF` — HV C-V topology: sense node at virtual ground

**The circuit picture (the plumber question, made a requirement).** A kV-class DC bias is held across the gap from an external HV supply; a 40 kHz (and 3–4 simultaneous tones, `CVR-REQ-ACQ`) probe rides on top; the front end reads the AC current back. The ±10 V-class sense front end (e.g. a cRIO AI or a transimpedance amp) cannot see the kV — so the HV must **stand off** from the sense node. The topology requirement is derived from where that standoff lives:

1. **Sense node at virtual ground; DC never threads the sense path.** The gap-under-test AC current is read at a virtual-ground summing node (transimpedance) so the sense-path DC potential is $\approx0$ and the kV is dropped across the bias/blocking network, not across the front end. This is a *topology boundary condition*, not a tolerance: a bare high-impedance node biased to kV is not an option.

2. **The blocking/coupling element's OWN $C(V)$ is the named care point.** Whatever element stands the kV off from the virtual-ground node (series blocking cap, or a bias-tee coupling cap) sits **directly in series with the signal**. Its own voltage-coefficient-of-capacitance is an $E^2$-even, potentially $f$-structured confound that is *degenerate on the sign axis with the lattice prediction* (a Class-II ceramic $C(V)$ sags negative under bias — the same sign as the lattice tangent roll-off). A "soaky" (dielectric-absorption-heavy) coupling cap adds an $f$-structured even-in-$V$ term on the flatness axis. **Requirement:** the blocking/coupling element in the sense path is EITHER Class-I (C0G/NP0, vacuum-gap, or air-gap — linear $C(V)$ to $\ll$ the acquisition floor) **OR** topologically excluded from the sense path (e.g. bias injected on the driven electrode so the blocking element sees no signal current). This mirrors `CVR-REQ-FIELDVOL`: the one dielectric the signal path may thread is Class-I.

3. **Standoff-network calibration stability.** The bias-tee / bleed-resistor / blocking-cap network's transfer function must be calibration-stable across the DC sweep and across the multi-tone acquisition window: any drift in the standoff network's insertion phase/gain masquerades as a change in the gap $C(V)$. **Requirement:** the standoff network transfer function is characterized and stable (its $C(V)$ and $D(V)$ tracked) across the full bias range and the acquisition window, to below the `CVR-REQ-ACQ` per-tone floor; a stability failure books as INCONCLUSIVE, not as a gap-$C(V)$ signal.

**Inherited discipline:** the `CLV-REQ-VALIDATE` positive control (`cleave-01-requirements-boundary-conditions.md:62`) is the anti-false-null guard here too — inject a known even-in-$V$ series-capacitance step at the gap node and confirm the chain (through the standoff network) resolves it before trusting any measured $C(V)$.

## §3 — `CVR-REQ-FIXTURE` — stiffness from the d⁻³ subtraction; gap sweep ≥4× at fixed V

**The load-bearing form axis: gap-power ($d$-power).** This is the CVR analog of the CLEAVE-01 fixed-$C_{in}$ gap-independence sweep (`project-cleave-01.md:80,89`). At fixed $V$:

- **Lattice term** — $A = E/E_{yield} = V/(d\,E_{yield})$, so $\delta C/C = \kappa\,(V/(d\,E_{yield}))^2 \propto V^2\,d^{-2}$ (negative sign; $\kappa<0$, §6).
- **Electrode-attraction term** — $\delta C/C = +\varepsilon_0 A V^2/(2 k d^{3}) \propto V^2\,d^{-3}$ (positive sign, §1).

**One full power of separation** ($d^{-2}$ vs $d^{-3}$) on a fixed-$V$ log-log gap sweep, orthogonal to the sign axis, and it respects the PONDER-05 invariant (keyed on the FIELD $E=V/d$, not on per-node access). This gap-power leaf has **no prior corpus site** — it is a genuinely un-written requirement (the two-method absence check in the walk card found no $1/d^3$ / electrode-attraction leaf in `manuscript/` or `research/`); it is assembled here.

**(3.1) Stiffness spec — derived FROM the $d^{-3}$ subtraction.** To subtract the electrode $d^{-3}$ term rather than merely fear it, the gap-holder stiffness $k$ must be (a) high enough to stay far below pull-in at max bias, and (b) KNOWN. Parallel-plate electrostatic pull-in (snap-together) occurs at a fractional gap closure $\delta d/d = 1/3$, at
$$
V_{PI} = \sqrt{\frac{8\,k\,d_0^{3}}{27\,\varepsilon_0 A}} .
$$
At $A=1\ \text{cm}^2$, $d_0=100\ \mu\text{m}$, $k=1\times10^{6}$ N/m: $V_{PI} = \sqrt{8(10^{6})(10^{-4})^{3}/[27(8.854\times10^{-12})(10^{-4})]} \approx 1.83\times10^{4}$ V $\approx 18.3$ kV, so $V_{PI}/2 \approx 9.1$ kV. At a **9 kV** max bias (satisfying $V_{max}\lesssim V_{PI}/2$) the gap closure is $\delta d/d = \varepsilon_0 A V^2/(2 k d^3) = 4.4\times10^{-10}(8.1\times10^{7}) = 3.6\%$ — comfortably below the $1/3$ pull-in threshold, keeping the $d^{-3}$ term a clean leading-order object. **Requirement:** $k$ chosen so $V_{max} \lesssim V_{PI}/2$ AND $\delta d/d \lesssim$ few-% at $V_{max}$. (Reaching the §1 illustrative 10 kV at this gap needs a stiffer fixture, $k\gtrsim1.2\times10^{6}$ N/m so $V_{PI}\gtrsim20$ kV and $V_{PI}/2\gtrsim10$ kV — the stiffness spec scales with the target max bias.)

**(3.2) Pull-in characterized BEFORE data runs (the confound→subtraction conversion).** Measure the actual pull-in voltage $V_{PI}$ of the assembled fixture *before* any $C(V)$ data run. $V_{PI}$ pins $k$ (via the formula above, at known $A,d_0$); knowing $k$ turns the electrode $d^{-3}$ term from an unquantified confound into a *computed, subtractable* term (its coefficient $\varepsilon_0 A/(2kd^3)$ is then fully determined). **The snap-in IS the $d^{-3}$ systematic announcing itself** (the plumber's "have you ever measured your fixture's pull-in?"). This is a mandatory pre-run characterization, not an optional check.

**(3.3) Gap sweep $\ge4\times$ at fixed $V$, holder unchanged.** Sweep the gap over a $\ge4\times$ geometric span (e.g. $d_0 \to 4d_0$, or $[d_0/4, d_0]$), $\ge4$ points, **at fixed $V$, with the holder/fixture unchanged** so $k$, $A$ and parallelism are constant and $d$ is the only variable. (The CLEAVE fixed-$C_{in}$ analog: the moving element must not change what holds it — `cleave-01-requirements-boundary-conditions.md:55` `CLV-REQ-CFIX`.)

**(3.4) Log-log $d$-power slope resolution (per-point precision derived).** Fit the log-log slope $s = d\ln(\delta C/C)/d\ln d$ of the resolved $E^2$-even residual; the lattice ($s=-2$) and electrode-attraction ($s=-3$) differ by $\Delta s = 1$, so a slope resolution $\sigma_s \le 0.1$ (10% of the separation) cleanly assigns the power. For $N$ geometrically-spaced points over a span $R = \ln(d_{max}/d_{min})$, the least-squares slope error is $\sigma_s = \sigma_y/(R\sqrt{N/12})$ where $\sigma_y$ is the per-point precision in $\ln(\delta C/C)$ (i.e. the *fractional* precision on $\delta C/C$). Solving for the per-point precision at $\sigma_s = 0.1$, $R = \ln 4 = 1.386$:
$$
\sigma_y \le 0.1\,R\,\sqrt{N/12} = \{0.080\ (N{=}4),\ 0.10\ (N{=}6),\ 0.12\ (N{=}9)\}.
$$
**Requirement:** per-point fractional precision on the resolved even-in-$V$ residual $\lesssim 8$–$12\%$ (i.e. $\sim10\%$) across the $\ge4\times$ sweep. This precision is on the *resolved* residual, which requires the residual to sit well above the `CVR-REQ-ACQ` floor — the reason `CVR-REQ-BIAS` specifies kV-class (it lifts both the material-analog signal and the electrode systematic well above the floor so the $d$-power fit has SNR).

## §4 — `CVR-REQ-FIELDVOL` — Class-I / vacuum spacer ONLY in the DC field volume

**The SIGN axis and its one degenerate confound.** The lattice transverse-T2 permittivity SAGS under bias → $\delta C$ is NEGATIVE (`dielectric-plateau-prediction.md:27,38` — "the sign of the deviation" is the named discriminating signature; the C↔ε same-sign monotonicity lemma is ratified at `research/2026-06-15_ceff-epsilon-monotonicity_result.md:20,81`). The dominant *geometric* systematic — electrode attraction (§1) — is POSITIVE-signed. So sign anti-correlates the two: a signed discriminator, not a magnitude race.

**But sign alone does not close the case.** A Class-II ceramic support dielectric has its own negative-going voltage-coefficient-of-capacitance, and electrostriction can also read negative — **both degenerate with the lattice on the sign axis.** This is the ONE confound that survives the sign discriminator. (The even-route confound inventory has no prior corpus leaf; it is written here.)

**Requirement:** the ONLY dielectric the DC field volume threads is **Class-I (C0G/NP0) or vacuum/air-gap spacer** — linear $C(V)$ to well below the acquisition floor. **No Class-II ceramic anywhere in the DC field volume.** This is the sign-axis analog of `CVR-REQ-STANDOFF` item 2 (the sense-path blocking element): the two together guarantee the only voltage-dependent dielectric in either the field volume or the sense path is Class-I, so a resolved negative-sign residual cannot be a support-dielectric or blocking-cap $C(V)$ artifact. With this met, the negative sign becomes a live discriminator; without it, sign is uninformative.

## §5 — `CVR-REQ-ACQ` — I/Q separation + 3–4 simultaneous probe tones + mandatory INCONCLUSIVE bin

**Why the acquisition must stack THREE axes (the even-route asymmetry — written nowhere in the corpus).** The lattice sag is **even-in-$V$**, so it is polarity-DEGENERATE with every even fixture systematic (electrostriction $\propto V^2$, electrode attraction $\propto V^2$, Class-II support $C(V)$, coupling-cap $C(V)$). **The CLEAVE-01 polarity-reversal trick is therefore UNAVAILABLE to this even route** — CLEAVE's chord is displacement-ODD and rejects even fakers by symmetry (`cleave-01-requirements-boundary-conditions.md:119`, the even-in-$V$ faker table); CVR has no such single-flip lever. The discrimination must instead STACK the three orthogonal form axes, no one of which any single classical mechanism survives:

- **SIGN** (`CVR-REQ-FIELDVOL`, §4): lattice negative vs electrode-attraction positive; degenerate confounds excluded by Class-I-only.
- **GAP-POWER** (`CVR-REQ-FIXTURE`, §3.4): lattice $d^{-2}$ vs electrode-attraction $d^{-3}$.
- **FLATNESS-in-$f$** (this section): the kernel is memoryless/dispersionless to $\omega_C \approx 7.7\times10^{20}$ rad/s (driver-confirmed flat, `manuscript/ave-kb/vol4/claim-quality.md:1849`, $\max_{\rm rel} = 2.0\times10^{-16}$, no $(\omega/\omega_C)^2$ factor), while fixture systematics are $f$-structured (spring-mass resonances kHz–MHz, PZT log-creep over seconds, Debye/dielectric-absorption relaxation) — all inside DC–40 kHz reach.

The non-fakeable object is the TRIPLE CONJUNCTION {negative-sign ∧ $d^{-2}$ ∧ flat-in-$f$}. Per `CVR-REQ-FRAME`, at bench magnitude this conjunction is ~$10^{-17}$ and unreachable — so the acquisition's job is to *classify any resolved $E^2$-even residual* against this conjunction (fixture-vs-anomaly), not to detect the lattice.

**(5.1) In-phase / quadrature separation of the $E^2$-even response.** The acquisition must resolve the in-phase (capacitive, $\delta C$) from the quadrature (loss/creep, $\delta D$) component of the $E^2$-even response. The lattice is anhysteretic/lossless (Ax3) → an in-phase-only even response; a quadrature even component is a loss/creep/soakage fixture signature. **Requirement:** I/Q demodulation at each probe tone, capacitive and loss channels reported separately. *(Open fence: the anhysteretic claim is gated by the SPICE constitutive-loop prereg `research/2026-06-13_spice-cvr-constitutive-loop_prereg.md` §0.1, pinched/$B_r=0$ hysteresis — cite, do not assume closed.)*

**(5.2) 3–4 SIMULTANEOUS probe tones across DC–40 kHz in ONE acquisition.** The flatness axis needs the $E^2$-even response as a function of $f$ in a *single thermal environment*: **sequential single-tone runs let drift fake dispersion**, contaminating the flatness discriminator with a thermal/1-f trend. **Requirement:** 3–4 probe tones spanning DC–40 kHz acquired simultaneously in one phase-coherent acquisition (the cRIO 4×4 phase-coherent bench is the natural fit — recorded as a candidate in the trade study, not selected here).

**(5.3) Mandatory INCONCLUSIVE bin.** Per the bench-model spine, every CVR prereg must carry an explicit INCONCLUSIVE outcome bin (`src/ave/bench/model.py:355` "MUST include an INCONCLUSIVE bin"; enforced by `has_inconclusive_bin` at `:372-374`), and any magnitude expectation must carry a dimensional eval from canonical primitives (`DimensionalIngredient`, `:320-332`). A standoff-network instability, an unresolved residual, or a failed `CLV-REQ-VALIDATE` positive control books INCONCLUSIVE — never a gap-$C(V)$ signal and never a false null.

> **⚠ Cite-correction (flag-don't-fix).** The walk card located the mandatory-INCONCLUSIVE-bin at `src/ave/bench/model.py:320-332`. Verified this branch: `:320-332` is the `DimensionalIngredient` dataclass (the magnitude-eval requirement); the INCONCLUSIVE-bin enforcement is at `:355` (docstring) + `:372-374` (the `has_inconclusive_bin` property). Both are cited above at their verified lines.

## §6 (D3) — ASSEMBLY: the tangent-slope expression d(δC/C)/dE²

> **TAG: ASSEMBLY.** The expression below is a one-substitution assembly from three canonical pieces; it is **written verbatim nowhere in the corpus before this doc** and is tagged ASSEMBLY (not a new derivation, not an emergence claim — it re-expresses ratified pieces in the bench's measured coordinate).

**The three canonical pieces (verified this branch):**
1. The transverse-T2 chord and tangent capacitance forms, ratified leaf `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:25-38`:
$$
C_{diel} = C_0\,S \approx C_0\left(1-\tfrac12 A^2\right)\ \text{(chord)}, \qquad
C_{ss} = \frac{dQ}{dV} = C_0\left(S - \frac{A^2}{S}\right) \approx C_0\left(1-\tfrac32 A^2\right)\ \text{(tangent)},
$$
with $S \equiv \sqrt{1-A^2}$ and the tangent zero (NDC snap-back) at $A = 1/\sqrt2$.
2. The transverse-FIELD keying (no per-node conflation), `manuscript/ave-kb/vol4/claim-quality.md:524`: a bench that specifies a FIELD $E$ (not a gap voltage) has $A = E/E_{yield}$ **directly**.
3. The canonical scale, `src/ave/core/constants.py:516`: $E_{yield} = V_{yield}/\ell_{node} \approx 1.13\times10^{17}$ V/m.

**The assembly.** Substitute $A = E/E_{yield}$ into the leading-order forms and read $\delta C/C \equiv C/C_0 - 1$:
$$
\left.\frac{\delta C}{C}\right|_{\text{chord}} = -\tfrac12\left(\frac{E}{E_{yield}}\right)^2,
\qquad
\left.\frac{\delta C}{C}\right|_{\text{tangent}} = -\tfrac32\left(\frac{E}{E_{yield}}\right)^2 .
$$
Differentiate with respect to $E^2$ (the natural abscissa for an $E^2$-even response, `CVR-REQ-ACQ`):
$$
\boxed{\ \left.\frac{d(\delta C/C)}{dE^2}\right|_{\text{tangent}} = -\frac{3}{2\,E_{yield}^2},
\qquad
\left.\frac{d(\delta C/C)}{dE^2}\right|_{\text{chord}} = -\frac{1}{2\,E_{yield}^2}\ } .
$$

**Numerical values** (with $E_{yield}^2 = (1.13\times10^{17})^2 = 1.28\times10^{34}\ (\text{V/m})^2$):
$$
\left.\frac{d(\delta C/C)}{dE^2}\right|_{\text{tangent}} = -1.18\times10^{-34}\ (\text{m/V})^2,
\qquad
\left.\frac{d(\delta C/C)}{dE^2}\right|_{\text{chord}} = -3.92\times10^{-35}\ (\text{m/V})^2 .
$$

**What this is and is not.** The **tangent** slope $-3/(2E_{yield}^2)$ is what an across-gap small-signal LCR meter reports — the meter-reported roll-off, the coefficient the CVR bench's $E^2$-even axis would fit. The **chord** slope $-1/(2E_{yield}^2)$ is the large-signal $C=Q/V$ (three-times shallower). Both are **negative** (the SIGN discriminator, `CVR-REQ-FIELDVOL`) and both are keyed on $E_{yield}$ = the transverse-T2 wall (`V_yield`), NOT the longitudinal $C_0/S$ divergence keyed on $V_{snap}$ (which an across-gap meter does not read — `dielectric-plateau-prediction.md:30`). Per `CVR-REQ-FRAME`, at any bench field these slopes are unmeasurably small (§1: $|\delta C/C|_{\rm tangent}\approx1.2\times10^{-18}$ at $E\sim10^8$ V/m; the $\sim10^{-17}$ figure in the page-one frame table is the strong-point value at $E\sim10^9$ V/m, $A_0\sim10^{-8}$); the expression is the *shape* the material-analog ladder validates and the *coefficient* against which a resolved anomaly is bounded, not a bench-reachable AVE signal.

---
