import numpy as np
import matplotlib.pyplot as plt

y_top= 1
y_bottom = 0
y_left = y_right = 0
step_t = 1/4.1
step_x = 1/1

#function to initialize the nxn matrix with only first line being 1 and rest 0
def initialize_matrix(n):
    matrix = np.zeros((n,n))
    matrix[0] = 1
    return matrix

#function to calculate the next time step, c(y=1)=1, c(y=0)=0, c(x=0,y)=c(x=1.y)
def next_time_step(matrix, step_t, step_x, d):
    #numpy function to calculate the next time step
    matrix_next = np.zeros(matrix.shape)
    matrix_next[0] = matrix[0]
    constant = d * step_t / (step_x**2)
    matrix_next[-1] = matrix[-1]
    # formula is c + constant * (c[i+1] + c[i-1] + c[j+1] + c[j-1] - 4c[i,j])
    # at the borders we are using the periodic boundary condition
    matrix_next[1:-1, 1:-1] = matrix[1:-1, 1:-1] + constant * (matrix[2:, 1:-1] + matrix[:-2, 1:-1] + matrix[1:-1, 2:] + matrix[1:-1, :-2] - 4 * matrix[1:-1, 1:-1])
    # at the borders we are using th esame formula but with the periodic boundary condition so c+ constant * (c[i+1] + c[i-1] + c[j+1] + c[j-1] - 4c[i,j])
    matrix_next[1:-1, 0] = matrix[1:-1, 0] + constant * (matrix[2:, 0] + matrix[:-2, 0] + matrix[1:-1, 1] + matrix[1:-1, -1] - 4 * matrix[1:-1, 0])
    matrix_next[1:-1, -1] = matrix_next[1:-1, 0]
    return matrix_next

# plot the matrix next with update function in animate
def update(frame):
    global matrix
    matrix = next_time_step(matrix, step_t, step_x, 1)
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    return matrix

from matplotlib.animation import FuncAnimation


print(4 * step_t / (step_x**2))
#initialize the matrix
matrix = initialize_matrix(10)
fig = plt.figure()
ani = FuncAnimation(fig, update, frames=1000, interval=1, blit=False)

plt.show()
