"""
update_sitemap.py
=================
Generates a Sitemap Index (sitemap.xml) + country-based sub-sitemaps.

ARCHITECTURE (Upwork-style):
  sitemap.xml             ← Sitemap Index listing all sub-sitemaps
    sitemap-main.xml      ← Core pages (homepage, hire pages, etc.)
    sitemap-usa.xml       ← All US city pages
    sitemap-uk.xml        ← All UK city pages
    sitemap-germany.xml
    sitemap-japan.xml
    sitemap-singapore.xml
    sitemap-canada.xml
    sitemap-australia.xml
    sitemap-saudi-arabia.xml
    sitemap-uae.xml
    sitemap-qatar.xml
    sitemap-middle-east.xml

WHY THIS WORKS IN GSC:
  - Every sub-sitemap is committed to GitHub before the index is submitted.
  - lastmod uses full ISO 8601 datetime (e.g. 2026-06-14T02:30:00+00:00).
  - All sub-sitemaps are valid <urlset> XML (schema-validated).
  - Submit each sub-sitemap individually in GSC for maximum indexing.
"""

import os
from datetime import datetime, timezone

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
BASE_URL  = "https://mrdasdeveloper.github.io"

html_files = [
    f for f in os.listdir(directory)
    if f.endswith('.html')
    and f not in ('google9bae3598255dbb1e.html', 'pinterest-6f253.html')
]

# ISO 8601 with UTC timezone — required for Upwork-style lastmod
now_iso  = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
today    = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# ── Priority map for core / main pages ────────────────────────────────────────
main_pages = {
    'index.html':                                          1.0,
    'hire-ai-full-stack-engineer.html':                    0.95,
    'hire-full-stack-developer.html':                      0.95,
    'hire-backend-engineer.html':                          0.95,
    'agentic-ai-developer.html':                           0.90,
    'full-stack-ai-engineer.html':                         0.90,
    'ai-backend-architecture-microservices-engineering-guide.html': 0.88,
    'business-automation.html':                            0.88,
    'freelancer.html':                                     0.85,
    'presentation.html':                                   0.85,
    'sitemap.html':                                        0.70,
}

# ── Country → city slug mappings ──────────────────────────────────────────────
country_slugs = {
    "usa":          ["san-francisco", "new-york", "seattle", "austin", "boston"],
    "uk":           ["london", "manchester", "cambridge"],
    "canada":       ["toronto", "vancouver", "montreal"],
    "australia":    ["sydney", "melbourne", "brisbane"],
    "germany":      ["berlin", "munich", "hamburg", "frankfurt", "stuttgart"],
    "japan":        ["tokyo", "osaka", "yokohama", "nagoya", "fukuoka",
                     "kyoto", "sapporo", "kobe", "sendai", "hiroshima"],
    "singapore":    ["singapore", "marina-bay", "one-north", "jurong-east", "tampines"],
    "saudi-arabia": ["riyadh", "jeddah", "dammam", "khobar", "dhahran",
                     "mecca", "medina", "tabuk", "abha", "yanbu"],
    "uae":          ["dubai", "abu-dhabi", "sharjah", "ajman", "ras-al-khaimah",
                     "fujairah", "umm-al-quwain", "al-ain", "khor-fakkan",
                     "dibba-al-fujairah"],
    "qatar":        ["doha", "al-rayyan", "lusail", "al-wakrah", "umm-salal",
                     "al-khor", "al-daayen", "mesaieed", "dukhan",
                     "madinat-ash-shamal"],
}

# Country hub landing pages
hubs_mapping = {
    "usa":          "hire-developers-usa.html",
    "uk":           "hire-developers-uk.html",
    "canada":       "hire-developers-canada.html",
    "australia":    "hire-developers-australia.html",
    "germany":      "hire-developers-germany.html",
    "japan":        "hire-developers-japan.html",
    "singapore":    "hire-developers-singapore.html",
    "saudi-arabia": "hire-developers-saudi-arabia.html",
    "middle-east":  "hire-developers-middle-east.html",
}

# ── XML builders ──────────────────────────────────────────────────────────────
URLSET_OPEN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
    '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9'
    ' http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n'
)
URLSET_CLOSE = '</urlset>\n'

INDEX_OPEN = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
)
INDEX_CLOSE = '</sitemapindex>\n'

def url_entry(path, changefreq, priority):
    loc = BASE_URL + "/" + path if path else BASE_URL + "/"
    return (
        "  <url>\n"
        f"    <loc>{loc}</loc>\n"
        f"    <lastmod>{now_iso}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        "  </url>\n"
    )

def sitemap_entry(filename):
    return (
        "  <sitemap>\n"
        f"    <loc>{BASE_URL}/{filename}</loc>\n"
        f"    <lastmod>{now_iso}</lastmod>\n"
        "  </sitemap>\n"
    )

def write_urlset(filename, url_entries):
    content = URLSET_OPEN + "".join(url_entries) + URLSET_CLOSE
    with open(os.path.join(directory, filename), "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"  ✅ {filename}  ({len(url_entries)} URLs)")
    return filename

# ── Bucket all files ──────────────────────────────────────────────────────────
processed = set()

# --- MAIN sitemap ---
main_entries = []
for page, priority in main_pages.items():
    if page in html_files:
        loc = "" if page == "index.html" else page
        main_entries.append(url_entry(loc, "weekly", priority))
        processed.add(page)
# LLM knowledge files go in main too
main_entries.append(url_entry("llm.txt",      "monthly", "0.70"))
main_entries.append(url_entry("full-llm.txt", "monthly", "0.70"))

# --- COUNTRY sitemaps ---
country_entries = {k: [] for k in list(country_slugs.keys()) + ["middle-east"]}

# Hub pages
for country, hub_file in hubs_mapping.items():
    if hub_file in html_files and hub_file not in processed:
        country_entries[country].append(url_entry(hub_file, "weekly", "0.90"))
        processed.add(hub_file)

# City pages
for country, slugs in country_slugs.items():
    for slug in slugs:
        for f in sorted(html_files):
            if f.endswith(f"-{slug}.html") and f not in processed:
                country_entries[country].append(url_entry(f, "weekly", "0.85"))
                processed.add(f)

# Anything left → main
for f in sorted(html_files):
    if f not in processed:
        main_entries.append(url_entry(f, "weekly", "0.80"))
        processed.add(f)

# ── Write sub-sitemaps ────────────────────────────────────────────────────────
print("\n📄  Generating sub-sitemaps …")
generated = []
generated.append(write_urlset("sitemap-main.xml", main_entries))

for country, entries in country_entries.items():
    if entries:
        generated.append(write_urlset(f"sitemap-{country}.xml", entries))

# ── Write Sitemap Index ───────────────────────────────────────────────────────
print("\n📑  Generating sitemap.xml (Sitemap Index) …")
index_entries = [sitemap_entry(f) for f in generated]
index_content = INDEX_OPEN + "".join(index_entries) + INDEX_CLOSE

with open(os.path.join(directory, "sitemap.xml"), "w", encoding="utf-8") as fh:
    fh.write(index_content)

total_urls = sum(len(e) for e in [main_entries] + list(country_entries.values()))
print(f"\n✅  sitemap.xml → Sitemap Index pointing to {len(generated)} sub-sitemaps")
print(f"    Total URLs across all sitemaps: {total_urls}")
print(f"    lastmod format: ISO 8601 with UTC ({now_iso})")
print()
print("📋  Submit each of these individually to Google Search Console:")
for g in generated:
    print(f"    https://mrdasdeveloper.github.io/{g}")
