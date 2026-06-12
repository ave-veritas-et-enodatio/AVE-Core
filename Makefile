# Applied Vacuum Engineering (AVE-Core) — Master Build System
# Public release — Volumes 0–6 + Vol 9 Datasheet

PYTHON ?= ./.venv/bin/python
PYTEST ?= ./.venv/bin/pytest
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

.PHONY: all clean distclean verify $(KB_VERIFY) $(KB_REFRESH) refresh-predictions kb-claim-stats verify-md-links verify-inter-repo-links framing-audit test test-genesis test-tools pdf pdf_manuscript figures help vol0 vol1 vol2 vol3 vol4 vol5 vol6 vol9 setup

help:
	@echo "Applied Vacuum Engineering (AVE-Core) Build System"
	@echo "--------------------------------------------------"
	@echo "  make setup                : bootstrap project"
	@echo "  make all                  : Run verify, then compile all PDFs"
	@echo "  make verify               : Run physics verification protocols (The Kernel Check) and kb claim id check"
	@echo "  make $(KB_REFRESH)  : Regenerate derived KB metadata (subtree-claims, solidity, claim index)"
	@echo "  make kb-claim-stats       : Print claim-graph counts + solidity build-band distribution (read-only)"
	@echo "  make verify-md-links      : Check Markdown link integrity + cited-id validity (inter-repo: warn)"
	@echo "  make verify-inter-repo-links : Same, but broken inter-repo links also gate (inter-repo: error)"
	@echo "  make framing-audit        : Scan corpus for reviewer-misread framing anti-patterns (advisory)"
	@echo "  make test                 : Run unit tests (src/tests + kb tools tests)"
	@echo "  make test-tools           : Run KB tooling tests only (manuscript/ave-kb/tools/tests)"
	@echo "  make pdf                  : Compile all 8 public volumes (Vols 0-6 + Vol 9 Datasheet)"
	@echo "  make pdf_manuscript       : Compile manuscript volumes"
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
verify: $(KB_VERIFY) verify-md-links
	@echo "\n[Verify] Running DAG Anti-Cheat Scan..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/verify_universe.py
	@echo "\n[Verify] Running FDTD LC Network solvers..."
	$(PYTHON) $(SCRIPT_DIR)/vol_4_engineering/visualize_impedance_rupture.py
	@echo "\n[Verify] Running Macroscopic Mutual Inductance bounds..."
	$(PYTHON) $(SCRIPT_DIR)/vol_4_engineering/simulate_mutual_inductance.py
	@echo "\n[Verify] Running Topological Borromean geometric limits..."
	$(PYTHON) $(SCRIPT_DIR)/vol_1_foundations/visualize_topological_bounds.py
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

verify-md-links:
	@echo "Checking Markdown link integrity + cited-id validity (inter-repo: warn)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) $(KB_TOOLS_DIR)/verify-md-links.py --inter-repo warn

verify-inter-repo-links:
	@echo "Checking Markdown links incl. inter-repo as gating (inter-repo: error)..."
	PYTHONPATH=$(KB_TOOLS_DIR) $(PYTHON) $(KB_TOOLS_DIR)/verify-md-links.py --inter-repo error

framing-audit:
	@echo "[Framing] Full defense-context anti-pattern scan (advisory; warn/info do not gate)..."
	$(PYTHON) $(SCRIPT_DIR)/defense_context_checker.py


# =============================================================================
# 2. Unit Testing
# =============================================================================
test: test-tools
	@echo "[Test] Running Unit Tests..."
	# Scope to the unit-test tree only. src/scripts/**/*_test.py are runnable
	# analysis/forward-prediction DRIVERS (each has a __main__ block), not pytest
	# tests; collecting them mis-runs driver functions as tests (and errors on
	# non-fixture positional args like test_wave_speed(N, ...)). Drivers run
	# standalone / via `make verify`, not here.
	$(PYTEST) $(SOURCE_DIR)/tests

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
	@find $(SRC_DIR) future_work \
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
