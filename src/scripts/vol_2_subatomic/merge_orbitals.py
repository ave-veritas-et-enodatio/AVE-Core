import os
import glob
import re
import shutil

src_base = "periodic_table_of_knots/chapters"
dst_base = "periodic_table/chapters"
img_dst_base = "periodic_table/simulations/outputs"

os.makedirs(img_dst_base, exist_ok=True)

mapping = {
    1: ('001_hydrogen', '03_hydrogen.tex'),
    2: ('002_helium', '04_helium.tex'),
    3: ('003_lithium', '05_lithium.tex'),
    4: ('004_beryllium', '06_beryllium.tex'),
    5: ('005_boron', '07_boron.tex'),
    6: ('006_carbon', '08_carbon.tex'),
    7: ('007_nitrogen', '09_nitrogen.tex'),
    8: ('008_oxygen', '10_oxygen.tex'),
    9: ('009_fluorine', '11_fluorine.tex'),
    10: ('010_neon', '12_neon.tex'),
    11: ('011_sodium', '13_sodium.tex'),
    12: ('012_magnesium', '14_magnesium.tex'),
    13: ('013_aluminum', '15_aluminum.tex'),
    14: ('014_silicon', '16_silicon.tex')
}

def replace_img_simple(m, src_dir):
    opts = m.group(1)
    img_path = m.group(2)
    filename = os.path.basename(img_path)
    
    full_img_path = os.path.join("periodic_table_of_knots", img_path)
    if not os.path.exists(full_img_path):
        full_img_path = os.path.join(src_dir, "simulations", "outputs", filename)
    
    if os.path.exists(full_img_path):
        shutil.copy(full_img_path, os.path.join(img_dst_base, filename))
        print(f"Copied {filename}")
    else:
        print(f"Warning: Could not find image {full_img_path}")
        
    if opts is not None:
        return f"\\includegraphics[{opts}]{{{filename}}}"
    else:
        return f"\\includegraphics{{{filename}}}"

for z, (src_folder, dest_file) in mapping.items():
    src_dir = os.path.join(src_base, src_folder)
    dst_path = os.path.join(dst_base, dest_file)
    
    if not os.path.exists(dst_path):
        print(f"Skipping Z={z}, {dest_file} not found.")
        continue
        
    tex_files = [f for f in glob.glob(os.path.join(src_dir, "*.tex")) if not f.endswith("_manifest.tex")]
    
    if tex_files:
        src_tex = tex_files[0]
        with open(src_tex, "r") as f:
            content = f.read()
            
        content = content.replace("\\subsection{", "\\subsubsection{")
        content = re.sub(r"\\section\{([^}]+)\}", r"\\subsection{\1}", content)
        content = re.sub(r"\\includegraphics(?:\[(.*?)\])?\{([^}]+)\}", lambda m: replace_img_simple(m, src_dir), content)
        
        append_txt = f"\n\n\\section{{Orbital Knot Topology}}\n{content}\n"
        
        with open(dst_path, "a") as f:
            f.write(append_txt)
            
        print(f"Merged {src_folder} orbital data into {dest_file}")
