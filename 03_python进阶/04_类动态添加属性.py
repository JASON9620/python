# -*- coding:utf-8 -*-
class Person(object):
    # __slots__ = ("name", "age")  ###__slots__固定Person的属性名字和个数，不能随便再添加属性
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

laowang = Person("laowang", 15)
laowang.add = "beijing"
print(laowang.add)

laozhao = Person("laozhao", 18)
"""laozhao类中不含有laozhao.add属性，动态添加的laowang.add，laowang唯一具有"""

Person.addl = "anhui"
"""添加到Person中的属性addl，所有类都具有"""
print(laozhao.addl)



