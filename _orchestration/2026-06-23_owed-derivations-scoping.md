# Owed-Derivations Scoping — Four Outstanding Rigour Gaps

**Date:** 2026-06-23
**Lane:** engine-consolidation (implementer)
**Type:** orchestration TRACKING doc (not a KB leaf — no claim-id / solidity metadata)

This is a **scoping / tracking** document for the four owed derivations listed in
[`mathematical-closure.md`](../manuscript/ave-kb/common/mathematical-closure.md)
§"Outstanding Rigour Gaps" (table) plus the Layer-8 back-edges. It does **NOT**
attempt to close, derive, or resolve any of them — closing is explicitly out of
scope for this lane. Its only job is to capture, per gap, the current status,
what would close it, the difficulty tier, and the closed-candidates state, so
that (a) the four gaps are individually auditable, and (b) the difficulty-tiering
is made explicit: these are research-hard items **flagged, not solved** here.

A load-bearing point this doc makes structurally explicit: the four gaps sit in
**four different epistemic states** (research-hard with no logged attempt /
tractable bounded re-eval / open-with-no-candidates / closed-negative). They are
not interchangeable "TODOs"; conflating them would misrepresent both the
remaining work and what has already been falsified. See the closing note.

All canonical-location lines below were spot-verified against HEAD
(`mathematical-closure.md` table at lines 165–168; back-edges at 130–138) on
2026-06-23. No line-number drift was found.

---

## Summary table

| Gap | Difficulty class | One-line status |
|---|---|---|
| **1 — m_e / ℓ_node Nyquist-independence** | RESEARCH-HARD (no logged attempt) | OPEN conditional back-edge; "smallest stable soliton" not yet shown well-defined without circular reference to m_e. |
| **2 — Flux-tube Gaussian-ansatz radial profile** | TRACTABLE (bounded re-eval) | OPEN; result internally consistent *conditional on* the Gaussian ansatz; binds ρ_threshold only, not V_total = 2. |
| **3 — H_∞ / G Chain B′ (G independent of R_H)** | OPEN-NO-CANDIDATES (route empty, not refuted) | OPEN; 0 closed-form Chain B′ candidates anywhere; one identity in (G, H_∞), disclosed as "consistency proof, not prediction." |
| **4 — δ_strain magnitude at T_CMB** | CLOSED-NEGATIVE (attempted + refuted) | CLOSED NEGATIVE; magnitude derivation ~31 OOM undershoot + generic-thermal; only the SIGN is substrate-set. |

---

## GAP 1 — m_e / ℓ_node Nyquist-independence circularity

- **Canonical location:**
  [`mathematical-closure.md:166`](../manuscript/ave-kb/common/mathematical-closure.md)
  (Outstanding Rigour Gaps row "m_e closure via Nyquist independence");
  back-edge at `:131`; acyclicity verdict at `:136`; cross-ref
  [`full-derivation-chain.md`](../manuscript/ave-kb/common/full-derivation-chain.md)
  §Layer 8.
- **Current status:** OPEN / unresolved back-edge. One of {m_e, ℓ_node} is the
  input scale; the other is computed via ℓ_node = ℏ/(m_e c). Layer 8 proposes
  that Nyquist resolution of "the smallest stable soliton" fixes ℓ_node
  independently of m_e. The back-edge is acyclic **ONLY IF** "smallest stable
  soliton" is well-defined without circular reference to m_e.
- **What would close it:** demonstrating that "smallest stable soliton" is
  well-defined without circular reference to m_e (e.g. from the Axiom-4
  saturation gradient + lattice cutoff alone). Closing removes the input-scale
  degree of freedom — both ℓ_node and m_e become emergent.
- **Difficulty:** RESEARCH-HARD.
- **Closed-candidates note:** NO closed-negative on file; NO logged attempt
  (no Q-id / prereg / result doc / closure-roadmap row). It is stated as a
  *conditional* back-edge ("acyclic IF…"), not an attempted-and-failed
  derivation. It reads as **open-stated-conditional**, not research-exhausted.
  Tractability hinges on whether "smallest stable soliton" can be grounded in
  the Axiom-4 saturation gradient + lattice cutoff alone — a suggested but
  undemonstrated path.

---

## GAP 2 — Flux-tube Gaussian-ansatz radial profile

- **Canonical location:**
  [`mathematical-closure.md:167`](../manuscript/ave-kb/common/mathematical-closure.md)
  (row "Flux-tube radial profile (Gaussian ansatz)"); inline at
  [`thermal-softening.md:77`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md)
  (+ `:73–101`).
