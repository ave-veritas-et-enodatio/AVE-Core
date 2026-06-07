# Electron-genesis — next-steps orchestration scope (post-2026-06-06)

**Executable plan for the next session.** Companion to `2026-06-06_session-handoff.md` (state) — this is the *forward plan*. The genesis arc is paused at a clean, well-understood decision point; resume by taking **D1** (below), not by re-deriving.

## §0 The state in one paragraph (what we actually learned)
The electron-genesis chain is **rupture (saturation `Γ=−1` wall) → blocked linear KE shatters into transverse curl → parity splits LH+RH → `(2,3)` on the A-B bond → confined standing wave** (`pair-production-axiom-derivation.md`). The corpus (§5) names three engine gaps for the `(2,3)`; two are real: **no dynamical bond state** (the `(2,3)` is a `(V_inc,V_ref)` phasor *on the bond*; the engine tracks node ports — it can't carry it dynamically) and **no per-node `Ω_node(A²)`** (C2 lock). The Option-D **impose** is already coded (`PairNucleationGate`, `vacuum_engine.py:1172` — Kelvin's vortex atom); the `phase5_*` harness ran the persistence test → **MODE III dissolution at step ~11** ("coupling-depth issue"). **Critical late finding:** the (II) "confinement" win was an **imposed `Γ=−1` clamp** (`use_impedance_boundary`, a stiff spring on the Cosserat-ω, `cosserat_field_3d.py:779,870`) — **NOT** the canonical self-created wall. The engine has energy-saturation (collapses, Arm C) + a *diagnostic* Γ-from-S + the imposed clamp; **the canonical emergent wall — the saturation driving the wave to reflect off its own impedance — is not implemented in the dynamics anywhere.**

---

## §1 OPEN DECISION D1 (gates everything below — Grant) — the canonical-wall location
**Where does "the particle weaves its own mirror" live in the engine?** My read: **modulate the K4-TLM bond impedances by `S(A)`** so a saturating bond → `Z_bond→0` and the **TLM scatter+connect natively reflects** off the mismatch (`Γ→−1` falls out of the scatter coefficients — no clamp, no energy term, no collapse), matching Vol 4 Ch 1's `C_eff→∞, Z→0, Γ=−1` *at the bond*. Alternative reads: the wall lives at the **node** (Cosserat done as a TLM), or elsewhere. **Resume here: confirm the location, then W1.**

---

## §2 Phase W1 — build the canonical emergent wall (gated on D1)
- **W1.0 — understand first (do NOT skip):** read the `k4_tlm.py` scatter+connect path — does it scatter? how are bond impedances set? where would `S(A)` enter? (The wall-clamp discovery came from finally reading code; honor the lesson.)
- **W1.1 — build:** make K4 bond impedance `S(A)`-dependent → native scatter reflects off saturated bonds → emergent `Γ=−1`. **Retire** the `use_impedance_boundary` Cosserat clamp (KEEP-BOTH, default OFF, `make verify` byte-identical).
- **W1.2 — test:** does the emergent wall **confine** a photon (reflect off its own saturated bonds) where (a) the energy-saturation *collapses* (Arm C) and (b) the clamp *pumps*? Three-way control: energy-OFF / clamp / emergent.
- **Outcomes:** (I) emergent wall confines, no pumping → canonical wall validated → W2. (II) confines partly → localize. (III) doesn't confine → the wall lives elsewhere → back to D1.
- **Discipline:** `ave-prereg` (grep K4-TLM + prior scatter work first), `substrate-native-check` (the scatter is wave-reflection, NOT energy-min/clamp), understand-before-dispatch.

## §3 Phase W2 — Option-D impose under the emergent wall (gated on W1=I)
- Run the existing **`PairNucleationGate`** impose (LH/RH Beltrami pair) + the **`phase5`** persistence harness, **under the W1 emergent wall** (not the clamp, not the energy term). + couple the V/ω sectors (audit §9).
- **Test:** does the imposed pair **persist past step ~11** (where MODE III dissolved under the collapsing energy-saturation) when held by the *field's own mirror*?
- **Outcomes:** (I) persists → the canonical wall was the missing "coupling depth"; Option-D impose + emergent wall = a stable e⁻e⁺ pair (Kelvin topological protection at lattice scale) → genesis closes at the **impose** level. (II) partial. (III) still dissolves → dissolution is independent of confinement → the §5 bond-state gap is the cause → W3/path-a.

## §4 Phase W3 — full `(2,3)` emergence vs impose (the a/b/c fork; gated on W2 — DECISION D2)
- **If W2=(I):** genesis is closed at the *impose* level. Genuine *(2,3) emergence* (not impose) still needs the §5 **dynamical-bond-state** (GAP 1) + **per-node `Ω_node(A²)`** (GAP 2) — a substantial engine build (**path a**). **D2:** build the bond-state engine for emergence, or **scope-closed (path c)**: "rupture-mechanism + canonical wall + Option-D pair-persistence validated; bond-state `(2,3)` emergence is a separate foundational engine capability."
- **If W2=(III):** path-a (the bond-state) is the only route to a stable pair, or path-c scope-closed.
- **path-a build (if taken):** a dynamical bond object carrying the `(V_inc,V_ref)` `(2,3)` phasor + per-node Duffing `Ω_node(A²)` resonance + the C1+C2+C3 nucleation rule wired to it. Corpus §5 + `STAGE6_V4_HANDOFF §9` are the spec.

## §5 Discipline carried forward (this session's hard-won lessons)
1. **`ave-prereg` BEFORE dispatch** — the arc re-derived ~6 builds of existing work (`PairNucleationGate`, `phase5` MODE-III, §5 gaps). Grep prior work + the canonical leaf first, always.
2. **Understand the engine before scoping** — read the actual code (the clamp vs emergent-wall confusion cost the whole (II)→path-(b) detour).
3. **`consistency-vs-emergence`** — Option-D is an **IMPOSE / stability test**, NOT emergence; genuine emergence is W3/path-a. Frame honestly in every result doc.
4. **KEEP-BOTH** — new mechanisms default-OFF, byte-identical `make verify`.
5. **flag-don't-fix** — surface (the clamp, the §5 gaps); Grant adjudicates the path.

## §6 Artifacts + reuse map (don't rebuild these)
- `vacuum_engine.py:1172` `PairNucleationGate` (Option-D impose) + `AutoresonantCWSource` + `NodeResonanceObserver` (C2 machinery, GAP-2 partial).
- `phase5_pair_nucleation.py` / `phase5_topological_pair_injection.py` (+ MODE-III result) — the persistence harness.
- `cosserat_field_3d.py`: `use_impedance_boundary` clamp (to RETIRE/KEEP-BOTH); native Op3/Op14 Γ-from-S (`:343,367,486`, currently diagnostic — to be made *load-bearing* in W1).
- `git stash` in `genesis2-wt`: coupled-port + implicit-integrator WIP (reference).
- Branches: `analysis/2026-06-06-saturation-tir-moving-boundary` ((II) + the work) is the active genesis branch; the genesis arms A/B/C + scope branches are held.

## §7 Resume checklist (next session, in order)
1. Read this + the handoff + the path-(b) interrupted state. 2. **Take D1** (wall location). 3. W1.0 understand `k4_tlm.py` → W1.1 build emergent wall → W1.2 test. 4. W2 impose-under-emergent-wall persistence. 5. **D2** (a/b/c) → W3. 6. Land PR #106 + PR the integrator branch when ready; merge PR #107.
