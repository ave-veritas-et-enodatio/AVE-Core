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

*(filling)*

### §2.1 — The Fork-A problem restated (the double-sided bracket)

*(filling)*

### §2.2 — The structural isomorphism (load-bearing variables)

*(filling)*

### §2.3 — Where the analogy BREAKS (substrate-native-check + ave-discrimination-check)

*(filling)*

### §2.4 — Substrate-native Fork-A confinement criterion (HYPOTHESIS, not import)

*(filling)*

---

## §3 — Mapping B: entrainment-buoyancy law → dark-wake / inertia

*(filling)*

---

## §4 — Mapping C: stratification → bulk-strain gradient `A₀(r)` / yield surface

*(filling)*

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
