# RESULT — EMF Lenz-Sign Correction: the K4↔Cosserat path-1 EMF runaway is a sign artifact, not non-conservation

**Date:** 2026-06-21 · **Lane:** implementer · **Branch:** `fix/emf-lenz-sign-correction`
**Scope (Grant ruling a):** fix the sign to `−2`, keep the path off-by-default, scoped-conservative framing.
**Class (consistency-vs-emergence):** **engine-correctness fix** — NOT a new physics claim, NOT an emergence
claim. The corrected sign restores a derivation the engine already had on paper (docstring + doc 67_ §13.6);
no CODATA input, no manifestation/identity/emergence target is asserted. Tag: **consistency** (the
implementation is brought into consistency with its own derivation and conservation requirement).

---

## 0. TL;DR

The EMF assignment in `_compute_emf_per_port` (`src/ave/topological/k4_cosserat_coupling.py`) wired the per-port Lagrangian-EMF
source as `emf = +2.0·V_inc·∂L/∂V_sq`. The method's **own** docstring (the `_compute_emf_per_port` docstring) and doc 67_ §13.6
(`research/_archive/L3_electron_soliton/67_lc_coupling_reciprocity_audit.md:568`) both derive **`−2`**. The
`+2` was a wiring bug. The corrected `−2` is the **Lenz back-EMF** sign: the reaction *opposes* the drive.
With `−2` the documented `E_V → 6.79×10⁸` **detonation of the V-sector energy is eliminated** (bounded, peak
~12, `reverses=True`) — so the runaway is a **confirmed sign artifact, not intrinsic non-conservation.** Scope:
this restores *V-sector-energy* conservation; the full three-part ledger (H-drift + |L|-bound + v-secular)
still does not fully close on the deep seed (the spin |L| transiently spikes), so it is an engine-correctness
fix, not a demonstrated full energize-LOCK.

---

## 1. The `−2` adjudication

### 1.1 Chain-rule derivation (doc 67_ §13.6 : 565–568)

`V_sq = Σ_k V_inc[k]²` is the scalar field the coupling energy `L_c` depends on (via `A²_ε_base`). The JAX
gradient returns `∂L/∂V_sq` directly. The per-port EMF is the negative variation of `L_c` w.r.t. the canonical
port variable `V_inc[k]`:

```
∂L/∂V_inc[k]  = ∂L/∂V_sq · 2·V_inc[k]            (chain rule, V_sq = Σ V_inc²)
EMF_c[k]      = −∂L/∂V_inc[k] = −2·V_inc[k]·∂L/∂V_sq
```

### 1.2 The physical sign (Lenz)

The `−` is the back-EMF: the induced source acts *against* the change that produces it. In Hamilton form
`dΦ/dt = −V + EMF_c`, the reaction-opposes-drive sign is what makes the cross-sector LC exchange conservative
(energy moves between K4 V_inc/Φ_link and Cosserat (u,ω), total bounded) rather than a pump. The prior in-code
rationale ("positive sign produces oscillatory exchange / adds positively to dΦ/dt") had the sign of the
reaction backwards.

---

## 2. Empirical `+2`-vs-`−2` head-to-head (genesis-24 deep-saturated seed)

Driver: `src/scripts/vol_1_foundations/genesis_24_saturated_seed.py` (N=24, 40-step run, 100-step emit window),
`use_lagrangian_emf_coupling=True`, deep frac=0.85/0.95 V-seed. This is the regime where the EMF source is live
(V≠0) and deeply biased — the discriminating scenario.

| sign | E_V peak (emit window) | `reverses` | V-sector energy | full 3-part ledger | smoke `dE_V` (frac 0.85) | verdict |
|---|---|---|---|---|---|---|
| `+2` (bug) | **6.79×10⁸** | **False** (monotone detonation) | runaway | FAILS | `> 0` (leading edge of runaway) | **B** |
| `−2` (Lenz) | **12.08 → unwinds to 5.20** | **True** (bounded) | bounded, `v_secular=0.79` | does NOT fully close | `−0.17 ≤ eps` (source reversed) | **C1** |

