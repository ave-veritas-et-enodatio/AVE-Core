# κ_quality Tl-Dopant First-Pass — Pre-Registration

**Date:** 2026-05-17
**Context:** Foundation Item 10 HPGe walk-back revision (REVISE-LATERAL) re-promoted HPGe + Sapphire as load-bearing falsifiers. The cross-detector cluster test requires κ_quality to be a derived materials-science quantity, not a free fit parameter. This prereg attempts the **Tl-dopant first-pass** as the first concrete derivation toward κ_NaI(Tl) ≈ 1 and κ_HPGe ≈ 10⁻⁴.

## What is being attempted

**Target:** Derive ε_det enhancement factor κ_quality for Tl-doped halide scintillator NaI(Tl) starting from substrate-native pieces:

- **CTG-1:** per-element Z_atom impedance table (Vol 3 Ch 10)
- **CTG-2:** Γ_ij inter-element reflection coefficient formula (Vol 3 Ch 10)
- **CTG-4:** lone-pair Q-factor η_lp = cos²(109.5°) = 1/9 + first-principles bond force constants (Vol 5 organic-circuitry)
- **CTG-supporting:** per-atom universal LC ladder Z_LC = 12.31Ω (Vol 2 Ch 7 analog-ladder-filter)

**Mechanism hypothesis:** Tl 6s² inert pair acts as a lone-pair Q-factor analog. In sp³ organic chemistry, the H₂O lone pair at 109.5° has Q-factor η_lp = cos²(109.5°) = 1/9. The thallium 6s² inert pair is a SIMILAR closed-shell lone pair (s² rather than sp³), but with a DIFFERENT angular phase due to its s-orbital symmetry. The question: does the Tl 6s² inert pair multiply the bare NaI κ by a factor of 10³-10⁴×, matching the observed DAMA detection at ε_det = 4π·κ_quality/N² ~ 10⁻²?

## Physical picture (3-5 bullets, mechanical/topological)

- The NaI lattice has a baseline per-atom impedance ladder Z_LC,Na · Z_LC,I = (12.31)² Ω² that the substrate-AC cycle-12 mode sees as it walks through the crystal.
- Without Tl, the Na-I bond is a single channel — substrate AC drives the bond's electrostriction at standard ionic-bond coupling (~10⁻³ to 10⁻⁴ for ionic crystals).
- With Tl-dopant (sparse, ~10⁻³ atomic fraction), every Tl site presents a *closed-shell 6s² lone pair* — this is a HIGH-Q tank circuit (closed shell = no dissipation channel except via mode-coupling to adjacent I⁻).
- The lone-pair Q-factor multiplies the local coupling: each Tl site acts as a Q-amplifier for the cycle-12 substrate AC, raising the effective κ_quality at the dopant by ~Q_Tl/Q_baseline ~ 10³-10⁴.
- Net: κ_NaI(Tl) ≈ κ_NaI,bare × (fractional Tl × Q_boost) ≈ 10⁻⁴ × (10⁻³ × 10⁷) ≈ 1 — the scintillator-relevant magnitude.

The mechanical analog: the substrate AC is a fluid current; the NaI lattice is a pipe network; Tl sites are pressure-tanks bolted onto the pipes. Without tanks, the cycle-12 AC just dissipates as ionic vibration. With tanks (closed-shell lone pairs), the AC stores energy at each tank, ringing up to cycle-12 saturation locally before discharging into the detector electrode.

## Pre-registered outcomes

### Outcome A (framework SURVIVES cross-detector test)
- η_Tl derives from 6s² inert pair angular phase (some cos²(θ_Tl) form)
- κ_NaI(Tl) end-to-end derivation matches ~10⁻² order needed for DAMA ε_det
- κ_HPGe (no dopant, pure covalent Ge) gives ~10⁻⁴ substrate-baseline matching MAJORANA bound
- κ_Sapphire (Al₂O₃, no closed-shell dopant) gives ~10⁻³-10⁻⁴ matching null constraint
- **Implication:** ε_det = 4π·κ_quality/N² becomes a parameter-free prediction across the cross-detector cluster. Framework survives.

