import os
from datetime import datetime

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f not in ('google9bae3598255dbb1e.html', 'pinterest-6f253.html')]

sitemap_entries = []

# Main pages
main_pages = {
    'index.html': 1.0,
    'hire-ai-full-stack-engineer.html': 0.95,
    'hire-full-stack-developer.html': 0.95,
    'hire-backend-engineer.html': 0.95,
    'agentic-ai-developer.html': 0.90,
    'full-stack-ai-engineer.html': 0.90,
    'ai-backend-architecture-microservices-engineering-guide.html': 0.88,
    'business-automation.html': 0.88,
    'freelancer.html': 0.85,
    'presentation.html': 0.85,
}

today = datetime.now().strftime("%Y-%m-%d")

# Header
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
          http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
"""

# Process main pages
for page, priority in main_pages.items():
    if page in html_files:
        path = "" if page == "index.html" else page
        sitemap_xml += f"""
  <url>
    <loc>https://mrdasdeveloper.github.io/{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
        html_files.remove(page)

# Process hubs
hub_files = [f for f in html_files if f.startswith('hire-developers-')]
for hub in hub_files:
    sitemap_xml += f"""
  <url>
    <loc>https://mrdasdeveloper.github.io/{hub}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.90</priority>
  </url>"""
    html_files.remove(hub)

# Process the rest (city pages)
for city_page in sorted(html_files):
    # Determine priority based on importance. We'll use 0.85 generally for city pages now
    sitemap_xml += f"""
  <url>
    <loc>https://mrdasdeveloper.github.io/{city_page}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>"""

# Add the txt files
sitemap_xml += f"""
  <url>
    <loc>https://mrdasdeveloper.github.io/llm.txt</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://mrdasdeveloper.github.io/full-llm.txt</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.70</priority>
  </url>
</urlset>
"""

with open(os.path.join(directory, "sitemap.xml"), "w") as f:
    f.write(sitemap_xml)

print(f"Generated sitemap.xml with {len(main_pages) + len(hub_files) + len(html_files) + 2} entries.")
