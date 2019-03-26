# -*- coding:utf-8 -*-
class tf(object):
    def __init__(self):
        print("---1---")
    def __call__(self, *args, **kwargs):
        print("---2---")


tfu = tf() #调用tf方法，执行__init__方法
tfu()     #直接调用tfu，执行__call__方法
