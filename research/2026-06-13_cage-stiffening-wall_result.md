# Cage stiffening-wall self-focus test (A1 dilatation) — RESULT (2026-06-13)

> **Prereg:** [`2026-06-13_cage-stiffening-wall_prereg_FROZEN.md`](2026-06-13_cage-stiffening-wall_prereg_FROZEN.md) (+ Amendments 1 & 2).
> **Branch:** `analysis/2026-06-13-cage-stiffening-wall` (implementor lane).
> **Engine:** `ave.core.crystal_engine.CrystalEngine` bulk branch (= the v14-Mode-I-validated `master_equation_fdtd.py`), AS-IS — driver job, engine unmodified.
> **Driver:** [`src/scripts/vol_1_foundations/cage_stiffening_wall.py`](../src/scripts/vol_1_foundations/cage_stiffening_wall.py) · **Keeper:** [`src/tests/test_cage_stiffening_wall.py`](../src/tests/test_cage_stiffening_wall.py) (11 pass) · **Data:** `cage_stiffening_wall_results.json`.

---

## TL;DR (framed per prereg A2 — NON-NEGOTIABLE)

- **The positive (consistency anchor):** the bare standing A1-dilatation `self.V` **SELF-FOCUSES** into the persistent breathing cage **when seeded with the soliton EIGEN-PROFILE (sech)** — `max|A|` grows beyond the seed, `gamma_bulk_min` deepens below t=0, and it persists, bounded. **This confirms `self.V` is the self-trapping grade, consistent with v14 Mode I.** It does **NOT** "build the electron cage" (v14 built it) and is **NOT** "scalar beats transverse" (moot — the harness cannot host the cage). CONSISTENCY-class, closing the "which V" question.
- **The pre-registered seed DISPERSES:** the prereg §2 `seed_bulk` **GAUSSIAN** profile **DISPERSES at every frac** {0.30 → 0.95}, converter OFF *and* ON — no growth beyond seed, no wall-deepening, **no critical-frac**. The cage's nucleation is **PROFILE-selective**; the Gaussian is not in the breather's basin of attraction.
- **The new load-bearing question this surfaces: "which SEED?"** — as load-bearing as the "which V" question the prereg closed. In the *identical* box at *matched* amplitude, the sech self-focuses and the Gaussian disperses (FLAG 1).

---

## Per-arm bins (prereg §3 / A2.1 — five bins)

| Arm | Config | frac/amp swept | Bin(s) | Critical-frac (A4) |
|:---|:---|:---|:---|:---|
| **F0** | no seed, conv OFF | — | **NO-WALL** (`γ_min_t0 = γ_min_deepest = 0`) | n/a |
| **S1** | `seed_bulk` Gaussian, conv **OFF** (bare V self-trap) | 0.30·0.50·0.70·0.85·0.95 | **DISPERSES ×5** | **None** (disperses at all frac) |
| **S2** | `seed_bulk` Gaussian, conv **ON** (+ ADD-2) | 0.30·0.50·0.70·0.85·0.95 | **DISPERSES ×5** | **None** (converter does not rescue) |
| **ANCHOR** | sech eigen-profile (v14 direct-assign), conv OFF | 0.20·0.30·0.50·0.70·0.85 | **SELF-FOCUS ×5** | **< 0.20** (nucleates at all tested amp) |
| **PROFILE** | sech vs Gaussian, identical box (N=24, dx=0.5) | 0.50, 0.85 | sech **SELF-FOCUS** / gauss **DISPERSES** | — |

**Bin definitions exercised (classifier proven on synthetic records — all five reachable):** SELF-FOCUS / TRANSIENT / **PLANTED-ONLY** / DISPERSES / (+ DETONATION-PUMP for the F4-fail genesis-24 outcome). The PLANTED-ONLY-vs-SELF-FOCUS guard (prereg A2.1, the whole point) is unit-tested: a flat planted wall (`γ<0` at t0, `max|A|` flat, no deepening) classifies **PLANTED-ONLY, never SELF-FOCUS**.

