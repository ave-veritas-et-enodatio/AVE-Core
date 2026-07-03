[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-fuajdb]
experiments: [exp-742kv5]
-->

## CLEAVE-01 Requirements / Boundary-Conditions Datasheet

> ↗ Sibling: [`project-cleave-01.md`](project-cleave-01.md) — the canonical Axiom-2 prediction (`clm-ydksh6`, $Q = \xi_{topo}\,x$) this datasheet specs the bench against.
>
> ↗ Sibling: [`cleave-01-trade-study-decision-register.md`](cleave-01-trade-study-decision-register.md) — the **OPEN** make-vs-buy + design-knob decision-space (STATUS:OPEN; no selection). The requirements **below are derived physics**; the choices are **over there**.
>
> ↗ Pre-reg: [`exp-c15-cleave-01-phase-3-measurement-prereg.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-phase-3-measurement-prereg.md) — chord-gated measurement protocol (Level-1 chord = GO/NO-GO; Level-2 slope = non-gating echo).

**What this leaf is.** The **derived, frozen boundary conditions** that any CLEAVE-01 apparatus must satisfy to adjudicate its own falsifier — read top-down from the measurement physics (the gap-independent integer-charge floor, the $\ge4\times$ gap-sweep, the 4-corner conjunction, CPD/drift/vibration rejection). Every number here is **physics-set** (forced by $\{m_e, \ell_{node}, e\}$ + the held-DC/multi-hour-sweep noise model) or is written **parametric in an open design knob** ($\delta$, $C_{in}$) — the requirement *as a function of* the knob, never a pinned number that pre-empts a decision. The knob *choices* and the make-vs-buy *selections* live in the sibling trade-study (STATUS:OPEN); **this leaf selects nothing.**

**Discipline tags.** The **floor** ($Q = \xi_{topo}\,x$, gap-independent integer-charge) is an **Axiom-2 MANIFESTATION (emergence-class)** prediction — zero free parameters, forced by $\xi_{topo} = e/\ell_{node}$. The **slope magnitude** (0.415 pC/µm) is a **consistency-class echo** ($\xi_{topo} = \sqrt{\alpha}$ in native units AND $\ell_{node}$ = electron Compton wavelength — doubly over-determined). Per `consistency-vs-emergence`: the requirements that protect the **chord** carry the emergence weight; the tight requirements that protect the **slope** are consistency-polishing and are explicitly demoted (they gate the non-gating Level-2 corroborator only).

> **★ COUPLING-STATUS — NULL-CONFIRMED-FINAL (2026-07-02, `clm-clvchn`).** The $Q=\xi_{topo}x$ coupling
> is a `def-tk1xfm` unit-bridge, not a derived pump: both the 2-band AND the faithful **N-band** srs
> occupied-manifold Chern returned **$C=0$** in both readings, both enantiomorphs (gapped, converged,
> validate-on-known PASS) → **NULL-CONFIRMED-FINAL**; the coupling question closes. The `CLV-REQ-FLOOR`
> 414.9 fC/µm is a VALUE-import (NOT integer-$C$-reachable; needs $C=2\sqrt2$). **AVE itself predicts
> no floor**, so this bench is a **corroborative-null discriminator** (a one-sided falsifier), NOT a
> chord-confirmation build-target — see the `project-cleave-01.md` Outcome-C rescope.
> **Disposition of the three new corners (this is the FINAL disposition, superseding the #454
> "add-as-axes" note):** the sidereal period-modulation, the fixed-gap moving-slab null, and the
> STAIRCASE phase-native readout are **fingerprints of the (now-null) registry mechanism** — they are
> **moot for THIS bench as live requirement axes** (there is no derived pump for them to characterize).
> They are **retained as diagnostics for any future REOPENS** of `clm-clvchn` (an unexpected positive
> floor), not added as gating requirement corners now. The legacy slope/floor `CLV-REQ-*` specs stay
> as written for the one-sided falsifier reading. **Legacy prose preserved (KEEP-BOTH).**

### REQ-ID INDEX — the canonical requirement identifiers (the bench repo cites + builds to these)

**These `CLV-REQ-<NAME>` identifiers are the canonical, stable CLEAVE-01 requirement IDs.** The bench-engineering sibling repo `AVE-Bench-FemtoElectrometer` **REFERENCES these IDs and builds to spec**; this Vol-4 KB leaf is the **single source of truth** for every derived requirement. The IDs are **descriptive and reorder-proof** — each names the physics object it constrains (readout / gap / PZT / vacuum / thermal / vibration / EMI / calibration / a named master coupling), **NOT** a section number — so a future §-reorder, insertion, or split leaves every ID and every external citation intact. **Stamping an ID changes no derived number, no STATUS:OPEN, and selects no design knob.** Each requirement below carries its `CLV-REQ-*` tag inline at the point of derivation.

| REQ-ID | One-line requirement | Open knob(s) it depends on |
|---|---|---|
| `CLV-REQ-FLOOR` | The derived floor $dQ/dx = \xi_{topo} = e/\ell_{node} = 414.9$ fC/µm the bench must detect (zero free params) | none (physics-set) |
| `CLV-REQ-CPL-A` | Master coupling A — position→charge: $dV/dx = \xi_{topo}/C_{in} = 41.49$ nV/pm; gap jitter rides the signal transfer function (non-averageable) | $C_{in}$ (D2) |
| `CLV-REQ-CPL-B` | Master coupling B — 1/f + drift noise model (held-DC step over multi-hour sweep); binding spec = LEVEL STABILITY, not single-shot resolution | none (physics-set) |
| `CLV-REQ-CPL-C` | Master coupling C — CPD systematic ~21.3% of floor $\propto1/g^2$; 19.97%-of-floor swing the chord-shape must beat across the sweep | none (physics-set) |
| `CLV-REQ-CPL-D` | Master coupling D — 20 fA bias-current ramp = 20.0 fC/s rails a passive node $\Rightarrow$ step-differencing/DC-restore/reset-integration mandatory (a topology BC) | readout topology (D3) |
| `CLV-REQ-READOUT` | Charge-readout chain: in-band noise floor, charge-domain level resolution, ENOB, sub-Hz BW, $C_{in}$ inheritance, validate-on-known (§3) | $\delta$ (D1), $C_{in}$ (D2), topology (D3) |
| `CLV-REQ-DRIFT` | Readout LEVEL STABILITY (the GATING readout spec): drift-referred-to-charge $\le\delta\times414.9$ fC AND beat the 83 fC CPD swing; reached by ARCHITECTURE (H1) | $\delta$ (D1), drift scheme (D4) |
| `CLV-REQ-GAP` | Gap-actuation + metrology: closed-loop linear nanopositioner; travel ratio, position resolution/repeatability/INL/hold, gap-knowledge, linear-DOF, thermal gap drift (§4) | $\delta$ (D1), $g_0$/stroke (D6), stage make-vs-buy (A6) |
| `CLV-REQ-CFIX` | $C_{in}$-FIXED across the $\ge4\times$ sweep (the moving plate IS a $1/g$ cap): $|dC_{in}/C_{in}|\le\delta/k$ (H3, UNCLOSED tension) | $C_{in}$-fixed topology (D5) |
| `CLV-REQ-PZT` | PZT-drive (sub-yield, NOT a field-bias chain): drive-noise mechanical + electrostatic paths, synchronous-step confound, DC stability, range (§5) | $C_{in}$ (D2), $g_0$/stroke (D6) |
| `CLV-REQ-VAC` | Vacuum $\le10^{-6}$ Torr (surface-leakage + patch-stationarity driver, NOT arc-breakdown); ion-gauge filament OFF during read (§6.1) | none (physics-set); A4/A5 make-vs-buy |
| `CLV-REQ-THERMAL` | Thermal $dT\le1$ K over the sweep + 2× calibrated RTDs logged (derived; NOT the binding systematic) (§6.2) | none (physics-set); CTE fixturing (A3/A4) |
| `CLV-REQ-VIB` | Vibration/seismic (the BINDING environmental systematic): gap RMS jitter $\le14.6$ pm in 1–50 Hz + turbo-decouple (§6.3) | $C_{in}$ (D2); isolation/stage make-vs-buy (A6) |
| `CLV-REQ-EMI` | EMI/Faraday SE 64–84 dB + break the BNC-shield→chamber→gauge ground loop + guarded triax (§6.4) | none (physics-set); design/discipline |
| `CLV-REQ-CAL` | Calibration / in-situ-$C$ / charge-reference: in-situ $C_{in}$ split-by-level + one-instrument-three-jobs charge-injection reference (§7) | $\delta$ (D1); $C_{in}$ method (D5), reference topology (A6) |
| `CLV-REQ-VALIDATE` | Validate-on-known (anti-false-null, gates Outcome C): inject ~0.415 pC, resolve to $\le0.1\times$ floor in-session before trusting $V=Q/C$ (§3.8, §7.2) | none (physics-set); reference topology (A6) |
| `CLV-REQ-H1` | Hardest item H1 — readout level stability sub-µV over the multi-hour sweep (= `CLV-REQ-DRIFT`, NEAR EDGE) | $\delta$ (D1), drift scheme (D4) |
| `CLV-REQ-H2` | Hardest item H2 — gap HOLD pm-class + VIBRATION isolation together (= `CLV-REQ-VIB`+`CLV-REQ-GAP`, AT EDGE) | $C_{in}$ (D2); stage+isolation (A6) |
| `CLV-REQ-H3` | Hardest item H3 — $C_{in}$-FIXED across the sweep (= `CLV-REQ-CFIX`, UNCLOSED) | $C_{in}$-fixed topology (D5) |
| `CLV-REQ-H4` | Hardest item H4 — absolute + relative gap-knowledge for the flat-vs-$1/g^2$ fit (= part of `CLV-REQ-GAP`; swap to closed-loop) | $g_0$/stroke (D6), stage make-vs-buy (A6) |
| `CLV-REQ-H5` | Hardest item H5 — travel/stroke $\ge4\times$ feasibility BLOCKER (15–30 µm actuators CANNOT execute the sweep; = part of `CLV-REQ-GAP`) | $g_0$/stroke (D6), stage make-vs-buy (A6) |

> The `CLV-REQ-H1..H5` IDs are **aliases-by-severity** onto the load-bearing primary IDs (`CLV-REQ-DRIFT`, `CLV-REQ-VIB`/`CLV-REQ-GAP`, `CLV-REQ-CFIX`), preserved as their own IDs so the §8 hardest-items register is independently citable. They name the same physics, not a new requirement.

### §1 — The derived floor + the master couplings (physics-set, frozen, zero free parameters)

Verified against `src/ave/core/constants.py` (imported, not hard-coded), 2026-06-22 per `ave-canonical-source`:

| Primitive | Canonical value | Source (verified line) |
|---|---|---|
| $\ell_{node} = \hbar/(m_e c)$ | $3.8616\times10^{-13}$ m | `constants.py:257` (`L_NODE`) |
| $e$ | $1.602177\times10^{-19}$ C | `constants.py:100` (`e_charge`) |
| $\xi_{topo} = e/\ell_{node}$ | $4.1490\times10^{-7}$ C/m | `constants.py:291` (`XI_TOPO`) |

> **FLAG (cite-line drift — FIXED this revision on the AVE-Core side; surfaced for the auditor).** The Phase-3 prereg §3 + Provenance cited $\xi_{topo}$ at `constants.py:246` and $\ell_{node}$ at `:234`; the **verified** lines on this branch are `XI_TOPO:291` / `L_NODE:257` / `e_charge:100`. The *values* were always correct ($4.1490\times10^{-7}$ C/m); only the line numbers drifted. The prereg cites are corrected this revision (per `verify-before-cite`, grepped against `constants.py` on 2026-06-22). `project-cleave-01.md` carries NO `constants.py` line citations (file-level pointer only — verified), so there is nothing to patch there.

**The floor (the thing the bench must detect) — `CLV-REQ-FLOOR`.** Per Axiom 2 ($[Q] \equiv [L]$), one $e$ per $\ell_{node}$ of relative displacement gives the parameter-free transduction
$$
\frac{dQ}{dx} = \xi_{topo} = \frac{e}{\ell_{node}} = 4.1490\times10^{-7}\ \text{C/m}
\quad\Rightarrow\quad
\boxed{414.9\ \text{fC/}\mu\text{m} = 0.4149\ \text{pC/}\mu\text{m}}
$$
At the *assumed* readout capacitance $C_{in} = 10$ pF the voltage projection is $dV/dx = \xi_{topo}/C_{in} = \boxed{41.49\ \text{mV/}\mu\text{m}}$. The **charge** floor is design-independent; the **voltage** floor inherits $C_{in}$ (the only knob in $V = Q/C$).

**Master coupling A — position → charge (the load-bearing one) — `CLV-REQ-CPL-A`.** The predicted floor *is* the transduction $dV/dx = \xi_{topo}/C_{in}$. Therefore a **position error $dx$ produces a voltage $\xi_{topo}\,dx/C_{in}$ that is indistinguishable from a real displacement-charge signal** — gap jitter / creep / repeatability is NOT a noise term that averaging beats; it rides the *same transfer function* as the signal. Numerically:
$$
\frac{dV}{dx}\bigg|_{C_{in}=10\,\text{pF}} = \frac{\xi_{topo}}{C_{in}} = \boxed{41.49\ \text{nV/pm}}
$$
**Consequence (frozen):** a 1 nm gap excursion forges $41.5\ \mu$V — which, against a sub-µV floor (§3), *swamps it by $\sim$40×*. **Vibration isolation and pm-class gap-hold are therefore the hardest mechanical specs on the bench, and they are physics-set: the per-pm sensitivity is fixed by $e/\ell_{node}$ and can only be moved by raising $C_{in}$ (which shrinks the readout voltage) or by mechanical-loop stiffness.**

**Master coupling B — the binding noise model is 1/f + drift, NOT white noise — `CLV-REQ-CPL-B`.** The observable is a **held-DC step** (~100 ms settle + ~1 s hold) compared across an **$N\ge50$, multi-hour, $\ge4\times$ gap-sweep**. The measurement band is therefore sub-Hz down to the inverse sweep duration ($\sim10^{-4}$ Hz). White noise is irrelevant: $e_n\sqrt{1/(2\,t_{hold})} = 14\ \text{nV/}\sqrt{\text{Hz}}\times\sqrt{0.5} \approx 9.9$ nV over a 1 s hold — $\sim4\times10^3$ below one 41.5 mV step. **What binds is the in-band (0.1–10 Hz) 1/f voltage noise (~4 µV p-p $\to$ ~0.61 µV rms) plus sub-0.1-Hz drift.** This is a *fundamental* property of any DC-comparison measurement, not a part choice: **the binding spec is LEVEL STABILITY over the sweep, not single-shot resolution.** (Reproduces the prior equipment-audit's "white-noise-×-√1Hz is the wrong model, overstates SNR by 1–2 OOM" finding.)

**Master coupling C — the CPD systematic the chord rides against — `CLV-REQ-CPL-C`.** The dominant classical background is contact-potential-difference (CPD / moving-Kelvin-probe), itself polarity-odd, at **~21.3% of the floor at the reference gap, scaling $\propto 1/g^2$** (`2026-06-04_round2-adjudications.md:48` "21.3% of floor, ∝1/g²"; `:54` 4-corner means-test). Across a $1\times\!\to\!4\times$ sweep the CPD *contribution* swings by
$$
0.213\times\left(1 - \tfrac{1}{16}\right) = \boxed{19.97\%\ \text{of floor}} \approx 8.3\ \text{mV} \approx 83\ \text{fC},
$$
dropping to $0.213/16 = 1.33\%$ of floor at the far ($4g_0$) end. **The bench's level-stability must beat this 20%-of-floor CPD swing to assert flat-vs-$1/g^2$** — this is the quantitative bar the chord adjudication rides against, and it is the reason the gating requirement is delta-loose (§2): the chord is a SHAPE.

**Master coupling D — the bias-current charge ramp (a topology requirement, not a number) — `CLV-REQ-CPL-D`.** A 20 fA input bias current on a passive 10 pF node injects $I_b/C_{in} = 2.0$ mV/s $= 20.0$ fC/s continuously. Over a 1 s hold this alone is ~4.8% of the 414.9 fC floor; over the multi-hour sweep a **bare follower into a passive node RAILS.** Therefore **step-differencing / DC-restore / reset-integration is mandatory** — a *topology* boundary condition, not a tolerance. (Reference: `AVE-Bench-FemtoElectrometer/hardware/cad/reference_design.md` §9 specifies a bare unity-gain follower into a passive 10 pF node with NO DC bleed path — flagged in the trade-study as the topology decision; not adjudicated here.)

**No fundamental wall.** $kTC$ noise on 10 pF at 300 K is $\sqrt{kT/C} = 20.35$ µV rms $= 0.20$ fC — at/below the floor and reset-differenced away by an integrator topology. There is no quantum/thermodynamic wall anywhere in the chain; every requirement below is reachable in principle, the engineering is in the *architecture* (drift-rejection, gap-hold), not in any part's intrinsic limit.

> **All §1 numbers reproduced from canonical primitives** in `/tmp` scratch (no repo mutation): $\xi_{topo} = 4.1490\times10^{-7}$ C/m; 414.9 fC/µm; 41.49 mV/µm; 41.49 nV/pm; CPD swing 19.97%; $kTC$ 0.20 fC; bias ramp 20.0 fC/s. These match the per-equipment spec-sheet exactly and correct the prior equipment-audit DRAFT arithmetic (bias 48→20.0 fC/s; $kTC$ 50→0.20 fC).

### §2 — The chord/slope reframe sets the requirement structure (carry these; they decide which specs are tight)

These reframes are **physics-set and load-bearing**: they determine *which* requirements are delta-gated and which are not. They are NOT design decisions.

1. **$\delta$ does NOT gate the chord.** The GO/NO-GO is the 4-corner gap-independent floor — a SHAPE (flat-vs-$1/g^2$), measurable *before* $C_{in}$ is pinned. Per `PR#361` (merged) / prereg `:121`: the in-situ-$C$ knob (Q-C15-02) "only affects the non-gating Level-2 slope precision, NOT the chord GO/NO-GO." The chord requires only that the floor LEVEL beat the 20.0%-of-floor CPD swing across the sweep — i.e. **$\delta_{chord}\sim10\%$ is sufficient for chord adjudication with comfortable margin.** The chord is **$C_{in}$-absolute-INDEPENDENT**; it needs only **~4% $C_{in}$ stability across the sweep** (§5), not absolute $C_{in}$ knowledge.

2. **The slope is the only delta-gated axis, and it is a non-gating Level-2 corroborator.** Resolving the 0.415 pC/µm slope to fractional precision $\delta$ is consistency-class echo-confirmation; it never moves an outcome. In-situ-$C$ precision (Q-C15-04) is a **Level-2, non-gating** term.

3. **No HV bias supply exists.** The only HV-class part is the **PZT drive amp** (`cleave_01.ato:51` "PCBA has no on-board HV nets"; `vol_cleave_01/03_bench_geometry.tex:48` "HV feedthrough is not required … ~mV levels not kV"). **"Polarity reversal" in the prereg §5.2 means DISPLACEMENT-direction reversal, NOT a voltage-flip.** The even-in-$V$ fakers (electrostriction $\propto V^2$, flexo, secondary-piezo) ride the PZT drive voltage and are rejected by the **displacement-ODD vs drive-EVEN symmetry**, not by flipping an applied bias. *(Whether to ADD a true bipolar DC bias for a stronger even-in-$V$ discriminator is an OPEN scope decision — sibling trade-study, not specced here.)*

4. **$C_{in}$ 10 pF → 1 pF raises the floor 10×** ($41.49 \to 414.9$ mV/µm), easing readout-resolution and drift requirements ~10×, at the cost of higher impedance/leakage sensitivity. **This is the single biggest lever and is an OPEN knob.**

5. **Drift-rejection by gap-dither + lock-in is the natural fit for Grant's cRIO** (DC–40 kHz phase-coherent) — **but this is recorded as an OPTION in the trade-study, not a decision.**

**Requirement-structure consequence (the parametric convention used throughout §3–§6).** Every design-dependent spec is written as the requirement **as a function of the open knob**, with a safety factor $k$ (default $k=3$) so each error term consumes $\le\delta/k$ of the floor budget:

$$
\sigma_{\text{(error)}} \le \frac{\delta}{k}\times(\text{floor term}),\qquad
\text{floor term} \in \{414.9\ \text{fC},\ 41.49\ \text{mV},\ 1\ \mu\text{m step}\}.
$$

The **recommended freeze** (a trade-study option, NOT selected here) is $\delta_{chord} = 10\%$ (gating) + $\delta_{slope} = 5\%$ (non-gating), matched to the ~5% $C_{in}$-knowledge floor. **This datasheet states the requirement *at every $\delta$*; the freeze is Q-C15-02 (OPEN).**

### §3 — Charge-readout requirement (`CLV-REQ-READOUT`) — electrometer follower + precision digitizer, $V = Q/C_{in}$

**Two-tier; the BINDING tier is held-DC LEVEL STABILITY over the multi-hour $N\ge50$ sweep, NOT single-shot resolution.**

**(3.1) In-band noise floor (per step) — physics-set, COTS design-complete.** In-band (0.1–10 Hz) input-referred voltage noise $\le 0.61$ µV rms (= 4 µV p-p / 6.6); the ADA4530-1 already meets this. White noise (~10 nV over a 1 s hold) is irrelevant (§1, Master Coupling B). *Requirement on the digitizer: it must not ADD in-band noise above this.* DELTA-DEP: none. **PHYSICS-SET that 1/f, not white, binds.**

**(3.2) Charge-domain level resolution (BINDING) — parametric in $\delta$.** The drift-corrected per-gap charge resolution must satisfy
$$
\sigma_Q \le \delta\times 414.9\ \text{fC}
\qquad\Longleftrightarrow\qquad
\sigma_V \le \delta\times 41.49\ \text{mV}\ \text{(at }C_{in}=10\text{ pF; scales }\propto 1/C_{in}).
$$

| $\delta$ | $\sigma_Q$ | $\sigma_V$ @10 pF | $\sigma_V$ @1 pF |
|---|---|---|---|
| 10% | $\le 41.5$ fC | $\le 4.15$ mV | $\le 41.5$ mV |
| 5% | $\le 20.7$ fC | $\le 2.07$ mV | $\le 20.7$ mV |
| 2% | $\le 8.3$ fC | $\le 0.83$ mV | $\le 8.3$ mV |
| 1% | $\le 4.15$ fC | $\le 0.41$ mV | $\le 4.15$ mV |

The chord is a SHAPE; the hardest point is the far ($4g_0$) end where CPD has fallen to 1.33% of floor and the floor must still be resolved at $\delta$. **PHYSICS-SET that LEVEL STABILITY binds; DELTA-DEP linear.**

**(3.3) Digitizer ENOB — parametric in $\delta$, on a $\pm50$ mV (100 mV span) range.**
$$
\text{ENOB}_{\text{single-shot}} \ge \log_2\!\left(\frac{100\ \text{mV}}{\delta\times 41.49\ \text{mV}}\right)
= \{4.6,\ 5.6,\ 6.9,\ 7.9\}\ \text{bits at }\delta=\{10,5,2,1\}\%.
$$
> **FLAG (prior-DRAFT arithmetic corrected, flag-don't-fix).** A prior equipment-audit DRAFT quoted single-shot ENOB as 7/8/9 at $\delta=10/5/2\%$; the correct values are **4.6/5.6/6.9** (the DRAFT was ~2.3 bits high). Surfaced; the DRAFT is not edited here.

The **drift-corrected LEVEL** that gap-independence demands (sub-µV stability on a 100 mV span) needs $\sim$17.3 effective ENOB — an 18–24-bit $\Delta\Sigma$ front end (ADS1262/LTC2400-class) OR a 6.5–7.5-digit DMM in DC mode, with $N\!\sim\!50$ averaging buying $\sqrt{50}=7.07\times$. **PHYSICS-SET level-ENOB; the $\Delta\Sigma$-vs-DMM choice is OPEN (trade-study). An 8-bit scope (390 µV/LSB) is the wrong instrument class** — $\sim$400× short — but the swap is trivially COTS.

**(3.4) Bandwidth — physics-set sub-Hz/DC.** DC-to-~10 Hz per step adequate; the binding measurement bandwidth is the inverse sweep duration ($\sim10^{-4}$ Hz). A wide-band scope is the wrong instrument class; no high-BW ADC is needed.

**(3.5) Topology — the bias-ramp bleed (physics-set existence, design cure).** Per §1 Master Coupling D: the 20 fA = 20.0 fC/s ramp forces step-differencing / DC-restore / reset-integration. **The ramp EXISTS = physics; the cure (follower+differencing vs charge-reset integrator) is an OPEN topology knob (trade-study).**

**(3.6) Drift / level stability (the GATING readout requirement) — `CLV-REQ-DRIFT` — parametric in $\delta$.** Total readout-chain drift (Vos drift + reference/gain drift + $C_{in}$ tempco + sub-0.1-Hz 1/f wander) over the full sweep must satisfy
$$
\text{drift}_{\text{referred-to-charge}} \le \delta\times 414.9\ \text{fC}, \qquad\text{AND must beat the CPD swing } 83\ \text{fC (}19.97\%\text{)}.
$$
Component budget at 10 pF: Vos drift 0.13 µV/°C typ is NOT the limiter (it has ~6000 °C of headroom against the floor); $C_{in}$ tempco (NP0/C0G ~30 ppm/K $\to$ ~0.012 fC/K) is negligible. **The binding terms are sub-0.1-Hz 1/f wander + reference drift + mechanical gap drift** — which is why an **auto-zero / chopper / CDS scheme OR a gap-dither + lock-in (cRIO)** is required to convert the DC-drift-limited measurement into a band-limited one. **PHYSICS-SET that drift (not the ADC) binds; the rejection scheme is an OPEN knob (trade-study). NEAR THE EDGE — reached by ARCHITECTURE, not a better ADC.**

**(3.7) $C_{in}$ inheritance — parametric in $\delta$, plus a load-bearing stability term.** The slope corroborator inherits $C_{in}$ error 1:1 ($Q = C_{in}V$): absolute $C_{in}$ known to $\le\delta$ (Level-2, non-gating). **Load-bearing for the chord:** $C_{in}$ held FIXED across the sweep to $\le0.5\%$ (a drift books as Outcome B, not a false GO; `2026-06-04_round2-adjudications.md:60`). **PHYSICS-SET 1:1 inheritance; the in-situ-$C$ method is OPEN (Q-C15-04).**

**(3.8) Validate-on-known (anti-false-null, gates Outcome C) — `CLV-REQ-VALIDATE`.** Inject a known ~0.415 pC step and confirm the chain resolves it to $\le 0.1\times$ floor *before* trusting $V = Q/C$ (prereg §5.7). DESIGN; COTS. **An Outcome-C cascade walk-back is gated on this passing in-session** (else the null is a dead-instrument artifact, Outcome D).

### §4 — Gap-actuation + metrology requirement (`CLV-REQ-GAP`) — closed-loop linear nanopositioner

**The load-bearing subsystem** (because position error maps 1:1 onto charge through the *same* transduction $\xi_{topo}/C_{in}$ — §1 Master Coupling A; gap jitter is NON-averageable). A **closed-loop, capacitive-sensor, flexure-guided LINEAR** nanopositioner (translation along the gap normal, NOT a tilt mount). Tolerances at safety factor $k=3$ (each error $\le\delta/k$ of the floor budget); written parametric in $\delta$.

**(4.1) Travel / stroke — physics-set RATIO, design-set absolute.** A true $\ge4\times$ geometric gap-span is PHYSICS-SET (the gap-independence corner). At a ~100 µm baseline: stroke $= 3g_0 = 300$ µm if swept UP ($g_0\!\to\!4g_0$), or $0.75g_0 = 75$ µm if taken as $[g_0/4, g_0]$. $\ge4$ points, geometric spacing (ratio ~1.587/step over 4 points). DELTA-INDEPENDENT. **The $4\times$ RATIO is forced; the absolute $g_0$ and hence the absolute stroke is an OPEN knob** (dropping $g_0$ to ~10–25 µm shrinks the required stroke into commodity closed-loop range — trades against parallelism/CPD).

**(4.2) Position resolution / repeatability / linearity / hold — parametric in $\delta$.**
$$
\sigma_x \le \frac{\delta}{k}\times(1\,\mu\text{m step}),\quad
\text{INL} \le \frac{\delta}{k},\quad
\text{creep over hold} \le \frac{\delta}{k}\times(1\,\mu\text{m step}).
$$

| $\delta$ | step repeatability $\sigma_x$ | resolution (target) | actuator INL |
|---|---|---|---|
| 10% | $\le 33$ nm | $\lesssim 3$ nm | $\le 3.3\%$ |
| 5% | $\le 17$ nm | $\lesssim 1.7$ nm | $\le 1.7\%$ |
| 2% | $\le 6.7$ nm | $\lesssim 0.7$ nm | $\le 0.67\%$ |

Closed-loop cap-sensor stages give ~0.1–1 nm resolution, ~nm repeatability, ~0.01–0.1% FS INL — beating the $\delta=10\%$ row by 1–2 OOM. **Open-loop PZT (10–15% hysteresis, log-creep ~10–20 nm in the first seconds = the hold window) FAILS by ~100×.** **PHYSICS-SET that $\sigma_x$ maps 1:1 onto charge; the closed-loop-vs-open-loop choice is OPEN (trade-study).**

**(4.3) Gap-knowledge — absolute LOOSE, relative TIGHT (parametric in $\delta$).** The CPD leverage discounts the absolute-gap requirement: a common-mode $dg/g$ tilts the inferred floor by $\sim 2\times0.213\times(dg/g)$, so
$$
\frac{dg}{g}\bigg|_{\text{absolute}} \le \frac{\delta/k}{2\times0.213} = 0.79\,\delta \quad(\le7.9\%\text{ at }\delta=10\%;\ \le4.0\%\text{ at }\delta=5\%).
$$
The TIGHT lever is the **relative per-point / $4\times$-ratio accuracy** (~1%) to fit-and-subtract the $1/g^2$ CPD SHAPE cleanly (CPD changes ~152% per geometric step). Open-loop PZT cannot place $g$ at all; a closed-loop cap sensor (relative) + one absolute baseline cal is required. **The chord serves the gap-INDEPENDENCE corner — which is why absolute-gap is loose and relative/$C_{in}$-fixed/repeatability are tight.**

**(4.4) Linear DOF, not tilt — physics-set.** The plates must translate along the gap normal staying PARALLEL; tilt changes $C_{in}$ and the gap definition. KMS/POLARIS-K1 mirror-TILT mounts are the wrong DOF. **PHYSICS-SET; the parallelism fixture is a DESIGN item.**

**(4.5) $C_{in}$-FIXED across a $4\times$ sweep — `CLV-REQ-CFIX` — parametric in $\delta$, the UNCLOSED design tension.** The moving plate-pair $C_{plate} = \varepsilon_0 A/g$ tracks $\sim 1/g$ (at $A=1\,\text{cm}^2$: 8.85 pF @100 µm $\to$ 35 pF @25 µm — a $\sim4\times$ swing, FATAL if it IS $C_{in}$). Requirement:
$$
\left|\frac{dC_{in}}{C_{in}}\right|_{\text{any two sweep points}} \le \frac{\delta}{k}\quad(\le 3.3\%\text{ at }\delta=10\%),
$$
met EITHER by a FIXED reference cap dominating $C_{in}$ with moving-plate coupling $C_{plate}(g_{min}) < 0.44$ pF, OR by measuring $C_{in}$ in-situ at every point and dividing out (then the requirement transfers to C-metrology accuracy $\le\delta/k$). **The tension is PHYSICS-SET; the resolution (fixed-ref-cap + weak-coupling sweep electrode vs in-situ-divide) is an OPEN knob (Q-C15-04, which currently treats $C_{in}$ as a static board parasitic and never addresses its $1/g$ motion-dependence — flagged unclosed).**

**(4.6) Thermal gap drift — parametric in $\delta$, CTE design lever.** $\alpha_{CTE} L\,dT < (\delta/k)\times(1\,\mu\text{m step})$: Al 10 mm mount $\to dT < 145$ mK ($\delta=10\%$); low-CTE Invar/Zerodur 10 mm $\to dT < 3.3$ K (~20× relaxation — a DESIGN lever). Closed-loop cap-sensor servo cancels thermal drift in the controlled DOF iff the sensor reference shares the plates' low-CTE frame.

> **FLAG (internal corpus inconsistency — AVE-Core side ALIGNED this revision; Femto side remains).** The KB leaf `project-cleave-01.md:28` **PCBA-Implementation prose is aligned this revision** to the chord-gated $\ge4\times$ gap-sweep framing (per-site, consistent with that leaf's own "Falsification Metric" + Outcome-A sections and the prereg). The Femto-side `AVE-Bench-FemtoElectrometer/hardware/TEST_PROCEDURE.md:31` still carries the SUPERSEDED single-1-µm-step framing at a ~100 µm baseline with a 15–30 µm actuator, which is physically incapable of the $\ge4\times$ sweep the chord-gated prereg makes load-bearing — the mechanical chain is specced to the obsolete measurement (ROOT CAUSE of the open-loop/tilt-mount under-spec). The Femto-side cure is flagged in the prereg (§9, F-R2-3) for a SEPARATE session per cross-repo-session-scope; not performed here.

### §5 — PZT-drive requirement (`CLV-REQ-PZT`) — NOT a field-bias chain; sub-yield, Q-C15-01

Referred to the binding readout floor $V_{floor}\approx0.61$ µV rms ($Q_{floor}\approx6$ aC). Budget fraction $\beta=0.3$ (drive $\le30\%$ of floor $\to$ adds $<5\%$ in quadrature).

**(5.1) Drive-noise, mechanical path (DOMINANT) — parametric in $k_{pzt}$.** Drive noise $\to$ PZT motion $\to$ gap jitter $\to$ charge via the 41.49 nV/pm coupling:
$$
dV_{drive} \le \frac{\beta\,V_{floor}}{G_{gap}\,k_{pzt}},\qquad G_{gap} = 41.49\ \text{nV/pm}.
$$
At a worst-case high-sensitivity $k_{pzt}=150$ nm/V: $dV_{drive}\le 29$ µV rms in-band (gap-jitter floor 14.6 pm rms at full floor, 4.4 pm at $\beta\cdot$floor). **This path binds unless the drive is filtered** — but the 1 µm step needs only ~10–50 Hz BW, so a passive RC/LC post-filter drops in-band noise below floor (free headroom).

**(5.2) Drive-noise, electrostatic path — parametric in residual coupling $C_c$.** $dV_{drive} \le \beta\,V_{floor}\,(C_{in}/C_c)$ = 1.8 mV / 0.18 mV / 18 µV / 1.8 µV rms at $C_c$ = 1 fF / 10 fF / 100 fF / 1 pF. **The grounded plate must drop $C_c$ to the fF class** (shield-effectiveness is itself a derived requirement, $C_c\le\sim10$ fF for a 0.18 mV budget — UN-BUDGETED in the baseline, flagged).

**(5.3) Synchronous-step confound (worst class) — physics-set, rejected by symmetry.** A 1 µm step demands ~6.7 V drive change (@150 nm/V), coupling $C_c\times6.7$ V *synchronous* with displacement: 0.67 / 6.7 / 67 mV at $C_c$ = 1 / 10 / 100 fF = 0.02 / 0.16 / 1.6× the signal — PERFECTLY correlated, cannot be averaged. **Rejected by the displacement-ODD vs drive-EVEN symmetry** (the chord is displacement-odd; the drive-coupled term and the even-in-$V$ fakers are displacement-even), provided the two displacement directions match to a few pm.

**(5.4) Drive DC stability — physics-set, design cure.** Gap must hold to $\le4.4$ pm (differenced) / $\le14.6$ pm (absolute); open-loop PZT creep violates this $\to$ closed-loop cap-sensor servo. DAC step precision (DAC8830 16-bit × gain 27.5 = 8.4 mV/LSB $\to$ sub-nm) is adequate. **The drive and the stage are ONE closed-loop problem, not two boxes.**

**(5.5) Range — design-set.** $\ge4\times$ sweep: 10 µm baseline $\to$ ~200 V drive span; 100 µm $\to$ ~2000 V (or a longer-stroke/lower-$k$ stage). Per-point ~1 µm modulation = ~6.7 V step.

### §6 — Environment requirement (vacuum / thermal / vibration / EMI)

Each sub-spec derived FROM the systematic it controls. The chord-clean specs (vibration, thermal) bind on the 0.61 µV intrinsic floor + the 21%-CPD separation (delta-INDEPENDENT); the delta-PARAMETRIC versions are the looser Level-2-slope budgets.

**(6.1) Vacuum — `CLV-REQ-VAC` — physics-set $\le10^{-6}$ Torr.** Driver is **surface-leakage-vs-20 fA-budget + patch stationarity, NOT arc-breakdown.** A 1 V node excursion across humid PTFE ($\rho_s\sim10^{13}\ \Omega/\square$) leaks ~100 fA = 5× over the 20 fA budget; at $\le10^{-6}$ Torr the adsorbed-water layer desorbs ($\rho_s\to\sim10^{16}\ \Omega/\square$) and surface leak falls to ~0.1 fA = 200× under budget. Arc-breakdown non-binding (100 V PZT $\ll$ ~kV Paschen at 100 µm·atm). STABILITY: reactive partial-pressure stable to $\pm20\%$ over the sweep (keep the $1/g^2$ CPD/patch background stationary). CLEANLINESS: hydrocarbon-free (dry scroll + turbo). **Ion-gauge filament OFF during the held-DC read** (charge/ion source). $\le10^{-6}$ Torr is explicitly NOT UHV (Q-C15-01).

**(6.2) Thermal — `CLV-REQ-THERMAL` — derived ~1 K (NOT the binding systematic).** Vos drift (0.13 µV/°C typ, 0.5 max) referred to the floor across the sweep: total drift $<0.61$ µV needs $dT_{sweep}<4.66$ K (typ) / 1.21 K (max-tempco). $C_{in}$ tempco (30 ppm/K) is Level-2-slope-only and loose. **TOLERANCE: $dT\le1$ K + 2× calibrated RTDs logged with the data. This $\le1$ K is the canonical operator drift-pause threshold the bench repo builds to (`CLV-REQ-THERMAL`); it SUPERSEDES the older corpus "pause if lab drifts $>5$ K" operator rule.**
> **FLAG (operator-rule tightened to the derived spec — surfaced for the auditor; the remaining un-landed site is cross-repo).** The older corpus "pause if lab drifts $>5$ K" operator rule (carried in the Femto-side `AVE-Bench-FemtoElectrometer/hardware/TEST_PROCEDURE.md` equipment-audit subsystem 5 — verified ABSENT from every AVE-Core-side cleave file on this branch: prereg, `project-cleave-01.md`, sim-audit) is ~4× looser than the derived $\le1$ K. NOT a physics contradiction — but it under-protects the chord. **On the AVE-Core side the canonical operator threshold is now the derived $\le1$ K (`CLV-REQ-THERMAL`), stated above.** Landing the $\le1$ K tightening into the Femto-side `TEST_PROCEDURE.md` is a Femto-repo edit, flagged for a SEPARATE session per `cross-repo-session-scope` (alongside the §4.6 / F-R2-3 stale-framing cure) — NOT performed here.

**(6.3) Vibration / seismic (the BINDING environmental systematic) — `CLV-REQ-VIB` — physics-set.** Gap RMS jitter $\le14.6$ pm in 1–50 Hz (chord-clean): $0.61\ \mu\text{V}/41.49\ \text{nV/pm} = 14.6$ pm. Needs isolation transmissibility $T<3\times10^{-4}$ (71 dB, quiet ~50 nm ambient) to $T<1.5\times10^{-5}$ (97 dB, noisy ~1000 nm ambient) across 1–50 Hz. PLUS a hard requirement to **DECOUPLE the turbo pump** (kRPM rotor = vibration SOURCE on the chamber) via bellows/remote-mount OR valve-off-and-coast during each held-DC read. Delta-bound regime: $\le10/20/50$ pm at $\delta=1/2/5\%$ — but the 14.6 pm chord-clean spec governs. **PHYSICS-SET (= the floor slope itself); only movable by raising $C_{in}$ or mechanical-loop stiffness. NEAR/AT the COTS edge — the hardest environmental requirement, shared with the gap-metrology subsystem.**

**(6.4) EMI / Faraday — `CLV-REQ-EMI` — derived 64–84 dB.** Referred pickup $dV_{in} = (C_{ant}/C_{in})V_{int}$; for $dV_{in}<0.61$ µV with $C_{ant}/C_{in}=10^{-3}$, $V_{int}<0.61$ mV $\to$ SE $\ge20\log_{10}(\text{ambient}/0.61\text{ mV})$ = 64 dB (1 V/m) to 84 dB (10 V/m) at mains 50/60 Hz. PLUS: break the documented BNC-shield→chamber→gauge-controller ground loop (single-point star ground + line filter), run guarded triax (not bare coax), gate the ion-gauge filament OFF during reads. **DESIGN/discipline, not exotic hardware.**

### §7 — Calibration / in-situ-C / charge-reference requirement (`CLV-REQ-CAL`)

**(7.1) In-situ $C_{in}$ — SPLIT by level.** LEVEL-1 (chord/GO-NO-GO): absolute $C_{in}$ NOT required; required is $C_{in}$ STABILITY across the sweep $dC_{in}/C_{in}<\sim4\%$ (delta-INDEPENDENT — derived from the CPD $1/g^2$ contrast 19.7% resolved to 1/5) + the §4.5 design constraint (moving-plate $C<\sim5\%$ of $C_{in}$). LEVEL-2 (slope, non-gating): absolute in-situ $C_{in}$ known to $\le\delta$, measured AS A WHOLE on the powered assembled board (an LCR-meter 2-terminal passive reading does NOT see the op-amp's powered input parasitics / guard-Miller at DC — pre-flight check only).

**(7.2) Charge-injection reference — SPLIT by use, ONE instrument three jobs.** USE A (anti-false-null, gates Outcome C): inject ~0.415 pC at SNR$\ge10$; accuracy ~10–20% sufficient (delta-INDEPENDENT). USE B (Level-2 magnitude validation): $Q_{inj}$ known to $\le\delta/2$ (split $C_{ref}, V_{ref}$ each $\sim\delta/4$). **UNIFICATION:** a single calibrated charge-injection reference read on the same floating node simultaneously (i) measures absolute in-situ $C_{in} = Q_{inj}/V_{meas}$ INCLUDING all powered parasitics (closes Q-C15-04 — an LCR meter cannot), (ii) validates the Level-2 transfer function, (iii) serves as the anti-false-null positive control. Its accuracy spec is the tightest = Use-B's $\sim\delta/2$.
> **Beyond-COTS edge dissolved by topology.** A discrete sub-pF 0.25% chip cap does not exist in catalog; the design move is a larger catalog-grade $C_{ref}$ (e.g. 10 pF 0.25% C0G) with an ATTENUATED precision $V_{ref}$ step — $Q_{inj}=C_{ref}V_{ref}$ still deposits 0.415 pC, with the tight tolerance on the voltage step (0.1–0.25% COTS). The reference *topology* is an OPEN knob (trade-study).

**(7.3) Phase-space-coordinate check (per A46).** This measurement is **genuinely real-space** — displacement in m, charge in C, voltage in V on a real cap; the corpus claim $[Q]\equiv[L]$ is itself a real-space dimensional identity. Real-space coordinates are MATCHING, not a mismatch. No phase-space discipline violation.

### §8 — Hardest requirements + the physics-set / fundamental-limits register

**Hardest (the spec-drivers):**

| # | REQ-ID | Requirement | Why hardest | Class |
|---|---|---|---|---|
| H1 | `CLV-REQ-H1` (= `CLV-REQ-DRIFT`) | Readout LEVEL STABILITY (§3.6): sub-µV held level over the multi-hour $N\ge50$ sweep | reached by ARCHITECTURE (auto-zero/chopper/CDS or gap-dither+lock-in), not a better ADC | NEAR EDGE |
| H2 | `CLV-REQ-H2` (= `CLV-REQ-VIB` + `CLV-REQ-GAP`) | Gap HOLD pm-class (§4.2) + VIBRATION isolation (§6.3): 41.49 nV/pm $\Rightarrow$ nm jitter = 40 µV swamps the floor | stage + isolation together; coupling is physics-set, non-averageable | AT EDGE |
| H3 | `CLV-REQ-H3` (= `CLV-REQ-CFIX`) | $C_{in}$-FIXED across the sweep (§3.7, §4.5): moving plate IS a $1/g$ cap | UNCLOSED design tension (Q-C15-04 ignores motion-dependence) | UNCLOSED |
| H4 | `CLV-REQ-H4` (⊂ `CLV-REQ-GAP` §4.3) | Absolute + relative gap-knowledge (§4.3) for the flat-vs-$1/g^2$ fit | open-loop PZT cannot place $g$ | swap to closed-loop |
| H5 | `CLV-REQ-H5` (⊂ `CLV-REQ-GAP` §4.1) | Travel/stroke (§4.1): $\ge4\times$ at 100 µm needs ~300 µm; selected 15–30 µm actuators CANNOT execute the sweep at all | a feasibility BLOCKER, not a tolerance | de-spec $g_0$ or buy travel |

**Physics-set fundamental limits (nature forces — cannot move):**
(a) the floor 414.9 fC/µm = 41.49 mV/µm @10 pF ($\xi_{topo}=e/\ell_{node}$, zero free params);
(b) the 1/f + drift-bound character of a held-DC step over a multi-hour sweep (any DC-comparison is 1/f+drift limited, NOT white) $\Rightarrow$ binding spec = LEVEL STABILITY;
(c) the 41.49 nV/pm position→charge coupling = $\xi_{topo}/C_{in}$ (makes H2 the hardest);
(d) the $C(g)\propto1/g$ geometric tension (H3);
(e) the bias-current ramp EXISTS (20.0 fC/s);
(f) the $4\times$ gap RATIO as the flat-vs-$1/g^2$ lever.
**There is NO quantum/thermodynamic WALL** ($kTC$ = 0.20 fC, at/below floor, reset-differenced away); all else is design-choice or COTS-reachable.

**Flag register (surfaced for the auditor lane / Grant):**
1. Cite-line drift — **FIXED on the AVE-Core side this revision.** The Phase-3 prereg cited `XI_TOPO:246`/`L_NODE:234`; the verified lines on this branch are `XI_TOPO:291`/`L_NODE:257`/`e_charge:100` (values always correct). The prereg §3 table + Provenance line are corrected this revision; `project-cleave-01.md` carries NO `constants.py` line cites (only a file-level pointer — verified), so nothing to fix there. §1.
2. Internal corpus inconsistency — **`project-cleave-01.md:28` PROSE ALIGNED this revision** to the chord-gated $\ge4\times$ gap-sweep framing (per-site, consistent with the leaf's own chord-gated Outcome section + the prereg). The Femto-side `TEST_PROCEDURE.md:31` still carries the superseded single-1-µm-step framing — that mechanical-chain cure is a Femto-repo edit, separate session (F-R2-3). §4.6.
3. Operator-rule under-protection — **TIGHTENED on the AVE-Core side this revision** to the derived $\le1$ K = `CLV-REQ-THERMAL` (canonical operator drift-pause threshold). The older "$>5$ K pause" string is verified ABSENT from every AVE-Core-side cleave file and lives only in the Femto-side `TEST_PROCEDURE.md` — landing the $\le1$ K there is a separate-session Femto-repo edit. §6.2.
4. Prior-DRAFT arithmetic corrected: single-shot ENOB 7/8/9 $\to$ 4.6/5.6/6.9; bias 48 $\to$ 20.0 fC/s; $kTC$ 50 $\to$ 0.20 fC. §1/§3.3.
5. White-noise seam: Q-C15-02:40 quotes 15 nV/√Hz @1 kHz vs the task brief's 14 nV/√Hz @10 kHz — both within datasheet spread, neither binds (white noise irrelevant sub-Hz). §1.
6. Consistency-vs-emergence: the floor is Axiom-2 MANIFESTATION (zero free params, emergence-class); the slope is a consistency-class echo (PR#361 says so). The tight Level-2 specs must NOT be read as gating the emergence claim.

---






