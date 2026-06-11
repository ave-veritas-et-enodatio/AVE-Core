# R3 — Lattice Decoration Discriminator (Pre-Registration)

**Epic:** `_orchestration/2026-06-11_lattice-d1-test-gated.md`
**Branch (implementor):** `analysis/2026-06-12-lattice-decoration-discriminator` (proposed, off `main`)
**Lane:** implementor — **Phase-0 extension only** (no genesis run)
**Status:** PRE-REG — frozen pending Grant threshold ratification on ⟨…⟩ lines below
**Supersedes:** any prose D1 ruling; D1 is an **outcome bin**, not a pre-test pick

---

## 0. Corpus-grep anchor (ave-prereg Step 2)

| Prior work | Verdict |
|---|---|
| v9 Phase-0 smokes on **bare** srs-R/L + **bare** diamond (`chiral_lattice.py`, PR #195) | **DONE** — writhe ±4.0867e-02 / 0.0; Bishop Δθ/L ±75.462°/unit |
| 2026-06-07 lattice-net resolution | **SUPERSEDED as ruling** — retained as **Arm-2 null hypothesis** until R3 runs |
| `cosserat_field_3d.py` κ_chiral = α·pq/(p+q) | **EXISTS** — decoration channel on **diamond** engine (`KAPPA_CHIRAL_ELECTRON` ≈ 8.757e-3) |
| CVR framing doc (PR #197) | **Framing only** — not a lattice adjudication |

**Gap this prereg closes:** Phase-0 compared bare srs to bare diamond. It never ran the **third arm** — achiral diamond + excited `κ_chiral` decoration — through the same signed-observable battery. Without Arm 3, a passing Smoke B on srs cannot discriminate substrate (A) from decoration-diagnostic (B).

---

## 1. Derivation target (one sentence)

> Test whether **Cosserat/Op14 chiral decoration on achiral diamond** reproduces the **signed chiral observables** that **bare srs** shows **without** `κ_chiral`, thereby falsifying or supporting srs-as-substrate vs diamond+decoration.

---

## 2. Physical picture (ave-prereg Step 1.5)

- **Cold srs:** handedness lives in **graph connectivity** (10-gon ring writhe, mirror-odd).
- **Cold diamond:** achiral positions; writhe = 0 by construction.
- **Decorated diamond:** achiral **graph**, chiral **constitutive split** via `A²_μ = (1+κ·h)A²_base`, `A²_ε = (1−κ·h)A²_base` (`cosserat_field_3d.py:522-523`).
- **Discriminator question:** Is signed gyrotropy **structural** (needs srs net at κ=0) or **excitable** (diamond + κ suffices)?

---

## 3. Three-arm battery (symmetric observables)

| Arm | Net | Chirality source | `κ_chiral` |
|-----|-----|------------------|------------|
| **1** | srs-R / srs-L | structural (graph) | **0** (no injection) |
| **2** | diamond | none (control) | **0** |
| **3** | diamond | decoration (Cosserat) | **{0, +κ_e, −κ_e}** |

κ_e = `KAPPA_CHIRAL_ELECTRON` = `kappa_chiral_from_topology(2, 3)` from `ave.core.constants` / `cosserat_field_3d.py` — **canonical import, no hand-set**.

---

## 4. Observables (substrate-native-check + phase-space-coordinate-check)

### O1 — Geometric ring writhe (Phase-0 replay)

- **Sector:** geometric pseudoscalar on shortest closed circuits (`chiral_lattice.net_ring_writhe`).
- **Class:** **consistency-class** on Arm 1/2 (replication gate). **Not** load-bearing for D1 alone — decoration does not relocate nodes.
- **Expectation:** Arm 1 ±writhe; Arm 2 ≈ 0; Arm 3 ≈ 0 at all κ (positions unchanged).
- **Purpose:** confirm Arm 3 doesn't accidentally mutate diamond geometry.

### O2 — Screw-axis Bishop transport rate Δθ/L (Phase-0 replay, dynamics)

- **Sector:** chirality coordinate (polarization-frame rotation), **not** lattice-Cartesian amplitude.
- **Class:** **emergence-class** only if measured with **dynamical** scatter+connect or vector-TLM step — **not** algebraic fit (`substrate-native-check` CP9).
- **Controls:** enantiomorph-pair difference (srs-R vs srs-L); κ-sign flip (Arm 3 +κ vs −κ); diamond κ=0 null.
- **Phase-0 baselines (L=6, grep-confirmed):**
  - srs-R: Δθ/L ≈ **+75.462°/unit**, writhe ≈ **−4.0867e-02**
  - srs-L: Δθ/L ≈ **−75.462°/unit**, writhe ≈ **+4.0867e-02**
  - diamond κ=0: Δθ/L ≈ **0**, writhe **0**

### O3 — Decoration-only dynamical channel (NEW — load-bearing for R3)

- **Setup:** diamond lattice + `use_asymmetric_saturation=True` + `kappa_chiral ∈ {+κ_e, −κ_e}` on the **same** screw-axis Bishop transport probe as O2.
- **Drive-chain audit (A3 from v9 prereg):** no circular polarization at launch; no handed boundary forcing; κ is the **only** parity-odd knob between +κ and −κ runs.
- **Measured:** `Δθ/L` and signed torsion along the screw orbit (same pipeline as `chiral_lattice_dynamics.py` / `chiral_lattice_smoke_dynamics.py`).

---

## 5. Pre-registered predictions (executable gates)

Thresholds in ⟨…⟩ — Grant ratifies at freeze; defaults proposed from Phase-0 floors.

| ID | Prediction | PASS | Falsifier |
|----|------------|------|-----------|
| **R3-P1** | O1 replication: Arm 1/2 writhe matches Phase-0 within ⟨1e-4⟩ relative | Both enantiomorphs sign-flip; diamond ≈ 0 | Regression ⇒ scaffold broken; block R3 |
| **R3-P2** | O2 replication: Arm 1/2 Δθ/L mirror-odd, diamond null within ⟨10%⟩ of srs magnitude | Same as Phase-0 | Regression ⇒ block R3 |
| **R3-P3** | **Arm 3 geometric writhe** ≈ 0 at all κ (‖wr‖ < ⟨5%⟩ of ‖wr_srs‖) | Positions achiral | ‖wr‖ ≥ 5% srs ⇒ geometry leak; flag |
| **R3-P4** | **Arm 3 at κ=0:** ‖Δθ/L‖ ≤ ⟨5%⟩ of ‖Δθ/L‖_srs | Decoration off = achiral null | κ=0 already done (Arm 2) |
| **R3-P5** | **Arm 3 at κ=±κ_e:** ‖Δθ/L‖ ≥ ⟨20%⟩ of ‖Δθ/L‖_srs **AND** sign(κ) flips sign(Δθ/L) | Decoration injects signed channel | κ≠0 still null ⇒ decoration cannot mimic structural chirality on this observable |
| **R3-P6** | **Arm 1 (κ=0) vs Arm 3 (+κ_e):** if both pass R3-P5-scale rotation, compare magnitudes: ‖Δθ/L‖_srs(κ=0) / ‖Δθ/L‖_diamond(+κ) = ρ. Record ρ; **no single PASS** — feeds D1 bin table §7 | — | — |

**Default thresholds (if Grant delegates):** use Phase-0 floors verbatim (10% control null, 5% geometry guard).

---

## 6. Consistency-vs-emergence classification (per observable)

| Observable | Class | Notes |
|------------|-------|-------|
| O1 writhe on Arm 1/2 | **Consistency** | Replication of committed Phase-0 |
| O1 writhe on Arm 3 | **Consistency** | Expect null — confirms decoration doesn't move nodes |
| O2 on Arm 1 at κ=0 | **Emergence-class candidate** | Signed rotation without κ injection |
| O2/O3 on Arm 3 at κ≠0 | **Consistency-class** | κ is explicit calibration-channel input |
| D1 ruling from R3 alone | **Forbidden** | R3 is **necessary**, not **sufficient** — Phase-1 P4/P6 required |

---

## 7. D1 outcome bins (post-R3 only — no pre-test pick)

| Bin | Condition | Framing read |
|-----|-----------|--------------|
| **D1-A** | R3-P5 **FAIL** (κ≠0 cannot produce signed Δθ/L) **AND** Arm 1 passes R3-P2 | Structural srs chirality not replaceable by decoration on this channel → **substrate-challenge evidence** |
| **D1-B** | R3-P5 **PASS** (κ reproduces signed Δθ/L at ≥20% srs magnitude) **AND** magnitudes comparable (ρ ∈ ⟨0.5, 2.0⟩) | Decoration on diamond suffices for this observable → **decoration-diagnostic evidence** |
| **D1-MIXED** | R3-P5 passes weakly OR only one of {writhe, Δθ/L} discriminates | **Do not rule** — proceed to Phase-1 P4/P6 |
| **D1-INCONCLUSIVE** | R3-P1/P2 regression fail | Fix scaffold; no framing language |

**ave-multi-falsifier-triangulation:** R3-P5 on Arm 3 is **generic-physics-consistent** (any chiral constitutive medium can rotate polarization). **D1-A requires pairing** with Arm 1 **at κ=0** (substrate-distinct: structural graph chirality without injection). R3-P5 PASS alone → **D1-B or D1-MIXED**, never D1-A.

---

## 8. Controls & kill conditions (Rule 11)

- **κ_chiral ablation:** Arm 3 must include κ=0 run (duplicate Arm 2 on O2/O3).
- **Sign flip:** +κ_e vs −κ_e on Arm 3 (matter/antimatter decoration sign).
- **No genesis:** no soliton seed, no Op14 global σ solve, no planted `(2,3)` — R3 is discriminator only.
- **Kill:** if O1 on Arm 1/2 regress → close R3, fix `chiral_lattice` first.
- **No rescue:** post-hoc threshold edits after seeing Arm 3 numbers.

---

## 9. Implementation sketch (implementor — not executed in this doc)

**Reuse:** `chiral_lattice.py` (Arms 1–2), `chiral_lattice_dynamics.py` observers.

**New (minimal):** driver `src/scripts/vol_1_foundations/lattice_decoration_discriminator.py` + keeper `src/tests/test_lattice_decoration_discriminator.py` that:
1. Builds diamond net (existing `build_diamond_net`).
2. Wires `CoupledK4Cosserat` / asymmetric saturation path with `kappa_chiral` sweep.
3. Runs O2/O3 Bishop transport at κ ∈ {0, +κ_e, −κ_e}.
4. Emits JSON artifact under `assets/sim_outputs/` with per-arm numbers.

**Skills at implement time:** `ave-canonical-source`, `ave-driver-script-honesty`, `substrate-native-check`, `phase-space-coordinate-check`, `consistency-vs-emergence`.

---

## 10. Sequencing

1. **R3** (this prereg) → implementor branch → CI green
2. **Freeze v9 Phase-1** (thresholds only; framing deferred) — see revised header in `2026-06-11_genesis-v9-phase1-prereg_DRAFT.md`
3. **Phase-1 P1–P6** on all three arms where applicable
4. **D1 adjudication memo** — cite bins from §7 + Phase-1 P4/P6; **then** corpus walk-back queue

---

## 11. Grant freeze checklist

- [ ] Ratify ⟨thresholds⟩ in §5 (or accept defaults-from-Phase-0-floors)
- [ ] Confirm Arm 3 uses `KAPPA_CHIRAL_ELECTRON` only (no extra κ sweep unless apparatus-floor tags each point)
- [ ] Confirm **no §0 framing pick** in freeze — D1 bin table §7 is the ruling machinery
