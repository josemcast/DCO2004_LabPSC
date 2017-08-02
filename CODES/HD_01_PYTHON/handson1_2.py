import numpy as np
inicio = 0
PI = np.pi #3.141592653...
N_termos = 100
t = np.arange(inicio,2*PI,2*PI/N_termos)
cos_t = np.cos(t)
sin_t = np.sin(t)


import matplotlib.pyplot as plt

plt.plot(t,cos_t)
plt.show()
plt.plot(t,sin_t)
plt.show()

