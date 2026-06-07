# Camassa–McLaughlin Entrainment / Vortex-Trapping in Stratification → AVE Electron-Soliton Genesis Confinement (Fork A) — a guided-analogy deep-dive

**Date:** 2026-06-07
**Lane:** implementer (research-doc — consistency-class mapping / literature deep-dive)
**Branch:** `analysis/2026-06-07-entrainment-vortex-trapping` (off `origin/main` @ `dbb60320`)
**Status:** SKELETON (incremental-write — one section per commit)
**Companions (same object, other lenses — cross-referenced, not edited):**
- `research/2026-06-07_electron-coherence-reynolds-mapping.md` (branch `analysis/2026-06-07-electron-coherence-reynolds`) — the Reynolds/loss-tangent lens on electron coherence; carries the canonical `S(Re,Re_c)` + Bingham + Kelvin-vortex corpus content this doc maps ONTO.
- `research/2026-06-07_electron-interstitial-rotor-synthesis.md` (branch `analysis/2026-06-07-electron-rotor-synthesis`) — the rotor/Meissner-cage ontology; defines the **Fork A/B/C/D** genesis taxonomy this doc's Mapping A targets.

> **One-line thesis.** A dense vortex ring falling through a sharp density transition either **traps** (stays at the interface) or **escapes** (core falls through), decided by whether viscous **entrainment** of light fluid accumulates enough buoyant reserve to rebound the core before it separates. Read as a *lens* (NOT imported physics) onto AVE genesis: **trap = confinement (the `Γ=−1` wall forms and the `(2,3)` winding closes); escape = MODE-III dissolution.** The AVE confinement mechanism is Meissner/saturation/`Γ=−1`, NOT buoyancy; the fluid supplies the *form* of a trap-vs-escape competition, and suggests a substrate-native **accumulation-rate vs leak-rate vs equilibration-rate** balance for Fork A. The whole mapping is **consistency-class** (echo, not chord); the one place it could grow teeth is flagged in §6.

---

## §0 — Scope, framing, honest classification, and access ledger

This document is a **guided-analogy mapping**, NOT an import of fluid physics into AVE. The
Camassa–McLaughlin (UNC Joint Fluids Lab) stratified-entrainment / vortex-trapping work is used as a
**lens** on one open AVE problem: **genesis confinement (Fork A)** — why a driven seed at a K4 A–B
node pair either confines into a stable electron (`Γ=−1` wall forms, `(2,3)` winding closes) or
dissolves (MODE III). The AVE confinement mechanism is **Meissner / Axiom-4 saturation / `Γ=−1`**
(`pair-production-axiom-derivation.md`, `01_vacuum_circuit_analysis.tex:294-362`), NOT literal
buoyancy. The fluid result supplies the *grammar* of a trap-vs-escape competition; every load-bearing
variable is re-grounded in substrate terms below, and §2.3 states exactly where the analogy breaks.

**Why this is not a re-map.** The companion coherence-Reynolds doc already specialised the corpus's
`δ_AVE ↔ Reynolds` axis and `S(Re,Re_c)` kernel to electron coherence. This doc maps a **different**
fluid phenomenon — *buoyant trapping at a stratification interface*, governed by an **entrainment /
buoyancy (Richardson/Froude-class) competition**, NOT a Reynolds (shear-instability) competition — onto
a **different** AVE target — *genesis confinement*, NOT steady-state coherence. The two are
complementary: Reynolds → laminar/turbulent (coherence); entrainment-buoyancy → trap/escape (genesis).
Vol 4 Ch 2 (`02_vacuum_fluid_dynamics.tex`) carries an "Aerodynamic Isomorphism" (compressible /
bow-shock), but **no stratified-entrainment content** — so this mapping is new relative to that chapter.

### Skills fired (and where)

- **`substrate-native-check`** — CP1 (the substrate runs reactive K4-TLM scatter+connect + Cosserat
  saturation, NOT energy-basin minimisation; "trapping" here is `Γ=−1` reflection + winding-closure,
  not a potential well); CP2 (sector: genesis is **cross-coupled** — V-sector `(2,3)` + Cosserat-`ω`
  "2", Op14 saturation the cross-coupling); CP8 (this is a **hosting/emergence** problem — the
  discipline is to grow from the generative precursor / driven seed, NOT plant the finished `(2,3)`,
  exactly the open Fork-A finding). Applied at §2.3–§2.4 before any criterion is proposed.
- **`consistency-vs-emergence`** — every section CLASSIFIED in the ledger below. The whole mapping is
  consistency-class (lens), inheriting the `historical-precedents.md:39` "echo, not chord" ceiling;
  §2.4 + §6 hold the single emergence *candidate* and assess it honestly.
