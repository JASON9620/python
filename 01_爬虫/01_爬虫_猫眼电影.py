# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

root = 'https://maoyan.com/board/4?offset='
header = {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
li = []
for i in range(9):
    i = i*10
    i = str(i)
    url = root + i
    r = requests.get(url, headers=header)
    r.status_code
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    for ti in soup.find_all('a'):
        tit = ti.get('title')
        if tit is not None:
            if tit not in li:
                li.append(tit)

print(li)



