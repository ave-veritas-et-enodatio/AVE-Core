# Handoff Note for Next Agent Session

**Previous Completed Feature:** `feature/universal_spice_library`
**Status:** Merged to main.

## Current Active Feature Branch
`feature/ip_separation`

**Objective:**
Split the AVE monorepo into 9 repositories (1 public + 8 private) in the `ave-veritas-et-enodatio` GitHub org. Preparing for company formation and public release.

**Status: Plan APPROVED — ready for execution.**

**What's been done:**
1. Comprehensive repo audit (manuscript flow, engine, orphans, IP, 46-prediction catalog)
2. Full IP strategy evaluated (3 options analyzed)
3. User chose multi-repo split for long-term company formation
4. All open questions resolved:
   - VCA stays public (theory)
   - Vol 7 absorbed into Vol 3, eliminated
   - Vol 8 → AVE-VirtualMedia (private)
   - Volumes renumbered 0–6
   - Metamaterials → own private repo
   - Protein engine → own private repo
   - SPICE exporter → AVE-APU
   - Fresh public repo (no filter-repo needed)

**Architecture:**
- `AVE-Core` (PUBLIC) — Physics engine + Vols 0–6
- `AVE-APU` (PRIVATE) — APU hardware (Vol 9, 22 modules, compiler)
- `AVE-PONDER` (PRIVATE) — Thrust experiments
- `AVE-HOPF` (PRIVATE) — Torus knot antenna
- `AVE-Protein` (PRIVATE) — Protein folding engines
- `AVE-Fusion` (PRIVATE) — Fusion/SMES/antimatter
- `AVE-Propulsion` (PRIVATE) — Metric streamlining/warp
- `AVE-VirtualMedia` (PRIVATE) — LLM topology/γ-scaling
- `AVE-Metamaterials` (PRIVATE) — Active topological metamaterials

**Next Steps:**
1. Phase 0: Create 9 repos on GitHub (user needs to do this)
2. Phase 1–9: Execute file migration (~1 day of agent work)
3. Phase 10: Validate (make verify && make test)
4. Phase 11: File 19 provisionals ($3,420) BEFORE making public
5. Make AVE-Core public

**Key docs:**
- Full plan: `.gemini/antigravity/brain/0b4f8ab7/implementation_plan.md`
- Feature tracker: `.agents/handoffs/ip_separation.md`
