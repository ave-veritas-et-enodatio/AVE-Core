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

.PHONY: all clean distclean verify $(KB_VERIFY) $(KB_REFRESH) refresh-predictions kb-claim-stats verify-md-links verify-inter-repo-links verify-provenance-stamps verify-frozen-provenance verify-lane-number-checks verify-coldq-v2-number-check verify-coldq-v22-number-check refresh-provenance-baseline framing-audit verify-anchor-content verify-new-cite-excerpts test test-engine test-genesis test-tools pdf pdf_manuscript paper figures help vol0 vol1 vol2 vol3 vol4 vol5 vol6 vol9 setup verify-coldq-v24-number-check verify-coldq-polar-number-check verify-echo-delay-number-check verify-coldq-axial-rhob-number-check verify-two-band-kp-number-check verify-echo-delay-v2-number-check verify-last-bond-number-check verify-srs-twist-number-check gamma-census verify-approach-leak-number-check verify-approach-leak-v2-number-check verify-last-bond-g-rho2-rerun-number-check verify-iomega-law-number-check

help:
	@echo "Applied Vacuum Engineering (AVE-Core) Build System"
	@echo "--------------------------------------------------"
	@echo "  make setup                : bootstrap project"
	@echo "  make all                  : Run verify, then compile all PDFs"
	@echo "  make verify               : Run physics verification protocols (The Kernel Check) and kb claim id check"
	@echo "  make $(KB_REFRESH)  : Regenerate derived KB metadata (subtree-claims, solidity, claim index)"
	@echo "  make kb-claim-stats       : Print claim-graph counts + solidity build-band distribution (read-only)"
	@echo "  make verify-md-links      : Check Markdown link integrity + cited-id validity + manuscript kbleaf tex-cites (inter-repo: warn)"
	@echo "  make verify-inter-repo-links : Same, but broken inter-repo links also gate (inter-repo: error)"
	@echo "  make verify-provenance-stamps : Check research/ provenance stamps carry a resolvable artifact reference (baseline-gated)"
	@echo "  make verify-frozen-provenance : Check research/ result-doc Frozen-label criteria appear byte-identically in the lane prereg (date-gated)"
	@echo "  make verify-lane-number-checks : Check research-lane result-doc numeric tokens against their shipped JSON sources (gating)"
	@echo "  make verify-coldq-v2-number-check : Check the cold-Q v2.1 result-doc numerals against its shipped JSON (gating)"
	@echo "  make verify-coldq-v22-number-check : Check the cold-Q v2.2 root-certification result-doc numerals against its shipped JSON (gating)"
	@echo "  make verify-coldq-v24-number-check : Check the cold-Q v2.4 root-certification result-doc numerals against its shipped JSON (gating)"
	@echo "  make verify-coldq-polar-number-check : Check the cold-Q POLAR FAMILY result-doc numerals against its shipped JSON (gating)"
	@echo "  make verify-echo-delay-number-check : Check the ECHO-DELAY regulated-sum result-doc numerals + mutation receipt (gating)"
	@echo "  make verify-coldq-axial-rhob-number-check : Check the cold-Q axial RHO-B result-doc numerals against its shipped JSON (gating)"
	@echo "  make verify-echo-delay-v2-number-check : Check the ECHO-DELAY v2 rerun + Y8 reach-through result-doc numerals + mutation receipt (gating)"
	@echo "  make verify-last-bond-g-rho2-rerun-number-check : Check the G-RHO2 rerun v2 result-doc numerals + mutation receipt (gating)"
	@echo "  make verify-srs-twist-number-check : Check the srs compression-twist result-doc numerals + mutation receipt (gating)"
	@echo "  make verify-approach-leak-number-check : Check the approach-leak result-doc numerals + G-DET re-run + mutation receipt (gating)"
	@echo "  make verify-approach-leak-v2-number-check : Check the approach-leak V2 result-doc numerals + G-DET-V2 re-run + BOTH mutation receipts, and the PRESERVED v1 target content (gating)"
	@echo "  make verify-iomega-law-number-check : Check the I_omega(A)-law result-doc numerals + law-check re-run + classification completeness + quote registry + mutation receipts (gating)"
	@echo "  make refresh-provenance-baseline : Regenerate the grandfather baseline from the live scan (allowed to shrink)"
	@echo "  make framing-audit        : Scan corpus for reviewer-misread framing anti-patterns (advisory)"
	@echo "  make verify-anchor-content : Check cited path:NN vs adjacent backtick excerpt drift (WARN-CLASS advisory)"
	@echo "  make verify-new-cite-excerpts : Require a verbatim excerpt beside every line-cite this branch ADDS to the KB (gating; CITE_BASE=<ref>)"
	@echo "  make gamma-census         : Signed-Gamma corpus census + reconciliation of the prior sweeps (SURVEY; never gates)"
	@echo "  make test                 : Run unit tests, bedrock keepers (src/tests + kb tools; engine-sims excluded)"
	@echo "  make test-engine          : Run slow engine-simulation tests (opt-in; -m engine_sim)"
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
verify: $(KB_VERIFY) verify-md-links verify-provenance-stamps verify-frozen-provenance verify-lane-number-checks verify-coldq-v2-number-check verify-coldq-v22-number-check verify-coldq-v24-number-check verify-coldq-polar-number-check verify-echo-delay-number-check verify-coldq-axial-rhob-number-check verify-two-band-kp-number-check verify-echo-delay-v2-number-check verify-last-bond-number-check verify-last-bond-g-rho2-rerun-number-check verify-srs-twist-number-check verify-approach-leak-number-check verify-approach-leak-v2-number-check verify-iomega-law-number-check
# FLAG-SCANFRAG -- REPAIRED UPSTREAM; the v1 target is RESTORED to this chain
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
	@echo "\n[Verify] Running predictions-manifest validator..."
	$(PYTHON) $(SCRIPT_DIR)/predictions_manifest_validator.py
	@echo "\n[Verify] Running ξ namespace collision guard..."
	$(PYTHON) $(SCRIPT_DIR)/verify_xi_namespace.py
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
verify-coldq-v22-number-check:
	@echo "Checking the cold-Q v2.2 root-certification result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/coldq_pole_v2p2_root_number_check.py

