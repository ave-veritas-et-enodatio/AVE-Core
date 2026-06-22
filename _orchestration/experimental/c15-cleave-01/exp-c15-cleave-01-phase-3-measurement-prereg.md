[↑ C15-CLEAVE-01 sub-epic](exp-c15-cleave-01.md)

# CLEAVE-01 Phase-3 Measurement Pre-Registration (DRAFT)

**Date:** 2026-06-01
**Sub-epic:** [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md) — Phase 3 (measurement)
**Canonical claim:** `clm-ydksh6` (Axiom-2 $Q \equiv \xi_{topo}\,x$) | **Experiment node:** `exp-742kv5`
**KB leaf (frozen prediction):** [`project-cleave-01.md`](../../../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md)
**Status:** **DRAFT** — frozen at the framing / discriminator / control level; the Level-2 *quantitative* precision target finalizes at `Q-C15-02` closure (in-situ $C$) on assembled hardware (gated Phase 1b KiCad → Phase 2 fab).

This pre-registration formalizes the **measurement protocol + adjudication** for the *already-canonical* CLEAVE-01 prediction. It does **not** re-derive the prediction (frozen in the leaf, per `ave-prereg` Step 4 closed-solution rule); it **pins the discriminator to the parameter-free charge** so the readout magnitude cannot float with the board's input capacitance.

## §1 — Target

Measure the charge liberated on an isolated floating conductor when a facing grounded plate is stepped away by a controlled displacement $x$ in hard vacuum, and adjudicate against the Axiom-2 topo-kinematic prediction $Q = \xi_{topo}\,x$ versus the standard-electrostatics null $Q = 0$.

## §1.5 — Physical picture (Axiom 2, mechanical terms)

