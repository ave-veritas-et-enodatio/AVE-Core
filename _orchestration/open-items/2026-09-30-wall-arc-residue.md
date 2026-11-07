---
id: wall-arc-residue
title: "R61 park residue, wall arc: evidence for the A1-vs-T2 wall question, polish residue, and the items that die with the parks"
status: OPEN
owner: lane
opened: 2026-11-01
source: _orchestration/docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md
anchor: "The A1-vs-T2 wall contradiction becomes one two-sided question for a later sitting."
---

What R61 keeps from the wall arc when #1021, #1023 and #1025 park. Each park is preserved at an annotated archive tag. Nothing here corrects, re-grades or adjudicates canon.

## Evidence for the A1-vs-T2 wall question (recording only; not a Grant ask; nothing is corrected)

**The question:** which wall confines the single electron: the A1 mass wall, the T2 self-trap wall, or each a different channel? It already has a home, open PR #1040's item `cage-ownership-provenance`, which is not yet on main. This section records seeds for that item, to be merged into `cage-ownership-provenance` when #1040 lands. It states both sides and asserts neither.

Cross-link: `_orchestration/open-items/2026-08-25-invariant-s2-sector-split.md`. Neither item is edited here.

The reopen trigger for #1023 and #1025 is Grant's answer to that question.

### Side A

From `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md`, verbatim in LaTeX source form. The sentence was written 2026-06-19 (commit `3b09e895`).

```markdown
> **Two coincident $\Gamma=-1$ walls — do NOT re-collide.** The confinement surface is the **A1 MASS wall** ($Z_{\mathrm{bulk}}\to0$, the impedance-short $\Gamma=-1$ of the Pauli/TIR derivation). It is numerically coincident with — but a **DISTINCT object** from — the **$\Gamma_{\mathrm{spinor}}=-1$** topological $2\pi\to4\pi$ stability wall of the T2 micro-rotation sector ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):89-94; $A1\perp T2$ per [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20, Grant-ratified). The electron carries BOTH; the confinement surface terminating the **bulk** channel is the MASS one only. Reading the two $-1$'s as one wall would wire the cage into the charge-winding and break the two-"3"s orthogonality.
```

The `def-cf1srf` block in `manuscript/ave-kb/common/vocabulary-register.md`, verbatim:

```markdown
## confinement surface
<!-- id: def-cf1srf -->

- **term:** confinement surface
- **adjudicated-meaning:** the $\Gamma=-1$ cage-wall $\partial\Omega$ that terminates the bulk channel of a `BoundResonator`, whose **SHAPE is FORCED by topology** — the real-space body + the phase-space winding + the node-span — and is therefore **DERIVED, never posited-spherical** (Grant D4). The electron ($0_1$ unknot) and the proton ($6^3_2$ Borromean, multi-node) get DIFFERENT derived shapes.
- **axis:** real-space (a closed 2-surface in the substrate); its shape is set jointly with the phase-space winding label.
- **dimension/type:** a closed orientable 2-surface (geometry); the impedance condition on it is $Z_{core}\to0\Rightarrow\Gamma_{bulk}=-1$ (dimensionless reflection coefficient).
- **status:** proposed — status OPEN: the shape-forcing CHAIN is not derived (no solved boundary-value problem produces the electron's surface from its topology; the proton single-vs-multi-node confinement is UNADJUDICATED). The $\Gamma=-1$ TIR condition itself is canonical (clm-kezk9z, T3.3 `sup-1ecv2m`); the SHAPE is the open object.
- **canonical-home:** `vol9/ch3-pin-port-configuration/device-circuit-models.md` §6.2; the underlying $\Gamma=-1$ TIR wall is canonical at `resonant-lc-solitons.md:25-52`.
- **clm-cross-links:** *(none — gate-register reference; the wall claim is clm-kezk9z)*
- **open-ambiguity-flag:** YES — **two coincident $\Gamma=-1$ walls guard.** The confinement surface is the **A1 MASS wall** ($Z_{bulk}\to0$, the impedance-short $\Gamma=-1$). It must NOT be re-collided with the **$\Gamma_{spinor}=-1$** topological $2\pi\to4\pi$ stability wall of the T2 micro-rotation sector — these are numerically coincident at $-1$ but **distinct objects** ($A1\perp T2$, `master-equation.md:20`, `resonant-lc-solitons.md:89-94`). The electron carries BOTH; the confinement surface is the mass one only.
  - conflicting sites: the two-$\Gamma$ Resultbox `resonant-lc-solitons.md:89-94`; the A1$\perp$T2 anchor `master-equation.md:20`; the boundary-observable surface $\partial\Omega$ `common/boundary-observables-m-q-j.md:29`.
- **verification:** VERIFIED the $\Gamma=-1$ TIR confinement at `resonant-lc-solitons.md:38,47-50`; VERIFIED the A1-mass-wall vs T2-spinor-wall distinction (both $-1$, not the same wall) at `resonant-lc-solitons.md:89-94` + `master-equation.md:20`; VERIFIED the electron $0_1$-unknot vs proton-Borromean real-space bodies at `common/boundary-observables-m-q-j.md:43-44`. OPEN — shape-forcing chain not derived.
```

