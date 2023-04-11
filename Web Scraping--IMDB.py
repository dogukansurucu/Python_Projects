import requests
from bs4 import BeautifulSoup
import xml

url = "https://www.imdb.com/chart/top/"
html = requests.get(url).content

a = BeautifulSoup(html,"lxml")
veri = a.find("tbody" ,attrs={"class":"lister-list"})


dondur = veri.find_all("tr",limit=50)

sayac = 0
for filmler in dondur:
    sayac += 1
    title = filmler.find("td",attrs = {"class": "titleColumn"}).a.text
    year = filmler.find("td",attrs = {"class":"titleColumn"}).span.text.strip("()")
    rating = filmler.find("td", attrs = {"class": "ratingColumn imdbRating"}).strong.get("title")
    print(f"{sayac}.film --> Başlık: {title} , Vizyona Çıkış Tarihi: {year} , Rating: {rating}\n")






