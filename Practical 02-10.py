# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 13:59:38 2017

@author: bc805136
"""

import numpy as np

N=int(1e4)

I=0

for i in xrange (1,N+1):
    I+=np.sum(0.01)

print I