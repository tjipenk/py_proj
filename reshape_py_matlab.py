# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:24:42 2017
About how to user reshape
@author: titik
"""
import numpy as np

A = np.arange(3*5*10).reshape((3,10,5))
z,x,y = A.shape
#Aa = np.reshape(A,(4,5*3), order='F')
Ba = np.reshape(Aa,(5,3,4),order='F')

Ca = A.transpose(1,2,0).reshape(-1,A.shape[0])
Da = Ca.transpose().reshape(Ca.shape[1],10,-1)

A = np.arange(3*5*10).reshape((3,10,5))
z,x,y = A.shape
Aaa = A.transpose(1,2,0).reshape(x*y,z)
Baa = Aaa.transpose().reshape(z,x,y)