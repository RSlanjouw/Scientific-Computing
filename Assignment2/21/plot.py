import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.50, 1.99, 0.02)

zoomed_omega = np.load('zoomed_omega1.npy')
zoomed_omega2 = np.load('zoomed_omega15.npy')
zoomed_omega3 = np.load('zoomed_omega05.npy')

zoomed_omega = np.array(zoomed_omega)
zoomed_omega2 = np.array(zoomed_omega2)
zoomed_omega3 = np.array(zoomed_omega3)

zoomed_omega = zoomed_omega.reshape(20, 25)
zoomed_omega2 = zoomed_omega2.reshape(20, 25)
zoomed_omega3 = zoomed_omega3.reshape(20, 25)

avr_omega = np.mean(zoomed_omega, axis=0)
avr_omega2 = np.mean(zoomed_omega2, axis=0)
avr_omega3 = np.mean(zoomed_omega3, axis=0)
plt.plot(x, avr_omega3, marker='o', label='eta=0.5')
plt.plot(x, avr_omega, marker='o', label='eta=1')
plt.plot(x, avr_omega2, marker='o', label=f'$\eta$=1.5')

std_dev = np.std(zoomed_omega, axis=0)
std_dev2 = np.std(zoomed_omega2, axis=0)
std_dev3 = np.std(zoomed_omega3, axis=0)
plt.fill_between(x, avr_omega3 - std_dev, avr_omega3 + std_dev, alpha=0.2)
plt.fill_between(x, avr_omega - std_dev, avr_omega + std_dev, alpha=0.2)
plt.fill_between(x, avr_omega2 - std_dev2, avr_omega2 + std_dev2, alpha=0.2)

plt.legend(['eta=1', 'eta=1.5', 'eta=0.5'])
plt.xlabel('Omega')
plt.ylabel('Iterations')
plt.title('Optimal Omega per step')
plt.grid()
plt.xlim(1.50, 1.95)
plt.show()

# print the min iterations
# print(np.min(avr_omega))
# print(np.min(avr_omega2))
# print(np.min(avr_omega3))
# print(x[np.argmin(avr_omega)])
# print(x[np.argmin(avr_omega2)])
# print(x[np.argmin(avr_omega3)])



