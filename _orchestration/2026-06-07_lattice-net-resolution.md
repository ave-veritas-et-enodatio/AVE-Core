# Lattice-net resolution-of-record (2026-06-07)

**Question:** is the vacuum 3-wire chiral srs (degree-3) or 4-wire diamond (degree-4)?
**Resolution: z=4 diamond.** It is the net the framework actually computes on. Sources: lattice audit `a4472bc5` + audit-of-audit `aea3cc7d` (both read-only, grep-confirmed).

## Conclusions (compact)
1. **Net = z=4 diamond (`Fd-3m`).** Both engines build it (`k4_tlm.py:105,109-115`; `cosserat_field_3d.py:129-145`). The computational weight is **entirely z=4** — `λ_G=4/21 → α`, the foreword Lorentz-suppression, the trampoline moduli are **all computed on diamond; no z=3 computation exists.** The z=3 "srs" leaves are **unbacked numerology — the outliers.** Burden inverted: the z=3 leaves diverge from the substrate, not the engine.
2. **The "3" everywhere = the 3 Cosserat microrotational sectors (the spin's SU(2) generators), NOT the lattice bonds.** Every 6-DOF node (3 translational→E + 3 microrotational→B) carries the spin-3 *regardless of coordination* — present on z=4 diamond. **Spin is 3-phase (Cosserat); lattice is 4-bond (diamond) — two different structures, not in conflict.** (The 2026-06-07 "spin-½ ⇒ 3-wire" argument was OVER-STATED — it welded the Cosserat-3 onto the bonds. Corrected here.)
3. **Chirality = a `k_χ` Cosserat order-parameter on the diamond** — `Fd-3m` (supergroup) + chiral decoration = `I4₁32`. **Already adjudicated** (`closure-roadmap:191`, Foundation Item 10, 2026-05-17). The cold lattice is achiral; chirality is **excited** (keyed to the soliton's (p,q), zero under linear drive; `k_χ` has 0 occurrences in `src/ave/`).
4. **"K4" is an ambiguous name** — Sunada's K4-*graph* (4 vertices, degree-3) vs 4-*coordination*. The substrate the engine computes is **diamond (z=4)**; the "chiral Laves K4 / srs (z=3)" name is the numerological outlier, not the computed object.
5. **Spin (II) holonomy tests probed the wrong sector** (node positions = achiral E-sector); spin lives in the Cosserat ω-sector → the intrinsic spin-½ / FM test re-scopes to the **ω-helicity**, not node-position rotation.

## The one open work item — RESOLVED (check `ad91271e`, PR #113)
**Verdict: KEEP z=4 + fix the bond-wording. Clean (sector-grounded) outcome; one localized Grant call at θ₁₃.**
- **δ_CP re-grounds CLEANLY + UNCONDITIONALLY:** the middle term stays 1/3 on the **3 Cosserat sectors** (z-independent) → restores **61/45 = 1.3556π** on z=4 (per-*bond* would degrade to 1.272π). The "3" was welded (bond=sector=crossing) only *coincidentally* at z=3; z=4 de-welds it and the sector/crossing groundings survive. **Axiom-supported:** `eq_axiom_1.tex:20` already says "4-fold connectivity … three microrotational DOF" — 4 bonds, 3 sectors, *distinct*.
- **θ₁₃ is the ONE load-bearing Grant call:** `Δc_crit` (the θ₁₃ screening threshold; Δc=4 knife-edge — the wrong reading unscreens it ~20×, 0.022→~0.44) re-grounds on the 3 Cosserat sectors via an **SU(2) selection rule** (angular momentum is intrinsically 3-component → max 3 quanta/interaction, z-independent) — BUT as written it's bond-channel transport (`op14-cross-sector-trading.md:11`: the trade goes via the bond LC tank's inductive side, ρ=−0.990). **Plumber-physical: is the AM-transfer bottleneck the 3 angular-momentum COMPONENTS (→ Δc_crit=3, θ₁₃ survives) or the bond CHANNELS (→ 4 on diamond, θ₁₃ breaks)?**
- δ_CP, θ₁₂, θ₂₃, the JUNO inverted-hierarchy falsifier **survive either way** (they depend on crossing-numbers 5,7,9, not connectivity-3). **NOT board-wide z=3-dependence — one localized call at θ₁₃.**

## Walk-back queue (pending the substitution check + Grant's confirm — NOT yet executed)
- z=3 bond-attribution wording → re-ground on Cosserat-sectors: `delta-cp-violation.md:23` (δ_CP "1/3 per bond"→"per sector") **UNCONDITIONAL** · `chiral-screening.md:11,13,24` (Δc_crit + the bond=sector=crossing weld) **GATED on Grant's θ₁₃/Δc_crit call** · `dielectric-snap-limit.md:32` · `bond-force-constants.md:110` · `vol1/claim-quality.md:141` (+ `:1188` is the z=3-vs-z=4 self-contradiction). Disambiguate the "3 Cosserat sectors" terminology collision: ω-components (`eq_axiom_1.tex:20`) vs translation/rotation/curvature-twist (`vol1/claim-quality.md:520`).
- `eq_axiom_1.tex:20` "4-fold + chiral Laves K4" self-contradiction → clarify: **4-bond diamond + 3-phase Cosserat spin + `k_χ` chiral decoration.**
- `closure-roadmap:191` → note the **coordination** axis is now resolved (was left open; only the space-group axis had been adjudicated).

**Engine action:** none — the engine is the grounded choice. **Do NOT rebuild on z=3 srs** (would invalidate the α + Lorentz chains).
