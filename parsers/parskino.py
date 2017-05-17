from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("https://www.kinopoisk.ru/premiere").content)

for text in soup('span','name_big'):
	print (text.next.contents[0])
for text in soup('span','name'):
	print (text.next.contents[0])
