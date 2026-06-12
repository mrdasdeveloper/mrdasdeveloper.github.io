import os
import re

japan_cities = [
    {
        "name": "Tokyo", "slug": "tokyo",
        "ecosystem": "AI startups, SaaS companies, fintech, and enterprise software hubs",
        "focus_title": "Enterprise SaaS & AI Platforms",
        "focus_desc": "Highly scalable platforms powering Tokyo's massive fintech and enterprise software ecosystem.",
        "hero_desc": "fintech innovators, AI startups, and enterprise operations",
        "pricing_market": "Tokyo Agency"
    },
    {
        "name": "Osaka", "slug": "osaka",
        "ecosystem": "major business districts and technology innovation hubs",
        "focus_title": "Business Innovation IT Systems",
        "focus_desc": "Robust enterprise software tailored for Osaka's strong startup and enterprise hiring demands.",
        "hero_desc": "major business hubs and growing startups",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Yokohama", "slug": "yokohama",
        "ecosystem": "large corporate technology centers and R&D facilities",
        "focus_title": "Corporate Tech & R&D Platforms",
        "focus_desc": "High-performance software engineering solutions tailored for Yokohama's R&D and large corporate sectors.",
        "hero_desc": "large corporate technology players and R&D facilities",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Nagoya", "slug": "nagoya",
        "ecosystem": "manufacturing technology and automotive software sectors",
        "focus_title": "Industrial & Automotive Software",
        "focus_desc": "Systems engineering and AI platforms built specifically for Nagoya's advanced manufacturing and automotive tech.",
        "hero_desc": "automotive technology and industrial manufacturing",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Fukuoka", "slug": "fukuoka",
        "ecosystem": "startup-friendly zones and growing SaaS ecosystems",
        "focus_title": "Startup MVP & SaaS Development",
        "focus_desc": "Agile software development catering to Fukuoka's thriving startup and emerging SaaS environments.",
        "hero_desc": "SaaS startups and agile tech businesses",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Kyoto", "slug": "kyoto",
        "ecosystem": "university-driven innovation, gaming, and AI research",
        "focus_title": "Research & AI Technology",
        "focus_desc": "Deep tech integrations and scalable software systems for Kyoto's gaming and AI research networks.",
        "hero_desc": "AI research centers, gaming, and technology companies",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Sapporo", "slug": "sapporo",
        "ecosystem": "growing remote-tech and emerging software sectors",
        "focus_title": "Remote Tech & Cloud Infrastructure",
        "focus_desc": "Distributed cloud applications built to support Sapporo's rapidly expanding remote-tech software sector.",
        "hero_desc": "remote tech operations and emerging software sectors",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Kobe", "slug": "kobe",
        "ecosystem": "enterprise technology and logistics tech networks",
        "focus_title": "Logistics Tech & Digital Transformation",
        "focus_desc": "Enterprise solutions specializing in digital transformation and logistics optimization for Kobe's businesses.",
        "hero_desc": "logistics networks and enterprise technology",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Sendai", "slug": "sendai",
        "ecosystem": "government projects and regional tech hubs",
        "focus_title": "Government & Regional Tech Systems",
        "focus_desc": "Secure, compliant IT architectures tailored for Sendai's government and regional research projects.",
        "hero_desc": "regional tech hubs and government projects",
        "pricing_market": "Japanese Agency"
    },
    {
        "name": "Hiroshima", "slug": "hiroshima",
        "ecosystem": "industrial software and engineering technology sectors",
        "focus_title": "Engineering IT & Industrial Software",
        "focus_desc": "Custom IT services and specialized industrial software built for Hiroshima's engineering sectors.",
        "hero_desc": "industrial software providers and engineering technology",
        "pricing_market": "Japanese Agency"
    }
]

