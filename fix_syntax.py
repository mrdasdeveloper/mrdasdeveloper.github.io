import os
import glob

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
generator_files = glob.glob(os.path.join(output_dir, "generate_*_pages.py")) + glob.glob(os.path.join(output_dir, "generate_*_pages_v2.py")) + [os.path.join(output_dir, "generate_mena_hubs_fix.py")]

for filepath in generator_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r") as f:
        content = f.read()
    
    # Let's fix the broken footer match string.
    # It currently looks like:
    # footer_match = '
    # </div>
    # <!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]
    
    # We want it to be:
    # footer_match = '\n</div>\n<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]
    
    fixed_content = content.replace("footer_match = '\n</div>\n<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]", 
                                    "footer_match = '\\n</div>\\n<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]")
    
    if fixed_content != content:
        with open(filepath, "w") as f:
            f.write(fixed_content)
        print(f"Fixed {filepath}")
