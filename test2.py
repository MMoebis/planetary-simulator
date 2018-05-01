import numpy as np
import matplotlib.pyplot as plt
ex = np.linspace(0, 2 * np.pi, 50, endpoint=True)
F = np.sin(ex)
plt.plot(ex,F)
startx, endx = -0.1, 2*np.pi + 0.1
starty, endy = -1.1, 1.1
plt.axis([startx, endx, starty, endy])
plt.show()