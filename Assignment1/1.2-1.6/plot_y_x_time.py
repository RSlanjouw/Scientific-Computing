# Name: plot_y_x_time.py
# Plots the data from the TTD equation

import numpy as np
import matplotlib.pyplot as plt
from modules import error_analytical as ea


show_analytic = True
# check if data files are there
try:
    x = np.load("data/x_valuesTTD.npy")
    y = np.load("data/y_valuesTTD.npy")
    dt_ = np.load("data/dt_valuesTTD.npy")
    frames_to_save = np.load("data/frames_to_saveTTD.npy")
except:
    # run the generate_y_x_time_data.py file
    import os
    os.system("python generate_y_x_time_data.py") 
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
        plt.plot(x, y_analytic[idx], label=fr"Analytical $\delta t =${dt_[idx]}", linestyle='-', marker='^', markersize=3)

#plot the resulting data

for idx, _ in enumerate(frames_to_save):
    plt.plot(x, y[idx], label=fr" $\delta t =${dt_[idx]}", linestyle='-', marker='o', markersize=3)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Plot")
plt.legend()
plt.show()