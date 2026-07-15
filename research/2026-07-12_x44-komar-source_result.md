# RESULT — X44 Komar / redshift-weighted source reconciliation

**Date:** 2026-07-12 · **Lane:** implementer · **Branch:** `analysis/x44-komar-source`
**Status:** engine + gates landed; **frozen bin (iii) UNRECONCILED**. **NOT merged**
(Grant / orchestrator merges via reviewed PR).
**FROZEN prereg:** `research/2026-07-12_x44-komar-source_prereg_FROZEN.md`
(freeze-by-push: prereg `b9f88823` BEFORE engine `4254034e` / this result).
**Class:** consistency / **CERTIFICATION-class reconciliation attempt** of the latent
`#86` M_eff-vs-far-field gap. **No chord.** α-CLEAN (gravity sector).

---

## 0 · One-paragraph summary

Grant RULED (c) 2026-07-12 authorized replacing the Picard source
`T₀₀^src = T₀₀^matter + u_field` with the redshift / Komar weight
`T₀₀^src = T₀₀^matter · √S(A)` (no separately-added `u_field`), expecting the
far-field Gauss flux to reconcile with the engine's own-labeled ADM mass
`M_eff = M − U_bind`. The weight is installed as the **default**
(`source_mode="komar"`); legacy ADD is retained behind `source_mode="add_field"`
(KEEP-BOTH). **Verdict: frozen bin (iii) UNRECONCILED.** Across the `#651`
fixed-rest-energy family, `η_mixed = slope(m_g/M_eff − 1 vs f)` is
**+1.048 (N=24), +1.049 (N=32), +1.050 (N=40)** — O(1), stable under resolution,
far above the reconcile tol `|η| < 1×10⁻³`. The fireable identity
`Δ_clock = ∫ T₀₀(1−√S)` vs `U_bind = ∫ ½g|∇ε₁₁|²` also FAILS MATCH
(relative mismatch ~93–97%; `Δ_clock/U_bind ~ 0.03–0.07`). Gauss flux ≡ ∫T₀₀^src
holds (install-tautology). No √S → S / 1/S retune was performed (prereg out-of-scope).
Escalation to Grant: the ruled Picard weight and the strain-energy ADM label are
**different functionals**; installing √S alone does not close the `#86` gap.

---

## 1 · STEP-0 (from frozen prereg; not re-litigated)

Authorized-open after `#651`. Current ADD source read M+U; designated ADM is M−U;
mixed η≈2.28 exposed the latent defect. RULED (c) = Komar √S weight as Picard
source. Diamond-K4 Grad/Div inherited from `#86` (D1 non-canonical; flag only).

## 2 · Substrate-native (walked; unchanged from prereg)

- **K4:** same `_build_native_grad_div` as `#86` / `#651`. Gauss residual on
  enclosed flux vs ∫T₀₀^src remains < 1×10⁻⁴ (measured ~10⁻⁶–10⁻⁷).
- **Sector:** A1 dilatation / gravity. Mass = A1 untouched.
- **Op14:** `S(A)=(1−A²)^{1/2}`, weight `√S` as ruled. No new kernel.
- **A46/A47:** real-space; certification / consistency. α-CLEAN.

## 3 · What shipped

| piece | change |
|---|---|
| `backreaction.komar_weight` / `build_picard_source` | √S weight; modes `komar` (default), `add_field`, `matter` (diagnostic bare control) |
| `solve_backreaction` | default `source_mode="komar"`; returns `Delta_clock` |
| `#86` suite | g_self=0 Stage-1 recovery pinned to `add_field`; check4 mode-aware |
| Nordtvedt LEG-1 | live gate = flux vs `M_eff`; records frozen bin (iii) |
| P11 | teeth = relative Δη recovery (baseline may be O(1)) |
| Legacy ADD mixed | KEEP-BOTH: η_mixed ≫ 1 still fires under `add_field` |

## 4 · LEG-1 / η_mixed family (N=24 live gate)

| σ | f | m_g | M_eff | (m_g−M_eff)/M_eff | Δ_clock/U | max A |
|---|---|---|---|---|---|---|
| 1.40 | 0.0561 | 3.98386 | 3.76225 | +5.89×10⁻² | 0.068 | 0.188 |
| 1.80 | 0.0397 | 3.99234 | 3.83443 | +4.12×10⁻² | 0.046 | 0.131 |
| 2.20 | 0.0300 | 3.99574 | 3.87645 | +3.08×10⁻² | 0.034 | 0.099 |
| 2.60 | 0.0234 | 3.99721 | 3.90423 | +2.38×10⁻² | 0.027 | 0.079 |

