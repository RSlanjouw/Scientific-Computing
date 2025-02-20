# Name: plot_y_x_time.py
# Plots the data from the TTD equation

import numpy as np
import matplotlib.pyplot as plt
from modules import error_analytical as ea
from modules.functions import TTD_Eq


show_analytic = True

def generate():
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

# check if data files are there
try:
    x = np.load("data/x_valuesTTD.npy")
    y = np.load("data/y_valuesTTD.npy")
    dt_ = np.load("data/dt_valuesTTD.npy")
    frames_to_save = np.load("data/frames_to_saveTTD.npy")
except:
    generate()
    x = np.load("data/x_valuesTTD.npy")
    y = np.load("data/y_valuesTTD.npy")
    dt_ = np.load("data/dt_valuesTTD.npy")
    frames_to_save = np.load("data/frames_to_saveTTD.npy")

plt.figure(figsize=(8, 6))

if show_analytic == True:
    # plot the analytic solustion next to the numerical solution
    y_analytic = []
    for idx, _ in enumerate(frames_to_save):
        y_analytic.append(ea.analytical_solution(x, dt_[idx], 1))
        plt.plot(x, y_analytic[idx], label=fr"Analytical $\delta t =${dt_[idx]}", linestyle='--', marker='^', markersize=3)

#plot the resulting data

for idx, _ in enumerate(frames_to_save):
    plt.plot(x, y[idx], label=fr" $\delta t =${dt_[idx]}", linestyle='-', marker='o', markersize=3)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Plot")
plt.legend()
plt.show()