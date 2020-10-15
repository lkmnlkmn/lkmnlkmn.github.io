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
