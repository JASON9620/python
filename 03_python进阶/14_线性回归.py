# -*- coding:utf-8 -*-
"""
 Author:
    Jason Wang
 Github:
    https://github.com/JASON9620
 Time:
    2019/4/18 11:16
 IDE:
    PyCharm
 """
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]
m = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(m, y)[0]
x = np.array(x)
y = np.array(y)

plt.plot(x, y, 'o')
plt.plot(x, a*x+b, 'r')
plt.show()









