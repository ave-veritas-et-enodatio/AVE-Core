# Applied Vacuum Engineering (AVE-Core) — Master Build System
# Public release — Volumes 0–6 + Vol 9 Datasheet

# Interpreter resolution (worktree-aware). Git worktrees share the main
# checkout's .venv — each worktree has none of its own (.venv is gitignored).
# Resolve in priority order so `make` works from a worktree as well as the
# main checkout, with NO hardcoded path:
#   1. a repo-local ./.venv (the main checkout, or a worktree that ran setup)
#   2. the .venv in the main working tree, derived from git's common dir
#      (git rev-parse --git-common-dir -> <main>/.git -> <main>/.venv)
#   3. python3 / pytest on PATH (CI clean checkout, or a self-contained venv)
_LOCAL_VENV := $(wildcard ./.venv/bin/python)
_MAIN_VENV  := $(patsubst %/.git,%/.venv,$(abspath $(shell git rev-parse --git-common-dir 2>/dev/null)))
ifneq ($(_LOCAL_VENV),)
  PYTHON ?= ./.venv/bin/python
  PYTEST ?= ./.venv/bin/pytest
else ifneq ($(wildcard $(_MAIN_VENV)/bin/python),)
  PYTHON ?= $(_MAIN_VENV)/bin/python
  PYTEST ?= $(_MAIN_VENV)/bin/pytest
else
  PYTHON ?= python3
  PYTEST ?= python3 -m pytest
endif

# Make THIS working tree's src/ win over the editable-install .pth (which pins
# `ave` to the main checkout's src/). Prepended so `make verify` driver scripts
# import the worktree's OWN ave/* rather than the main checkout's. pytest also
# gets src/ via pyproject.toml [tool.pytest.ini_options] pythonpath. $(CURDIR)
# is the worktree when run from inside it or via `make -C <worktree>`.
export PYTHONPATH := $(CURDIR)/src$(if $(PYTHONPATH),:$(PYTHONPATH),)

LATEX = pdflatex -interaction=nonstopmode -halt-on-error
BIBTEX = bibtex

# Directory Configuration
OUT_DIR = build
SRC_DIR = manuscript

SOURCE_DIR = src
SCRIPT_DIR = $(SOURCE_DIR)/scripts
KB_TOOLS_DIR = manuscript/ave-kb/tools

# KB-metadata target names: single-sourced because they are also referenced as
# user-facing remediation hints in the Python tools ("run `make <name>`").
# Used as the rule target, in .PHONY, and in help so a rename touches one line.
KB_REFRESH = refresh-kb-metadata
KB_VERIFY = verify-kb-metadata

# Volume list — public volumes (0–6) + Vol 9 datasheet (synthesis volume)
VOLUMES = vol_0_engineering_compendium vol_1_foundations vol_2_subatomic vol_3_macroscopic vol_4_engineering vol_5_biology vol_6_periodic_table vol_9_vacuum_datasheet

# Standalone papers — release artifacts on a submission-gated lifecycle.
# Deliberately NOT part of `all`/`pdf`: the committed PDF is the artifact of
# record for a pre-registered document; it is rebuilt only via `make paper`.
PAPER_DIR = papers/2026_birefringence_letter
PAPER_JOB = sve_vacuum_birefringence_letter

# LEGACY per-lane number-check target names. FROZEN 2026-08-06 at the umbrella-glob
# adoption (see the UMBRELLA-GLOB section below). This is the complete set of
# per-lane target names that existed when auto-discovery landed. They are KEPT, as
# thin one-line aliases, because a two-engine census (`git grep` + `grep -r`, run
# 2026-08-06) found 24 corpus references naming them -- including sites inside
# FROZEN prereg and result documents, and inside checker-script docstrings, that
# cannot be rewritten to point somewhere else.
#
# ***APPEND NOTHING TO THIS LIST.*** A new lane's checker is auto-discovered from
# `research/drivers/*_number_check.py` and requires ZERO Makefile edits -- no
# .PHONY entry, no `verify:` prerequisite, no help line, no target block. This
# variable exists so the shared `.PHONY` line is structurally final rather than
# final by promise.
LEGACY_LANE_CHECK_ALIASES = \
	verify-coldq-v2-number-check \
	verify-coldq-v22-number-check \
	verify-coldq-v24-number-check \
	verify-coldq-polar-number-check \
	verify-coldq-axial-rhob-number-check \
	verify-echo-delay-number-check \
	verify-echo-delay-v2-number-check \
	verify-two-band-kp-number-check \
	verify-last-bond-number-check \
	verify-last-bond-g-rho2-rerun-number-check \
	verify-srs-twist-number-check \
	verify-approach-leak-number-check \
	verify-approach-leak-v2-number-check

.PHONY: all clean distclean verify $(KB_VERIFY) $(KB_REFRESH) refresh-predictions kb-claim-stats verify-md-links verify-inter-repo-links verify-provenance-stamps verify-frozen-provenance verify-rule12-freeze verify-lane-number-checks refresh-provenance-baseline framing-audit verify-anchor-content verify-new-cite-excerpts verify-engine-capability-anchors test test-engine test-genesis test-tools pdf pdf_manuscript paper figures help vol0 vol1 vol2 vol3 vol4 vol5 vol6 vol9 setup gamma-census $(LEGACY_LANE_CHECK_ALIASES)

