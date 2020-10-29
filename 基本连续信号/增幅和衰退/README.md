# 复指数 基本信号显示

## 目的
通过编写基本程序，实现信号的显示。
## 代码
```
# -*- coding: UTF-8 -*-
#coding=utf-8

  
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 1000)
plt.subplot(211)
f = np.exp(5/4*t)*np.cos((np.pi)*4*t)
plt.title(u'5/4')
plt.plot(t, f)
plt.subplot(212)
f = np.exp(-5/4*t)*np.cos((np.pi)*4*t)
plt.title(u'-5/4')
plt.plot(t, f)

plt.show()
```

## 图形
根据上述代码，最终显示的图形如下所示。
<center>
  <img src="https://github.com/lkmnlkmn/lkmnlkmn.github.io/blob/main/%E5%9F%BA%E6%9C%AC%E8%BF%9E%E7%BB%AD%E4%BF%A1%E5%8F%B7/%E5%A2%9E%E5%B9%85%E5%92%8C%E8%A1%B0%E9%80%80/%E5%9B%BE%E7%89%875.png" > 
  图复指数 
</center>
