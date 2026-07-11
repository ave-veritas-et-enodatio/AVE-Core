# RESULT — x40: the 10-ring closure transient (the derivable stick/slip split)

**Lane:** implementer, branch `analysis/x40-ring-closure-transient`.
**Prereg (frozen + amended):** `research/2026-07-10_x40-ring-closure-transient_prereg_FROZEN.md`.
**Brief:** `_orchestration/2026-07-10_x40-ring-closure-brief.md` (+ §Addendum).
**Driver:** `src/scripts/vol_1_foundations/x40_ring_closure_transient.py`.
**Tests:** `src/tests/test_x40_ring_closure.py` (23 keepers, all pass; +3 from the adversarial-review repairs — S5, S2b, independent-BFS-girth).
**Figure:** `src/scripts/vol_1_foundations/x40_ring_closure_transient.png`.

---

## HEADLINE NUMBER (first)

At each nucleation, of the parent circulation donated to the closing bond of an
srs 10-ring, the LOSSLESS split is — substrate-native TLM, machine-exact:

    ┌───────────────────────────────────────────────────────────────────────┐
    │  TRAPPED  f_E = 1/10 = 0.1000000000000000  (persistent DC mesh current) │
    │  RADIATED       9/10 = 0.9                  (AC transient → the bath)    │
    │  Flux linkage Λ banks WHOLE (conserved 100%, drift 2.2e-16)             │
    └───────────────────────────────────────────────────────────────────────┘

The trapped 1/10 lives ENTIRELY in the **cycle-space (T-odd loop current)**; the
radiated 9/10 is the **cut-space (T-even bond-strain)** part driven into the
matched stubs. The split is scale-free by construction (only ring topology N=10
survives; L′,C′ cancel through Z₀,τ).

**Geometric second axis (KEEP-BOTH, mixed footing — NOT the headline):**

    Σ_{j≠k} m_jk = 0.6448522895896426   (ordered-pair sum, srs 10-ring, μ₀ℓ footing)
    f_E^(geom)   = 1/(10 + Σm_jk) = 0.09394212082942391
    L_loop^(geom)/(μ₀ℓ) = 10.644852289589643   (adjacent +1.2218, non-adjacent −0.5769)

Σm_jk is a GEOMETRIC INVARIANT of the srs 10-ring (ring-choice independent to
~1e-11; identical magnitude for the left enantiomorph).

**Which P10 branch fired:** branch (iii) — the E4 Σm_jk magnitude, a genuinely
UNKNOWN number, computed here for the first time (0.6448522896), plus the entailed
DEMONSTRATION (branches i/ii could NOT fire: the energy ledger and the plateau
both hit the frozen theorem at machine precision). This is a **consistency
demonstration + one computed characterization**, NOT an emergence test.

---

## PREREG-vs-SHIPPED DIFF (every deviation, even forced)

