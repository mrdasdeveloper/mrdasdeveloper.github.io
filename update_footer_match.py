import os
import re
import glob

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
generator_files = glob.glob(os.path.join(output_dir, "generate_*_pages.py")) + glob.glob(os.path.join(output_dir, "generate_*_pages_v2.py")) + [os.path.join(output_dir, "generate_mena_hubs_fix.py")]

def fix_footer_match(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, "r") as f:
        content = f.read()
        
    # Replace the footer_match line
    old_line = r"footer_match = '\\n</div>\\n<footer class=\"footer\">' \+ template\.split\('<footer class=\"footer\">'\)\[1\]"
    new_line = "footer_match = '\\n</div>\\n<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]"
    
    if "footer_match =" in content:
        content = re.sub(old_line, new_line, content)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filepath}")

for f in generator_files:
    fix_footer_match(f)
