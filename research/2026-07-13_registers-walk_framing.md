# FRAMING NOTE — the registers walk: T_ij, the depletion primitive, the transducer, and the cascade filter (2026-07-13)

**★ FRAMING, NOT DERIVATION — nothing canonized; every claim awaits its own gate.** This note captures a core-session planning walk verbatim-faithful. No §-claim below upgrades any observable or lands any result; the cited PRs / leaves / research walks are *pointers* to where the load-bearing work either already lives or is owed. Grant's two ontologies (the transducer, §3; the cascade filter, §5) are recorded as **ruling-grade walk inputs to the X44b / F6 charters**, not as canon.

**Date:** 2026-07-13 · **Status:** Grant-walked 2026-07-13, verbatim-faithful. Q1 / Q2 **answered in-walk** (§3); Q3 **refined by Grant to the cascade-filter ontology** (§5), locus-ruling pending the vol9 circuit-mapping investigation (in flight, workflow `ww0giq5he`); Q4 **pending Grant** (ρ_latent go + two-tier build order, §4). Nothing canonized. Companion to the R-B fossil-walk note (`research/2026-07-10_rb-fossil-walk_framing.md`), the impedance-register note (`research/2026-07-10_impedance-register-walks_framing.md`), and the rulings docket (`_orchestration/2026-07-10_rulings-docket.md`).

**SECTOR / REGIME / PHASE-STATE (the frame this note reasons in).** The T_ij register (§1–§2) is the **cold, static, bound-resonator** stress object of the K4 / Cosserat medium — the materialized flux the engine has never written, not a driven mode. The depletion primitive (§2b, §4) is a **driven off-line↔on-line boundary** transfer into the T2 bath. §3 (transducer) is the **envelope equilibrium interface** where cycle-averaged transverse-EM Maxwell stress balances static A1 lattice strain. §5 (cascade) is the **whole hierarchy** from electron (terminal pole) to the universe envelope (top port). §6 (SYM-gravity) is the **A1 even-strain / matched-impedance** loading regime. All substrate claims below carry the quarantine header; none is an observable upgrade.

---

## §1 THE PLAN OF RECORD — registers-first

**Grant ratified the plan: registers first.** The build order for the engine's open frontier is **walk the two registers (T_ij + the depletion primitive) → X44b (the gravity-source ladder) → F6 (the dark-energy depletion handle).** The rationale is that both registers bottom out in the *same missing shape* — the corpus derives forms and forces but has never materialized the *flux objects* (§2, §7) — so a single materialization build discharges the shared debt before the sector-specific charters (X44b, F6) can fire.

This ordering was set against the **2026-07-11 engine audit** and the **nine-PR engine-refresh wave** (`_orchestration/2026-07-11_engine-refresh-handoff.md`; `research/2026-07-11_engine-refresh-batch_result.md`). The audit's engine-gap ranking, as it bears on this walk:

