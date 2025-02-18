# Name: compare_j_g_s_analytic.py
# Makes a plot comparing the numerical discrete solutions to the analytical solution
import numpy as np
import matplotlib.pyplot as plt
from modules.functions import TIDE_Eq, Gauss_Eq, SOR_Eq
from modules.error_analytical import analytical_solution

#initialize the matrix
n = 50
matrix = np.zeros((n,n))
matrix[0] = 1
matrix[-1] = 0
D = 1
dx = 1/n
dt = (dx**2)/4
time = 1
frames_to_save = [10, 100, 1000, 10000]
y_J = []
y_G = []
y_S = []
x = np.linspace(0, 1, n)
dt_ = []

matrix2 = np.copy(matrix)
matrix3 = np.copy(matrix)


#run the diffusion while saving our four cases
for i in range(10001):
    matrix = TIDE_Eq(matrix)
    matrix2 = Gauss_Eq(matrix2)
    matrix3 = SOR_Eq(matrix3)
    if i in frames_to_save:
        y_J.append(matrix[::-1, 0])
        y_G.append(matrix2[::-1, 0])
        y_S.append(matrix3[::-1, 0])
        dt_.append(dt * i)

#save the resulting data
np.save("data/x_values.npy", x)
np.save("data/y_values_J.npy", y_J)
np.save("data/y_values_G.npy", y_G)
np.save("data/y_values_S.npy", y_S)
np.save("data/dt_values.npy", dt_)
np.save("data/frames_to_save.npy", frames_to_save)

#plot the results
for i in range(4):
    plt.plot(x, y_J[i], label="Jacobi")
    plt.plot(x, y_G[i], label="Gauss-Seidel")
    plt.plot(x, y_S[i], label="SOR")
    plt.plot(x, analytical_solution(x, dt_[i], D), label="Analytical")
plt.legend()
plt.title("Comparison of numerical and analytical solutions")
plt.xlabel("Position")
plt.ylabel("Concentration")
plt.show()


