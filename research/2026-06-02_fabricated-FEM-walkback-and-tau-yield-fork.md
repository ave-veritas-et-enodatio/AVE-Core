# Fabricated-FEM Walk-Back: V_total-vs-ρ_threshold Decoupling + the τ_yield Fork

**Date:** 2026-06-02
**Branch:** `analysis/parameter-ledger-v2-reframe` (continues PR-B: `f9bd8da2` core + `063e7c1b` propagation)
**Type:** Corpus-honesty walk-back — substrate-physics untangling + exhaustive propagation + a held fork
**Discipline:** `ave-walk-back` (3h-exhaustive), `substrate-native-check`, `consistency-vs-emergence`, `verify-before-cite`, flag-don't-fix
**Predecessor:** `2026-06-01_baryon-V2-dual-reactance-closure.md` (the V=2 reactance-count reframe this completes)

> **One-line:** the corpus fused two distinct quantities — the **dual-reactance count** `V_total = 2` (a forced Axiom-1 integer, profile-INDEPENDENT) and the **saturation density threshold** `ρ_threshold ≈ 1.1062` (Gaussian-ansatz-derived, profile-DEPENDENT) — and anchored both to a "3D FEM integration" narrative. That narrative is retired: the only "FEM" script is voxel quadrature of the Gaussian-ansatz saturated overlap volume (a `ρ_threshold` consistency check), not finite-element, and not a derivation of the reactance count. The two 2's are now decoupled. A SECOND fork — whether the τ_yield "2" is the dual-reactance count or a separate `6 × V_crossing` geometric factor — is **HELD for Grant's adjudication** with verbatim evidence (Bucket A unchanged).

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

## §3 — The τ_yield fork (Bucket A) — HELD-AND-FLAGGED for Grant

### §3.1 — The fork

The 7 Bucket-A sites embed `V_total = 2` in the dielectric-yield-stress formula. Two presentations co-exist in the corpus:

- **Compact form** (`appendices-overview.md:66`; `01_appendices.tex:72`, already PR-B-reframed): `τ_yield = e²·V_total/(8πε₀ℓ⁴)` — `V_total` appears as a bare factor.
- **Expanded form** (`magnetic-saturation.md:10,20`; `04_continuum_electrodynamics.tex:219,228`; `tvs-transition.md:24,27`; `vol4/claim-quality.md:977,993`; `vol1/claim-quality.md:492,506`): `τ_yield = ρ_bulk·c² · (6 × V_crossing) · p_c/(8π)`, where **`V_crossing = V_toroidal/6 = 2.0/6` is the per-crossing halo volume** and `V_total = 6 × V_crossing = 2.0`.

**The fork:** does the τ_yield "2" genuinely scale with the **dual-reactance count** (Grant's lean: the dielectric yield is an Axiom-4 saturation event; saturation = reactance hitting its limit → 2 sectors → factor 2), or is it a **separate geometric factor** — "6 Borromean crossings × per-crossing-volume (⅓ each) = 2" — that only coincidentally equals 2?

### §3.2 — Why HELD (the "don't-fuse-the-2's" risk materialized — verbatim evidence)

The brief's flag-don't-force fallback: *"if your in-session physics work shows the τ_yield '2' is actually a separate geometric factor ('6 Borromean crossings × ⅓ = 2') that only coincidentally equals 2 — i.e. the 'don't-fuse-the-2's' risk materializes — then HOLD Bucket A unchanged and flag it."* It materialized:

1. **The expanded form derives the 2 via a geometric 6-crossing route**, verbatim (`tvs-transition.md:27`):
   > *"where $\mathcal{V}_{crossing} = V_{toroidal}/6 = 2.0/6$ is the per-crossing halo volume, $\mathcal{V}_{total} = 6 \times \mathcal{V}_{crossing} = 2.0$..."*

   and the physical story (`magnetic-saturation.md:10,12`), verbatim:
   > *"...the verified topological halo volume ($\mathcal{V}_{total} = 2.0$...)."* ... *"By evaluating the scalar volume summation of these topological knot crossings ($\Sigma \mathcal{V}_{crossing}$)..."*

   This is a **sum over the proton's 6 Borromean crossings**, structurally distinct from the dual-reactance count's structure (X_C sector + X_L sector = 2).

2. **The crossing number `c` is a real, separate, load-bearing topological primitive** throughout the corpus (the (2,q) torus-knot ladder; `c=5` cinquefoil proton; `r_opt = κ_FS/c`; "≈170 MeV per crossing"). The proton 6³₂ Borromean's 6-crossing structure is not the same object as the 2 reactance sectors. `6 × (1/3) = 2 sectors` is an unproven bridge.

3. **No corpus derivation links the dielectric yield to the 2-reactance-sector count.** A targeted grep (`yield ∩ reactance`, `saturation ∩ two reactance`, `dual-reactance ∩ yield`) returns nothing — the only "reactance sectors yields" hits are the baryon eigenvalue's regenerative loop, not the τ_yield formula. So Grant's lean ("saturation → reactance limit → 2 sectors") is a *physically-natural re-interpretation* the corpus does not currently derive, and the existing leaves derive the 2 via the *different* geometric `6 × V_crossing` route.

4. **The shared anchor is the fabricated volume claim, not a physics identity.** The two presentations agree on 2.0 only because the corpus set `V_crossing = V_toroidal/6` — i.e. the τ_yield "2" inherits its value from the (now-reframed) `V_total`-as-volume. Applying Grant's lean would assert `6 × V_crossing ≡ X_C + X_L` — fusing the 6-crossing geometric sum with the 2-sector reactance count, manufacturing a false identity from the shared digit 2. This is exactly the failure mode `dual-reactance-storage-taxonomy.md` §"three distinct 2's" warns against ("do not write 'the reactance count equals [the other 2]' or imply one derives the other").

### §3.3 — Disposition

**HELD-AND-FLAGGED.** All 7 Bucket-A sites left unchanged (verified: `git diff` touches no Bucket-A file). The genuine fork is surfaced for Grant's physical intuition — the resolution mechanism per the brief.

Note an **internal inconsistency already on-branch** (introduced by PR-B propagation `063e7c1b`, surfaced here, not resolved): `01_appendices.tex:72` was already reframed to call `V_total` the dual-reactance count in the *compact* `e²·V_total/(8πε₀ℓ⁴)` form, while the Vol 1 Ch 4 derivation it points to (`magnetic-saturation.md:20`) still calls it "FEM-verified" and builds it as `6 × V_crossing`. The corpus is therefore already ambiguous on this exact point. Resolving it requires the fork decision below, NOT a unilateral edit.

### §3.4 — The named open item (regardless of fork outcome)

> **Open item — derive that τ_yield ∝ the dual-reactance count, vs merely inheriting the value 2.** The dielectric yield is an Axiom-4 saturation event; saturation = a reactance sector reaching its limit. *If* the yield stress scales with the count of saturating reactance sectors (2), then `τ_yield ∝ V_total` is the reactance count and Grant's lean applies cleanly. *But* the corpus currently derives the τ_yield "2" via a geometric `6 × V_crossing` (6 Borromean crossings × per-crossing volume) route that reaches 2.0 by an unrelated path. Closing this requires a substrate-mechanism derivation establishing **either** (a) that `6 × V_crossing` IS the 2-reactance-sector count (collapsing the fork toward Grant's lean), **or** (b) that the τ_yield 2 is a genuinely separate geometric factor (keep the geometric story; the shared value 2 is a coincidence to be flagged, not fused). Until then, the two 2's stay separate.

