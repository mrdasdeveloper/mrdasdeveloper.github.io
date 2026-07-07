import os
import re

qatar_cities = [
    {
        "name": "Doha",
        "slug": "doha",
        "ecosystem": "Qatar Financial Centre, fintech, telecom, and government digital transformation hubs",
        "focus_title": "Fintech & Enterprise AI Platforms",
        "focus_desc": "End-to-end scalable enterprise solutions, fintech applications, and government digital transformation systems built with Next.js and FastAPI.",
        "hero_desc": "fintech startups, telecom enterprises, and government tech sectors",
        "pricing_market": "Doha Agency"
    },
    {
        "name": "Al Rayyan",
        "slug": "al-rayyan",
        "ecosystem": "Education City, universities, and commercial business districts",
        "focus_title": "EdTech & Business IT Solutions",
        "focus_desc": "Custom learning management systems and robust enterprise IT solutions serving Al Rayyan's universities and growing commercial zones.",
        "hero_desc": "universities, educational initiatives, and commercial enterprises",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Lusail",
        "slug": "lusail",
        "ecosystem": "Smart city developments, IoT hubs, and modern digital infrastructure",
        "focus_title": "Smart City & IoT Infrastructure",
        "focus_desc": "High-performance backend architectures powering IoT, smart city dashboards, and data-intensive platforms for Lusail's expanding digital ecosystem.",
        "hero_desc": "smart city initiatives, IoT startups, and modern digital infrastructure projects",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Al Wakrah",
        "slug": "al-wakrah",
        "ecosystem": "Al Wakrah's growing commercial sector and logistics networks",
        "focus_title": "Commercial Automation & Logistics Tech",
        "focus_desc": "Digital transformation tools and custom supply chain tracking platforms designed for growing commercial and logistics sectors.",
        "hero_desc": "logistics networks and expanding commercial business sectors",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Umm Salal",
        "slug": "umm-salal",
        "ecosystem": "expanding local business districts and enterprise sectors",
        "focus_title": "Enterprise Software & IT Integration",
        "focus_desc": "Tailored enterprise resource planning and local IT software solutions designed to modernize expanding business districts.",
        "hero_desc": "local enterprise sectors and expanding business operations",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Al Khor",
        "slug": "al-khor",
        "ecosystem": "Energy, industrial hubs, and oil/gas technology sectors",
        "focus_title": "Energy Tech & Industrial Data Systems",
        "focus_desc": "Secure data management platforms, predictive maintenance dashboards, and custom software for the energy and industrial sectors.",
        "hero_desc": "energy companies, industrial enterprises, and data-driven sectors",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Al Daayen",
        "slug": "al-daayen",
        "ecosystem": "rapidly developing municipalities and infrastructure projects",
        "focus_title": "Infrastructure Tech & Automation",
        "focus_desc": "Scalable web applications supporting smart-city projects, municipal automation, and fast-growing infrastructure developments.",
        "hero_desc": "infrastructure developers, municipal projects, and smart-city initiatives",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Mesaieed",
        "slug": "mesaieed",
        "ecosystem": "Mesaieed Industrial City and enterprise software hubs",
        "focus_title": "Industrial Enterprise Software",
        "focus_desc": "Heavy-duty enterprise software solutions supporting industrial tracking, energy operations, and large-scale manufacturing IT.",
        "hero_desc": "industrial operations, energy sectors, and heavy manufacturing IT",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Dukhan",
        "slug": "dukhan",
        "ecosystem": "Qatar's vital oil and gas technology networks",
        "focus_title": "Oil & Gas IT Support Systems",
        "focus_desc": "Specialized internal tooling, data visualization systems, and compliance-driven software for the oil and gas sector.",
        "hero_desc": "oil and gas technology departments and technical IT support sectors",
        "pricing_market": "Qatar Agency"
    },
    {
        "name": "Madinat ash Shamal",
        "slug": "madinat-ash-shamal",
        "ecosystem": "emerging local markets and localized business networks",
        "focus_title": "Local Digital Presence & Automation",
        "focus_desc": "Responsive web applications and streamlined business automation tools capturing emerging local search demand.",
        "hero_desc": "emerging local businesses and long-tail digital growth markets",
        "pricing_market": "Qatar Agency"
    }
]