help:
	@echo "Applied Vacuum Engineering (AVE-Core) Build System"
	@echo "--------------------------------------------------"
	@echo "  make setup                : bootstrap project"
	@echo "  make all                  : Run verify, then compile all PDFs"
	@echo "  make verify               : Run physics verification protocols (The Kernel Check) and kb claim id check"
	@echo "  make $(KB_REFRESH)  : Regenerate derived KB metadata (subtree-claims, solidity, claim index)"
	@echo "  make refresh-predictions  : Regenerate derived predictions-manifest fields (axioms_used from the claim DAG)"
	@echo "  make kb-claim-stats       : Print claim-graph counts + solidity build-band distribution (read-only)"
	@echo "  make verify-md-links      : Check Markdown link integrity + cited-id validity + manuscript kbleaf tex-cites (inter-repo: warn)"
	@echo "  make verify-inter-repo-links : Same, but broken inter-repo links also gate (inter-repo: error)"
	@echo "  make verify-provenance-stamps : Check research/ provenance stamps carry a resolvable artifact reference (baseline-gated)"
	@echo "  make verify-frozen-provenance : Check research/ result-doc Frozen-label criteria appear byte-identically in the lane prereg (date-gated)"
	@echo "  make verify-rule12-freeze : Rule-12 append-only GATE — every freeze stamp still matches its base commit + every note the DETECTOR RECOGNISES carries a stamp; prints its own blind-spot counts and stamp coverage (gating; runs its mutation receipt)"
	@echo "  make verify-lane-number-checks : Run EVERY research/drivers/*_number_check.py (auto-discovered) + each one's mutation receipt (gating)"
	@echo "     ...one checker only : make verify-lane-number-checks LANE_CHECK_FILTER=<script-stem>   (e.g. LANE_CHECK_FILTER=srs_twist_coefficient_number_check)"
	@echo "     legacy per-lane aliases (frozen set, kept for corpus cites): $(LEGACY_LANE_CHECK_ALIASES)"
	@echo "  make refresh-provenance-baseline : Regenerate the grandfather baseline from the live scan (allowed to shrink)"
	@echo "  make framing-audit        : Scan corpus for reviewer-misread framing anti-patterns (advisory)"
	@echo "  make verify-anchor-content : Check cited path:NN vs adjacent backtick excerpt drift (WARN-CLASS advisory)"
	@echo "  make verify-new-cite-excerpts : Require a verbatim excerpt beside every line-cite this branch ADDS to the KB (gating; CITE_BASE=<ref>)"
	@echo "  make verify-engine-capability-anchors : Fail-loud text-anchors for loop-gap doctrine cells in engine_capability_matrix.yaml"
	@echo "  make gamma-census         : Signed-Gamma corpus census + reconciliation of the prior sweeps (SURVEY; never gates)"
	@echo "  make test                 : Run unit tests, bedrock keepers (src/tests + kb tools; engine-sims excluded)"
	@echo "  make test-engine          : Run slow engine-simulation tests (opt-in; -m engine_sim)"
	@echo "  make test-genesis         : Run genesis / srs research drivers (opt-in, not default CI)"
	@echo "  make test-tools           : Run KB tooling tests only (manuscript/ave-kb/tools/tests)"
	@echo "  make pdf                  : Compile all 8 public volumes (Vols 0-6 + Vol 9 Datasheet)"
	@echo "  make pdf_manuscript       : Compile manuscript volumes"
	@echo "  make paper                : Rebuild the birefringence Letter PDF ($(PAPER_DIR)/$(PAPER_JOB).pdf; NOT part of 'all')"
	@echo "  make vol0                 : Vol 0:  The Engineering Compendium"
	@echo "  make vol1                 : Vol I:  Foundations & Universal Operators"
	@echo "  make vol2                 : Vol II: The Subatomic Lattice"
	@echo "  make vol3                 : Vol III: The Macroscopic Continuum"
	@echo "  make vol4                 : Vol IV: Applied Impedance Engineering"
	@echo "  make vol5                 : Vol V:  Topological Biology"
	@echo "  make vol6                 : Vol VI: The Periodic Table"
	@echo "  make vol9                 : Vol IX: The Vacuum Datasheet (synthesis volume)"
	@echo "  make figures              : Generate particle topology figure suite"
	@echo "  make clean                : Remove auxiliary build artifacts (preserves PDFs)"
	@echo "  make distclean            : Remove ALL build artifacts including PDFs"

all: verify pdf

setup:
	@./setup.sh

