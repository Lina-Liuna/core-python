from typing import Any

import requests
import lxml
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from xlwt import *
from openpyxl import load_workbook

url = "https://www.rottentomatoes.com/top/bestofrt/"
dir = '/Users/linaliu/Movies/rottentomatoes/'

def get_movielist(url, dir):
    f = requests.get(url)
    soup = BeautifulSoup(f.content, 'lxml')
    movies = soup.find_all('img')
    print(movies)
    movie_lists = [[], []]
    for movie in movies:
        if not movie.has_attr('src'):
            continue
        print(movie['src'])
        movie_lists[0].append(movie['src'])
        movie_lists[1].append(movie['alt'])
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
    return movie_lists

def write_movieinfo_to_excel(dir, movie_info):
    workbook = Workbook(encoding= 'utf-8')
    table = workbook.add_sheet('data')
    table.write(0, 0, 'Number')
    table.write(0, 1, 'movie_url')
    table.write(0, 2, 'movie_name')

    for i in range(1, len(movie_info[0])):
        table.write(i, 0, i)
        table.write(i, 1, movie_info[0][i])
        table.write(i, 2, movie_info[1][i])


    workbook.save(dir + 'movielist.xls')

Movieinfo = get_movielist(url, dir)

write_movieinfo_to_excel(dir, Movieinfo)

