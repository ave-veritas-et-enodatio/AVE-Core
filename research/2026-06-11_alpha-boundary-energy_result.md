# α as boundary-energy partition — RESULT (Phase-2 forward check)

**Date:** 2026-06-11
**Branch:** `analysis/2026-06-11-r1-alpha-forward-check`
**Prereg (FROZEN, committed ALONE):** [`research/2026-06-11_alpha-boundary-energy_prereg.md`](2026-06-11_alpha-boundary-energy_prereg.md) @ `cd7e7ae3`
**Driver:** `src/scripts/vol_9_device/alpha_boundary_forward_check.py` (FORWARD-FIRST; analytic + measured printed before α loads)
**MEASURED data:** SHA-pinned `570b50d7…` : `src/scripts/vol_9_device/_output/s11_denovo_results.json` [`made_build`]

> **VERDICT: DIFFERENT-RATIO (bin 2, §7).** The pre-registered most-probable outcome (§8) is **confirmed**.
> This is a **clean negative** (Rule 11 honest closure): the prediction failed where it was registered to be
> most likely to fail, a single mechanism explains it, the branch position is recorded. **Not** debugged
> toward a rescue.

---

## 1 — The numbers (forward-first; α loaded LAST)

| Quantity | Value | Frozen gate (§7) |
|---|---|---|
| `E_V_cons_first / last` | `11.699920 / 12.910681` | banked scalars |
| `H_cons_first / last` | `29202.798000 / 24611.637367` | banked scalars |
| **`r = E_V_cons_last / H_cons_last`** | **`5.245763e-4`** | FROZEN primary (a) |
| `r2 = E_V_cons_last/(H_cons_last−E_V_cons)` | `5.248516e-4` | arm (a2) — `r2≈r` ✓ |
| `r_first = E_V_cons_first / H_cons_first` | `4.006438e-4` | stationarity companion |
| **stationary** (`|r/r_first−1| ≤ 0.10`) | **False** (drift `0.3093`) | FAILS the 10% band |
| `ALPHA` (CODATA, `constants.py:133`) | `7.2973525693e-3` | comparison target |
| **`r/ALPHA`** | **`0.071886`** (`r` is **~13.9× below α**) | bin gate |
| `match` (`|r/ALPHA−1| ≤ 0.25`) | **False** (`|·| = 0.9281`) | bin-1 gate FAILS |
| `tight` (`≤ 0.05`) | False | — |
| arm (b): `pocket_cells` | `0` → **VOID** | SHELL-NEVER-FORMS |

**Bin = DIFFERENT-RATIO.** `r ≈ 5.25e-4 ≈ α/13.9`. The longitudinal V-share of *total* conserved energy is
**not** α at the frozen definition (a), and it is **not even stationary** across the settle window (drifts
31%) — so it is not a structural fraction at all on this object.

## 2 — The mechanism (one cause, named — the §8 pre-registration was right)

