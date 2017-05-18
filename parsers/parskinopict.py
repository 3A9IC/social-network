from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("https://www.kinopoisk.ru/premiere").content)

for img in soup('img'):
    print (img.get('src'))