# ORCHESTRATION HANDOFF — Vacuum-Impedance Probe (feasibility-first derivation arc)

**Created:** 2026-06-22 · **Role:** orchestration session · **Posture:** refute-by-default, feasibility-gated

---

## ⚠ SUPERSEDED-IN-PART / DEPENDENT — read this first (added 2026-06-23)

A second, **better-grounded** brief now exists: **`_orchestration/2026-06-23_vacuum-impedance-probe-primitive-handoff.md`** (from the Cleave-01 session, red-teamed). **Read it first.** It corrects framing errors in *this* brief and supplies the canonical anchors this brief told you to go find. Specifically:

- **DO NOT use the "high-Z / category-fix" framing below.** The corrected design axis is **`Re(Z_probe)/Z_channel → 0` in READ-mode**, with a **READ-vs-MEASURE** mode split (this brief lacks the split). `|Z|` is a proxy that fails for any lossy high-`|Z|` probe. (Ax3-lossless ⇒ Re(Z) is the energy-back-action budget; note reactive Im(Z) still detunes the mode — a separate, calibratable systematic.)
- **DO NOT use this brief's "dilatational/pressure drive for bulk."** AVE's confined-bulk boundary is a **SHORT** (Z_bulk→0, Γ=−1, pressure *node*), and `Γ_flow = −Γ_pressure` flips which field you null. The bulk-SHORT-vs-rigid config is an **open physics question for Grant** (§5 of the primitive brief) — do not pre-decide it.
- **The canonical anchors already exist** — `def-gv1net` (graded vacuum impedance network), the three-impedance law (file:line in the primitive brief), `def-cf1srf`, the loaded-Q / matched-port lexicon. Build on them; don't re-grep blind.
- **The load-bearing node for THIS feasibility arc is `def-tk1xfm`** (the EM↔mechanical TKI-transformer) — `status:proposed`, carries an *"identity-by-translation NOT a derivation"* ceiling. **Phase A reframes accordingly:** the feasibility question is **not** "invent a channel-selective transducer" but **"what is `def-tk1xfm`'s status/ceiling, and do you need cross-channel coupling at all, or do you probe each channel in its native domain?"** (the fleet table shows GW-echo already probes Z_bulk mechanically — no EM transducer). A channel-selective probe is most likely **MEASURE-mode / Axiom-4**, not the READ-mode "minimize Re(Z)" instrument.

**Sequencing:** the primitive brief's canonicalization should land FIRST (it's the foundation, extends `def-gv1net`). This feasibility arc is DOWNSTREAM of it and should be re-scoped against the canonized leaf before launch. Everything below stands only as the *original feasibility-gate intent*; the framing is superseded by the primitive brief.

---

## 0. What this session is

You are running an **orchestration session** to derive whether AVE can build a **channel-selective vacuum-impedance probe** — and, only if feasibility clears, to scope its parameters. You spawn sub-agents / workflows; you do not hand-build hardware. The single most important thing: **this is feasibility-first, parameters-gated.** Do not skip to designing probe numbers. Read §3 before doing anything.

You have **no memory of the originating conversation.** Everything you need is below. Verify every corpus pointer with grep before relying on it (file:line drift is real).

---

## 1. Context — AVE and the impedance-network reframe

AVE (Applied Vacuum Engineering) models the vacuum as a **real, compressible, lossless-reactive elastic medium** — a discrete lattice with pitch `ℓ_node = ℏ/(m_e c)` (the reduced Compton length). Every observable is a *substrate excitation*. AVE **forces FORMS** (the structural shapes of laws) but **imports VALUES** (dimensionful calibration constants are echoes, not derivations). The AVE-distinct, make-or-break content lives in the **forward predictions**.

The reframe this probe lives inside: the vacuum is a **multi-grade impedance network** with **three characteristic-impedance channels**:

