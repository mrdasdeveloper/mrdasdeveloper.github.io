import os

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/mrdasdeveloper.github.io/"
html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f not in ('google9bae3598255dbb1e.html', 'pinterest-6f253.html', 'sitemap.html')]

main_pages = {
    'index.html': 'Home - Main Portfolio',
    'hire-ai-full-stack-engineer.html': 'Hire AI Full-Stack Engineer',
    'hire-full-stack-developer.html': 'Hire Full-Stack Developer',
    'hire-backend-engineer.html': 'Hire Backend Engineer',
    'agentic-ai-developer.html': 'Agentic AI Developer',
    'full-stack-ai-engineer.html': 'Full-Stack AI Engineer',
    'ai-backend-architecture-microservices-engineering-guide.html': 'AI Backend Architecture Guide',
    'business-automation.html': 'Business Automation Services',
    'freelancer.html': 'Freelance Engineering Services',
    'presentation.html': 'Executive Presentation',
}

country_slugs = {
    "United States": ["san-francisco", "new-york", "seattle", "austin", "boston"],
    "United Kingdom": ["london", "manchester", "cambridge"],
    "Canada": ["toronto", "vancouver", "montreal"],
    "Australia": ["sydney", "melbourne", "brisbane"],
    "Germany": ["berlin", "munich", "hamburg", "frankfurt", "stuttgart"],
    "Japan": ["tokyo", "osaka", "yokohama", "nagoya", "fukuoka", "kyoto", "sapporo", "kobe", "sendai", "hiroshima"],
    "Singapore": ["singapore", "marina-bay", "one-north", "jurong-east", "tampines"],
    "Saudi Arabia": ["riyadh", "jeddah", "dammam", "khobar", "dhahran", "mecca", "medina", "tabuk", "abha", "yanbu"],
    "UAE": ["dubai", "abu-dhabi", "sharjah", "ajman", "ras-al-khaimah", "fujairah", "umm-al-quwain", "al-ain", "khor-fakkan", "dibba-al-fujairah"],
    "Qatar": ["doha", "al-rayyan", "lusail", "al-wakrah", "umm-salal", "al-khor", "al-daayen", "mesaieed", "dukhan", "madinat-ash-shamal"]
}

hubs_mapping = {
    "United States": "hire-developers-usa.html",
    "United Kingdom": "hire-developers-uk.html",
    "Canada": "hire-developers-canada.html",
    "Australia": "hire-developers-australia.html",
    "Germany": "hire-developers-germany.html",
    "Japan": "hire-developers-japan.html",
    "Singapore": "hire-developers-singapore.html",
    "Saudi Arabia": "hire-developers-saudi-arabia.html",
    "Middle East": "hire-developers-middle-east.html"
}

country_flags = {
    "United States": "🇺🇸",
    "United Kingdom": "🇬🇧",
    "Canada": "🇨🇦",
    "Australia": "🇦🇺",
    "Germany": "🇩🇪",
    "Japan": "🇯🇵",
    "Singapore": "🇸🇬",
    "Saudi Arabia": "🇸🇦",
    "UAE": "🇦🇪",
    "Qatar": "🇶🇦",
    "Middle East": "🌍"
}

icons = {
    "ai": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="sitemap-icon ai"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>',
    "dev": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="sitemap-icon dev"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
    "hub": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="sitemap-icon hub"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    "core": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="sitemap-icon core"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
}

def get_role_info(filename, slug):
    name = filename.replace('.html', '')
    city_str = slug.replace('-', ' ').title()
    
    # We will strip the city name out for a clean hierarchy
    if name.startswith('hire-full-stack-developer-'):
        return f"Full-Stack Developer", "dev"
    elif name.startswith('hire-agentic-ai-engineer-'):
        return f"Agentic AI Engineer", "ai"
    elif name.startswith('hire-ai-full-stack-engineer-'):
        return f"AI Full-Stack Engineer", "ai"
    elif name.startswith('hire-backend-engineer-'):
        return f"Backend Engineer", "dev"
    elif name.startswith('hire-fastapi-developer-'):
        return f"FastAPI Developer", "dev"
    elif name.startswith('hire-llm-engineer-'):
        return f"LLM Engineer", "ai"
    elif name.startswith('hire-rag-developer-'):
        return f"RAG Developer", "ai"
    elif name.startswith('hire-backend-architect-'):
        return f"Backend Architect", "dev"
    return name.replace('-', ' ').title(), "core"

