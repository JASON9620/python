# -*- coding:utf-8 -*-
'''装饰器
开放封闭原则
重复调用相同的函数时，可以使用装饰器'''

# def fun1():
#     print('----1---')
#
# def fun1():
#     print('---2---')
#
# if __name__ == "__main__":
#     a = fun1()

def w1(fun):
    print("---正在进行装饰")
    def inner():
        print("---正在验证权限---")
        fun()
    return inner

"""解释器执行到这行代码时，就会自动进行装饰，而不是等到调用的时候才进行装饰"""
@w1   #f1 = w1(f1)   语法糖
def f1():
    print("---f1---")

@w1
def f2():
    print("---f2---")

# f1()
# f2()








