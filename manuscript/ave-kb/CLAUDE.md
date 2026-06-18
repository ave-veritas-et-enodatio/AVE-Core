# AVE Knowledge Base — Cross-Cutting Invariants

The following invariants are confirmed genuinely cross-cutting: each appears in two or more volumes and requires no qualification when applied to any single volume. These belong here and must NOT be duplicated in domain documents.

---

## Notation and Rendering

### INVARIANT-N1: Substrate noun — prose only (no object glyph)

The vacuum medium has **no dedicated object symbol**. Retired 2026-06-18: `$\mathcal{M}_A$` (collided with boundary-observable `$\mathcal{M}$`, implied "manifold", and carried stale "amorphous" subscript semantics). Use context-appropriate **prose nouns** instead:

| Context | Preferred noun |
|---|---|
| Axiom / formal | **chiral Laves K4 Cosserat crystal** |
| EE / circuit / impedance | **chiral LC network** or **substrate LC network** |
| General prose | **the substrate** or **the vacuum lattice** |
| Discrete / Nyquist / graph | **the lattice** |

**Retired 2026-06-18 (condensate):** do **not** use *condensate* as a substrate/vacuum-medium noun (conflicts with Axiom 1 crystal identity and implies BEC/QFT condensation). Keep *condensate* only for standard CM references (BCS/BEC/pair-condensate in the A-034 ladder) or explicitly bounded engine lenses (Meissner-*class*).

**Knot / trefoil disambiguation (extends INVARIANT-N1):** the electron's **real-space body** is the $0_1$ **unknot**; the proton's is the $6^3_2$ **Borromean** linkage. Rolfsen names ($3_1$ trefoil, $5_1$ cinquefoil, …) and "$(2,q)$ torus knot" labels refer to **phase-space winding portraits** on the bond-pair LC tank (Clifford torus), **not** real-space body knots. Never write "trefoil electron" without an explicit *phase-space* qualifier; valence electrons in orbital topology are $0_1$ unknot solitons on harmonic tracks. See `def-kn0t01` and `def-3638f2` (winding).

First mention in a chapter may spell out the axiom name once, then drop to "substrate" or "lattice". Do **not** reintroduce `$\mathcal{M}_A$`, `$\mathcal{M}_C$`, or any Greek letter as a substrate object. Boundary observables `$\mathcal{M}$`, `$\mathcal{Q}$`, `$\mathcal{J}$`; alpha-decomposition `$\Lambda_{\text{vol/surf/line}}$`; and Einstein `$\Lambda$` / `$\rho_\Lambda$` are unchanged.

Do NOT use the `\vacuum` macro (exists but unused in chapter bodies). KB distillers follow the prose table above.

*Confirmed by: vol1–vol9 + KB (2026-06-18 substrate-noun retirement adjudication)*

### INVARIANT-N2: Lattice node spacing notation (vol-split)

Volumes 1–5 write `$\ell_{node}$` (script ell) as the primary form. Volumes 6–7 write `$l_{node}$` (roman ell) as the primary form. Vol 8 does not use this symbol. Vols 2 and 4 contain isolated roman-ell instances in their source; those specific instances must be preserved as roman (do not normalize to script). Distillers must preserve the source notation within each volume; do not normalize across volumes.

*Confirmed by: source grep — vol1 (52 script, 2 roman); vol2 (56 script, 4 roman); vol3 (19 script, 1 roman); vol4 (22 script, 4 roman); vol5 (29 script, 0 roman); vol6 (1 script, 3 roman); vol7 (1 script, 4 roman); vol8 (0)*

### INVARIANT-N3: AVE Operator numbering convention

Topological operators are named OpN where N is the operator number. Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling). The naming convention is cross-volume; individual operator formulae live in domain documents.

*Confirmed by: vol2, vol3, vol4, vol5 (explicit); vol7 (Op3, Op8 in Ch.4)*

### INVARIANT-N4: $S_{11}$ dual-use notation

$S_{11}$ is used as the standard EE reflection coefficient in Vol 4 and Vol 7, AND as a folding free-energy functional / objective function in Vol 5. An agent navigating from Vol 4 to Vol 5 must not assume the same physical meaning. Both uses are intentional and AVE-specific.

*Confirmed by: vol4 (EE context), vol5 (biology context)*

---

## Structural Conventions

### INVARIANT-S1: tcolorbox environments

All volumes share these named environments: `resultbox`, `axiombox`, `simbox`, `examplebox`, `summarybox`, `exercisebox`, `circuitbox`, `codebox`, `objectivebox`. In KB markdown, each renders as a named blockquote with a bold environment-type prefix:

```markdown
> **[Resultbox]** *Title of the Result*
>
> Body content...
```

Individual volumes may use only a subset; resultbox is the most common. Vol 5 uses only resultbox. Vol 8 uses none.

*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7 (confirmed in surveys); vol8 (zero instances)*

### INVARIANT-S2: AVE Axiom numbering

The four AVE axioms carry stable meanings across all volumes. Canonical source of truth: [`manuscript/common_equations/eq_axiom_[1-4].tex`](../common_equations/). KB documents must use these labels; volume-specific re-instantiations may add a parenthetical domain alias but the canonical name is primary.

- Axiom 1: **Substrate Topology** — vacuum is a 3D chiral Laves K4 Cosserat crystal, with micropolar nodes (6 DOFs each: 3 translational → E, 3 microrotational → B; Cosserat rotational DOF IS the substrate-native origin of intrinsic spin), $I4_1 32$ chiral space group, intrinsic LC oscillators at each node, modeled in continuum as a Trace-Reversed Chiral LC Network. Legacy aliases: *Chiral Laves K4 Crystal*, *LC Network*. Operational signatures: K4 graph, ABCD cascade, $\ell_{node}$, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$.
- Axiom 2: **Topo-Kinematic Isomorphism** — charge as discrete geometric dislocation in the substrate; $[Q] \equiv [L]$; $\xi_{topo} = e/\ell_{node}$. Operational signatures: TKI, $(2,q)$ torus knot, topological phase dislocation, chiral SRS.
- Axiom 3: **Minimum Reflection Principle** — substrate minimizes the boundary reflection $|\Gamma|^2$ at every internal impedance boundary (substrate-native, names the externally-observable quantity); equivalently extremizes hardware action $S_{AVE}$ with $\mathcal{L}_{node} = \tfrac{1}{2}\varepsilon_0|\partial_t\mathbf{A}_n|^2 - \tfrac{1}{2\mu_0}|\nabla\times\mathbf{A}_n|^2$. Legacy alias: *Effective Action Principle*. Operational signatures: minimum-$|\Gamma|^2$, least reflected action, lossless reactive cycling, $S_{11}$ minimization (EE-projection form).
- Axiom 4: **Universal Saturation Kernel** — $S(A) = \sqrt{1 - (A/A_{yield})^2}$ — universal quarter-arc kernel governing all 26 cross-scale saturation events at zero free parameters (full catalog in Backmatter Ch. 7). Dielectric specialization (atomic / bench scale, $A = \Delta\phi/\alpha$): $C_{eff} = C_0/S$, $\varepsilon_{eff} = \varepsilon_0 S$, $\mu_{eff} = \mu_0 S$. **Sector split (Q1 = (B), Grant-ratified 2026-06-15; `research/2026-06-15_ceff-epsilon-monotonicity_result.md`):** the inverse monotonicity is **NOT a sign error** — $C_{eff}=C_0/S$ (↑) is the **longitudinal-A1 bond compliance** ($1/k_a$, the stretch-reactance that softens/diverges as the bond yields), a DISTINCT object from the **transverse-T2 permittivity** $\varepsilon_{eff}=\varepsilon_0 S$ (↓; the LCR-measured cell capacitance $C_{diel}=\varepsilon_{eff}A/d\propto S$ rolls off with it — the bench-netlist $C_0\!\cdot\!S$ form). They are **orthogonal reactances** (A1 ⊥ T2, `master-equation.md:20`) sharing the EE name "capacitance"; identifying them is the genesis-24 double-count. The $Z\to0$ (longitudinal tank $\sqrt{L/C_{comp}}$, confinement) vs $Z\to\infty$ (transverse wave $\sqrt{\mu/\varepsilon}$, rupture) readings are the two sectors' impedances — both $|\Gamma|=1$, differing only in boundary phase. Legacy alias: *Dielectric Saturation* (the atomic-scale specialization, mis-promoted to axiom-level name in earlier KB iterations). Operational signatures: saturation gate, V_snap, B_snap, Regime IV, yield boundary.

