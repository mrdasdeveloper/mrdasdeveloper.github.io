import os
import re

qatar_cities = [
    {
        "name": "Doha", "slug": "doha",
        "ecosystem": "Fintech, telecom, AI, cloud, and enterprise software",
        "focus_title": "Enterprise SaaS & Fintech Platforms",
        "focus_desc": "Highly scalable platforms powering Doha's massive government and fintech ecosystem.",
        "hero_desc": "government digital transformation, AI startups, and enterprise operations",
        "pricing_market": "Doha Agency"
    },
    {
        "name": "Al Rayyan", "slug": "al-rayyan",
        "ecosystem": "Universities and technology initiatives",
        "focus_title": "EdTech & IT Systems",
        "focus_desc": "Robust enterprise software tailored for Al Rayyan's strong university and enterprise hiring demands.",
        "hero_desc": "education initiatives and major business hubs",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Lusail", "slug": "lusail",
        "ecosystem": "Smart city developments, AI, IoT",
        "focus_title": "Smart City & Startup IT",
        "focus_desc": "High-performance software engineering solutions tailored for Lusail's growing tech sectors.",
        "hero_desc": "smart city projects and emerging startups",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Al Wakrah", "slug": "al-wakrah",
        "ecosystem": "Logistics and business technology demand",
        "focus_title": "Business Automation & Software",
        "focus_desc": "Systems engineering and automation platforms built specifically for Al Wakrah's business sectors.",
        "hero_desc": "commercial sectors and logistics networks",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Umm Salal", "slug": "umm-salal",
        "ecosystem": "Local IT and enterprise opportunities",
        "focus_title": "Enterprise Tech & Integrations",
        "focus_desc": "Scalable software systems catering to Umm Salal's expanding business districts.",
        "hero_desc": "business districts and enterprise software providers",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Al Khor", "slug": "al-khor",
        "ecosystem": "Energy and industrial sector technology",
        "focus_title": "Energy Tech & Digital Transformation",
        "focus_desc": "Secure cloud applications built to support Al Khor's energy and industrial sectors.",
        "hero_desc": "industrial networks and energy tech operations",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Al Daayen", "slug": "al-daayen",
        "ecosystem": "Infrastructure and smart-city projects",
        "focus_title": "Infrastructure Tech Solutions",
        "focus_desc": "Enterprise solutions specializing in infrastructure development for Al Daayen.",
        "hero_desc": "infrastructure projects and emerging digital sectors",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Mesaieed", "slug": "mesaieed",
        "ecosystem": "Industrial and energy technology opportunities",
        "focus_title": "Enterprise Software Hubs",
        "focus_desc": "Secure, compliant IT architectures tailored for Mesaieed's industrial sector.",
        "hero_desc": "industrial providers and energy tech hubs",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Dukhan", "slug": "dukhan",
        "ecosystem": "Oil and gas technology sector",
        "focus_title": "Oil & Gas IT Systems",
        "focus_desc": "Custom IT services and specialized software built for Dukhan's resource sectors.",
        "hero_desc": "oil and gas providers and technical operations",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Madinat ash Shamal", "slug": "madinat-ash-shamal",
        "ecosystem": "Local business and technology projects",
        "focus_title": "Local Business IT Systems",
        "focus_desc": "Scalable web applications serving Madinat ash Shamal's local enterprise needs.",
        "hero_desc": "local retail and regional technology initiatives",
        "pricing_market": "Qatar Agency"
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

    for city in qatar_cities:
        content = base_content
        
        # Title and Description
        content = re.sub(r'<title>.*?</title>', f'<title>Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & Qatar</title>', content)
        content = re.sub(r'<meta name="description" content=".*?" />', f'<meta name="description" content="Hire Ramesh Kumar Das, Top {tpl["role"]} in {city["name"]} & Qatar. Building scalable systems for {city["hero_desc"]}." />', content)
        
        # Meta Keywords
        content = re.sub(r'<meta name="keywords" content=".*?" />', f'<meta name="keywords" content="hire {tpl["kw_prefix"]} {city["name"]}, {tpl["kw_prefix"]} for hire Qatar, freelance developer {city["name"]}, Next.js developer {city["name"]}, remote developer Qatar, SaaS developer Doha, Ramesh Kumar Das" />', content)
        
        # Canonical & OG
        content = re.sub(r'<link rel="canonical" href=".*?\.html" />', f'<link rel="canonical" href="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & Qatar" />', content)
        content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        
        # Schema Area Served
        content = content.replace('"areaServed":"Worldwide"', f'"areaServed":"{city["name"]}, Qatar"')
        
        # Hero Adjustments
        content = content.replace('Available for Hire — Remote', 'Available for Hire — Remote (AST / Qatar Timezone)')
        content = content.replace(f'<h1 id="hero-heading">{tpl["hero_original"]}</h1>', f'<h1 id="hero-heading">Top {tpl["role"]}<br>for {city["name"]} & Qatar</h1>')
        
        # Add focus chip
        content = content.replace('<span class="chip neutral">Nepal &nbsp;·&nbsp; Remote</span>', f'<span class="chip neutral">{city["name"]} / Qatar Focus</span>')
        
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
        
        # Only collect the AI and Backend URLs for appending to sitemap, as full-stack is already there
        if tpl["role"] != "Full-Stack Developer":
            urls.append(f"<url><loc>https://mrdasdeveloper.github.io/{filename}</loc><lastmod>2026-06-12</lastmod><changefreq>weekly</changefreq><priority>0.80</priority></url>")

print("\n--- New Sitemap Entries ---")
print("\n".join(urls))
