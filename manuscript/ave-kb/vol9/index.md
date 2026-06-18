[↑ AVE Knowledge Base](../entry-point.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
bootstrap: true
-->

> ⛔ **Bootstrap.** **KB leaves are canonical; LaTeX is the render.** Vol 9 `ave-kb/vol9/**` leaves (e.g. [`device-circuit-models.md`](ch3-pin-port-configuration/device-circuit-models.md), [`three-channel-impedances.md`](ch4-dc-electrical-characteristics/three-channel-impedances.md)) are the **source of truth** for Vol-9-scoped synthesis content. `manuscript/vol_9_vacuum_datasheet/` supplies the PDF (figures, `\kbleaf{}` wiring) and must not be edited ahead of the KB leaf. Primary substrate-physics derivations still live in Vols 1–6. Before forming any claim, load [`./claim-quality.md`](./claim-quality.md) and follow citations to the canonical leaf.

# Vol 9: The Vacuum Datasheet

Volume 9 documents the natural vacuum substrate (the substrate) in engineering datasheet format. The substrate is the universe's own vacuum — a 3D chiral Laves K4 Cosserat crystal of intrinsic LC oscillators (Axiom 1). Engineering practice is the process of empirically measuring the substrate's limits and corrections; AVE substrate-physics derives the substrate-mechanism behind each measurable parameter; this volume consolidates both into a single canonical datasheet.

Vol 9 is a **synthesis volume**: no chapter contains a primary substrate-physics derivation. Every spec table cites the canonical derivation in Vols 1–6. The corresponding KB tree under `vol9/` carries chapter-index stubs that route to the canonical leaves and (where applicable) host Vol-9-scoped synthesis content (e.g., the datasheet-format integration table for a chapter's substrate primitives, or a Vol-9-scoped consolidation note explicitly classified Class B per `consistency-vs-emergence` v1.3).

> **Epistemic position (Grant 2026-05-28 directive).** The substrate is **natural** (the universe's vacuum). Engineering practice is the **process of measuring** its limits through empirical observation. AVE substrate-physics **derives** the substrate-mechanism for each engineering-empirical correction. Same epistemic status as a copper datasheet — Cu is natural; the datasheet is the engineering characterization. Vol 9 documents the natural substrate's measurable behavior. Engineering empirically measures; AVE derives.

## Volume role in the corpus

| Aspect | Vol 9 role |
|---|---|
| Primary derivations | NONE — all derivations live in Vols 1–6 |
| Synthesis content | Datasheet-format consolidation; spec tables with Typical / Min / Max / Units / Conditions / Canonical-Source |
| Audience | Engineers (datasheet format familiar) · experimentalists (clear empirical predictions + falsification) · new readers (substrate-physics entry point via familiar format) · AVE practitioners (single canonical substrate-spec reference) |
| Cross-volume dependency | xr-hyper into Vol 1 (axioms / Op14 / Op16 / Op17 / Op21), Vol 3 (mechanical moduli / gravity / cosmology), Vol 4 (engineering / falsification programme), Vol 0 (backmatter; universal saturation kernel) |
| Falsification integration | Ch 15 — every load-bearing substrate-physics claim tied to at least one bench-falsifiable experiment |

## Chapter map

| Ch | Topic | Primary canonical source(s) |
|---|---|---|
| 1  | [General Description and Features](ch1-general-description/index.md) | Axiom 1 (CLAUDE.md INVARIANT-S2); Vol 1 Ch 1 |
| 2  | [Absolute Maximum Ratings](ch2-absolute-maximum-ratings/index.md) | Vol 1 + Vol 4 canonical constants; four-regimes Regime IV |
| 3  | [Pin and Port Configuration](ch3-pin-port-configuration/index.md) | Op17, Op21; $\Gamma$ boundary classes; [**device-circuit-models**](ch3-pin-port-configuration/device-circuit-models.md) leaf |
| 4  | [DC Electrical Characteristics](ch4-dc-electrical-characteristics/index.md) | `constants.py`; [**three-channel-impedances**](ch4-dc-electrical-characteristics/three-channel-impedances.md) leaf |
| 5  | [AC Electrical Characteristics](ch5-ac-electrical-characteristics/index.md) | translation-circuit.md §1; Op14 / Op16; Vol 1 Ch 5 |
| 6  | [Temperature Characteristics](ch6-temperature-characteristics/index.md) | Cosserat-Curie $\delta_{strain}$; translation-circuit.md §9 |
| 7  | [Saturation Characteristics](ch7-saturation-characteristics/index.md) | Axiom 4 kernel; Vol 0 backmatter Ch 7 |
| 8  | [Breakdown Characteristics](ch8-breakdown-characteristics/index.md) | Schwinger pair production; Miller avalanche; Regime III |
| 9  | [Mechanical Characteristics](ch9-mechanical-characteristics/index.md) | Vol 3 $G_{vac}$, $K_{vac}$, $\gamma_c$, $\nu_{vac} = 2/7$ |
| 10 | [Magnetic and Microrotational Characteristics](ch10-magnetic-microrotational-characteristics/index.md) | Cosserat flywheel L; rotation-sector mass-gap; $l_c$ |
| 11 | [Topological Characteristics](ch11-topological-characteristics/index.md) | $(2,3)$ knot uniqueness; $I4_1 32$ chiral space group |
| 12 | [Cosmological Characteristics](ch12-cosmological-characteristics/index.md) | $R_H/\ell_{node} \sim 10^{39}$; Machian $G$ (mixed); $u_0^* \approx 0.187$ (value back-fit — see Ch.12 banner) |
| 13 | [Application Examples](ch13-application-examples/index.md) | Cross-references to canonical leaves |
| 14 | [Phase Diagrams](ch14-phase-diagrams/index.md) | four-regimes.md; Vol 3 cosmology |
| 15 | [Falsification Tests](ch15-falsification-tests/index.md) | Vol 4 Ch 11 experimental programme; kill-switch tests |
| 16 | [Cross-Volume Reference Index](ch16-cross-volume-reference/index.md) | Auto-generated parameter → derivation map |
| 17 | [Engine Requirements for Faithful Simulation](ch17-engine-requirements/index.md) | Datasheet read as a simulator spec; per-line requirement ← documented engine-failure lesson |

## Multi-PR sequencing

This Vol 9 KB tree was established in PR-A (skeleton + Ch 1 + Makefile integration). Subsequent PRs populate the chapter content in the sequencing documented in `_orchestration/2026-05-28_vol-9-vacuum-datasheet-plan-and-handoff.md`:

| PR | Scope |
|---|---|
| PR-A | Skeleton + Ch 1 + Makefile integration + KB tree (THIS PR) |
| PR-B | Ch 2 (Absolute Maximum Ratings) + Ch 4 (DC Electrical) |
| PR-C | Ch 5 (AC Electrical) + Ch 9 (Mechanical) |
| PR-D | Ch 6 (Temperature) |
| PR-E | Ch 7 (Saturation) + Ch 8 (Breakdown) |
| PR-F | Ch 10 (Magnetic) + Ch 11 (Topological) |
| PR-G | Ch 3 (Pin/Port) + Ch 12 (Cosmological) |
| PR-H | Ch 13 (Application Examples) |
| PR-I | Ch 14 (Phase Diagrams) + Ch 15 (Falsification) |
| PR-J | Ch 16 (Cross-Volume Reference Index) + final polish |

---