**Operating-point state and small-signal modulation:** beyond the 6 spatial DOFs per node (Ax 1), each LC tank carries a saturation-amplitude state $A$ — its operating point along the Axiom 4 kernel. This state is **gauge-relative**: only spatial gradients of $A$ across the substrate are physically observable, not absolute per-node values. Small-signal transverse propagation through a region at operating point $A_0$ sees modulated effective parameters $\varepsilon_{eff} = \varepsilon_0 S(A_0)$, $\mu_{eff} = \mu_0 S(A_0)$, $C_{eff} = C_0/S(A_0)$ — the same varactor-bias mechanism producing refractive-index gradients across all scales (Op14 local clock modulation, Op16 universal wave speed). **Scope (W6 clarification 2026-06-05; basis: `research/2026-06-05_gravity-sign-frequency-modulation-result.md`):** this *symmetric* both-sectors-scale form ($S_\varepsilon = S_\mu = S$, so $Z = Z_0\sqrt{\mu_0 S/\varepsilon_0 S} = Z_0$ invariant → reflectionless) is the **SYMMETRIC-loading operating point** — realized when *both* sectors are driven, e.g. a mass-soliton carrying internal $\mathbf{E}$ **and** $\mathbf{B}$ (Symmetric Gravity), or symmetric bulk strain. It does **NOT** follow that any DC bias scales both sectors. A **static-E-only drive is ASYMMETRIC**: a static field has no $\partial\mathbf{B}/\partial t$ to load the $\mu$ / microrotational (Cosserat-B) sector, so it loads the $\varepsilon$ / capacitive sector only ($S_\varepsilon < 1$, $S_\mu = 1$). This gives the **Op14 Meissner-asymmetric** impedance $Z_{eff} = Z_0\sqrt{S_\mu/S_\varepsilon}$ ([`operators.md:54`](common/operators.md) canonical asymmetric form) — $Z$ **changes**, so the boundary reflects ($\Gamma \neq 0$): this is the vacuum-impedance-mirror bench mechanism (Vol 4 Ch 11), NOT the reflectionless symmetric-gravity case. Even **PONDER-05** (DC-biased *non-magnetic* quartz) shifts $\varepsilon$ only — i.e. it is an **asymmetric** ($\varepsilon$-sector) load, not the symmetric both-scale form. PONDER-05 (DC-biased quartz showing 27.4% $\varepsilon_{eff}$ collapse at ~30 kV) is a **material-scale consistency analog of the kernel SHAPE** (a Class-II ceramic / quartz voltage-coefficient-of-capacitance reproduces the saturation-arc form) — **NOT a vacuum-kernel falsifier**. The conflation to avoid: $A_0 = V_{DC}/V_{yield}$ is a **per-node** ratio (the field across ONE cell $\ell_{node} = 0.386$ pm relative to the yield FIELD $E_{yield} = V_{YIELD}/\ell_{node} \approx 1.13\times10^{17}$ V/m); reaching $A_0 = 0.687$ requires 30 kV across 1.0 node-lengths. Across real quartz (mm–µm) the per-node $A_0 = 10^{-7}$–$10^{-10}$ → vacuum-kernel collapse ~0; appreciable per-node $A_0$ needs facility fields ($\sim 8\times10^{16}$ V/m). The 27.4% is the quartz material's own voltage coefficient (consistency-class), separated from the vacuum kernel per `vol4/claim-quality.md:51` ($V_{yield}$-vs-$V_{snap}$ + per-node-vs-apparatus discipline) and the Q-G42 $V_{yield}^{(apparatus)} = E_{yield}^{(substrate)}/G_{geom}$ template (`trampoline-framework.md:439`). This is **not** a 7th spatial DOF — it is the dynamical state of the LC tank, analogous to DC bias on a semiconductor varactor.

**Two distinct effective wave speeds (load-bearing for α-invariance discipline):** the substrate carries TWO substrate-native effective speeds at operating-point $A_0$, and they are NOT interchangeable in derivations. Conflating them is the canonical Pitfall #5 framework-leakage error (caught in 2026-05-28 Phase 3-A3 WALK-BACK).

- $c_{EM}(A_0) = 1/\sqrt{\mu_{eff}\,\varepsilon_{eff}} = c_0/S(A_0)$ — **Maxwell phase velocity** (the speed that enters $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ and all Maxwell-equation derivations). Canonical at clm-8nkvwy:111.
- $c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ — **substrate mechanical / group / rest-mass velocity** (oscillator-frequency × $\ell_{node}$; energy-transport speed; tracks Schwarzschild $c\sqrt{1-r_s/r}$ in the SYM-class weak-field limit). Canonical at clm-8nkvwy:113.

Both reduce to a single $c_0$ at the cold-lattice limit $S(0) = 1$.

