from scipy.stats import binom
from scipy.special import comb
from scipy.optimize import bisect
from math import factorial
from sympy.functions.combinatorial.numbers import stirling


def empty(n,m,k):
    r=n-k
    return (factorial(r)*stirling(m,r)*comb(n,r))/n**m

def ans(p):
    n=0
    for x in range(1,24):
        n+=sum([min(1,k/x)*empty(8,24-x,k)*binom.pmf(x,24,p) for k in range(9)])
    return n/(1-binom.pmf(0,24,p))-1/3

print((1-bisect(ans,0.000001,1)))