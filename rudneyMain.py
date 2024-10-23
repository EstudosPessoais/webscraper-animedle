import requests
from bs4 import BeautifulSoup

def fetch_animes(url):
    # Faz a requisição para o site
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Falha ao acessar {url}")
        return []

    # Faz a análise do conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra os elementos que contêm os animes
    anime_list = []
    for anime in soup.select('.seasonal-anime'):
        title = anime.select_one('.title').get_text(strip=True)
        link = anime.select_one('a')['href']
        anime_list.append({'title': title, 'link': link})

    return anime_list


url = 'https://myanimelist.net/anime/season'
animes = fetch_animes(url)

for anime in animes:
    print(f"Título: {anime['title']}, Link: {anime['link']}")