# =============================================================================
# 1. Physics Verification (The "Simulate to Verify" Protocol)
# =============================================================================
verify: $(KB_VERIFY) verify-md-links verify-provenance-stamps verify-frozen-provenance verify-rule12-freeze verify-lane-number-checks
# UMBRELLA-GLOB ADOPTION 2026-08-06: the thirteen per-lane `verify-*-number-check`
# prerequisites that used to be listed on the line above are GONE FROM THIS LINE and
# from nowhere else -- `verify-lane-number-checks` now auto-discovers and runs all
# seventeen `research/drivers/*_number_check.py` checkers plus the eight mutation
# receipts, which is the identical execution multiset (measured before/after on the
# same tree: 17 plain + 8 receipts, both sides). The names survive as aliases below.
# This line is now STRUCTURALLY FINAL: a new lane adds nothing to it.
#
# FLAG-SCANFRAG -- REPAIRED UPSTREAM; the v1 target is RESTORED to this chain
# [DATED NOTE 2026-08-06, umbrella-glob adoption: "this chain" is now the single
#  `verify-lane-number-checks` prerequisite rather than a named entry on the line
#  above. `approach_leak_number_check.py` is auto-discovered and still GATES on
#  every `make verify`, with its mutation receipt -- the restoration this block
#  records is intact, only its wiring changed. The block below is preserved
#  verbatim as the history of why it was ever dropped.]
# (AMENDED 2026-08-06, research/2026-08-06_approach-leak-v2_result.md §9.2(c)).
#
# HISTORY, because the previous comment here asserted the fragility as live and it
# is not: `verify-approach-leak-number-check` machine-gates G-DET by re-running the
# v1 driver, whose shipped digest USED TO BE a function of how many tracked files
# existed under manuscript/ research/ src/, so any commit adding one turned it RED.
# That is why it was dropped from this list at the v2 freeze.  The orchestrator has
# since PINNED the v1 driver's scan surface to a commit (approach_leak.py SCAN_PIN,
# v1 tip f3607be8, merged into this branch), so the v1 digest is now a function of a
# COMMIT and not of the working tree.  MEASURED on this merged tree, whose live
# census under the scan directories is 4428 -- TEN above the pinned 4418 (five
# from the v1 lane, five from the v2 lane) -- the v1 target is GREEN and reproduces
# 2af8acfe23aabb96.  Re-measured with an eleventh, deliberately-added tracked file:
# still green, same digest.  The basis for dropping it is void, so it is back.
#
# BOTH targets now gate.  `verify-approach-leak-v2-number-check` remains a STRICT
# SUPERSET of the v1 target's content (v1 doc-numeral registry, v1 gate
# reconciliations, v1 mutation receipt, v1 G-DET under the prereg §3.2 wrapper), so
# the two overlap deliberately -- belt and braces on a gate that has already failed
# once in a way a same-tree live-fire could not see.
	@echo "\n[Verify] Running categorization guards (ledger / wave-speed / theorem keepers)..."
	$(PYTHON) $(SCRIPT_DIR)/verify/categorization_smoke.py
	@echo "\n[Verify] Running DAG Anti-Cheat Scan..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/verify_universe.py
	@echo "\n[Verify] Running FDTD LC Network solvers..."
	$(PYTHON) $(SCRIPT_DIR)/vol_4_engineering/visualize_impedance_rupture.py
	@echo "\n[Verify] Running Macroscopic Mutual Inductance bounds..."
	$(PYTHON) $(SCRIPT_DIR)/vol_4_engineering/simulate_mutual_inductance.py
	@echo "\n[Verify] Running Topological Borromean geometric limits..."
	AVE_VERIFY_NO_WRITE=1 $(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/visualize_topological_bounds.py
	@echo "\n[Verify] Running Ch 8 α closure: Clifford half-cover rigor..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/verify_clifford_half_cover.py
	@echo "\n[Verify] Running Ch 8 α closure: λ_line rigor..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/verify_lambda_line.py
	@echo "\n[Verify] Running Ch 8 α closure: ropelength → Golden Torus..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/ropelength_trefoil_golden_torus.py
	@echo "\n[Verify] Running Ch 8 α closure: multipole decomposition..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/derive_alpha_from_golden_torus.py
	@echo "\n[Verify] Running Vol 2 Ch 7 atomic IE manuscript-table reproducibility..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/verify_atomic_ie_manuscript_table.py
	@echo "\n[Verify] Running defense-context checker (critical-tier gate)..."
	$(PYTHON) $(SCRIPT_DIR)/defense_context_checker.py --severity critical
	@echo "\n[Verify] Running predictions-manifest validator (forward)..."
	$(PYTHON) $(SCRIPT_DIR)/predictions_manifest_validator.py
	@echo "\n[Verify] Running predictions-manifest validator (consistency)..."
	$(PYTHON) $(SCRIPT_DIR)/predictions_manifest_validator.py --manifest manuscript/consistency-manifest.yaml
	@echo "\n[Verify] Running ξ namespace collision guard..."
	$(PYTHON) $(SCRIPT_DIR)/verify_xi_namespace.py
	@echo "\n[Verify] Engine-capability YAML text-anchors (fail-loud)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-engine-capability-anchors.py
	@echo "\n[Verify][advisory] Running anchor-content drift check (WARN-CLASS, non-gating)..."
	-$(PYTHON) $(KB_TOOLS_DIR)/verify-anchor-content.py
	-$(PYTHON) $(KB_TOOLS_DIR)/verify-docket-keys.py
	@TEX_T=$$(git log -1 --format=%ct -- $(PAPER_DIR)/main.tex $(PAPER_DIR)/refs.bib $(PAPER_DIR)/figures 2>/dev/null || echo 0); \
	PDF_T=$$(git log -1 --format=%ct -- $(PAPER_DIR)/$(PAPER_JOB).pdf 2>/dev/null || echo 0); \
	if [ "$${TEX_T:-0}" -gt "$${PDF_T:-0}" ]; then \
		echo "\n[Verify][warn] Letter source ($(PAPER_DIR)) has commits newer than the committed PDF — run 'make paper' and commit $(PAPER_JOB).pdf (warn-only, non-gating)"; \
	fi
	@echo "\n=================================================="
	@echo "[Verify] ALL PHYSICS PROTOCOLS PASSED."
	@echo "=================================================="

$(KB_VERIFY):
	@echo "Running KB claim-quality framework integrity check (read-only)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) $(KB_TOOLS_DIR)/verify-kb-metadata.py

$(KB_REFRESH):
	@echo "Regenerating derived KB metadata fields (subtree-claims, ...)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) $(KB_TOOLS_DIR)/refresh-kb-metadata.py

refresh-predictions:
	@echo "Regenerating derived predictions-manifest fields (axioms_used from claim DAG)..."
	PYTHONPATH=$(SOURCE_DIR) $(PYTHON) $(SCRIPT_DIR)/predictions_manifest_refresh.py

kb-claim-stats:
	@echo "Claim-graph stats summary (counts + solidity build-band distribution, read-only)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) -m kb_cmd stats

# Placed as its OWN target, and placed HERE rather than beside the other
# number-check recipes: PR #854 has open, unmerged edits both to the
# verify-lane-number-checks recipe and to the block after verify-anchor-content,
# and a third edit adjacent to either would collide.  Same gating effect.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-coldq-v22-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=coldq_pole_v2p2_root_number_check

# Placed as its OWN target rather than appended to the verify-lane-number-checks
# recipe: PR #854 and PR #856 both carry open, unmerged edits to that recipe, and
# a third edit inside it would collide.  Same gating effect.  DISCLOSED (prereg
# FLAG-12): the .PHONY line and the verify: prerequisite line ARE shared with
# those branches and are a REAL two-line conflict, not an append-only merge.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-coldq-v24-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=coldq_pole_v2p4_root_number_check

# FIFTH cold-Q number-check target.  Placed as its OWN target rather than
# appended to any existing recipe: the four predecessor cold-Q recipes each
# belong to a different branch's history, and a fifth edit inside any of them
# would collide.  Same gating effect.  DISCLOSED (prereg FLAG-MK): the .PHONY
# line and the verify: prerequisite line ARE shared and are a REAL two-line
# conflict with any other open cold-Q branch, not an append-only merge.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-coldq-polar-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=coldq_polar_family_number_check

# SIXTH lane number-check target.  Placed as its OWN target rather than
# appended to any existing recipe, for the same reason the fifth was: each
# predecessor recipe belongs to a different branch's history.  This one also
# runs the MUTATION RECEIPT, so the gate proves it can FAIL on every invocation
# rather than only when something is already broken.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-echo-delay-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=echo_delay_regulated_sum_number_check
# Wired as its OWN target so no recipe body is shared with any other cold-Q
# lane.  DISCLOSED, carrying v2.4's FLAG-12 forward unchanged: the .PHONY line
# and the verify: prerequisite line ARE shared and are a REAL conflict, not an
# append-only merge.  The polar-family branch (PR #869) edits the same two
# lines.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-coldq-axial-rhob-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=coldq_axial_rhob_number_check

# EIGHTH lane number-check target.  Own target, own recipe body — no recipe line is
# shared with any predecessor lane, so a merge conflict here is impossible.
# DISCLOSED, carrying the v2.4 FLAG-12 / axial-RHO-B disclosure forward unchanged: the
# .PHONY line and the verify: prerequisite line ARE shared with every other lane's
# number-check target and are a REAL union-conflict class — any concurrently-open lane
# that adds a number-check edits the same two lines, and the correct resolution is the
# UNION of all lanes' targets, never a pick-one.  Runs its MUTATION RECEIPT on every
# invocation so the gate is proven fireable, not assumed to be.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-two-band-kp-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=two_band_kp_kinematics_number_check
# SEVENTH lane number-check target.  Placed as its OWN target rather than
# appended to any existing recipe, for the same reason the fifth and sixth
# were: each predecessor recipe belongs to a different branch's history.  Like
# the echo-delay v1 target it also runs the MUTATION RECEIPT, so the gate
# proves it can FAIL on every invocation rather than only when something is
# already broken.
# DISCLOSED, carrying the same FLAG forward unchanged: the .PHONY line and the
# verify: prerequisite line ARE shared with every other lane's number-check
# target and are a REAL two-line union-conflict class with any concurrent
# lane, not an append-only merge.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-echo-delay-v2-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=echo_delay_v2_number_check

# Its OWN target (not appended to verify-lane-number-checks): that recipe already
# carries an open unmerged edit from PR #845, and the umbrella-glob proposal that
# would replace all of these with one wildcard target is PENDING, so a per-lane
# target is still the shipping form.  Same gating effect.
# ADOPTED 2026-08-06 (Rule 12 shape -- the paragraph above is PRESERVED, not edited).
# The umbrella-glob proposal it calls PENDING HAS LANDED; see the UMBRELLA-GLOB
# section further down this file.  "A per-lane target is still the shipping form"
# is HISTORY as of that date: the shipping form is now auto-discovery, and this
# target name survives only as an alias.
# DISCLOSED, carrying the FLAG forward unchanged: the .PHONY line and the verify:
# prerequisite line ARE shared with every other lane's number-check target and are
# a REAL two-line union-conflict class with any concurrent lane, not an
# append-only merge.  This lane touched exactly those two shared lines plus this
# appended block.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-last-bond-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=last_bond_kernel_collapse_number_check
# G-RHO2 RERUN v2 number-check.  Its OWN target with its OWN recipe body -- no recipe
# line is shared with any other lane.  The mutation receipt runs on EVERY invocation, so
# the gate cannot silently degrade into a no-op.  This checker additionally reconciles
# every LABEL in the v2 result doc against the COMPUTED truth in its JSON (verdict,
# every pass/fires flag, the zero-mismatch claim, the byte-untouched claim), so it is a
# gate rather than a checklist.
# DISCLOSED UNION-CONFLICT CLASS, declared at freeze (prereg section 8) and not discovered
# at merge: the `.PHONY` line, the `verify:` prerequisite line and the `help` recipe are
# SHARED with every other lane's number-check target and are a REAL union-conflict class
# with any concurrently open lane -- not an append-only merge.  The correct resolution is
# the UNION of all lanes' targets, never a pick-one.  This lane touched exactly those three
# shared lines plus this appended block.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-last-bond-g-rho2-rerun-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=last_bond_g_rho2_rerun_number_check
# SRS COMPRESSION-TWIST lane number-check.  Its OWN target with its OWN recipe
# body -- no recipe line is shared with any other lane.  The mutation receipt runs
# on EVERY invocation, so the gate cannot silently degrade into a no-op.
# DISCLOSED UNION-CONFLICT CLASS: the `.PHONY` line and the `verify:` prerequisite
# line ARE shared with every other lane's number-check target.  Any concurrently
# open lane adding a number-check edits those same two lines, and the correct
# resolution is the UNION of all lanes' targets -- never a pick-one.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-srs-twist-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=srs_twist_coefficient_number_check

# APPROACH-LEAK lane number-check.  Its OWN target with its OWN recipe body -- no
# recipe line is shared with any other lane.  The mutation receipt runs on EVERY
# invocation, so the gate cannot silently degrade into a no-op.  This target also
# MACHINE-GATES G-DET: the checker re-runs the driver into a temp path via
# APPROACH_LEAK_OUT and requires the recomputed digest to match the shipped one.
# DISCLOSED UNION-CONFLICT CLASS (carried forward unchanged from the last-bond and
# srs-twist lanes): the `.PHONY` line, the `verify:` prerequisite line and the
# `help` block ARE shared with every other lane's number-check target.  Any
# concurrently open lane adding a number-check edits those same lines, and the
# correct resolution is the UNION of all lanes' targets -- never a pick-one.  The
# standing umbrella-glob proposal (one `verify-lane-number-checks` that globs
# `research/drivers/*_number_check.py`) would retire this conflict class entirely
# and REMAINS PENDING; it is not adopted here because adopting it unilaterally
# would change the gate surface of every other open lane.
# ADOPTED 2026-08-06 (Rule 12 shape -- the paragraph above is PRESERVED, not edited).
# The proposal it calls PENDING HAS LANDED; see the UMBRELLA-GLOB section further
# down this file.  Its stated reason for deferral -- "adopting it unilaterally
# would change the gate surface of every other open lane" -- was DISCHARGED by
# measurement rather than waived: the execution multiset is identical before and
# after on the same tree (17 plain runs + 8 mutation receipts on BOTH sides), so
# no lane's gate surface moved.  This block's diagnosis of the conflict class was
# correct and is the reason the class is now retired.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-approach-leak-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=approach_leak_number_check

# APPROACH-LEAK V2 lane number-check.  Its OWN target with its OWN recipe body --
# no recipe line is shared with any other lane.  It MACHINE-GATES G-DET-V2 (re-runs
# the v2 driver into a temp path via APPROACH_LEAK_V2_OUT and requires digest
# equality) and it is a STRICT SUPERSET of `verify-approach-leak-number-check`
# above: it runs that target's entire content by calling the v1 number-check
# module's OWN functions, with v1's G-DET executed in-process under the prereg §3.2
# wrapper.  Both mutation receipts run on EVERY invocation, so neither gate can
# silently degrade into a no-op.  AMENDED 2026-08-06: the v1 target is ALSO back in
# the `verify:` chain above -- the SCANFRAG repair landed upstream and the v1 target
# is green on this merged tree -- so the superset relation is now redundancy rather
# than a substitution.  That redundancy is deliberate and is kept.
# It ALSO gates the AMENDMENT-NCBYTES-2026-08-06 leaf receipt: the pre-amendment v2
# JSON is read out of git by blob hash and the leaf delta recomputed, so "only the
# NC-BYTES block, the digest and _runtime_sec moved" is a GATE, not a sentence.
# DISCLOSED UNION-CONFLICT CLASS (carried forward unchanged from the last-bond,
# srs-twist and approach-leak lanes): the `.PHONY` line, the `verify:` prerequisite
# line and the `help` block ARE shared with every other lane's number-check target.
# Any concurrently open lane adding a number-check edits those same lines, and the
# correct resolution is the UNION of all lanes' targets -- never a pick-one.  The
# standing umbrella-glob proposal (one `verify-lane-number-checks` that globs
# `research/drivers/*_number_check.py`) would retire this conflict class entirely
# and REMAINS PENDING; it is not adopted here because adopting it unilaterally
# would change the gate surface of every other open lane.
# ADOPTED 2026-08-06 (Rule 12 shape -- the paragraph above is PRESERVED, not edited).
# The proposal it calls PENDING HAS LANDED; see the UMBRELLA-GLOB section further
# down this file.  Measured discharge of the deferral reason: identical execution
# multiset before and after on the same tree (17 plain runs + 8 mutation receipts,
# both sides).  The AMENDED-2026-08-06 sentence above about the v1 target being
# "back in the `verify:` chain" still holds -- both v1 and v2 checkers are
# auto-discovered and both gate; only the wiring changed, never the coverage.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-approach-leak-v2-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=approach_leak_v2_number_check

verify-md-links:
	@echo "Checking Markdown link integrity + cited-id validity (inter-repo: warn)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) $(KB_TOOLS_DIR)/verify-md-links.py --inter-repo warn

verify-inter-repo-links:
	@echo "Checking Markdown links incl. inter-repo as gating (inter-repo: error)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) $(KB_TOOLS_DIR)/verify-md-links.py --inter-repo error

verify-provenance-stamps:
	@echo "Checking research/ provenance stamps carry a resolvable artifact reference (baseline-gated)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-provenance-stamps.py

verify-frozen-provenance:
	@echo "Checking research/ result-doc Frozen-label criteria appear byte-identically in the lane prereg (date-gated)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-frozen-provenance.py

# RULE-12 APPEND-ONLY GATE.  Its OWN target with its OWN recipe body -- no recipe
# line is shared with any other check.  The MUTATION RECEIPT runs on EVERY
# invocation (16 arms, ~0.6 s, synthetic fixtures in a throwaway git repo), so the
# gate cannot silently degrade into a no-op: a green `make verify` is also a proof
# that this gate can still FIRE, and that it still STAYS QUIET under the sanctioned
# append.  That second half is not padding -- a gate that reds on the correct
# Rule-12 move gets switched off, and a switched-off gate protects nothing.
#
# DISCLOSED UNION-CONFLICT CLASS (carried forward unchanged from every lane
# number-check block above): the `.PHONY` line, the `verify:` prerequisite line and
# the `help` recipe ARE shared with every other check, and are a REAL union-conflict
# class with any concurrently open lane.  The correct resolution is the UNION of all
# targets, never a pick-one.  This lane touched exactly those three shared lines plus
# this appended block.
verify-rule12-freeze:
	@echo "\n[Verify] Rule-12 append-only gate: mutation receipt (proving the gate can fire AND stay quiet)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-rule12-freeze.py --mutation-receipt
	@echo "\n[Verify] Rule-12 append-only gate: freeze stamps vs their base commits + unstamped-note detector (a green run states what it PROVED, not a universal — read its OK block)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-rule12-freeze.py

# =============================================================================
# UMBRELLA-GLOB LANE NUMBER-CHECKS -- ADOPTED 2026-08-06
# =============================================================================
# ADOPTED 2026-08-06.  The standing umbrella-glob proposal documented in the
# per-lane FLAG blocks ABOVE (search this file for "umbrella-glob proposal") is
# now the shipping form.  Those FLAG blocks are PRESERVED verbatim as history --
# they are the record of a conflict class that was disclosed at freeze by five
# separate lanes and then observed ten times at merge -- and each carries a dated
# ADOPTED pointer back to here.  Nothing about their rationale is retracted; the
# only thing that changed is that the proposal they deferred has landed.
#
# WHAT THIS RETIRES.  Every lane used to add (a) its name to the `.PHONY` line,
# (b) its name to the `verify:` prerequisite line, (c) an echo to the `help`
# recipe, and (d) its own target block.  (a)-(c) are SHARED lines: two concurrent
# lanes touching them conflict on GitHub's server-side merge regardless of the
# union merge driver in `.gitattributes` (same mechanism the docket news-fragments
# convention was adopted for -- see `_orchestration/docket-entries/README.md`).
# Under auto-discovery a new lane edits NONE of those four things: it drops
# `research/drivers/<lane>_number_check.py` in and this target finds it.
#
# THE DISCOVERY CONTRACT, so a lane knows what it is opting into:
#   1. Any `research/drivers/*_number_check.py` is run, plain, exactly once.
#   2. It is then run a second time with `--mutation-receipt` IF AND ONLY IF its
#      own source contains that literal flag.  Every checker in this repo parses
#      the flag by `"--mutation-receipt" in sys.argv` rather than by argparse, so
#      a checker that does NOT implement it silently ignores the flag and re-runs
#      the plain check -- a double-run masquerading as a gate.  Source-grep is the
#      only honest detector available, and it is exact: measured 2026-08-06, the
#      grep set is byte-identical to the set of 8 lanes that had hand-wired a
#      receipt line, with 0 false positives and 0 false negatives over 17 files.
#   3. Fail-fast: the first non-zero exit stops the run and the failing checker is
#      named with its mode (plain vs mutation receipt) and its exit code.
#   4. Discovery is measured at RUN time by the shell, not at parse time by
#      `$(wildcard)`, so a checker added while make is resolving is still seen.
#      An EMPTY discovery set is a hard error, not a silent pass -- a glob that
#      matches nothing is exactly how this kind of gate rots into a no-op.
#   5. HARDENED 2026-08-06 (review finding A1).  The receipt detector distinguishes
#      grep's THREE outcomes, not two: exit 0 = match (run the receipt), exit 1 =
#      no match (skip it), anything else = grep ITSELF failed, which is a HARD
#      FAILURE of the umbrella (exit 3).  The earlier `if grep -q ...; then/else`
#      form folded "grep broke" into "no receipt", so a broken detector narrowed
#      the receipt set toward ZERO while every checker reported `no-receipt` and
#      the gate still reported OK.  Demonstrated with a PATH shim; see the docket.
#
# `LANE_CHECK_FILTER=<script-stem>` restricts the run to one checker.  That is the
# single mechanism the legacy per-lane aliases below are built on, so an alias and
# the umbrella can never drift apart in HOW a checker is invoked.
#
# HARDENED 2026-08-06 (review finding B1, BLOCKING).  The filter SELECTS FROM the
# expanded discovery set by exact path equality; it does NOT build a path.  The
# earlier form concatenated `$(LANE_CHECK_DIR)/$(LANE_CHECK_FILTER).py` and gated
# it on `[ -f ]` alone, so the filter could reach ANY .py file in research/drivers/
# -- including the bare lane DRIVERS, 14 of which are same-prefix siblings of a
# checker (`approach_leak.py` next to `approach_leak_number_check.py`).  Running a
# bare driver from a `verify-*` target is not a read-only gate: drivers WRITE their
# results JSON, so `LANE_CHECK_FILTER=approach_leak` mutated a gated baseline and
# still printed `[lane-checks] OK` with exit 0.  Selecting from the glob makes that
# unreachable by construction rather than by a filename convention.
LANE_CHECK_DIR    = research/drivers
LANE_CHECK_GLOB   = $(LANE_CHECK_DIR)/*_number_check.py
LANE_CHECK_FILTER ?=

verify-lane-number-checks:
	@echo "Checking research-lane result-doc numeric tokens against their shipped JSON sources (gating)..."
	@set -u; \
	discovered=$$(ls $(LANE_CHECK_GLOB) 2>/dev/null); \
	if [ -z "$$discovered" ]; then \
		echo "[lane-checks] *** DISCOVERY ERROR: no checker matched $(LANE_CHECK_GLOB)"; \
		echo "[lane-checks]     an empty glob is treated as a FAILURE, never as a pass."; \
		exit 2; \
	fi; \
	if [ -n "$(LANE_CHECK_FILTER)" ]; then \
		want="$(LANE_CHECK_DIR)/$(LANE_CHECK_FILTER).py"; \
		checkers=""; \
		for d in $$discovered; do \
			if [ "$$d" = "$$want" ]; then checkers="$$d"; fi; \
		done; \
		if [ -z "$$checkers" ]; then \
			echo "[lane-checks] *** FILTER ERROR: LANE_CHECK_FILTER=$(LANE_CHECK_FILTER) does not name a MEMBER of the discovery set."; \
			echo "[lane-checks]     The filter SELECTS FROM $(LANE_CHECK_GLOB) by exact path equality."; \
			echo "[lane-checks]     It can never reach a path outside that set -- in particular it can"; \
			echo "[lane-checks]     never execute a bare driver, which may WRITE a gated JSON baseline."; \
			exit 2; \
		fi; \
		echo "[lane-checks] filtered to 1 checker (LANE_CHECK_FILTER=$(LANE_CHECK_FILTER))"; \
	else \
		checkers="$$discovered"; \
		echo "[lane-checks] auto-discovered $$(echo $$checkers | wc -w | tr -d ' ') checker(s) via $(LANE_CHECK_GLOB)"; \
	fi; \
	nplain=0; nreceipt=0; nskip=0; \
	for c in $$checkers; do \
		echo "[lane-checks] RUN      $$c"; \
		$(PYTHON) "$$c"; rc=$$?; \
		if [ $$rc -ne 0 ]; then \
			echo "[lane-checks] *** FAILED (plain run): $$c  [exit $$rc]"; \
			exit $$rc; \
		fi; \
		nplain=$$((nplain+1)); \
	done; \
	for c in $$checkers; do \
		grep -qF -e '--mutation-receipt' "$$c"; g=$$?; \
		if [ $$g -eq 0 ]; then \
			echo "[lane-checks] RECEIPT  $$c --mutation-receipt"; \
			$(PYTHON) "$$c" --mutation-receipt; rc=$$?; \
			if [ $$rc -ne 0 ]; then \
				echo "[lane-checks] *** FAILED (mutation receipt): $$c  [exit $$rc]"; \
				exit $$rc; \
			fi; \
			nreceipt=$$((nreceipt+1)); \
		elif [ $$g -eq 1 ]; then \
			echo "[lane-checks] no-receipt $$c (source declares no --mutation-receipt handler; passing the flag would silently re-run the plain check)"; \
			nskip=$$((nskip+1)); \
		else \
			echo "[lane-checks] *** RECEIPT-DETECTOR ERROR: grep exited $$g on $$c."; \
			echo "[lane-checks]     grep exit 0 = match, 1 = no match, >=2 = grep ITSELF failed."; \
			echo "[lane-checks]     A broken detector narrows the receipt set toward ZERO while every"; \
			echo "[lane-checks]     checker still reports 'no-receipt' and the gate still reports OK."; \
			echo "[lane-checks]     Refusing to report a green gate on an unknown receipt set."; \
			exit 3; \
		fi; \
	done; \
	echo "[lane-checks] OK -- $$nplain plain run(s), $$nreceipt mutation receipt(s), $$nskip checker(s) with no receipt support"

refresh-provenance-baseline:
	@echo "Regenerating the provenance-stamp grandfather baseline from the live scan (allowed to shrink)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-provenance-stamps.py --update-baseline

framing-audit:
	@echo "[Framing] Full defense-context anti-pattern scan (advisory; warn/info do not gate)..."
	$(PYTHON) $(SCRIPT_DIR)/defense_context_checker.py

# Survey instrument, deliberately NOT a `verify:` prerequisite. Nobody has ruled
# what the right signed-Gamma count is, so gating the build on an unadjudicated
# census would be a checklist wearing a gate's clothes. This target RUNS the
# census; nothing FAILS on the count. The only non-zero exit is 3, raised when
# the script's own two scan methods disagree -- an instrument bug, not a corpus
# finding.
gamma-census:
	@echo "[Census] Signed-Gamma corpus census + reconciliation (survey; never gates)..."
	$(PYTHON) $(SCRIPT_DIR)/signed_gamma_census.py --reconcile

# Cite-rot option (3): the NEW-cite excerpt ratchet. Deliberately NOT a
# `verify:` prerequisite -- it needs a base ref, which a detached or offline
# local run does not have, and `verify` must stay runnable anywhere. It IS a
# real gate: nonzero exit on any line-cite this branch ADDS to the
# canonical-authority surface without an adjacent verbatim excerpt. Override
# the base with `make verify-new-cite-excerpts CITE_BASE=<ref>`.
CITE_BASE ?= origin/main
verify-new-cite-excerpts:
	@echo "Checking every line-cite added vs $(CITE_BASE) carries an adjacent verbatim excerpt (gating)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-anchor-content.py --new-cites $(CITE_BASE)

verify-anchor-content:
	@echo "[Anchor] Cited-line vs quoted-excerpt drift check (WARN-CLASS advisory; always exit 0)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-anchor-content.py

# Fail-loud text-anchors for loop-gap-doctrine cells in engine_capability_matrix.yaml.
# Own target so a missing recipe cannot silently drop the class-kill; also invoked
# from the `verify` recipe body (not the `verify:` prerequisite line — that line
# is a union-conflict class). Matching does not strip `**` (C6 receipt).
verify-engine-capability-anchors:
	@echo "[Anchors] engine_capability_matrix.yaml doctrine text-anchors (fail-loud)..."
	$(PYTHON) $(KB_TOOLS_DIR)/verify-engine-capability-anchors.py

# Placed as its OWN target rather than appended to the verify-lane-number-checks
# recipe: PR #845 has an open, unmerged edit to that recipe, and a second
# addition to the same three-line block would collide.  Same gating effect.
# ALIAS since 2026-08-06 (umbrella-glob): body is one filtered delegation; the checker gates via auto-discovery, not via this name. Comment above preserved as history.
verify-coldq-v2-number-check:
	@$(MAKE) --no-print-directory verify-lane-number-checks LANE_CHECK_FILTER=coldq_pole_v2_number_check


# =============================================================================
# 2. Unit Testing
# =============================================================================
test: test-tools
	@echo "[Test] Running Unit Tests (bedrock keepers; engine-sims excluded)..."
	# Scope to the unit-test tree only. src/scripts/**/*_test.py are runnable
	# analysis/forward-prediction DRIVERS (each has a __main__ block), not pytest
	# tests; collecting them mis-runs driver functions as tests (and errors on
	# non-fixture positional args like test_wave_speed(N, ...)). Drivers run
	# standalone / via `make verify`, not here.
	# `-m "not engine_sim"` routes the slow tier-1/2 engine-simulation tests to
	# the opt-in `make test-engine` lane (CI partition prereg 2026-06-13).
	# `-n auto` (pytest-xdist): parallelize across cores. The ~1830-test suite ran
	# ~30 min serial and hit the CI timeout; parallel run keeps the PR gate well under.
	# `--timeout` (pytest-timeout): per-test hang guard — a single stuck test fails
	# itself instead of silently eating the whole job budget. NOT on test-engine
	# (those are legitimately-slow sims; the gate's slowest keeper is now ~50s).
	$(PYTEST) $(SOURCE_DIR)/tests -m "not engine_sim" -n auto --timeout=180 --timeout-method=thread \
		--ignore=$(SOURCE_DIR)/tests/test_mass_sector_a1_port.py
	# Serial tail (2026-07-17): the A1-port suite transiently spikes ~340 MB; when
	# xdist packing lands it late in the schedule it stacks on per-worker memory
	# accumulation and the 2-core CI runner OOM-kills the worker ("node down",
	# schedule-dependent so branch CI can red while main greens). A fresh serial
	# process gives the spike a zero baseline; costs ~15 s.
	$(PYTEST) $(SOURCE_DIR)/tests/test_mass_sector_a1_port.py --timeout=180 --timeout-method=thread

test-engine:
	@echo "[Test] Running engine-simulation tests (opt-in; slow tier-1/2)..."
	# `engine_sim`-marked: full-resolution harness/eigensolve/genesis drivers,
	# excluded from the PR-blocking gate on cost+role (never on physics status).
	# Run this lane (and CI's engine job) for engine-development coverage.
	# `--timeout=1800` (30 min/test, ~7× the slowest documented driver): converts a
	# genuinely-hung sim into a bounded per-test failure instead of a silent 60-min job
	# cancel. Lane stays SERIAL by design (these heavy N=24-48 sims OOM under xdist —
	# the very crash this routing avoids in the gate), so no `-n auto` here.
	$(PYTEST) $(SOURCE_DIR)/tests -m engine_sim --timeout=1800 --timeout-method=thread

test-genesis:
	@echo "[Test] Running genesis / srs research drivers (opt-in, not default CI)..."
	@files=$$(find $(SOURCE_DIR)/tests -maxdepth 1 \( \
		-name 'test_chiral_lattice_v*.py' -o \
		-name 'test_chiral_lattice_phase*.py' -o \
		-name 'test_chiral_lattice_vector_phase*.py' -o \
		-name 'test_genesis_*.py' \) 2>/dev/null); \
	if [ -z "$$files" ]; then echo "[Test] No genesis test files present."; exit 0; fi; \
	$(PYTEST) $$files

test-tools:
	@echo "[Test] Running KB tools tests..."
	# The kb tooling tree (kb_cmd query CLI, kb_index_lib, refresh/verify scripts)
	# lives under $(KB_TOOLS_DIR), outside src/. PYTHONPATH makes kb_cmd +
	# kb_index_lib importable as siblings (no sys.path manipulation in the code).
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTEST) $(KB_TOOLS_DIR)/tests

