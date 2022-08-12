# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,0.01)
y=np.sin(x)
#
plt.xlim((-10,10))
new_ticks=np.linspace(-10,10,21)
print(new_ticks)
plt.xticks(new_ticks)
plt.plot(x,y)
plt.show()