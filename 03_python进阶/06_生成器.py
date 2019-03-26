# -*- coding:utf-8 -*-
"""yield生成器，执行到yield，程序暂停
next返回当前值并使得程序继续往下执行，
send可使得yield返回某一指定值
执行send之前必须先执行next，或者send(None)"""


def creatNum():
    print("----start----")
    a, b = 0, 1
    for i in range(9):
        print("---1---")
        bb = yield b   # yield 执行完毕，程序暂停，但并不返回值（None）
        print("---2---")
        a,b = b, a+b
        print("---3---")
    print("---end---已经没有生成能力了---")

num = creatNum()

"""这种方法会导致生成器崩溃或者是未执行完毕，
不建议采取这种做法"""
# for i in range(9):
#     ne = next(num)   #ne = num.__next__()  #效果等效
#     print(ne)

"""完全打印生成器的内容，不会导致崩溃或者未执行完毕"""
for i in num:
    print(i)






