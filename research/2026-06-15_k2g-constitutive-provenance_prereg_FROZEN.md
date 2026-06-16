# PREREG (FROZEN, Rule-11) — K=2G constitutive provenance (Phase 2 of PR #261)

**Frozen:** 2026-06-15. Phase 2 of the K=2G provenance lane — the **last route to a substrate-forced
K=2G**: does the chiral LC tank's OWN constitutive law pin ρ=k_a/k_s to the K=2G value? Rule-11: no
post-driver edits to §Prediction / §Outcomes / §Falsifier; Rule-12 dated amendments only.

## Target (Step 1)

From ONE constitutive law, produce both: (i) the saturation monotonicity (C_eff vs ε_eff — Grant's
original Q, the open `crio-ceff-saturation-onset` lane) AND (ii) the linear bond-stiffness ratio
ρ = k_a/k_s. Then read K/G off the validated lattice-dynamics moduli. Does ρ land at the K=2G value?

## The bridge (Step 1.5 — DERIVE, not assume; Grant's load-bearing flag)

**Corpus-anchored half (DOF-sector, qualitative):** stretch ↔ capacitive ↔ E-sector
(`electron-plumbing-primer.md:26`); twist/microrotation ↔ couple-stress ↔ inductive/μ-sector
(`translation-circuit.md:99-104`). Direction confirmed.

**Quantitative bridge (DERIVED here):**
- Canonical EE identity (`translation-circuit.md:23`): **C = ξ²·κ, κ=compliance=1/stiffness** ⟹
  capacitive-sector stiffness **k_a = ξ²/C_eff** (elastance). [corpus-canonical]
- EE dual (the new step, flag for Grant): the inductive sector's "stiffness" is the magnetic
  **reluctance ℛ = 1/permeance ∝ 1/L_eff** (energy = ½ℛΦ²; microrotation angle ↔ flux). ⟹
  **k_s ∝ 1/L_eff**. [derived by EE duality, not yet in corpus]
- ⟹ **ρ = k_a/k_s ∝ L_eff/C_eff = Z_eff²** — the bond-stiffness ratio IS the substrate's local
  characteristic impedance, squared.

## Physical picture

- The substrate is a balanced LC line whose defining constant is Z₀=√(μ₀/ε₀) (Axiom 1). ρ = Z_eff²
  is impedance-squared.
