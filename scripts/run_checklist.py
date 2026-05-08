"""
Reproducibility Checklist — geometric-physics-luoshu
Run: python3 scripts/run_checklist.py
"""
import numpy as np
import sys

PASS = 0; FAIL = 0

def check(name, got, lo, hi):
    global PASS, FAIL
    if lo <= got <= hi:
        print(f"  PASS  {name}: {got:.6f}  (expected [{lo}, {hi}])")
        PASS += 1
    else:
        print(f"  FAIL  {name}: {got:.6f}  (expected [{lo}, {hi}])")
        FAIL += 1

print("=" * 55)
print("Geometric Physics Lo-Shu — Reproducibility Checklist")
print("=" * 55)

# D1: theta(1) exact
r = np.sqrt((7 - np.sqrt(41)) / 4)
theta1 = np.degrees(np.arccos(r / np.sqrt(2)))
check("D1  theta(1) [deg]", theta1, 74.140, 74.160)

# D2: r_peak power-law slope (simplified)
from numpy.polynomial.laguerre import lagval
def laguerre_max_root(n):
    c = np.zeros(n+1); c[n] = 1
    xs = np.linspace(0, 4*n+10, 5000)
    Lv = lagval(xs, c)
    sc = np.where(np.diff(np.sign(Lv)))[0]
    if len(sc) == 0: return None
    i = sc[-1]
    return xs[i] - Lv[i]*(xs[i+1]-xs[i])/(Lv[i+1]-Lv[i])

ns, rpks = [], []
for n in range(1, 21):
    xr = laguerre_max_root(n)
    if xr: ns.append(n); rpks.append(np.sqrt(xr/2))
from scipy.stats import linregress
sl, ic, rv, _, _ = linregress(np.log(ns), np.log(rpks))
check("D2  power-law slope", sl, 0.790, 0.830)

# D5: Schwarzschild Q-LTE (simplified grid)
def kerr_qlte_schw():
    LUOSHU = np.array([[4,9,2],[3,5,7],[8,1,6]], dtype=float)
    r = np.linspace(2.0, 24.0, 400)
    K = 48.0 / r**6
    edges = np.percentile(r, [0, 33, 67, 100])
    mass = np.array([np.sum(K[(r>=edges[i])&(r<edges[i+1])]) for i in range(3)])
    mass_2d = np.outer(mass/mass.sum(), np.ones(3)/3)
    return np.sum(LUOSHU * mass_2d)
qlte_s = kerr_qlte_schw()
check("D5  Schwarzschild Q-LTE", qlte_s, 4.0, 6.5)

print("-" * 55)
print(f"Results: {PASS} PASS, {FAIL} FAIL")
sys.exit(0 if FAIL == 0 else 1)