# Placed as its OWN target rather than appended to the verify-lane-number-checks
# recipe: PR #854 and PR #856 both carry open, unmerged edits to that recipe, and
# a third edit inside it would collide.  Same gating effect.  DISCLOSED (prereg
# FLAG-12): the .PHONY line and the verify: prerequisite line ARE shared with
# those branches and are a REAL two-line conflict, not an append-only merge.
verify-coldq-v24-number-check:
	@echo "Checking the cold-Q v2.4 root-certification result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/coldq_pole_v2p4_root_number_check.py

# FIFTH cold-Q number-check target.  Placed as its OWN target rather than
# appended to any existing recipe: the four predecessor cold-Q recipes each
# belong to a different branch's history, and a fifth edit inside any of them
# would collide.  Same gating effect.  DISCLOSED (prereg FLAG-MK): the .PHONY
# line and the verify: prerequisite line ARE shared and are a REAL two-line
# conflict with any other open cold-Q branch, not an append-only merge.
verify-coldq-polar-number-check:
	@echo "Checking the cold-Q POLAR FAMILY result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/coldq_polar_family_number_check.py

# SIXTH lane number-check target.  Placed as its OWN target rather than
# appended to any existing recipe, for the same reason the fifth was: each
# predecessor recipe belongs to a different branch's history.  This one also
# runs the MUTATION RECEIPT, so the gate proves it can FAIL on every invocation
# rather than only when something is already broken.
verify-echo-delay-number-check:
	@echo "Checking the ECHO-DELAY regulated-sum result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/echo_delay_regulated_sum_number_check.py
	@echo "Mutation receipt: the numeral checker must FAIL on perturbed sources..."
	$(PYTHON) research/drivers/echo_delay_regulated_sum_number_check.py --mutation-receipt
# Wired as its OWN target so no recipe body is shared with any other cold-Q
# lane.  DISCLOSED, carrying v2.4's FLAG-12 forward unchanged: the .PHONY line
# and the verify: prerequisite line ARE shared and are a REAL conflict, not an
# append-only merge.  The polar-family branch (PR #869) edits the same two
# lines.
verify-coldq-axial-rhob-number-check:
	@echo "Checking the cold-Q axial RHO-B result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/coldq_axial_rhob_number_check.py

# EIGHTH lane number-check target.  Own target, own recipe body — no recipe line is
# shared with any predecessor lane, so a merge conflict here is impossible.
# DISCLOSED, carrying the v2.4 FLAG-12 / axial-RHO-B disclosure forward unchanged: the
# .PHONY line and the verify: prerequisite line ARE shared with every other lane's
# number-check target and are a REAL union-conflict class — any concurrently-open lane
# that adds a number-check edits the same two lines, and the correct resolution is the
# UNION of all lanes' targets, never a pick-one.  Runs its MUTATION RECEIPT on every
# invocation so the gate is proven fireable, not assumed to be.
verify-two-band-kp-number-check:
	@echo "Checking the two-band / k.p kinematics result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/two_band_kp_kinematics_number_check.py
	@echo "Mutation receipt: the numeral checker must FAIL on perturbed shipped values..."
	$(PYTHON) research/drivers/two_band_kp_kinematics_number_check.py --mutation-receipt
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
verify-echo-delay-v2-number-check:
	@echo "Checking the ECHO-DELAY v2 rerun + Y8 reach-through result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/echo_delay_v2_number_check.py
	@echo "Mutation receipt: the numeral checker must FAIL on perturbed sources..."
	$(PYTHON) research/drivers/echo_delay_v2_number_check.py --mutation-receipt

