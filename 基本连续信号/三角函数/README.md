# exp 基本信号显示

## 目的
通过编写基本程序，实现信号的显示。
## 代码
```
# -*- coding: UTF-8 -*-
#coding=utf-8

import numpy as np
from matplotlib import pyplot as plt


x = np.linspace((-np.pi)*2, np.pi*2, 50, endpoint=True)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1, c='g', marker='s', label='sin(x)')
plt.plot(x, y2, c='r', marker='o', label='con(x)')
plt.legend(loc='upper left', numpoints=2,)
plt.show()
```

## 图形
根据上述代码，最终显示的图形如下所示。
<center>
  <img src="https://github.com/lkmnlkmn/lkmnlkmn.github.io/blob/main/%E5%9F%BA%E6%9C%AC%E8%BF%9E%E7%BB%AD%E4%BF%A1%E5%8F%B7/%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0/%E5%9B%BE%E7%89%874.png" > 
  图exp 
</center>