Single-arm `−2` trajectory (Arm-1, frac 0.85): `E_V` `12.08 → 5.73` over 40 steps, monotone decay = the seed
unwinds. `max|V_inc|` stays `~0.23` (vs `+2`'s `→ 1.08×10⁴`).

**Conclusion:** the runaway that motivated the "NON-CONSERVATIVE / off-by-default" tag was a `+2` **wiring**
artifact in the V-sector energy, not the physics. With the Lenz-correct `−2`, the deep-seed `V`-sector energy
is **bounded and reverses** — the detonation is eliminated.

**Honest scope (flag-don't-fix / honest-closure).** The `−2` fix removes the *V-sector energy* detonation.
It does **not** by itself close the *full* three-part conservation ledger on that run: the ledger
(`_ledger_closes`, Arm-1 frac 0.95) reports `closes=False` because the spin `|L|` still transiently spikes
(`L_first=2.63 → L_max=42.9 → L_last=11.0`; no longer *pinned* at 43.4 as under `+2`, but the peak still
exceeds the `5×L[0]` bound) and `H_drift=−6.8%` (above the 5% floor). `v_secular=0.79` (sub-unity, good — no
secular V-pump). So the correct claim is **V-sector-energy conservation restored, full energize-LOCK NOT
demonstrated** — a sharper C1, not a positive lock.

---

## 3. Scoping — why the path stays OFF by default (Grant ruling a)

The `−2` is correct AND conservative **on the deep-saturated seed**. It nonetheless remains gated off
(`use_lagrangian_emf_coupling=False`, unchanged), for a **sign-INDEPENDENT** reason: the Op14 varactor
double-count (doc 67_ §14.1–§14.4).

- §14.2–§14.4: the `V²/V_SNAP²` in `A²_ε_base` (the EMF source's V-dependence) is the *same* `V²` that produces
  the K4 self-varactor `C_eff(V)` already implemented via Op14 `z_local` modulation. Adding the EMF source
  re-injects energy Op14 already accounts for ⇒ double-count.
- §14.1: on the **small-amplitude mixed-mode** test (`V_inc_amp = 0.05·V_YIELD`), **both** signs blow up
  (`+2` and `−2` both → `1.20×10¹³` at step 5, ~160× legacy). This is the double-count regime; the sign is
  irrelevant there. (Note: this is a *different* regime from the deep-saturated seed of §2, where `−2` is
  bounded — both findings co-exist.)

So: `−2` is the right sign and is conservative where it is live (deep saturation); the path is parked because
the Op14 redundancy (sign-independent) is unresolved. The **A28** `disable_cosserat_lc_force` channel is a
*separate*, sign-independent `W_refl` double-count and is untouched by this fix.

---

## 4. Impact map (the bottom line — both negatives HOLD)

- **genesis GAP-1 (no ω→V winder primitive): HOLDS — now via a cleaner C1.** Under `−2` the deep-saturation
  gate reads C1 (`dE_V ≤ eps`, source reversed, V-sector bounded). The §8-structural finding **(2,3) does not
  close** is sign-independent and stands. The V-sector detonation is removed, so the C1 is a clean negative
  (the source unwinds rather than detonating), not a detonation artifact — though, per the honest-scope note
  in §2, the full ledger still does not fully close. `research/2026-06-09_genesis-24-saturated-seed_result.md:51`
  updated with a Rule-12 addendum.
- **keystone energize-LOCK: UNAFFECTED.** Its H-pump is the *distinct* curl-coupling in
  `a1_cosserat_moving_wall_engine.py`, which is grep-clean of EMF references
  (per `2026-06-16_keystone-discriminator-spec.md:11`). This fix touches only `_compute_emf_per_port`; the
  keystone negative is independent and unchanged.
- **native_electron_model_v2: aggregate UNCHANGED (`V2_CHANNELS_NO_BREAKTHROUGH`).** The `leak_bemf_emf` arm
  is still outcome E (destabilized), but its destabilization is dominated by the **dark-wake back-EMF**
  channel (`bemf_feedback`), not the Lagrangian EMF — the `bemf_feedback` and `leak_plus_bemf` arms (no
  Lagrangian EMF) are independently destabilized (ω_persist ~1660/1627). The `−2` fix does not rescue this
  arm (ω_persist ~5.3×10¹¹ before and after), and correctly so.
- **genesis-23: verdict UNCHANGED (C).** The §8 emf=True gap-localization diagnostic does not feed the §9
  verdict; only the `gap_localization` sub-dict refreshes (`v_end max|V_inc|` 0.086→0.084, bounded both ways,
  still does not close (2,3)).
- **KB claims affected: NONE.** No `clm-*` claim leaf depends on the EMF sign; the only KB touch is the Vol 9
  Ch 3 datasheet narrative tag (re-scoped, not a claim).

---

## 5. Changes landed (this branch)

| File | Change |
|---|---|
| `src/ave/topological/k4_cosserat_coupling.py:838` | `+2.0 → −2.0`; comment block :830–837 and constructor NOTE :260 re-scoped (A28 reasoning preserved) |
| `src/scripts/vol_1_foundations/genesis_24_saturated_seed.py` | re-run JSON refreshed; stale `:703`→`:838` cite fixed (:158); FIG-4 caption made data-driven (closes vs fails) |
| `src/scripts/vol_1_foundations/_output/native_electron_model_v2_results.json` | re-run refreshed (schema also re-aligned to current `classify()`) |
| `src/scripts/vol_1_foundations/reflection_genesis_23_self_assembly_results.json` | re-run refreshed (§8 gap_localization) |
| `manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex:138` | adjudicated the implemented-vs-derived sign question to `−2`-Lenz-conservative |
| `manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex` | requirement stands; `+2` is the wrong-sign example, `−2` satisfies it on the deep seed but stays gated |
| `manuscript/ave-kb/vol9/ch3-pin-port-configuration/index.md:18` | Rule-12 re-scope of the NON-CONSERVATIVE tag |
| `research/2026-06-09_genesis-24-saturated-seed_result.md:51` | Rule-12 addendum: `−2 ⇒ C1`; missing-winder finding unchanged |

---

## 6. Discipline applied

- **ave-walk-back / Rule 12:** all re-scopes preserve the prior body and add a 🔴 successor header; no silent
  deletion. The +2-era reasoning is preserved as the empirical record under its own header.
- **verify-before-cite:** `:792` docstring, doc 67_ §13.6 `:568`, §14.1–§14.4 all read and quoted from the
  working tree; the stale `:703` cite confirmed stale (line 703 is now an unrelated method body) and corrected
  to `:838`.
- **flag-don't-fix:** surprises surfaced, not silently resolved (see the result report / PR body):
  (i) the constructor NOTE at :258–259 *already* cited `−2` while the code wired `+2` — an internal
  inconsistency; (ii) the committed `native_electron_model_v2_results.json` was generated by a stale `classify()`
  schema; (iii) `native_electron_v2`'s EMF-arm destabilization is dark-wake-BEMF-dominated, so the `−2` fix
  correctly does NOT rescue it.
- **consistency-vs-emergence:** classified as engine-correctness / consistency (above), explicitly NOT an
  emergence claim.
