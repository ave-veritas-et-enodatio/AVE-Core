# Pre-Registration: Does τ_yield *scale with* the dual-reactance count, or merely *inherit* the value 2?

**Date:** 2026-06-02
**Branch:** `analysis/tau-yield-reactance-count` (off `main` @ `ac5ed5f4`)
**Type:** Substrate-physics derivation — provenance-upgrade + cross-scale-unification candidate (NOT a new empirical prediction)
**Discipline:** `ave-prereg` → `ave-ee-first-mapping` → `substrate-native-check` → `consistency-vs-emergence` → `pre-test-physics-check` Trigger 7
**Brief:** [`_orchestration/2026-06-02_tau-yield-scales-with-count-brief.md`](../_orchestration/2026-06-02_tau-yield-scales-with-count-brief.md)
**Predecessors:** [`2026-06-02_fabricated-FEM-walkback-and-tau-yield-fork.md`](2026-06-02_fabricated-FEM-walkback-and-tau-yield-fork.md) (raised this open item) · [`2026-06-01_baryon-V2-dual-reactance-closure.md`](2026-06-01_baryon-V2-dual-reactance-closure.md) (the V=2 reactance-count it would unify with)

> **One-line:** `τ_yield = e²·𝒱_total/(8πε₀·ℓ_node⁴)` with `𝒱_total = 2`. Is the 2 *forced* because the dielectric yield = the **sum** of the stored reactive energy density over both sectors `E_C + E_L` at the saturation limit (→ axiom-derived) — or does the formula merely **inherit** the integer 2 from `𝒱_total` (→ a re-interpretation)? This prereg freezes the expectation; the **crux is a plumber-physical call reserved for Grant** before any verdict lands.

---

## Target (precise)

Determine the provenance status of the factor `𝒱_total = 2` in `τ_yield`. Two sub-targets:

1. **Non-circularity guard:** derive `e²/(8πε₀ℓ⁴)` as the per-sector (capacitive) reactive energy density **independently** of the τ_yield formula.
2. **Yield-event class:** classify the dielectric-yield event as **resonant-tank** (oscillating, `E_C=E_L` time-averaged → ×2 forced), **static single-sector** (one sector at limit, other empty → ×1, 2 inherited), or **saturation-skewed** (Axiom-4 kernel modulates the sectors oppositely → modulated, non-integer factor).

## Physical picture (mechanical, no equations)

- A vacuum node is an LC tank — charge strain stored capacitively (`E_C`, translational-E sector), flux strain stored inductively (`E_L`, microrotational-B sector). Two reactive sectors (Axiom 1, 6 DOF: 3 translational → E → C, 3 microrotational → B → L).
- The dielectric "yields" when local strain amplitude `A` hits the saturation ceiling `A_yield` — the Γ=−1 boundary forms, substrate ruptures. A **discrete onset / threshold** event.
- Crux: at the rupture instant, is the tank *oscillating* (energy sloshing between sectors) or *single-sector* (only the saturating sector loaded)?
- Axiom-4 kernel `S=√(1−(A/A_yield)²)` modulates the sectors **oppositely** as `A→A_yield`: `C_eff=C₀/S→∞` (ε_eff→0), `μ_eff=μ₀S→0`. So the sectors are **not symmetric** at the breakdown point even if equipartition holds at small signal.

## Corpus state — **PARTIAL** (value CLOSED, scaling-mechanism OPEN, per-sector density NOT independently derived)

| Piece | Status | Source (verified) |
|---|---|---|
| `τ_yield = e²·𝒱_total/(8πε₀ℓ⁴) ≈ 1.04×10²² Pa`, two factorings ("differ only by factoring choice") | canonical, zero drift across 6 sites | `magnetic-saturation.md:10,:20`; `backmatter/01_appendices.tex:71`; `common/appendices-overview.md:66`; `04_continuum_electrodynamics.tex:219,:228` |
| `𝒱_total = 2` = the dual-reactance count (X_C + X_L), mass-confirmed (V=2 → 1836.117 m_e) | **CLOSED** | `dual-reactance-storage-taxonomy.md:50,:102-116`; `2026-06-01_baryon-V2-dual-reactance-closure.md` §1-2 |
| "yield *stress* scales with the reactance count" | **OPEN — re-interpretation, not a derivation** | `dual-reactance-storage-taxonomy.md:155-165` (§τ_yield open item) + clm-8ep2b4 / clm-o2shcn |
| per-sector density `e²/(8πε₀ℓ⁴)` derived **independently** | **NOT IN CORPUS** (only appears *as* the τ_yield numerator) | grep negative (corpus-grep `a34a8e206265761bc`) |
| yield-event class | corpus classifies dielectric-rupture as **ε-only asymmetric saturation, μ intact** | `master-equation.md:77-81` (clm-lv3uw1) |

> **Provenance correction (verify-before-cite):** the brief's "derived from {ρ_bulk c², ρ_threshold, V_total=2}" is **outdated**. The live formula is `τ_yield = ρ_bulk c² · 𝒱_total · α` (≡ compact `e²·𝒱_total/(8πε₀ℓ⁴)`); `ρ_threshold ≈ 1.106` was **decoupled** from `𝒱_total` in the 2026-06-02 walk-back and is **not** a factor in τ_yield.

