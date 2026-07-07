import os
import json
import time
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# ==============================================================================
# CONFIGURATION
# ==============================================================================
BASE_URL = "https://www.rameshdas.dev"
JSON_KEY_FILE = "ramesh-portfolio-499406-2f223aed9f17.json"  # <-- You need to put your GCP service account JSON key here
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# Google's strict default limit for the Indexing API is 200 URLs per day.
# We save progress to avoid hitting limits and getting blocked.
PROGRESS_FILE = "indexing_progress.json"
DAILY_LIMIT = 200

def get_all_html_urls(directory="."):
    """Finds all HTML files in the directory and returns their full URLs."""
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    # We also want to include the root domain
    urls = [f"{BASE_URL}/"]
    for file in html_files:
        # Avoid duplicate index.html 
        if file != "index.html":
            urls.append(f"{BASE_URL}/{file}")
    return sorted(list(set(urls)))

def load_progress():
    """Loads the list of already indexed URLs to resume safely."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {"indexed_urls": [], "last_run_date": None}

def save_progress(progress):
    """Saves the current progress to the local JSON file."""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=4)

def main():
    print("🔍 Fetching all pages...")
    all_urls = get_all_html_urls("/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev
    print(f"Total HTML pages found: {len(all_urls)}")

    progress = load_progress()
    today_str = time.strftime("%Y-%m-%d")

    # Reset daily count if it's a new day
    if progress.get("last_run_date") != today_str:
        progress["last_run_date"] = today_str
        progress["daily_count"] = 0
    else:
        # Handle cases where daily_count might be missing in older progress files
        if "daily_count" not in progress:
            progress["daily_count"] = 0

    already_indexed = set(progress.get("indexed_urls", []))
    urls_to_index = [u for u in all_urls if u not in already_indexed]

    print(f"Pages already submitted previously: {len(already_indexed)}")
    print(f"Pages left to submit: {len(urls_to_index)}")
    print(f"Quota used today: {progress['daily_count']}/{DAILY_LIMIT}")

    if not urls_to_index:
        print("🎉 All pages have been successfully submitted to the Google Indexing API!")
        return

    if progress["daily_count"] >= DAILY_LIMIT:
        print("⚠️ You have reached the 200 URL daily limit for today. Please run this script again tomorrow to continue indexing the rest.")
        return

    # Check for credentials before starting
    if not os.path.exists(JSON_KEY_FILE):
        print(f"\n❌ ERROR: Service account key file '{JSON_KEY_FILE}' not found.")
        print("Please read the instructions on how to generate this key from Google Cloud Console.")
        return

    # Authenticate via Service Account
    print("\n🔐 Authenticating with Google Indexing API...")
    try:
        credentials = service_account.Credentials.from_service_account_file(
            JSON_KEY_FILE, scopes=SCOPES
        )
        authed_session = AuthorizedSession(credentials)
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return

    # Process URLs up to the daily limit
    available_quota = DAILY_LIMIT - progress["daily_count"]
    batch_to_process = urls_to_index[:available_quota]

    print(f"\n🚀 Submitting {len(batch_to_process)} URLs to Google...\n")

    for url in batch_to_process:
        payload = {
            "url": url,
            "type": "URL_UPDATED"
        }
        
        try:
            response = authed_session.post(ENDPOINT, json=payload)
            if response.status_code == 200:
                print(f"✅ SUCCESS: {url}")
                progress["indexed_urls"].append(url)
                progress["daily_count"] += 1
                save_progress(progress)
            elif response.status_code == 429:
                print("⚠️ ERROR 429: Quota Exceeded. Stopping for today.")
                break
            else:
                print(f"❌ FAILED: {url} | Status: {response.status_code} | Response: {response.text}")
        except Exception as e:
            print(f"❌ NETWORK ERROR for {url}: {e}")
        
        # Slight delay to respect API rate limits
        time.sleep(0.5)

    print("\n🏁 Run complete!")
    if len(progress["indexed_urls"]) < len(all_urls):
        print(f"⚠️ You still have {len(all_urls) - len(progress['indexed_urls'])} pages left. Run this script again tomorrow to continue submitting.")

if __name__ == "__main__":
    main()
