# Lattice-net resolution-of-record (2026-06-07)

**Question:** is the vacuum 3-wire chiral srs (degree-3) or 4-wire diamond (degree-4)?
**Resolution: z=4 diamond.** It is the net the framework actually computes on. Sources: lattice audit `a4472bc5` + audit-of-audit `aea3cc7d` (both read-only, grep-confirmed).

## Conclusions (compact)
1. **Net = z=4 diamond (`Fd-3m`).** Both engines build it (`k4_tlm.py:105,109-115`; `cosserat_field_3d.py:129-145`). The computational weight is **entirely z=4** — `λ_G=4/21 → α`, the foreword Lorentz-suppression, the trampoline moduli are **all computed on diamond; no z=3 computation exists.** The z=3 "srs" leaves are **unbacked numerology — the outliers.** Burden inverted: the z=3 leaves diverge from the substrate, not the engine.
2. **The "3" everywhere = the 3 Cosserat microrotational sectors (the spin's SU(2) generators), NOT the lattice bonds.** Every 6-DOF node (3 translational→E + 3 microrotational→B) carries the spin-3 *regardless of coordination* — present on z=4 diamond. **Spin is 3-phase (Cosserat); lattice is 4-bond (diamond) — two different structures, not in conflict.** (The 2026-06-07 "spin-½ ⇒ 3-wire" argument was OVER-STATED — it welded the Cosserat-3 onto the bonds. Corrected here.)
3. **Chirality = a `k_χ` Cosserat order-parameter on the diamond** — `Fd-3m` (supergroup) + chiral decoration = `I4₁32`. **Already adjudicated** (`closure-roadmap:191`, Foundation Item 10, 2026-05-17). The cold lattice is achiral; chirality is **excited** (keyed to the soliton's (p,q), zero under linear drive; `k_χ` has 0 occurrences in `src/ave/`).
4. **"K4" is an ambiguous name** — Sunada's K4-*graph* (4 vertices, degree-3) vs 4-*coordination*. The substrate the engine computes is **diamond (z=4)**; the "chiral Laves K4 / srs (z=3)" name is the numerological outlier, not the computed object.
5. **Spin (II) holonomy tests probed the wrong sector** (node positions = achiral E-sector); spin lives in the Cosserat ω-sector → the intrinsic spin-½ / FM test re-scopes to the **ω-helicity**, not node-position rotation.

## The one open work item
Re-ground the neutrino "3" on the **3 Cosserat sectors / trefoil crossings** (both survive z=4) via a **per-bond → per-sector substitution check**:
- δ_CP: per-bond "1/3" → π/4 at z=4, but δ_CP survives anyway (1.27π vs 1.36π, inside ±0.2). Sharper exposure: `Δc_crit = 3 → 4` flips the θ₁₃ screening regime.
- **Re-grounds on sectors → keep z=4, walk back the bond-*wording*. Doesn't → walk back the neutrino leaves.**

## Walk-back queue (pending the substitution check + Grant's confirm — NOT yet executed)
- z=3 bond-attribution wording: `chiral-screening.md:11,24` · `delta-cp-violation.md:23,30` · `dielectric-snap-limit.md:32` · `bond-force-constants.md:110` · `vol1/claim-quality.md:141` → re-ground on Cosserat-sectors OR 🔴.
- `eq_axiom_1.tex:20` "4-fold + chiral Laves K4" self-contradiction → clarify: **4-bond diamond + 3-phase Cosserat spin + `k_χ` chiral decoration.**
- `closure-roadmap:191` → note the **coordination** axis is now resolved (was left open; only the space-group axis had been adjudicated).

**Engine action:** none — the engine is the grounded choice. **Do NOT rebuild on z=3 srs** (would invalidate the α + Lorentz chains).
