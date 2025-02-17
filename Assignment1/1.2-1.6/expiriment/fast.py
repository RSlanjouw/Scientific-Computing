# Name: fast.py
# This file contains the fast numpy functions which are not handy to be used when plotting. 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

y_top= 1
y_bottom = 0
y_left = y_right = 0
step_t = 1/4.1
step_x = 1/1

def initialize_matrix(n):
    matrix = np.zeros((n,n))
    matrix[0] = 1
    return matrix

def next_time_step(matrix, step_t, step_x, d):
    """
    Calculate the next time step of the matrix with Numpy vectorization.
    Thought it would reduce the complexity but seems to be the same, just faster c pointers. (O(n^2)) 
    """
    matrix_next = np.zeros(matrix.shape)
    matrix_next[0] = matrix[0]
    constant = d * step_t / (step_x**2)
    matrix_next[-1] = matrix[-1]
    matrix_next[1:-1, 1:-1] = matrix[1:-1, 1:-1] + constant * (matrix[2:, 1:-1] + matrix[:-2, 1:-1] + matrix[1:-1, 2:] + matrix[1:-1, :-2] - 4 * matrix[1:-1, 1:-1])
    matrix_next[1:-1, 0] = matrix[1:-1, 0] + constant * (matrix[2:, 0] + matrix[:-2, 0] + matrix[1:-1, 1] + matrix[1:-1, -2] - 4 * matrix[1:-1, 0])
    matrix_next[1:-1, -1] = matrix_next[1:-1, 0]
    return matrix_next


# plot the matrix next with update function in animate
def update(frame):
    global matrix
    matrix = next_time_step(matrix, step_t, step_x, 1)
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    return matrix


fig, ax = plt.subplots()
#initialize the matrix
matrix = initialize_matrix(10)
ani = FuncAnimation(fig, update, frames=1000, interval=1, blit=False)

plt.show()
