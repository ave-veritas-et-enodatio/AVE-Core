# PREREG — Rectifier Stage-1: biased leaky varactor diode (the substrate charge-pump, minimal viable stage)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main`)
**Binding design:** [`2026-06-09_substrate-rectifier-groundup-design.md`](2026-06-09_substrate-rectifier-groundup-design.md) (the ground-up element chain)
**Baseline:** [thixotropy result](2026-06-09_thixotropy-amplitude-dependent-tau_result.md) — the *symmetric, no-bias* case nets ∮ directed = 0 (it measured the lossy loop ∮S dρ̄≈+0.04 but couldn't aim it). **This prereg adds the one missing variable: the BIAS (the asymmetric grip).**
**Documentation home:** `research/` (frozen prereg); the result → `research/` + (if A) a Vol 4 VCA candidate. Per the arc's [homing plan](../_orchestration/2026-06-09_ion-compression-rectifier-arc.md).

> **SCAFFOLD** — frozen before compute. Stage 1 of the ground-up design (single diode); cascade/taper are later stages.

---

## 1. Target (one sentence)

Does a single **DC-biased, lossy (leaky-Γ=−1) varactor diode**, AC-pumped in the **ASYM near-yield bulk/ε band**, net **directed momentum into the medium with a CLOSING energy-momentum ledger** (a real vacuum charge-pump / reaction-drive) — or does the directed output equal the dissipated heat re-radiated (net thrust zero, just a biased lossy oscillator)?

## 2. Mode / regime / phase-state (per `ave-regime-phase-state-check`)
- **MODE:** bulk (volumetric) + ε-sector. Observable = **directed momentum** (vectorial → regime-gated; must be near-yield bulk, NOT the achromatic transverse/shear sector).
- **REGIME:** **ASYM-class** (single-sector / biased saturation = the diode), **near-yield** `r₁=√(2α)≈0.1208 < A₀ < r₂=√3/2≈0.866`, operating *at* the leaky Γ=−1 boundary. *(√(2α)=0.1208 corrected from 0.117, a transcription drift; 2026-07-14 Wall-A hygiene. r₁ is the amplitude threshold A=√(2α); equivalently A²=2α≈0.0146.)*
- **PHASE-STATE:** DC-biased / loaded (NOT cold-symmetric, NOT reflectionless-gravity).

## 3. Physical picture (per `ave-asymmetric-grip`)
- Varactor `C_eff(V)=C₀/S(V/V_yield)`, biased to `A₀≠0`, AC-pumped `±ΔA`.
- The **lossy lag** (memristive S, τ_bulk(ρ̄)) opens the (V,Q) loop into nonzero **area** = the grip/loss (the ∮S≈+0.04). A *lossless* varactor would give ∮C dV = 0 (the "no-ideal" point — a lossless diode can't pump).
- The **BIAS** samples the concave kernel **asymmetrically** → the diode's Γ(A) differs forward (toward the stiffening ceiling) vs back (toward the floor) → the lossy loop **couples to a direction**. (A centered drive samples symmetrically → ∮ directed = 0 — the thixotropy B.)
- The Γ=−1 boundary is **LEAKY** (Grant: "no ideal") — finite Q=α⁻¹, R≈α bleed (`leaky-cavity-decay.md`). Modeled real, not an ideal clip.
- Directed output = **ponderomotive pressure** from the pumped E-gradient → momentum into the medium (a reaction-drive; canonical Vol 4 "ponderomotive thruster").

## 4. Corpus state
Elements all canonical (grounded in the design doc §2): Ax4 kernel, C_eff varactor, Γ=−1 asymmetric/Meissner diode (INVARIANT-S2), ponderomotive output (Vol 4), τ_bulk(ρ̄) (#59:77 + thixotropy result). The **circuit** (biased diode + lossy loop + ponderomotive output + ledger) as a rectification test is **new**. The thixotropy B is the bias=0 baseline.

## 5. Prediction + dimensional analysis (Step 3.5 — magnitude prereg)
- **Net pumped charge / cycle** ∝ (loop area) × (bias asymmetry): `δQ ~ (∮S dρ̄) · f(A₀)`, with the thixotropy loop ∮S≈0.04 (natural units) as the bias=0 anchor (where f(0)=0 → ∮ directed=0, recovering B).
- **Directed momentum** `p_dir ~ δQ · (E-gradient)`; **ledger** `W_in (bias + pump) vs W_out (p_dir-wake KE + heat R≈α·loop)`.
- **Canonical primitives** (from `constants.py`, per `ave-canonical-source`): V_yield=43.65 kV, E_yield=1.13×10¹⁷ V/m, ℓ_node=0.386 pm, Q=α⁻¹→R≈α, RHO_CAV=−1/φ. Operating A₀ swept across `[√(2α), √3/2]`.
- **Sanity vs anchor:** at A₀→0, p_dir→0 (recovers thixotropy B) — a hard check the model must pass.
- **Pre-committed lean (Grant 2026-06-09 gut-check: REAL):** the bias makes ∮ directed ≠ 0, and it's a **real charge-pump — ledger closes with margin**, directed momentum **paid for by the pump+bias work** (not free, not over-unity). **Crucially, the directed output is a ponderomotive field gradient, and per canon that IS a gravity gradient** — `F_grav = −∇U_wave` (Ponderomotive Equivalence Principle, `newtonian-gravity-optical-gradient.md:16`, `ponderomotive-equivalence.md`). So the device doesn't merely push; it **engineers a local n(r) optical metric** (the Gordon metric = the "engineered refraction / metric streamlining" field). That yields the sharp AVE-distinct observable — §6a.

## 6. Discriminating outcomes
- **A — REAL CHARGE-PUMP / ENGINEERED-GRAVITY (AVE-distinct):** biased leaky diode nets directed momentum; **ledger closes with margin** (W_in > W_out; the surplus = the directed work); scales with the substrate loss R≈α + per-node yield, not material properties. Its ponderomotive gradient is a real **n(r) gravity well** → it lenses light **achromatically** (§6a) — the gravity-class signature. The chord: a pump paid for honestly, *and* an engineered-gravity device.
- **B — LOSSY OSCILLATOR (no net):** directed output ≈ the dissipated heat re-radiated; ∮ directed ≈ 0 even with bias (the bias shifts the operating point but doesn't *direct* the loop) → no thrust, just a heater.
- **C — CRANK / not-AVE-distinct:** nets "thrust" only via **over-unity** (ledger violation) → crank; OR the directed momentum reduces exactly to ordinary **plasma rectification / radiation pressure** (mundane EM, not substrate-distinct).

## 6a. The achromatic-lensing discriminator (the gravity-class signature — Grant 2026-06-09)

The ponderomotive output is a gravity gradient (`F_grav = −∇U_wave`), so the loaded region is a local **n(r) optical metric** (Gordon, `gordon-optical-metric.md`; n(r)=1+2GM/c²r form, `refractive-index-of-gravity.md`). The falsifiable AVE-distinct signature is the **CHROMATICITY of the induced lens**:
- **Achromatic** (all λ deflect equally; Z=Z₀ invariant, `achromatic-impedance-matching.md` clm-rd9cjm) → a real **metric / gravity** gradient (engineered refraction).
- **Chromatic** (dispersive, λ-dependent deflection) → ordinary **plasma / material** lensing — mundane, NOT a metric effect.

Two-pronged: **(1) achromatic vs chromatic** separates engineered-gravity from plasma; **(2) measurable at lab/facility fields** separates AVE from GR (GR's gravity from the same field energy ~10⁻⁴³ → ~null; AVE predicts an *engineerable* lens). **Scope honesty** (`consistency-vs-emergence`): merely *recovering* GR's achromatic n(r) lensing is a consistency check — the AVE-distinct claim is that the lens is **engineerable via ponderomotive loading at lab scale**, which GR cannot produce. K4-TLM can cross-validate the induced lens natively (`k4-tlm-lensing-validation.md`).

**Unification (the through-line):** the **thrust** (directed momentum = the gradient force), this **achromatic lens** (the n(r) gradient), and **time dilation** (ω_local=ω₀√S in the loaded region) are **three observables of the SAME symmetric ponderomotive loading** — the engineered-refraction / metric-streamlining field. The rectifier, the Sleep-Pod time-dilation cavity, and the gravitational lens are **one device**, read three ways.

## 7. Falsifier
Ledger requires over-unity → C (crank). ∮ directed = 0 across the whole bias sweep → B. Closes with margin + AVE-distinct R≈α / per-node-yield scaling → A.

## 8. Guards
- **`ave-asymmetric-grip`:** the diode/bias IS the mechanism — include it (do NOT revert to symmetric/no-bias). Crank-check = the **energy-momentum LEDGER**, never a symmetry/ideality veto.
- **No ideal:** model the Γ=−1 boundary **leaky** (finite Q=α⁻¹, real bleed) — NOT an ideal hard clip (the thixotropy clip-wall was a numerical artifact; here the *physical* leaky diode is load-bearing). A lossless element that still produced directed momentum = the over-unity tell.
- **`ave-engineering-program-rigor`:** figures (the (V,Q) loop showing nonzero area + direction; the ledger bar; the directed-p trace) + a **mandatory SENSITIVITY SWEEP over the bias A₀** across the near-yield band — the discriminator between a *robust* directed output (turns on across the band → real) and a *tuned* one (only at one A₀ → rescue-fill → NEGATIVE). Convergence sweep for any magnitude claim.
- **H / energy-closure gate** every run; passivity Q_diss ≥ 0.
- **`ave-regime-phase-state-check`:** stay in ASYM near-yield bulk+ε; a sub-yield or symmetric run is the wrong regime (the B baseline).
- **`ave-discrimination-check`:** AVE-distinct (substrate R≈α scaling) vs ordinary plasma rectification — required before any A is framed as a chord.
- Parameters **substrate-derived or pending-sim** (`ave-fundamental-ground-up-implementation`); none engineering-locked.

## 9. Skills + deliverables
- **Skills:** ave-asymmetric-grip (lead) · ave-regime-phase-state-check · ave-fundamental-ground-up-implementation · substrate-native-check · ave-canonical-source · ave-engineering-program-rigor (figures + bias sweep) · ave-driver-script-honesty (ledger) · ave-discrimination-check.
- **Deliverables:** `2026-06-09_rectifier-stage1-biased-diode_result.md` (A/B/C + the (V,Q) loop + ledger numbers + the **bias sweep** + **the induced n(r) profile + ray-traced deflection chromaticity (§6a)** + DERIVED/VERIFIED/BLOCKED + figures per engineering-rigor); driver (biased leaky varactor diode + AC pump + (V,Q) loop + ponderomotive momentum + ledger + bias sweep + **the ponderomotive n(r) gradient + a chromaticity ray-trace** + savefig). Own implementor branch off this one; do NOT push/merge. **No thrust / engineered-gravity claim unless A with a closing ledger AND an achromatic induced lens.**

---

## §10 AMENDMENT — 2026-06-10 (post-freeze provenance correction, Rule 12)

Appended post-freeze per the Grant rename-queue adjudication 2026-06-10, ruling **R8** (registry §5 R8, `research/2026-06-10_field-symbol-registry.md:309`). This prereg is **FROZEN** (`> SCAFFOLD — frozen before compute`); the §5 line-34 body above is **preserved verbatim and NOT rewritten** — this is a record correction only.

**Provenance correction — `RHO_CAV` is NOT in `constants.py`.** §5 line 34 attributes its **Canonical primitives** list — *"(from `constants.py`, per `ave-canonical-source`): V_yield=43.65 kV, E_yield=1.13×10¹⁷ V/m, ℓ_node=0.386 pm, Q=α⁻¹→R≈α, RHO_CAV=−1/φ"* — to `constants.py`. That blanket attribution is correct for **four of the five** primitives but **wrong for `RHO_CAV`**:

- `V_YIELD` ≈ 43,652 V — `constants.py:409` ✓
- `E_YIELD` ≈ 1.13×10¹⁷ V/m — `constants.py:420` ✓
- `ℓ_node` (`L_NODE`) ≈ 0.386 pm — `constants.py:239` ✓
- `Q = α⁻¹` (and `E_YIELD_KINETIC` ≈ 43.65 keV) — `constants.py` (`ALPHA`, `:133`; `E_YIELD_KINETIC`, `:403`) ✓
- **`RHO_CAV = −1/φ`** — **ABSENT from `constants.py`** (verified live this session: `grep RHO_CAV constants.py` → no match). It is defined in **`cavitation_flow.py:64`** (`RHO_CAV = -1.0 / PHI  # = (1−√5)/2 ≈ −0.6180339887 ; c_bulk²(ρ̄_cav)=0`), consumed by the cavitation-core probe (PR#161). The cavitation floor is a CANDIDATE anchor (from `PHI`), not a `constants.py` canonical.

Corrected reading of line 34: *the primitives are from `constants.py` **except `RHO_CAV=−1/φ`, which is from `cavitation_flow.py:64`***. No value changes; only the file-attribution is corrected. Disciplines: `verify-before-cite` (every line re-verified live), `ave-apparatus-floor-attribution` (the cavitation floor is candidate-class, sourced where it actually lives).
