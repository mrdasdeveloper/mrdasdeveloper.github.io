import os

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"

with open(os.path.join(output_dir, "hire-full-stack-developer.html"), "r") as f:
    template = f.read()

header_match = template.split('<div class="container">')[0] + '<div class="container">\n'
footer_match = '\n</div>\n<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]

uae_cities = [
    {"name": "Dubai", "slug": "dubai", "desc": "Startups, Fintech & SaaS"},
    {"name": "Abu Dhabi", "slug": "abu-dhabi", "desc": "GovTech & Enterprise"},
    {"name": "Sharjah", "slug": "sharjah", "desc": "EdTech & Software Market"},
    {"name": "Ajman", "slug": "ajman", "desc": "Business Automation"},
    {"name": "Ras Al Khaimah", "slug": "ras-al-khaimah", "desc": "Tourism & Manufacturing IT"},
    {"name": "Fujairah", "slug": "fujairah", "desc": "Logistics & Marine Tech"},
    {"name": "Umm Al Quwain", "slug": "umm-al-quwain", "desc": "Local Digital Presence"},
    {"name": "Al Ain", "slug": "al-ain", "desc": "Healthcare & Education IT"},
    {"name": "Khor Fakkan", "slug": "khor-fakkan", "desc": "Port & Logistics Scheduling"},
    {"name": "Dibba Al-Fujairah", "slug": "dibba-al-fujairah", "desc": "Trading & Retail Systems"}
]

qatar_cities = [
    {"name": "Doha", "slug": "doha", "desc": "Fintech & Telecom Hub"},
    {"name": "Al Rayyan", "slug": "al-rayyan", "desc": "Education City IT Solutions"},
    {"name": "Lusail", "slug": "lusail", "desc": "Smart City & IoT"},
    {"name": "Al Wakrah", "slug": "al-wakrah", "desc": "Commercial Automation"},
    {"name": "Umm Salal", "slug": "umm-salal", "desc": "Enterprise Integrations"},
    {"name": "Al Khor", "slug": "al-khor", "desc": "Energy Tech & Industrial"},
    {"name": "Al Daayen", "slug": "al-daayen", "desc": "Infrastructure Tech"},
    {"name": "Mesaieed", "slug": "mesaieed", "desc": "Enterprise Software Hubs"},
    {"name": "Dukhan", "slug": "dukhan", "desc": "Oil & Gas Support IT"},
    {"name": "Madinat ash Shamal", "slug": "madinat-ash-shamal", "desc": "Localized Business Systems"}
]

mena_hubs = """
<main class="main">
  <section class="section">
    <div class="ps-inner" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <h1 style="font-size: 3rem; margin-bottom: 20px;">Hire Tech Talent in the Middle East 🌍</h1>
      <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 40px; max-width: 800px;">
        The Middle East is accelerating its digital transformation. We provide elite, remote-first Full-Stack, AI, and Backend developers perfectly aligned with Gulf Standard Time (GST). Explore our specialized hubs for the UAE and Qatar below.
      </p>

      <h2 style="font-size: 2rem; margin-bottom: 20px; color: var(--accent-hi);">United Arab Emirates (UAE)</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 40px;">
"""
for city in uae_cities:
    mena_hubs += f"""
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">{city["name"]}</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">{city["desc"]}</p>
          <a href="hire-full-stack-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-{city["slug"]}.html" style="display: block;">↳ Backend Engineer</a>
        </div>
"""

mena_hubs += """
      </div>

      <h2 style="font-size: 2rem; margin-bottom: 20px; color: var(--accent-hi);">Qatar</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
"""
for city in qatar_cities:
    mena_hubs += f"""
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">{city["name"]}</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">{city["desc"]}</p>
          <a href="hire-full-stack-developer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-{city["slug"]}.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-{city["slug"]}.html" style="display: block;">↳ Backend Engineer</a>
        </div>
"""

mena_hubs += """
      </div>
    </div>
  </section>
</main>
"""

def generate_hub(filename, body_content, title, description):
    h = header_match.replace("<title>Hire Ramesh Kumar Das — Senior Full-Stack Developer | React, Next.js, Node.js, FastAPI</title>", f"<title>{title}</title>")
    h = h.replace('<meta name="description" content="Senior Full-Stack Developer with 6.5+ years. Expert in React.js, Next.js, Node.js, FastAPI. Available for remote hire." />', f'<meta name="description" content="{description}" />')
    
    full_html = h + body_content + footer_match
    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(full_html)
    print(f"Generated {filename}")

generate_hub(
    "hire-developers-middle-east.html", 
    mena_hubs, 
    "Hire Tech Talent in the Middle East — UAE & Qatar Hub", 
    "Hire top-tier remote developers for the Middle East (Dubai, Doha, Abu Dhabi). Specialized in SaaS, AI, and Government tech on Gulf Standard Time."
)
