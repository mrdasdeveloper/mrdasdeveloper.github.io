import os
import re

cities = [
    {"name": "Dubai", "slug": "dubai", "pricing_market": "Dubai Agency"},
    {"name": "Abu Dhabi", "slug": "abu-dhabi", "pricing_market": "Abu Dhabi Agency"},
    {"name": "Sharjah", "slug": "sharjah", "pricing_market": "UAE Agency"},
    {"name": "Ajman", "slug": "ajman", "pricing_market": "UAE Agency"},
    {"name": "Ras Al Khaimah", "slug": "ras-al-khaimah", "pricing_market": "UAE Agency"},
    {"name": "Fujairah", "slug": "fujairah", "pricing_market": "UAE Agency"},
    {"name": "Umm Al Quwain", "slug": "umm-al-quwain", "pricing_market": "UAE Agency"},
    {"name": "Al Ain", "slug": "al-ain", "pricing_market": "UAE Agency"},
    {"name": "Khor Fakkan", "slug": "khor-fakkan", "pricing_market": "UAE Agency"},
    {"name": "Dibba Al-Fujairah", "slug": "dibba-al-fujairah", "pricing_market": "UAE Agency"}
]

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/"

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
              <li>• Build multi-tenant SaaS platform</li>
              <li>• Enterprise software developer {City}</li>
              <li>• B2B portal developer {City}</li>
              <li>• Custom CRM developer UAE</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">⚙️ Backend & AI</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire AI developer {City}</li>
              <li>• Python FastAPI specialist {City}</li>
              <li>• LLM integration expert UAE</li>
              <li>• RAG pipeline developer Middle East</li>
              <li>• Backend API engineer {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💻 Full-Stack & Frontend</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Hire React and Next.js developer</li>
              <li>• Freelance full-stack engineer {City}</li>
              <li>• Remote software engineer {City}</li>
              <li>• Best web app developer UAE</li>
              <li>• MERN stack developer {City}</li>
            </ul>
          </div>
          <div class="svc-card" style="padding: 16px;">
            <h3 style="color: var(--accent-hi);">💰 Hiring & Cost</h3>
            <ul style="list-style:none;padding:0;font-size:13px;color:var(--muted);line-height:1.8;margin-top:8px;">
              <li>• Cost to hire app developer {City}</li>
              <li>• Freelance web developer rates</li>
              <li>• Remote software developer salary UAE</li>
              <li>• Tech co-founder for hire UAE</li>
              <li>• Cheaper alternative to {PricingMarket}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

"""

for city in cities:
    filename = f"hire-full-stack-developer-{city['slug']}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "r") as f:
        content = f.read()
        
    # Prevent duplicate injection
    if "<!-- ── High-Value Keywords Section ── -->" in content:
        print(f"Skipping {filename}, already injected.")
        continue
        
    new_section = keyword_section_template.replace("{City}", city["name"]).replace("{PricingMarket}", city["pricing_market"])
    
    # Inject right before the SEO keyword cloud
    target_string = "<!-- ── SEO Keyword Cloud ── -->"
    if target_string in content:
        content = content.replace(target_string, new_section + target_string)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find target string in {filename}")

print("Update complete.")
