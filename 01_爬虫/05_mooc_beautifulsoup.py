# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
tag = soup.body
bb = tag.p
print(bb)
print(tag, type(tag))


# for child in soup.html.descendants:
#     print(child)



