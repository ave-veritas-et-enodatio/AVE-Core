# G2: single-auditor audit of #1031 (X44 unblock) at `8b53eaa2`

**Status:** audit record, stage G2 of the R61 gravity audit lane. It is not canon. It repairs nothing, and the X44 physics stays parked.
**Criteria:** `_orchestration/2026-09-30_wave1-gravity-audit-brief.md@d55401e6e60db50b3a24e24fe57777c4fcac964c, section G2`.
**Object:** PR #1031, branch `research/2026-08-27-x44-unblock`, head `8b53eaa2c544e6e628eeb2ee0c3b8d4ae379e9a5`. The head matched the brief's table at launch. Branch line numbers below are at that head.
**Run:** 2026-11-01, one auditor in a throwaway detached worktree, removed afterwards. Merge base `a3f4fef7`. Every file audited is unchanged between the merge base and `origin/main` `cbc668e7`.
**Verified by the launching session, separately from the auditor:** the frozen-prefix hash, the `komar_weight` identity and first-order series, the Z1 algebra against the frozen text and the driver, the docket text, the quoted PR lines, and the test-log summaries.

**MODE / REGIME / PHASE-STATE.** Matter clock; sub-yield engine runs at `A = |ε₁₁|`; cold, static. The clock is a mean deficit, so its existence is not regime-gated and only its magnitude scales.

---

## §1. Bins

| Check | Bin |
|---|---|
| F-3, `komar_weight` against docket Ruling 1 | **F3-MISMATCH-REAL** |
| Frozen-prereg compliance | **BIN-Z-UPHELD**, as procedure only (§3) |
| Engine safety | **ENGINE-EDIT-SAFE**, with two named footguns (§4) |
| Scope of "unreachable at ANY amplitude" | conclusion survives across FAM-A; the numbers stated with it do not transfer (§5) |

---

## §2. F-3: the code's clock has no slope in the strain

**Code, `origin/main`.** `src/ave/gravity/backreaction.py:250-252`: `A = np.clip(np.abs(eps11), 0.0, 1.0)`, `S = saturation_kernel(A, exponent=0.5, S_min=S_min)`, `return np.sqrt(S)`. `src/ave/solvers/graded_vacuum_network.py:229-231`: `base = np.maximum(1.0 - A**2, 0.0)`, `S = base**exponent`, `return np.clip(S, S_min, 1.0)`.

**Result.** For `S ≥ S_min`, `w = (1 − A²)^¼`: maximum difference 1.1e-16 over 100,001 points, and `array_equal` with `sqrt(sqrt(1−A²))` is True. For `S < S_min`, that is `A > 0.9999995`, it returns the constant `√S_min = 0.0316228`. It does not follow `(1−A²)^¼` to zero.

**Series.** `w = 1 − A²/4 − 3A⁴/32 + …`. The linear term is zero, and rescaling `A` cannot create one. Launching-session check: `(1−w)/A²` tends to 0.2500 and `(1−w)/A` tends to 0 as `A → 0`.

**The docket.** `_orchestration/2026-07-10_rulings-docket.md:855`: "### Ruling 1 — F6 Komar-clock register: √S (slope-1) IS the clock — CONFIRMED". At `:857-860`: "**Ruling (paraphrase, faithful).** On Flag F6, Grant confirmed that the **slope-1** quantity `√g₀₀ = √S` **IS the local clock / Komar-redshift weight**. The engine's live `komar_weight` ... is on the correct side".

**What the record settles, and what it does not.**
- It settles the register choice: slope-1 over the slope-2 index (`:881-882`).
- It does not settle that the code is slope-1. That attribution sits inside the paraphrased sentence, and the algebra above contradicts it.
- It cannot show whether Grant's own words carried the code attribution. No verbatim is on file: Ruling 1 labels itself a paraphrase, while the block header at `:834` says "verbatim-faithful".
- It does not fix the functional form past first order, since "slope-1" fixes only the linear coefficient.
- It does not say which side is the defect: the code, or the `= √S` bridge in `temporal-spatial-lattice-decomposition.md`.

