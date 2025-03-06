import numpy as np
from numba import njit

@njit
def update_contour(candidate_loc, contour, domain):
    """
    Update the contour and domain matrices after a candidate location is chosen to aggregate.

    Parameters:
    candidate_loc (tuple): Coordinates of the chosen candidate.
    contour (ndarray): Matrix tracking the cluster (1s) and neighboring candidates (2s).
    domain (ndarray): Matrix where the diffusion equation is solved.

    Returns:
    tuple: Updated contour matrix and list of new candidate locations.
    """
    n = len(contour)
    x, y = candidate_loc
    domain[x, y] = 0
    contour[x, y] = 1

    neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    candidates = []

    for nx, ny in neighbors:
        if 0 < nx < n-1 and 0 < ny < n-1 and contour[nx, ny] != 1:
            contour[nx, ny] = 2
            candidates.append((nx, ny))

    return contour, candidates

def aggregate_candidate(candidates, domain, eta):
    """
    Choose a candidate to aggregate based on their probabilities.

    Parameters:
    candidates (list): List of candidate coordinates.
    domain (ndarray): Matrix where the diffusion equation is solved.
    eta (float): Exponent for probability calculation.

    Returns:
    tuple: Coordinates of the chosen candidate.
    """
    a = np.array([(np.abs(domain[i, j]))**eta for i, j in candidates])
    prob_cand = a / np.sum(a)
    return candidates[np.random.choice(len(candidates), p=prob_cand)]

@njit
def sor_iteration(matrix, contour, w):
    """
    Perform one iteration of the Successive Over-Relaxation (SOR) method.

    Parameters:
    matrix (ndarray): Current state of the domain matrix.
    contour (ndarray): Matrix tracking the cluster (1s).
    w (float): Relaxation factor.

    Returns:
    ndarray: Updated domain matrix after one SOR iteration.
    """
    n = len(matrix)
    next_matrix = np.copy(matrix)

    for j in range(1, n-1):
        for i in range(n):
            if contour[j, i] == 1:
                next_matrix[j, i] = 0
            else:
                if i == 0:
                    next_matrix[j, i] = w/4 * (matrix[j, 1] + matrix[j, -2] + matrix[j+1, i] + next_matrix[j-1, i]) + (1 - w) * matrix[j, i]
                elif i == n-1:
                    next_matrix[j, i] = w/4 * (matrix[j, 1] + matrix[j, -2] + matrix[j+1, i] + next_matrix[j-1, i]) + (1 - w) * matrix[j, i]
                else:
                    next_matrix[j, i] = w/4 * (matrix[j, i+1] + next_matrix[j, i-1] + matrix[j+1, i] + next_matrix[j-1, i]) + (1 - w) * matrix[j, i]

    return next_matrix

@njit
def sor(domain, contour, w, eps=1e-5):
    """
    Run the SOR method until convergence.

    Parameters:
    domain (ndarray): Initial state of the domain matrix.
    contour (ndarray): Matrix tracking the cluster (1s).
    w (float): Relaxation factor.
    eps (float): Convergence precision.

    Returns:
    tuple: Converged domain matrix and number of iterations.
    """
    conv = 1
    iter_count = 0

    while conv > eps:
        next_domain = sor_iteration(domain, contour, w)
        conv = np.max(np.abs(next_domain - domain))
        domain = next_domain
        iter_count += 1

    return domain, iter_count

def next_step(domain, contour, candidates, eta, w, optimal_omega=False):
    """
    Perform the next step in the DLA model.

    Parameters:
    domain (ndarray): Current state of the domain matrix.
    contour (ndarray): Matrix tracking the cluster (1s).
    candidates (list): List of candidate coordinates.
    eta (float): Exponent for probability calculation.
    w (float): Relaxation factor.

    Returns:
    tuple: Updated domain, contour, and candidates.
    """
    cand = aggregate_candidate(candidates, domain, eta)
    contour, candidates = update_contour(cand, contour, domain)
    if optimal_omega:
        import scipy.optimize as opt
        def sor_opt(matrix, contour, omega, tol=1e-5):
            return sor(matrix, contour, omega, eps=tol)[1]
        result = opt.minimize_scalar(sor_opt, args=(contour, w))
        domain, iter = sor(domain, contour, result.x)
        return domain, contour, candidates, iter, result.x
    domain, iter = sor(domain, contour, w)
    return domain, contour, candidates, iter

