# L3 → BLR KB Migration — Framing Concordance

TRANSIENT reconciliation artifact. Companion to `claim-map.yaml`. Delete when the
migration completes.

## Purpose

The L3 author ran several repo-wide *framing sweeps* — near-mechanical terminology
propagations — across the KB. This table pins each sweep to a single canonical
target so the Phase II leaf port translates terminology consistently instead of
carrying three variants forward. `claim-map.yaml` says *which* leaves get ported;
this says *how* to phrase them.

Scope: `common/` + `vol1/` (the claim-map scope).

NOT in this table: the axiom-numbering scheme (Scheme A/B/C) — reconciled in
Phase I; see `axiom-homologation.md`.

Sources: agent diff analysis of the 13 modified-leaf files
(`git diff 05e2a45..l3/research/l3-electron-soliton -- ave-kb/common/ ave-kb/vol1/`)
+ BLR working-tree cross-check. Generated 2026-05-17.

## Concordance — four sweeps

### A — Substrate substance noun   ·   ADOPT L3

| field | value |
|---|---|
| Ancestor (05e2a45) | "Chiral LC Network" (bare) |
| BLR current | "Chiral LC Network" (bare) — unchanged in body prose |
| L3 variant | "Chiral LC Network in continuum-EM dialect, corresponding to a chiral Laves K4 Cosserat crystal at the substrate level" (dialect-bridge form) |
| **Canonical target** | **L3's dialect-bridge form.** Matches Phase I Axiom 1: the substrate *is* a chiral Laves K4 Cosserat crystal; the "(Trace-Reversed) Chiral LC Network" is its macroscopic continuum-EM dialect — one structural reality, two dialects. |
| Port action | Adopt L3's A-sweep edits. BLR did the axiom *header* rework but never propagated it into running body prose; ~6 bare "Chiral LC Network" hits survive (incl. compounds like "Structurally Over-Braced Chiral LC Network"). |
| L3 commits | 2eb2b1c, 590c47c, bd61693, e779d78 |

### B — Axiom 1 / Axiom 3 headers + definitions   ·   NO DELTA

| field | value |
|---|---|
| Ancestor | "Substrate Topology (The LC Network)" / "Effective Action Principle" |
| BLR current | Scheme A — "Substrate Topology (Chiral Laves K4 Cosserat Crystal)" / "Minimum Reflection Principle", with legacy-name notes |
| L3 variant | Same canonical content as BLR |
| **Canonical target** | = BLR current (already canonical via Phase I homologation) |
| Port action | None — no delta to port. |

### C — Electron body topology   ·   ADOPT L3 (user decision 2026-05-17)

| field | value |
|---|---|
| Ancestor | "trefoil electron soliton" |
| BLR current | "trefoil electron soliton" — BLR's canonical KB carried this as an *unresolved dispute* in `claim-quality.md`: `clm-trf3bd` (trefoil) vs `clm-unk0bd` (unknot). |
| L3 variant | "electron's 0₁ unknot soliton with (2,3) phase-space Clifford-torus winding" — recasts the real-space body as the unknot, demotes the trefoil to a phase-space winding label; adds an SU(2)→SO(3) provenance block in ch8 |
| **Canonical target** | **L3's unknot reframe.** Per user decision 2026-05-17: L3's resolution is adopted as a derivation improvement to migrate. Electron real-space body = the 0₁ unknot; the (2,3)/trefoil structure = its phase-space (Clifford-torus) winding. |
| Port action | Adopt L3's C-sweep edits. This resolves the canonical-KB dispute: at the port/rescore step, `clm-unk0bd` becomes the canonical electron-body-topology claim and `clm-trf3bd` is retired/superseded — record the resolution in `claim-quality.md`. Downstream-coupled: `clm-0ktpcn` (ch8 α derivation, solidity 0.41 — uses the electron knot geometry); re-check its framing during the ch8 port. The derived `.tex` (`eq_axiom_2.tex` still reads "the (2,3) torus knot is the electron") is downstream — synced to the canonical KB separately, not in this leaf port. |
| L3 commits | d301c22 ("[CRIT] Complete Trefoil-electron framing propagation — 17 instances / 13 files") |

### D — Sibling-repo pointers   ·   ADOPT L3

| field | value |
|---|---|
| Ancestor | names private repos: "AVE-APU", "AVE-Propulsion", "ave-veritas-et-enodatio/…" |
| BLR current | names private repos (unchanged) |
| L3 variant | generic "separate hardware engineering / propulsion engineering compendium" — repo names stripped |
| **Canonical target** | **L3's stripped form.** L3's commits did explicit "private-repo IP cleanup"; the KB should not hard-name sibling private repos. |
| Port action | Adopt L3's D-sweep edits. Also sweep BLR's `claim-quality.md` prose for the same repo names — not yet done there. |
| L3 commits | e779d78 ("Private-repo IP cleanup …"), 590c47c |

## Application

- The canonical artifacts are the `manuscript/ave-kb/` KB leaves. The `.tex`
  manuscript is derived — keep the port focused on the leaves.
- Phase II port: for each leaf in `claim-map.yaml`, apply the A, C, D targets when
  translating L3 content into the BLR leaf. B is a no-op.
- All four sweeps have a determined target — no blockers. Sweep C carries a
  claim-quality consequence: the `clm-trf3bd`/`clm-unk0bd` resolution and the
  ch8 α-derivation framing are handled at the port/rescore step.
- A single leaf may carry more than one sweep (e.g. `ch8-alpha-golden-torus.md`
  carries C; `vol1/ch0-intro.md` carries A + C).
