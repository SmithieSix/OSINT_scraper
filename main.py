from config import KEYWORDS
from scraper_news import scrape_hacker_news
from scraper_darkweb import scrape_darkweb
from database import store_if_new
from alerts import send_alert

darkweb_sites = ["http://exampledarkweb.onion"]  # Replace with real URLs

def run_osint():
    all_items = []

    # Scrape HN
    news_items = scrape_hacker_news(KEYWORDS)
    all_items.extend(news_items)

    # Scrape Dark Web
    for site in darkweb_sites:
        dark_items = scrape_darkweb(site, KEYWORDS)
        all_items.extend(dark_items)

    # Store and alert
    for item in all_items:
        if store_if_new(item):
            send_alert("🚨 New OSINT Match Found", f"{item['title']}\n{item.get('link', '')}")

if __name__ == "__main__":
    run_osint()
