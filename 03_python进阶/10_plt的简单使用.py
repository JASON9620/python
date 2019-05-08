# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.rcParams['font.family'] = 'Kaiti'
# matplotlib.rcParams['font.size'] = 15    #修改全局中文的字体属性和大小
# plt.subplot(234)     #创建子图
plt.ylabel('随机值', fontproperties='Kaiti', fontsize=10, color='red')
plt.xlabel('整数值', fontproperties='SimHei', fontsize=15) #对有中文出现的地方进行局部修改，推荐使用
plt.title(r'瞎鸡儿编 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=15)
plt.axis([0,10,0,8])
plt.plot([2,3,4,5,6],[3,4,7,2,1],'r:o')
plt.grid(True)
plt.annotate(r'$\mu =100', xy=(2, 5), xytext=(3, 6),
             arrowprops=dict(facecolor='green', shrink=0.1, width=5))
#网格和箭头配合使用
# plt.savefig('test',dpi=800)  #png文件
plt.show()
