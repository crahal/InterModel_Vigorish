import numpy as np
from scipy.optimize import minimize


def calc_r2(truth, pred, ybar_train):
    """Replicate FFC eval metric"""
    pred_err_sq = (truth - pred)**2
    sum_pred_err_sqr = pred_err_sq.sum()
    dev_sqr = (truth-ybar_train)**2
    sum_dev_sqr = dev_sqr.sum()
    r2 = 1 - (sum_pred_err_sqr/sum_dev_sqr)
    return r2


def ll(x, p):
    """x is the truth, p is the guess"""
    z = (np.log(p)*x) + (np.log(1-p)*(1-x))
    return np.exp(np.sum(z)/len(z))


def get_w(a, guess=0.5, bounds=[(0.001, 0.999)]):
    """argmin calc for 'w'"""
    res = minimize(minimize_me, guess, args=a,
                   options={'ftol': 0, 'gtol': 1e-09},
                   method='L-BFGS-B', bounds=bounds)
    return res['x'][0]


def minimize_me(p, a):
    """ function to be minimized"""
    # abs(p*log(p)+(1-p)*log(1-p)-log(a))
    return abs((p*np.log(p))+((1-p)*np.log(1-p))-np.log(a))


def get_ew(w0, w1):
    """calculate the e(w) metric from w0 and w1"""
    return (w1-w0)/w0


def get_vw(w0, w1):
    """ calculate the v(w) metric from w0 and w1"""
    return (np.divide([1 - i for i in w0], w0)**2)*w1+1-w1