| Item | Prereg | Shipped | Note |
|------|--------|---------|------|
| Model / gates / tolerances (frozen set) + POST-REVIEW STRENGTHENING | E1–E5, G-A..G-F, S1–S4 as frozen | frozen set implemented exactly; then STRENGTHENED after review — F1 added an INDEPENDENT BFS-girth witness to G-D (+ sabotage S5); F2 name-keyed the G-E ImportFrom scan (+ sabotage S2b) | STRENGTHENING (gate fireability), NOT a physics deviation — see the ADVERSARIAL-REVIEW REPAIR LOG (F1/F2) and ORCHESTRATOR-REVIEW REPAIRS below; every headline number re-verified byte-identical, nothing moves |
| E3 "(gated in sabotage)" clause (frozen prereg:71) | "The −1/3 scattering coefficient is FROZEN as the mechanism (gated in sabotage)" | INTRA-PREREG OVER-CLAIM logged: NO shipped sabotage perturbs the node scatter S=(2/3)J−I (driver:185 hardcodes `v=(2/3)(p_left_in+m)`; S1 plants series resistance, S3 drops a ledger term — neither touches the coefficient). The −1/3 is only INDIRECTLY gated: S1/S3 fire on any energy-NON-conserving scatter, but a wrong-but-LOSSLESS coefficient would SLIP. The value is structurally FORCED — equal-Z₀ z=3 port S=(2/n)J−I, Pozar-class reciprocal 3-port floor (frozen prereg:35) — not established by a direct sabotage. | HONESTY LOG (frozen file left byte-identical). Optional S6 (a unitary-but-WRONG 3-port to make the direct gate fireable) evaluated and DECLINED as not-genuinely-cheap — see ORCHESTRATOR-REVIEW REPAIRS below. No number moves. |
| G-B plateau | mean (=Λ/N) AND flatness max\|i_k−0.1\| | both reported | as frozen |
| Figure location | "one figure minimum" | tracked at `src/scripts/vol_1_foundations/x40_ring_closure_transient.png` (repo policy: cited renders live in the tracked scripts dir, not the gitignored `_output/`) | location choice, disclosed |
| Figure content | Λ(t)+I_mesh transient + plateau + ledger | plotted the per-bond current SPREAD [min,max] (richer than a single trace) + Λ(t)/Λ₀ + plateau line; energy ledger as the second panel | faithful-plus, disclosed |
| E4 method | 1-D reduction of the Neumann double integral; Gauss cross-check <1e-9 | implemented; non-adjacent agreement 0.0e0 | no deviation |
| Amendment E5 | appended dated post-freeze (original frozen file untouched) | pushed BEFORE any cut/cycle/G-F/S4 code existed | freeze-by-push honored for the new content |

No forced SCIENTIFIC deviations to any headline number; the headline theorem was
reproduced live-fire. The two rows above the G-B row are post-review bookkeeping/
honesty deltas — a gate-fireability STRENGTHENING (F1/F2) and one logged E3
intra-prereg over-claim — and neither moves a number (all re-verified byte-identical).

---

## ADVERSARIAL-REVIEW REPAIR LOG (post-PR, 4 lenses / 3 CONFIRMED MINOR findings)

All three findings were MINOR and EVIDENCE-VOID — the conclusions BANK
(1/10, Σm_jk = 0.6448522896, and cut/cycle 9:1 were independently reproduced by
the review). The repairs strengthen gates / fix a comment + a locator; they do
NOT move any number (re-verified byte-identical after each repair). Hodge lens
and freeze-integrity came back CLEAN.

- **F1 (G-D was unfireable on its named failure mode).** `enumerate_girth_faces`
  pre-filters to length SRS_GIRTH, so the old guards gated N against the literal
  that produced it and could not fire on a girth<10 net still containing 10-cycles
  (an L=2 srs net has TRUE girth 8 by BFS, yet the enumeration returns 192 spurious
  length-10 cycles). **Repair:** added an INDEPENDENT `_bfs_girth` + `assert_srs_girth`
  (three-way BFS girth == enumeration length == SRS_GIRTH); softened the section
  comment + `derive_ring` docstring; new sabotage **S5** fires G-D on the L=2 net
  (BFS girth 8 ≠ 10). Commit `7a2aa648`. Number unchanged (L=3 genuinely girth-10).
- **F2 (G-E ImportFrom keyed on module path only, not the imported name).** Slip:
  `from ave.core.chiral_lattice import <forbidden> as w` scanned CLEAN. **Repair:** the
  ImportFrom branch now flags any forbidden constant NAME from ANY module (aliased
  or not); new planted artifact + sabotage **S2b** (`from ave.core.chiral_lattice
  import L_NODE as w` — a GENUINE forbidden re-export at chiral_lattice.py:41 that
  RESOLVES) fires G-E; honest SCOPE note added (the gate guards constant IMPORTS/uses,
  not every runtime scale injection — that residual is covered by construction:
  Z₀=τ=ℓ=1 + integer topology). Commits `321f4a0b` + the CI-hardening follow-up
  (the first draft aliased a non-resolving OMEGA_C, which the repo's separate
  import-resolution smoke gate correctly rejected; switched to L_NODE, which both
  resolves and is name-flagged). Real driver still self-scans clean; no physics touched.
