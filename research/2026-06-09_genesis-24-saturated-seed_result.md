# RESULT — Genesis-24: Photon Absorption by a Pre-Saturated Seed (the "saturated-seed" reframe of GAP-1)

**Date:** 2026-06-09 · **Lane:** implementer · **Branch:** `analysis/2026-06-09-genesis-24-saturated-seed` (worktree `AVE-Core-genesis24-wt`)
**Prereg (FROZEN — GO, Lane 1):** [`research/2026-06-09_genesis-24-saturated-seed_prereg.md`](2026-06-09_genesis-24-saturated-seed_prereg.md)
**Lineage:** direct successor to genesis-23 ([`research/2026-06-09_reflection-genesis-23-self-assembly_result.md`](2026-06-09_reflection-genesis-23-self-assembly_result.md), GAP-1 = no ω→V source; GAP-2 = no stable confining window for a free photon).
**Driver (reuses ALL genesis-23 machinery — no new physics):** [`src/scripts/vol_1_foundations/genesis_24_saturated_seed.py`](../src/scripts/vol_1_foundations/genesis_24_saturated_seed.py) · **JSON:** `…_results.json` (N=24, 40 steps, emit-window 100 steps)
**Engine:** `ave.topological.vacuum_engine.VacuumEngine3D` (COUPLED K4⊗Cosserat) — `use_impedance_boundary` + `couple_v_sector` + **`use_lagrangian_emf_coupling=True`** (the ω→V EMF reciprocal `k4_cosserat_coupling.py:703`, dead at V=0 / live at V≠0) + `use_asymmetric_saturation=True` (default; κ_chiral·h photon-ω is the wall, the V-seed biases the EMF source).
**CANONICAL-AVE-ONLY:** absorb/emit IS the Axiom-4 saturation engage/relax cycle on the bond LC tank; the "3" is the real Heaviside/Gibbs-excised longitudinal V-sector. Zero QED framing anywhere.

---

## 🔴 CORRECTING HEADER (2026-06-09, post-run demotion — Rule 12 / ave-walk-back; body preserved unchanged below)

**Two over-claims in the body below are DEMOTED. The original reasoning is preserved verbatim (Rule 12);
where it conflicts with this header, this header governs.** A deterministic re-run of the driver added the
decisive Arm-2 toroidal control (`arm12_toroidal` / `task1_toroidal_resolution` in the JSON) and the |L|
range in the ledger. Both demotions are now backed by serialized JSON, not asserted.

**(1) §0 "FORWARD STEP / one new step past genesis-23" + §9 row "Photon energizes V beyond control —
VERIFIED" → DEMOTED to: the photon triggers a seed-biased, NON-CONSERVATIVE SECULAR PUMP — not an
absorption step.** The live channel is the path-1 EMF reciprocal (`k4_cosserat_coupling.py:703`,
`_compute_emf_per_port`, `emf = +2·V_inc·∂L/∂V_sq`, enabled by `use_lagrangian_emf_coupling=True`), whose
own docstring at **`k4_cosserat_coupling.py:242`** states *"this AMPLIFIES the runaway; path-1 was the wrong
direction."* The ledger FAILS (Arm-1 @ frac 0.95, 40-step window: `H_drift = −6.3 %`; `|L|` **UNBOUNDED
2.7 → 43.4**, ~16×, `ledger.L_bounded = False`) and the 100-step emit window **DETONATES** (`E_V → 6.8×10⁸`
monotone to the last step, `max|V_inc| → 1.08×10⁴`, `reverses = False`). **`dE_V` is the leading edge of
that runaway — NOT a demonstrated energize-LOCK absorption** (`ave-conserved-vs-pumped`). The raw delta is
real; its reading *as a forward absorption step* is withdrawn — the photon tips the EMF amplifier from decay
into runaway, it does not lock energy into a bound absorber.