# Read the base template
with open(os.path.join(directory, "hire-full-stack-developer.html"), "r") as f:
    template = f.read()

# Extract header and footer
header = template.split('<section class="hero"')[0]
footer = '<!-- ── Global Tech Hiring Hubs ── -->' + template.split('<!-- ── Global Tech Hiring Hubs ── -->')[1]

header = header.replace("<title>Hire Ramesh Kumar Das — Senior Full-Stack Developer | React, Next.js, Node.js, FastAPI</title>", "<title>Site Directory & Premium Sitemap — Ramesh Kumar Das</title>")
header = header.replace('<meta name="description" content="Hire Ramesh Kumar Das, Senior Full-Stack Developer with 6.5+ years. Expert in React.js, Next.js, Node.js, FastAPI, PostgreSQL. Building scalable SaaS, APIs & web apps. Available for remote work." />', '<meta name="description" content="Explore the comprehensive directory of global tech hiring hubs, city-specific developer profiles, and core AI and full-stack services for Ramesh Kumar Das." />')

custom_css = """
<style>
/* Reset and Base Overrides */
.sm-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
}

/* Premium Hero Search Area */
.sm-hero {
    position: relative;
    padding: 80px 0 60px;
    text-align: center;
    background: radial-gradient(circle at 50% -20%, rgba(124,111,247,0.15) 0%, transparent 60%);
    margin-bottom: 20px;
}

.sm-title {
    font-size: clamp(36px, 6vw, 56px);
    font-weight: 800;
    letter-spacing: -0.03em;
    color: var(--text);
    margin-bottom: 16px;
}

.sm-subtitle {
    font-size: 17px;
    color: var(--muted);
    max-width: 600px;
    margin: 0 auto 40px;
    line-height: 1.6;
}

.sm-search-container {
    position: relative;
    max-width: 640px;
    margin: 0 auto;
    z-index: 10;
}

.sm-search-icon {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--accent);
    width: 22px;
    height: 22px;
    pointer-events: none;
}

.sm-search-input {
    width: 100%;
    padding: 20px 24px 20px 56px;
    font-size: 16px;
    font-family: 'Inter', sans-serif;
    color: var(--text);
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 16px;
    outline: none;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.08);
}

.sm-search-input:focus {
    border-color: var(--accent);
    background: var(--surface);
    box-shadow: 0 0 0 4px var(--accent-bg), 0 12px 40px rgba(0,0,0,0.12);
}

.sm-search-input::placeholder {
    color: var(--dim);
}

/* Category Headers */
.sm-category-title {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 24px;
    font-weight: 700;
    color: var(--text);
    margin: 60px 0 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border);
}
.sm-category-icon {
    width: 28px;
    height: 28px;
    color: var(--accent);
    padding: 6px;
    background: var(--accent-bg);
    border-radius: 8px;
}

/* Grid Layouts */
.sm-grid-hubs {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
}

/* Glassmorphic Cards */
.sm-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    margin-bottom: 32px;
}

.sm-card:hover {
    border-color: var(--border2);
    box-shadow: 0 12px 40px rgba(0,0,0,0.08);
}

/* Hub specific styling */
.sm-hub-link {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text);
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
}
.sm-hub-link:hover {
    background: var(--surface2);
    border-color: var(--accent-bd);
    color: var(--accent-hi);
    transform: translateY(-2px);
}
.sm-hub-link svg {
    color: var(--accent);
    width: 20px;
    height: 20px;
}

/* Country Card Details */
.sm-country-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px dashed var(--border);
}

.sm-country-flag {
    font-size: 24px;
    line-height: 1;
}

.sm-country-name {
    font-size: 20px;
    font-weight: 800;
    color: var(--text);
}

/* City Inner Grid */
.sm-city-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 32px 24px;
}

.sm-city-group {
    display: flex;
    flex-direction: column;
}

.sm-city-title {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 15px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}
.sm-city-title::before {
    content: "📍";
    font-size: 14px;
}

/* Links List */
.sm-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.sm-item a {
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--muted);
    font-size: 13.5px;
    font-weight: 500;
    text-decoration: none;
    padding: 6px 8px;
    border-radius: 8px;
    transition: all 0.2s ease;
    margin: -4px -8px;
}

.sitemap-icon {
    width: 15px;
    height: 15px;
    flex-shrink: 0;
    transition: all 0.2s ease;
}
.sitemap-icon.ai { color: #f5c842; } /* Sparkle gold for AI */
.sitemap-icon.dev { color: var(--green); } /* Green for Code */
.sitemap-icon.core { color: var(--accent); } /* Purple for Core */

.sm-item a:hover {
    color: var(--text);
    background: var(--surface2);
}

.sm-item a:hover .sitemap-icon {
    transform: scale(1.15) rotate(5deg);
}

/* No Results State */
.sm-no-results {
    display: none;
    text-align: center;
    padding: 60px 20px;
    background: var(--surface);
    border: 1px dashed var(--border2);
    border-radius: 16px;
    margin-top: 40px;
    animation: fadeIn 0.3s ease;
}

.sm-no-results svg {
    width: 48px;
    height: 48px;
    color: var(--dim);
    margin-bottom: 16px;
}

.sm-no-results h3 {
    font-size: 20px;
    color: var(--text);
    margin-bottom: 8px;
}

.sm-no-results p {
    color: var(--muted);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Smooth filtering transition */
.filter-item {
    transition: opacity 0.3s ease, transform 0.3s ease;
}
.filter-hidden {
    opacity: 0 !important;
    transform: scale(0.95) !important;
    position: absolute !important;
    visibility: hidden !important;
    pointer-events: none !important;
}
.city-hidden {
    display: none !important;
}
</style>
"""

