# Feature: IP Separation — Multi-Repo Split (FINAL)

**Branch:** `feature/ip_separation`
**Created:** 2026-04-13
**Status:** ✅ Plan APPROVED — ready for execution
**Objective:** Split the monorepo into 1 fresh public core repo + 8 private IP repos

## Architecture (9 repos total)

| Repo | Visibility | Content | Provisionals |
|------|-----------|---------|-------------|
| **AVE-Core** | PUBLIC | Physics engine + Vols 0–6 | — |
| **AVE-APU** | PRIVATE | Vol 9, 22 HW modules, compiler | 9 ($1,620) |
| **AVE-PONDER** | PRIVATE | PONDER experiments | 2 ($360) |
| **AVE-HOPF** | PRIVATE | Torus knot antenna | 1 ($180) |
| **AVE-Protein** | PRIVATE | Protein folding engines | 2 ($360) |
| **AVE-Fusion** | PRIVATE | Fusion, SMES, antimatter | 2 ($360) |
| **AVE-Propulsion** | PRIVATE | Metric streamlining, warp | 1 ($180) |
| **AVE-VirtualMedia** | PRIVATE | LLM topology, γ-scaling | 1 ($180) |
| **AVE-Metamaterials** | PRIVATE | Active topological metamaterials | 1 ($180) |

**Total: 19 provisionals, $3,420**

## Key Decisions (All Resolved)
- Fresh AVE-Core repo (clean git history)
- VCA stays public (theory, not device)
- SPICE netlist compiler stays public
- Vol 7 absorbed into Vol 3 → eliminated
- Vol 8 moved to AVE-VirtualMedia
- Volumes renumbered: 0–6 (clean, no gaps)
- Metamaterials gets own repo
- Semiconductor SPICE exporter → AVE-APU
- Vol 5 split: theory public, engine implementation → AVE-Protein
- Archive original Applied-Vacuum-Engineering repo