### S1 / S2 (the pre-registered Gaussian arms) — DISPERSES, verbatim production read

```
S1 (conv OFF):  frac=0.30 A0=0.300 Apk=0.300 Apersist=0.037 g0=-0.0059 gdeep=-0.0059 dEc=-9% -> DISPERSES
                frac=0.50 A0=0.500 Apk=0.500 Apersist=0.062 g0=-0.0180 gdeep=-0.0180 dEc=-7% -> DISPERSES
                frac=0.70 A0=0.700 Apk=0.700 Apersist=0.087 g0=-0.0421 gdeep=-0.0421 dEc=-4% -> DISPERSES
                frac=0.85 A0=0.850 Apk=0.850 Apersist=0.107 g0=-0.0799 gdeep=-0.0799 dEc=-1% -> DISPERSES
                frac=0.95 A0=0.950 Apk=0.950 Apersist=0.121 g0=-0.1445 gdeep=-0.1445 dEc=+2% -> DISPERSES
S2 (conv ON):   same -> DISPERSES ×5; converter_work in [-1.40, -2.4e-6] (bounded, energize-LOCK)
```

`Apk = A0` at every frac → the field **never grows beyond the seed** (F1-FAIL). `gdeep = g0` at every frac → the wall **never deepens below its t=0 read** (F3-FAIL): the `γ<0` is purely the seed amplitude re-read through the algebraic kernel (CP9), not a self-created wall. `Apersist` decays to 4–13% of the seed → the amplitude shrinks. **This is the clean honest negative for the prereg §2 seed.**

### ANCHOR (sech eigen-profile, conv OFF) — SELF-FOCUS, verbatim production read

```
amp=0.20 A0=0.200 Apk=0.396 Apersist=0.185 g0=-0.0026 gdeep=-0.0107          dEc=+879% maxV=0.40 -> SELF-FOCUS
amp=0.30 A0=0.300 Apk=0.583 Apersist=0.270 g0=-0.0059 gdeep=-0.0259          dEc=+869% maxV=0.58 -> SELF-FOCUS
amp=0.50 A0=0.500 Apk=0.899 Apersist=0.411 g0=-0.0180 gdeep=-0.1028          dEc=+790% maxV=0.90 -> SELF-FOCUS
amp=0.70 A0=0.700 Apk=1.075 Apersist=0.501 g0=-0.0421 gdeep=-0.2400(=floor)  dEc=+602% maxV=1.08 -> SELF-FOCUS
amp=0.85 A0=0.850 Apk=1.219 Apersist=0.566 g0=-0.0799 gdeep=-0.2400(=floor)  dEc=+484% maxV=1.22 -> SELF-FOCUS
```

`Apk ≈ 2× A0` (grows beyond seed, F1-PASS), `gdeep < g0` (deepens below t0, F3-PASS), persists bounded. **Independent v14 sanity:** the same engine + sech reproduces v14 Mode I (post-transient `V_peak` mean 0.644, breathing std/mean 0.374 — PASS the regression-test criteria).

---

## Envelope trend (A2.4) — flat-persistent, NOT transient

Resolving SELF-FOCUS vs TRANSIENT over a long run (sech amp 0.85, **1500 steps**): `Apersist = 0.637`, `envelope_late/envelope_mid = 1.048` → **flat-persistent breather** (a TRANSIENT would slow-decay; this does not). The Gaussian arms' `late/mid ≈ 1.05–1.08` is **flat at near-zero** (0.04–0.13, a PML-absorbed dispersed remnant) — flat-at-floor, not a retained bound state. The two "flat" envelopes are physically opposite: one persistent at the breather amplitude, one extinguished.

---

## F1 ∧ F4 co-occurrence (A2.3) — the self-focus-vs-pump discriminator

| | `max|A|` grows? | bounded (no detonation)? | verdict |
|:---|:---|:---|:---|
| sech anchor | YES (`Apk` up to 1.22) | YES (`maxV ≤ 1.22 ≪ 10`) | **self-focus** (concentrating) |
| Gaussian S1/S2 | NO (`Apk = A0`) | YES | disperse |
| (synthetic genesis-24) | YES | NO (`maxV → 1e4`) | DETONATION-PUMP |

