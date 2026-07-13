# CVR Bench — Trade Study / Decision Register (STATUS: OPEN throughout)

**Date:** 2026-07-13 · **Lane:** CVR dielectric-C-V bench (implementer) · **Status:** DECISION RECORD, not a claim. Every entry ends STATUS:OPEN. SELECTS NOTHING. Cost OUT OF SCOPE.

> **THIS IS A DECISION RECORD, NOT A CLAIM.** Following the CLEAVE-01 pattern (`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/cleave-01-trade-study-decision-register.md`): this is an OPEN decision-space record of each CVR make-vs-buy / design-knob as a worked option set — options + physics-relevant differences + dependencies — each ending **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.** The derived, frozen boundary conditions are in the sibling `research/2026-07-13_cvr-requirements_DERIVED.md` (the `CVR-REQ-*` datasheet). **Derived = there. Open = here.**

**Cost is OUT OF SCOPE here** (adjudicated separately); these are feasibility-and-fit tradeoffs, not a BOM roll-up.

> **★ Binding epistemic frame (`CVR-REQ-FRAME` — stated in full in the sibling `research/2026-07-13_cvr-requirements_DERIVED.md`; cited here by ID, cite-don't-duplicate).** Before any trade below: the CVR bench is a **validation-ladder + material-analog shape bench** and a **one-sided anomaly bound (corroborative-null class)** — it is **NOT an AVE-confirming channel**. The magnitude route is dead three ways; at bench magnitude the lattice's own conjunction-passing signal is $\sim10^{-17}$, unreachable. **Any conjunction-passing residual at bench magnitude falsifies AVE *and* QED alike.** Every trade below serves the material-analog ladder + the fixture-vs-anomaly classifier, never an AVE confirmation.

---

## Part A — the trades

### T-A — gap-holding construction (vacuum spacer / fused-silica / flexure)

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE` (stiffness $k$ from the $d^{-3}$ pull-in subtraction; $\ge4\times$ fixed-$V$ gap sweep, holder unchanged), `CVR-REQ-FIELDVOL` (Class-I / vacuum only in the DC field volume — the gap-holder material IS in the field volume).
- **Options:**
  - **(a) Vacuum-gap spacer** (rigid insulating standoffs outside the field volume, vacuum between the plates). Field volume threads vacuum only — the cleanest `CVR-REQ-FIELDVOL` pass. Stiffness set by the standoff geometry/material.
  - **(b) Fused-silica (Class-I) spacer** in the field volume. Class-I linear $C(V)$ (passes `CVR-REQ-FIELDVOL`), high stiffness, low CTE. A solid dielectric partly in the field volume changes the effective $C_0$ and the $d^{-2}$ vs $d^{-3}$ geometry — must be modeled.
  - **(c) Flexure-guided plate** (monolithic flexure holds one plate, sweeps the gap). Highest, best-characterized stiffness (flexure $k$ is designable + measurable), naturally parallel-keeping; but the flexure itself is a spring whose resonances are an $f$-structured term on the `CVR-REQ-ACQ` flatness axis.
- **Physics-relevant differences:** (a) maximizes `CVR-REQ-FIELDVOL` cleanliness (vacuum-only field volume) at the cost of a less-stiff, harder-to-characterize $k$; (b) trades a Class-I solid in the field volume (modeled $C_0$ shift) for high, stable stiffness; (c) gives the best-known $k$ (directly serving the `CVR-REQ-FIXTURE` pull-in subtraction) and best parallelism, but injects mechanical resonances onto the flatness axis. Class-II ceramic is EXCLUDED from all options by `CVR-REQ-FIELDVOL` (the one sign-degenerate confound).
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-B — standoff topology (series blocking cap vs virtual-ground transimpedance vs guard)

- **Builds to REQ-IDs:** `CVR-REQ-STANDOFF` (sense node at virtual ground, DC never threads the sense path; blocking element's $C(V)$ Class-I or topologically excluded; standoff-network calibration-stability), couples to `CVR-REQ-ACQ` (the standoff network sits in series with every probe tone).
- **Options:**
  - **(a) Series blocking cap** into the sense node. Simple; but the blocking cap sits directly in series with the signal and its OWN $C(V)/D(V)$ is an $E^2$-even, potentially $f$-structured confound *sign-degenerate with the lattice*. Requires a Class-I (C0G/vacuum/air) blocking cap and a characterized/stable network — the load-bearing `CVR-REQ-STANDOFF` care point.
  - **(b) Virtual-ground transimpedance** (bias on the driven electrode, sense electrode at op-amp virtual ground). The sense node is held at $\approx0$ V so the kV never appears there and no series blocking element carries signal current — the topology that most directly satisfies "DC never threads the sense path." Front-end bias-current / bandwidth become the care points instead.
  - **(c) Guard / driven-shield** around the sense node (bias stood off by a guarded triax + driven guard). Rejects leakage + stray coupling; typically combined with (b) rather than a standalone standoff.
- **Physics-relevant differences:** (a) puts a voltage-dependent dielectric in series with the signal (the exact thing `CVR-REQ-STANDOFF` + `CVR-REQ-FIELDVOL` warn against) unless the blocking element is Class-I; (b) removes the series blocking element from the signal path entirely (topological exclusion — the preferred `CVR-REQ-STANDOFF` reading) at the cost of front-end bias/BW discipline; (c) is a leakage/EMI hardening layer, not a standoff by itself. `CLV-REQ-VALIDATE` (`cleave-01-requirements-boundary-conditions.md:62`) applies to whichever topology: inject a known even-in-$V$ series-C step and confirm the chain resolves it.
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-C — gap-sweep mechanism (shim set vs flexure + micrometer vs piezo)

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE` (the $\ge4\times$ fixed-$V$ gap sweep with the holder/stiffness unchanged; the $d^{-2}$-vs-$d^{-3}$ log-log axis lives or dies on this), couples to `CVR-REQ-ACQ` (a sweep mechanism that creeps in $f$ contaminates the flatness axis).
- **Options:**
  - **(a) Discrete shim set** (swap calibrated spacers for each gap). Dead-simple, no active creep, absolute-gap known from the shim. But each swap DISTURBS the fixture (re-clamps → parallelism + $k$ can change between points), directly threatening the "holder unchanged" clause of `CVR-REQ-FIXTURE`; and it is not a continuous sweep.
  - **(b) Flexure + micrometer / closed-loop nanopositioner.** Continuous, repeatable, keeps parallelism, $k$ characterizable; a closed-loop capacitive-sensor stage places $d$ to the relative accuracy the log-log slope fit needs. The larger stroke (to span $\ge4\times$ at a ~100 µm baseline) narrows the vendor list (the same H5-class travel issue as CLEAVE-01).
  - **(c) Piezo (PZT) actuator.** Fine resolution, but **open-loop PZT log-creep (~10–20 nm over the first seconds = the hold window) is a known $f$-structured confound** sitting directly on the `CVR-REQ-ACQ` flatness axis (receipt: `cleave-01-requirements-boundary-conditions.md:198`, "log-creep ~10–20 nm in the first seconds"). Usable only closed-loop; open-loop PZT contaminates both the gap-power axis (creep during the hold mis-places $d$) and the flatness axis (creep is $f$-structured).
- **Physics-relevant differences:** (a) zero active-creep but violates "holder unchanged" per swap; (b) preserves the fixture across a continuous sweep (best `CVR-REQ-FIXTURE` fit) at a stroke/vendor cost; (c) risks a creep term that is simultaneously an $f$-structured flatness confound and a gap-placement error — the one option that couples negatively into TWO of the three form axes unless closed-loop.
- **STATUS: OPEN — decision pending (Grant + collaborator). SELECT NOTHING.**

### T-D — tips vs plates — **core-session THEORY ruling RECORDED: PLATES**

- **Builds to REQ-IDs:** `CVR-REQ-FIXTURE` (the $d^{-2}$ parallel-plate gap-power axis), `CVR-REQ-FIELDVOL`, `CVR-REQ-FRAME` (what the bench can claim).
- **Distinct from the other trades.** T-A/T-B/T-C are OPEN engineering knobs. T-D **records a core-session THEORY ruling** (not an engineering make-vs-buy): the CVR bench stays **PARALLEL-PLATE**. The ruling is recorded here so the trade study is complete; it is a physics decision, not a knob left open.
- **Rationale recorded (why PLATES, why NOT tips):**
  1. **Tips cannot reach the window anyway.** Sharp-emission-tip enhancement maxes out at the field-evaporation ceiling of order $\sim10^{11}$ V/m. **[TAG: from-memory engineering bound — receipt OWED.]** That is still $\sim5$ orders of magnitude below the $A=1/\sqrt2$ NDC window, which opens at local fields $>10^{16}$ V/m (`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:36-38`). Tips do not buy reachability of the vacuum kernel — consistent with `CVR-REQ-FRAME` (magnitude route dead).
  2. **Tips destroy the parallel-plate $d^{-2}$ axis.** A tip makes the field map strongly non-uniform, so the C-readout averages the sag over a non-uniform field and the clean $V^2 d^{-2}$ (lattice) vs $V^2 d^{-3}$ (electrode-attraction) gap-power separation of `CVR-REQ-FIXTURE` is lost.
  3. **Tips add field-emission current as a confound.** At tip fields, field-emission current becomes its own $E$-dependent term contaminating the $E^2$-even capacitance channel.
- **Where the tip physics banks instead.** The $1/\sqrt2$ NDC snap-back is a parameter-free, incumbent-unpredicted instability — but at $>10^{16}$ V/m it is **facility-class**. It banks as a **FORWARD FALSIFIER candidate** (companion to the banked E-route vacuum birefringence `clm-pp3qwf`, `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`), **NOT as a CVR bench axis.** The tabletop CVR stays parallel-plate and honestly a material-analog / validation-ladder + anomaly-bound bench (`CVR-REQ-FRAME`).
- **STATUS: THEORY-RULED (PLATES). The remaining plate-construction choices are OPEN in T-A; the tip route is theory-closed for this bench (retained as a facility-class forward-falsifier note, not an open knob).**

> **⚠ Receipt owed (flag).** The $\sim10^{11}$ V/m field-evaporation ceiling is tagged from-memory (engineering bound). It is directionally load-bearing for the "5 OOM short" statement but should be pinned to a citable source before this trade migrates into the KB. Surfaced for the auditor lane.

---

## Part B — dependency map (which decisions must be frozen together)

| Trade | Must freeze WITH | Why (physics-relevant coupling) | REQ-IDs |
|---|---|---|---|
| T-A (gap-holding) | T-C (sweep mech), T-D (plates ruling) | the holder material sits in the field volume (`CVR-REQ-FIELDVOL`) AND sets $k$ for the pull-in subtraction; the sweep mechanism must keep that holder unchanged across the $\ge4\times$ span | `CVR-REQ-FIXTURE`, `CVR-REQ-FIELDVOL` |
| T-B (standoff) | acquisition front-end | the standoff network sits in series with every probe tone; whether a blocking element carries signal current (option a) or not (option b) decides whether a $C(V)$ confound is in the sense path | `CVR-REQ-STANDOFF`, `CVR-REQ-ACQ` |
| T-C (sweep mech) | T-A (holder) | the $d^{-2}$-vs-$d^{-3}$ log-log axis needs the holder/stiffness constant across the sweep; open-loop creep couples into BOTH the gap-power and flatness axes | `CVR-REQ-FIXTURE`, `CVR-REQ-ACQ` |
| T-D (plates) | — (theory-ruled) | recorded ruling; sets the parallel-plate $d^{-2}$ axis the whole bench depends on | `CVR-REQ-FIXTURE`, `CVR-REQ-FRAME` |

**Standing rule for this register:** **SELECT NOTHING** (except the recorded T-D theory ruling: PLATES). Every engineering entry ends STATUS: OPEN. Decisions are adjudicated by Grant + collaborator in a separate session; this register makes the option-analysis + dependencies visible BEFORE any selection.

---