- **Current status:** OPEN derivation gap; result internally consistent
  **CONDITIONAL on the ansatz**. Axiom 1 fixes the FWHM (= ℓ_node) but NOT the
  functional form; the Gaussian is an ansatz for tractability. It binds
  ρ_threshold ≈ 1.1062 (= 1 + ℓ_node/(8√(2 ln 2))) **ONLY**; it does NOT bind
  V_total = 2 (the profile-independent dual-reactance count X_C + X_L).
- **What would close it:** either (a) derive the Gaussian profile from Axiom-4
  LC dynamics + transmission-line boundary conditions, OR (b) replace it with
  the framework-consistent profile (sech² kink, Bessel J₀ fundamental, or the
  algebraic √(1−r²) Axiom-4 kernel) and re-evaluate ρ_threshold. Closing removes
  the Gaussian as a buried assumption.
- **Difficulty:** TRACTABLE. It narrowly binds one scalar; explicit candidate
  replacement profiles are already enumerated; and the mass confirmation via
  m_p/m_e ≈ 1836.15 is profile-independent (so a profile swap re-evaluates
  ρ_threshold without disturbing the mass result).
- **Closed-candidates note:** NO closed-negative on file; a concrete path (b)
  exists (three candidate profiles named, un-attempted). NOTE the retired
  provenance: the legacy "V_total = 2.0 FEM-converged to 0.13%" claim was
  **RETIRED** — the only "FEM" script
  ([`src/scripts/vol_2_subatomic/fem_borromean_convergence.py`](../src/scripts/vol_2_subatomic/fem_borromean_convergence.py))
  is voxel quadrature of the Gaussian-ansatz overlap volume (a ρ_threshold
  consistency check), NOT a profile derivation. Do-not-fuse-the-two hazard per
  [`thermal-softening.md:101–109`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md).

---

## GAP 3 — H_∞ / G Chain B′ (derive G independent of R_H, the cosmological horizon)

- **Canonical location:**
  [`mathematical-closure.md:168`](../manuscript/ave-kb/common/mathematical-closure.md)
  (row "H_∞ closure: G derivation independent of R_H"); back-edge at `:132`;
  inline at
  [`asymptotic-hubble-constant.md`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md)
  and
  [`lattice-genesis-hubble-tension.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md)
  §Verification; source circularity at
  [`constants.py:577–589`](../src/ave/core/constants.py)
  (`XI_MACHIAN = HBAR*C_0/(7.0*G*M_E**2)` at `:589` literally inverts the closed
  form using CODATA G); corpus self-statement at
  [`cosmological-constant-closure.md:103–111`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md);
  verdict doc
  [`research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md`](../research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md)
  (§4.2 ~line 262).
- **Current status:** OPEN. Verdict (d) confirmed 2026-05-19: 0 closed-form
  Chain B′ candidates anywhere (any repo, branch, or archive); 5
  qualitative-gloss locations only. H_∞ = 28π m_e³ c G/(ℏ²α²) is the **same
  constraint** as G = ℏc/(7ξ m_e²) rearranged — ONE identity in (G, H_∞), not
  two independent predictions (the corpus discloses this as "consistency proof,
  not prediction"). `constants.py:577` tags G as "CODATA-input (Bounding Limit
  3)".
- **What would close it:** derive G from a thermodynamic balance whose closure
  conditions are LOCAL (lattice tension, equipartition, generation rate per
  node) rather than horizon-scale; then substitute that local-G into the H_∞
  formula → a true downstream prediction. (Closure-roadmap path: derive
  Δ_E_cryst + Γ_cryst from substrate-local primitives {ℓ_node, α} ALONE without
  routing through R_H/H_∞; verify the Friedmann route and the latent-heat route
  give the same numerical G.)
- **Difficulty:** OPEN-NO-CANDIDATES (NOT closed-negative — the route is *empty*,
  not refuted). The exhaustive search returned 0 closed-form candidates; the
  engine source confirms the structural absence (`XI_MACHIAN` cannot evaluate
  from substrate primitives because R_H = c/H_∞ requires H_∞ requires G — the
  engine inverts CODATA G).
- **Closed-candidates note:** showstoppers doc §1 search log: 7 brief terms +
  expanded corpus-native greps → 0 closed-form, only 5 qualitative-gloss prose
  locations; cross-repo grep across all 10 AVE-staging repos +
  Applied-Vacuum-Engineering archive + L3 archive → 0 new closed-form work.

---

## GAP 4 — δ_strain magnitude at T_CMB

- **Canonical location:**
  [`mathematical-closure.md:165`](../manuscript/ave-kb/common/mathematical-closure.md)
  (row "δ_strain magnitude at T_CMB (route CLOSED NEGATIVE)"); back-edge `:130`
  + `:136`; result doc
  [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md);
  mechanism leaf
  [`delta-strain-cosmic-tcc.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md)
  (clm-hp7nlm).
