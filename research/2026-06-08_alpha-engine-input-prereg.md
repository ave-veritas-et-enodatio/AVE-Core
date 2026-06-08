# Prereg: α in engine dynamics vs snap-genesis instrumentation

**Status:** FROZEN PREREG (retroactive — driver/adjudication completed 2026-06-08).  
**Parent:** `2026-06-07_theorem-31-alpha-identity-audit.md`, `2026-06-08_native-electron-propagation-adjudication.md`  
**Adjudication:** `research/2026-06-08_alpha-engine-input-adjudication.md`  
**Corpus-grep:** ave-corpus-grep session 2026-06-08 (α yield vs gate default vs snap contract)

---

## §0 Question

Before automating electron snap genesis, must we **remove α from the engine** (`constants.py`, `VacuumEngine3D`, `PairNucleationGate`)?

Distinguish:

- **Structural √α** — `V_YIELD = √α · V_SNAP` (Axiom-4 operating point)
- **Dynamics α-input** — `PairNucleationGate` default `δ_lock = ω_drive · α`

---

## §1 Physical picture

1. Electron LC tank at **Γ = −1 TIR** leaks reactively per cycle; corpus gives **Q = 1/α** at wall (Theorem 3.1′).
2. **V_YIELD** is substrate yield geometry (√α strain), not a forward-test dial.
3. **PairNucleationGate C2** imports CODATA α as autoresonant lock tolerance — justified in pair-rupture theory (doc 54_ §7) but smuggles α into dynamics if used with default constructor.
4. Forward snap drivers should use **measured ε = 1−Γ²** or explicit `delta_lock_fraction`, never default gate.
5. Calibration crux is **rest vs wall** and **projection vs native** lane split — not presence of √α in yield definition.

---

## §2 Corpus state (grep)

| Topic | State | Key prior work |
|-------|-------|----------------|
| `V_YIELD = √α·V_SNAP` | **Closed** | `constants.py:387`, `divergence-test-substrate-map.md` INVARIANT-C1 |
| `Q = 1/α` at TIR | **Closed** | `theorem-3-1-q-factor.md:38` |
| Gate `δ_lock = ω·α` | **Closed** (corpus-derived default) | `vacuum_engine.py:1264-1275`, doc 54_ §7 |
| Native Γ ceiling | **Closed** (C1 revised) | `2026-06-07_native-k4-gamma-ceiling-prereg.md` Outcome A |
| Projection vs native split | **Partial** | `projection_native_gamma_gate.py`, `LANE_SPLIT_CONFIRMED` |

---

## §3 Predictions

**Primary (Outcome A):** **Do not remove** √α from `V_YIELD` / engine yield path. Snap genesis proceeds with `axiom_4_enabled=True` (inherits structural yield). Isolate `PairNucleationGate` default from forward drivers.

**Alternative (Outcome B):** Removing all α references from engine improves snap TIR or ε→α match — would imply calibration crux was α-contamination, not lane/coordinate issue.

**Null (Outcome C):** Snap cannot reach TIR without `delta_lock_fraction=ALPHA` in dynamics — would force gate-default α as necessary input.

**Falsifier:** If `electron_genesis_snap.py` with `alpha_used_as_input: false` fails TIR while identical run with `PairNucleationGate(delta_lock_fraction=ALPHA)` registered as observer succeeds — α-default would be load-bearing for snap (contradicts primary).

---

## §4 Protocol

Adjudication doc + snap driver contract:

- KEEP: `V_YIELD`, `_V_YIELD_FRAC`, regime map references
- ISOLATE: no `PairNucleationGate()` default in snap path; `delta_lock` from measured ε or `explicit_delta_lock_fraction=0.02`
- Drivers: `alpha_used_as_input: false`; `ALPHA_COLD` post-hoc only

No engine code changes required before snap test.

---

## §5 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | Keep √α yield; isolate gate default; snap reaches TIR without α dynamics input |
| B | Engine α removal improves results (not observed) |
| C | Snap requires gate-default α (not observed) |

---

## §6 Result

**Driver:** `src/scripts/vol_1_foundations/electron_genesis_snap.py` (hybrid/position modes)  
**JSON:** `src/scripts/vol_1_foundations/_output/electron_genesis_snap_results.json`

## §7 Adjudication

**Verdict: Outcome A — `NO_ENGINE_ALPHA_REMOVAL`**

| Check | Result |
|-------|--------|
| √α yield kept | `axiom_4_enabled=True`; no constants surgery |
| Gate default isolated | `_FIELD_HELPER` uses `delta_lock_fraction=0.02`; never registered as observer |
| Snap TIR without α input | position/hybrid: `SNAP_TRAP_PINNED_WITH_TIR`, Γ_post ≈ −0.994, ε ≈ 0.0126 |
| α removal unnecessary | Identical outcome to `native_electron_reseed_handoff` at trap_amp=1.5 |

**Corpus alignment:** Matches `theorem-3-1-q-factor.md` (α is derived leak at TIR, not snap trigger) and doc 54_ (autoresonant δ_lock is pair-rupture mechanism, separate from discrete wall replace).

**Do not:** Remove `sqrt(ALPHA)` from `V_YIELD`. **Do:** Document gate-default override discipline for all forward genesis drivers.

**Next:** Optional engine hygiene (gate docstring note); ε proxy study (ε ≈ 1.7× α at native TIR).