- **K=2G is the SYMMETRIC (SYM) operating point** (backmatter/07: "SYM = vacuum K=2G; ε,μ saturate
  together") — the **impedance-matched, reflectionless Γ=0 gravity null** where ε_eff=ε₀S, μ_eff=μ₀S
  co-scale so **Z_eff=Z₀ stays INVARIANT**.
- On that very branch, Z_eff (hence ρ) is **pinned/invariant along the operating-point family** — the
  saturation state cannot tune ρ. The 2:1 of K=2G would have to be baked into the COLD geometric
  prefactor, which Phase 1 (this lane) already showed is an unforced one-parameter family.
- ASYM branch (static-E-only, C_eff=C₀/S, Z_eff=Z₀/√S changes — the crio "Branch R"): ρ=Z₀²S² →
  DECREASES toward saturation, moving AWAY from the K=2G value (ρ≥2).

## Decomposition (the load-bearing structure)

**ρ = 𝒢 · (Z_eff/Z₀)²** — a cold geometric prefactor 𝒢 × an operating-point impedance factor.
- Operating-point factor (Z_eff/Z₀)²: **= 1 (SYM, invariant)** or **= S² (ASYM, ≤1)**. NEVER freely
  tunable above 1 → cannot reach the K=2G value.
- Geometric prefactor 𝒢: the Phase-1 free ratio (Cosserat K=2G⟺ρ=2; Keating ρ*=3.67–6.62). Unforced.

## Model choice (Grant's flag — substrate-native)

AVE is **Cosserat micropolar** (Axiom 1) → native moduli **K₀=4k_a+8k_s, G₀=8k_s** ⟹ K=2G⟺**ρ=2**.
**Keating** (central-force, Phase-1, validated vs diamond to −0.36%) ⟹ K=2G⟺ρ*∈{3.67,5.30,6.62}.
Verdict is robust to the choice; the choice only sets the numerical target. Cosserat is primary;
Keating is the validated cross-check.

## My prediction

**K=2G is NOT constitutively forced (verdict: GR-imported, end of line).**
1. ρ = 𝒢·(Z_eff/Z₀)². The constitutive law's only handle is the operating-point factor (Z_eff/Z₀)²,
   which is **SYM-INVARIANT (=1)** on the K=2G branch and **≤1 (ASYM, =S²)** off it — it can NEVER
   raise ρ to the K=2G value (≥2). Independent constitutive-side corroboration of the u₀*≈0.187 ECHO
   retraction: the saturation operating point CANNOT select K=2G.
2. The cold impedance-matched reading Z_eff=Z₀ ⟹ operating-point factor=1 ⟹ ρ=𝒢. The balanced point
   ρ=1 gives Cosserat ν=0.227 / Keating ν=0 — close-ish (Cosserat) but **not** 2/7; K=2G needs a 2:1+
   ε/μ-sector elastance mismatch (Z_eff≥√2·Z₀) the impedance-matched substrate does not have.
3. The two outputs are COUPLED through the impedance factor: the open crio **Branch-R-vs-F monotonicity
   Q = the SYM-vs-ASYM operating-point Q = the "does saturation tune ρ" Q.** Same question.

## Discriminating outcomes

- **A (predicted, fork→imported).** Operating-point factor SYM-invariant/ASYM-decreasing; ρ never
  reaches the K=2G value; 𝒢 is the unforced Phase-1 ratio. K=2G constitutively imported.
- **B (would force a chord).** The constitutive law makes (Z_eff/Z₀)² land exactly at the K=2G value
  AND pin it there independent of geometry — i.e. the chiral LC structure forces Z_eff/Z₀=√2 (Cosserat)
  on the SYM branch. **Predicted NOT to happen** (SYM ⟹ Z_eff=Z₀ by definition).
- **C (null).** The k_s∝1/L dual is wrong / the bridge is under-determined → ρ not derivable from the
  constitutive law → K=2G stays a free input (still imported, via a different door).

## Falsifier (what would mean my framing is wrong)

If on the SYM branch (ε,μ co-scaling) the bond-stiffness ratio ρ is NOT invariant — i.e. Z_eff is NOT
pinned to Z₀ on the K=2G branch, or k_s does not scale with the μ-sector the same way k_a scales with
the ε-sector — then the operating point CAN tune ρ and could select K=2G constitutively (fork a). Or:
if the cold geometric 𝒢 is shown (by the chiral coupling) to be forced to exactly 2 (Cosserat), K=2G
is constitutively forced.

---

*Rule-12 amendments (post-freeze, dated) below this line:*

**A1 (2026-06-15, pre-driver) — rest the verdict ONLY on SYM-invariance; do not assert the ASYM
direction.** The prediction's "ASYM ρ=Z₀²S² (decreasing)" sub-claim over-specifies a sign that is
actually tied to the OPEN crio Branch-R-vs-F monotonicity Q (whether the elastic k_a∝1/C_eff uses the
rising C_eff=C₀/S or the falling C_eff=C₀S reading). The **robust, verdict-bearing claim** is the
**SYM-invariance**: on the K=2G branch (ε,μ co-scale by a common S), ρ = L_eff/C_eff = (μ₀S)/(ε₀S) =
Z₀² **exactly, all S** — the common factor cancels regardless of the open sign. So ON THE K=2G BRANCH
ρ is operating-point-INVARIANT, and K=2G reduces to "is the cold geometric 𝒢 = the K=2G value?"
(Phase-1 NEGATIVE). Off-SYM (ASYM) ρ DOES change with S, but its direction is sign-ambiguous (open
crio Q) AND K=2G is not even defined there (Z≠Z₀, not the gravity null). The verdict (Outcome A,
imported) is unchanged and now does NOT depend on the ASYM direction. The driver demonstrates the SYM
ρ-invariance and flags the ASYM direction as tied to the open crio lane, not resolved here.
