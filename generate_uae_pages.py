import os
import re

base_file = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/hire-full-stack-developer-dubai.html"
with open(base_file, "r") as f:
    template = f.read()

# First, let's generalize the template to replace Dubai specific stuff with placeholders.
template = template.replace("Dubai &amp; UAE", "{City} &amp; UAE")
template = template.replace("Dubai & UAE", "{City} & UAE")
template = template.replace("in Dubai", "in {City}")
template = template.replace("Dubai startups", "{City} businesses")
template = template.replace("Dubai (DIFC, Internet City)", "{City}")
template = template.replace("DIFC, Internet City, and DMCC", "{Ecosystem}")
template = template.replace("Dubai Agency", "{PricingMarket}")
template = template.replace("hire-full-stack-developer-dubai.html", "hire-full-stack-developer-{Slug}.html")
template = template.replace("Dubai Focus", "{City} Focus")
template = template.replace("Dubai / UAE Focus", "{City} / UAE Focus")
template = template.replace("Dubai UAE", "{City} UAE")
template = template.replace("from Dubai", "from {City}")
template = template.replace("Hire Developer Dubai", "Hire Developer {City}")
template = template.replace("Backend Developer Dubai", "Backend Developer {City}")
template = template.replace("Next.js Developer Dubai", "Next.js Developer {City}")
template = template.replace("Node.js Developer Dubai", "Node.js Developer {City}")
template = template.replace("AI Developer Dubai", "AI Developer {City}")
template = template.replace("SaaS & AI Platform Development", "{FocusTitle}")
template = template.replace(
    "End-to-end SaaS platforms integrated with LLMs, user management, Stripe/PayFort billing, multi-tenancy dashboards, and scalable microservices architecture built with Next.js + FastAPI.",
    "{FocusDesc}"
)
template = template.replace("Dubai, United Arab Emirates", "{City}, United Arab Emirates")
template = template.replace("startups and enterprises", "{HeroDesc}")

# Some cleanup for things that might have been double-replaced
template = template.replace("{City} Focus", "{City}")

cities = [
    {
        "name": "Dubai",
        "slug": "dubai",
        "ecosystem": "DIFC, Internet City, and DMCC",
        "focus_title": "SaaS & AI Platform Development",
        "focus_desc": "End-to-end SaaS platforms integrated with LLMs, user management, Stripe/PayFort billing, multi-tenancy dashboards, and scalable microservices architecture built with Next.js + FastAPI.",
        "hero_desc": "startups, fintech, SaaS, and AI companies",
        "pricing_market": "Dubai Agency"
    },
    {
        "name": "Abu Dhabi",
        "slug": "abu-dhabi",
        "ecosystem": "Abu Dhabi Global Market (ADGM), Hub71, and government sectors",
        "focus_title": "Enterprise & Government AI Systems",
        "focus_desc": "Highly secure, scalable backend architectures and AI integrations tailored for government technology projects and enterprise-level hiring.",
        "hero_desc": "government tech projects, enterprises, and AI innovators",
        "pricing_market": "Abu Dhabi Agency"
    },
    {
        "name": "Sharjah",
        "slug": "sharjah",
        "ecosystem": "SRTI Park and the expanding software market",
        "focus_title": "Startup & EdTech Platform Development",
        "focus_desc": "Custom software solutions and scalable platforms designed to support Sharjah's growing startup ecosystem and educational sectors.",
        "hero_desc": "growing startups, educational platforms, and the local software market",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Ajman",
        "slug": "ajman",
        "ecosystem": "Ajman Free Zone and emerging business districts",
        "focus_title": "Business Automation Solutions",
        "focus_desc": "Digital transformation tools and custom web applications aimed at modernizing local software companies and the growing business sector.",
        "hero_desc": "local software companies and the expanding business sector",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Ras Al Khaimah",
        "slug": "ras-al-khaimah",
        "ecosystem": "RAKEZ, tourism hubs, and manufacturing centers",
        "focus_title": "Tourism Tech & Industrial IT",
        "focus_desc": "Robust digital platforms and integrations built for increasing technology investments in tourism tech and manufacturing logistics.",
        "hero_desc": "tourism, manufacturing, and increasing technology investments",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Fujairah",
        "slug": "fujairah",
        "ecosystem": "Fujairah Creative City and marine logistics centers",
        "focus_title": "Logistics & Digital Transformation",
        "focus_desc": "Specialized tracking software and backend APIs built to power digital transformation projects within the logistics and port operations sector.",
        "hero_desc": "logistics operations and comprehensive digital transformation projects",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Umm Al Quwain",
        "slug": "umm-al-quwain",
        "ecosystem": "UAQ Free Trade Zone and local retail markets",
        "focus_title": "Local Business Digital Presence",
        "focus_desc": "High-performance websites, e-commerce solutions, and digital automation tools helping smaller markets achieve broad location-based SEO coverage.",
        "hero_desc": "local businesses seeking powerful digital transformation and SEO coverage",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Al Ain",
        "slug": "al-ain",
        "ecosystem": "Al Ain's healthcare, education, and government IT hubs",
        "focus_title": "Healthcare & Education IT Architecture",
        "focus_desc": "HIPAA-compliant data handling, educational portals, and scalable backends catering to the massive IT demand in education and healthcare.",
        "hero_desc": "education, healthcare, and high-demand government IT projects",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Khor Fakkan",
        "slug": "khor-fakkan",
        "ecosystem": "Khor Fakkan Port and regional logistics channels",
        "focus_title": "Port & Logistics Tech Solutions",
        "focus_desc": "Custom inventory, shipping, and supply chain management systems utilizing modern microservices for reliable port logistics.",
        "hero_desc": "port operations, logistics scheduling, and regional business technologies",
        "pricing_market": "UAE Agency"
    },
    {
        "name": "Dibba Al-Fujairah",
        "slug": "dibba-al-fujairah",
        "ecosystem": "local manufacturing and trade operations",
        "focus_title": "Trading & Retail Automation Systems",
        "focus_desc": "Streamlined backend solutions tailored for local commerce, capturing long-tail local searches and digital market presence.",
        "hero_desc": "local trading, manufacturing, and long-tail technological growth sectors",
        "pricing_market": "UAE Agency"
    }
]

output_dir = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev

urls = []

for city in cities:
    content = template
    content = content.replace("{City}", city["name"])
    content = content.replace("{Slug}", city["slug"])
    content = content.replace("{Ecosystem}", city["ecosystem"])
    content = content.replace("{FocusTitle}", city["focus_title"])
    content = content.replace("{FocusDesc}", city["focus_desc"])
    content = content.replace("{HeroDesc}", city["hero_desc"])
    content = content.replace("{PricingMarket}", city["pricing_market"])
    
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
