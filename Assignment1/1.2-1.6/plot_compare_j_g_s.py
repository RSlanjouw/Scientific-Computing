# makes 4 vertical subplots with the data from comparison
import numpy as np
import matplotlib.pyplot as plt
from modules.error_analytical import analytical_solution
# Load the data
x = np.load("data/x_values.npy")
y_J = np.load("data/y_values_J.npy")
y_G = np.load("data/y_values_G.npy")
y_S = np.load("data/y_values_S.npy")
dt_ = np.load("data/dt_values.npy")
frames_to_save = np.load("data/frames_to_save.npy")

# Plot the data
fig, axs = plt.subplots(4, 1, figsize=(8, 8))
for i in range(4):
    axs[i].plot(x, y_J[i], label="Jacobi")
    axs[i].plot(x, y_G[i], label="Gauss-Seidel")
    axs[i].plot(x, y_S[i], label="SOR")
    axs[i].plot(x, analytical_solution(x, dt_[i], 1), label="Analytical")
    axs[i].legend()
    axs[i].set_title(f"Time: {dt_[i]:.3f}")
    axs[i].set_xlabel("Position")
    axs[i].set_ylabel("Concentration")
    # make lim x 0-1
    axs[i].set_xlim(0, 1)
    # make lim y 0-1
    axs[i].set_ylim(0, 1)
    axs[i].grid()
plt.tight_layout()
plt.show()