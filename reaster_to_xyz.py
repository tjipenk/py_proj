# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:30:30 2017

@author: titik
"""
import rasterio
#import gdal
import numpy as np
import csv
import sys

filename = sys.argv[1]
#filename = '/home/titik/TXT/Sawah_2015.tif'
## raster gdal
#image = gdal.Open(filename)
#data = image.ReadAsArray()
#bands,rows,cols = np.shape(data)
#image1 = image.reshape (rows*cols,bands)

## raster io
with rasterio.open(filename) as img:
#img = rasterio.open(filename)
    image = img.read()
    # transform image
    bands,rows,cols = np.shape(image)
    image1 = image.reshape (rows*cols,bands)
    print(np.shape(image1))
    ncell = np.arange(0,rows*cols)  # 0,1,2,3,...,6253470
    # bounding box of image
    #l,b,r,t = img.bounds
    #resolution of image
    #res = img.res
    #res = img.res
    # meshgrid of X and Y
    #x = np.arange(l,r-0.000000002, res[0])
    #y = np.arange(t,b, -res[0])
    #X,Y = np.meshgrid(x,y)
    #print (np.shape(X))
    # flatten X and Y
    #newX = np.array(X.flatten(1))
    #newY = np.array(Y.flatten(1))
    #print (np.shape(newX))
    # join XY and Z information
    export = np.column_stack((ncell, image1))
    fname=filename+'.txt'
    with open(fname, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(export)
        fp.close() # close file
    print(fname)
    