**Under SYM-class scaling (gravity-class realization)** — $\mu(r)$ and $\varepsilon(r)$ scale together by the same factor so $Z_0$ stays invariant — the asymmetry between $c_{EM}$ and $c_{shear}$ makes $\alpha$ EXACTLY invariant: $\alpha = e^2/(4\pi(\varepsilon_0 nS)\hbar(c_0/(nS))) = \alpha_0$. **Canonical proof at `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (clm-3zz0f6, confidence/solidity 0.85).** SYM scaling produces gravitational time-dilation via $c_{shear}$ tracking $\sqrt{S}$ (Schwarzschild reduction) WHILE simultaneously preserving α exactly — multi-species clock comparisons at different gravitational potentials predict a null result for $\Delta\alpha/\alpha$, consistent with all current experimental bounds.

**Substituting $c_{shear} = c_0\sqrt{S}$ into the α formula** produces $\alpha_{eff}/\alpha_0 = 1/S^{3/2} \neq 1$, contradicting the canonical SYM invariance. This was the substantive Phase 3-A3 prework-brief error caught by `ave-prereg` v1.1 Step 3.5 substrate-thermodynamic-mapping audit: the implementor verified the substitution against canonical clm-3zz0f6 + clm-8nkvwy, surfaced the c_shear-vs-c_EM category error, returned WALK-BACK rather than committing to a broken derivation. Future agents deriving α-modulation must use $c_{EM}$ (not $c_{shear}$) in the α formula; future agents deriving gravitational time-dilation / Schwarzschild reduction use $c_{shear}$ (not $c_{EM}$).

**Asymmetric scaling (ASYM-class)** — when $\mu$ and $\varepsilon$ scale by different factors (canonical at clm-8nkvwy:112; applies to strong-field large-amplitude saturation regimes) — α is NOT invariant; this is the canonical mechanism for substrate-distinct α-modulation predictions. Low-amplitude thermal-bath regimes (e.g., $\delta_{strain}$ at $T_{CMB}$) are identified as a third substrate-mechanism class — **Cosserat-rotation-sector mass-gap thermal-mode-population ASYM** — canonical at [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm). Q-DELTA-MAP-1 closed at mechanism-class identification 2026-05-28 via `ave-ee-first-mapping` v1.0 + Grant adjudication, and the mechanism predicts the SIGN of α-vs-T running. The candidate quantitative magnitude derivation (Q-DELTA-MAP-1-quant) was **ATTEMPTED and CLOSED NEGATIVE** (FT-1, 2026-05-31): the E-mode Bose-Einstein occupation undershoots $\eta_\varepsilon$ by ~31 OOM and is generic-thermal, not AVE-distinct — so $\delta_{strain}$'s magnitude is a **definitional residual** ($1-$CODATA$/\alpha_\text{cold}$), not a derivable thermal observable; the thermal mechanism holds in **sign only**. The mechanism-class identification + its weak-force $\gamma_c$ joint-constraint SURVIVE this magnitude-only re-scope.

The numerical calibration constants ($Z_0$, $\ell_{node}$, $\alpha$, $\xi_{topo}$, $V_{snap}$, $V_{yield}$, $G$) are **derived** from these axioms — not axioms themselves; see `eq_calibration_constants.tex` and `eq_gravity_derived.tex`. Specifically, gravity is the Machian boundary impedance, derived from Ax 1 + Ax 4 symmetric scaling, not a primitive axiom.

⚠ Do not confuse $\xi_{topo} = e/\ell_{node}$ (electromechanical transduction, C/m) with the dimensionless Machian hierarchy coupling $\xi \approx 8.15 \times 10^{43}$ that appears in `eq_gravity_derived.tex`.

*Confirmed by: Vol 1 Ch 1 canonical .tex, `eq_axiom_[1-4].tex` (homologated to Scheme A 2026-05-17), and `backmatter/02_full_derivation_chain.tex`.*

### INVARIANT-S3: Shared experimental appendix

`common/appendix_experiments.tex` (Unified Index of Experimental Falsifications) is not owned by any volume. Its canonical KB location is `ave-kb/common/appendix-experiments.md`. Each volume that includes this file points to the canonical location; it is never duplicated in a volume tree.

*Confirmed by: vol7, vol8 (explicit); implied by vol1, vol3, vol4 context*

### INVARIANT-S4: Up-link format

Every KB document except `ave-kb/entry-point.md` begins with exactly one up-link on line 1:

```markdown
[↑ Parent Name](../index.md)
```

The `↑` character (U+2191) is the machine-checkable marker. Pattern: `^\[↑ `.

*Confirmed by: all 8 volumes (unanimous)*

### INVARIANT-S5: KB frontmatter (unified metadata block)

Every KB content file (`.md` under `manuscript/ave-kb/`, excluding `claim-quality.md`, `CLAUDE.md`, `CONVENTIONS.md`, `README.md`, and the `session/` working directory) carries a YAML-in-HTML-comment frontmatter block immediately after the up-link line. This block consolidates what was previously a stack of separate comment-line conventions (leaf marker, path-stable, claim-quality, no-claim, subtree-IDs).

**Format:**

```markdown
[↑ Parent Title](relative/path)

<!-- kb-frontmatter
kind: leaf
claims: [clm-h9aqmt]
path-stable: "referenced from vol2 as eq:dynamic_capacitance_yield"
-->

# Title
... body ...
```

**Required field on every file:**
- `kind` — one of `leaf`, `leaf-as-index`, `index`, `entry-point`.

**For `kind: leaf` and `kind: leaf-as-index`:**
- A leaf is a **container**: it hosts ANY number of ANY combination of `clm` / `exp` / `sup` node-bodies — there is no one-per-leaf and no one-per-flavor cap. At least one of `claims: [id1, id2, ...]`, `no-claim: <reason>`, an `exp-id: exp-xxxxxx` (one or more — see INVARIANT-S9), or a `sup-id: sup-xxxxxx` (one or more — see INVARIANT-S10) satisfies coverage (hosting an experiment or support node satisfies coverage on its own). `claims` and `no-claim` are mutually exclusive *with each other*; `exp-id` and `sup-id` are orthogonal to both and to each other and may co-exist with either. Multiple `exp-id:` / `sup-id:` keys may appear, each opening its own block (see S9/S10 for the per-block syntax). Verifier enforces.
- Optional `path-stable: <provenance string>` — preserves the prior INVARIANT-S6 cross-volume label provenance.

**For `kind: index`:**
- `subtree-claims: [id1, id2, ...]` — **derived field**, regenerated by `make refresh-kb-metadata`. Do not hand-edit.
- Optional `bootstrap: true` — set on volume roots and `entry-point`; the bootstrap blockquote directive in the body is hand-maintained for now.

**For `kind: entry-point`:**
- `subtree-claims: [id1, id2, ...]` — derived (union of all leaf claims in the KB).
- `bootstrap: true`.

**Exceptions** (formerly noted under INVARIANT-S5/S6/S8):
- *Leaf-as-index*: when a directory contains only `index.md`, that file may declare `kind: leaf-as-index` and carry `claims:` directly. Its frontmatter subsumes any subtree summary — no separate `subtree-claims` line is needed because the leaf IS the subtree.
- *Empty subtree*: an index whose children are all `no-claim` carries `subtree-claims: []`. The empty list is intentional, not forgotten.
- *Navigation-pointer index*: an index that delegates results to children may use a `> **Navigation note:**` blockquote in lieu of `## Key Results`. Treat absence of `## Key Results` as a signal to check for a Navigation note, not automatically a defect.

**Maintenance pipeline:**
- `make refresh-kb-metadata` regenerates derived fields (`subtree-claims` on index frontmatter; `solidity` — value, build-status phrase, and depends-on `(solidity X)` annotations — in every `claim-quality.md` claim entry). Idempotent. Run after any change to leaf claims or to a claim's authored `confidence`.
- `make verify-kb-metadata` is read-only — never modifies. Failures tagged refresh-fixable suggest running refresh first; manual-fix failures must be repaired by hand.

*Confirmed by: convention spec at `mad-review/kb-metadata-spine-spec.md`; migration script and standing refresh+verify scripts at `manuscript/ave-kb/tools/`.*

### INVARIANT-S6: (subsumed into S5 frontmatter)

Path-stable provenance is now the `path-stable` field of the kb-frontmatter block. The legacy `<!-- path-stable: ... -->` line form is no longer used. Cross-volume references that need stable labels declare them in their leaf's frontmatter.

### INVARIANT-S7: Canonicality of leaves

Leaves are canonical. Intermediate, index, and entry-point nodes are *derived* via summarization; even faithfully executed, a summary may suggest implications not present in or supported by the leaves. Summary content is a routing aid, not a source of claims.

Cross-cutting claim-quality content lives in [`claim-quality.md`](claim-quality.md) (KB root). Per-volume claim-quality content lives in `volN/claim-quality.md` — one each for [vol1](vol1/claim-quality.md), [vol2](vol2/claim-quality.md), [vol3](vol3/claim-quality.md), [vol4](vol4/claim-quality.md), [vol5](vol5/claim-quality.md), [vol6](vol6/claim-quality.md), and [common](common/claim-quality.md). Every consumer (agent or human) forming a claim about an AVE result must consult the cited leaf — and, where a relevant `claim-quality.md` entry exists, that claim-quality entry — before treating a summary statement as a claim source.

The volume `index.md` files and `entry-point.md` carry blockquoted bootstrap directives instructing consumers to load the relevant claim-quality documents on entry; these directives are binding on agents that visit those files.

*Confirmed by: convention spec at `AVE-Core/kb-claims-boundaries-convention.md` (gestation; promoted to `CONVENTIONS.md` in Dispatch 8); plan at `mad-review/kb-claims-boundaries-plan.md` (umbrella).*

### INVARIANT-S8: Claim-quality ID propagation

Each entry in a `claim-quality.md` file carries a stable ID of the form `clm-` plus 6 lowercase-alphanumeric characters (`<!-- id: clm-xxxxxx -->`). These IDs propagate downward through the KB via the kb-frontmatter (INVARIANT-S5) so any consumer can grep an ID and reach every location that participates in the claim.

**Frontmatter `claims` field (mandatory on every leaf and leaf-as-index, unless no-claim).** Lists every claim-quality ID this leaf hosts. A leaf either carries `claims: [...]` or `no-claim: <reason>`; the verifier enforces mutual exclusivity. The list is the complete index of which claim-quality entries depend on this leaf, and it is the authoritative source from which each entry's derived "Leaf references" footer (below) is regenerated.

**Tier 2 — inline markers (mandatory for multi-claim leaves).** When a leaf's `claims` list has 2+ IDs, every ID must have a proximal `<!-- claim-quality: clm-<id> -->` marker adjacent to the specific equation, named principle, section, or block that maps to that ID. The frontmatter `claims` list says "these IDs apply to this leaf"; Tier 2 markers say "this specific equation IS that claim." For single-claim leaves, Tier 2 is not required — the frontmatter is unambiguous.

**Frontmatter `subtree-claims` field (derived).** Each `kind: index` and `kind: entry-point` file carries `subtree-claims: [...]` listing the union of leaf claims under its scope. This field is regenerated by `make refresh-kb-metadata` from the leaf frontmatter — never hand-edited. Drift between declared and computed is a hard verifier failure (refresh-fixable category).

**"Leaf references" footer (derived).** Each `clm-` / `exp-` / `sup-` entry in a `claim-quality.md` register carries a `> **Leaf references:**` blockquote footer — the reverse-citation map of which leaves host the entry's id (the inverse of the `claims:` / `experiments:` / `exp-id:` / `sup-id:` declarations). It is a **derived field**, regenerated by `make refresh-kb-metadata` and drift-gated by `make verify-kb-metadata`, exactly like `subtree-claims` and the derived `solidity` line — **do not hand-edit it.** Refresh writes a plain, stable-sorted list of relative links to the citing leaves (a `clm-` lists every leaf whose `claims:` declares it; an `exp-` lists its `exp-id:` home plus any `experiments:` referrer; a `sup-` lists its `sup-id:` home), dropping all free-text editorial annotations. Each link is a real Markdown link `[<leaf-name>](./<rel-path>)` (leaf filename stem as link text, no backticks), so the footer paths are also checked by `verify-md-links` — a dead path *gates* rather than rotting silently. A hand-edited or stale footer is a refresh-fixable verifier failure, so the footer always reflects reality.

**Bidirectional coverage (verifier-enforced).** Every canonical entry in any `claim-quality.md` file must be cited by at least one leaf's `claims` field. An entry with no leaf citation is a hard failure: either back-link from the relevant leaves, or remove the entry. Meta-claims and reading-hazards belong in `CLAUDE.md`, `CONVENTIONS.md`, or `LIVING_REFERENCE.md`, not in `claim-quality.md`.

**Grep guarantee.** `grep -r "clm-<id>"` across the KB returns: the canonical entry in `claim-quality.md`, every leaf whose frontmatter cites the ID, every Tier 2 inline marker, and every intermediate-index `subtree-claims` summary that scopes the entry. The `clm-` prefix makes IDs unambiguously greppable — `\bclm-[a-z0-9]{6}\b` matches IDs and nothing else, never an English or physics word. Walking from a claim-quality entry to its supporting derivations (and back) is mechanical and bidirectional.

**Query index.** The claim graph is also materialized as JSONL under `manuscript/ave-kb/.index/` (claim nodes, dependency edges, citations, subtree aggregates) and queryable via the `kb_cmd` CLI — run `PYTHONPATH=manuscript/ave-kb/tools python -m kb_cmd <command>` from the repo root (commands: `show`, `deps`/`-i`, `solidity-below`, `weak-points`, `gated-on`, `cited-by`, `subtree`, `stats`; `--json` for machine output). Faster and more precise than grep for dependency, solidity, and citation questions, and the `solidity` values are tool-computed — query through the CLI rather than hand-reading the JSONL. See `manuscript/ave-kb/.index/SCHEMA.md`.

*Confirmed by: spec at `mad-review/kb-metadata-spine-spec.md`; live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,check-claim-quality}.py` (one-shot migration tools retired to `tools/archival/`); CI gate via `make verify-kb-metadata`.*

### INVARIANT-S9: Experiment DAG-id propagation (`exp-`)

Physical experiments are first-class graph nodes carrying a stable ID of the form `exp-` plus 6 lowercase-alphanumeric characters (`\bexp-[a-z0-9]{6}\b`), parallel to the `clm-` claim id (INVARIANT-S8). An experiment **validates / strengthens** one or more claims; it never originates a derivation.

**Physical experiments we design, originate, and control only.** A simulation is NOT an experiment — a simulation feeds a claim's *derivation* confidence (the min-branch), not its experimental solidity. Beyond being physical, an `exp-` id is reserved for an apparatus + measurement protocol **we design, originate, and control**. A **re-analysis of outside / public data** — e.g. a LIGO ringdown catalog, a SPARC rotation-curve table, a CMB map — is NOT an `exp-`: we neither designed nor control that measurement. Such analytical re-analysis is a `sup-` support node (INVARIANT-S10) when it does fresh analytical work (derivation-branch lift), or a plain `clm-` citation when it raises no new work. The bright line: *did we build the apparatus and run our own protocol* (`exp-`), or *did we re-analyze someone else's measurement* (`sup-` / `clm-`)?

**Two-graph model — container vs. node.** A KB leaf is a **container**; its `kind` (`leaf` | `leaf-as-index` | `index` | `entry-point`, per INVARIANT-S5) is its role in the *topography graph* (the hyperlink/navigation tree) and does NOT encode node-flavor. Separately, a leaf *originates* zero or more **node-bodies** in the *claim graph* — `clm` claim nodes (via `claims:`), `exp` experiment nodes (via `exp-id:`), and `sup` support nodes (via `sup-id:`) — connected by `strengthens` (exp→clm), `supports` (sup→clm), and `references` (leaf→exp) edges. **A container hosts any number of any combination of `clm` / `exp` / `sup` node-bodies** — there is no one-per-leaf and no one-per-flavor cap. The claim graph is acyclic; reverse views (`strengthen-by`, `supported-by`, `cites`) are untraversed bookkeeping. The flavors are **orthogonal**: one container may host a `claims:` list AND one or more `exp-id` AND one or more `sup-id` (e.g. a bench leaf that states a prediction, describes the experiment testing it, and carries an analytical support, all in one file).

**Experiment-hosting leaf frontmatter.** Experiment-ness is conferred by a leaf *hosting an `exp-id`*, not by a `kind` — there is no `kind: experiment`. An experiment-hosting leaf is a `kind: leaf` (or `leaf-as-index`) carrying, **per experiment** (a container may host several):
- `exp-id: exp-xxxxxx` — the node's stable id. The leaf is its own canonical home (no separate register). Each `exp-id:` key opens a new experiment block; its following `status:` and `strengthens:` lines belong to that block until the next `exp-id:` (a single `exp-id:` is just the one-element case — existing single-experiment leaves are unchanged).
- `status: run | pending` — `run` once a result exists; `pending` while unrun. A `pending` experiment's `strengthens` edges contribute nothing.
- `strengthens:` — a list of `clm-<id>: <strength>` pairs, one per claim the result bears on; `<strength>` ∈ [0,1] is the conferred experimental-solidity for that claim (typically `1.0` for the designed target on an unequivocal result, lower for orthogonally-implicated claims). A target may be a claim that the *same leaf* also originates via `claims:` — a node→node edge between two distinct co-located node-bodies, not a self-loop and not a cycle.

A leaf hosting one or more `exp-id` MAY also carry `claims:` (and/or `sup-id:`) — orthogonal node-bodies, **not** mutually exclusive. When co-hosted, the leaf materializes a `node_type: claim` record AND one `node_type: experiment` record per `exp-id`. The only surviving exclusivity is that an `exp-id`-owning leaf must not also carry an `experiments:` reference (an owner does not also reference foreign experiments).

**Strengthening is non-transitive (max-branch).** A `strengthens` edge lifts only its directly-targeted claim. A claim's solidity is `max(derivation_solidity, experimental_solidity)`, where `experimental_solidity = max` of the strengths from `run` experiments targeting it. Validation does NOT flow to a claim's upstream derivation dependencies — an experiment that also bears on an input authors a *separate* `strengthens` edge to that input with its own strength. A claim is `*pending*` iff its derivation is pending **and** no run experiment strengthens it (unassessed ≠ refuted; an unrun experiment can never float a pending claim down to a refuted `0.0`).

**Leaf `experiments:` references.** A leaf that REFERENCES an experiment it does not own carries an optional `experiments: [exp-xxxxxx, ...]` frontmatter field — the experiment-reference analog of `claims:` for claims (a leaf-level citation, the inverse of the experiment's Leaf-references; not rolled up transitively, not for prose mentions). It is additive: allowed alongside `claims:` OR `no-claim:`, and never a primary field (a referencing leaf with no claims of its own uses `no-claim: <reason>` + `experiments: [...]`). An owning `exp-id` leaf must NOT also carry `experiments:`. Every referenced id must resolve to a real experiment node; a verifier check enforces this. `index` / `entry-point` files carry a derived `subtree-experiments: [...]` aggregate = the OWNED-only union of exp-ids declared under their scope (a leaf's `experiments:` references do not propagate into it), regenerated by `make refresh-kb-metadata`.

**Grep guarantee.** `grep -r "exp-<id>"` returns the experiment leaf's frontmatter declaration, every `strengthens` reference, and every leaf's `experiments:` reference line that cites the id (plus the derived `subtree-experiments:` aggregates that scope it). `\bexp-[a-z0-9]{6}\b` matches exp-ids and nothing else. The experiment node and its strengthens edges are materialized in `.index/claims.jsonl` (`node_type: experiment`) and `.index/depends-on.jsonl` (`relation: strengthens`); see `.index/SCHEMA.md`.

*Confirmed by: spec at `manuscript/ave-kb/.index/SCHEMA.md` (experiment node + strengthens edge + max-solidity rule); live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,verify-kb-metadata}.py`; CI gate via `make verify-kb-metadata`.*

