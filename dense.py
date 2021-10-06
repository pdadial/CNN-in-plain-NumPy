# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:12:17 2019

@author: Prateek
"""

def fc_forward(X, W):
    out = W @ X
    cache = (X, W)
    return out, cache
    