- **`ave-discrimination-check`** — §2.3 (where the analogy breaks) + §6 (SM-counterfactual): a
  trap/escape *threshold* is generic bistability, NOT AVE-distinct; only a substrate-traced **number**
  would be.
- **`ave-evidence-framing-discipline`** — strength language kept honest; "suggests", "candidate",
  "hypothesis" used deliberately; the access ledger discloses the read-vs-inferred denominator.
- **`verify-before-cite`** — every corpus file:line below was opened/greped this session (companion
  docs, `19_phase_transition_turbulence.tex`, `01_vacuum_circuit_analysis.tex`,
  `pair-production-axiom-derivation.md`, `historical-precedents.md`, `vol2/claim-quality.md:670`,
  `_orchestration/2026-06-06_genesis-next-steps-scope.md`). Paper content tagged read-vs-inferred.
- **`pre-test-physics-check`** — §7 surfaces ONE plumber-physical question to Grant (dissipative-
  equilibration vs reactive-resolution of the over-amplitude state) BEFORE any driver is scoped.
- **`phase-space-coordinate-check`** — §2.3 + §5: every CFD construct here is **real-space**; the AVE
  `(2,3)` lives in `(V_inc,V_ref)` phase space (Clifford torus). Any *test* must measure in matching
  coordinates; the fluid lens is intuition, not a measurement prescription.

### Consistency-vs-emergence ledger (per section)

| § | Claim | Class | Basis |
|---|---|---|---|
| §1 | Extraction of the fluid trap/escape phenomenology + VARDEN method | **literature record** | papers; read-vs-inferred tagged per sub-section |
| §2 | trap=confinement / escape=MODE-III; structural isomorphism to Fork A | **consistency (lens)** | inherits `historical-precedents.md:39` echo-not-chord ceiling |
| §2.4 | substrate-native accumulation/leak/equilibration-rate balance for Fork A | **EMERGENCE CANDIDATE (structural)** | the one reach past lens; assessed honestly in §6 — *form*, not closed number |
| §3 | entrainment-buoyancy ↔ inertia (added-mass lens on `clm-jwyy6l`) | **consistency (lens) + discrimination** | added-mass(reactive) vs viscous-entrainment(dissipative) split flagged |
| §4 | stratification ↔ operating-point field `A₀(r)` / yield surface | **consistency (lens / identity-adjacent)** | `A₀(r)` gradient is canonical (`ave-kb/CLAUDE.md` Ax-4 operating-point) |
| §5 | VARDEN scheme → future AVE soliton-in-`A₀(r)` driver | **FLAG, do not build** | numerical-method note; substrate is K4-TLM, not continuum NS |
| §6 | classification + SM-counterfactual + teeth | meta | — |

### Access ledger — READ vs INFERRED (honest; do not fabricate)

| Paper | Access | What I actually have |
|---|---|---|
| **arXiv 1110.3435** — "The trapping and escape of buoyant vortex rings in sharply stratified fluids" (Camassa, Khatri, McLaughlin, Mertens, Monbureau, Nenon, Smith, Viotti, White) | **READ** — full text of the 1-page document (downloaded PDF, `/tmp/camassa_1110.3435.pdf`) | It is a **Gallery-of-Fluid-Motion VIDEO abstract** ("In this fluid dynamics video…"), 1 page. Gives the four named regimes + control-parameter ranges + the entrainment-bubble mechanism **verbatim**. Contains **NO equations and NO explicit dimensionless group** (no Froude/Richardson number written). |
| **IOP Comput. Sci. Discov. 6:014001 (2013)** — VARDEN numerical-method paper | **READ** (abstract + method via WebFetch) | Governing variable-density NS equations, VARDEN (LBNL) approximate-projection + multigrid + 2nd-order upwind + Crank–Nicholson + adaptive Δt, **Hill's spherical vortex** initial condition, and the "critical bifurcation… trapped at density interfaces or escape" phase-diagram framing. |
| **PhysRevFluids 1, 050503 (2016)** — "Liquid Chandeliers by Entrainment" | **INFERRED** — gated (HTTP 403); Semantic Scholar API returned empty | It is the **journal version of the same work** as 1110.3435 (the "chandeliers" regime is named in the 1110.3435 abstract I READ). I work from that video-abstract content + general Camassa–McLaughlin physics; I do **not** quote the PRF text. |
| **Zhi Lin et al.** — subsurface oil-plume trapping in stratification | **INFERRED** — gated (ResearchGate); not fetched | I work from the title + the shared entrainment-trapping mechanism (a subsurface plume, e.g. Deepwater-Horizon-class, trapped at a pycnocline by the same entrainment-buoyancy balance). No verbatim content; flagged throughout. |

