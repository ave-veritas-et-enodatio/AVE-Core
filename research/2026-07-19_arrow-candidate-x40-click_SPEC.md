# X40-class CLICK as the local-arrow candidate — derivation + adjudication + SPEC (build-gated)

**Date:** 2026-07-19 · **Class:** SPEC + derivation + clamp-adjudication (DESIGN ONLY — stops at the build gate; no engine/meter edit, no arm fired).
**Lane:** implementer — X40-CLICK ARROW-CANDIDATE. **Scope:** derive whether the energy-conserving X40 *click* can supply the local arrow the static reactive floor structurally could not; adjudicate the certified meter's hard-zero clamp as accidental-click-vs-numerical-guard; SPEC the honest click-arm + a Grant design-walk brief. **NOTHING fired, nothing built.**
**Sibling lanes (cross-pointer, NOT duplicated here):** the OTHER surviving arrow candidate — *interacting-bath thermalization* (mode–mode coupled / dissipative dephasing) — has its own parallel lane per [`2026-07-19_f6-thermal-floor-arm_result.md`](2026-07-19_f6-thermal-floor-arm_result.md) §4 follow-on 1. This lane is the *click* (topological/counting minting) candidate only; where the click-count turns out `Δω`-dependent it ROUTES to that lane rather than claiming the arrow (§4 verdict tree, `MODE-SPREAD-CONFOUND`).

---

## 0 · Sector header + regime declaration (mandatory before any substrate claim)

- **Sector.** The arrow *question* is R7 thermal / entropy-sink (the F6 ε→T2 candidate). The click *mechanism* lives in the **graph cycle-space** (the T-odd loop current / `b_1` of the srs ring), NOT in A1 dilatation-mass and **NOT** in the Cosserat `(2,3)` winding-**charge**. ★Sector-ownership guard (memory `feedback_sector_ownership_a1_t2_crosswiring`): the click's trapped mesh quantity is a **cycle-space loop current** (Hodge T-odd part of the injected 1-cochain), a *conserved graph label* — it must **not** be cross-wired with the electron's `(2,3)` phase-space charge-winding, which is a different object on a different (bond-pair LC / Clifford-torus) coordinate. Same word "winding," different sector.
- **Mode.** Classical reactive K4-TLM lattice (K4, z=3 srs, 4 ports), lossless (Ax3). Two instrument families are in play and must be kept distinct: (i) the **X40 ring-closure** instrument — a standalone TLM ring-completion sim minting a conserved flux linkage `Λ` with matched-stub radiation (`x40_ring_closure_transient.py`); (ii) the **F6 bath-meter** (`LatticeBathCoupler`) — the certified lossless-reactive Caldeira–Leggett comb whose back-reaction carries the clamp under adjudication in §2. The click-arm is built on (i); (ii) is READ-ONLY and byte-untouched.
- **Regime + phase-state — ★the load-bearing carve.** The **static reactive floor** (the closed-negative candidate, [`2026-07-19_f6-thermal-floor-arm_result.md`](2026-07-19_f6-thermal-floor-arm_result.md)) is a **Regime-I sub-yield, drive-OFF, PRODUCT-moment** mechanism — persistence of a latched state, LOSSLESS, no crossing. The **click** is a **TRANSITION-moment** mechanism: a *ring-completion / capture event* is a topological state-change (`b_1: 0→1`) at/across a threshold. Per the retention/transition split (`retention-transition-split.md:16`, `:31`), an arrow is admissible **only** at the TRANSITION moment and **only** from counting (mode-spread with reconvergence ≈ 0, **or** the energy-conserving click) — **never** a valve (`:36`; tier-1 verbatim, `2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256` "the arrow comes from mode-count or a click, never a valve"; `:176` "reservoir mode-count … or a click (X40) … never from a valve"). **This is the whole reason the floor structurally could not carry the arrow and the click might:** the floor was asked to source a TRANSITION arrow while sitting in the PRODUCT moment, on a phase-non-mixing bath — the wrong moment *and* the wrong coordinate. The click is natively a TRANSITION-moment, counting-coordinate mechanism.
- **Coordinate discipline (A46 / `phase-space-coordinate-check`).** ★The methodological fix vs the floor arm. The floor arm's frozen observable `S(ρ)` was a **modal-amplitude / real-energy revival** read; the walked mechanism (dephasing a coherent revival) lives in **modal-phase** coordinate, which is inexpressible on independent oscillators (`…thermal-floor-arm_result.md` §0b). The click's claim lives in the **cycle-space / `b_1` count** coordinate (a topological integer) plus the **per-event `Λ` ledger** — a matching-coordinate test must count *mint events* and audit *`Λ`-conservation*, NOT read a real-space revival amplitude. Measuring the click in the floor's revival coordinate would be exactly the A46 mismatch that made the floor test uninformative.
- **Consistency-vs-emergence tag (`consistency-vs-emergence`).** The X40 mint itself is **CONSISTENCY / manifestation-class** — `f_E = 1/N` and `Λ`-conservation are *theorems* of the TL model (`…x40-ring-closure…_result.md` §"CONSISTENCY-vs-EMERGENCE"), zero CODATA. This SPEC does **not** promote anything to emergence-class; the strongest reachable claim is a **substrate-mechanism statement about the arrow's COORDINATE** (topological-count, not modal-phase), gated on the Loschmidt + `Δω`-invariance discriminators (§4). No instrument constant is CODATA-derived; `N`, comb params, and matched-stub `Z_0` are engineering choices / calibration, tagged as such.

