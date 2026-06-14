import os
import re

uae_cities = [
    {
        "name": "Dubai", "slug": "dubai",
        "ecosystem": "Startups, fintech, SaaS, AI companies",
        "focus_title": "Enterprise SaaS & Fintech Platforms",
        "focus_desc": "Highly scalable platforms powering Dubai's massive fintech and enterprise software ecosystem.",
        "hero_desc": "fintech innovators, AI startups, and enterprise operations",
        "pricing_market": "Dubai Agency"
    },
    {
        "name": "Abu Dhabi", "slug": "abu-dhabi",
        "ecosystem": "Government technology projects and AI hubs",
        "focus_title": "Government IT & AI Systems",
        "focus_desc": "Robust enterprise software tailored for Abu Dhabi's strong government and enterprise hiring demands.",
        "hero_desc": "government initiatives and major business hubs",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Sharjah", "slug": "sharjah",
        "ecosystem": "Growing startup and software market",
        "focus_title": "Startup Software & Enterprise IT",
        "focus_desc": "High-performance software engineering solutions tailored for Sharjah's growing tech sectors.",
        "hero_desc": "emerging startups and enterprise companies",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Ajman", "slug": "ajman",
        "ecosystem": "Growing business sector and local software companies",
        "focus_title": "Business Automation & Software",
        "focus_desc": "Systems engineering and automation platforms built specifically for Ajman's business sectors.",
        "hero_desc": "local businesses and automation networks",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Ras Al Khaimah", "slug": "ras-al-khaimah",
        "ecosystem": "Investment in technology and tourism tech",
        "focus_title": "Tourism Tech & Enterprise Software",
        "focus_desc": "Scalable software systems catering to Ras Al Khaimah's booming tourism and industrial tech.",
        "hero_desc": "tourism tech and enterprise software providers",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Fujairah", "slug": "fujairah",
        "ecosystem": "Logistics and digital transformation projects",
        "focus_title": "Logistics & Digital Transformation",
        "focus_desc": "Secure cloud applications built to support Fujairah's rapidly expanding logistics sector.",
        "hero_desc": "logistics networks and marine tech operations",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Umm Al Quwain", "slug": "umm-al-quwain",
        "ecosystem": "Local business and technology projects",
        "focus_title": "Local Digital Solutions",
        "focus_desc": "Enterprise solutions specializing in local business transformation for Umm Al Quwain.",
        "hero_desc": "local businesses and emerging digital sectors",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Al Ain", "slug": "al-ain",
        "ecosystem": "Education, healthcare, and government IT demand",
        "focus_title": "Healthcare & EdTech Platforms",
        "focus_desc": "Secure, compliant IT architectures tailored for Al Ain's healthcare and education projects.",
        "hero_desc": "healthcare providers and education tech hubs",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Khor Fakkan", "slug": "khor-fakkan",
        "ecosystem": "Port, logistics, and business technology",
        "focus_title": "Port Systems & Logistics IT",
        "focus_desc": "Custom IT services and specialized software built for Khor Fakkan's logistics sectors.",
        "hero_desc": "logistics providers and port operations",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Dibba Al-Fujairah", "slug": "dibba-al-fujairah",
        "ecosystem": "Local market and business technology",
        "focus_title": "Local Business IT Systems",
        "focus_desc": "Scalable web applications serving Dibba Al-Fujairah's local enterprise needs.",
        "hero_desc": "local retail and regional technology initiatives",
        "pricing_market": "UAE Agency"
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

    for city in uae_cities:
        content = base_content
        
        # Title and Description
        content = re.sub(r'<title>.*?</title>', f'<title>Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & UAE</title>', content)
        content = re.sub(r'<meta name="description" content=".*?" />', f'<meta name="description" content="Hire Ramesh Kumar Das, Top {tpl["role"]} in {city["name"]} & UAE. Building scalable systems for {city["hero_desc"]}." />', content)
        
        # Meta Keywords
        content = re.sub(r'<meta name="keywords" content=".*?" />', f'<meta name="keywords" content="hire {tpl["kw_prefix"]} {city["name"]}, {tpl["kw_prefix"]} for hire UAE, freelance developer {city["name"]}, Next.js developer {city["name"]}, remote developer UAE, SaaS developer Dubai, Ramesh Kumar Das" />', content)
        
        # Canonical & OG
        content = re.sub(r'<link rel="canonical" href=".*?\.html" />', f'<link rel="canonical" href="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & UAE" />', content)
        content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        
        # Schema Area Served
        content = content.replace('"areaServed":"Worldwide"', f'"areaServed":"{city["name"]}, UAE"')
        
        # Hero Adjustments
        content = content.replace('Available for Hire — Remote', 'Available for Hire — Remote (GST / UAE Timezone)')
        content = content.replace(f'<h1 id="hero-heading">{tpl["hero_original"]}</h1>', f'<h1 id="hero-heading">Top {tpl["role"]}<br>for {city["name"]} & UAE</h1>')
        
        # Add focus chip
        content = content.replace('<span class="chip neutral">Nepal &nbsp;·&nbsp; Remote</span>', f'<span class="chip neutral">{city["name"]} / UAE Focus</span>')
        
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
