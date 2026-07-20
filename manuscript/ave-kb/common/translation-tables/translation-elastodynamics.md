[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Elastodynamics / seismology translation spoke — maps the elastic-medium sibling discipline to the substrate's elastodynamic sector (hub). Consistency-class external-anchor rows citing merged derivations; mints no new physical claim (no clm-)."
path-stable: "the elastodynamics/seismology spoke of the hub-and-spoke translation architecture (README-architecture.md); the elastic-medium measurement-sibling of the substrate's A1/T2 sector"
-->

# Elastodynamics / Seismology ↔ AVE Translation

Seismology is the **elastic-medium sibling discipline**: the vacuum substrate is a linear-elastic Cosserat solid (Ax 1), so its far-field radiation partitions into a longitudinal (compressional, A1/bulk-dilatation) and a transverse (shear, T2) channel exactly as an isotropic elastic solid partitions a moment-tensor source into P and S waves. Seismology supplies **external, non-AVE textbook anchors** (Aki–Richards moment-tensor radiation, mode conversion at boundaries, Rayleigh/head waves) for the substrate's elastodynamic sector — the measurement-sibling alongside the EE rows of [`translation-circuit.md`](translation-circuit.md).

> **Architecture note.** This spoke follows the [hub-and-spoke rule](README-architecture.md): rows map the discipline (seismology/elastodynamics) to the substrate-native hub, never to a sibling discipline. Every row carries a **means-test receipt**, an **Ax3-compatibility tag**, and a **provenance class** (`consistency-vs-emergence`). Cross-discipline rows are consistency/import-class by construction (a sibling discipline is an external anchor, not an AVE-distinct chord).

## Validated rows (means-test receipt on file)

| Elastodynamics / seismology | AVE (substrate-native hub) equivalent | Means-test receipt | Ax3-compat | Provenance |
|---|---|---|---|---|
| **P/S far-field partition** of an isotropic (Poisson) elastic solid — Aki–Richards moment-tensor radiation | **A1/T2 far-field radiation partition**: A1/bulk-dilatation (longitudinal, P) vs T2/shear-transverse (S) from a rotating mass quadrupole; the substrate's derived angular partition $\mathcal{A}_{ang}=I_P/I_S=(8\pi/15)/(4\pi/5)=2/3$ is the inverse of the *identical* P/S angular integrals | $E_S/E_P=(I_S/I_P)(V_p/V_s)^5=(3/2)(\sqrt3)^5\approx 23.4$ — **means-test PASS at value level** (exact textbook agreement, external non-AVE anchor; not order-of-magnitude) | **CLEAN** — a far-field radiative port is an Ax3-legal loss channel (the substrate stores-and-returns in bulk; radiation is a boundary/radiative port, never a bulk resistor) | **consistency** (external anchor; sharpens Q1 Reading B — a generic elastic solid *does* radiate its P/bulk channel copiously, so the vacuum's bulk-port suppression cannot come from generic elasticity) |

**Source (verify-before-cite, two-method, at build):** merged **PR #753** (`research/2026-07-20_q1-pulsar-hardening.md` §1 the $8\pi/15$ / $4\pi/5$ integrals, §6 the $E_S/E_P\approx 23.4$ receipt) — `gh pr view 753` merged 2026-07-20. Already landed in the EE spoke as a ⚠ cross-discipline entry: [`translation-circuit.md`](translation-circuit.md) §4 (line 157) + §6 means-test #28. Companion: [`port-register.md`](../port-register.md) (the A1/T2 channels + the OPEN Q1 bulk-radiation row).

> **Flag-don't-fix — duplicate home.** This P/S row currently lives in BOTH this spoke and the EE spoke ([`translation-circuit.md`](translation-circuit.md) §4/§6 #28, ⚠-tagged "cross-discipline / NOT EE"). Per the [hub-and-spoke corollary](README-architecture.md) §3, its discipline home is HERE (elastodynamics); the circuit-spoke entry should be relocated to a pointer — an **auditor-lane cleanup, not done here**. Both cite the same merged source (#753), so this is consistency-class duplication, not a contradiction.

## Candidate / watch rows (no means-test yet — do NOT treat as validated)

The seismology external-anchor toolkit was opened as a **posture-B watch candidate** (Grant-gated, watch-not-mint) at the #753 landing (`_orchestration/index.md` §2026-07-20; `q1-pulsar-hardening.md` §6 routed follow-on ii). These are correspondences the elastic-medium sibling supplies but which have **no AVE means-test on file yet**:

| Seismology anchor | Candidate substrate equivalent | Status |
|---|---|---|
| Mode conversion at a boundary (P↔S at an impedance contrast) | Mode conversion at a $\Gamma$-wall (A1↔T2 at a substrate impedance boundary) | **WATCH** — no means-test; candidate only |
| Rayleigh / boundary (surface) waves | Boundary-localized substrate modes | **WATCH** — no means-test; candidate only |
| Evanescent head waves (refracted along a fast interface) | Evanescent modes on the gapped/fast branch | **WATCH** — no means-test; candidate only |

## Owed / flagged rows (surfaced, not fabricated)

Per **flag-don't-fix** + **verify-before-cite**: two rows named in this batch's dispatch brief could **not** be seeded because they have no verified merged source at build. Recorded here, not invented:

- **"soft-mode / ring-down" row** — the ring-down content in the corpus (`research/2026-07-20_jomega-derivation_result.md`, PR #751) is an **undriven ring-down explicitly labeled POST-HOC CHARACTERIZATION, NOT in the frozen prereg** (§4.2). It is not a validated elastodynamics translation row. Not seeded; routed for a proper derivation if the correspondence is wanted.
- **"Gibbs–Thomson / precipitate" row** — `grep -rn "gibbs.thomson"` over `research/ manuscript/` returned **0 hits** at build (2026-07-20). The precipitate/"matter precipitation" content that exists (`dark-wake-bemf-foc-synthesis.md`, moving-front freeze-in) is a **materials/metallurgy** concept and belongs to [`translation-materials.md`](translation-materials.md) (curvature-dependent solubility is a metallurgy anchor), not elastodynamics. Not seeded; surfaced for Grant/auditor adjudication of where (if anywhere) it lands.

> ↗ See also: [Materials / Metallurgy Translation](translation-materials.md) — the sibling new spoke (quench/anneal, Kibble–Zurek, residual stress); [Circuit / EE Translation](translation-circuit.md) — the privileged operational spoke; [Architecture](README-architecture.md) — the hub-and-spoke rule.
