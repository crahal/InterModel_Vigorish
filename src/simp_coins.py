import numpy as np
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage as STAP
from big_fun import ll, get_w, get_ew


def main():
    """A function to replicate Ben's simpcoins in python"""

    string = """
    calc_w <- function(a0){
      f<-function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
      w<-nlminb(.5,f,lower=0.001,upper=.999,a=a0)$par
      return (w)
    }    
    """
    
    r_func = STAP(string, "r_func")
    x = np.array([0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
                  1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  0, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # truth
    p_baseline = 0.55  # baseline guess
    p_enhanced = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                           0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                           0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
                           0.9, 0.9, 0.9, 0.9, 0.9,0.9, 0.9, 0.9, 0.9, 0.9])
    a0 = ll(x, p_baseline)
    a1 = ll(x, p_enhanced)
    w0_r = r_func.calc_w(float(a0))[0]
    w1_r = r_func.calc_w(float(a1))[0]
    ew_r = get_ew(w0_r, w1_r)
    w0_p = get_w(a0)
    w1_p = get_w(a1)
    ew_p = get_ew(w0_p, w1_p)
    print('The E(W) using nlminb via rpy is: ', ew_r)
    print('The E(W) using scipy.optimize is: ', ew_p)


if __name__ == '__main__':
    main()
