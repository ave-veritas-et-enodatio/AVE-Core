[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-zp4kqr, clm-zp7bds]
-->

## The Measurement-Coupling Port on the Vacuum Impedance Network

> **Scope + epistemic register (read first — `consensus-bias-symmetric-standard`).** This leaf
> is a **measurement-coupling primitive**: how an external instrument couples to a substrate mode
> *without being modeled as part of the substrate*. It is a **port on the equivalent-circuit MODEL**
> ([`def-gv1net`](../../../common/vocabulary-register.md):569 — the graded vacuum impedance network),
> **NOT a new substrate object** (respects INVARIANT-N1: the substrate-noun slot stays prose-only;
> this primitive adds no ontological glyph). **MOST of the content here is textbook EE / measurement
> theory applied honestly** — loaded-vs-intrinsic $Q$, read-vs-excite, the reactive-tap rule. A
> vanilla RF/instrumentation engineer states all of it. It is recorded here because **(i)** the AVE
> substrate's per-channel characteristic impedances are unusual (three unit-incommensurable channels,
> §1), so "high-Z" has no single referent; and **(ii)** the lossless axiom (Axiom 3) sharpens
> *exactly* one statement into something AVE-specific (§3). The value is a **design primitive that
> unifies the falsification-bench fleet** (§4), **not a physics chord.** The genuinely AVE-distinct
> content is narrow and is flagged explicitly in §3; everything else is tagged textbook and cited
> as such.

This leaf extends [`resonant-lc-solitons.md`](resonant-lc-solitons.md) (the matched/radiative PORT,
loaded-$Q$) and [`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md) (loaded-vs-intrinsic $Q$). It does
**not** reinvent the channel impedances — those are the Grant-ratified three-impedance law
([`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md):20,
field-symbol registry §3.11). It adds the **measurement-apparatus-loads-a-substrate-mode** framing,
which is **corpus-confirmed absent** as a substrate-side concept (the only prior "back-action" hit is a
sim-engine artifact, not a measurement apparatus).

---

## 1. The corrected primitive — three coupled statements (NOT "always high-Z")

The naive instinct — *"use a high-vacuum-impedance probe, like a scope's high $Z_{electric}$"* — is
**wrong as stated.** The corrected primitive is three coupled statements. Statements 1–2 are textbook
(tagged); statement 3 is textbook in form but is sharpened by Axiom 3 in §3.

### 1.1 Know the channel and its characteristic impedance (textbook)

The substrate has **three** characteristic impedances, one per grade, and they are
**unit-incommensurable**:

