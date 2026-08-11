# THE 𝒜_g DERIVATION (R46 DERIVE-FIRST) — RESULT

**Date:** 2026-08-10 · **Branch:** `lane/2026-08-10-ag-derivation` · **Base:** `origin/main` @ `8424995f`
**Frozen prereg:** [`2026-08-10_ag-derivation_prereg-FROZEN.md`](2026-08-10_ag-derivation_prereg-FROZEN.md), committed ALONE + pushed at `ee728d89` (freeze-by-push) before any driver code, consumer arithmetic, or 𝒜_g number existed. Byte-untouched since.
**Driver:** [`research/drivers/ag_derivation_lane.py`](drivers/ag_derivation_lane.py) → [`ag_derivation_lane_results.json`](drivers/ag_derivation_lane_results.json) + [`ag_derivation_lane_number_check.py`](drivers/ag_derivation_lane_number_check.py) (`--mutation-receipt` fires; auto-discovered by the `make verify` umbrella). Two full runs byte-identical (sha256 `2a2160fd…`).
**Class:** DERIVATION-ADJUDICATION. **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, or ruling; changes no solidity; all propagation ROUTED.** Engine `src/ave` byte-untouched (`git diff --stat 8424995f..HEAD -- src/` empty; backreaction.py consumed READ-ONLY + run, per the brief's stencil-lens fence).
**Lane brief:** [`_orchestration/2026-08-10_ag-derivation-brief.md`](../_orchestration/2026-08-10_ag-derivation-brief.md) (R46).

**Instrument deviations, disclosed FIRST (direction-of-effect stated):** (1) The prereg's G-C3 wording keyed on profile fits ("f measured with fit receipts…"); the site-averaged profile fit on the native operator turned out PARITY-CLASS CONFOUNDED — a point source feeds exactly one of 16 decoupled sublattice classes (interior zero-fraction measured `0.93752 ≈ 15/16`; the sourced-class fit inflates by the measured `15.5–15.7 ≈ 16×` = 1/class-fraction), consistent with the corpus's own banked exposure note on this stencil (`master-equation.md:113`: *"diamond `TETRA_OFFSETS` `L_D` nullspace-heavy / sublattice-decoupled"*). The load-bearing chain receipt was therefore taken from the **exact discrete Gauss-flux identity** (`Σ_ball L·ε = Σ_ball T₀₀`, exact by adjointness, stencil-independent; measured ratio `1.0` machine-exact point / `1.0000034` blob) with the profile fits retained as DIAGNOSTIC-ONLY. Cross-receipt closing the loop: the smooth BLOB feeds all 16 classes and its site-averaged fit lands `b/b_bare-GF = 0.951 ≈ 1` — the ×16 appears exactly when and only when the sublattice mechanism predicts it. Direction-of-effect: STRENGTHENS (an exact identity replaces a confounded fit; both fits are still reported). (2) The frozen "point + blob" runs were executed as: point via `relax_finite_core_strain` (the Stage-1 entry the two-way loop wraps) + blob via the full two-way `solve_backreaction` (`source_mode="komar"`, converged, `max_A = 1.07e-2` linear-regime) — together covering the frozen configuration set, disclosed here. (3) GNU grep absent on this host; sweep engine 1 = BSD `grep -rniE`, engine 2 = Python `re` (inherited disclosure; engines agreed on presence/absence for every pattern).

---

## §0 — REGIME / SECTOR / PHASE-STATE (prereg SVA §0 governs; restated)

**MODE** — over-determination adjudication of one constant (𝒜_g). **SECTOR** — A1 bulk/dilatation slot; dress `u₀` and grade `ε₁₁` are TWO OBJECTS, named per use; T2/Cosserat untouched. **REGIME** — all consumers read crystalline cold-linear Regime-I, exterior D→1; the C3 lattice legs measured `max_A ≤ 1.1e-2` (linear ✓). **STENCIL** — `backreaction.py` is a CONSUMER, not an adjudicator; no engine file edited.

---

## HEADLINE

> **🔴 VERDICT (per the frozen §4 grammar, mechanically applied): `OVER-DETERMINATION-FAILS` — the receipted consumers DISAGREE on 𝒜_g by exactly 4π. BC-SRC's internal falsifier has fired; the lane STOPPED at the frozen rule and routes to Grant immediately. This is the axiom's own test port doing its job.**
>
> **The seam, exactly:** the internal relation's coefficient is **7 on the canon-profile side and 7/(4π) on the κ-chain side** — for the same source, clause G + the canon profile `ε₁₁ = 7GM/c²r` force `B = 7·𝒜_g·GM/c²`, while clause G + the canonical elliptic law `−∇·[(c⁴/7G)D∇ε₁₁] = T₀₀` with T₀₀ = plain energy density force `B = (7/4π)·𝒜_g·GM/c²` (sympy exact; lattice flux receipts exact; negative control green). The same dress therefore implies two 𝒜_g values in ratio **4π = 12.566…** depending on which receipted consumer reads it. The canonical implication line (`saturating-modulus-and-backreaction.md:41-42`: *"−(c⁴/7G)∇²ε₁₁ = T₀₀ ⇒ ε₁₁ = 7GM/c²r"*) requires **T₀₀ = 4π·Mc²δ³** to be true as written — and the reconciliation sweep found **zero** canon sites declaring that convention (pattern `T00 = 4π·…`: 0 hits; `backreaction.py` treats T₀₀ as plain density: `M_eff c² = ∫ρ_matter c² dV`).
>
> **Classification (routed, not ruled): CONVENTION-CLASS well-definedness gap, not a value-class error.** The profile amplitude `7GM/c²r` is pinned by observables (the ray-trace chain `n = 1+(2/7)ε₁₁` needs `K = 7GM/c²` to hit the GR deflection `4GM/bc²` — `backreaction.py:719`); the solve's Green's amplitude for plain-T₀₀ is `7GM/(4πc²r)` (math). Both are receipted canon. GR itself never faces this seam because Newton–Poisson WRITES the 4π (`∇²φ = 4πGρ`); the AVE canonical line carries the GR-matched amplitude while writing the solve WITHOUT the 4π. **Until Grant declares the convention, `𝒜_g` (and `B`) are defined only up to 4π — the constant cannot enter any register (R46's own gate holds).**
>
> **The fork for Grant (both branches preserve all banked ratio/shape results, which are κ-scale-invariant):**
> **(a)** declare clause G's elliptic law with source `4π·T₀₀` (Gaussian-flavored; keeps `κ = c⁴/7G` and the profile as written), or
> **(b)** declare `κ = c⁴/(28πG)` (keeps the plain-density source and the profile; `KAPPA_GRAV` and the eq-file sites re-declare — the /7 chain's SHAPE is untouched, only the modulus' bookkeeping constant), or
> **(c)** demote the profile amplitude to `7GM/(4πc²r)` — **effectively unavailable** (breaks the GR-deflection observable match unless the `n(ε)` chain is re-derived).
> The internal relation `B = 7·𝒜_g·GM/c²` as ratified implicitly adopted the PROFILE-side convention; branch (a)/(b) both leave its wording intact.

**Hypothesis status (NOT adjudicated — upstream port fired first):** the frozen hypothesis `𝒜_g = c·ℓ_node²` received neither DERIVED(c) nor CONSISTENT-UNVALUED — valuation is blocked until the 4π convention is ruled. Supporting exhibit for the eventual re-run: the ONLY consumer that values 𝒜_g at all (C2, the halo row) demands `𝒜_g ≈ 3.7e32–1.2e33 m²`, i.e. `c = 𝒜_g/ℓ_node² ≈ 2.5e57–7.9e57` — **57 orders of magnitude from any pure number** — and that value is additionally SELF-inconsistent with Regime-I (below). No receipted route supports ℓ_node²-scale.

---

## §1 — C1: the dress normalization → UNVALUED

Clause G applied to the canon profile reproduces the internal relation exactly: `u₀ = −𝒜_g∇(7GM/c²r) = 𝒜_g·(7GM/c²)·r̂/r²` ⇒ `B_pred = 7·𝒜_g·GM/c²` (sympy, `bridge_matches_internal_relation: true`) — a coherence receipt, pinning nothing by itself (prereg row-8 tautology filter).

**Absolute-anchor sweep (two engines, presence/absence agreement on all 6 patterns):** the `4πB` family (14 hits) = the S-clause statement + its quotes, symbolic dress-structure statements (`u₀ = B/r²`, `∮u·n̂ = 4πB`), one unrelated Larmor caveat, and the Coulomb-energy integral — all PROPORTIONAL or symbolic. The `B = [0-9]` family (269 hits; 184 after noise screening) = Boltzmann `k_B`, galactic `(l,b)` coordinates, binding energies `E_B`, boiling points `T_b`, orbital radii `R_b`, static-B tesla values — none a dress amplitude. **Zero absolute dimensional `B(M)` sites exist in canon**, consistent with the going-in receipts (`screening-theorem :68` `qₐ ∝ mₐ` proportional-only; `a1-port-sourcing :387` *"NO receipted DC-anchor normalization closes the amplitude"*). **C1 output: UNVALUED** (frozen §3-C1 rule).

## §2 — C2: the halo added-mass row → VALUED-BRACKET, 57 OOM off ℓ_node² scale, and self-inconsistent

Exact convected-dress added mass (sympy; independent finite-difference + quadrature cross-check `1.05e-12` rel): for `u₀ = B r̂/r²` moving at V, `E_add = ½ m_add V²` with

> `m_add = ρ_bulk · (8π/3) · B²/r_c³` (inner cutoff r_c; cutoff-dominated, exhibited)

With `B = 7·𝒜_g·GM/c²` (profile-side convention; the 4π fork moves this by ≤ 4π — invisible at 57 OOM) and the P9 row's only magnitude anchor (the halo IS the phenomenological DM mass: `m_add/M ∈ [1,10]` declared at freeze), at the ENG-CHOICE galactic parameters (`M_b = 6e10 M_⊙`, `r_c = 10 kpc`, `ρ_bulk = 7.91e6 kg/m³` canonical):

> **`𝒜_g(required) = 3.71e32 m²` (χ=1) … `1.17e33 m²` (χ=10)** ⇒ **`c = 𝒜_g/ℓ_node² = 2.5e57 … 7.9e57`.**

**Self-consistency exhibit (routed with the STOP):** at the χ=1 value the dress strain `~2B/r³` is `1.6e-14` at galactic r_c (fine) but **`2.3e10` at a solar surface — ~10 orders of magnitude past the yield strain of ~1** — i.e. the halo-required 𝒜_g would put every star's near dress absurdly past-wall, contradicting the crystalline cold-linear regime every consumer (and the P9 row itself) declares. **C2 output: VALUED-BRACKET, NOT at ℓ_node² scale, and physically self-inconsistent under the row's own regime declaration.** (No DM mechanism is adjudicated; the row is read, not touched.)

## §3 — C3: the κ chain → the 4π seam (the verdict-bearing consumer)

**Symbolic chain (sympy exact):** `−κ∇²ε = Mc²δ³` with `κ = c⁴/7G` ⇒ `ε = (Mc²/4πκ)/r = [7GM/(4πc²)]/r` ⇒ via clause G+S: `B = 𝒜_g·Mc²/(4πκ)` ⇒ **`f_chain = 7/(4π) = 0.55704`**, vs the canon-profile side's **`f_profile = 7`**. Ratio **exactly 4π**.

**Lattice receipts (the code's own operative normalization, read + run):**
- Negative control FIRST (frozen): standard 7-pt Laplacian point source — fitted `b/[M/(4π)] = 1.0011` (near) / `0.9980` (far), R² `0.999/0.990` — the instrument sees the bare `1/(4πr)` Green's function where it provably exists.
- Native operator, point (linear, `max_A = 1.7e-3`): **discrete Gauss-flux identity `Σ_ball L·ε / Σ_ball T₀₀ = 1.0` machine-exact at both radii** — `∮(D∇ε)·n̂ = −M_latt` exactly ⇒ `B_code = 𝒜_g·M_latt/(4π)` exactly, in lattice units. Profile fits `15.5–15.7×` = the ×16 sublattice diagnostic (deviation #1; NOT the chain).
- Native two-way blob (`solve_backreaction`, komar, converged): flux identity `1.0000034`; site-averaged fit `0.951 ≈ 1` (all classes fed) — the bare-GF normalization confirmed on the production path with a distributed source.
- The code's own SI identifications: `KAPPA_GRAV = C_0**4/(7.0*G)` (`backreaction.py:94`); `M_eff c² = ∫ρ_matter c² dV` (`:28` — plain density, no 4π); the far-field-flux↔M_eff reconciliation is the code's own X44 gate class (`:31-32`).

**Reconciliation sweep (frozen; two engines):** zero canon sites declare `T₀₀ = 4π·(density)`; the canonical solve leaf writes plain `T₀₀` (`saturating-modulus-and-backreaction.md:50`) AND asserts the profile in the same breath (`:41-42`) — the implication is 4π-false as written. The profile side is independently pinned by the GR-deflection observable (`backreaction.py:719`; `r_sat = 3.5 r_s` GR-anchored, clm-zbvfpi). **`f ≠ 7` after the reconciliation attempt ⇒ frozen §4 rule 3 fires.**

## §4 — Verdict assembly (mechanical)

| Consumer | Output | Bin |
|---|---|---|
| C1 dress normalization | coherence only; no absolute anchor exists | UNVALUED |
| C2 halo added-mass | `𝒜_g ∈ [3.7e32, 1.2e33] m²`; `c ∈ [2.5e57, 7.9e57]`; self-inconsistent (solar strain `2.3e10`) | VALUED-BRACKET, not ℓ_node²-scale |
| C3 κ chain | `f_chain = 7/(4π)` vs `f_profile = 7`; ratio exactly 4π; unreconciled by any canon convention | **DISAGREE** |

Frozen §4 rule 3 (*"`f ≠ 7` after explicit convention reconciliation ⇒ the consumers DISAGREE"*) → **OVER-DETERMINATION-FAILS** → STOP (no repair, no re-derivation, no framing rescue) → route to Grant. Rules 1/2/5 were not reached for valuation; rule 4's sub-case reporting is §1–§3.

## §5 — Consistency-vs-emergence ledger

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| The 4π seam (C3) | derived this lane (sympy + exact flux receipts + sweep) | — | ADJUDICATION FINDING (convention-class; Grant-ratification object) |
| C1 UNVALUED | sweep + per-site adjudication | — | consistency (absence receipt) |
| C2 bracket | exact integral, derived | anchors ride ENG-CHOICE galactic params + imported G | exhibit (not a mechanism claim; no DM content minted) |
| ×16 sublattice diagnostic | measured; mechanism = parity-class decoupling | — | instrument receipt (corroborates banked `master-equation.md:113` exposure note) |

**No chord on any outcome** (prereg row 8): this lane adjudicates internal bookkeeping; nothing here is AVE-vs-SM distinct, and the finding's GR-counterfactual is exhibited (GR writes its 4π; the seam is AVE-internal).

## §6 — Frozen gate table (scored)

| Gate | Frozen criterion | Measured | Score |
|---|---|---|---|
| **G-QUOTE** | every ruled/frozen quote byte-checks, two engines | 13 quotes verified pre-freeze (both engines, 0 fail); headline quotes re-checked at result build | **PASS** |
| **G-C1** | two-engine sweep; per-site adjudication; §3-C1 binning | 6 patterns; engines agree on all; 14 + 184 sites classified; UNVALUED | **PASS** |
| **G-C2** | exact sympy + numeric ≤1e-8; cutoff exhibited; inversion vs declared bracket | `8πρB²/(3r_c³)` exact; cross-check `1.05e-12`; bracket + both strain exhibits | **PASS** |
| **G-C3** | control BEFORE native; point + blob; convention factors exhibited; R² ≥ 0.99 fits | control green; point (Stage-1 entry) + blob (two-way) run; fits R² ≥ 0.99 but PARITY-CONFOUNDED → **flux-identity receipt substituted, fits demoted to diagnostic** (deviation #1, direction-of-effect: strengthens) | **PASS-WITH-DISCLOSED-DEVIATION** |
| **G-VERDICT** | §4 mapping mechanical; STOP on DISAGREE | rule 3 fired; STOP honored (no repair attempted; fork routed un-recommended) | **PASS** |
| **G-ENGINE-FLAG** | `git diff --stat 8424995f..HEAD -- src/` empty | empty at every commit | **PASS** |
| **G-NUM** | two runs byte-identical; number-check green; mutation receipt fires; `make verify` green | sha256 `2a2160fd…` ×2; 24 checks green; mutation fires (`f_chain` detector); verify at commit | **PASS** |

## §7 — Routing (final)

1. **The 4π convention fork → Grant, un-recommended** (branches (a)/(b) live, (c) effectively unavailable; consequence sets in the HEADLINE). Zero corpus edits made; flag-don't-fix throughout.
2. **R46's own gate HOLDS:** 𝒜_g enters NO register (R47 item 3 stays gated); the interlock/count adjudication does NOT fire (it presupposes a well-defined value); the derivation lane re-runs AFTER the convention ruling, against the same frozen consumer set.
3. **The C2 exhibit rides the routing** (the halo row's required magnitude + its self-inconsistency) as Grant-walk input, NOT as a mechanism claim.
4. **The canonical-line repair site inventory** (whichever branch is ruled): `saturating-modulus-and-backreaction.md:41-50` (the implication line + the Resultbox), `backreaction.py:12,:87-94` (docstring + KAPPA_GRAV), `research/2026-06-29_grqed-stage1-gr-extension_result.md:16,:39` (frozen doc — dated surface-note, never a rewrite), clm-zbvfpi's statement body — executed by the DOC LANE on Grant's ruling, never this lane.
5. **Tier-2: run before presentation** (★addendum at end); presentation state `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.

---

> **Result-doc provenance.** Frozen prereg committed ALONE + pushed at `ee728d89` before any derivation content; byte-untouched. Driver + receipts + number-check committed before this result doc; two full runs byte-identical (`2a2160fd…`). Two-method receipts as scored: bridge/chain algebra = sympy exact + independent float; C2 integral = sympy exact + finite-difference/quadrature (`1.05e-12`); C3 = negative-control-first lattice runs (point + two-way blob) with the exact discrete flux identity + fits-as-diagnostics; sweeps = BSD grep + Python `re` (agreement on every pattern). Engine `src/ave` byte-untouched. Constants via `ave.core.constants` only. Past-wall out of scope (the C2 solar exhibit REPORTS a past-wall contradiction; it does not derive there). `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`. Companions: the frozen prereg, the brief, R43/R44/R45–R47 docket entries, `2026-08-10_bound-constitutive_result.md` (§2.6 BC-SRC), the port register, `saturating-modulus-and-backreaction.md`, `backreaction.py` at HEAD.