- **Z_EM = Z₀ ≈ 377 Ω** — transverse electromagnetic (the textbook channel; QED's projection).
- **Z_shear** — deviatoric / micro-rotational (Cosserat) channel. Carries gravitational-wave-class shear and the spin/charge winding.
- **Z_bulk** — dilatational / **longitudinal-scalar** channel. This is the "3" / **V-sector**: the Heaviside/Gibbs-excised scalar grade that QED deletes. It is *physical* in AVE, not Gauss-removable.

Grep the canonical leaf for this network (search `manuscript/ave-kb/**` for the multi-grade / vacuum-circuit / graded-impedance leaf; it carries the per-channel impedance definitions and the chiral-circulator coupling `H_couple`). Confirm the three impedances and their provenance before citing magnitudes.

Relevant constants (verify in `src/ave/core/constants.py`): `L_NODE`, `C_0`, `OMEGA_C = C_0/L_NODE ≈ 7.76e20 rad/s` (with `ħ·OMEGA_C = m_e c² = 511 keV`), `Z_0`, `B_SNAP`.

---

## 2. The task — the channel-selective vacuum-impedance probe

**The originating analogy (correct, but watch the category fix):** an oscilloscope has high input impedance so it samples a voltage without *loading* the circuit. The AVE analog is **not** "a high vacuum impedance" — the vacuum's channel impedances are **fixed by the medium** (you can't pick Z₀ the way you pick a 10 MΩ scope input; for a propagating wave the probe is *matched* to Z₀ by construction). What you engineer is the **probe's coupling**: a transducer that **couples selectively to one channel (Z_shear or Z_bulk) while *rejecting* the loud EM channel (Z_EM)** — so you can read a longitudinal/shear vacuum effect without it being swamped by electromagnetic response.

That channel-selective transducer is the **missing instrument** for the longitudinal/V-sector and shear tests — the AVE-distinct measurement territory that has no off-the-shelf analog. *That* is what makes this worth a derivation arc.

**Explicitly out of scope (do NOT reinvent):**
- The **EM-channel probe** for the birefringence prediction is a standard **high-finesse optical cavity** (HIBEF / cavity-QED). Low AVE-instrumentation novelty — don't redesign known optical metrology.
- The **cRIO/Cleave electrical measurement chain** (the DC–40 kHz in-hand bench, the `C_eff(V)` saturation-onset experiment, the `Z_in ≫ Z_DUT` non-loading spec) is an **EM-channel** instrument and belongs with the **Cleave bench design**, not this probe arc. If you find yourself designing the cRIO chain, you've drifted — flag it and stop.

---

## 3. The disciplined sequencing — READ THIS BEFORE ACTING

**The prerequisite that is easy to skip:** the channel where a *novel* probe is needed (shear / bulk) currently has **no derived, bankable target observable** with a known amplitude; the channel that *has* a bankable target (EM / birefringence-coefficient) uses standard optical probes. **Designing probe parameters for an underived target is picking numbers in a vacuum** — the exact "design-the-test-before-deriving-the-prediction" anti-pattern AVE discipline forbids.

So the arc is strictly staged:

