import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plots

# ============================================================
# 1. Basic Plotting: f(x) = x^2 - 4x + 4
# ============================================================

x = np.linspace(-10, 10, 20)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y,  'r--o', label="f(x)",)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.legend()
plt.grid(True)
plt.show()
