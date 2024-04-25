import requests
from bs4 import BeautifulSoup
import json

url = "https://letterboxd.com/lexiamoriello/list/movies-that-inspired-music/"
response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

page = html.find('div', class_='cols-2')
posters = page.find_all('li', class_='poster-container')

film_list = []
film_list.append({"title": "Movies That Inspired Music"})

for poster in posters:
    img_tag = poster.find('img', class_='image')
    alt_text = img_tag['alt']
    film_list.append(alt_text)
    print(alt_text)

with open('letterboxd.json', 'w', encoding='utf-8') as file:
    json.dump(film_list, file, ensure_ascii=False, indent=4)
