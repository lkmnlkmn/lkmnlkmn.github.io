# exp 基本信号显示

## 目的
通过编写基本程序，实现信号的显示。
## 代码
```
# -*- coding: UTF-8 -*-
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-2.5, 2.5, 1000)
ft = np.exp(-3/4*t)
plt.plot(t, ft)
ft1 = np.exp(3/4*t)
plt.plot(t, ft1)
ft2 = np.exp(0*t)
plt.plot(t, ft2)
plt.title("exp")

plt.show()
```

## 图形
根据上述代码，最终显示的图形如下所示。$f(x)=sin(\omega x)$，其中，$\omega = \frac{3}{8} \pi $。

<center>
  <img src="https://github.com/lkmnlkmn/lkmnlkmn.github.io/blob/main/%E5%9F%BA%E6%9C%AC%E8%BF%9E%E7%BB%AD%E4%BF%A1%E5%8F%B7/exp/%E5%9B%BE%E7%89%871.png" > 
  图exp 
</center>