## 1 · The derivation — what is irreversible about the click (substrate-native)

**The question (task).** Can the click supply the *local arrow* where the static floor structurally could not? Answer, derived below: **yes in principle, because the click sources the arrow in a DIFFERENT coordinate (topological count) than the one that was structurally barred (modal phase) — but the arrow is a COUNTING/statistical (Loschmidt-class) arrow, and whether it survives on a driven ensemble is exactly what the SPEC'd arm must decide.** Nothing here banks the arrow; this is the mechanism derivation that licenses the arm.

### 1.1 · The click, unpacked from the X40 canon (verify-before-cite, `…x40-ring-closure-transient_result.md`)

At each ring-completion in an srs `N`-ring (`N = 10` for srs), the parent circulation donated to the closing bond splits, **machine-exact and LOSSLESS**:

- **TRAPPED `f_E = 1/N = 0.1000…`** — lives **entirely** in the **cycle-space** (T-odd loop current); a *persistent DC mesh current* (a conserved graph label). Flux linkage `Λ` banks WHOLE (`Λ`-drift `2.2e-16`).
- **RADIATED `(N−1)/N = 9/10`** — the **cut-space** (T-even bond-strain), AC transient driven into the **matched stubs** (`R_rad ≡ Z_0`, `Γ=0`, a real port).

Two facts from the canon are load-bearing: **(b)** "Trapping occurs ONLY at discrete ring-COMPLETION events. An open chain has no mesh and no conserved `Λ` … The instant the 10th bond closes, a conserved mesh quantity is MINTED" — so **discreteness of trapping = discreteness of ring completions**; and the split is **energy-EXACT** (`|E_ring+E_rad−E0|/E0 = 2.2e-16`), the defining property of the *energy-conserving* click.

### 1.2 · WHAT is irreversible — counting over what ensemble, where the boundary is, what the EE element is

- **Counting over what ensemble.** Over discrete **capture/mint events**. For the X40 click: **ring-completion events** (each increments `b_1: 0→1`, minting one trapped mesh loop). For the detector-boundary click (`clm-ldmvwi`, Born-rule-from-Ohmic-measurement-work, solidity 0.65, build-status "ok to build on, see caveats"): **threshold-crossing self-traps** — the first-passage of the accumulated absorbed energy across the Ax4 saturation-yield `S(A)→0`, one click per capture cell (`2026-06-08_ave-double-slit_born-from-clicks_result.md`). The ensemble is the set of *independent capture sites/events*; the counted observable is `N_click(t)`, the accumulated number of mints.
- **Where the boundary is.** A **real impedance boundary**, not a bulk reactance. X40: the ring-completion topological event **plus** the matched-stub termination `R_rad ≡ Z_0` the radiated `9/10` disperses into. Detector click: the detector port `Z_det` (a matched real port). Per the retention/transition regime table (`retention-transition-split.md:60`), a **matched radiative/detector PORT** with `R_rad ≡ Z_0` / `Z_det` is the **SYSTEM-loss** row and is **`requires_R = port-only (Ax3-legal)`** — a real boundary of the system, categorically distinct from the **forbidden bulk valve** (`:36`, tier-1 §(iv) "do not resurrect a valve", `…tier-1…CHARTER.md:174`).
- **What the EE circuit is — the capture work-function as which element.** The capture work-function is the **Joule extraction `W = ∫ V²/Z_det dt`** at the boundary (`clm-ldmvwi` rationale, step (4): "Joule extraction … with signal/noise decomposition"). In EE terms it is a **matched real port resistance** `R_rad ≡ Z_0` (X40) / `Z_det` (detector) — a *travelling-wave termination*, `Γ=0`, into which launched energy **does not reflect** (reconvergence ≈ 0 within the window). ★This is the honest reconciliation of "never a valve": the click's dissipative-looking channel is a **matched port at the actual system boundary**, the Ax3-legal radiative channel — NOT a `Re(Z)`/diode inserted into the bulk to *manufacture* an arrow.

### 1.3 · The arrow itself — a protected-count ratchet, no valve (the Loschmidt honesty)

★The subtle part, stated honestly. The TLM microdynamics are **lossless-reactive and time-reversible**; a *single* ring-completion, run backward, un-closes. So the arrow is **not** microscopic irreversibility. It is a **counting / Boltzmann–Loschmidt arrow**:

1. **The MINT** deposits a **discrete counted quantity** (a trapped cycle-space loop, `b_1`+1; `Λ = L_bond·i(0)` banked whole) that is **topologically / threshold protected** — PRODUCT-lossless, cannot spontaneously un-mint sub-yield (`retention-transition-split.md:15,:24` "charge/label latched by topology … a conserved label, not an energy that leaks").
2. **The RADIATED remainder** (`9/10`) disperses into a **matched quasi-continuum** (`R_rad ≡ Z_0`) with **reconvergence ≈ 0** — the home-leaf premise of the mode-count arrow (`…tier-1…CHARTER.md:176` "reconvergence probability effectively zero"; `dark-energy-latent-heat-definition.md:84-86` cited there).
3. **The ARROW** is that `N_click(t)` — the count of protected mints — is **monotone-non-decreasing under forward driving**, and the phase-space measure of *un-minting* is vanishingly small because un-minting requires **both** the improbable reconvergence of the dispersed `9/10` **and** a topological un-protection event. The "pawl" of the ratchet is **not a valve** (no bulk `Re(Z)`); it is the **topological protection of the minted label + the reconvergence-0 dispersal into a matched port**.

