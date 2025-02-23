# Name: sink_calculate.py
# calculate the amount of iterations needed for the sink

import numpy as np
from modules.functions import SOR_Eq_TOL, Jacob_Eq_TOL, Gauss_Eq_TOL
from scipy.optimize import minimize_scalar

grid = np.zeros((50,50))
grid[0] = 1
grid[-1] = 0
mask_base = np.ones((50,50))
mask_1 = np.copy(mask_base)
mask_1[22:28, 22:28] = 0
mask_2 = np.copy(mask_base)
mask_2[15:35, 15:35] = 0
mask_3 = np.copy(mask_base)
mask_3[10:15, 10:15] = 0
mask_3[35:40, 35:40] = 0
mask_i1 = np.copy(mask_base)
mask_i1[22:28, 22:28] = 0.95
mask_i2 = np.copy(mask_base)
mask_i2[15:35, 15:35] = 0.95
mask_i3 = np.copy(mask_base)
mask_i3[10:15, 10:15] = 0.95
mask_i3[35:40, 35:40] = 0.95



def calculate_min_omega(matrix, tol,mask):
    def f(omega):
        return SOR_Eq_TOL(matrix, tol, omega, mask=mask)
    
    result = minimize_scalar(f, bounds=(1, 2), method='bounded', options={'xatol': 1e-3})
    return result.x


print("\textbf{Jacobi} & \textbf{Gauss-Seidel} & \textbf{SOR $\omega$ = 1.8} & \textbf{Optimal $\omega$} \\")
for mask in [mask_base, mask_1, mask_2, mask_3, mask_i1, mask_i2, mask_i3]:
    jacobi = Jacob_Eq_TOL(grid, 10**-7, mask=mask)
    gauss = Gauss_Eq_TOL(grid, 10**-7, mask=mask)
    sor = SOR_Eq_TOL(grid, 10**-7, 1.8, mask=mask)
    optimal_omega = calculate_min_omega(grid, 10**-7, mask)
    Sor_optimal = SOR_Eq_TOL(grid, 10**-7, optimal_omega, mask=mask)
    print(f"Sinkhole . & {jacobi} & {gauss} & {sor} & {optimal_omega}& {Sor_optimal} \\ \hline")