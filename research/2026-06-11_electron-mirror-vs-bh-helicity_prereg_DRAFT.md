# T4 — Electron mirror vs BH boundary: helicity at Γ=−1 (Pre-Registration DRAFT)

**Parent:** `research/2026-06-11_helicity-visual-model.md`  
**Status:** DRAFT — **not frozen**; does not touch canon  
**Motivation:** Grant visual picture conflates (a) electron reactive mirror trap, (b) BH/horizon Γ=−1, and (c) "inverted crystal" allowing one helicity only. This prereg separates falsifiers.

---

## 1. Derivation target (one sentence)

> At AVE **Γ=−1** boundaries, determine whether an incident transverse wave's **helicity sign is preserved, flipped, or annihilated** — and whether **symmetric gravity** (Z=Z₀) and **asymmetric saturation** (Z→0) boundaries behave differently.

---

## 2. Physical picture (pre-test)

| Boundary class | Corpus expectation | Helicity hypothesis |
|----------------|-------------------|---------------------|
| **SYM gravity** (weak field) | Z_eff = Z₀, Γ≈0 | No sign change; no "inverted crystal" filter |
| **Electron-class trap** (CVR core) | Z→0, Γ→−1, standing reactive | Reflect/absorb; **not** a global helicity flip valve |
| **Horizon-class** (Γ→−1 pole) | Rupture / saturation boundary | Reflect or trap; **sign-flip is NOT assumed** |

**Grant hypothesis under test (H_T4):** BH-like oversaturation **does not** selectively admit left-handed helicity into an "inverted crystal." If supported, that image is **retired**. If falsified, name the mechanism — do not merge with lattice D1 without a second gate.

---

## 3. Consistency-vs-emergence tag

| Sub-test | Class |
|----------|-------|
| Γ from impedance definition | A (identity) |
| Compare SYM vs ASYM reflection coefficient | C (consistency — both routes use corpus Op14) |
| "Helicity sign change at boundary" | **D** (emergence) — must not use target helicity as input |

---

## 4. Three-arm simulation battery (minimal, Phase-0/1 scale)

All arms: launch **linear pol**, fixed k, single frequency; measure helicity proxy **before** and **after** interaction region.

| Arm | Setup | Observable |
|-----|-------|------------|
| **T4-A** | **Symmetric** Op14 strain (μ, ε scale together): Z invariant | Δ(sign h_proxy), \|Γ\| |
| **T4-B** | **Asymmetric** saturation (electron-class, `κ·h` or seeded core): Z→0 locally | Same |
| **T4-C** | **Horizon-class** Γ→−1 template (existing horizon/impedance boundary observer if available; else impedance-clamp BC) | Same |

**Helicity proxy (locked at freeze):** circulation of transverse phasor in (V_inc, V_ref) plane per A46 — **not** lattice-Cartesian amplitude.

---

## 5. Pre-registered predictions (placeholders ⟨…⟩)

| ID | Prediction | PASS | Falsifier |
|----|------------|------|-----------|
| **T4-P1** | T4-A: \|Γ\| ≤ ⟨0.05⟩; helicity sign unchanged to ⟨1°⟩ equivalent | Stealth gravity | Large Γ or sign flip ⇒ SYM path wrong |
| **T4-P2** | T4-B: \|Γ\| ≥ ⟨0.9⟩ at core; energy predominantly reflected/trapped | Electron mirror | Transparent core |
| **T4-P3** | T4-B/C: helicity sign **unchanged** on reflection (\|Δsign\| = 0 within ⟨noise⟩) | Mirror reflects, does not flip h | Sign flip ⇒ "inverted crystal" valve **live** — escalate |
| **T4-P4** | T4-B vs T4-C: same sign rule (both Γ≈−1) — mechanism may differ, **helicity rule identical** | Unified Γ pole | BH flips, electron does not (or converse) without named mechanism |

**Default noise floor (delegated):** ⟨1°⟩ polarization equivalent from Phase-1 P2 diamond floor (5% of srs) scaled to T4 grid.

---

## 6. Controls

- RH vs LH **launch** (circular basis decomposition from linear + geometry — or explicit small circular fraction tagged).
- `κ_chiral = 0` on T4-A.
- Reverse propagation direction (A2 hygiene).

---

## 7. Kill conditions

- T4-P3 **sign flip** on any arm without pre-registered boundary model ⇒ **stop**, write result, do not fold into CVR genesis narrative until replicated.
- Cannot separate SYM vs ASYM in code ⇒ return **BLOCKED**, do not substitute prose.

---

## 8. Sequencing

1. **After** v9 Phase-1 vector-TLM exists (P1 PASS) — shares transverse channel machinery.
2. **Parallel OK** with D1 Phase-1; **no** lattice identity ruling in this doc.
3. Implementor branch: `analysis/2026-06-12-t4-helicity-at-gamma-minus-one` (proposed).

---

## 9. Grant freeze checklist

- [ ] Ratify ⟨Γ⟩ and ⟨noise⟩ thresholds
- [ ] Confirm T4-C boundary implementation (horizon observer vs impedance-clamp)
- [ ] Confirm helicity proxy definition matches Phase-1 P2