| Channel | Characteristic impedance | Unit | Anchor |
|---|---|---|---|
| EM-transverse | $Z_{\mathrm{EM}} \equiv Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$ | electrical ($\Omega$, V/A) | [`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md):20; [`z0-derivation.md`](z0-derivation.md):37 |
| Shear / GW | $Z_{\mathrm{shear}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{shear}}$ | mechanical/acoustic ($\rho\times$speed, Rayl) | [`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md):21 |
| Bulk-longitudinal | $Z_{\mathrm{bulk}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}} = \sqrt{2}\,\rho_{\mathrm{bulk}}\,c_0$ (at $K=2G$) | mechanical/acoustic (Rayl) | [`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md):22 |

Only $Z_{\mathrm{EM}}$ is electrical. $Z_{\mathrm{shear}}$ and $Z_{\mathrm{bulk}}$ are mechanical/acoustic
and live **~12.8 orders of magnitude away AND in a different unit** ($\approx 377\,\Omega$ vs
$Z_{\mathrm{mech}} \approx 2\text{–}3\times10^{15}$ Rayl;
[`research/2026-06-20_node-2domain-nport.md`](../../../../../research/2026-06-20_node-2domain-nport.md):171,197).
**There is no single "$Z$" to be high relative to** — you must re-derive the characteristic impedance
*per channel* before "high" or "low" means anything. "Same principle, different hardware" is really
"same *analogy*, different physics." EM↔mechanical coupling therefore needs a **transducer, not a wire**
— the candidate bridge is the TKI-transformer
([`def-tk1xfm`](../../../common/vocabulary-register.md):324), which is **`status:proposed`-not-ratified**
and carries an *"identity-by-translation, NOT a derivation"* ceiling. **Any cross-channel probe claim
inherits that ceiling** ([`resonant-lc-solitons.md`](resonant-lc-solitons.md):122).

### 1.2 Know whether you are in READ-mode or MEASURE-mode (textbook)

These want **opposite** couplings:

- **READ-mode** (sample the existing state, à la a voltmeter / electrometer): minimize the *fractional
  resistive loading* $\mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}} \to 0$, and couple
  **reactively**. This is the genuine "high-vacuum-impedance probe" — but its design axis is the
  resistive ratio, not the magnitude (§1.3).
- **MEASURE-mode** (drive the substrate; the observable *is* the reactance/response, à la a network
  analyzer / impedance spectroscope): you want **controlled small-signal** coupling and you read back
  $Z(V, f)$ or $\Gamma$. High-$Z$ is the *wrong* target here, and the coupling is **not** "matched"
  in the power-transfer sense — a small-signal lock-in is ratiometric, not power-matched.

### 1.3 In READ-mode, invasiveness is set by the RESISTIVE part, not the magnitude (textbook form; §3 sharpens)

The energy a probe drains per cycle is set by $\mathrm{Re}(Z_{\mathrm{probe}})$, **not**
$|Z_{\mathrm{probe}}|$. A lossy high-$|Z|$ probe loads a mode *harder* than a low-loss low-$|Z|$ reactive
tap. $|Z|$ is only a proxy that happens to work for a bench scope-probe — where high-$|Z|$ is *also*
low-loss — and it **fails** for any lossy high-$|Z|$ probe. The design axis is:

> **[Resultbox]** *Back-action design axis (READ-mode)*
>
> $$
> \frac{\mathrm{Re}(Z_{\mathrm{probe}})}{Z_{\mathrm{channel}}} \;\to\; 0
> \qquad\text{(NOT } |Z_{\mathrm{probe}}|\text{ large)}.
> $$

The reactive part $\mathrm{Im}(Z_{\mathrm{probe}})$ is **not free of consequence**: it **detunes** the
mode (pulls $\omega_0$ via the loading reactance, exactly as a loading capacitance pulls an LC tank).
But that detuning is a **conservative, calibratable systematic** — it shifts the measured frequency, it
does not drain the mode — so it is a *correctable* error, not an irreversible back-action. The
energy-draining (irreversible) back-action budget is $\mathrm{Re}(Z_{\mathrm{probe}})$; the
mode-pulling (reversible, calibratable) systematic is $\mathrm{Im}(Z_{\mathrm{probe}})$. Keep them
separate: $\mathrm{Re}(Z_{\mathrm{probe}})$ is the *energy* back-action budget, not the *entire* probe
influence.

> **Proposed symbols (GRANT-CALL — naming not yet ratified).** This leaf provisionally writes the
> probe/port coupling impedance as $Z_{\mathrm{probe}}$ and the READ-mode design ratio as
> $\mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}}$. Both the symbol $Z_{\mathrm{probe}}$ and the
> ratio name are **proposed, pending Grant ratification** (sibling-symbol precedent: the registry's
> $z_{local}$ / $Z_0$ / $Z_{\mathrm{EM}}$ discipline,
> [`research/2026-06-10_field-symbol-registry.md`](../../../../../research/2026-06-10_field-symbol-registry.md):205).
> No new substrate-object glyph is introduced (INVARIANT-N1).

---

## 2. Derivation — the lossless-port energy ledger (DERIVED, Axiom 3)

This is the one quantitative result the leaf **derives** (everything in §1.2 and the reactive-tap
rule is asserted-as-textbook; see §6). The derivation is short because it rides Axiom 3.

A substrate mode of stored energy $U$ and angular frequency $\omega$ rings on a channel of
characteristic impedance $Z_{\mathrm{channel}}$. Attach a probe presenting a port impedance
$Z_{\mathrm{probe}} = R_p + jX_p$ (with $R_p \equiv \mathrm{Re}(Z_{\mathrm{probe}})$,
$X_p \equiv \mathrm{Im}(Z_{\mathrm{probe}})$). The per-cycle energy ledger has two destinations for any
energy the probe exchanges with the mode:

1. **Reactive (storage) exchange** — energy shuttled into $X_p$ and returned each cycle. Net per-cycle
   drain $= 0$ (a reactance stores, it does not dissipate). It **pulls** the resonant frequency
   (mode-detuning) but conserves the mode energy.
2. **Resistive (dissipative) exchange** — energy delivered into $R_p$ and **not** returned. This is the
   only irreversible term.

The standard loaded-resonator result for the energy fraction lost per cycle to a resistive load is
$\Delta U/U \propto R_p / Z_{\mathrm{channel}}$ (the loaded-$Q$ relation; the leak per bounce scales as
the resistive fraction of the loading impedance — same algebra as
[`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md):156, where the matched-port leak is
$|\Gamma_{\mathrm{EM}}|^2$ per bounce). So far this is **ordinary** loaded-$Q$ — true in any medium.

