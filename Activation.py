# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:27:29 2019

@author: Prateek
"""

import numpy as np
 
def sigmoid(X):
    out = (1.0 / (1.0 + np.exp(-1.0 * X)))
    cache = out
    return out, cache
    
#def softmax(X):
#    e_x = np.exp(X - np.max(X))
#    return e_x / e_x.sum()

def relu(X):
    out = np.maximum(X,0)
    cache = X
    return out, cache