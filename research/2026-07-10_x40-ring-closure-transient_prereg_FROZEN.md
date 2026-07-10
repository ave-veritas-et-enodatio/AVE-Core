# PRE-REGISTRATION (FROZEN) — x40: the 10-ring closure transient

**Status:** FROZEN by push (P9). Frozen BEFORE any driver code exists in any commit.
**Lane:** implementer, worktree `analysis/x40-ring-closure-transient` off `origin/main` @ `7fedf5c3`.
**Brief:** `_orchestration/2026-07-10_x40-ring-closure-brief.md` (commit 1 of this branch).
**Board slot:** task #38 — the ring-quantization transient; a conditional kill-test for the u₀* triple-convergence rhyme; discriminating, cheap.
**Walked picture:** `research/2026-07-10_impedance-register-walks_framing.md` §(b) — the nucleation walk WRITES a frozen bias; this lane makes the write mechanism a derivable number.

This prereg reproduces the four frozen analytic expectations E1–E4 with their derivations, the gates G-A..G-E with tolerances, the sabotage plan S1–S3, the P10 entailed-branch statement, the deliverable list, and the result→verdict branch table. Nothing here is adjudicated after the driver runs; deviations are logged verbatim in the result doc's prereg-vs-shipped diff.

---

## SECTOR HEADER (binding — before any standard-physics word)

- **MODE:** formation-epoch transient — a single nucleation event at the growth front, modeled at the moment one new bond closes onto the settled lattice.
- **REGIME:** lossless. Linear TL abstraction at a fixed operating point; the Axiom-4 kernel is NOT engaged (any constant saturation S is absorbed into Z₀; kernel-independence of the split at this abstraction is a STATED MODEL SCOPE, not a claim about the saturated front).
- **SECTOR:** winding-vs-wave partition. The trapped DC mesh circulation is GRAPH-register content (the winding/counting bin of the four-bin taxonomy); the AC transient is on-line wave content radiated to the bath. The mesh circulation is a 2-cochain quantity — it is measured as the loop flux linkage Λ = Σ over ring bonds, NEVER as a per-node Cartesian proxy (phase-space-coordinate-check).
- **VOCABULARY:** *reactive / trapped / radiated* — NEVER "loss." Each ring node's stub is the bath port (energy carried away down a semi-infinite lossless line), not dissipation. Re(Z_stub)=Z₀ is a matched radiating port, not a resistor.

## LOAD-BEARING PREMISE (re-verified in worktree before freeze)

srs = the (10,3)-a net with 10-gon smallest rings (girth 10). Verified at worktree HEAD:

