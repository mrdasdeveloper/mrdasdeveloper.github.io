import os
import re

saudi_cities = [
    {
        "name": "Riyadh", "slug": "riyadh",
        "ecosystem": "Vision 2030 digital transformation, AI, fintech, and enterprise software hubs",
        "focus_title": "Enterprise SaaS & Digital Transformation",
        "focus_desc": "Highly scalable platforms powering Riyadh's massive government and fintech ecosystem.",
        "hero_desc": "government initiatives, AI startups, and enterprise operations",
        "pricing_market": "Riyadh Agency"
    },
    {
        "name": "Jeddah", "slug": "jeddah",
        "ecosystem": "major commercial centers and e-commerce technology hubs",
        "focus_title": "E-Commerce & Enterprise IT Systems",
        "focus_desc": "Robust enterprise software tailored for Jeddah's strong commercial and enterprise hiring demands.",
        "hero_desc": "major commercial hubs and growing e-commerce platforms",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Dammam", "slug": "dammam",
        "ecosystem": "energy, logistics, and industrial technology centers",
        "focus_title": "Logistics & Industrial Platforms",
        "focus_desc": "High-performance software engineering solutions tailored for Dammam's energy and industrial sectors.",
        "hero_desc": "energy technology players and logistics facilities",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Khobar", "slug": "khobar",
        "ecosystem": "technology companies serving the Eastern Province",
        "focus_title": "Cloud Infrastructure & Backend Systems",
        "focus_desc": "Systems engineering and API platforms built specifically for Khobar's growing tech demands.",
        "hero_desc": "cloud technology providers and backend engineering sectors",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Dhahran", "slug": "dhahran",
        "ecosystem": "research innovation and AI ecosystems",
        "focus_title": "Research & AI Technology",
        "focus_desc": "Deep tech integrations and scalable software catering to Dhahran's engineering and research environments.",
        "hero_desc": "AI research centers and engineering technology companies",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Mecca", "slug": "mecca",
        "ecosystem": "smart-city, tourism, and digital services projects",
        "focus_title": "Smart-City & Tourism Tech",
        "focus_desc": "Scalable software systems handling massive concurrent users for Mecca's tourism and smart-city networks.",
        "hero_desc": "smart-city initiatives, tourism tech, and digital services",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Medina", "slug": "medina",
        "ecosystem": "government and digital infrastructure projects",
        "focus_title": "Digital Infrastructure & Systems",
        "focus_desc": "Secure cloud applications built to support Medina's rapidly expanding government IT sector.",
        "hero_desc": "government tech operations and digital infrastructure sectors",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Tabuk", "slug": "tabuk",
        "ecosystem": "regional development initiatives and emerging tech",
        "focus_title": "Regional Tech & Development Platforms",
        "focus_desc": "Enterprise solutions specializing in scalable transformation for Tabuk's regional development businesses.",
        "hero_desc": "development initiatives and regional technology projects",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Abha", "slug": "abha",
        "ecosystem": "regional business and emerging technology projects",
        "focus_title": "Government & Emerging Tech Systems",
        "focus_desc": "Secure, compliant IT architectures tailored for Abha's government and emerging research projects.",
        "hero_desc": "regional tech hubs and government projects",
        "pricing_market": "Saudi Agency"
    },
    {
        "name": "Yanbu", "slug": "yanbu",
        "ecosystem": "industrial software and logistics technology sectors",
        "focus_title": "Engineering IT & Industrial Software",
        "focus_desc": "Custom IT services and specialized industrial software built for Yanbu's logistics and engineering sectors.",
        "hero_desc": "industrial software providers and logistics technology",
        "pricing_market": "Saudi Agency"
    }
]

templates = [
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
]

keyword_section_template = """
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

"""

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
urls = []

