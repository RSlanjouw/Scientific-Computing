# Name: plot_y_x_time.py
# Plots the data from the TTD equation

import numpy as np
import matplotlib.pyplot as plt
from modules.error_analytical import analytical_solution
from modules.functions import TTD_Eq


show_analytic = True

def generate():
    y_top= 1
    y_bottom = 0
    y_left = y_right = 0
    n = 50
    dx = 1/n
    dt = (dx**2)/4
    print(dt)
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
color = ["blue", "red", "green", "purple", "yellow"]

if show_analytic == True:
    for idx, f in enumerate(frames_to_save):
        # read from dictionary
        dx = 1/50
        dt = (dx**2)/4
        print(dt_[idx] / dt)
        x = np.linspace(0, 1, 50)
        l = analytical_solution(x,f, 1)
        plt.plot(x, l, label=fr"Analytical $\delta t =${dt_[idx]}", linestyle='-', marker='^', markersize=3, color=color[idx])

# make line for t=0
matrix = np.zeros((50, 50))
matrix[0] = 1
matrix[-1] = 0

# calculate analytical solution at t=0
y_analytic = analytical_solution(matrix, 0, 1)[0]
plt.plot(x, y_analytic, label=fr"Analytical $\delta t=$ 0", linestyle='-', marker='^', markersize=3,color="black")
plt.plot(x, matrix[::-1, 0], label="$\delta t =$ 0", linestyle='--', marker='o', markersize=3, color="black")




#plot the resulting data

for idx, _ in enumerate(frames_to_save):
    plt.plot(x, y[idx], label=fr" $\delta t =${dt_[idx]}", linestyle='--', marker='o', markersize=3, color=color[idx])

plt.xlabel("Y-values")
plt.ylabel("Consentration")
plt.grid()
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title("Analytical vs Time Dependent Diffusion Equation")
plt.legend()
plt.show()