**Bottom line on the dimensionless group:** the single most-requested deliverable — *the* closed-form
dimensionless trap/escape threshold — is **NOT present in any source I read**. The READ sources give the
criterion as a **2-parameter empirical phase boundary** in (top-layer thickness `H`, droplet excess
density `Δρ`), explicitly a "critical bifurcation… phase diagram" (IOP). The Richardson/Froude/
entrainment-ratio *form* I reconstruct in §1.5 is **my synthesis from the described physics + standard
Turner entrainment theory**, tagged INFERRED there. I do not present it as quoted.

---

## §1 — Per-paper extraction (the fluid mechanics, with read-vs-inferred tags)

### §1.1 — arXiv 1110.3435 (Camassa, McLaughlin et al.) — READ (1-page Gallery-of-Fluid-Motion video abstract)

**What it is.** A *fluid-dynamics video* extended abstract (1 page). Miscible (dye-in-water) vortex
rings falling in a near-two-layer stratified tank; experiments + variable-density Navier–Stokes (VARDEN)
DNS. **No equations in the document.**

**The setup (verbatim parameters).** Fixed top layer = fresh water (0.998 g/cc) stably stratified above
salt water (1.020 g/cc), transition layer ~1 cm. Two controls swept: **top-layer thickness `H` = 10–70
mm** and **droplet (ring) density = 1.020–1.040 g/cc** (so droplet excess density over the lower layer
`Δρ ∈ [0, 0.020] g/cc`). The ring is **denser than both layers**.

**The surprise + the mechanism (verbatim sense).** "It may initially be surprising that a fluid of
greater density than either of the two layers… can become trapped at the density transition." During
descent a **growing entrainment bubble of light upper-layer fluid forms and travels downward with the
ring** (viscous entrainment). On entering the lower layer the entrainment bubble **feels a buoyant force
→ rebound** at some depth; during rebound **enhanced mixing** equilibrates the conglomerate to local
ambient density → **the ring content traps in the transition layer.**

**The four regimes (the phase diagram, ordered by decreasing `H` and/or increasing `Δρ`):**

1. **"Settling"** (large `H`, small `Δρ`) — ring content **completely trapped** within/on top of the
   transition layer, with possible damped oscillations. *(Complete trap.)*
2. **"Chandeliers"** — ring **destroyed on impact**; fingers form and can break through, but the
   **majority of content stays trapped** in the transition layer. *(Mostly trap; partial breakthrough.)*
3. **"Bouncing"** — ring + bubble **pass below** the transition, then the **bubble rebounds and carries
   the entire content back** to the transition layer, where strong rebound-mixing holds it. *(Trap via
   overshoot+rebound.)*
4. **"Core-fallout"** (small `H`, large `Δρ`) — the **entrainment bubble can no longer carry the entire
   ring content back**; some rebounds but **core material continues downward.** *(Escape — the core is
   lost through the interface.)*

**The load-bearing physical claim:** trap-vs-escape is set by a competition between **accumulated
entrained buoyancy** (which grows with descent distance `H` — more entrainment) and the **core's excess
weight / downward momentum** (which grows with `Δρ`). Core-fallout is precisely the regime where
accumulated buoyancy loses the race to carry the core back up.

### §1.2 — IOP Comput. Sci. Discov. 6:014001 (2013) — READ (abstract + numerical method, via WebFetch)

**Abstract (paraphrased from fetched text):** 3-D DNS of a vortex ring settling in sharply stratified
miscible ambient (near-two-layer), compared with lab experiments; identifies a **"critical bifurcation…
distinguishing whether settling vortex rings become trapped at density interfaces or escape through
them,"** with numerical predictions in qualitative agreement with experimental **phase diagrams**.

**Governing equations (variable-density incompressible Navier–Stokes), verbatim form fetched:**

> `∂ρ/∂t + ∇·(ρu) = 0`   (density continuity)
> `ρ(∂u/∂t + u·∇u) = −∇p + μ∇²u + ρg`   (momentum; `μ` dynamic viscosity, `g` gravity)

**Numerical method (VARDEN, LBNL):** approximate-projection method with a **multigrid** solver enforcing
incompressibility; **conservative 2nd-order upwind** advection of momentum + density; **implicit
Crank–Nicholson** for momentum diffusion; **adaptive time step**. **Initial condition = Hill's spherical
vortex** (an inviscid exact compact-vortex solution), tuned to the measured ring radius + velocity.

**Why this matters for the deliverable:** (i) the trap/escape criterion is explicitly an **empirically-
mapped phase boundary** (a *bifurcation*), not a closed-form single dimensionless number — this is the
honest status of "the dimensionless group"; (ii) the method (compact-vortex IC + projection + adaptive
stiff-gradient handling) is the §5 sim-import flag.

### §1.3 — PhysRevFluids 1, 050503 (2016), "Liquid Chandeliers by Entrainment" — INFERRED (gated; journal version of the same work as §1.1)

