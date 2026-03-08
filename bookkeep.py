import json
import notify
from pathlib import Path

SEEN_FILE = "./json/seen_listings.json"

def load_seen() -> set:
    if Path(SEEN_FILE).exists():
        return set(json.loads(Path(SEEN_FILE).read_text()))
    return set()

def save_seen(seen: set):
    Path(SEEN_FILE).write_text(json.dumps(list(seen)))

def notify_new(listings: list):
    seen = load_seen()
    # only notify about listings that have not been seen before
    new_listings = [l for l in listings if l['link'] not in seen]
    print(f"Found {len(new_listings)} new listings")
    for listing in new_listings:
        notify.send_telegram_notifications(listing)
        seen.add(listing['link'])

    save_seen(seen)