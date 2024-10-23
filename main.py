import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://myanimelist.net/topanime.php"

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

animes = []
for item in soup.select(".ranking-list .detail .di-ib a"):
    title = item.text.strip()
    animes.append(title)

animes = [item for item in animes if item and item.strip()]

df = pd.DataFrame(animes, columns=["Title"])
print(df)