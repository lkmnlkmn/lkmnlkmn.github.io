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
