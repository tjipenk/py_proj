# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 07:39:34 2017

@author: titik
"""

import rasterio
import numpy as np
import csv
#filename = 'C:\\Users\\sukuchha\\Documents\\gdal\\02MAR02_multi_Maps_ChangeDetection.TIF'
#filename ='/home/titik/rGIS/qgis_sample_data/raster/landcover.img'
filename = '/home/titik/TXT/Sawah_2015.tif'
with rasterio.open(filename) as src:
    #read image
    image= src.read()
    # transform image
    bands,rows,cols = np.shape(image)
    image1 = image.reshape (rows*cols,bands)
    print(np.shape(image1))
    # bounding box of image
    l,b,r,t = src.bounds
    #resolution of image
    res = src.res
    res = src.res
    # meshgrid of X and Y
    x = np.arange(l,r, res[0])
    y = np.arange(t,b, -res[0])
    X,Y = np.meshgrid(x,y)
    print (np.shape(X))
    # flatten X and Y
    newX = np.array(X.flatten(1))
    newY = np.array(Y.flatten(1))
    print (np.shape(newX))
    # join XY and Z information
    export = np.column_stack((newX, newY, image1))
    fname='/home/titik/XYZsawah.csv'
    with open(fname, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(export)
        fp.close() # close file
    
