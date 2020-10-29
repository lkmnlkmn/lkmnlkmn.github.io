# 矩形信号 基本信号显示

## 目的
通过编写基本程序，实现信号的显示。
## 代码
```
# -*- coding: UTF-8 -*-
#coding=utf-8

  
import numpy as np
import matplotlib.pyplot as plt

def rect_wave(x, c, c0):      
     if x >= (c+c0):
          r = 0.0
     elif x < c0:
          r = 0.0
     else :
          r = 1
     return r


x = np.linspace(-2, 4, 1000)
y = np.array([rect_wave(t, 2.0, -1.0) for t in x])
plt.ylim(-0.2, 1.2)
plt.plot(x, y)
plt.show()

```

## 图形
根据上述代码，最终显示的图形如下所示。
<center>
  <img src="https://github.com/lkmnlkmn/lkmnlkmn.github.io/blob/main/%E5%9F%BA%E6%9C%AC%E8%BF%9E%E7%BB%AD%E4%BF%A1%E5%8F%B7/%E7%9F%A9%E5%BD%A2/%E5%9B%BE%E7%89%873.png" > 
  图矩形信号 
</center>
