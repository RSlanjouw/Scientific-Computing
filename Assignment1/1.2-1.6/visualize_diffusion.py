# Name: visualize_diffusion.py 
# Yes the file visualize diffusion makes a plot animation of the diffusion function.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from modules.functions import TDDE_Eq, TIDE_Eq, Gauss_Eq

y_top= 1
y_bottom = 0
y_left = y_right = 0
step_t = 1/10000
step_x = 1/50

#function to initialize the nxn matrix with only first line being 1 and rest 0
def initialize_matrix(n):
    matrix = np.zeros((n,n))
    matrix[0] = 1
    return matrix



def update(frame):
    global matrix
    matrix = TDDE_Eq(matrix, step_t, step_x, 1)
    im.set_array(matrix)
    return [im]

def on_close(event):
    ani.event_source.stop() 

matrix = initialize_matrix(50)

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap="hot", interpolation="nearest")

# BE ABLE TO CLOSE
fig.canvas.mpl_connect("close_event", on_close)

ani = FuncAnimation(fig, update, frames=1000, interval=0.1, blit=False)

plt.yticks([0, 25], [0, 0.5])
plt.xticks([0, 50], [0, 1])
plt.show() 