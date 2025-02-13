import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# dt =0.001 seconds
t = np.linspace(0, 1, 1000)
n = 1000
l = 1 
x = np.linspace(0, l, n+1)

def starting_positions_t_0(x,t):
    return np.where((1/5 < x) & (x < 2/5), np.sin(5 * np.pi * x), 0)

def next_time_step(u_before, u_now, c, dt, dx):
    u_next = np.zeros(len(u_before))
    u_next[0] = u_before[0]
    u_next[-1] = u_before[-1]
    if np.array_equal(u_before, u_now):
        for i in range(1, len(u_before)-1):
            second_part = (c*(dt/dx)) ** 2
            third_part = u_now[i+1] - 2*u_now[i] + u_now[i-1]
            u_next[i] = u_now[i] + second_part * third_part
    else:
        for i in range(1,len(u_before)-1):
            first_part = 2*u_now[i] - u_before[i]
            second_part = (c*(dt/dx)) ** 2
            third_part = u_now[i+1] - 2*u_now[i] + u_now[i-1]
            u_next[i] = first_part + second_part * third_part
    return u_next

# Initialize wave states
u_before = starting_positions_t_0(x, 0)
u_now = u_before.copy()

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, l)
ax.set_ylim(-1.1, 1.1)
line, = ax.plot(x, u_now, lw=2)

dt = 0.001
# Update function for animation
def update(frame):
    global u_before, u_now
    c = 1
    dx = l/n
    u_next = next_time_step(u_before, u_now, c, dt, dx)  # Compute next step
    u_before, u_now = u_now.copy(), u_next.copy()  # Ensure proper time-stepping
    line.set_ydata(u_now)  # Update the plot
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=dt * 1000, blit=True)
# make the y-axis range bigger

plt.show()