**The Axiom-3 sharpening (this is the AVE-specific step).** In an ordinary lab medium, some of the
probe's back-action is absorbed by **internal dissipation in the medium** — the medium has its own loss
channel, so the probe's $R_p$ is one of *several* sinks, and "$R_p$ small" is necessary but not
sufficient for non-invasiveness. The AVE substrate is **lossless-reactive (Axiom 3)**: there is
**nowhere inside the substrate** for back-action energy to go (no bulk loss; the confinement walls are
$|\Gamma|=1$ perfect reflectors, [`resonant-lc-solitons.md`](resonant-lc-solitons.md):47,50). Therefore
**all** irreversible energy exchange with the mode must flow **out through the probe's resistance**, and:

<!-- claim-quality: clm-zp4kqr (the lossless-port energy ledger: in a lossless-reactive substrate (Axiom 3) the irreversible measurement back-action = κ·Re(Z_probe)/Z_channel with no internal-loss term; READ-mode non-invasiveness axis is Re(Z_probe)/Z_channel→0, not |Z| large; Im(Z_probe) = calibratable mode-detuning only) -->

> **[Resultbox]** *Lossless-port back-action budget (DERIVED, Axiom 3) — `clm-zp4kqr`*
>
> In a lossless-reactive substrate (Axiom 3), the entire irreversible measurement back-action on a
> mode is carried by the probe's resistive part, with **no internal-loss term**:
> $$
> \left(\frac{\Delta U}{U}\right)_{\!\text{per cycle}}
> \;=\; \kappa \,\frac{\mathrm{Re}(Z_{\mathrm{probe}})}{Z_{\mathrm{channel}}},
> \qquad
> \mathrm{Im}(Z_{\mathrm{probe}}) \;\Rightarrow\; \text{conservative detuning only (calibratable).}
> $$
> where $\kappa$ is an $O(1)$ geometric coupling factor (the port coupling factor; cf. the
> matched/radiative port at [`resonant-lc-solitons.md`](resonant-lc-solitons.md):118). The READ-mode design target is therefore
> $\mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}} \to 0$, and $\mathrm{Re}(Z_{\mathrm{probe}})$ is
> the **exact and entire** *energy* back-action budget — a cleaner statement than in a lossy medium,
> where it would be only a lower bound.

**What this is and is not.** It is a clean reframing of loaded-$Q$ specialized to a lossless medium:
the lossless axiom *removes* a term (the internal-loss sink) rather than adding one. Note this
**undercuts** a magnitude framing rather than supporting it: with no internal loss, only the probe's
resistance can drain the mode, so $|Z_{\mathrm{probe}}|$ is irrelevant and
$\mathrm{Re}(Z_{\mathrm{probe}})$ is everything (for *energy* — the reactance still detunes, §1.3). It
is **NOT** a novel prediction: it predicts no new measurable that ordinary loaded-$Q$ would not, once
you grant the lossless axiom. Recorded as a **CONSISTENCY-class** result (§ solidity).

---

## 3. The narrow AVE-distinct content (only two items — don't oversell the rest)

Exactly two pieces of this primitive are genuinely AVE-specific. Everything else is honest textbook EE
(§6 tags it). Per `consensus-bias-symmetric-standard`: this is *peer-mapped-honestly*, not an AVE
comedown — the SM likewise does not derive its own measurement-back-action principles; they are
universal instrumentation theory there too.

### 3.1 Axiom-3-lossless makes $\mathrm{Re}(Z_{\mathrm{probe}})$ the *exact* (not merely asymptotic) entire *energy* back-action budget

