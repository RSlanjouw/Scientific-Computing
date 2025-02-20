# Name: generate_sor_omega_it.py
# Generates data for the SOR method for different omega values

import numpy as np 
from modules.functions import SOR_Eq_TOL
import matplotlib.pyplot as plt


def save_data():
    #initialize the matrix
    n = 50
    matrix = np.zeros((n,n))
    matrix[0] = 1
    matrix[-1] = 0
    omega_values = np.linspace(0.001, 1.999, 8)
    tol = np.linspace(1, 7, 7)
    iterations = []

    # run the SOR method for each omega value
    for omega in omega_values:
        print(omega)
        for t in tol:
            iterations.append(SOR_Eq_TOL(matrix, 10**-t, omega))
    print("DONE")
    # plot the 8 lines
    # save the data
    np.save("data/omega_values.npy", omega_values)
    np.save("data/tol_values.npy", tol)
    np.save("data/iterations.npy", iterations)
    return True

try:
    tol = np.load("data/tol_values.npy")
    iterations = np.load("data/iterations.npy")
    omega_values = np.load("data/omega_values.npy")
except FileNotFoundError:
    save_data()
    tol = np.load("data/tol_values.npy")
    iterations = np.load("data/iterations.npy")
    omega_values = np.load("data/omega_values.npy")



for i in range(8):
    plt.plot(tol, iterations[i*7:(i+1)*7], label=f"Omega = {omega_values[i]}")
plt.xlabel("Tolerance")
plt.ylabel("Iterations")
# log
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.title("Iterations needed for different omega values")
plt.show()