- **F3 (locator drift — NOT a fabricated quote).** CITATION ERRATUM: the frozen
  prereg's LOAD-BEARING PREMISE cites `MIN_SRS_L` at `src/ave/topological/srs_dec.py:138`;
  the correct locator is **`:137`**. The quoted text `MIN_SRS_L: int = 3` is
  verbatim-correct; only the line pointer is off by one; no scientific dependency.
  The frozen prereg body is left BYTE-IDENTICAL (freeze integrity) — this erratum
  is logged here per the do-not-rewrite-history rule.

---

## ORCHESTRATOR-REVIEW REPAIRS (post-PR, 4 findings — all MINOR, EVIDENCE-VOID)

The orchestrator's adversarial review (after the satellite session's own F1/F2/F3
log above) confirmed the headline numbers INDEPENDENTLY — including a dimensionful
scipy-ODE cross-realization giving 1/10, and N=7→1/7, N=13→1/13; freeze-by-push
verified at server-timestamp level; the Hodge/theorem lens came back clean. The
four new findings are bookkeeping / honesty repairs; NO number moves. Landed here
(the frozen prereg is untouched), in the tests, and in the PR body.

- **Repair 1 — deviation-ledger reconciliation.** The prereg-vs-shipped ledger's
  "Model/gates/tolerances = no deviation" row contradicted the F1/F2 STRENGTHENING
  20 lines below (independent BFS girth + S5; name-keyed G-E ImportFrom + S2b).
  Fixed: that row now logs the strengthening; the "every deviation" ledger is
  self-consistent. (Ledger, this doc.)
- **Repair 2 — E3 "(gated in sabotage)" intra-prereg over-claim logged.** Frozen
  prereg:71 says the −1/3 scatter coefficient is "gated in sabotage," but NO shipped
  sabotage perturbs S=(2/3)J−I (driver:185; S1 = series R, S3 = dropped ledger
  term). The −1/3 is only INDIRECTLY gated (S1/S3 fire on any energy-non-conserving
  scatter; a wrong-but-LOSSLESS coefficient would slip). The value is structurally
  FORCED by the equal-Z₀ z=3 port S=(2/n)J−I (Pozar-class reciprocal 3-port floor,
  prereg:35). Logged as a ledger row; frozen file byte-identical.
  - *Optional S6 evaluated and DECLINED (not-genuinely-cheap).* The task offered an
    OPTIONAL S6 — plant a UNITARY-but-WRONG 3-port to make the −1/3 DIRECTLY
    fireable (the f_E=1/N comparator should then fire while G-A/G-C stay clean). The
    cheap candidates do NOT isolate the coefficient: the sign-variant scatter
    S′ = I − (2/3)J = −[(2/3)J − I] is just a GLOBAL wave-amplitude sign relabeling,
    so every energy (a square) and f_E are byte-identical to the canonical run — it
    reproduces 1/10 and demonstrates nothing. A genuine wrong-but-lossless 3-port
    (a circulator / port-space rotation) requires per-port re-plumbing of the
    vectorized synchronous step and careful re-validation — beyond the "<30 min,
    genuinely cheap" bar. Declined; the ledger row (Repair 2) fully discharges the
    finding without it.
- **Repair 3 — the "BALANCED (net ~ 0)" leg DEMOTED to convention-dependent.** The
  signed-mean leg measures the DFS enumeration convention, not physics (see the E5
  CORRECTION NOTE and the corrected deliverable (e)). Reproduced receipt (worktree,
  L=3 srs, 324 rings):

  ```
  as-enumerated  |Σn̂|/N          = 0.046603916267103   (Q eigenvalues all 0.333333)
  full-reversal  |Σn̂|/N          = 0.046603916267103   (Δ = 2.1e-17 — IDENTICAL)
  max|Q − Q_reversed|            = 2.1e-18              (sign-free to machine precision)
  random-sign null (2000 draws)  mean = 0.0513, 5–95% = [0.0205, 0.0909]
  noise floor 1/√324             = 0.0556
  as-enumerated percentile in null = 0.446             (dead-center)
  null 95th pct = 0.0909 < 0.1   => the old test_..._balanced <0.1 assert is NEAR-VACUOUS
  ```

  The sign-free Q-tensor isotropy leg (eigenvalues 1/3; max|Q−Q_reversed|=2.1e-18)
  SURVIVES and stays load-bearing. Test fixed: the ensemble test now asserts ONLY
  the Q-eigenvalue isotropy (renamed `..._is_isotropic`); the near-vacuous
  signed-mean `<0.1` assertion was removed with a comment naming the convention
  artifact.
