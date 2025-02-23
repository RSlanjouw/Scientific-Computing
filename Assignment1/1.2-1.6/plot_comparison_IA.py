# Name: compare_j_g_s_analytic.py
# Makes a plot comparing the numerical discrete solutions to the analytical solution
import numpy as np
import matplotlib.pyplot as plt
from modules.functions import TIDE_Eq, Gauss_Eq, SOR_Eq
from modules.error_analytical import analytical_solution

def generate():
    #initialize the matrix
    n = 50
    matrix = np.zeros((n,n))
    matrix[0] = 1
    matrix[-1] = 0
    dx = 1/n
    dt = (dx**2)/4
    time = 1
    frames_to_save = [10, 100, 1000, 10000]
    y_J = []
    y_G = []
    y_S = []
    y_S2 = [] 
    x = np.linspace(0, 1, n)
    dt_ = []

    matrix2 = np.copy(matrix)
    matrix3 = np.copy(matrix)
    matrix4 = np.copy(matrix)

    #run the diffusion while saving our four cases
    for i in range(10001):
        matrix = TIDE_Eq(matrix)
        matrix2 = Gauss_Eq(matrix2)
        matrix3 = SOR_Eq(matrix3)
        matrix4 = SOR_Eq(matrix4, 1.8)
        if i in frames_to_save:
            y_J.append(matrix[::-1, 0])
            y_G.append(matrix2[::-1, 0])
            y_S.append(matrix3[::-1, 0])
            y_S2.append(matrix4[::-1, 0])
            dt_.append(dt * i)

    #save the resulting data
    np.save("data/x_values.npy", x)
    np.save("data/y_values_J.npy", y_J)
    np.save("data/y_values_G.npy", y_G)
    np.save("data/y_values_S.npy", y_S)
    np.save("data/y_values_S2.npy", y_S2)
    np.save("data/dt_values.npy", dt_)
    np.save("data/frames_to_save.npy", frames_to_save)


try: 
    x = np.load("data/x_values.npy")
    y_J = np.load("data/y_values_J.npy")
    y_G = np.load("data/y_values_G.npy")
    y_S = np.load("data/y_values_S.npy")
    y_S2 = np.load("data/y_values_S2.npy")
    dt_ = np.load("data/dt_values.npy")
except FileNotFoundError:
    generate()
    x = np.load("data/x_values.npy")
    y_J = np.load("data/y_values_J.npy")
    y_G = np.load("data/y_values_G.npy")
    y_S = np.load("data/y_values_S.npy")
    y_S2 = np.load("data/y_values_S2.npy")
    dt_ = np.load("data/dt_values.npy")

D = 1

fig, axs = plt.subplots(4, 1, figsize=(6, 8))
for i in range(4):
    print(dt_[i]/ 0.0001)
    axs[i].plot(x, y_J[i], label="Jacobi", linestyle='--', marker='s', markersize=3)
    axs[i].plot(x, y_G[i], label="Gauss-Seidel", linestyle='--', marker='x', markersize=3)
    axs[i].plot(x, y_S[i], label=f"SOR, $\omega$ = 1.5", linestyle='--', marker='^', markersize=3)
    axs[i].plot(x, y_S2[i], label=f"SOR, $\omega$ = 1.8", linestyle='--', marker='o', markersize=3)
    axs[i].plot(x, analytical_solution(x, dt_[i] / 0.0001, 1), label="Analytical")
    axs[i].legend(fontsize='small')
    axs[i].set_title(f"Time: {dt_[i]:.3f}")
    axs[i].set_xlabel("Y-position")
    axs[i].set_ylabel("Concentration")
    axs[i].set_xlim(0, 1)
    axs[i].set_ylim(0, 1)
    axs[i].grid()
plt.tight_layout()
# plt.savefig("plots/compare_j_g_s_analytic.png")
plt.show()


