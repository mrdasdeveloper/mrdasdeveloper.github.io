import os
import re

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

new_footer_content = """<!-- ── Global Tech Hiring Hubs ── -->
    <section aria-label="Global tech hiring hubs" style="padding:36px 0 22px;border-top:1px solid var(--border,rgba(255,255,255,0.08));">
      <div style="max-width:1000px;margin:0 auto;padding:0 20px;">
        <p style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--dim,#4a4a5a);margin-bottom:14px;">Global Tech Hiring Hubs</p>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          
          <!-- North America & UK -->
          <a href="/hire-developers-usa.html" class="seo-kw seo-biz">Hire Developers USA</a>
          <a href="/hire-developers-canada.html" class="seo-kw seo-biz">Hire Developers Canada</a>
          <a href="/hire-developers-uk.html" class="seo-kw seo-biz">Hire Developers UK</a>
          <a href="/hire-agentic-ai-engineer-san-francisco.html" class="seo-kw seo-ai">AI Engineer San Francisco</a>
          <a href="/hire-fastapi-developer-new-york-city.html" class="seo-kw seo-be">FastAPI Developer NYC</a>
          
          <!-- Middle East -->
          <a href="/hire-developers-middle-east.html" class="seo-kw seo-ops">Hire Developers Middle East</a>
          <a href="/hire-developers-saudi-arabia.html" class="seo-kw seo-ops">Hire Developers Saudi Arabia</a>
          <a href="/hire-agentic-ai-engineer-dubai.html" class="seo-kw seo-ai">AI Engineer Dubai</a>
          <a href="/hire-fastapi-developer-riyadh.html" class="seo-kw seo-be">FastAPI Developer Riyadh</a>
          
          <!-- APAC & Europe -->
          <a href="/hire-developers-singapore.html" class="seo-kw seo-fs">Hire Developers Singapore</a>
          <a href="/hire-developers-australia.html" class="seo-kw seo-fs">Hire Developers Australia</a>
          <a href="/hire-developers-germany.html" class="seo-kw seo-fs">Hire Developers Germany</a>
          <a href="/hire-developers-japan.html" class="seo-kw seo-fs">Hire Developers Japan</a>
          <a href="/hire-backend-architect-berlin.html" class="seo-kw seo-be">Backend Architect Berlin</a>
          
        </div>
      </div>
    </section>

    <!-- ── SEO Keyword Cloud ── -->
"""

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        return
        
    with open(filepath, "r") as f:
        content = f.read()

    # First, let's remove any existing Global Tech Hiring Hubs if we ran this script multiple times
    content = re.sub(r'<!-- ── Global Tech Hiring Hubs ── -->.*?(?=<!-- ── SEO Keyword Cloud ── -->|<section aria-label="Related expertise|<section aria-label="Skills)', '', content, flags=re.DOTALL)
    
    # Strip out the border-top from the related expertise section since the hubs section will have it now
    content = re.sub(r'(<section aria-label="(Related expertise and hire keywords|Skills and expertise keywords)"\s+style=")padding:[^;]+;\s*border-top:[^"]+(">)', r'\1padding:10px 0 22px;\3', content)

    # In case there's an <!-- ── SEO Keyword Cloud ── --> tag right before it, let's replace that + the section tag
    if "<!-- ── SEO Keyword Cloud ── -->" in content:
        pattern = r'<!-- ── SEO Keyword Cloud ── -->\s*(<section aria-label="(Related expertise and hire keywords|Skills and expertise keywords)"\s+style="padding:10px 0 22px;">)'
    else:
        pattern = r'(<section aria-label="(Related expertise and hire keywords|Skills and expertise keywords)"\s+style="padding:10px 0 22px;">)'
        
    content = re.sub(pattern, new_footer_content + r'\1', content, count=1)
    
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Successfully updated {filepath}")

if __name__ == "__main__":
    directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/"
    for f in base_templates:
        update_file(os.path.join(directory, f))
