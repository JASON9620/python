# -*- coding:utf-8 -*-
"""类作为装饰器，形参func和__func指向函数func1，func1指向__call__"""
class tf(object):
    def __init__(self, func):
        print("---init---")
        print("---func name is %s"%func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("---装饰器的功能---")
        self.__func()


@tf
def func1():
    print("---func1---")

func1()
