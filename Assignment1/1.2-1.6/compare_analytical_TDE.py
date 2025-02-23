# NAME: compare_analytical_TDE.py
# This file compares the analytical solution to the numerical solution of the TTD equation

import numpy as np
from modules.functions import TDDE_Eq
from modules.error_analytical import compare_a_e, analytical_solution
import matplotlib.pyplot as plt

def generate():
    matrix = np.zeros((50,50))
    matrix[0] = 1
    matrix[-1] = 0
    start_matrix = np.copy(matrix)
    # Tim to save is 0,2,4,6,8,10 etc
    time_to_save = [i for i in range(0, 10001, 2)]
    y = []
    error = []
    dx = 1/50
    dt = (dx**2)/4


    for i in range(int(1/dt)):
        matrix = TDDE_Eq(matrix, dt, dx, 1)
        if i in time_to_save:
            x = np.linspace(0, 1, 50)
            an = analytical_solution(x, i,1)
            # print(an[20,20])
            e = compare_a_e(an, matrix[::-1, 0])
            print(e)
            error.append(e)
            y.append(matrix[::-1, 0])
    np.save("data/y_values3.npy", y)
    np.save("data/error.npy", error)
    np.save("data/x_values3.npy", dx)
    np.save("data/time_to_save3.npy", time_to_save)

try:
    # plot the results
    y = np.load("data/y_values3.npy")
    error = np.load("data/error.npy")
    dx = np.load("data/x_values3.npy")
    time_to_save = np.load("data/time_to_save3.npy")

except FileNotFoundError:   
    generate()
    y = np.load("data/y_values3.npy")
    error = np.load("data/error.npy")
    dx = np.load("data/x_values3.npy")
    time_to_save = np.load("data/time_to_save3.npy")

plt.figure(figsize=(8, 6))
color = ["blue", "red", "green", "purple", "yellow"]
# print error
# print(len(error))
# print(error.shape)
# print(time_to_save.shape)
plt.plot(time_to_save[:5000] * 0.0002, error, label="Error", linestyle="-")
plt.xlabel("y values")
plt.title("Absolute error")
plt.grid()
plt.ylabel("concentration")
plt.legend()
# plt.xlim(0, 1)

plt.show()
# get max error in np array
# error = np.array(error[1:])
# print(error)
# # get max error
# print(max(error))
# # get index
# print(477 * 0.0001)
# print(error[])