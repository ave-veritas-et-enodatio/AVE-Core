# Genesis planning — node-birth fork (A vs B)

**Status:** PHASE-2 DRIVERS LANDED · **REBINNED → per-fidelity SPLIT: smoke (i) A-SUPPORTED (2/3), production (ii) A-WEAKENED (0/3); ruling-grade DEFERRED to Grant**  
**Branch (drivers):** `analysis/genesis-node-birth-d14` · **Prereg:** merged via #654 on `main`  
**Class:** architecture / fork freeze. **No chord. No new `genesis_v{N}`. No graph-growth engine.**  
**Discipline:** `ave-loop-gap-harness-discipline` v1.1 — advance ranks / freeze forks, do not open srs v18+ or a fourth engine without Grant + firewall justification.

**Phase-0 ruling (plan ratification 2026-07-12):** **KEEP-BOTH** — design fireable discriminators (D1–D4) before ruling (A) or (B) or building graph-growth. Do not assert (B); do not bank fixed-mesh runs as “genesis” without a claim-class tag.

**Phase-2 adjudication (2026-07-12, SUPERSEDED):** D1 PASS + D2 FAIL (single `photon_lock`/`fast=True` leg) + D3 not-entailed + D4 SKIPPED → bin (ii) A-WEAKENED.

**Phase-2 RE-adjudication (2026-07-12, adversarial-review repair R1–R8):** the D2
battery was a **battery-of-one** on the seed mode most expected to fail. Broadened
to all three landed seed modes at the banked config, run at BOTH fidelities ⇒
**per-fidelity SPLIT**:
- **SMOKE** (`n_quiet=12`): **2/3 persist** (`pair` E=0.8639/φ=7.7295, `graded_a0`
  E=0.8544/φ=1.9636; `photon_lock` FAILs — φ-channel dead) ⇒ **bin (i) A-SUPPORTED**.
- **PRODUCTION** (`n_quiet=52`): **0/3 persist** — every mode's E falls below the
  0.85 floor (`pair`→0.6929, `graded_a0`→0.6764, `photon_lock`→0.7750) ⇒ **bin (ii)
  A-WEAKENED**. Smoke PASS is a short-drive-off-window artifact; production is the
  more faithful read and **vindicates the original (ii) direction** on the broadened
  battery.

Ruling-grade banking (which fidelity is authoritative) **DEFERRED to Grant** — the
frozen bins name no fidelity authority and ruling the fork is not the implementer
lane's call. `make verify` PASS. Result (per-fidelity + KEEP-BOTH quote of the old
(ii) text): `research/2026-07-12_genesis-node-birth-discriminator_result.md`. Still
does **not** rule (A) or (B); R10 still open.

---

## 0 · One-paragraph framing

Grant's contention: **dynamic transduction of mechanical stress on the K4 lattice that genesises the electron feels tied to new-node genesis and a dynamically changing universe lattice.** That contention splits what the LOOP GAP ranks have treated as one problem ("form + keep an electron on the medium") into two:

| Fork | Claim | Engine implication |
|---|---|---|
| **(A) Reconfiguration** | Electron = topological / saturation pattern on a **fixed** graph (N constant). Node birth is cosmological-only. | Continue ranks 1–4 on existing platforms; node-creation stays cosmology-front. |
| **(B) Node birth** | Electron genesis **requires** N→N+1 (or bond birth / site mint) at Compton scale; cosmology is the integrated history of that process. | Fixed-mesh "electron forms" runs answer the **wrong question**; need a graph-growth primitive (new capability — Grant + firewall required). |

Capability map already lists **node-creation** as an empty column on every engine (`engine-capability-map.md` §1, §5–§6). This plan does **not** assume (B) is true — it freezes the fork so the next work cannot silently answer (A) while claiming genesis.

---

## 1 · What is already banked (do not re-litigate)

