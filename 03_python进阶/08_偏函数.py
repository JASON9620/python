# -*- coding:utf-8 -*-
import functools

"""###对偏函数的输出结果，不是很明白###"""

def showarg(*args, **kwargs):
    print(args)
    print(kwargs)

p1 = functools.partial(showarg, 1,2,3)
p1()
p1(4,5,6)
p1(a="python", b="it cast")

p2 = functools.partial(showarg, a=3, b="linux")
p2()
p2(1, 2)
p2(a="python", b="it cast")




