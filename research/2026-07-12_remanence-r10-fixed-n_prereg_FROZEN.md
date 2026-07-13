# Remanence R10 fixed-\(N\) discriminator — FROZEN prereg

**Freeze discipline.** This prereg is frozen **by push** as its own commit **BEFORE**
any remanence driver / harness-fire code exists (ave-prereg v1.7 Step 3.11).
Bins below enforce; flags don’t.

**Authorization.** ★RULED G-PERSIST 2026-07-12 — constitutive remanence before
node-mint; KEEP-BOTH; no `genesis_v{N}`. Charter walk:
`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md`.

**Class.** Constitutive-DOF / LOOP GAP rank-4 discriminator. Rule-14:
`loop_gap_harness` on `VacuumEngine3D`. No fourth engine. No srs v18+. No graph-growth.

**α-CLEAN** on the verdict path. α may appear only in seed/geometry helpers already
canonical — not as a persistence target.

---

## Sector header

- **SECTOR** = constitutive remanence (Level-2 loop DOF) for lasting dilatation /
  Cosserat localization on **fixed \(N\)**.
- **DOF today:** Level-1 \(S_{\rm eq}(A)\) anhysteretic YES; memristive profile on
  harness YES; **emergent zero-drive \(B_r\)** — OPEN (REMANENCE-LANDED never).
- **MODE** = bulk / harness rank-4 (not EM-\(S_{11}\) alone; not µ-R2 as PASS).
- **REGIME** = near-yield / post-drive quiescence (zero-drive persistence).
- **PHASE-STATE** = cold–warm solid lattice; not melt; not node-mint.
- **Instrument:** P11 after pinned quiet; memristive-OFF ablation; latch-ban sabotage.
- **consistency-vs-emergence:** FIREABLE persistence + ablation. Refuse
  EMERGENCE-as-electron from PASS alone.

---

## Corpus sweep (STEP-0)

| Prior | Finding |
|---|---|
| LOOP GAP doctrine | Mass = zero-drive remanence; CVR-SET under drive ≠ mass |
| `loop_gap_harness` rank 4 | Carrier exists; REMANENCE-LANDED never |
| #215 / spice-cvr | IMPOSED-LATCH retract |
| #655 D2 | Persist fail → A-WEAKENED; G-PERSIST → remanence first |
| A1–A3 | Orthogonal medium-continuation kit |
| R2 ferrite prereg | FROZEN; bench not run — optional parallel only |

**VERDICT: authorized-open** under G-PERSIST. Thin discriminator missing as a
post-ruling freeze; carrier already named.

---

## Target (one sentence)

On fixed \(N\), fire `loop_gap_harness` rank 4 so that **zero-drive persistence**
(P11) either lands with memristive-ON and dies under memristive-OFF (candidate
constitutive remanence), or fails honestly — without imposed latch and without
opening node-mint.

---

## Analytic expectations (mandatory numbers)

### Battery (frozen)

Reuse harness defaults unless noted:

- `rank_target = 4`
- `P11_E_PERSIST_MIN = 0.85`
- `P11_A_PERSIST_MIN = 0.80` (\(\phi\) persist)
- Quiet window: pinned `DEFAULT_QUIET_MULT` (existing harness)
- Primary seed: `photon_lock` + bulk density ON (same class as #655 D2 smoke), \(N\) as harness default for rank-4 smoke (declare exact \(N\) in result; do not retune floors)

### Primary observables

\[
E_{\rm persist},\quad \phi_{\rm persist},\quad {\tt rank4\_pass}
\]

**PASS bar (remanence candidate):**  
\(E_{\rm persist}\ge 0.85\) AND \(\phi_{\rm persist}\ge 0.80\) AND `rank4_pass`  
with memristive saturation **ON**.

### Ablations (mandatory)

| Ablation | Expectation if remanence is real Level-2 |
|---|---|
| Memristive OFF | Persist **fails** (below floor) or rank4_pass false |
| \(\Omega_{\rm freeze}\) OFF | Must **not** be required for PASS (IC ≠ loop) |
| Explicit latch clamp \(S=\min(S,S_{\rm latched})\) | Sabotage arm: if this alone “passes,” bin **IMPOSED-LATCH** |

### Entailed-branch check (Step 3.10)

- Cardinality \(N^3\) invariant on fixed mesh is **ENTAILED** — not a remanence bin.  
- P11 floors are **fireable**.  
- “Latch ON ⇒ persist PASS” is **DEMONSTRATED install**, not adjudicated remanence.

---

## Frozen bins (enforce)

| Bin | Label | Criterion |
|---|---|---|
| **(i)** | **REMANENCE-CANDIDATE** | Memristive-ON clears P11; memristive-OFF fails P11; latch sabotage does **not** count as PASS; Ω-OFF still allows the ON path (or Ω-OFF also passes — IC not required) |
| **(ii)** | **OPERATOR-SET-ONLY** | Structure / CVR-like set under drive or short quiet, but P11 fails at full quiet (prior landscape: \(E\sim 0.71$–\(0.82\)) |
| **(iii)** | **IMPOSED-LATCH** | Persistence appears only when an explicit ratchet/latch is present; memristive-OFF irrelevant because latch carries the state |
| **(iv)** | **HARNESS-FAIL** | Battery cannot run / carrier broken / non-finite observables |

**Default expectation:** (ii) or prior-like fail — REMANENCE-LANDED has never cleared.  
Bin (i) is **allowed** but must survive ablations.

Flags (non-enforcing): R2 ferrite bench; exact \(N\); seed-mode variants.

---

## Out of scope

- Node-mint / `genesis_v{N}` / graph-growth / soft-select (B)  
- Claiming electron manufacture / SM particle creation  
- Equating A2 \(\Omega_{\rm freeze}\) with remanence  
- Silent floor retune to force (i)  
- Fourth engine / srs v18+  
- Merging HOLD stacks without Grant  

---

## Deliverables after this freeze push

1. This FROZEN prereg (this commit, pushed first).  
2. Charter doc (analysis) on follow-on commit if not already present.  
3. Later: thin driver wrapping `run_loop_gap_probe` rank-4 + ablations + result — **HOLD PR, no merge**.

---

## Physical / EE one-liner (for the result narrative)

Drive the saturable medium, remove the drive, ask whether anything ferrite-like
remains — and kill the claim if it only remains because you clamped \(S\) by hand.

---

## AMENDMENT 2026-07-12 (dated — frozen body above is BYTE-UNTOUCHED; x40-pattern amendment, legitimate and timely because NO driver exists yet)

**Why this is a legitimate amendment, not a goalpost move.** This follows the **x40 pattern**: the frozen prereg body above is left **byte-for-byte unchanged** and these repairs are appended as a **dated amendment section below it**. The amendment is **legitimate and timely because NO remanence driver / harness-fire code exists yet** — nothing has been measured against these bins, so converting an *unexecutable* gate into a *fireable* one **before any number is generated** strengthens the prereg rather than moving goalposts on a result. Adversarial review (#662) confirmed two MAJOR gaps, resolved here **before the driver fires**: (R7) the frozen ablation table mandates knobs the declared carrier does not expose; (R8) \(N\) is left ambiguous.

### R7 — make the mandated ablations FIREABLE before any driver runs

**Verified defect (grep-confirmed this session).** The frozen §"Ablations (mandatory)" table mandates (a) an **\(\Omega_{\rm freeze}\)-OFF** arm and (b) an explicit **latch clamp \(S=\min(S,S_{\rm latched})\) sabotage** arm. The declared Rule-14 carrier is `VacuumEngine3D` via `loop_gap_harness` rank 4 (`run_loop_gap_probe`, `src/ave/core/loop_gap_harness.py`).

- `run_loop_gap_probe` exposes `impedance_on`, `converter_on`, `memristive_on`, `bulk_density_on`, `bulk_seed`, `a_lock`, `n_drive_mult`, `n_quiet_mult`, `seed_mode`, `N`, `amp`, `front_target`, `fast` — and **NO \(\Omega_{\rm freeze}\) toggle** and **NO latch clamp**.
- \(\Omega_{\rm freeze}\) (`omega_freeze_ic`) exists **only in the FROZEN srs engine** `src/ave/core/chiral_lattice_v10.py:65,163,181` — a **different engine** the carrier never instantiates.
- The latch clamp `S = min(S, S_latched)` exists **only in the retracted-#215** `src/ave/solvers/spice_cvr_loop.py:170` (auditor-adjudicated IMPOSED-LATCH, PR #215) — also a different engine.

**No gate may remain frozen-but-unfireable.** Per-arm resolution:

**Arm (a) — \(\Omega_{\rm freeze}\)-OFF → ROUTE (ii): re-scope to an executable IC-control on knobs the carrier HAS.** \(\Omega_{\rm freeze}\) is an initial condition of the frozen srs engine, not the carrier; the carrier **never applies it**, so the arm as written is vacuous (building a toggle for a fool-mode that cannot occur on the carrier is theater, not a detector). The carrier's genuine analogue of the same fool-mode — *persistence baked into the initial data rather than written by driving through yield* — is detected on **existing carrier knobs**: run the **`heal_zero_seed` arm** (`amp=0.0`, `seed_mode="pair"`, already a `loop_gap_battery` arm) and/or a **no-drive control** (`n_drive_mult→0` at the same seed). If \(E_{\rm persist}\) is unchanged whether or not the medium was driven through yield, the "memory" was in the IC, not written by the drive ⇒ **IC-fool, not constitutive** — the identical verdict the \(\Omega_{\rm freeze}\)-OFF arm was meant to render, now on knobs the carrier actually exposes.

**Arm (b) — latch-clamp sabotage → ROUTE (i): BUILD a harness-level latch-clamp option (engine untouched) with its own P11 receipt, BEFORE the driver runs.** The sabotage arm is a **positive control** — it must demonstrate that IF a latch is imposed, a fake PASS results — so the ability to *impose* the latch must exist to run it. Build a **harness-level** `latch_clamp: bool` (+ `s_latched` threshold) option in `loop_gap_harness` (`run_loop_gap_probe` applies `S = min(S, S_latched)` as a **harness-side post-step clamp**; **`VacuumEngine3D` untouched**), added under **test-infra discipline with its own P11 receipt** (a `src/tests/test_loop_gap_harness.py` case asserting the clamp reproduces the #215 IMPOSED-LATCH signature) **before** the remanence driver runs. **Plus** the executable *imposed-latch-vs-emergent* distinguisher on THIS carrier: an imposed latch **(1) survives the existing `memristive_OFF` arm** (the clamp carries state independent of the Level-2 lag) **and (2) fails the R6 energy-ledger audit** (nonzero sub-yield per-cycle dissipation / unlicensed state change), whereas emergent Level-2-(a) remanence **dies under `memristive_OFF`** and shows **zero sub-yield dissipation**. On-carrier distinguisher: `{memristive_OFF survival}` ∧ `{sub-yield dissipation > ledger tol}` ⇒ **IMPOSED-LATCH / IMPOSED-LEAK**, not remanence.

### R8 — pin \(N\)

**Verified ambiguity.** The frozen body leaves \(N\) as "harness default"; the carrier default is `N=14` (`run_loop_gap_probe` signature) while the **#655 D2 same-class smoke ran N=10**.

**Resolution (minimal honest option): PIN \(N=10\).** Reason (one line): pin \(N=10\) so this remanence re-fire is **directly comparable to the #655 D2 banked negative it is motivated by** (same-class smoke). The P11 floors (`P11_E_PERSIST_MIN=0.85`, `P11_A_PERSIST_MIN=0.80`) stay **fixed** — no per-\(N\) retune. Any later \(N\)-sweep inherits a **SAME-FLOORS rule** (floors fixed across the sweep; declare exact \(N\) per run; no floor retune to force bin (i)).

### Amendment bin addition (composes with the frozen bins)

| Bin | Label | Criterion |
|---|---|---|
| **(v)** | **IMPOSED-LEAK** | A bin-(i)-shaped PASS whose **sub-yield per-cycle dissipation is nonzero** (energy-ledger audit, charter §Ax3 reconciliation (iii) / repair R6) — the retired Ax3 leak re-imported; **not** REMANENCE-CANDIDATE. Distinct from (iii) IMPOSED-LATCH (a hand-clamped ratchet); (v) is a smuggled sub-yield \(R\). |

Frozen bins (i)–(iv) above are **unchanged**. This amendment only: (a) makes arms (a)/(b) fireable (route ii / route i respectively), (b) pins \(N=10\) with a SAME-FLOORS rule, (c) adds bin (v). The frozen body is byte-untouched.