**(2) §3 "the toroidal '2' genuinely enters phase-space / sharper than genesis-23" → RETRACTED (sub-gate).**
The Arm-2 (no-photon) toroidal control — `vinc_w_tor` AND `vinc_rel_tor` for BOTH arms, all fracs, t=0 and
peak, serialized for the first time — returns **Case C (sub-gate)**: toroidal winding reliability
`rel_tor = 0.000` for BOTH Arm-1 and Arm-2 at EVERY frac, two orders below the `> 0.1` closure gate. Arm-1's
`w_tor = 1/2/2/1` is **non-monotone, collapses at the deepest frac 0.95, and rides a zero-reliability
contour — it is meaningless noise, not a populated winding.** So the toroidal half is NOT "sharper than
genesis-23": genesis-23's V-sector was *empty* (`amp = 0`); genesis-24's is *populated but
winding-unreliable* (`amp > 0`, `rel_tor = 0`) — a different distinction than "no 2" vs "real 2." The
de-novo toroidal "2" is **UNVERIFIED** — neither photon-driven (Case A needs Arm-1 `rel_tor > 0.1` — FAILS)
nor a clean seed artifact (Case B needs Arm-2 to reach a reliable `w_tor ≈ 2` — Arm-2 is `0`). See the
Arm-1-vs-Arm-2 table added to §3.

**SOURCE-COUNT VERDICT (the deliverable):** **NOT RESOLVED — Case C.** The toroidal channel is sub-gate, so
the run establishes neither "one source (poloidal q=3 only, because the photon supplies the 2)" nor "two
sources (a toroidal-2 AND a poloidal-3 source)." Crucially it **removes the positive evidence for the
one-source reading** — the toroidal "2" is not demonstrated to arise dynamically, so it cannot be counted as
handled. The only robust topological result stands: **(2,3) does not close; the residual gap is the winder
primitive** (the poloidal q=3 fibre is unpopulated AND the toroidal "2" is sub-gate noise — the §3
"only-the-poloidal-fibre-is-missing" asymmetry is itself withdrawn).

**What SURVIVES intact (NOT demoted):** `dE_V > 0` real, deep, monotone (decisively **not C1**) · seed-audit
clean, charge-neutral, no forbidden seeder (**not C2 / not laundered**) · charge = photon helicity,
Arm-4 `−h` flips H_bel sign at every frac (provenance, not emergent (2,3) charge) · (2,3) does not close,
gap localized to the winder primitive.

**verify-before-cite:** the *"this AMPLIFIES the runaway"* quote is at `:242` (the
`use_lagrangian_emf_coupling` NOTE), not `:703`; `:703` is where that same path-1 EMF is computed. Both are
cited accurately above and match the body's own §7 (`:242`) usage.

---

## 🔴 ADDENDUM (2026-06-21, Rule 12 — EMF Lenz-sign correction; the CORRECTING HEADER above is the preserved record, this is the adjudicated successor)

The CORRECTING HEADER's diagnosis of a *"non-conservative secular pump"* / *detonation* rested on the path-1
EMF being wired `emf = +2·V_inc·∂L/∂V_sq`. That `+2` was a **sign-wiring bug**: the method's own docstring
and doc 67_ §13.6 both derive **`−2`** (the Lenz back-EMF — the reaction opposes the drive). The fix is at
`src/ave/topological/k4_cosserat_coupling.py:838` (note `:703` in the header above is now stale; the EMF
source moved to `:838` as the file grew). Empirical head-to-head on this same deep-saturated genesis-24 seed:

| sign | E_V peak (emit window) | reverses | V-sector | full ledger |
|---|---|---|---|---|
| `+2` (bug) | `6.79×10⁸` | `False` (detonation) | runaway | FAILS |
| `−2` (Lenz) | `~12` → unwinds to `~5` | `True` (bounded) | bounded, `v_secular<1` | does NOT fully close (`\|L\|` spikes to ~43 then relaxes; H-drift ~−7%) |

So **the V-sector runaway is a CONFIRMED SIGN ARTIFACT, not intrinsic non-conservation.** (Scope: the `−2`
fixes the V-sector-energy detonation; it does not by itself close the full three-part conservation ledger —
`|L|` still transiently spikes before relaxing, H drifts ~−7%. This is a V-sector-energy correction, not a
demonstrated full energize-LOCK.) Under the corrected `−2`,
the smoke `dE_V` at frac 0.85 is **negative** (`E_V(Arm-1)=5.73 < E_V(Arm-2)=5.90 ⇒ dE_V=−0.17 ≤ eps_machine`),
so the deep-saturation gate reads **verdict C1** (`dE_V ≤ eps`), not the body's verdict B. The :51 line above
("`dE_V > 0` … decisively **not C1**") is therefore superseded: under `−2` the source is reversed and the
test reads **C1**.