- **Repair 4 — PR body refreshed** to the post-repair state (23 keepers; sabotage
  S1–S5 + S2b; F1/F2/F3 + these 4 repairs; BALANCED language struck from FLAG 2).

---

## GATE RECEIPTS (clean run, verbatim)

```
G-D  N_derived              = 10
G-A  |Lambda-Lambda0|/Lambda0 max = 2.220e-16   (tol 1e-12)   PASS
G-B  max_k|i_k - 1/N| @300t = 1.388e-17   (tol 1e-6)          PASS
G-B  i_dc mean              = 0.1000000000000000   (target 0.1)
G-C  |E_ring+E_rad-E0|/E0 max = 2.220e-16   (tol 1e-12)       PASS
     f_E trapped            = 0.1000000000000000   (target 0.1)
     f_rad                  = 0.8999999999999998   (target 0.9)
G-E  driver self-scan       = []   (dimensionless end-to-end) PASS
G-F  ortho <Pcut i,Pcyc i>/|i|^2 = -1.39e-17  (tol 1e-12)     PASS
G-F  completeness |Pcut i|^2+|Pcyc i|^2-|i|^2 = 0.0e0         PASS
G-F  projector-sum max|Pcut+Pcyc-I| = 0.0e0                   PASS
```

## E4 — geometric second axis (verbatim)

```
sum_m_jk               = 0.6448522895896426
sum_m_adjacent         = 1.2217557099831846   (60-deg adjacent bonds reinforce)
sum_m_nonadjacent      = -0.5769034203935421  (far side antiparallel)
f_E_geom               = 0.09394212082942391
L_loop_geom_over_mu0l  = 10.644852289589643
ell                    = 1.0
```
Cross-check: non-adjacent M_jk (1-D reduction) vs 32×32 Gauss–Legendre = 0.0e0;
M_jk = M_kj to 3.5e-18; adjacent shared-vertex M finite (0.0611).

## E5 — cut/cycle Hodge split (verbatim)

```
PRIMARY (tree-local nucleation ring):
  cut_fraction  (T-even, bond strain)  = 0.9
  cycle_fraction(T-odd, loop current)  = 0.09999999999999998   <-- the gyro-fossil candidate
  b1 (cycle-space dim)                 = 1
  dynamical residue == cycle projection: |f_E_sim - cyc| = 5.6e-17
SECONDARY (full srs L=3 net, KEEP-BOTH):
  cut_fraction_fullnet  = 0.6635802469135801
  cycle_fraction_fullnet= 0.3364197530864199   (> 1/10: extra parallel paths)
  b1_fullnet = 109, n_edges = 324
ORIENTATION ENSEMBLE (324 rings; Omega = unit reference axis only, no scale):
  Q = <n n^T> eigenvalues = [0.333333, 0.333333, 0.333333]   -> ISOTROPIC ring planes
  |sum n|/N_rings = 0.046604                                   -> BALANCED (net ~ 0)
  mean|n.[001]|=0.4714 (signed +0.0306);  |n.[111]|=0.4082 (+0.0353);  |n.[110]|=0.5000 (+0.0216)
```

**CORRECTION NOTE (orchestrator review — the signed-mean leg is CONVENTION-DEPENDENT).**
KEEP-BOTH: the superseded reading in the block above — `|sum n|/N_rings = 0.046604
-> BALANCED (net ~ 0)` — is DEMOTED to CONVENTION-DEPENDENT / DECORATIVE. Each
ring's Newell-normal SIGN comes SOLELY from the cyclic tuple order returned by
`enumerate_girth_faces` (a DFS enumeration convention), NOT from physics: reversing
EVERY ring tuple leaves |Σn̂|/N = 0.046604 IDENTICAL (Δ = 2.1e-17), and a random
per-ring-sign null (2000 draws) has mean 0.051, 5–95% [0.021, 0.091], noise floor
1/√324 = 0.0556 — the as-enumerated 0.0466 sits at percentile ~0.45, dead-center in
the null. The per-axis signed_mean values (+0.0306 / +0.0353 / +0.0216) are
likewise convention artifacts; only the sign-free `mean_abs` is meaningful. What
SURVIVES and stays LOAD-BEARING is the SIGN-FREE Q tensor: eigenvalues all 1/3
(max|Q − Q_reversed| ~ 2e-18) → ISOTROPIC ring planes, which BOUNDS rather than
supports a coherent large-scale swirl. The PHYSICAL balanced-vs-biased question —
ring normals keyed to the TRAPPED-CURRENT CIRCULATION SENSE per formation event
(NOT to the DFS tuple order) — is UNMEASURED here; it lands with the
front-roughness / ring-completion-statistics follow-on (task #34 / the D-IV capture
spec). Reproduced null-distribution receipt: see ORCHESTRATOR-REVIEW REPAIRS below.

