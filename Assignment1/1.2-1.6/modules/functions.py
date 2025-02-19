# Name: functions.py
# Has the different equations for this exercise

import numpy as np

def TTD_Eq(matrix, dt, dx, D):
    cons = dt*D/(dx**2)
    if cons > 1:
        return r"Unstable"
    else:
        n = len(matrix)
        next_matrix = np.copy(matrix)
        
        for j in range (1, n-1):
            next_matrix[j,0] = matrix[j,0] + cons * (matrix[j,1] + \
            matrix[j,-2] + matrix[j+1,0] + matrix[j-1,0] - 4 * matrix[j,0])            
            for i in range (1, n-1):
                next_matrix[j,i] = matrix[j,i] + cons * (matrix[j,i+1] + \
                matrix[j,i-1] + matrix[j+1,i] + matrix[j-1,i] - 4 * matrix[j,i])
            next_matrix[j,-1] = next_matrix[j,0]
        return next_matrix
    

def TIDE_Eq(matrix, mask=None):
    new_matrix = np.copy(matrix)
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            new_matrix[i,j] = (matrix[i+1,j] + matrix[i-1,j] + matrix[i,j+1] + matrix[i,j-1])/4
        new_matrix[i,0] = (matrix[i-1,0] + matrix[i+1,0] + matrix[i,1] + matrix[i,-2]) / 4
        new_matrix[i,-1] = new_matrix[i,0]
    return new_matrix

def Gauss_Eq(matrix, mask=None): 
    new_matrix = np.copy(matrix)
    if mask is None:
        mask = np.ones_like(matrix)
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            if mask[i, j] != 0:
                new_matrix[i,j] = mask[i, j] * (new_matrix[i+1,j] + new_matrix[i-1,j] + new_matrix[i,j+1] + new_matrix[i,j-1])/4
        if mask[i, 0] != 0:
            new_matrix[i,0] = mask[i, 0] * (new_matrix[i-1,0] + new_matrix[i+1,0] + new_matrix[i,1] + new_matrix[i,-2]) / 4
        new_matrix[i,-1] = new_matrix[i,0]
    return new_matrix

def SOR_Eq(matrix, omega=1.5):
    new_matrix = np.copy(matrix)
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            new_matrix[i,j] = (1-omega) * matrix[i,j] + omega * (new_matrix[i+1,j] + new_matrix[i-1,j] + new_matrix[i,j+1] + new_matrix[i,j-1])/4
        new_matrix[i,0] = (1-omega) * matrix[i,0] + omega * (new_matrix[i-1,0] + new_matrix[i+1,0] + new_matrix[i,1] + new_matrix[i,-2]) / 4
        new_matrix[i,-1] = new_matrix[i,0]
    return new_matrix


def Jacob_Eq_TOL(matrix, tol):
    error = tol + 1
    iterations = 0
    while error > tol and iterations < 10**8:
        iterations += 1
        new_matrix = np.copy(matrix)
        for i in range(1, len(matrix)-1):
            for j in range(1, len(matrix)-1):
                new_matrix[i,j] = (matrix[i+1,j] + matrix[i-1,j] + matrix[i,j+1] + matrix[i,j-1])/4
            new_matrix[i,0] = (matrix[i-1,0] + matrix[i+1,0] + matrix[i,1] + matrix[i,-2]) / 4
            new_matrix[i,-1] = new_matrix[i,0]
        error = np.max(np.abs(matrix - new_matrix))
        matrix = new_matrix
    if iterations == 10**8:
        return None
    return iterations

def Gauss_Eq_TOL(matrix, tol):
    error = tol + 1
    iterations = 0
    while error > tol and iterations < 10**8:
        iterations += 1
        new_matrix = np.copy(matrix)
        for i in range(1, len(matrix)-1):
            for j in range(1, len(matrix)-1):
                new_matrix[i,j] = (new_matrix[i+1,j] + new_matrix[i-1,j] + new_matrix[i,j+1] + new_matrix[i,j-1])/4
            new_matrix[i,0] = (new_matrix[i-1,0] + new_matrix[i+1,0] + new_matrix[i,1] + new_matrix[i,-2]) / 4
            new_matrix[i,-1] = new_matrix[i,0]
        error = np.max(np.abs(matrix - new_matrix))
        matrix = new_matrix
    if iterations == 10**8:
        return None
    return iterations


def SOR_Eq_TOL(matrix, tol, omega=1.5):
    error = tol + 1
    iterations = 0
    while error > tol and iterations < 10**8:
        iterations += 1
        new_matrix = np.copy(matrix)
        for i in range(1, len(matrix)-1):
            for j in range(1, len(matrix)-1):
                new_matrix[i,j] = (1-omega) * matrix[i,j] + omega * (new_matrix[i+1,j] + new_matrix[i-1,j] + new_matrix[i,j+1] + new_matrix[i,j-1])/4
            new_matrix[i,0] = (1-omega) * matrix[i,0] + omega * (new_matrix[i-1,0] + new_matrix[i+1,0] + new_matrix[i,1] + new_matrix[i,-2]) / 4
            new_matrix[i,-1] = new_matrix[i,0]
        error = np.max(np.abs(matrix - new_matrix))
        matrix = new_matrix
    if iterations == 10**8:
        return None
    return iterations