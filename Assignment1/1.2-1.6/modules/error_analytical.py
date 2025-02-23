# Name: error_analytical.py
# Contains the analytical solution for the error function

import numpy as np
from scipy.special import erfc

def analytical_solution(x, t, D, dt=0.0001):
    """X = positions, t = time, D = diffusion coefficient"""
    y = np.zeros_like(x)
    t = t * dt
    for i in range(10):
        y += erfc((1 - x + 2 * i) / (2 * np.sqrt(D * t))) - erfc((1 + x + 2 * i) / (2 * np.sqrt(D * t)))
    return y


def compare_a_e(x,y):
    """Compares the analytical solution to the numerical solution"""
    error = np.abs(y - x)
    error = np.sum(error)
    return error