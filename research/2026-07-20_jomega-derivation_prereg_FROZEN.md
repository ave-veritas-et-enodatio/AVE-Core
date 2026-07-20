# PREREG (FROZEN) — J(ω) derivation: the z=3 bath spectral density as the yield-fork adjudicator

> **SECTOR HEADER (read first).**
> - **MODE:** derivation + research-driver (0D ODE-level; explicit-bath GLE). Object = the z=3 srs bath spectral density `J(ω)` for the near-yield transverse-bow coordinate `S`, and the per-cycle energy ledger at the near-yield crossing. NOT a minimization, NOT continuum-Helmholtz, NOT an engine change.
> - **REGIME / PHASE-STATE:** near-yield crossing, Regime II→III (`k4_tlm.py:308–311`), driven time-domain, `A = V/V_SNAP → 1`. Cold-linear band structure of the *bath* (the z=3 srs net); saturation enters only as the Op14 reactance grading that couples `S` to the bath.
> - **SECTOR:** the load coordinate `A` = axial A1 dilatation (V-sector); the response `S` = transverse **T2** bow. **A1 ⊥ T2** (sector-ownership guard; this `S` is the mechanical bow, NOT the Cosserat (2,3) charge winding).
> - **DISCIPLINE:** freeze-by-push BEFORE any computation. Every step tagged **[DERIVED]** / **[ENGINE-READ]** / **[IMPORTED]** / **[ASSUMED]** / **[CALIBRATION-TAGGED]** with provenance. Verify-before-cite (grep-verified at HEAD `64f1894d`). Flag-don't-fix. Rule-11 (the frozen tree governs the verdict; findings do not retro-edit it). Rule-12 (falsification retracts, does not refill). Anti-seduction fence BOTH directions (world (a) flatters Grant's reversible-reactive lean; world (b) flatters the Op3-transduction narrative — the frozen tree adjudicates, not the story).

**Date:** 2026-07-20 · **Lane:** implementer, J(ω) derivation (yield-fork adjudicator; Grant dispatch 2026-07-20 "1. fire") · **Branch:** `research/jomega-derivation` · **Base HEAD:** `64f1894d`.

---

## 0. What this prereg freezes and why it exists

The RE-BANKED verdict of `research/2026-07-19_flag-f-s-dynamics-derivation.md` §0 left the near-yield (a)/(b) fork **OPEN pending `J(ω)`** — the z=3 bath spectral density, "never computed" (F13, R-6). The routed follow-on (verbatim, that doc §0/§23):

> *"Derive `J(ω)` from the K4/z=3 bond couplings `c_j`, evaluate `Γ = πJ(ω_drive)` and the per-cycle loop at the crossing, and combine with the §5.1 shape-class discriminators."*

This lane executes that. It also resolves that doc's flagged internal inconsistency: **§4.3 uses `Γ = πJ(ω→0)`; §5.3 uses `Γ = πJ(ω_drive)`** — two different physical objects conflated under one symbol (§4 below states both cleanly).

**The three-way loss-location contradiction this adjudicates** (all three grep-verified at HEAD, verbatim below):
- **Site 1** — `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:358` (already fork-open-caveated at `:338–339`): *"At `f ≪ 1/τ_relax`, complete yield and recovery occur within each cycle, producing **maximum hysteresis loss**."* → **max loss at f≪1/τ.**
- **Site 2** — `manuscript/backmatter/06_spice_verification_manual.tex:147–148`: *"At any practical SPICE simulation frequency (`f ≪ 7.8×10²⁰ Hz`), the lattice responds purely elastically---the hysteresis loop has **zero enclosed area**."* → **zero-area elastic at f≪1/τ.**
- **Site 3** — `#735` Leg B (`research/2026-07-19_yield-fork-discriminators_result.md:19,81`): the (V,I)-plane loop-area **peaks at `ωτ=0.911`, INSIDE `[0.85,0.95]`** — a Debye/rate-dependent lag peaking at `ωτ≈0.9`.

