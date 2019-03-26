# -*- coding:utf-8 -*-
"""闭包
闭包应用于固定num1的情况，一般用于函数"""
def exfun1(num1):
    print("----I am fengexian----")
    def test2(num2):
        print(num1+num2)
    return test2

tes=exfun1(100)
a=tes(200)
















