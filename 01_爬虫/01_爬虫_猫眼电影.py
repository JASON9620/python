# -*- coding:utf-8 -*-
import requests
import lxml

def getonepage(n):

    url = 'https://maoyan.com/board/4?offset={}'.format(n)
    header = {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    r = requests.get(url, headers=header)
    print(r)
    # print(r.text)
    return r.text

def parse():
    pass




getonepage(10)