base_file = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/hire-full-stack-developer.html"
with open(base_file, "r") as f:
    template = f.read()

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
              <li>• Build scalable SaaS platform Qatar</li>
              <li>• Enterprise software developer {City}</li>
              <li>• Business portal developer {City}</li>
              <li>• Custom CRM developer Qatar</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">⚙️ Backend & AI</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire AI developer {City}</li>
              <li>• Python FastAPI specialist {City}</li>
              <li>• Smart city software engineer {City}</li>
              <li>• LLM integration expert Qatar</li>
              <li>• Backend API engineer {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💻 Full-Stack & Frontend</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire React and Next.js developer</li>
              <li>• Freelance full-stack engineer {City}</li>
              <li>• Remote software engineer {City}</li>
              <li>• Best web app developer Qatar</li>
              <li>• MERN stack developer {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💰 Hiring & Cost</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Cost to hire app developer {City}</li>
              <li>• Freelance web developer rates</li>
              <li>• Remote software developer salary Qatar</li>
              <li>• Tech co-founder for hire Qatar</li>
              <li>• Cheaper alternative to {PricingMarket}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

"""

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/"
urls = []

for city in qatar_cities:
    content = template
    
    # 1. Update Title and Meta
    content = re.sub(r'<title>.*?</title>', f'<title>Hire Ramesh Kumar Das — Top Full-Stack AI Developer in {city["name"]} & Qatar</title>', content)
    content = re.sub(r'<meta name="description" content=".*?" />', f'<meta name="description" content="Hire Ramesh Kumar Das, Top Full-Stack AI Developer in {city["name"]} & Qatar. Expert in React, Next.js, FastAPI. Building scalable SaaS for {city["hero_desc"]}." />', content)
    content = re.sub(r'<meta name="keywords" content=".*?" />', f'<meta name="keywords" content="hire full-stack developer {city["name"]}, full stack developer for hire Qatar, freelance AI engineer {city["name"]}, Next.js developer {city["name"]}, remote full stack developer Qatar, SaaS developer Middle East, Ramesh Kumar Das" />', content)
    content = re.sub(r'<link rel="canonical" href=".*?hire-full-stack-developer\.html" />', f'<link rel="canonical" href="https://www.rameshdas.dev/hire-full-stack-developer-{city["slug"]}.html" />', content)
    
    # OG Tags
    content = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="Hire Ramesh Kumar Das — Top Full-Stack AI Developer in {city["name"]} & Qatar" />', content)
    content = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://www.rameshdas.dev/hire-full-stack-developer-{city["slug"]}.html" />', content)
    
    # Schema Area Served
    content = content.replace('"areaServed":"Worldwide"', f'"areaServed":"{city["name"]}, Qatar"')
    
    # Hero Adjustments
    content = content.replace('Available for Hire — Remote', 'Available for Hire — Remote (AST / Qatar Timezone)')
    content = content.replace('<h1 id="hero-heading">Senior Full-Stack<br>Developer for Hire</h1>', f'<h1 id="hero-heading">Top Full-Stack AI<br>Developer for {city["name"]} & Qatar</h1>')
    content = content.replace('building scalable web applications, SaaS platforms, and distributed backend systems.', f'building scalable web applications, SaaS platforms, and distributed backend systems for the Qatar market.')
    
    # Add focus chip
    content = content.replace('<span class="chip neutral">Nepal &nbsp;·&nbsp; Remote</span>', f'<span class="chip neutral">{city["name"]} / Qatar Focus</span>')
    
    # Services
    content = content.replace('<h2>What I Can Build For You</h2>', f'<h2>What I Can Build For Your {city["name"]} Business</h2>')
    content = content.replace('<p>Full-stack engineering services for startups, scale-ups, and enterprises</p>', f'<p>Full-stack engineering services tailored for {city["ecosystem"]}</p>')
    
    # Replace first service card to highlight the local focus
    content = re.sub(r'<div class="svc-card"><h3>🚀 SaaS Platform Development.*?</div>', f'<div class="svc-card"><h3>🚀 {city["focus_title"]}</h3><p>{city["focus_desc"]}</p></div>', content, count=1)
    
    # Pricing market reference
    content = content.replace('Market Standard:', f'{city["pricing_market"]}:')
    
    # Inject High Value Keywords
    kw_section = keyword_section_template.replace("{City}", city["name"]).replace("{PricingMarket}", city["pricing_market"])
    content = content.replace('<!-- ── SEO Keyword Cloud ── -->', kw_section + '<!-- ── SEO Keyword Cloud ── -->')
    
    # SEO Keyword Cloud Adjustments (just basic string replacements for the cloud area)
    content = content.replace('Hire Full-Stack Developer · Related Expertise', f'Hire Full-Stack Developer · {city["name"]} & Qatar')
    content = content.replace('href="/hire-full-stack-developer.html"', f'href="/hire-full-stack-developer-{city["slug"]}.html"')
    
    # Generate the file
    filename = f"hire-full-stack-developer-{city['slug']}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Save file
    with open(filepath, "w") as out_f:
        out_f.write(content)
        
    print(f"Generated {filename}")
    urls.append(f"<url><loc>https://www.rameshdas.dev/{filename}</loc><lastmod>2026-06-12</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>")

print("\n--- Sitemap Entries ---")
print("\n".join(urls))
