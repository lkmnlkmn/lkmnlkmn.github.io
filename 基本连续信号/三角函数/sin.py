import numpy as np
from matplotlib import pyplot as plt


x = np.linspace((-np.pi)*2, np.pi*2, 50, endpoint=True)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1, c='g', marker='s', label='sin(x)')
plt.plot(x, y2, c='r', marker='o', label='con(x)')
plt.legend(loc='upper left', numpoints=2,)
plt.show()
