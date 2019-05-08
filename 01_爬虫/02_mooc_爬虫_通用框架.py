# -*- coding:utf-8 -*-
import requests
# import time
# url = 'http://www.baidu.com'
# r = requests.get(url)
# r.encoding = 'utf-8'
# r.apparent_encoding
# r.text
# r.headers


"""网络连接有风险，异常控制有必要"""
def fn(url, kv):
    try:
        r = requests.get(url, timeout=30, headers=kv)
        print(r.request.headers)  #返回访问网页时的头文件
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    kv = {"user-agent": "Mozilla/5.0"}
    """增加headers，访问有保密措施的网页"""
    print(fn(url, kv))