This is the §2 result. In a normal lab medium some back-action dissipates *in the medium*; in a
lossless-reactive substrate it cannot, so the probe's resistance is exactly and only the irreversible
invasiveness. Clean, correct reframing. **Symmetric-standard scope (what is and isn't AVE-distinct here):**
the *logic* — a lossless single-port resonator means only the external coupling resistance can drain the
mode — is shared by any high-$Q$ resonator (e.g. an idealized optical cavity); AVE does not invent it.
What *is* AVE-distinct is that the losslessness is **axiomatic-exact** (Axiom 3), not an engineering
idealization carrying finite residual loss — so here $\mathrm{Re}(Z_{\mathrm{probe}})$ is the *exact* and
entire energy budget, where in a real cavity it is only the asymptotic low-loss-limit one. **Caveat (carried from §1.3):** "entire" scopes the *energy*
(irreversible) budget — the reactive $\mathrm{Im}(Z_{\mathrm{probe}})$ still detunes the mode as a
separate, *calibratable* systematic. Do not read this as "$\mathrm{Re}(Z)$ is literally the entire probe
influence with no other term."

### 3.2 Per-channel boundary geometry decides WHERE you couple — and for the bulk sector it INVERTS the naive acoustic intuition

The naive acoustic rule *"high-Z coupler = rigid wall = pressure antinode = good place to read
pressure"* is **wrong for the standing-V mass scalar.** AVE's own confined-bulk boundary — the electron
mass-cage — is a **SHORT, not a rigid wall**:

> **[Resultbox]** *Bulk confinement boundary is a SHORT (not a rigid wall) — corpus-cited*
>
> $$
> Z_{\mathrm{bulk}} \to 0 \;\;\Rightarrow\;\; \Gamma_{\mathrm{bulk}} = -1
> \quad\text{(a pressure NODE / displacement antinode at the wall).}
> $$
> Anchors: [`research/2026-06-20_node-2domain-nport.md`](../../../../../research/2026-06-20_node-2domain-nport.md):81
> (electron mass-cage = confined A1 dilatation, $Z_{\mathrm{bulk}}\to0 \Rightarrow \Gamma=-1$);
> corroborated [`research/2026-06-15_ceff-epsilon-monotonicity_result.md`](../../../../../research/2026-06-15_ceff-epsilon-monotonicity_result.md):46
> ("short $\Gamma=-1$ puts a voltage node at the wall"). The mass-cage is the **A1 dilatation** wall
> ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).

Two consequences for measurement siting:

1. **A rigid (high-$Z$) coupler placed at the substrate's natural bulk boundary reads a NODE** (near
   zero) and you would **mis-conclude non-invasiveness while actually being mis-sited** — you are
   reading the null of the wrong field, not a quiet mode.
2. **Which field you null is sector-dependent**, because
   $\Gamma_{\mathrm{flow}} = -\Gamma_{\mathrm{pressure}}$
   ([`research/2026-06-10_field-symbol-registry.md`](../../../../../research/2026-06-10_field-symbol-registry.md):160).
   A boundary that is a node for the pressure field is an antinode for the flow field, and vice versa.

**Do not conflate the two $\Gamma=-1$ walls.** The A1 impedance-short ($Z_{\mathrm{core}}\to0$, mass
sector) is **orthogonal** ($A1 \perp T2$) to the T2 $\Gamma_{\mathrm{spinor}}$ topological spinor-sign
wall ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20;
[`resonant-lc-solitons.md`](resonant-lc-solitons.md):91). They are numerically coincident at $-1$ but
are distinct objects; a measurement port couples to the A1 impedance wall, not the topological winding.

> **🚩 OPEN PHYSICS QUESTION — ROUTED TO GRANT (`flag-don't-fix`; NOT decided in this leaf).**
> **In the bulk / V-scalar sector, does a non-invasive READ want to sit at the substrate's native
> SHORT ($Z_{\mathrm{bulk}}\to0$, the pressure node) or at a rigid high-$Z$ coupler — given that
> $\Gamma_{\mathrm{flow}} = -\Gamma_{\mathrm{pressure}}$ flips which field is nulled?** This is the one
> genuine physics call in this primitive (everything else is corrected engineering). The naive acoustic
> answer (rigid wall) is *suspect* precisely because the substrate's own confined-bulk boundary is a
> short, but which siting is actually least-invasive for a given observable depends on whether the
> instrument couples to the pressure (V-scalar) field or the flow field — a sector choice this leaf
> deliberately does **not** make. The bulk-sector coupling LOCATION is flagged as OPEN and surfaced to
> Grant; the EM-sector READ (§4 Cleave-01) is unaffected and proceeds.

---

## 4. The fleet payoff — a common design language that maps onto the axiom partition (`clm-zp7bds`)

