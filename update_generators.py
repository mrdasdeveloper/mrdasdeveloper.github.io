import os
import re

files_to_update = [
    "generate_saudi_pages.py",
    "generate_qatar_pages_v2.py",
    "generate_uae_pages_v2.py",
    "generate_japan_pages.py"
]

new_templates_str = """templates = [
    {
        "file": "hire-full-stack-developer.html",
        "slug_prefix": "hire-full-stack-developer-",
        "role": "Full-Stack Developer",
        "hero_original": "Senior Full-Stack<br>Developer for Hire",
        "kw_prefix": "full-stack developer"
    },
    {
        "file": "hire-ai-full-stack-engineer.html",
        "slug_prefix": "hire-ai-full-stack-engineer-",
        "role": "AI Full-Stack Engineer",
        "hero_original": "AI Full-Stack<br>Engineer for Hire",
        "kw_prefix": "AI engineer"
    },
    {
        "file": "hire-backend-engineer.html",
        "slug_prefix": "hire-backend-engineer-",
        "role": "Backend Engineer",
        "hero_original": "Senior Backend<br>Engineer for Hire",
        "kw_prefix": "backend engineer"
    },
    {
        "file": "hire-ai-full-stack-engineer.html",
        "slug_prefix": "hire-agentic-ai-engineer-",
        "role": "Agentic AI Engineer",
        "hero_original": "AI Full-Stack<br>Engineer for Hire",
        "kw_prefix": "agentic AI engineer"
    },
    {
        "file": "hire-backend-engineer.html",
        "slug_prefix": "hire-fastapi-developer-",
        "role": "FastAPI Developer",
        "hero_original": "Senior Backend<br>Engineer for Hire",
        "kw_prefix": "FastAPI developer"
    },
    {
        "file": "hire-ai-full-stack-engineer.html",
        "slug_prefix": "hire-llm-engineer-",
        "role": "LLM Engineer",
        "hero_original": "AI Full-Stack<br>Engineer for Hire",
        "kw_prefix": "LLM engineer"
    },
    {
        "file": "hire-ai-full-stack-engineer.html",
        "slug_prefix": "hire-rag-developer-",
        "role": "RAG Developer",
        "hero_original": "AI Full-Stack<br>Engineer for Hire",
        "kw_prefix": "RAG developer"
    },
    {
        "file": "hire-backend-engineer.html",
        "slug_prefix": "hire-backend-architect-",
        "role": "Backend Architect",
        "hero_original": "Senior Backend<br>Engineer for Hire",
        "kw_prefix": "backend architect"
    }
]"""

new_keyword_section_template = '''keyword_section_template = """
    <!-- ── High-Value Keywords Section ── -->
    <section class="section" id="high-value-searches" style="padding-top: 20px; padding-bottom: 20px;">
      <div class="ps-inner" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
        <div class="section-header">
          <h2>🔥 Top Tech Hiring Searches in {City}</h2>
          <p>Companies and founders in {City} frequently search for these specialized development services:</p>
        </div>
        <div class="svc-grid" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));">
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">🤖 AI & Agentic Systems</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire Agentic AI Engineer {City}</li>
              <li>• LLM Engineer {City}</li>
              <li>• RAG Developer {City}</li>
              <li>• Generative AI Developer {City}</li>
              <li>• Multi-Agent Systems Developer</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">⚙️ Backend & Architecture</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire FastAPI Developer {City}</li>
              <li>• Backend Architect {City}</li>
              <li>• Python Microservices Expert</li>
              <li>• Secure API engineer {City}</li>
              <li>• Node.js Backend Developer</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💻 Full-Stack & Frontend</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire React and Next.js developer</li>
              <li>• Freelance full-stack engineer {City}</li>
              <li>• Remote software engineer {City}</li>
              <li>• Best web app developer {City}</li>
              <li>• Vue.js / Tailwind expert {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">📈 SaaS & Hiring</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• AI Automation Consultant {City}</li>
              <li>• SaaS MVP developer cost {City}</li>
              <li>• Enterprise software developer {City}</li>
              <li>• Tech co-founder for hire {City}</li>
              <li>• Cheaper alternative to {PricingMarket}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

"""'''

def update_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # Find templates = [...]
    # We use a non-greedy match to find the templates array
    templates_pattern = r'templates\s*=\s*\[.*?\]'
    content = re.sub(templates_pattern, new_templates_str, content, flags=re.DOTALL)

    # Find keyword_section_template = """..."""
    keyword_pattern = r'keyword_section_template\s*=\s*""".*?"""'
    content = re.sub(keyword_pattern, new_keyword_section_template, content, flags=re.DOTALL)

    # In japan, we need to ensure the hub generator at the bottom also supports these if it has a hub generator, but wait, japan doesn't have a hub generator in the same file. Actually it does? We will see.
    # Japan has a specific template with "title_original", but we've removed that from our templates array. 
    # Let's fix that by ensuring we don't depend on "title_original" in the template parsing loop.
    # Wait, the parsing loop in those files doesn't use `title_original`, they just use `hero_original`.

    # Fix hub generation loops if they exist (saudi, uae) to include the new links
    if "saudi_hub_content" in content:
        hub_links = """          <a href="hire-full-stack-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-agentic-ai-engineer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Agentic AI Engineer</a>
          <a href="hire-fastapi-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ FastAPI Developer</a>
          <a href="hire-backend-architect-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Backend Architect</a>
          <a href="hire-rag-developer-{city["slug"]}.html" style="display: block;">↳ RAG Developer</a>"""
        content = re.sub(r'<a href="hire-full-stack-developer-{city\["slug"\]}\.html".*?↳ Backend Engineer</a>', hub_links, content, flags=re.DOTALL)
        
    if "uae_hub_content" in content:
        hub_links = """          <a href="hire-full-stack-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-agentic-ai-engineer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Agentic AI Engineer</a>
          <a href="hire-fastapi-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ FastAPI Developer</a>
          <a href="hire-backend-architect-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Backend Architect</a>
          <a href="hire-rag-developer-{city["slug"]}.html" style="display: block;">↳ RAG Developer</a>"""
        content = re.sub(r'<a href="hire-full-stack-developer-{city\["slug"\]}\.html".*?↳ Backend Engineer</a>', hub_links, content, flags=re.DOTALL)

    with open(filepath, "w") as f:
        f.write(content)
        print(f"Updated {filepath}")

for f in files_to_update:
    filepath = os.path.join("/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/", f)
    update_file(filepath)
