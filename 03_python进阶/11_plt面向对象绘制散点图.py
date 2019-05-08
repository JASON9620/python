# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots() #面向对象绘制三点图，且默认plt.subplots(111)
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'ro')
ax.set_title('面向对象绘制散点图', fontproperties='Kaiti', fontsize=20, color='blue')
plt.show()