### 1.4 · Why this clears the wall the floor hit (the structural contrast)

The floor arm closed negative at the STRONG-form + **structural** level (`…thermal-floor-arm_result.md` §0b): "a static random floor sets the local arrow by dephasing a coherent revival **requires** the floor to scramble the signal's phase, which needs an **interacting/mode-coupled/dissipative** channel — absent by construction in the Ax3 lossless-reactive regime … **structurally inexpressible** … the same reason the #721 conservation was an ALGEBRAIC IDENTITY." That barrier is **coordinate-specific**: it bars an arrow *sourced from modal phase* on independent oscillators.

The click **does not source its arrow from modal phase.** It sources it from a **topological count** (`b_1` mints) + a **matched-port dispersal** (reconvergence-0). Neither requires mode–mode coupling in the reactive comb: the X40 driver already *demonstrates* the mint is energy-exact and the trapped label well-defined on a **lossless** TLM, live-fire (`Λ`-drift `2.2e-16`, `f_E=1/10`, `b_1=1`). So the click's arrow-coordinate is **structurally EXPRESSIBLE** where the floor's was not — that is the precise sense in which the click can supply what the floor could not.

★**But — the honest ceiling (Rule 11 pre-commitment).** "Expressible" ≠ "demonstrated." What the X40 canon banks is CONSISTENCY-class (the WRITE mechanism is coherent; it "does NOT prove the bias is real", `…x40…result.md` §"CONSISTENCY"). What is **NOT** yet shown, and what the arm must decide: that on a **driven ensemble of many completions** the count `N_click` (a) monotonically accumulates, (b) does **not** un-count under a **Loschmidt time-reversal** within the window, and (c) is **`Δω`-INVARIANT** (independent of the radiated bath's recurrence structure) — the three signatures that separate a genuine counting arrow (chord) from reversible bookkeeping (echo) or a mode-spread confound. Those are §4's gates. This derivation *licenses* the arm; it does not pre-judge it.

## 2 · ★THE CLAMP ADJUDICATION — accidental click, or numerical guard?

**The sharp sub-question (task).** The certified meter's back-reaction clamp is a **hard-zero ABSORBING STATE** already sitting in the instrument — an accidental click-analog. The clamp: `scale = √(max((E_lat − d_e_bath)/E_lat, 0))`, which **hard-zeroes** `E_lat` (`scale=0`) the step `d_e_bath ≥ E_lat`; `E_lat ≡ 0` thereafter (`…certified-kappa-sweep_result.md` R-2, `f6_bath_meter.py` back-reaction). The #726 review treated its dead windows as **NO-INFORMATION** artifacts (85–90% dead rows on dense combs). Is that (a) a numerical guard merely mimicking click phenomenology, or (b) a derivable correspondence — clamp = crude click at the port boundary — that reframes those "artifacts" as the click-arrow showing up uninvited?

### 2.1 · The test — score the clamp against the THREE positive click signatures

The click is not defined by "one-way capture" alone (that is shared with any absorbing state). It carries **three positive signatures**, each *verified* from the X40 canon. Scoring the clamp against each:

| # | Click signature (verified source) | The clamp | Verdict |
|---|---|---|---|
| **S1 — energy-EXACT** | `Λ` conserved to `2.2e-16`; `1/N` trapped + `(N−1)/N` radiated = **100%**, nothing lost (`…x40…result.md` HEADLINE) | `max(…,0)` **truncates** a would-be-imaginary √; when `d_e_bath > E_lat` the bath took more than the lattice held ⇒ `(d_e_bath − E_lat)` is **unaccounted**. #726 R-2/§2: the densest comb's conservation drift `6.8e-6` is **"largely clamp-created."** | **FAILS S1** — the clamp *breaks* conservation; the click's defining property is that it does not. |
| **S2 — mints a COUNTED protected label** | `b_1: 0→1`; a trapped cycle-space `Λ=1/N` that **PERSISTS** (a conserved integer/label) | mints **nothing** — it **destroys** state (`E_lat→0`). Opposite sign of information: the click *adds* a protected quantity; the clamp *removes all* quantities. No count, no persistence, no topology. | **FAILS S2** — the clamp is a state-*sink*, not a label-*mint*. |
| **S3 — a PHYSICAL-port boundary** | ring-completion (a real srs-graph topological event) + matched stubs (`R_rad ≡ Z_0`, a real port) | the "boundary" is a **floating-point guard** in the amount-not-phase global-rescale arithmetic, firing on an over-extraction transient at **no physical port** — `max(…,0)` in code, not a `Γ` crossing (`…no-discharge-scan…md` §3: the back-reaction enters only as the product `κ·g0`; the clamp is downstream of that rescale). | **FAILS S3** — the clamp fires at a code guard, not a substrate port. |

**The clamp fails all three positive click signatures.** Its resemblance to a click is confined to the one property it shares with *any* absorbing state — "once captured, stays captured" — which is **not** a click signature. **Verdict lands on (a): the clamp is a NUMERICAL GUARD that superficially mimics click phenomenology; it is NOT a derivable click.** The #726 review's NO-INFORMATION reading of its dead windows is **correct**.

### 2.2 · Both-ways consensus-bias check (`consensus-bias-symmetric-standard`) — steelmanning (b)

I carry, by training volume, an SM/QED "it's just a numerical bug, exclude it" prior. Symmetric-standard demands I steelman (b) before dismissing:

**Steelman for (b).** The clamp does **not** fire at random. It fires exactly when `d_e_bath ≥ E_lat` — i.e. at **FULL DISCHARGE** (`E_lat→0`), the moment the mode-spread into the quasi-continuum has *completed*. The #727 INSTRUMENT-INCOMPATIBLE scan proves this is *structural*: on the certified instrument the quasi-continuum threshold (`N_occ ≥ 10`) and the full-discharge/clamp event are crossed at the **same** comb density — "quasi-continuum transfer **is** full discharge — the clamp is the instrument **faithfully reporting** that the lattice fully drained" (`…no-discharge-scan…INSTRUMENT-INCOMPATIBLE.md` §5). So the clamp is keyed to a **physically meaningful transition** — the completion of irreversible mode-spread — not to noise.

**Why the steelman does NOT rescue (b) — and where it DOES point.** Even granting that the clamp is keyed to a real transition, that transition is **mode-spread completion**, which is the *interacting-bath / mode-spread* picture (candidate 1), **NOT** a ring-completion topological mint (the click). And the clamp is a **corrupting** sensor even of mode-spread: genuine mode-spread leaves the energy in the bath modes *still oscillating* (a recurrence would return it at `T_rec`); the clamp instead **zeroes `E_lat` and freezes it**, destroying the recurrence structure that is the very observable needed to measure *either* arrow (this is exactly why #726/#727 read 85–90% NO-INFORMATION). So the honest resolution of the steelman:

> The clamp is a **crude, information-destroying mode-spread-completion flag**, not a click. It is not physically arbitrary — that much of (b) survives — but it routes to the **interacting-bath lane** as a *warning about the meter*, not to the click lane as evidence. It is **not** the click-arrow showing up uninvited; it is a numerical guard that happens to trip at the mode-spread transition and then **erases** the information an arrow-test needs. The dismissal in §2.1 is **earned** (three failed positive signatures + a routed steelman), not defaulted from prior.

### 2.3 · What would discriminate (whichever way it lands) + the design consequence

**The empirical discriminator (cheap, read-only, byte-untouched).** Overlay the X40 mint-observable — `Λ`-conservation *across the event* + `b_1` increment + the `f_E = 1/N` trapped split — onto the **existing banked meter clamp event**:

- If the clamp event **mints a persistent trapped mesh quantity AND conserves `Λ` across the event (drift ≈ 0)** → it is a click (b); reopen and route to Grant.
- If (as §2.1 predicts) it **zeroes `E_lat`, breaks conservation (clamp-created drift), and mints no persistent counted quantity** → numerical guard (a), confirmed by receipt.

This is Phase-0 of the SPEC (§4) — minutes, read-only, uses the existing X40 observable on the existing meter, no edit.

★**The load-bearing design consequence.** Because the accidental click-analog in the meter is a **corruptor**, the honest click-arm must **NOT** build on the meter's back-reaction/clamp. It must build on the **X40 ring-closure mint machinery** (energy-exact, its own instrument, §3). The clamp adjudication is thus not a side-quest: it *forces the instrument choice* for the whole arm.

## 3 · The honest click-arm design — frozen observable, certificates, byte-untouched set

### 3.1 · The frozen observable that would show arrow-from-click

Per §0's A46 discipline, the observable is in the **count / `Λ`-ledger coordinate**, not the revival coordinate. On a **driven ensemble of ring-completions** (the instrument fork is Grant's, §5 Decision 1), record every step:

- **PRIMARY — the count trajectory `N_click(t)`.** The accumulated number of mint events = `b_1` increments (trapped cycle-space loops). Frozen reads: (i) **monotonicity** under forward driving (`N_click` non-decreasing); (ii) **`Δω`-INVARIANCE** — sweep the radiated bath's comb spacing `Δω` and require the count-arrow signature to be *independent* of `T_rec = 2π/Δω`. `Δω`-invariance is the discriminator that the arrow is in the **counting** (topological), not the modal recurrence — the exact axis on which the floor/counting-arrow arms failed (`R_return` was `T_rec`/`τ_transfer`-controlled, `…counting-arrow-arm_result.md` §0, `…certified-kappa-sweep_result.md` §3).
- **PER-EVENT ledger (the click's defining property).** For each mint: `Λ`-conservation across the event (drift ≈ 0) and the `f_E = 1/N` trapped split. A "mint" that fails `Λ`-conservation is a numerical artifact (the clamp's failure mode, §2), not a click — this is the built-in honesty gate.
- **THE KILL-SHAPE — a Loschmidt echo.** Time-reverse the TLM state at the window end (swap `V_inc ↔ V_ref` on every line — the native TLM time-reversal) and evolve backward. Measure whether `N_click` **un-counts**. A genuine counting arrow does **not** un-count within the window (the trapped `1/N` is protected; the dispersed `9/10` cannot reconverge). If the count fully reverses, the "arrow" was reversible bookkeeping (echo, not chord). This is the sharpest separation of the Loschmidt-class arrow (§1.3) from an artifact.
- **Click-rate statistics vs recurrence structure (task's explicit alternative).** Report both framings: **click-rate** (mints per window, and its `Δω`-invariance) *and* the **recurrence structure** (`R_return(x)` in the radiated channel). The click claim rests on the click-rate being recurrence-*independent*; if the click-rate tracks the recurrence, that is the `MODE-SPREAD-CONFOUND` verdict (§4) and routes away.

### 3.2 · Which certificates break — and which do not

- **The #721 R-1 identity — DOES NOT break (if built on X40).** #721 R-1 is that on the **standalone-K4 bath-meter** energy conservation is an *algebraic identity* of the amount-not-phase global rescale. The X40 ring-closure instrument is a **different instrument** (standalone TLM ring-completion; its own conservation identity is the `Λ`-drift `2.2e-16`). A click-arm on the X40 instrument does **not** use `LatticeBathCoupler`'s back-reaction, so it **does not touch** the #721 bath-meter identity. ★This is a *reason to build on X40*, not the meter: it sidesteps both the clamp (§2) and the #721 identity.
- **The port abstraction — DOES NOT break, but a real-port FORK is surfaced (flag-don't-fix).** The click's "port" is the ring-completion + matched stubs (`R_rad ≡ Z_0`), **not** the meter's collar-coupling port — so the meter's port abstraction is untouched. **BUT** the matched-stub bath is a **real radiative port** (SYSTEM-loss, Ax3-legal port-only, `retention-transition-split.md:60`), a *different bath model* from the meter's lossless-reactive Caldeira–Leggett comb (which recurs at `T_rec`). Whether the click's arrow is permitted to invoke a real matched port, or must stay in the meter's lossless-reactive world, is a genuine **physics-framing fork** — surfaced to Grant (§5 Decision 2), **not** resolved here.
- **`clm-ldmvwi` (Born-rule capture) — CONSUMED, not redefined.** A click-primitive that keys the detector-boundary capture on "capture work-function = Joule extraction at `Z_det`" **consumes** `clm-ldmvwi` (build-status "ok to build on, see caveats"; solidity 0.65) as the capture definition. It does **not** touch or redefine the leaf. Its `Z_det` matched port is the *same* real-port fork as above. No `manuscript/ave-kb/` edit is entailed or permitted by this lane.

### 3.3 · What stays byte-untouched

- **`src/ave/thermal/f6_bath_meter.py`** (`LatticeBathCoupler`, `OscillatorBath`) — READ-ONLY (the Phase-0 clamp discriminator overlays a read-only observable; no edit).
- **The K4 engine** (`k4_tlm.py`, `k4_cosserat_coupling.py`, …) — untouched.
- **The #721 / #724 meter certificates** — untouched (the arm is off-instrument).
- **The interacting-bath lane's files** — untouched; the one-line cross-pointer (§0) is the only contact.
- **The canon leaves** `retention-transition-split.md`, `clm-ldmvwi`'s home leaf, the tier-1 charter, and **all files PR #738 touches** — untouched (this is a `research/` SPEC only; no `manuscript/ave-kb/` or `_orchestration/`-substantive edit; the docket append is a union-safe tail entry only, §6).
- **The X40 driver `x40_ring_closure_transient.py`** — this SPEC does **not** edit it either (build-gated); the arm, *if built*, adds a **new** driver reusing it. STOP at the build gate.

## 4 · SPEC (build-gated) — stages, frozen tree, kill-shapes, compute cost

> **BUILD GATE.** Everything below is a design. No code is written, no arm fired. The arm — *if* Grant greenlights — earns its own FROZEN prereg (push-before-code) + verification chain. This lane STOPS here.

### 4.1 · Stages

- **Phase 0 — the clamp discriminator (cheap, read-only, gating the framing).** Overlay the X40 mint-observable (`Λ`-conservation across event + `b_1` + `f_E=1/N`) on the **existing banked meter clamp event** (§2.3). Confirms (a) numerical-guard vs (b) uninvited-click empirically. **No edit** to the meter (read-only observable). Outcome routes the whole arm's framing.
- **Phase 1 — the mint-count arm (the click, on the X40 instrument).** A *new* driver reusing `x40_ring_closure_transient.py`: drive an **ensemble of `M` ring-completions** (fork = Decision 1), record `N_click(t)`, the per-event `Λ`-ledger, and the `f_E=1/N` split. Frozen reads: count monotonicity + per-event `Λ`-conservation.
- **Phase 2 — the discriminators (chord-vs-echo).** (2a) **Loschmidt echo** — time-reverse at window end, evolve back, measure `N_click` un-count. (2b) **`Δω`-invariance sweep** — vary the radiated-bath comb `Δω`; require the count-arrow to be `T_rec`-independent. These two are the decisive gates.

### 4.2 · Frozen-tree sketch (verdict classes — to be frozen in the arm's prereg, NOT here)

```
Phase 0 clamp observable:
  clamp event mints persistent Λ-conserving counted quantity? ── yes ──► REOPEN (b): route to Grant (clamp = uninvited click)
                                                              └─ no ───► CONFIRM (a): clamp = numerical guard [expected]; proceed on X40 instrument

Phase 1+2 (on the X40 instrument):
  per-event Λ conserved (drift ≈ 0)? ─ no ──► MINT-ARTIFACT: the "mint" is numerical, not a click → close negative (Rule 11)
                                     └ yes ─┐
  N_click monotone under forward drive? ─ no ─► NO-RATCHET: no accumulation → click gives no counting arrow → close negative
                                        └ yes ─┐
  N_click un-counts under Loschmidt echo? ─ yes ─► REVERSIBLE-BOOKKEEPING (echo): "arrow" reverses → no chord → close negative (Rule 11)
                                          └ no ──┐
  count-arrow Δω-dependent (tracks T_rec)? ─ yes ─► MODE-SPREAD-CONFOUND: arrow rides the radiated 9/10's mode-spread, not the topological count
                                                    → ROUTE to the interacting-bath lane; do NOT double-claim the mode-spread arrow as the click
                                           └ no ──► CLICK-ARROW-LIVE: a Δω-invariant, Loschmidt-surviving, Λ-exact protected count
                                                    → the click supplies a counting arrow the floor could not (substrate-mechanism / coordinate-class;
                                                       NOT emergence — no CODATA). The strongest honest outcome.
```

### 4.3 · Kill-shapes (what a clean negative looks like — pre-committed, Rule 11)

- **`MINT-ARTIFACT`** — per-event `Λ`-conservation fails. The mint is a numerical event (the clamp's own failure, §2), not a topological click. One mechanism, close the branch.
- **`REVERSIBLE-BOOKKEEPING`** — the Loschmidt echo un-counts the mints. The microdynamics' time-reversibility (§1.3) wins; there is no arrow, only bookkeeping. Clean negative, mechanism named.
- **`MODE-SPREAD-CONFOUND`** — the count-arrow is `Δω`-dependent. The apparent arrow is the radiated `9/10`'s mode-spread (candidate 1) riding on the click event, **not** the topological count. Route to the interacting-bath lane; do **not** refill the click slot with it (Rule 12).
- **`NO-RATCHET`** — `N_click` does not accumulate under forward driving. The completions do not net-mint. Close.

Each kill-shape is a **single mechanism explaining the failure** — the Rule-11 shape. None is a rescue path; the arm banks whichever fires.

### 4.4 · Compute cost

- **Phase 0:** minutes. Reuses the banked meter run + the existing X40 observable; read-only. Effectively free.
- **Phase 1:** the X40 single-ring closure is a small TLM sim (`Λ`-drift `2.2e-16`, sub-second). An ensemble of `M ~ 10²–10³` completions is **seconds-to-minutes** on a laptop.
- **Phase 2:** the Loschmidt echo doubles a Phase-1 run (forward + backward); the `Δω` sweep is `~6–8` comb points × a Phase-1 run. **Tens of minutes**, laptop-scale.
- **No engine build, no meter edit, no GPU.** The whole arm is cheaper than the floor arm (which ran 6-seed ensembles × 6 `ρ` × `11·T_rec` windows). The dominant cost is design rigor (the frozen prereg), not compute.

## 5 · DESIGN-WALK BRIEF for Grant — the decisions only he should make

Four decisions gate the arm. Each is a physics-framing call, not an implementation detail — the implementer must not resolve them by fiat (`feedback_substrate_adjudicates_forks`). Each carries a sit-inside-the-cell picture + the circuit, options bulleted, my rec marked ★.

### Decision 1 — the counting ensemble: what does `N_click` count over?

- **Lattice-first picture.** Sit inside the srs lattice. A driven front sweeps through; bonds close into rings one at a time. Each closure is a *click* — a mesh loop is minted, `1/10` of the donated circulation trapped as a persistent DC loop current, `9/10` radiated as an AC transient into the matched stub-bath. The "count" is: how many rings have closed.
- **Circuit.** Each ring = an LC mesh; completion = the 10th bond's switch closing, minting a conserved flux linkage `Λ = L_bond·i(0)`; the trapped current is a persistent DC mesh circulation (lossless, PRODUCT-latched).
- **Options.**
  - **(1a)** Count `b_1` increments (trapped mesh loops) — the topological PRODUCT counter (protected, monotone, integer).
  - **(1b)** Count radiated-fraction dispersals (`9/10` into the matched bath) — the TRANSITION reconvergence-0 events.
  - **(1c) ★** Count **both** and report the split; the *arrow claim* rests on **(1a)** + `Δω`-invariance, with (1b) reported as the radiated channel.
- **My rec: (1c), arrow on (1a).** Rationale: the `b_1` count is the PRODUCT-lossless topological ratchet (no valve); the radiated `9/10` is where reconvergence-0 lives but that is the *mode-spread* channel — keeping them separate is what prevents double-claiming the mode-spread arrow (candidate 1) as the click. Measuring both lets the `MODE-SPREAD-CONFOUND` gate (§4) actually fire.

### Decision 2 — ★the real-matched-port fork: may the click's arrow invoke a real port?

- **Lattice-first picture.** The radiated `9/10` goes into MATCHED STUBS (`R_rad ≡ Z_0`) — a real port (travelling-wave, `Γ=0`, no return within the window). The meter's Caldeira–Leggett bath is instead LOSSLESS-REACTIVE (recurs at `T_rec`). These are *different bath models*, and the choice decides whether "reconvergence ≈ 0" is a real-port fact or a large-`T_rec` approximation.
- **Circuit.** Matched stub = a resistor equal to the line's characteristic impedance — a real port at the system boundary (Ax3-legal SYSTEM-loss, `retention-transition-split.md:60`); vs the reactive comb = a bank of lossless LC tanks (recurs).
- **Options.**
  - **(2a) ★** The click's arrow *may* invoke the matched real port (`R_rad ≡ Z_0`) — the Ax3-legal radiative boundary, "port-only," not a bulk valve. The radiated `9/10` genuinely does not return; the topological count carries the PRODUCT arrow.
  - **(2b)** The click must stay in the meter's lossless-reactive world (no real port) — the radiated `9/10` recurs, and the *only* arrow left is the topological `b_1` count.
- **My rec: (2a), with the arrow claim scoped.** The matched port supplies reconvergence-0 for the radiated `9/10` (Ax3-legal per the canon's own SYSTEM-loss row — *not* the forbidden bulk valve), while the COUNTING arrow rests on the `b_1` mint count. This is the honest reading of "never a valve": a matched port at the actual boundary is not a bulk diode. **★This is the load-bearing fork** — bears on your PHASE-ONLY / counting epistemology and the "longitudinal scalar is real, no QED-transverse-only garbage" posture. If you rule **(2b)**, the click reduces to the pure topological-count and the matched-stub radiation is out of scope (a cleaner but weaker claim). **Flag-don't-fix: I have NOT resolved this; it is yours.**

### Decision 3 — the Loschmidt gate: is the arrow required to survive time-reversal?

- **Lattice-first picture.** Run the ensemble of completions forward to the window end, then FLIP every `V_inc ↔ V_ref` (native TLM time-reversal), evolve backward. Do the rings UN-close? Does the count come back down?
- **Circuit.** Time-reversal = swapping incident/reflected on every line; a truly reversible LC network retraces; a genuine arrow does not (the dispersed `9/10` cannot reconverge, the trapped `1/10` is protected).
- **Options.**
  - **(3a) ★** GATE the click-arrow on Loschmidt-survival — the count must NOT un-count under reversal within the window.
  - **(3b)** Do not gate on Loschmidt; claim only the WRITE-mechanism coherence (consistency-class, as X40 did).
- **My rec: (3a).** The whole question is whether the click gives an ARROW (chord) or a coherent write (echo). The Loschmidt echo is THE discriminator (`project_ave_chord_north_star`: real chord vs echo — prioritize discriminating tests). Without it the arm is consistency-class only and cannot answer the arrow question. Cost is one extra backward run (§4.4) — cheap insurance against banking an echo as a chord.

### Decision 4 — run Phase-0 clamp discriminator, or trust the three-signature derivation?

- **Lattice-first picture.** Overlay the `Λ`/`b_1` mint-observable on the EXISTING banked meter clamp event (read-only, byte-untouched). Does the clamp event mint a persistent counted quantity + conserve `Λ`?
- **Options.**
  - **(4a) ★** Run Phase-0 (minutes, read-only) — empirically close the "uninvited click?" both-ways question with a receipt.
  - **(4b)** Trust the §2.1 three-signature derivation (clamp fails all three) — skip.
- **My rec: (4a).** It is minutes and read-only, and it converts the §2 adjudication from *derivation* to *receipt* (`feedback_validate_what_you_did`: not done until live-fire has run). Cheap insurance against the consensus-bias dismissal being wrong.

**Summary of my recs (for a fast read):** 1c (arrow on 1a) · **2a (scoped) — the one genuinely load-bearing physics call** · 3a · 4a. Decisions 1/3/4 are low-regret; **Decision 2 is the fork that changes what the click *is*** and should get the walk-the-picture treatment in chat before the arm's prereg freezes.

## 6 · Provenance + verify-before-cite receipts + fences honored

### 6.1 · verify-before-cite receipts (grepped this session, at `origin/main` HEAD `1be045a1`)

- **Tier-1 "never a valve"** — verbatim `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256` "the arrow comes from mode-count or a click, never a valve"; `:176` "The tier-1 ledger must get its arrow from … reservoir mode-count … or a click (X40), never from a valve." ★**Flag (minor):** the task's quoted phrase "arrow from counting, never a valve" is a **faithful paraphrase**, not verbatim — the canon says "**mode-count** or a click." `retention-transition-split.md:31` carries the counting gloss ("admissible **only** from counting"). Recorded, not silently normalized.
- **Retention/transition split** — `manuscript/ave-kb/common/retention-transition-split.md:16` (TRANSITION = crossing arrow, licensed only from counting, never a valve), `:31–:36` (the two counting sources: mode-spread reconvergence≈0 **or** the energy-conserving click (X40)), `:60` (SYSTEM-loss matched-port row, `requires_R = port-only (Ax3-legal)`).
- **`clm-ldmvwi`** — `manuscript/ave-kb/.index/claims.jsonl`: "Born Rule from Ohmic Measurement Work", `canonical_path: vol1/claim-quality.md`, `canonical_anchor: born-rule-from-ohmic-measurement-work`, solidity **0.65**, build_status **"ok to build on, see caveats"**. Capture chain step (4): "Joule extraction `W(t) = ∫ V²/Z_det dt`." READ-ONLY; consumed as the detector-capture definition, not edited.
- **X40 click canon** — `research/2026-07-10_x40-ring-closure-transient_result.md`: `f_E` trapped `= 1/10`, radiated `9/10`, `Λ`-drift `2.2e-16`; cut/cycle Hodge split (T-even 9/10, T-odd 1/10, `b_1=1`); "Trapping occurs ONLY at discrete ring-COMPLETION events … a conserved mesh quantity is MINTED"; CONSISTENCY-class ("does NOT prove the bias is real").
- **The clamp** — `research/2026-07-18_f6-certified-kappa-sweep_result.md` R-2: `scale = √(max((E_lat − d_e_bath)/E_lat, 0))` hard-zeroes `E_lat` (absorbing state); dead combs 89%/84% NO-INFORMATION; conservation drift "largely clamp-created." `research/2026-07-19_f6-no-discharge-scan_INSTRUMENT-INCOMPATIBLE.md` §5: quasi-continuum threshold and full-discharge/clamp coincide; "the clamp is the instrument faithfully reporting that the lattice fully drained."
- **Floor arm (the structural wall)** — `research/2026-07-19_f6-thermal-floor-arm_result.md` §0(b): the reactive-floor arrow mechanism is "STRUCTURALLY INEXPRESSIBLE on a non-interacting bath … identity-class" (the #721-W2 shape). §4 follow-ons name the two open candidates: interacting-bath thermalization (candidate 1, separate lane) and the X40-class click (candidate 2, this lane).

### 6.2 · Discipline skills applied (`feedback_skill_selection_planning` retro-pass)

`substrate-native-check` (§0 K4/Cosserat/Op14/phase-space walk — cycle-space mint ≠ (2,3) charge; sector-ownership guarded) · `phase-space-coordinate-check` (§0/§3 — count/`Λ` coordinate, not the floor's revival coordinate; the A46 fix) · `consistency-vs-emergence` (§0 — CONSISTENCY-class mint; no emergence promotion; strongest reachable = coordinate-class) · `verify-before-cite` (§6.1 receipts) · `consensus-bias-symmetric-standard` (§2.2 steelman of clamp-(b)) · `pre-test-physics-check` (surfaced Decision 2, the real-port fork, to Grant BEFORE the arm's design freezes) · flag-don't-fix (Decision 2 unresolved; the tier-1 paraphrase; the #738-docket overlap below).

### 6.3 · Fences honored

- **No `manuscript/ave-kb/` or tex-volume edit** — this is a `research/` SPEC only. `clm-ldmvwi` and the canon leaves are READ-ONLY.
- **No engine/meter edit** — `f6_bath_meter.py`, the K4 engine, and `x40_ring_closure_transient.py` are untouched (build-gated; Phase-0 is a read-only overlay design).
- **No files PR #738 touches** — verified against #738's file list (KB leaves + ratings map + docket). This SPEC touches none of them **except** the union-safe docket tail-append (§6.4), which is the merge-driver-designed exception. ★**Flagged for the orchestrator** below.
- **No duplication of the interacting-bath lane** — one-line cross-pointer only (§0); the `MODE-SPREAD-CONFOUND` gate routes *to* that lane rather than absorbing it.
- **`make verify` green** — the precommit hook gated each commit.

### 6.4 · ★Flag-don't-fix — the PR #738 / rulings-docket overlap (surfaced, not resolved)

The task's deliverable "dated docket append (union-safe)" targets `_orchestration/2026-07-10_rulings-docket.md`, which carries `merge=union` in `.gitattributes` (PR #737's union-merge extension — designed so concurrent lanes append at the tail without conflict). **PR #738 ALSO modifies that docket** (`+24` lines). The fence "no files PR #738 touches" and the "union-safe docket append" instruction are in **tension**; the union-merge driver **resolves it mechanically** (both tails concatenate, no conflict), which is precisely why #737 landed. Disposition (flag-don't-fix): I append a **minimal, dated, tail-only** pointer entry to the docket (union-safe), and surface this overlap here + in the final report for the orchestrator to adjudicate. I did **not** edit any substantive content #738 changes.

---

*This is a DESIGN + ADJUDICATION document. Verdict: **the click can source the local arrow in a coordinate (topological count) the floor's barred coordinate (modal phase) was not** — but only as a Loschmidt-class counting arrow whose chord-vs-echo status is undecided until the SPEC'd arm runs its Loschmidt + `Δω`-invariance gates. **The meter's clamp is a numerical guard (a), not a derivable click** — it fails all three positive click signatures; #726's NO-INFORMATION reading stands; the steelman of (b) routes to the interacting-bath lane, not the click. **Nothing built, nothing fired, nothing banked at emergence-class.** The arm, if greenlit, earns its own frozen prereg + verification chain.*
