# Name: sink_visualize.py
# visualizes the sink holes

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from modules.functions import TDDE_Eq, TIDE_Eq, Gauss_Eq

n = 50
dx = 1/n
dt = (dx**2)/4 
print(f'dt = {dt}')
x = np.linspace(0,1,n+1)
D = 1

#function to initialize the nxn matrix with only first line being 1 and rest 0
def initialize_matrix(n):
    matrix = np.zeros((n,n))
    matrix[0] = 1
    return matrix

mask = np.ones((50,50))

# makes a sinkhole on those rows if zero, 1 normal, other value 0<x<1 is an insulating material.
mask[22:28, 22:28] = 0.95

def update(frame):
    global matrix
    matrix = Gauss_Eq(matrix, mask=mask)
    im.set_array(matrix)
    return [im]

def on_close(event):
    ani.event_source.stop() 

matrix = initialize_matrix(50)

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap="hot", interpolation="nearest")

# BE ABLE TO CLOSE THE WINDOW WITHOUT CRASHING IT!!!
fig.canvas.mpl_connect("close_event", on_close)

ani = FuncAnimation(fig, update, frames=1000, interval=1, blit=False)
# # add colorbar
plt.colorbar(im)
plt.title('Diffusion in a 50x50 matrix with sinkhole')

plt.yticks([0, 25], [0, 0.5])
plt.xticks([0, 50], [0, 1])
plt.show()