# Name: generate_y_x_time_data.py
# Saves data for plots
import numpy as np
import matplotlib.pyplot as plt
from modules.functions import TTD_Eq

y_top= 1
y_bottom = 0
y_left = y_right = 0
n = 50
dx = 1/n
dt = (dx**2)/4

y = [] 
frames_to_save = [10, 100, 1000, 10000]
domain = np.zeros((n ,n))
domain[0, :] = 1
x = np.linspace(0, 1, n)
dt_ = []

#run the diffusion while saving our four cases 
for i in range(10001):
    domain = TTD_Eq(domain, dt, dx, 1)
    if i in frames_to_save:
        y.append(domain[::-1, 0])
        dt_.append(dt * i)

#save the resulting data
np.save("data/x_valuesTTD.npy", x)
np.save("data/y_valuesTTD.npy", y)
np.save("data/dt_valuesTTD.npy", dt_)
np.save("data/frames_to_saveTTD.npy", frames_to_save)


