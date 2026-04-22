"""
§10 Numeric Spot-Check — Master Runner
========================================

Runs all volume spot-check scripts in sequence and reports pass/fail.

Run: PYTHONPATH=src python src/scripts/peer_review/run_all_spot_checks.py
"""

import subprocess
import sys
import os

SCRIPTS = [
    "src/scripts/peer_review/spot_check_vol1.py",
    "src/scripts/peer_review/spot_check_vol2.py",
    "src/scripts/peer_review/d_proton_delta_analysis.py",
    "src/scripts/peer_review/spot_check_vol6.py",
]

root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(root, "../../.."))

env = os.environ.copy()
env["PYTHONPATH"] = os.path.join(project_root, "src")

print("╔" + "═" * 88 + "╗")
print("║    §10 PEER REVIEW NUMERIC SPOT-CHECK — ALL VOLUMES" + " " * 36 + "║")
print("╚" + "═" * 88 + "╝")
print()

results = {}
for script in SCRIPTS:
    full_path = os.path.join(project_root, script)
    if not os.path.exists(full_path):
        print(f"⚠️  SKIP: {script} (not found)")
        results[script] = "SKIP"
        continue

    print(f"▶ Running: {script}")
    print()
    result = subprocess.run(
        [sys.executable, full_path],
        cwd=project_root,
        env=env,
        capture_output=False,
    )
    results[script] = "PASS" if result.returncode == 0 else "FAIL"
    print()

# Summary
print("╔" + "═" * 88 + "╗")
print("║    SUMMARY" + " " * 77 + "║")
print("╚" + "═" * 88 + "╝")
for script, status in results.items():
    icon = "✅" if status == "PASS" else ("⚠️" if status == "SKIP" else "❌")
    print(f"  {icon}  {script}: {status}")
