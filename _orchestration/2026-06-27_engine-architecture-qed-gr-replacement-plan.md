# STANDING REFERENCE — "QED + GR as ONE ENGINE": coupled-sector architecture, data-flow design, and pressure-test ledger

**Class:** FRAMING / PLANNING. No new `clm-` IDs. This is an architecture plan + standing stress-test, NOT a claim of completed replacement. It is iterated on in place.

**Verification basis:** HEAD `00f1e97b` (PR#432 merged, P1a carrier-unification), `/private/tmp/audit-electron`. Every file:line below was grep/read-confirmed this turn unless explicitly tagged STALE / corrected. Anchors that the upstream maps/pressure-tests cited but that did not resolve this turn are flagged inline (one stale module path corrected).

**Honest one-line posture:** AVE reproduces the *structure* of QED+GR (exact-integer charge, no-renormalization, real lossless photon, gravity-as-graded-index matching GR at O(GM/rc²)) and forces the *forms* through a single Axiom-4 kernel `S(A)`, while *importing* the values (α, G, m_e) and *not yet* realizing the back-reaction loop, the explicit bulk→EM pipe, the genesis source, or the per-mille predictive precision QED owns. The replacement is **PARTIAL — structural-real, magnitude/precision/genesis-open.**

---

## §1 — ARCHITECTURE MAP (sectors · modules · state · existing couplings)

### 1.1 The four substrate sectors and their modules

| Sector | Physics role | Module(s) (corrected paths) | Build/validate state @ HEAD |
|---|---|---|---|
| **A1 dilatation / BULK / longitudinal** | mass · gravity · the "3" (Heaviside scalar) | `ave.solvers.native_cage_imex` (diamond z=4, P0); re-homed onto chiral srs z=3 by `ave.solvers.srs_cage_winding.SrsCageWinding` (P1a). Facade `src/ave/facade/unified_engine.py:270-301` (`a1_cage`/`energy_gate`), `:422-437` (`unified_srs`) | **BUILT + VALIDATED.** P0 closed-box energy gate clears 1e-8 (A→0); live-fire `test_facade_p0_validate_on_known` 9/9 + `test_p1a_carrier_unification` 6/6 PASS. Localizer = Γ=−1 boundary cavity (bulk self-trap CLOSED-NEGATIVE) |
| **Cosserat T2 micro-rotation** | charge · spin · the (2,3) winding (helicity) | `ave.solvers.srs_cage_winding` carrier `:309-327`, `:396-412`; integer reader `compute_Q_link_srs` `:190-258`; canonical reader `ave.topological.charge_quantization.compute_Q_link:257` | **BUILT + VALIDATED as a STATIC winding.** Live-fire: seeded (2,3) reads Q_link(pol)=3, w_tor=2, ω≡0→0; Q_link 3→3 HELD over 60 coupled steps, verdict WORKS. Genesis-24-orthogonal to the A1 phasor |
| **srs-3 EM transverse** | photon · the QED sector | `ave.core.chiral_lattice{,_vector,_dynamics}`, wired `src/ave/facade/unified_engine.py:184-265` | **BUILT + VALIDATED.** Z₀=376.730 Ω derived-from-moduli (`:216`, ℓ_node cancels), unitary-scatter drift <1e-8, isotropy c(k→0)/c_link=1/√3; P0 9/9 + P1b 11/11 PASS. CONSISTENCY/IDENTITY-class (`:204-207`) |
| **Axiom-4 saturation** (the value-selector) | the ONLY nonlinear coupling — where the Γ=−1 wall sits, where mass forms | kernel `S(A)=(1−A²)^p` clipped `[S_min,1]` `src/ave/solvers/graded_vacuum_network.py:222-231`; facade `:386-416`; isolation eigensolver `solve_isolation_Q_sparse` `:431-466` | **KERNEL BUILT + VALIDATED, but CARRIED-DORMANT at P0** (regime-gated). `Regime.LINEAR_FREE` runs S=1; SATURATED dynamical exercise is P1+ scope. Isolation leg reproduces ECHO Q~30.8 (NOT 137) — α stays echo at the value level |

**EXCLUDED engines (firewall working as designed — do NOT re-import onto the verdict path):**
- `src/ave/core/fdtd_3d.py` — μ-on-static-|B| bug (fixed in-module via VCA-R01 `_compute_local_mu:222-260`, μ keys on circulation rate ω→ω_C not static |B|, but the module stays OFF the chord path). Facade docstring `:24` verbatim: *"EXCLUDED: master_equation_fdtd (Cartesian artifact), fdtd_3d (μ-on-static-|B| bug)."*
- `src/ave/topological/cosserat_field_3d.py` — α-BAKED (imports ALPHA, V_SNAP at `:56`); supplies α-free `TETRA_OFFSETS` + `KAPPA_TILDE_ELECTRON=6/5` (`:94`) as geometry-only inputs.
- `src/ave/topological/k4_cosserat_coupling.py` — legacy K4⊗Cosserat sim, α-baked (V_SNAP, KAPPA_CHIRAL_ELECTRON `:59,73`); superseded by `srs_cage_winding` for the α-clean path. **(Brief's `core/` path is STALE — actual home is `topological/`.)**

### 1.2 The existing inter-sector couplings (the data-flow ledger)

| # | Coupling | Direction | Derived/Asserted | Anchors (verified) |
|---|---|---|---|---|
| **1** | gravity → EM index `n(r)` | **ONE-WAY** (gravity strain sets EM medium; no EM back-reaction) | **DERIVED** (one Axiom-4 channel) | corpus `boundary-observables-m-q-j.md:95`; engine `gw_propagation.py:84-185`; linear index `universal_operators.py:1056,1075` (`n=1+ν_vac·ε₁₁`, ν_vac=2/7) |
| **2** | A1 ↔ ω `H_couple` | **TWO-WAY + conservative** (continuum-exact) | form DERIVED (Hamiltonian / Axiom-1 non-centrosymmetry); magnitude **κ̃=6/5 ASSERTED** (knot-topological) | `cross_sector_coupling.py:9-11,76-90`; `crystal_engine.py:221-250` |
| **2t** | trilinear photon-deplete arm | — | **CORRECTED-NEGATIVE** (Rule-12 RED): discrete H INDEFINITE, `photon_deplete=True` DETONATES; NOT a conservative lock | `cross_sector_coupling.py:130-141` |
| **3** | saturation → constitutive `ε_eff/μ_eff/C_eff` | constitutive ONE-WAY into EM update | **DERIVED** (one kernel projected) | `scale_invariant.py:164-221`; property(ε drops)-vs-response(C diverges) caveat `:181-184`; free-EM μ LINEAR per VCA-R01 `fdtd_3d.py:226-233` |
| **4** | graded network `Z_EM/Z_shear/Z_bulk` | inter-channel via `H_couple` (two-way) + TKI-transformer (`status:proposed`) | **CONSISTENCY re-expression**; route-decoupling DERIVED (static-E ⇒ S_μ=1 exact); chiral-circulator magnitude ASSERTED-pending-engine | `graded-network-response.md` §5/§7; `device-circuit-models.md:131,159-165,203,210` |

**The seed coupling — `n(r) = gravity → EM-index` — is the kernel of the whole unification.** Gravity enters EM by setting the operating-point strain `ε₁₁(r) = 7GM/(c²r)` that the single Axiom-4 channel reads, then `ε_eff/μ_eff/Z_EM` follow. Auditor arithmetic confirms the two corpus forms agree: `gw_propagation` linearizes to `n = 1 + (2/7)·(7GM/c²r) = 1 + 2GM/c²r` (first order of `1/(1−r_s/r)`), matching the manuscript `n(r)=1+2GM/rc²`.

### 1.3 QED-replacement status (the srs-3 / EM-transverse sector)

| QED feature | AVE status | Class |
|---|---|---|
| `Z₀=376.73 Ω` from moduli (ℓ_node cancels) | REPRODUCED-as-FORM / value-ECHO (Class-B SI substitution) | `z0-derivation.md:37,40` |
| `c` (wave speed from LC ladder) | REPRODUCED (`v_g=1/√(μ₀ε₀)≡c`) | `z0-derivation.md:49`; `master-equation.md:16` |
| photon lossless + emergent-Lorentz isotropy | REPRODUCED, validated (RAN: 11 passed) | `test_p1b_photon_l2_on_srs.py:100,101,104,165,169` |
| **charge = Link(∂Ω,F) ∈ ℤ EXACT, topologically forced** | **REPRODUCED — structural win QED LACKS** (validated, RAN 25 passed, 𝒬=3) | `charge_quantization.py:49-51,258`; result `2026-06-19-...:156-162` |
| **no-renormalization / finite** | **REPRODUCED — structural win QED LACKS** (lattice IS the UV regulator at ℓ_node) | `charge_quantization.py:49-51`; `master-equation.md:14-16` |
| α (fine-structure value) | **ECHO** (value-level), SCRUB not derivation | doctrine §B:81 (Class-B); `test_p1b_photon_l2_on_srs.py:234,241`; 3 lift-routes closed-negative (clm-0ktpcn) |
| per-mille / ppb predictions (g-2, Lamb shift, running) | **NOT DELIVERED** — the honest precision gap | — |

**Scope-guards on the charge win (echo-cite hygiene, already in source):** the EXACT-integer claim is CONDITIONAL on the `[Q]≡[L]` posit; the C.3 two-integrals gap STAYS OPEN (the direct Chern-Simons/Beltrami helicity integral returns ~18% of p·q, does not normalize to the integer); `p=2`/`N=3` are FIT/ECHO, not lattice-forced (`charge_quantization.py:14-34`; result `:170-173`; `2026-06-23-winding-result.md:12`).

### 1.4 GR-replacement status (the A1 / BULK / longitudinal sector)

| GR feature | AVE status | Class |
|---|---|---|
| `n(r)=1+2GM/rc²` (Shapiro / lensing / redshift) | REPRODUCED — **consistency-class, AVE=GR at O(GM/rc²) BY CONSTRUCTION** (Gordon optical metric) | `refractive-index-of-gravity.md:14-16,18` |
| mass = A1 dilatation | REPRODUCED — settled (#260 in HEAD ancestry @ 04bda99b) | `boundary-observables-m-q-j.md:19`; vol9 N-port index |
| K=2G trace-reversed = Einstein-elastic | REPRODUCED (FORM) but **provenance-corrected: GR-IMPORTED, not crystalline-forced** (PR#261 @ b49ce3b1) | `appendices-overview.md:99,119`; `trace-reversal-mechanism.md:20,23` |
| M/Q/J universal no-hair (BH↔electron) | REPRODUCED — structural win | `boundary-observables-m-q-j.md:35,43-48` |
| G (gravitational coupling) | **OPEN/MIXED** — form-derived, value-fitted (Chain B′ forward-derivation open) | `gravitational-coupling-constant.md:10` |
| ρ_Λ (cosmological constant) | **OPEN/MIXED** — ×1.54 of Planck-2018 (de Sitter asymptote exact); ρ_latent/Γ_cryst derivation open | `vol3/claim-quality.md:960,980,639,982` |
| genesis / self-formation of a confined core | **CLOSED-NEGATIVE** (clean, Rule-11) — NO-GENESIS, free longitudinal A1 wave DISPERSES (triply-confirmed) | `2026-06-14_t2-genesis-selflock_result.md`; Stage-2 MODE-III, S3 DISPERSE-FALSIFIED, #415 eigensolve DOES-NOT-EXIST |
| **EM stress-energy → bulk back-reaction (the GR half)** | **UNWIRED — zero hits in `src/ave`** (grep-confirmed this turn) | see §3 WEAKEST SEAM |

**Carried-forward GR-sector FLAGs (auditor-lane / Grant, not implementer silent-fix):**
- **PPN /7 couplings internally INCONSISTENT** — the `(9/7)` "controls light deflection" label gives 4.5× GR, contradicting the corpus's own `(2/7)`-derived 4GM/bc². W1 walk-back QUEUED-not-applied (`2026-06-05_gravity-ppn-coherence-result.md:10,84,159`). Relabel-not-delete; Grant picks frame-dragging-relabel vs bookkeeping-removal.
- **K=2G "emergent property" wording** at `appendices-overview.md:119` in tension with the PR#261 GR-imported ruling — needs a Rule-12 status-caveat.
- **The longitudinal scalar V is non-radiating in FREE propagation** (gauge, ∇·E=0) and re-engages CONFINED only at saturation Γ=−1. Auditor-correct phrasing: *"no free longitudinal RADIATION; the longitudinal scalar is confined (Γ=−1) standing strain"* — avoid implying the A1 core itself disperses (it binds as a cavity eigenmode; fork-b A1-only confined eigenmode EXISTS, GATE1 PASS, lossless).

---

## §2 — THE COUPLED DATA-FLOW DESIGN ("QED+GR = one engine")

> **CRITICAL PRE-DESIGN FLAG (flag-don't-fix, surfaced before the design — see §3 for the full firewall verdict).** The pipe described below — *"bulk emits S(A) → EM network reads ε₀·S"* — is a **NEW DESIGN PROPOSAL, not the existing HEAD data flow**, and it crosses an EM-vs-MECHANICAL domain fence that canon requires a transducer for. It is presented here as the *target architecture*; the gates it must clear are in §3 (the weakest-seam ledger) and §4 (standing work). Do not read §2 as a description of what runs today.

### 2.1 BULK / longitudinal / genesis sim — the OUTPUT side (source of the medium)

The bulk/A1 sector is the slow, large-scale background. Its job is to produce, at every lattice site `r`, the **local longitudinal strain operating point** `A(r)` (the A1 dilatation amplitude). From `A(r)` the single Axiom-4 kernel derives the medium:

```
bulk sim  →  A(r)                                          [the raw field]
S(A(r)) = (1 − A(r)²)^p   clipped [S_min, 1]               graded_vacuum_network.py:222-231
ε_eff(r) = ε₀ · S(A(r))                                    scale_invariant.py:164-195  [property, DROPS]
μ_eff(r) = μ₀ · S(A(r))                                    scale_invariant.py:198-221
Z_bulk(r), stiffness D(r) = 1/S(A)                         graded_vacuum_network.py:246-251
```

**Genesis / casting source — what it is NOT and what it is.** Self-formation is CLOSED-NEGATIVE (the free longitudinal A1 wave disperses). So the genesis source is NOT a free-running self-lock. The only legitimate sources of a confined core `A(r)` are:
- an **externally-seeded, POSITED saturated core** (`saturated_core_strain`, `graded_vacuum_network.py:234-242`, tagged "ASSUMED-not-derived, falsifier F8"), OR
- the **fork-b A1-only confined cavity eigenmode** that DOES exist (GATE1 PASS, core_frac=1.0, lossless).

The mass localizer is the **Γ=−1 boundary cavity** — not a winding-pin, not a self-trapped soliton. There is **no derived casting event** that grows the `A(r)` the pipe consumes; the bulk field must be *prescribed* or *eigen-solved*.

### 2.2 srs-3 / EM NETWORK — the INPUT side (QED running on the medium)

The QED sector = the saturable LC/TLM network on chiral srs z=3, reading the bulk-produced medium as its **per-cell L and C**:

```
INPUT to EM network, per srs cell at site r:
    C_cell(r) = ε_eff(r) · ℓ_node = ε₀·S(A(r)) · ℓ_node
    L_cell(r) = μ_eff(r) · ℓ_node = μ₀·S(A(r)) · ℓ_node
  ⇒ local TLM update uses Z_cell(r)=√(L/C), v_cell(r)=1/√(LC)=c_eff(r)
  ⇒ Bloch dispersion / scatter run on the GRADED net (spatially-varying L,C)
```

`ℓ_node` cancels in `Z_cell` (`z0-derivation.md:37,40` — pitch-independence), so `Z_EM` is set by the *ratio* `μ_eff/ε_eff` = the bulk strain field's signature on the EM channel. **The unification statement made concrete: the bulk strain `A(r)` is not a force on the EM field — it is the local reactance of the wires the EM field propagates on.** Gravity is a graded-index medium; the index is the bulk operating point; QED is the network running on that index.

**c_eff is channel-dependent (load-bearing — do NOT propagate a flat `c_eff`):**
- **Symmetric channel** (bulk / circulation): both ε and μ scale by the *same* S ⇒ `c_eff = c₀/S` (speeds up by 1/S) and `Z_EM = √(μ_eff/ε_eff) = Z₀ exactly` (index-captured, no EM reflection, `gw_propagation.py:160-185`).
- **Transverse-free channel** (the free photon probe): per VCA-R01 (`fdtd_3d.py:226-233`) μ is LINEAR (keys on circulating I/ω, not static bulk strain); only ε saturates ⇒ `c_eff = c₀·√S` and a genuine `Z_EM` modulation.

The interface contract MUST carry the channel tag, not a flat `c_eff`.

### 2.3 THE INTERFACE CONTRACT

**What crosses the boundary (the exact wire).** A single dimensionless field crosses, with a channel tag. The canonical primitive is **`S(A(r))`** (scale-free, α-free, ∈ (0,1]) — NOT the raw `A(r)`, NOT the dimensionful `ε_eff`:

| Quantity | Symbol | Produced | Consumed | Class |
|---|---|---|---|---|
| Saturation factor (PRIMARY wire) | `S(A(r))` | bulk sim → `graded_vacuum_network.py:222` | EM net cell L,C | derived (one kernel) |
| Bulk operating-point strain | `A(r)` / `ε₁₁(r)` | bulk sim | kernel input only | derived |
| Constitutive ε,μ | `ε₀S, μ₀S` | `scale_invariant.py:164-221` | TLM C,L per cell | derived; **property (drops)** |
| Bulk impedance / stiffness | `Z_bulk(r)`, `1/S` | `graded_vacuum_network.py:246-251` | shear/bulk channel | derived |
| Channel tag | {symmetric \| transverse-free} | — | selects c_eff law | **MUST be carried** |

**Why `S` and not `ε_eff`:** `S` is the scale-free, α-free, channel-agnostic primitive. `ε_eff=ε₀S` re-introduces the SI-substituted Class-B value and the property-vs-response trap (`ε₀S` drops, observable `C=C₀/S` diverges). Wiring `S` keeps the seam honest: the bulk emits a dimensionless modulation; the EM side multiplies its known `ε₀, μ₀`.

**At what scale — the multi-scale coupling.** Bulk: slow in time, large in space (`A(r)` varies over `r_s` / cavity radius ≫ ℓ_node) — the quasi-static varactor bias, re-evaluated rarely. EM: fast in time, ℓ_node in space — the photon sees `S(A(r))` as locally constant over its wavelength (adiabatic / WKB). **This is a scale-separated, adiabatic, frozen-medium coupling** — slow background, fast probe (the vacuum-engineer ledger). The architecture MUST enforce: snapshot the bulk field, run N fast EM steps against the frozen `S(A(r))`, re-snapshot. It MUST NOT co-evolve them at the same dt — co-evolution at dt→0 is exactly the convergence-engine pump that produced the keystone energize-LOCK negative.

**ONE-WAY or TWO-WAY.** ONE-WAY today, by construction, grep-confirmed: `gravity strain → S(A) → {ε_eff, μ_eff, Z, n(r), c_eff} → EM updates`. Zero hits in `src/ave` for any EM→bulk back-reaction (EM-stress→lattice, radiation-pressure→bulk, E-sources-V).
- The **only genuinely two-way** coupling in the engine is **A1↔ω H_couple** — but that is **bulk↔shear, NOT bulk↔EM.** The EM-transverse port is neither arm of `H_couple`.
- **The self-consistent GR loop — EM stress-energy sourcing the bulk — is UNWIRED.** "EM energy warps the vacuum" is not realized in code. It would be a NEW term: `T_μν^EM → source on A(r)`.

### 2.4 THE UNIFICATION STATEMENT (as built vs as designed)

**As designed (target):** Gravity = the bulk strain field `A(r)` whose Axiom-4 kernel `S(A(r))` sets the per-cell `L_cell=μ₀S·ℓ, C_cell=ε₀S·ℓ` of the srs-3 EM/LC network. QED = the saturable transverse TLM network running on that graded medium. The form is unified through the single kernel `S(A)`.

**As built (honest):** only the **one-way half** (gravity → EM medium) is realized, and even that runs through the *linear* `n=1+(2/7)ε₁₁` map analytically from `r_s`, **not** through `S(A)` of a running bulk-sim field. The **back-reaction loop**, the **explicit bulk-field → graded-network pipe**, and the **`n(r)↔1/S` sign reconciliation** are the missing physics. The engine today is a **test-field-on-fixed-background solver** (QED on a *prescribed* gravity well), not full self-consistent GR+QED.

---

## §3 — PRESSURE-TEST LEDGER

**Aggregate verdict across three independent lenses (coherence/firewall · replacement-honesty · weakest-seam): SOUND-WITH-GAPS.** The design's central facts are corpus-accurate; its central FLAG (sign conflict) is *real but mis-ranked and imprecisely located*; the *first* break is the absent back-reaction loop.

### 3.1 Coherence / firewall verdict

- **PASS** — the opposite-sign constitutive flag is verbatim-correct: saturation route `ε_eff=ε₀·S≤1` (ε DROPS, `scale_invariant.py:195`, docstring `:179`) vs gravity route `ε_eff=ε₀·n≥1` (ε RISES, `gw_propagation.py:137`, `n=1/(1−r_s/r)`). Two distinct functions in code.
- **PRECISION-FAIL to correct in the design's flag (load-bearing).** The design asserted *"There is NO S(A) kernel call in the gravity path."* **FALSE as stated.** The gravity module DOES call `saturation_factor` — `gw_propagation.py:293` (`S = saturation_factor(eps11, yield_limit=1.0)` inside `shear_wave_speed`, `c_shear=c·√S`). The correct, narrower statement: the **EM-transverse** gravity path (`refractive_index`/`epsilon_eff_schwarzschild`, `:84-157`) carries no S(A); the **SHEAR/GW** path does. The two "opposite-sign maps" are **not a single-channel contradiction** — they are **TWO DIFFERENT CHANNELS** (EM-transverse vs shear) driven by the **same** strain `ε₁₁=7GM/c²r`, read through two projections: `n=1+ν·ε₁₁` on EM (rises), `S=√(1−ε₁₁²)` on shear (collapses). **The design's "ASSERTED bridge n(r)≡1/S(A)" conflates the EM index with the shear-collapse factor.** Grant-adjudication-item-#1, as originally framed (single-channel sign conflict), is *partly an artifact of this conflation* and must be re-stated as a two-channel question before adjudication.
- **FLAG — the bulk→EM `ε₀·S` pipe does NOT exist in the operative solver and, as proposed, crosses a domain fence.** In `graded_vacuum_network.py` the S(A) kernel drives ONLY the bulk mechanical stiffness (`stiffness_profile:246-251`, `D=1/S`); EM enters ONLY as a separate **bare matched loss-port** at the outer boundary (`em_loss_port_mask:268`; docstring `:214-217`: *"a BARE matched loss-port (DEC-4), NOT a TKI transducer (avoids the units-bridge-Q hazard F4)"*). There is **no `ε_eff=ε₀·S` wire from the bulk solver into an EM constitutive param** anywhere in this solver. `H_couple` and the circulator are explicitly **Build-B — NOT here** (`:20,25,209`).
- **FAIL-as-written / FLAG-for-design — the EM-vs-MECHANICAL domain guard is engaged and not satisfied by a direct `ε₀·S` multiply.** `resonant-lc-solitons.md:129` (verbatim): *"EM↔mechanical coupling needs a TRANSDUCER, not a direct wire ... the TKI-transformer ... is itself status:proposed-not-ratified and carries the 'identity-by-translation, NOT a derivation' ceiling — FLAGGED, not asserted."* `vocabulary-register.md:430` already REVERSED a symmetric `μ_eff→Z_shear` direct-wire as FORBIDDEN. A direct multiply of A1's saturation state onto EM ε/μ is the same forbidden move. **The named-axis near-miss:** the prompt's `mass(A1)→charge(T2)` cross-wire is NOT the live violation (the flow targets ε/μ, the EM sector, not the T2/charge channel). The live leak is one register over: **bulk-A1 (MECHANICAL) → EM-ε/μ (ELECTRICAL)**, which needs the transducer.
- **FLAG — stiffening-vs-softening conflation in the reconciliation prose.** `engine-capability-map.md:65` flags the bulk **rarefaction/softening** pocket as *"a FOURTH object — NOT Γ=−1"*, distinct from the A1 **stiffening** wall (`c_eff→∞`). The design's *"gravity = bulk rarefaction ... mass-confinement = bulk saturation ... two ends of the SAME operating-point axis"* collapses an orthogonality the canon preserves. Countervailing cover: `:76` (INVARIANT-S2 Q1=B, Grant-ratified) says the split is *"IMPLEMENTATION, not fundamental"* and every node carries BOTH as **orthogonal reactances driven by the same S** — but that is orthogonal-reactances-on-one-S, **not** a single signed scalar axis with two "ends." Surface the `:65`-vs-`:76` tension to Grant; do not assert "two ends."
- **PASS** — units mis-scope is anticipated, not yet violated: only `Z_EM≡Z₀` is electrical (Ω); `Z_shear, Z_bulk` are mechanical/acoustic (ρ·speed, Pa·s/m). The design names the seam; it does not numerically equate the registers — contingent on the contract never multiplying across the unit boundary without the transducer.

### 3.2 The honest replacement ledger (vs QED+GR, symmetric-standard)

| | **EXCEEDS** (structural win SM/GR lacks) | **MATCHES** (consistency / reproduction) | **FALLS-SHORT** (open / imported) |
|---|---|---|---|
| **QED** | exact-integer charge `Link(∂Ω,F)∈ℤ` (topologically counted, no hypercharge-by-hand); no-renormalization / finite-by-construction (ℓ_node IS the UV regulator); real lossless isotropic photon (not a point particle) | `Z₀=376.73 Ω`, `c`, transverse vacuum response — all QED-peer; finiteness scoped QED-EQUIVALENT not AVE-distinct | per-mille/ppb predictions (g-2, Lamb shift, running couplings) NOT delivered; α IMPORTED (3 lift-routes closed-negative, echo clm-0ktpcn) |
| **GR** | M/Q/J universal no-hair (BH↔electron same mechanism); gravity-as-impedance-gradient (not geometric) | `n(r)=1+2GM/rc²` lensing/Shapiro/redshift = GR at O(GM/rc²) BY CONSTRUCTION; K=2G Einstein-elastic FORM | G=MIXED (form-derived/value-fitted, Chain B′ open); ρ_Λ ×1.54 (ρ_latent open); genesis CLOSED-NEGATIVE; **back-reaction loop ABSENT** |

**Symmetric-standard note (load-bearing, not a comedown):** *AVE imports α/G/m_e* is **peer-with-SM, NOT an AVE-specific weakness* — SM imports α, the Yukawas, Λ, and charge quantization equally un-derived. This is corpus-sanctioned (`_orchestration/2026-06-23_engine-derived-vs-constrained-ledger.md:46-50`, Grant-adjudicated). The object-level knife stays sharp: the **AVE-DISTINCT content lives ONLY in untested forward predictions** (OA sign-flip, GW-echo, E-route birefringence coefficient clm-pp3qwf ~1.93×10⁷×QED, α-invariance-under-gravity null) — and the design does NOT claim predictive parity.

**Lane / novelty note:** the corpus ALREADY carries this ledger (the 7-tier derived→constrained ranking, Grant-adjudicated 2026-06-23). Per closure-discipline-already-exists, this standing doc **re-indexes** that ledger and flags deltas since 2026-06-23 (the S3 DISPERSE-FALSIFIED reroute, the P1a/P1b validation, the (q·ℓ)⁴ demotion) — it does NOT mint a parallel ranking.

### 3.3 THE WEAKEST SEAM — where the engine breaks FIRST

**The TWO-WAY BACK-REACTION (the GR half) is the single weakest seam, and it breaks first and hardest.** Not the sign conflict — the sign conflict *cannot be exercised yet* because the two routes are never composed in the same call path (`graded_vacuum_network.py` imports neither `scale_invariant.epsilon_eff` nor `gw_propagation`; the gravity index lives standalone). A sign conflict between two functions never called in the same pipe is a *latent contract bug*, not the first break.

At HEAD the gravity sector is a **one-way, hand-prescribed graded-index map**: `refractive_index(r, r_s)` takes `r_s=2GM/c²` as external input (`gw_propagation.py:68,84`), and the strain is **back-computed by inverting the desired GR n(r)**: `eps_11 = (ratio/(1−ratio))/NU_VAC` (`gw_propagation.py:114-117`). So AVE-gravity is **GR-fitted through the index**, not sourced by any field. Grep for `stress_energy / back-react / T_munu` across `src/ave/gravity/` and `src/ave/solvers/` returns **ZERO** this turn. A field→index pipe with the index imposed by hand is **graded-index OPTICS, not a closed Einstein-equation replacement.**

> **STALE-CITATION CORRECTION (verify-before-cite).** The upstream weakest-seam analysis attributed the n(r)-inversion to `orbital_resonance.py:62-70`. **That module does not exist at HEAD** (`src/ave/gravity/` has `orbital_lc_damping.py`, `solar_impedance.py`, `lense_thirring.py`, etc., no `orbital_resonance.py`). The inversion it described is real but lives at **`gw_propagation.py:114-117`**. The substantive finding (gravity is prescribed, not sourced) STANDS on the real anchor + the zero-hit grep; only the module path was wrong. Relay corrected.

**Grant-adjudication item #0 (upstream of the design's sign-reconciliation item #1):** *Is there a back-reaction loop at all, or is gravity a prescribed boundary condition?*

**CONCRETE VALIDATE-OR-BREAK TEST for the GR-replacement claim:** build a minimal closed-loop fixed-point case — a single localized EM/bulk energy density ρ sourcing a geometry `n(ρ)` which feeds back as the medium that confines that same ρ — and require self-consistency: (a) the emitted geometry must equal `schwarzschild_radius(M_eff)` where `M_eff = ∫(energy density)/c²` to the claimed tolerance (coordinate-match check); (b) iterate to a fixed point. **PASS** = the Schwarzschild profile EMERGES from the field's own stress-energy (GR replacement is real). **BREAK** = it does not converge, or `M_eff` must be re-imposed by hand (then AVE-gravity is a GR-fitted graded-index analogue, the back-reaction is a narrative not a computation, and "QED+GR as one engine" is two disjoint subsystems sharing a vocabulary).

---

## §4 — STANDING WORK (what to BUILD / VALIDATE to realize the architecture)

Ordered by the §3 break-ranking (most-load-bearing first). Each item names its gate.

1. **[BACK-REACTION LOOP — the GR half, item #0]** Build the minimal closed-loop fixed-point test of §3.3. This is the make-or-break for the "replaces GR" claim. Until a `T_μν^EM → source(A(r))` term exists and converges to `schwarzschild_radius(M_eff)`, the engine is test-field-on-fixed-background and "QED+GR as one engine" is two disjoint subsystems sharing a vocabulary. **Gate:** self-consistent fixed point with M_eff emergent (not re-imposed).

2. **[SIGN/CHANNEL RECONCILIATION — Grant-item #1, RE-STATED]** Resolve, as a **two-channel** question (NOT a single-channel sign conflict): the EM-transverse index `n=1+(2/7)ε₁₁` (rises) and the shear-collapse factor `S=√(1−ε₁₁²)` (collapses) are two projections of the same strain `ε₁₁=7GM/c²r`. The design's `n(r)≡1/S` bridge conflates them and must be either derived or retired. Reconcile against the `:65`-vs-`:76` stiffening/softening tension (orthogonal-reactances-on-one-S, NOT "two ends of one axis"). **Gate:** Grant adjudication + a single documented strain→medium map per channel.

3. **[EXPLICIT BULK→EM PIPE — through the transducer, not a direct wire]** Build the module that takes a spatially-varying `A(r)` (prescribed or eigen-solved, since genesis is closed-negative) → `S(A(r))` snapshot → per-cell graded `{L_cell, C_cell}` → graded TLM scatter on srs-3, enforcing the adiabatic snapshot/N-fast-step/re-snapshot separation (NOT co-evolution at dt→0). **The cross-domain ε₀·S multiply MUST route through `def-tk1xfm` explicitly**, carrying its `status:proposed` + "identity-by-translation, NOT a derivation" ceiling on the interface contract — do NOT present the multiply as a derivation (resonant-lc-solitons.md:129; the 2026-06-24 vocabulary-register.md:430 reversal precedent). **Gate:** graded-medium EM run with energy-conservation certification + the transducer ceiling carried, not asserted.

4. **[GENESIS SOURCE — only as posited seed or eigenmode]** Since self-formation is CLOSED-NEGATIVE, supply the bulk `A(r)` field as either the POSITED `saturated_core_strain` (falsifier F8) or the fork-b A1-only confined cavity eigenmode (GATE1 PASS). **Gate:** the pipe consumes a *prescribed/eigen-solved* field — do NOT attempt to grow it (no derived casting event exists; re-running genesis is a re-litigated closed negative).

**Make-or-break seam to watch (the AVE-distinct content, all `experimental_solidity:null`):** the structural wins are real but peer-with-SM; the ONLY make-or-break AVE-distinct content is in **forward predictions**. The surviving near-term bankable QED-discriminator is the **E-route vacuum-birefringence COEFFICIENT** (clm-pp3qwf, ~1.93×10⁷×QED) — **NOT** the `(q·ℓ_node)⁴` dispersion, which was DEMOTED to slope-2 CHORD-CONDITIONAL on HEAD (`test_p1b_dispersion_gate.py:92`, commit f6ee2641; slope measured 1.9999, not 4; CONDITIONAL on the unproven weak-C no-zone-edge theorem gate wejkhvnfb). **Do not lean the gravity/lattice discriminator on `(q·ℓ)⁴`.** OA sign-flip (magnitude ~40 OOM over cosmic bound) and GW-echo (~4ms-in-tension) are DEMOTED/non-bankable.

**Doc-hygiene follow-ons (auditor-lane lands; implementer surfaces):**
- The `unified-engine-design-doctrine.md` §G:310 / §D:188 still list `(q·ℓ)⁴` as a clean derived "leak" — STALE (doctrine 07:52 predates demotion 09:22, same day). Needs a 🟡 Type-B demotion note mirroring clm-k4d4ph.
- `k4-bloch-dispersion-quartic.md` header lines 17,22 read "surviving forward prediction"/"CHORD" un-qualified while the body (`:91+`) carries the demotion — header-vs-body staleness.
- `electron-vacuum-state-synthesis.md:58` still cites `(qℓ_node)⁴` as "the only AVE-distinct piece" — stale vs HEAD.
- D1 production-net `eq_axiom_1.tex:37` (diamond) vs doctrine §E 2026-06-25 (srs) UNRECONCILED — engine runs ahead of canon; Grant adjudication item.

---

## KEY FILES (absolute)

- `/private/tmp/audit-electron/src/ave/solvers/graded_vacuum_network.py` — kernel `:222-231`, stiffness `:246-251`, posited core `:234-242`, EM loss-port `:268`, isolation eigensolver `:431-466`; H_couple/circulator OFF `:20,25,209`
- `/private/tmp/audit-electron/src/ave/axioms/scale_invariant.py` — constitutive `ε₀S/μ₀S` `:164-221`, property-vs-response caveat `:181-184`
- `/private/tmp/audit-electron/src/ave/gravity/gw_propagation.py` — gravity index route `:84-185` (linear `n=1+(2/7)ε₁₁`, NOT through `S(A)`); strain back-inverted from GR n(r) `:114-117`; shear-channel S(A) `:293` (the EM-vs-shear two-channel correction)
- `/private/tmp/audit-electron/src/ave/core/universal_operators.py` — `universal_refractive_index` `:1056,1075` (Op19 linear index)
- `/private/tmp/audit-electron/src/ave/facade/unified_engine.py` — EM net wiring `:184-265`, A1 cage `:270-301`, regimes `:72-80,130-131` (graded EM dormant), EXCLUSIONS `:24`
- `/private/tmp/audit-electron/src/ave/core/cross_sector_coupling.py` — the only two-way coupling, bulk↔shear NOT bulk↔EM, `:9-11,76-90`; trilinear CORRECTED-NEGATIVE `:130-141`
- `/private/tmp/audit-electron/src/ave/solvers/srs_cage_winding.py` — bulk A1 carrier on srs z=3; `compute_Q_link_srs:190-258`
- `/private/tmp/audit-electron/manuscript/ave-kb/common/engine-capability-map.md:65,76` — stiffening-vs-softening firewall + INVARIANT-S2 cover
- (canon firewall) `resonant-lc-solitons.md:129` (transducer-not-direct-wire); `vocabulary-register.md:430` (the reversed μ_eff→Z_shear precedent)
- (existing ledger to re-index) `/private/tmp/audit-electron/_orchestration/2026-06-23_engine-derived-vs-constrained-ledger.md`
