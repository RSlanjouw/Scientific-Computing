# Name: error_analytical.py
# Contains the analytical solution for the error function

import numpy as np
from scipy.special import erfc

def analytical_solution(x, t, D):
    """X = positions, t = time, D = diffusion coefficient"""
    sum_term = np.zeros_like(x)
    for i in range(10):  # Amount of iterations, in formula it is infinite but fuck that 1mil is enough, felt like it.
        sum_term += erfc((1 - x + 2 * i) / np.sqrt(2 * D * t)) - erfc((1 + x + 2 * i) / np.sqrt(2 * D * t))
    return sum_term