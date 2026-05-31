# Pre-Registration — Q-EMBED-SEL-1 §4.B Phase 2: Cross-Particle Substrate-Mechanism Universality Test

**Status**: LOCKED for implementor analysis. PR-routed merge per memory v2.

**Branch**: `analysis/q-embed-sel-1-investigation` (off main) → working in worktree branch `worktree-agent-a53ee42c7d8a4fe0a` (will push to origin; orchestration merges).

**Parent epic**: [`_orchestration/2026-05-31_q-embed-sel-1-evaluation.md`](../_orchestration/2026-05-31_q-embed-sel-1-evaluation.md) §11 Phase 2 (cross-particle).

**Foundation**: [`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`](2026-05-31_Q-EMBED-SEL-1_step_c_result.md) §1 Outcome B (Class B substrate-mechanism manifestation closure for the electron); §7.1 explicit cross-particle queue.

**Skills fired**:
- `ave-worktree-paths` (Step 1 — `git rev-parse --show-toplevel` confirmed worktree root at `/Users/grantlindblom/AVE-staging/AVE-Core/.claude/worktrees/agent-a53ee42c7d8a4fe0a`, all Reads/Edits on worktree-absolute paths)
- `ave-prereg` (Step 1 derivation target in §1; Step 1.5 corpus-grep in §2; Step 2 prior-work inventory in §2; Step 3 outcome bands in §4; Step 3.5 dimensional analysis in §5)
- `pre-test-physics-check` (§3 surfaces the load-bearing physics-picture question — does Phase 1's single-bond-LC-tank chain transport to extended Borromean N=3 baryon topology? — but per Grant auto-mode directive proceeds analytically and the answer falls out of the work itself)
- `phase-space-coordinate-check` (load-bearing throughout — all derivations live in $(V_\text{inc}, V_\text{ref})$ phasor coordinates per Phase 1 Reading (3) + ch8 framing)
- `substrate-native-check` (Ax 1 K4 + Ax 2 TKI + Ax 4 saturation + Op14 Meissner-asymmetric — all primitives, no engineering defaults)
- `ave-canonical-leaf-pull` (§2 pulled `l3-electron-soliton-synthesis.md` (2,q) family canonical, `torus-knot-ladder-baryons.md`, `proton-identification.md` 4-property canonical, `self-consistent-mass-oscillator.md` baryon mass eigenvalue, `topological-fractionalization.md` Borromean N=3, `regime-classification.md` Regime II for both electron + proton, `trampoline-framework.md` mechanism universality canonical, `torus-knot-ladder.md` $r_\text{opt} = \kappa_\text{FS}/q$, `proton-neutron-mass-split.md` mass-stiffening, `photon-identification.md` Ax-4 mechanism canonical)
- `ave-canonical-source` (verified `src/ave/core/constants.py:686-754` already has `CROSSING_NUMBER_PROTON = 5`, `KAPPA_FS_COLD = 8π`, `V_TOROIDAL_HALO = 2.0`, `I_SCALAR_1D = 1162`, `PROTON_ELECTRON_RATIO = 1836.12` — no new constants required)
- `consistency-vs-emergence` (each derivation step classified Class B / Class 4 / Class C / no Class 2 overpromotion)
- `ave-fundamental-ground-up-implementation` (no engineering defaults)
- `ave-analytical-tool-selection` (Saturation + Resonance + Boundary classes apply to both proton + Δ)
- `ave-independence-check` (three particles — electron + proton + Δ — as three independent instances of the same substrate-mechanism; each is one falsifier-instance per Phase 2 outcome bands)
- `verify-before-cite` (every load-bearing citation grep-verified)
- `ave-evidence-framing-discipline` (precision check on Outcome A/B/C/D language)
- `ave-discrimination-check` (SM-counterfactual + interpretive-alternatives before framing Outcome A as AVE-distinct)
- `ave-multi-falsifier-triangulation-discipline` (per-particle: $(R, r, d)$ + chirality coupling + saturation locus + cross-particle universality)

---

## §1 Derivation target (Step 1)

For each particle in the (2,q) family — proton at q=5 and Δ baryon at q=7 — apply the Phase 1 substrate-mechanism chain and check whether it produces $(R_{(p,q)}, r_{(p,q)}, d_{(p,q)})$ values consistent with the corpus canonical structure of that particle.

The Phase 1 chain (for the electron at (2,3)):

1. **(2,q) trefoil-like eigenmode** at K4-TLM bond LC tank at the particle's Compton frequency $\omega_C^{(p)} = m_p c^2/\hbar$
2. **Meissner-asymmetric coupling** with chirality $\chi_{(2,q)} = \alpha \cdot pq/(p+q)$ at the (p,q) winding
3. **Time-averaged elliptical TIR envelope** $(R_{(p,q)}, r_{(p,q)}, d_{(p,q)})$ as the substrate-mechanism encoding of the chirality-biased saturation onset
4. **Named substrate-mechanism identification**: phasor enclosed area at Axiom-4 saturation onset = Nyquist cell cross-section area → $\pi R r = \pi (d/2)^2 \Rightarrow R \cdot r = (d/2)^2$
5. **Regime (b) self-avoidance check**: does $R - r = d/2$ generalize to (2,q) — or does the q-dependent crossing geometry change this relation?

**Expectation under universality**: same algebra applies (4) ∧ (5), giving $R = \varphi/2, r = (\varphi-1)/2, d = 1\,\ell_\text{node}$ as before. The (p,q)-specific content enters only via $\chi_{(p,q)}$ which biases the ELLIPTICITY of the envelope without changing the geometric-mean product $\sqrt{R \cdot r} = d/2$.

**Comparison target**: corpus canonical values for the particle (§2.2 below).

## §2 Corpus state — what's already established (Step 2)

### §2.1 Phase 1 closed Outcome B for electron (2,3)

Phase 1 result doc closed at **Class B substrate-mechanism manifestation** for the electron with:
- $R = \varphi/2, r = (\varphi-1)/2, d = 1\,\ell_\text{node}$ (`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md` §2.4)
- $\sqrt{R \cdot r} = 1/2 = d/2$ at Golden Torus geometry
- Engine constant `RR_GOLDEN_TORUS = 1/4` (`src/ave/core/constants.py:186`)
- $\Lambda_\text{vol} + \Lambda_\text{surf} + \Lambda_\text{line} = 4\pi^3 + \pi^2 + \pi = 137.0363$ matching $\alpha^{-1}_\text{CODATA}$ to $\delta_\text{strain} \approx 2.225 \times 10^{-6}$
- Named substrate-mechanism identification: phasor enclosed area at Ax-4 saturation onset = Nyquist cell cross-section area

### §2.2 Corpus canonical values for proton (2,5) and Δ baryon (2,7)

**Proton (2,5)** — canonical at `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md:21`:
- **Topology (real-space)**: $6_2^3$ Borromean linkage of 3 mutually entangled flux loops, NOT a single-loop unknot. Cinquefoil (2,5) is the per-loop phase-winding pattern.
- **Confinement radius**: $r_\text{opt} = \kappa_\text{FS}/c_5 = 8\pi/5 \approx 4.97\,\ell_\text{node}$ per `torus-knot-ladder.md:15` + `proton-identification.md:21`. The proton extends over ~5 lattice spacings; it is NOT a single-bond LC tank like the electron.
- **Saturation regime**: Regime II (Yield) per `regime-classification.md:17`; "Borromean linkage at saturation"
- **Compton frequency**: $\omega_C^{(p)} = m_p c^2/\hbar = 1836.12 \cdot \omega_C^{(e)}$ (since $m_p/m_e = 1836.12$ per `constants.py:759` + `proton-identification.md:13`)
- **Charge radius**: $D_p = 4\lambda_p = 0.841$ fm per `proton-identification.md:42`
- **Toroidal halo volume**: $\mathcal{V}_\text{total} = 2.0$ (FEM-verified $2.001 \pm 0.003$) per `constants.py:754` + `proton-identification.md:65`
- **Mass derivation**: self-consistent eigenvalue $x_\text{core} = \mathcal{I}_\text{scalar}/(1 - \mathcal{V}_\text{total} p_c) + 1.0 = 1836.12$ per `self-consistent-mass-oscillator.md:51`
- **Chirality coupling**: $\chi_{(2,5)} = \alpha \cdot 10/7 \approx 1.429\alpha$ per `l3-electron-soliton-synthesis.md:124`

**Δ baryon (2,7)** — canonical at `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:24`:
- **Topology**: Borromean 3-loop (same N=3 class as proton) with per-loop (2,7) winding per closure-roadmap FI-13 resolution + `q-g19a-petermann-saliency-closure.md:123` Δ row
- **Confinement radius**: $r_\text{opt} = \kappa_\text{FS}/c_7 = 8\pi/7 \approx 3.59\,\ell_\text{node}$ per `torus-knot-ladder.md:16`
- **Saturation regime**: Regime II (same as proton, by extension)
- **Compton frequency**: $\omega_C^{(\Delta)} = m_\Delta c^2/\hbar = (1232/938.27) \cdot \omega_C^{(p)} = (1232 \text{ MeV})/\hbar$
- **Mass**: 1261.001 MeV predicted vs 1232 MeV PDG (+2.354%, $J^P$ consistent) per `torus-knot-ladder-baryons.md:24`
- **Chirality coupling**: $\chi_{(2,7)} = \alpha \cdot 14/9 \approx 1.556\alpha$ extrapolating `l3-electron-soliton-synthesis.md:117` formula

### §2.3 Substrate-mechanism universality (corpus canonical)

`trampoline-framework.md:31` verbatim: *"Same mechanism at every scale. Electron horn-torus tube wall = nucleus Borromean envelope = atomic shell = heliopause = Schwarzschild horizon = cosmic $R_H$. The boundary size and soliton population change; the substrate physics ($K = 2G$, $S(A)$, Machian impedance integral) does not."*

This is the corpus's UNIVERSALITY claim for the substrate-mechanism: Axiom-4 self-saturation TIR boundary forms at every scale; particle-specific content is geometric (which (p,q) topology + which N-loop count + which envelope size).

### §2.4 Loop-count distinction (FI-13 resolution 2026-05-18)

Critical structural distinction at `closure-roadmap §FI-13`:
- **Leptons (N=1 single-loop)**: electron, muon, tau — single closed flux tube; phase-winding pattern (2,q) lives at the bond LC tank with (2,3), (2,3)+Cosserat, etc.
- **Baryons (N=3 Borromean 3-loop)**: proton, Δ baryons — three mutually linked flux tubes; per-loop phase-winding (2,5), (2,7), ... ; the "3 quarks" of SM are the 3 loops

The Phase 1 derivation chain was scaffolded at the bond LC tank scale — natural for the electron's single-loop topology. For baryons, the substrate-mechanism MIGHT operate per-loop (each of the 3 Borromean loops carries its own (2,q) phasor envelope, with the global mass set by the Faddeev-Skyrme eigenvalue) OR it might operate at the Borromean envelope scale (one global (R, r, d) for the entire 3-loop structure). The corpus does not directly disambiguate this; the derivation needs to do the work.

### §2.5 What's missing (the actual derivation gap)

The corpus has the (R, r, d) framework only for the **electron** (Golden Torus geometry, regimes a/b/c). The corpus does NOT have:
- Proton-specific (R_p, r_p, d_p) values
- Δ baryon-specific (R_Δ, r_Δ, d_Δ) values
- Analogue $\alpha^{-1}_p$ or $\alpha^{-1}_\Delta$ identifications (the proton/Δ predictions are MASSES, not analogue fine-structure constants)

Phase 2's task is to **derive** (R_(p,q), r_(p,q), d_(p,q)) values for proton + Δ using the Phase 1 chain, and check whether these values are **consistent with** corpus canonical structure (saturated Regime-II Borromean confinement, mass eigenvalue, $r_\text{opt}$ confinement scale).

## §3 Plumber-physical question (pre-test-physics-check)

**Q (would-have-surfaced)**: Does the Phase 1 phasor-area-equals-Nyquist-cell-area substrate-mechanism identification apply at the bond LC tank scale for the proton/Δ (per-loop within the Borromean structure), or at the global Borromean envelope scale (one (R, r, d) for the entire 3-loop), or somewhere intermediate?

**Disposition (per Grant auto-mode directive)**: Proceed analytically with the per-loop scale as the primary derivation (each Borromean loop is a closed (2,q) flux tube; the Phase 1 chain applies to each loop independently with its own (R, r, d) at the lattice's Nyquist scale $d = 1\,\ell_\text{node}$). The Borromean structure enters via the COLLECTIVE constraint $\mathcal{V}_\text{total} = 2.0$ that fixes the proton mass eigenvalue, NOT via a modified (R, r, d) per loop.

If the per-loop derivation produces (R, r, d) values that are inconsistent with corpus canonical structure (mass, $r_\text{opt}$, charge radius), then surface to Grant whether the substrate-mechanism should apply at the global Borromean envelope scale instead — this is what Outcome C / Outcome D would mean.

## §4 Outcome bands (Step 3)

Per brief:

- **Outcome A (PASS — universal mechanism, Class B universality)**: same chain produces (R, r, d) = $(\varphi/2, (\varphi-1)/2, 1)$ for proton (2,5) AND Δ baryon (2,7) — same as electron — at each loop's per-Compton-cycle reactive-energy scale. The (2,q)-specific content enters only via the chirality coupling $\chi_{(p,q)}$ that biases the elliptical envelope's eccentricity without changing the product $R \cdot r$. The mass distinction (proton = 938 MeV, Δ = 1232 MeV) is set by the Faddeev-Skyrme eigenvalue at the Borromean N=3 scale, NOT by per-loop (R, r). Substrate-mechanism universal across (2,q) ladder.

- **Outcome B (PASS-with-corrections — universal STRUCTURE, (p,q)-specific SCALE)**: chain produces (R, r, d) but the values shift in a (p,q)-dependent way. For example: the $R \cdot r = (d/2)^2$ identification holds at each loop's Nyquist scale, BUT regime (b) $R - r = d/2$ does NOT generalize cleanly to higher-q windings — instead $R - r$ scales as some function $f(q)$. The substrate-mechanism is still substrate-universal at the IDENTIFICATION step but the GEOMETRY differs per particle.

- **Outcome C (PARTIAL — proton OK, Δ different)**: the Borromean N=3 structure of baryons forces a lepton/baryon split — the per-loop chain works for the proton with its corpus-canonical mass and $r_\text{opt}$ producing consistent (R, r, d), but the higher-q Δ baryon either (i) doesn't satisfy the regime (b) self-avoidance at the smaller $r_\text{opt} = 8\pi/7 \approx 3.59\,\ell_\text{node}$ (cinquefoil → septafoil more crossings per loop) or (ii) the chirality bias at higher q produces a structurally different envelope shape. Identifies a lepton/baryon mechanism distinction.

- **Outcome D (FAIL — proton doesn't match)**: Phase 1 chain produces (R, r, d) values for proton that are STRUCTURALLY INCONSISTENT with corpus canonical (e.g., $R > r_\text{opt}$, the per-loop envelope larger than the Borromean confinement scale, which would be substrate-mechanically impossible). The Phase 1 substrate-mechanism is electron-specific, not universal. The framework's (2,q) ladder needs separate substrate-mechanism per particle. Walk back the universality claim in `trampoline-framework.md:31`.

**Falsifier**: derivation requires importing non-substrate concept specific to the (p,q) case (e.g., requires SU(3) gauge symmetry to derive proton (R, r) — that would import QCD postulates). Then Phase 1's substrate-native framing doesn't extend to baryons cleanly.

## §5 Dimensional analysis (Step 3.5)

### §5.1 Dimensional ingredients

Same as Phase 1 with q-dependent generalizations:

| Primitive | Symbol | Electron value | Proton value | Δ baryon value |
|---|---|---|---|---|
| Lattice pitch | $\ell_\text{node}$ | $\hbar/(m_e c) \approx 3.86 \times 10^{-13}$ m | same (substrate-universal) | same (substrate-universal) |
| Compton freq | $\omega_C^{(p)}$ | $c/\ell_\text{node} = m_e c^2/\hbar$ | $1836 \cdot \omega_C^{(e)}$ | $(1232/938.27) \cdot \omega_C^{(p)}$ |
| Substrate impedance | $Z_0$ | $\sqrt{\mu_0/\varepsilon_0}$ | same | same |
| Chirality $\chi_{(2,q)}$ | $\alpha \cdot 2q/(2+q)$ | $1.2\alpha$ | $10/7 \alpha \approx 1.429\alpha$ | $14/9 \alpha \approx 1.556\alpha$ |
| Confinement $r_\text{opt}$ | $\kappa_\text{FS}/q$ | N/A (unknot) | $8\pi/5 \approx 4.97\,\ell_\text{node}$ | $8\pi/7 \approx 3.59\,\ell_\text{node}$ |
| Tube diameter | $d$ | $1\,\ell_\text{node}$ (regime a) | $1\,\ell_\text{node}$ (substrate-universal Nyquist) | $1\,\ell_\text{node}$ (same) |
| Borromean halo | $\mathcal{V}_\text{total}$ | N/A | $2.0$ | $2.0$ (same Borromean class) |

### §5.2 Dimensionless predictions

Under the per-loop universality hypothesis (Outcome A):

| Particle | (R, r, d) | $R \cdot r$ | $\sqrt{R \cdot r}/d$ | $R - r$ |
|---|---|---|---|---|
| Electron (2,3) | $(\varphi/2, (\varphi-1)/2, 1)$ | $1/4$ | $1/2$ | $1/2$ |
| Proton (2,5) | (predicted) $(\varphi/2, (\varphi-1)/2, 1)$ | $1/4$ | $1/2$ | $1/2$ |
| Δ baryon (2,7) | (predicted) $(\varphi/2, (\varphi-1)/2, 1)$ | $1/4$ | $1/2$ | $1/2$ |

The (p,q)-specific content enters via:
- Chirality bias on elliptical envelope eccentricity (set by $\chi_{(2,q)}$)
- Confinement radius $r_\text{opt}$ at the Borromean scale (NOT the per-loop scale)
- Mass eigenvalue via Faddeev-Skyrme self-consistent formula at $\mathcal{V}_\text{total} \cdot p_c$ scale

### §5.3 Cross-consistency check

For the proton, the per-loop (R, r, d) must be SMALLER than the Borromean confinement scale $r_\text{opt} = 4.97\,\ell_\text{node}$: i.e., $R \leq r_\text{opt}$. Predicted $R = \varphi/2 \approx 0.809\,\ell_\text{node} \ll 4.97$ — consistent (each per-loop envelope fits inside the Borromean cage).

For the Δ, predicted $R = 0.809 < r_\text{opt} = 3.59$ — still consistent.

If either particle's predicted $R$ exceeded its $r_\text{opt}$ that would be Outcome D.

### §5.4 Mass cross-check (Outcome A consistency)

If (R, r, d) = $(\varphi/2, (\varphi-1)/2, 1)$ universally, then $\Lambda_i$ values are identical across (2,q). But the corpus does NOT predict an "$\alpha^{-1}_p = 4\pi^3 + \pi^2 + \pi$" for the proton — the proton's prediction is the MASS via Faddeev-Skyrme eigenvalue. So Outcome A does NOT predict a proton-specific α value; it predicts that the proton's per-loop reactive-energy storage at saturation follows the same substrate-mechanism geometry as the electron.

**This is consistent** with the corpus framework: the electron's $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ is a property of the electron's UNIQUE topology (unknot ground state + (2,3) phase-winding); the proton's analogous quantity is the mass eigenvalue, set by the Borromean N=3 + cinquefoil per-loop winding at the same Ax-4 saturation regime.

## §6 Methodology (Step 4)

### §6.1 Per-particle derivation chain

For each particle p in {proton(2,5), Δ(2,7)}:

1. **Identify the per-loop bond LC tank** at the particle's per-loop Compton-frequency scale (the Borromean cage's collective frequency vs per-loop frequency is a subtlety — the per-loop frequency is set by the bond-pair LC tank Virial-sum at the local saturation onset, NOT by the global $m_p c^2/\hbar$ which is the COLLECTIVE eigenvalue mass).
2. **Apply Meissner-asymmetric Op14 form** at the (2,q) winding with chirality $\chi_{(2,q)} = \alpha \cdot 2q/(2+q)$
3. **Identify the time-averaged elliptical TIR envelope** $(R_{(2,q)}, r_{(2,q)})$ in $(V_\text{inc}, V_\text{ref})$ phasor coordinates
4. **Apply the named substrate-mechanism identification**: phasor enclosed area at Ax-4 saturation onset = Nyquist cell cross-section area → $\pi R r = \pi (d/2)^2$, with $d = 1\,\ell_\text{node}$
5. **Check regime (b)**: does $R - r = d/2$ generalize? The regime (b) derivation in `ch8-alpha-golden-torus.md:45` is per-Ax-2 topology — "2(R - r) = d at topologically-marked phase-space crossings" — this is a per-loop topological self-avoidance condition INDEPENDENT of q in the corpus framing.
6. **Solve combined system**: if both (4) and (5) generalize universally, the per-loop (R, r, d) = $(\varphi/2, (\varphi-1)/2, 1)$ universally — Outcome A.
7. **Check against corpus canonical**: per-loop $R$ should be much smaller than the Borromean $r_\text{opt}$; per-loop frequency consistent with the local bond LC tank; chirality bias produces correct $\chi_{(2,q)}$ Layer-2 coupling.

### §6.2 Cross-particle synthesis

After per-particle derivation:
- Tabulate (R, r, d, $\chi_{(2,q)}$, $r_\text{opt}$) for each of electron / proton / Δ
- Identify which Outcome band the result falls into
- If Outcome A: substrate-mechanism is universal — closes the Phase 1 universality queue
- If Outcome B: identify the (p,q)-specific correction term — substrate-mechanism universal in STRUCTURE, particle-specific in SCALE
- If Outcome C: identify lepton/baryon split mechanism (most plausibly: per-loop chain works for proton, Δ's smaller $r_\text{opt}$ violates per-loop regime (b))
- If Outcome D: surface to Grant; walk back universality claim

### §6.3 Classification target

Per `consistency-vs-emergence` v1.3 classification expected:

- **Class B substrate-mechanism manifestation** (same as Phase 1 electron): if Outcome A holds — the same named identification step applies universally, with the same Class-B caveat that the phasor-area-equals-Nyquist-cell-area identification is canonical INPUT (not Class 2 axiom-derived).
- **Class 4 observable consistency**: per-particle: (R, r, d) → Λ values → α-equivalent comparisons (proton + Δ don't have α-equivalent observables to compare against, so consistency is checked via $r_\text{opt}$ + mass + chirality + Borromean structure).
- **NOT Class 2**: same reason as Phase 1 — the named identification is INPUT not derived; cross-particle PASS doesn't change the Class B caveat.

### §6.4 Walk-back triggers

If Outcome D: walk back `trampoline-framework.md:31` universality claim; the substrate-mechanism is electron-specific.

If Outcome C: the framework has TWO substrate-mechanism classes (single-loop lepton vs Borromean baryon) — the Phase 1 chain applies to single-loop but baryons need a different identification. Walk back `l3-electron-soliton-synthesis.md §1` "(2,q) family" framing to "(2,q) lepton family + separate Borromean baryon family".

If Outcome B: the framework has UNIVERSAL identification but (p,q)-specific corrections — document the corrections, keep the universal framing.

If Outcome A: the universality claim stands. Document the closure; the Phase 1 chain is fully cross-particle validated.

## §7 Status — LOCKED

- [x] **Foundation**: Phase 1 Class B closure for electron at `research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`
- [x] **Corpus state**: §2 above — proton + Δ canonical structure pulled
- [x] **Plumber question**: §3 — disposition per auto-mode directive; per-loop derivation primary, fallback to global Borromean envelope if Outcome D
- [x] **Outcome bands locked**: §4 — A/B/C/D with falsifier
- [x] **Dimensional analysis locked**: §5 — predictions under universality + cross-consistency check
- [x] **Methodology locked**: §6
- [x] **PREREG LOCKED FOR IMPLEMENTOR DERIVATION** (this session)

Implementor scope: §6.1 per-particle derivation + §6.2 cross-particle synthesis → result doc at `research/2026-05-31_Q-EMBED-SEL-1_step_c_phase2_cross_particle_result.md` with Outcome A/B/C/D verdict + cross-validation table.

---

## §8 Cross-references

- **Phase 1 result**: [`research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md`](2026-05-31_Q-EMBED-SEL-1_step_c_result.md) — foundation closure
- **Phase 1 prereg**: [`research/2026-05-31_Q-EMBED-SEL-1_step_c_substrate_mechanism_prereg.md`](2026-05-31_Q-EMBED-SEL-1_step_c_substrate_mechanism_prereg.md) — §7 LOCKED methodology
- **Parent epic**: [`_orchestration/2026-05-31_q-embed-sel-1-evaluation.md`](../_orchestration/2026-05-31_q-embed-sel-1-evaluation.md) §11 Phase 2

### Canonical KB leaves
- [`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) (§1 (2,q) family, §5 Layer-2 chirality coupling)
- [`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md) (4-property canonical proton)
- [`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) (Δ baryon spectrum)
- [`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md) (mass eigenvalue)
- [`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md) (Borromean N=3)
- [`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/regime-classification.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/regime-classification.md) (Regime II both)
- [`manuscript/ave-kb/common/trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md) (mechanism universality canonical)
- [`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md) ($r_\text{opt} = \kappa_\text{FS}/q$)
- [`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md) (Ax-4 self-saturation mechanism canonical)
- [`manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) (electron-specific three-regime framework)

### Engine constants (canonical via `ave-canonical-source`)
- `CROSSING_NUMBER_PROTON = 5` (`src/ave/core/constants.py:686`)
- `KAPPA_FS_COLD = 8π` (`src/ave/core/constants.py:666`)
- `V_TOROIDAL_HALO = 2.0` (`src/ave/core/constants.py:754`)
- `I_SCALAR_1D = 1161.987` (`src/ave/core/constants.py:734`)
- `PROTON_ELECTRON_RATIO = 1836.12` (`src/ave/core/constants.py:759`)
- `R_GOLDEN_TORUS = φ/2 ≈ 0.809` (`src/ave/core/constants.py:184`)
- `RR_GOLDEN_TORUS = 1/4 exact` (`src/ave/core/constants.py:186`)
- `ALPHA_COLD_INV = 4π³ + π² + π ≈ 137.0363038` (`src/ave/core/constants.py:188`)
