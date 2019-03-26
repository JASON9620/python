# -*- coding:utf-8 -*-
class Test(object):
    def __init__(self):
        self.__num = 100

    # def getnum(self):
    #     return self.__num
    #
    # def setnum(self, numb):
    #     self.__num = numb
    #
    # num = property(getnum, setnum)
    # # """property对方法进行了封装"""

    """@property对getnum和setnum
    进行修饰
    调用property的第二种方法"""
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, numb):
        self.__num = numb




t = Test()
t.num = 9
print(t.num)