- Charge **is** topological displacement in the substrate (Axiom 2, $[Q]\equiv[L]$): a dislocation Burgers-vector count in the K4 lattice. $\xi_{topo} = e/\ell_{node}$ is the charge-per-node-length.
- Mechanically pulling the gap apart **drives the discrete substrate LC-network capacitance**; the displacement exposes topological charge natively from the spatial metric (one $e$ per $\ell_{node}$ of relative displacement, integrated over the plate's node-front).
- $\Gamma = -1$ boundary: the floating-plate/vacuum interface; the electrometer reads the node-charge **reactively** ($\theta \to 90°$, no dissipation). **Regime I** (sub-yield, $S(A)\to 1$) — far below $V_{yield}$, linear.
- Scales **linearly with displacement $x$** — NOT with the dielectric $d_{ij}$, NOT with $V^2$. The discriminator is the **4-corner conjunction** {linear-in-$x$ ∧ polarity-odd ∧ material-independent ∧ gap-INDEPENDENT} surviving a ≥4× gap-sweep (§4) — NOT the slope magnitude (the echo).
- No discrete onset at this scale: a smooth linear charge-vs-displacement (no saturation events during the PZT step; lossless).

## §2 — Corpus state: CLOSED / canonical (prediction); this doc formalizes the protocol

The prediction is canonical + frozen — **not green-field**:

- [`project-cleave-01.md:20-38`] — Axiom-2 hypothesis, $Q=\xi_{topo}x$, the 0.415 pC / 41.5 mV figures. (Round-2 cured: SM is NOT exactly 0.0 — CPD gives a gap-DEPENDENT $\propto1/g^2$ background; the chord is the gap-INDEPENDENT floor, NOT a 0.0-vs-nonzero magnitude call.)
- [`xi-topo-traceability.md`](../../../manuscript/ave-kb/common/xi-topo-traceability.md) — $\xi_{topo}=e/\ell_{node}$ canonical (51-file cross-ref); zero-free-parameter chain $\{m_e,\ell_{node}\}\to\alpha\to\xi_{topo}$.
- [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md) — sub-epic: Phases 0–1a-rev1 MERGED; `Q-C15-01…12` CLOSED (Grant); hardware in build.

Per `ave-prereg` Step 4 (closed-solution): do **not** re-derive; integrate + pin the measurement protocol.

## §3 — Dimensional analysis (canonical-primitive verification, `ave-prereg` Step 3.5)

Verified against `src/ave/core/constants.py` (imported, not hard-coded); line numbers re-verified per `verify-before-cite` on 2026-06-22:

| Primitive | Canonical value | Source (verified line) |
|---|---|---|
| $\ell_{node} = \hbar/(m_e c)$ | $3.8616\times10^{-13}$ m | `constants.py:257` (`L_NODE`) |
| $e$ | $1.602177\times10^{-19}$ C | `constants.py:100` (`e_charge`) |
| $\xi_{topo} = e/\ell_{node}$ | $4.1490\times10^{-7}$ C/m | `constants.py:291` (`XI_TOPO`) |

Forward evaluation at $x = 1\,\mu$m:
- $dQ/dx = \xi_{topo} = 4.149\times10^{-7}$ C/m $\Rightarrow$ **$Q(1\,\mu\text{m}) = 0.4149$ pC** — depends only on $\{m_e,\ell_{node},e\}$, **zero free parameters**.
- $dV/dx = \xi_{topo}/C$; at the *assumed* $C = 10$ pF $\Rightarrow$ **41.49 mV/µm** — $C$-dependent (see §4).

The **charge** slope $dQ/dx = 0.415$ pC/µm carries zero free parameters. The **voltage** slope inherits the readout capacitance $C$ — which is why the falsifiable target is pinned to charge, not voltage.

## §4 — The discriminator: the CHORD is the 4-corner gap-independent integer floor (NOT the slope)

**What the GO/NO-GO MUST gate on (the chord).** The Axiom-2 ([Q] ≡ [L]) prediction is a **topological integer charge floor**: the boundary linking charge $\mathcal{Q} = \mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ (the no-hair observable, [`boundary-observables-m-q-j.md:20`](../../../manuscript/ave-kb/common/boundary-observables-m-q-j.md)). The non-fakeable signature is the **4-corner conjunction** {linear-in-$x$ ∧ polarity-odd ∧ material-independent ∧ gap-INDEPENDENT} surviving a **≥4× gap-sweep at fixed $C_{in}$** ([`2026-06-04_round2-adjudications.md:54`](../2026-06-04_round2-adjudications.md): "NO single classical mechanism fakes all 4 corners"). SM predicts **no** gap-independent floor → the test is genuinely two-sided + non-fakeable *on the chord*. The chord is **$C$-independent at the corner level**: gap-independence is a SHAPE (flat-vs-$1/g^2$ across the sweep), measurable even before $C$ is pinned.

**What the GO/NO-GO must NOT gate on (the echo).** The 41.5 mV/µm slope magnitude (equivalently the 0.415 pC/µm charge slope) is a **consistency-class echo**, doubly over-determined: $\xi_{topo} = \sqrt{\alpha}$ in native units ([`45_lattice_impedance_first_principles.md:117`](../../../research/_archive/L3_electron_soliton/45_lattice_impedance_first_principles.md)) AND $\ell_{node} = \hbar/m_e c$ is the electron Compton wavelength. An isolated slope deviation (floor present but slope off) is therefore *also* an $\alpha$-chain signal (leaf F3 note). **A slope-match is NOT the chord and a slope-deviation is NOT a falsification.** The slope is demoted to a Level-2 secondary corroborator — it confirms the magnitude of an *already-detected* chord; it never gates GO/NO-GO.

**Level 1 — THE CHORD (gap-independence + 4-corner; the binding GO/NO-GO axis).**
Across the ≥4× gap-sweep at fixed $C_{in}$, does a charge component survive that is simultaneously (i) **linear in $x$**, (ii) **polarity-odd** (sign flips on displacement-direction reversal), (iii) **material-independent** (dielectric-invariant under gap-material swap), and (iv) **gap-INDEPENDENT** (flat across the sweep, NOT $\propto 1/g^2$)? The polarity-odd, gap-independent component is classically **0.0**; the raw vacuum charge is NOT — CPD gives a polarity-odd, gap-DEPENDENT $\propto V_{CPD}/g^2$ term (the dominant Casimir/Kelvin-probe systematic), separated from the floor by the gap-sweep. A 4-corner floor surviving the sweep is the load-bearing chord — it does not float with $C$ and is not faked by CPD or any single classical mechanism (§5).

**Level 2 — SECONDARY corroborator (parameter-free charge magnitude; needs in-situ $C$; NON-gating).**
*Given a Level-1 chord is detected*, the magnitude $dQ/dx = 0.415$ pC/µm is a secondary cross-check. The electrometer reads $V = Q/C_{\text{in-situ}}$; to compare to 0.415 pC/µm, **$C$ must be measured in-situ on the assembled board, not assumed 10 pF** — open item `Q-C15-02`. With $C$ measured, the secondary corroborator is the **charge** slope 0.415 pC/µm (drift-proof); the 41.5 mV/µm figure is the $C=10$ pF projection only. A slope offset here is an $\alpha$-chain / $\xi_{topo}$-coefficient signal (leaf F3), NOT a falsification of the chord.

## §5 — Pre-registered controls (the 4-corner machinery + mundane-faker rejection)

Frozen BEFORE measurement. The controls are not optional add-ons — each one **measures one corner of the chord**, and the GO requires all four corners conjoined (§6). The mundane-faker rejection (`2026-06-04_round2-adjudications.md:54`) is the design rationale: no single classical mechanism survives all four.

1. **≥4× gap-sweep at FIXED $C_{in}$ — the gap-INDEPENDENCE corner (round-2 cure; the corner CPD cannot fake).** Repeat the displacement-charge measurement at ≥4 different baseline gaps spanning ≥4×. The $\xi_{topo}$ floor is gap-INDEPENDENT ($e/\ell_{node}$ is a pure constant → flat across the sweep). CPD / moving-Kelvin-probe (the dominant Casimir/Kelvin-probe systematic, ~21%-of-floor and itself polarity-odd) is gap-DEPENDENT $\propto V_{CPD}/g^2$ → drops across the sweep. **$C_{in}$ MUST be held fixed across the sweep** (or explicitly accounted for) or the gap-independence corner is contaminated, because the measured *voltage* floor is gap-independent only at fixed readout capacitance (`2026-06-04_round2-adjudications.md:60`). A gap-flat floor surviving the sweep is the corner CPD provably cannot fake.
2. **Polarity reversal — the polarity-ODD corner.** Reverse displacement direction $\to$ $\xi_{topo}x$ predicts the charge sign flips. Removes the even-in-$V$ fakers at *any* magnitude: electrostriction, flexoelectric, and secondary-piezo are even in the drive field (they do not flip sign under displacement-direction reversal). A fixed-sign offset is a leakage/contact/even-faker artifact, not the chord.
3. **Dielectric-material swap — the material-INDEPENDENCE corner.** Vary the dielectric in the gap at fixed PZT displacement and fixed $C_{in}$. SM $\to Q$ varies with the dielectric's $d_{ij}$ (the piezo/tribo piece rides material); AVE $\to$ the $\xi_{topo}x$ floor is dielectric-INVARIANT (the integer linking charge is no-hair-invisible to Pauli-filled interior occupancy — gap-protected, leaf §"Node-occupation gap CLOSED"). A signal that tracks the dielectric is mundane.
4. **Linearity-in-$x$ — the linear corner.** Charge scales linearly with displacement $x$ (NOT with $V^2$, NOT with $d_{ij}$). A super-/sub-linear or $V^2$ dependence is a mundane field-driven term.
5. **Time-gating (tribo rejection).** Triboelectric contact charging produces a step that **decays** with relaxation time; the $\xi_{topo}$ floor is static. Record the relaxation profile after each step; a decaying component is tribo, removed by time-gating.
6. **Zero-displacement null**: PZT energized but zero net step $\to$ expect 0.0 (controls drive-coupling artifacts).
7. **Calibrated positive-control (anti-false-null).** Inject a known $0.415$ pC charge onto the floating electrode via a calibrated reference path in the same session. An all-null result counts as Outcome C (chord falsified) **only if** the calibration channel registers the injected charge in that same session — otherwise the null is a dead-instrument artifact (Outcome D), not a falsification. (Femto-repo `prereg.md` positive-control parity.)
8. **Guard-ring + Teflon-standoff leakage floor** (ADA4530-1, 20 fA bias): pre-register the noise floor; every corner signal must be $\ge N\times$ over it.
9. **Thermal-drift operator rule (`CLV-REQ-THERMAL`, derived $\le1$ K).** Log $\ge2$ calibrated RTDs with the data and **pause the sweep if lab temperature drifts $>1$ K** across the multi-hour $N\ge50$ acquisition. This $\le1$ K threshold is the derived operator drift-pause spec ([`cleave-01-requirements-boundary-conditions.md`](../../../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md) §6.2, `CLV-REQ-THERMAL`: Vos drift referred to the floor needs $dT_{sweep}<1.21$ K max-tempco) and **SUPERSEDES the older "$>5$ K pause" operator rule** carried in the Femto-side `TEST_PROCEDURE.md` (~4× too loose — it under-protects the chord). Landing the $\le1$ K into the Femto-side `TEST_PROCEDURE.md` is a separate-session cross-repo edit.

## §6 — Outcome bins (GO/NO-GO gates on the CHORD; slope is non-gating)

**The binding adjudication axis is the 4-corner chord, NOT the slope.** GO = the 4-corner conjunction survives the gap-sweep; NO-GO = the gap-independence corner fails (no gap-flat floor). The 0.415 pC/µm slope-match is a secondary corroborator inside Outcome A and never moves an outcome on its own.

- **A — CHORD CONFIRMED (GO)**: the 4-corner conjunction survives the ≥4× gap-sweep at fixed $C_{in}$ — a charge floor that is **linear-in-$x$ ∧ polarity-odd ∧ material-independent ∧ gap-INDEPENDENT (flat, not $1/g^2$)** — and the calibrated positive-control passed in-session. **Axiom-2 ([Q] ≡ [L]) topological-integer-charge chord confirmed at bench.** $\xi_{topo}$ cascade (B4/C9/C16/B5-7) gains bench corroboration. Foreword-promotion-grade.
  - *Secondary corroborator (non-gating):* with $C$ measured in-situ, the magnitude $dQ/dx = 0.415$ pC/µm. A match strengthens the consistency-class $\xi_{topo} = \sqrt{\alpha}$ / Compton echo; a deviation does NOT demote the GO — it books as A with an $\alpha$-chain / $\xi_{topo}$-coefficient flag (leaf F3), and routes the coefficient question to the $\alpha$-dependent rows.
- **B — partial (chord ambiguous)**: a non-zero, displacement-correlated, polarity-odd, material-independent floor is detected, BUT the gap-sweep is inconclusive (too few gaps, $C_{in}$ drift across the sweep, or floor and $1/g^2$ background not cleanly separated). The integer-charge chord is suggested but the gap-independence corner is not established. Re-run the gap-sweep at fixed $C_{in}$ with wider gap span. **NOT a GO** — the chord requires the gap-independence corner.
- **C — null (CHORD FALSIFIED, NO-GO)**: across the gap-sweep, **no gap-independent floor survives** — any displacement charge is either absent within the noise floor OR fully accounted for by the gap-DEPENDENT ($\propto 1/g^2$) CPD background — with all §5 corners checked AND the calibrated positive-control passing in-session (so the null is not a dead-instrument artifact). **Axiom-2 dies**; $\xi_{topo}$ cascade walk-back (largest single-row cascade in the matrix; F-severity). *Note: a clean slope-deviation with the floor still gap-independent is Outcome A-with-flag, NOT C — the chord, not the slope, is what falsifies.*
- **D — confound**: a floor is seen but fails a corner — tracks the dielectric (fails material-independence), fails polarity-reversal (even-faker / leakage), shows a decaying tribo component, fails the zero-displacement null, OR the calibrated positive-control did NOT register (dead-instrument null). Re-design guards / re-run; NOT adjudicated A or C.

## §7 — Falsifier

**No gap-independent integer charge floor survives the ≥4× gap-sweep at fixed $C_{in}$** — i.e. any displacement charge is either within the ADA4530-1 noise floor OR fully accounted for by the gap-DEPENDENT ($\propto 1/g^2$) CPD background — with all §5 corners checked and the calibrated positive-control (§5.7) registering the injected reference charge in the same session (so the null is not a dead-instrument artifact). This is Outcome C $\to$ Axiom 2 (hence $\xi_{topo}$) falsified at substrate-foundational level.

**NOT a falsifier:** a slope deviation from 0.415 pC/µm while the floor remains gap-independent. The slope is the over-determined $\sqrt{\alpha}$ / Compton echo (leaf F3); a slope offset routes to the $\alpha$-chain rows, it does not falsify the chord. Conversely a bare "$V$ steps at all" is NOT sufficient for a GO — CPD also steps; only the gap-INDEPENDENT 4-corner floor confirms.

## §8 — Gates / dependencies (why DRAFT, not FROZEN)

- **Phase 1b** (KiCad GUI layout — Grant) $\to$ **Phase 1c** (Gerbers) $\to$ **Phase 2** (fab + assembly, ~\$7670) $\to$ board exists.
- **`Q-C15-02`** (in-situ parasitic $C$ measurement) — closes the **non-gating Level-2** secondary-corroborator precision target ONLY. The chord GO/NO-GO (gap-independence + 4-corner) does NOT depend on $C$: gap-independence is a SHAPE measurable before $C$ is pinned. Until the board exists, $C$ is assumed 10 pF for the secondary corroborator; this prereg **freezes the chord discriminator (4-corner gap-independent floor) + the §5 controls now**, and defers the $C$-pinning of the slope corroborator to measurement-time.
- FROZEN at framing/discriminator/control level (Level-1 CHORD = 4-corner gap-independent floor + §5 controls + A/B/C/D chord-gated); the Level-2 numeric (slope) precision finalizes at `Q-C15-02` closure and is NON-gating.

## §9 — Femto-side (cross-repo) propagation status

The bench-engineering sibling repo `AVE-Bench-FemtoElectrometer` holds the hardware/test-procedure artifacts. Status as of this revision (verified read-only; the Femto repo is NOT edited in this session per cross-repo-session-scope):

- The Femto repo's OWN round-2 analysis IS cured: `docs/analysis/2026-06-04_cleave-round2-smcounterfactual-result.md` (VERDICT PARTIAL→SURVIVES with gap-sweep added; SM "exactly 0.0" found FALSE at ~21%-of-floor CPD; gap-independence cure + 4-corner table + 6-mechanism faker table) and the Femto `prereg.md` (CPD pre-test-physics question + calibrated positive-control) live on the Femto repo's **`main`**.
- **FLAG (Femto-side stale framing, SEPARATE session required):** the Femto repo's on-disk default checkout carries STALE round-1 framing in `hardware/TEST_PROCEDURE.md`, `docs/open_questions.md`, `docs/glossary.md` ("standard EE predicts Q→0"; discriminator framed as slope/linearity, NOT 4-corner). The round-2 cured `TEST_PROCEDURE.md` additions (gap-sweep + polarity-odd + positive-control as binding) exist on `main` but the cure has NOT propagated to all sites. The round-2 doc itself flags this un-landed remainder (F-R2-3). **A Femto-repo edit is needed to land the gap-independence / 4-corner / positive-control framing across the stale sites — flagged here for a SEPARATE session per cross-repo-session-scope. This AVE-Core revision does NOT edit the Femto repo.**
- The AVE-Core-side propagation (this leaf + this prereg) is what THIS revision lands; the Femto-side propagation is the tracked follow-on.

## §10 — Spend-decision package (for Grant)

A concise GO/NO-GO-on-spend summary for the ~$7.7k build commitment. This is a decision aid, not an authorization.

**What it tests.** Axiom-2 Topo-Kinematic Isomorphism ([Q] ≡ [L]): that electric charge is topological displacement in the substrate. The bench reads the boundary linking charge $\mathcal{Q} = \mathrm{Link}(\partial\Omega,\mathbf{F}) \in \mathbb{Z}$ on a floating electrode (ADA4530-1, 20 fA bias) as $V = Q/C_{in}$ while a PZT steps the gap. **The chord** = a gap-INDEPENDENT integer charge floor, the 4-corner conjunction {linear ∧ polarity-odd ∧ material-indep ∧ gap-indep} surviving a ≥4× gap-sweep at fixed $C_{in}$ — which no single classical mechanism fakes. SM predicts NO gap-independent floor → genuinely two-sided and non-fakeable on the chord.

**The GO/NO-GO (this revision).** GO = the 4-corner chord survives the gap-sweep (Outcome A). NO-GO = no gap-independent floor survives — charge absent or fully explained by the $\propto1/g^2$ CPD background — Outcome C, Axiom-2 falsified (largest single-row cascade: B4/C9/C16/B5/B6/B7 all fall; F-severity). The 41.5 mV/µm slope is an over-determined $\sqrt{\alpha}$/Compton ECHO and is a non-gating secondary corroborator only — a slope-match is NOT the chord; a slope-deviation is NOT a falsification.

**Cost / time.** ~$7,670 mid-range BOM (chamber subsystem ~$5,450 + PCBA/drive ~$1,230 + auxiliary ~$994). ~2–3 weeks fab+parts+assembly+chamber integration + ~1 week measurement+analysis.

**Build-readiness.** Phase 1a-rev1 MERGED (atopile design at Femto repo main @ `7f9c721`; HWMOD modules @ `8b0626b`). Blocker is **Phase 1b manual KiCad GUI layout** (Grant) → Phase 1c Gerbers → Phase 2 fab — NOT derivation, and NOT this prereg. The Phase-3 prereg is FROZEN at framing/discriminator/control level; the Level-2 numeric precision target finalizes at `Q-C15-02` (in-situ $C$) on assembled hardware.

**NOT cRIO-native.** This bench is independent of Grant's NI cRIO DC–40 kHz lock-in rig: it needs a dedicated vacuum chamber (≤10⁻⁶ Torr) + PZT actuator + HV amp + the ADA4530-1 electrometer board. It is a separate apparatus, not a cRIO experiment.

**Risks / open items.**
- `Q-C15-02` (in-situ $C_{in}$) — only affects the non-gating Level-2 slope precision, NOT the chord GO/NO-GO. The chord is gap-independence (a SHAPE), measurable before $C$ is pinned.
- `Q-C15-04` (parasitic $C_{in}$ tolerance), `Q-C15-06` (tribo discrimination) — OPEN, addressed by the §5 controls (fixed-$C_{in}$ gap-sweep + time-gating).
- **Femto-side stale framing (§9)** — the Femto repo's default checkout still carries round-1 slope/0.0 framing; landing the 4-corner cure across those sites is a SEPARATE-session Femto-repo edit (NOT in this AVE-Core revision).
- $C_{in}$-held-fixed across the gap-sweep is load-bearing (`:60`); a drifting $C_{in}$ contaminates the gap-independence corner → would book as Outcome B (re-run), not a false GO.

## Provenance

- Framing per `pre-test-physics-check` 2026-06-01: corpus settles the mechanism (Axiom-2 $Q\equiv\xi_{topo}x$) + the SM-0.0 counterfactual + the dielectric-independence control; **no open plumber-question**. Charge-pinning of the discriminator added to close the readout-$C$-floating seam (the leaf's "assume $C=10$ pF" $\to$ charge-based binary + quantitative).
- **Chord-gating revision (2026-06-22, this branch `bench/cleave01-chord-gated`):** the binding GO/NO-GO was re-anchored from the slope-echo (41.5 mV/µm) to the 4-corner gap-independent integer-charge chord, per `2026-06-04_round2-adjudications.md:54` (4-corner, no single classical mechanism fakes all four) + `boundary-observables-m-q-j.md:20` ($\mathcal{Q} = \mathrm{Link} \in \mathbb{Z}$) + the leaf F3 $\sqrt{\alpha}$ echo note. The round-2 framing cure (SM≠0.0; CPD gap-dependent; gap-sweep separates) was half-landed (body framing patched; bins/controls not). This revision rewrites §4 discriminator, §5 controls (gap-sweep + faker-rejection + positive-control as binding), §6 outcome bins, §7 falsifier so the chord — not the echo — gates. $C_{in}$-held-fixed subtlety embedded per `:60`.
- $\xi_{topo}$ verified against `constants.py` (`XI_TOPO:291`, `L_NODE:257`, `e_charge:100` — line numbers re-verified 2026-06-22 per `verify-before-cite`; the earlier `:246`/`:234` cites were stale-line drift, values always correct) per `ave-canonical-source`.
- Canonical prediction `clm-ydksh6` / `exp-742kv5` / `project-cleave-01.md` unchanged — this is the **protocol**, not a re-derivation.
