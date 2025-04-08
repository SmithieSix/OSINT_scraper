import requests
from bs4 import BeautifulSoup

def scrape_hacker_news(keywords):
    url = "https://news.ycombinator.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for item in soup.select(".titleline a"):
        title = item.text
        link = item["href"]
        if any(k.lower() in title.lower() for k in keywords):
            results.append({"source": "HackerNews", "title": title, "link": link})
    return results
