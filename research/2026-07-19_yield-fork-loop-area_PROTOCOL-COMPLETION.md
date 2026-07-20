# PROTOCOL-COMPLETION — Leg B of the yield-fork discriminator lane (P_phase5_memristor_loop_area)

> **SECTOR HEADER (read first).**
> - **MODE:** frozen protocol completion for a pre-registered, previously-UNRUN prediction. This document mints no claim and moves no value; it enumerates every implementer choice for measuring the memristive loop area, so the driver has zero post-hoc freedom.
> - **REGIME:** near-yield crossing, **Regime II→III** (V_SNAP-referenced three-regime convention, `k4_tlm.py:308–311`).
> - **PHASE-STATE:** driven, time-domain, at/approaching the A1 longitudinal saturation `r=V/V_SNAP→1`.
> - **DISCIPLINE:** freeze-then-run (pushed **before** driver code); engine/meter byte-UNTOUCHED; verify-before-cite (every `file:line` re-verified at worktree HEAD before writing); flag-don't-fix; Rule-11 (the frozen adjudication governs the verdict; findings do not retro-edit it).

**Date:** 2026-07-19 · **Lane:** implementer, yield-fork discriminators (Grant dispatch 2026-07-19) · **Branch:** `feat/yield-fork-discriminators`.

## 0. Why this is a standalone doc (disclosed deviation from "bottom-append")

The registered prediction `P_phase5_memristor_loop_area` lives **inside a claim-hosting KB leaf** — `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md:109` (hosts `clm-n3un96`) — and its origin derivation is `research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md` §6/§11. There is **no editable prereg document** to bottom-append to (the thixotropy prereg is Leg A only). Editing the canonical leaf to append protocol choices would be a corpus-state change in the auditor's lane and Rule-12-sensitive. So this leg's completion is frozen here, dated, referencing the registered prediction verbatim upstream. This is the honest equivalent of the bottom-append; the deviation is disclosed.

**Upstream registered prediction (verify-before-cite, re-grepped at HEAD):**
- `tau-relax-derivation.md:109`: *"$P_{phase5\_memristor\_loop\_area}$ | Loop area $= \ell_{node}^2 m_e c^2 \cdot f(\omega\tau)$ where $f$ peaks at $\omega\cdot\tau_{relax}\approx0.9$ (K4-nonlinear correction to Debye)."*
- `tau-relax-derivation.md:24,:89`: loop area `$\oint S\,dr$` = dissipated energy per cycle.
- `nonlinear-vacuum-capacitance.md:66`: the `V–I` Lissajous "passes through the origin but encloses a finite area proportional to the energy dissipated during each thixotropic yield–heal cycle" (the pinched-hysteresis plane).
- `#59` §6.2 shape `f_linear(ωτ)=ωτ/(1+(ωτ)²)` (Debye, peak exactly 1); §6.3–6.4 two-channel nonlinear correction shifts the peak to `ωτ≈0.9`; §6.4/§11 **falsification window: peak outside `[0.85,0.95]`** at the registered drive → NEITHER/artifact.

## 1. The fork adjudication this leg feeds (restated before running, per the dispatch)

