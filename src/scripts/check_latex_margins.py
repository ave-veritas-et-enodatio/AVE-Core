import sys
import re

def check_log(log_path):
    overfull_pattern = re.compile(r"Overfull \\hbox \(([\d\.]+)pt too wide\)")
    max_allowed = 15.0 # Permit minor kerning/hyphenation overruns up to 15pt
    failed = False
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                match = overfull_pattern.search(line)
                if match:
                    pt_over = float(match.group(1))
                    if pt_over > max_allowed:
                        print(f"\n[Error] Hard margin overrun detected: {pt_over}pt")
                        print(f"Log Output: {line.strip()}")
                        failed = True
    except FileNotFoundError:
        print(f"[Error] Log file not found: {log_path}")
        sys.exit(1)
                    
    if failed:
        print(f"\n[Fatal] Build blocked. Fix tables or elements exceeding the text margin by >{max_allowed}pt.\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_latex_margins.py <logfile>")
        sys.exit(1)
    check_log(sys.argv[1])
