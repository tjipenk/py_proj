# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:04:30 2017

@author: titik
"""
import rasterio
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

filegrid = '/home/titik/kmeans/parallel-kmeans-int64/outsawah.nc'
fileraster = '/home/titik/TXT/Sawah_2015.tif'
def raster_grid(filename):
    with rasterio.open(filename) as img:
        image = img.read()
        bands,rows,cols = np.shape(image)
        image1 = image.transpose(1,2,0).reshape(rows*cols,bands)
        return image1;
def raster_baca(filename):
    with rasterio.open(filename) as img:
        image = img.read()
        bands,rows,cols = np.shape(image)
        image1 = image.transpose(1,2,0).reshape(rows*cols,bands)
        return image;
img = raster_baca(filename=fileraster)
img2 = raster_grid(filename=fileraster)
bands,rows,cols = np.shape(img)

plt.imshow(img[0,:,:])
plt.colormaps()
plt.show()

A = img2.transpose()
A =A[1,:]
B = A.transpose().reshape(1,rows,cols)


bands,rows,cols = np.shape(img)
A =hasil[1,:]
B = A.transpose().reshape(1,rows,cols)


plt.imshow(B[0,:,:])
plt.colormaps()
plt.show()