## Dimensional analysis (mandatory — Step 3.5; canonical primitives)

Using `α = e²/(4πε₀ℏc)` (INVARIANT identity) and `ℓ_node = ℏ/(m_e c)` (reduced Compton wavelength, `01_appendices.tex:65`):

- Coulomb self-energy: `e²/(8πε₀ℓ_node) = ½·(e²/(4πε₀ℓ_node)) = ½·α·m_e c²`. **The per-sector numerator is α-suppressed relative to rest energy.**
- Per-sector energy density: `e²/(8πε₀ℓ⁴) = ½·α·(m_e c²/ℓ_node³)`.
- `τ_yield = 2·e²/(8πε₀ℓ⁴) = α·(m_e c²/ℓ_node³)`.

Numerical check: `m_e c²/ℓ_node³ = 8.19×10⁻¹⁴ J / (3.86×10⁻¹³ m)³ ≈ 1.42×10²⁴ Pa`; × α (7.30×10⁻³) ≈ **1.04×10²² Pa**. ✓ Matches the canonical value and the `ρ_bulk c²·𝒱_total·α` factoring (`tvs-transition.md:24`).

**Power-counting consequence (load-bearing for the crux):** the per-sector quantity being doubled is the **α¹ Coulomb (electrostatic) self-energy**, NOT the **α⁰ virial half-rest-mass** `E_C=E_L=½m_e c²` that the corpus equipartition leaves derive (`relativistic-inductor-newtonian-limit.md:22-24`). These are **different energies** — any argument that licenses the ×2 via the virial 50/50 must first reconcile the α-order mismatch.

## Prediction (pre-registered, honest)

The `ave-prereg` corpus-grep already surfaced a strong directional signal: the corpus's own master equation (`master-equation.md:78`, clm-lv3uw1) classifies the **dielectric-yield event as the ε-only asymmetric-saturation branch — only the capacitive sector saturates, μ_eff (the inductive sector) remains intact.** If that classification governs τ_yield, the yield stress is a **single-sector** energy density and the 2 is an inherited count-tag.

- **Most likely (≈ STAYS-INHERITED / REFRAME):** the yield is single-sector (capacitive breakdown); the 2 does not arise as `E_C + E_L` summed within one event. The genuine cross-scale structure is that the **two reactance sectors are the two *branches* of the master equation** (electric breakdown = τ_yield; magnetic confinement = mass), each single-sector — not a sum inside one event.
- **Possible (CLOSE):** if Grant's physical call is that the yield is the **nucleation of a new two-sector defect** (which must populate both `E_C` and `E_L` to exist) rather than the breakdown of a pre-existing tank, the ×2 could be forced by the defect's two-sector structure — but the α-order mismatch above must still be resolved.
- **Possible (REFINE):** the Axiom-4 opposite-modulation (`C_eff↑`, `L_eff↓` as `S→0`) yields a modulated, non-integer factor.

## Discriminating outcomes

- **CLOSE** → yield = `E_C + E_L` at breakdown; 2 = reactance count, axiom-derived; unifies baryon `V=2` (fm scale) with τ_yield (~10²² Pa) through the same X_C+X_L sectors.
- **REFINE** → factor is saturation-modulated, not a clean integer 2; report the modulated form.
- **STAYS-INHERITED** → yield is single-sector / no clean sector-sum; open item stands; value 2 honestly inherited.

## Falsifier (of the CLOSE framing)

The CLOSE framing is falsified if: (a) the yield event is single-sector (corpus master-equation ε-only branch governs) **and** (b) `E_C` and `E_L` do not coexist at their per-sector maxima at the rupture instant (conjugate `V_inc ↔ Φ_link` trade off in time; local clock freezes at `A²→1`). Either kills "τ_yield = E_C + E_L at breakdown."

## Classification (consistency-vs-emergence)

- **Governing trigger: Trigger 8** (classification-promotion past canonical ceiling). Canonical ceiling = *"inherits the value 2 ... a re-interpretation, not a derivation"* (`dual-reactance-storage-taxonomy.md:165`, verbatim). A CLOSE promotes to axiom-derived **only** if new substrate content forcing `E_C+E_L` co-participation at yield is named and traces to an axiom (Step 8b/8d).
- **Observable axis: Class 4 consistency / provenance** — the sector count cannot be varied empirically (there are always two sectors), so even CLOSE produces **no new experimental discriminator**. This confirms the brief's scope: provenance-upgrade + unification, NOT a new empirical prediction.
- **Non-circularity (Step 3):** `e²/(8πε₀ℓ⁴)` is currently structurally circular (read *off* the formula); an independent derivation requires the isolated-sphere self-capacitance `C=4πε₀ℓ`, which differs from the canonical node capacitance `C_cell=ε₀ℓ_node` by 4π. **The non-circularity guard is not yet met.**

## Scope guard

Derivation-closure / provenance only. Output: this prereg + an analysis doc carrying the substrate-walk up to the crux. **STOP at the crux and surface it to Grant** before any verdict, propagation, or matrix change (per brief + `pre-test-physics-check` Trigger 7 + `substrate-native-check` Rule 16). Branch pushed; **NOT merged** — orchestration merges after review.