**Wrong-coordinate check on this negative.** With `A = √(r_s/r)`, the Axiom-4 `S` equals `√g₀₀` exactly, so the clock would be `S`, not `√S`. That does not rescue the code: the engine's `A = ε₁₁` is affine in `1/r`, and `√S` would still carry slope ½, not 1. It does narrow the prereg's dismissal of the dialect fork (`:155-157`), which holds only for affine `A`.

**Consequence the PR reports, reproduced.** Control `Δ_clock` across FAM-A: 0.01614 / 0.00766 / 0.00426 / 0.00258 against the linear weight's 0.06629 / 0.04638 / 0.03474 / 0.02701, ratios 4.11 to 10.48.

---

## §3. Frozen-prereg compliance

**Frozen prefix.** The file at `44e0315a` is 62,264 bytes and 1,015 lines, blob `1ea7b129d7527f9e4a7e0585f9066b1e8a65e803`. The first 62,264 bytes at the tip hash to the same blob and are byte-identical. The tip blob is `2dd4bf29aa4aa042b5e96dc545936133a4325a2e`; lines 1016-1112 are the appended NOTE 1 and NOTE 2 only.

**Z1 is an identity of its own target.** Frozen definitions: `Δ_clock ≡ Σ T₀₀^matter · (1 − w)` (prereg `:655`) and `Δ_clock^broadcast ≡ (1 − w̄)·M` with `w̄` the `T₀₀`-weighted mean (`:721-722`). So `(1 − w̄)M = M − ΣT₀₀w = ΣT₀₀(1 − w) = Δ_clock` for any `w` and any `T₀₀` with `M ≠ 0`. The driver implements this as frozen (`research/drivers/x44_unblock_run.py:143-144`, `:379-380`).

Live checks: 4,000 adversarial float trials give a maximum deviation of 4.98e-13, and 200 exact-rational trials give exactly 0. The only inputs that exceed 0.10 are roundoff cancellation at `Δ_clock/M ≲ 5e-17`. The unweighted-mean diagnostic the PR flags reads 0.98 on a Gaussian blob, so the detector the prereg meant is not the detector it froze. The prereg's own sentence "This is a genuine gate, not a formality" (`:724`) and the Z1 row answering YES under "can it FAIL?" (`:763`, `:769`) are false as frozen.

**Ladder.** The PR's driver re-run at the tip reproduces the committed JSON with 0 differing leaves: BIN Z, `Z_fires = [Z1]`, `Y_fires = [Y2]`, control `η_mixed` +1.047893, frozen +0.828031. Z2 to Z6 are clear. With Z1 treated as non-firing, the ladder gives BIN Y through Y2 (`V_resid` 1.506e-6 at λ = 0.25), and that residual falls to 2.04e-8 at `outer_tol = 1e-9`. So the Z label rests on Z1 alone.

**Bin reasoning.** The frozen ladder, applied as frozen, outputs Z, and the PR neither re-binned nor repaired. Overturning would mean dropping a frozen clause, which is re-posing it. So BIN-Z-UPHELD. As evidence, the Z verdict says nothing about the run, because it is the output for every non-degenerate input. Nothing is banked either way.

---

## §4. Engine safety

**(a) Bit-identity of the komar default.** `origin/main` source run verbatim against the tip, by `.tobytes()` equality and `array_equal`, no tolerance. `komar_weight` on random arrays is identical. `solve_backreaction` at N = 16 (default call; `komar`, `add_field`, `matter`) and at N = 24, σ = 1.8 through `solve_config` (three modes): all 20 common keys identical. New-only keys: `Delta_clock_src`, `k_clock`.

**(b) Legacy `Delta_clock` under `source_mode="ponderomotive"`.** Footgun 1. `backreaction.py:495` stays the komar reading unconditionally: at σ = 1.8, N = 24, `Delta_clock` = 0.00749 against `Delta_clock_src` = 0.04638, ratio 6.19. The same already held for `add_field` and `matter` at the merge base. The in-tree consumers are `test_nordtvedt_eta.py:124/206` (gated by an assert for komar at `:220`) and `test_grqed_stage3_backreaction.py:164`. None reads it under ponderomotive.

**(c) Tests at the tip, no `-m` filter.** The three-file pytest gives 33 passed, 0 skipped, 0 deselected, 4 warnings. `make test` exits 0: KB tools 359 passed; main phase 3123 passed, 3 skipped, 14 xfailed; serial tail 4 passed. No failure, retry, OOM or timeout. Deviation from the brief's command: `-p no:cacheprovider` was added to keep the worktree clean, which does not change collection.

