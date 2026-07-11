# RESULT — X43 Appendix A0: the tide-branch dimensional-`L` kill-test → **TIDE BRANCH DEAD AT BIRTH**

**Date:** 2026-07-11 · **Branch:** `analysis/x43-ringdown-port` · **Class:** CONSISTENCY / scope-closure (a KILL — negative outcome, not an emergence claim).
**Severable appendix** to the X43 ringdown-port arc (`_orchestration/2026-07-11_x43-ringdown-port-handoff.md`); run FIRST per the brief (kill-on-failure expected). **Kill-test criterion inherited-frozen** from `research/2026-07-11_keying-register-walk_framing.md` §4 kill-test #1 (on `origin/main`); NOT re-minted here.
**Pre-reg:** `research/2026-07-11_x43-ringdown-port_prereg.md` §"APPENDIX A0" (frozen, pushed before this result — commit `8d672d3a`).

---

## SECTOR HEADER

**SECTOR / REGIME / PHASE-STATE.** Gravity-bulk (Axiom-4 `η_eff` saturation of the galactic drag), weak-field embedded-dwarf regime. The object under test is the **argument** of the saturation kernel `S(A) = √(1−A²)` in the §4 T4 "third branch," which keys on the external **tide `∇g_ext`** rather than external acceleration `g_ext`.

---

## VERDICT

> **The §4 T4 tide-EFE "third branch" DIES AT BIRTH.** There is **no canon-chain-FORCED length `L`** at the galactic (~kpc, `10¹⁹–10²¹` m) scale that a tide-keyed Axiom-4 kernel requires. Per the frozen binary criterion (no forced `L` → dead; forced `L` → write the kernel + flag to astro-sweep A2): **report the tide branch DEAD to the docket.** The astro-sweep A2 lane inherits **nothing** from this appendix (no tide-kernel FORM to flag).

The kill is robust on two independent fronts (an exhaustive canon-length enumeration and an adversarial *save-the-branch* refute-pass, both read-only): the enumeration finds no galactic-scale forced length; the refute-pass, tasked to save the branch, concedes `branch_survives = false` after testing every horizon-, length-free-, system-size-, and numerology-combination candidate.

---

## THE KILL-TEST (why a length is needed, and why its absence kills the branch)

The canonical MOND kernel keys on `g_N/a₀` — **dimensionless** (acceleration / acceleration), with `a₀ = c·H_∞/2π ≈ 1.07×10⁻¹⁰ m/s²` (`derived-mond-acceleration-scale.md:15`). Its transition radius is **emergent per-galaxy**, `r = √(GM/a₀)` — an OUTPUT of the galaxy's own imported baryonic mass, **not** an input length (verified: `1.14 kpc` for a `10⁹ M_⊙` dwarf, `8.83 kpc` for a `6×10¹⁰ M_⊙` Milky Way). **No length is needed** because the argument is an acceleration ratio.

A **tide-keyed** argument is structurally different. A tide `∇g` has units `s⁻²` (acceleration / length). To enter the kernel dimensionlessly it must be formed as `(∇g · L)/a₀` — which **requires a length `L`**. The whole branch stands or falls on whether the canon chain **forces** such an `L` at the scale where galactic phenomenology lives (`L ~ kpc` so the transition lands at `O(1)`).

---

## THE ENUMERATION — canon forces exactly TWO length poles, with a 39-OOM gap

| Length | value (m) | forcing | scale | source |
|---|---|---|---|---|
| `ℓ_node ≡ ℏ/(m_e c)` | `3.862×10⁻¹³` | **canon-forced** (the primitive) | microscopic | `constants.py:291` |
| `ℓ_c = √6·ℓ_node` (Cosserat coupling) | `9.46×10⁻¹³` | derived (×ℓ_node) | microscopic | `constants.py:336` |
| Bohr `a₀ = ℓ_node/α` | `5.29×10⁻¹¹` | derived (×ℓ_node) | atomic | `constants.py:346` |
| weak `l_c = √(γ_c/G_vac)` | `~10⁻¹⁸` | derived (Cosserat moduli) | subnuclear | `gauge-boson-masses.md:39` |
| proton/nuclear (`4ℓ_node·m_e/m_p`, …) | `10⁻¹⁵`–`10⁻¹⁶` | derived | subnuclear | `constants.py:1113,1117,1142` |
| **`R_H ≡ c/H_∞`** (de-Sitter horizon) | `1.335×10²⁶` | **canon-forced** (sets `a₀`) | cosmic | `constants.py:753` |
| **`L_gal` (what the tide needs)** | **`~10²⁰` (needed)** | **ABSENT from canon** | galactic | `universal-saturation-kernel-catalog.md:52` (`L_gal = "TBD"`) |

**The canon forces `ℓ_node` (microscopic) and `R_H` (cosmic) and nothing between.** The two forced-pole gap `ℓ_node → R_H` is **~39 orders of magnitude** (`log₁₀(1.335×10²⁶ / 3.862×10⁻¹³) = 38.5`); even measuring from the *derived* Bohr pole `a₀` (`5.3×10⁻¹¹ m`) to `R_H` the span is **~36.4 OOM** — either way it **fully CONTAINS the galactic kpc scale, and canon defines NO forced length in it.** A grep for kpc/parsec/`10¹⁹`–`10²¹` across `constants.py` + the entire `ave-kb` returns only (a) per-galaxy *observational* `R_d`/`M_disk` in SPARC-fit tables, (b) the bullet-cluster `~150 kpc` offset the KB itself flags matched-by-construction / "do not build on" (`clm-527k22`), and (c) the `L_gal = "TBD"` placeholder — **none a forced constant.**

