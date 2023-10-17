import numpy as np
from scipy.optimize import minimize


def ll(x, p):
    """Calculate the log-likelihood"""
    z = np.log(p) * x + np.log(1 - p) * (1 - x)
    return np.exp(np.sum(z) / len(z))


def get_w(a, guess=0.5, bounds=[(0.001, 0.999)]):
    """Calculate 'w' using optimization"""
    res = minimize(minimize_me, guess, args=a,
                   options={'ftol': 0, 'gtol': 1e-09},
                   method='L-BFGS-B', bounds=bounds)
    return res.x[0]


def minimize_me(p, a):
    """Function to be minimized"""
    return abs(p * np.log(p) + (1 - p) * np.log(1 - p) - np.log(a))


def get_ew(w0, w1):
    """Calculate the e(w) metric"""
    return (w1 - w0) / w0


def main():
    x = np.array([0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,
                  0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    p_baseline = 0.55
    p_enhanced = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                           0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                           0.5, 0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.9,
                           0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
                           0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])
    a0 = ll(x, p_baseline)
    a1 = ll(x, p_enhanced)
    w0_p = get_w(a0)
    w1_p = get_w(a1)
    ew_p = get_ew(w0_p, w1_p)
    print('E(W) using scipy.optimize is: ', ew_p)


if __name__ == '__main__':
    main()
