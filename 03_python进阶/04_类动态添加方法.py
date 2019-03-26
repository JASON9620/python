# -*- coding:utf-8 -*-
import types
class Person(object):
    # __slots__ = ("name", "age") ###也不可再额外添加方法
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("---%s is eating---"%self.name)


def run(self):
    print("---%s is running---"%self.name)

pr = Person("wang", 18)
pr.eat()
pr.run = types.MethodType(run, pr)   #动态添加方法
pr.run()





