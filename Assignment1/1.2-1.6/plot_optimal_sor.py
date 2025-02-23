# plot the optimal sor
import numpy as np
import matplotlib.pyplot as plt
from modules.functions import SOR_Eq_TOL
from scipy.optimize import minimize_scalar

# load the data
def generate():
        
    #initialize the matrix
    n = [10,30,50,100,200]
    iterations = []
    tol = 10**-5
    lb = 1
    for i in n:
        matrix = np.zeros((i, i))
        matrix[0] = 1
        matrix[-1] = 0
        # use scipy's minimize_scalar method to find the optimal omega for a certain n

        def f(omega):
            return SOR_Eq_TOL(matrix, tol, omega)
        
        result = minimize_scalar(f, bounds=(1, 2), method='bounded', options={'xatol': 1e-3})
        omega = result.x
        print(omega)
        lb = omega
        iterations.append(result.fun)

    # save the data
    np.save("data/n_values.npy", n)
    np.save("data/iterations_optimal.npy", iterations)

try: 
    n_values = np.load("data/n_values.npy")
    iterations = np.load("data/iterations_optimal.npy")

except FileNotFoundError:
    generate()
    n_values = np.load("data/n_values.npy")
    iterations = np.load("data/iterations_optimal.npy")

plt.plot(n_values, iterations, linestyle="-", marker="o")
plt.xlabel("Matrix size")
plt.ylabel("Iterations")
plt.title("Optimal omega for different matrix sizes")
plt.show()

