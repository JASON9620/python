# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series

d1 = {"城市": ["北京", "上海", "广州", "深圳"],
      "环比": [0.1, 0.2, 0.3, 0.4],
      "同比": [0.6, 0.5, 0.2, 0.3],
      "人口": [5, 3, 7, 2]}
d = pd.DataFrame(d1, index=['c1', 'c2', 'c3', 'c4'])
d = d.reindex(columns=["城市", "人口", "同比", "环比"])
newc = d.columns.insert(4, "新增")  #4表示插入的列号
newd = d.reindex(columns=newc, fill_value=200)
nc = d.columns.delete(2)
ni = d.index.insert(5, "c5")
nd = d.reindex(index=ni, columns=nc).ffill()  #ffill前向填充，bfill后向填充
d.drop("人口", axis=1)  #使用drop删除0轴和1轴上的元素

a = pd.DataFrame(np.arange(20).reshape(4, 5))
b = pd.DataFrame(np.arange(12).reshape(3, 4))
a.add(b, fill_value=10)
a.mul(b, fill_value=1)
#a与b相乘，索引缺失的项，用NaN填充，使用fill_value可替代NaN

c = pd.Series(np.arange(4))
a-c
a.sub(c, axis=0)



