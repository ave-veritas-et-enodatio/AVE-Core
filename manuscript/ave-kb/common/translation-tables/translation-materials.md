[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Materials-science / metallurgy translation spoke — maps the imported Landau law-vs-texture toolkit + Kibble-Zurek + solidification metallurgy to the substrate's FORM/VALUE split and genesis-freeze sector (hub). Consistency-class classification rows; mints no new physical claim (no clm-). SOURCE-GATED: rows provisional pending #762 merge (see banner)."
path-stable: "the materials/metallurgy spoke of the hub-and-spoke translation architecture (README-architecture.md); the solidification/casting-relic sibling of the substrate's genesis-freeze sector"
-->

# Materials Science / Metallurgy ↔ AVE Translation

Metallurgy answers "which of a casting's numbers are the *law* and which are the *casting history*?" with a principled split (Landau: Hamiltonian-class law quantities vs texture-class history quantities). The substrate is a **cast, once-frozen chiral crystal** (genesis freeze-in), so the same split classifies which of the framework's numbers are law (boundary-equilibrium, same for every re-freeze) and which are frozen accidents of *this* casting (texture, history-derivable only). Metallurgy also supplies the **Kibble–Zurek** relic-density scaling (built for cosmology, imported back) and the **solidification / quench–anneal** sample-and-hold latch.

> ## ⚠⚠ SOURCE-GATED — ROWS PROVISIONAL, NOT YET CANONICAL ⚠⚠
>
> The source derivation is **`research/2026-07-20_vacuum-metallurgy_mapping.md` (PR #762, branch `research/vacuum-metallurgy`)**, which is **NOT YET MERGED** — verified at build 2026-07-20: `gh pr view 762` → `mergedAt: null`; the file is **absent from `main`**; the rows below were content-verified against the branch at commit `e5dd9d9b`. **Until #762 merges, treat every row in this leaf as PROVISIONAL / branch-sourced — NOT canonical.** This leaf lands the hub-and-spoke *architecture slot* for the materials discipline; the row *content* is merge-gated. The dispatch brief that requested this spoke asserted "#762 merged" — flag-don't-fix: it is not, so no row is tagged `[canon]`. Re-verify + retag `[canon]` (and add a live source link) when #762 merges. *(The source doc references it as plain text above, not a markdown link, precisely because linking an absent-from-main file would fail `verify-md-links`.)*

> **Architecture note.** This spoke follows the [hub-and-spoke rule](README-architecture.md): rows map the discipline (materials/metallurgy) to the substrate-native hub, never to a sibling discipline. Every row carries a **means-test/classification receipt**, an **Ax3-compatibility tag**, and a **provenance class**. The metallurgy import is a *classification toolkit*, not new physics — the Landau split is the same cut as the framework's own FORM/VALUE (chord/echo) split, viewed through a materials lens.

## Rows (PROVISIONAL — `[branch:#762 UNMERGED]`, content-verified @ `e5dd9d9b`)

| Materials science / metallurgy | AVE (substrate-native hub) equivalent | Receipt / classification | Ax3-compat | Provenance |
|---|---|---|---|---|
| **Landau Hamiltonian-class vs texture-class split** (law quantities vs frozen-history quantities) | **FORM / VALUE (chord / echo) split** — the framework's own cut: law-side FORMs (derived) vs history-side VALUEs (fitted / cast-in) | the split is a *criterion*, Ax3-agnostic; maps `m_e`, `ℓ_node`, `K=2G` → law-class; `Ω_freeze`, baryon asymmetry, handedness → texture-class (see [`form-deriving-value-importing.md`](../form-deriving-value-importing.md)) | **CLEAN** (a classification criterion imports no dynamics) | **consistency** (a lens on the existing FORM/VALUE verdict; imports no new physics) `[branch:#762]` |
| **Kibble–Zurek relic-density scaling** — topological-defect density $n\sim(\tau_{quench}/\tau_{relax})^{-\nu/(\nu z+1)}$ left by a finite-rate transition | **Genesis defect-freezing** — the moving-front / BEMF defect-freeze at the substrate's cooling transition (doc-59 regime table; $\Omega_{freeze}$ cascade) | causal **core** is the KZ spine ($\xi\le c\cdot t$: correlation length cannot outrun the signal speed) | **causal core CLEAN** (a causality/geometry argument, Ax3-native); **kinetics/exponent GATED** on the open lossless-vs-dissipative yield fork (Flag F) | **consistency** (causal core) / **UNDETERMINED** (exponent) `[branch:#762]` |
| **Solidification / quench–anneal sample-and-hold** — a fast front latches the local state as it passes | **Moving-front freeze-in** — the AVE-native sample-and-hold latch (already in-corpus; moving-front freeze-in + doc-59 Flag B) | already-derived, rate-dependent; cite-don't-reinvent | **CLEAN at the latch level**; the *dissipative* content of the latch is unforced (Flag F) | **consistency** (cites existing corpus) `[branch:#762]` |
| **Residual stress** — a stress field locked in at solidification, not the equilibrium state, derivable only from casting history (the history-vs-equilibrium archetype) | **Residual over-bracing $u_0^\*\approx0.187$** — bond rest-lengths lock at the *rotating-frame* equilibrium at genesis, leaving a frozen-in over-bracing residual that is not the static-frame equilibrium ([`omega-freeze-cosmic-grain-cascade.md`](../omega-freeze-cosmic-grain-cascade.md) §2) | history-vs-equilibrium discriminator ↔ the three-route test ($u_0^\*$ back-solved from CODATA α, G; tested by the independent $\mathcal{J}_{cosmic}$ route) | **CLEAN** — a residual *elastic* pre-stress is stored reactive strain, Ax3-native (the loaded-cold elastic tensor is banked lossless); the *plastic*/STZ residual is excluded (already retired as Ax3-failing) | **consistency** (elastic residual only) `[branch:#762]` |

## Owed follow-ons (routed, not done here)

- **On #762 merge:** re-verify each row two-method against the merged source, retag `[branch:#762]` → `[canon]`, add the live source link, and touch this banner. (Currency-owed; verify-before-cite ship-time clause.)
- **Gibbs–Thomson / precipitate:** the dispatch brief named a "Gibbs–Thomson / precipitate" row (`grep gibbs.thomson` = 0 corpus hits at build). Curvature-dependent solubility is a metallurgy anchor and would land HERE if wanted, but there is no source derivation — routed for Grant/auditor, not fabricated.

> ↗ See also: [Elastodynamics / Seismology Translation](translation-elastodynamics.md) — the sibling new spoke; [Condensed Matter Translation](translation-condensed-matter.md) — the phase-transition sibling; [Architecture](README-architecture.md) — the hub-and-spoke rule + source-provenance requirement.
