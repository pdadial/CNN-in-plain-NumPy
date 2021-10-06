# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:52:21 2019

@author: Prateek
"""
import numpy as np

#Dropout prevents overfitting by droping some of the neurons
#Overfitting occurs when the network learns from memorization rather than understanding, therefore doesn't gives correct predictions with a never before seen input 
#Consider the below network   
#   O1--
#       \
#        O3--> 
#       /
#  O2--
#neuron1 gives correct prediction on 80% of training instances
#neuron2 gives correct prediction randomly
#So,neuron3 always forwards the output of neuron1. Thus the gradients only get propagated through neuron1 and neuron3
#Therefore there is one neuron being wasted
#This is overfitting, Dropout removes the neuron1 from the network and forces neuron2 to start doing better than random guesses
def dropout(X, keep_prob):

    mask = np.random.choice([0,1], size = X.shape, p = [1-keep_prob, keep_prob])#generating a random matrix of 0s or 1s using keep_prob as threshold
    X = np.multiply(X, mask)#applying mask to shut down some neurons
    return (X / keep_prob), mask#scaling down the remaining neurons