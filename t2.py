# -*- coding:utf-8 -*-
# import matplotlib.pyplot as plt
# x = [1,2,3,4]
# y = [10,20,25,30]
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(x, y, color='lightblue', linewidth=3)
# ax.scatter([2,4,6],
#            [5,15,25],
#            color='darkgreen',
#            marker='^')
# ax.set_xlim(1, 6.5)
# plt.savefig('foo.png')
# plt.show()


#
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(1, 100)
# #作图1
# plt.subplot(221)
# plt.plot(x, x)
# #作图2
# plt.subplot(222)
# plt.plot(x, -x)
# #作图3
# plt.subplot(223)
# plt.plot(x, x ** 2)
# plt.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
# #作图4
# plt.subplot(224)
# plt.plot(x, np.log(x))
# plt.show()


#
# my_list2 = [[4,5,6,7], [3,4,5,6]]
#
# print (my_list2[1][:2])
# a = 'is'
# b = 'nice'
# my_list = ['my', 'list', a, b]
# my_list.reverse()
# print( my_list )

# from pyspark.sql import SparkSession
# spark = SparkSession \
#     .builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()


# import os
# path1=os.path.join('aaaa','bbbb',)



# import r
# print(r.b)

# dir()
# print(dir())
# from tkinter import *
# L=[1,2]
# L.append(L)
# print(L)

# import  sys
# print(sys.argv)
# L=['ahj',['abc','sdf']]
# print(L[1][1]*2)
# print(2**16)
# L=[1,2,3,4]
# print(L[3:1])


# [ ].__methods__
# print(dir([]))

# print(2<3)

# for i in range(50):
    # print( 'hello %d\n\a' %i)

# D={'a':1,'f':2,'c':3,'d':4}
# print(type (D.keys()))
# type (D.keys())
# print(D)
# keys=list(D.keys())
# print(keys)
# print (type(keys))
# keys.sort()
# for key in keys:
#     print(key,'---',D[key])

# def mut(x,y):
#     x=2
#     y[0]=3
#     return x,y
# x=1
# L=[1,2]
# mut(x,L)
# print(x,L)
# x,L=mut(x,L)
# print(x,L)


# def f(x):
#     print(x+6)
# y=f(3)
# print(y)

# L=[1,2,3]
# L=L.append(4)
# print(L)

# x = 88
# def sel():
#     import __main__
#     print(__main__.x)
#     x=22
#
#     print(x)
#
# sel()


# def ss(**x):
    # return (x)
# print(ss(dd=2,ff=4))

# import sys
# print(sys.path)

# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.c_[a,b]
#
# print(np.r_[a,b])
# print(c)


# print('sss'*0)

# while True:
#     print(input().strip("吗?？")+"!")

# L=range(5)
# print(L)

# import os
# from collections import Counter
# def make_Dictionary(train_dir):
#     emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
#     all_words = []
#     for mail in emails:
#         with open(mail) as m:
#             for i, line in enumerate(m):
#                 if i == 2:
#                     words = line.split()
#                     all_words += words
#     dictionary = Counter(all_words)
#     # print(dictionary)
#     list_to_remove = list(dictionary.keys())
#     # print(list_to_remove)
#     for item in list_to_remove:
#         if item.isalpha() == False:
#             del dictionary[item]
#         elif len(item) == 1:
#             del dictionary[item]
#     dictionary = dictionary.most_common(3000)
#     return dictionary
#
#
# train_dir = 'E:\\document\\python\\spam\\train-mails'
# dictionary = make_Dictionary(train_dir)
# print(dictionary)

# print(1)
#
# print(2)
# raise ValueError

# file = open("filename.txt", "r")
# print(file.read(16))
# print(file.read(4))
# print(file.read(4))
# print(file.read())
# file.close()

# file = open("filename.txt", "r")
# print(file.readlines())
# file.close()

# file = open("filename.txt", "r")
#
# for line in file:
#     print(line)
#     # print("\n")
#
# file.close()
# print("spam, eggs, ham".split(", "))


# print(round(9.23551,2))
# filename = input("Enter a filename: ")
#
# with open(filename) as f:
#    text = f.read()
#
# print(text)


# nums = [11, 22, 33, 44, 55]
#
# result = map(lambda x: x+5, nums)
# print(result)
# def decor(func):
#   def wrap():
#     print("============")
#     func()
#     print("============")
#   return wrap
#
# def print_text():
#   print("Hello world!")
#
# # decorated = decor(print_text)
# # decorated()
#
# print_text = decor(print_text)
# print_text()
#
# from itertools import product, permutations
#
# letters = ("A", "B", "C")
# print(list(product(letters, range(2))))
# print(list(permutations(letters)))

