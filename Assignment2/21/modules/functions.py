import numpy as np
from numba import njit

def analytical_start(domain):
    domain[0, :] = 1
    domain[-1, :] = 0
    # is an equal line over the whole grid
    x = np.linspace(1, 0, len(domain))
    for i in range(0, len(domain)):
        domain[:, i] = x
    return domain


def update_contour(candidate_loc, contour, domain, candidates):
    n = len(contour)
    x, y = candidate_loc
    domain[x, y] = 0
    contour[x, y] = 1

    neighbors = []
    if x > 0:
        neighbors.append([x-1, y])
    if y > 0:
        neighbors.append([x, y-1])
    if x < n-1:
        neighbors.append([x+1, y])
    if y < n-1:
        neighbors.append([x, y+1])

    for i, j in neighbors:
        if contour[i, j] == 0:
            contour[i, j] = 2
            candidates.append((i, j))
    return contour, candidates

def aggregate_candidate(candidates, domain, eta):
    a = np.array([(np.abs(domain[i, j]))**eta for i, j in candidates])
    prob_cand = a / np.sum(a)
    # print(prob_cand)
    return candidates[np.random.choice(len(candidates), p=prob_cand)]

@njit
def SOR_Eq(matrix, omega, mask):
    new_matrix = matrix.copy()

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix)-1):
            if mask[i, j] == 0 or mask[i, j] == 2:
                new_matrix[i,j] = (1-omega) * matrix[i,j] + omega * (new_matrix[i+1,j] + new_matrix[i-1,j] + new_matrix[i,j+1] + new_matrix[i,j-1])/4
        if mask[i, 0] == 0 or mask[i, 0] == 2:
            new_matrix[i,0] = (1-omega) * matrix[i,0] + omega * (new_matrix[i-1,0] + new_matrix[i+1,0] + new_matrix[i,1] + new_matrix[i,-2]) / 4
        if mask[i, -1] == 0 or mask[i, -1] == 2:
            new_matrix[i,-1] = new_matrix[i,0]
    return new_matrix

@njit
def sor(domain, contour, w, eps=1e-5):
    conv = 1
    iter_count = 0

    while conv > eps:
        next_domain = SOR_Eq(domain, w, contour)
        conv = np.max(np.abs(next_domain - domain))
        domain = next_domain
        iter_count += 1

    return domain, iter_count

def next_step(domain, contour, candidates, eta, w):
    cand = aggregate_candidate(candidates, domain, eta)
    contour, candidates = update_contour(cand, contour, domain, candidates=candidates)
    domain, iter = sor(domain, contour,w)
    return domain, contour, candidates, iter

def test_run_iterations(omega, eta):
    n = 100 
    eta = eta 
    N = 100 
    domain = np.zeros((n, n))
    domain[0, :] = 1
    domain[-1, :] = 0
    contour = np.zeros((n, n))
    domain = analytical_start(domain)
    contour, candidates = update_contour([n-1, n//2], contour, domain, [])
    domain, iter = sor(domain, contour, omega)
    # print(iter)
    iterations = iter
    for k in range(N):
        domain, contour, candidates,iter= next_step(domain, contour, candidates, eta, omega)
        iterations += iter
    return iterations

def run(omega, eta):
    n = 100 # grid length (once squared)
    eta = eta # shape parameter
    N = 250
    domain = np.zeros((n, n))
    domain[0, :] = 1
    domain[-1, :] = 0
    contour = np.zeros((n, n))
    contour, candidates = update_contour([n-2, n//2], contour, domain, candidates=[])
    domain, iter = sor(domain, contour, omega)
    # print(iter)
    for k in range(N):
        domain, contour, candidates,_= next_step(domain, contour, candidates, eta, omega)
    return domain, contour


# # start test sor vs analytical
domain1 = analytical_start(np.zeros((100, 100)))
domain2 = np.zeros((100, 100))
domain2[0, :] = 1
domain2[-1, :] = 0
domain2, _ = sor(domain2, np.zeros((100, 100)), 1.9)
# test or the analytical solution is the same as the sor solution
assert np.allclose(domain1, domain2, atol=1e-2)