### §3.5 — Boundary question for Grant

Three options:

- **(A) Apply Grant's lean** — reframe the τ_yield `V_total` to the dual-reactance count + retire the "FEM-verified" label + record the §3.4 open item. (Risk: asserts `6 × V_crossing ≡ X_C + X_L` without derivation — fuses two 2's.)
- **(B) Keep the geometric `6 × V_crossing` story, drop only the fabricated "FEM-verified" label** — the "2" stays a per-crossing-volume sum; flag the numerical coincidence with the reactance count; record the §3.4 open item. (Drops the fabrication without pre-judging the fork.)
- **(C) Something else** per your physical read of whether dielectric yield scales with reactance-sector count or with crossing-volume sum.

The unambiguous Bucket-B fabrication retirement + the V_total/ρ_threshold decoupling are executed; the τ_yield fork (which fuses-or-doesn't-fuse two 2's) is your call.

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

### §4.2 — Held (Bucket A — fork, unchanged)

`magnetic-saturation.md:10,20`; `04_continuum_electrodynamics.tex:219,228`; `tvs-transition.md:24,27`; `vol4/claim-quality.md:977,993`; `vol1/claim-quality.md:492,506`; `appendices-overview.md:66`. (7 site-references; `01_appendices.tex:72` was already PR-B-reframed and is the internal-inconsistency partner noted in §3.3.)

### §4.3 — NEW beyond the brief's enumeration (the expected "more")

The fresh exhaustive grep surfaced, beyond the brief's Bucket A+B lists: the FEM-labeled scripts (`fem_borromean_convergence.py` + JAX port), the `thermal-softening.md:104-105` / `02_baryon_sector.tex:162-163` FEM data table, `ARCHITECTURE.md:55-56`, and the already-landed PR-B comment lines (`full-derivation-chain.md`, `02_full_derivation_chain.tex`) whose "no FEM driver" wording needed the §2 correction. The script is NOT wired as a strengthening `exp-` node (only ARCHITECTURE.md references it), so relabeling it does not touch any claim-DAG solidity.

### §4.4 — Out of scope (left alone)

`vol6/claim-quality.md:38` (correct per-result He-4 claim, per the brief). Verified untouched.

---

## Verification log (`verify-before-cite`)

- `fem_borromean_convergence.py` run live this session → N=256 = 2.001208, Richardson = 2.002655 (0.133%); matches manuscript table + the "2.001 ± 0.003 Richardson" provenance exactly.
- `git log --follow` + `git cat-file -e f9bd8da2:…` → the FEM script tracked since `de9d2293`, present at PR-B core and HEAD.
- Post-edit sweep: "3D finite-element integration" prose = 0; "topological bound as a geometric identity" overclaim = 0; Bucket A "FEM-verified Borromean halo volume" sites intact (held); the only residual "FEM-converged" prose is the three deliberately-reframed rigour-gap rows (now "voxel quadrature... not a derivation of the reactance count").
- No corpus derivation links dielectric yield to the 2-reactance-sector count (targeted grep empty) — basis for §3.2 point 3.
