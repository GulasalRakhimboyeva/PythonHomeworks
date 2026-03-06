import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plots

# ============================================================
# 1. Basic Plotting: f(x) = x^2 - 4x + 4
# ============================================================

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.grid(True)
plt.show()


# ============================================================
# 2. Sine and Cosine Plot
# ============================================================

x = np.linspace(0, 2*np.pi, 400)

plt.figure()
plt.plot(x, np.sin(x), linestyle='-', marker='o', label='sin(x)')
plt.plot(x, np.cos(x), linestyle='--', marker='x', label='cos(x)')
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid(True)
plt.show()


import csv
