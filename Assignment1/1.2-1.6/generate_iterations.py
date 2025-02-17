from modules.functions import Jacob_Eq_TOL, Gauss_Eq_TOL, SOR_Eq_TOL
import numpy as np
import matplotlib.pyplot as plt

#initialize the matrix
n = 50
matrix = np.zeros((n,n))
matrix[0] = 1
matrix[-1] = 0

# make list of tolerances
tolerances = [10**-i for i in range(1, 6)]
jacob_iterations = []
gauss_iterations = []
sor_iterations = []

# run the three methods for each tolerance
for tol in tolerances:
    jacob_iterations.append(Jacob_Eq_TOL(matrix, tol))
    gauss_iterations.append(Gauss_Eq_TOL(matrix, tol))
    sor_iterations.append(SOR_Eq_TOL(matrix, tol))

# plot the results
plt.plot(tolerances, jacob_iterations, label="Jacobi")
plt.plot(tolerances, gauss_iterations, label="Gauss-Seidel")
plt.plot(tolerances, sor_iterations, label="SOR")
plt.xlabel("Tolerance")
plt.ylabel("Iterations")
plt.legend()
plt.title("Iterations needed for different methods")
plt.show() 