### Phase A — coupling-feasibility theory (this session's core; NON-BLOCKED)
The question: **can a physical transducer couple to the shear or bulk vacuum channel with rejection of the EM channel — and if so, how efficiently?** Derive:
- The **coupling mechanism**: what physical structure / drive / boundary couples energy into Z_shear vs Z_bulk rather than Z_EM? (Substrate-native: micro-rotation drive for shear, dilatational/pressure drive for bulk — derive from the channel constitutive relations, don't assert.)
- The **coupling efficiency** (how much of the applied drive lands in the target channel).
- The **EM-rejection ratio** (how strongly the EM channel is suppressed — the analog of common-mode rejection).
This phase is a **hard gate**: if channel-selective coupling is physically hopeless or hopelessly inefficient (e.g., the channels are not separately drivable at the bench, or any real transducer dumps ≥99% into EM), **the probe is dead — report that as a clean negative and stop.** A one-session negative is a win.

### Phase B — probe parameters (GATED; do NOT start until both clear)
Proceed only if **(a)** Phase A says coupling is feasible **AND (b)** a bankable target observable in that channel exists with a derived amplitude (this likely requires a *separate* target-derivation effort — flag it as a dependency, do not fabricate a target). Then spec: sensitivity, bandwidth, coupling geometry, noise floor vs target amplitude, readout chain.

### Phase C — canonicalization (GATED on adversarial verify-pass)
Stub → **Vol 9 experimental-prints** chapter for the hardware, with a **Vol 4 (falsifiable-predictions) pointer** from the prediction it tests. **Stub/scope only until the gates clear — do not write finished chapter prose for an underived target.** Confirm the exact chapter slot by grepping the Vol-9 / Vol-4 chapter structure before scaffolding.

---

## 4. Standing gate — refute-by-default (applies to every claim and every landing)

Every claim passes a **refute-by-default adversarial audit**, not a verify-pass. **Deflate-then-document:** if the gate refutes or deflates, canonicalize the *deflated honest* version (or nothing), never the exciting one — and surface the deflation plainly.

- **Symmetric-standard lens:** guard BOTH directions — the SM/QED-prior direction *and* the in-an-AVE-favorable-conversation direction. Before flagging an AVE limitation as a comedown, ask whether standard physics has the same gap and gets a pass; before celebrating an AVE win, ask whether you're being seduced by the favorable frame.
- **Over-rescue tripwire:** if the analysis concludes "the probe is feasible and wonderful," be suspicious — the honest prior is that **channel-selective vacuum coupling at the bench is HARD**. An audit that finds chords/wins everywhere has a too-permissive lens; throw the lens out, don't celebrate.

---

## 5. Priority context (for your strategic awareness)

This arc **competes for budget with weak-C slope resolution** — the 4-OOM lever that governs whether the directional/dispersion/LIV chord family is bankable at all (the photon (q·ℓ_node)⁴ slope-4-vs-slope-2 question; grep `k4-bloch-dispersion-quartic.md`). Phase A (feasibility) is cheap and non-blocked — run it; it gates-or-greenlights the whole probe arc for one session's cost. Phase B genuinely waits on a bankable target. Keep the arc honest about this: it is a *forward, ambitious* instrument, not a near-term bench.

---

## 6. Constraints — STANDING, non-negotiable

- **PURE-AVE-CORPUS:** never mention investors, funds, interviews, external pitches, or any non-physics external context anywhere — not in docs, code, commits, or branch names. Translate any external rationale into pure physics/engineering before writing.
- **`main` is PROTECTED:** Grant merges via reviewed PR. **NEVER self-merge.**
- **Self-isolate git-mutating work** in a `/tmp` worktree off `origin/main` (the workspace root is not a git repo; `AVE-Core` is one level down — `cd` into it or target it explicitly).
- **NEVER put the substring `build` in a worktree or branch name** (trips `predictions_manifest_validator.py:136`).
- **Flag-don't-fix:** surface contradictions with verbatim file:line evidence; let Grant's physical intuition resolve framing-level physics questions. Ask Grant first on framing-level calls (inline prose questions with bulleted options — NOT multi-choice UI).
- **Substrate-first for every number:** derive from the canonical chain or honestly tag as engineering-choice; never default to SM / EE / textbook convention.
- **Verify-before-cite** + grep-completeness second-pattern cross-check (the auditor is not exempt). RESOLVED/status stamps are verify-don't-trust.

---

## 7. Deliverables

1. **Phase-A feasibility verdict:** `FEASIBLE` / `INFEASIBLE` / `CONDITIONAL`, with the derived coupling mechanism, coupling efficiency, and EM-rejection ratio — each refute-by-default audited, each with file:line provenance.
2. If `FEASIBLE`/`CONDITIONAL`: a scoped **Phase-B plan** naming the target-observable dependency and the gates.
3. A **research doc** in `research/` (dated, scratch) capturing the derivation; and **only if a gate clears**, a Vol-9 stub (via PR, Grant merges).
4. **All forks surfaced to Grant** as inline prose with bulleted options.

## 8. Success criteria

A defensible, adversarially-audited answer to **"can we build a channel-selective vacuum-impedance probe, and what would it take?"** — explicitly *not* a hardware spec for an underived target. A clean `INFEASIBLE` is a full success. The failure mode to avoid is a confident parameter sheet built on a phantom signal.
