import os
from datetime import datetime

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f not in ('google9bae3598255dbb1e.html', 'pinterest-6f253.html')]

today = datetime.now().strftime("%Y-%m-%d")

# Define groupings
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

# Add hub pages to their respective country
hubs_mapping = {
    "usa": "hire-developers-usa.html",
    "uk": "hire-developers-uk.html",
    "canada": "hire-developers-canada.html",
    "australia": "hire-developers-australia.html",
    "germany": "hire-developers-germany.html",
    "japan": "hire-developers-japan.html",
    "singapore": "hire-developers-singapore.html",
    "saudi-arabia": "hire-developers-saudi-arabia.html",
    "middle-east": "hire-developers-middle-east.html" # We'll put this in main or UAE/Qatar
}

# Initialize data structures for each sitemap
sitemaps_data = {
    "main": [],
    "usa": [],
    "uk": [],
    "canada": [],
    "australia": [],
    "germany": [],
    "japan": [],
    "singapore": [],
    "saudi-arabia": [],
    "uae": [],
    "qatar": [],
    "middle-east": []
}

def generate_url_xml(loc, lastmod, changefreq, priority):
    return f"""  <url>
    <loc>https://mrdasdeveloper.github.io/{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""

# 1. Main Pages
for page, priority in main_pages.items():
    if page in html_files:
        path = "" if page == "index.html" else page
        sitemaps_data["main"].append(generate_url_xml(path, today, "weekly", priority))
        html_files.remove(page)

# 2. Text files to main
sitemaps_data["main"].append(generate_url_xml("llm.txt", today, "monthly", "0.70"))
sitemaps_data["main"].append(generate_url_xml("full-llm.txt", today, "monthly", "0.70"))

# 3. Process the remaining html files
for f in sorted(html_files):
    assigned = False
    
    # Check if it's a hub page
    if f.startswith('hire-developers-'):
        country = f.replace('hire-developers-', '').replace('.html', '')
        if country in sitemaps_data:
            sitemaps_data[country].append(generate_url_xml(f, today, "weekly", "0.90"))
            assigned = True
    
    # Check if it's a city page
    if not assigned:
        for country, slugs in country_slugs.items():
            for slug in slugs:
                if f.endswith(f"-{slug}.html"):
                    sitemaps_data[country].append(generate_url_xml(f, today, "weekly", "0.85"))
                    assigned = True
                    break
            if assigned:
                break
                
    # If not assigned to any specific country, put in main
    if not assigned:
        sitemaps_data["main"].append(generate_url_xml(f, today, "weekly", "0.80"))

# 4. Generate the XML files
urlset_header = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
          http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
'''
urlset_footer = '\n</urlset>'

generated_sitemaps = []

for sitemap_name, urls in sitemaps_data.items():
    if not urls:
        continue
    
    filename = f"sitemap-{sitemap_name}.xml"
    content = urlset_header + "\n".join(urls) + urlset_footer
    
    with open(os.path.join(directory, filename), "w") as f:
        f.write(content)
        
    generated_sitemaps.append(filename)
    print(f"Generated {filename} with {len(urls)} entries.")

# 5. Generate the Sitemap Index
sitemapindex_header = '''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
sitemapindex_footer = '\n</sitemapindex>'

index_urls = []
for s in generated_sitemaps:
    index_urls.append(f"""  <sitemap>
    <loc>https://mrdasdeveloper.github.io/{s}</loc>
    <lastmod>{today}</lastmod>
  </sitemap>""")

sitemap_index_content = sitemapindex_header + "\n".join(index_urls) + sitemapindex_footer

with open(os.path.join(directory, "sitemap.xml"), "w") as f:
    f.write(sitemap_index_content)
    
print(f"Generated Sitemap Index (sitemap.xml) pointing to {len(generated_sitemaps)} sub-sitemaps.")
