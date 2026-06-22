[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "OPEN decision-space record — CLEAVE-01 make-vs-buy + design-knob worked option sets; STATUS:OPEN throughout; SELECTS NOTHING; not a physics claim. The derived physics lives in the sibling requirements leaf (clm-fuajdb)."
experiments: [exp-742kv5]
-->

## CLEAVE-01 Trade Study / Decision Register (STATUS: OPEN throughout)

> **THIS IS A DECISION RECORD, NOT A CLAIM.** This document carries `no-claim` in its frontmatter by design: it asserts **no physics**. It is an **open decision-space record** of every CLEAVE-01 make-vs-buy and design-knob as a fully-worked option set — options, derived tradeoffs (including build-feasibility given the team), and dependencies — each ending in **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.** The derived, frozen, solidity-tagged boundary conditions are in the sibling [`cleave-01-requirements-boundary-conditions.md`](cleave-01-requirements-boundary-conditions.md) (`clm-fuajdb`); the open Q-C15 design decisions are registered in [`exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md). **Derived = there (a claim). Open = here (a decision-record). The separation is unmistakable: this leaf is `no-claim`.**

**Team-awareness inputs (carried into every build-feasibility cell, NOT a selection):**
- **Grant** — staff EE (Tesla Megapack thermal); can build the femto-amp PCB, the PZT-drive / HV-class board, and the thermal control; owns an NI cRIO-9014 + 9263 (AO) + 9215 (AI) = a DC–40 kHz 4×4 phase-coherent lock-in bench.
- **Collaborator** — scrappy, high-quality vacuum chambers + fixturing.
- **Buy-side (precision metrology the team does NOT self-build):** closed-loop nanopositioner + capacitive gap sensor ($\ge300$ µm, pm-class), the charge-cal reference, pump/gauge, and the precision readout digitizer.

**Cost is OUT OF SCOPE here** (adjudicated separately); these are make-vs-buy *feasibility-and-fit* tradeoffs, not a BOM roll-up.

## Part A — MAKE-vs-BUY per subsystem (team-aware option sets)

### A1 — Femto-amp PCB (ADA4530-1 front-end + guard ring + Teflon standoffs)
- **Builds to REQ-IDs:** `CLV-REQ-READOUT` (§3 the charge-readout chain), `CLV-REQ-CPL-D` (the bias-ramp bleed topology the feedback network must implement), `CLV-REQ-EMI` (guard ring + guarded triax), `CLV-REQ-CAL` (the floating-node where the charge-injection reference is read).
- **Options:** (a) MAKE — Grant lays out + builds the PCB (atopile/KiCad already merged Phase 1a-rev1). (b) BUY — order assembled / use EVAL-ADA4530-1RZ as-is.
- **Derived tradeoffs:** The front-end is the ONE design-complete subsystem (equipment-audit verdict 1: ADA4530-1 unity-gain follower + Pin-4 guard + PTFE turret posts is textbook-correct, fit-for-purpose). MAKE is squarely in Grant's wheelhouse (staff EE); the guard-ring + Teflon-standoff discipline is the load-bearing skill and is already captured. BUY adds little since the front-end is solved; the EVAL board is a fast bring-up path but does not carry the floating-plate / vacuum-feedthrough integration.
- **Dependencies:** the readout-topology knob (D3) — a charge-reset integrator changes the front-end feedback network, so freeze D3 before final layout.
- **STATUS: OPEN — decision pending (Grant + collaborator). Leaning MAKE is *recorded as a leaning, not a selection.***

### A2 — PZT-drive / HV-class board (DAC + piezo amp + driven shield + return)
- **Builds to REQ-IDs:** `CLV-REQ-PZT` (§5 the whole drive chain — drive-noise mechanical + electrostatic paths, synchronous-step confound, DC stability, range), couples to `CLV-REQ-VIB` (drive noise → gap jitter via the 41.49 nV/pm path) + `CLV-REQ-GAP` (drive + stage are ONE closed-loop problem, §5.4).
- **Options:** (a) MAKE — Grant builds the bipolar drive amp + a switchable sub-Hz–~165 Hz post-filter + a driven shield electrode. (b) BUY — a closed-loop servo controller (PI E-625/E-709-class) that bundles 20-bit DAC + low-noise amp + cap-sensor input.
- **Derived tradeoffs:** This is the only HV-class chain (NO field bias exists — §2.3 of the requirements leaf). MAKE fits Grant's HV-board skill and the requirement is forgiving: the 1 µm step needs only ~10–50 Hz BW, so a free passive post-filter drops the drive noise below the 29 µV mechanical-path budget (§5.1). BUY is attractive ONLY because the drive and the stage are ONE closed-loop problem (§5.4) — if D6 (gap-metrology) goes closed-loop-servo, that controller subsumes the discrete drive and A2-MAKE collapses into A6-BUY. The driven-shield (to hold $C_c\le10$ fF, §5.2) is UN-BUDGETED in the baseline and is a MAKE design task either way.
- **Dependencies:** tightly coupled to A6/D6 (closed-loop stage) — do NOT freeze A2 before D6.
- **STATUS: OPEN — decision pending (Grant + collaborator).**

### A3 — Thermal control (shroud + RTD logging, ~1 K over the sweep)
- **Builds to REQ-IDs:** `CLV-REQ-THERMAL` (§6.2 the derived $dT\le1$ K over the sweep + 2× calibrated RTDs logged — the canonical operator drift-pause threshold). Low-CTE fixturing (§4.6 thermal gap drift, part of `CLV-REQ-GAP`) is an A4/D5 material choice, not here.
- **Options:** (a) MAKE — Grant builds an insulated shroud + 2× calibrated RTD logging (his Tesla-thermal domain). (b) BUY — a temperature-stabilized enclosure.
- **Derived tradeoffs:** The derived spec is $dT\le1$ K (§6.2), the loosest of the four environment specs and explicitly NOT the binding systematic. MAKE is trivially in Grant's wheelhouse and ~1 K is achievable with an insulated shroud or a stable room. BUY buys nothing the team can't make. (Low-CTE Invar/Zerodur fixturing — a ~20× thermal-gap relaxation, §4.6 — is a fixturing material choice that belongs to A4/D5, not here.)
- **STATUS: OPEN — decision pending (Grant + collaborator). Leaning MAKE.**

### A4 — Vacuum chamber + fixturing ($\le10^{-6}$ Torr, oil-free)
- **Builds to REQ-IDs:** `CLV-REQ-VAC` (§6.1 $\le10^{-6}$ Torr, dry train, ion-gauge-off-during-read), `CLV-REQ-GAP` (§4.4 PARALLELISM fixturing — tilt changes $C_{in}$), `CLV-REQ-VIB` (§6.3 turbo-decouple is a chamber-integration decision), and couples `CLV-REQ-CFIX` (the parallelism fixture feeds the $C_{in}$-fixed knob D5).
- **Options:** (a) MAKE — collaborator builds the chamber + plate fixturing (their stated strength). (b) BUY — refurb 4–6" CF chamber.
- **Derived tradeoffs:** The architecture is sound (dedicated $\le10^{-6}$ Torr, dry train, ion-gauge-off-during-read — §6.1; UHV correctly rejected). MAKE fits the collaborator's "scrappy high-quality vacuum chambers" skill and the spec is non-exotic. The load-bearing fixturing requirement is PARALLELISM (tilt changes $C_{in}$, §4.4) + a low-microphonic, strain-relieved floating-electrode lead — a fixturing-design task the collaborator owns. The turbo-decouple (bellows / remote-mount / valve-off-and-coast, §6.3) is a chamber-integration decision that sits here.
- **Dependencies:** the pump/gauge (A5-BUY) and the parallelism fixture couple the C_in-fixed knob (D5).
- **STATUS: OPEN — decision pending (Grant + collaborator). Leaning MAKE (collaborator).**

### A5 — Pump / gauge train (turbo + dry scroll + ion gauge)
- **Builds to REQ-IDs:** `CLV-REQ-VAC` (§6.1 hydrocarbon-free dry train, adsorbate reproducibility, ion-gauge filament OFF during read), couples `CLV-REQ-VIB` (the turbo is a vibration SOURCE → mount decision back to A4).
- **Options:** (a) BUY — refurb turbo (Edwards nEXT85 / Pfeiffer HiPace 80) + dry scroll (nXDS6i) + ion gauge. (b) REUSE — if the team already owns a turbo + dry scroll + gauge.
- **Derived tradeoffs:** This is precision-vacuum hardware outside the team's build scope = BUY/REUSE, not MAKE. The hydrocarbon-free requirement (§6.1, adsorbate reproducibility) mandates a dry train (no oil backstreaming). The turbo is a vibration SOURCE on the chamber (§6.3) — so the mount decision (bellows/remote) couples back to A4. REUSE swings the build feasibility heavily if a dry train is in hand.
- **STATUS: OPEN — decision pending (Grant + collaborator). BUY-or-REUSE, not MAKE.**

### A6 — Precision metrology (closed-loop nanopositioner + cap gap sensor + charge-cal reference + readout digitizer)
- **Builds to REQ-IDs:** `CLV-REQ-GAP` (the closed-loop cap-sensor stage = §4.1–4.4, incl. the H4/H5 items `CLV-REQ-H4`/`CLV-REQ-H5`), `CLV-REQ-VIB` (`CLV-REQ-H2` stage+isolation together), `CLV-REQ-READOUT` (the 18–24-bit $\Delta\Sigma$ / DMM digitizer, §3.3), `CLV-REQ-DRIFT` (the digitizer feeds the H1 level-stability spec), `CLV-REQ-CAL` + `CLV-REQ-VALIDATE` (the charge-cal reference = the one-instrument-three-jobs of §7.2, also the anti-false-null positive control), and `CLV-REQ-CFIX` (the stage stroke vs the $C_{in}$-fixed topology D5).
- **Options:** (a) BUY — closed-loop capacitive-sensor flexure nanopositioner ($\ge300$ µm or de-spec'd $g_0$, pm-class) + its servo controller; an 18–24-bit $\Delta\Sigma$ DAQ or 6.5–7.5-digit DMM; a charge-cal reference (the unified one-instrument-three-jobs of §7.2). (b) MAKE-fragment — only the charge-cal reference (catalog $C_{ref}$ + attenuated precision $V_{ref}$ step, §7.2) is buildable in-house.
- **Derived tradeoffs:** This is the instrument-grade precision the team does NOT self-build = BUY. The closed-loop cap-sensor stage is what makes the gap-sweep discriminator real (beats the §4.2 specs by 1–2 OOM where open-loop PZT fails by ~100×); the $\ge300$ µm-AND-vacuum-AND-pm-class corner narrows the vendor list (RFQ territory — or de-spec $g_0$ via D2/D7 to widen it). The readout digitizer is a TRIVIAL COTS swap (the 8-bit scope is the wrong class, §3.3). The charge-cal reference is the one MAKE-fragment AND it closes Q-C15-04 (in-situ $C_{in}=Q_{inj}/V_{meas}$) + the anti-false-null gate simultaneously (§7.2).
- **Dependencies:** the stroke depends on D2 (baseline gap) + D7 ($C_{in}$-fixed topology); the digitizer ENOB depends on D1 ($C_{in}$) + D3 (topology).
- **STATUS: OPEN — decision pending (Grant + collaborator). BUY the metrology; the charge-cal reference is the MAKE-fragment.**

## Part B — DESIGN KNOBS (the 6 OPEN decisions; each cross-linked to its Q-C15 register entry + the REQ-IDs it touches)

Each knob is also formalized as a Q-C15 open decision in [`exp-c15-cleave-01.md`](../../../../../_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md) "Open questions (forward-active)" table; the IDs below are the cross-links. Each knob also cites the canonical `CLV-REQ-*` requirement IDs it parametrizes — those derived requirements live in the sibling [`cleave-01-requirements-boundary-conditions.md`](cleave-01-requirements-boundary-conditions.md) (the REQ-ID INDEX at its top is the master list). **Citing a REQ-ID here selects no option and changes no derived number; it records which boundary condition the open decision moves.**

### D1 — $\delta$: $\delta_{chord}$ vs $\delta_{slope}$ (↔ **Q-C15-02** / **Q-C15-13**) — touches `CLV-REQ-READOUT`, `CLV-REQ-DRIFT`, `CLV-REQ-GAP`, `CLV-REQ-CAL`
- **REQ-IDs touched:** `CLV-REQ-READOUT` (§3.2 charge-domain resolution scales with $\delta$), `CLV-REQ-DRIFT` (§3.6 the GATING drift budget is $\delta\times414.9$ fC), `CLV-REQ-GAP` (§4.2 position tolerances scale $\delta/k$), `CLV-REQ-CAL` (§7.2 Use-B reference accuracy $\sim\delta/2$). Note: $\delta$ does NOT touch `CLV-REQ-FLOOR` or the chord-protecting `CLV-REQ-CPL-C` / `CLV-REQ-VIB` (those are $\delta$-INDEPENDENT, chord-clean).
- **Options:** (a) freeze $\delta_{chord}=10\%$ (gating) + $\delta_{slope}=5\%$ (non-gating); (b) tighten $\delta_{slope}$ to 2%; (c) leave OPEN until assembled hardware.
- **Derived tradeoffs:** $\delta$ does NOT gate the chord (PR#361, requirements §2.1) — the chord needs only the floor LEVEL to beat the 19.97% CPD swing, so $\delta_{chord}\sim10\%$ has comfortable margin. $\delta_{slope}=5\%$ matches the ~5% $C_{in}$-knowledge floor (D5); tighter than ~5% is not adjudicable until $C_{in}$ is measured better. The chord/slope split is the load-bearing reframe: the tight readout/drift specs (§3.2/§3.6) are needed ONLY for the non-gating slope.
- **STATUS: OPEN — decision pending (Grant + collaborator).**

### D2 — $C_{in}$: 10 pF vs 1 pF (↔ **Q-C15-04** / **Q-C15-14** $C_{in}$ control) — touches `CLV-REQ-CPL-A`, `CLV-REQ-READOUT`, `CLV-REQ-DRIFT`, `CLV-REQ-VIB`
- **REQ-IDs touched:** `CLV-REQ-CPL-A` (the 41.49 nV/pm position→charge coupling IS $\xi_{topo}/C_{in}$ — 1 pF moves it 10×), `CLV-REQ-READOUT` (§3.2/§3.3 the voltage floor + ENOB scale $1/C_{in}$), `CLV-REQ-DRIFT` (§3.6 drift budget eases ~10× at 1 pF), `CLV-REQ-VIB` (§6.3 the pm-jitter spec is $V_{floor}/(\xi_{topo}/C_{in})$ — raising $C_{in}$ is one of only two levers on the binding vibration spec). Does NOT change `CLV-REQ-FLOOR` (the CHARGE floor is $C_{in}$-independent).
- **Options:** (a) keep 10 pF; (b) drop to 1 pF.
- **Derived tradeoffs:** THE single biggest lever (requirements §2.4). 1 pF raises the voltage floor 10× ($41.49\to414.9$ mV/µm), easing readout-resolution AND drift ~10× — but raises impedance/leakage sensitivity. The chord (a SHAPE) survives any $C_{in}$; this knob trades readout/drift headroom against leakage robustness. Freeze BEFORE the digitizer-ENOB (A6) and drift (D4) budgets lock.
- **STATUS: OPEN — decision pending (Grant + collaborator).**

### D3 — Readout front-end topology: follower+differencing vs charge-reset integrator (↔ **Q-C15-04** / **Q-C15-15** / front-end) — touches `CLV-REQ-CPL-D`, `CLV-REQ-READOUT`
- **REQ-IDs touched:** `CLV-REQ-CPL-D` (the 20.0 fC/s bias-ramp BC that forces step-differencing / DC-restore / reset-integration — a topology requirement), `CLV-REQ-READOUT` (§3.3/§3.5 the integrator removes the high-ENOB-ADC dependence and resets-away $kTC$ + the bias ramp). Couples to make-vs-buy A1 (front-end feedback network).
- **Options:** (a) bare follower + step-differencing / DC-restore; (b) charge-sensitive reset-integrator.
- **Derived tradeoffs:** PHYSICS forces a bias-ramp bleed (20.0 fC/s rails a bare passive node, §3.5). (a) keeps the front-end simple but pushes the precision burden onto a high-ENOB voltage ADC. (b) puts the fC measurement in the charge domain, removes the high-ENOB-ADC dependence, and resets-away $kTC$ + the bias ramp — the better-conditioned architecture. The corpus `reference_design.md` §9 specifies a bare follower into a passive 10 pF node with NO DC path (the unmitigated case).
- **STATUS: OPEN — decision pending (Grant + collaborator).**

### D4 — Drift-rejection scheme: auto-zero/chopper/CDS vs cRIO gap-dither + lock-in (↔ **Q-C15-02** / **Q-C15-16** / drift) — touches `CLV-REQ-DRIFT`, `CLV-REQ-CPL-B`
- **REQ-IDs touched:** `CLV-REQ-DRIFT` (this knob decides whether the sub-µV LEVEL stability = the H1 hardest spec is reached — by ARCHITECTURE, not a better ADC), `CLV-REQ-CPL-B` (the 1/f + drift noise model that makes LEVEL STABILITY the binding spec is what this scheme converts into a band-limited measurement). Equivalently touches `CLV-REQ-H1`.
- **Options:** (a) auto-zero / chopper / correlated-double-sampling; (b) gap-dither + lock-in on Grant's cRIO (DC–40 kHz phase-coherent).
- **Derived tradeoffs:** This decides whether the sub-µV LEVEL stability (§3.6, the H1 hardest spec) is reachable — it is reached by ARCHITECTURE, not a better ADC. (a) is standard precision-metrology practice (Kelvin-probe / vibrating-reed electrometers). (b) is the natural fit for Grant's cRIO and converts the DC-drift-limited measurement into a band-limited one. **Recorded as an OPTION (the cRIO is a candidate), NOT a decision** — note the prereg flags this bench as "NOT cRIO-native" for the core apparatus (the cRIO would serve the drift-rejection role only).
- **STATUS: OPEN — decision pending (Grant + collaborator).**

### D5 — $C_{in}$-fixed-vs-gap-motion topology: fixed-ref-cap + weak-coupling sweep electrode vs in-situ-measure-and-divide (↔ **Q-C15-04** / **Q-C15-17**) — touches `CLV-REQ-CFIX` (= H3), `CLV-REQ-CAL`
- **REQ-IDs touched:** `CLV-REQ-CFIX` (the UNCLOSED H3 tension — the moving plate IS a $\sim1/g$ cap; this knob decides whether the binding spec is MECHANICAL (coupling $<0.44$ pF) or METROLOGICAL ($C$ measured to $<\delta/k$)), `CLV-REQ-CAL` (§7.1 in-situ-$C$ method; option (b) transfers the requirement onto in-situ C-metrology). Equivalently touches `CLV-REQ-H3`. Couples make-vs-buy A4 (fixturing) + A6 (stage).
- **Options:** (a) a separate FIXED reference cap dominates $C_{in}$, moving-plate coupling held $C_{plate}(g_{min})<0.44$ pF; (b) measure $C_{in}$ in-situ at every sweep point and divide out.
- **Derived tradeoffs:** The UNCLOSED design tension (H3): the moving plate-pair IS a $\sim1/g$ capacitor swinging ~4× across the sweep — FATAL if it IS $C_{in}$ (§4.5). (a) transfers the requirement to a MECHANICAL spec (coupling $<0.44$ pF); (b) transfers it to a METROLOGICAL spec (C measured to $<\delta/k$). **This must be resolved BEFORE the gap-actuation hardware is frozen** because it determines which spec binds. Q-C15-04 currently treats $C_{in}$ as a static board parasitic and never addresses its $1/g$ motion-dependence — the load-bearing gap.
- **STATUS: OPEN — decision pending (Grant + collaborator).**

### D6 — Baseline gap $g_0$ + sweep range + N (↔ **Q-C15-02** / **Q-C15-18** precision target / stage travel) — touches `CLV-REQ-GAP` (§4.1 = H5), `CLV-REQ-PZT`, `CLV-REQ-CPL-C`
- **REQ-IDs touched:** `CLV-REQ-GAP` (§4.1 travel/stroke: the $\ge4\times$ RATIO is physics-set, the absolute $g_0$/stroke is the open knob; the 15–30 µm actuators CANNOT execute the sweep = the H5 feasibility blocker; N sets the $\sqrt{N}$ drift-corrected resolution feeding `CLV-REQ-DRIFT`), `CLV-REQ-PZT` (§5.5 range: the stroke sets the drive span), `CLV-REQ-CPL-C` (a wider span gives a larger CPD $1/g^2$ lever-arm to separate flat-vs-$1/g^2$). Equivalently touches `CLV-REQ-H5`. Couples make-vs-buy A6 (stage) + A2 (drive).
- **Options:** (a) keep $g_0\sim100$ µm $\Rightarrow$ ~300 µm closed-loop travel for $g_0\!\to\!4g_0$; (b) de-spec $g_0$ to ~10–25 µm $\Rightarrow$ a 30–75 µm closed-loop stage suffices; widen the sweep beyond $4\times$ for a larger CPD lever-arm; choose N (~50) trading session time for $\sqrt{N}=7.07\times$ drift-corrected resolution.
- **Derived tradeoffs:** The $\ge4\times$ RATIO is physics-set (§4.1); only the absolute $g_0$ and stroke are open. (a) needs $\ge300$ µm vacuum-compatible closed-loop travel (narrow vendor list); (b) widens the vendor list but tightens parallelism/CPD budgets. A wider span gives a larger CPD lever-arm to separate flat-vs-$1/g^2$. **The selected 15–30 µm open-loop actuators CANNOT execute $\ge4\times$ at 100 µm at all (H5 feasibility blocker)** — so this knob and A6 must be frozen together.
- **STATUS: OPEN — decision pending (Grant + collaborator).**

## Part C — Dependency map (which decisions must be frozen together)

| Knob | Must freeze WITH | Why (derived coupling) | REQ-IDs |
|---|---|---|---|
| D2 ($C_{in}$) | A6 (digitizer ENOB), D4 (drift) | $C_{in}$ sets the voltage floor $\Rightarrow$ the ENOB + drift budgets (§3.2/§3.6) | `CLV-REQ-CPL-A`, `CLV-REQ-READOUT`, `CLV-REQ-DRIFT`, `CLV-REQ-VIB` |
| D3 (topology) | A1 (PCB), A6 (digitizer) | integrator vs follower changes the feedback network + whether a high-ENOB ADC is needed (§3.3/§3.5) | `CLV-REQ-CPL-D`, `CLV-REQ-READOUT` |
| D5 ($C_{in}$-fixed) | A4 (fixturing), A6 (stage), D6 ($g_0$) | the unclosed H3 tension is mechanical OR metrological depending on D5 (§4.5) — resolve before freezing gap hardware | `CLV-REQ-CFIX` (=`CLV-REQ-H3`), `CLV-REQ-CAL` |
| D6 ($g_0$/stroke) | A6 (stage), A2/A6 (drive) | the $4\times$ stroke sets the stage travel + drive range (§4.1/§5.5); the 15–30 µm actuators can't do it (H5) | `CLV-REQ-GAP` (=`CLV-REQ-H5`), `CLV-REQ-PZT`, `CLV-REQ-CPL-C` |
| A2 (drive) | A6/D6 (closed-loop stage) | drive + stage are ONE closed-loop problem (§5.4); a servo controller subsumes the discrete drive | `CLV-REQ-PZT`, `CLV-REQ-GAP`, `CLV-REQ-VIB` |
| D4 (drift) | A6 (cRIO/digitizer) | the sub-µV LEVEL stability (H1) is an ARCHITECTURE choice, not an ADC choice (§3.6) | `CLV-REQ-DRIFT` (=`CLV-REQ-H1`), `CLV-REQ-CPL-B` |

**Standing rule for this register:** **SELECT NOTHING.** Every entry ends STATUS: OPEN. Decisions are adjudicated by Grant + collaborator in a separate session; this register exists to make the option-analysis work visible and the dependencies explicit BEFORE any selection.

---


