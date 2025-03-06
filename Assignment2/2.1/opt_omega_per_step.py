# show the optimal omega per step for the DLA simulation
from modules.functions import sor, update_contour, aggregate_candidate, next_step
import numpy as np
import matplotlib.pyplot as plt

n = 100 # grid length (once squared)
eta = 0.24 # shape parameter
w = 1.8 # relaxation factor
N = 150 #size of constructed cluster  

# Initialize domain and contour
domain = np.zeros((n, n))
domain[0, :] = 1



contour = np.zeros((n, n))
# initialize a 1x1 cluster at the bottom/middle of the grid
contour, candidates = update_contour([n-2, n//2], contour, domain)
domain, iter = sor(domain, contour, w)


to_test_eta = np.linspace(0.1, 2, 20)
to_test_w = np.linspace(1, 2, 10)
amount_of_iterations = np.zeros((len(to_test_eta), len(to_test_w)))

for i, eta in enumerate(to_test_eta):
    for j, w in enumerate(to_test_w):
        domain = np.zeros((n, n))
        domain[0, :] = 1
        contour = np.zeros((n, n))
        contour, candidates = update_contour([n-2, n//2], contour, domain)
        domain, iter = sor(domain, contour, w)
        for k in range(N):
            domain, contour, candidates = next_step(domain, contour, candidates, eta, w)
        amount_of_iterations[i, j] = iter
        print(f"eta: {eta}, w: {w}, iterations: {iter}")




# I change the resulting domain a little so the color map shows more contrast, thus we see the cluster better
color_domain = np.copy(domain)
for x in range(0, n):
    for y in range(0, n):
        if contour[x, y] == 1:
            color_domain[x, y] = -1

# plot the resulting grid and cluster
im = plt.imshow(color_domain, cmap='hot_r')
plt.xlabel("x (100)")
plt.ylabel("y (100)")
plt.title(fr"Diffusion Limited Aggregation with $\omega=${w} and $\eta=${eta}")
plt.xlim(0, n-1)
plt.ylim(n-1, 0)
#plt.savefig("dla_set2_2a.png", dpi = 300)
plt.show()