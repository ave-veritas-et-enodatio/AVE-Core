#!/usr/bin/env python3
"""
Package the vacuum-lattice DIY kit as a release artifact (zip).

Regenerates the kit (GATING QC must pass) then bundles the print-ready STLs +
manifest + README into a single versioned zip suitable for a GitHub release.
The repo tracks the GENERATORS as source of truth; this produces the downloadable
artifact so the binaries never bloat git.

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/package_kit_release.py
    KIT_PRINT_MM_PER_L_NODE=60 ASSEMBLY_L=4 \\
        PYTHONPATH=src python src/scripts/vol_1_foundations/package_kit_release.py --out dist/

Env (forwarded to the generator): KIT_PRINT_MM_PER_L_NODE, ASSEMBLY_L,
KIT_FRICTION_INTERFERENCE_MM. The artifact is named by the scale + L.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys
import zipfile

VERSION = "v1"


def main() -> None:
    repo = pathlib.Path(__file__).resolve().parents[3]
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(repo / "dist"), help="output directory for the zip")
    args = ap.parse_args()

    scale = os.environ.get("KIT_PRINT_MM_PER_L_NODE", "100")
    asm = os.environ.get("ASSEMBLY_L", "4")
    kit_dir = repo / "assets" / "3d_models" / "kit"
    driver = repo / "src" / "scripts" / "vol_1_foundations" / "generate_vacuum_lattice_kit.py"

    # 1. Regenerate the kit — GATING QC will sys.exit(1) if any part is non-manifold.
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join([
        str(repo / "src"),
        str(repo / "src" / "scripts" / "vol_1_foundations"),
        str(repo / "src" / "scripts" / "vol_2_subatomic"),
        env.get("PYTHONPATH", ""),
    ])
    print(f"[package] regenerating kit @ {scale} mm/l_node, L={asm} (gating QC) ...")
    r = subprocess.run([sys.executable, str(driver)], env=env)
    if r.returncode != 0:
        print("[package] ABORT — generator QC failed; not packaging a broken kit.")
        sys.exit(r.returncode)

    # 2. Collect print-ready files (STLs + manifest + README), skip the visual preview.
    members = sorted(
        [p for p in kit_dir.glob("*.stl") if p.name != "reference_tetra_unit_cell.stl"]
        + list(kit_dir.glob("vacuum_assembly_L*.json"))
        + [kit_dir / "README.md"]
    )
    members = [p for p in members if p.exists()]

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"vacuum-lattice-kit-{VERSION}-{scale}mm-L{asm}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in members:
            z.write(p, arcname=f"vacuum-lattice-kit/{p.name}")

    size_mb = zip_path.stat().st_size / 1e6
    print(f"[package] wrote {zip_path}  ({len(members)} files, {size_mb:.2f} MB)")
    print(f"[package] release: gh release create vacuum-lattice-kit-{VERSION} '{zip_path}'")


if __name__ == "__main__":
    main()
