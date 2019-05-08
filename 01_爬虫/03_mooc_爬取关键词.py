# -*- coding:utf-8 -*-
import requests
url = "http://www.baidu.com/s"
keyword = 'python'
try:
    kv = {'wd': keyword }
    """爬取关键词格式http://www.baidu.com/s?wd=python"""
    r = requests.get(url, params=kv)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
except:
    print("产生异常")