**What is UNCHANGED:** the §8-structural finding — **(2,3) does not close; the residual gap is the winder
primitive** — is sign-independent and **stands**. The corrected `−2` makes the C1 cleaner (a bounded,
conservative source that nonetheless does not wind the topology), it does not revive an absorption-LOCK
reading. The genesis GAP-1 (no ω→V winder) holds, now via a cleaner conservative C1 rather than a runaway.
The path stays `use_lagrangian_emf_coupling=False` by default for the sign-INDEPENDENT Op14 varactor
double-count (doc 67_ §14.1–§14.4, where both signs diverge on small-amplitude mixed-mode).

Full capture: [`research/2026-06-21_emf-lenz-sign-correction_result.md`](2026-06-21_emf-lenz-sign-correction_result.md).

---

## §0 — VERDICT: **B** — source channel FIRES, topology does NOT wind. Two gaps localized; one *new step past genesis-23*.

> 🔴 **See CORRECTING HEADER above** — the "FORWARD STEP / one new step past genesis-23" framing in this §0
> is demoted: `dE_V>0` is the leading edge of a seed-biased secular pump (ledger fails, emission detonates),
> not a demonstrated energize-LOCK absorption. The §0 reasoning is preserved below as written.

> **The saturated-seed reframe is PARTIALLY VINDICATED at the source level and DECISIVELY FALSIFIED at the
> topology level — and the run localizes the residual obstruction to two precise, independent mechanisms.**
>
> **FORWARD STEP vs genesis-23 (the deliverable result).** genesis-23: a lone transverse photon **never
> energizes the K4 V-sector** — `max|V_inc| = 0` to machine precision, every config (GAP-1, the dead
> ω→V source channel). genesis-24: with a **non-circular V-populated seed** present, the photon now adds a
> **photon-attributable, monotone-in-seed-depth** V-sector energization: `dE_V = E_V(photon) − E_V(control)`
> = **+0.011 / +0.083 / +0.367 / +0.781** at frac = 0.30 / 0.60 / 0.85 / 0.95 (monotone ↑, both deep fracs
> > eps_machine). The **no-seed + photon control (Arm-3) reproduces genesis-23 exactly** (`E_V = 0`,
> `max|V_inc| = 0`). **So the V-seed converts the dead ω→V channel into a live one** — "missing IC, not
> missing axiom" holds *at the source level*. The live channel is the EMF reciprocal `:703`, biased by the
> standing V_inc exactly as the chain predicts (`emf = +2·V_inc·∂L/∂V_sq`).
>
> **TOPOLOGY DOES NOT CLOSE (the falsified half — the winder gap).** The de-novo (V_inc,V_ref) phase-space
> winding reaches the **toroidal "2"** (`w_tor → 2.0` at frac 0.60/0.85) but the **poloidal "3" never
> enters phase-space**: `w_pol = 0` at every frac, with poloidal-contour reliability `rel_pol ≈ 0.002–0.005`
> (the poloidal contour is essentially **unpopulated**). `closes(2,3) = False` at every frac, t=0 **and**
> peak. The missing primitive is the **poloidal (q=3) winder**, robustly — see §3, §8.
>
> **NO migration to the Γ=−1 rim (the Smith-chart half).** The operating point stays **near the matched
> center** (|Γ| < 0.08, all arms): seed+photon starts at Γ_min ≈ −0.02…−0.08, the photon drives it **toward
> Γ=0** (−0.009), the control relaxes fully to Γ=0. The electron's Γ=−1 short **never forms** — §4. This is
> the genesis-23 **GAP-2** (under-engaged soft wall) reproduced coupled-with-seed.
>
> **flag-don't-fix — the source channel is a PUMP, not a LOCK (load-bearing 2nd gap).** The `dE_V>0` rides
> on the EMF `:703` reciprocal, which is **non-conservative**: over a 40-step window the ledger already
> fails (`H_drift = −6.3 %`, `|L|` unbounded), and over a 100-step emit window the channel **detonates**
> (`E_V: 7 → 6.8×10⁸`, `max|V_inc| → 1.1×10⁴`). **Emission does NOT reverse** — the channel runs away
> instead of relaxing. So the source-reversal is real but is the **early phase of a secular pump**, not a
> demonstrated energize-LOCK absorption. Surfaced, not smoothed (§7).

