# DISPATCH BRIEF — x40: the 10-ring closure transient (the derivable stick/slip split)

**Lane:** implementer, worktree `analysis/x40-ring-closure-transient` off `origin/main` @ `7fedf5c3`.
**Board slot:** task #38 on the 2026-07-10 fresh-session slate — "the ring-quantization transient (a kill-test for the u₀* triple-convergence); discriminating test, cheap."
**Walked picture:** `research/2026-07-10_impedance-register-walks_framing.md` §(b) — the nucleation walk WRITES a frozen bias; this lane makes the write mechanism a derivable number.

---

## SECTOR HEADER (binding, before any standard-physics word)

- **MODE:** formation-epoch transient — a single nucleation event at the growth front, modeled at the moment one new bond closes onto the settled lattice.
- **REGIME:** lossless. Linear TL abstraction at fixed operating point; the Axiom-4 kernel is NOT engaged (any constant S is absorbed into Z₀; kernel-independence of the split at this abstraction is a stated model scope, not a claim about the saturated front).
- **SECTOR:** winding-vs-wave partition. The trapped DC mesh circulation is GRAPH-register content (the winding/counting bin of the four-bin taxonomy); the AC transient is on-line wave content radiated to the bath. Do not cross-wire: the mesh circulation is a 2-cochain quantity (phase-space-coordinate-check — measure mesh circulation, never a per-node Cartesian proxy).
- **VOCABULARY:** *reactive / trapped / radiated* — NEVER "loss." The stub's Re(Z) is the bath port (energy carried away down a semi-infinite lossless line), not dissipation.

## THE PHYSICS (walked, ratified — implement, don't re-adjudicate)

Each nucleation at the growth front = a switch closure connecting a new bond carrying inherited circulation i(0) = I_parent to the settled lattice. LOSSLESS split:
1. **DC loop current** trapped in the smallest closed mesh the new bond completes (frozen winding → u₀* accretion), and
2. **AC transient** radiated into the semi-infinite Z₀ line (→ the bath).

## STEP 1 — LOAD-BEARING PREMISE (verified by orchestrator this session; re-verify in worktree before citing)

