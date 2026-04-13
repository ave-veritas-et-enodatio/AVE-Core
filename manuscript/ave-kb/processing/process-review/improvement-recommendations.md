# Process Reviewer Improvement Backlog

## 2026-04-03 Applied-Vacuum-Engineering KB Pipeline — Error-class propagation rule for accuracy reviewer
Priority: Critical
Target: kb-accuracy-reviewer.md
Section: New section after "Review Scope"
Problem: Accuracy reviewer sampled documents per iteration rather than exhaustively scanning error classes once identified. When ell normalization errors were found in vol2/ch02, vol3 was not scanned; Phase 4b found 20 more instances. When resultbox format errors were found in vol3/cosmology, vol3/condensed-matter and applied-physics were not scanned; Phase 4b found 18 more. Each discovery added a full review iteration.
Proposed: Add "Error-Class Propagation" section requiring that once an error class is identified, the reviewer must scan ALL volumes/chapters for that error class before completing the review. If exhaustive scan is infeasible, flag the error class as "NOT EXHAUSTIVELY SCANNED" in Out of Scope as a risk signal.
Evidence: Accuracy reviews iter-1 through final; human evaluation: "the 'sampling' decision was an attempt at efficiency, but it sacrificed the rigor necessary to make the process work right on the first time through"
Status: pending

## 2026-04-03 Applied-Vacuum-Engineering KB Pipeline — Entry-point domain count audit for structure reviewer
Priority: Critical
Target: kb-structure-reviewer.md
Section: Review Scope > Navigability
Problem: Entry-point was missing Applied Physics domain row for 4 review iterations. Structure reviewer checked link resolution and token count but never cross-checked domain counts between entry-point and volume indexes.
Proposed: Add "Domain count verification" bullet: for each volume row in entry-point, count domains listed, compare to volume index domain count. Mismatch is Critical.
Evidence: Structure review final: "One Critical finding was uncovered that all prior review passes missed: the entry-point's Vol 3 domain routing table omits the Applied Physics domain entirely."
Status: pending

## 2026-04-03 Applied-Vacuum-Engineering KB Pipeline — CLAUDE.md invariant read requirement for content distiller
Priority: Important
Target: kb-content-distiller.md
Section: Before Writing Anything
Problem: Multiple distiller instances produced wrong resultbox heading format (## Resultbox: Title instead of blockquote). Distiller rules do not require reading CLAUDE.md invariants before writing.
Proposed: Add step 3: "Read CLAUDE.md and confirm you can reproduce the exact rendering format for every tcolorbox environment type and notation convention before writing any file."
Evidence: 18 resultbox format violations in vol3/condensed-matter and applied-physics found in Phase 4b. Same error class caught in vol3/cosmology iter-1 but persisted in other chapters.
Status: pending

## 2026-04-03 Applied-Vacuum-Engineering KB Pipeline — Scope exclusion risk flagging for accuracy reviewer
Priority: Important
Target: kb-accuracy-reviewer.md
Section: Output Format
Problem: Out of Scope sections normalized incomplete coverage without distinguishing between routine unsampled areas and known error classes not exhaustively scanned. Coordinator lacked information to direct subsequent review passes.
Proposed: Require Out of Scope to distinguish "not sampled" (routine) from "error class not exhaustively scanned" (risk signal). Category 2 items direct the next review pass to complete those scans first.
Evidence: Accuracy review iter-3 Out of Scope lists unreviewed volumes without flagging that ell normalization error class was not exhaustively scanned.
Status: pending

## 2026-04-03 Applied-Vacuum-Engineering KB Pipeline — Intentional omission exception for accuracy reviewer
Priority: Nice-to-have
Target: kb-accuracy-reviewer.md
Section: Leaf fidelity
Problem: FINDING-001 iter-1 was a Critical finding retracted because summarybox/exercisebox omission was an intentional scope decision. The rule "any omission is Critical" does not account for documented scope exclusions.
Proposed: Add exception: if taxonomy/coordinator explicitly excludes a content category, absence is not a leaf-fidelity violation. Check documented scope exclusions before classifying omission as Critical.
Evidence: Session state: "FINDING-001 RETRACTED: Chapter Summary/Exercises absence is intentional scope decision."
Status: pending
