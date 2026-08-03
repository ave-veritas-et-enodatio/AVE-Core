[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-cltls0]
exp-id: exp-71uhr0
status: pending
strengthens:
  - clm-cltls0: 1.0
-->

> 🔴 **PER-NODE / APPARATUS-VOLTAGE CORRECTION (2026-08-01 — propagation of the 2026-06-04 per-node
> adjudication to this leaf; Rule 12, body preserved below unedited, git is the trail).**
>
> **The conflation.** The Falsification Criteria below read the **apparatus** voltage (the 80 kV Marx
> transient across the electrode standoff) as if it were the **per-node** Axiom-4 kernel argument
> $A_0$. It is not. $V_{yield} \approx 43.65$ kV is the voltage across **ONE** node
> $\ell_{node} = 0.386$ pm — i.e. the yield **FIELD** $E_{yield} = V_{YIELD}/\ell_{node} \approx
> 1.13\times10^{17}$ V/m — **not** a terminal voltage. The per-node operating point is
> $A_0 = E_{local}\,\ell_{node}/V_{YIELD}$.
>
> **The arithmetic at this config.** 80 kV across a 1 mm standoff ⇒ $E_{local} = 8.0\times10^{7}$ V/m ⇒
> $A_0 \approx 7.1\times10^{-10}$ — about **8.2 orders of magnitude below** the proportional-limit knee
> $R_I = \sqrt{2\alpha} \approx 0.1208$ (`src/ave/core/constants.py` `R_I`). Reaching $A_0 = 1$ across
> even a 1 µm gap needs **~113 GV**. The lattice sits deep in Regime I at the specified drive.
>
> **Scale reference (engineering choice, not leaf-specified).** The **1 mm standoff is a representative
> laboratory engineering reference**, not a leaf parameter — the Test Protocol below specifies only an
> *"encapsulated, highly polished, symmetrical spherical electrode"* and fixes no gap. Geometry enters
> through the Q-G42 field-concentration factor
> ($V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$); the **polished-sphere** specification
> pins that factor at the un-enhanced end, $G_{geom} \approx 1$ (no tip enhancement) — the *conservative*
> reading in the sense that it assumes no geometric help. **The conclusion is not sensitive to the
> choice:** granting the geometry every benefit at once — a sharp-tip enhancement of $10$–$10^2$ *and* a
> $1\,\mu$m gap ($10^3$) — still leaves $A_0 \lesssim 7\times10^{-5}$, $\gtrsim 3$ OOM below the $R_I$
> knee. Restating any bench-reachable threshold honestly requires performing that Q-G42
> apparatus→substrate step, which this leaf does not do.
>
> **Consequence (regime discipline).** No "Avalanche Knee" is predicted at 43.65 kV of *apparatus*
> volts, and **a null on this bench is an artifact-of-regime, not a falsification of Axiom 4** — the
> effect cannot exist at the drive specified. What survives is the Zener/TVS **mechanism** (the
> substrate does clip at its own yield *field*) and the displacement-current-vs-linear-charging
> signature — realizable only at facility-class **local** fields, not at bench terminal volts.
>
> **Provenance.** 2026-06-04 per-node adjudication:
> [`research/2026-06-04_corrections-walkback-pernode-result.md`](../../../../../research/2026-06-04_corrections-walkback-pernode-result.md)
> work-item #3 (ledger `_orchestration/experimental/2026-06-04_round2-adjudications.md` §3). Applied-banner
> template = [`vacuum-impedance-mirror.md`](vacuum-impedance-mirror.md) (its 2026-06-04 RE-SCOPED box).
> Reading-hazard discipline: [`vol4/claim-quality.md`](../../claim-quality.md) ($V_{yield}$-vs-$V_{snap}$
> + per-node-vs-apparatus); Q-G42 apparatus-vs-substrate template
> $V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$ (`trampoline-framework.md:465` — ★cite-**shift** repair 2026-08-02, framing corrected 2026-08-03: this banner inherited `:439` from the walk-back doc's template cite — `research/2026-06-04_corrections-walkback-pernode-result.md` (`1f3e7b8f`), where `:439` **was** the template sentence byte-for-byte on 2026-06-04. It then shifted: `:455` 2026-06-05, `:457` 2026-06-13, `:459` 2026-06-20, `:461` 2026-07-02, `:465` 2026-07-03→HEAD. This banner was itself written 2026-08-02 (`6afe3749`), so **for this leaf the defect is inherited-stale, not shift-under-the-citer** — the upstream cite was correct at its own date, the copy was already stale at its own. The 2026-08-02 wording *"`:439` … never carried the template"* was historically false and is **withdrawn**. Content-primary target `:465`; the block explicitly **headed** *"The $V_{yield}$ apparatus-geometry-scaling (Q-G42)"* is at `:730`).

## Project ZENER-04: The Impedance Avalanche Detector

**The Hypothesis:** The vacuum LC network acts identically to a Transient Voltage Suppression (TVS) Zener diode. It behaves as a rigid $Z_0 \approx 377\,\Omega$ transmission line until the topological voltage exceeds $V_{yield} = \sqrt{\alpha} \times V_{snap} \approx 43.65\,\text{kV}$, at which point its inductive capacity saturates and it undergoes **Absolute Impedance Rupture** ($\Gamma = -1$).

**The Test Protocol:** Design a multi-stage Marx Generator PCBA capable of generating an $80\,\text{kV}$ transient spike with a sub-microsecond rise time. Terminate the pulse into an encapsulated, highly polished, symmetrical spherical electrode to prevent classical atmospheric arc-over.

**Falsification Criteria:** Monitor the input displacement current ($I_D$) and topological voltage ($V$). In standard electromagnetics, charging an isolated spherical capacitor yields a perfectly linear charging curve ($I_D = C \frac{dV}{dt}$). AVE strictly predicts that the moment the localized field crosses the $43.65\,\text{kV}$ Impedance Rupture limit, the effective transmission line impedance of the surrounding spatial vacuum drops to zero. The oscilloscope will display a distinct, anomalous "Avalanche Knee" — a sudden non-linear spike in displacement current as the vacuum lattice physically undergoes dielectric breakdown.

---
