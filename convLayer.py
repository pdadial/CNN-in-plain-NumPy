# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:18:56 2019

@author: Prateek
"""
#import numpy as np
#from convolution import convolve
import im2col
import sys

def conv(img, fil, padding, stride):
    if fil.shape[-1] != fil.shape[-2]:#filter matrix must be square
        print("Filter matrix must be square")
        sys.exit()
    
    fil_h = fil.shape[-2]
    fil_w = fil.shape[-1]
    n_filters = fil.shape[0]
    img_h = img.shape[-2]
    img_w = img.shape[-1]
    
    out_h = int(((img_h - fil_h + 2*padding) / stride) + 1)
    out_w = int(((img_w - fil_w + 2*padding) / stride) + 1)
    
    img_col = im2col.im2col_indices(img, fil_h, fil_w, padding, stride)
    fil_col = fil.reshape(n_filters, -1)
    
    conv = fil_col @ img_col
    
    out = conv.reshape(1, n_filters, out_h, out_w)
    cache = (img, fil, img_col)
    return out, cache

#img = np.random.rand(1,32,93,93)
#fil = np.random.randn(64,32,3,3)
#z=conv(img,fil,stride=1, padding =1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#        temp = convolve(image, fil[0,:,:], stride)
#        res = temp[np.newaxis,:,:]
#        num = 1    
#        no_of_filter = fil.shape[0]
#        while num < no_of_filter:
#            temp = convolve(image, fil[num,:,:], stride)[np.newaxis,:,:]   
#            res = np.concatenate((res,temp), axis = 0)
#            num += 1    
#    
#    elif len(fil.shape) > 3:
#        if fil.shape[2] != fil.shape[3]:#filter matrix must be square
#            print("Filter matrix must be square")
#            sys.exit()
#        temp = convolve(image, fil[0,:,:,:], stride)
#        res = temp[np.newaxis,:,:]
#        num = 1    
#        no_of_filter = fil.shape[0]
#        while num < no_of_filter:
#            temp = convolve(image, fil[num,:,:,:], stride)[np.newaxis,:,:]   
#            res = np.concatenate((res,temp), axis = 0)
#            num += 1    
#    return res
#
#img = np.random.rand(5,5)
#fil = np.random.randn(10,4,4)
#z=conv(img,fil,stride=1)