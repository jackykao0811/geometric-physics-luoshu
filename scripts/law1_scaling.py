"""Law I: r_peak(n) power-law scaling."""
import numpy as np
from numpy.polynomial.laguerre import lagval
from scipy.stats import linregress

def laguerre_max_root(n):
    c = np.zeros(n+1); c[n] = 1
    xs = np.linspace(0, 4*n+10, 5000)
    Lv = lagval(xs, c)
    sc = np.where(np.diff(np.sign(Lv)))[0]
    if len(sc) == 0: return None
    i = sc[-1]
    return xs[i] - Lv[i]*(xs[i+1]-xs[i])/(Lv[i+1]-Lv[i])

ns, rpks, thetas = [], [], []
for n in range(1, 51):
    xr = laguerre_max_root(n)
    if xr:
        rp = np.sqrt(xr/2)
        ns.append(n); rpks.append(rp)
        thetas.append(np.degrees(np.arccos(min(rp/np.sqrt(2*n), 1.0))))

sl, ic, rv, _, _ = linregress(np.log(ns), np.log(rpks))
print(f"r_peak(n) = {np.exp(ic):.3f} * n^{sl:.3f}  (R-sq={rv**2:.4f})")
print(f"theta(1) exact = {np.degrees(np.arccos(np.sqrt((7-np.sqrt(41))/8))):.4f} deg")
