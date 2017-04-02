# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:17:25 2017

@author: titik
"""

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(2)
    hasil = p.map(f, [1, 2, 3])
    print(hasil)