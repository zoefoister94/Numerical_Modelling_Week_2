# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 14:30:12 2017

@author: bc805136
"""
import numpy as np

def solveByBisect(f, a, b, nmax=100, e=1e-6):
    "Solve function f by bisection method."
    "Solve to error e starting from a and b. Maximum nmax iterations"

    if nmax <= 0:
        raise ValueError('Argument nmax to solveByBisect should be >0')


    # Iterate until the solution is within the
    # error or too many iterations
    for it in range(nmax):
        c = 0.5*(a+b)
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        if abs(f(c)) < abs(e):
            break
    else:
        raise Exception("No root found by solveByBisect")
    
    return c, it+1

try:
    solveByBisect(np.cos,-1.,1.)
except:
    pass
else:
    print("Error in solveByBisect, should raise an exception as there is no root")
 
root=solveByBisect(np.cos, -10., 10., 10000)[0]
print ("root=",root)