for tpl in templates:
    base_file_path = os.path.join(output_dir, tpl["file"])
    with open(base_file_path, "r") as f:
        base_content = f.read()

    for city in saudi_cities:
        content = base_content
        
        # Title and Description
        content = re.sub(r'<title>.*?</title>', f'<title>Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & Saudi Arabia</title>', content)
        content = re.sub(r'<meta name="description" content=".*?" />', f'<meta name="description" content="Hire Ramesh Kumar Das, Top {tpl["role"]} in {city["name"]} & Saudi Arabia (KSA). Building scalable systems for {city["hero_desc"]}." />', content)
        
        # Meta Keywords
        content = re.sub(r'<meta name="keywords" content=".*?" />', f'<meta name="keywords" content="hire {tpl["kw_prefix"]} {city["name"]}, {tpl["kw_prefix"]} for hire Saudi Arabia, freelance developer {city["name"]}, Next.js developer {city["name"]}, remote developer KSA, SaaS developer Riyadh, Ramesh Kumar Das" />', content)
        
        # Canonical & OG
        content = re.sub(r'<link rel="canonical" href=".*?\.html" />', f'<link rel="canonical" href="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & Saudi Arabia" />', content)
        content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        
        # Schema Area Served
        content = content.replace('"areaServed":"Worldwide"', f'"areaServed":"{city["name"]}, Saudi Arabia"')
        
        # Hero Adjustments
        content = content.replace('Available for Hire — Remote', 'Available for Hire — Remote (AST / Saudi Timezone)')
        content = content.replace(f'<h1 id="hero-heading">{tpl["hero_original"]}</h1>', f'<h1 id="hero-heading">Top {tpl["role"]}<br>for {city["name"]} & KSA</h1>')
        
        # Add focus chip
        content = content.replace('<span class="chip neutral">Nepal &nbsp;·&nbsp; Remote</span>', f'<span class="chip neutral">{city["name"]} / KSA Focus</span>')
        
        # Services text adaptation
        content = content.replace('<h2>What I Can Build For You</h2>', f'<h2>What I Can Build For Your {city["name"]} Business</h2>')
        
        # Pricing market reference
        content = content.replace('Market Standard:', f'{city["pricing_market"]}:')
        
        # Inject High Value Keywords
        kw_section = keyword_section_template.replace("{City}", city["name"]).replace("{PricingMarket}", city["pricing_market"])
        content = content.replace('<!-- ── SEO Keyword Cloud ── -->', kw_section + '<!-- ── SEO Keyword Cloud ── -->')
        
        # Generate the file
        filename = f"{tpl['slug_prefix']}{city['slug']}.html"
        filepath = os.path.join(output_dir, filename)
        
        # Save file
        with open(filepath, "w") as out_f:
            out_f.write(content)
            
        print(f"Generated {filename}")
        urls.append(f"<url><loc>https://mrdasdeveloper.github.io/{filename}</loc><lastmod>2026-06-12</lastmod><changefreq>weekly</changefreq><priority>0.80</priority></url>")

print("\n--- Sitemap Entries ---")
print("\n".join(urls))

# Now generate the Saudi Hub page
saudi_hub_content = """
<main class="main">
  <section class="section">
    <div class="ps-inner" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <h1 style="font-size: 3rem; margin-bottom: 20px;">Hire Tech Talent in Saudi Arabia 🇸🇦</h1>
      <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 40px; max-width: 800px;">
        Aligned with Vision 2030, Saudi Arabia is a global technology powerhouse. We provide elite, remote-first Full-Stack, AI, and Backend developers aligned with Arabia Standard Time (AST). Explore our specialized hubs tailored for KSA's fastest-growing tech cities.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
"""

for city in saudi_cities:
    saudi_hub_content += f"""
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">{city["name"]}</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">{city["focus_title"]}</p>
                    <a href="hire-full-stack-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-agentic-ai-engineer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Agentic AI Engineer</a>
          <a href="hire-fastapi-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ FastAPI Developer</a>
          <a href="hire-backend-architect-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Backend Architect</a>
          <a href="hire-rag-developer-{city["slug"]}.html" style="display: block;">↳ RAG Developer</a>
        </div>
"""

saudi_hub_content += """
      </div>
    </div>
  </section>
</main>
"""

with open(os.path.join(output_dir, "hire-full-stack-developer.html"), "r") as f:
    template = f.read()

header_match = template.split('<div class="container">')[0] + '<div class="container">\n'
footer_match = '\n</div>\n<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]

# Adjust title and meta in header
h = header_match.replace("<title>Hire Ramesh Kumar Das — Senior Full-Stack Developer | React, Next.js, Node.js, FastAPI</title>", "<title>Hire Tech Talent in Saudi Arabia (KSA) — Developers Hub</title>")
h = h.replace('<meta name="description" content="Senior Full-Stack Developer with 6.5+ years. Expert in React.js, Next.js, Node.js, FastAPI. Available for remote hire." />', '<meta name="description" content="Hire elite remote developers specialized for the Saudi Arabia (KSA) market. AI, Full-Stack, and Backend engineers available on AST." />')

full_html = h + saudi_hub_content + footer_match
with open(os.path.join(output_dir, "hire-developers-saudi-arabia.html"), "w") as f:
    f.write(full_html)
print("Generated hire-developers-saudi-arabia.html")
