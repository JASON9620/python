# -*- coding:utf-8 -*-
"""两层装饰器
带有参数的装饰器"""

def tf_arg(arg):
    print("---第一层装饰---")
    def w1(fun):
        print("---第二层装饰---arg=%s"%arg)
        def inner():
            print("---正在验证权限---")
            ret=fun()
            return ret
        return inner
    return w1

"""先执行tf_arg，再返回@w1"""

@tf_arg("haha")
def f1():
    print("---f1---")

f1()