---

## SABOTAGE RECEIPTS (every gate proven able to FAIL — P11, verbatim)

**S1 — planted series resistance (bond_loss=0.05 on one ring bond) → G-A + G-B FIRE:**
```
S1   G-A drift = 5.337e-01  (>> 1e-12  => Lambda decays, G-A FIRES)
S1   i_dc mean = 0.046630     (<  0.100  => plateau undershoots, G-B FIRES)
```

**S2 — planted anti-install (`_x40_s2_antiinstall_planted.py` imports OMEGA_C) → G-E FIRES:**
```
S2   ['line 17: from ave.core.constants import OMEGA_C',
      "line 22: use of dimensional constant 'OMEGA_C'"]
     (real driver self-scan remains []  => the gate is real, not decorative)
```

**S3 — dropped stub #3 from the radiated ledger → G-C FIRES, G-A UNTOUCHED (discriminator):**
```
S3   G-C drift = 5.107e-02  (>> 1e-12  => ledger loses energy, G-C FIRES)
S3   G-A drift = 2.220e-16  (<  1e-12  => dynamics unchanged; S3 hits the LEDGER only)
```

**S4 — planted oblique (non-orthogonal) Hodge projector (perturb=0.1) → G-F FIRES on all three legs:**
```
S4   G-F ortho        = 9.0000e-02   (>> 1e-12  => cut & cycle overlap, FIRES)
S4   G-F completeness = 9.0000e-02   (>> 1e-12  => projections don't sum to |i|^2)
S4   G-F projsum      = 9.0000e-02   (>> 1e-12  => P_cut + P_cyc != I)
```

**S5 — spurious-net girth (L=2 srs, true girth 8) → G-D FIRES (added by F1 repair):**
```
S5   enumerate_girth_faces lengths = [10]   (pre-filtered, silent — the defect)
S5   independent BFS girth         = 8      (the true girth)
S5   assert_srs_girth FIRES: independent BFS girth 8 != enumeration length 10
     (spurious PBC-folded rings; G-D FAIL)
```

**S2b — aliased forbidden-name import from a non-constants module → G-E FIRES (added by F2 repair; CI-hardened):**
```
S2b  ['line 20: from ave.core.chiral_lattice import L_NODE as w
       (forbidden constant name, any module)']
     (real driver self-scan remains []  => the tightened gate stays clean on the physics)
```
L_NODE is a GENUINE forbidden re-export from a non-constants module
(chiral_lattice.py:41 does `from ave.core.constants import ... L_NODE ...`), so the
planted import RESOLVES — it passes the repo's static import-resolution smoke gate
(`test_scripts_import_smoke.py`) — while the name-keyed G-E scanner still flags the
forbidden NAME. That is the faithful form of the aliased-re-export slip (the earlier
draft used a non-resolving OMEGA_C, which the import-smoke gate correctly rejected).

All six sabotage cases (S1–S5, S2b) fire their target gate; each gate is
therefore a real gate. The S3 / S4 / S5 discriminators (G-C-only /
all-three-G-F-legs / BFS-girth-only) confirm the gates are targeted, not blanket.
S5 and S2b close the P11 gaps the adversarial review found for G-D and G-E.

---

## CONSISTENCY-vs-EMERGENCE CLASSIFICATION

