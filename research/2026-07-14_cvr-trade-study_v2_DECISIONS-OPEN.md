# CVR Bench — Trade Study v2 / Decision Register (STATUS: OPEN throughout)

**Date:** 2026-07-14 · **Lane:** CVR dielectric-C-V bench (implementer) · **Status:** DECISION RECORD, not a claim. Supersedes v1 (`research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md`, preserved unchanged). Every entry ends STATUS:OPEN. SELECTS NOTHING. Cost OUT OF SCOPE.

> **Supersedes-with-pointer.** This is trade-study **v2**. It supersedes v1 (`research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md`), which is **preserved unchanged** (v1 = the first pass: 4 trades / 3-options-each + the T-D PLATES theory ruling). v2 answers Grant's structured ask, verbatim: *"broadest set of options, tiered levels of qualifiers, what remains to hit our targets."* It (1) **widens** the option space per trade and adds four missing trades (**T-E** cell material/geometry, **T-F** thermal control, **T-G** acquisition chain, **T-H** environmental isolation); (2) grades every option against a **tiered qualifier framework** (TIER-0 physics must-holds / TIER-1 form-axis enablement / TIER-2 performance targets); (3) tabulates the **remains-to-target gap** per form axis, including the receipt-debts. The **T-D PLATES theory ruling** from v1 §T-D carries forward unchanged and is **NOT re-opened** here.

