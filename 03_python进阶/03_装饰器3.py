# -*- coding:utf-8 -*-
"""装饰器传递有参数和无参数的情况
有返回值和无返回值的情况
----通用装饰器----"""
def tf(funName):
    print("---01---")
    def wrapped(*args,**kwargs):    #fun指向wrapped，参数保持一致
        print("----wrapped---")
        ret = funName(*args,**kwargs)   #funName指向fun，参数保持一致
        return ret    #加入返回值，若返回值则返回，若没有则返回None
    return wrapped

@tf       #执行到此行代码时，调用tf函数
def fun(a,b):
    print("----fun---a=%d,b=%d"%(a,b))
    return a

aa = fun(1,2)

@tf       #执行到此行代码时，调用tf函数
def fun2(a,b,c):
    print("----fun---a=%d,b=%d,c=%d"%(a,b,c))



fun2(22,33,44)






