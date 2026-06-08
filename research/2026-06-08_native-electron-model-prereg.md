# Prereg: Native AVE electron model (4-property joint seed)

**Status:** FROZEN PREREG.
**Driver:** `src/scripts/vol_1_foundations/native_electron_model.py`

---

## §0 Question

Does the **corpus-correct joint seed** — Golden Torus \((R,r)\) + \((2,3)\) quadrature \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) + **0₁ unknot** Cosserat \(\omega\) — **persist** as an electron identification on `VacuumEngine3D` **without** manual snap?

This is the substrate-native model attempt; genesis bench snap is a **control arm only**.

---

## §1 Seed (forward, α not a fit knob)

| Layer | Mechanism | Source |
|-------|-----------|--------|
| Phase-space (2,3) | `initialize_quadrature_2_3_eigenmode` @ `R_GOLDEN_TORUS`, `R_GOLDEN_TORUS_MINOR` | doc 28 §5.1 |
| Real-space 0₁ | `initialize_electron_unknot_sector` (horn torus) | electron-unknot.md |
| Engine | `VacuumEngine3D`, asymmetric Op14, zero drive | native lane |

**Variants:** amp=0.48 (sub-yield), amp=0.92 (saturated); bench snap @ trap=1.25 control.

---

## §2 Property checks (electron-identification §1)

| ID | Criterion |
|----|-----------|
| P1 | Energy localized on shell (fraction > 0.35) |
| P2 | Shell or bond phasor PCA \(R/r\) within 15% of \(\varphi^2\) |
| P3 | \(\Gamma_{\min} \le -0.99\) sustained (TIR) |
| P4 | \(\|\omega\| \gg \|u\|\) on shell (T₂ dominance) |

**α:** `eps_gamma` vs `ALPHA_COLD` — comparison only.

---

## §3 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | 4/4 properties pass on a canonical arm |
| B | TIR + localization + ≥2 properties |
| C | TIR only |
| D | Persistence fails |

---

## §4 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/native_electron_model.py
```

**JSON:** `src/scripts/vol_1_foundations/_output/native_electron_model_results.json`  
**PNG:** `assets/sim_outputs/native_electron_model_phasor.png`

## §5 Adjudication

**Verdict: `NATIVE_MODEL_TIR_WITHOUT_FULL_FOUR_PROPERTY` (Outcome B) — TIR trap without corpus electron**

| Arm | Snap? | Pass | Γ_min | ε̄ | \|ε−α\| | shell R/r | bond R/r | ω persist |
|-----|-------|------|-------|-----|---------|-----------|----------|-----------|
| canonical_subyield 0.48 | no | 2/4 | −0.994 | 0.0126 | 0.0053 | 4.23 | 7.78 | **0.034** |
| canonical_saturated 0.92 | no | 2/4 | −0.994 | 0.0127 | 0.0054 | 3.50 | 7.85 | **0.034** |
| bench_snap_reference | yes | 3/4 | −0.994 | 0.0323 | 0.025 | 3.92 | **2.13** | 0.034 |

**Properties landed (all canonical arms):** P1 localization (e_shell≈96%), P3 TIR held.  
**Properties failed:** P2 \(R/r \neq \varphi^2\) (bond closest on bench only); P4 T₂ (\(\omega\) decays to ~3% of seed — flywheel dies).

**Key reads:**

1. **Joint Golden-Torus seed + zero drive still pins TIR** — manual snap is **not required** for Γ≈−0.99 once amplitude is in trap regime.
2. **Still not a derived electron** — ω circulation does not persist; crossing count c=1 not corpus (2,3); ε_Γ still ~1.7× α.
3. **Bench snap ≠ better model** — higher ε̄, only marginal bond R/r improvement (2.13 vs φ²=2.62).
4. **Honest model class:** **localized Op14 TIR cavity with (2,3) phasor seed** — missing sustained Beltrami circulation + golden-torus phase-space closure.

**Conclusion:** Corpus-correct **static joint seed** is necessary but not sufficient. Next: back-EMF feedback + reactance-boundary leak + circulation-preserving coupling (see handoff §6 tooling stack).
