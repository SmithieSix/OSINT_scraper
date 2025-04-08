import requests
from bs4 import BeautifulSoup

def scrape_darkweb(url, keywords):
    proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = []
            for post in soup.find_all("h2"):
                if any(k.lower() in post.text.lower() for k in keywords):
                    results.append({"source": "DarkWeb", "title": post.text})
            return results
        return []
    except Exception as e:
        print(f"Dark web scrape error: {e}")
        return []
