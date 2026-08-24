[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Formalism register for Feynman diagrammatics: collects existing canonical substrate statements (each row points at its canonical home + status) and one explicitly WALK-tagged organizing reading; mints no claim, moves no solidity, adjudicates nothing (consistency/translation register only)."
-->

# Feynman Diagrammatics ↔ AVE Translation (the formalism register)

> **Register: NO-CLAIM consistency/translation leaf.** This leaf mints no claim, moves no
> solidity, and adjudicates nothing. It closes a documented gap — the corpus interpreted
> individual diagram *components* (virtual particles, loops, the pair-production vertex) but
> never the diagram *formalism* — by collecting the existing canonical statements into one
> register and adding a single organizing reading, tagged WALK below. Every row's rightmost
> column carries the canonical home the row POINTS AT plus that home's status as stated there;
> where a home carries a 🔴/🟡 marker or an echo tag, the row says so. The particle zoo
> (lepton/quark/boson rows) is NOT duplicated here — see
> [translation-particle-physics.md](translation-particle-physics.md); this leaf owns the
> FORMALISM axis only.
>
> **Provenance.** 2026-08-23 orchestrator walk over a six-lane corpus pull (leptons /
> quark-gluon / photon-propagator / weak / QED-formalism / gauge-topology), each lane returning
> file:line receipts. The organizing reading in §1 is an un-audited chat-walk synthesis
> ([WALK]); it is recorded so it can be attacked, not because it is settled.

## §1 — The organizing reading [WALK — proposed, consistency-class re-expression, NOT a result]

A Feynman diagram is one term of a **small-signal perturbation expansion of a weakly
nonlinear network** — in EE terms, a Volterra / harmonic-balance ledger. The substrate is
linear at the cold operating point (sub-yield, $\Gamma = 0$ everywhere on the matched
continuum); the Axiom-4 saturation kernel is the weak nonlinearity; the expansion-in-$\alpha$
is the expansion in that nonlinearity. The series exists because the observer expands; the
medium does not — where the corpus meets a diagram-sum result it replaces the sum with a
boundary/geometry calculation on the medium (the Schwinger $\alpha/2\pi$ leaf's own words:
*"No Feynman diagrams or renormalization are required"* — while remaining PEER-WITH-Schwinger
at value level). Substrate-natively: **diagrams are the incumbent's bookkeeping for medium
response that the medium computes directly.**

What this reading does NOT establish: why the expansion parameter is $\alpha$ per vertex
(see the α-row guard in §4), the asymptotic character of the series, or any vertex-counting
rule — all open, listed in §5.

## §2 — The formalism table

| **Diagram element** | **Substrate object** | **Canonical home + status** |
|---|---|---|
| Internal line (propagator) | Band-limited lattice Green function; the QED denominator $\lvert k\rvert^2$ is its $q\ell \ll 1$ limit (Taylor remainder $(k\ell)^2/12$) | [`brillouin-zone-uv-cutoff.md`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/brillouin-zone-uv-cutoff.md) §1 — FORM-DERIVED; recover-QED limit Class C consistency |
| Virtual particle / "exchange" | Reactive near-field / evanescent stored energy; the vocabulary register **replaces** the term outright | [`substrate-native-terminology.md:56`](../substrate-native-terminology.md) (FAIL-replace row); near/far split at [`dark-back-reaction-taxonomy.md:45`](../dark-back-reaction-taxonomy.md) — *"the QED self-energy (near) vs radiation-reaction (far) split"*, LOCKED decision-B |
| Virtual pairs in the vacuum ("foam") | Failed topologies — transient phase twists off the deterministic LC thermal-noise floor that never close a stable unknot | [`quantum-foam-virtual.md:28`](../../vol1/dynamics/ch3-quantum-signal-dynamics/quantum-foam-virtual.md) — clm-unk0bd, canonical interpretation |
| External line (real particle leg) | Propagating far-field mode on the matched continuum ($Z_0$ everywhere, $\Gamma = 0$ at every bond) | [`photon-identification.md:113`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md) §3 — canonical; weak-C regime reading canonized, DEC-01 primitive-vs-regime OPEN |
| Loop integral | Mode-sum over the first Brillouin zone — finite by mode-count, no counterterm; the same integrand diverges in the continuum | [`brillouin-zone-uv-cutoff.md:53`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/brillouin-zone-uv-cutoff.md) — clm-1wmyx3; ⚑ "one lattice cutoff or four?" tension routed at [`wall-taxonomy.md:171`](../wall-taxonomy.md), unadjudicated |
| UV regulator | The lattice pitch itself ($k_{max} = \pi/\ell_{node}$); geometric, Axiom-1-derived, α-clean | same leaf — FORM-DERIVED; no scheme-correspondence map exists (§5) |
| Renormalization | Wilsonian insensitivity-proof, not a wound: a divergence marks where the incumbent cannot see its own microphysics — which *predicts* the FORM-forced/VALUE-imported pattern at divergence-adjacent targets | [`form-deriving-value-importing.md`](../form-deriving-value-importing.md) §renormalization — MERGED meta-finding; F8 fork (renormalize vs saturate) registered with HIBEF discriminator at [`physics-lineage-map.md`](../physics-lineage-map.md) |
| Pair-production vertex | Zener field-tunneling (spontaneous) / Miller avalanche impact-ionization (seeded) at $V_{BR}$; $M = 1/S^2$ (Op22); the WKB exponent is QED's by construction | [`q-g18-schwinger-pair-wkb.md`](../../vol2/particle-physics/ch01-topological-matter/q-g18-schwinger-pair-wkb.md) — clm-lj4ok5, structurally closed at WKB level; Zener/Miller split ruled 2026-08-05 |
| Vertex (general $e\gamma e$) | The saturation nonlinearity sampled at the operating point **[WALK]** — no canonical leaf owns the ordinary vertex (§5, gap 1) | — |
| Vacuum polarization / running α | Both classical routes closed WRONG-FORM (#685 power-law-not-log; #693 spectator no-log); rows re-tagged SCOPED IMPORT; AVE-distinct content = sub-Compton α-freeze + structural Landau-pole removal; retarded + inductive channels declared NOT probed | [`q-g20f-vacuum-polarization.md`](../../vol2/particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md) — clm-bqtasn, solidity 0.60 input-only |
| Self-energy (Lamb-class) | Structural FORM match only (Bethe-log with geometric cutoff; 1.75× coefficient tension); dominant magnitude QED-imported | [`q-g20a-lamb-shift-structural-closure.md`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/q-g20a-lamb-shift-structural-closure.md) — clm-3i66gp, consistency-class, honesty re-tagged 2026-07-02 |
| Detector-side line termination (the "measurement") | Detector capture work-function at the Joule integration boundary; Born-rule click probability derived end-to-end, no Born input | [`ohmic-decoherence-born.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md) — clm-ldmvwi, solidity 0.65; AC/sign-symmetric scope |

## §3 — Two structural observations [WALK — both un-audited]

1. **The internal-line-only bosons are the evanescent ones.** W/Z appear in diagrams
   overwhelmingly as internal lines, and the substrate books them as *evanescent* sub-cutoff
   modes of the $\gamma_c$ torsional sector ([`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md),
   solidity 0.55 input-only) — modes that structurally cannot be external legs. The diagram
   grammar and the medium agree about which objects get to leave the page.
2. **The gluon line is a transmission line, not a particle line.** Confinement canon is the
   $\Gamma=-1$ TIR flux tube whose constant cross-section yields $V(r) \propto r$
   ([`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md);
   shape-forcing chain def-cf1srf OPEN). Under that canon the line drawn between quarks is a
   guided-wave channel with no free-space counterpart — consistent with no free gluon, and
   with the corpus having no gluon-as-particle dynamics at all (§5, gap 3).

## §4 — Anti-collision guards (standing discipline, restated not re-derived)

- **α per vertex**: $Q_{tank} = 1/\alpha$ is a **definitional identity, never a derivation**
  (keystone α-verdict; the baked constant was ruled culpable for a solver circularity and
  CI-scrubbed). Any reading of "why the expansion parameter is α" that routes through
  $Q_{tank}$ is citing a calibration identity, not explaining a value.
- **$a_e = \alpha/2\pi$** is PEER-WITH-Schwinger — SM's value equally rides measured α; the
  higher orders and the muon anomaly are explicit non-claims, and the muon Q-G27 forward
  ($+502\times10^{-11}$) is **in 4.6σ tension above Fermilab** on the e⁺e⁻ baseline — a
  liability rider, not a win.
- **W/Z rows** were re-typed `derived_prediction → consistency_check` (2026-08-19, D9-1);
  the public derived-predictions category is empty as of that date.
- **Longitudinal sector**: $\nabla\!\cdot\!\mathbf{u}$ propagates; $\nabla\!\cdot\!\mathbf{A}$
  is gauge (def-l0ngdu, Grant-ratified; entry carries an R40-B2a re-derivation stamp). The A1
  compression scalar is physical and never framed in QED-vector terms; no longitudinal photon.

## §5 — Gap ledger (the corpus's own; what this register cannot yet say)

1. **The ordinary vertex is unowned** — no substrate reading of the $e\gamma e$ vertex,
   vertex-counting rules, or why the order parameter is α-per-vertex; the weak V−A current
   structure is likewise absent (parity violation exists only as propagation filtering).
2. Perturbation-series structure (asymptotic/divergent character, Borel) — no coverage.
3. Gluon dynamics — no spectrum, no self-interaction, no $\alpha_s(\mu)$, no asymptotic
   freedom; the flux-tube row is the entire gluon corpus.
4. Path integral, Wick rotation, gauge-fixing/ghosts, QFT S-matrix — zero substrate
   interpretation (every KB "S-matrix" is the EE port-scattering object).
5. Time-dependent U(1) invariance — only the residual time-independent family is derived;
   the Gauss-constraint completion rides Axiom-5 FORK-1, OPEN.
6. Regularization-scheme correspondence (lattice cutoff ↔ dim-reg) — none.
7. Higher-order QED coefficients ($\alpha^3$+ of $a_e$; $\alpha^5$ Lamb pieces) — explicit
   non-claims; the corpus has no generator for them.
8. "One lattice cutoff or four?" — routed to Grant at `wall-taxonomy.md:171`, unadjudicated;
   gates the loop-integral row's edge.
