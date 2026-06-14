import os

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"

# We will read index.html to steal the CSS/Header/Footer for consistency, then inject custom Hub Body.
with open(os.path.join(output_dir, "hire-full-stack-developer.html"), "r") as f:
    template = f.read()

# Extract header (up to the <div class="container"> tag)
header_match = template.split('<div class="container">')[0] + '<div class="container">\n'
footer_match = '\n</div>\n<footer class="footer">' + template.split('<footer class="footer">')[1]

japan_hubs = """
<main class="main">
  <section class="section">
    <div class="ps-inner" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <h1 style="font-size: 3rem; margin-bottom: 20px;">Hire Tech Talent in Japan 🇯🇵</h1>
      <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 40px; max-width: 800px;">
        Japan's tech ecosystem is rapidly evolving. We provide elite, remote-first Full-Stack, AI, and Backend developers aligned with JST (Japan Standard Time). Below are our localized hubs tailored for Japan's fastest-growing tech cities.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Tokyo</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Enterprise SaaS & AI Platforms</p>
          <a href="hire-full-stack-developer-tokyo.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-tokyo.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-tokyo.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Osaka</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Business Innovation IT Systems</p>
          <a href="hire-full-stack-developer-osaka.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-osaka.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-osaka.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Yokohama</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Corporate Tech & R&D Platforms</p>
          <a href="hire-full-stack-developer-yokohama.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-yokohama.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-yokohama.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Nagoya</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Industrial & Automotive Software</p>
          <a href="hire-full-stack-developer-nagoya.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-nagoya.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-nagoya.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Fukuoka</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Startup MVP & SaaS Development</p>
          <a href="hire-full-stack-developer-fukuoka.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-fukuoka.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-fukuoka.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Kyoto</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Research & AI Technology</p>
          <a href="hire-full-stack-developer-kyoto.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-kyoto.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-kyoto.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Sapporo</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Remote Tech & Cloud Infrastructure</p>
          <a href="hire-full-stack-developer-sapporo.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-sapporo.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-sapporo.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Kobe</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Logistics Tech & Digital Transformation</p>
          <a href="hire-full-stack-developer-kobe.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-kobe.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-kobe.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Sendai</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Government & Regional Tech Systems</p>
          <a href="hire-full-stack-developer-sendai.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-sendai.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-sendai.html" style="display: block;">↳ Backend Engineer</a>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px;">Hiroshima</h2>
          <p style="color: var(--dim); font-size: 14px; margin-bottom: 16px;">Engineering IT & Industrial Software</p>
          <a href="hire-full-stack-developer-hiroshima.html" style="display: block; margin-bottom: 8px;">↳ Full-Stack Developer</a>
          <a href="hire-ai-full-stack-engineer-hiroshima.html" style="display: block; margin-bottom: 8px;">↳ AI Full-Stack Engineer</a>
          <a href="hire-backend-engineer-hiroshima.html" style="display: block;">↳ Backend Engineer</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""

mena_hubs = """
<main class="main">
  <section class="section">
    <div class="ps-inner" style="max-width: 1000px; margin: 0 auto; padding: 40px 20px;">
      <h1 style="font-size: 3rem; margin-bottom: 20px;">Hire Tech Talent in the Middle East 🌍</h1>
      <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 40px; max-width: 800px;">
        The Middle East is accelerating its digital transformation. We provide elite, remote-first Full-Stack, AI, and Backend developers perfectly aligned with Gulf Standard Time (GST). Explore our specialized hubs for the UAE and Qatar below.
      </p>

      <h2 style="font-size: 2rem; margin-bottom: 20px; color: var(--accent-hi);">United Arab Emirates (UAE)</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px;">
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-dubai.html" style="font-size: 1.2rem; font-weight: bold;">Dubai</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Startups, Fintech & SaaS</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-abu-dhabi.html" style="font-size: 1.2rem; font-weight: bold;">Abu Dhabi</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">GovTech & Enterprise</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-sharjah.html" style="font-size: 1.2rem; font-weight: bold;">Sharjah</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">EdTech & Software Market</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-ajman.html" style="font-size: 1.2rem; font-weight: bold;">Ajman</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Business Automation</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-ras-al-khaimah.html" style="font-size: 1.2rem; font-weight: bold;">Ras Al Khaimah</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Tourism & Manufacturing IT</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-fujairah.html" style="font-size: 1.2rem; font-weight: bold;">Fujairah</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Logistics & Marine Tech</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-umm-al-quwain.html" style="font-size: 1.2rem; font-weight: bold;">Umm Al Quwain</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Local Digital Presence</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-al-ain.html" style="font-size: 1.2rem; font-weight: bold;">Al Ain</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Healthcare & Education IT</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-khor-fakkan.html" style="font-size: 1.2rem; font-weight: bold;">Khor Fakkan</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Port & Logistics Scheduling</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-dibba-al-fujairah.html" style="font-size: 1.2rem; font-weight: bold;">Dibba Al-Fujairah</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Trading & Retail Systems</p>
        </div>
      </div>

      <h2 style="font-size: 2rem; margin-bottom: 20px; color: var(--accent-hi);">Qatar</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-doha.html" style="font-size: 1.2rem; font-weight: bold;">Doha</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Fintech & Telecom Hub</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-al-rayyan.html" style="font-size: 1.2rem; font-weight: bold;">Al Rayyan</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Education City IT Solutions</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-lusail.html" style="font-size: 1.2rem; font-weight: bold;">Lusail</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Smart City & IoT</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-al-wakrah.html" style="font-size: 1.2rem; font-weight: bold;">Al Wakrah</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Commercial Automation</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-umm-salal.html" style="font-size: 1.2rem; font-weight: bold;">Umm Salal</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Enterprise Integrations</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-al-khor.html" style="font-size: 1.2rem; font-weight: bold;">Al Khor</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Energy Tech & Industrial</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-al-daayen.html" style="font-size: 1.2rem; font-weight: bold;">Al Daayen</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Infrastructure Tech</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-mesaieed.html" style="font-size: 1.2rem; font-weight: bold;">Mesaieed</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Enterprise Software Hubs</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-dukhan.html" style="font-size: 1.2rem; font-weight: bold;">Dukhan</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Oil & Gas Support IT</p>
        </div>
        <div class="svc-card" style="padding: 24px;">
          <a href="hire-full-stack-developer-madinat-ash-shamal.html" style="font-size: 1.2rem; font-weight: bold;">Madinat ash Shamal</a>
          <p style="color: var(--dim); font-size: 13px; margin-top: 8px;">Localized Business Systems</p>
        </div>
      </div>
    </div>
  </section>
</main>
"""

def generate_hub(filename, body_content, title, description):
    # Adjust title and meta in header
    h = header_match.replace("<title>Hire Ramesh Kumar Das — Senior Full-Stack Developer | React, Next.js, Node.js, FastAPI</title>", f"<title>{title}</title>")
    h = h.replace('<meta name="description" content="Senior Full-Stack Developer with 6.5+ years. Expert in React.js, Next.js, Node.js, FastAPI. Available for remote hire." />', f'<meta name="description" content="{description}" />')
    
    full_html = h + body_content + footer_match
    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(full_html)
    print(f"Generated {filename}")

generate_hub(
    "hire-developers-japan.html", 
    japan_hubs, 
    "Hire Tech Talent in Japan — Developers Hub | React, AI, Node.js", 
    "Hire elite remote developers specialized for the Japan market (Tokyo, Osaka, etc.). AI, Full-Stack, and Backend engineers available on JST."
)

generate_hub(
    "hire-developers-middle-east.html", 
    mena_hubs, 
    "Hire Tech Talent in the Middle East — UAE & Qatar Hub", 
    "Hire top-tier remote developers for the Middle East (Dubai, Doha, Abu Dhabi). Specialized in SaaS, AI, and Government tech on Gulf Standard Time."
)

