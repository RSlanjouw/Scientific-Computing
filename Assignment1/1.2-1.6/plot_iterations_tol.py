from modules.functions import Jacob_Eq_TOL, Gauss_Eq_TOL, SOR_Eq_TOL
import numpy as np
import matplotlib.pyplot as plt


def generate():
    #initialize the matrix
    n = 50
    matrix = np.zeros((n,n))
    matrix[0] = 1
    matrix[-1] = 0

    # make list of tolerances
    tolerances = [10**-i for i in range(1, 8)]
    jacob_iterations = []
    gauss_iterations = []
    sor_iterations = []
    sor2_iterations = []

    # run the three methods for each tolerance
    for tol in tolerances:
        jacob_iterations.append(Jacob_Eq_TOL(matrix, tol))
        gauss_iterations.append(Gauss_Eq_TOL(matrix, tol))
        sor_iterations.append(SOR_Eq_TOL(matrix, tol))
        sor2_iterations.append(SOR_Eq_TOL(matrix, tol, 1.8))

    # save the data
    np.save("data/tolerances1.npy", tolerances)
    np.save("data/jacob_iterations1.npy", jacob_iterations)
    np.save("data/gauss_iterations1.npy", gauss_iterations)
    np.save("data/sor_iterations1.npy", sor_iterations)
    np.save("data/sor2_iterations1.npy", sor2_iterations)

try:
    tolerances = np.load("data/tolerances1.npy")
    jacob_iterations = np.load("data/jacob_iterations1.npy")
    gauss_iterations = np.load("data/gauss_iterations1.npy")
    sor_iterations = np.load("data/sor_iterations1.npy")
    sor2_iterations = np.load("data/sor2_iterations1.npy")
except FileNotFoundError:
    generate()
    tolerances = np.load("data/tolerances1.npy")
    jacob_iterations = np.load("data/jacob_iterations1.npy")
    gauss_iterations = np.load("data/gauss_iterations1.npy")
    sor_iterations = np.load("data/sor_iterations1.npy")
    sor2_iterations = np.load("data/sor2_iterations1.npy")

# plot the results
l = np.linspace(1,7,7)


plt.plot(l, jacob_iterations, label="Jacobi", linestyle="--", marker="o")
plt.plot(l, gauss_iterations, label="Gauss-Seidel", linestyle="--", marker="o")
plt.plot(l, sor_iterations, label=r"SOR $\omega$ = 1.5", linestyle="--", marker="x")
plt.plot(l, sor2_iterations, label=r"SOR $\omega$ = 1.8", linestyle="--", marker="^")
plt.xlabel("Tolerance ($10^{-i}$)")
# plt.yscale("log")
# plt.xscale("log")
# make x axis only discrete values
plt.xticks(l, [f"{i}" for i in l])
plt.ylabel("Iterations")
plt.legend()
plt.grid()
plt.xlim(2, 7)
plt.title("Comparison in efficiency of different iteration methods")
# plt.savefig("plots/compare_iterations.png")
plt.show()