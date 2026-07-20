# THE PORT REGISTER (draft) — per-channel × per-port table for the graded-vacuum medium

**Date:** 2026-07-20
**Class:** RESEARCH-DOC DRAFT (register scaffold; **canon promotion is a routed, Grant-gated follow-on** — this doc lives in `research/`, edits no `manuscript/` or `manuscript/ave-kb/` leaf). Provenance-tags every row; mints no `clm-`; propagates to no KB/tex leaf. Companion: the Q1 hardening doc `research/2026-07-20_q1-pulsar-hardening.md` and the docket continuation (`_orchestration/2026-07-10_rulings-docket.md`, ENTRY 27).
**Provenance of the conceptual base:** Grant-fired 2026-07-20, verbatim `[sic]`: *"fire the port channel lane and continue it."* The port taxonomy below (the port/channel/valve distinctions, the DM-conflation resolution) is the **orchestrator's walk wording, ratified by the firing** — tagged as WALK-WORDING throughout, never as Grant verbatim. Every `[canon]` input was content-verified in this worktree at HEAD `64f1894d` (verify-before-cite, two-method: `grep -F` + direct read).
**Branch-state honesty (load-bearing).** Several rows cite content that lives on **open, unmerged PRs** (#749 ratification batch; #750 scalar-GW port; #751 J(ω)/arccos). Those cites are tagged `[branch:#NNN]` and state the branch content is **not-yet-canon**; the register does not treat branch content as landed. Fenced per the lane brief: **no edits to #748/#750/#751 branch files.**

---

## §0 — The taxonomy (walk-wording, ratified by the firing)

**A PORT** is an interface where a subsystem's energy ledger connects to modes *outside* it, characterized by the **impedance looking out**. A port is **RADIATIVE iff `Re(Z) > 0`** there, which requires BOTH:
- **(i) a propagating channel at that frequency** (band structure — a real-`k` mode must exist), AND
- **(ii) source coupling into it** (multipole content + impedance matching).

If either fails, the port is **REACTIVE** (`Re(Z)=0`; stores-and-returns) or **CLOSED**.

**Port-not-valve (Axiom-3 legality).** Ax3 forbids a *bulk resistor* (`eq_axiom_3.tex:24` `[canon]`: the medium "stores and returns energy but does not dissipate it… any apparent loss must be a boundary-radiation or mode-conversion channel, **never a bulk resistive one**"). Ports are legal because **port-loss = delivery-elsewhere** (the energy leaves as a propagating wave to the far field / a matched termination; reconvergence ≈ 0), NOT bulk dissipation. This is the `R_rad ≡ Z_0` "wave-making drag, a real port" statement (`common/substrate-native-terminology.md:47` `[canon]`).

**Channels are INHERENT; ports are EMERGENT or ENGINEERED.**
- **CHANNELS** are axiom-level: the four branches of the graded-vacuum medium (their speeds, gaps, band edges are fixed by the constitutive constants). A channel is a *standing capability of the medium*.
- **PORTS** are **emergent/configurational** (a multipole selection rule, a band-edge position, an impedance match, a boundary geometry, a source velocity) or **engineered** (an instrument's deliberate coupling termination). A port is *whether, here and now, this configuration actually delivers energy out through some channel*.

**The DM-conflation resolution (walk-wording).** The dark-matter halo = the **bulk channel's reactive NEAR-FIELD** (stores/loads, added-mass — shapes rotation curves), **NOT a port** (a port *drains*; the near-field *stores-and-returns*). Consequence: pulsar timing already polices any bulk *radiative* port (see Q1 row §3 and the companion hardening doc).

**Taxonomy foundation `[canon]`:** the K4 4-port amplitude space decomposes under `T_d` as `V_4port = A_1 ⊕ T_2` (`k4-port-irrep-decomposition.md:1,18-19` `[canon]`, `clm-j550uh`/`clm-9kd2t3`): `A_1` = common-mode scalar/longitudinal (dilatation, mass), `T_2` = traceless triplet (shear, the photon/GW). Every reflection/port statement carries a **channel subscript** under the three-impedance law (`bulk-impedance-at-saturation-boundary.md:10` `[canon]`).

---

## §1 — CHANNELS (inherent; axiom-level) — the four branches

Speeds/edges/gaps `[canon]` from the band-map (`research/2026-07-19_deep-space-band-map_derivation.md:52-67` merged via #741) + the "three speeds, do not fuse" table (`cosserat-mass-gap.md:120-132`) + the adjudicated arccos band model (`srs-band-structure.md:19,49,62`, `clm-bnd5rq`, gates PASS #604/#607). **★The #750 FLAG-A port-speed-vs-radiative-speed split is carried as its own COLUMN** for channel 3 — resolving the label confusion structurally rather than picking a side.

| # | Channel (sector) | Irrep | Impedance | Long-λ **PORT/impedance** speed | **RADIATIVE (far-field) speed** | Band model / edge | Gap | Provenance |
|---|---|---|---|---|---|---|---|---|
| 1 | **EM-transverse** (photon; `T₂` shear-EM, the transverse-`u` circulation) | `T₂` | `Z_EM = Z₀` | `c = √(G/ρ)` | `c` | gapless acoustic; arccos top `π√3·ω_C ≈ 5.44 ω_C` (cosine idealization `2c/ℓ_node`) | none | `clm-j550uh`, `band-map §2.2 ch1` `[canon]`; G2 relabel: photon = transverse-`u`, not micro-`ω` (`k4-port-irrep-decomposition.md` G2 note `[canon]`) |
| 2 | **Mechanical shear / GW** (`T₂` shear-G) | `T₂` | `Z_shear = ρ c_shear` | `c_shear = c` | `c` (the **observed GW** channel) | gapless acoustic; edge `2c/ℓ_node` | none | `einstein-field-equation.md:62-63,84` "GW are transverse shear modes"; `band-map §2.2 ch2` `[canon]` |
| 3 | **Bulk-longitudinal / dilatation** (`A₁` mass) | `A₁` | `Z_bulk = ρ c_bulk` | **`√2·c`** (`V_LONG`; `K=2G` magic-angle PORT/impedance mode) | **`√(10/3)·c ≈ 1.83c`** (isotropic-solid P-wave; the `4G/3` shear term cannot be dropped for a real far-field wave) | gapless acoustic; edge `2√2·c/ℓ_node` | none | `clm-uu1qbo`; **FLAG-A**: `constants.py:770-781` `[canon]` (verbatim: V_LONG = √2·c "drops 4G/3"; c_L = √(10/3)·c "the full compressional (P) wave"; "two distinct physical longitudinal modes, both retained"); `#750 §2.1` `[branch:#750]` |
| 4 | **Cosserat micro-rotation / wryness** (couple-stress; the `(2,3)` winding) | (micro-rot.) | couple-stress `γ`-grade | `c_κ = √2·c` | (gapped — see gap) | **GAPPED**: `ω² = c_κ²k² + m_ω²`; edge `2√2·c/ℓ_node` | **`m_ω = √(4G_c/I_ω) ~ c/ℓ_node`** (Yukawa reach `~ℓ_node`) | `clm-kmliqx`, `cosserat-mass-gap.md:59` `[canon]`; `master-equation.md:24` "Yukawa-screened" `[canon]` |

**Channel-row two-method receipts:** speeds cross-checked at (a) `cosserat-mass-gap.md:120-132` three-speeds table AND (b) `constants.py:758-781` (`G_VAC = ρc²`, `V_LONG = √(2G/ρ)`, the K=2G note). The `√2·c` vs `√(10/3)·c` FLAG-A split is confirmed in BOTH `constants.py:770-781` and `#750 §2.1`/`mond-hoop-stress.md:43`/`lc-electrodynamics.md:28` (the c_L-reconciliation Rule-12 notes). Band edges cross-checked at (a) band-map §2.1-2.2 and (b) `translation-circuit.md:154,353` (`f_max = c/(π ℓ_node)`).

**★FLAG-A structural resolution (the register's answer to the label confusion).** The corpus carries **two distinct longitudinal objects** on channel 3; the register splits them into two columns rather than "fixing" one:
- The **PORT/impedance speed `√2·c`** (`Z_bulk = ρc_bulk`) governs *reflection at a boundary* (saturation wall, TIR) and *reactive near-field storage* (the DM halo, §2 row 9). This is the speed the band-map channel-3 row and the three-impedance law inherited.
- The **RADIATIVE (far-field) speed `√(10/3)·c`** governs a *freely propagating longitudinal wave* (a plane compression shears the medium → the `4G/3` term is live). This is the speed a bulk **radiative port** (Q1 row) would use.
- **Both superluminal** ⇒ the causality/observability consequences are robust to the fork; only the exact flux prefactor moves (companion doc §1).
- **This split is load-bearing for Q1:** it means "leave the halo reactive (√2·c port) while asking whether the binary opens a radiative port (√(10/3)·c)" is *structurally two different modes* — Reading B does not need a single mechanism spanning both (companion doc §3).

---

## §2 — KNOWN PORTS (emergent/configurational or engineered)

Each row: **provenance** (axiom-forced / emergent-configurational / instrument-engineered), **radiative-vs-reactive**, **open/closed**, **ruling status + receipt**. Two-method verified. Branch-state cites tagged `[branch:#NNN]` (not-yet-canon).

| # | Port | Channel(s) | Provenance | Radiative / Reactive | Open / Closed | Ruling status + receipt (two-method) |
|---|---|---|---|---|---|---|
| P1 | **`R_rad ≡ Z₀` — EM radiative port** (SYSTEM-loss row; the vacuum's always-available far-field EM port for a matched, propagating, coupled multipole) | 1 (EM-`T₂`) | **axiom-forced** (`Z₀` is *the* vacuum EM impedance; radiation resistance = wave-making real port) | **RADIATIVE** (`Re(Z)=R_rad=Z₀>0`; port-not-valve — loss = delivery to the far field) | **OPEN** (this is *how* the vacuum radiates) | **CANONICAL.** `substrate-native-terminology.md:47` verbatim "radiation resistance `R_rad≡Z₀` (wave-making drag, a real port)" + `dark-wake-bemf-foc-synthesis.md:10-16` port taxonomy (R_rad / X_L near-field / back-EMF are three distinct port objects). Per-cycle value `Z₀/(4π)`: `theorem-3-1-q-factor.md:79` + `dama-matched-lc-coupling.md:80`. **Two-method:** both files. |
| P2 | **`Z_det` — detector / capture port** (`clm-ldmvwi`) | 1/2 (matched termination) | **instrument-engineered / emergent** (a detector is an engineered matched termination that Joule-extracts at a boundary node) | **RADIATIVE** (real port; the Born-rule *click* = work extracted at `Z_det`; FDT `⟨fₙ fₙ⟩ = 2k_B T Z_det δ`) | **OPEN** (configurational — a detector is placed) | **CANONICAL.** `clm-ldmvwi` Born-rule end-to-end chain, `ohmic-decoherence-born.md:5,40,48` (`Z_det` thermal-port impedance in the stochastic master vacuum eq). **Two-method:** frontmatter `claims:` line 5 + step-3 body line 48. |
| P3 | **X40 matched stubs** (the ring-closure transient's radiated remainder → matched real port) | 1 (EM-`T₂`, matched) | **emergent-configurational** (the X40 mint's `9/10` radiated remainder terminates into the matched real port; the `1/10` trapped fraction is mesh-geometry) | **RADIATIVE** (radiated `9/10` = T-even bond strain into the matched `R_rad`; trapped `1/10` = T-odd loop current, reactive) | **OPEN / real** | **RULED R4 2026-07-20 (ratified walk).** Decision 2 = **2a**: radiated remainder → **matched real port `R_rad≡Z₀`** (Ax3-legal, not a bulk valve); cost-of-genesis ledger well-defined; **trapped fraction = mesh-geometry, NOT `m_e`** (mass stays A1/definitional); keystone fence rides. `[branch:#749]` ENTRY 27 R4 + `x40-ring-closure-transient_result.md:328-354` (merged, `[canon]`). **Two-method:** #749 docket entry + the result-doc line range. |
| P4 | **Electron `Γ = −1` wall** (deliberately closed) | 2/3 (shear/bulk) | **axiom-forced / topological** (the electron is a `0₁` unknot confined by a `Γ=−1` total-internal-reflection boundary at `ℓ_node`) | **REACTIVE-reflecting** (perfect reflector; energy returns; `Z→0 ⇒ Γ=−1`) | **CLOSED** (by design — confinement) | **CANONICAL.** `electron-bh-isomorphism.md:10` (`Γ=−1` TIR boundary) + `bulk-impedance-at-saturation-boundary.md:73,78` (`Z_bulk→0 ⇒ Γ_bulk=−1` at the TIR/cavitation wall; *opposite EOS branch* from the BH melt). **Two-method:** two leaves, channel-subscripted. |
| P5 | **Casimir below-cutoff** (closed by band position) | 1 (EM-`T₂`) | **emergent-configurational** (band position — the mode sits at/above the lattice cutoff `f_max = c/(π ℓ_node)`; condition (i) *no propagating channel* fails below-cutoff) | **REACTIVE / closed** (zero group velocity at the edge; a standing mode, does not propagate away) | **CLOSED** (band position) | **CANONICAL.** `translation-circuit.md:154,353` (`f_max = c/(π ℓ_node)`, `ω_max = 2c/ℓ_node`) recovered as the `k=π/ℓ_node` corner of the band, `v_g→0` (band-map §2.1). **Two-method:** translation-circuit + band-map §2.1. |
| P6 | **Cherenkov / Mach threshold ports** (closed below `v_crit`) | 1-3 (per channel) | **emergent-configurational** (band position + source velocity — a *steady-drift* radiative port opens only when `v > v_crit = v_{p,min}`) | **RADIATIVE when open / REACTIVE (added-mass) below threshold** | **CLOSED below `v_crit`** (deep-space matter doubly protected: `v~10⁻⁴c` AND bandlimited) | **band-map §3.3** `v_crit = (2/π)c_ch ≈ 0.637 c_ch` (**cosine-branch**) → **#751 correction** `v_{p,min}/c₀ = 0.80` (srs 3D arccos) / **`1.0`** (1D-chain arccos, *no* onset below `c`); the cosine `2/π` is a **branch artifact** and does NOT survive the model switch. `[branch:#751]` §9. Per-channel: EM/shear `≈0.80c`; bulk `≈0.80·√2c ≈ 1.13c`. **★NUANCE (load-bearing for Q1):** this threshold is for a **STEADY-drift source dragging a near-field**; an **accelerated multipole** (a binary at `2Ω`) has **no velocity threshold** into a *gapless* channel — so `v_crit` does NOT close the Q1 radiative port. **Two-method:** band-map §3.3 + #751 §9 arccos table. |
| P7 | **F6 scalar collar** (instrument-engineered; piston-geometry) | 3 (A1 dilatation-port projection) | **instrument-engineered** (the F6 bath-meter collar = a fixed shell of active lattice sites, Caldeira-Leggett bilinear, scalar dilatation-port read `q = Σ mean_p V_inc`) | **REACTIVE when bath-coupled (stores-returns) / RADIATIVE only under a deliberate lossy `Re(Z)` friction-plant termination** | **instrument-class** (a coarse acknowledged port) | **RULED R3 2026-07-20 (ratified walk).** The real T2 sink couples as a **PHASED ARRAY** (many independent local contacts, statically-random per-contact phases) — *composing with, not contradicting* #734's "effectively-constant" aggregate (**piston = aggregate; array = port geometry**); #734 structural-inexpressibility **rescopes to instrument-class**; phase-carrying build **LICENSED but PARKED**. `[branch:#749]` ENTRY 27 R3 + `f6-bath-meter_CHARTER.md:39` (merged, `[canon]`). **Two-method:** #749 docket R3 + charter §coupling. |
| P8 | **J(ω) scope-split** (a register ROW-CLASS, not a single port) | 3/4 (z=3 srs bath) | **emergent-configurational, scope-dependent** (the same physics is port-closed or port-open depending on the sampled scope) | **0D cell = REACTIVE (recurs, Poincaré-bounded) / ∞-lattice = "RADIATIVE" (drains via Op3 transduction — still Ax3-lossless microscopically, not a resistor)** | **0D = port-CLOSED config; ∞-lattice = port-OPEN config** | **`[branch:#751]`** GLE scope-split (`jomega-derivation_result.md` §4): 0D few-mode cell recovers **70-95% `E_S`** (reactive return); dense/∞-lattice bath drains to **0-10%** (transduction). This row-class formalizes "port-open vs port-closed is a *scope* statement, not a property of the channel." **Two-method:** #751 §4 result table + §c-scope summary. |
| P9 | **DM-halo NEAR-FIELD** (explicitly **NOT-A-PORT**) | 3 (A1 bulk `√2·c` reactive) | **axiom-forced reactive storage** (the halo = the bulk channel's reactive near-field; added-mass; d'Alembert zero-steady-drag) | **REACTIVE (stores/loads; shapes flat rotation curves without loss)** | **NOT-A-PORT** (a port *drains*; this *stores-and-returns*) | **RULED (deep-space reactive-bulk arc).** `deep-space-reactive-bulk-walk_RECORD.md:54,68` (added-mass/d'Alembert; the **dark-matter added-mass reading survives = reactive**; the *dissipative* stall corollary demoted, `clm-h55fy1` flipped). This IS the DM-conflation resolution. **Two-method:** walk-record §54 (mechanism) + §68 (KEEP-BOTH table "what survives = reactive"). |

---

## §3 — ★Q1: THE FIRST EXPLICITLY-OPEN ROW

| # | Port | Channel | Provenance | Radiative / Reactive | Open / Closed | Ruling status + receipt |
|---|---|---|---|---|---|---|
| **Q1** | **A1 bulk channel — far-field radiative port for gravitating sources** | 3 (A1 bulk; radiative speed `√(10/3)·c` per FLAG-A) | **the load-bearing UNFORCED CHOICE** (band-map channel 3 is a *gapless propagating* branch — does a mass quadrupole open an *independent far-field radiative port* into it?) | **UNRULED — Reading-dependent** | **★UNRULED (the register's first explicitly-OPEN row)** | **UNRULED — Grant/auditor sector-ownership adjudication** (FLAG-1 / band-map D5). `[branch:#750]` frames it; companion `research/2026-07-20_q1-pulsar-hardening.md` hardens it against pulsar timing. |

**Reading A (independent elastic radiative DOF).** The A1/bulk-dilatation sector radiates like any elastic solid's longitudinal channel: monopole + dipole killed by conservation, but the **quadrupole radiates** (same nonzero rotating mass quadrupole as the T2/GW; no conservation law left to kill it — `#750 §3.3`). With an O(1) coupling (`K=2G`, no `1/ω_BD` suppression) the predicted admixture is **large** ⇒ **kill-class**, EXCLUDED. This is the elastic-medium *default*.

**Reading B (constrained / near-field-reactive-only, GR-like).** The longitudinal/scalar sector is *constrained* (pure-gauge, as GR's scalar metric parts) or *reactive-near-field-only* (the DM-halo mode, P9) ⇒ **no scalar-GW**, UNTOUCHED — but the corpus then **owes a mechanism** for why a mode that propagates freely at `√(10/3)·c` in its linear passband does not radiate from a strong quadrupolar source.

**Register verdict:** neither reading is forced by current canon ⇒ **the row stays OPEN**. The companion hardening doc (Deliverable 2) sharpens the consequence: under Reading A the extra flux fraction `F_bulk/F_shear ≈ 0.03–0.12` is **EXCLUDED at 9–110σ by Hulse-Taylor and by 100–1400× the double-pulsar bound** — a kill-class result to bank if Reading A is ruled; if Reading B is ruled, a suppression-derivation lane is owed. **Decision is Grant's.**

---

## §4 — PROVENANCE LEDGER + row count + rows-not-provenanced

**Register row count = 14** (4 channel rows §1 + 9 port rows §2 + 1 open Q1 row §3).

**Provenance class tally:**
- **axiom-forced / inherent:** channels 1-4; ports P1 (`R_rad≡Z₀`), P4 (`Γ=−1` wall), P9 (DM near-field NOT-A-PORT).
- **emergent-configurational:** P3 (X40 stubs), P5 (Casimir cutoff), P6 (Cherenkov/Mach), P8 (J(ω) scope-split), Q1 (the unforced fork).
- **instrument-engineered:** P2 (`Z_det`), P7 (F6 collar).

**Radiative / reactive tally:** RADIATIVE-open = P1, P2, P3, (P6-when-`v>v_crit`); REACTIVE/closed = P4, P5, P8-0D, P9, (P6-below-threshold); scope-dependent = P8; instrument-class = P7; **UNRULED = Q1**.

**Branch-state cites (not-yet-canon; flagged honestly):**
- P3, P7 receipts cite **#749** (ratification batch) docket ENTRY 27 R3/R4 — *ratified-walk content on an unmerged PR*. The underlying result-docs (`x40-ring-closure-transient_result.md`, `f6-bath-meter_CHARTER.md`) ARE merged `[canon]`; the *rulings* are branch-state.
- P6 arccos correction (`0.80`/`1.0` vs cosine `2/π`) cites **#751** — unmerged.
- P8 (J(ω) scope-split) cites **#751** — unmerged.
- Q1 framing cites **#750** — unmerged.

**Rows I could NOT provenance: NONE.** Every row is provenance-tagged to a content-verified `[canon]` leaf or an honestly-flagged `[branch:#NNN]` source. The honest caveat is the branch-state dependence of P3/P6/P7/P8/Q1 (five rows lean on unmerged PRs), NOT an un-provenanced row.

**Contradictions surfaced (flag-don't-fix; see companion doc §4 for the load-bearing one):**
- **FLAG-A** (channel 3 speed label): the band-map channel-3 row labels the bulk `√2·c` (the PORT/impedance speed); the *radiative* far-field longitudinal wave is the P-wave `√(10/3)·c` (`constants.py:770-781`). The register resolves this **structurally** (two columns), does not edit the band-map leaf (fence). Owed: an auditor-lane band-map channel-3 speed-label reconciliation.
- **The `08_gravitational_waves.tex` warningbox** (unresolved channel attribution): the Hulse-Taylor `Ṗ_b` step-3 attributes the radiated power to the *bulk / longitudinal* channel, while the KB canon assigns GW to the *transverse shear* channel. This is **exactly the Q1 fork surfacing inside the existing manuscript** — carried to the companion doc §4 as the load-bearing corpus contradiction. Not fixed here (fence).

**Canon-promotion routing (Grant-gated, NOT executed here):** if Grant greenlights, the register promotes to a canonical leaf (candidate home: a `common/` port-register discipline leaf, or `vol9` datasheet chapter) — a **separate session**, auditor-landed, after the #749/#750/#751 branches merge (so the branch-state cites become `[canon]`). This draft mints nothing and edits no leaf.

---

> **Register-draft provenance.** Fired by Grant 2026-07-20 (`"fire the port channel lane and continue it"` `[sic]`). Taxonomy = orchestrator's walk-wording ratified by the firing (tagged throughout). All `[canon]` citations content-verified two-method at HEAD `64f1894d`; `[branch:#NNN]` cites flagged as not-yet-canon. Mints no `clm-`; propagates to no leaf. Companion: `research/2026-07-20_q1-pulsar-hardening.md`; docket ENTRY 27.
