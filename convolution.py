# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:56:43 2019

@author: Prateek
"""
#import time
#s=time.time()
import numpy as np
from imToCol import im2col_


def convolve(A,B, stride):#convolves 2 matrices using one big matrix multiplication(instesd of loops) by stretching the image into columns using im2col_ function
    a,x,y = B.shape
    b,m,n = A.shape
    x_dif, y_dif = np.subtract((m,n), (x,y))
    fil,_,_ = im2col_(B, (1,1,1), 1, padding='valid')

    mat, pad_x, pad_y = im2col_(A, (a,x,y), stride, padding='valid')

    res = np.dot(fil, mat)#dot product

    res = np.reshape(res, (np.int((x_dif+pad_x)/stride+1), np.int((y_dif+pad_y)/stride+1)))#result shape is of order (W-F+2P/S+1)
    return res

#img = np.arange(50).reshape(2,5,5)
#ker = np.arange(8).reshape(2,2,2)
#res = convolve(img, ker, stride=1)
#       
#end=time.time()
#print(end-s)