The self-focusing sech stays **bounded at ≈ V_yield** (the saturation cap) — it is the soliton signature (energy *concentrating* in a bound state), categorically distinct from genesis-24's detonation (`max|V_inc| → 1.08e4`, `E_V → 6.8e8`). No arm detonated.

---

## Conservation (F4) — and a flag on the frozen criterion (see FLAG 2)

- **`converter_work`** (S2): bounded, `[-1.40, -2.4e-6]` — energize-LOCK, no one-way runaway. (S1 trivially 0 — converter off.)
- **`total_energy` drift:** Gaussian arms within ±10% (dispersing, then PML-absorbed).
- **`bulk_energy_conserved` drift:** Gaussian arms ±2–9% (≈flat). **The self-focusing sech grows it +484% → +907%** (bounded, oscillating ≈ 8×, NOT detonating). See FLAG 2 — this is the canonical v14 breather's own behavior on this engine, so the literal frozen "bulk_E_conserved flat" criterion needs adjudication.

---

## Magnitude — APPARATUS-QUALIFIED (prereg A3 / §3; NEVER binned on Γ=−1)

The wall depth is **doubly bench-capped** and is **reported, not a verdict axis**:

1. **Clip floor:** `A_cap = 0.99` floors the achievable `gamma_bulk_min` at **−0.2400** (S^{1/4} index; `A_cap` binds, not `S_min`). The self-focusing sech at amp ≥ 0.70 sits **exactly on this floor** (`gdeep = −0.2400`) → its depth is **bench-limited, not physics**. The shallow seeds (amp 0.20–0.50) deepen to −0.011 → −0.103 (below t0, above the floor — genuine dynamic deepening).
2. **Exponent defect** (`crystal_engine.py:421-432`, flag-don't-fix): the diagnostic uses `n = S^{1/4}` but the wave-speed identity `c_eff² = c0²/S` implies physical `n = S^{1/2}` — which would deepen the same floor to **−0.4539**. Understates depth; sign unaffected. A PHYSICS-REVIEW item, not landed here.

A genuine cage reaching only −0.24 dynamically is a **PASS**, exactly as the prereg anticipated.

---

## Hypothesis dispositions (prereg §5 — consistency-vs-emergence)

| ID | Statement | Class | Disposition |
|:---|:---|:---|:---|
| H1 | master-eq bulk V self-focuses (de-contaminated seed) | consistency-check | **CONFIRMED** for the sech eigen-profile; `self.V` is the self-trapping grade ("which V" closed). |
| H2 | cage self-creates with `converter_on=False` (bare V self-trap) | emergence-test (narrow) | **CONFIRMED for the sech, FALSIFIED for the Gaussian** — the bare V self-traps from the eigen-profile (converter off), but NOT from the prereg §2 Gaussian. |
| H3 | ADD-2 converter deepens/sharpens the wall vs S1 | consistency-check | **N/A for the Gaussian** — it forms no wall to sharpen; the converter does not rescue dispersal. (Converter-on sech is downstream / out of scope here.) |

**Overall: CONSISTENCY-class** (v14 Mode I re-confirmation on the engine that hosts the A1 channel), with one new structural finding — the nucleation is **profile-selective** (FLAG 1). Not an emergence frontier; retention/R10/the-loop remain the downstream open frontier (prereg §6, out of scope).

---

## FLAGS for adjudication (flag-don't-fix — surfaced, NOT silently resolved)

**FLAG 1 — "which SEED?" / a prereg-internal tension (§2 Gaussian vs A2 sech target).** The prereg §2 pins the seed as `seed_bulk` (a **Gaussian**), but its A2 framing target — "reproduce the v14 self-trap" — used a **sech** (the v14 doc/test eigen-profile). These diverge decisively: in the *identical* box at *matched* amplitude (converter OFF), the **sech self-focuses and the Gaussian disperses**. So the literal pre-registered arm (Gaussian) returns DISPERSES; the consistency-with-v14 positive requires the sech. *The "which seed" question is now as load-bearing as the "which V" question the prereg closed.* Mechanism: the sech is the soliton eigen-profile (fat exponential tails matching the bound-state); the Gaussian (thin tails) sheds its shape-mismatch as radiation and disperses — it is not in the breather's basin at any sub-saturation amplitude or PML-safe width tested (σ = 3 → 10 cells, N = 37 and N = 64 big-box). **For adjudication:** should the prereg's "self-create from `seed_bulk`" be read as falsified (the Gaussian does not nucleate), or should the seed be the eigen-profile (then the positive stands, v14-consistent)? I did NOT silently substitute the seed — both arms are reported under their own labels.

**FLAG 2 — the frozen F4 criterion ("bulk_E_conserved flat") would falsify canonical v14.** The self-focusing sech grows `bulk_energy_conserved` +484% → +907% (bounded, oscillating ≈ 8×, not detonating). This is **the canonical v14 Mode I breather's own behavior** on this engine (same engine, same sech; the v14 regression test deliberately does not gate on energy). Applying the literal frozen F4 would therefore falsify the already-accepted v14 Mode I — evidence the criterion is mis-specified for this leapfrog, not that v14 is wrong. The growth is a **numerical leapfrog-at-saturation-front artifact**, not a physical pump: (a) it occurs with `converter_on=False` (no source term in the pure master equation); (b) the field stays bounded at ≈ V_yield (a real pump → unbounded); (c) it *decreases* with seed amplitude (+879% at amp 0.20 → +484% at 0.85 — inverse of a saturation-driven pump). **The operative self-focus/pump discriminator used here is BOUNDEDNESS + PERSISTENCE (vs genesis-24 detonation to ~1e4), not energy-flatness.** The classifier does NOT gate SELF-FOCUS on energy-flatness; it reports the drift and flags it. **For adjudication (Grant/auditor):** confirm the energy-flat F4 reading is superseded by the boundedness reading on this engine, or specify the variable-coefficient ledger that *is* flat for the v14 breather.

**FLAG 3 (confirmation, not a defect):** the magnitude sits on the −0.2400 clip floor for the deep seeds, exactly as the prereg's apparatus-qualification anticipated. Reported, not binned.

---

## Substrate-native-check (design-time, walked against the actual engine)

- **CP8 (generative precursor, THE checkpoint):** seeded a bare, sub-saturation, standing `self.V` (`∂_tV = 0`); the wall must EMERGE, not be planted. ✓ (seeds span frac 0.20 → 0.95, all sub-`A_cap`.)
- **CP9 (dynamical-not-algebraic):** the signal is the **dynamic** `max|A|` growth + `gamma_bulk_min` deepening *below t0*, NOT the t=0 algebraic `gamma_bulk` read. ✓ (the whole DISPERSES verdict rests on `gdeep = g0` — no dynamic deepening.)
- **CP10 (boundary-not-bulk):** the wall is read as the `Γ = (n−1)/(n+1)` boundary (`gamma_bulk`), never a bulk confining force. ✓
- **phase-space-coordinate-check:** the corpus claim here is a **real-space scalar-amplitude self-focusing** claim (does `|V|/V_yield` self-steepen), measured in the engine's own `A = |V|/V_yield` and Smith-Γ coordinates — coordinate-matched. The A46 phase-space (2,3)-winding trap applies to the CHARGE "3" (`phase_space_vinc_vref`), explicitly out of scope (prereg §6). ✓

---

## Reproduce

```bash
PYTHONPATH=src .venv/bin/python src/scripts/vol_1_foundations/cage_stiffening_wall.py --production   # ~15 s
PYTHONPATH=src .venv/bin/python -m pytest src/tests/test_cage_stiffening_wall.py -v                  # 11 pass, ~2 s
```

(Interpreter: `/Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python`.)