### Side B

The `def-vyvsn1` block in `manuscript/ave-kb/common/vocabulary-register.md` as it stands on `origin/main`, verbatim. The 2026-06-30 attribution of its confining clause is disputed by #1040, which removes that clause.

```markdown
## V_yield / V_snap *(SOLID — adjudicated T2, Grant 2026-06-30)*
<!-- id: def-vyvsn1 -->

- **term:** V_yield / V_snap (the two Axiom-4 saturation thresholds)
- **adjudicated-meaning:** two voltage thresholds on the Axiom-4 saturation kernel, in **two orthogonal sectors** ($A_1 \perp T_2$). **$V_{\text{yield}} = \sqrt{\alpha}\cdot V_{\text{snap}} \approx 43.65$ kV** = the **transverse Cosserat ($T_2$) self-trap wall** (Grant 2026-06-30 ruling): the transverse micro-rotation crosses Axiom-4 onset, $\Gamma\to-1$, and the single-electron confining $\Gamma=-1$ TIR cavity self-creates here. **$V_{\text{snap}} = m_e c^2/e \approx 511$ kV** = the **longitudinal $A_1$ sector fully saturates** ($A^2=1$, $Z_{\text{core}}\to0$, the A1 varactor bond compliance $C_{\text{eff}}=C_0/S$ diverges HERE); this is the mass-completion + Schwinger / pair-nucleation energy. **The A1 mass channel does NOT saturate at $V_{\text{yield}}$** — it saturates at the $1/\sqrt\alpha\approx11.7\times$-higher $V_{\text{snap}}$.
- **axis:** sectoral saturation thresholds (transverse-T2 self-trap onset vs longitudinal-A1 completion)
- **dimension/type:** voltage (both); BOTH are **CALIBRATION, not derived** ($V_{\text{snap}}\equiv m_e c^2/e$ definitional with $m_e$ in voltage units; $V_{\text{yield}}\equiv\sqrt{\alpha}\cdot V_{\text{snap}}$, the $\sqrt{\alpha}$ being the imported $\alpha$-echo). `src/ave/core/constants.py:455` (V_SNAP), `:464` (V_YIELD).
- **status:** SOLID — adjudicated (Grant 2026-06-30). The formerly-BLOCKING grade-attribution fork is RESOLVED = T2: $V_{\text{yield}}$ is the transverse-$T_2$ self-trap wall; the longitudinal-A1 compliance bound is at $V_{\text{snap}}$. Canonized in prose at `pair-production-axiom-derivation.md:93-104` (T2 horn) and reconciled at `nonlinear-vacuum-capacitance.md:16` (A1 horn re-keyed to $V_{\text{snap}}$).
- **canonical-home:** `pair-production-axiom-derivation.md:93-104` (sectoral prose, Grant 2026-06-30 T2 ruling); `nonlinear-vacuum-capacitance.md:16` (A1 varactor keyed on $V_{\text{snap}}$); `src/ave/core/constants.py:455,:464` (calibration); the electron-binding derivation `research/2026-06-30_electron-portmap-derivation_result.md` §5.
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** **PARTIAL — the sector fork (2) is RESOLVED; the α-lock (1) STANDS as an honest caveat.** **(1) ALPHA-LOCK, not two free thresholds (STANDS):** $V_{\text{yield}}/V_{\text{snap}} = \sqrt{\alpha}\approx0.0854$ EXACTLY (`constants.py:464`). They are NOT two independent per-sector thresholds — the transverse-$T_2$ onset sits at $\sqrt{\alpha}$ of the longitudinal-$A_1$ scale. Do NOT import "one free threshold per sector"; the $\sqrt{\alpha}$ relation is itself a VALUE-level $\alpha$-echo. **Consequence of the ruling:** the electron's A1 mass core operates at strain $A=V_{\text{yield}}/V_{\text{snap}}=\sqrt\alpha$ — an $\alpha$-echo operating point (Class-C), sub-saturated ($S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$), which is why the mass channel does not run away. **(2) sector-attribution fork — RESOLVED = T2 (Grant 2026-06-30):** the earlier conflict — KB leaf `nonlinear-vacuum-capacitance.md:16` had the $V_{\text{yield}}$ varactor on the LONGITUDINAL-A1 bond compliance, while `constants.py` + `pair-production-axiom-derivation.md:102` put $V_{\text{yield}}$ on the TRANSVERSE-$T_2$ self-trap — is now settled: **$V_{\text{yield}}$ is the T2 wall**; the A1 varactor's divergence was re-keyed to $V_{\text{snap}}$, removing the conflict. **(3) keep DISTINCT** from the C_eff/ε_eff saturation-reactance sector split at `ave-kb/CLAUDE.md:73` (a different object — the saturation reactances, not the two-event threshold ladder).
- **verification:** VERIFIED the Grant 2026-06-30 T2 ruling landed in prose at `pair-production-axiom-derivation.md:93-104`; VERIFIED the A1-horn reconciliation (varactor re-keyed $V_{\text{yield}}\to V_{\text{snap}}$) at `nonlinear-vacuum-capacitance.md:16`; VERIFIED the calibration definitions at `constants.py:455,:464` and the $V_{\text{yield}}=\sqrt{\alpha}\cdot V_{\text{snap}}$ alpha-lock ($\sqrt\alpha=0.0854$). Status SOLID — fork (2) resolved, α-lock (1) retained as caveat. See `research/2026-06-30_electron-portmap-derivation_result.md` + `research/2026-06-24_engine-reroute-epic-summary.md`.
```