- `src/ave/topological/srs_dec.py:132` — `SRS_GIRTH: int = 10`; :129-136 "GIRTH — the srs net's girth. EXTERNAL MATHEMATICS (srs = (10,3)-a, girth-10 …). The minimal cycles ARE the 10-rings"; :138 `MIN_SRS_L: int = 3` with the encoded caveat "at L=2 the periodic wrap folds the girth-10 rings into spurious 8-rings … L>=3 recovers the true girth-10 everywhere." `enumerate_girth_faces()` (:140) enumerates them algorithmically.
- `manuscript/ave-kb/common/engine-capability-map.md:176` — "**srs-z3** — the true Sunada-K4 / Laves / (10,3)-a / srs net (degree-3, chiral, $I4_1 32$ …)"; §8b.4 — DEC 2-complex on girth-10 faces, ∂₁∂₂=0 int64-exact.
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md:38` — "srs $(10,3)$-a / Wyckoff-8a motif."
- `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md` (the #609 canon) — checked: carries NO smallest-ring-count statement (band-structure/TL-map leaf; no `ring`/`girth`/`(10,3)` occurrence). Non-contradicting; recorded, no FLAG.

**External-literature anchor (corpus-carried, not fabricated):** the (10,3)-a / girth-10 geometry is EXTERNAL MATHEMATICS asserted by the executable keepers, source class cited in `src/ave/core/chiral_lattice.py:20-23` — *Sunada, "Crystals that nature might miss creating," Notices AMS 2008; RCSR `srs`; Wells (10,3)-a.*

**N is DERIVED, not hardcoded:** the driver builds an L=3 srs net (`build_srs_net`), enumerates rings (`enumerate_girth_faces`), asserts the minimal-cycle length == 10, and takes N from it. Live probe at freeze time: L=3 → 216 nodes, 324 bonds, 324 faces, all cycles length 10; bond lengths all 1.0; adjacent bond direction dot u_j·u_{j+1}=0.5.

## CANONICAL POINTERS (re-verified this session; FRAMING cites only)

- **Bare z=3 junction:** `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md` §1 (`clm-v3port`, merged PR #630): Γ = (2−z)/z = −1/3, |Γ|² = 1/9, "lossless … not a 'loss'"; the reciprocal 3-port floor |S₁₁| ≥ 1/3 (Pozar §7.1 class).
- **Canonical per-bond scales (FRAMING ONLY — see anti-install gate G-E):** `src/ave/core/constants.py:310-311` — `L_CELL = Z_0/OMEGA_C` (= μ₀·ℓ_node), `C_CELL = 1/(Z_0·OMEGA_C)` (= ε₀·ℓ_node). The driver imports NONE of these; it works in dimensionless units. Load-bearing identity: on a TL, L_bond = L′ℓ = μ₀ℓ = Z₀·(ℓ/c) = Z₀·τ_bond exactly — so the split fraction is scale-free by construction; only ring topology (and optionally geometry) survives.
- **u₀* accretion (downstream consumer — cite-don't-canonize):** `manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md:62-67` (freeze-in as bond over-bracing u₀*), `trampoline-framework.md:91-119`.

---

## THE PHYSICS (walked, ratified — implemented, not re-adjudicated)

Each nucleation at the growth front = a switch closure connecting a new bond carrying inherited circulation i(0) = I_parent to the settled lattice. LOSSLESS split into: (1) a **DC loop current** trapped in the smallest closed mesh the new bond completes (frozen winding → u₀* accretion), and (2) an **AC transient** radiated into the semi-infinite Z₀ stub lines (→ the bath).

## FROZEN ANALYTIC EXPECTATIONS (E1–E4)

### E1 — the Λ-conservation theorem (the DC trap)

For lossless telegrapher bonds, ∂/∂t(L′i) = −∂v/∂x ⇒ d/dt ∫₀^ℓ L′i dx = v(0) − v(ℓ) per bond. Summed around the closed 10-mesh with single-valued node voltages, the RHS telescopes:

    dΛ/dt = Σ_bonds [v(start) − v(end)] = Σ_k (v_k − v_{k+1}) = 0   (cyclic)

⇒ the ring flux linkage **Λ = Σ_k ∫ L′i_k dx is EXACTLY conserved from the instant of closure**, independent of what flows out the stubs (the stub outflow is a branch current at each node; it does not enter the ring-loop KVL telescope). With IC i = I_parent uniform on the closing bond (v ≡ 0, all else quiescent): **Λ(0) = L_bond·I_parent**. Final state (all AC radiated) = uniform DC loop current with v ≡ 0: **I_dc = Λ(0)/L_loop = I_parent·(L_bond/L_loop)**.

### E2 — the DC fraction form vs L_loop : Z₀τ

Trapped energy fraction

    f_E = (½ L_loop I_dc²) / (½ L_bond I_parent²) = L_bond/L_loop = Z₀τ_bond/L_loop,

using I_dc/I_parent = L_bond/L_loop. Substrate-native TLM — the circuit graph carries NO mutual terms (each bond is an independent TL segment) ⇒ **L_loop = N·L_bond with N = 10**, hence

    ┌─────────────────────────────────────────────────────────┐
    │  f_E = f_I = 1/N = 1/10  EXACTLY  (radiated fraction 9/10) │
    └─────────────────────────────────────────────────────────┘

Flux/winding banks WHOLE (Λ conserved 100%); the split is in ENERGY and CURRENT, not in flux. (f_E = f_I here because f_E = (L_loop/L_bond)(I_dc/I_parent)² = (L_loop/L_bond)(L_bond/L_loop)² = L_bond/L_loop = f_I.)

### E3 — the bare-junction Γ = −1/3 leg (the AC ring-down)

Each ring node is exactly the canonical z=3 junction: 2 ring-continuation ports + 1 dangling semi-infinite stub (z=3 ⇒ exactly one stub per ring node, clean). Per-node voltage-wave passage: reflect Γ = −1/3, transmit 2/3 to each downstream port; forward power retention per node (2/3)² = 4/9. Per-lap forward retention ~(4/9)¹⁰ ≈ **3.03e-4**. The −1/3 scattering coefficient is FROZEN as the mechanism (gated in sabotage). The multi-path ring-down envelope is CHARACTERIZED, not over-frozen (E3 gate is qualitative: monotone-decaying radiated increment; the AC energy E_ring(t)−E_dc → 0).

### E4 — the Neumann-mutual second axis (KEEP-BOTH; genuinely open number)

The field-honest loop inductance includes geometric mutual terms between ring bonds:

    L_loop^(geom) = N·L_self + Σ_{j≠k} M_jk,
    M_jk = (μ₀/4π) ∮_j ∮_k (dl_j · dl_k)/|r_j − r_k|   (radius-free for j≠k),

computed over the ACTUAL skew 10-ring geometry pulled from the srs coordinates (`ring_coords`), with a consistent SIGNED ring orientation (all bonds in the +ring-forward direction; M_jk carries the sign of u_j·u_k). Normalize m_jk = M_jk/(μ₀ℓ) ⇒

    f_E^(geom) = 1/(N + Σ_{j≠k} m_jk).

**FOOTING DECLARATION (mandatory, mixed-footing honesty):** the self-term footing is the canonical TLM per-bond μ₀ℓ (substrate-native), NOT the divergent filament self-inductance. The geometric axis therefore MIXES a TLM self-term with Neumann mutual terms and is reported as a SEPARATE characterization axis with this footing declared — never folded into the headline. **Headline number = the substrate-native TLM 1/10.** Σ_{j≠k} m_jk (ordered-pair sum) is the one genuinely unknown number in this lane; it is reported to full precision.

**E4 computation method (frozen):** each M_jk is evaluated by reducing the double Neumann integral to a 1-D outer integral of a closed-form inner segment potential — G_k(r) = ∫₀^{L2} dt/|r − r₂(t)| has the exact asinh/log form; the outer ∫₀^{L1} ds·(u_j·u_k)·G_k(r₁(s)) is a 1-D adaptive quadrature. Adjacent bonds share a vertex ⇒ the outer integrand has an INTEGRABLE log endpoint singularity (∫ of 1/R over two segments meeting at a point converges); the singular endpoint is flagged to the quadrature. Cross-check (test): non-adjacent M_jk agrees with a 32×32 Gauss–Legendre tensor quadrature to < 1e-9.

## MODEL REALIZATION (the exact synchronous TLM the driver implements)

Dimensionless units: Z₀ = 1, per-bond delay τ = 1, length ℓ = 1 ⇒ L_bond = Z₀τ = 1, C_bond = τ/Z₀ = 1. Ten ring bonds, nodes 0..9 cyclic; bond k connects node k→node k+1. Per bond, two directed wave samples: p_k (traveling k→k+1), m_k (traveling k+1→k). Each node is the equal-Z₀ 3-port shunt (2 ring ports + 1 matched stub), S_pq = 2/n − δ_pq (n=3): S_jj = −1/3, S_jk = 2/3. Synchronous scatter+connect update:

    v_k      = (2/3)(p_{k-1} + m_k)          # node voltage = stub reflected wave (radiated)
    p_k(t+1) = v_k − m_k                       # reflected onto +ring port
    m_k(t+1) = v_{k+1} − p_k                   # reflected onto −ring port (from node k+1)
    E_rad   += Σ_k v_k²                        # stub outflow, accumulated; nothing returns

**Derived model identities (why the gates are entailed, machine-exact):**
- Per-bond current i_k = p_k − m_k; loop flux Λ = Σ_k(p_k − m_k). Λ(t+1) = Σ_k[(v_k−m_k)−(v_{k+1}−p_k)] = Σ_k(v_k−v_{k+1}) + Σ_k(p_k−m_k) = Λ(t) (telescope). **Λ conserved EXACTLY every tick** ⇒ G-A.
- The uniform circulating state p_k = A, m_k = −A (v_k = 0, no radiation) is an EXACT period-1 fixed point; i_k = 2A = I_dc, Λ = 20A = N·I_dc ⇒ **I_dc = Λ/N = 1/10** ⇒ G-B. All other modes carry v≠0 somewhere ⇒ leak into stubs ⇒ decay; the DC circulation is the unique undamped mode.
- The shunt scatter S = (2/n)J − I has eigenvalues {+1 (once), −1 (n−1 times)} ⇒ S is orthogonal (S²=I) ⇒ Σ reflected² = Σ incident² at every node ⇒ **E_ring(t) + E_rad(t) = E₀ exactly** ⇒ G-C. With E_ring = Σ_k(p_k²+m_k²).
- IC (closing bond = bond 0): p_0 = ½, m_0 = −½ (i = 1 = I_parent, v = 0); all other p,m = 0 ⇒ E₀ = ¼+¼ = ½ = ½L_bond I_parent², Λ(0) = 1 = L_bond I_parent.


---

## GATES (G-A .. G-E) with tolerances

| Gate | Statement | Tolerance |
|------|-----------|-----------|
| **G-A** (Λ-theorem) | \|Λ(t) − Λ(0)\|/\|Λ(0)\| < 1e-12 at ALL ticks | 1e-12 |
| **G-B** (plateau) | \|I_dc/I_parent − L_bond/L_loop\| < 1e-6 at t = 300τ, where I_dc = the settled uniform per-bond current; ALSO max_k\|i_k − 0.1\| < 1e-6 (profile flat) | 1e-6 |
| **G-C** (energy ledger, lossless) | \|E_ring(t) + E_rad(t) − E₀\|/E₀ < 1e-12 at ALL ticks | 1e-12 |
| **G-D** (ring count derived) | N from `enumerate_girth_faces` on L≥3, minimal cycle length == 10, N := that length; FAIL if enumeration unavailable or ≠ 10 | exact |
| **G-E** (ANTI-INSTALL, machine-checked) | AST/import scan of the driver module: any import or use of OMEGA_C, M_E, HBAR, ALPHA, L_NODE, or ANY dimensional constant from `ave.core.constants` = automatic FAIL | exact |

Note on G-B: because Λ is conserved exactly, the MEAN per-bond current is Λ/N = 0.1 at ALL ticks (trivially); the load-bearing G-B content is the PLATEAU — that the profile has become FLAT (AC drained), i.e. max_k|i_k − 0.1| < 1e-6. Both are reported.

## SABOTAGE PLAN (S1–S3) — every gate proven able to FAIL

Each planted violation is run, the FAIL is recorded verbatim in the result doc (P11: a gate that cannot fail is not a gate).

- **S1** — series resistance R>0 planted in one ring bond (a real Re on a ring line, breaking Axiom-3 lossless) ⇒ **G-A must FIRE** (Λ decays) and **G-B must FIRE** (plateau undershoots 0.1). Expected: monotone Λ decay, I_dc < 0.1.
- **S2** — planted anti-install violation: a driver variant that imports `OMEGA_C` from `ave.core.constants` to set a scale ⇒ **G-E must FIRE** (import scan flags it).
- **S3** — drop one stub's outflow from the radiated ledger (fail to accumulate v_k² for one node) ⇒ **G-C must FIRE** (E_ring + E_rad ≠ E₀; the ledger loses the dropped node's radiated energy).

## P10 — ENTAILED-BRANCH CHECK (stated honestly, pre-run)

Within the frozen TL model, f_E = 1/10 is a THEOREM (E1/E2 + the discrete telescope/fixed-point/orthogonality identities in MODEL REALIZATION). The live-fire **DEMONSTRATES an entailed branch**; it does NOT adjudicate an open fork. Genuinely fireable branches:

  (i)  the energy ledger failing (model inconsistency / bug) — G-C FIRE;
  (ii) the plateau missing the theorem (implementation gap → artifact hunt, NOT physics) — G-B FIRE;
  (iii) the E4 Σ_{j≠k} m_jk magnitude — a GENUINELY UNKNOWN number, computed here for the first time;
  (iv) the ring-down envelope vs the Γ=−1/3 mechanism — characterization, not a pass/fail fork.

The kill-test value for the u₀* triple-convergence rhyme is CONDITIONAL: this lane demonstrates the WRITE mechanism is coherent and derivable in the ratified bath model — it does NOT prove the bias is real. Per consistency-vs-emergence: this is a **CONSISTENCY demonstration + one computed CHARACTERIZATION (E4)**, NOT an emergence test. The 1/10 is a THEOREM of the model (a manifestation/consistency-class result), not an emergent CODATA-matched number.

## DELIVERABLES (a)–(d) — restated for the result

(a) The trapped/radiated split as a NUMBER: headline substrate-native f_E = 1/10 (live-fire vs the frozen theorem) + the geometric second-axis f_E^(geom) = 1/(10 + Σ_{j≠k} m_jk) with Σ_{j≠k} m_jk reported to full precision. Inputs: L′, C′ (through Z₀, τ, which cancel), ring topology, and (E4 only) ring geometry. Nothing else.
(b) The flux-quantization statement: trapping occurs ONLY at discrete ring-COMPLETION events. An open chain has no mesh, no conserved Λ (KVL does not telescope on an open path); the instant the 10th bond closes, a conserved mesh quantity is MINTED with ΔΛ = L_bond·i(0) banked whole. Discreteness of trapping = discreteness of ring completions — the u₀*-accretion write mechanism at circuit level (cite the freeze-in canon as downstream consumer; DO NOT canonize).
(c) Frozen-to-radiated fraction of parent angular momentum per nucleation: of the circulation donated to the closing bond, L_bond/L_loop (= 1/10 TLM) freezes as persistent mesh circulation; (N−1)/N = 9/10 of the donated energy radiates. Angular momentum rides linearly on circulation at fixed ring geometry ⇒ same fraction of the donated leg's contribution. The absolute per-nucleation ΔL requires I_parent from the parent-soliton model — named as the input owed by the D-IV capture spec (task #34), NOT derived here.
(d) Open follow-on (named, not attempted): front-roughness / ring-completion statistics — the i(0) distribution across nucleation events, correlated completions sharing bonds, and the real-lattice branch input impedance vs the matched-stub bath abstraction.

## RESULT → VERDICT BRANCH TABLE

| Observed result | Verdict |
|-----------------|---------|
| G-A,B,C,D,E all PASS; f_E → 1/10 at 1e-6; ledger exact | Entailed branch DEMONSTRATED; TLM split = 1/10 confirmed live-fire; consistency-class. |
| G-A or G-C FIRE (unplanted) | Model inconsistency / implementation bug — artifact hunt, NOT a physics falsification (branch i). Do NOT report a physics result until resolved. |
| G-B FIRE (unplanted), G-A & G-C pass | Plateau not reached / not flat by 300τ — extend ticks or diagnose a mode that fails to drain; implementation gap (branch ii). |
| G-D FIRE | srs ring enumeration disagrees with girth-10 canon → FLAG-DON'T-FIX with verbatim canon evidence; halt. |
| Sabotage S1/S2/S3 does NOT fire its gate | The gate is decorative, not a gate (P11 violation) — fix the gate, re-run. |
| Σ_{j≠k} m_jk computed | Report the number + f_E^(geom); this is a NEW characterization (branch iii), never merged into the headline. |

**FROZEN.** Any deviation below this line in the shipped work is logged verbatim in the result doc's prereg-vs-shipped diff.
