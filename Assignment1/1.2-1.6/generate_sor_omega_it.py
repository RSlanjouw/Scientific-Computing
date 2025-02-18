# Name: generate_sor_omega_it.py
# Generates data for the SOR method for different omega values

import numpy as np 
from modules.functions import SOR_Eq_TOL
import matplotlib.pyplot as plt


#initialize the matrix
n = 50
matrix = np.zeros((n,n))
matrix[0] = 1
matrix[-1] = 0
omega_values = np.linspace(0.001, 1.999, 8)
tol = np.linspace(1, 6, 6)
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

for i in range(8):
    plt.plot(tol, iterations[i*6:(i+1)*6], label=f"Omega = {omega_values[i]}")
plt.xlabel("Tolerance")
plt.ylabel("Iterations")
# log
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.title("Iterations needed for different omega values")
plt.show()
