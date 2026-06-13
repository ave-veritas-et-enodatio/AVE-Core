# ORCHESTRATOR DIRECTIVE — Fresh D-stack adjudication (2026-06-12)

**Status:** ACTIVE — Grant-ratified auditor framing (2026-06-12); supersedes agent-self-adjudicated D1/D2/D4/D5 rows for **execution**  
**Lane:** orchestrator / implementor executes; auditor verifies  
**Persistence:** mirror in `AUDITOR_STATE.md` §E (orchestrator-maintained)  
**Rule:** Rule-12 only — preserve body, dated addenda; no silent overwrites

> **Grant confirm queue (blocking ratification block only):** D4 — which inter-channel knob did you mean (α boundary vs GAP-C)? Bulk boundary — K finite vs K→0 at melt?

---

## D5 — DROP Ω_freeze from local-genesis runs (category error)

**Ruling:** Ω_freeze is a **cosmological substrate IC** (sets enantiomorph / $u_0^*$ / α / G at crystallization; Ω=0 ⇒ non-viable lattice). A single electron forms in an **already-frozen** lattice — handedness is already in srs / $\kappa_{\mathrm{chiral}}$ geometry. Re-imposing it locally double-counts the freeze.

**Evidence (local genesis non-gating):**
- `research/2026-06-12_genesis-v10-cvr-convergence_result.md` §Ω-free (still CVR-SET)
- `research/2026-06-12_genesis-program-status.md` + `research/2026-06-12_genesis-parameter-provenance-audit.md` (v15 cosmic deposit ~$10^{-40}$ of yield, logged-not-injected)
- `research/2026-06-11_chiral-vacuum-reactor-framing.md:530` (non-collapse noted)

**Actions:**
| ID | Task | Acceptance |
|:---|:---|:---|
| D5-A | Demote Ω_freeze to **logged control only** in all **local-genesis** preregs | No load-bearing arm / gate on electron harness |
| D5-B | Rule-12 amend `research/2026-06-11_chiral-vacuum-reactor-framing.md:525` | D5 scoped to substrate-genesis only; dated strike |

**Harness alignment:** LOOP GAP plan already lists Ω_freeze as ablation-only (`_orchestration/2026-06-12_loop-gap-orchestration-plan.md` §2 D5).

---

## D4 — SPLIT the name collision ($\chi_{\mathrm{shock}}$ ≠ inter-channel coupling)

**Finding:** D4's “χ” is **`chi_shock`** = snap **dissipation fraction** (KE-above-yield → mass ledger, per channel), NOT inter-channel coupling.

**Anchors:** `research/2026-06-12_genesis-v10-cvr-convergence_prereg_FROZEN.md`; `src/ave/core/sonic_horizon_flow.py:52`

**Actions:**
| ID | Task | Acceptance |
|:---|:---|:---|
| D4-A | Relabel decision: **“chi_shock dissipation fraction, equal default”** | Stops reading as “channel coupling” |
| D4-B | Register **inter-channel transformer** separately | Own decision item: **α** (`research/2026-06-11_alpha-boundary-energy_prereg.md`) OR **GAP-C** (`research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md`) — currently OFF; spurious-pump caught at `research/2026-06-10_genesis-v6-pump-isolation_result.md` |
| D4-C | **Grant voice:** which knob was intended | One-sentence ratification in PR body |

**Note:** Bulk↔shear ratio √2 from K=2G is already derived (“the 1.41”).

---

## D2 — DEFER kernel choice; persistence-at-the-cusp first

**Finding:** LOOP GAP is real (doctrine §1; substrate-hysteresis-index) but remanence is **Rank 4 (last)**. Winding doesn't survive drive-off at Rank 2–3 (v16 $E_{\mathrm{persist}}=0.71<0.85$). v10 “snap non-load-bearing” was **post-rupture** — silent on snap-at-the-cusp.

**Actions:**
| ID | Task | Acceptance |
|:---|:---|:---|
| D2-A | **Do NOT** bake snap into v10+ as load-bearing yet | Harness rank ≤3 σ-only default |
| D2-B | P11 zero-drive persistence at **cusp** ($A_{\mathrm{yield}}=\sqrt{\alpha}$, NOT post-rupture) | `research/2026-06-12_genesis-v11-loop-closure_prereg_DRAFT.md` §70–81 |
| D2-C | Loop-ablation: motion-lock vs constitutive remanence | v5 seeded-snap certified path |
| D2-D | Schedule **R2 ferrite bench** | `research/2026-06-12_constitutive-loop-r2-prereg_FROZEN.md` |
| D2-E | Rule-12 repair `research/2026-06-11_chiral-vacuum-reactor-framing.md:495` | Struck σ-only D2 + dated; v10 vindicated at post-rupture depth |

