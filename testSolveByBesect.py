# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 14:44:41 2017

@author: bc805136
"""

import numpy as np

execfile("solveByBisect.py")
#import solveByBisect

assert abs(np.cos(solveByBisect(np.cos,1,np.pi)[0])) < 1e-6, \
        "solveByBisect gave the wrong answer for cos"
        
assert abs(solveByBisect(lambda x: 2*x+3,-10,10)[0]+1.5) < 1e-6, \
        "solveByBisect gave the wrong answer for a linear function"