srs = the (10,3)-a net with 10-gon smallest rings (girth 10). Canon sites, grep-confirmed at `origin/main` 7fedf5c3:
- `src/ave/topological/srs_dec.py:129-131` — "GIRTH — the srs net's girth. EXTERNAL MATHEMATICS (srs = (10,3)-a, girth-10; ...) minimal cycles ARE the 10-rings"; `enumerate_girth_faces()` enumerates them algorithmically. **Caveat encoded there: an L=2 PBC supercell folds girth-10 rings into spurious 8-rings; L≥3 required.**
- `manuscript/ave-kb/common/engine-capability-map.md:176` — "the true Sunada-K4 / Laves / (10,3)-a / srs net (degree-3, chiral, I4₁32)"; `:211`, `:268` — DEC 2-complex on girth-10 faces, ∂∂=0 int64-exact.
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md:38` — "srs (10,3)-a / Wyckoff-8a motif."
- Also check `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md` (the #609 canon) for any ring-size statement.

External-literature anchor for (10,3)-a (Wells nomenclature): if the corpus carries a citable ref, cite it; else mark **[CITE-PENDING: srs/(10,3)-a girth-10, Wells-class net-taxonomy ref]** — do not fabricate.

## CANONICAL POINTERS (verified this session)

- **Bare z=3 junction:** `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md` §1 (`clm-v3port`, merged PR #630): Γ = (2−z)/z = −1/3, |Γ|² = 1/9, "lossless — not a 'loss'"; the reciprocal 3-port floor |S₁₁| ≥ 1/3.
- **Canonical per-bond scales:** `src/ave/core/constants.py:310-311` — L_CELL = Z₀/ω_C = μ₀·ℓ_node; C_CELL = 1/(Z₀·ω_C) = ε₀·ℓ_node. **These are cited for FRAMING ONLY — see the anti-install gate. The driver works in dimensionless units and imports none of them.** The load-bearing identity: on a TL, L_bond = L′ℓ = μ₀ℓ = Z₀·(ℓ/c) = Z₀τ_bond exactly — so the split fraction is scale-free by construction; only ring topology (and optionally geometry) survives.
- **u₀* accretion (downstream consumer, cite-don't-canonize):** `manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md:62-67` — freeze-in as bond over-bracing u₀*; `trampoline-framework.md:91-119`.
- **Prior-art inventory (clean):** `ring_bondframe_probe.py` (bond-frame strain of a traveling wave — different object), `electron_halfflux_*` (texture holonomy — different object), `srs_dec.py` (REUSE for ring enumeration). No prior closure-transient work found.

## FROZEN ANALYTIC EXPECTATIONS (derive-first content — reproduce these derivations in the prereg, then freeze BEFORE any driver code)

**E1 — the Λ-conservation theorem (the DC trap).** For lossless telegrapher bonds, d/dt ∫₀^ℓ L′i dx = v(0) − v(ℓ) per bond. Summed around the closed 10-mesh with single-valued node voltages, the RHS telescopes to zero ⇒ the ring flux linkage Λ = Σₖ∫L′iₖdx is EXACTLY conserved from the instant of closure, independent of what flows out the stubs. With IC i = I_parent uniform on the closing bond (v ≡ 0, all else quiescent): Λ(0) = L_bond·I_parent. Final state (all AC radiated) = uniform DC loop current: I_dc = Λ(0)/L_loop = I_parent·(L_bond/L_loop).

**E2 — the DC fraction form vs L_loop : Z₀τ.** Trapped energy fraction f_E = (½L_loop I_dc²)/(½L_bond I_parent²) = **L_bond/L_loop = Z₀τ_bond/L_loop**. Substrate-native TLM (no mutual terms exist in the circuit graph): L_loop = N·L_bond with N = 10 ⇒ **f_E = f_I = 1/10 exactly; radiated fraction 9/10**. Flux/winding banks WHOLE (Λ conserved 100%); the split is in energy and current, not in flux.

**E3 — the bare-junction Γ = −1/3 leg (the AC ring-down).** Each ring node is exactly the canonical z=3 junction (ring-continuation + one dangling semi-infinite branch per node — z=3 gives exactly one stub per ring node, clean): per node passage the voltage wave reflects −1/3, transmits 2/3 to each downstream port, forward power retention (2/3)² = 4/9 → per-lap forward retention ~(4/9)¹⁰ ≈ 3.0e-4. Freeze the −1/3 scattering coefficient as the mechanism (gate on it in sabotage); characterize (don't over-freeze) the multi-path envelope.

**E4 — the Neumann-mutual second axis (KEEP-BOTH; genuinely open number).** The field-honest L_loop includes geometric mutual terms between ring bonds: L_loop = N·L_self + Σ_{j≠k} M_jk, M_jk = (μ₀/4π)∮ⱼ∮ₖ dlⱼ·dlₖ/|rⱼ−rₖ| (radius-free for j≠k), computed over the ACTUAL skew 10-ring geometry pulled from the srs net coordinates, with consistent ring orientation (signed). Normalize m_jk = M_jk/(μ₀ℓ) ⇒ f_E^(geom) = 1/(N + Σ_{j≠k} m_jk). **Footing declaration (mandatory, mixed-footing honesty):** the self-term footing is the canonical TLM per-bond μ₀ℓ (substrate-native), NOT the divergent filament self-inductance — the geometric axis mixes a TLM self-term with Neumann mutual terms and must be reported as a SEPARATE characterization axis with this footing declared, never folded into the headline. Headline number = the substrate-native TLM 1/10. Σm_jk is the one genuinely unknown number in this lane — report it to full precision.

## THE COMPUTATION (driver)

Exact synchronous TLM bounce-stepping (no numerical dispersion, machine-exact energy bookkeeping):
- 10 ring bonds, each an ideal TL segment (Z₀ = 1, delay τ = 1, dimensionless units ℓ = 1).
- At each ring node: the 3-port equal-Z₀ shunt junction S-matrix (S_jj = −1/3, S_jk = 2/3) — the stub port is a matched semi-infinite line: whatever enters never returns; accumulate its energy per tick (the radiated ledger).
- IC: uniform current I_parent = 1 on the closing bond (equal counter-propagating wave decomposition), v = 0; all other bonds quiescent.
- Evolve ≥ 300 ticks. Track: Λ(t) (mesh flux linkage), ring energy E_ring(t), radiated cumulative E_rad(t), per-bond DC current profile.
- **N is DERIVED, not hardcoded:** enumerate rings via `ave.topological.srs_dec.enumerate_girth_faces` on an L≥3 net; assert the minimal-cycle length == 10 and take N from it. Pull one actual ring's node coordinates for E4.

## DELIVERABLES

(a) **The trapped/radiated split as a NUMBER** — headline substrate-native f_E = 1/10 (demonstrated live-fire against the frozen theorem), plus the geometric second-axis f_E^(geom) = 1/(10 + Σm_jk) with Σm_jk reported. Inputs: L′, C′ (through Z₀, τ — which cancel), ring topology, and (E4 only) ring geometry. Nothing else.
(b) **The flux-quantization statement:** trapping occurs ONLY at discrete ring-COMPLETION events — an open chain has no mesh, no conserved Λ (KVL doesn't telescope on an open path; a current transient on an unclosed front fully radiates); the instant the 10th bond closes, a conserved mesh quantity is MINTED with ΔΛ = L_bond·i(0) banked whole. Discreteness of trapping = discreteness of ring completions. This is the u₀*-accretion write mechanism at circuit level (cite the freeze-in canon as downstream consumer; DO NOT canonize).
(c) **Frozen-to-radiated fraction of parent angular momentum per nucleation:** of the circulation donated to the closing bond, fraction L_bond/L_loop (= 1/10 TLM) freezes as persistent mesh circulation; (N−1)/N of the donated energy radiates. Angular momentum rides linearly on circulation at fixed ring geometry ⇒ same fraction of the donated leg's contribution. The absolute per-nucleation ΔL requires I_parent from the parent-soliton model — name it as the input owed by the D-IV capture spec (task #34), do not derive it here.
(d) **Open follow-on (named, not attempted):** front-roughness / ring-completion statistics — the i(0) distribution across nucleation events, correlated completions sharing bonds, and the real-lattice branch input impedance vs the matched-stub bath abstraction.

## GATES + SABOTAGE (P11 — every gate proven able to FAIL)

- **G-A (Λ-theorem):** |Λ(t) − Λ(0)|/Λ(0) < 1e-12 at all ticks.
- **G-B (plateau):** |I_dc/I_parent − L_bond/L_loop| < 1e-6 at t = 300τ (TLM: target 0.1).
- **G-C (energy ledger, lossless):** |E_ring(t) + E_rad(t) − E₀|/E₀ < 1e-12 at all ticks.
- **G-D (ring count derived):** N from `enumerate_girth_faces` on L≥3, assert == 10; FAIL if enumeration unavailable or ≠ 10.
- **G-E (ANTI-INSTALL, machine-checked):** an AST/import scan of the driver module: any import or use of OMEGA_C, M_E, HBAR, ALPHA, L_NODE, or ANY dimensional constant from `ave.core.constants` = automatic FAIL. The driver is dimensionless end-to-end.
- **Sabotage receipts (run, record, and show the FAIL):**
  - **S1:** series resistance planted in one ring bond ⇒ G-A and G-B must FIRE (Λ decays, plateau undershoots).
  - **S2:** planted anti-install violation — a variant importing OMEGA_C to set a scale ⇒ G-E must FIRE.
  - **S3:** drop one stub's outflow from the radiated ledger ⇒ G-C must FIRE.

## P10 — ENTAILED-BRANCH CHECK (state this honestly in prereg AND result)

Within the frozen TL model, f_E = 1/10 is a THEOREM (E1/E2) — the live-fire DEMONSTRATES an entailed branch; it does not adjudicate an open fork. State which branches are genuinely fireable: (i) the energy ledger failing (model inconsistency), (ii) the plateau missing the theorem (implementation gap → artifact hunt, not physics), (iii) the E4 Σm_jk magnitude (genuinely unknown number), (iv) the ring-down envelope vs the Γ=−1/3 mechanism. The kill-test value for the u₀* triple-convergence rhyme is CONDITIONAL: this lane demonstrates the WRITE mechanism is coherent and derivable in the ratified bath model — it does not prove the bias is real. Classify per consistency-vs-emergence in the result (this is a consistency demonstration + one computed characterization, NOT an emergence test).

## DISCIPLINE (binding)

1. **Freeze-by-push (P9):** commit 1 = this brief; commit 2 = `research/2026-07-10_x40-ring-closure-transient_prereg_FROZEN.md` AS ITS OWN COMMIT; push BOTH to origin BEFORE any driver code exists in any commit. The freeze is claimed by push ordering (gh-api-auditable).
2. **Prereg content:** sector header; the four frozen expectations E1–E4 with the derivations reproduced; gates G-A..G-E with tolerances; sabotage plan S1–S3; the P10 entailed-branch statement; the deliverable list; the branch table (what result → what verdict).
3. **KEEP-BOTH:** the TLM axis and the Neumann-geometry axis are two axes — never redefine one into the other.
4. **verify-before-cite:** every file:line above re-grepped in the worktree before it lands in a tracked doc.
5. **Figures:** WHITE via `ave.viz.style.apply`, Okabe-Ito, honest axes+units (dimensionless: state "units of τ", "units of I_parent"), legend outside data, no on-figure title. One figure minimum: Λ(t) + I_mesh(t) transient with the frozen 1/10 plateau line + energy ledger inset or second panel.
6. **Result doc:** `research/2026-07-10_x40-ring-closure-transient_result.md` — headline number first; prereg-vs-shipped diff section (any deviation listed, even forced); gate receipts incl. sabotage FAIL outputs verbatim; consistency-vs-emergence classification; deliverables (a)–(d); the open follow-on.
7. **Driver:** `src/scripts/vol_1_foundations/x40_ring_closure_transient.py` + test `src/tests/test_x40_ring_closure.py` (gates as pytest, sabotage as parametrized planted-violation cases asserting FAIL). Run `make verify` in the worktree before the final push (worktree-aware validation is live per repo CLAUDE.md).
8. **Pure corpus.** No KB edits (canonical propagation is a gated follow-on). FLAG-DON'T-FIX: anything found contradicting canon (e.g., a canon site asserting a different smallest-ring count) → verbatim evidence in the result doc's FLAGS section, no silent fix.
9. **Commits:** incremental (skeleton-first, one section per commit — no single large writes). Trailer on every commit: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
10. **PR:** title exactly `[DO-NOT-MERGE][REVIEW: pending-orchestrator] x40: 10-ring closure transient — the derivable stick/slip split`; body = summary + gate receipts + the P10 statement + the follow-on list; `gh pr create --base main`. Do NOT merge. Report back: split number(s), Σm_jk, branch fired, PR number, any FLAGS.