**Why B and not A / C1 / C2 (no dropped criteria, Rule 11):** **not A** — (2,3) does not close, ledger does
not close, emission does not reverse, no Γ=−1 migration. **not C1** — `dE_V > eps_machine` decisively, deep.
**not C2** — the seed-audit is clean (no t=0 winding), no forbidden seeder, Arm-2 is null in topology (no
laundering). The pre-registered booleans return **B**; the secular-pump instability is reported as a
distinct *qualifying* finding (it fails the A-criteria, it does not manufacture circularity).

**consistency-vs-emergence (prereg §9):** the `dE_V>0` source-reversal is **consistency-class** — the
V-population is a SUPPLIED IC and the EMF channel manifesting at V≠0 is axiom-structure, NOT emergence.
Emergence was scoped ONLY to de-novo (2,3) winding + photon-traced charge; **neither closes**, so **no
emergence-class claim is made**. The Arm-4 charge flip is the **photon's own helicity** (supplied), not an
emergent (2,3) charge (§6).

---

## §1 — Seed-audit certificate (CP8 seed-not-plant) — the non-circularity guard, PASSED

The decisive guard against a laundered positive: the **bare V-seed** (the exact Arm-2 initial condition;
Cosserat ω left EMPTY) must carry NO (2,3) and NO charge at t=0. Direct-write `k4.V_inc` via the genesis-23
`_seed_v_partner` shape (circularly-polarized in-plane V-vector, `amp = frac·V_SNAP`, `A²_V = frac²`); the
**forbidden** knot planters (`initialize_electron_2_3_sector` / `initialize_2_3_torus_knot_sector`) are
**not referenced** (static guard = `[]`).

| frac | E_V_seed | `vinc_closes_23` | `vref_closes_23` | ω real-space `c` | `max|ω|` | `|H_bel|` | **admissible** |
|---|---|---|---|---|---|---|---|
| 0.30 | 1.503 | False | False | 0 | 0.0 | 0.0 | **True** |
| 0.60 | 6.010 | False | False | 0 | 0.0 | 0.0 | **True** |
| 0.85 | 12.06 | False | False | 0 | 0.0 | 0.0 | **True** |
| 0.95 | 15.07 | False | False | 0 | 0.0 | 0.0 | **True** |

**SEED-AUDIT CERTIFICATE = PASS (all fracs).** `vinc_closes_23 = vref_closes_23 = False`, ω-sector provably
empty (`max|ω| = 0` ⇒ ω-(2,3) absent), `|H_bel| = 0` (charge-neutral by construction). The seed is an
admissible **generative precursor**, NOT a planted answer. No frac is VOIDed.

---

## §2 — HEADLINE: `dE_V = E_V(photon-ON Arm-1) − E_V(no-photon Arm-2)` — the source half REVERSES

Frozen pre-run: `eps_machine = 1×10⁻⁹` (natural V_SNAP² units), Arm-2 the decisive control. `max|V_inc|≠0`
is **NOT** the headline (trivially true for any legitimate seed — the circularity trap). `E_V = Σ_interior
V_inc²` (PML-excluded, active-masked).

| frac | E_V(Arm-1, photon) | E_V(Arm-2, control) | **dE_V** (photon-attributable) | Arm-2 / seed (control decays) |
|---|---|---|---|---|
| 0.30 | — | — | **+1.076×10⁻²** | 0.533 |
| 0.60 | — | — | **+8.336×10⁻²** | 0.549 |
| 0.85 | 7.358 | 6.991 | **+3.667×10⁻¹** | 0.580 |
| 0.95 | — | — | **+7.814×10⁻¹** | 0.602 |

