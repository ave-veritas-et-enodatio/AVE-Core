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