---

## THE ADVERSARIAL SAVE-THE-BRANCH PASS — every candidate FAILS on ≥1 of the three axes

A candidate `L` (or length-free tide argument) **SAVES** only if it is (1) **dimensionally consistent**, (2) **canon-forced** (not picked by taste), AND (3) **phenomenologically OK** (lands galactic systems near argument `O(1)` at the MOND transition). Numbers use the source-stated Crater-II-class case (`g_ext = 2a₀`, `R_gal = 30 kpc`, `∇g = g_ext/R = 2.32×10⁻³¹ s⁻²`).

| Candidate `L` / argument | dim? | canon-forced? | pheno? | verdict | why it fails |
|---|---|---|---|---|---|
| **(a) `L = R_H = c/H_∞`** → `(∇g·R_H)/a₀` | ✔ | ✔ | ✗ | **FAILS** | `= 2.88×10⁵` — ~5 OOM too big; the horizon puts the MOND transition at **cosmological**, not galactic, scale. |
| **(b) length-free `∇g/H_∞²`** | ✔ | ✔ | ✗ | **FAILS** | **Identical to (a)** up to `2π` via the verified identity `a₀/R_H = H_∞²/2π` (`= 8.03×10⁻³⁷`), so `∇g/H_∞² = (1/2π)(∇g·R_H)/a₀ = 4.6×10⁴`. Not an independent escape. |
| **(c) `L = system size` (~15 kpc)** | ✔ | **✗** | ✔ | **FAILS** | Phenomenology OK **because** `L` is a per-system tunable (`L ~ a₀/∇g`), not a canon quantity — exactly the "picked by taste" the kill-test forbids. A *different* `L` for every system ⇒ no universal law. |
| **(d-i) `L = Bohr a₀` or `ℓ_node`** | ✔ | ✔ | ✗ | **FAILS** | `(∇g·a_Bohr)/a₀ = 1.1×10⁻³¹`; `(∇g·ℓ_node)/a₀ = 8×10⁻³⁴` — ~31–33 OOM below `O(1)` (dead kernel). Confirms the Bohr-`a₀`/MOND-`a₀` homonym is a trap. |
| **(d-ii) `L = R_H·α² ≈ 7×10²¹ m`** | ✔ | **✗** | ✔ | **FAILS** | Lands at `15.3` (~galactic) — the seductive numerology shot — but is **reverse-engineered**: the only canon place `α` couples to `R_H` is `ξ_M = 4π(R_H/ℓ_node)·α⁻²` (`interlock-register.md:172`), where `α` appears as **`α⁻²` (the wrong sign)**. The `+2` exponent is hand-picked, not Machian-forced. |

**Strongest survival case (the branch's genuine best shot), stated fairly:** the horizon route (a)/(b) is **both dimensionally consistent AND fully canon-forced** — `R_H` is the unique macroscopic canon length (Chain-B′ has **0 closed-form candidates** for any G-length bypassing `R_H`, `interlock-register.md:170,258`). If the bar were only "dimensionally consistent + canon-forced," it passes. **It dies solely on phenomenology:** the one canon-forced macroscopic length is ~5 OOM too long, so it places the transition at cosmological scale.

---

## THE PHYSICAL REASON (why no patch saves it)

**A tide × length is intrinsically a per-object quantity — that is what a tide *is*.** The canon supplies no universal macroscopic length between the atomic `ℓ_node` and the cosmological `R_H` that both (i) the Machian structure **forces** and (ii) lands galactic systems near argument `O(1)`. The acceleration-keyed MOND kernel escapes this because `g_N/a₀` needs no length; the tide branch cannot, because its argument is dimension-ful without one. **This is the branch's own §4 first gate firing exactly as written.**

---

## RECOMMENDED DOCKET / REGISTRY ENTRY (recommended, NOT executed — lane discipline)

This appendix is a read-only audit finding. The corresponding **docket entry and any T4-registry update require implementer execution in the owning lane** (the astro-sweep / rulings-docket lane); no cross-lane authorization was given here. **Recommended entry for Grant/the core session:**

- `_orchestration/…rulings-docket` / `research/2026-07-10_collapse-target-registry.md` **T4**: the §4 KEEP-BOTH **tide-`∇g_ext` third branch** is **RETIRED (dead at birth)** — no canon-forced galactic-scale `L`; the horizon length is the only forced macroscopic candidate and is phenomenologically dead by ~5 OOM. The frozen T4 pair (**internal `g_N`** vs **total local field**) is **unaffected** — both remain acceleration-keyed and need no length; only the *tide* third axis dies.
- **Astro-sweep A2 lane** (`2026-07-11_astro-adjudicator-sweep-handoff.md`): inherits **no** tide-kernel FORM from A0 (the branch it would have adjudicated is dead upstream).

---

## PROVENANCE

Two-front adversarial probe (workflow `x43-A0-tide-dimensional-L`, run `wf_774719ce-8d4`): an exhaustive canon-length enumeration (`ave-corpus-grep`, `galactic_scale_forced_length_exists = false`) + an adversarial *save-the-branch* refute-pass (`ave-auditor`, `branch_survives = false`), both read-only against `origin/main`, every value grep/Read-verified. Constants: `H_∞ = 28π·m_e³·c·G/(ℏ²α²)` (`constants.py:750`), `R_H/ℓ_node ≈ 3.456×10³⁸`, `ξ_M ≈ 8.155×10⁴³`.
