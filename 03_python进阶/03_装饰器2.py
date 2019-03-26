# -*- coding:utf-8 -*-
def makebole(fn):
    print("---正在装饰1---")
    def wrapped():
        print("---1---")
        return "<b>" + fn() + "</b>"
    return wrapped

def makeItalic(fn):
    print("---正在装饰2---")
    def wrapped():
        print("---2---")
        return "<i>" + fn() + "</i>"
    return  wrapped

@makebole
@makeItalic #"""先装饰完makeItalic，再装饰makebole"""
def tf3():
    print("---3---")
    return "hello world"


ret=tf3()
print(ret)