> **THIS IS A DECISION RECORD, NOT A CLAIM.** Following the CLEAVE-01 pattern (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-trade-study-decision-register.md`): this is an OPEN decision-space record of each CVR design knob as a worked option set — options + physics-relevant differences + tiered grades + dependencies — each ending **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.** The derived, frozen boundary conditions are in the sibling `research/2026-07-13_cvr-requirements_DERIVED.md` (the `CVR-REQ-*` datasheet). **Derived = there. Open = here.** Cost is OUT OF SCOPE (adjudicated separately) — these are feasibility-and-fit physics tradeoffs, not a BOM roll-up.

> **★ Binding epistemic frame (`CVR-REQ-FRAME` — stated in full in the sibling `research/2026-07-13_cvr-requirements_DERIVED.md`; cited here by ID, cite-don't-duplicate).** Before any trade or tier below: the CVR bench is a **validation-ladder + material-analog shape bench** and a **one-sided anomaly bound (corroborative-null class)** — it is **NOT an AVE-confirming channel**. The magnitude route is dead three verified ways; at bench magnitude the lattice's own conjunction-passing signal is $\sim10^{-17}$, unreachable. **Any conjunction-passing residual at bench magnitude falsifies AVE *and* QED alike.** Every option and every qualifier tier below serves the material-analog ladder + the fixture-vs-anomaly classifier, never an AVE confirmation. This frame is itself a **TIER-0 must-hold**: an option or protocol sold as AVE-confirming is struck.

---

## PART 1 — THE BROADEST OPTION SPACE

Physics-relevant differences only. Cost is OUT OF SCOPE. Each option carries the REQ-ID it builds to and the form-axis it lives on. Options new to v2 (not in v1) are marked **[v2-new]**.

### T-A — gap-holding construction (what physically holds the plates apart)

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE` (stiffness $k$ for the $d^{-3}$ pull-in subtraction; $\ge4\times$ fixed-$V$ gap sweep, holder unchanged), `CVR-REQ-FIELDVOL` (Class-I / vacuum only in the DC field volume — the holder material sits IN the field volume). Form-axes: **sign** (via field-volume dielectric class) + **d-power** (via $k$/parallelism) + **flatness** (via holder mechanical resonances).
- **Options:**
  - **(a) Vacuum-gap spacer** — rigid insulating standoffs *outside* the field volume, vacuum between the plates. Cleanest `CVR-REQ-FIELDVOL` pass (field volume threads vacuum only). Stiffness set by standoff geometry/material; harder to characterize $k$ than a monolith.
  - **(b) Fused-silica (Class-I) spacer** in the field volume. Class-I linear $C(V)$ (passes `CVR-REQ-FIELDVOL`), high stiffness, low CTE. A solid dielectric partly in the field volume shifts effective $C_0$ and perturbs the $d^{-2}$-vs-$d^{-3}$ geometry — must be modeled.
  - **(c) Flexure-guided monolithic plate** — one plate on a monolithic flexure. Highest, best-characterized $k$ (designable + measurable → directly serves the pull-in subtraction), naturally parallel-keeping; but the flexure is a spring whose resonances are an $f$-structured term on the flatness axis.
  - **(d) Optical-flat + kinematic spacer-ball registration [v2-new]** — two optical flats gapped by three Class-I (sapphire / fused-silica) precision balls in a kinematic (3-ball) mount. Deterministic absolute gap from ball diameter, sub-µm parallelism from optical contact, Class-I-only field volume. Very high stiffness through the ball contacts; gap is *quantized* by ball set (couples to T-C option d). Hertzian contact compliance at the ball is the one soft term to characterize.
  - **(e) Single-crystal sapphire Class-I spacer [v2-new]** — sapphire (or crystalline quartz) instead of amorphous fused silica: higher Young's modulus (stiffer $k$), markedly lower loss tangent than glass (sharper `CVR-REQ-ACQ` flatness/quadrature discrimination), low CTE. Anisotropy/birefringence is irrelevant to the C-V channel. The premium Class-I field-volume solid.
  - **(f) MEMS / micromachined parallel-plate cell [v2-new]** — monolithic Si / thermal-SiO₂ micro-cell; $k$ lithographically designable and directly measurable via its own pull-in, best parallelism. But: gap is µm–sub-µm (small stroke for the $\ge4\times$ sweep), thermal-SiO₂ in the field volume must be verified Class-I-linear at kV-equivalent fields, and comb/interdigital MEMS variants break the parallel-plate $d^{-2}$ axis (that geometry choice is **T-E**, not here). Kept as a distinct construction because its $k$ is the best-known of any option.
- **Physics-relevant differences:** (a) maximizes field-volume cleanliness at a soft/hard-to-characterize $k$; (b)/(e) trade a Class-I solid in the field volume (modeled $C_0$ shift; (e) lower-loss than (b)) for high stable stiffness; (c) gives the best-known continuous $k$ but injects mechanical resonances on the flatness axis; (d) gives deterministic absolute gap + Class-I-only field volume but a quantized gap set; (f) gives the best-characterized $k$ (self-reporting pull-in) at a small-stroke, small-gap cost. **Class-II ceramic is EXCLUDED from all options** by `CVR-REQ-FIELDVOL` (the one sign-degenerate confound, `research/2026-07-13_cvr-requirements_DERIVED.md` §4).
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-B — HV-standoff / sense topology (how the kV stands off from the sense node)

- **Builds to REQ-IDs:** `CVR-REQ-STANDOFF` (sense node at virtual ground; DC never threads the sense path; blocking element $C(V)$ Class-I or topologically excluded; standoff-network calibration-stability), couples to `CVR-REQ-ACQ` (the standoff network sits in series with every probe tone). Form-axes: **sign** + **flatness** (the standoff element's own $C(V)/D(V)$ is an $E^2$-even, potentially $f$-structured confound *sign-degenerate with the lattice*).
- **Options:**
  - **(a) Series blocking cap** into the sense node. Simple; but the blocking cap sits directly in series with the signal and its OWN $C(V)/D(V)$ is $E^2$-even and *sign-degenerate with the lattice*. Requires a Class-I (C0G/NP0/vacuum/air) blocking cap and a characterized/stable network — the load-bearing `CVR-REQ-STANDOFF` care point.
  - **(b) Virtual-ground transimpedance** — bias on the driven electrode, sense electrode at op-amp virtual ground ($\approx0$ V). The kV never appears at the sense node and no series blocking element carries signal current — the topology that most directly satisfies "DC never threads the sense path." Front-end bias-current / bandwidth become the care points.
  - **(c) Guard / driven-shield** around the sense node (guarded triax + driven guard). Rejects leakage + stray coupling; typically combined with (b), not a standalone standoff. (The cabling realization is **T-G**.)
  - **(d) Bias-tee (RF-choke DC-inject + AC blocking cap) [v2-new]** — DC injected through a series choke onto the driven electrode, probe tones AC-coupled. Classic and calibration-friendly, but the choke's parasitic + the coupling cap's $C(V)$ form a transfer function that must be characterized across DC–40 kHz; the coupling cap is the same sign-degenerate care as (a).
  - **(e) Ratio-transformer / capacitance-bridge topology [v2-new]** — the gap cell is one arm of a transformer-ratio bridge (Andeen-Hagerling class); the HV stands off through the bridge/injection network and the standoff cap is *nulled by ratio* rather than carried in series. Metrology-grade sign + floor; pairs naturally with T-G(c). The bridge injection network's own $C(V)$ moves to the balance, not the signal.
  - **(f) Resonant-tank / frequency-readout [v2-new]** — put the gap in an LC tank and read the shift in resonant $f$ (DC bias through an RF choke). Converts a hard δC/C measurement into an $f$-shift, potentially higher $Q$-leveraged resolution; but it collapses the *simultaneous multi-tone* flatness axis (a resonator is single-band) — a TIER-0 tension unless multiplexed. Pairs with T-G(d).
  - **(g) Floating "electrometer-at-potential" [v2-new]** — the entire sense front-end floats at (or near) the bias potential, guarded up to kV, with fiber-optic telemetry to ground. Removes the standoff *element* entirely (no series blocking cap in the signal path) at the cost of a floating, battery/opto-isolated front end and its stability discipline.
- **Physics-relevant differences:** (a)/(d) put a voltage-dependent dielectric in series with the signal (the exact thing `CVR-REQ-STANDOFF` + `CVR-REQ-FIELDVOL` warn against) unless the element is Class-I; (b)/(g) remove the series blocking element from the signal path (topological exclusion — the preferred `CVR-REQ-STANDOFF` reading); (e) nulls the standoff cap by ratio (metrology-grade); (c) is a hardening layer, not a standoff by itself; (f) buys $f$-shift resolution but fights the multi-tone flatness axis. `CLV-REQ-VALIDATE` (`cleave-01-requirements-boundary-conditions.md:62`) applies to whichever topology: inject a known even-in-$V$ series-C step and confirm the chain resolves it before trusting any null.
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-C — gap-sweep mechanism (how $d$ moves across the $\ge4\times$ sweep, holder unchanged)

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE` (the $\ge4\times$ fixed-$V$ gap sweep with holder/stiffness unchanged — the $d^{-2}$-vs-$d^{-3}$ log-log axis lives or dies here), couples to `CVR-REQ-ACQ` (a sweep mechanism that creeps in $f$ contaminates the flatness axis). Form-axes: **d-power** (primary) + **flatness** (via creep).
- **Options:**
  - **(a) Discrete shim set** — swap calibrated spacers per gap. Dead-simple, no active creep, absolute gap from the shim. But each swap DISTURBS the fixture (re-clamp → parallelism + $k$ can change point-to-point), threatening the "holder unchanged" clause of `CVR-REQ-FIXTURE`; not continuous.
  - **(b) Flexure + micrometer / closed-loop nanopositioner** — continuous, repeatable, keeps parallelism, $k$ characterizable; a closed-loop capacitive-sensor stage places $d$ to the relative accuracy the log-log slope fit needs. Larger stroke (to span $\ge4\times$ at ~100 µm baseline) narrows the vendor list (the CLEAVE-01 H5-class travel issue).
  - **(c) Piezo (PZT) actuator** — fine resolution, but **open-loop PZT log-creep (~10–20 nm over the first seconds = the hold window) is a known $f$-structured confound** on the `CVR-REQ-ACQ` flatness axis (`cleave-01-requirements-boundary-conditions.md:198`). Usable only closed-loop; open-loop couples negatively into BOTH the gap-power and flatness axes.
  - **(d) Kinematic ball-swap [v2-new]** — pairs with T-A(d): the gap is set deterministically by the diameter of the swapped precision-ball set. Absolute gap known a-priori (no cap-sensor needed for absolute $d$), no active creep; but a swap disturbs the stack like a shim (holder-unchanged tension) and the gap set is quantized.
  - **(e) Differential-CTE thermal actuator [v2-new]** — a controlled temperature difference expands a calibrated element to move the gap. Monotonic, no PZT-style creep hysteresis; but it couples the gap directly to the *thermal* channel, so any thermal drift is simultaneously a gap error and an $f$-structured flatness term — the worst possible coupling for the flatness axis. Recorded for completeness; strongly disfavored on physics.
  - **(f) Voice-coil / magnetic closed-loop actuator [v2-new]** — continuous, large-stroke, closed on a cap sensor. Introduces a magnetic actuator force + stray $B$ (irrelevant to the ε-only DC load, but a fixture force term to bound); stroke is generous (eases the $\ge4\times$-at-100 µm problem that constrains (b)).
  - **(g) Fixed-gap parallel-cell array [v2-new]** — NO sweep mechanism: a bank of separate rigid cells at different fixed gaps, all measured simultaneously (pairs with T-G multi-channel). Each cell's holder is *truly* unchanged (there is no motion), which is the strongest possible "holder unchanged" pass; but cell-to-cell variation in $A$, parallelism and Class-I spacer becomes the systematic *instead of* sweep-repeatability, and the $d^{-2}$ fit is now across cells, not within one fixture.
- **Physics-relevant differences:** (a)/(d) zero active-creep but disturb the holder per point (or quantize the gap); (b)/(f) preserve the fixture across a continuous sweep (best `CVR-REQ-FIXTURE` fit) at a stroke/vendor (b) or stray-force (f) cost; (c) risks a creep term simultaneously on the gap-power AND flatness axes unless closed-loop; (e) is the one option that hard-couples the gap to the thermal/flatness channel; (g) trades sweep-motion systematics for cell-matching systematics (the holder-unchanged clause is satisfied trivially, `CVR-REQ-FIXTURE` §3.3, but the $d$-power fit moves across cells).
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-D — tips vs plates — **core-session THEORY ruling CARRIED FORWARD FROM v1: PLATES**

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE`, `CVR-REQ-FIELDVOL`, `CVR-REQ-FRAME`.
- **This trade is NOT re-opened in v2.** It records the v1 core-session THEORY ruling (`research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md` §T-D): the CVR bench stays **PARALLEL-PLATE**. Rationale (recorded, unchanged from v1): (1) sharp-emission tips max out near the field-evaporation ceiling of order $\sim10^{11}$ V/m **[TAG: from-memory engineering bound — receipt OWED, carried as a gap-table row in Part 3]** — still $\sim5$ OOM below the $A=1/\sqrt2$ NDC window at $>10^{16}$ V/m (`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:36-38`); (2) tips destroy the parallel-plate $d^{-2}$ axis (non-uniform field averages the sag); (3) tips add field-emission current as an $E$-dependent confound on the $E^2$-even channel. The $1/\sqrt2$ NDC snap-back banks as a **facility-class FORWARD FALSIFIER candidate** (companion to the E-route birefringence `clm-pp3qwf`), NOT a CVR bench axis.
- **STATUS: THEORY-RULED (PLATES) — carried forward from v1, not re-opened. The plate-construction choices remain OPEN in T-A/T-E; the tip route stays theory-closed for this bench.**

### T-E — cell material / geometry (parallel-plate vs cylindrical vs interdigital) **[v2-new trade]**

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE` (the $d^{-2}$ gap-power axis is *derived for parallel-plate*), `CVR-REQ-FIELDVOL`, `CVR-REQ-FRAME`. Form-axes: **d-power** (load-bearing — the geometry sets the exponent) + **sign** (field uniformity sets whether a single $A=E/E_{yield}$ applies).
- **Why this trade is load-bearing (physics receipt).** The whole TIER-1 gap-power discriminator — lattice $\delta C/C \propto V^2 d^{-2}$ vs electrode-attraction $\propto V^2 d^{-3}$ (`research/2026-07-13_cvr-requirements_DERIVED.md` §3, §1) — is **derived for a uniform-field parallel-plate cell**, where a single field $E=V/d$ maps to a single kernel argument $A=E/E_{yield}$. Change the geometry and you change (or destroy) that exponent. This is why T-D ruled PLATES; T-E enumerates the geometry space honestly so the ruling is a *chosen* base, not an unexamined default.
- **Options:**
  - **(a) Parallel-plate** — the T-D-ruled base. Uniform field → single $A=E/E_{yield}$ → clean $d^{-2}$ (lattice) vs $d^{-3}$ (attraction) separation. The only geometry for which the derived form axes hold as written.
  - **(b) Cylindrical / coaxial** — $C = 2\pi\varepsilon L/\ln(b/a)$; the "gap" is radial and the field $E(r)=V/[r\ln(b/a)]$ is *non-uniform*, so $A=E/E_{yield}$ is radius-dependent and $\delta C/C$ is NOT a clean $d^{-2}$ — the gap-power axis must be **re-derived** for this geometry or it is lost. Buys higher $C$ per volume and a self-guarding outer conductor. FAILS TIER-1 d-power as-derived; would need its own assembly.
  - **(c) Interdigital / comb** — $C$ is fringe-field-dominated ($\approx d^{-1}$, strongly non-uniform field). Both the uniform-field assumption (needed to convert $V\to E\to A$) and the $d^{-2}$ axis are lost; high $C$ in a small MEMS-native volume. FAILS TIER-1 d-power and the sign-axis field-uniformity premise. Recorded as the MEMS-native geometry so the trade is complete.
  - **(d) Thompson–Lampard cross-capacitor / guarded-disc [calculable geometry]** — $C$ per unit length $=\varepsilon_0\ln2/\pi$ is geometry-exact and self-guarding (the SI calculable-capacitor geometry), giving the *cleanest possible* field volume and floor. BUT it is a fixed-$C$ metrology object, not a gap-sweep object — you cannot sweep "$d$" and keep the calculable property. PASSES sign + flatness with the best floor; FAILS the d-power axis (no gap sweep). A candidate *reference/validation* geometry, not the sweep cell.
  - **(e) Spherical / weakly-curved (one flat, one long-radius lens)** — self-aligning with a defined minimum gap, but a mild version of the tip non-uniformity T-D ruled against; the field map is non-uniform so the sag is averaged. A parallelism-robustness option that partially sacrifices the d-power axis.
- **Physics-relevant differences:** only (a) preserves the derived form axes; (b)/(c)/(e) trade field uniformity (hence the clean $d$-power exponent and the single-$A$ sign premise) for $C$-density, self-guarding, or self-alignment; (d) is the metrology-grade *reference* geometry (best sign/flatness/floor) that cannot itself execute the gap sweep. **Consistent with the T-D PLATES ruling, (a) is the base; the rest are recorded so the geometry space is honestly enumerated.**
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING. (Parallel-plate is the T-D-ruled base, not a v2 selection.)**

### T-F — thermal control (the drift-budget owner) **[v2-new trade]**

- **Builds to REQ-IDs:** `CVR-REQ-ACQ` (drift on the flatness axis — sequential-run drift fakes dispersion; §5.2), and the TIER-2 **drift/hour** target. Inherits the CLEAVE-01 thermal discipline (`cleave-01-trade-study-decision-register.md:36-40`, A3: $dT\le1$ K, 2× RTD). Form-axes: **flatness** (primary — drift is the flatness-axis owner) + **d-power** (thermal gap drift is a $d$ error).
- **Why this trade owns the drift budget.** The flatness discriminator needs the $E^2$-even response as a function of $f$ in a *single thermal environment* — a thermal drift across a run is an $f$-structured / 1-$f$ trend that fakes dispersion (`research/2026-07-13_cvr-requirements_DERIVED.md` §5.2). The **primary** defense is architectural (simultaneous multi-tone — `CVR-REQ-ACQ`, so drift is common-mode across tones); T-F is the **secondary** defense and the owner of the residual drift/hour that survives common-mode rejection.
- **Options:**
  - **(a) Ambient / stable-room (passive)** — cheapest, but thermal drift of $\varepsilon$, geometry, and electronics is uncontrolled → the largest flatness-axis drift term. Viable ONLY if the simultaneous-multi-tone common-mode rejection is strong enough to carry the whole flatness budget.
  - **(b) Insulated shroud + 2× calibrated RTD logging** — Grant's Tesla-thermal domain (CLEAVE A3); ~1 K class, the loosest of CLEAVE's environment specs. Adequate if drift is common-mode-rejected and only bounded, not eliminated.
  - **(c) Active TEC/oven enclosure (mK-class)** — tightens the residual drift/hour well below the flatness floor; supports even sequential-tone operation. The path if a single-band readout (T-B(f) resonant, T-G(c) precision bridge) forces sequential acquisition.
  - **(d) Cryogenic operation (LN₂ / LHe) [the task-named axis]** — lower thermal noise, **lower loss tangent** in the Class-I dielectric (sharper quadrature/flatness discrimination — a real physics gain on the flatness axis), lower CTE drift. Costs: cryostat vibration (couples to **T-H**), thermal-contraction gap uncertainty (a $d$-power error to re-zero cold), and vacuum-cryo integration. The one option that *improves the physics of the flatness axis* rather than merely bounding drift.
- **Physics-relevant differences:** (a)→(d) monotonically tighten the residual drift/hour and (d) *additionally* sharpens the flatness discriminator via reduced loss tangent — at the cost of new vibration + cold-gap-metrology terms. The choice is coupled to T-G: a simultaneous-multi-tone platform (`CVR-REQ-ACQ`) relaxes T-F toward (a)/(b); a sequential platform pushes toward (c)/(d).
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-G — acquisition chain (cRIO 4×4 lock-in front-end + external-bridge alternatives) **[v2-new trade]**

- **Builds to REQ-IDs:** `CVR-REQ-ACQ` (I/Q separation §5.1; 3–4 SIMULTANEOUS tones DC–40 kHz in one acquisition §5.2; mandatory INCONCLUSIVE bin §5.3), couples to `CVR-REQ-STANDOFF` (the front-end sees the standoff network in series). Form-axes: **flatness** (simultaneity is the flatness-axis enabler) + **sign** (I/Q separates capacitive $\delta C$ from loss/creep $\delta D$) + the TIER-2 **δC/C floor**.
- **Platform options:**
  - **(a) cRIO 4×4 phase-coherent lock-in** — Grant owns the NI cRIO (+ 9263 AO, + 9215 AI), DC–40 kHz, multi-channel *simultaneous phase-coherent* → natively delivers the 3–4 simultaneous tones + I/Q (`CVR-REQ-ACQ` §5.1/§5.2 in one box). The ±10 V AO/AI class means the kV MUST stand off (hard dependency on **T-B**). The natural TIER-0 simultaneity + I/Q PASS.
  - **(b) Commercial LCR bridge (e.g. Keysight E4980A-class)** — turnkey $C_p$–$D$ (I/Q PASS), good floor. But measures ONE frequency at a time → **sequential**, which FAILS the simultaneous-multi-tone TIER-0 unless the flatness budget is carried entirely by T-F thermal control. Its internal bias-tee has its own $C(V)$ (sign-axis care, `CVR-REQ-STANDOFF`).
  - **(c) Precision capacitance bridge (Andeen-Hagerling AH2700A-class)** — the metrology gold standard for $C$ + $\tan\delta$ (best TIER-2 floor, ppm-class), transformer-ratio (pairs with T-B(e)). But a discrete frequency set (~50 Hz–20 kHz) acquired **sequentially** → FAILS simultaneous multi-tone; best sign/floor, worst simultaneity.
  - **(d) VNA / impedance analyzer (resonant-$f$ readout)** — pairs with the T-B(f) resonant tank; wideband, high-$Q$-leveraged resolution, but not sub-audio phase-coherent-*simultaneous* — a different measurement class that fights the DC–40 kHz simultaneity requirement.
  - **(e) Custom FPGA multi-tone DDS + I/Q demod [build]** — synthesizes the `CVR-REQ-ACQ` spec exactly (3–4 simultaneous tones + per-tone I/Q + INCONCLUSIVE-bin logic). A build; the most direct TIER-0 acquisition PASS if the cRIO channel count/bandwidth is a constraint.
- **Cabling sub-trade (the sense-path $C(V)$ cleanliness — task-named "guarded triaxial vs twinax"):**
  - **(i) Guarded triax (driven guard)** — driven inner shield holds the sense conductor's environment at signal potential → rejects cable-$C(V)$ + leakage; the `CVR-REQ-STANDOFF`-clean choice.
  - **(ii) Twinax (differential)** — common-mode rejection of pickup; good EMI posture but the cable dielectric $C(V)$ is still in the differential path.
  - **(iii) Coax (baseline)** — the cable dielectric $C(V)$ sits in series with the signal (a sign-degenerate cable-$C(V)$ term). The reference-baseline, disfavored where the sense path must be Class-I-clean.
- **Physics-relevant differences:** only (a)/(e) deliver *simultaneous* multi-tone (the flatness-axis enabler); (b)/(c) give the best turnkey floor + I/Q but are sequential (push the flatness budget onto T-F); (d) is a resonant/wideband class that fights sub-audio simultaneity. On cabling, guarded triax (i) is the sense-path-clean choice; coax (iii) reintroduces a sign-degenerate cable $C(V)$.
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-H — environmental isolation (vibration / acoustic / EMI) **[v2-new trade]**

- **Builds to REQ-IDs:** `CVR-REQ-ACQ` (in-band confounds on the flatness axis) + the TIER-2 **δC/C floor**. Inherits CLEAVE-01 `CLV-REQ-VIB` (vibration → gap jitter) and the turbo-decouple discipline (`cleave-01-trade-study-decision-register.md:45,52`). Form-axes: **flatness** (in-band mechanical/acoustic lines) + **sign** (2$f$-mains is $E^2$-even).
- **Why environmental isolation is MORE binding for CVR than for CLEAVE (physics receipt).** CVR's readout lives IN the DC–40 kHz *audio* band. A gap jitter $\delta d$ gives $\delta C/C = -\delta d/d$ (parallel plate); with a kV static bias held, mechanical/acoustic vibration at $f_{vib}$ modulates $d$ → an AC capacitance AT $f_{vib}$ landing *directly in the probe band* — an $f$-structured confound on the flatness axis plus a broadband δC/C floor. The CLEAVE DC-readout bench does not share this in-band exposure.
- **Options:**
  - **Vibration:** **(a) passive air-table** (baseline), **(b) active isolation** (needed where audio-band vibration overlaps the probe tones), **(c) rigid/massive monolith** (push the lowest fixture resonance above 40 kHz — stiff-and-light or heavy-and-damped). The choice tracks the T-A/T-C fixture resonances and the T-G tone placement.
  - **Acoustic: (d) acoustic enclosure [CVR-specific]** — the audio-band probe makes acoustic pressure a *direct in-band* modulator of the fixture; an acoustic hood is a genuinely CVR-specific requirement the DC CLEAVE bench does not carry.
  - **EMI: (e) Faraday enclosure + driven guard** — the HV supply ripple and **2$f$-mains (100/120 Hz) are $E^2$-even** → they land on BOTH the sign and flatness axes; the lock-in rejects out-of-band, but in-band mains harmonics need synchronous notch / line-sync rejection. Guarded cabling (T-G(i)) is the co-requisite.
  - **Pump vibration: (f) turbo/pump decouple** — bellows / remote-mount / valve-off-and-coast (inherited CLEAVE `CLV-REQ-VIB`); the turbo is a vibration SOURCE in the probe band.
- **Physics-relevant differences:** (a)→(c) trade against the fixture resonance placement; (d) is the CVR-unique acoustic exposure (audio-band readout); (e) is the $E^2$-even mains coupling that hits sign + flatness together; (f) removes the pump as an in-band source. The binding common thread: **CVR's flatness axis is exposed to any mechanical/acoustic/mains line inside DC–40 kHz**, so T-H is a first-class flatness-axis owner alongside T-F.
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

---

## PART 2 — THE TIERED QUALIFIER FRAMEWORK

Auditable per the open-goal-framing discipline: **graduation criteria are a set of auditable qualifier checks, not permanent tracks.** Three tiers, gated in order. **TIER-0 is binary (a must-hold): any option failing a TIER-0 check it *touches* is STRUCK from the science run** (it may survive as a reference/validation instrument). TIER-1 (form-axis enablement) and TIER-2 (performance targets) are graded, not gating, and record what remains to measure/select. Each option is graded only against the checks its trade **touches** (others marked "—").

**Grade legend:** **PASS** = the physics receipt shows the check is met by construction · **FAIL** = the physics precludes the check (struck at TIER-0; disabled-on-axis at TIER-1/2) · **UNK-M** = unknown, needs a measurement/derivation named in Part 3 · **—** = the trade does not touch this check.

### The 11 qualifier checks (with REQ-ID receipts)

| Tier | ID | Check | Receipt |
|---|---|---|---|
| **TIER-0** | T0.1 | Class-I-only DC field volume (no sign-degenerate dielectric) | `CVR-REQ-FIELDVOL` (`…_cvr-requirements_DERIVED.md` §4) |
| **TIER-0** | T0.2 | Holder unchanged across the $\ge4\times$ gap sweep | `CVR-REQ-FIXTURE` §3.3 |
| **TIER-0** | T0.3 | In-phase / quadrature ($\delta C$ vs $\delta D$) separation | `CVR-REQ-ACQ` §5.1 |
| **TIER-0** | T0.4 | Simultaneous multi-tone (3–4 tones DC–40 kHz, one acquisition) | `CVR-REQ-ACQ` §5.2 (sequential runs let drift fake dispersion) |
| **TIER-0** | T0.5 | Binding not-AVE-confirming frame (corroborative-null class) | `CVR-REQ-FRAME` |
| **TIER-1** | T1.1 | Log-log $d$-power slope resolution $\sigma_s\le0.1$ (per-point precision $\sim8$–$12\%$) | `CVR-REQ-FIXTURE` §3.4 |
| **TIER-1** | T1.2 | Frequency-flatness discrimination across DC–40 kHz | `CVR-REQ-ACQ` §5.2 flatness axis |
| **TIER-1** | T1.3 | Sign-axis integrity (no sign-degenerate material in field volume *or* sense path) | `CVR-REQ-FIELDVOL` §4 + `CVR-REQ-STANDOFF` item 2 |
| **TIER-2** | T2.1 | $\delta C/C$ floor (representative $\Phi\sim10^{-8}$) | `CVR-REQ-ACQ`; §1 bias-bound arithmetic |
| **TIER-2** | T2.2 | Drift/hour (the flatness/dispersion budget owner) | `CVR-REQ-ACQ` §5.2 + T-F |
| **TIER-2** | T2.3 | Pull-in margin $V_{max}\le V_{PI}/2$ ($V_{PI}\approx18.3$ kV, $V_{PI}/2\approx9.1$ kV at the §3.1 representative fixture) | `CVR-REQ-FIXTURE` §3.1 |

> **T0.5 note.** T0.5 is a *protocol/framing* must-hold, not a hardware property: it is PASS for every hardware option provided the option is documented under `CVR-REQ-FRAME` (validation-ladder + anomaly-bound, never AVE-confirming). It is listed so the framework is complete and so any future protocol that headlines an AVE confirmation is auto-struck. Hardware-option tables below therefore grade T0.1–T0.4 and T1/T2; T0.5 is carried once, at the framework level (PASS by construction of this document).

### T-A grading — gap-holding construction

| Option | T0.1 field-vol | T0.2 holder | T1.1 d-power | T1.3 sign | T2.3 pull-in | Physics receipt |
|---|---|---|---|---|---|---|
| (a) vacuum-gap spacer | **PASS** | via T-C | UNK-M | **PASS** | UNK-M | vacuum-only field volume (cleanest T0.1); soft/hard-to-char $k$ → pull-in subtraction + slope both need $k$ measured (§3.2) |
| (b) fused-silica spacer | **PASS** | via T-C | UNK-M | **PASS** | **PASS** | Class-I linear $C(V)$; high $k$; but a solid in the field volume shifts $C_0$/geometry — model before the $d$-power fit |
| (c) flexure monolith | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | best-known continuous $k$ → well-posed $d^{-3}$ subtraction; ⚠ flexure resonances are a T1.2 flatness term |
| (d) optical-flat + kinematic ball | **PASS** | UNK-M | **PASS** | **PASS** | **PASS** | deterministic absolute gap + Class-I field volume; gap *quantized* by ball set; Hertzian contact compliance UNK-M; swap disturbs (T0.2) |
| (e) sapphire spacer | **PASS** | via T-C | UNK-M | **PASS** | **PASS** | stiffest + lowest loss tangent → a T1.2 flatness *boost*; $C_0$ shift to model |
| (f) MEMS cell | UNK-M | **PASS** | **PASS** | UNK-M | **PASS** | self-reporting pull-in ($k$ known); ⚠ thermal-SiO₂ must be verified Class-I-linear at field (T0.1/T1.3 UNK-M); small stroke fights the $\ge4\times$ sweep |

### T-B grading — HV-standoff / sense topology

| Option | T0.4 simultaneity | T1.2 flatness | T1.3 sign | T2.1 floor | Physics receipt |
|---|---|---|---|---|---|
| (a) series blocking cap | ok | UNK-M | UNK-M | **PASS** | blocking cap in series → its $C(V)/D(V)$ is $E^2$-even & sign-degenerate; PASS only if Class-I + characterized (`CVR-REQ-STANDOFF` item 2) |
| (b) virtual-ground transimpedance | ok | **PASS** | **PASS** | **PASS** | no series blocking element in the signal path (topological exclusion); front-end bias-current/BW care |
| (c) guard / driven-shield | — | **PASS** | **PASS** | — | hardening layer; combine with (b), not standalone |
| (d) bias-tee | ok | UNK-M | UNK-M | **PASS** | choke+coupling-cap transfer fn must be characterized DC–40 kHz; coupling-cap $C(V)$ = same sign-degenerate care as (a) |
| (e) ratio-transformer bridge | ⚠ (pairs T-G(c) sequential) | **PASS** | **PASS** | **PASS** (metrology) | standoff cap *nulled by ratio*; best sign+floor; but couples to a sequential platform → T0.4 tension |
| (f) resonant-tank / $f$-readout | **FAIL** | UNK-M | **PASS** | **PASS** | single-band resonator collapses simultaneous multi-tone (T0.4) → **STRUCK as standalone** unless multiplexed |
| (g) floating-at-potential | ok | UNK-M | **PASS** | UNK-M | no series standoff element; floating front-end stability UNK-M |

### T-C grading — gap-sweep mechanism

| Option | T0.2 holder | T1.1 d-power | T1.2 flatness | Physics receipt |
|---|---|---|---|---|
| (a) discrete shim | UNK-M (swap disturbs) | **PASS** (absolute gap) | **PASS** (no creep) | re-clamp per point risks $k$/parallelism change (T0.2, §3.3) |
| (b) flexure + closed-loop nanopositioner | **PASS** | **PASS** | **PASS** | continuous, holder unchanged, no open-loop creep; stroke/vendor UNK (the H5-class travel issue) |
| (c) piezo open-loop | UNK-M | **FAIL** | **FAIL** | log-creep mis-places $d$ (T1.1) *and* is $f$-structured (T1.2) — `…boundary-conditions.md:198`; PASS only closed-loop |
| (d) kinematic ball-swap | UNK-M (swap) | **PASS** | **PASS** | deterministic gap, no creep; quantized + swap-disturbance |
| (e) thermal-CTE actuator | ok | UNK-M | **FAIL** | hard-couples gap to the thermal channel → thermal drift is simultaneously a $d$-error and an $f$-structured flatness term |
| (f) voice-coil closed-loop | **PASS** | **PASS** | **PASS** | continuous, large stroke; stray $B$/force UNK-M (irrelevant to ε-load, but a fixture-force term to bound) |
| (g) fixed-gap array | **PASS** (no motion) | UNK-M | **PASS** | strongest T0.2 pass; but cell-to-cell $A$/parallelism variation replaces sweep repeatability → the $d$-power fit is across cells |

### T-E grading — cell material / geometry

| Option | T1.1 d-power | T1.3 sign (field uniformity) | T2.1 floor | Physics receipt |
|---|---|---|---|---|
| (a) parallel-plate | **PASS** | **PASS** | baseline | the geometry the $d^{-2}$-vs-$d^{-3}$ axis is *derived* for (§3); uniform field → single $A=E/E_{yield}$ |
| (b) cylindrical / coaxial | **FAIL** (as-derived) | UNK-M | **PASS** | $E(r)$ non-uniform → $A$ radius-dependent; $d$-power must be **re-derived** or the axis is lost |
| (c) interdigital / comb | **FAIL** | **FAIL** | **PASS** | fringe-dominated ($\sim d^{-1}$), strongly non-uniform field; both the $d$-power axis and the single-$A$ sign premise lost |
| (d) cross-capacitor (calculable) | **FAIL** (no gap sweep) | **PASS** (best) | **PASS** (best) | calculable, self-guarding → cleanest field volume/floor, but a fixed-$C$ object, not a sweep cell → a **reference/validation** geometry |
| (e) spherical / curved | UNK-M | UNK-M | baseline | mild non-uniformity (a soft version of the T-D-ruled tip); parallelism-robust, partial $d$-power sacrifice |

### T-F grading — thermal control (drift-budget owner)

| Option | T1.2 flatness | T2.2 drift/hour | Physics receipt |
|---|---|---|---|
| (a) ambient / stable-room | UNK-M | UNK-M (largest) | viable ONLY if simultaneous-multi-tone common-mode rejection carries the whole flatness budget |
| (b) insulated shroud + RTD | **PASS** (if common-mode) | **PASS** (~1 K) | CLEAVE A3 discipline; bounds drift, does not eliminate |
| (c) active TEC/oven (mK) | **PASS** | **PASS** (best) | tightens residual drift below the flatness floor; supports sequential platforms |
| (d) cryogenic | **PASS** (boost) | **PASS** | lower loss tangent *sharpens* the flatness discriminator; new cryostat vibration (→T-H) + cold-gap re-zero (→T1.1) UNK-M |

### T-G grading — acquisition chain

| Option | T0.3 I/Q | T0.4 simultaneity | T1.2 flatness | T2.1 floor | Physics receipt |
|---|---|---|---|---|---|
| (a) cRIO 4×4 lock-in | **PASS** | **PASS** | **PASS** | UNK-M | native simultaneous phase-coherent multi-channel; ±10 V → hard T-B standoff dependency; floor vs $\Phi\sim10^{-8}$ needs measurement |
| (b) commercial LCR bridge | **PASS** | **FAIL** | via T-F | **PASS** | $C_p$–$D$ turnkey but one frequency at a time → **STRUCK as science-run acquisition**; retain as reference instrument |
| (c) precision cap bridge (AH2700A) | **PASS** | **FAIL** | via T-F | **PASS** (ppm) | best floor + $\tan\delta$, transformer-ratio; discrete sequential frequencies → **STRUCK as science run**; ideal `CLV-REQ-VALIDATE` reference |
| (d) VNA / impedance analyzer | **PASS** | **FAIL** | — | **PASS** | wideband/resonant class, not sub-audio simultaneous → **STRUCK** as the DC–40 kHz acquisition; pairs only with T-B(f) |
| (e) custom FPGA multi-tone | **PASS** | **PASS** | **PASS** | UNK-M | synthesizes `CVR-REQ-ACQ` exactly (simultaneous tones + per-tone I/Q + INCONCLUSIVE-bin); a build |
| cabling (i) guarded triax | — | — | — | T1.3 **PASS** | driven guard rejects cable-$C(V)$ + leakage — the sense-path-clean choice |
| cabling (ii) twinax | — | — | — | T1.3 UNK-M | common-mode reject, but cable dielectric $C(V)$ still in the differential path |
| cabling (iii) coax | — | — | — | T1.3 **FAIL** | cable dielectric $C(V)$ in series = sign-degenerate → disfavored on the sense path |

### T-H grading — environmental isolation

| Option | T1.2 flatness | T2.1 floor | Physics receipt |
|---|---|---|---|
| vibration (a) air-table | UNK-M | UNK-M | in-band ($\le40$ kHz) vibration → $\delta C/C=-\delta d/d$ AT $f_{vib}$ on the flatness axis |
| vibration (b) active isolation | **PASS** | **PASS** | needed where audio-band vibration overlaps probe tones |
| vibration (c) rigid monolith | **PASS** | **PASS** | push lowest fixture resonance $>40$ kHz (out of the probe band) |
| acoustic (d) enclosure | **PASS** | — | CVR-specific: audio-band probe → acoustic pressure is a *direct in-band* modulator |
| EMI (e) Faraday + driven guard | **PASS** (w/ sync-notch) | — | 2$f$-mains (100/120 Hz) is $E^2$-even → lands on sign + flatness; in-band harmonics need line-sync reject |
| pump (f) turbo decouple | **PASS** | — | bellows / valve-off-coast; the turbo is an in-band vibration SOURCE (inherited `CLV-REQ-VIB`) |

### TIER-0 strikes (the binary gate, applied)

Options that FAIL a TIER-0 check they touch, hence **STRUCK from the science-run configuration** (retained only where noted as a reference/validation instrument):

- **T-B(f) resonant-tank** — FAILS **T0.4** (single-band resonator ≠ simultaneous multi-tone). Struck as standalone; survives only if multiplexed into a multi-band tank set.
- **T-G(b) commercial LCR bridge, T-G(c) precision cap bridge, T-G(d) VNA/impedance analyzer** — all FAIL **T0.4** (sequential single-frequency acquisition). Struck as the *science-run* acquisition; **T-G(c) is retained as the metrology-grade `CLV-REQ-VALIDATE` reference** (inject a known even-in-$V$ step and confirm the chain resolves it).

**No hardware option outright fails T0.1 (Class-I field volume) — MEMS (T-A(f)) is UNK-M pending the thermal-SiO₂ linearity check, not a strike.** No option fails T0.5 (framing) as long as this document's `CVR-REQ-FRAME` binding is respected. The TIER-1 disablers (T-C(c) open-loop piezo, T-C(e) thermal-CTE, T-E(b)/(c) non-parallel geometries, T-G cabling(iii) coax) are **not** TIER-0 strikes — they are recorded as disabled-on-axis, available if their axis is defended another way.

---

## PART 3 — REMAINS-TO-HIT-TARGETS (the gap table)

> **Honest rail (`CVR-REQ-FRAME`).** At bench magnitude the lattice's own conjunction-passing signal is $\delta C/C\sim10^{-17}$ — unreachable (the bias-bound arithmetic, `…_cvr-requirements_DERIVED.md` §1: a strong bench point bounds the anomalous coefficient only to $|\kappa|<1.3\times10^{10}$, ~10 OOM looser than the lattice $|\kappa|=\tfrac32$). **These gaps are therefore what the bench must close to be a competent *fixture-vs-anomaly classifier + material-analog ladder*, NOT what it must close to detect the vacuum kernel.** Every "must achieve" below is a classifier/ladder target.

### The best-graded option combination (recorded as ANALYSIS — SELECTS NOTHING)

Reading the Part-2 tables for the config that maximizes PASS grades across all three form axes (this is a grade-count observation, **not** a selection): **T-E(a) parallel-plate** (the only d-power-PASS geometry, consistent with the T-D ruling) · **T-A(c) flexure monolith OR T-A(e) sapphire spacer** (a genuine fork: (c) is d-power-best via known continuous $k$ but carries a T1.2 flexure-resonance caveat; (e) is flatness-best via low loss tangent but its $C_0$-shift leaves T1.1 UNK-M) · **T-B(b) virtual-ground transimpedance** (removes the series sign-degenerate element) · **T-C(b) closed-loop nanopositioner OR T-C(f) voice-coil** (continuous, holder-unchanged) · **T-G(a) cRIO OR T-G(e) FPGA multi-tone + cabling(i) guarded triax** (simultaneous I/Q) · **T-F(b/c/d)** + **T-H(b/c/d/e/f)** (drift + in-band isolation). This combination clears every TIER-0 gate and leaves the UNK-M items enumerated below.

### Gap table — per form axis + receipt-debts

| Axis / debt | Bench MUST achieve (classifier target) | Best-combo DELIVERS | GAP (what remains) | Closing action |
|---|---|---|---|---|
| **SIGN** | Resolve the sign of the $E^2$-even residual; guarantee the ONLY voltage-dependent dielectric in the field volume AND the sense path is Class-I (so a *negative* residual cannot be a support / blocking-cap $C(V)$ artifact); I/Q split of $\delta C$ vs loss $\delta D$ (`§4, §5.1`) | Class-I field volume (T-A a/b/c/e PASS) + no series standoff element (T-B(b) PASS) + guarded triax (T-G(i)) + I/Q (T-G a/e) → **T1.3 achievable** | The support-dielectric class must be *verified* (MEMS SiO₂ UNK-M); any retained series/coupling element $C(V)$ is UNK-M | **SELECT** Class-I field volume + virtual-ground topology; **MEASURE** any residual blocking-element $C(V)$ (receipt-debt below) |
| **d-POWER** | $\sigma_s\le0.1$ → per-point fractional precision $\sim8$–$12\%$ over a $\ge4\times$, $\ge4$-point fixed-$V$ sweep (`§3.4`); fixture $k$ KNOWN so the $d^{-3}$ electrode term is *subtracted*, not feared; parallel-plate (the only geometry the $d^{-2}$ axis is derived for, T-E(a)) | Parallel-plate (T-E(a)) + continuous closed-loop sweep, holder unchanged (T-C b/f) + known-$k$ fixture (T-A c/f) → **T1.1 axis enabled** | (1) fixture $k$/$V_{PI}$ UNK-M until measured; (2) per-point $\sim10\%$ precision requires the residual lifted above the T2.1 floor $\Phi$ (UNK-M); (3) which sweep option preserves "holder unchanged" best is a SELECT | **MEASURE** $V_{PI}$ pre-run (pins $k$, §3.2); **SELECT** continuous closed-loop sweep + parallel-plate; **VERIFY** per-point precision $>$ floor |
| **FLATNESS** | 3–4 SIMULTANEOUS tones DC–40 kHz (drift common-mode, `§5.2`); flat $E^2$-even response distinguished from $f$-structured fixture terms (spring-mass resonances, PZT creep, Debye/soakage, in-band vibration/acoustic/2$f$-mains); I/Q routes loss into $\delta D$ | Simultaneous multi-tone (T-G a/e PASS) + drift control (T-F b/c/d) + in-band isolation (T-H b/c/d/e/f), avoiding T-C(c)/(e) → **T1.2 axis enabled** | (1) fixture resonances (T-A(c) flexure) must sit outside DC–40 kHz or be characterized (UNK-M); (2) the anhysteretic claim is gated by the SPICE constitutive-loop fence (`research/2026-06-13_spice-cvr-constitutive-loop_prereg.md` §0.1); (3) the residual in-band acoustic/vibration/mains floor UNK-M until isolation is measured | **MEASURE** the fixture resonance spectrum + the in-band isolation floor; **DERIVE/close** the SPICE anhysteretic fence; **SELECT** simultaneous platform + isolation |
| **debt: ~$10^{11}$ V/m field-evaporation ceiling** | A citable source for the field-evaporation ceiling used in the T-D tips-are-5-OOM-short rationale | v1 §T-D + this doc T-D carry it **[TAG: from-memory engineering bound]** | No citable receipt; directionally load-bearing for the "tips 5 OOM short" line — **but T-D is already ruled PLATES on two *independent* grounds** ($d^{-2}$ destruction + field-emission confound), so the pin does NOT gate the ruling | **DERIVE/CITE** a field-evaporation ceiling source before this migrates to the KB (auditor-lane; non-blocking for the bench) |
| **debt: fixture-$k$ measurement** | $k$ known so the $d^{-3}$ electrode-attraction term is computed + subtracted (`§3.2`: the snap-in IS the $d^{-3}$ systematic announcing itself) | The Part-2 T2.3 / T1.1 grades assume $k$ known; the assembled fixture's $k$ is UNK-M | $k$ is UNK until the assembled fixture's pull-in $V_{PI}$ is measured; without it the $d^{-3}$ term is a *fear*, not a subtraction | **MEASURE** $V_{PI}$ of the assembled fixture BEFORE any $C(V)$ run (mandatory pre-run characterization, §3.2) |
| **debt: blocking-element $C(V)$** | Any series standoff element's $C(V)/D(V)$ characterized below the `CVR-REQ-ACQ` floor across the bias range (it is $E^2$-even + sign-degenerate + potentially $f$-structured) | T-B(b/g) *removes* the series element (topological exclusion); T-B(a/d/e) retain one | UNK-M for any topology (a/d) that keeps a series/coupling element; the confound sits on BOTH the sign and flatness axes | **MEASURE** the Class-I blocking/coupling element $C(V)$ vs bias below floor, OR **SELECT** T-B(b/g) (no series element) |

**Reading of the gap table.** Every TIER-0 gate is *clearable* by the best-graded combination — there is no physics wall between the current option space and a competent classifier/ladder bench. What "remains to hit the targets" is **three measurements** ($V_{PI}$/$k$; any retained blocking-element $C(V)$; the fixture-resonance + in-band-isolation floor), **one derivation/closure** (the SPICE anhysteretic fence), **one citation debt** (the $10^{11}$ V/m ceiling, non-blocking), and **the selections themselves** (field-volume material, standoff topology, sweep mechanism, acquisition platform, thermal + isolation class). None of these is an AVE-confirmation gate; all serve the classifier + material-analog ladder per `CVR-REQ-FRAME`.

---

## PART 4 — DECISIONS REMAIN OPEN + updated dependency map

**SELECT NOTHING.** Every engineering entry in Parts 1–3 ends STATUS: OPEN. The single recorded decision in the whole CVR trade study is the **T-D PLATES theory ruling** (carried forward from v1, §T-D), which is a physics ruling, not an engineering make-vs-buy. All other trades — T-A, T-B, T-C, T-E, T-F, T-G, T-H — and every option within them are adjudicated by **Grant + collaborator in a separate session**. The tiered grades and gap table above make the option analysis + the physics receipts visible BEFORE any selection; they do not make a selection. The "best-graded option combination" in Part 3 is a **grade-count observation, not a recommendation**.

### Updated Part-B dependency map (which trades must freeze TOGETHER)

| Trade | Must freeze WITH | Why (physics-relevant coupling) | REQ-IDs |
|---|---|---|---|
| **T-A** (gap-holding) | T-C (sweep), T-E (geometry), T-D (plates ruling) | the holder material sits in the field volume (`CVR-REQ-FIELDVOL`) AND sets $k$ for the pull-in subtraction; the sweep must keep that holder unchanged across the $\ge4\times$ span; the geometry decides whether the $d^{-2}$ axis exists at all | `CVR-REQ-FIXTURE`, `CVR-REQ-FIELDVOL` |
| **T-B** (standoff) | T-G (acquisition) | the standoff network sits in series with every probe tone; whether a blocking element carries signal current (T-B a/d) or not (T-B b/g) decides whether a $C(V)$ confound is in the sense path; T-B(f) resonant vs T-G simultaneity is a hard T0.4 coupling | `CVR-REQ-STANDOFF`, `CVR-REQ-ACQ` |
| **T-C** (sweep) | T-A (holder), T-E (geometry) | the $d^{-2}$-vs-$d^{-3}$ log-log axis needs holder/stiffness constant across the sweep; open-loop creep couples into BOTH the gap-power and flatness axes; the geometry sets the exponent being fit | `CVR-REQ-FIXTURE`, `CVR-REQ-ACQ` |
| **T-D** (plates) | T-E (geometry) | the PLATES ruling IS the parallel-plate geometry selection — T-D and T-E(a) are the *same* physics decision (recorded ruling, not re-opened) | `CVR-REQ-FIXTURE`, `CVR-REQ-FRAME` |
| **T-E** (geometry) | T-A, T-C, T-D | the geometry sets the $d$-power exponent the whole bench fits; only parallel-plate (T-E(a)) preserves the derived $d^{-2}$ axis | `CVR-REQ-FIXTURE`, `CVR-REQ-FIELDVOL` |
| **T-F** (thermal) | T-G (acquisition), T-H (isolation) | simultaneous multi-tone (T-G a/e) makes drift common-mode → RELAXES T-F toward (a/b); a sequential platform pushes T-F to (c/d); cryo (T-F d) adds a vibration source → T-H | `CVR-REQ-ACQ` |
| **T-G** (acquisition) | T-B (standoff), T-F (thermal), T-H (isolation) | the front end sees the standoff network in series (T-B); simultaneity-vs-sequential sets the T-F drift burden; the in-band confounds T-H isolates land on the acquisition's own flatness axis | `CVR-REQ-ACQ`, `CVR-REQ-STANDOFF` |
| **T-H** (isolation) | T-A/T-C (fixture resonances), T-F(d) cryo, T-G (tone placement) | in-band ($\le40$ kHz) vibration/acoustic/2$f$-mains land on the flatness axis the acquisition reads; the fixture resonances (T-A/T-C) set *what* must be isolated; cryo (T-F d) adds a vibration source | `CVR-REQ-ACQ` |

### The two freeze-clusters (the synthesis)

The eight trades collapse into **two tightly-coupled freeze-clusters that meet at one seam**:

- **Cluster 1 — the FIXTURE / $d$-power cluster: {T-A, T-C, T-E, T-D}.** These jointly own the $d^{-2}$ gap-power axis, the holder-unchanged clause, and the fixture $k$ (pull-in subtraction). They must be frozen as a group because the geometry (T-E), the holder (T-A), and the sweep mechanism (T-C) together determine whether a clean, subtractable $d^{-2}$-vs-$d^{-3}$ separation exists — and T-D already fixed the geometry base (PLATES = T-E(a)).
- **Cluster 2 — the ACQUISITION / flatness cluster: {T-B, T-G, T-F, T-H}.** These jointly own the flatness axis (simultaneous multi-tone + I/Q), the drift budget, the in-band isolation, and the sense-path $C(V)$ cleanliness. They must be frozen as a group because the acquisition platform (T-G) sets the simultaneity that determines the thermal burden (T-F), reads through the standoff network (T-B), and is exposed to exactly the in-band confounds T-H controls.
- **The single seam between the clusters:** the **fixture mechanical resonances** (Cluster 1: T-A(c) flexure, T-C spring-mass) land directly on the **flatness axis** (Cluster 2) — an $f$-structured term inside DC–40 kHz. Plus the geometry/gap (Cluster 1) sets the $C_0$ the acquisition (Cluster 2) reads. So the two clusters can be designed largely independently EXCEPT that the Cluster-1 resonance spectrum must be handed to Cluster-2's flatness-axis budget (the gap-table FLATNESS row's "measure the fixture resonance spectrum" closing action is exactly this hand-off).

### Standing rule for this register

**SELECT NOTHING** (except the recorded T-D theory ruling: PLATES, carried forward from v1). Every engineering entry ends STATUS: OPEN. Decisions are adjudicated by Grant + collaborator in a separate session; this v2 register makes the *broadened* option-analysis + tiered qualifiers + remains-to-target gaps + dependencies visible BEFORE any selection.

---

**Provenance.** v1: `research/2026-07-13_cvr-trade-study_DECISIONS-OPEN.md` (preserved). Requirements datasheet (derived numbers, re-verified against this doc): `research/2026-07-13_cvr-requirements_DERIVED.md`. Ratified prediction leaf: `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:25-38`. Canonical scales re-verified this branch: `src/ave/core/constants.py:496` (V_SNAP ≈ 511 kV), `:505` (V_YIELD ≈ 43.65 kV), `:516` (E_YIELD ≈ 1.13e17 V/m). Structural template: the CLEAVE-01 doc set (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/`).

