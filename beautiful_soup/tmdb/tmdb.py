import requests
from bs4 import BeautifulSoup
import json


url="https://www.themoviedb.org/movie"

headers={
    "User-Agent":"---------------------------------------------------------------------------------------"
}

response=requests.get(url,headers=headers).content
html=BeautifulSoup(response, "html.parser")

film_list=[]

div_1=html.find('div', {'class':'page_wrapper'}).find_all('div', {'class':'card style_1'})

for item in div_1:
    text=item.find('a', {'class': 'image'})
    alt_text= text['title'] 

    icon_class = item.find('span', {'class': 'icon'})['class']
    rate = icon_class[1].split('-')[-1]  
    film_info= {
        "Movie Name": alt_text,
        "Movie Rate": rate
    }
    film_list.append(film_info)

    print("Movie Name: " + alt_text + ", Rate is: " + rate)


with open("tmdb.json", "w", encoding="utf-8") as file:
    json.dump(film_list, file, ensure_ascii=False, indent=4)