# Its OWN target (not appended to verify-lane-number-checks): that recipe already
# carries an open unmerged edit from PR #845, and the umbrella-glob proposal that
# would replace all of these with one wildcard target is PENDING, so a per-lane
# target is still the shipping form.  Same gating effect.
# DISCLOSED, carrying the FLAG forward unchanged: the .PHONY line and the verify:
# prerequisite line ARE shared with every other lane's number-check target and are
# a REAL two-line union-conflict class with any concurrent lane, not an
# append-only merge.  This lane touched exactly those two shared lines plus this
# appended block.
verify-last-bond-number-check:
	@echo "Checking the LAST-BOND kernel-collapse result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/last_bond_kernel_collapse_number_check.py
	@echo "Mutation receipt: the numeral checker must FAIL on perturbed sources..."
	$(PYTHON) research/drivers/last_bond_kernel_collapse_number_check.py --mutation-receipt
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
verify-last-bond-g-rho2-rerun-number-check:
	@echo "Checking the G-RHO2 RERUN v2 result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/last_bond_g_rho2_rerun_number_check.py
	@echo "Mutation receipt: the numeral checker must FAIL on perturbed sources..."
	$(PYTHON) research/drivers/last_bond_g_rho2_rerun_number_check.py --mutation-receipt
# SRS COMPRESSION-TWIST lane number-check.  Its OWN target with its OWN recipe
# body -- no recipe line is shared with any other lane.  The mutation receipt runs
# on EVERY invocation, so the gate cannot silently degrade into a no-op.
# DISCLOSED UNION-CONFLICT CLASS: the `.PHONY` line and the `verify:` prerequisite
# line ARE shared with every other lane's number-check target.  Any concurrently
# open lane adding a number-check edits those same two lines, and the correct
# resolution is the UNION of all lanes' targets -- never a pick-one.
verify-srs-twist-number-check:
	@echo "Checking the srs compression-twist result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/srs_twist_coefficient_number_check.py
	@echo "Mutation receipt: the numeral checker must FAIL on perturbed sources..."
	$(PYTHON) research/drivers/srs_twist_coefficient_number_check.py --mutation-receipt

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
verify-approach-leak-number-check:
	@echo "Checking the APPROACH-LEAK result-doc numerals against its shipped JSON (gating; includes the G-DET re-run)..."
	$(PYTHON) research/drivers/approach_leak_number_check.py
	@echo "Mutation receipt: the numeral checker must CATCH every perturbation..."
	$(PYTHON) research/drivers/approach_leak_number_check.py --mutation-receipt

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
verify-approach-leak-v2-number-check:
	@echo "Checking the APPROACH-LEAK V2 result-doc numerals + the PRESERVED v1 target content (gating; includes the G-DET-V2 re-run)..."
	$(PYTHON) research/drivers/approach_leak_v2_number_check.py
	@echo "Mutation receipt: the v2 numeral checker must CATCH every perturbation..."
	$(PYTHON) research/drivers/approach_leak_v2_number_check.py --mutation-receipt

verify-iomega-law-number-check:
	@echo "Checking the I_omega(A)-law result-doc numerals + law-check re-run + classification completeness + quote registry + mutation receipts (gating)..."
	$(PYTHON) research/drivers/iomega_law_number_check.py


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

verify-lane-number-checks:
	@echo "Checking research-lane result-doc numeric tokens against their shipped JSON sources (gating)..."
	$(PYTHON) research/drivers/continuum_radial_solver_number_check.py
	$(PYTHON) research/drivers/subc_kubc_bracket_number_check.py
	$(PYTHON) research/drivers/coldq_pole_derivation_number_check.py
	$(PYTHON) research/drivers/pasteur_kappa_desk_calc_number_check.py

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

# Placed as its OWN target rather than appended to the verify-lane-number-checks
# recipe: PR #845 has an open, unmerged edit to that recipe, and a second
# addition to the same three-line block would collide.  Same gating effect.
verify-coldq-v2-number-check:
	@echo "Checking the cold-Q v2.1 result-doc numerals against its shipped JSON (gating)..."
	$(PYTHON) research/drivers/coldq_pole_v2_number_check.py


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
