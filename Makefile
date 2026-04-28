# Applied Vacuum Engineering (AVE-Core) — Master Build System
# Public release — Volumes 0–6

PYTHON ?= ./.venv/bin/python
PYTEST ?= ./.venv/bin/pytest
LATEX = pdflatex -interaction=nonstopmode -halt-on-error
BIBTEX = bibtex

# Directory Configuration
OUT_DIR = build
SRC_DIR = manuscript

SOURCE_DIR = src
SCRIPT_DIR = $(SOURCE_DIR)/scripts

# Volume list — public volumes only (0–6)
VOLUMES = vol_0_engineering_compendium vol_1_foundations vol_2_subatomic vol_3_macroscopic vol_4_engineering vol_5_biology vol_6_periodic_table

.PHONY: all clean distclean verify test pdf pdf_manuscript figures help vol0 vol1 vol2 vol3 vol4 vol5 vol6 setup

help:
	@echo "Applied Vacuum Engineering (AVE-Core) Build System"
	@echo "--------------------------------------------------"
	@echo "  make setup           : bootstrap project"
	@echo "  make all             : Run verify, then compile all PDFs"
	@echo "  make verify          : Run physics verification protocols (The Kernel Check)"
	@echo "  make test            : Run unit tests (pytest)"
	@echo "  make pdf             : Compile all 7 public volumes"
	@echo "  make pdf_manuscript  : Compile manuscript volumes"
	@echo "  make vol0            : Vol 0:  The Engineering Compendium"
	@echo "  make vol1            : Vol I:  Foundations & Universal Operators"
	@echo "  make vol2            : Vol II: The Subatomic Lattice"
	@echo "  make vol3            : Vol III: The Macroscopic Continuum"
	@echo "  make vol4            : Vol IV: Applied Impedance Engineering"
	@echo "  make vol5            : Vol V:  Topological Biology"
	@echo "  make vol6            : Vol VI: The Periodic Table"
	@echo "  make figures         : Generate particle topology figure suite"
	@echo "  make clean           : Remove auxiliary build artifacts (preserves PDFs)"
	@echo "  make distclean       : Remove ALL build artifacts including PDFs"

all: verify pdf

setup:
	@./setup.sh

# =============================================================================
# 1. Physics Verification (The "Simulate to Verify" Protocol)
# =============================================================================
verify:
	@echo "[Verify] Running DAG Anti-Cheat Scan..."
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
	@echo "\n[Verify] Running defense-context checker (warning-only)..."
	-@$(PYTHON) $(SCRIPT_DIR)/defense_context_checker.py
	@echo "\n[Verify] Running claim-graph validator..."
	$(PYTHON) $(SCRIPT_DIR)/claim_graph_validator.py
	@echo "\n=================================================="
	@echo "[Verify] ALL PHYSICS PROTOCOLS PASSED."
	@echo "=================================================="

# =============================================================================
# 2. Unit Testing
# =============================================================================
test:
	@echo "[Test] Running Unit Tests..."
	$(PYTEST) $(SOURCE_DIR)

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
	@echo "[Build] Compiling Volumes 0–VI..."
	@for dir in $(VOLUMES); do \
		$(MAKE) --no-print-directory _compile_vol VOL=$$dir; \
	done
	@echo "[Build] All 7 volume PDFs generated in $(OUT_DIR)/"

_compile_vol:
	$(call COMPILE_VOL,$(VOL))

# --- Individual volume targets ---
# Note: Vols 0, 2, 3, 4, 5, 6 use xr-hyper to pull Vol 1 labels (Ch.\ref{ch:alpha_golden_torus}
# etc.) into their \ref namespace. They depend on vol1 so `build/aux/vol_1_foundations.aux`
# is present when each is compiled. The \IfFileExists guard in each main.tex allows
# standalone builds to fall through silently, but targeting them via these Makefile
# rules guarantees cross-volume refs resolve.
vol0: vol1
	$(call COMPILE_VOL,vol_0_engineering_compendium)

vol1:
	$(call COMPILE_VOL,vol_1_foundations)

vol2: vol1
	$(call COMPILE_VOL,vol_2_subatomic)

vol3: vol1
	$(call COMPILE_VOL,vol_3_macroscopic)

vol4: vol1
	$(call COMPILE_VOL,vol_4_engineering)

vol5: vol1
	$(call COMPILE_VOL,vol_5_biology)

vol6: vol1
	$(call COMPILE_VOL,vol_6_periodic_table)

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
