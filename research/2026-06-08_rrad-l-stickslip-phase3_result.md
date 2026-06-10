# Result — stick-slip / Bingham-yield LATCHING rectification (dark-wake thrust, Phase 3)

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-rrad-l-darkwake` (Phase 3; same branch as Phase 1 + Phase 2)
**Prereg**: [`2026-06-08_rrad-l-stickslip-phase3_prereg.md`](2026-06-08_rrad-l-stickslip-phase3_prereg.md)
**Driver**: [`src/scripts/vol_4_engineering/rrad_l_stickslip_rectification.py`](../src/scripts/vol_4_engineering/rrad_l_stickslip_rectification.py)
**Phase-2 result**: [`2026-06-08_rrad-l-rectification_result.md`](2026-06-08_rrad-l-rectification_result.md) (rectification NOT confirmed — even-in-A kernel)
**Canonical mechanism**: [dark-wake-bemf-foc-synthesis.md §1.2](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md) (Op14/Lenz yield-freeze)

> 🟠 **2026-06-09 REGIME-RESCOPE (Rule 12 — header-only addition; every line of the body below is PRESERVED VERBATIM).**
> **Governing discipline:** `ave-regime-phase-state-check`. **Adjudication:** Grant, 2026-06-09 (regime / phase-state discipline).
>
> **(a) This OUTCOME-B is a SUB-YIELD-LINEAR SHEAR/CHIRAL-ω regime null = a WRONG-REGIME ARTIFACT, not a falsification.** Rate-asymmetry / rectification can live ONLY in the BULK NEAR-YIELD (ruptured) regime. The §1.2 latch acts on the Cosserat-ω (shear/microrotation) sector under a time-symmetric carrier — the sub-yield-linear regime — where the Axiom-4 kernel is instantaneous and even-in-A (achromatic + reversible → ∮ = 0 *by construction*). A null in a regime that forbids the effect is uninformative as a falsification (`ave-regime-phase-state-check`: a null where the effect cannot exist is an artifact, not a falsification).
>
> **(b) The rectification question WAS subsequently closed in the correct (bulk near-yield) regime — by derivation.** Branch `analysis/2026-06-09-thixotropy-bulk-derivation` (2026-06-09, tip `5969bda1`; UNMERGED — cited by branch + date, not a HEAD path), **Outcome B**: the bulk relaxation time τ_bulk(ρ̄) = τ₀/√(1+ρ̄/(1−ρ̄²)) depends on the INSTANTANEOUS ρ̄ ONLY — no sign(dρ̄/dt) memory — so the bulk sat/desat channel has NO rate-asymmetry and cannot rectify a symmetric cyclic drive (dead-by-derivation; clm-7tynm2 walk-back upgrades from empirical → STRUCTURAL for the bulk channel). NOTE the sharper reading this gives Phase 3: the §1.2 latch τ_relax is itself an instantaneous-τ(state) modulation — exactly the non-rectifying case the thixotropy derivation isolates — so the FLAT τ_relax sweep here is the *same* structural fact, not an independent coincidence.
>
> **(c) The in-doc mechanism finding REMAINS CORRECT.** The sector-mismatch + engaged-but-no-rect diagnosis below is still the right EXPLANATION of WHY this regime nulls. The rescope is of the FALSIFICATION-STRENGTH interpretation, **not** the mechanics. The verdict "the canonical §1.2 latch does not rectify HERE" stands; what is rescoped is its reach.
>
> **(d) Read all falsification-strength language in this doc as REGIME-SCOPED per this header** (sub-yield-linear shear/chiral), NOT as a regime-independent falsification of substrate rectification. Specific phrases swept (preserved verbatim in-body): the HEADLINE "**rectification is DEAD regardless of hysteresis**" and "the **strongest possible negative**: it kills the slow-grip/fast-slip latching thrust route"; §6 "The dark-wake-as-thruster premise is now deflated on **three** objects on the same branch". These are now scoped to the sub-yield-linear regime; the in-regime closure is (b).

> **HEADLINE — OUTCOME B (prereg §5B): rectification is DEAD regardless of hysteresis.**
> Adding the canonical rate-dependent yield-freeze LATCHING (§1.2) to the Cosserat-ω
> dynamics does **NOT** revive rectification. At the **canonical** τ_relax = ℓ_node/c
> the symmetric-vs-asymmetric directed-momentum ratio is **1.18** — statistically
> identical to the Phase-2 latch-OFF null (**1.20**) — and it stays **flat at ~1.18
> across a τ_relax sweep ×0.25 → ×4** (no rectifying band exists at ANY τ_relax, so
> this is **not even a rescue-fill C** — there is no value to tune to). This is the
> **strongest possible negative**: it kills the slow-grip/fast-slip latching thrust
> route. The latching mechanism Phase 2 named as "the missing piece" is implemented,
> at canonical parameters, and it does not rectify the measured momentum.

---

## 0. Headline (the prereg §5 verdict)

**B — still NO rectification.** Symmetric control and asymmetric (slow-charge /
fast-quench) drive produce the **same** directed DC momentum even with the canonical
§1.2 stick-slip latch engaged. The Phase-2 single mechanism (even-in-A ⟨A²⟩
degeneracy) is **NOT** lifted by the latch.

Three load-bearing facts establish B (not an inconclusive null):

1. **No contrast at canonical τ_relax.** `J_dir = (T_pp^RH − T_pp^LH)/2`:
   SYM `−4.87e-3`, ASYM `−5.77e-3` → ratio **1.18**. The Phase-2 latch-OFF
   baseline (reproduced this pass) is SYM `−5.04e-3`, ASYM `−6.06e-3` → ratio
   **1.20**. The latch moves the ratio by **<2%** — within noise. (CONFIRMED-A
   would require ratio ≫1 AND `J_dir_SYM ≈ 0`; neither holds.)

2. **No rectifying band at ANY τ_relax (rules out rescue-fill C).** τ_relax sweep
   ×0.25 / ×0.5 / **×1.0 (canonical)** / ×2.0 / ×4.0 → ratio **1.18 / 1.19 / 1.18
   / 1.18 / 1.18**. Flat. There is **no** non-canonical τ_relax that produces
   rectification — so the negative is not "rectifies only when tuned" (C); it is
   "does not rectify, period" (B). The rescue-fill guard (prereg §3) is satisfied
   by absence: there was no value to tune toward.

3. **Latch engagement confirmed → B is 'engaged-but-no-rect', NOT 'never engaged'.**
   At the canonical operating point (amp=1.4) the propagating wake is mostly
   sub-yield, so the latch under-engages (peak wake grip `g_max=0.075`, **no** cell
   reaches g>0.1). Pushed above yield (amp=3.0, `A²_src,max=18.7`) the latch
   **engages substantially** (`g_max=0.490` — the peak wake cell is ~half-frozen) —
   and the directed-momentum ratio is **STILL unchanged**: latch-OFF `1.203` →
   latch-ON `1.225` (Δ < 2%, both n_cyc=6). So the latch is real, it demonstrably
   grips, and gripping does **not** rectify the measured momentum.

**Single mechanism (Rule 7) — why latching cannot rectify here:** the measured
2nd-order momentum is dominated by the **non-chiral common-mode radiation pressure
`ρ⟨u̇²⟩`** (Phase 2 §0), a property of the **translational `u` (P-wave)** field. The
§1.2 latch freezes the **rotational `ω` (Cosserat microrotation)** field (it "blocks
dω/dt"). Freezing ω asymmetrically does break ω-sector time-symmetry, but the
directed momentum the experiment measures lives in the `u̇²` channel, which the
ω-freeze does not redirect. The latch acts on the wrong sector for *this* observable.
(See §4 — this is a SECTOR finding, surfaced for Grant, not a tuning failure.)

**Classification:** Class-B manifestation attempt that produced a **null** — the
engine now implements the §1.2 stated latch, and the stated latch does not produce
the claimed rectification. NOT a Class-2 emergence claim either direction.

---

## 1. What was built (substrate-native-check applied)

The latch is the §1.2 Op14/Lenz **rate-dependent yield-freeze**, implemented as a
per-cell dynamical **grip state `g(r,t) ∈ [0,1]`** on the **Cosserat ω** dynamics —
NOT a phenomenological friction model:

- `g=1` gripped/FROZEN: dω/dt blocked (the diverging-`L_eff` Lenz back-EMF that
  "blocks dω/dt during the τ_relax window", §1.2); the config couples.
- `g=0` slipped: Γ=−1, ω evolves freely (decoupled).

**Rate rule (§1.2, exact):** the freeze requires DWELL near the yield boundary
(S→0, diverging `L_eff`) for ≥ τ_relax — a SLOW crossing of the **saturation
operating point** A₀ through A_yield:

```
A₀  ← (A₀·τ_relax + dt·A)/(τ_relax + dt)          # operating-point lag (doc-59 §9 form)
rate_slow = clip(1 − |dA₀/dt|·τ_relax/A_yield, 0, 1)   # 1 slow → 0 fast
sat       = 1 − S(A₀) = 1 − √(1 − min(A₀², 1))     # Op14 engagement, →1 near S→0
g_eq      = sat · rate_slow
g  ← (g·τ_relax + dt·g_eq)/(τ_relax + dt)          # backward-Euler memory, canonical τ
```

Then dω/dt is blocked by the gripped fraction `g` (the step's Δω is reverted by `g`
and ω_dot is damped by `(1−g)`), in the PML-excluded propagating wake (Rule 10;
source slab excluded so the source can inject).

**ZERO tunable knobs.** Every factor is the engine's own canonical quantity:
τ_relax (one physical relaxation time, used identically for the operating-point lag,
the rate threshold, AND the grip memory), A_yield, the kernel `S=√(1−A²)`, and the
doc-59 §9 backward-Euler form. The τ_relax sweep is a CLASSIFY-only diagnostic.

## 2. τ_relax provenance (DERIVED / canonical — the rescue-fill guard)

τ_relax is a **single canonically-pinned number**, NOT a bound to be tuned:

- **`constants.py:335`**: `TAU_RELAX_NATIVE = 1.0` ("ℓ_node/c = 1 in natural units");
  `TAU_RELAX_SI = L_NODE/C_0 ≈ 1.288e-21 s`. Comment: *"Thixotropic relaxation time
  — minimum state-change time of the K4 lattice. Derived from Ax1 (ℓ_node from K4
  pitch) + Ax3 (propagation at c) in doc 59_ §1 ... Matches Vol 4 Ch 1:214
  (thixotropic hysteresis) exactly."*
- The engine **uses exactly this**: `k4_cosserat_coupling.py:284`
  `self.k4.tau_relax = self.k4.dx/self.k4.c = 1.0` (native); `outer_dt = k4.dt = 1/√2`.
  So τ_relax = 1.0 native = **√2 ≈ 1.41 outer steps**. The ratio `dt/τ_relax = 1/√2`
  is unit-system-invariant (k4_tlm.py:185-189).
- **The §1.2 "≥100 Compton periods" is the residue PERSISTENCE, NOT τ_relax** — a
  separate, longer LOWER bound (claim-quality.md:738). Reduced-Compton time =
  ℏ/(m_e c²) = ℓ_node/c = τ_relax = 1 native; one full Compton period = 2π native, so
  ≥100 periods ≈ 628 native ≈ 888 steps ≫ the sim window (~130 steps). Within the
  run a gripped residue therefore never spontaneously releases — consistent with
  "residues persist", and it makes no difference to the null.

Because τ_relax is pinned and the sweep ×0.25→×4 brackets it widely, there was **no
free τ_relax to tune toward a positive** — the rescue-fill guard (prereg §3) is met
by construction.

`A_yield = 1` — the Cosserat kernel's own zero (`epsilon_yield = 1.0`,
`omega_yield = π`; A² = ε²/ε_y² + κ²/ω_y², S = √(1−A²) → 0 at A=1) — the canonical
Γ=−1 saturation/TIR boundary (Axiom 4). Imported, `verify_constants`-checked.

## 3. NUMERICALLY VERIFIED (smoke; SIGNS / RATIOS / CONTRAST)

Representative run N=24, pml=4, amp=1.4, carrier λ=4, duty=16, charge_frac(ASYM)=0.85,
4-integer-cycle average (robustness checks below).

| | J_dir (directed) | ratio vs SYM | common-mode | grip chg/qnch |
|---|---|---|---|---|
| latch OFF (Phase-2 repro) | SYM `−5.04e-3`, ASYM `−6.06e-3` | **1.20** | SYM `+0.977` | — |
| latch ON @ **canonical** τ | SYM `−4.87e-3`, ASYM `−5.77e-3` | **1.18** | SYM `+0.952` | `0.002 / 0.002` |

Latch-ON common-mode SYM `+0.947` ASYM `+0.953` (unchanged by handedness → non-chiral
radiation pressure, as Phase 2). Latch effect on `T_pp` is small + non-chiral:
ΔT_pp(on−off) ≈ `−0.025` for both SYM and ASYM (a ~2.6% uniform reduction, NOT a
directed contrast).

**τ_relax CLASSIFY sweep (canonical = ×1.0; amp=1.4):**

| τ_relax × | 0.25 | 0.5 | **1.0 (canon)** | 2.0 | 4.0 |
|---|---|---|---|---|---|
| rect ratio | 1.18 | 1.19 | **1.18** | 1.18 | 1.18 |

→ **Flat. No rectifying band at any τ_relax.** Rules out outcome C.

**K4-latch control** (engine's canonical `use_memristive_saturation=True`, Cosserat
latch OFF): ratio **1.20** — identical to the latch-OFF baseline. → the engine's
**own** canonical doc-59 K4-sector latch is **DECOUPLED** from the measured Cosserat
momentum under this driver's `disable_cosserat_lc_force=True` (see §4).

### 3.1 Amplitude robustness (engaged-but-no-rect; n_cyc=6, canonical τ)

| amp | A²_src,max | latch g_max | OFF ratio | ON ratio | Δ |
|---|---|---|---|---|---|
| 1.4 (Phase-2 op-pt) | 4.4 | 0.075 (under-engaged) | 1.20 | 1.18 | −2% |
| 3.0 (pushed >yield) | 18.7 | **0.490 (engaged)** | 1.203 | 1.225 | +2% |

At amp=3.0 the wake is driven well above yield and the latch grips hard
(`g_max=0.49`), yet the SYM-vs-ASYM ratio is **unchanged** (1.203 → 1.225). The latch
engages and does not rectify — the §5 BLOCKED sector finding (FLAG-1), not an
engagement failure.

**Reactance pair (Rule 10), ASYM_LH @ canonical:** C-store `⟨ω²⟩ = 5.79`,
L-store `⟨ω̇²⟩ = 27.7` — both present and non-trivial (an active oscillator, not a
static snapshot). **Local clock (Rule 10):** at the top-A² interior sites
`A²_peak = 1.80` → `ω_local/ω_drive = √(1−A²) = 0` (the load-bearing sites are
saturated/clock-frozen — consistent with the latch engaging there, yet not
rectifying the far-field `u̇²` momentum).

## 4. FLAGS for Grant (flag-don't-fix — surfaced, not silently resolved)

**FLAG-1 (sector mismatch — the mechanism of the null).** The measured 2nd-order
directed momentum is `ρ⟨u̇²⟩`-dominated (the **translational/P-wave `u` sector**,
Phase 2 §0). The §1.2 latch acts on the **rotational/Cosserat `ω` sector** ("blocks
dω/dt"). These are different sectors. Freezing ω asymmetrically does not redirect the
`u̇²` momentum, so no directed DC contrast appears. **The §1.2 latch is real but
orthogonal to the observable.** Whether a *bulk/translational* rectifier could thrust
remains the Phase-2 §6.3 BLOCKED item (needs a compressional drive), now reinforced.

**FLAG-2 (engine's canonical latch is decoupled from the measured object).** The
engine ships a canonical memristive latch (`use_memristive_saturation`, doc-59 §9) —
but it lives in the **K4 photon sector** (S_field on V_inc/V_ref), and under the
driver's `disable_cosserat_lc_force=True` the V→ω coupling force is **zeroed**
(`k4_cosserat_coupling.py:427`). So the engine's own canonical latch cannot reach the
measured Cosserat momentum (confirmed: K4-control ratio identical to baseline). §1.2
is *literally* a Cosserat-ω freeze, so the Cosserat-sector latch built here is the
right home — but it too is orthogonal to the `u̇²` observable (FLAG-1).

**FLAG-3 (§1.2 reading (a) vs (b) — substrate-physics ambiguity).** "V(t) drops
through V_yield at a rate ‖dV/dt‖" admits two readings: **(a)** the instantaneous
field V(t) (carrier-included) — in the ω·τ_relax ≈ 2.2 > 1 regime the carrier always
reads "fast", so the instantaneous-rate grip target stays ≈ 0 (`g_inst ≈ 0`); **(b)**
the saturation OPERATING POINT A₀ (the τ_relax-lagged slow state, INVARIANT-S2). Reading
(b) is used as primary (it is the L_eff-setting state); reading (a) is reported as a
diagnostic. **Both give B.** Surfaced for Grant — not silently resolved.

## 5. DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED (analytic / canonical):**
- τ_relax = ℓ_node/c = 1 native, canonically pinned (constants.py:335; Ax1+Ax3, doc-59 §1).
- The §1.2 latch is a Cosserat-ω freeze; A_yield = 1 (ε_yield); the doc-59 §9
  backward-Euler memory form; zero tunable knobs.
- Sector logic: the measured `ρ⟨u̇²⟩` directed momentum is P-wave/`u`-sector; the
  latch is `ω`-sector → orthogonal (FLAG-1).

**NUMERICALLY VERIFIED (smoke, qualitative):**
- Latch ON @ canonical τ: ratio 1.18 ≈ latch-OFF 1.20 → **no rectification**.
- τ_relax sweep ×0.25→×4: ratio flat ~1.18 → **no rectifying band** (rules out C).
- K4-control: ratio identical to baseline → engine's K4 latch decoupled (FLAG-2).
- Engagement: latch grips hard when driven above yield (amp=3.0: g_max=0.490,
  A²_src=18.7) yet ON ratio 1.225 ≈ OFF 1.203 → engaged-but-no-rect (NOT inconclusive).
- Reactance pair (C-store ⟨ω²⟩, L-store ⟨ω̇²⟩) both nonzero; local clock √(1−A²)=0 at
  the saturated load-bearing sites (Rule 10 diagnostics recorded).

**BLOCKED (unchanged from Phase 2):**
1. Absolute thrust magnitude (converged radiating sim + source-current normalization).
2. The translational/bulk-P-wave "genuine bounce" channel — a *compressional* drive
   (the latch + observable would then co-live in the `u` sector). The natural Phase-4
   if the dark-wake-thrust premise is pursued further.

## 6. Honest closure (Rule 11) + substitution-not-retraction (Rule 12)

The Phase-3 hypothesis — *"the canonical §1.2 rate-dependent yield-freeze latching
revives acoustic rectification (SYM nulls, ASYM → directed DC) where Phase-2's
even-in-A kernel could not"* — is **FALSIFIED** at canonical τ_relax, with a single
explanatory mechanism (the latch is ω-sector; the measured directed momentum is
`u̇²`/`u`-sector — orthogonal). This is the discipline at full strength: a clean
negative, one mechanism named, no rescue-debug. The obvious rescue (sweep τ_relax to
manufacture a positive) was run as a *classifier* and came back **flat** — there is no
value to tune, so even outcome C is excluded. **No new hypothesis refills the slot**
(Rule 12): the named forward path (a compressional/`u`-sector drive so the latch and
the observable co-live) is logged as BLOCKED §5.2, not executed.

The dark-wake-as-thruster premise is now deflated on **three** objects on the same
branch: Phase 1 (linear object: reactance-dominated high-Q), Phase 2 (2nd-order
rectified object: even-in-A kernel, no rectification), and **Phase 3 (the §1.2
latching rescue: no rectification, ω-sector orthogonal to the `u̇²` observable)**.

What SURVIVES (preserve, do not over-retract): the **mechanism diagnosis** sharpens
Phase 2's. Phase 2 said "needs a hysteretic latch." Phase 3 BUILT the canonical
hysteretic latch and shows that is **not sufficient** — the latch must also live in
the **same sector as the thrust observable** (translational/P-wave), which the
canonical chiral-ω source + ρ⟨u̇²⟩ object do not. This is a forward-useful constraint:
a substrate-realizable acoustic-rectification thruster needs **(i)** a hysteretic
latch AND **(ii)** a compressional (`u`-sector) drive so the latch grips the same
momentum the device radiates.

## 7. Result-time skills

- **consistency-vs-emergence → Class-B manifestation that NULLED.** The engine now
  implements the §1.2 stated latch; the stated latch does not produce the claimed
  rectification. Not headlined as emergence; not a Class-2 claim.
- **ave-discrimination-check → no AVE-distinct thrust signal.** The dominant signal
  remains generic `ρ⟨u̇²⟩` radiation pressure (any nonlinear medium). The AVE-distinct
  content (substrate-forced chiral rectified thrust) is NOT demonstrated; adding the
  substrate-forced latch did not change that.
- **ave-driver-script-honesty.** B reported loudly; no rescue-fill toward A; the
  τ_relax sweep is explicitly a classifier, came back flat, and is reported as such.

## 8. Corpus-state deltas to queue (auditor lands; I surface only)

- **`clm-7tynm2` (dark-wake τ_zx thrust object):** the §1.2 rate-dependent
  yield-freeze latching does **NOT** revive 2nd-order rectified-DC thrust in the
  engine. The latch is the right *mechanism* (Cosserat-ω freeze) but the *wrong
  sector* for the `ρ⟨u̇²⟩` (translational/P-wave) directed-momentum observable.
  Phase-1/2 deflation now extends to the latching rescue (Phase 3).
- **FLAG-1 (sector mismatch):** acoustic-rectification thrust needs the latch AND the
  observable in the **same** (compressional/`u`) sector; the canonical chiral-ω source
  is shear-sector. Substrate-physics adjudication for Grant.
- **FLAG-2 (decoupled engine latch):** the engine's canonical `use_memristive_saturation`
  (doc-59 §9) is K4-photon-sector; under `disable_cosserat_lc_force=True` it does not
  reach the measured Cosserat momentum.
- **FLAG-3 (§1.2 reading (a)/(b)):** instantaneous-V vs operating-point-A₀ — both give
  B; surfaced for Grant, not resolved.
- **Driver capability added:** `rrad_l_stickslip_rectification.py` — reusable Cosserat-ω
  stick-slip latch (canonical τ_relax, zero knobs) + τ_relax classify sweep +
  engagement diagnostics + K4-latch decoupling control.
