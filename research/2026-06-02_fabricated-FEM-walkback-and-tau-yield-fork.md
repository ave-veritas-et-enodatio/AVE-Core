# Fabricated-FEM Walk-Back: V_total-vs-ρ_threshold Decoupling + the τ_yield Fork

**Date:** 2026-06-02
**Branch:** `analysis/parameter-ledger-v2-reframe` (continues PR-B: `f9bd8da2` core + `063e7c1b` propagation)
**Type:** Corpus-honesty walk-back — substrate-physics untangling + exhaustive propagation + a held fork
**Discipline:** `ave-walk-back` (3h-exhaustive), `substrate-native-check`, `consistency-vs-emergence`, `verify-before-cite`, flag-don't-fix
**Predecessor:** `2026-06-01_baryon-V2-dual-reactance-closure.md` (the V=2 reactance-count reframe this completes)

> **One-line:** the corpus fused two distinct quantities — the **dual-reactance count** `V_total = 2` (a forced Axiom-1 integer, profile-INDEPENDENT) and the **saturation density threshold** `ρ_threshold ≈ 1.1062` (Gaussian-ansatz-derived, profile-DEPENDENT) — and anchored both to a "3D FEM integration" narrative. That narrative is retired: the only "FEM" script is voxel quadrature of the Gaussian-ansatz saturated overlap volume (a `ρ_threshold` consistency check), not finite-element, and not a derivation of the reactance count. The two 2's (V_total vs ρ_threshold) are now decoupled. A SECOND fork was raised — whether the τ_yield "2" is the dual-reactance count or a separate `6 × V_crossing` geometric factor — and is now **RESOLVED (Grant 2026-06-02): FINISH.** The corpus shows there is **one** `V_total = 2.0` (the dual-reactance count PR-B already reframed in the compact form), presented two ways that "differ only by factoring choice"; the `6 × V_crossing` is circular (`V_crossing := V_toroidal/6`), a vestige of the retired geometric framing, NOT an independent derivation of 2. Bucket A is now finished (FEM-verified label dropped, dual-reactance reframe propagated); the only genuinely-open thing is the **mechanism** (does the yield *stress* scale with the reactance-sector count). See the §3 in-session correction below.

---

## §1 — The decoupling (Bucket B, executed)

### §1.1 — Two distinct quantities, one fabricated anchor

The corpus tied `V_total = 2` to "FEM convergence of the Gaussian-ansatz integration," which made the forced reactance count look both *profile-dependent* and *FEM-derived*. Both are false. Decoupled:

| Quantity | What it is | Profile? | Provenance |
|---|---|---|---|
| `V_total = 2` | **dual-reactance count** — the node's two reactance sectors `X_C` (3 translational-E DOF) + `X_L` (3 microrotational-B DOF), Axiom 1 | **INDEPENDENT** | Forced integer count; mass-confirmed (V=2 → 1836.117 m_e vs CODATA 1836.153). Counted, not integrated. |
| `ρ_threshold ≈ 1.1062` | **saturation density threshold** — where mutual coupling `M/L = 1/√2` between orthogonal Gaussian flux tubes exceeds the topological-coherence floor; `ρ_threshold = 1 + σ/4` | **DEPENDENT** | Gaussian flux-tube ansatz (FWHM = ℓ_node fixed by Axiom 1; the functional *form* is the open gap). Legitimate open derivation gap — KEPT. |

The Gaussian-ansatz rigour gap binds `ρ_threshold` **only**. It does NOT bind `V_total = 2`. A channel count does not change if the flux-tube profile changes.

### §1.2 — `substrate-native-check`: why the "FEM-integrated volume" frame is an SM-leak

The substrate is discrete K4-TLM scatter+connect + Cosserat LC. The AVE-native object for `V_total` is a **count of reactance channels** (Axiom-1 DOF), not a continuum spatial integral. The "FEM-integrated geometric toroidal-halo volume" framing is exactly the continuum-integration default that `substrate-native-check` Checkpoint 1/3 flags: it substitutes a continuum-Helmholtz-style spatial integral for what is a discrete sector count. Rejected. `V_total = 2` is counted (two sectors); `ρ_threshold` is the only quantity in this neighborhood that a profile integral legitimately bears on.

