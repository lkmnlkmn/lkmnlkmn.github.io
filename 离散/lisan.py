import numpy as np
import matplotlib.pyplot as plt
n = np.arange(0, 15)
a = 3/4
f = a**n
plt.subplot(221)
plt.title('a=3/4')
plt.stem(n, f)
a = -3/4
f = a**n
plt.subplot(222)
plt.title('a=-3/4')
plt.stem(n, f)
a = 5/4
f = a**n
plt.subplot(223)
plt.title('a=5/4')
plt.stem(n, f)
a = -5/4
f = a**n
plt.subplot(224)
plt.title('a=-5/4')
plt.stem(n, f)
plt.show()