**monotone ↑ in seed depth = True · deep-positive (0.85 ∧ 0.95) = True · NOT C1.** The control (Arm-2: same
seed, no photon) **decays** to 0.53–0.60× its seed E_V over the window — the seed V-sector relaxes without
the photon. The photon **tips the EMF channel from decay to growth**, by an amount that grows monotonically
with the seed's standing V_inc (deeper seed → larger `emf = 2·V_inc·∂L/∂V_sq`). This is the source half of
GAP-1 reversing — a genuine, photon-attributable, seed-depth-monotone effect, distinct from genesis-23's
identically-zero source channel. **Figure 1.**

---

## §3 — The winder gap: V-sector phase-space gets the "2", never the "3"

A46 phase-space winding (the ONLY headline-paired topology read), sampled on the |ω|² density-peak (CP7),
Arm-1 (seed + photon):

| frac | t=0 `(w_tor,w_pol)` | peak `(w_tor,w_pol)` | peak `rel_pol` | `closes(2,3)` |
|---|---|---|---|---|
| 0.30 | (0, 0) | (1.0, 0.0) | 0.002 | **False** |
| 0.60 | (0, 0) | (**2.0**, 0.0) | 0.004 | **False** |
| 0.85 | (0, 0) | (**2.0**, 0.0) | 0.005 | **False** |
| 0.95 | (0, 0) | (1.0, −0.0) | 0.005 | **False** |

**The toroidal "2" appears in the V-sector phase-space** (`w_tor → 2.0` at frac 0.60/0.85) — the longitudinal
"3" grade now genuinely enters phase-space carrying a *p=2* winding. **The poloidal "3" (q=3) does not:**
`w_pol = 0` at every frac, and the poloidal contour is **unpopulated** (`rel_pol ≈ 0.002–0.005`, two orders
below the `> 0.1` reliability gate). The (2,3) **never closes**, t=0 or peak. **The missing primitive is the
poloidal (q=3) winder** — sharper than genesis-23's "the '3' never enters phase-space at all" (there the
whole V-sector was unpopulated; here the toroidal half populates and winds, only the poloidal fibre is
missing). **Figure 1 (right).**

> **🔴 RETRACTION + ARM-2 TOROIDAL CONTROL (2026-06-09, Rule 12 — the §3 prose above is preserved; this
> block governs).** The claim above that "the toroidal half populates and winds" is **withdrawn as
> sub-gate.** The decisive Arm-2 (no-photon) toroidal control — `vinc_w_tor` AND `vinc_rel_tor` for BOTH
> arms, all fracs, at the |ω|² density peak (CP7) — was serialized for the first time (the prior run
> COMPUTED Arm-2's `vinc_w_tor` at `genesis_24_saturated_seed.py:224` then DISCARDED it; `rel_tor` was
> recorded for NO arm):
>
> | frac | Arm-1 (seed+photon) `w_tor` | Arm-1 `rel_tor` | Arm-2 (seed, NO photon) `w_tor` | Arm-2 `rel_tor` | reliable (`rel_tor>0.1`)? |
> |---|---|---|---|---|---|
> | 0.30 | 1.0 | **0.000** | 0.0 | **0.000** | NO (both) |
> | 0.60 | **2.0** | **0.000** | 0.0 | **0.000** | NO (both) |
> | 0.85 | **2.0** | **0.000** | 0.0 | **0.000** | NO (both) |
> | 0.95 | 1.0 | **0.000** | 0.0 | **0.000** | NO (both) |
>
> (t=0, every frac, both arms: `w_tor = 0.0`, `rel_tor = 0.0`.)
>
> **Case C — sub-gate: `rel_tor = 0.000` for BOTH arms at EVERY frac**, two orders below the `>0.1` closure
> gate (`reflection_genesis_23_self_assembly.py::_phase_space_winding:227`). Arm-1's `w_tor = 1/2/2/1` is
> **non-monotone, collapses at the deepest frac 0.95 (back to 1), NOT reproduced at deepest saturation, and
> rides a zero-reliability contour → meaningless noise, not a populated winding.** The toroidal "2" is
> **UNVERIFIED**: not photon-driven (Case A needs Arm-1 `rel_tor>0.1` — FAILS) and not a clean seed artifact
> (Case B needs Arm-2 to reach a reliable `w_tor≈2` — Arm-2 is `0`). The genesis-23 contrast is therefore
> *empty V-sector* (`amp=0`) vs genesis-24 *populated-but-winding-unreliable* (`amp>0`, `rel_tor=0`), NOT
> "no 2" → "real 2". **Source-count: NOT resolved by the toroidal channel** (see CORRECTING HEADER). The
> robust topological result stands — (2,3) does not close and the winder primitive is absent — now true of
> BOTH the poloidal fibre (`rel_pol ≈ 0.005`) AND the toroidal "2" (`rel_tor = 0.000`); the
> "only-the-poloidal-fibre-is-missing" asymmetry above is withdrawn. JSON: `arm12_toroidal`,
> `task1_toroidal_resolution.case = "C_subgate"`.