`H_cons` (total conserved energy) carries the **canon-flagged decoupled-bulk reservoir**:
`bulk_sector_unstable_free_evolution = True`, `bulk_decoupled_from_V_proof = "V|bulk-live − bulk-zeroed|=0.0
over 8000 steps (V finite, decoupled)"`. The longitudinal V-sector (`E_V_cons ≈ O(10)`) is a tiny share of a
total dominated (`H_cons ≈ O(10⁴)`) by that decoupled reservoir, so `r ~ 5e-4 ≪ α`. This is **exactly** the
a-priori most-probable outcome the prereg registered (§8: "`r ~ O(5e-4)` — ~14× BELOW α → DIFFERENT-RATIO is
the a-priori most probable bin"). The forward number landed inside the registered expectation.

## 3 — Arms status (all pre-registered; no post-hoc selection)

- **ANALYTIC arm → ANALYTIC-BLOCKED (reconstruction-fenced).** The standing-V wall-energy integral is
  reachable on banked primitives only via the golden-torus geometric `Q = 4π³+π²+π` (= `ALPHA_COLD`), which
  **is** the ¼-/golden-torus family. No independent `S(A)=√(1−A²)` + `Γ_bulk=−1` wall-energy integral
  primitive is banked. Per the §1.1 fence it bins **ANALYTIC-BLOCKED**; the route would stand on the
  MEASURED arm alone — which is DIFFERENT-RATIO.
- **arm (a2)** ran: `r2 ≈ r` ✓ (consistent, both DIFFERENT-RATIO).
- **arm (a3)** (exclude the decoupled reservoir — the *only* α-ward path) is **FENCED + ANALYTIC-BLOCKED**:
  the field is not banked, and excluding a reservoir to reach α is coincidence-magnet-adjacent — justified
  only by the `bulk_decoupled` flag, **never** by α-proximity. Not run.
- **arm (b)** is **VOID**: `pocket_cells = 0` (SHELL-NEVER-FORMS) — no interface band exists.
- **arm (c)** (reactance-pair share) **ANALYTIC-BLOCKED** on banked data (ringdown banks `w_est/Q`, not an
  energy split).
- **Pre-registered DEFINITION-SPREAD finding stands:** only (a)/(a2) run on banked data; (b) VOID, (a3)/(c)
  blocked. The robustness spread is **UNDER-EVALUABLE** — and that limitation is itself the registered result.

## 4 — Class (consistency-vs-emergence): α is a DEAD input — but there is no match to class

Static dead-input + forward-vs-fit (§5 steps 4–5), grep-verified this session:
- The genesis engine (`unified_genesis_engine.py`) and the energy accounting (`bulk_energy_conserved` /
  `total_energy_unified`) take **no fine-structure α** as a dynamical input.
- The **only** α touch in the whole `s11_de_novo` pipeline is the post-hoc ringdown-Q note at
  `s11_de_novo_sweep.py:698` (`ALPHA_COLD_INV`, explicitly *"post-hoc, NOT a bin criterion"*) — it consumes
  the ringdown `Q`, **not** `E_V_cons`/`H_cons`. No `comparison_only_alpha` / `gamma_target` field feeds the
  partition.
- **⇒ α is a DEAD input to the partition by construction** (forward-vs-fit PASS). The de-novo MADE object is
  **α-free** — unlike the v6 phasor object, which carries `gamma_target_for_alpha` → consistency-class
  (prereg §4.2).

So a match *would* have been emergence-candidate (clean inputs). But **there is no match** (DIFFERENT-RATIO),
so the class question is moot: nothing to class.

## 5 — Secondary (the §2 discriminator): SECONDARY-BLOCKED + MOOT

Cross-object-class partition invariance is **SECONDARY-BLOCKED** on banked data (the `planted` leg banks
probe-response only — no `E_V_cons`/`H_cons`), and **MOOT**: the secondary exists to guard a *match* against
a coincidence-magnet; with no primary match, there is nothing to guard. No re-extraction was run (the
prereg's "one cheap re-extraction" is not load-bearing for a DIFFERENT-RATIO verdict).

## 6 — flag-don't-fix: the two-α value is STALER and TIGHTER than the prereg/constants comment state

**verify-before-cite catch.** The driver computes `ALPHA_COLD = 1/(4π³+π²+π) = 7.2973363441e-3`. But:
- `src/ave/core/constants.py:205` comment reads `# ≈ 7.29352e-3`, and
- the prereg §0.1 #3 / §0.2 both quote `ALPHA_COLD ≈ 7.29352e-3` ("differ only at the **4th** significant
  digit").

The value `7.29352e-3` is **stale/incorrect** — the actual arithmetic is `7.29734e-3` (the comment is off in
the 4th digit; the constant itself, computed `1.0/ALPHA_COLD_INV`, is correct — only the inline comment and
the prereg's copy of it are wrong). The real gap is `|ALPHA/ALPHA_COLD − 1| = 2.2e-6` — the two αs agree to
**~2 ppm (≈6th digit)**, far **tighter** than the prereg's stated "4th digit". The driver's
`two_alpha_indistinct` gate is therefore **True** (`2.2e-6 < 0.25`).

This **strengthens** the coincidence-magnet warning (the golden-torus geometric α reproduces CODATA α to
~2 ppm), and is moot only because `r` lands nowhere near either α here. **Surfaced, not silently fixed:** the
stale comment at `constants.py:205` and the prereg's copy are flagged; the prereg is FROZEN and not edited
(the verdict is unaffected — `r/α = 0.072` is two orders below the 1.0-match band either way).

## 7 — Honest closure (Rule 11 / Rule 12)

The pre-registered hypothesis — *the longitudinal boundary-energy share equals α* (def (a), share-of-total) —
is **falsified on this object**: `r/α = 0.072`, non-stationary, single decoupled-reservoir mechanism. The
prereg registered this as the most-probable outcome; the forward number confirmed it. **The discipline worked
at full strength:** clean negative, mechanism named (decoupled-bulk reservoir dominates `H_cons`), arms
honestly under-evaluable, branch position recorded. **No rescue** (the α-ward arm a3 is fenced and unbanked;
chasing it would be coincidence-magnet number-hunting). Per Rule 12 the prereg body is preserved; this result
adds the 🔴 falsification record. **No new hypothesis is refilled into the slot** here — any successor (e.g. a
parameter-free wall-energy derivation, or a re-extraction with the decoupled reservoir properly accounted)
gets its **own** version number and verification chain.