---

## D1 — DON'T migrate; price the asserted cost

**Finding:** “srs migration invalidates α + Lorentz” (`_orchestration/2026-06-07_lattice-net-resolution.md:24`) is **UNVERIFIED**. α from knot geometry; Lorentz from cubic symmetry (srs I4₁3₂ also has). R3: srs chirality structural; diamond decoration ~0.057%.

**Actions:**
| ID | Task | Acceptance |
|:---|:---|:---|
| D1-A | Keep **diamond = computational substrate, srs = structural-chirality instrument** — label **PROVISIONAL** | Matches `research/2026-06-12_lattice-d1-adjudication-memo.md` |
| D1-B | Reconcile stale **D1-FINAL / CLOSED** banner | `research/2026-06-11_genesis-v9-chiral-lattice_design.md:18-21` → SESSION-RECORD |
| D1-C | **α-on-srs re-derivation check** (THE UNLOCK) | Does $4\pi^3+\pi^2+\pi$ survive on non-bipartite trivalent net? Bipartite-2 via knot double-cover? |

---

## Cross-cutting repairs

| ID | Task | Owner |
|:---|:---|:---|
| X-1 | **Bulk-leaf Rule-12:** demote `bulk-impedance-at-saturation-boundary.md` Γ_bulk=−1 to **provisional pending K-call** | corpus PR |
| X-2 | **Provenance:** one **Grant-voiced ratification block** for this D-stack (replaces agent-self-adjudicated record) | orchestration PR |
| X-3 | **PR discipline:** decisions via reviewed PRs (not self-merge batch) | workflow |

**Grant physics call (bulk):** at melt (G→0), does **K stay finite or vanish**? K≡2G_vac rigid at all operating points vs cold-equilibrium-only (`cauchy-implosion-resolution.md:14`).

---

## H1 — CI hygiene (🔴)

**Finding:** PR #211 “archive” was documentation-only. `chiral_lattice_v11..v17.py` + `genesis_v18_coupled.py` still tracked under `src/ave/core/`. Six `test_chiral_lattice_v12..v17.py` files exist (default CI **already ignores** via `src/tests/conftest.py` `collect_ignore_glob` — verify before claiming 30m timeout cause).

**Actions:**
| ID | Task | Acceptance |
|:---|:---|:---|
| H1-A | `git mv` v11–v17 core modules + genesis drivers to `src/ave/_archive/genesis/` (or equivalent) | History preserved; not on active import path |
| H1-B | Move matching tests to archive or keep opt-in `make test-genesis` only | Default `make test` unchanged |
| H1-C | Fold `_orchestration/2026-06-12_loop-gap-v11..v15-charter.md` into archive record | DAG + harness plan supersede |

**Keep live:** `loop_gap_harness.py`, `VacuumEngine3D`, bedrock keepers.

---

## Execution order (orchestrator)

| Priority | Slice | Branch suggestion |
|:---:|:---|:---|
| P0 | X-2 ratification block + this doc + `index.md` reconciliation | `analysis/2026-06-12-d-stack-adjudication` |
| P0 | D5-A/B, D4-A, D2-E, D1-B Rule-12 corpus strikes | same PR (corpus-only) |
| P1 | H1 archive move + import path audit | separate PR (engine hygiene) |
| P1 | D1-C α-on-srs check (implementor) | `analysis/alpha-on-srs-check` |
| P2 | D2-B P11-at-cusp on harness rank 4 | harness Phase G |
| P2 | X-1 bulk-leaf provisional demotion | corpus PR |
| — | D4-B inter-channel decision | **blocked on Grant** |
| — | X-1 K-call | **blocked on Grant** |

**Parallel with LOOP GAP:** C′ PR (`analysis/2026-06-13-loop-gap-scalar-grade`) is independent; merge order: C′ implementor PR first OR D-stack orchestration PR first — no file overlap if scoped.

---

## Grant ratification block (template — voice before merge)

```text
Grant ratifies fresh D-stack (2026-06-12 auditor directive):
- D5: Ω_freeze DROP from local genesis — YES / NO
- D4-A: chi_shock relabel — YES / NO
- D4-C: inter-channel knob = [ α boundary | GAP-C | other: ___ ]
- D2: defer snap load-bearing; P11-at-cusp first — YES / NO
- D1: don't migrate; queue α-on-srs check — YES / NO
- Bulk K-call: [ K finite | K→0 ] at melt
Date: ___
```

---

## Change log

| Date | Change |
|:---|:---|
| 2026-06-13 | Initial doc — orchestrator intake from auditor directive |