### Outcome B (framework partially holds — Tl mechanism works but cross-element scaling fails)
- η_Tl derives correctly from 6s² angular phase
- κ_NaI(Tl) magnitude ~10⁻² roughly correct
- BUT κ_HPGe or κ_Sapphire prediction is off by ≥1 OOM
- **Implication:** Cross-detector cluster falsifier survives partially — Tl-dopant mechanism is established but the substrate-baseline for non-doped detectors needs separate work. Framework walks back to "Tl-dopant lone-pair Q-factor is mechanistically derived; cross-detector cluster requires Step 2 (heavy-element table extension) for closure."

### Outcome C (framework walks back — Tl mechanism doesn't derive at first pass)
- η_Tl does NOT cleanly derive from 6s² inert pair angular phase using existing CTG-1/2/4 pieces
- OR: η_Tl derives but the magnitude is off by ≥2 OOM
- OR: the substrate-baseline derivation requires phonon-coherence work (Step 4) that isn't in current corpus
- **Implication:** κ_quality is GENUINELY OPEN at the materials-science derivation level. Multi-session program (Steps 2-6) remains required. Framework walks back the "1-session closure" claim and confirms the Foundation Item 10 corpus-state finding that "κ_quality materials-science derivation is multi-session open work."

## What this attempts (mechanical pieces)

1. Read CTG-1 (per-element Z_atom table) to get Z_Na, Z_I, Z_Tl values
2. Read CTG-2 (Γ_ij inter-element formula) to compute Γ_NaI baseline reflection coefficient
3. Read CTG-4 (lone-pair Q-factor η_lp = 1/9 derivation) to understand the H₂O sp³ analog
4. Identify the 6s² inert pair angular phase — is it cos²(0°) = 1 (s-orbital is spherically symmetric)? cos²(180°)? Something derived from the L = 0 → L = 0 transition?
5. Apply: κ_NaI(Tl) = f(Z_Na, Z_I) × η_Tl × (atomic fraction × phase-bin enumeration)
6. Cross-check: κ_HPGe = f(Z_Ge) with no η_Tl multiplier (covalent, no closed-shell dopant)
7. Cross-check: κ_Sapphire = f(Z_Al, Z_O) with no η_Tl multiplier (no closed-shell dopant)

## Falsifier (what would invalidate the attempt)

- η_Tl cannot be derived from existing CTG pieces without invoking a parameter that doesn't itself derive from CTG (would be a free fit, defeating the purpose)
- The 6s² inert pair angular phase analysis doesn't return a number — it returns a tautology (e.g., "L=0 means cos²(0)=1" without physics content)
- κ_NaI(Tl) calculation gives the wrong sign or wrong OOM by >2

## Discipline applied

- **ave-prereg:** this doc
- **substrate-native-check trigger 6 (prose-derivation construction):** will walk the 7 checkpoints WHILE assembling the derivation, not after
- **consistency-vs-emergence:** if the Tl-dopant mechanism derives, it's an emergence test (Class D) — the H₂O lone-pair Q-factor was derived for organic chemistry; applying it to Tl 6s² is an emergence claim about substrate-universal lone-pair coupling. NOT a consistency check.
- **ave-canonical-leaf-pull trigger 4 (existing corpus has the pieces):** must use CTG-1/2/4 verbatim from corpus, not re-derive
- **No external references** per pure-AVE-corpus rule

## Authorship

- Foundation Item 10 REVISE-LATERAL outcome required κ_quality to become a derived quantity
- User authorized Option A (Tl-dopant first-pass NOW) over Options B/C (defer multi-session work) on 2026-05-17
- Auditor recommendation: assemble CTG-1+2+4 into Tl-dopant first-pass; ~1 session attempt; could partially close OR confirm gap

---

**Status:** prereg COMMITTED. Now assembling derivation. Result to land at `2026-05-17_kappa-quality-tl-dopant-first-pass-result.md` regardless of outcome (A, B, or C).