- **η_mixed(N=24) = +1.048** ≥ 1×10⁻³ ⇒ **bin (iii) UNRECONCILED**.
- Δ_clock↔U_bind: max relative mismatch **0.973** (≥ 0.30) — MATCH fails.
- Converged, max A < 0.2, Gauss identity PASS, monopole plateau PASS.
- Picard contractive (bin iv does not fire).

### 4a · η_mixed-vs-N receipt (prereg gate #3)

| N | η_mixed | notes |
|---|---|---|
| 24 | +1.0479 | live gate |
| 32 | +1.0489 | |
| 40 | +1.0502 | |

**Not resolution-limited.** The O(1) slope is stable to ~0.2% across N∈{24,32,40}.
Banking basis for unreconciliation = the measured slope + the analytic mismatch
of functionals (§5), not an N=24 accident.

### 4b · Fireability disclosure — which bins were structurally reachable (R1)

Honest reach-of-the-test statement (added post-review). In the **frozen family**
(`g_self=1.0`, `max A < 0.2`) only bins **(iii)/(partial)** were structurally
reachable: `Δ_clock/U_bind ≈ ⟨ε⟩/2 ≤ ~0.07` in-band (measured **0.03–0.07**, the
§4 table), so RECONCILE (`|η_mixed| < 1×10⁻³`) required `Δ_clock/U ~ 1` ⇒ `f ~ 0.6`,
**~10× outside the frozen regime**. `Δ_clock/U` is `g_self`-tunable and was
**correctly NOT tuned** (prereg forbid; a retune to force `U_bind ≈ Δ_clock` would
manufacture η→0). Bin (iii) therefore banks as **"the ruling's density-only
implementation tested in a regime that could only fail to reconcile"** — NOT
"reconciliation given a fair shot and lost." The genuinely-fireable completion (a
regime where reconcile is reachable) is the escalation §7 option 5 (X44b).

## 5 · Why √S did not close the gap (honest mechanism)

Under Komar:

```
m_g  = ∫ T₀₀^src = ∫ T₀₀^matter √S = M − Δ_clock ,   Δ_clock = ∫ T₀₀(1−√S)
M_eff = M − U_bind ,   U_bind = ∫ ½ g_self |∇ε₁₁|²
```

Weak-field: `√S ≈ 1 − A²/4` ⇒ `Δ_clock ∼ ∫ T₀₀ A²/4`, while `U_bind ∼ ∫ ½|∇ε|²`.
These are **different functionals** (prereg § analytic expectation #3, pre-declared
fireable). Measured `Δ_clock / U_bind ~ 0.03–0.07` in this band ⇒ flux sits near M
while `M_eff` deficits by a much larger U_bind ⇒ `m_g/M_eff − 1 ∼ O(f)` with
slope η_mixed ∼ +1.

**Additional structural fact (surfaced, not retuned):** under `source_mode="komar"`,
`g_self` does **not** enter the Picard source (only the U_bind / M_eff *ledger*).
The historical check4 g_self-ON/OFF discriminator is therefore vacuous under Komar
(engage_ratio ≡ 1 when comparing g_self). Legacy ADD still engages at **2.38×**
(KEEP-BOTH). A `matter` control mode isolates √S-vs-bare for future work.

**Not done (prereg forbid):** silent swap √S→S or 1/S; retuning `g_self` so
`U_bind ≈ Δ_clock` to force η→0.

### 5b · The virial/Tolman structure + the wrong-register clock (review-verified closure chain, R2)

Post-review, the mechanism resolves to a four-step closure chain — WHY the
density-only √S implementation could not reconcile, and what a faithful test needs:

> 🔴 **FALSIFYING-EVIDENCE HEADER — bullet (i) is the FALSIFIED SIDE (2026-07-14; Rule-12 — the bullet body below is PRESERVED VERBATIM, git is the trail).**
> Grant **Ruling 1 (F6, in-chat 2026-07-14; ruling record: PR #695 docket continuation)** adjudicated the F6 fork in favour of
> **√S slope-1 IS the Komar / local-clock weight** — the W2 walk-back and the RULED-(c) `komar_weight` **prevail**, and **this
> bullet (i)'s "wrong strain-register" diagnosis is the falsified side.** Bullet (i) argues the shipped `√S` weight is the *EM*
> operating-point register and that the *gravitational* clock register is instead the LINEAR `n = 1 + (2/7)ε`. That inverts the
> canonical clock-vs-propagation split: the **local clock rate / gravitational redshift IS the slope-1 `√S`**
> (`../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`:28, the **W2 walk-back**:
> "the genuine local clock rate / gravitational redshift is a slope-1 quantity: √g₀₀ = √S"; :26, W1, fixes `1 + (2/7)ε` as the
> *transverse deflection / propagation* index), and `n = 1 + (2/7)ε` is the **slope-2 bulk/coordinate-time propagation
> (Shapiro / deflection) index — NOT the redshift clock**. The live engine agrees: `src/ave/gravity/backreaction.py:235-252`
> `komar_weight` returns `√S` with docstring *"Redshift / Komar weight √S(A) on the local clock (Grant RULED (c), X44)"*, and the
> `n = 1 + (2/7)ε` the bullet points at (`backreaction.py:647-651`) is the ray-trace **EMERGENT optical / refractive-index**
> (Op19, EM-channel deflection), by that function's own docstring. So the reconciliation MISS banked in §4/§7 stands as an
> empirical result, but its **mechanistic attribution to a "√S register-mismatch" — bullet (i), and the X44b premise in §7·5 that
> rests on it — is RETRACTED per Ruling 1**: the `√S` weight is the *correct* clock register, not a mismatched one. Body preserved
> per Rule-12; see the §7 option-5(a) correction note.

- **(i) The shipped weight is in the WRONG strain-register (quadratic, not linear).**
  The shipped `komar_weight = (1−A²)^{1/4} ≈ 1 − A²/4` is **QUADRATIC in strain** —
  it is the **EM kernel operating-point factor** `√S` (Op14, exponent 0.5). This is
  the ch17 `n_eff`-overload flag **materializing**: the promoted item (13a) "the KB
  symbol `n_eff` is OVERLOADED (√S EM vs 1/√S gravitational)"
  (`manuscript/ave-kb/vol9/ch17-engine-requirements/index.md:32`) warned exactly this
  — `√S` is the **EM-transverse** register. The engine's own **GRAVITATIONAL**
  register is **LINEAR in ε**: the check-3 ray-trace optical metric
  `n(r) = 1 + ν_vac·ε₁₁`, `ν_vac = 2/7`
  (`src/ave/gravity/backreaction.py:647-651`), whose deflection recovers
  `δ = (4/7)·K/b = 4GM_eff/(bc²)` — the GR-doubled 4GM (`:716-717`). Weighting the
  source by the EM operating-point `√S` (a quadratic ε² deficit) instead of the
  gravitational linear-ε clock is a **register mismatch**, not a magnitude tune.

- **(ii) With a LINEAR clock the deficit OVERSHOOTS the other way (η ≈ −1).**
  For a linear-in-ε clock weight the source deficit tracks the potential energy:
  `∫ρφ = 2W = −2U` (virial), so the far-field flux under-reads by `2U` where the
  M_eff ledger deficits by only `U` ⇒ `η ≈ −1`. The quadratic √S under-reads by
  `Δ_clock ≪ U` (η ≈ +1, this arc); a linear clock over-reads (η ≈ −1). **Neither
  bare weight lands at 0** — the reconcile sits between them.

- **(iii) The virial/Tolman STRESS term is what closes it (η → 0).** The Tolman/
  Komar mass for a **static, force-balanced** source carries a `+3∫p` pressure/stress
  term; with `+3∫p = +U` (virial for a bound static configuration) the ledger closes
  to `M − U` (η = 0). This is valid **ONLY for static force-balanced (virialized)
  configurations**. The as-built engine has **NO stress/pressure register** —
  `gaussian_blob` is a **bare prescribed scalar** `T₀₀^matter` with no `T_{ij}`
  companion — and the blob family is **NOT force-balanced** (a prescribed profile,
  not a self-consistent hydrostatic solution). So the term that would close the
  ledger is **structurally absent from the engine**, independent of the weight form.

- **(iv) Attribution receipt (review finding 8; independently re-measured this
  session).** Decomposing the `η_mixed(flux/M_eff)` drop `ADD → komar` via a bare
  `matter`-mode control (delete the `u_field` ADD, no √S): `ADD = +2.2792`,
  `matter = +1.1585`, `komar = +1.0479`. Of the total drop `1.2313`: **91.0%**
  (`1.1208`) was the **deletion of the `u_field` ADD** (`ADD → matter`), and the
  **√S weight itself contributed only `−0.11` (9.0%)** (`matter → komar`). ⚠
  **Flag (verify-before-cite):** the review's finding-8 stated `~96%` for the ADD
  deletion; direct 3-mode measurement gives **91%** (the `√S ≈ −0.1` contribution
  matches). The headline is unchanged either way: **√S did almost no work — the
  reconciliation was ~9/10ths just removing the double-counted `+u_field`**, which
  the one-ledger `#651` entailment already banked. The ruled `√S` form is a
  register-mismatched near-no-op on top of that.

## 6 · `#86` at-risk suite under default komar

| check | result under komar |
|---|---|
| α-clean | PASS |
| field energy / binding deficit definition | PASS |
| g_self=0 → Stage-1 | PASS (pinned to `add_field`) |
| komar default + Δ_clock ≥ 0 | PASS |
| weak converge / bind | PASS |
| recover-GR weak | PASS — **but was VACUOUS as first shipped** (komar-vs-komar, `shape_dev ≡ 0.0`); **REPAIRED R3** → komar-two-way-vs-Stage-1, real `shape_dev = 6.08×10⁻⁴` + perturb receipt (see §9) |
| 1/r monopole | PASS |
| S_min-independent M_eff | PASS |
| ray-trace 4GM | PASS |
| two-mass nonlinearity | mode-aware: ADD KEEP-BOTH PASS (2.38× g_self on/off); Komar komar-vs-matter PASS (2.24× — √S feedback engages) |
| boundedness / energy stationary | PASS |

## 7 · KEEP-BOTH / escalation

- **ADD convention** remains callable; mixed-register η_mixed ≫ 1 still exposes the
  pre-X44 gap under `add_field`.
- **Komar is installed as default** per RULED (c), even though reconciliation
  missed — the ruling was about the source *form*, and the fireable identity was
  pre-declared as a real risk. Bin (iii) means: do **not** claim the `#86` defect
  is closed; escalate options to Grant:
  1. redefine ADM label to `M − Δ_clock` (clock-native inertial mass);
  2. keep ADD for flux / Komar for clock diagnostics (split registers explicitly);
  3. charter a different weight only after a new ruled form (not silent retune);
  4. accept unreconciliation and fence M_eff as a strain-energy diagnostic only.
  5. **★X44b — the FAITHFUL test of RULED (c) (recommended).** The three
     ingredients §5b names as absent/mismatched, built as their own disciplined arc:
     (a) a **linear-in-ε clock weight** — the engine's OWN gravitational redshift
     register (`n = 1 + (2/7)ε`, `backreaction.py:647-651`), NOT the EM operating-
     point `√S`; (b) a **stress/pressure register** `T_{ij}` (a new engine
     capability, own prereg + discipline — the `+3∫p` Tolman term); (c) a
     **FORCE-BALANCED (virialized) test family** (a self-consistent hydrostatic
     source, not a prescribed `gaussian_blob`). **Expectation ladder (each rung
     genuinely fireable):** linear clock alone → `η ≈ −1` (overshoot); linear clock
     + virialized stress → `η → 0` (reconcile). Unlike this arc, reconcile is
     **structurally reachable**, so a miss would be a real falsification of (c) — not
     a regime artifact (§4b).

> 🔴 **CORRECTION NOTE — option 5(a)'s label is the upstream mislabel, FALSIFIED (2026-07-14; Grant Ruling 1, F6; body above preserved per Rule-12; ruling record: PR #695 docket continuation).**
> Option 5(a) proposes "a **linear-in-ε clock weight** — the engine's OWN gravitational redshift register (`n = 1 + (2/7)ε`), NOT
> the EM operating-point `√S`." Per **Ruling 1**, that attribution is **inverted**: `n = 1 + (2/7)ε` is the **slope-2**
> bulk/coordinate-time propagation (Shapiro / deflection) index — the ray-trace optical / refractive index (`backreaction.py:647-651`
> docstring "EMERGENT optical metric"; `../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`:18,24,28) —
> **NOT** the gravitational redshift register. The redshift / local clock IS the **slope-1 `√S`** (W2 walk-back, :28), which is
> exactly what the RULED-(c) `komar_weight` (`backreaction.py:235-252`) already installs. So the X44b "linear-clock" expectation
> ladder rests on a **falsified premise** (`√S` is the *correct* clock register, not a register-mismatch); options 1-4 and the
> empirical reconciliation MISS are untouched. Only the "`√S` is the wrong register / `n=1+(2/7)ε` is the redshift register"
> attribution is corrected.

**Framing (R2):** the **(c) READING stands untested** — X44 tested a density-only
`√S` implementation in a regime that could only fail to reconcile (§4b), and the
`√S` weight did ~1/10th of the work (§5b·iv). Options 1–4 remain on the table;
**option 5 (X44b) is the completion path** — the first genuinely-fireable test of
whether the ruled Komar/redshift source closes the `#86` gap.

U6 / A7 freezes untouched (auditor/Grant-gated from `#651`).

## 8 · Deliverables checklist

- [x] FROZEN prereg pushed first (`b9f88823`)
- [x] Engine Komar default + `source_mode` kwarg
- [x] `#86` re-green (mode-aware check4) + Nordtvedt bin-(iii) recorder + η_mixed-vs-N
- [x] This result doc
- [x] Docket continuation row
- [x] **R3** — recover-GR gate un-vacuated (§9); **R4** — ADD-side one-ledger
      diagnostic shipped (§9); **R1/R2/R5** — fireability (§4b), closure chain +
      X44b (§5b/§7·5), docket (c)-stands
- [ ] PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` — no self-merge

---

## 9 · Repair addendum (post-review, 2026-07-12)

Adversarial review returned 9 confirmed findings, all MINOR/NONE (the arc was
honest); the composite repairs R1–R5 are landed here + in code. FROZEN prereg
byte-untouched.

- **R1 (§4b):** fireability disclosure — only bins (iii)/(partial) were structurally
  reachable in the frozen family; reconcile needed `f ~ 0.6` (~10× out-of-band);
  `Δ_clock/U` correctly NOT tuned.
- **R2 (§5b + §7·5):** the review-verified closure chain — (i) shipped `√S` is the
  QUADRATIC EM operating-point register (ch17 (13a) overload flag materialized), the
  gravitational register is LINEAR-in-ε (`n=1+(2/7)ε`, 4GM); (ii) linear clock →
  `η≈−1`; (iii) the `+3∫p` virial/Tolman stress term closes it (η→0) but is
  structurally absent (no stress register, blob not force-balanced); (iv) attribution
  receipt — 91% of the drop = deleting the `u_field` ADD, √S itself = −0.11. Plus
  **★X44b** escalation option 5 = the faithful, genuinely-fireable test of (c).
- **R3 (code, gate-repair):** `recover_gr_weak_field` compared komar-vs-komar
  (`shape_dev ≡ 0.0` — g_self is ledger-only under komar, so both legs solved the
  identical elliptic; the gate could not fire). Pinned OFF = Stage-1 one-way
  (`add_field`, g_self=0.0), ON = shipped komar default. **Real `shape_deviation =
  6.078×10⁻⁴`** (0.06%, passes ≤10%). **Perturb receipt:** vacuous (self/old) = 0.0;
  repaired (komar-vs-Stage-1) = 6.08×10⁻⁴; perturb (ADD self-energy vs Stage-1) =
  1.63×10⁻² (**26.8× — the gate has teeth**). Test-semantics fix of a gate-only
  engine-file function (grep-confirmed no engine caller); NO physics-logic change.
- **R4 (code):** shipped the missing frozen ADD-side ONE-LEDGER diagnostic (prereg
  gate #2 KEEP-BOTH). Under `add_field`, flux ≡ ∫T₀₀^src = M+U (Gauss), so flux-vs-
  `m_i=M+U` certifies **η_one = +8.28×10⁻⁵** (< 10⁻³) — the `#651` η≈0 certification's
  regression coverage. KEEP-BOTH with the mixed exposure (η = +2.2792, reproduces
  `#651`) off one shared solve.
- **R5 (docket):** restored the Gauss install-tautology caveat + added the "(c)
  ratification of the source FORM stands; banked negative = the reconciliation
  expectation of THIS density-only implementation; faithful test = X44b" clause;
  coordinated with the `#661` merge-resolution X-LEDGER row (drop the duplicate).

Gates after repair: `#86` suite 16 passed (both tiers); nordtvedt 5 passed.