<!-- claim-quality: clm-zp7bds (the bench-fleet mode partition: every bench classifies READ vs MEASURE; Cleave-01 = unique READ-mode / unique Axiom-2 test, the other four MEASURE-mode / Axiom-4; the mode partition maps onto the axiom partition so Ax2-fail ≠ Ax4-fail; MEASURE-mode is NOT power-matched; a design-organizing claim, not a physics claim) -->

The load-bearing reason to formalize this primitive: the impedance frame **unifies the
falsification-bench fleet** as a common language and **partitions it by mode — and the mode partition
maps onto the axiom partition.** Every future bench gets a four-question design checklist: *(i)* which
channel-$Z$? *(ii)* READ or MEASURE? *(iii)* minimize $\mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}}$
or control the small-signal drive? *(iv)* where is the boundary node/antinode for the coupled field?

| Bench | Channel | Mode | Tests | Coupling note |
|---|---|---|---|---|
| **Cleave-01 femto-electrometer** | TKI charge-dislocation $[Q]\equiv[L]$ (EM-sector readout) | **READ** | **Axiom 2** | The femto-amp guard-ring + DC-restore front-end **IS** the engineering of $\mathrm{Re}(Z_{\mathrm{probe}})\to0$. The ADA4530-1's 20 fA is the op-amp's *input-bias-current spec* — a parasitic resistive-leakage floor treated as a defect to **null**, not a tunable coupling. Anchors: `AVE-Bench-FemtoElectrometer` `hardware/cad/reference_design.md`:57 (guard ring), `hardware/BOM.md`:21 (ADA4530-1 20 fA), `hardware/TEST_PROCEDURE.md`:76 (CPL-D / DC-restore). |
| **AVE-Bench-VacuumMirror** | EM transverse / asymmetric-$\varepsilon$ | **MEASURE** | **Axiom 4** | drives $E$ to modulate $\varepsilon_{\mathrm{eff}}$, reads $\Gamma(V)$. |
| **cRIO $C_{\mathrm{eff}}(V)$ saturation-onset** | EM / VCA mode | **MEASURE** | **Axiom 4** | ratiometric small-signal lock-in quadrature $C_{\mathrm{eff}}(V)$; the observable **IS** the reactance. **NOT power-matched — controlled small-signal, do not call it "matched."** Anchor: [`research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md`](../../../../../research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md):235 (§5 lock-in design), :237 (small-signal differential-$C$ principle). |
| **Vacuum birefringence / optical-activity** | EM transverse (polarization) | **MEASURE** | **Axiom 4** | reads phase $\delta n(E)$. |
| **GW-echo** | bulk longitudinal $Z_{\mathrm{bulk}}$ | **MEASURE** | **Axiom 4** | reads reflected amplitude at the saturation-$Z$ discontinuity (the bulk-sector siting question of §3.2 applies — flagged OPEN). |

**Cleave-01 is the *only* READ-mode bench in the fleet, and the *only* Axiom-2 test.** The other four
are all MEASURE-mode and all gated on **Axiom 4** (the saturation kernel). Consequence for falsification
strategy: **Ax2-fail $\neq$ Ax4-fail** — the framework can survive a *partial* falsification (Cleave
passes while Ax4 fails, or the reverse) with a clean walk-back, and this primitive makes that partition
**explicit** rather than implicit. That partition — not any single-bench result — is the canonization
payoff.

---

## 5. Derive-vs-assert ledger (`substrate-first-for-numbers`)