### INVARIANT-S10: Support DAG-id propagation (`sup-`)

A **support** node is **non-physical analytical support work** that strengthens existing claims without originating a new proposition. It carries a stable ID of the form `sup-` plus 6 lowercase-alphanumeric characters (`\bsup-[a-z0-9]{6}\b`), parallel to the `clm-` claim id (INVARIANT-S8) and the `exp-` experiment id (INVARIANT-S9). A support is **claim-like inside, experiment-like in fan-out, and contributes to the DERIVATION branch** (never the experimental/max branch). It is the analytic counterpart of the physical experiment: where an `exp-` confers *experimental* solidity via the max-branch, a `sup-` confers *derivation* lift, dep-gated.

**Two-graph model.** As with `clm` and `exp` (INVARIANT-S9), a KB leaf is a **container** whose `kind` (topography role) does NOT encode node-flavor. **A container hosts any number of any combination of `clm` / `exp` / `sup` node-bodies** — no one-per-leaf and no one-per-flavor cap. A `sup` support node-body is originated by a leaf hosting a `sup-id`, orthogonal to `claims:` / `exp-id:` / `no-claim:` (all may co-exist on one container, in any multiplicity).

**Id + hosting (one or more per container).** `sup-id: sup-xxxxxx` in a `kind: leaf` (or `leaf-as-index`) container, each immediately followed by its own `supports:` block. A container may host SEVERAL supports: each `sup-id:` key opens a new support block, and the `supports:` pairs that follow belong to that block until the next `sup-id:` (or end of frontmatter). A single `sup-id:` is just the one-element case. Each `sup-id` materializes its own `node_type: support` record (sharing the one container's canonical home) and its own `supports` fan-out edges. Hosting a `sup-id` satisfies Tier-1 coverage on its own: a leaf is valid with at least one of `{claims, no-claim, exp-id, sup-id}`.

Frontmatter example — one container hosting two supports:

```markdown
<!-- kb-frontmatter
kind: leaf
no-claim: "hosts two support nodes"
sup-id: sup-aaaaaa
supports:
  - clm-111111: 1.0
sup-id: sup-bbbbbb
supports:
  - clm-111111: *pending*
  - clm-222222: 0.50
-->
```

**Claim-like internals.** A support has a **local rigor** `quality` (scored by the same rubric as a claim's `confidence`; `*pending*` until evaluated) and **may carry its own `depends-on`** (consume other claims) OR be free-standing. These live in a **claim-quality-style entry keyed by the sup-id** — a `<!-- id: sup-xxxxxx -->` marker + a `### Quality` block (`quality:` / `depends-on:` / `solidity:` / `rationale:`) in the same `claim-quality.md` register as claims, following the claim-entry shape with `quality:` substituted for `confidence:`.

**Its own solidity (computed exactly like a claim's derivation):** `sup_solidity = round2(min(quality, *its dependency final solidities))` — the weakest link in the support's dependency cone; framework deps contribute 1.0 (never lower the min); pending propagates (pending `quality` OR a pending dep ⇒ pending `sup_solidity`). A free-standing support (no deps) has `sup_solidity = quality`.

**Experiment-like fan-out.** A single support may support MULTIPLE beneficiary claims; the hosting leaf's `supports:` block carries one `clm-<id>: <fraction>` pair per beneficiary, where `<fraction>` is the **on-point fraction** f ∈ (0,1] (how on-point the support is for that claim; 0 excluded — a zero-relevance edge is not authored). Materialized as `relation: supports` edges (source = sup-id, target = claim, carrying `fraction`) in `depends-on.jsonl`.

**Contribution to beneficiaries (DERIVATION branch, dep-gated — NOT the max/experimental branch):** each beneficiary claim `C` receives `sup_solidity × f` into its **local_quality**:
- `local_quality(C) = max(confidence(C), max over supporting sups of (sup_solidity × f))` — a pending `sup_solidity` contributes nothing (excluded from the max; no NaN, no poison), exactly as an unrun experiment is excluded from the experimental max. The on-point fraction `f` is a single edge-weight relevance discount (`sup_solidity × f`), a lone edge and NOT a chain, so it stays **multiplicative** — it is not subject to the granularity argument that motivates the `min` dep-gate below.
- `derivation_solidity(C) = round2(min(local_quality(C), *C's dependency final solidities))` — the **weakest link** in C's dependency cone, NOT the product down the chain. A support lift is still throttled by C's own deps (dep-gated; it does NOT bypass deps the way an experiment's max-branch does). **Why `min`:** solidity must be refactor-invariant — splitting one derivation step into two same-quality steps must not lower it, and a deep clean chain must not decay toward 0 as a bookkeeping artifact of derivation granularity. Confidence/quality grades are ordinal bands, not independent probabilities to be multiplied; the weakest link is the honest end-to-end summary. (Deliberate change from the earlier product form; hand-assessed confidence/quality are unchanged.)
- `solidity(C) = max(derivation_solidity, experimental_solidity)`; `*pending*` iff both branches null.
- **CRITICAL:** a pending support (pending quality or pending dep) must NEVER drag a beneficiary with otherwise-valid quality to pending. Pending-poison flows ONLY from a claim's own load-bearing `depends-on`, never from an inbound `supports` edge.

**Acyclicity.** A support's `depends-on` and its `supports` edges are hand-authored backward edges (point to claims at ≤ the support's volume), preserving the acyclic claim graph. The reverse view `supported-by` may point forward and is never traversed for solidity.

**Materialization.** `claims.jsonl` gains `node_type: "support"` records (`node_type`, `id`, `title`, `canonical_path`, `canonical_anchor`, `quality`, `solidity`), sorted last (axiom < claim < experiment < invariant < support). `depends-on.jsonl`: a support's OWN deps are `relation: depends` edges (source = sup-id); its beneficiary edges are `relation: supports` (source = sup-id, target = claim, with `fraction`). The `supported-by.jsonl` reverse view is untraversed bookkeeping. Both `sup_solidity` and the beneficiary `local_quality` lift come from the SAME shared `kb_index_lib.compute_solidity_full` (no dual-compute drift); the verifier recomputes from that same source.

**Grep guarantee.** `grep -r "sup-<id>"` returns the support's claim-quality entry, the hosting leaf's `sup-id:` + `supports:` block, and every materialized `supports` / `supported-by` reference. `\bsup-[a-z0-9]{6}\b` matches sup-ids and nothing else.

*Confirmed by: spec at `manuscript/ave-kb/.index/SCHEMA.md` (support node + supports edge + supported-by view + local_quality/sup_solidity rule); live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,verify-kb-metadata}.py`; CI gate via `make verify-kb-metadata`.*

### INVARIANT-S11: Single identification system — extend, don't reinvent

The `clm-`/`exp-`/`sup-` metadata spine (INVARIANT-S8/S9/S10) is the **single identification system** for AVE-KB knowledge. A new class of identifiable knowledge entity is added by **extending the spine** — a `node_type` declared deliberately in `.index/SCHEMA.md` + the pipeline tools, with its own greppable `\b<prefix>-[a-z0-9]{6}\b` id — **never** by spinning up a parallel local id scheme.

**Why this is an invariant, not a guideline.** The framework's history accumulated a series of one-off identification schemes — research-thread ids (`A-NNN` axiom-status, `E-NNN` manuscript-propagation, `Q-GNN` research-questions, `L5` trackers, etc.) — each invented locally for an immediate need, propagated, then buried by context-churn and left unmaintained, forcing the next need to invent yet another scheme (wash, rinse, repeat). Each rotted *silently*, which is what let the loop run. The unified spine ends it **because it is verifier-gated**: `make verify-kb-metadata`, the `verify-md-links` id-validity check, and byte-identical `.index/` regeneration all **fail loudly on drift**. A local scheme rots invisibly; a spine id cannot. The thing that keeps the single system single is *enforcement* (CI), not discipline (which churns away).

**Process/workflow ids are not knowledge ids.** Operational thread-ids in `_orchestration/` (`A-`/`E-`/`Q-G`) are legitimate *process* labels for tracking work — not knowledge-claim ids. But where a process artifact references KB knowledge it must **bridge into the spine by `clm-`/`exp-`/`sup-` id** (e.g. the closure-roadmap's hashed-id annotations), so the reference resolves into the claim DAG and is id-check-guarded. Do not let a process-tracking scheme accrete into a shadow knowledge-identification system.

*Confirmed by: the metadata-spine tooling (INVARIANT-S8/S9/S10) + CI gates `make verify-kb-metadata` / `verify-md-links`; motivated by the documented churn of legacy local schemes (A-/E-/Q-G/L5), now bridged into or superseded by the spine.*

### INVARIANT-S12: Vocabulary DAG-id propagation (`def-`)

An **adjudicated vocabulary term** is a first-class metadata node carrying a stable ID of the form `def-` plus 6 lowercase-alphanumeric characters (`\bdef-[a-z0-9]{6}\b`), parallel to the `clm-` claim (INVARIANT-S8), `exp-` experiment (INVARIANT-S9), and `sup-` support (INVARIANT-S10) ids. `def-` is the **third tracked index** — after the claim graph (`clm`/`exp`/`sup`) and the code-provenance index — and is a deliberate **extension of the single identification spine** per INVARIANT-S11 (extend, don't reinvent), not a parallel local glossary scheme. It exists because a load-bearing term whose meaning silently drifts or overloads is exactly the rot the spine ends, and a `def-` node makes that drift **verifier-gated**.

**What a `def-` node records.** The *locked meaning* of a term, the substrate **axis** it lives on (`spatial-Brillouin` | `phase-carrier` | `dimensionless` | `notation` | `other`), its **dimension/type**, an adjudication **status**, the `clm`/`exp`/`sup` ids it is load-bearing for (`clm_cross_links`), and — for an overloaded surface form — an **open-ambiguity flag** plus the verified file:line **conflicting sites**. The record shape (12 fields), `def-` id format, and sort position are frozen in [`.index/SCHEMA.md`](.index/SCHEMA.md) ("Definition record").

**Terminal metadata node.** Like a framework node (invariant / axiom), a `def-` node carries **NO scoring fields** (no `confidence` / `solidity` / `quality`) and emits **NO graph edges** — it never participates in `depends` / `strengthens` / `supports`. Its `clm_cross_links` are reverse-citation bookkeeping (which claims a term is load-bearing for), **never traversed** for solidity. A definition is **register-hosted** — one entry per `<!-- id: def-xxxxxx -->` marker in the canonical vocabulary register [`common/vocabulary-register.md`](common/vocabulary-register.md), the def- analog of how `clm-`/`sup-` entries are hosted in a `claim-quality.md` register. `canonical_path` is that register leaf; `canonical_anchor` is the slug of the term's `## <term>` heading.

**Materialization + drift-gate (Stage 2).** `refresh-kb-metadata` parses each `def-` entry and emits one `node_type: "definition"` record into `.index/claims.jsonl`; the sort key `(node_type, id)` slots the `definition` group **between `claim` and `experiment`** (axiom < claim < **definition** < experiment < invariant < support), so no existing record's relative order changes — a new group is inserted. `verify-kb-metadata` extends the referential-integrity pass so **every id in `clm_cross_links` resolves to a `claim` / `experiment` / `support` node** (an orphan, or a target resolving to a framework / definition node, is a hard failure), enforces the `\bdef-[a-z0-9]{6}\b` id format, and folds the def-count into the freshness check. A perturbed or malformed `def-` entry — a broken cross-link, an unknown `status`, a missing required field, an `ambiguous` term that drops its mandatory open-ambiguity flag — **fails `make verify-kb-metadata`**, the same loud-on-drift gate that keeps the rest of the spine single. `ANY_NODE_ID_RE` and `verify-md-links`'s id-validity check span the `def-` prefix; the illustrative `def-xxxxxx` field-legend token is in the `_ID_PLACEHOLDERS` exemption set.

**Status semantics.** `status` ∈ {`SOLID` (meaning locked AND cite confirms), `ambiguous` (≥2 corpus meanings, no locked sense yet — canon gated; always carries open-ambiguity), `proposed` (a coinage gated on review, verified to have 0 prior corpus hits — NEVER seed a coinage `SOLID`), `retired` (a superseded / walked-back term preserved per Rule 12 so a grep resolves to its replacement)}.

**`status` and `open_ambiguity` are ORTHOGONAL axes (canonical).** `status` answers *"is the canonical sense adjudicated?"*; `open_ambiguity` answers *"is the surface form overloaded?"*. They are **independent**: a term may be **`SOLID` AND carry `open_ambiguity: true`** (the canonical sense is locked, but the same word is used loosely elsewhere and must be qualified at every cite — e.g. `node` = spatial-Brillouin cell is SOLID, yet "node" is also a graph-vertex / field-null elsewhere). **Long-term rationale:** *meaning-confidence* (have we pinned the intended sense?) and *surface-overloading* (does the glyph collide with other senses?) are distinct failure modes — collapsing them would force a locked term to masquerade as unsettled merely because its spelling is reused, or hide a real overloading behind a confident sense. Keeping them orthogonal makes **`status == "SOLID" AND open_ambiguity` the canonical mis-use watch-list query** — the locked terms whose surface form still invites a wrong reading, the exact set an author must qualify. Materialized as the `definition` record's `status` + `open_ambiguity` fields and queryable via `kb_cmd` (`show <def-id>`; the `Index.watch_list` accessor returns the SOLID-and-overloaded subset).

*Confirmed by: spec at [`.index/SCHEMA.md`](.index/SCHEMA.md) (Definition record + Stage-2 materialization rule); live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,verify-kb-metadata}.py` (+ `kb_index_lib` parser/emitter, `kb_cmd` query path); CI gate via `make verify-kb-metadata` / `verify-md-links`; the canonical vocabulary register `common/vocabulary-register.md`.*

### INVARIANT-S13: Interlock DAG-id propagation (`ilk-`) + the calibration-parameter interlock

A **joint-constraint mechanism** is a first-class metadata node carrying a stable ID of the form `ilk-` plus 6 lowercase-alphanumeric characters (`\bilk-[a-z0-9]{6}\b`), parallel to the `clm-` claim (INVARIANT-S8), `exp-` experiment (S9), `sup-` support (S10), and `def-` definition (S12) ids. `ilk-` is the **seventh tracked node type** and a deliberate **extension of the single identification spine** per INVARIANT-S11 (extend, don't reinvent), NOT a parallel local scheme. It makes the calibration-parameter **INTERLOCK** (the substrate's mutual constraints among its calibration constants — α, G, Ω_freeze, u₀*, …) first-class and **machine-enforced**, where previously it existed only as prose.

**What an `ilk-` node records.** The named substrate relation that mutually constrains two (or more) calibration constants (e.g. R·r=1/4 linking the operating point u₀* and α), a `real_or_fitted` **chord/echo classification**, an adjudication `status`, the `derived_endpoint` (the constant made dependent iff the mechanism is real), and the EXISTING corpus `cited_leaf` grounding it. The record shape (10 fields), `ilk-` id format, and sort position are frozen in [`.index/SCHEMA.md`](.index/SCHEMA.md) ("Interlock-mechanism record"). Interlock-mechanism nodes are **register-hosted** — one per `<!-- id: ilk-xxxxxx -->` marker in the canonical interlock register [`common/interlock-register.md`](common/interlock-register.md), the `ilk-` analog of how `def-` entries are hosted in the vocabulary register.

**The `interlocks` relation (fourth edge class) — SYMMETRIC, hub-node-encoded.** Distinct from the 1-directional `depends`/`strengthens`/`supports` edges, `interlocks` is a SYMMETRIC mutual constraint. It is encoded hub-node style: a joint-constraint among N constants is N `interlocks` edges, one from each constant to a SHARED `ilk-` mechanism node — the symmetry is the shared target, so the loader's directed-edge assumption is unchanged (no mirrored pairs). An `interlock-mechanism` node is a valid edge **target** but originates **no** edges and carries **no scoring fields**; `interlocks` edges are **never** traversed by `compute_solidity` (which follows only `depends`).

**`real_or_fitted` is the chord/echo axis (CI-enforced consistency-vs-emergence; THREE values as of the 2026-06-14 G-ruling).** `real-geometric-constraint` = a **chord** (the substrate independently forces it → removes one DOF from the LIVE independent-parameter count); `fitted-identification` = an **echo** (a named identification the substrate does NOT independently select → a consistency match that buys NO parameter reduction); `mixed` = **form-derived / value-fitted** (G — gravity's FORM is derived (the Achromatic-Lens: SYM ε·μ co-scaling → Z=Z₀, Γ=0; the /7 PPN couplings) but G's VALUE is a calibration input (the Machian-boundary-impedance termination ξ back-solved from CODATA G via `ξ=ℏc/(7Gm_e²)`, circular not forward)). **COUNT SEMANTICS: `mixed` and `fitted-identification` BOTH do NOT reduce the count; ONLY `real-geometric-constraint` reduces** (a mixed mechanism's value-fitted half counts as an echo until its flip-test — G's = Chain B′ — closes form-first and lifts it `mixed→real`). This makes `consistency-vs-emergence` machine-enforced per mechanism. Two DERIVED, verifier-checked quantities ride on the relation: (1) the **LIVE independent-parameter count** — per the G-ruling `(# marked calibration-param nodes {m_e, α, G}) − (DOF removed by real, wired chords)` (the explicitly-marked calibration set via the register's `calibration-params:` meta line, =3; replaces the earlier `build_band:"input-only"` band =143, the build-band path retained only as the unmarked fallback), CI-asserted against the interlock register's `expected-independent-count:` so a tag flip (`fitted`/`mixed`→`real`) is loud; (2) the **falsification net** — per [`omega-freeze-cosmic-grain-cascade.md`](common/omega-freeze-cosmic-grain-cascade.md) the substrate has ONE DOF (the operating point), the channels are joint-constrained, and falsification of ANY one kills the operating point: marking any interlocked channel `refuted` propagates a verifier failure naming the `operating-point-root:`.

**Materialization + drift-gate.** `refresh-kb-metadata` parses each `ilk-` entry, emits one `node_type: "interlock-mechanism"` record into `claims.jsonl` (sort key slots it between `experiment` and `invariant`) plus one `interlocks` edge per interlocked constant into `depends-on.jsonl`. `verify-kb-metadata` enforces the `\bilk-[a-z0-9]{6}\b` id format, the `interlocks`-edge referential integrity, the `real_or_fitted`/`status` enums, `derived_endpoint` resolution, `cited_leaf` file resolution, the count assertion, and the falsification net. A perturbed entry fails `make verify-kb-metadata` — the loud-on-drift gate that keeps the spine single (INVARIANT-S11). `ANY_NODE_ID_RE` and `verify-md-links`'s id-validity check span the `ilk-` prefix.

*Confirmed by: spec at [`.index/SCHEMA.md`](.index/SCHEMA.md) (Interlock-mechanism record + interlocks edge class + independent-parameter count + falsification net); live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,verify-kb-metadata}.py` (+ `kb_index_lib` parser/emitter); CI gate via `make verify-kb-metadata` / `verify-md-links`; the canonical interlock register `common/interlock-register.md`.*

---

## Cross-Volume Physical Constants

### INVARIANT-C1: Dielectric yield limit

$V_{\text{yield}} \approx 43.65\,\text{kV}$ is defined in Vol 4 Ch.1. When this value appears in any KB document outside Vol 4, it must carry a cross-reference primary pointer to its Vol 4 definition.

*Confirmed by: vol4 (definition), vol3, vol6, vol7 (references without qualification)*

### INVARIANT-C2: Electromechanical transduction constant

$\xi_{topo} = e / l_{node}$ (units: C/m). The bridge between AVE lattice parameters and mechanical/biological quantities. Used in Vol 2 (atomic orbital mappings), Vol 4 (circuit engineering derivations), and Vol 5 (mass-to-inductance, bond stiffness-to-capacitance translations). Canonical definition: Vol 5 `organic-circuitry/electromechanical-transduction-constant.md`.

*Confirmed by: vol5 (proposes as CLAUDE.md invariant, three or more volumes)*

### INVARIANT-C3: H-bond canonical values

$d_{HB} = 1.754\,\text{\AA}$ and $E_{HB} = 4.98\,\text{kcal/mol}$ are the canonical AVE predictions for the hydrogen bond equilibrium distance and energy, derived from Op4 potential minimum in Vol 5. Referenced from Vol 3. The result values belong here; the derivation lives in `vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md`.

*Confirmed by: vol5 (derivation), vol3 (cross-volume reference)*

### INVARIANT-C4: Z-proportionality regimes

Two distinct impedance scaling regimes in the AVE framework:

- Physical/biological media: $Z \propto 1/A$
- Virtual media (LLM / information topology): $Z \propto A$

This inversion defines the hardware/software isomorphism. Cross-referenced from Vols 1, 2, 5, and 8.

*Confirmed by: vol8 (explicit); vol1 (foundation); vol2, vol5 (biological context)*

---

## Cross-Reference Formats

### INVARIANT-F1: Primary cross-volume dependency

When a KB document requires the reader to navigate to another location to get a definition, use:

```markdown
> → Primary: [Document Name](relative/path/to/target.md) — brief rationale (source label if known)
```

### INVARIANT-F2: Optional cross-volume suggestion

When a KB document suggests (but does not require) navigation to a related location:

```markdown
> ↗ See also: [Document Name](relative/path/to/target.md) — brief rationale
```

Cross-volume references appear in index documents and in leaf documents where the source text explicitly references another section. They must never paraphrase or summarize the target content.