# =============================================================================
# 3. Manuscript Compilation
# =============================================================================

# --- Single volume compilation macro ---
define COMPILE_VOL
	@mkdir -p $(OUT_DIR)/aux
	@echo "[Build] Compiling $(1)..."
	@rm -f $(OUT_DIR)/aux/$(1).out $(OUT_DIR)/aux/$(1).aux $(OUT_DIR)/aux/$(1).toc
	@(cd $(SRC_DIR)/$(1) && $(LATEX) -jobname=$(1) -output-directory=../../$(OUT_DIR)/aux main.tex)
	@if [ -f $(SRC_DIR)/bibliography.bib ]; then \
		cp $(SRC_DIR)/bibliography.bib $(OUT_DIR)/; \
		(cd $(OUT_DIR)/aux && $(BIBTEX) $(1) || true); \
		(cd $(SRC_DIR)/$(1) && $(LATEX) -jobname=$(1) -output-directory=../../$(OUT_DIR)/aux main.tex); \
	fi
	@(cd $(SRC_DIR)/$(1) && $(LATEX) -jobname=$(1) -output-directory=../../$(OUT_DIR)/aux main.tex)
	@$(PYTHON) $(SCRIPT_DIR)/check_latex_margins.py $(OUT_DIR)/aux/$(1).log
	@mv $(OUT_DIR)/aux/$(1).pdf $(OUT_DIR)/
	@echo "[Build] $(1).pdf → $(OUT_DIR)/"
