import json
import os
from collections import defaultdict

PROGRESS_FILE = "indexing_progress_v2.json"

def main():
    if not os.path.exists(PROGRESS_FILE):
        print(f"❌ Could not find {PROGRESS_FILE}. Run the indexing script first!")
        return

    with open(PROGRESS_FILE, 'r') as f:
        data = json.load(f)

    pages = data.get("pages", {})
    
    total = len(pages)
    submitted = sum(1 for p in pages.values() if p.get("status") == "submitted")
    pending = total - submitted

    # Breakdowns
    by_category = defaultdict(lambda: {"total": 0, "submitted": 0})
    by_country = defaultdict(lambda: {"total": 0, "submitted": 0})

    for url, info in pages.items():
        cat = info.get("category", "unknown")
        country = info.get("country")

        by_category[cat]["total"] += 1
        if info.get("status") == "submitted":
            by_category[cat]["submitted"] += 1

        if country:
            by_country[country]["total"] += 1
            if info.get("status") == "submitted":
                by_country[country]["submitted"] += 1

    print("==================================================")
    print(" 📊 GOOGLE INDEXING PROGRESS REPORT ")
    print("==================================================")
    print(f"Total Pages Tracked : {total}")
    print(f"✅ Successfully Sent: {submitted}")
    print(f"⏳ Pending / Queued : {pending}")
    print("==================================================")
    
    print("\n📁 BREAKDOWN BY CATEGORY:")
    for cat, stats in sorted(by_category.items()):
        pct = (stats['submitted'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"  - {cat.upper().ljust(12)} : {stats['submitted']}/{stats['total']} ({pct:.1f}%)")

    print("\n🌍 BREAKDOWN BY COUNTRY (City & Hub pages):")
    # Sort countries alphabetically
    for country, stats in sorted(by_country.items()):
        pct = (stats['submitted'] / stats['total']) * 100 if stats['total'] > 0 else 0
        name = country.replace("-", " ").title()
        print(f"  - {name.ljust(15)} : {stats['submitted']}/{stats['total']} ({pct:.1f}%)")
    
    print("\n==================================================")
    print(f"📅 Last Run Date   : {data.get('last_run_date')}")
    print(f"📈 Quota Used Today: {data.get('daily_count')}/200")
    print("==================================================")

if __name__ == "__main__":
    main()