header = header.replace('</head>', custom_css + '\n</head>')

body = """
<main class="sm-main">
  <!-- Premium Hero -->
  <section class="sm-hero">
    <div class="sm-container">
      <h1 class="sm-title">Global Directory</h1>
      <p class="sm-subtitle">Instantly navigate through 500+ premium tech hubs, city-specific developer portfolios, and core enterprise AI services.</p>
      
      <div class="sm-search-container">
        <svg class="sm-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="smSearch" class="sm-search-input" placeholder="Search by city, role, or country (e.g. 'Dubai', 'AI Engineer')..." autocomplete="off" spellcheck="false" />
      </div>
    </div>
  </section>

  <section class="sm-content" style="padding-bottom: 100px;">
    <div class="sm-container">
      
      <div id="smNoResults" class="sm-no-results">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <h3>No matching profiles found</h3>
        <p>Try searching for a different city or role.</p>
      </div>

      <div id="smGridContainer">
        
        <!-- Core Services -->
        <div class="sm-section filter-category">
          <div class="sm-category-title">
            <svg class="sm-category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            Core Services
          </div>
          <div class="sm-card">
            <ul class="sm-list sm-grid-hubs" style="gap: 16px 24px;">
"""
for page, title in main_pages.items():
    icon_svg = icons["core"]
    body += f'              <li class="sm-item filter-item"><a href="{page}" data-search="{title.lower()}">{icon_svg}<span>{title}</span></a></li>\n'
body += """            </ul>
          </div>
        </div>

        <!-- Global Hubs -->
        <div class="sm-section filter-category">
          <div class="sm-category-title">
            <svg class="sm-category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            Global Hubs
          </div>
          <div class="sm-grid-hubs">
"""
for country, url in hubs_mapping.items():
    flag = country_flags.get(country, "🌍")
    body += f'            <a href="{url}" class="sm-hub-link filter-item" data-search="{country.lower()} hub"><span style="font-size:18px">{flag}</span> {country} Hub</a>\n'
body += """          </div>
        </div>

        <!-- City Index -->
        <div class="sm-section filter-category">
          <div class="sm-category-title" style="margin-top: 80px;">
            <svg class="sm-category-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            City Directories
          </div>
"""

for country, slugs in country_slugs.items():
    flag = country_flags.get(country, "🌍")
    
    # Check if there are any files for this country
    has_files = False
    for slug in slugs:
        matching = [f for f in html_files if f.endswith(f"-{slug}.html") and not f.startswith("hire-developers-")]
        if matching:
            has_files = True
            break
            
    if not has_files:
        continue
        
    body += f'''
          <div class="sm-card filter-card" data-country="{country.lower()}">
            <div class="sm-country-header">
              <span class="sm-country-flag">{flag}</span>
              <h3 class="sm-country-name">{country}</h3>
            </div>
            <div class="sm-city-grid">
'''
    for slug in slugs:
        matching_files = [f for f in html_files if f.endswith(f"-{slug}.html") and not f.startswith("hire-developers-")]
        if not matching_files:
            continue
            
        city_name = slug.replace('-', ' ').title()
        
        body += f'''              <div class="sm-city-group">
                <h4 class="sm-city-title">{city_name}</h4>
                <ul class="sm-list">
'''
        for mf in matching_files:
            title, role_type = get_role_info(mf, slug)
            icon_svg = icons.get(role_type, icons["core"])
            search_terms = f"{country.lower()} {city_name.lower()} {title.lower()} {mf.lower()}"
            body += f'                  <li class="sm-item filter-item"><a href="{mf}" data-search="{search_terms}">{icon_svg}<span>{title}</span></a></li>\n'
            
        body += '''                </ul>
              </div>
'''
    body += '''            </div>
          </div>
'''