- **Current status:** CLOSED NEGATIVE (route refuted). The definitional residual
  ≈ 2.225×10⁻⁶ (= 1 − CODATA/α_cold) is back-subtracted from CODATA; the
  structure (existence + SIGN) is predicted, but the magnitude does NOT derive.
  Q-DELTA-MAP-1-quant (η_ε from substrate E-mode dispersion + Bose-Einstein
  occupation) was **ATTEMPTED and CLOSED NEGATIVE** (FT-1, 2026-05-31): ~31 OOM
  undershoot (BE occupation SUPPRESSES below equipartition at
  T_CMB ≪ Θ_Debye), and is generic-thermal, not AVE-distinct. Only the SIGN is
  substrate-set.
- **What would close it:** a different (un-named) substrate-distinct
  amplification mechanism supplying ~31 OOM over the generic-thermal baseline;
  none is on file. As stated, the magnitude stays a definitional residual.
- **Difficulty:** CLOSED-NEGATIVE.
- **Closed-candidates note:** forward BE η_ε = 2.2×10⁻³⁸ … 2.6×10⁻³⁷ (~31.2 OOM
  undershoot); classical-equipartition foil 6.9×10⁻¹⁰ … 8.1×10⁻⁹ (~2.7 OOM
  undershoot); target ~4.45×10⁻⁶. Prior 2026-05-27 Phase 3-A3 WALK-BACK: the
  earlier "G_vac + equipartition" SM-vocabulary framing leaked classical
  thermal-expansion onto a substrate problem (a c_shear-vs-c_EM category error).
  The mechanism-class identification (Cosserat-rotation-sector mass-gap
  thermal-mode-population ASYM, which predicts the sign) and its weak-force γ_c
  joint-constraint SURVIVE the magnitude-only re-scope.

---

## Closing note — four distinct epistemic states

The four gaps are deliberately **not** filed as one undifferentiated backlog.
They occupy four different epistemic states, and the distinction is itself the
load-bearing output of this scoping pass:

- **RESEARCH-HARD — no logged attempt (Gap 1).** The back-edge is stated as a
  *condition* ("acyclic IF 'smallest stable soliton' is well-defined without
  circular reference to m_e"). No Q-id, prereg, result doc, or closure-roadmap
  row exists. It is open-stated-conditional — the work has not been *tried*, so
  it is neither tractable-by-evidence nor refuted; it is genuinely unexplored
  and plausibly hard.

- **TRACTABLE — bounded re-eval (Gap 2).** The gap narrowly binds a single
  scalar (ρ_threshold), the candidate replacement profiles are already named,
  and the mass confirmation is profile-independent. A swap-and-re-evaluate path
  (b) is concrete and un-attempted. This is the most actionable of the four.

- **OPEN-NO-CANDIDATES — route empty, not refuted (Gap 3).** An exhaustive
  cross-repo / cross-branch / archive search returned **zero** closed-form
  Chain B′ candidates, and the engine source structurally cannot host one
  (it inverts CODATA G). This is **not** a closed-negative: nothing was
  attempted-and-failed; the route is simply *empty*. A new local-thermodynamics
  derivation could populate it.

- **CLOSED-NEGATIVE — attempted + refuted (Gap 4).** The named magnitude route
  (Q-DELTA-MAP-1-quant) was registered, run, and **falsified** (~31 OOM
  undershoot; generic-thermal not AVE-distinct). Per honest-closure discipline,
  this is a clean negative with a single named mechanism, not a debug-toward-
  rescue candidate. The surviving residue is scoped down to the SIGN
  (substrate-set) plus the mechanism-class identification — the magnitude itself
  is a definitional residual unless a fundamentally different, un-named
  amplification mechanism appears.

The operational takeaway for the consolidation lane: only Gap 2 is
"bounded-actionable now"; Gap 1 needs a research program; Gap 3 needs a *new*
derivation (not a search); and Gap 4 is closed (do not re-open as a magnitude
derivation without a genuinely new, substrate-distinct mechanism — re-opening it
to chase the magnitude would be a debug-toward-rescue).