- **mass = A1** (#260 / #311) — untouched.
- **Bulk self-trap on native stencil** — Mode-III DISPERSE / Cartesian artifact (2026-06-24); surviving localizer leans **Γ=−1 boundary / cavity**, not autonomous bulk stress-well.
- **LOOP GAP ranks 1–4** on VacuumEngine3D harness — platform rule stands; srs v9–v17 frozen.
- **R10 remanence** — anhysteretic `S(A)` cannot keep; imposed latch ≠ chord. **Rider (default):** treat as **independent constitutive gap** under (A); under (B) *hypothesis-only* that retention is a micro-proxy of lasting DOF mint — not engine law until discriminators run.
- **#86 back-reaction** — reversible self-gravitation landed; **F6 / irreversible depletion / a(t) evolver** still UNBUILT (cosmology Stage-4).
- **Categorization guards (#653)** — ledger / claim-class / slot refusal — available on this branch for tagging any future gate as CERTIFICATION vs FIREABLE.

---

## 2 · How (A)/(B) sits relative to LOOP GAP ranks

```mermaid
flowchart TD
  fork["KEEP-BOTH Phase-0"]
  A["A: fixed-N reconfiguration"]
  B["B: N to N+1 node birth"]
  ranks["LOOP GAP ranks 1-4 existing harness"]
  r10["R10 remanence still open under A"]
  cosm["Cosmology node birth H_inf latent heat G"]
  graph["NEW graph-growth primitive Grant+firewall"]
  disc["Discriminator battery D1-D4 BEFORE any new engine"]

  fork --> disc
  disc --> A
  disc --> B
  A --> ranks
  ranks --> r10
  A --> cosm
  B --> graph
  B -.->|"hypothesis: micro-proxy of same DOF"| r10
```

**Hypothesis to test (not assert):** under (B), **R10 retention** may be the soft micro-form of node birth (keeping a lasting DOF), not a separate ferrite latch on a frozen mesh. Under (A), R10 stays constitutive-loop-only and node birth stays cosmological.

---

## 3 · Work phases

### Phase 0 — Fork freeze (THIS DOC) · DONE (KEEP-BOTH)

| bin | meaning |
|---|---|
| **(A)-ruled** | Electron genesis work proceeds on fixed-N engines; node-creation stays cosmology + Stage-4 F6 track |
| **(B)-ruled** | Fixed-mesh genesis batteries are reclassified as **pattern/cage probes only**; true genesis gated on a graph-growth charter |
| **KEEP-BOTH** | **AUTHORIZED** — discriminator suite (D1–D4) can kill (A) or (B) before any fourth engine |

### Phase 1 — Discriminator prereg · DONE (#654)

Frozen prereg: `research/2026-07-12_genesis-node-birth-discriminator_prereg_FROZEN.md` (freeze-by-push before drivers).

| ID | Discriminator | Fireable content |
|---|---|---|
| **D1** | DOF conservation | Existing cage/genesis runs: invariant node/bond count ⇒ class-(A)-capable only; tag `ClaimClass` — never bank as genesis under (B) |
| **D2** | Fixed-N persistence | A1 stress → Γ=−1 cavity + winding surviving drive-off on fixed N ⇒ supports (A) for *pattern*; R10 still open |
| **D3** | Necessity of (B) | Analytic/corpus: saturable Cosserat + ℓ_node can confine without cardinality change; Kelvin gap ≠ entail (B) |
| **D4** | Cosmology OOM fence | If (B), Compton mint rate must not contradict `H_∞` / packing / latent-heat by absurd OOMs |

Use `#653` pairing discipline: Gauss-style install identities ≠ genesis.

### Phase 2 — Drivers · DONE · REBINNED (per-fidelity split; ruling-grade deferred)

Driver + tests + result on `analysis/genesis-node-birth-d14`. Still **no** `genesis_v{N}` / srs v18+ / fourth engine.

| ID | outcome (post-repair R1–R8) |
|---|---|
| D1 | PASS (2 measured crystal/ME + 1 structural harness; certification_entailed; R3) |
| D2 | **SMOKE 2/3 persist** (`pair`, `graded_a0` PASS; `photon_lock` FAIL — φ dead, R5) ⇒ (i). **PRODUCTION 0/3 persist** (all E below floor) ⇒ (ii). Window-dependent (R1) |
| D3 | PASS not-entailed |
| D4 | SKIPPED-WITH-REASON |
| **bin** | **per-fidelity SPLIT: smoke (i) A-SUPPORTED, production (ii) A-WEAKENED**; ruling-grade DEFERRED to Grant. Original **(ii)** vindicated at production (KEEP-BOTH quote in result doc) |

**Adjudicator halt (R2):** `adjudicate_bin` now returns OUT-OF-BIN
`D1_CARDINALITY_VIOLATION_HALT` for any `d1_ok=False` (a fork-(B) cardinality
mutation halts for Grant, no longer mis-binned as A-WEAKENED).

### Phase 3 — Engine path (BLOCKED until Grant rules A/B or deepens D2)

- **Forbidden until (A) or (B) ruled:** new `chiral_lattice_v18+`, new `genesis_v{N}`, silent "node birth" flags inside VacuumEngine3D.
- **Allowed under (A):** rank advancement + R10 honest attempts on existing platforms; optional deeper D2 cavity battery.
- **Allowed under (B) after explicit Grant ruling:** one Grant-signed graph-growth spike with ablation battery (create-node OFF must null).
- **bin (ii) does not authorize graph-growth by itself.**

---

## 4 · Out of scope (this planning arc)

- Merging / retuning **#652 X44** (bin iii; separate escalation).
- U6 / A7 / α Class-B ceiling.
- Claiming electron mass = energy cost of one node mint.
- Equating Schwinger pair production on a fixed grid with node birth.

---

## 5 · Merge / rebase notes

1. **Merge #653** when CI greens (categorization).  
2. Rebase this branch onto `main`.  
3. **Hold #652** until Grant picks X44 §7 escalation.  
4. Planning PR = orchestration + index pointer + frozen prereg — **no engine**. Drivers = later PR.