body += """
        </div>

      </div>
    </div>
  </section>
</main>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('smSearch');
    const noResults = document.getElementById('smNoResults');
    const gridContainer = document.getElementById('smGridContainer');
    
    const filterItems = document.querySelectorAll('.filter-item');
    const filterCards = document.querySelectorAll('.filter-card');
    const filterCategories = document.querySelectorAll('.filter-category');
    const cityGroups = document.querySelectorAll('.sm-city-group');

    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase().trim();
        let hasAnyResults = false;

        // 1. Filter Individual Items (Links & Hub Cards)
        filterItems.forEach(item => {
            const el = item.tagName.toLowerCase() === 'a' ? item : item.querySelector('a');
            if (!el) return;
            
            const searchableText = el.getAttribute('data-search') || '';
            const textContent = el.textContent.toLowerCase();
            
            const parentCard = item.closest('.filter-card');
            const countryText = parentCard ? parentCard.getAttribute('data-country') || '' : '';
            
            if (term === '' || searchableText.includes(term) || textContent.includes(term) || countryText.includes(term)) {
                item.classList.remove('filter-hidden');
                item.style.display = '';
                hasAnyResults = true;
            } else {
                item.classList.add('filter-hidden');
                setTimeout(() => { if(item.classList.contains('filter-hidden')) item.style.display = 'none'; }, 300);
            }
        });

        // 2. Hide City Groups if all links inside are hidden
        cityGroups.forEach(group => {
            const items = group.querySelectorAll('.filter-item');
            let hasVisibleItem = false;
            
            items.forEach(i => {
                if (!i.classList.contains('filter-hidden')) hasVisibleItem = true;
            });
            
            const cityName = (group.querySelector('.sm-city-title')?.textContent || '').toLowerCase();
            
            // If the user searches specifically for the city name, show the group and all its items
            if (term !== '' && cityName.includes(term)) {
                hasVisibleItem = true;
                items.forEach(i => {
                    i.classList.remove('filter-hidden');
                    i.style.display = '';
                });
                hasAnyResults = true;
            }
            
            if (hasVisibleItem || term === '') {
                group.classList.remove('city-hidden');
            } else {
                group.classList.add('city-hidden');
            }
        });

        // 3. Filter Cards (Hide card if all city groups inside are hidden)
        filterCards.forEach(card => {
            const groups = card.querySelectorAll('.sm-city-group');
            let hasVisibleGroup = false;
            
            groups.forEach(g => {
                if (!g.classList.contains('city-hidden')) hasVisibleGroup = true;
            });
            
            const countryName = card.getAttribute('data-country') || '';
            
            // If search matches Country directly, show everything
            if (term !== '' && countryName.includes(term)) {
                hasVisibleGroup = true;
                hasAnyResults = true;
                groups.forEach(g => {
                    g.classList.remove('city-hidden');
                    g.querySelectorAll('.filter-item').forEach(i => {
                        i.classList.remove('filter-hidden');
                        i.style.display = '';
                    });
                });
            }
            
            if (hasVisibleGroup || term === '') {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });

        // 4. Hide Empty Categories
        filterCategories.forEach(category => {
            const items = category.querySelectorAll('.filter-item:not(.filter-hidden)');
            const cards = category.querySelectorAll('.filter-card[style=""]');
            
            if (items.length === 0 && cards.length === 0 && term !== '') {
                category.style.display = 'none';
            } else {
                category.style.display = '';
            }
        });

        // 5. Toggle No Results state
        if (hasAnyResults || term === '') {
            noResults.style.display = 'none';
            gridContainer.style.display = 'block';
        } else {
            noResults.style.display = 'block';
            gridContainer.style.display = 'none';
        }
    });
});
</script>
"""

full_html = header + body + footer

with open(os.path.join(directory, "sitemap.html"), "w") as f:
    f.write(full_html)

print("Generated premium sitemap.html with nested City hierarchy and CSS Grid layout")
