from bs4 import BeautifulSoup
import requests


def Parser():
    URL = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
    except :
        print("Не удалось подключиться к сайту")
        return -1

    Top_movies = {}
    block = soup.findAll('tr') #контейнер с нужным классом
    for data in block: #цикл по контейнеру
        title = []
        rating = []
        temp1 = data.find('td', class_="titleColumn")
        if temp1 is not None:
            title = temp1.text.split() #нахожение название фильма как списка
        temp2 = data.find('td', class_="ratingColumn imdbRating")
        if temp2 is not None:
            rating = temp2.text.split() #нахождение рейтинга фильма
        if title != [] and rating != []:
            Top_movies[' '.join(title)] = rating
    return Top_movies