## Polish residue

- **T3.3 off the operating point (#1025).** `sup-1ecv2m` was probed at A = 0.95 and 0.99, while the electron's A1 core sits at A = √α (`def-vyvsn1`). `device-circuit-models.md` cites T3.3 as support (search `T3.3`). Recomputed for this item with the `gamma_bulk` route in `src/ave/core/crystal_engine.py`, `Z_eff = S^(1/2)` and `Γ = (Z_eff − 1)/(Z_eff + 1)`, using `ALPHA` from `src/ave/core/constants.py`: at A = √α, S = 0.9963446, Z_eff = 0.9981706 and **Γ_bulk(√α) = −9.155e-4**. The same route returns −0.283 at A = 0.95 and −0.454 at A = 0.99, matching the T3.3 row. Source: `archive/research/2026-08-26-virtual-neutral-arc:research/2026-08-26_virtual-neutral-boundary-arc_RECORD.md`.
- **W4-4 (#1021).** `manuscript/ave-kb/vol2/appendices/app-b-paradoxes/peierls-nabarro-paradox.md` says the moving electron is matched (search `co-moving self-matched envelope`). `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` says it is a Γ = −1 mismatch (search `permanent macroscopic`). This records the pair and rules nothing. Source: `archive/research/2026-08-26-wall-first-walk:research/2026-08-26_wall-first-and-trefoil-propagation-walk_RECORD.md`, row W4-4.
- **R-2 (#1021).** Is `cosserat-mass-gap.md`'s "T2/ω" the same object as `port-register.md`'s "channel 4 (micro-rot.)"? Source: `archive/research/2026-08-26-wall-first-walk:_orchestration/open-items/2026-08-26-electron-rest-energy-channel.md`.
- **VN-F1, restated (#1023).** The `S_min=0.05` floor in `src/ave/solvers/vacuum_varactor_scatter.py` is "unreachable at the default cap, reachable via an A_cap override", not "dead code". Source: `archive/research/2026-08-26-virtual-neutral-prereg:research/2026-08-26_virtual-neutral-vs-saturation-wall_prereg_FROZEN.md`, row VN-F1.
- **VN-F4, third site (#1023), fixed under R63 (#1080).** `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:207` cited `gamma_mag_sq_leak` at line 161 of `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`, and the function is defined at line 170 of that file. The live sites were three. The wave-1 cite fix covered `electron-bound-resonator-coverage.md` and `theorem-3-1-q-factor.md`, under `_orchestration/docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md:33`: "the VN-F4 line-number cite fix in two KB leaves". R63 (#1080) extends that fix to this third leaf, which now reads "(`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`:170 `gamma_mag_sq_leak`)", the same one-token edit in the leaf's backticked form. Source: `archive/research/2026-08-26-virtual-neutral-prereg:research/2026-08-26_virtual-neutral-vs-saturation-wall_prereg_FROZEN.md`, row VN-F4.
- **VN-F5 (#1023).** The scalar `solve_tone` accepts `term=None` and returns the trivial zero as converged (`src/ave/solvers/harmonic_balance_srs.py`, search `def solve_tone`). This is already routed by R58 §4 (`_orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md`, search `non-triviality gate`). Cross-link only; it is not re-routed here.
- **The parked virtual-neutral register-move line.** Should the electron row move from boundary register 1 (AMPLITUDE LEVEL-SET) to register 4 (BALANCE LOCUS)? The line parks with both tags: `archive/research/2026-08-26-virtual-neutral-arc` and `archive/research/2026-08-26-virtual-neutral-prereg`.

## Open items that die with the parks

Each was re-read on its branch.

- #1021 `electron-rest-energy-channel`: dropped, because its content is already canon (`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`, search `SECTOR RE-SCOPE`). Its R-2 is carried above.
- #1021 `electron-rest-energy-channel`, R-1 and R-3: both stay recorded at `archive/research/2026-08-26-wall-first-walk:_orchestration/open-items/2026-08-26-electron-rest-energy-channel.md`. R-1 is not in the cite above: it stays attached to the R40-B2a debt, not tracked separately, as that item's Disposition recommends. R-3 stays a standing tag: the rest-energy answers are identity-class by their own leaves' words.
- #1021 `wall-first-reframe-audit`: dropped, because the record parks and its lead item W1-1 is answered in the `src/ave/solvers/harmonic_balance_srs.py` docstring (search `T2/Cosserat channel is NOT`; the sentence wraps onto the next line).
- #1023 `prereg-control-termination`: dropped. The prereg parks, and the reopen trigger is above.
- #1025 `device-circuit-models-165-correction`: folded into this item. Side A shows the line asserts the A1 mass wall and does not prohibit it, and the canon tension that item registered is the wall question above.
- #1025 `virtual-neutral-register-move`: folded into this item, as the register-move line above.
