import requests
from bs4 import BeautifulSoup

url = "https://myanimelist.net/topanime.php"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

animes = []
for item in soup.select(".ranking-list .detail"):
    title = item.select_one("div.di-ib a.hoverinfo_trigger").text
    link = item.select_one("div.di-ib a.hoverinfo_trigger").get("href")
    animes.append((title, link))

print(animes)