templates = [
    {
        "file": "hire-full-stack-developer.html",
        "slug_prefix": "hire-full-stack-developer-",
        "role": "Full-Stack Developer",
        "hero_original": "Senior Full-Stack<br>Developer for Hire",
        "title_original": "Hire Ramesh Kumar Das — Senior Full-Stack Developer | React, Next.js, Node.js, FastAPI",
        "kw_prefix": "full-stack developer"
    },
    {
        "file": "hire-ai-full-stack-engineer.html",
        "slug_prefix": "hire-ai-full-stack-engineer-",
        "role": "AI Full-Stack Engineer",
        "hero_original": "AI Full-Stack<br>Engineer for Hire",
        "title_original": "Hire Ramesh — AI Full-Stack Engineer | Generative AI, LLMs, RAG, FastAPI, Next.js",
        "kw_prefix": "AI engineer"
    },
    {
        "file": "hire-backend-engineer.html",
        "slug_prefix": "hire-backend-engineer-",
        "role": "Backend Engineer",
        "hero_original": "Senior Backend<br>Engineer for Hire",
        "title_original": "Hire Ramesh Kumar Das — Senior Backend Engineer | Node.js, FastAPI, Django, PostgreSQL",
        "kw_prefix": "backend engineer"
    }
]

keyword_section_template = """
    <!-- ── High-Value Keywords Section ── -->
    <section class="section" id="high-value-searches" style="padding-top: 20px; padding-bottom: 20px;">
      <div class="ps-inner" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
        <div class="section-header">
          <h2>🔥 Popular Tech Hiring Searches in {City}</h2>
          <p>Businesses and founders in {City} frequently search for these specialized development services:</p>
        </div>
        <div class="svc-grid" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));">
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">📈 SaaS & Enterprise</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• SaaS MVP developer cost in {City}</li>
              <li>• Build scalable software {City}</li>
              <li>• Enterprise software developer {City}</li>
              <li>• Business portal developer Japan</li>
              <li>• Custom CRM developer Japan</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">⚙️ Backend & AI</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire AI developer {City}</li>
              <li>• Python FastAPI specialist {City}</li>
              <li>• LLM integration expert Japan</li>
              <li>• Secure API engineer {City}</li>
              <li>• Node.js microservices {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💻 Full-Stack & Frontend</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire React and Next.js developer</li>
              <li>• Freelance full-stack engineer {City}</li>
              <li>• Remote software engineer {City}</li>
              <li>• Best web app developer Japan</li>
              <li>• MERN stack developer {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💰 Hiring & Cost</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Cost to hire app developer {City}</li>
              <li>• Freelance web developer rates</li>
              <li>• Remote software developer salary Japan</li>
              <li>• Tech co-founder for hire Japan</li>
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

    for city in japan_cities:
        content = base_content
        
        # Title and Description
        content = re.sub(r'<title>.*?</title>', f'<title>Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & Japan</title>', content)
        content = re.sub(r'<meta name="description" content=".*?" />', f'<meta name="description" content="Hire Ramesh Kumar Das, Top {tpl["role"]} in {city["name"]} & Japan. Building scalable systems for {city["hero_desc"]}." />', content)
        
        # Meta Keywords
        content = re.sub(r'<meta name="keywords" content=".*?" />', f'<meta name="keywords" content="hire {tpl["kw_prefix"]} {city["name"]}, {tpl["kw_prefix"]} for hire Japan, freelance developer {city["name"]}, Next.js developer {city["name"]}, remote developer Japan, SaaS developer Asia, Ramesh Kumar Das" />', content)
        
        # Canonical & OG
        content = re.sub(r'<link rel="canonical" href=".*?\.html" />', f'<link rel="canonical" href="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="Hire Ramesh Kumar Das — Top {tpl["role"]} in {city["name"]} & Japan" />', content)
        content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://mrdasdeveloper.github.io/{tpl["slug_prefix"]}{city["slug"]}.html" />', content)
        
        # Schema Area Served
        content = content.replace('"areaServed":"Worldwide"', f'"areaServed":"{city["name"]}, Japan"')
        
        # Hero Adjustments
        content = content.replace('Available for Hire — Remote', 'Available for Hire — Remote (JST / Japan Timezone)')
        content = content.replace(f'<h1 id="hero-heading">{tpl["hero_original"]}</h1>', f'<h1 id="hero-heading">Top {tpl["role"]}<br>for {city["name"]} & Japan</h1>')
        
        # Add focus chip
        content = content.replace('<span class="chip neutral">Nepal &nbsp;·&nbsp; Remote</span>', f'<span class="chip neutral">{city["name"]} / Japan Focus</span>')
        
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
