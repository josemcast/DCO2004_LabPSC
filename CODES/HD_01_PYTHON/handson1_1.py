import numpy as np
Am = 1.0
fm = 60
ka=1.0
u =ka*Am
Ac = 2.0
t = np.linspace(0,1000,1000)
fc = 70
m_t = Am*np.cos(2*np.pi*fm*t)
s_t = Ac*(1+u*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*t*fc)
from matplotlib import pyplot as plt
plt.plot(t,s_t)
plt.show()