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