---

## §4 — Smith chart: NO migration to the Γ=−1 rim (genesis-23 GAP-2 reproduced)

Smith Γ = (Z_eff−1)/(Z_eff+1) (the Op3 reflection map; `_impedance_gamma_shared`), Γ_min over interior-alive
cells. Γ<0 = μ-side short (toward the Γ=−1 electron rim); Γ>0 = ε-side open.

| frac | seed+photon Γ_min (t=0) | Arm-1 photon-end Γ_min | Arm-2 control-end Γ_min |
|---|---|---|---|
| 0.30 | −0.078 | −0.015 | +0.000 |
| 0.60 | −0.061 | −0.012 | +0.000 |
| 0.85 | −0.034 | −0.009 | +0.000 |
| 0.95 | −0.018 | −0.009 | +0.000 |

**The photon does NOT drive the operating point to the Γ=−1 rim** — it drives it *toward* the matched center
(Γ→−0.009), and the control relaxes fully to Γ=0. |Γ| < 0.08 everywhere: the confining wall is
**under-engaged** in *every* arm — exactly the genesis-23 **GAP-2** (the soft, non-pumping wall under-engages;
no stable Γ=−1 confining window), now reproduced coupled-with-seed. The electron's Γ=−1 short never forms,
so there is no rim for the (2,3) to close onto. **Figure 2** (all operating points cluster at center; the
red Γ=−1 rim sits empty).

---

## §5 — Decisive controls: Arm-2 null, Arm-3 = genesis-23 null reproduced

- **Arm-2 (SAME seed, NO photon) — the decisive control.** Topology **null at every frac** (`closes(2,3) =
  False`); E_V **decays** to 0.53–0.60× seed (no spontaneous energization, no drift to the rim). The seed
  does **not** carry the answer → no circularity, the `dE_V` is genuinely photon-attributable.
- **Arm-3 (no seed + photon) = the genesis-23 lone-photon null.** `E_V = 0.0`, `max|V_inc| = 0.0`,
  `closes(2,3) = False`, Γ_min = −0.015. **Exact reproduction of genesis-23 GAP-1** — the lone transverse
  photon never energizes the V-sector. This is the null the seed reverses (§2).

---

## §6 — Arm-4 charge flip: the photon's helicity (provenance), NOT an emergent (2,3) charge

| frac | final H_bel (+h photon) | final H_bel (−h photon) | sign flips |
|---|---|---|---|
| 0.30 | −78.3 | +78.6 | **True** |
| 0.60 | −71.7 | +71.4 | **True** |
| 0.85 | −66.0 | +65.3 | **True** |
| 0.95 | −64.7 | +63.8 | **True** |

