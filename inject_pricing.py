#!/usr/bin/env python3
"""
Inject a Pricing / Services section before the SEO Keyword Cloud on each page.
This version implements a "50% exclusive offer" visual with crossed-out market standard prices
and lowered final prices (max $29/hr, $1,999/mo).
Includes the homepage (index.html).
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/9779700864900"

STYLE = """<style>
/* ── Pricing Section ─────────────────────────────────────────── */
.pricing-section{padding:52px 0 40px;border-top:1px solid var(--border,rgba(255,255,255,.08));}
.pricing-section .ps-inner{max-width:1000px;margin:0 auto;padding:0 20px;}
.ps-head{margin-bottom:32px;text-align:center;}
.ps-label{display:inline-block;background:rgba(251,146,60,.15);color:#fb923c;padding:4px 10px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.1em;margin-bottom:12px;border:1px solid rgba(251,146,60,.3);}
.ps-title{font-size:28px;font-weight:800;color:var(--text,#ededf5);letter-spacing:-.02em;margin-bottom:8px;}
.ps-sub{font-size:14px;color:var(--muted,#7a7a8e);max-width:600px;margin:0 auto;}
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-bottom:28px;}
.pc{background:var(--surface,#111115);border:1px solid var(--border,rgba(255,255,255,.08));border-radius:14px;padding:22px 20px;position:relative;transition:border-color .2s,box-shadow .2s;}
.pc:hover{border-color:rgba(124,111,247,.45);box-shadow:0 8px 32px rgba(124,111,247,.1);}
.pc.featured{border-color:rgba(124,111,247,.45);background:linear-gradient(160deg,rgba(124,111,247,.09) 0%,rgba(13,13,24,.95) 100%);transform:scale(1.02);z-index:2;}
.pc-badge{position:absolute;top:-1px;right:16px;background:linear-gradient(90deg,#fb923c,#f97316);color:#fff;font-size:10px;font-weight:800;padding:4px 12px;border-radius:0 0 8px 8px;letter-spacing:.05em;box-shadow:0 4px 12px rgba(249,115,22,.3);}
.pc-type{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.1em;color:var(--muted,#7a7a8e);margin-bottom:4px;}
.pc-market-rate{font-size:14px;font-weight:600;color:var(--muted,#7a7a8e);text-decoration:line-through;opacity:0.7;margin-bottom:2px;}
.pc-rate{font-size:36px;font-weight:800;color:var(--text,#ededf5);letter-spacing:-.03em;line-height:1;}
.pc-rate span{font-size:14px;font-weight:600;color:#25d366;letter-spacing:0;background:rgba(37,211,102,.1);padding:2px 6px;border-radius:6px;vertical-align:middle;margin-left:6px;}
.pc-period{font-size:12px;color:var(--muted,#7a7a8e);margin:8px 0 14px;}
.pc-divider{border:none;border-top:1px solid var(--border,rgba(255,255,255,.08));margin:14px 0;}
.pc-features{list-style:none;padding:0;margin:0 0 18px;display:flex;flex-direction:column;gap:8px;}
.pc-features li{font-size:13px;color:var(--text,#d4d4e8);display:flex;align-items:flex-start;gap:8px;line-height:1.4;}
.pc-features li::before{content:"✓";color:#25d366;font-weight:800;flex-shrink:0;margin-top:1px;}
.pc-cta{display:inline-flex;align-items:center;justify-content:center;gap:6px;width:100%;padding:12px 16px;border-radius:8px;font-size:13px;font-weight:700;background:var(--surface2,#18181f);border:1px solid var(--border2,rgba(255,255,255,.12));color:var(--text,#ededf5);text-decoration:none;transition:all .2s;}
.pc-cta:hover{background:rgba(124,111,247,.18);border-color:rgba(124,111,247,.5);color:#fff;transform:translateY(-2px);}
.pc.featured .pc-cta{background:linear-gradient(135deg,#7c6ff7,#9d93ff);border-color:transparent;color:#fff;box-shadow:0 6px 20px rgba(124,111,247,.3);}
.pc.featured .pc-cta:hover{background:linear-gradient(135deg,#6a5fe0,#8a7fe8);box-shadow:0 8px 24px rgba(124,111,247,.4);}
.ps-note{font-size:13px;color:var(--dim,#4a4a5a);text-align:center;padding:16px;background:var(--surface,#111115);border:1px solid rgba(251,146,60,.2);border-radius:10px;max-width:700px;margin:0 auto;}
.ps-note strong{color:#fb923c;}
@media(prefers-color-scheme:light){
  .pc{background:#fff;border-color:#d0d7de;}
  .pc.featured{background:linear-gradient(160deg,#f3eeff 0%,#fff 100%);border-color:#d2b4fe;}
  .pc:hover{border-color:#9d93ff;box-shadow:0 8px 32px rgba(110,64,201,.1);}
  .ps-title{color:#1f2328;} .ps-sub{color:#656d76;}
  .pc-rate{color:#1f2328;}
  .pc-period{color:#656d76;} .pc-features li{color:#24292f;}
  .pc-cta{background:#f6f8fa;border-color:#d0d7de;color:#1f2328;}
  .pc-cta:hover{background:#ede8ff;border-color:#9d93ff;color:#6e40c9;}
  .pc.featured .pc-cta{background:linear-gradient(135deg,#6e40c9,#9d93ff);color:#fff;}
  .ps-note{background:#fff1e5;border-color:#ffa657;color:#bc4c00;}
  .ps-note strong{color:#bc4c00;}
}
@media(max-width:768px){
  .pc.featured{transform:none;z-index:1;}
}
@media(max-width:600px){
  .pricing-grid{grid-template-columns:1fr;}
  .pc-rate{font-size:32px;}
  .ps-title{font-size:22px;}
}
</style>"""

def wa_link(msg):
    import urllib.parse
    return WA + "?text=" + urllib.parse.quote(msg)

def pricing_section(label, title, subtitle, plans, note):
    cards = ""
    for p in plans:
        featured = p.get("featured", False)
        badge = f'<span class="pc-badge">{p["badge"]}</span>' if p.get("badge") else ""
        feats = "".join(f"<li>{f}</li>" for f in p["features"])
        cta_href = wa_link(p["cta_msg"])
        market_rate = f'<div class="pc-market-rate">Market Standard: {p["market_rate"]}</div>' if p.get("market_rate") else ""
        
        cards += f"""
      <div class="pc{'  featured' if featured else ''}">
        {badge}
        <div class="pc-type">{p["type"]}</div>
        {market_rate}
        <div class="pc-rate">{p["rate"]}<span>{p["rate_unit"]}</span></div>
        <div class="pc-period">{p["period"]}</div>
        <hr class="pc-divider">
        <ul class="pc-features">{feats}</ul>
        <a class="pc-cta" href="{cta_href}" target="_blank" rel="noopener">
          🚀 {p["cta_label"]}
        </a>
      </div>"""

    return f"""
    <!-- ── Pricing & Services ── -->
    <section class="pricing-section" aria-label="Pricing and services">
      <div class="ps-inner">
        <div class="ps-head">
          <span class="ps-label">{label}</span>
          <h2 class="ps-title">{title}</h2>
          <p class="ps-sub">{subtitle}</p>
        </div>
        <div class="pricing-grid">
          {cards}
        </div>
        <p class="ps-note">{note}</p>
      </div>
    </section>
{STYLE}
"""

common_note = "💡 <strong>Exclusive Direct Offer:</strong> Skip the agency fees. By hiring me directly, you get top-tier US/EU engineering quality at a fraction of the market cost. Prices reflect my current 50% discount for direct client engagements."

# ── Page-specific pricing data ────────────────────────────────────
PAGES = {

"hire-ai-full-stack-engineer.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Enterprise AI Engineering. Startup Pricing.",
    "Get production-grade LLM, RAG, and agentic AI systems at unmatched value. Limited time direct-hire pricing.",
    [
        {
            "type": "Hourly Consulting",
            "market_rate": "$60 - $80",
            "rate": "$29", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "LLM integration & RAG pipeline setup",
                "Architecture & code review",
                "Prompt engineering & optimization",
                "Min. 4 hours per session",
                "Async or video call support",
            ],
            "cta_label": "Book Hourly Session",
            "cta_msg": "Hi Ramesh, I'd like to book an hourly AI engineering session at the $29/hr promotional rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,000+",
            "rate": "$1,999", "rate_unit": "Best Value",
            "period": "Full-time equivalent · 160 hrs/mo",
            "badge": "Most Popular",
            "featured": True,
            "features": [
                "Dedicated LangChain / CrewAI dev",
                "RAG pipeline + vector DB architecture",
                "End-to-end multi-agent systems",
                "LLMOps, deployment & fine-tuning",
                "Daily standups & priority access",
                "Direct Slack / WhatsApp communication",
            ],
            "cta_label": "Secure Monthly Rate",
            "cta_msg": "Hi Ramesh, I want to secure the $1,999 monthly AI engineering retainer. Can we schedule a call?",
        },
        {
            "type": "Fixed-Price MVP",
            "market_rate": "$3,000+",
            "rate": "From $1,499", "rate_unit": "Fixed",
            "period": "Milestone-based · Clear deliverables",
            "features": [
                "Complete AI product MVP (4–6 weeks)",
                "Custom RAG chatbot deployment",
                "Secure LLM API integrations",
                "Clear scope defined upfront",
                "Invoice at completed milestones",
            ],
            "cta_label": "Get Custom Quote",
            "cta_msg": "Hi Ramesh, I have a fixed-price AI project. Can you share a quote with the discounted pricing?",
        },
    ],
    common_note
),

"hire-full-stack-developer.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Elite Full-Stack Quality. Accessible Pricing.",
    "React, Next.js, Node.js, FastAPI — end-to-end web development with transparent, unbeatable rates.",
    [
        {
            "type": "Hourly Rate",
            "market_rate": "$50 - $70",
            "rate": "$25", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "Frontend (React/Next.js) dev",
                "Backend API development",
                "Bug fixes & performance boosts",
                "Min. 4 hours per session",
                "Code review & refactoring",
            ],
            "cta_label": "Book Hourly Session",
            "cta_msg": "Hi Ramesh, I want to book hourly full-stack development time at the $25/hr promotional rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$3,500+",
            "rate": "$1,899", "rate_unit": "Best Value",
            "period": "Full-time equivalent · 160 hrs/mo",
            "badge": "Top Choice",
            "featured": True,
            "features": [
                "Dedicated Next.js + FastAPI dev",
                "Full UI/UX component library build",
                "REST API & Database architecture",
                "CI/CD setup & cloud deployment",
                "Daily standups, Slack comms",
                "Zero agency overhead fees",
            ],
            "cta_label": "Secure Retainer Rate",
            "cta_msg": "Hi Ramesh, I want to discuss a monthly full-stack development retainer at $1,899/mo.",
        },
        {
            "type": "SaaS MVP Build",
            "market_rate": "$4,000+",
            "rate": "From $1,800", "rate_unit": "Fixed",
            "period": "Fixed-price · 4–8 weeks delivery",
            "features": [
                "Complete SaaS platform MVP",
                "Auth, Stripe payments, dashboard",
                "Scalable API + DB architecture",
                "Production deployment (Vercel/AWS)",
                "Full IP ownership handover",
            ],
            "cta_label": "Get MVP Quote",
            "cta_msg": "Hi Ramesh, I need a SaaS MVP built. Can you provide a quote with your direct pricing?",
        },
    ],
    common_note
),

"hire-backend-engineer.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Scalable Backend Architecture. Startup Rates.",
    "FastAPI, microservices, PostgreSQL, Redis — robust infrastructure at a fraction of standard cost.",
    [
        {
            "type": "Hourly Rate",
            "market_rate": "$60 - $80",
            "rate": "$29", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "FastAPI / Python backend coding",
                "Database schema & optimization",
                "Microservice architecture review",
                "Performance bottleneck fixes",
                "Min. 4 hours per session",
            ],
            "cta_label": "Book Hourly Session",
            "cta_msg": "Hi Ramesh, I want to book hourly backend engineering time at the $29/hr promotional rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,000+",
            "rate": "$1,999", "rate_unit": "Best Value",
            "period": "Full-time equivalent · 160 hrs/mo",
            "badge": "Most Popular",
            "featured": True,
            "features": [
                "Dedicated FastAPI microservices dev",
                "PostgreSQL + Redis architecture",
                "Docker + K8s cloud deployment",
                "CI/CD pipeline automation",
                "API gateway & security (OAuth/JWT)",
                "Observability (Prometheus/Grafana)",
            ],
            "cta_label": "Secure Monthly Rate",
            "cta_msg": "Hi Ramesh, I want to discuss a monthly backend engineering retainer at $1,999/mo.",
        },
        {
            "type": "Architecture Audit",
            "market_rate": "$1,200",
            "rate": "$599", "rate_unit": "One-Time",
            "period": "Flat fee · 3–5 business days",
            "features": [
                "Comprehensive API & DB audit",
                "Scalability & security review",
                "Query performance report",
                "Actionable recommendations doc",
                "1-hour follow-up strategy call",
            ],
            "cta_label": "Request Audit",
            "cta_msg": "Hi Ramesh, I'd like a backend architecture audit at the $599 promotional rate.",
        },
    ],
    common_note
),

"agentic-ai-developer.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Advanced Agentic AI. Unbeatable Value.",
    "LangGraph, CrewAI, multi-agent workflows — get cutting-edge autonomous AI for your business.",
    [
        {
            "type": "Hourly Consulting",
            "market_rate": "$70 - $90",
            "rate": "$29", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "Agent architecture design",
                "LangGraph / CrewAI implementation",
                "Custom tool & memory integration",
                "Debugging complex workflows",
                "Min. 4 hours per session",
            ],
            "cta_label": "Book Hourly Session",
            "cta_msg": "Hi Ramesh, I want to book an hourly agentic AI session at the $29/hr promotional rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,500+",
            "rate": "$1,999", "rate_unit": "Best Value",
            "period": "Full-time equivalent · 160 hrs/mo",
            "badge": "Startups Choice",
            "featured": True,
            "features": [
                "Dedicated multi-agent system dev",
                "Complex LangGraph / CrewAI workflows",
                "Enterprise RAG + Vector DB setups",
                "Custom fine-tuning & LLMOps",
                "Priority daily communications",
                "Zero agency markup fees",
            ],
            "cta_label": "Secure Monthly Rate",
            "cta_msg": "Hi Ramesh, I want a monthly agentic AI development retainer at the $1,999/mo rate.",
        },
        {
            "type": "Agent MVP Build",
            "market_rate": "$3,500+",
            "rate": "From $1,999", "rate_unit": "Fixed",
            "period": "Fixed-price · 4–6 weeks",
            "features": [
                "Custom autonomous AI agent MVP",
                "Multi-step reasoning & tool use",
                "External API integrations",
                "Cloud deployment & monitoring",
                "Full source code handover",
            ],
            "cta_label": "Get Agent Quote",
            "cta_msg": "Hi Ramesh, I need a custom AI agent built. Can you share a quote with direct pricing?",
        },
    ],
    common_note
),

"full-stack-ai-engineer.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Full-Stack AI Solutions. Startup Pricing.",
    "End-to-end AI-integrated web apps (React, FastAPI, LLMs) at a fraction of market cost.",
    [
        {
            "type": "Hourly Rate",
            "market_rate": "$60 - $80",
            "rate": "$29", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "AI web app development",
                "React + FastAPI feature builds",
                "LLM API integration & prompt eng",
                "Code review & architecture sync",
                "Min. 4 hours per session",
            ],
            "cta_label": "Book Hourly Session",
            "cta_msg": "Hi Ramesh, I want to book hourly full-stack AI dev time at the $29/hr promotional rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,000+",
            "rate": "$1,999", "rate_unit": "Best Value",
            "period": "Full-time equivalent · 160 hrs/mo",
            "badge": "Most Popular",
            "featured": True,
            "features": [
                "Dedicated Next.js + FastAPI + AI dev",
                "Deep LLM / RAG feature integration",
                "Scalable database architecture",
                "CI/CD + Docker deployment",
                "Daily standups, weekly reports",
                "Direct developer collaboration",
            ],
            "cta_label": "Secure Monthly Rate",
            "cta_msg": "Hi Ramesh, I want to discuss a monthly full-stack AI retainer at $1,999/mo.",
        },
        {
            "type": "AI SaaS MVP",
            "market_rate": "$4,000+",
            "rate": "From $1,999", "rate_unit": "Fixed",
            "period": "Fixed-price · 4–8 weeks",
            "features": [
                "Complete AI-powered SaaS MVP",
                "Auth, Stripe payments, core AI",
                "React dashboard + FastAPI backend",
                "LLM/RAG integration included",
                "Production-ready deployment",
            ],
            "cta_label": "Get MVP Quote",
            "cta_msg": "Hi Ramesh, I need an AI SaaS MVP built. Can you share a direct pricing quote?",
        },
    ],
    common_note
),

"business-automation.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Smart Business Automation. Smart Pricing.",
    "Replace manual workflows with AI agents and API integrations at unmatched value.",
    [
        {
            "type": "Hourly Rate",
            "market_rate": "$50 - $70",
            "rate": "$25", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "API webhooks & integrations",
                "Custom automation scripts (Python)",
                "Zapier/Make complex setups",
                "AI chatbot configuration",
                "Min. 4 hours per session",
            ],
            "cta_label": "Book Hourly Session",
            "cta_msg": "Hi Ramesh, I want to book hourly automation work at the $25/hr promotional rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$3,500+",
            "rate": "$1,899", "rate_unit": "Best Value",
            "period": "Full-time equivalent · 160 hrs/mo",
            "badge": "Top Choice",
            "featured": True,
            "features": [
                "Dedicated automation engineering",
                "Deploy AI agents for business tasks",
                "Deep CRM & Stripe integrations",
                "Lead gen & support automation",
                "Ongoing maintenance & monitoring",
                "Direct WhatsApp / Slack support",
            ],
            "cta_label": "Secure Retainer Rate",
            "cta_msg": "Hi Ramesh, I want a monthly business automation retainer at $1,899/mo.",
        },
        {
            "type": "Automation Project",
            "market_rate": "$1,500",
            "rate": "From $799", "rate_unit": "Fixed",
            "period": "Fixed-price · 1–3 weeks",
            "features": [
                "End-to-end automation workflow",
                "Secure 3rd-party API integration",
                "Internal AI chatbot deployment",
                "Thorough testing & docs",
                "30 days post-launch support",
            ],
            "cta_label": "Get Project Quote",
            "cta_msg": "Hi Ramesh, I have an automation project. Can you provide a discounted quote?",
        },
    ],
    common_note
),

"freelancer.html": pricing_section(
    "🔥 Direct Hire Discount",
    "Premium Engineering without Agency Fees.",
    "Hourly, monthly retainer, or fixed-price — get 50% off market rates by hiring me directly.",
    [
        {
            "type": "Hourly · All Services",
            "market_rate": "$60 - $80",
            "rate": "$25–29", "rate_unit": "-50% Off",
            "period": "Billed weekly · 4hr minimum",
            "features": [
                "AI engineering: $29/hr",
                "Full-Stack dev: $25/hr",
                "Backend engineering: $29/hr",
                "Business automation: $25/hr",
                "Flexible schedule, async friendly",
            ],
            "cta_label": "Book Hourly Work",
            "cta_msg": "Hi Ramesh, I want to book hourly freelance work at the discounted rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,000+",
            "rate": "$1,899–1,999", "rate_unit": "/ month",
            "period": "160 hrs · Full-time equivalent",
            "badge": "Best Value",
            "featured": True,
            "features": [
                "Dedicated full-time capacity",
                "Focus on AI, Backend, or Full-Stack",
                "Daily standups + weekly reports",
                "Direct Slack/WhatsApp comms",
                "Invoiced monthly (NET-7)",
                "Cancel anytime with 2-week notice",
            ],
            "cta_label": "Discuss Retainer",
            "cta_msg": "Hi Ramesh, I'm interested in a monthly retainer at the promotional pricing.",
        },
        {
            "type": "Fixed-Price Project",
            "market_rate": "Market Value",
            "rate": "Custom", "rate_unit": "Quote",
            "period": "Milestone-based · Clear scope",
            "features": [
                "Automation project: from $799",
                "Backend API project: from $1,199",
                "SaaS MVP: from $1,899",
                "AI agent / RAG: from $1,999",
                "Invoiced at completed milestones",
            ],
            "cta_label": "Request Quote",
            "cta_msg": "Hi Ramesh, I have a fixed-price project I'd like a discounted quote for.",
        },
    ],
    common_note
),

"presentation.html": pricing_section(
    "🔥 Exclusive Direct Offer",
    "Service Rates & Engagement Models",
    "By hiring directly, you bypass agency markups and access senior engineering at a fraction of the cost.",
    [
        {
            "type": "Hourly Consulting",
            "market_rate": "$60 - $80",
            "rate": "$25–29", "rate_unit": "/ hour",
            "period": "Flexible · Min. 4 hours",
            "features": [
                "AI/LLM engineering: $29/hr",
                "Full-Stack development: $25/hr",
                "Backend engineering: $29/hr",
                "Business automation: $25/hr",
            ],
            "cta_label": "Book Hours",
            "cta_msg": "Hi Ramesh, I'd like to book hourly consulting at the direct-hire rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,000+",
            "rate": "$1,899–1,999", "rate_unit": "/ month",
            "period": "Full-time · 160 hrs/month",
            "badge": "Recommended",
            "featured": True,
            "features": [
                "Dedicated engineering capacity",
                "AI, Full-Stack, or Backend focus",
                "Daily standups, weekly reports",
                "WhatsApp / Slack support",
                "Professional monthly invoice",
            ],
            "cta_label": "Discuss Retainer",
            "cta_msg": "Hi Ramesh, I want to discuss a monthly retainer at the promotional rate.",
        },
        {
            "type": "Fixed Project",
            "market_rate": "Agency Pricing",
            "rate": "Custom", "rate_unit": "Quote",
            "period": "Milestone-based invoicing",
            "features": [
                "Automation: from $799",
                "Backend API: from $1,199",
                "SaaS MVP: from $1,899",
                "AI agent: from $1,999",
            ],
            "cta_label": "Get a Quote",
            "cta_msg": "Hi Ramesh, I need a direct-hire quote for a project.",
        },
    ],
    common_note
),

"index.html": pricing_section(
    "🔥 50% Exclusive Discount",
    "Premium Engineering without Agency Fees.",
    "Hire a senior Full-Stack & Agentic AI Engineer directly and save on massive agency markups. High-quality code, unbeatable value.",
    [
        {
            "type": "Hourly Consulting",
            "market_rate": "$60 - $80",
            "rate": "$25–29", "rate_unit": "-50% Off",
            "period": "Pay-as-you-go · Billed weekly",
            "features": [
                "AI engineering: $29/hr",
                "Full-Stack dev: $25/hr",
                "Backend engineering: $29/hr",
                "Business automation: $25/hr",
                "Flexible schedule, async friendly",
            ],
            "cta_label": "Book Hourly Work",
            "cta_msg": "Hi Ramesh, I found your portfolio and want to book hourly freelance work at the discounted rate.",
        },
        {
            "type": "Monthly Retainer",
            "market_rate": "$4,000+",
            "rate": "$1,899–1,999", "rate_unit": "/ month",
            "period": "160 hrs · Full-time equivalent",
            "badge": "Best Value",
            "featured": True,
            "features": [
                "Dedicated full-time capacity",
                "Focus on AI, Backend, or Full-Stack",
                "Daily standups + weekly reports",
                "Direct Slack/WhatsApp comms",
                "Invoiced monthly (NET-7)",
                "Cancel anytime with 2-week notice",
            ],
            "cta_label": "Discuss Retainer",
            "cta_msg": "Hi Ramesh, I saw your portfolio and I'm interested in a monthly retainer at the promotional pricing.",
        },
        {
            "type": "Fixed-Price Project",
            "market_rate": "Market Value",
            "rate": "Custom", "rate_unit": "Quote",
            "period": "Milestone-based · Clear scope",
            "features": [
                "Automation project: from $799",
                "Backend API project: from $1,199",
                "SaaS MVP: from $1,899",
                "AI agent / RAG: from $1,999",
                "Invoiced at completed milestones",
            ],
            "cta_label": "Request Quote",
            "cta_msg": "Hi Ramesh, I found your portfolio and have a fixed-price project I'd like a discounted quote for.",
        },
    ],
    common_note
),

}

INJECT_BEFORE = "<!-- ── SEO Keyword Cloud ──"
FALLBACK_INJECT_BEFORE = "<!-- SEO Keyword Cloud -->"

for filename, html_block in PAGES.items():
    path = os.path.join(BASE, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean up old pricing sections injected previously
    content = re.sub(
        r'\s*<!-- ── Pricing & Services ── -->.*?</style>\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )
    # Also clean up the presentation.html custom injection
    content = re.sub(
        r'\s*<!-- Pricing & Services -->.*?</section>\s*\n',
        '\n',
        content,
        flags=re.DOTALL
    )

    if INJECT_BEFORE in content:
        content = content.replace(INJECT_BEFORE, html_block + INJECT_BEFORE, 1)
    elif FALLBACK_INJECT_BEFORE in content:
        content = content.replace(FALLBACK_INJECT_BEFORE, html_block + FALLBACK_INJECT_BEFORE, 1)
    else:
        # Final fallback: inject before <footer
        marker = '<footer class="footer">'
        if marker in content:
            content = content.replace(marker, html_block + marker, 1)
        else:
            print(f"WARN (no injection point found): {filename}")
            continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {filename}")

print("\nDone.")
