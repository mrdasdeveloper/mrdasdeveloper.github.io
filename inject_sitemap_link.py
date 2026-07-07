import os

base_templates = [
    "index.html",
    "hire-full-stack-developer.html",
    "hire-ai-full-stack-engineer.html",
    "hire-backend-engineer.html",
    "business-automation.html",
    "freelancer.html",
    "agentic-ai-developer.html",
    "full-stack-ai-engineer.html",
    "presentation.html"
]

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/"

target = """<a href="https://github.com/mrdasdeveloper" target="_blank">github.com/mrdasdeveloper</a>"""
replacement = """<a href="https://github.com/mrdasdeveloper" target="_blank">github.com/mrdasdeveloper</a>
        &nbsp;·&nbsp;
        <a href="/sitemap.html" style="color:var(--dim); text-decoration:underline;">Sitemap</a>"""

for template in base_templates:
    filepath = os.path.join(directory, template)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r") as f:
        content = f.read()
        
    if '<a href="/sitemap.html"' not in content:
        content = content.replace(target, replacement)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {template}")