These three functional forms for `loss(ω)` are mutually exclusive: monotone-max-at-DC (Site 1) vs zero-at-DC (Site 2) vs peaked-at-ωτ≈0.9 (Site 3). `J(ω)` decides which is right in which regime.

---

## 1. THE LOAD-BEARING CORRECTION (frozen before computation): the band edge is NOT ω_C

`research/2026-07-19_flag-f-s-dynamics-derivation.md` §4.2 assumed the z=3 bath band edge is `ω_max ~ c/ℓ_node = 1/τ_relax = OMEGA_C` (i.e. `ωτ_max = 1`), and built the band-edge step (CRITICAL F1/F11) on it: it placed the crossing (`ωτ≈0.9`) *near the band edge*.

The **corpus-ADJUDICATED** band model (`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`, `clm-bnd5rq`, gates PASS #604/#607) is the **arccos transmission-line map**, `ω_n(k) = ω_link·arccos(μ_n(k)/3)`, `ω_link = √3·ω_C`, with scalar **band top `π√3·ω_C ≈ 5.4414 ω_C` at H** — NOT `ω_C`. **[ENGINE-READ / CANONICAL]**

**Consequence, frozen as the pivot of this derivation:** in `ωτ_relax` coordinates (`τ_relax = 1/ω_C` native), the bath band spans `[0, π√3] ≈ [0, 5.44]`. The near-yield crossing at `ωτ ≈ 0.9` sits **deep INSIDE the band** (`0.9 ≪ 5.44`), at ≈1/6 of the band top — NOT near the edge. So `J(ω_drive)` at the crossing is **not band-edge-suppressed**; whether it is *appreciable* is a shape question the DOS decides (§2). This corrects the flag-F doc's factor-of-~5.4 band-edge underestimate and is the reason the fork is genuinely live rather than trivially world-(a).

---

## 2. The derivation objects (frozen definitions — no post-hoc convention shift)

**Caldeira–Leggett bilinear bath** (`flag-f` §4.1, [DERIVED form]): `H_int = −S·Σ_j c_j q_j`, bath oscillators `q_j` at `ω_j`. Spectral density (standard CL convention, frozen):

```
J(ω) ≡ (π/2) Σ_j (c_j² / (m_j ω_j)) δ(ω − ω_j)  →  (continuum)  (π/2)·g(ω)·[c(ω)²/(m(ω) ω)]
```

- `g(ω)` = the z=3 srs **density of states** [DERIVED from the arccos band, computed by dense BZ histogram; the simple cosine chain is the robustness contrast].
- `c(ω)` = the S→bath **coupling**; its ω-scaling is the one genuinely unforced modeling choice (§3) → both models run, UNDETERMINED fail-close on the parts that differ.

**Friction kernel & the two Γ objects** (resolves the §4.3/§5.3 inconsistency, frozen):
- **Markovian friction CONSTANT** (the ω→0 object, §4.3's `πJ(ω→0)`): `γ_0 ≡ lim_{ω→0} J(ω)/ω`. This is the DC friction that would appear in the overdamped first-order Eq 2.1. It governs ONLY the slow limit `ωτ≪1`.
- **Per-cycle transduction at finite drive** (the finite-ω object, §5.3's `πJ(ω_drive)`): the energy dissipated into resonant bath modes per cycle at drive `ω_d` is `ΔE_cycle = π S_0² J(ω_d)` [standard bilinear-bath result]. It requires REAL bath modes at `ω_d` to absorb into; `J(ω_d)` counts them.
- **These are DIFFERENT physical objects** (a DC-limit constant vs a finite-frequency per-cycle transfer), both legitimately written `πJ(·)` but evaluated at different arguments because the friction is frequency-dependent. The flag-F doc's error was treating them as one `Γ`. The crossing verdict uses `J(ω_drive)`; the Eq-2.1-recoverability uses `J(ω→0)`.

**Low-ω exponent `s`** (`J(ω) ∝ ω^s` as ω→0): `s=1` Ohmic (γ_0 finite, Eq 2.1 recoverable) / `s>1` super-Ohmic (γ_0=0, no DC friction, Eq 2.1 NOT recoverable as friction-relaxation) / `s<1` sub-Ohmic. To be read off, per coupling model.

---

## 3. The coupling model — the one unforced choice, both run, fail-closed on the difference

`S` modulates `Z_eff = Z_0/√S` (Op14, `k4_tlm.py:315,318,362`; `universal_operators.py`), so the bond reflection `Γ_bond = (Z_B−Z_A)/(Z_B+Z_A)` (`k4_tlm.py:440`) couples `S` to the neighbour bond waves. **[ENGINE-READ]** Whether the linearized S→mode coupling is **on-site** (constant `c(ω)`) or **strain/gradient** (`c(ω) ∝ k ∝ ω` on the acoustic branch) is not fixed by the constitutive form alone:

- **Model C1 (on-site):** `c(ω)=const` ⇒ with 3D acoustic `g(ω)∝ω²`, `J(ω) ∝ g/ω ∝ ω` → **Ohmic (s=1)**.
- **Model C2 (strain/gradient):** `c(ω)∝ω` ⇒ `J(ω) ∝ g·ω²/ω ∝ ω³` → **super-Ohmic (s=3)**.

Both are computed. The **ROBUST** conclusions are what BOTH share; the coupling-scale prefactor (which sets the damping ratio `ζ` and hence the (a)/(b) *magnitude*) is genuinely unforced without a full engine coupling derivation and **fails-closed to UNDETERMINED on the magnitude** (§5 bin C), with the choice surfaced. Note: the S-bow is an *internal transverse deformation* (buckling response), so it is not a rigid translation — on-site coupling (C1) is not forbidden by translation invariance; both models are physical candidates.

---

## 4. FROZEN DECISION TREE (Rule-11: this governs the verdict)

**Coordinates:** `ωτ_relax = ω/ω_C` (native, `τ_relax = 1/ω_C`). Band = `[0, π√3] ≈ [0, 5.44]`. Crossing `ωτ_drive ≈ 0.9` (the `#735` (V,I) datum). Normalized shape `J_norm(ω) ≡ J(ω)/max_ω J(ω)`.

### (i) World (a) — REACTIVE / lossless refusal — requires ALL of:
- **(a-shape):** `J_norm(0.9 ω_C) < 0.1` — the per-cycle transduction at the crossing is suppressed an order of magnitude below the band-interior peak (either the drive is above the band edge — FALSE here, edge=5.44 — or super-Ohmic suppression holds it down at 0.9 ω_C).
- **(a-ledger):** the 0D explicit-bath GLE energy ledger at the crossing shows net per-cycle transfer into the bath **RETURNS within the recording window** (Poincaré-bounded), and the net-per-cycle transfer `< tol` (adopting `#735` Leg B `tol = 3.53×10⁻³` relative, `result.md:75`).

### (ii) World (b) — TRANSDUCTIVE / finite per-cycle loss — requires BOTH of:
- **(b-shape):** `J_norm(0.9 ω_C) ≥ 0.1` — finite `Re(J)` at the crossing ⇒ a live resonant-absorption channel.
- **(b-ledger):** the open-bath (dense-continuum-limit) GLE ledger shows **monotonic net per-cycle transfer ≥ tol** NOT returned within a sub-recurrence physical window.

### (iii) DEGENERATE / UNDETERMINED — fail-closed here if EITHER:
- **(c-magnitude):** `J` finite at the crossing (channel open by shape) but the (a)/(b) *magnitude* split hinges on the un-forced coupling-scale prefactor `ζ` (Model C1 vs C2 differ, or the absolute `c(ω)` scale is not engine-derivable) → UNDETERMINED **on the (a)/(b) magnitude**, coupling choice surfaced; the SHAPE conclusions still stand.
- **(c-scope):** the verdict SCOPE-SPLITS — 0D finite-cell reactive-return (a-character) vs infinite-lattice transductive (b-character) — in which case **report the split explicitly**, do NOT force a single bin.

### (iv) Per-cycle GLE loop protocol (frozen):
- **Drive** (matched to `#735` Leg B, `result.md:33`): `r(t) = 0.7 + 0.3·sin(ω_d t)`, `ω_d = 0.9 ω_C` native. `S_eq(r) = √(max(0,1−min(|r|,1)²))` **byte-locked to `k4_tlm.py:283`**. Also sweep `ωτ ∈ logspace(0.05,10)` for the loss(ω) shape.
- **Bath:** explicit `N`-oscillator realization sampled from the srs scalar arccos DOS (dense discretization of `g(ω)`), coupled bilinearly, `c_j` set by the chosen `J(ω)` model (C1 and C2 both). System+bath integrated as one Hamiltonian ODE (symplectic) — energy-exactly-closed by construction, so the ledger is trustworthy.
- **Mode-resolved ledger:** `E_S(t)` (kinetic+potential), `E_bath(t)` (total AND per-mode), net-per-cycle transfer, Poincaré recurrence (finite bath) vs monotone drain (dense bath). Both the C-state (`S`/reactive-potential) and the reactive pair are recorded over the whole window (reactance-pair-tracking discipline).
- **Contrasts (closes `#735` C-3 owed item, `PROTOCOL-COMPLETION:82`):** on the identical drive, run (1) first-order Eq 2.1 (byte-locked), (2) the second-order reactive form `S̈ + γ Ṡ + ω_S²(S−S_eq)=0` in the `γ→0` lossless limit — compare loop shape, peak `ωτ`, and H-ledger. The flag-F doc predicts (1)=Debye-monotonic-lag, (2)=Lorentzian-resonance-with-180°-inversion.

### (v) Precedence + FLAG-to-Grant:
- The frozen tree governs the verdict (Rule-11); findings do not retro-edit the bins. The (a)/(b) fork **RULING stays Grant's**; this lane delivers `J(ω)`, the ledger, and the frozen-bin classification. Loss-location contradictions are **FLAGGED verbatim + file:line, not silently resolved** — routed to Grant/auditor (flag-don't-fix). Anti-seduction fence held both directions. Engine byte-UNTOUCHED (research driver only). If the derivation forces the `I_S` kinetic-term provenance (flag-F R-5), that is noted; scope is NOT stretched to close it if it stays open.

---

## 5. Batched secondary task (frozen) — arccos drag-onset ratio

Re-derive the minimum phase velocity / drag-onset ratio `v_{p,min}/c_ch` on the corpus-ADJUDICATED **arccos** TL map (`srs-band-structure.md`, `clm-bnd5rq`), replacing/scoping the **cosine-branch `2/π`** carried (cosine-scoped) in the merged `#741` (`research/2026-07-19_deep-space-band-map_derivation.md` §3.3, §5-D4). Frozen deliverable: the arccos-map `v_{p,min}/c_ch` value (computed on the srs acoustic branch AND on the 1D-chain arccos analog) + a verdict on **whether `2/π` survives** the model switch. Owed KB-caveat-update pointer fenced (no KB edits this lane).

---

## 6. FORM/VALUE + consistency-vs-emergence ledger (frozen tags)
- `J(ω)` SHAPE (Ohmic/super-Ohmic, band edge, peak location): **[DERIVED] MANIFESTATION** (theorem of the arccos band + coupling model). No CODATA on the verdict path.
- Band edge `π√3 ω_C`, `ω_C`, `τ_relax`: **[CALIBRATION-TAGGED]** (calibrated via `ℓ_node ≡ λ̄_C`; consistency-class, not headlined as emergent).
- `v_{p,min}/c_ch`: **[DERIVED] MANIFESTATION**, dimensionless, `ℓ_node`-free.
- The GLE ledger's per-cycle transfer *fraction*: **[DERIVED]** shape; its absolute `ζ` prefactor **[UNDETERMINED / coupling-scale]**.

---

*Frozen 2026-07-20 by Opus 4.8 (implementer lane) per Grant's J(ω) dispatch. Pushed before any computation. Verify-before-cite at HEAD `64f1894d`. Anti-seduction fence both directions. Engine byte-untouched.*