- **The 1/10 split (E1/E2), the cut/cycle 9:1 (E5), the 1/10 = cycle-space
  identity:** CONSISTENCY / manifestation-class. These are THEOREMS of the frozen
  TL model and of the graph (the effective-resistance identity R_eff = 9/10 for a
  tree-local N-ring). The live-fire DEMONSTRATES the entailed branch at machine
  precision; it does not adjudicate an open fork and is not an emergence claim.
  Zero CODATA / manuscript-quoted target enters; the split is pure topology.
- **Σm_jk = 0.6448522896 (E4):** a genuinely UNKNOWN number, COMPUTED here — a
  characterization (geometry-only). Not emergence (no external target to match).
- **The gyrotropic-fossil / field-cooled-magnetization interpretation of the T-odd
  cycle fraction:** a FRAMING candidate — FLAGGED, not canonized (see FLAGS).
- **Kill-test value for the u₀* triple-convergence rhyme is CONDITIONAL:** this
  lane demonstrates the WRITE mechanism is coherent and derivable in the ratified
  matched-bath model. It does NOT prove the bias is real.

---

## DELIVERABLES

**(a) The trapped/radiated split as a number.** Headline substrate-native TLM
f_E = 1/10 (radiated 9/10), live-fire vs the frozen theorem at 2.2e-16. Geometric
second axis f_E^(geom) = 0.0939421208 with Σm_jk = 0.6448522896 (mixed-footing,
separate axis). Inputs: L′,C′ (cancel through Z₀,τ), ring topology N=10, and (E4)
ring geometry. Nothing else.

**(b) Flux-quantization statement.** Trapping occurs ONLY at discrete
ring-COMPLETION events. An open chain has no mesh and no conserved Λ (KVL does not
telescope on an open path — a transient on an unclosed front fully radiates). The
instant the 10th bond closes, a conserved mesh quantity is MINTED, ΔΛ =
L_bond·i(0) banked whole. Discreteness of trapping = discreteness of ring
completions — the u₀*-accretion write mechanism at circuit level (freeze-in canon
`cosmic-axes-and-frames-glossary.md:62-67` cited as downstream consumer; NOT
canonized here).

