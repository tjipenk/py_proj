# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 06:33:30 2017

@author: titik
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
from joblib import Parallel, delayed
import multiprocessing
    
# what are your inputs, and what operation do you want to 
# perform on each input. For example...
inputs = range(10) 
def processInput(i):
	return i * i
 
num_cores = multiprocessing.cpu_count()

    
def wavelet_trasnform(sig):
    mode = pywt.Modes.smooth
    w = 'coif3'
    w = pywt.Wavelet(w)
    
#    hasil=[]
#    for n in range(data.shape[0]):
        #dd = data[n,1:24]
    ca = []
    cd = []
    for i in range(5):
            (a, d) = pywt.dwt(sig, w, mode)
            ca.append(a)
            cd.append(d)
    rec_a = []
    rec_d = []
    for i, coeff in enumerate(ca):
        coeff_list = [coeff, None] + [None] * i
        rec_a.append(pywt.waverec(coeff_list, w))
    for i, coeff in enumerate(cd):
        coeff_list = [None, coeff] + [None] * i
        rec_d.append(pywt.waverec(coeff_list, w))
#    hasil.append(rec_a[0])
        
    return rec_a[0];

#fname = '/home/titik/TXT/numlowpass-sawah_2015.tif.txt.cluster_centres'
fname = '/home/titik/TXT/Sawah_2015.tif.txt'
data = np.loadtxt(fname)
sig = data[:,1:24]
hasil=[]
#plt.plot(data[:,1:23].transpose())
#for n in range(sig.shape[0]):
#    dd = wavelet_trasnform(sig[n,:].transpose())
#    hasil.append(dd)
#hasil = np.asarray(hasil)
#plt.plot(hasil[:,0:23].transpose())
#results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
hasil_par = Parallel(n_jobs=num_cores)(delayed(wavelet_trasnform)(i) for i in sig)