endef

pdf: pdf_manuscript

# The Letter builds ONLY on demand — see the PAPER_DIR comment above.
paper:
	@echo "[Paper] Building the birefringence Letter ($(PAPER_JOB).pdf)..."
	cd $(PAPER_DIR) && latexmk -pdf -jobname=$(PAPER_JOB) main.tex
	@echo "[Paper] Done: $(PAPER_DIR)/$(PAPER_JOB).pdf"

pdf_manuscript:
	@echo "[Build] Compiling Volumes 0–VI + Vol IX (two-pass for cross-volume xr-hyper resolution)..."
	@echo "[Build] === Pass 1 (collect aux files) ==="
	@for dir in $(VOLUMES); do \
		$(MAKE) --no-print-directory _compile_vol VOL=$$dir; \
	done
	@echo "[Build] === Pass 2 (resolve cross-volume refs) ==="
	@for dir in $(VOLUMES); do \
		$(MAKE) --no-print-directory _compile_vol VOL=$$dir; \
	done
	@echo "[Build] All 8 volume PDFs generated in $(OUT_DIR)/"

_compile_vol:
	$(call COMPILE_VOL,$(VOL))

# --- Individual volume targets ---
# Cross-volume xr-hyper architecture (A-034 expansion 2026-05-16):
#   Vol 1 is the base (defines ch:alpha_golden_torus, etc.)
#   Vol 0 + Vol 3 are secondary bases (Vol 0 defines app:universal_saturation_kernel
#       in backmatter Ch 7; Vol 3 defines sec:tki_strain_snap in Ch 4)
#   Vol 0 ↔ Vol 3 are mutually pulling — full resolution requires the two-pass loop
#       in pdf_manuscript above (single-volume targets below resolve to single-pass
#       per call; users invoking specific vol targets should run them twice if
#       cross-vol refs from Vol 0 ↔ Vol 3 are load-bearing).
#   The \IfFileExists guard in each main.tex allows standalone single-pass builds
#   to fall through silently with unresolved refs.
vol0: vol1 vol3
	$(call COMPILE_VOL,vol_0_engineering_compendium)

