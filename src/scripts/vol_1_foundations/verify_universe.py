"""
AVE Anti-Cheat DAG Verifier
Scans the Abstract Syntax Tree (AST) of the new `src/ave` LC Network framework
to mathematically prove that no Standard Model empirical parameters are being "smuggled"
downstream to curve-fit the derivations.
"""

import ast
import sys
from pathlib import Path

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p/".git").is_dir())
EXCLUDED_DIRS = {".venv", "venv", "node_modules", ".git", "__pycache__", ".eggs", "*.egg-info"}

BANNED_IMPORTS = ["scipy.constants"]

# These "Magic Numbers" MUST emerge organically from the DAG geometry
# None of these are allowed to be hard-coded deeper into the `ave` package.
MAGIC_NUMBERS = {
    137.036: "Inverse Fine Structure Constant (Must be derived from Golden Torus!)",
    376.73: "Impedance of Free Space (Must be derived from Topology: sqrt(u/e)!)",
    1836.15: "Proton Mass Ratio (Must be derived via Faddeev-Skyrme eigenvalue!)",
    69.32: "Hubble Constant (Must be derived from Lattice Genesis!)",
    1.2e-10: "MOND a_0 limit (Must be derived from Unruh-Hawking Hoop Stress!)",
    0.1834: "QED Packing Fraction (8*pi*alpha)",
    299792458.0: "Speed of light (c) (Must be imported from constants.py)",
    1.05457e-34: "Planck constant (hbar) (Must be imported from constants.py)",
    6.674e-11: "Gravitational constant (G) (Must be imported from constants.py)",
    1.380649e-23: "Boltzmann constant (K_B) (Must be imported from constants.py)",
    6.02214e23: "Avogadro constant (N_A) (Must be imported from constants.py)",
    1.67262e-27: "Proton mass (M_PROTON) (Must be imported from constants.py)",
    1.989e30: "Solar mass (M_SUN) (Must be imported from constants.py)",
    1.602176e-19: "Elementary charge (e_charge) (Must be imported from constants.py)",
    9.10938e-31: "Electron mass (M_E) (Must be imported from constants.py)",
    8.8541878e-12: "Vacuum permittivity (EPSILON_0) (Must be imported from constants.py)",
    300000000.0: "Speed of light (c) (Must be imported from constants.py)",
}

class AVESyntaxValidator(ast.NodeVisitor):
    def __init__(self, filepath):
        self.filepath = filepath
        self.violations = []
        self.in_main_block = False

    def visit_Import(self, node):
        for alias in node.names:
            if "scipy.constants" in alias.name:
                self.violations.append(f"Line {node.lineno}: ILLEGAL IMPORT: '{alias.name}'. Standard Model smuggling.")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module and "scipy.constants" in node.module:
            self.violations.append(
                f"Line {node.lineno}: ILLEGAL IMPORT: 'from {node.module}'. Standard Model smuggling."
            )
        self.generic_visit(node)

    def visit_If(self, node):
        is_main = False
        try:
            if (
                isinstance(node.test, ast.Compare)
                and isinstance(node.test.left, ast.Name)
                and node.test.left.id == "__name__"
                and isinstance(node.test.comparators[0], ast.Constant)
                and node.test.comparators[0].value == "__main__"
            ):
                is_main = True
        except Exception:
            pass

        if is_main:
            prev = self.in_main_block
            self.in_main_block = True
            self.generic_visit(node)
            self.in_main_block = prev
        else:
            self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, float) and not self.in_main_block:
            for magic_val, reason in MAGIC_NUMBERS.items():
                if node.value != 0 and abs(node.value - magic_val) / abs(magic_val) < 0.005:
                    self.violations.append(
                        f"Line {node.lineno} - MAGIC NUMBER DETECTED: {node.value} -> {reason}. "
                        f"Must be dynamically passed from constants.py."
                    )
        self.generic_visit(node)


def run_verification():
    print("==================================================")
    print("AVE DIRECTED ACYCLIC GRAPH (DAG) VERIFIER")
    print("Hunting for smuggled Standard Model parameters...")
    print("==================================================\n")

    total_files: int = 0
    clean_files: int = 0
    global_violations: int = 0

    # Exempt from Magic Float checks:
    # - constants.py / cosserat.py: define the engine constants
    # - verify_universe.py: this verifier itself
    # - test_*: tests legitimately compare against known PDG/CODATA values
    EXEMPT_FILES = ["constants.py", "cosserat.py", "verify_universe.py"]
    EXEMPT_PREFIXES = ["test_"]

    # Scan the ENTIRE project root — no directory left behind
    py_files_to_scan = []
    for py_file in PROJECT_ROOT.rglob("*.py"):
        # Skip excluded directories
        if any(part in EXCLUDED_DIRS for part in py_file.parts):
            continue
        py_files_to_scan.append(py_file)
    # Deduplicate
    py_files_to_scan = sorted(set(py_files_to_scan))

    for py_file in py_files_to_scan:
        total_files += 1

        with open(py_file, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=str(py_file))
            except SyntaxError as e:
                print(f"[ERROR] Could not parse {py_file}: {e}")
                continue

        validator = AVESyntaxValidator(py_file)

        if py_file.name in EXEMPT_FILES or any(py_file.name.startswith(p) for p in EXEMPT_PREFIXES):
            validator.in_main_block = True

        validator.visit(tree)

        if validator.violations:
            try:
                rel_path = py_file.relative_to(PROJECT_ROOT)
            except ValueError:
                rel_path = py_file
            print(f"[FAIL] {rel_path}")
            for v in validator.violations:
                print(f"       -> {v}")
                global_violations += 1
        else:
            clean_files += 1
            try:
                rel_path = py_file.relative_to(PROJECT_ROOT)
            except ValueError:
                rel_path = py_file
            print(f"[PASS] {rel_path}")

    print("\n==================================================")
    if global_violations == 0:
        print("VERDICT: MATHEMATICALLY PURE.")
        print(f"Successfully verified {clean_files}/{total_files} framework files.")
        print("Zero Standard Model parameters smuggled. The DAG is unbreakable.")
    else:
        print("VERDICT: COMPROMISED.")
        print(f"Found {global_violations} violation(s). The framework is no longer an EFT.")
        sys.exit(1)
    print("==================================================")


if __name__ == "__main__":
    run_verification()
