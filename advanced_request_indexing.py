import os
import json
import time
from datetime import datetime, timedelta, timezone
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# ==============================================================================
# CONFIGURATION
# ==============================================================================
BASE_URL = "https://mrdasdeveloper.github.io"
JSON_KEY_FILE = "ramesh-portfolio-499406-2f223aed9f17.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

PROGRESS_FILE_V1 = "indexing_progress.json"
PROGRESS_FILE_V2 = "indexing_progress_v2.json"
DAILY_LIMIT = 200

# ==============================================================================
# CATEGORIZATION LOGIC
# ==============================================================================
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

hubs_mapping = {
    "hire-developers-usa.html": "usa",
    "hire-developers-uk.html": "uk",
    "hire-developers-canada.html": "canada",
    "hire-developers-australia.html": "australia",
    "hire-developers-germany.html": "germany",
    "hire-developers-japan.html": "japan",
    "hire-developers-singapore.html": "singapore",
    "hire-developers-saudi-arabia.html": "saudi-arabia",
    "hire-developers-middle-east.html": "middle-east",
}

def categorize_url(filename):
    if filename in hubs_mapping:
        return {"category": "hub", "country": hubs_mapping[filename], "city": None}
    
    # Check if it's a city page
    for country, cities in country_slugs.items():
        for city in cities:
            if filename.endswith(f"-{city}.html"):
                return {"category": "city_page", "country": country, "city": city}
    
    return {"category": "core", "country": None, "city": None}

def get_all_html_files(directory="."):
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    return html_files

# ==============================================================================
# STATE MANAGEMENT
# ==============================================================================
def load_and_migrate_progress():
    now_str = datetime.now(timezone.utc).isoformat()
    today_str = time.strftime("%Y-%m-%d")
    
    state = {
        "last_run_date": today_str,
        "daily_count": 0,
        "pages": {}
    }

    # Load existing V2 if it exists
    if os.path.exists(PROGRESS_FILE_V2):
        with open(PROGRESS_FILE_V2, 'r') as f:
            state = json.load(f)
            if state.get("last_run_date") != today_str:
                state["last_run_date"] = today_str
                state["daily_count"] = 0
            return state

    # Migrate from V1 if V2 doesn't exist
    if os.path.exists(PROGRESS_FILE_V1):
        with open(PROGRESS_FILE_V1, 'r') as f:
            v1_data = json.load(f)
            
            # Keep the daily quota in sync!
            if v1_data.get("last_run_date") == today_str:
                state["last_run_date"] = today_str
                state["daily_count"] = v1_data.get("daily_count", 0)
            
            for url in v1_data.get("indexed_urls", []):
                state["pages"][url] = {
                    "last_submitted": now_str, # Just submitted recently
                    "status": "submitted"
                }
    return state

def save_progress(state):
    with open(PROGRESS_FILE_V2, 'w') as f:
        json.dump(state, f, indent=4)

# ==============================================================================
# MAIN LOGIC
# ==============================================================================
def main():
    print("🔍 Initializing Advanced Indexing Tracker...")
    state = load_and_migrate_progress()
    
    # Discover all pages and update schema
    html_files = get_all_html_files()
    all_urls = []
    
    for file in html_files:
        url = f"{BASE_URL}/{file}" if file != "index.html" else f"{BASE_URL}/"
        all_urls.append(url)
        
        # Add to state if not tracked
        if url not in state["pages"]:
            cat_data = categorize_url(file)
            state["pages"][url] = {
                "category": cat_data["category"],
                "country": cat_data["country"],
                "city": cat_data["city"],
                "status": "pending",
                "last_submitted": None
            }
            # Fill in the missing categories for V1 migrated pages
        elif "category" not in state["pages"][url]:
            cat_data = categorize_url(file)
            state["pages"][url].update(cat_data)

    save_progress(state)

    # Filtering logic:
    # 1. Prioritize pages that have NEVER been submitted (status: pending)
    # 2. Then, find pages submitted > 24 hours ago
    pending_urls = []
    resubmit_urls = []
    
    now = datetime.now(timezone.utc)
    
    for url, data in state["pages"].items():
        if data["status"] == "pending":
            pending_urls.append(url)
        else:
            last_sub_str = data.get("last_submitted")
            if last_sub_str:
                try:
                    last_sub_dt = datetime.fromisoformat(last_sub_str)
                    if now - last_sub_dt >= timedelta(hours=24):
                        resubmit_urls.append(url)
                except Exception:
                    pass
    
    print(f"📊 Tracking {len(all_urls)} total pages.")
    print(f"   -> 🆕 Pending (Never submitted): {len(pending_urls)}")
    print(f"   -> 🔄 Eligible for 24h Resubmission: {len(resubmit_urls)}")
    print(f"   -> 📈 Quota used today: {state['daily_count']}/{DAILY_LIMIT}")

    # Sort to prioritize CORE > HUB > CITY_PAGE
    def get_priority(url):
        cat = state["pages"][url]["category"]
        priorities = {"core": 1, "hub": 2, "city_page": 3}
        return priorities.get(cat, 4)

    pending_urls.sort(key=get_priority)
    resubmit_urls.sort(key=get_priority)

    # Combine lists, putting completely fresh pages first
    urls_to_process = pending_urls + resubmit_urls

    if not urls_to_process:
        print("🎉 No pages need submission! All pages have been submitted within the last 24 hours.")
        return

    if state["daily_count"] >= DAILY_LIMIT:
        print("⚠️ Daily limit reached. Try again tomorrow.")
        return

    print("\n🔐 Authenticating with Google Indexing API...")
    try:
        credentials = service_account.Credentials.from_service_account_file(
            JSON_KEY_FILE, scopes=SCOPES
        )
        authed_session = AuthorizedSession(credentials)
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return

    available_quota = DAILY_LIMIT - state["daily_count"]
    batch = urls_to_process[:available_quota]

    print(f"\n🚀 Submitting {len(batch)} URLs to Google...\n")

    for url in batch:
        payload = {"url": url, "type": "URL_UPDATED"}
        page_info = state["pages"][url]
        
        # Just to print nicely
        cat_str = f"[{page_info['category'].upper()}]"
        if page_info['country']: cat_str += f" [{page_info['country'].upper()}]"

        try:
            response = authed_session.post(ENDPOINT, json=payload)
            if response.status_code == 200:
                print(f"✅ SUCCESS: {cat_str} {url}")
                state["pages"][url]["status"] = "submitted"
                state["pages"][url]["last_submitted"] = datetime.now(timezone.utc).isoformat()
                state["daily_count"] += 1
                save_progress(state)
            elif response.status_code == 429:
                print("⚠️ ERROR 429: Quota Exceeded. Stopping for today.")
                break
            else:
                print(f"❌ FAILED: {url} | Status: {response.status_code}")
        except Exception as e:
            print(f"❌ NETWORK ERROR for {url}: {e}")
        
        time.sleep(0.5)

    print("\n🏁 Advanced Run complete!")
    remaining = len(urls_to_process) - len(batch)
    if remaining > 0:
        print(f"⚠️ You still have {remaining} pages queued. Run again tomorrow.")

if __name__ == "__main__":
    main()