| Statement | Status | Where |
|---|---|---|
| Back-action $\propto \mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}}$, with **no internal-loss term** | **DERIVED** from the lossless-port energy ledger (Axiom 3) | §2, `clm-zp4kqr` |
| Per-channel boundary $\Gamma$ that sets where you couple ($Z_{\mathrm{bulk}}\to0\Rightarrow\Gamma=-1$ SHORT; $\Gamma_{\mathrm{flow}}=-\Gamma_{\mathrm{pressure}}$) | **CITED** (already in corpus — not re-derived) | §3.2 |
| READ-vs-MEASURE dichotomy | **ASSERTED (textbook)** — standard instrumentation theory | §1.2 |
| Reactive-tap rule / "minimize $\mathrm{Re}(Z)$, couple reactively" | **ASSERTED (textbook)** — standard | §1.3 |
| Loaded-vs-intrinsic $Q$ (the mode does not decay; reactive re-absorption) | **CITED** (already in corpus) | [`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md):156 |
| EM↔mechanical cross-channel probe path | **INHERITS CEILING** — goes through [`def-tk1xfm`](../../../common/vocabulary-register.md):324, `status:proposed`, "identity-by-translation NOT a derivation" | §1.1 |
| Bulk-sector coupling LOCATION (short vs rigid) | **OPEN — routed to Grant** | §3.2 🚩 |

**Symbol naming (`Z_{probe}`, the ratio name) and leaf placement are Grant-calls** — see the §1.3
proposed-symbols box and the cross-reference footer.

---

## 6. Guardrails honored (the red-team's corrections — recorded so they are not re-made)

1. **NOT "high-Z".** The rule is $\mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}} \to 0$ in
   READ-mode; $|Z|$ is a proxy that fails for any lossy high-$|Z|$ probe (§1.3, §2). ✔
2. **Bulk boundary is a SHORT, not a rigid wall.** The non-invasive bulk-read config is NOT "high-Z =
   rigid wall = pressure antinode"; AVE's confined-bulk boundary is $Z_{\mathrm{bulk}}\to0$, $\Gamma=-1$,
   a node; $\Gamma_{\mathrm{flow}}=-\Gamma_{\mathrm{pressure}}$ makes "which field you null"
   sector-dependent (§3.2). ✔
3. **MEASURE-mode is NOT "matched".** The cRIO bench is ratiometric small-signal lock-in, not
   power-matched; "controlled small-signal" is used throughout (§1.2, §4). ✔
4. **INVARIANT-N1 respected.** This is a measurement *port on the circuit MODEL*, not a new
   substrate-object noun; no new substrate glyph (scope box, §1.3 proposed-symbols box). ✔
5. **`consensus-bias-symmetric-standard` applied.** Textbook-EE parts are tagged textbook (§1.2, §1.3,
   §5 ledger); AVE-distinct parts are narrowed to the two §3 items; framed peer-mapped-honestly. ✔

---

## Quality / solidity

> **[Resultbox]** *Solidity — CONSISTENCY-class, NOT a chord (`consistency-vs-emergence`)*
>
> The derived back-action relation (`clm-zp4kqr`) is a **Class-C CONSISTENCY** result: it specializes
> standard loaded-$Q$ to a lossless medium by *removing* the internal-loss term, and predicts no new
> measurable beyond ordinary loaded-$Q$ once Axiom 3 is granted — **never headlined as emergence.**
> The fleet partition (`clm-zp7bds`) is a **design-organizing** claim (a checklist + an axiom-mapped
> mode partition), not a physics claim; its solidity reflects that it correctly classifies existing
> bench designs, not that it predicts anything. Most of the surrounding primitive is textbook EE,
> tagged as such (§6 guardrail 5).

- The `clm-zp4kqr` back-action relation builds on Axiom 3 (lossless-reactive) and the loaded-$Q$ canon
  ([`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md), `clm-rtdmsn`).
- The `clm-zp7bds` fleet partition builds on the three-impedance law
  ([`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md))
  and the READ/MEASURE-mode dichotomy.

---

## Cross-references

- **Extends:** [`resonant-lc-solitons.md`](resonant-lc-solitons.md) (matched/radiative port, loaded-$Q$,
  units discipline) · [`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md) (loaded-vs-intrinsic $Q$) ·
  [`z0-derivation.md`](z0-derivation.md) ($Z_0$, $\Gamma$ definition).
- **Channel impedances:** [`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md)
  (Grant-ratified three-impedance law).
- **Model it ports onto:** [`def-gv1net`](../../../common/vocabulary-register.md):569 (graded vacuum
  impedance network; INVARIANT-N1).
- **Bench-falsification context (back-pointer target):** Vol 4 Ch 11 hardware-falsification benches
  (Cleave-01 READ-mode exemplar; cRIO / VacuumMirror MEASURE-mode exemplars).
- **GRANT-CALLS flagged in this leaf:** (1) leaf **placement** (recommended: this directory, sibling to
  `resonant-lc-solitons.md`); (2) **symbol naming** ($Z_{\mathrm{probe}}$ + the ratio
  $\mathrm{Re}(Z_{\mathrm{probe}})/Z_{\mathrm{channel}}$, §1.3); (3) the **bulk-sector coupling
  location** open physics question (§3.2 🚩, `flag-don't-fix`).