**(d) Footgun 2: no pytest exercises the new code.** Outside `backreaction.py`, the only hits for the new names are the pass-through in `src/tests/engine_acceptance/_nordtvedt.py:40,104,109,119`. The 33 passes and the green `make test` are legacy-mode receipts. The edit is additive and gated, hence SAFE, but the new mode is exercised only by the research driver.

---

## §5. Scope of "unreachable at ANY amplitude"

The phrase is at `_orchestration/open-items/2026-08-27-x44-unblock.md:44`: "**`f ~ 0.6` is 3.2× above the reachable supremum and is unreachable at ANY amplitude.**" The prereg's own `:942` says "The regime map is `σ = 1.8` only."

Driver copy with line 30 changed only, `SIGMA = 1.8` to each value. Default komar weight, N = 24:

| σ | sup f, converged | at λ (max A) | first unconverged λ | 0.60 / sup |
|---|---|---|---|---|
| 1.4 | 0.1901 | 6 (0.809) | 8 | 3.16 |
| 1.8 | 0.1859 | 8 (0.783) | 12 | 3.23 |
| 2.2 | 0.1909 | 12 (0.834) | 16 | 3.14 |
| 2.6 | 0.1909 | 16 (0.857) | 24 | 3.14 |

σ = 1.8 reproduces the prereg table digit for digit. σ = 2.2 was an extra run beyond the brief's two.

- **Survives:** `f ~ 0.6` sits about 3.1 to 3.2× above the komar-weight supremum at all four FAM-A members.
- **Does not transfer:** the turnover at λ ≈ 8, "fails for λ ≳ 12" (σ = 2.6 converges at 12 and 16) and the ceiling "`ε₁₁ ≤ 0.783`" (converged maxima reach 0.857). These are σ = 1.8 figures stated at prereg `:384-386` as if they were engine properties.
- **Weight dependence, an extra probe with one more line changed:** under `source_mode="ponderomotive"` at σ = 1.8, f = 0.1955, 0.2288, 0.2427 at λ = 8, 12, 16, all converged, with no turnover. The PR's own FAM-B row at λ = 8 (f 0.1955, max A 0.822) already breaks the band at prereg `:386`.
- **Not tested:** N ≠ 24, `g_self` ≠ 1, other profiles, λ > 24. "ANY amplitude" is a ten-point grid ending at 24.

---

## §6. Finding on the frozen criteria (recorded, not re-posed)

UPHELD / OVERTURNED is not defined for a ladder whose first gate fires on every input. The bin here answers "does the frozen ladder, applied as frozen, output Z". This criterion is left as posed.

---

## §7. Where this departs from the PR's own claims

The PR's NOTE 2 flags Z1 as an identity (F-1), which this audit confirms. It departs on the consequences:

1. Result `:34` calls the outcome "a real outcome, not a failed run". With Z1 an identity, bins A to D are unreachable for every non-degenerate run. That is the defect the prereg diagnosed in its predecessor: "So the verdict was fixed by the freeze, not by the substrate" (prereg `:65`).
2. Result `:418-419` says the gates caught the run "via Z1, an unrelated defect, and that is luck rather than protection". It is structure, not luck.
3. Prereg `:895` says bin A "banks on P9 + P7 + Z1", which is vacuous as frozen.
4. The open item's "ANY amplitude" and the prereg's band read wider than a σ = 1.8, komar-weight, N = 24 grid (§5).
5. "33 passed" reads as cover for the engine edit; it covers legacy modes only (§4d).

**Receipts that hold at the tip:** the committed JSON, 33 passed, control +1.047893, the FAM-A table, the F-3 `Δ_clock` numbers and the frozen-prefix blob.

---

## §8. Grant question, for a later sitting, routed nowhere

The clock you confirmed falls off in a straight line going into the well; the code's clock is a bowl, flat in a planet's orbit and curling down only near yield.
Which shape is the engine's clock, and is the `A` inside it the strain or its square root (#1033's clock-as-`S(A)` reading, frozen prereg `:75` on its branch; the archive tag does not exist yet)?
