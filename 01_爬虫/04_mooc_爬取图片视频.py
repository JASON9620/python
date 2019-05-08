# -*- coding:utf-8 -*-
import requests
import os
url = "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1554187895&di=fdf0205eb8e2f355cbf255022aa4b5d5&src=http://ditu.ps123.net/china/UploadFile/201411/2014113007074051.jpg"
root = "E://mooc//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')

except:
    print('文件保存失败')

