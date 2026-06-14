import os
from datetime import datetime

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f not in ('google9bae3598255dbb1e.html', 'pinterest-6f253.html')]

today = datetime.now().strftime("%Y-%m-%d")

# ── Priority map for main / core pages ────────────────────────────────────────
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
    'sitemap.html': 0.70,
}

# ── Country / city slug mappings ──────────────────────────────────────────────
country_slugs = {
    "usa": ["san-francisco", "new-york", "seattle", "austin", "boston"],
    "uk": ["london", "manchester", "cambridge"],
    "canada": ["toronto", "vancouver", "montreal"],
    "australia": ["sydney", "melbourne", "brisbane"],
    "germany": ["berlin", "munich", "hamburg", "frankfurt", "stuttgart"],
    "japan": ["tokyo", "osaka", "yokohama", "nagoya", "fukuoka", "kyoto", "sapporo", "kobe", "sendai", "hiroshima"],
    "singapore": ["singapore", "marina-bay", "one-north", "jurong-east", "tampines"],
    "saudi-arabia": ["riyadh", "jeddah", "dammam", "khobar", "dhahran", "mecca", "medina", "tabuk", "abha", "yanbu"],
    "uae": ["dubai", "abu-dhabi", "sharjah", "ajman", "ras-al-khaimah", "fujairah", "umm-al-quwain", "al-ain", "khor-fakkan", "dibba-al-fujairah"],
    "qatar": ["doha", "al-rayyan", "lusail", "al-wakrah", "umm-salal", "al-khor", "al-daayen", "mesaieed", "dukhan", "madinat-ash-shamal"]
}

hubs_mapping = {
    "usa": "hire-developers-usa.html",
    "uk": "hire-developers-uk.html",
    "canada": "hire-developers-canada.html",
    "australia": "hire-developers-australia.html",
    "germany": "hire-developers-germany.html",
    "japan": "hire-developers-japan.html",
    "singapore": "hire-developers-singapore.html",
    "saudi-arabia": "hire-developers-saudi-arabia.html",
    "middle-east": "hire-developers-middle-east.html"
}

def make_url(loc, changefreq, priority):
    """Return a fully-formed <url> element string."""
    return (
        f"  <url>\n"
        f"    <loc>https://mrdasdeveloper.github.io/{loc}</loc>\n"
        f"    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        f"  </url>"
    )

# ── Collect ALL URLs in priority order ────────────────────────────────────────
all_urls = []
processed = set()

# 1. High-priority main / core pages
for page, priority in main_pages.items():
    if page in html_files:
        loc = "" if page == "index.html" else page
        all_urls.append(make_url(loc, "weekly", priority))
        processed.add(page)

# 2. LLM knowledge files
all_urls.append(make_url("llm.txt",      "monthly", "0.70"))
all_urls.append(make_url("full-llm.txt", "monthly", "0.70"))

# 3. Country hub pages (priority 0.90)
for country, hub_file in hubs_mapping.items():
    if hub_file in html_files and hub_file not in processed:
        all_urls.append(make_url(hub_file, "weekly", "0.90"))
        processed.add(hub_file)

# 4. City-specific pages grouped by country (priority 0.85)
for country, slugs in country_slugs.items():
    for slug in slugs:
        for f in sorted(html_files):
            if f.endswith(f"-{slug}.html") and f not in processed:
                all_urls.append(make_url(f, "weekly", "0.85"))
                processed.add(f)

# 5. Any remaining HTML files not yet categorised
for f in sorted(html_files):
    if f not in processed:
        all_urls.append(make_url(f, "weekly", "0.80"))
        processed.add(f)

# ── Build the single flat <urlset> sitemap ────────────────────────────────────
# WHY FLAT?  Google Search Console requires a sitemapindex to successfully
# fetch *every* child sitemap before it marks the index as "Success".
# On GitHub Pages a single CDN cache miss on any sub-sitemap causes
# "Sitemap could not be read".  A single <urlset> file (like winsta.ai)
# removes that dependency and always works correctly.
sitemap_xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
    '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9'
    ' http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'
    + "\n".join(all_urls)
    + '\n</urlset>\n'
)

out_path = os.path.join(directory, "sitemap.xml")
with open(out_path, "w", encoding="utf-8") as fh:
    fh.write(sitemap_xml)

size_kb = len(sitemap_xml.encode("utf-8")) / 1024
print(f"✅  sitemap.xml — single flat <urlset> — {len(all_urls)} URLs — {size_kb:.1f} KB")
print(f"    Google's 50 000-URL / 50 MB limit: {'OK' if len(all_urls) < 50000 and size_kb < 51200 else 'EXCEEDED'}")
print(f"    Same structure as winsta.ai/sitemap.xml  →  GSC compatible ✔")
