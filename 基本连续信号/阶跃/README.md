# exp 基本信号显示

## 目的
通过编写基本程序，实现信号的显示。
## 代码
```
# -*- coding: UTF-8 -*-
#coding=utf-8

# 定义阶跃信号
import numpy as np
import matplotlib.pyplot as plt
def unit(t):
     r = np.where(t > 0.0, 1.0, 0.0)
     return r 
t = np.linspace(-1.0, 3.0, 1000)
plt.ylim(-1.0, 3.0)
plt.plot(t, unit(t))

plt.show()

```

## 图形
根据上述代码，最终显示的图形如下所示。
<center>
  <img src="https://github.com/lkmnlkmn/lkmnlkmn.github.io/blob/main/%E5%9F%BA%E6%9C%AC%E8%BF%9E%E7%BB%AD%E4%BF%A1%E5%8F%B7/%E9%98%B6%E8%B7%83/%E5%9B%BE%E7%89%872.png" > 
  图exp 
</center>
