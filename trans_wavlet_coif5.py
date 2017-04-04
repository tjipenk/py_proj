# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:39:06 2017

@author: titik
"""

import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data


ecg = pywt.data.ecg()

mode = pywt.Modes.smooth
w = 'coif1'
w = pywt.Wavelet(w)
a = ecg
ca = []
cd = []

for i in range(5):
        (a, d) = pywt.dwt(a, w, mode)
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