**(c) Frozen-to-radiated fraction of parent angular momentum per nucleation.** Of
the circulation donated to the closing bond, L_bond/L_loop = 1/10 (TLM) freezes as
persistent mesh circulation; (N−1)/N = 9/10 of the donated energy radiates. Angular
momentum rides linearly on circulation at fixed ring geometry ⇒ the same fraction
of the donated leg. The absolute per-nucleation ΔL requires I_parent from the
parent-soliton model — OWED by the D-IV capture spec (task #34), NOT derived here.

**(d) Open follow-on (named, not attempted).** Front-roughness / ring-completion
statistics — the i(0) distribution across nucleation events, correlated
completions sharing bonds, and the real-lattice branch input impedance vs the
matched-stub bath abstraction.

**(e) Cut/cycle (T-even/T-odd) split of the trapped fraction (amendment).**
- **Two numbers, graph-projection footing:** cut-space (T-even bond strain) = 9/10;
  cycle-space (T-odd loop current) = 1/10. Footing: orthogonal Hodge projection of
  the unit injected-current 1-cochain on the tree-local nucleation ring;
  |P_cut δ_e|² = R_eff(e) = 9/10 for the ring-in-parallel-with-its-9-edge-path.
- **The T-odd cycle fraction = 1/10 is the load-bearing gyrotropic-fossil
  candidate** and it EQUALS the E2 energy split — because the divergence-free loop
  current is exactly the part that satisfies KCL with zero stub current and so
  CANNOT drain the matched stubs (verified: the bounce sim's trapped fraction =
  the cycle projection to 5.6e-17).
- **Sign-vs-orientation result (CORRECTED — orchestrator review):** the LOAD-BEARING,
  SIGN-FREE leg is the orientation tensor Q = ⟨n̂n̂ᵀ⟩ — eigenvalues all 1/3 to ~2e-16
  (max|Q − Q_reversed| ~ 2e-18) → ISOTROPIC ring planes, which BOUNDS rather than
  supports a coherent large-scale swirl (no preferred plane axis). The signed-mean
  leg (|Σn̂|/N = 0.047, FORMERLY read as "BALANCED (net ~ 0)") is DEMOTED to
  CONVENTION-DEPENDENT / DECORATIVE: the per-ring normal SIGN is fixed by the DFS
  tuple order of `enumerate_girth_faces`, is IDENTICAL under full ring reversal, and
  sits dead-center in a random-sign null (percentile ~0.45) — it measures the
  ENUMERATION CONVENTION, not physics. The PHYSICAL balanced-vs-biased question —
  normals keyed to the TRAPPED-CURRENT CIRCULATION SENSE per formation event — is
  UNMEASURED here and lands with the front-roughness / ring-completion-statistics
  follow-on (task #34 / D-IV capture spec). Reported with NO preferred outcome.
- **KEEP-BOTH fork for the cut-space (9/10) fate:** (i) matched-bath reading — the
  T-even part radiates, the frozen fossil is PURELY T-odd (trapped cut→0, cycle→1);
  (ii) strain-holding-lattice reading — u₀* over-bracing IS a frozen T-even
  node-potential/strain field, so the cut-space part FREEZES as static bond strain
  and the total frozen deposit splits cut:cycle = 9:1. Surfaced, not adjudicated.
- **KEEP-BOTH tree-local vs full-net:** the unambiguous 1/10 is the tree-local
  nucleation projection; on the full srs L=3 net the same edge has cycle fraction
  0.336 (extra parallel paths lower R_eff) — the tree-local qualifier is
  load-bearing and stated, never folded into the headline.

---

## FLAGS (FLAG-DON'T-FIX)

1. **No canon contradiction found on the smallest-ring count.** All checked sites
   agree srs = (10,3)-a / girth-10: `srs_dec.py:132` (`SRS_GIRTH=10`),
   `engine-capability-map.md:176` + §8b.4, `chirality-and-antimatter.md:38`. The
   #609 canon `srs-band-structure.md` carries NO smallest-ring statement (a
   band-structure / TL-map leaf) — non-contradicting, recorded here, NOT a
   contradiction. N was DERIVED (=10) by `enumerate_girth_faces`, not asserted.

2. **FRAMING candidate (do not canonize) — the gyrotropic-fossil reading.** The
   T-odd cycle fraction is a mathematically clean, T-odd, divergence-free trapped
   quantity. Its interpretation as a "field-cooled gyrotropic fossil" (Ω_parent as
   a Barnett-type effective field, trapped ring flux as a magnetization analog) is
   a FRAMING candidate surfaced by the amendment, NOT established by this lane.
   This lane proves the WRITE mechanism is coherent and the cut/cycle split is a
   geometry FACT; it does NOT prove any cosmological fossil is real. The sign-free
   ring-plane orientation tensor Q is ISOTROPIC (eigenvalues all 1/3), which BOUNDS
   rather than supports a coherent large-scale swirl — surfaced for Grant/auditor
   adjudication. (The signed-mean "balanced" reading is CONVENTION-DEPENDENT and has
   been demoted — see the E5 CORRECTION NOTE.)

3. **Mixed-footing on the E4 geometric axis (disclosed, not a contradiction).**
   f_E^(geom) mixes a TLM self-term (μ₀ℓ) with Neumann mutual terms; it is a
   separate characterization axis and is NOT comparable term-for-term to the
   substrate-native TLM 1/10. Never folded into the headline.

---

## PROVENANCE / P10 ENTAILED-BRANCH (restated)

f_E = 1/10 is a THEOREM (E1/E2 + the discrete telescope/fixed-point/orthogonality
identities). The live-fire DEMONSTRATED the entailed branch; branches (i) ledger
failure and (ii) plateau-miss could not fire (both hit machine precision). Branch
(iii) — Σm_jk = 0.6448522896 — is the one genuinely new number. Branch (iv) — the
ring-down envelope vs the Γ=−1/3 mechanism — is a characterization (radiated
increment monotone-decaying; AC energy E_ring−E_dc → 0), not a pass/fail fork.
RESULT → VERDICT: all gates PASS + all sabotage FIRES ⇒ entailed branch
DEMONSTRATED; TLM split = 1/10 confirmed; consistency-class.
