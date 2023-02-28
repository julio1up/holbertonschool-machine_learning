#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0, 11) ** 3

plt.plot(y, color = "red")
plt.xlim(0, 10)
plt.show()