**Access:** HTTP 403 (paywalled); Semantic Scholar API returned no abstract. I did **not** read it.
**What I rely on instead:** the term "chandeliers" is defined **verbatim in the 1110.3435 video abstract
I READ** (regime 2 above) — fingering breakthrough with majority-trapping. The PRF paper is the
peer-reviewed write-up of the same UNC Joint-Fluids program. I therefore treat the chandeliers physics as
**covered by §1.1's READ content**, and make **no independent quantitative claim** sourced to PRF. Any PRF
specifics (exact entrainment coefficient, exact phase-boundary fit) are **NOT in hand** — flagged.

### §1.4 — Zhi Lin et al., subsurface oil-plume trapping in stratification — INFERRED (gated; from title + shared Camassa–McLaughlin mechanism)

**Access:** ResearchGate-gated; not fetched. I did **not** read it.
**What I infer (clearly tagged):** a buoyant **oil plume** rising/settling through a stratified water
column (a pycnocline) **traps at the density transition** by the *same* entrainment-buoyancy mechanism —
entrainment of ambient water changes the plume's effective buoyancy until it equilibrates at a
neutral-density horizon (the canonical "subsurface plume" / intrusion, e.g. Deepwater-Horizon-class). This
is the **same trap mechanism with reversed sign** (buoyant plume rising vs dense ring falling) — useful
only as confirmation that the entrainment-trapping mechanism is **direction-agnostic** (it traps at a
neutral horizon regardless of which way the element is moving). **No numbers; lens-confirmation only.**

### §1.5 — The synthesized trap-vs-escape physics + the (absence of a closed) dimensionless group

**Honest status first:** none of the READ sources writes a closed-form dimensionless threshold. The
criterion is a **2-D empirical phase boundary** in (`H`, `Δρ`). What follows is **my reconstruction**
(tagged **INFERRED — synthesis from the described physics + standard Turner entrainment theory**), offered
because the deliverable asks for the dimensionless-group *form*, not because it is quoted anywhere.

**The competition, in standard buoyant-element variables.** Classic entrainment (Turner 1957/1986;
Morton–Taylor–Turner plume theory) models a buoyant element growing by entraining ambient fluid at a rate
proportional to its surface area × velocity: `dr/dt ≈ α_E · U` with entrainment constant `α_E ~ 0.2–0.25`.
Over a descent of depth `H` the entrained light-fluid volume grows ~ `(α_E H)`-fashion, building a buoyant
reserve `B_entr ∝ Δρ_strat · V_bubble(H)` (where `Δρ_strat = ρ_lower − ρ_upper` is the layer jump that the
light bubble is now buoyant against). The core's excess weight is `W_core ∝ Δρ_core · V_core` (`Δρ_core` =
ring density − lower-layer density). Two dimensionless ratios govern the bifurcation:

- **Entrainment / weight ratio** (the trap reserve): `Π_trap ≡ B_entr / W_core ∝ (Δρ_strat · V_bubble(H)) / (Δρ_core · V_core)`. `Π_trap > 1` → the bubble can rebound the core → **trap**; `Π_trap < 1` → **core-fallout**.
- **Froude / Richardson timing** (rebound vs separation): a Froude number `Fr ≡ U / √(g' a)` (or its inverse-square Richardson `Ri = 1/Fr²`), with `g' = g·Δρ/ρ` the reduced gravity and `a` the ring scale, sets whether the buoyant rebound out-paces the core's inertial penetration. High `Fr` (inertia wins) → overshoot then **bouncing** or, if too high, **core-fallout**; low `Fr` (buoyancy wins promptly) → **settling**.

**The four regimes as a path in `(Π_trap, Fr)`:** settling (`Π_trap ≫ 1`, low `Fr`) → chandeliers
(`Π_trap > 1`, moderate `Fr`, impact-fingering) → bouncing (`Π_trap ≳ 1`, high `Fr`, overshoot+rebound) →
core-fallout (`Π_trap < 1`). The single most load-bearing variable is **`Π_trap` — the accumulated
entrained buoyant reserve relative to the core's excess weight.** That is the variable Mapping A maps.

> **INFERRED-tag, restated for the auditor:** `Π_trap`, `Fr`, `Ri`, `α_E ≈ 0.25` and the "path in
> `(Π_trap, Fr)`" are **standard stratified-entrainment theory applied by me**, not quoted from the
> Camassa–McLaughlin papers (which present the boundary as an empirical phase diagram). The *direction* of
> the dependences (trap ↑ with `H`, escape ↑ with `Δρ`) **is** verbatim from §1.1.

---

## §2 — Mapping A: trap-vs-escape → genesis confinement (Fork A) [THE SPINE]

### §2.1 — The Fork-A problem restated (the double-sided bracket)