# class Vector2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#   def __add__(self, other):
#     return Vector2D(self.x + other.x, self.y + other.y)
#
# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first + second
# print(result.x)
# print

# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings
#
#   @staticmethod
#   def validate_topping(topping):
#     if topping == "pineapple":
#       raise ValueError("No pineapples!")
#     else:
#       return True
#
# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#   pizza = Pizza(ingredients)

# def get_input():
#   command = input(": ").split()
#   verb_word = command[0]
#   if verb_word in verb_dict:
#     verb = verb_dict[verb_word]
#     print(verb)
#   else:
#     print("Unknown verb {}". format(verb_word))
#     return
#   print(type(verb))

#   if len(command) >= 2:
#     noun_word = command[1]
#     print (verb(noun_word))
#   else:
#     print(verb("nothing"))
#
# def say(noun):
#   return 'You said "{}"'.format(noun)
#
# verb_dict = {
#   "say": say,
# }
#
# while True:
#   get_input()
#

# import re
#
# pattern = r"^gr.y$"
#
# if re.match(pattern, "grwy"):
#    print("Match 1")
#
# if re.match(pattern, "gray"):
#    print("Match 2")
#
# if re.match(pattern, "stingray"):
#    print("Match 3")

# import re
#
# pattern = r"[A-Z][a-z][0-9]"
#
# if re.search(pattern, "Las3"):
#    print("Match 1")
#
# if re.search(pattern, "SES3"):
#    print("Match 2")
#
# if re.search(pattern, "1ab"):
#    print("Match 3")
#

# import this
# for i in range(10):
#   try:
#     if 10 / i == 2.0:
#       break
#   except ZeroDivisionError:
#     print(1)
# else:
#     print(2)
#




# for i in range(10):
#
#     if i==0:
#       break
#
# else:
#     print(2)#正常执行才触发else

# import logging
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

# import logging

# create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

# def do_install(pkgs):
#     try:
#         # import pip
#         try:
#             from pip._internal import main
#         except Exception:
#             from pip import main
#     except ImportError:
#         error_no_pip()
#     return main(['install'] + pkgs)
#
#
# def do_uninstall(pkgs):
#     try:
#         # import pip
#         try:
#             from pip._internal import main
#         except Exception:
#             from pip import main
#     except ImportError:
#         error_no_pip()
#     return main(['uninstall', '-y'] + pkgs)


# a=input()
# print("it is " + a)
#
# import pandas as pd
# train_data='E:\\courseware\\zhao\\final\\transaction1.csv'
# data1=pd.read_csv(train_data, quoting=3)
# # print( data1.head(5))
# a="0xb9b4cfe4194d7e8511aa9b9f1260bc7b9634249e"
# sum1=0
# for a in data1:
#      sum1=sum1+1
#
# print(sum1)
# import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
# a=~-10
# print(a)

# class Node(object):
#     """创建一个节点"""
#     def __init__(self):
#         self.__elem = 100
#         self.next = None
# n=Node()
# a=n._Node__elem
# print(a)

# import temp as tf
# c=tf.a
# print(c)


# a = list(range(9))
# print(a)
# import numpy as np
# li = [1,2,3,4,5,6]
# Li = np.array(li)
# print(Li)
# type(Li)

# import matplotlib.pyplot as plt
#
# a = [1,2,3,4,5]
# b = [4,5,6,8,9]

# plt.plot(a, b, 'r', label='original data',markersize = 10)
# plt.plot(a, b,label='haha',markersize=10)
# plt.show()
# help(plt)
# import numpy as np
# li = np.ones(5)
# Li = li/2.0
# aa = li * Li
# print(aa)
# print(Li)
# type(li)

# len("asd")
# import numpy as np
# li = np.array([1,2,3,4])
# l = np.array([1,2,3,4])
# # b = li * l
# # a = np.mat(li).transpose()
# # b = a.transpose()
# # print(a, b)
# a = np.ones((4,1))
# b = li * a
# print(type(a), type(li), b)

# aa= np.zeros((1,8))
# bb=np.ones((3,8))
# li = np.append(li,l,axis = 0)
# print(li)
# DNA_SIZE = 10
# aa = np.arange(DNA_SIZE)[::-1]
# pop = np.random.randint(2, size=(100, 10))
# bb = 2 ** np.arange(DNA_SIZE)[::-1]
# cc = pop.dot(aa)
# print(aa, bb, cc)
#
#
# a = 1000
# b = 1000
# c = a
# id(a)
# id(b)
# print(a is c)
import numpy as np
import matplotlib.pyplot as plt
# xMat = np.mat([[1,2,4],[3,4,2]])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([0,1], [1,2], 'b--')
plt.show()