Fork (`2026-07-17_regime-iv-dissipation-audit.md` §5): **finite-area memristive loop (`∮S dr≠0`, dissipative) vs zero-area saturating reactance (lossless refusal)** at the near-yield crossing. Frozen bins (verbatim):
- **ZERO area within tolerance** (tolerance = integrator floor, A.6) → **lossless-reactance branch** (Grant's reversible lean corroborated).
- **FINITE crossing-attributable area matching the P_phase5 magnitude** (nonzero **and** peak within `[0.85,0.95]`) → **memristive branch** (the lean falsified; the loop earns its resistor).
- **NEITHER** (finite but peak outside the window, or non-finite) → **fail closed** (artifact bin).

The verdict per these bins is the frozen output. The fork RULING stays Grant's (dispatch); this leg does not close it. A structural finding on what the bins do and do not license is recorded in the RESULT and routed to Grant — it does **not** retro-edit the frozen verdict (Rule-11).

## 2. Canonical kernel + integrator (byte-locked to the engine; engine byte-UNTOUCHED)

Identical to Leg A §A.2: `S_eq(r)=√(max(0,1−min(r,1)²))` (`k4_tlm.py:283`); Level-2 ODE `dS/dt=(S_eq−S)/τ_relax` integrated by backward Euler `S_{n+1}=(S_n·τ+dt·S_eq)/(τ+dt)` (`k4_tlm.py:291`); engine-native units (`τ_relax=TAU_RELAX_NATIVE=1.0`, `V_SNAP=1`, `ℓ_node=1`, `m_e c²=1`, so `r≡V/V_SNAP`, `ωτ=ω`). A pinned test asserts the driver's per-step update is **bit-identical** to a live `K4Lattice3D(use_memristive_saturation=True)` driven at one site.

## 3. Drive + operating point (registered)

`r(t)=r_0+Δr·sin(ω t)`, **`r_0=0.7`, `Δr=0.3`** (native V_SNAP units; the `#59` §6.4/§11 registered point that fixes the 0.9 peak). `dt=min(2π/ω/N_ppp, τ/50)`, `N_ppp=512`; settle `max(8 periods, 20τ)`; measure over the last full steady-state period.

Secondary (reported, not the primary adjudication point): a sub-rupture variant `r_0=0.7, Δr=0.25` (max `r=0.95`, stays below `r=1`) as a KEEP-BOTH robustness axis — checks the peak location is not an artifact of the top-of-stroke `S_eq→0` singularity (`#59` Flag C, strong-nonlinear in-cycle partial yielding). The primary adjudication uses the **registered** `Δr=0.3`.

## 4. ω-sweep + the two registered planes

Sweep `ωτ` over `logspace(log10(0.05), log10(10), 60)`. At each `ωτ` measure, on the last steady-state period:
- **Plane 1 — (r,S) [`tau-relax-derivation.md:24` plane, primary]:** `A_rS(ω) = |∮ S dr| = |∫ S (dr/dt) dt|` (trapezoid on the closed loop).
- **Plane 2 — (V,I) pinched Lissajous [`nonlinear-vacuum-capacitance.md:66` plane, cross-check]:** native `V=r`, current under Op14 `I = V/Z_eff = r·√S` (`Z_eff=Z_0/√S`, `Z_0=1` native); `A_VI(ω)=|∮ I dV|`. Verify the loop **pinches through the origin** (`I=0` at `r=0` — record min `|V|,|I|` reached; the registered qualitative signature).

The **peak** `ωτ*` is located from the (r,S)-plane sweep (the plane the P_phase5 magnitude is stated in). Both planes' peak locations are reported.

## 5. Magnitude comparison to P_phase5

`∮ S dr` is dimensionless (S, r dimensionless). The prediction `A_loop=ℓ_node²·m_e c²·f(ωτ)` fixes the **physical** units via the native energy·length² unit (`ℓ_node²·m_e c² = 1` native), with `f` the dimensionless shape. "Matching the P_phase5 magnitude" is therefore operationalized as **(i) peak location `ωτ*∈[0.85,0.95]`** (the falsifiable content, `#59`§11) **AND (ii) the measured shape tracks the two-channel `f` (Eq 6.3)** to within the reported residual. The absolute prefactor `ℓ_node²·m_e c²` is a unit identity (stated, not independently "measured" by a dimensionless loop) — disclosed, not a fudge.

## 6. Zero-tolerance derivation (integrator floor)

Both analytic zero-area limits are computed to fix the numerical floor:
- Quasi-static `ωτ=1e−3`: `S→S_eq(r)` exactly ⇒ `∮ S_eq dr = 0` (state function). Residual `ε_qs`.
- Frozen `ωτ=1e3`: `S→const` ⇒ `∮ ≈ 0`. Residual `ε_fr`.

**`tol = 10 · max(ε_qs, ε_fr)`** (one order-of-magnitude safety over the worst analytic-zero residual). Frozen. `A_rS(ω) ≤ tol` ⇒ ZERO-area bin; `> tol` ⇒ finite. `tol` is exported to Leg A §A.6 (identical numerics).

## 7. Gates (fail-closed, checked FIRST)

- **Regime gate:** the registered drive must reach Regime III (`max r ≥ √3/2`). At `r_0=0.7,Δr=0.3`, `max r=1.0` ✓.
- **Finite gate:** any non-finite state at any swept `ωτ` → that point banks **INSTRUMENT** (blow-up = instrument), excluded from the peak fit; if the whole sweep is non-finite → leg banks INSTRUMENT-DEAD (not a verdict).
- **Byte-match gate:** driver kernel must be bit-identical to the live engine's memristive update (§2) or the leg does not run (CANNOT-RUN-AS-FROZEN).

## 8. What Leg B does NOT decide (the structural finding routed to Grant)

The frozen bins equate "finite `∮`" with "dissipative." A first-order **overdamped** relaxation (Eq 2.1, as written) produces `∮S dr≠0` **by its own structure** — that is elementary Debye lag, not independent evidence of an axiom-sourced resistor. Whether the same `τ_relax=ℓ_node/c` lag is a *dissipated-work* loop (Eq 2.1 first-order, overdamped) or a *reversible reactive* lag (a second-order kinetic-`S` form, `I_S≠0`) is exactly **`#59` Flag F** (§12: *"'Ax3 overdamped-action limit gives the first-order relaxation ODE' is asserted but not derived rigorously"*) and the audit's ★ no-axiom-sourced-resistor flag (F2). This leg RUNS Eq 2.1 as frozen and reports the bin; the RESULT additionally reports the H-ledger and a clearly-labeled *reactive second-order contrast* to make the fork's true locus (Flag F, upstream of the measurement) crisp for Grant. This is a disclosed finding, not a retro-edit of the frozen verdict.

---

## POST-FREEZE CORRECTIONS — 2026-07-19 (implementer lane, review `wf_f0870d0d`)

**Rule-12 append.** The frozen §0–§8 body above is preserved as-written. These are corrections/disclosures found by the post-run review; they do **not** retro-edit the frozen verdict (Rule-11).

**C-1 (R-5 finding 11) — the "(verbatim)" provenance on the frozen bins is over-stated.** §1's "Frozen bins (**verbatim**)" is only partly accurate:
- **Genuine, verbatim upstream:** the falsification **window `[0.85,0.95]`** is quoted verbatim from `#59` §11 / `59_memristive_yield_crossing_derivation.md:635` ("*measured peak outside [0.85, 0.95] … → different axiom-derivation required*"). Re-verified at HEAD.
- **Minted in this completion doc (NOT verbatim upstream):** the **three-bin structure**, the **`NEITHER` label**, and the **conjunction** ("nonzero **AND** peak within `[0.85,0.95]`" for the memristive bin) are this doc's operationalization of the `2026-07-17` §5 fork record — they are a reasonable frozen construction, but they were authored here, not quoted from `#59`. The "(verbatim)" tag should be read as applying to the *window* only.

**C-2 (R-2, clause-(ii) never ran) — the "shape-tracks-Eq-6.3" criterion was not evaluated.** §5 operationalized "matching the P_phase5 magnitude" as **(i)** peak location `ωτ*∈[0.85,0.95]` **AND (ii)** the measured shape tracks the two-channel `f` (Eq 6.3) to within the reported residual. **Only clause (i) ran.** The driver never fit the measured loop-area shape against Eq 6.3 (clause (ii)) — an **undisclosed deviation**, now disclosed. It is **verdict-invariant**: clause (i) already delivers NEITHER, and (see the RESULT F-B1) the whole (r,S)-plane comparison is information-free anyway, and Eq 6.3's own peak at the registered drive is `~0.954–0.978`, not the registered `0.9`.

**C-3 (R-3, second-order contrast never ran) — SPEC'd, not delivered.** §8 promised the RESULT would report "*a clearly-labeled reactive second-order contrast*." **It never ran** — there is no second-order kinetic-`S` integration in the drivers, and (per the RESULT F-B3 correction) an earlier claim that a second-order form gives "the same τ-lag" is **retracted as FALSE** (a lossless second-order kinetic-`S` is resonant, not Debye). The Flag-F relocation therefore rests on the **model-tautology leg only** (this driver integrates first-order Eq 2.1 on itself, so it cannot distinguish first- from second-order). **SPEC for the Flag-F derivation branch:** integrate `d²S/dt² + γ·dS/dt + ω_S²(S − S_eq) = 0` in the undamped (`γ→0`) lossless limit on the identical registered drive; compare its (r,S)/(V,I) loop shape, peak location, and H-ledger against first-order Eq 2.1. That contrast is what makes the first-vs-second-order distinction empirically crisp; a driver that only runs Eq 2.1 cannot.