Genesis (`pair-production-axiom-derivation.md`, 7-step chain) drives a seed at a K4 A–B node pair through
saturation until `A²→1` shorts the bond (`Z_core→0`, `Γ=−1` wall forms at the nodes), the blocked
longitudinal KE is forced into the transverse curl channel, and the `(2,3)` winding closes into a confined
standing wave at `ω_C` — the electron. **Nucleation needs three simultaneous local conditions**
(`pair-production-axiom-derivation.md:83-85`): **C1** amplitude (`A²≥1` at both nodes), **C2** frequency
(`Ω_node(A²_local) ≈ ω_drive`, the Duffing-shifted resonance locks the drive), **C3** phase (the field
phase lets the `(2,3)` close on the `(V_inc,V_ref)` trajectory — *"without the right phase relation… the
blocked KE cannot resolve into a topologically coherent standing wave (dissipates instead)"*).

**Fork A is the amplitude-calibration crux** (`_orchestration/2026-06-06_genesis-next-steps-scope.md:84`):
*"rest-energy-sized pair (`A²≈0.23`, no wall) vs short-its-own-bond-sized (`A²→1`, pumps). ~4× apart.
This tension is the genesis blocker."* The live empirical finding (same doc, C2 `:63`) is a **double-sided
bracket** with **no stable window between**:

- **Low end (1×, `A²_μ≈0.23`, `S_μ≈0.88`, `Γ≈−0.03`):** the wall **does not engage** — a matched bulk, no
  reflection. The seed **dissolves → MODE III**. *(This is the "falls through, no confinement" end.)*
- **High end (4×, `Γ_min=−0.994`):** the wall **forms** but the seed **parametric-pumps** (energy →
  `10⁴–10⁷×`). *(Runaway — not a bound particle either.)*
- *"There is no amplitude in [1×,4×] where the wall both forms AND stays bounded."*

So Fork A is not "too weak vs just right" — it is **"too weak (dissolve) vs too strong (pump)", with the
bound trapped state nowhere in the swept window.** Holding this exact shape is what the fluid lens
illuminates.

### §2.2 — The structural isomorphism (load-bearing variables)

| Fluid (Camassa–McLaughlin) | AVE genesis (Fork A) | Status of the bridge |
|---|---|---|
| Dense vortex ring falling through stratification | Driven seed at a K4 A–B node pair under the genesis ramp | the moving "object" |
| **Trap** (settling / chandeliers / bouncing — content held at the interface) | **Confinement** — `Γ=−1` wall forms, `(2,3)` winding closes, stable standing wave at `ω_C` = the electron | **trap ⇒ confinement** |
| **Escape — core-fallout** (entrainment can't carry the core back; core falls through) | **MODE-III dissolution** — wall does not engage / KE *"dissipates instead"* (C3 fail), seed lost | **escape ⇒ MODE III** |
| **Entrainment bubble** of light fluid the ring drags down, growing with descent | The **self-dug saturated pocket** the seed builds around itself as `A²_μ→1` at its bounding nodes — the *self-Meissner cage forming* (`rotor-synthesis §3`: "strong enough to expel itself") | accumulation of a confining envelope |
| **Buoyant rebound** of the entrainment bubble at the transition | The **`Γ=−1` reflection** of the blocked KE back into the bond (the "moving reflective boundary" that converts collapse→confinement, `historical-precedents.md:28` verdict-II) | reflection/return of energy |
| **Rebound-mixing → equilibrate to local ambient density → lock** (what makes the trap *stable*) | The **C3-gated resolution** of the blocked KE into the coherent `(2,3)` standing wave (the "equilibrated", *bounded* end-state) | the lock that makes confinement bounded |
| Accumulated buoyant reserve vs core excess weight, `Π_trap` (§1.5) | **Accumulated self-saturation** (toward `A²_μ=1`, weaving the wall) vs the **amplitude that leaks/detunes away** | the central competition |
| Control: top-layer thickness `H` (more descent → more entrainment) | Control: **drive ring-up duration / power** (more autoresonant pumping → more accumulated `A²_μ`) | the "more confinement reserve" knob |
| Control: droplet excess density `Δρ_core` (more downward pull → escape) | Control: **the rest-energy calibration** (the `m_ec²`-sized impose sits at `A²≈0.23`; the "weight" that must be overcome to reach `A²=1`) | the "harder to trap" knob |

**The load-bearing variable on both sides is the same shape:** an **accumulated confining reserve** (entrained
buoyancy / self-saturation) racing against a **loss** (core penetration / amplitude leak), with a **lock step**
(mixing-equilibration / C3-resolution) that decides whether a formed wall yields a *bounded* trapped object.

### §2.3 — Where the analogy BREAKS (substrate-native-check + ave-discrimination-check)

Stated plainly, because the lens is only as honest as its failure modes:

1. **The confinement force is NOT buoyancy.** Fluid trapping is gravity acting on a density difference. AVE
   confinement is an **impedance** effect: Axiom-4 saturation drives `μ_eff,ε_eff→0` *asymmetrically* →
   `Z→0` → `Γ=−1` perfect mirror (`01_vacuum_circuit_analysis.tex:432`, `:438`;
   `k4_cosserat_coupling.py` asymmetric-Meissner). No `g`, no `Δρ`. The fluid `Π_trap`, `Fr`, `Ri` are
   **not substrate quantities** — they are the *grammar* of "reserve vs loss", re-instantiated, not imported.
2. **Coordinate mismatch (phase-space-coordinate-check / A46).** The vortex ring, entrainment bubble, and
   rebound are **real-space** velocity-field events. The AVE `(2,3)` lives in **phase space** — a
   `(V_inc,V_ref)` loop on the Clifford torus (`pair-production-axiom-derivation.md:85`; Kelvin real-space
   vs AVE phase-space, `historical-precedents.md:30`). The "trap" is the *winding closing in phase space*,
   not an object settling in real space. **Any test of this mapping must measure winding-closure in
   `(V_inc,V_ref)` coordinates**, never a real-space lattice-Cartesian "did the blob stay put" metric.
3. **The decisive disanalogy — the pump end has no fluid counterpart.** The fluid trap is **stable because
   it is DISSIPATIVE**: viscous mixing during rebound is an irreversible, entropy-producing settle to
   neutral buoyancy. The fluid has **one** failure mode (core-fallout — under-reserve). The AVE bracket has
   **two**: under-amplitude **dissolves** (matches core-fallout) *and* over-amplitude **parametric-pumps**
   (`10⁴–10⁷×`) — and **the pump has no fluid analog**, precisely because the genesis ramp as currently
   modelled is **reactive/lossless** (autoresonant positive feedback), with no equilibrating dissipation in
   the swept window. *This break is the most useful thing the lens tells us* (it points straight at the
   missing equilibration channel — §2.4).
4. **Generic-bistability caveat (ave-discrimination-check).** "A system with a trap/escape threshold" is
   **generic** — SM, classical fluids, any bistable medium has one. The lens, by itself, is **not
   AVE-distinct**. Only a threshold whose **number** traces to substrate primitives (`A²=1`, `α`, `ℓ_node`)
   would be (see §6).

### §2.4 — Substrate-native Fork-A confinement criterion (HYPOTHESIS, not import)

The fluid trap is really **three** things working together (§1.1): (i) **enough** accumulated buoyant
reserve to rebound at all; (ii) the rebound is **fast enough** to catch the core before it separates; (iii)
**mixing equilibrates** the conglomerate to neutral buoyancy so the trap is *bounded and stable* rather than
oscillatory/runaway. Re-grounded in the substrate, this proposes a **three-rate balance** for Fork A —
substrate-native, derived from the engine's own processes, NOT from `Π_trap`/`Fr`:

> **HYPOTHESIS (Fork-A trapping criterion, substrate-native).** A driven seed **confines** (→ electron)
> iff, at the bounding nodes:
>
> 1. **Accumulation beats leak.** The autoresonant ring-up drives `A²_μ` to the self-Meissner threshold
>    (`A²_μ→1`, weaving `Γ=−1`) **before** the amplitude leaks/detunes back below it. Define
>    `τ_acc` = ring-up time to `A²_μ=1`; `τ_leak` = amplitude-drain time (intrinsic floor `~Q/ω_C = 1/(α ω_C)`,
>    shorter once a detuning channel opens as `Ω_node(A²)` slides off `ω_drive`). **Condition: `τ_acc < τ_leak`.**
>    *(Failure → the 1× MODE-III "dissolve" end = core-fallout.)*
> 2. **An equilibration channel beats the pump.** Once the wall forms, a **C3-gated, irreversible commit
>    step** must convert the blocked KE into the bounded `(2,3)` standing wave **faster** than the
>    autoresonant feedback amplifies it. Define `τ_eq` = C3-resolution time; `τ_pump` = parametric e-folding
>    time. **Condition: `τ_eq < τ_pump`.** *(Failure → the 4× "pump" end — the regime with no fluid analog,
>    because the fluid's viscous mixing always supplies `τ_eq < τ_pump`.)*
>
> **Trap (confinement) ⇔ `τ_acc < τ_leak` AND `τ_eq < τ_pump`.** Either inequality failing reproduces one
> arm of the observed double-sided bracket.

**What the lens contributes that the prior framing did not:** Fork A was posed as a **1-parameter**
amplitude tension (`A²≈0.23` vs `A²→1`, ~4× apart). The entrainment lens says the bracket is **2-failure-mode**
and that the high (pump) arm is failing for a *different reason* than the low (dissolve) arm — it is missing
the **equilibration/dissipation step** that, in the fluid, is supplied by mixing. This **links Fork A to Fork
D (the dropped C3 phase-gate)** through a concrete physical reading: **C3 is the substrate's
mixing-equilibration** — the irreversible "settle to neutral buoyancy" that locks a formed wall into a
*bounded* particle instead of a reactive runaway. The genesis scope already proposes the cheap test (add the
C3 gate + re-run, `…genesis-next-steps-scope.md:68,89`); **the fluid lens does not invent a new methodology —
it predicts the OUTCOME of that already-scoped test**: a C3-gated commit step should convert the 4× pump into
a bounded trap (or, if it does not, the equilibration must be genuinely *dissipative* — see §7's question to
Grant).

**Honest ceiling.** This is a **structural hypothesis** (a three-rate balance + a Fork-A↔Fork-D link), not a
number. It **does not resolve** the genesis blocker — *"None resolve the genesis blocker, which remains Fork
A amplitude-gating"* (`rotor-synthesis:616`). Its value is (a) reframing the pump arm as a missing-channel
problem, (b) supplying a falsifiable engine prediction for the already-scoped C3 test, (c) surfacing the
dissipative-vs-reactive question (§7). Class: **consistency-class lens with one structural emergence
candidate** (the criterion), assessed in §6.

---

## §3 — Mapping B: entrainment-buoyancy law → dark-wake / inertia

**The corpus target.** AVE identifies inertia as a **reactive, inductive (Lenz) back-EMF**: `clm-jwyy6l`
(`vol2/claim-quality.md:666-674`) — *"mass is identified with stored inductive energy required to maintain
the topological integrity of the closed flux loop. Newton's `F = ma` is then a macroscopic phenomenological
consequence of Lenz's law on a confined electromagnetic phase loop,"* with `E_mass = ½ L_eff |A|²` and
back-EMF `V = −L di/dt` the resistance to acceleration. It is explicitly a *"category (i) ontological
reinterpretation, not a new numerical prediction"* (confidence 0.3; leaves
`dark-wake-bemf-foc-synthesis.md`, `newtonian-inertia-as-lenz.md`).

> **verify-before-cite flag.** The brief paraphrased `:670` as *"can't be entrained without motion."* That
> phrase is **not** at `:670`; the verbatim claim is the Lenz/back-EMF text above. I use the brief's phrasing
> as an *intuition gloss* only, not as a corpus quote.

**Is the entrainment RATE a candidate inertia model? Yes — but only the REACTIVE branch, and the
Camassa–McLaughlin entrainment is the WRONG (dissipative) branch.** This is the load-bearing discrimination:

- **Inviscid ADDED-MASS (virtual mass) is the correct fluid analog of AVE inertia.** A body accelerating
  through a fluid must also accelerate the fluid it displaces/drags; the reaction is an **extra,
  velocity-history-independent, lossless** inertia — the classic added-mass `m_add = C_M ρ V`. This is
  **reactive** (potential-flow, no entropy), and it is the *exact* structure of `clm-jwyy6l`: the soliton
  accelerating must accelerate its dragged **reactive dark-wake** (the lattice's inductive response) too →
  back-EMF → inertial mass. `m_add ↔ L_eff`; the entrained/displaced reactive field IS the stored `½L|A|²`.
  **This is a genuinely good lens** — added-mass is the fluid word for "inertia = dragging your own reactive
  field."
- **The Camassa–McLaughlin entrainment is VISCOUS — dissipative — so it is NOT the inertia branch.** Their
  abstract says *"viscous entrainment which alters the effective buoyancy."* Viscous entrainment is
  irreversible mass-accumulation; it changes *buoyancy* (a real-power / settling effect), and it is exactly
  the **confinement-accumulation** of Mapping A (§2), **not** reactive inertia. Mapping the *viscous*
  entrainment rate onto inertia would import the wrong polarity (a lossy drag onto a lossless reactance).

**Net for Mapping B.** The entrainment-rate framing **is** a candidate model for inertial-mass accumulation
— provided one takes the **reactive added-mass** limit (the field the soliton must drag-accelerate, `↔ L_eff`),
and explicitly **separates it from the dissipative viscous entrainment** that the Camassa–McLaughlin papers
actually study (which belongs to confinement, §2, and to decoherence/real-power loss, companion §3). So the
two fluid effects bifurcate cleanly onto two AVE targets:

| Fluid effect | Character | AVE target |
|---|---|---|
| **Inviscid added-mass** (`m_add = C_M ρ V`) | reactive, lossless | **inertia** = back-EMF `½L|A|²` (`clm-jwyy6l`) |
| **Viscous entrainment** (Camassa–McLaughlin bubble) | dissipative, accumulating | **confinement** (Fork A, §2) + real-power loss (decoherence) |

**Discrimination + classification.** The added-mass lens adds **intuition, not a number**; it inherits
`clm-jwyy6l`'s own ceiling (confidence 0.3, *"not a new numerical prediction"*). SM-counterfactual: added-mass
is textbook classical/quantum field-reaction physics; "inertia = field reaction" is **not AVE-distinct**
unless the *prefactor* (`C_M`, or equivalently `L_eff` for the `(2,3)` geometry) is **derived from substrate
topology** and shown to differ from a generic field-dressed mass. Class: **consistency-class lens** (the clean
reactive/dissipative bifurcation is the contribution).

---

## §4 — Mapping C: stratification → bulk-strain gradient `A₀(r)` / yield surface

**The corpus target.** Each LC node carries a saturation-amplitude **operating-point state `A₀`** along the
Axiom-4 kernel (`ave-kb/CLAUDE.md` INVARIANT-S2, "Operating-point state and small-signal modulation"). A
spatial profile `A₀(r)` modulates the local effective medium: `ε_eff = ε₀ S(A₀)`, `μ_eff = μ₀ S(A₀)`,
`C_eff = C₀/S(A₀)` — the same **varactor-bias** mechanism that produces refractive-index gradients at all
scales. **A `A₀(r)` profile is therefore a graded-impedance / graded-refractive-index background.**

**The mapping.**

| Fluid stratification | AVE operating-point background |
|---|---|
| Density profile `ρ(z)` (two layers) | Operating-point field `A₀(r)` (graded saturation = two operating points) |
| Sharp density transition (pycnocline, ~1 cm) | **Yield surface** — where `A₀(r)` crosses a regime boundary (`r₁ = √(2α) ≈ 0.121`, Regime I→II, `19_phase_transition_turbulence.tex:19,28`; or `A²→1`, the `Γ=−1` boundary) |
| Buoyancy frequency `N² = −(g/ρ) dρ/dz` (only the *gradient* is dynamically active; uniform `ρ` does nothing) | `∇A₀` — **only the gradient is physically observable** (operating-point state is *gauge-relative*; "only spatial gradients of `A` are physically observable, not absolute per-node values", `ave-kb/CLAUDE.md` INVARIANT-S2) |
| Ring descending from light → dense layer through the transition | Seed driven from **sub-yield (Regime I)** through the yield surface toward **saturated (`A²=1`, `Γ=−1`)** |
| The transition layer where trapping happens | The **yield-surface region** where the wall forms and the `(2,3)` can lock |

**The genuinely suggestive structural parallel (flag, not a claim).** Both systems share the property that
**only the gradient is dynamically active** — fluid stratification acts through `N² ∝ dρ/dz` (a uniform
density column is inert), and the AVE operating point acts through `∇A₀` (absolute per-node `A₀` is
gauge-relative; only gradients are observable). This is a real structural match between *stratification* and
*the operating-point field*, beyond the loose "layers ↔ regions" analogy. It is the cleanest part of Mapping C.

**Symmetric vs asymmetric loading — which gradient reflects (substrate-native-check).** Not every `A₀(r)`
gradient is a trapping yield surface. Per `ave-kb/CLAUDE.md` INVARIANT-S2: a **symmetric** both-sector scaling
(`S_ε = S_μ`) keeps `Z = Z₀` **invariant → reflectionless** (the gravity-class, transparent gradient — the
ring would merely *refract*). Only an **asymmetric** load (`S_μ→0`, `S_ε` finite — the particle/Meissner
case, `01_vacuum_circuit_analysis.tex:432,438`) gives `Z→0`, `Γ=−1` — a **reflecting** yield surface. **The
trap happens only at the asymmetric (Meissner) yield surface**, consistent with §2's confinement mechanism.
So Mapping C sharpens §2: the "sharp density transition" is specifically an **asymmetric-saturation yield
surface**, not a generic refractive step.

**Classification.** Consistency-class, **identity-adjacent** — it re-describes the canonical `A₀(r)`
operating-point in stratification vocabulary and adds **no new primitive**; the `∇A₀`-only-observable parallel
is the one piece of new intuition. Honest ceiling: same echo-not-chord as the rest of this doc.

---

## §5 — Mapping D: numerical method (VARDEN) → possible future sim import (FLAG, don't build)

*(filling)*

---

## §6 — Classification: consistency-vs-emergence + SM-counterfactual + the one place with teeth

*(filling)*

---

## §7 — Honest ledger, open items, KB-placement flag, and Grant/auditor surface

*(filling)*

---

## Cross-references (canonical leaves + corpus + papers — verify-before-cite checked)

*(filling)*
