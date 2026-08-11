[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Register/discipline leaf — the per-channel × per-port map of the graded-vacuum medium (which configurations actually deliver energy out through which of the four channels, and by what provenance). Consolidates already-canonical channel/port/impedance content into one taxonomy; the port/channel/valve distinctions and the DM-conflation resolution are the orchestrator's WALK-WORDING ratified by the 2026-07-20 firing (tagged throughout, never Grant-verbatim), asserting no independent derivation. Mints no new physical claim; every row is provenance-tagged to a canonical leaf or an honestly-flagged branch source. Q1 is a RULED row — REVERTED 2026-07-20 to Reading-A-live: the make-or-break mechanical common-mode derivation returned NONE-DERIVES (#761 merged @ caa51c17), firing the row's own clause, so the RULED-CONDITIONAL Reading-B reverts and the independent-radiative-port exclusion is live against the framework (was: explicitly-OPEN, adjudication-pending)."
path-stable: "the canonical port-register discipline leaf — the per-channel × per-port map; referenced from engine-capability-map.md (3-channel-coupling DOF) and translation-circuit.md (A1/T2 ↔ P/S means-test row). Promoted from research/2026-07-20_port-register_draft.md (merged #753) 2026-07-20."
-->

# The Port Register — per-channel × per-port map of the graded-vacuum medium

This leaf answers one question for the four-branch graded-vacuum medium: **whether, here and now, a given configuration actually delivers energy out through some channel** — and, if so, whether that delivery is radiative (a real port, $\mathrm{Re}(Z) > 0$) or reactive (stores-and-returns), and by what provenance (axiom-forced / emergent-configurational / instrument-engineered). It consolidates already-canonical channel, port, and three-impedance content into one map. It mints no new physical claim.

> **[Resultbox]** *Classification — register consolidation (WALK-WORDING, ratified by the firing; NOT emergence)*
>
> Fired by Grant 2026-07-20 (verbatim `[sic]`: *"fire the port channel lane and continue it"*; the canon promotion satisfied by *"lets do it"* 2026-07-20). The **taxonomy below** (the port/channel/valve distinctions, the DM-conflation resolution, the FLAG-A speed split carried as a column) is the **orchestrator's walk wording, ratified by the firing** — tagged as walk-wording throughout, **never** as Grant verbatim. `consistency-vs-emergence`: this leaf is a **CONSISTENCY-class consolidation** — it re-organizes canonical sub-claims into a coherent framing and adds no new substrate-mechanism content beyond the cited axioms/leaves. Companion research docs (preserved, KEEP-BOTH): `research/2026-07-20_port-register_draft.md` (the draft, merged #753) and `research/2026-07-20_q1-pulsar-hardening.md` (the Q1 hardening + the seismology external anchor).

---

## §0 — The taxonomy (walk-wording, ratified by the firing)

**A PORT** is an interface where a subsystem's energy ledger connects to modes *outside* it, characterized by the **impedance looking out**. A port is **RADIATIVE iff $\mathrm{Re}(Z) > 0$** there, which requires BOTH:

- **(i) a propagating channel at that frequency** (band structure — a real-$k$ mode must exist), AND
- **(ii) source coupling into it** (multipole content + impedance matching).

If either fails, the port is **REACTIVE** ($\mathrm{Re}(Z) = 0$; stores-and-returns) or **CLOSED**.

**Port-not-valve (Axiom-3 legality).** Axiom 3 forbids a *bulk resistor* (`eq_axiom_3.tex:24` `[canon]`: the medium "stores and returns energy but does not dissipate it… any apparent loss must be a boundary-radiation or mode-conversion channel, **never a bulk resistive one**"). Ports are legal because **port-loss = delivery-elsewhere** (the energy leaves as a propagating wave to the far field / a matched termination; reconvergence $\approx 0$), NOT bulk dissipation. This is the $R_{rad} \equiv Z_0$ "wave-making drag, a real port" statement ([`substrate-native-terminology.md`](substrate-native-terminology.md):47 `[canon]`).

**Channels are INHERENT; ports are EMERGENT or ENGINEERED.**

- **CHANNELS** are axiom-level: the four branches of the graded-vacuum medium (their speeds, gaps, band edges fixed by the constitutive constants). A channel is a *standing capability of the medium*.
- **PORTS** are **emergent/configurational** (a multipole selection rule, a band-edge position, an impedance match, a boundary geometry, a source velocity) or **engineered** (an instrument's deliberate coupling termination). A port is *whether, here and now, this configuration actually delivers energy out through some channel*.

**The DM-conflation resolution (walk-wording).** The dark-matter halo $=$ the **bulk channel's reactive NEAR-FIELD** (stores/loads, added-mass — shapes rotation curves), **NOT a port** (a port *drains*; the near-field *stores-and-returns*). Consequence: pulsar timing already polices any bulk *radiative* port (see the Q1 row §3 and the companion hardening doc).

**Taxonomy foundation `[canon]`.** The K4 4-port amplitude space decomposes under $T_d$ as $V_{\text{4-port}} = A_1 \oplus T_2$ ([`k4-port-irrep-decomposition.md`](../vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) `[canon]`, `clm-j550uh`/`clm-9kd2t3`): $A_1$ $=$ common-mode scalar/longitudinal (dilatation, mass), $T_2$ $=$ traceless triplet (shear, the photon/GW). Every reflection/port statement carries a **channel subscript** under the three-impedance law ([`bulk-impedance-at-saturation-boundary.md`](../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md):10 `[canon]`).

---

## §1 — CHANNELS (inherent; axiom-level) — the four branches

Speeds / edges / gaps `[canon]` from the band-map derivation (`research/2026-07-19_deep-space-band-map_derivation.md`:52–67, merged via #741) + the "three speeds, do not fuse" table ([`cosserat-mass-gap.md`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md):120–132) + the adjudicated arccos band model ([`srs-band-structure.md`](../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md):19,49,62, `clm-bnd5rq`, gates PASS #604/#607). **★The FLAG-A port-speed-vs-radiative-speed split is carried as its own COLUMN** for channel 3 — resolving the label confusion structurally rather than picking a side.

| # | Channel (sector) | Irrep | Impedance | Long-λ **PORT/impedance** speed | **RADIATIVE (far-field) speed** | Band model / edge | Gap | Provenance |
|---|---|---|---|---|---|---|---|---|
| 1 | **EM-transverse** (photon; $T_2$ shear-EM, the transverse-$u$ circulation) | $T_2$ | $Z_{EM} = Z_0$ | $c = \sqrt{G/\rho}$ | $c$ | gapless acoustic; arccos top $\pi\sqrt3\,\omega_C \approx 5.44\,\omega_C$ | none | `clm-j550uh`, band-map §2.2 ch1 `[canon]`; G2 relabel: photon $=$ transverse-$u$, not micro-$\omega$ ([`k4-port-irrep-decomposition.md`](../vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) G2 note `[canon]`) |
| 2 | **Mechanical shear / GW** ($T_2$ shear-G) | $T_2$ | $Z_{shear} = \rho\,c_{shear}$ | $c_{shear} = c$ | $c$ (the **observed GW** channel) | gapless acoustic; edge $2c/\ell_{node}$ | none | [`einstein-field-equation.md`](../vol3/gravity/ch02-general-relativity/einstein-field-equation.md):62–63,84 "GW are transverse shear modes"; band-map §2.2 ch2 `[canon]` |
| 3 | **Bulk-longitudinal / dilatation** ($A_1$ mass) | $A_1$ | $Z_{bulk} = \rho\,c_{bulk}$ | **$\sqrt2\,c$** ($V_{LONG}$; $K=2G$ magic-angle PORT/impedance mode) | **$\sqrt{10/3}\,c \approx 1.83c$** (isotropic-solid P-wave; the $4G/3$ shear term cannot be dropped for a real far-field wave) | gapless acoustic; edge $2\sqrt2\,c/\ell_{node}$ | none | `clm-uu1qbo`; **FLAG-A**: `constants.py:770–781` `[canon]` (verbatim: $V_{LONG}=\sqrt2\,c$ "drops $4G/3$"; $c_L=\sqrt{10/3}\,c$ "the full compressional (P) wave"; "two distinct physical longitudinal modes, both retained"); confirmed [`cosserat-mass-gap.md`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md):13 `[canon]`; `#750 §2.1` `[canon, #750 merged 2026-07-20]` (cross-cite, off-main) 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |
| 4 | **Cosserat micro-rotation / wryness** (couple-stress; the $(2,3)$ winding) | (micro-rot.) | couple-stress $\gamma$-grade | $c_\kappa = \sqrt2\,c$ | (gapped — see gap) | **GAPPED**: $\omega^2 = c_\kappa^2 k^2 + m_\omega^2$; edge $2\sqrt2\,c/\ell_{node}$ | **$m_\omega = \sqrt{4G_c/I_\omega} \sim c/\ell_{node}$** (Yukawa reach $\sim\ell_{node}$) | `clm-kmliqx`, [`cosserat-mass-gap.md`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md):59 `[canon]`; [`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):24 "Yukawa-screened" `[canon]` |

**Channel-row two-method receipts.** Speeds cross-checked at (a) [`cosserat-mass-gap.md`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md):120–132 (three-speeds table) AND (b) `constants.py:758–781` ($G_{VAC}=\rho c^2$, $V_{LONG}=\sqrt{2G/\rho}$, the $K=2G$ note). The $\sqrt2\,c$ vs $\sqrt{10/3}\,c$ FLAG-A split is confirmed in BOTH `constants.py:770–781` AND `cosserat-mass-gap.md:132` (the "FOURTH speed" P-wave guard). Band edges cross-checked at (a) band-map §2.1–2.2 and (b) [`translation-circuit.md`](translation-tables/translation-circuit.md):154,353 ($f_{max}=c/(\pi\ell_{node})$).

**★FLAG-A structural resolution (the register's answer to the label confusion).** The corpus carries **two distinct longitudinal objects** on channel 3; the register splits them into two columns rather than "fixing" one:

- The **PORT/impedance speed $\sqrt2\,c$** ($Z_{bulk}=\rho c_{bulk}$) governs *reflection at a boundary* (saturation wall, TIR) and *reactive near-field storage* (the DM halo, §2 row P9). This is the speed the band-map channel-3 row and the three-impedance law inherited.
- The **RADIATIVE (far-field) speed $\sqrt{10/3}\,c$** governs a *freely propagating longitudinal wave* (a plane compression shears the medium → the $4G/3$ term is live). This is the speed a bulk **radiative port** (Q1 row) would use.
- **Both superluminal** ⇒ the causality/observability consequences are robust to the fork; only the exact flux prefactor moves (companion doc §1).
- **This split is load-bearing for Q1:** "leave the halo reactive ($\sqrt2\,c$ port) while asking whether the binary opens a radiative port ($\sqrt{10/3}\,c$)" is *structurally two different modes* — Reading B does not need a single mechanism spanning both (companion doc §3).

---

## §2 — KNOWN PORTS (emergent/configurational or engineered)

Each row: **provenance** (axiom-forced / emergent-configurational / instrument-engineered), **radiative-vs-reactive**, **open/closed**, **ruling status + receipt**. Two-method verified against current main at build. Branch-state cites tagged `[branch:#NNN]` (not-yet-canon; off-main).

| # | Port | Channel(s) | Provenance | Radiative / Reactive | Open / Closed | Ruling status + receipt (two-method) |
|---|---|---|---|---|---|---|
| P1 | **$R_{rad} \equiv Z_0$ — EM radiative port** (SYSTEM-loss row; the vacuum's always-available far-field EM port for a matched, propagating, coupled multipole) | 1 (EM-$T_2$) | **axiom-forced** ($Z_0$ is *the* vacuum EM impedance; radiation resistance $=$ wave-making real port) | **RADIATIVE** ($\mathrm{Re}(Z)=R_{rad}=Z_0>0$; port-not-valve — loss $=$ delivery to the far field) | **OPEN** (this is *how* the vacuum radiates) | **CANONICAL.** [`substrate-native-terminology.md`](substrate-native-terminology.md):47 verbatim "radiation resistance $R_{rad}\equiv Z_0$ (wave-making drag, a real port)" + [`dark-wake-bemf-foc-synthesis.md`](dark-wake-bemf-foc-synthesis.md):1–4 port taxonomy ($R_{rad}$ / $X_L$ near-field / back-EMF are three distinct port objects). Per-cycle value $Z_0/(4\pi)$: [`theorem-3-1-q-factor.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):79 + [`dama-matched-lc-coupling.md`](../vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md):80. **Two-method:** both files. |
| P2 | **$Z_{det}$ — detector / capture port** (`clm-ldmvwi`) | 1/2 (matched termination) | **instrument-engineered / emergent** (a detector is an engineered matched termination that Joule-extracts at a boundary node) | **RADIATIVE** (real port; the Born-rule *click* $=$ work extracted at $Z_{det}$; FDT $\langle f_n f_n\rangle = 2k_B T Z_{det}\,\delta$) | **OPEN** (configurational — a detector is placed) | **CANONICAL.** `clm-ldmvwi` Born-rule end-to-end chain, [`ohmic-decoherence-born.md`](../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md):5,40,48 ($Z_{det}$ thermal-port impedance in the stochastic master vacuum eq). **Two-method:** frontmatter `claims:` line 5 + step-3 body line 48. |
| P3 | **X40 matched stubs** (the ring-closure transient's radiated remainder → matched real port) | 1 (EM-$T_2$, matched) | **emergent-configurational** (the X40 mint's $9/10$ radiated remainder terminates into the matched real port; the $1/10$ trapped fraction is mesh-geometry) | **RADIATIVE** (radiated $9/10 =$ T-even bond strain into the matched $R_{rad}$; trapped $1/10 =$ T-odd loop current, reactive) | **OPEN / real** | **RULED R4 2026-07-20 (ratified walk).** Decision 2 $=$ **2a**: radiated remainder → **matched real port $R_{rad}\equiv Z_0$** (Ax3-legal, not a bulk valve); cost-of-genesis ledger well-defined; **trapped fraction $=$ mesh-geometry, NOT $m_e$** (mass stays A1/definitional); keystone fence rides. `[canon, #749 merged 2026-07-20]` docket ENTRY 27 R4 + `research/2026-07-10_x40-ring-closure-transient_result.md:328–354`. **Two-method:** #749 docket entry + the result-doc line range. |
| P4 | **Electron $\Gamma = -1$ wall** (deliberately closed) | 2/3 (shear/bulk) | **axiom-forced / topological** (the electron is a $0_1$ unknot confined by a $\Gamma=-1$ total-internal-reflection boundary at $\ell_{node}$) | **REACTIVE-reflecting** (perfect reflector; energy returns; $Z\to0 \Rightarrow \Gamma=-1$) | **CLOSED** (by design — confinement) | **CANONICAL.** [`electron-bh-isomorphism.md`](../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md):10 ($\Gamma=-1$ TIR boundary) + [`bulk-impedance-at-saturation-boundary.md`](../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md):76,81 ($Z_{bulk}\to0 \Rightarrow \Gamma_{bulk}=-1$ at the TIR/cavitation wall; *opposite EOS branch* from the BH melt). **Two-method:** two leaves, channel-subscripted. |
| P5 | **Casimir below-cutoff** (closed by band position) | 1 (EM-$T_2$) | **emergent-configurational** (band position — the mode sits at/above the lattice cutoff $f_{max}=c/(\pi\ell_{node})$; condition (i) *no propagating channel* fails below-cutoff) | **REACTIVE / closed** (zero group velocity at the edge; a standing mode, does not propagate away) | **CLOSED** (band position) | **CANONICAL.** [`translation-circuit.md`](translation-tables/translation-circuit.md):154,353 ($f_{max}=c/(\pi\ell_{node})$, $\omega_{max}=2c/\ell_{node}$) recovered as the $k=\pi/\ell_{node}$ corner of the band, $v_g\to0$ (band-map §2.1). **Two-method:** translation-circuit + band-map §2.1. |
| P6 | **Cherenkov / Mach threshold ports** (closed below $v_{crit}$) | 1–3 (per channel) | **emergent-configurational** (band position + source velocity — a *steady-drift* radiative port opens only when $v > v_{crit} = v_{p,min}$) | **RADIATIVE when open / REACTIVE (added-mass) below threshold** | **CLOSED below $v_{crit}$** (deep-space matter doubly protected: $v\sim10^{-4}c$ AND bandlimited) | **CANONICAL (#751 merged 2026-07-20).** band-map §3.3 $v_{crit}=(2/\pi)c_{ch}\approx0.637\,c_{ch}$ (**cosine-branch**) → **#751 §9 arccos correction** `v_{p,min}/c_0 = 0.80` (srs 3D) / **exactly `1.0`** (1D-chain, *no* onset below $c$); the cosine $2/\pi$ is a **branch artifact** and does NOT survive the model switch (`research/2026-07-20_jomega-derivation_result.md:194–204`, `[canon]`). Per-channel (arccos, by $\sqrt2$ scaling for bulk): EM/shear $\approx0.80c$; bulk $\approx0.80\sqrt2\,c\approx1.13c$. **★NUANCE (load-bearing for Q1):** this threshold is for a **STEADY-drift source dragging a near-field**; an **accelerated multipole** (a binary at $2\Omega$) has **no velocity threshold** into a *gapless* channel — so $v_{crit}$ does NOT close the Q1 radiative port. **Two-method:** band-map §3.3 + #751 §9 arccos table (both merged). 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |
| P7 | **F6 scalar collar** (instrument-engineered; piston-geometry) | 3 (A1 dilatation-port projection) | **instrument-engineered** (the F6 bath-meter collar $=$ a fixed shell of active lattice sites, Caldeira–Leggett bilinear, scalar dilatation-port read $q=\Sigma\,\mathrm{mean}_p V_{inc}$) | **REACTIVE when bath-coupled (stores-returns) / RADIATIVE only under a deliberate lossy $\mathrm{Re}(Z)$ friction-plant termination** | **instrument-class** (a coarse acknowledged port) | **RULED R3 2026-07-20 (ratified walk).** The real T2 sink couples as a **PHASED ARRAY** (many independent local contacts, statically-random per-contact phases) — *composing with, not contradicting* #734's "effectively-constant" aggregate (**piston $=$ aggregate; array $=$ port geometry**); #734 structural-inexpressibility **rescopes to instrument-class**; phase-carrying build **LICENSED but PARKED**. `[canon, #749 merged 2026-07-20]` docket ENTRY 27 R3 + `research/2026-07-16_f6-bath-meter_CHARTER.md:39`. **Two-method:** #749 docket R3 + charter §coupling. |
| P8 | **J(ω) scope-split** (a register ROW-CLASS, not a single port) | 3/4 (z=3 srs bath) | **emergent-configurational, scope-dependent** (the same physics is port-closed or port-open depending on the sampled scope) | **0D cell $\to$ REACTIVE-leaning (recurs, returns within the window) / ∞-lattice $\to$ "RADIATIVE" only for the super-Ohmic (C2) coupling model (drains via Op3 transduction — still Ax3-lossless microscopically, not a resistor)** | **0D $\approx$ port-CLOSED config; ∞-lattice $\approx$ port-OPEN config — but see the RE-BANK** | **CANONICAL (#751 merged 2026-07-20) — with a currency correction.** `research/2026-07-20_jomega-derivation_result.md` §0.1/§4.1: the **frozen driven criterion lands bin (iii) DEGENERATE / UNDETERMINED** ((a-ledger) 0/4 cells, (b-ledger) only the C2 super-Ohmic ∞-lattice) — the clean quantitative split (70–95% / 0–10%) came ONLY from a **post-hoc undriven ring-down** (NOT the frozen prereg) and its "0–10% / coupling-scale-robust / unambiguous" grade is **🔴 RE-BANKED** (§0.3, §4.2). **What survives:** only the ORDERING (0D returns more than ∞-lattice) is coupling-scale-robust; the transfer magnitude tracks the undetermined coupling prefactor. This row-class still formalizes "port-open vs port-closed is a *scope* statement, not a property of the channel," but the quantitative half is UNDETERMINED. **Two-method:** #751 §0.1 frozen-output + §4.1 ledger table. |
| P9 | **DM-halo NEAR-FIELD** (explicitly **NOT-A-PORT**) | 3 (A1 bulk $\sqrt2\,c$ reactive) | **axiom-forced reactive storage** (the halo $=$ the bulk channel's reactive near-field; added-mass; d'Alembert zero-steady-drag) | **REACTIVE (stores/loads; shapes flat rotation curves without loss)** | **NOT-A-PORT** (a port *drains*; this *stores-and-returns*) | **RULED (deep-space reactive-bulk arc).** `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md:54,68` (added-mass/d'Alembert; the **dark-matter added-mass reading survives $=$ reactive**; the *dissipative* stall corollary demoted, `clm-h55fy1` flipped). This IS the DM-conflation resolution. **Two-method:** walk-record §54 (mechanism) + §68 (KEEP-BOTH "what survives $=$ reactive"). |

**★Currency correction on P8 (flag-don't-fix; draft-vs-merged divergence).** The draft (`research/2026-07-20_port-register_draft.md` §2 P8) stated the scope-split with the quantitative "0D recovers 70–95% $E_S$ / ∞-lattice drains to 0–10%" wording, which was correct *at the branch state it cited*. Since #751 merged (2026-07-20T17:20:35Z), that same source now carries a **🔴 RE-BANK** of exactly that quantitative half: the frozen driven criterion lands bin (iii) DEGENERATE, and only the ordering is coupling-scale-robust. **This canon leaf carries the MERGED (re-banked) truth, not the pre-rebank draft wording** — surfaced here, not silently reframed. The draft is preserved (KEEP-BOTH) with its own branch-state honesty note.

---

## §3 — ★Q1: the first explicitly-OPEN row

| # | Port | Channel | Provenance | Radiative / Reactive | Open / Closed | Ruling status + receipt |
|---|---|---|---|---|---|---|
| **Q1** | **A1 bulk channel — far-field radiative port for gravitating sources** | 3 (A1 bulk; radiative speed $\sqrt{10/3}\,c$ per FLAG-A) | **the load-bearing UNFORCED CHOICE** (band-map channel 3 is a *gapless propagating* branch — does a mass quadrupole open an *independent far-field radiative port* into it?) | **Reading A — RADIATIVE, DERIVED-OPEN** *(was "UNRULED — Reading-dependent")* | **★REVERTED 2026-07-20 → Reading-A LIVE** *(was RULED-CONDITIONAL; was the register's first explicitly-OPEN row)* | **★REVERTED 2026-07-20 per this row's own clause — Reading-A is the standing state; the pulsar exclusion is LIVE against the framework.** The make-or-break mechanical $\nabla\!\cdot\!u$ common-mode derivation returned **NONE-DERIVES** at review grade (#761 merged @ `caa51c17`, `research/2026-07-20_mechanical-commonmode-derivation_result.md` §5): the A1-dilatation rides the gapless P-branch, the binary drives it at quadrupole order, and the EM Gauss-kill is *structurally blocked* from $\nabla\!\cdot\!u$ by the bulk restoring force $K\neq0$ — firing this row's own conditional clause. **Verbatim clause that fired** (`[sic]`, from the superseded RULED-CONDITIONAL text preserved below): *"if NONE-DERIVES this ruling REVERTS and the banked Reading-A exclusion (falsification ledger; 9–110σ pulsar) goes live."* Standing physics is now **Reading A** (independent far-field bulk radiative port + O(1) coupling); the banked exclusion is **LIVE** — excluded at **9–110σ (Hulse-Taylor)** / **100–1400× (double-pulsar)** (falsification ledger, entry `q1-reading-A-radiative-bulk-port`, promoted LIVE 2026-07-20). A clean closed-negative against the gravitational bulk sector (Rule 11 honest closure), NOT a softening. **Forward path (a separate FUTURE ruling, not a softening of this revert):** the envelope-sector reduction lane (`research/envelope-sector-reduction`, in flight) is the routed derivation that could later ground a re-open with a **DERIVED** coupling; a re-open needs its own Grant ruling. **Receipts:** #761 result §5 CONSEQUENCE + docket ENTRY 37 + ENTRY 2026-07-20-q1-revert-execution. *(Superseded RULED-CONDITIONAL text — preserved verbatim per Rule 12; do NOT delete Grant's ruling text:)* **RULED-CONDITIONAL (Grant 2026-07-20, #756 merged — Reading B = standing physics: no far-field radiative port for gravitating sources; the halo is its complete story).** CONDITIONAL: stands on the make-or-break derivation (mechanical ∇·u common-mode + cold-regime emptying — per re-banked #758 the candidate T_d structure's closing step is currently UN-DERIVED, clm-9kd2t3 do-not-build); if NONE-DERIVES this ruling REVERTS and the banked Reading-A exclusion (falsification ledger; 9–110σ pulsar) goes live. Receipts: docket ENTRY 32 (ruling) + the #758 re-bank. *(Superseded: "UNRULED — Grant/auditor sector-ownership adjudication (FLAG-1 / band-map D5; docket ENTRY 29 §Q1)" — preserved per Rule 12.)* `[canon, #750 merged 2026-07-20]` frames it (off-main); companion `research/2026-07-20_q1-pulsar-hardening.md` hardens it against pulsar timing. |

**Reading A (independent elastic radiative DOF).** The A1/bulk-dilatation sector radiates like any elastic solid's longitudinal channel: monopole + dipole killed by conservation, but the **quadrupole radiates** (same nonzero rotating mass quadrupole as the T2/GW; no conservation law left to kill it). With an O(1) coupling ($K=2G$, no $1/\omega_{BD}$ suppression) the predicted admixture is **large** ⇒ **kill-class**, EXCLUDED. This is the elastic-medium *default*.

**Reading B (constrained / near-field-reactive-only, GR-like).** The longitudinal/scalar sector is *constrained* (pure-gauge, as GR's scalar metric parts) or *reactive-near-field-only* (the DM-halo mode, P9) ⇒ **no scalar-GW**, UNTOUCHED — but the corpus then **owes a mechanism** for why a mode that propagates freely at $\sqrt{10/3}\,c$ in its linear passband does not radiate from a strong quadrupolar source.

**★Register verdict — REVERTED 2026-07-20 (was: OPEN).** The make-or-break mechanical $\nabla\!\cdot\!u$ common-mode derivation landed **NONE-DERIVES** at review grade (#761 merged @ `caa51c17`), firing the Q1 row's own conditional clause: the RULED-CONDITIONAL **Reading-B reverts** and **Reading A is the standing state — the pulsar exclusion is LIVE against the framework** (Reading A = independent far-field bulk radiative port + O(1) coupling; excluded at 9–110σ Hulse-Taylor / 100–1400× the double-pulsar bound). The seismology external anchor ($E_S/E_P\approx23.4$; §6 of the companion), originally carried to *sharpen Reading B*, now reads for Reading A: a generic isotropic elastic solid **does** radiate its P/bulk channel — exactly the structure the #761 derivation found AVE's vacuum has (bulk restoring force $K\neq0$ ⇒ radiating P-wave), so no generic-elasticity suppression rescues the framework. The forward path (the envelope-sector reduction lane, `research/envelope-sector-reduction`, in flight) could ground a future re-open with a **DERIVED** coupling — a separate future Grant ruling, **not** a softening of this revert. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**

*(Superseded verdict text, preserved verbatim per Rule 12:)* **Register verdict:** neither reading is forced by current canon ⇒ **the row stays OPEN**. The companion hardening doc (`research/2026-07-20_q1-pulsar-hardening.md` §1–§2) sharpens the consequence: under Reading A the extra flux fraction $F_{bulk}/F_{shear}\approx0.03$–$0.12$ (with the DERIVED angular partition $\mathcal{A}_{ang}=2/3$) is **EXCLUDED at 9–110σ by Hulse-Taylor and by 100–1400× the double-pulsar bound** — a kill-class result to bank if Reading A is ruled; if Reading B is ruled, a suppression-derivation lane (B1–B4) is owed. **Decision is Grant's** (§4 adjudication package of the companion doc). The seismology external anchor ($E_S/E_P\approx23.4$; §6 of the companion) sharpens Reading B: a generic elastic solid *does* radiate its P/bulk channel, so Reading B's suppression cannot come from generic elasticity.

---

## §4 — Provenance ledger + row count + currency state

**Register row count $= 14$** (4 channel rows §1 + 9 port rows §2 + 1 open Q1 row §3).

**Provenance class tally:**

- **axiom-forced / inherent:** channels 1–4; ports P1 ($R_{rad}\equiv Z_0$), P4 ($\Gamma=-1$ wall), P9 (DM near-field NOT-A-PORT).
- **emergent-configurational:** P3 (X40 stubs), P5 (Casimir cutoff), P6 (Cherenkov/Mach), P8 (J(ω) scope-split), Q1 (the unforced fork).
- **instrument-engineered:** P2 ($Z_{det}$), P7 (F6 collar).

**Radiative / reactive tally:** RADIATIVE-open $=$ P1, P2, P3, (P6-when-$v>v_{crit}$); REACTIVE/closed $=$ P4, P5, P8-0D, P9, (P6-below-threshold); scope-dependent (now bin-(iii)-degenerate on the quantitative half) $=$ P8; instrument-class $=$ P7; **Q1 $=$ ★REVERTED 2026-07-20 → Reading-A LIVE** (the make-or-break derivation returned NONE-DERIVES, #761 @ `caa51c17`; the RULED-CONDITIONAL Reading-B reverted per the Q1 row's own clause; the independent-radiative-port reading is now RADIATIVE-open and its pulsar exclusion is live against the framework).

**★Row-currency state at build (2026-07-20; re-verified against origin/main tip `1003661c` = #751 merge).** The register may honestly carry branch-tagged rows if labeled. At build the state is **13 rows `[canon]` / 1 row `[branch]`**:

| Change from draft | Rows | State at build |
|---|---|---|
| stayed `[canon]` | channels 1,2,4; P1, P2, P4, P5, P9 | `[canon]` (unchanged) |
| `[canon]` via #749 (merged) | P3, P7 | `[canon, #749 merged 2026-07-20]` (as draft) |
| **FLIPPED `[branch:#751]` → `[canon]`** | **P6, P8** | `[canon, #751 merged 2026-07-20]` — **P8 carries the merged RE-BANK** (§2 note) |
| **stays `[branch]` (source OPEN)** | **Q1** (and the channel-3 `#750 §2.1` cross-cite) | `[canon, #750 merged 2026-07-20]` — **#750 still OPEN; NOT on main** |

**Currency-touch-owed (dated 2026-07-20).** One row (**Q1**) and one cross-cite (channel-3 `#750 §2.1`) remain branch-tagged because **#750 (scalar-GW bulk-channel derivation) is still OPEN**. The FLAG-A physics under channel 3 is independently `[canon]` (`constants.py:770–781`, `cosserat-mass-gap.md:132`); only the `#750 §2.1` cross-cite is off-main. **When #750 merges, re-touch the Q1 row and the channel-3 cross-cite** (`[canon, #750 merged 2026-07-20]` → `[canon]`) and cite the Q1 ruling if one has landed. A separate lane (**#754**, A1 amplitude transfer — OPEN at build) is *not* cited by any register row; noted here so a future currency-touch does not mistake it for a dependency.

**Rows I could NOT provenance: NONE.** Every row is provenance-tagged to a content-verified `[canon]` leaf or an honestly-flagged `[canon, #750 merged 2026-07-20]` source. The honest caveat is the single branch-state dependence of Q1 (leaning on the still-open #750).

**Contradictions surfaced (flag-don't-fix):**

- **FLAG-A** (channel-3 speed label): the band-map channel-3 row labels the bulk $\sqrt2\,c$ (the PORT/impedance speed); the *radiative* far-field longitudinal wave is the P-wave $\sqrt{10/3}\,c$ (`constants.py:770–781`). The register resolves this **structurally** (two columns), does not edit the band-map leaf (fence). **Owed:** an auditor-lane band-map channel-3 speed-label reconciliation.
- **The `08_gravitational_waves.tex` warningbox** (unresolved channel attribution): the Hulse-Taylor $\dot P_b$ step-3 attributes the radiated power to the *bulk / longitudinal* channel, while the KB canon assigns GW to the *transverse shear* channel. This is **exactly the Q1 fork surfacing inside the existing manuscript** (a bulk+shear double-count pulsar timing forbids). Carried to the companion doc §2.4 as the load-bearing corpus contradiction. **Not fixed here** (fence: `08_gravitational_waves.tex` not edited by this lane); resolves *with* the Q1 ruling.
- **P8 draft-vs-merged divergence** (§2 currency note): the draft's quantitative scope-split is RE-BANKED in the merged #751; canon carries the merged truth.

> **Register provenance.** Promoted 2026-07-20 from `research/2026-07-20_port-register_draft.md` (merged #753) under the Grant firing *"fire the port channel lane and continue it"* `[sic]` + the canon-promotion gate *"lets do it"* `[sic]`. Taxonomy $=$ orchestrator's walk-wording ratified by the firing (tagged throughout). All `[canon]` citations re-verified two-method (`grep -F` + direct read) against origin/main tip `1003661c` (#751 merge) at build; `[canon, #750 merged 2026-07-20]` cites flagged as not-yet-canon / off-main. Mints no `clm-`. Companions (KEEP-BOTH): the draft + `research/2026-07-20_q1-pulsar-hardening.md`; docket ENTRY 29 (port-register) + ENTRY 27 (R3/R4 ratifications) + ENTRY 31 (this promotion).


---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:49`** — *"$\sqrt{10/3}\,c \approx 1.83c$ (isotropic-solid P-wave; the $4G/3$ shear term cannot be dropped for a real far-field wave)"*
  Stamped in place at `:49`.
  **⚑ MIXED-BIN ROW — read the stamp as scoped, not blanket (disclosure added 2026-08-11 at review).**
  `:49` is a 9-cell channel-3 table row, and the banked worklist hosts a **second, co-resident row on
  this same line** binned **NEEDS-RE-DERIVATION**, not DIES: quote *"$Z_{bulk} = \rho\,c_{bulk}$ …
  $\sqrt2\,c$ ($V_{LONG}$; $K=2G$ magic-angle PORT/impedance mode) … gapless acoustic; edge
  $2\sqrt2\,c/\ell_{node}$"*, rationale *"Prereg-explicit: Z_bulk=rho*c_bulk owes formula-level
  re-derivation; the gapless band-edge entry presumes a spectrum branch the carve removes."* **That
  row is BATCH 2 and is not demoted here.** The stamp — inserted before the row's final `|`, so it
  lands in the provenance cell — demotes exactly the **RADIATIVE (far-field) speed** cell
  `$\sqrt{10/3}\,c \approx 1.83c$` quoted above; the PORT/impedance-speed and band-edge cells carry
  the co-resident NEEDS row and await batch 2.
  **Why it dies (audited row rationale, verbatim):** Prereg-named ch-3 radiative column: a far-field bulk wave with a physical transit speed IS the phantom; also covers :57 (freely-propagating-wave bullet) and :58 (both-superluminal causality/flux-prefactor claim, void with no transit speeds).
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:57`, `:58`.
- **`:74`** — *"Per-channel (arccos, by $\sqrt2$ scaling for bulk): EM/shear $\approx0.80c$; bulk $\approx0.80\sqrt2\,c\approx1.13c$"*
  Stamped in place at `:74`.
  **Why it dies (audited row rationale, verbatim):** Guidance-named class: a bulk Cherenkov/Mach onset requires a propagating bulk branch to open into; only the bulk member dies — the EM/shear members and the steady-drift-vs-accelerated nuance are untouched.
- **`:93`** — *"a generic isotropic elastic solid does radiate its P/bulk channel ... (bulk restoring force $K\neq0$ ⇒ radiating P-wave)"*
  Stamped in place at `:93`.
  **Why it dies (audited row rationale, verbatim):** The #761 chain (A1 rides the gapless P-branch, K≠0 forces radiation) is exactly the K-import minting a compressible far-field branch; covers :89 Reading-A mechanism (quadrupole radiates, O(1) coupling, kill-class).
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:89`.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).