### §1.3 — `consistency-vs-emergence` classification

- `V_total = 2`: **Class B axiom-manifestation** (the count IS Axiom 1's reactance-sector structure at the baryon scale; mass-confirmed). NOT a Class D emergence test — it is a forced count, not a dimensionless observable derived from simulation primitives without using the target. The honest residual remains the per-channel coupling `p_c = 8πα` (consistency-class), per the predecessor doc §4 ("1-residual Skyrme").
- The Gaussian-ansatz saturated overlap volume (the script's output): a **Class C consistency check** on the Gaussian profile — it lands near 2.0 *by property of the ansatz at this `ρ_threshold`*, not as an independent geometric derivation. Reporting it as "confirming a topological bound as a geometric identity" was the overclaim retired here.

---

## §2 — The no-FEM-script verification (`verify-before-cite`) — a correction to the predecessor doc

The predecessor V2-closure doc §3 Failure-4 asserted: *"There is no finite-element driver in the repo... A grep for an FEM halo-volume solver returns nothing."* **This is empirically imprecise and is corrected here** (flag-don't-fix — surfaced, not silently overwritten; the predecessor doc's §3 is a frozen result doc, so the correction lives here + in the propagated sites, not by editing §3 in place).

**What actually exists (verified live this session):**

- `src/scripts/vol_2_subatomic/fem_borromean_convergence.py` (tracked since initial release `de9d2293`; present at PR-B core `f9bd8da2` and at HEAD) + its JAX port `fem_borromean_convergence_jax.py` ("All physics is IDENTICAL").
- Run live this session, it produces: N=128 → 2.0002, N=256 → **2.001208**, Richardson N→∞ → **2.002655 (0.133%)**. These match the manuscript table (`thermal-softening.md` 2.0012 / 2.0027 / 0.13%) and the cited "FEM-verified 2.001 ± 0.003 Richardson N→∞" provenance **exactly**. So this script IS the genuine computational source of the "FEM-verified" claims — the predecessor's "no FEM driver" was a miss (a third 5×-miss surprise on top of the two the predecessor flagged).

**But the script is NOT what the narrative claimed, on three counts:**

1. **Not finite-element.** It is a uniform-Cartesian-grid Riemann sum / voxel quadrature: `V_sat = Σ Θ(ρ_total > ρ_threshold)·Δx³` (`np.linspace`, `dV = dx³`, `np.sum(sat_mask)·dV`). No basis functions, no mesh elements, no weak form, no stiffness matrix. "FEM" is a misnomer.
2. **Does not compute the reactance count.** It integrates the **Gaussian-ansatz** three-tube saturated overlap volume against `ρ_threshold ≈ 1.1062`. That is a `ρ_threshold`-bound quantity (the open Gaussian-ansatz gap), NOT the dual-reactance count `V_total = 2`.
3. **Is a self-consistency check, not a derivation.** That the Gaussian overlap volume lands near 2.0 is a property of the Gaussian profile at this `ρ_threshold` — corroborative of internal consistency, not an independent geometric derivation of the integer 2.

So the canonical conclusion is unchanged and in fact strengthened: the "3D finite-element integration of the full Borromean topology yields V_total=2.0" narrative is false (mislabeled method + false fusion of the profile-dependent overlap integral with the profile-independent reactance count). The script is kept (it is a legitimate Gaussian-ansatz integration bearing on the `ρ_threshold` discussion) but relabeled honestly per `ave-driver-script-honesty`.

---

## §3 — The τ_yield "fork" (Bucket A) — RESOLVED (Grant 2026-06-02): FINISH

> **DISPOSITION (Grant 2026-06-02): RESOLVED — FINISH.** Propagate the
> dual-reactance reframe to all Bucket-A τ_yield sites + drop the fabricated
> "FEM-verified" label + record the named open item. The prior framing in this
> §3 (a genuine "two distinct 2's" fork, HELD-AND-FLAGGED) was **WRONG and is
> corrected in-session below** (flag-don't-fix: the original §3.2 reasoning is
> preserved struck-through-in-prose with the correction adjacent, not silently
> overwritten — see §3.2′). The corrected reality: there is **ONE** `V_total =
> 2.0` (the dual-reactance count PR-B reframed at `01_appendices.tex:72`),
> presented in two forms that the corpus itself says "differ only by factoring
> choice and yield identical 1.04×10²² Pa" (`magnetic-saturation.md:20`); the
> `6 × V_crossing` form is **circular** — `tvs-transition.md:27` *defines*
> `V_crossing := V_toroidal/6 = 2.0/6`, so `6 × V_crossing = V_toroidal =
> V_total = 2.0` is a re-factoring of the same 2, NOT an independent geometric
> derivation. The genuinely-open item is purely the **mechanism** (does the
> yield *stress* scale with the reactance-sector count, or merely inherit the
> value 2). Bucket A is now executed; the §3.3 on-branch inconsistency is
> thereby resolved (all forms now consistently call V_total the dual-reactance
> count).

### §3.1 — The fork

The 7 Bucket-A sites embed `V_total = 2` in the dielectric-yield-stress formula. Two presentations co-exist in the corpus:

- **Compact form** (`appendices-overview.md:66`; `01_appendices.tex:72`, already PR-B-reframed): `τ_yield = e²·V_total/(8πε₀ℓ⁴)` — `V_total` appears as a bare factor.
- **Expanded form** (`magnetic-saturation.md:10,20`; `04_continuum_electrodynamics.tex:219,228`; `tvs-transition.md:24,27`; `vol4/claim-quality.md:977,993`; `vol1/claim-quality.md:492,506`): `τ_yield = ρ_bulk·c² · (6 × V_crossing) · p_c/(8π)`, where **`V_crossing = V_toroidal/6 = 2.0/6` is the per-crossing halo volume** and `V_total = 6 × V_crossing = 2.0`.

**The fork:** does the τ_yield "2" genuinely scale with the **dual-reactance count** (Grant's lean: the dielectric yield is an Axiom-4 saturation event; saturation = reactance hitting its limit → 2 sectors → factor 2), or is it a **separate geometric factor** — "6 Borromean crossings × per-crossing-volume (⅓ each) = 2" — that only coincidentally equals 2?

### §3.2 — [SUPERSEDED — see §3.2′] Why HELD (the "don't-fuse-the-2's" risk materialized — verbatim evidence)

> **🔴 SUPERSEDED IN-SESSION (Grant 2026-06-02).** The four points below
> concluded the τ_yield "2" was a *structurally independent* geometric factor
> (a "sum over 6 Borromean crossings") distinct from the dual-reactance count,
> and that fusing them would manufacture a false identity. **That conclusion was
> wrong.** It mistook a **circular re-factoring** for an independent derivation.
> The body is preserved unedited for the audit trail; the correction is §3.2′
> immediately below. (Rule-12 substitution-not-retraction: the original
> reasoning is not deleted; the corrected analysis carries its own statement.)

The brief's flag-don't-force fallback: *"if your in-session physics work shows the τ_yield '2' is actually a separate geometric factor ('6 Borromean crossings × ⅓ = 2') that only coincidentally equals 2 — i.e. the 'don't-fuse-the-2's' risk materializes — then HOLD Bucket A unchanged and flag it."* It materialized:

1. **The expanded form derives the 2 via a geometric 6-crossing route**, verbatim (`tvs-transition.md:27`):
   > *"where $\mathcal{V}_{crossing} = V_{toroidal}/6 = 2.0/6$ is the per-crossing halo volume, $\mathcal{V}_{total} = 6 \times \mathcal{V}_{crossing} = 2.0$..."*

   and the physical story (`magnetic-saturation.md:10,12`), verbatim:
   > *"...the verified topological halo volume ($\mathcal{V}_{total} = 2.0$...)."* ... *"By evaluating the scalar volume summation of these topological knot crossings ($\Sigma \mathcal{V}_{crossing}$)..."*

   This is a **sum over the proton's 6 Borromean crossings**, structurally distinct from the dual-reactance count's structure (X_C sector + X_L sector = 2).

2. **The crossing number `c` is a real, separate, load-bearing topological primitive** throughout the corpus (the (2,q) torus-knot ladder; `c=5` cinquefoil proton; `r_opt = κ_FS/c`; "≈170 MeV per crossing"). The proton 6³₂ Borromean's 6-crossing structure is not the same object as the 2 reactance sectors. `6 × (1/3) = 2 sectors` is an unproven bridge.

3. **No corpus derivation links the dielectric yield to the 2-reactance-sector count.** A targeted grep (`yield ∩ reactance`, `saturation ∩ two reactance`, `dual-reactance ∩ yield`) returns nothing — the only "reactance sectors yields" hits are the baryon eigenvalue's regenerative loop, not the τ_yield formula. So Grant's lean ("saturation → reactance limit → 2 sectors") is a *physically-natural re-interpretation* the corpus does not currently derive, and the existing leaves derive the 2 via the *different* geometric `6 × V_crossing` route.

4. **The shared anchor is the fabricated volume claim, not a physics identity.** The two presentations agree on 2.0 only because the corpus set `V_crossing = V_toroidal/6` — i.e. the τ_yield "2" inherits its value from the (now-reframed) `V_total`-as-volume. Applying Grant's lean would assert `6 × V_crossing ≡ X_C + X_L` — fusing the 6-crossing geometric sum with the 2-sector reactance count, manufacturing a false identity from the shared digit 2. This is exactly the failure mode `dual-reactance-storage-taxonomy.md` §"three distinct 2's" warns against ("do not write 'the reactance count equals [the other 2]' or imply one derives the other").

### §3.2′ — CORRECTED: there is ONE `V_total = 2.0`; the "fork" was a misread of a circular re-factoring (Grant 2026-06-02)

The §3.2 analysis above had **the verbatim corpus text backwards.** It treated `6 × V_crossing` as a *structurally independent* geometric quantity ("a sum over the proton's 6 Borromean crossings") that merely coincidentally equals the dual-reactance count, and on that basis held the two 2's apart. But the corpus text it quotes **defines `V_crossing` in terms of `V_total`, not the reverse** — the "derivation" is circular, so it is not an independent derivation of the value at all. The corrected reading (each point answers the same-numbered §3.2 point):

1. **The expanded form does NOT derive the 2 via an independent geometric route — it re-factors `V_total`.** `tvs-transition.md:27` (verbatim): *"$\mathcal{V}_{crossing} = V_{toroidal}/6 = 2.0/6$ ... $\mathcal{V}_{total} = 6 \times \mathcal{V}_{crossing} = 2.0$."* Read the chain: `V_crossing` is **defined as** `V_toroidal/6`, so `6 × V_crossing = V_toroidal = V_total = 2.0` is an algebraic identity that reproduces the input. It computes nothing about crossings; it re-states `V_total`. The "Σ over 6 crossings" prose (`magnetic-saturation.md:12`) is window-dressing on that circular factoring.

2. **The crossing number `c` is real and load-bearing elsewhere — but it is NOT what sets this 2.** The (2,q) torus-knot ladder, `c=5` cinquefoil, `r_opt = κ_FS/c`, "~170 MeV/crossing" are all genuine and untouched. The error was inferring that *because* crossing-number is load-bearing elsewhere, the `6 × V_crossing` writing here must be an independent crossing-count derivation. It is not: here `V_crossing` is back-defined from `V_total`. The proton's 6³₂ Borromean topology remains as topology; it does not set the value 2.

3. **That no corpus derivation links yield to the reactance count is exactly — and only — the named open item, not grounds to hold a fork.** The empty `yield ∩ reactance` grep does not show the τ_yield 2 is a *different* quantity; it shows the **mechanism** (yield *stress* ∝ reactance-sector count) is **not yet derived**. That is the §3.4 open item, full stop. The value 2 is unambiguously the one `V_total` (the compact form `e²·V_total/(8πε₀ℓ⁴)` at `01_appendices.tex:72` was already reframed to the dual-reactance count by PR-B; the expanded form is the same quantity, as `magnetic-saturation.md:20` states the two "differ only by factoring choice and yield identical 1.04×10²² Pa").

4. **There is no second 2 to fuse — so there is no false identity to manufacture.** `6 × V_crossing` and `V_total` are the *same* number by the corpus's own definition `V_crossing := V_toroidal/6`, not two numerically-coincident objects. Dropping `6 × V_crossing` to honest re-factoring language (or removing it) and calling `V_total` the dual-reactance count does **not** assert `6 × V_crossing ≡ X_C + X_L` as a derived identity — it states they are one quantity (`V_total`) written two ways, with the *mechanism* (does yield scale with the count) flagged open. The `dual-reactance-storage-taxonomy.md` §"three distinct 2's" warning applies to **V=2 vs K/G=2 vs E_L=E_C** (genuinely unrelated objects); the τ_yield `6 × V_crossing` is not a fourth distinct 2 — it is the V=2 itself, re-factored.

**Net:** one `V_total = 2.0` (the dual-reactance count), two factorings, one open mechanism question. Bucket A is finished accordingly (§2 of the return: all sites reframed; the circular `6 × V_crossing` demoted to honest re-factoring language).

### §3.3 — Disposition

**RESOLVED (Grant 2026-06-02): FINISH — executed.** All Bucket-A sites reframed to the dual-reactance count + the fabricated "FEM-verified" / "confirmed by FEM" label dropped + the `6 × V_crossing` circular re-factoring demoted to honest language (or removed). Sites executed (fresh-grep-verified enumeration, see §4.2′): `tvs-transition.md:27`; `magnetic-saturation.md:10,20`; `04_continuum_electrodynamics.tex:219,228`; `vol4/claim-quality.md:977,993`; `vol1/claim-quality.md:492,506,508`; `appendices-overview.md:66`. The named open item (§3.4) is recorded canonically at the two τ_yield claim-quality entries + a dedicated `§τ_yield open item` subsection in `dual-reactance-storage-taxonomy.md`.

The **on-branch internal inconsistency** flagged below is now **resolved by this finish**: `01_appendices.tex:72` (already PR-B-reframed to the dual-reactance count in the compact form) and the expanded-form derivation sites (`magnetic-saturation.md`, `04_continuum_electrodynamics.tex`, `tvs-transition.md`) now **all** consistently call `V_total` the dual-reactance count; the "FEM-verified" label and the circular `6 × V_crossing`-as-derivation are gone from the expanded sites.

> *(Original flag, preserved for trail:)* Internal inconsistency introduced by PR-B propagation `063e7c1b`: `01_appendices.tex:72` was reframed to the dual-reactance count in the *compact* form while the Vol 1 Ch 4 derivation it points to (`magnetic-saturation.md:20`) still said "FEM-verified" and built it as `6 × V_crossing`. — *Resolved by the FINISH above.*

### §3.4 — The named open item (regardless of fork outcome)

> **Open item — derive that τ_yield ∝ the dual-reactance count, vs merely inheriting the value 2.** The dielectric yield is an Axiom-4 saturation event; saturation = a reactance sector reaching its limit. *If* the yield stress scales with the count of saturating reactance sectors (2), then `τ_yield ∝ V_total` is the reactance count and Grant's lean applies cleanly. *But* the corpus currently derives the τ_yield "2" via a geometric `6 × V_crossing` (6 Borromean crossings × per-crossing volume) route that reaches 2.0 by an unrelated path. Closing this requires a substrate-mechanism derivation establishing **either** (a) that `6 × V_crossing` IS the 2-reactance-sector count (collapsing the fork toward Grant's lean), **or** (b) that the τ_yield 2 is a genuinely separate geometric factor (keep the geometric story; the shared value 2 is a coincidence to be flagged, not fused). Until then, the two 2's stay separate.

### §3.5 — Boundary question for Grant — ANSWERED (2026-06-02): FINISH

The three options below were surfaced for Grant. **Grant adjudicated FINISH** — option (A), as **corrected by §3.2′**: the "risk" annotation on (A) was itself the misread. Because `6 × V_crossing` is a circular re-factoring of the same `V_total` (`V_crossing := V_toroidal/6`), reframing `V_total` to the dual-reactance count does **not** assert `6 × V_crossing ≡ X_C + X_L` as a derived identity — there is only one 2 to begin with. The yield-scales-with-count *mechanism* is recorded as the named open item (§3.4), not asserted. Options preserved for the trail:

- **(A) [CHOSEN — as corrected by §3.2′] Apply Grant's lean** — reframe the τ_yield `V_total` to the dual-reactance count + drop the fabricated "FEM-verified" label + record the §3.4 open item. (The original "Risk: fuses two 2's" annotation was the misread §3.2′ corrects: there is one `V_total`, re-factored; nothing is fused.)
- **(B) Keep the geometric `6 × V_crossing` story, drop only the fabricated "FEM-verified" label** — *not chosen.* The `6 × V_crossing` is circular (re-states `V_total`), not a genuine per-crossing-volume sum; keeping it would preserve a vestige of the retired geometric framing presented as a derivation.
- **(C) Something else** — *not chosen.*

The unambiguous Bucket-B fabrication retirement + the V_total/ρ_threshold decoupling were already executed; the τ_yield finish is now executed too, per Grant's call.

---

## §4 — Propagation inventory (`ave-walk-back` 3h-exhaustive)

### §4.1 — Executed (Bucket B + script honesty)

| Site | Change |
|---|---|
| `thermal-softening.md:77` + `02_baryon_sector.tex:137` | Decouple: Gaussian-ansatz gap binds `ρ_threshold` only, not `V_total`; "do-not-fuse" note added. |
| `thermal-softening.md:99-107` + `02_baryon_sector.tex:156-167` | **SOURCE** retired: "3D finite-element integration... geometric identity" → honest "Gaussian-ansatz voxel-quadrature overlap-volume; `ρ_threshold` consistency check; NOT FEM, NOT the reactance count." Data table kept, relabeled. |
| `mathematical-closure.md:167` + `12_mathematical_closure.tex:144` | Rigour-gap row: drop `V_total` from the "re-evaluate" clause (gap binds `ρ_threshold` only); legacy "FEM-converged" provenance dropped. |
| `vol2/claim-quality.md:50,65` | Caveat + rationale: `V_total=2` is profile-independent reactance count; gap binds `ρ_threshold`; "FEM convergence is binding" → voxel-quadrature consistency check, not derivation. |
| `proton-identification.md:120` | **Correction** to PR-B's "no FEM driver exists": script exists, is voxel quadrature of the Gaussian-ansatz overlap volume (not FEM, not the reactance count). "Do not build `v-total-fem-verification.md`" kept. |
| `full-derivation-chain.md:525-530` + `02_full_derivation_chain.tex:610-615` | **Correction** to PR-B's "(no FEM driver; provenance fabricated)" comment: same precise reframe. |
| `fem_borromean_convergence.py` (+ JAX port) | `ave-driver-script-honesty` scope note: voxel quadrature, not FEM; computes Gaussian-ansatz overlap volume (bears on `ρ_threshold` gap), not the V=2 reactance count. Runtime header + plot title corrected. |
| `ARCHITECTURE.md:55-56` | Row descriptions reframed (voxel quadrature, not FEM; ρ_threshold, not the reactance count). |

### §4.2′ — Executed (Bucket A — FINISH, Grant 2026-06-02)

The §4.2 "held" list is now **executed**. Per-site changes:

| Site | Change |
|---|---|
| `tvs-transition.md:27` | Prose: drop "FEM-verified Borromean halo volume"; `V_total = 2.0` = dual-reactance count (link to taxonomy); the `6 × V_crossing` writing demoted to a circular re-factoring of the same `V_total` (vestige of retired geometric framing), not a derivation. |
| `magnetic-saturation.md:10` | Drop "confirmed by FEM to 0.13%"; "verified topological halo volume" → dual-reactance count (link). |
| `magnetic-saturation.md:20` | Notation block: drop "(FEM-verified)"; `V_total` = dual-reactance count; `6 V_crossing` demoted to circular re-factoring; compact-form equivalence kept. |
| `04_continuum_electrodynamics.tex:219` | `.tex` mirror of :10 — same reframe. |
| `04_continuum_electrodynamics.tex:228` | `.tex` mirror of :20 — same reframe. |
| `vol4/claim-quality.md:977` | Specific-claim: drop "(FEM-verified Borromean halo volume)"; `V_total` = dual-reactance count; circular `6 × V_crossing` parenthetical. |
| `vol4/claim-quality.md:993` | Rationale: drop "FEM-verified Borromean halo volume"; dual-reactance count + named open item appended. |
| `vol1/claim-quality.md:492` | Specific-claim: drop "FEM-verified to 0.13%"; dual-reactance count; circular-re-factoring note. |
| `vol1/claim-quality.md:506` | Rationale: drop "FEM-verified to 0.13%" provenance; reframe to dual-reactance count; **distinct** macroscopic-embedding open question preserved verbatim; solidity arithmetic untouched; named open item noted as distinct. |
| `vol1/claim-quality.md:508` | strengthen-by: "proton-specific 6-crossing Borromean topology" → "proton-provenanced dual-reactance count" (embedding question substance preserved). |
| `appendices-overview.md:66` | Drop "FEM-verified"; `V_total` = dual-reactance count (link), "not an integrated/geometric halo volume" — matches `01_appendices.tex:72` compact form. |

`01_appendices.tex:72` was already PR-B-reframed (compact form) and now agrees with the expanded-form sites — the §3.3 on-branch inconsistency is resolved.

**Display-equation note:** the expanded-form *equations* (`tvs-transition.md:24`, `04_continuum_electrodynamics.tex:224`, `magnetic-saturation.md:17`) still display `… × (6 × V_crossing) × …` as one factoring equal to `… × V_total × α`. This is arithmetically true and the *adjacent prose* now explicitly labels it a circular re-factoring, not a derivation (Grant's "demote to honest language" option, chosen over "drop it" to preserve the audit trail of the corpus's historical writing). No site now *asserts* an independent geometric derivation of 2.

### §4.3 — NEW beyond the brief's enumeration (the expected "more")

The fresh exhaustive grep surfaced, beyond the brief's Bucket A+B lists: the FEM-labeled scripts (`fem_borromean_convergence.py` + JAX port), the `thermal-softening.md:104-105` / `02_baryon_sector.tex:162-163` FEM data table, `ARCHITECTURE.md:55-56`, and the already-landed PR-B comment lines (`full-derivation-chain.md`, `02_full_derivation_chain.tex`) whose "no FEM driver" wording needed the §2 correction. The script is NOT wired as a strengthening `exp-` node (only ARCHITECTURE.md references it), so relabeling it does not touch any claim-DAG solidity.

### §4.4 — Out of scope (left alone)

`vol6/claim-quality.md:38` (correct per-result He-4 claim, per the brief). Verified untouched.

---

## Verification log (`verify-before-cite`)

- `fem_borromean_convergence.py` run live this session → N=256 = 2.001208, Richardson = 2.002655 (0.133%); matches manuscript table + the "2.001 ± 0.003 Richardson" provenance exactly.
- `git log --follow` + `git cat-file -e f9bd8da2:…` → the FEM script tracked since `de9d2293`, present at PR-B core and HEAD.
- Post-edit sweep (Bucket B, original): "3D finite-element integration" prose = 0; "topological bound as a geometric identity" overclaim = 0.
- **Post-FINISH sweep (Bucket A, 2026-06-02):** `FEM-verified` / `confirmed by FEM` / `geometric halo volume` / `integrated volume` / `FEM-verified Borromean halo volume` in the τ_yield context = **0** (fresh exhaustive grep across `manuscript/` + `.index/`, pasted in the return §3). The only surviving "FEM"/"halo volume" hits are: (a) the three deliberately-reframed rigour-gap rows (`mathematical-closure.md`, `12_mathematical_closure.tex` — "FEM-converged ... is dropped" reframe prose); (b) the legitimate CEM-methods-survey FEM-as-solver content (vol4 future-geometries, unrelated); (c) the already-reframed Bucket-B dual-reactance sites (vol2, `01_appendices.tex`, etc.); (d) the dropped-claim comment blocks in `full_derivation_chain` (history, marked DROPPED). None assert a τ_yield FEM-verified halo volume.
- No corpus derivation links dielectric yield to the 2-reactance-sector count (targeted grep empty) — this is the **named open item** (§3.4), NOT grounds for a fork (§3.2′ corrects the prior §3.2 reading).
- `make refresh-kb-metadata` run post-edit → regenerated `.index/claims.jsonl` picked up the reframed `clm-8ep2b4` + `clm-o2shcn` rationale strings (no hand-edit of jsonl); `make verify` green. Commit + push: see return §7.
