import requests
from bs4 import BeautifulSoup

url = "https://myanimelist.net/topanime.php"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

animes = []
for item in soup.select(".ranking-list .detail .di-ib a.hoverinfo_trigger"):
    title = item.text.strip()
    url = item.get("href")
    animes.append((title, url))

print(animes)