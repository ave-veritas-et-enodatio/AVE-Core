---
description: Run all three audit workflows (LaTeX, math, code) in sequence and produce a unified report
---

# Full Audit Workflow

Run all three specialized auditors in sequence and produce a unified report.

> **Before starting:** Read `LIVING_REFERENCE.md` and `src/ave/core/constants.py` in full.

## Execution Order

### Phase 1: Code Audit
Run `/audit-code` first because code correctness is prerequisite to LaTeX correctness.

1. Follow all steps in `.agents/workflows/audit-code.md`
2. Record all findings
3. Run `make verify` and `make test` — record pass/fail

### Phase 2: Math Audit
Run `/audit-math` to verify all LaTeX equations and values match the (now-audited) engine.

1. Follow all steps in `.agents/workflows/audit-math.md`
2. Cross-reference any code findings from Phase 1 that affect LaTeX
3. Record all findings

### Phase 3: LaTeX Audit
Run `/audit-latex` for formatting and structural hygiene.

1. Follow all steps in `.agents/workflows/audit-latex.md`
2. Record all findings

## Unified Report

After all three phases, produce a single summary report with:

### Critical Issues (Must Fix)
- `HARDCODED` constants, `TIER-VIOLATION`s, `VIOLATION`s of canonical values
- Broken `\ref{}` or `\input{}` paths, missing files

### Warnings (Should Fix)
- `STALE` values, `UNDOCUMENTED` functions, `UNTESTED` modules
- Style inconsistencies, heading hierarchy issues

### Info (Optional Improvement)
- Unused bibliography entries, `MAGIC` numbers to document
- Suggestions for better organization

### Summary Statistics
| Category | Count |
|----------|-------|
| Engine modules audited | X |
| Scripts audited | X |
| Test files audited | X |
| LaTeX files audited | X |
| Critical issues | X |
| Warnings | X |
| Info items | X |
| `make test` | PASS/FAIL |
| `make verify` | PASS/FAIL |