vol1:
	$(call COMPILE_VOL,vol_1_foundations)

vol2: vol1 vol3 vol0
	$(call COMPILE_VOL,vol_2_subatomic)

vol3: vol1
	$(call COMPILE_VOL,vol_3_macroscopic)

vol4: vol1 vol3 vol0
	$(call COMPILE_VOL,vol_4_engineering)

vol5: vol1 vol3 vol0
	$(call COMPILE_VOL,vol_5_biology)

vol6: vol1 vol3 vol0
	$(call COMPILE_VOL,vol_6_periodic_table)

# Vol 9: The Vacuum Datasheet (synthesis volume; cross-references Vols 1/3/4/0)
vol9: vol1 vol3 vol4 vol0
	$(call COMPILE_VOL,vol_9_vacuum_datasheet)

# =============================================================================
# 4. Figure Generation
# =============================================================================
figures:
	@echo "[Figures] Generating particle topology suite..."
	$(PYTHON) $(SCRIPT_DIR)/vol_2_subatomic/generate_particle_topology_suite.py
	@echo "[Figures] Regenerating electron topology figure..."
	$(PYTHON) $(SCRIPT_DIR)/vol_2_subatomic/simulate_electron_topology.py
	@echo "[Figures] Regenerating gyroscopic spin simulator transition..."
	$(PYTHON) $(SCRIPT_DIR)/vol_2_subatomic/simulate_gyroscopic_spin.py
	@echo "[Figures] All figures generated."

# =============================================================================
# 5. Cleanup
# =============================================================================
clean:
	@echo "[Clean] Removing auxiliary build artifacts AND wiping compiled PDFs..."
	rm -rf $(OUT_DIR)/aux
	rm -f $(OUT_DIR)/*.pdf
	@echo "[Clean] Removing in-tree LaTeX artifacts..."
	@find $(SRC_DIR) future_work papers \
		\( -name "*.aux" -o -name "*.toc" -o -name "*.lof" -o -name "*.lot" \
		   -o -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.out" \
		   -o -name "*.log" -o -name "*.synctex.gz" -o -name "*.bbl" \
		   -o -name "*.blg" \) -delete 2>/dev/null || true
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "[Clean] Done."

distclean: clean
	@echo "[DistClean] Removing ALL build artifacts including PDFs..."
	rm -rf $(OUT_DIR)
	@echo "[DistClean] Done."