- **T_ij — the stress-materialization gap** (Register 1, §2d): the engine goes strain → energy → force and skips σ_ij entirely by design (`cosserat_field_3d.py:14`). This is the register the walk builds.
- **the F6 depletion primitive** — the DC→AC chord object, **HARD-BLOCKED** and a multi-arc build, ranked RANK-3 on the board (`_orchestration/index.md:187`; note #86 two-way back-reaction already LANDED 2026-06-29 and is *not* the make-or-break). Register 2 (§2b) is the autopsy that scopes it.
- **the n_eff overload** — the KB symbol `n_eff` is silently reconciled to two distinct quantities in the FDTD path; promoted to its own gap line by the audit (`_orchestration/2026-07-11_engine-refresh-handoff.md:135-138`). This is X44b's chain (§6 open ends).
- **R10 remanence** — the fixed-N localization / remanence-before-node-mint charter (`_orchestration/index.md:8-15`), the branch this worktree forked from; independent of the registers but the surrounding board state.
- **boundary infrastructure** — PML-cell exclusion, closed-box re-runs, density-peak sampling (the empirical-driver discipline the genesis and register drivers both need).

The walk is the core session getting the two registers **walk-ready** (materials assembled, the two genuinely-new build items named, adjudicators identified) — not executing the drivers, which is a satellite's job.

## §2 THE GROUNDING VERDICTS (from the walk card)

These are the four lane-verified verdicts the walk stands on. All receipts were lane-verified and the heaviest independently spot-checked; re-verified at this HEAD for the cites quoted here.

### (a) The diode / rectifier class is DEAD for the depletion primitive

Four independent deaths, all standing:

- **The Ax4 kernel provably cannot rectify.** `S(A) = √(1−A²)` is instantaneous, **even in A**, memoryless — identical second-order response to symmetric and asymmetric drive. The one RUN test (rr-radiation-L rectification) is a **NULL** (`research/2026-06-08_rrad-l-rectification_result.md:66-78`).
- **Any true rectifying loop is Level-2 memristive = dissipative.** "Any rectification / latching / path-memory requires Level-2 dynamics, which the smooth `√(1−A²)` kernel does not implement" (`manuscript/ave-kb/common/substrate-hysteresis-index.md:24-25,96`). So "lossless + rectifier" is a contradiction in the corpus's own loop taxonomy — the same graveyard as the retired STZ / plastic dissipation leaks.
- **The diode threshold is FREE, not forced.** P4: "V_f is FREE — no canonical scale forces a forward-voltage dead zone"; kernel analytic at origin, dispersion gapless (`research/2026-07-08_p4-forward-voltage-threshold_RESULT.md:19`).
- **Chirality-ratchet-as-arrow is REFUTED — do not reopen.** "Chirality is a PARITY selector, not the arrow … 'chirality-ratchet as arrow' is REFUTED" — the genesis freeze is mirror-symmetric (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:89-100,127`). An ideal-diode framing risks re-opening this retracted slot.

### (b) What IS licensed — lossless Ax3-legal one-wayness (three instances)

- **Entropic mode-count transfer (arrow-of-time class).** "Energy-conserving one-way TRANSFER into the huge T2 reservoir (dS>0), NOT a friction loss, so it is Ax3-COMPLIANT" (`…/dark-energy-latent-heat-definition.md:84-87`); one-way-street radiation, reconvergence ≈ 0 (`manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/arrow-of-time.md:16`). Irreversibility from **reservoir mode-count**, not nonlinearity.
- **X40-class discrete topological minting.** Trapped `f_E = 1/10` is the conserved cycle-space mesh current; flux linkage Λ banks WHOLE (drift 2.2e-16), minted ONLY at the discrete ring-completion event (`research/2026-07-10_x40-ring-closure-transient_result.md:18-20,161,306-313`). One-way **at the click**, exactly conserving — but it *partitions* at nucleation, it does not *deplete* a reservoir.
- **The v5 skew-Hermitian circulator.** An **orthogonal field-space rotation — NOT a trilinear potential**: the 3-port skew-Hermitian circulator conserves and transfers 100%, one-way, "magnitude imposed" (`src/ave/core/cross_sector_coupling.py:137-141`, PR #321).

**v4's death names the boundary.** The continuous trilinear coupling `H = κ̃∫gV[w·∇×ω]` is **linear in each of V, w, ω** ⇒ an **INDEFINITE Hamiltonian, unbounded below** ⇒ the discrete dynamics PUMP / DETONATE (`src/ave/core/crystal_graft_v4.py:158-172`, verbatim). The licensed instances in (b) are exactly the ones that avoid the indefinite trilinear form: an orthogonal rotation (bounded), an event-gated mint (bounded), a reservoir transfer (entropic, not potential-driven).

### (c) Brace corrections — carry these into the T_ij build

- **The brace is a FORCE, not a pressure.** As derived, `B_a = −dU_rot/dr = +L_w²/(m_eff r³)` is energy/length [N], not energy/volume [Pa] (`research/2026-06-30_electron-portmap-derivation_result.md:250-254`; `sign(dF/dr) = sign(3−p)` at `:364-373`). To feed a Komar `+3∫p` integrand it is **one integration short** — the missing object is `T_rr(r)`. `T_rr` is unbuilt.
- **Research-doc-only — pointer correction.** The `sign(3−p)` brace lives ONLY in `research/2026-06-30_electron-portmap-derivation_result.md`, **NOT** in `clm-hvb7q3`. That leaf (`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:47-49,57-66`) is a *different* binder: the Laplace hoop `Γ²/R³` vs surface-tension `σ/R` model, no `sign(3−p)` anywhere. Never canonized to a leaf.
- **The one force-balance sim is INCONCLUSIVE.** The bind-sim did not dynamically realize the brace: `r⁻³` not reproduced, `|L_w|` drifts 16–17% under lossless evolution (`research/2026-06-30_electron-bind-sim_result.md:17,110-121,147`). The `L_w = const` premise the brace rests on is not satisfied.
- **`clm-jwyy6l` is at solidity 0.30, do-not-build-on** (`manuscript/ave-kb/vol2/claim-quality.md:717`): the Lenz *mechanism* survives, but rest-mass *store* ownership is A1 — inductance-L is a TKI translation-image, not sector ownership.

### (d) The T_ij minimal build — assembly, 2 new items + 1 gate

- **Constitutive contraction CARRYING the asymmetric couple-stress.** `σ_ij = λδ_ij ε_kk + 2με_(ij) + couple-stress(κ)` — all inputs live. It **must carry the antisymmetric `σ^A`** (the couple-stress source that drives microrotation — the chiral/spin channel; `manuscript/ave-kb/common/trampoline-framework.md:47,87,356`). A Cauchy-symmetric-only σ welds the swivels shut — a disabled-DOF stencil bug, not a physics simplification (structural-null stencil lens).
- **Spatial momentum-flux `T^ij`.** Today only the single scalar `T^0x` exists: `field_momentum_x = −∫(∂_tV)(∂_xV)/c²` (V-sector, x-axis, interior-only; `src/ave/core/annihilation_engine.py:173-181`).
- **The reconciliation gate.** `div σ` on the **native K4 tetrahedral stencil** must equal the existing autodiff `−∂E/∂u` to machine precision — the only certificate that hand-assembled σ is not a Cartesian-stencil leak. The engine deliberately carries no hand-derived stress today: "the energy gradient is computed by jax.grad — no hand-derived stress tensors" (`src/ave/topological/cosserat_field_3d.py:14`); the load-bearing native operator is `_tetrahedral_gradient` (`:177`).
- **`τ^far_zx` is observer-only — never engine-carried.** The far-field Maxwell row exists in code only as observer proxies; the one dynamics hook `tau_zx_arm` is **declared-but-unwired** — no stepper consumes it (`src/ave/core/unified_genesis_engine.py:975,993,995`). The walk must not treat `τ^far_zx` as engine-carried.

### (e) ★ ONE BUILD SERVES BOTH — the unbuilt bridge

The general `σ_ij` register (d) manufactures the electron's `T_rr` as a special case. That `T_rr` is precisely the object missing from (c) — and it is the **unbuilt bridge** between the two disconnected virials:

- the **electron LC virial** (`E_elec = E_mag = ½m_e c²`; the two reactive-store halves sum to rest mass; `research/2026-06-30_electron-portmap-derivation_result.md:489-495`), and
- the **gravity-sector Komar source** (all `Komar` / redshift-weighted `T₀₀` hits are gravity-side; `src/ave/core/categorization.py:155-168`; `research/2026-07-11_nordtvedt-eta_result.md:208,278`).

There are zero electron-side `+3∫p` / Tolman hits today. Brace → `+3∫p` needs `T_rr(r)` first; building Register 1 manufactures it. **One build discharges both registers' shared materialization debt.**

## §3 ★ GRANT'S TRANSDUCER ONTOLOGY (verbatim-faithful)

> **Grant, verbatim:** "the envelope is the transducer between transverse EM stress and lattice mechanical stress; all mechanical stress derives from, and returns to, the physical lattice."

**Elaboration, as walked.** The **envelope** is the surface where the winding's **cycle-averaged Maxwell stress** balances the **static lattice strain**. *Wording rail (binding):* the cycle-averaging is a **Jensen magnitude** — `⟨S⟩ < S(⟨A⟩)` gives a cycle-averaged deficit `δ = 1 − ⟨S⟩` (`manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md:28,51`) — and its **direction is set by external geometry, not by the kernel.** Never say "the kernel rectifies": the kernel is even-in-A and cannot (§2a). The transducer produces a *magnitude*; geometry orients it.

This makes matter's `T_ij` **two coupled halves at the envelope interface**:

- **wave-side** — the winding's cycle-averaged transverse-EM Maxwell stress, **including the angular flux** (the couple-stress / spin channel), and
- **lattice-side** — the full Cosserat `σ` (the two constitutive halves: microrotation ω → μ → L, strain → ε → C; `manuscript/ave-kb/common/trampoline-framework.md:356`).

The **envelope is the equilibrium interface** between them — TKI made local. All mechanical stress derives from and returns to the physical lattice; the wave-side is the reactive store, not an independent source.

**Q1 ANSWERED — carry the twist.** The angular handover at the envelope **IS spin**: it lives in the couple-stress channel (the antisymmetric `σ^A`; `trampoline-framework.md:87`). A **symmetric-only `σ` deletes spin from the stress ledger.** So the T_ij register must be the full Cosserat asymmetric object, not a symmetric reduction — the plumber's answer to §2(d)'s "does the register carry the twist."

**Q2 ANSWERED — the brace is the envelope's own ⟨Maxwell stress⟩.** The brace is the **cycle-averaged Maxwell stress of the (2,3) winding evaluated at its own envelope.** The general register build (§2d) manufactures `T_rr` as that special case **AND** is the instrument that retries the inconclusive bind-sim (§2c): the brace is not a separately-postulated force, it is what the transducer reads at equilibrium.

**★ Derivable consequence — a SOURCE-side theorem-target for X44b.** Bound transverse content carries the **radiation equation of state `p = u/3`**. A Komar / Tolman source weights `(ρ + 3p)`, so pure wave content contributes `(ρ + 3·u/3) = ρ + u` — a **factor-2 doubling for the wave part.** This is the *same* factor-2 as the derived light-deflection doubling (`n_⊥ = 1 + (2/7)χ_vol → 4GM/bc²`; the bridge `z = (n_temporal − 1)/2`, a propagating signal picks up 2× the local clock; `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:26,28`). **This is a theorem-target, not a result** — the claim owed is that the envelope's wave-side `T_rr`, fed through the Komar source, reproduces the deflection doubling from the source side. It slots directly onto X44b's `η ≈ −1 → 0` ladder (the Nordtvedt / Komar-source reconciliation, `research/2026-07-12_x44-komar-source_result.md`; `research/2026-07-11_nordtvedt-eta_result.md:208,278`).

## §4 Q3 / Q4 — THE FULL PICTURE (as delivered for Grant's ruling)

The depletion primitive, laid out as a **4-element transfer map**:

| element | what it is |
|---|---|
| **source** | `ρ_latent` — the **static sector's held store** (the latent heat banked at genesis freeze) |
| **destination** | the **T2 bath** — the huge mode-count reservoir |
| **transducer / locus** | **MASS / the envelope** — the §3 interface, the only ε↔T2 machinery |
| **the door** | the **off-line ↔ on-line boundary** — where the transfer is gated |

**★ bias ≠ release — two independent questions.** R-A asks whether a held static field **biases** the saturation kernel (the K1-vs-canon fork, docket R-A; the muon loads the full `|E|` into the `V_yield` / T2 key, `research/2026-07-10_x41-radiative-scoping-why_RESULT.md:154`). F6 asks whether stored energy **releases** into T2. A bias is not a release; conflating them is the trap.

**Three candidate release mechanisms (as delivered):**

- **(A) Continuous entropic drainage.** Rotation-coupling into the mode-count arrow (§2b); irreversibility from reservoir mode-count, **rate unforced.** The arrow-of-time class.
- **(B) Frontier clicks — X40 writ cosmological.** Discrete ring-completion mints (§2b) at the crystallization frontier. ★The corpus rate `Γ = 3H·ρ_latent` is exactly the **frontier-minting reading** — "∝ crystallization-FRONTIER-rate `3Hρ_latent`, reading-ii by construction" (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:84-87`), with the `3` reading as dimensions. This is the route that **converts the FORCED-form / ASSERTED-rate `Γ`** (`…:121-136`) into a *derived* rate class.
- **(C) Envelope ports.** The transducers (§3) are the ONLY ε↔T2 machinery ⇒ ★**DE-TRACKS-MATTER becomes a port-LOCATION signature** (dark energy drains where matter's envelopes are). ★**Hard constraint:** the port must **NOT drain its own transducer** — the electron is stable / lossless (the terminal pole, §5), so whatever F6 is, it cannot bleed the electron's own store.

**Q4 — the two-tier build (pending Grant's go).**

1. **A global two-reservoir ODE ledger.** There is **no `a(t)` evolver today** — `solve_backreaction` is static-elliptic (`manuscript/ave-kb/common/engine-capability-map.md:155`). The first build is the missing global state object: a two-bucket (ε-store, T2) first-law ODE.
2. **Then ONE X40-class click demo** — a single ring-completion-class mint booked into the ledger, to show one-way-at-an-event coexists with exact conservation.

**Gates and scope (CC-HONEST):**

- **`ρ_latent` parameterization is the Grant-gated go.** `clm-s4n33u` solidity 0.45, build_status "use as input only, don't build deeper" (`manuscript/ave-kb/.index/claims.jsonl`); the numeric value is SYMBOLIC-ONLY / ABSENT (`…/dark-energy-latent-heat-definition.md:121-136`), and F6 hard-blocks on it (gate 5, `…:152-158`).
- **Scope is existence + form of DE-tracks-matter ONLY.** The naive `ρ_latent` overshoots `ρ_Λ` by ~120 OOM (`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:8,58`) — so the value is not the deliverable; the *mechanism-existence* is.
- **Book both legs.** Every mint leaves an X40-style **cycle-space deposit** (the trapped `f_E = 1/10`; `research/2026-07-10_x40-ring-closure-transient_result.md:18-20`). The ledger must book the trapped fraction as well as the radiated one — depletion is a *partition*, not a one-sided drain.

**★ FLAGGED — the R-A / F6 ONE-DOOR unification (11th convergence).** The candidate: **statics are stable BECAUSE release requires a topological event** — the same door that gates F6's release (B/C) is why R-A's held field does not bleed the static store. One door, two faces. Named **kill-shapes** (this stays a flag until it survives them): (i) it must leave the R-A *bias* question untouched (bias ≠ release, above); (ii) it must reproduce the **muon fence** (the muon loads `|E|` into T2 but does not decay by it); (iii) it must survive **electron-no-drain** (constraint C). This is a convergence *candidate*, not a ruling — recorded for Grant, owed its kill-tests.

## §5 ★★ GRANT'S CASCADE-FILTER ONTOLOGY (his Q3 answer, verbatim-faithful)

> **Grant, verbatim:** "the first two [A, B] are more of a description of why there's levels of stability if you think about this as a cascade filter; the electron is the lowest order; the universe envelope would be the highest order — so that would mean the amount of nodes or total collective; mechanical stress internal would be the differentiation creating the boundary regions."

This reframes §4's mechanisms A and B: they are not two competing depletion primitives — they are the **two coupling classes of a multi-stage cascade filter**, and "why there are levels of stability" is the cascade's stopband structure. The electron is the **lowest-order stage**; the universe envelope is the **highest-order stage**; the ordering variable is node count / total collective; and **internal mechanical stress is the differentiation that draws the boundary regions between stages.**

**INTERIM CANON MAPPING (as walked).** *Receipt discipline: the electron and black-hole ENDS of the ladder verify at this HEAD; the middle-ladder numbers and the input-impedance framing are the walk's reading and are FLAGGED PENDING the vol9 circuit-mapping investigation `ww0giq5he` (§ note below).*

- **(a) The top stage's port already exists in canon = the Machian horizon termination.** The walk's reading: `G` as the **transmission-line input impedance at the Hubble radius `R_H`** (~1e39 cells), with `a₀ = cH/2π` the same port. The canonical anchors are `G = ħc/(7ξ m_e²)`, `α_G = 1/(7ξ)` (`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/gravitational-coupling-constant.md`) and `H_∞ = 28π m_e³ cG/(ħ²α²)` (`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md`). ⇒ **`Γ = 3H·ρ_latent` reads as the top-port drain law** (the §4(B) frontier-minting rate; `…/dark-energy-latent-heat-definition.md:84-87`). *(The specific `input-impedance @ R_H` / `~1e39 cells` / `a₀ = cH/2π` identification is the walk's framing, pending `ww0giq5he`.)*
- **(b) The Q-ladder is the cascade's stability spectrum.** VERIFIED ends: the **electron = the TERMINAL POLE**, `Q_tank = 4π³ + π² + π = α⁻¹` (lossless, no onward port — why every ringdown ends there); the **black-hole stage** rings at `Q = ℓ` (for `ℓ = 2`, `Q = 2`) — both are cross-scale fires of the one Op21 `Γ = −1` saturation-boundary mode-counting mechanism (`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md:18,20`). ⚠ The MIDDLE of the ladder as recalled in-walk (muon `≈ 3.5e17`, atom `≈ 1e7`) is **NOT verified at this HEAD** — flagged pending `ww0giq5he`.
- **(c) A / B unify as the two coupling classes of any cascade.** (A) = passband drainage (continuous entropic transfer); (B) = boundary-click reconfiguration (topological mint). **Which dominates at a stage is set by that stage's boundary quality.** So F6's ruling becomes: **which stage's door** is F6, and **which coupling class** does it use.
- **(d) ★ Stress differentials CREATE the stage boundaries.** The cascade is **EMERGENT from the T_ij register**: internal mechanical stress is the field that draws the boundary regions (Grant's closing clause). So the two registers are **one architecture** — `T_ij` (Register 1, §2d) is the **boundary-drawing field of the hierarchy**, and the cascade (Register 2's home) is what that field partitions. The materialization build (§1) is therefore load-bearing for *both* registers in a second, deeper sense.
- **(e) Rails (OPEN).** The **ordering variable** (node count vs mode count vs winding complexity) needs the canon check. **Stress-drawn vs topology-drawn boundaries** is likely a division of labor — topology draws the terminal wall (the electron's `π₁` pole), stress draws the intermediate ones — but this is OPEN. **12th convergence** of the arc, FLAGGED; kill-tests owed (it is not a ruling until the ordering variable is pinned and the middle-ladder verifies).

**NOTE — the vol9 investigation is in flight.** The vol9 circuit-mapping investigation (Grant-directed, workflow `ww0giq5he`) is running; its cascade-map — the firmed Q-ladder, the ordering variable, the stress-vs-topology boundary division — **lands as a follow-on addendum, not in this note.** §5 records the ontology and its verified ends; it does not close the mapping.

## §6 THE SYM-GRAVITY WALK (2026-07-12, chat-record landing here)

*This section lands a 2026-07-12 chat-record walk in the durable trail. FRAMING NOT DERIVATION; the quarantine header governs.*

**The picture.** Gravity is **even (A1) mechanical strain coupling to transverse waves through SYMMETRIC saturation** — both elastic moduli grade *together*. Then the index `n = √(εμ)` grades while the impedance `Z = √(μ/ε)` stays matched at `377 Ω` everywhere ⇒ **refraction without reflection.** The canonical ray-trace is the derived transverse-shear index `n_⊥ = 1 + (2/7)χ_vol`, which recovers `4GM/bc²` (the observed 1.75″); the `ν = 2/7 ⟺ K = 2G` algebraic identity is at `src/ave/core/constants.py:385`, and the deflection derivation + the `z = (n_temporal − 1)/2` factor-2 bridge are at `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:26,28`.

**The SECTOR CARVE.**

- **Gravity = SYM loading** — both moduli graded, impedance matched, `Γ = 0`, **EP-clean**. This is the coupling-CMRR face: a common-mode grade the differential instrument rejects (the EP / CMRR acceptance framing, `research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md`).
- **EM statics = ASYM loading** — `S_ε` only (permittivity softens alone), so `Z` changes and `Γ ≠ 0` is **readable**.

> ⚠ **Cite correction (verify-before-cite).** The walk pointed this carve at `CLAUDE.md:75`; that line did **not** verify — `CLAUDE.md:75` is the repo's *Pure-AVE-corpus rule* text, not the SYM/ASYM physics carve. So the carve is recorded here as **chat-record framing**, anchored on the `ν = 2/7` both-moduli grade (`constants.py:385`) and the common-mode-blindness of the differential birefringence observable (`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md:108` — "the common-mode (isotropic) shift the polarimeter is blind to"), **pending a canonical carve leaf.**

**The REGIME LADDER.**

- **Weak field = LINEAR in even strain.** `S(A)` is second-order in the amplitude, so a first-order weak-field effect is linear in the even strain — which is **exactly why X44's `√S` clock failed** to match at leading order (`Δ_clock/U_bind ~ 0.03–0.07`, relative mismatch 93–97%; `research/2026-07-12_x44-komar-source_result.md:17,25-26`).
- **Deep-MOND / near-yield = where "symmetric saturation" IS the coupling** — the `η_eff` sector, where the second-order `S(A)` structure stops being negligible.

**Open ends (named, not closed):**

- the **`n_eff` overload** — the per-sector sign / power chain is unpinned (the KB `n_eff` symbol reconciled to two quantities; `_orchestration/2026-07-11_engine-refresh-handoff.md:135-138`). This is **X44b's chain.**
- **T4 keying** — the transverse-sector keying, open.
- **`K = 2G` + perihelion imports** — `K = 2G` is GR-imported (`src/ave/core/constants.py:781,769-773`), and the perihelion coefficient is hand-set; both ride into this sector as imports, not derivations.

**★ FORWARD STATEMENT — the SYM exposure.** The symmetric carve predicts **ZERO gravitational reflection** and **ZERO lensing birefringence**: light bends but never *partially reflects* off a gravitational well, and lensing is **polarization-blind**. This is consistent with all current data. **Kill-shape:** any confirmed **polarization-dependence** or **reflection component** in gravitational lensing kills the symmetric carve outright. This is the standing empirical exposure of the SYM-gravity picture.

## §7 SEDUCTION ACCOUNTING

This walk added **three convergence flags** to the 2026-07-10 → 13 arc:

- **Convergence 10 — SYM / EP unification** (§6): gravity as symmetric-saturation matched-impedance loading unifies the equivalence-principle cleanliness with the coupling-CMRR face.
- **Convergence 11 — the ONE-DOOR R-A / F6 unification** (§4): statics stable *because* release requires a topological event.
- **Convergence 12 — the cascade filter** (§5): the stability hierarchy as a multi-stage filter whose boundaries the T_ij register draws.

**The discipline check.** Three convergences in four days is exactly the pattern the seduction ledger exists to guard. That ledger stands at **0-for-7** — every prior hopeful-rhyme collapse target that was seduction-flagged has either been killed or is still held un-fired (`research/2026-07-10_collapse-target-registry.md:23,64,317`, the RHYME tier). Against that base rate, **every framing in this note carries either a named kill-shape or a named investigation**: §3 the radiation-EOS theorem-target (owed, not claimed); §4 the one-door kill-shapes (i)/(ii)/(iii); §5 the ordering-variable rail + the `ww0giq5he` investigation; §6 the lensing polarization / reflection kill-shape. No convergence here is asserted as a win.

> ⚠ **Cite discrepancy (flag-don't-fix).** The walk referenced the ledger as "**0-for-8**"; the last citable value in the corpus is **0-for-7** (`collapse-target-registry.md`, 2026-07-10). Either the walk's count is off by one, or an 8th seduction-flagged negative landed after 2026-07-10 that has not yet been booked into the registry. Recorded as-is for Grant / the auditor to reconcile — not silently adopted either way.

**Standing.** The transducer ontology (§3) and the cascade-filter ontology (§5) are **Grant-walked, ruling-grade INPUTS to the X44b and F6 charters** — not canon, not results. They set the *shape* of those charters (the source-side theorem-target for X44b; the which-stage's-door + coupling-class framing for F6); they do not discharge them. Nothing in this note is canonized.

---

## CONTINUATION (2026-07-13 EOD): walk rounds 2-3 + the cascade adjudication (RATIFIED)

**★ FRAMING, NOT DERIVATION — the quarantine header of this file governs this continuation too.** **KEEP-BOTH:** §1–§7 above STAND as the mid-day walk record; this continuation is the EOD close and **SUPERSEDES §5's cascade ontology *where explicitly noted*** — the cascade-filter framing is now **RATIFIED-KILLED at the atom rung** (see (e)). Grant statements below are verbatim-faithful walk record. **Nothing is canonized by this note.**

**What changed between the mid-day note and EOD.** §5 closed the cascade as the **12th convergence, FLAGGED, kill-tests owed**, and pointed at the vol9 investigation `ww0giq5he` "as a follow-on addendum, not in this note." That addendum landed; three satellite drivers fired (T1 #668, k-sweep #669, genesis #670 — all MERGED); Grant ratified the adjudication in-chat (2026-07-13). The headline, truth-first: **the cascade-filter framing has no distinct content at the atom rung — it is the homogeneous vacuum line relabeled, a vocabulary echo — and Grant RATIFIED its death.** This is Rule 11 working at full strength: a single mechanism (the α-echo on other-sector ports) explains the intermediate-rung Qs, the pre-registered kill fired, the branch is closed. No rescue was attempted; a clean negative is recorded and the branch is shelved.

### (a) Walk round 2 — Grant's six cascade answers

Round 2 answered the six open Grant-adjudications the vol9 map (c) surfaced. Recorded as walk positions (FRAMING):

1. **The ordering axis → the complex-power mapping (the 13th convergence, AS FLAGGED AT THE TIME).** Grant proposed the ordering as a **complex-number free-vs-entrained** axis; the core session mapped it to **complex power `S = P + jQ`** — a **power-factor ladder**: the photon is pure **real** power (`PF → 1`, free/propagating), the electron/soliton is pure **reactive** power (`PF → 0`, entrained/stored), and the intermediate rungs sit at intermediate power factors. This was flagged **AT THE TIME as the 13th convergence** of the arc. ⚠ *Per the ratified kill (e): the **endpoint** mapping (photon-`PF→1` / soliton-`PF→0`) survives as dictionary/peer content; **the ladder between the endpoints does not**.*
2. **`order ⊥ stability` accepted PROVISIONAL, pending T1.** Grant accepted the vol9 map's proposed dissolution — filter **order** = mode/pole count = `ℓ ≅ c` (electron lowest at `c=3`), **stability** = loss-Q (electron highest), the two anti-correlate as in any real filter — as a **PROVISIONAL** acceptance explicitly gated on the T1 atom-rung result. ⚠ *Per (e): T1 fired the kill, so this provisional acceptance is now **REVOKED** (there is no stability-spectrum ladder to order).*
3. **Top rung RULED LOCAL** (survives the kill). Grant ruled the "universe envelope" is the **LOCAL top rung of OUR stack** — the daughter membrane = our matched termination — which is **canon-compatible** (`manuscript/vol_9_vacuum_datasheet/chapters/12_cosmological_characteristics.tex:155,159,171`: our cosmic `Γ=−1` horizon is a parent-BH Schwarzschild radius, a **two-way-opaque symmetric membrane**; our universe is a daughter of a parent cosmology). His **BH-as-inter-universe-transducer** aside is **vol9 ch12's own generative picture** — a melted `Γ=−1` interior can re-crystallize into a daughter K4 lattice (ch12:170), so a BH horizon transducing between parent and daughter cosmologies is the corpus's own permitted (not-proven-universal) reading, not a new posit. *(Cite-correction / flag-don't-fix: the vol9 map `ww0giq5he` receipt #12 anchored this content at `ch12:23-24`; those lines carry the `R_H/ℓ_node` arithmetic, NOT the daughter-membrane text — the load-bearing content is at ch12:155,159,170,171. Corrected here.)*
4. **The envelope-eigenmode reconciliation** (survives the kill). The vol9 map's Lane-4 open fork — *is Grant's surface a stress-**balance** locus or the canonical strain-**yield** locus?* — Grant answered: **both coincide.** Yield **derives from opposite-but-equal stresses balancing across the envelope**, and that **balance-locus ≡ the `A_yield` level-set**. This is the **ENVELOPE-EIGENMODE GATE**, folded into the `T_ij` build (§2d) and **task-tracked with X44b**: the register must reproduce that the stress-balance surface and the strain-yield surface are the same eigenmode boundary.
5. **The srs `1/9` homogenization + Grant's carrier-wave lean.** Grant accepted the vol9-map reading that the srs per-vertex `Γ=−1/3` (`|Γ|²=1/9`) is **homogenized away for in-band collective carriers** and **resolves only near the band edge** — and leaned to the **carrier-wave** frame (below, (b)) as the propagation-view statement of the same physics. This is what the k-sweep #669 then measured directly (d).
6. **The component thesis STANDS.** Grant confirmed the vol9 datasheet's opening thesis — *"the vacuum as a **component**, not a stage"* (`manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex:18`) — is **not amended**. The planned vol9 **cascade material-property section is NOW SHELVED** per the ratified kill (see (e)); the book's opening posture is untouched.

### (b) Walk round 3 — the PFC anchors, the definability carve, the carrier-wave frame

**PFC calibration anchors (walk framing; arithmetic tagged as arithmetic).** The power-factor picture's two calibration ends:
- **`saturate = yield` (43.65 kV) ≠ `melt = snap` (511 kV)** — the carve between the T2 self-trap wall (`V_yield = √α·V_snap ≈ 43.65 kV`, `src/ave/core/constants.py:505`) and A1 longitudinal completion (`V_snap ≈ 511 kV`, `constants.py:496`). These are two *different* operating-point terminations, not one; the entrained-node ladder tops out at **yield**, not snap.
- **CMB floor `k_B T ≈ 2.35×10⁻⁴ eV`** (arithmetic: `8.617×10⁻⁵ eV/K × 2.725 K`) — the substrate's ambient reactive bias floor. `δ_strain` = **the floor's measured bias-load** on the node (the always-on DC operating point every node sits at).
- **`~93 dB` headroom** from the floor to yield is **TAGGED as arithmetic** (a `20·log₁₀` span between the floor bias and the yield wall), not a derived physical prediction.
- **The entrained-node definition is bounded `floor → yield`**: a node counts as "entrained" between its ambient CMB bias floor and its yield termination.

**★ THE DEFINABILITY CARVE — a binding model-scope rail (survives the kill).** The structure is **definable exactly between its two terminations**, and **both terminations enter models as BOUNDARY IMPEDANCES, never modeled-through**:
- **Bottom termination = the electron:** `Γ=−1`, `PF→0`, the **terminal pole** (no onward port; `Q_tank = 4π³+π²+π = α⁻¹`, lossless). A model may set it as a boundary impedance; it is never modeled *through* (there is no interior to the pole).
- **Top termination = the local daughter membrane:** `Γ→0` (matched), **impedance measurable from inside = `G/a₀`** (the Machian-horizon input-impedance port). A model may set it as a boundary impedance measured from within.
- **Through-membrane = UNDEFINABLE IN PRINCIPLE** — the `Γ=−1`/two-way-opaque symmetric membrane makes the exterior causally + impedance-disconnected; no observable crosses it (ch12:171,176).
- **The three-way definability ledger:** (i) **defined now** — the interior between the two terminations, at `Z_0`; (ii) **definable-pending-a-named-build** — the two terminations' impedances as boundary conditions (need the named build to instantiate them); (iii) **undefinable-in-principle** — anything through either membrane.
- ⚠ *The mid-day note's "ladder between the terminations" language is now **SOFTENED** per the kill: the two terminations are canon and stand as boundary impedances, but the **graded ladder of distinct filter sections between them does not** — the interior is one homogeneous line at `Z_0`, not a staged cascade (see (e), (g)).*

**The carrier-wave frame (now VALIDATED as bin (i) by #669).** The propagation-view statement of the free/entrained axis:
- **photon = envelope on the linear carrier** — pure **real** power, **no stored potential** (it rides the medium, deposits nothing);
- **soliton = self-carried envelope** — **stored potential = the Coulomb-dress graded carrier well** (it carries its own well with it);
- **carrier/envelope IS free/entrained** in the propagation view — the same axis as (a.1)'s `PF` mapping, stated for propagating modes.
This frame predicted that a band-interior collective carrier barely sees the per-vertex tee (homogenized) while a band-edge mode resolves it — **exactly bin (i), which #669 measured** (σ=0.123 suppression, ρ=3.14 band-edge rise; see (d)).

### (c) The vol9 cascade map (`ww0giq5he`, receipts grep-confirmed by the lanes)

The vol9 circuit-mapping investigation returned a four-lane synthesis. Headline (its own, truth-first): **Grant's cascade-filter picture is a genuinely new framing that canon does not carry, but every load-bearing PART already exists with receipts; what is missing is the ordering axis, a distinct per-stage cutoff, and the inter-stage coupling law — and the framing's cleanest payoff is that it gives F6 a physical address.**

- **CANON-SUPPORTS (the rungs and walls exist; the cascade does not).** Six concentric `Γ=−1` scales with the same M/Q/J boundary-observable per row (`manuscript/vol_9_vacuum_datasheet/chapters/12_cosmological_characteristics.tex:70`; `manuscript/ave-kb/common/trampoline-framework.md:716`); the Machian top port `G` = TL input impedance at the Hubble-horizon termination (`translation-circuit.md:126`, MIXED-tagged, engine ξ a CODATA back-solve `constants.py:650`); the Q-ladder endpoints (electron intrinsic `Q→∞`; BH QNM `Q=ℓ`) are canon while the middle rungs are FRAMING walk-estimates; walls form at the Ax4 strain-yield threshold; inter-scale walls are made of impedance mismatch (the atom = "a wave trapped between its own reflections in a well made of MISMATCH"); the native ordering ladder is **topological** (`c = 3,5,7… ↔ ℓ`, electron ground at `c=3`); the only true circuit cascade in vol9 is **N identical cells** (homogeneous TL).
- **GENUINELY-NEW (five items, absence two-method-confirmed).** (1) stage ordering by **node count** (zero canon hits); (2) **A/B-as-stability-levels** of one cascade filter (F6/depletion entirely absent from vol9); (3) **universe-as-top-stage-envelope** (canon carries the OPPOSITE topology — daughter membrane inside a parent, nesting inward-generative, no outermost stage); (4) **stress-differentiation as boundary-formation** (canon forms walls at strain *thresholds*, not stress *gradients*; the bulk self-trap route is natively FALSIFIED as a Cartesian-grid artifact, `engine-acceptance-suite.md:158`, under re-adjudication); (5) the framing, if adopted, would **amend** the datasheet's "component, not a stage" thesis.
- **★ THE A-B PORT-CLASS UNIFICATION PROPOSAL.** Each stage = a `Γ=−1` envelope acting as one filter section; each inter-stage junction = a mismatched port carrying **exactly two coupling classes**: **A (continuous entropic drainage) = the sub-threshold class** (the always-on leak through the port's residual `Re(Z)` — what a loss-Q measures; the srs `−1/3` counting floor is its primitive unit), and **B (frontier clicks) = the supra-threshold class** (discrete transfer of one topological unit when the SAME yield surface is driven past threshold — pair-production at `V_yield` the type specimen). Stability then falls out: a stage is stable to the degree its port is mismatched below threshold and its occupancy is topologically protected above it; the ladder runs monotonically DOWN in loss-Q toward the matched Machian termination.
- **THE SIX ADJUDICATIONS surfaced for Grant** (all answered in round 2, (a)): (1) which node count orders — standing-wave `ℓ≅c` (canon) vs lattice-population (new axis); (2) which Q the stability spectrum orders on — or accept the order⊥stability anti-correlation; (3) top rung = local daughter membrane (canon-compatible) vs true outermost envelope (supersedes canon); (4) stress-balance vs strain-yield surface (and gradient-as-cause vs gradient-as-localizer); (5) the srs `1/9` real-loss-vs-idealization fork; (6) whether the framing amends the "component, not a stage" thesis.
- **★ THE KILL-SHAPE, AS FROZEN (one sentence, `ww0giq5he`).** *"If the nested envelopes turn out to be the same cell tiled at different span-lengths — identical sections, no distinct per-stage cutoffs — the cascade filter is the homogeneous vacuum line relabeled, and the picture is an echo of vocabulary, not a structure."* The seduction accounting was maximal-by-profile (it unifies A, B, the Q-ladder, F6, and the Machian port in one EE-native metaphor — a shared-narrative magnet; the ½/¼-style over-determination tell = it "explains" stability levels before a single distinct per-stage cutoff is derived).
- **THE FOUR NAMED TESTS the framing owed.** **T1** (cheapest discriminating): derive ONE intermediate rung's Q from substrate — the atom's `~10⁷` — *a derived distinct value kills the relabel-echo; failure to get a distinct value IS the kill firing*. **T2**: assemble the cosmic-envelope Q from `T_U / ∂_rS` and check it lands `O(1)`-matched. **T3** (the chord): build F6 as the top port's irreversible A-channel, rate slaved to lower-stage B-occupancy — the DE-tracks-matter numeric (unchanged make-or-break). **T4** (gating fork): resolve the srs `1/9` per-vertex ontology.

### (d) The three satellite verdicts (all MERGED; re-verified at main `f007fe34`)

**★ T1 — the atom-Q cascade gate (#668 MERGED; `research/2026-07-13_t1-atom-q-cascade-gate_RESULT.md`) = BIN (ii) NO-DISTINCT-VALUE — the pre-registered kill FIRED.** Run on x42's own de Broglie dispersion, the atom's wall insertion-loss `Q_wall → ∞` — the electron-**intrinsic endpoint** — for H(1s), H(2s), He⁺(1s), and the reduced-mass leg, **α-free** (`I(R)` identical for Z=1 and Z=2 to `rel<1e-9`; no `Zα` signature). The observed `~10⁷` "excited atom" rung is **not a wall loss-Q at all**: it is the **transverse-EM (`Z_EM`) radiative port** — a *different sector* x42's longitudinal Hermitian eigencavity does not express (bin (iii) rider) — and it is **α-sourced: `Q_rad = 4α⁻³` exact** (the QM `≈ 9.6α⁻³ ≈ 2.5×10⁷` is the measured rung). The **false-kill probe cleared it as a TRUE-KILL** (all four wall-leakage refutation channels — tunneling escape, shape resonance, `ℓ>0` centrifugal, autoionization — tested and closed; the outer Coulomb barrier is infinitely thick for any sub-threshold bound state ⇒ `T=0`). The **positive control fired bin (i)** (a planted finite barrier returned `Q_control = 1.02×10⁶`, in-window) — so the `∞` is a physics verdict, not an unfireable gate. Class: **CONSISTENCY / framing-demotion, not an axiom falsification** (`clm-acdc07` pure-AC). The kill is **robust to the X41 K1∧K2 open fork** (a reactive `S_ε<1` loading is not a resistive loss; `Re(Z)=0` sub-yield holds regardless).

**k-SWEEP — srs vertex k-sweep backscatter (#669 MERGED; `research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md`) = BIN (i) HOMOGENIZATION-SPLIT.** All four frozen classifier conditions pass with margin: **σ = R_LW/R_dis = 0.123** (suppression ≤0.35), **ρ = R_BE/R_LW = 3.14** (band-edge rise ≥2.0), disorder control flat at **0.500**, chirality-blind to **2×10⁻¹⁶** (enantiomorph symmetry, exact). Lossless to machine ε (drift `1.7×10⁻¹⁴`); all three evolved-field sabotage plants caught (plant D — the lossless fwd↔bwd mix — caught by the monotone-rise gate G3). **Honest refinement:** long-λ is a strongly-**suppressed plateau** (`R≈0.062`), not a strict power-law-to-zero (a refinement, not a walk-back — the classifier tested suppression + band-edge rise, both hold). **The band edge is not independently located** — the dispersion probe reaches only `k·ℓ≤0.83`, so "band-edge" labels the high-k end of the monotone rise, not a measured `v_g→0`. Class: **CONSISTENCY / peer-with-SM** — ordinary "periodic medium transparent to long-λ carriers, reflective at band edges" physics, quantified for the chiral srs `z=3` net; **not an AVE-distinct chord.** This validates the carrier-wave frame (b) as bin (i).

**GENESIS — N≥14 persistence battery (#670 MERGED; `research/2026-07-13_genesis-npersist-n14-battery_RESULT.md`) = the two frozen channels SPLIT.** Reproduction byte-exact vs banked #655. Under PML the two detector channels diverge: **`E_persist` recovers** with N (`0.69 → 0.84 → 0.87`, N 10→14→16) = **absorber leakage confirmed** (the handoff's E-channel artifact premise holds); **`φ_persist` collapses** with N (`0.87 → 0.73 → 0.51`) = **boundary-CLEAN non-persistence** (persistence fails *worse* where the boundary matters *less* — the opposite of a boundary artifact). **Closed-box = reflecting-cavity artifact-leaning:** `E_persist ≡ 1.0000` exactly (a conservation identity, structure-independent) and `φ_persist` **runs away to ~10×** (N-stable at both N=14/16 — a systematic cavity mode-feeding, not stable retention; a genuinely persistent structure holds `φ≈1`). The frozen E/φ detector is **boundary-degenerate** (same seed, same N: φ=0.51 absorber vs 10.5 reflector). The only boundary-**insensitive** signal — the cross-N φ-dispersion trend under PML — **leans CONFIRMS bin (ii) A-WEAKENED** (G-PERSIST CONFIRMS). **(B) node-mint stays firewalled** either way.

### (e) ★ THE CASCADE ADJUDICATION — RATIFIED (Grant, 2026-07-13, in-chat)

Per the frozen kill-shape (c), T1 fired it cleanly at the atom rung. **Grant RATIFIED the kill in-chat (2026-07-13):** the cascade-filter framing **has no distinct content at the atom rung** — it is *"the homogeneous vacuum line relabeled — a vocabulary echo."* This is not a partial demotion; it is the honest closure (Rule 11) of the cascade convergence.

**DIES WITH IT (★RATIFIED):**
- **The PFC / power-factor ordering (the 13th convergence)** rode T1 and dies with it. **Surviving remainder:** the **endpoint** mapping (photon-`PF→1` / soliton-`PF→0`) survives as **dictionary / peer content**; **the ladder between the endpoints does not.**
- **The `order ⊥ stability` provisional acceptance (a.2) is REVOKED** — there is no stability-spectrum to order once the middle rungs are not distinct sections.
- **The Q-ladder-as-stability-spectrum reading dies.** Honest read: **two canon endpoints** — the electron's **intrinsic `Q→∞`** (terminal pole) and the BH's **`Q=ℓ` mode-count** — **plus middle rungs that are radiative α-echoes on other-sector ports** (the atom's `~10⁷ = 4α⁻³` transverse `Z_EM` port, per T1). The middle of the "ladder" is not a cascade cutoff spectrum; it is the same α-echo family read at different powers on ports the longitudinal cavity does not own.
- **The planned vol9 cascade section is SHELVED** (a.6); the datasheet's "component, not a stage" thesis stands unamended.

**SURVIVES INDEPENDENT OF THE CASCADE (each stands on its own canon/verdict, not on the killed framing):**
- **Top-rung-LOCAL ruling** (a.3) — a canon-based ruling about the daughter membrane, independent of whether a cascade orders the interior.
- **The definability carve's two terminations** (b) — electron `Γ=−1` bottom pole + local daughter-membrane `Γ→0` top port — are **canon-based boundary impedances**; only the *graded ladder between them* was killed.
- **The envelope-eigenmode gate** (a.4) — the stress-balance ≡ strain-yield level-set reconciliation, folded into the `T_ij`/X44b build.
- **The F6 charter** (#666 MERGED) — it **quarantined the cascade address as a Grant-walked INPUT** (`research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:50,178`), so the kill does not retract F6; and F6's **own review relocated the chord to the DESI/Euclid *spatial* cross-correlation channel** (`…_CHARTER.md:358`; `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:159`) — a homogeneous global ledger (tier-1) is the wrong instrument, and bin (iii) FORM-DEGENERATE is the *expected* tier-1 outcome.
- **A / B as F6 ledger bookkeeping** — A (drainage) and B (clicks) survive as the two entries the two-reservoir ODE ledger books, not as cascade coupling-classes.
- **The homogenization physics** (peer-class) — now **measured** by #669 (σ=0.123, ρ=3.14); the srs `1/9` is a real yet **carrier-selective** unit (expressed for band-edge-straddling content, homogenized for band-interior carriers).

**Ledger routing.** **Convergences 12 (cascade filter) + 13 (power-factor ordering) → the killed ledger** (booking IN FLIGHT, sibling lane `docs/cvr-miskey-qladder-relabel-killed-ledger`, Grant-GO'd). **Routed follow-ons GO:** the **Q-ladder atom-rung relabel + the CVR-DC mis-key fix** (sibling lane, IN FLIGHT); the **F6 tier-1 driver** (sibling lane `analysis/f6-tier1-ledger-driver`, IN FLIGHT, charter merged #666).

### (f) THE G-PERSIST FORK (PENDING-GRANT — do not pre-empt)

The #670 battery (d) leaves one framing-level fork open for Grant. The physical picture, plumber-stated:

- **Reading A — echo chamber (the core session leans A).** In the closed reflecting box, `φ→10×` is a **structured seed acting as a good antenna for its own returns**: the projection accumulates because the flux has nowhere to leave. **Tells:** `E_persist ≡ 1.0` (mode-independent, a conservation identity — even the structure-dead `photon_lock` seed clears it); the `10×` growth is **N-stable** (systematic cavity effect, not a box-size recurrence); a *genuinely* persistent structure would hold `φ≈1`, not run to 10×.
- **Reading B — genesis-under-confinement.** The closed-box growth is a **real localization instability** (the flux self-amplifying into a bound resonance), which would support A-SUPPORTED.
- **The discriminating meter = SPATIAL CONCENTRATION** (a participation-ratio / core-fraction observable): a genuinely localized structure keeps a high central-core fraction of interior energy / `Φ_link²` under **both** boundaries; a dispersing/sloshing one does not.
- **★ The stamp flip does NOT require the fork.** The PML φ-dispersion trend (`0.87→0.51`, worsening as the interior grows) is **boundary-clean on its own** and supports bin (ii) A-WEAKENED regardless of how the closed-box fork resolves. The fork bears only on whether the closed-box read is rehabilitated, not on the G-PERSIST lean.
- **Follow-on candidates (PENDING-GRANT):** (1) the **localization observable** (KEEP-BOTH new axis alongside the frozen E/φ detector — never a swap); (2) a **φ-channel plant** (a negative control that sustains φ *without* clobbering the Cosserat state — the #670 plant destroys φ, so it exercised only the E-channel).

*Recorded as **PENDING-GRANT**: the closed-box fork ruling, the two follow-on candidates, and the docket stamp flip are Grant's word to give. Nothing here canonizes them.*

### (g) ★ THE SHAPE-OF-THE-MATHEMATICS synthesis (core-session, Grant-prompted; FRAMING)

Grant prompted the core session for the shape of the mathematics the week's five instruments actually exercised. Recorded as framing, not as a result:

1. **Two fixed points, no ladder.** There are exactly two: **perfect mismatch** (`Γ=−1`, topologically gated, `Q→∞`) and **perfect match** (`Γ→0`, absorbing). Everything "between" is not a rung — it is **the same two fixed points projected through sector ports** (the atom's `~10⁷` is `Γ=−1` electron content seen through the transverse `Z_EM` port, an α-echo, not an intermediate `Γ`).
2. **The interior is IDENTITY-DOMINATED; discriminating content lives only at identity-BREAKS.** Between the fixed points the dynamics is identity (homogeneous line, `Z_0` everywhere). Real content appears only where an identity breaks: the **band edge** (periodicity identity breaks → #669), the **yield surface** (the linear-response identity breaks → the envelope), the **periodicity defect** = envelope / sector port / decorrelated inputs. This is **the mathematical face of the phase-only epistemology** — no direct observable in the bulk; the signal is the self-cancellation *failing*.
3. **Even nonlinearity ⇒ second-order-only signatures ⇒ all discriminators are FORM-class, never MAGNITUDE-class.** The `S(A)=√(1−A²)` kernel is even in A; its leading correction is `−½A²`, second-order. So every discriminator the framework offers is a **form** (a sign, a power law, a flatness, a `1/√2` fraction), never a magnitude — which is exactly why the CVR magnitude route is dead and the discrimination must stack `{sign ∧ gap-power ∧ flatness}`.
4. **Exactly three value-generators, closed.** **Topology owns integers** (winding numbers, `c=3`, `Γ=(2−z)/z`); **the kernel's algebra owns parameter-free forms** (`4π³+π²+π`, `1/√2`, `1/9`, `2/7`); **the import basis `{m_e, α, G}` owns scales**, with **α-POWERS as the sector-port ladder** (`α⁻¹` = electron loaded Q, `α⁻³` = the atom/birefringence radiative echo — the "ladder" that survives is *powers of α on ports*, not distinct cascade cutoffs).
5. **Operational corollary = the test-design rule: never measure a magnitude, break an identity.** The week's five instruments were each **exactly one identity-break**: T1 (the atom wall-Q vs the intrinsic-endpoint identity), #669 (the periodicity identity at the band edge), #670 (the persistence identity under boundary swap), the CVR sign/gap-power axes (the even-response identity), the F6 decorrelated-history arm (the `H↔n_matter` lock identity).

**Honest coda (Grant-faithful).** This is **the shape of the mathematics we have** — form-deriving, value-importing. Whether it is **the shape of the vacuum** or **the shape of our echo** is precisely what the identity-breaking **forward** tests decide; the mathematics itself cannot settle it, because a form-deriving/value-importing structure is uniformly peer-with-SM inside. The chord, if there is one, lives only in the forward predictions.

### (h) Reconciliations (flag-don't-fix; receipt-debt tracked)

- **The seduction ledger stands 0-for-7 BOOKED + pending increments.** The corpus's last citable value is **0-for-7** (`research/2026-07-10_collapse-target-registry.md:23,64,317,769,772`, re-verified at this HEAD; `program-arc-map.md:404`). The mid-day note's §7 flagged a "0-for-8" walk-reference; **reconciled here: the "0-for-8" counted a *pending* X43 increment that has not yet booked.** Pending increments awaiting Grant's miss-ledger gating: **X43** (ringdown-port, `analysis/x43-ringdown-port` in flight) and **C13b** (`analysis/c13b-gamma-run` in flight). The booked value stays **0-for-7**; the increments are pending, not booked.
- **The muon "0.74-cell radial straddle" figure remains UNRECEIPTED** — a walk estimate (Grant, 2026-07-13) with **no corpus home** (confirmed by #669: *"muon content ~0.74-cell radial = Grant's leaned estimate, no corpus receipt"*, `research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md:203`). **Receipt debt — do not cite as fact.** Relatedly, the middle-of-ladder `Q_μ ≈ 3.5×10¹⁷` (`vol4/…/ch14-leaky-cavity-particle-decay/theory.md:14`) stays **flagged NOT-verified at HEAD** (as §5 already noted), carried as a cited lean only.

**Standing of this continuation.** The cascade adjudication is **★RATIFIED** (Grant 2026-07-13); the G-PERSIST closed-box fork + follow-ons + docket stamp flip are **PENDING-GRANT**. Everything else here is FRAMING-record of walk rounds 2–3 and the three merged satellite verdicts. **Nothing in this continuation is canonized.**