The integrated Beltrami helicity flips sign with the seeded photon helicity at every frac (reproduces
genesis-23's +h −78.4 / −h +81.0). **Honest scope:** because the (2,3) does **not** close (§3), this is the
**photon's own carried helicity** — a provenance certificate that the ω-charge is tracked, **not** an
emergent torus-knot charge. No emergence-class charge claim. **Figure 5.**

---

## §7 — flag-don't-fix: the EMF `:703` source channel is a SECULAR PUMP, not an energize-LOCK

The conservation ledger (A-Rule-10 reactance pair recorded every step; energize-LOCK vs secular-pump
discriminator) **does not close** for the very channel that produces `dE_V>0`:

- **Arm-1 @ frac 0.95, 40-step window:** `H_drift = −6.3 %` (exceeds the 5 % gate), `H_span = 7.4 %`,
  `v_secular_ratio = 1.22` (mild), **`|L|` unbounded** (> 5× growth). `ledger.closes = False`.
- **Emission window (frac 0.85, 100 steps):** `E_V` rises **monotonically** to **6.8×10⁸** at step 99
  (the last step — it *never peaks-then-falls*), `max|V_inc| → 1.08×10⁴` (A²_V ~ 10⁸, far past rupture).
  **`reverses = False`** — the channel **detonates** rather than relaxing the photon back out.

This is the known EMF-reciprocal runaway (engine docstring `k4_cosserat_coupling.py:242`: *"this AMPLIFIES
the runaway; path-1 was the wrong direction"*) and it echoes the reactive-entrainment / GAP-2 pump bug.
**Consequence (stated, not smoothed):** the `dE_V>0` source-reversal is the **early phase of a secular
pump**, not a conservative absorb-LOCK. A *source channel exists and fires*; it is **not** a locked
absorber. **Figures 3 (reactance pair) + 4 (ledger).**

---

## §8 — Arm-5 (Class-C discriminator): the winder gap is STRUCTURAL, not drive-strength

CW free-work drive at ω₀ on the seed V-tank (amplitude 0.20·V_SNAP):

| frac | H_drift | v_secular | `closes(2,3)` | pump-only structure? |
|---|---|---|---|---|
| 0.30 | +0.552 | 0.96 | False | — |
| 0.60 | −0.204 | 0.88 | False | — |
| 0.85 | −0.301 | 0.96 | False | — |
| 0.95 | −0.304 | 1.05 | False | — |

`arm5_pump_only_structure = False`: a sustained CW free-work pump produces **no (2,3) structure either**.
Since **neither** the finite single-photon absorb (Arm-1) **nor** the CW pump (Arm-5) winds the poloidal
"3", the winder gap is **not a drive-strength artifact** — it is **structural** (a missing primitive). This
is the clean Class-C discriminator outcome: the absence of (2,3) survives the pump that would have exposed a
mere energy-deficit.

---

## §9 — Gap localization (two gaps) + DERIVED / VERIFIED / BLOCKED

**The run localizes the residual obstruction to two precise, independent mechanisms:**

1. **WINDER gap (primary, the falsified half).** The V-sector phase-space populates the **toroidal "2"**
   (`w_tor → 2`) but **not the poloidal "3"** (`w_pol = 0`, `rel_pol ≈ 0.005`). Missing primitive = the
   **poloidal (q=3) winder**. Robust across finite-photon (Arm-1) AND CW-pump (Arm-5) ⇒ structural.
2. **SOURCE-STABILITY gap (secondary, flagged).** The ω→V source channel exists (the EMF `:703` reciprocal,
   activated by the V-seed bias — genesis-23 had none) but is a **secular pump**, not an energize-LOCK
   (ledger fails, emission detonates). Same class as the genesis-23 GAP-2 / reactive-entrainment pump bug.

| Claim | Status |
|---|---|
| Non-circular seed is admissible (no t=0 (2,3), charge-neutral) | **VERIFIED** (§1, all fracs) |
| Photon energizes V beyond no-photon control, monotone in seed depth | **VERIFIED (raw dE_V>0)** → 🔴 **DEMOTED to PUMP-ONSET** (CORRECTING HEADER: seed-biased secular pump via EMF `:703`; ledger fails `H_drift −6.3 %` / `\|L\|` 2.7→43.4, emit detonates `E_V→6.8×10⁸`; **not** an energize-LOCK absorption) |
| Lone photon (no seed) leaves V-sector at zero (= genesis-23 GAP-1) | **VERIFIED** (§5 Arm-3) |
| Charge = photon helicity (provenance, sign flips) | **VERIFIED** (§6) |
| Source channel = the EMF `:703` reciprocal, biased by standing V_inc | **DERIVED** (mechanism chain; genesis-23 dead→genesis-24 live) |
| de-novo (2,3) closes in (V_inc,V_ref) phase-space | **BLOCKED** (§3: poloidal q=3 winder absent, rel_pol≈0.005) |
| Operating point migrates to the Γ=−1 electron rim | **BLOCKED** (§4: stays near center, |Γ|<0.08) |
| Conservative absorb-LOCK + emission reverses | **BLOCKED** (§7: secular pump, detonates, no reversal) |
| α from the Golden-Torus (2,3) geometry | **BLOCKED** (no (2,3) ⇒ no Golden-Torus to realize) |

**consistency-vs-emergence:** `dE_V>0` and the charge flip are **consistency/manifestation-class** (supplied
IC + axiom-structure). **No emergence-class positive** — the two emergence-scoped quantities (de-novo (2,3)
winding, emergent knot charge) both BLOCKED. The headline is honestly a **gap-localization**, not a genesis.

---

## §10 — Skills fired · figures · honest closure

**Skills:** `substrate-native-check` (CP8 seed-not-plant — seed-audit PASS; CP9 dynamical time-domain; CP10
confinement-as-boundary-Γ — Smith chart, not bulk force) · `consistency-vs-emergence` (no emergence claim;
dE_V = supplied-IC manifestation) · `ave-conserved-vs-pumped` (the EMF channel is a PUMP — ledger fails,
emission detonates) · `phase-space-coordinate-check` / A46 (winding in (V_inc,V_ref); Smith Γ-plane the
native diagnostic) · `ave-canonical-source` (V_SNAP / V_YIELD = √α·V_SNAP / R_I = √(2α) imported, zero new
free params) · `ave-driver-script-honesty` (every number measured from EVOLVED fields; reactance pair every
step) · `ave-regime-phase-state-check` (the secular-pump regime explicitly flagged, not read as genesis) ·
`verify-before-cite`.

**Figures** (`src/scripts/vol_1_foundations/`):
- [`genesis24_fig1_dEV_headline.png`](../src/scripts/vol_1_foundations/genesis24_fig1_dEV_headline.png) — dE_V(t) per frac, photon-ON vs control + the headline delta.
- [`genesis24_fig2_smith_chart.png`](../src/scripts/vol_1_foundations/genesis24_fig2_smith_chart.png) — Smith chart: seed → photon-end → control-end; **all cluster at center, no Γ=−1 migration**.
- [`genesis24_fig3_reactance_pair.png`](../src/scripts/vol_1_foundations/genesis24_fig3_reactance_pair.png) — C-state (V_inc) vs L-state (Φ_link); Arm-1 vs Arm-5 pump.
- [`genesis24_fig4_ledger.png`](../src/scripts/vol_1_foundations/genesis24_fig4_ledger.png) — H, H_bel, |L| vs t (ledger non-closure).
- [`genesis24_fig5_arm4_charge_flip.png`](../src/scripts/vol_1_foundations/genesis24_fig5_arm4_charge_flip.png) — Arm-4 charge sign flip.

**Honest closure (Rule 11 / substitution-not-retraction).** 🔴 *Post-run demotion (see CORRECTING HEADER):
"reverses the source half / one real step past genesis-23" is demoted — the live ω→V channel is a
NON-CONSERVATIVE secular pump (ledger fails `H_drift −6.3 %` / `|L|` 2.7→43.4; emission detonates
`E_V→6.8×10⁸`), so `dE_V>0` is pump-onset, not a demonstrated absorption; and the toroidal "2" is sub-gate
(Case C, `rel_tor=0.000` both arms), so the localization is to the winder primitive generally, not "only the
poloidal fibre." The closure remains a clean B; the prose below is preserved unchanged.* Genesis-24 is a
**clean, reproduced B**: the
saturated-seed reframe **reverses the source half of GAP-1** (a V-populated IC converts the dead ω→V channel
into a live, monotone, photon-attributable one — *one real step past genesis-23*) but **does not close the
topology** — the poloidal (q=3) winder is structurally absent and the Γ=−1 rim never forms. The deliverable
is a **sharper localization** of the L3 open problem: the residual gap is the **poloidal winder primitive**
(plus a flagged secondary **source-channel-stability** gap — the EMF `:703` reciprocal is a secular pump, not
an energize-LOCK). No framework failure; no debug-toward-A; no dropped adjudication criteria. Per
substrate-native-check, the winder-primitive question must be re-walked BEFORE any new coupling primitive is
added — surfaced for Grant / auditor adjudication, NOT auto-resolved.
