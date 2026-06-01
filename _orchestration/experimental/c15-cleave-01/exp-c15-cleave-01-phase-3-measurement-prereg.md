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

- Charge **is** topological displacement in $\mathcal{M}_A$ (Axiom 2, $[Q]\equiv[L]$): a dislocation Burgers-vector count in the K4 lattice. $\xi_{topo} = e/\ell_{node}$ is the charge-per-node-length.
- Mechanically pulling the gap apart **drives the discrete $\mathcal{M}_A$ LC-network capacitance**; the displacement exposes topological charge natively from the spatial metric (one $e$ per $\ell_{node}$ of relative displacement, integrated over the plate's node-front).
- $\Gamma = -1$ boundary: the floating-plate/vacuum interface; the electrometer reads the node-charge **reactively** ($\theta \to 90°$, no dissipation). **Regime I** (sub-yield, $S(A)\to 1$) — far below $V_{yield}$, linear.
- Scales **linearly with displacement $x$** — NOT with the dielectric $d_{ij}$, NOT with $V^2$. The discriminator IS the linearity-in-$x$ + dielectric-independence.
- No discrete onset at this scale: a smooth linear charge-vs-displacement (no saturation events during the PZT step; lossless).

## §2 — Corpus state: CLOSED / canonical (prediction); this doc formalizes the protocol

The prediction is canonical + frozen — **not green-field**:

- [`project-cleave-01.md:20-38`] — Axiom-2 hypothesis, $Q=\xi_{topo}x$, the 0.415 pC / 41.5 mV figures, SM $\to$ exactly 0.0 counterfactual.
- [`xi-topo-traceability.md`](../../../manuscript/ave-kb/common/xi-topo-traceability.md) — $\xi_{topo}=e/\ell_{node}$ canonical (51-file cross-ref); zero-free-parameter chain $\{m_e,\ell_{node}\}\to\alpha\to\xi_{topo}$.
- [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md) — sub-epic: Phases 0–1a-rev1 MERGED; `Q-C15-01…12` CLOSED (Grant); hardware in build.

Per `ave-prereg` Step 4 (closed-solution): do **not** re-derive; integrate + pin the measurement protocol.

## §3 — Dimensional analysis (canonical-primitive verification, `ave-prereg` Step 3.5)

Verified against `src/ave/core/constants.py` (imported, not hard-coded) on 2026-06-01:

| Primitive | Canonical value | Source |
|---|---|---|
| $\ell_{node} = \hbar/(m_e c)$ | $3.8616\times10^{-13}$ m | `constants.py:234` (`L_NODE`) |
| $e$ | $1.602177\times10^{-19}$ C | `constants.py:100` (`e_charge`) |
| $\xi_{topo} = e/\ell_{node}$ | $4.1490\times10^{-7}$ C/m | `constants.py:246` (`XI_TOPO`) |

Forward evaluation at $x = 1\,\mu$m:
- $dQ/dx = \xi_{topo} = 4.149\times10^{-7}$ C/m $\Rightarrow$ **$Q(1\,\mu\text{m}) = 0.4149$ pC** — depends only on $\{m_e,\ell_{node},e\}$, **zero free parameters**.
- $dV/dx = \xi_{topo}/C$; at the *assumed* $C = 10$ pF $\Rightarrow$ **41.49 mV/µm** — $C$-dependent (see §4).

The **charge** slope $dQ/dx = 0.415$ pC/µm carries zero free parameters. The **voltage** slope inherits the readout capacitance $C$ — which is why the falsifiable target is pinned to charge, not voltage.

## §4 — The two-level discriminator (charge-pinned)

**Level 1 — BINARY ($C$-independent; the chord/echo falsifier).**
Does $V$ step **at all** — monotonically with displacement, repeatably, in the vacuum-gap-only config? SM/linear electrostatics $\to$ **exactly 0.0** (displacing a neutral conductor in vacuum liberates no net charge). AVE $\to$ **non-zero, sign-tracking displacement**. This level needs **no** knowledge of $C$: any clean, displacement-correlated, polarity-correct step is a non-zero result; a flat 0.0 within noise falsifies. **This is the load-bearing chord/echo discriminator — it does not float with $C$.**

**Level 2 — QUANTITATIVE (parameter-free charge; needs in-situ $C$).**
$dQ/dx = 0.415$ pC/µm. The electrometer reads $V = Q/C_{\text{in-situ}}$; to compare to 0.415 pC/µm, **$C$ must be measured in-situ on the assembled board, not assumed 10 pF** — this is open item `Q-C15-02`. With $C$ measured, the falsifiable quantitative target is the **charge** slope 0.415 pC/µm (drift-proof); the 41.5 mV/µm figure is the $C=10$ pF projection only.

## §5 — Pre-registered controls (mundane-charge exclusion)

Frozen BEFORE measurement:

1. **Dielectric-independence** (rules out piezoelectric $d_{ij}$ / triboelectric — `project-cleave-01.md:40-42`): vary the dielectric in the gap at fixed PZT displacement. SM $\to Q$ varies with dielectric; AVE $\to$ the $\xi_{topo}x$ component is **dielectric-independent**. A signal that tracks dielectric is mundane, not $\xi_{topo}$.
2. **Vacuum-gap-only baseline**: the starkest single-axis config — no piezo/tribo/dielectric term for SM to hide behind.
3. **Zero-displacement null**: PZT energized but zero net step $\to$ expect 0.0 (controls drive-coupling artifacts).
4. **Polarity reversal**: reverse displacement direction $\to$ $\xi_{topo}x$ predicts the charge sign flips; a fixed-sign offset is a leakage/contact artifact.
5. **Guard-ring + Teflon-standoff leakage floor** (ADA4530-1, 20 fA bias): pre-register the noise floor; signal must be $\ge N\times$ over it.

## §6 — Outcome bins (per leaf §"Outcome adjudication", mapped to the two levels)

- **A — confirmed**: Level-1 binary non-zero AND Level-2 slope $= 0.415$ pC/µm within noise ($C$ measured). Ax2 confirmed at bench; $\xi_{topo}$ cascade (B4/C9/C16/B5-7) gains bench corroboration. Foreword-promotion-grade.
- **B — partial**: Level-1 non-zero, displacement-correlated, dielectric-independent, BUT Level-2 slope $\ne 0.415$ pC/µm. Topological charge-length identity holds qualitatively; coefficient revision needed.
- **C — null (framework-falsifying)**: Level-1 binary $= 0.0$ within noise floor, all §5 controls clean. **Ax2 dies**; $\xi_{topo}$ cascade walk-back (largest single-row cascade in the matrix; F-severity).
- **D — confound**: non-zero but tracks dielectric / fails polarity-reversal / fails zero-displacement null $\to$ mundane (piezo/tribo/leakage/outgassing). Re-design guards, re-test. NOT adjudicated A or C.

## §7 — Falsifier

A clean **0.0 mV step within the ADA4530-1 noise floor**, with all §5 controls passing (so the null is not a missed-signal artifact), per 1 µm vacuum-gap displacement $\to$ Outcome C $\to$ Axiom 2 (hence $\xi_{topo}$) falsified at substrate-foundational level.

## §8 — Gates / dependencies (why DRAFT, not FROZEN)

- **Phase 1b** (KiCad GUI layout — Grant) $\to$ **Phase 1c** (Gerbers) $\to$ **Phase 2** (fab + assembly, ~\$7670) $\to$ board exists.
- **`Q-C15-02`** (in-situ parasitic $C$ measurement) — closes the Level-2 precision target. Until the board exists, $C$ is assumed 10 pF; this prereg **freezes the charge target (0.415 pC/µm) + the Level-1 binary discriminator now**, and defers the $C$-pinning to measurement-time.
- FROZEN at framing/discriminator/control level (Level-1 binary + dielectric-independence + A/B/C/D); the Level-2 numeric precision finalizes at `Q-C15-02` closure.

## Provenance

- Framing per `pre-test-physics-check` 2026-06-01: corpus settles the mechanism (Axiom-2 $Q\equiv\xi_{topo}x$) + the SM-0.0 counterfactual + the dielectric-independence control; **no open plumber-question**. Charge-pinning of the discriminator added to close the readout-$C$-floating seam (the leaf's "assume $C=10$ pF" $\to$ charge-based binary + quantitative).
- $\xi_{topo}$ verified against `constants.py` (`XI_TOPO:246`, `L_NODE:234`, `e_charge:100`) per `ave-canonical-source`.
- Canonical prediction `clm-ydksh6` / `exp-742kv5` / `project-cleave-01.md` unchanged — this is the **protocol**, not a re-derivation.
