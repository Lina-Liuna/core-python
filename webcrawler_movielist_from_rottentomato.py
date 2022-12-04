import requests
import lxml
from bs4 import BeautifulSoup


url = "https://www.rottentomatoes.com/top/bestofrt/"
dir = '/Users/linaliu/Movies/rottentomatoes/'

def get_movielist(url, dir):
    f = requests.get(url)
    soup = BeautifulSoup(f.content, 'lxml')
    movies = soup.find_all('img')
    print(movies)
    for movie in movies:
        if not movie.has_attr('src'):
            continue
        print(movie['src'])
        print(movie['alt'])
        img_url = movie['src']
        movie_name = movie['alt']
        pic_ext = '.' + img_url.split(".")[-1][0:3]
        if 'https' not in img_url:
            continue
        if '<em>' in movie_name:
            movie_name = movie_name.replace('<em>', '')
        if '</em>' in movie_name:
            movie_name = movie_name.replace('</em>', '')
        print(pic_ext)
        img_data = requests.get(img_url).content
        img_name = dir + movie_name + pic_ext
        with open(img_name, 'wb') as handler:
            handler.write(img_data)


get_movielist(url, dir)

