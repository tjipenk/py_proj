# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:03:58 2017

@author: titik
"""

import rasterio
#import gdal
import numpy as np
import matplotlib.pyplot as plt
import csv
from netCDF4 import Dataset
import sys
import os

#filegrid = sys.argv[1]
#fileraster = sys.argv[2]
#fileext = sys.argv[3]

filegrid = '/home/titik/kmeans/parallel-kmeans-int64/outsawah.nc'

filegrid = '/home/titik/TXT/Sawah_2015.tif.nc'
fileraster = '/home/titik/TXT/Sawah_2015.tif'
fileext = 'nc'

def baca_txt(filename,rows,cols):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        grid = reader.transpose().reshape(1,rows,cols)
    return grid;
    
def baca_nc(filename,rows,cols):
    nc_fid = Dataset(filename, 'r')
    #reader = nc_fid.variables['membership'][:]
    reader = nc_fid.variables['data'][:]
    reader = reader[:,1]
    grid = reader.transpose().reshape(1,rows,cols)
    return grid;

## main
with rasterio.open(fileraster) as src:
    profile=src.profile
    #a, b, c = src.read()
    raster_ori = src.read()
    bands,rows,cols = np.shape(src.read())
    profile.update(dtype=rasterio.uint16, count=1)
    plt.imshow(raster_ori[0,:,:])
    plt.colormaps()
    plt.show()
   
if fileext == 'txt':
    image = baca_txt(filegrid,rows,cols)
    with rasterio.open(fileraster+'hasil.tif', 'w', **profile) as dst:
        dst.write(image.astype(rasterio.uint16),1)
    
elif fileext == 'nc':
    nc5to4 = 'ncks '+ filegrid + ' -4 ' + filegrid +'.4.nc' 
    filegrid = filegrid+'.4.nc' 
    os.system(nc5to4)
    image = baca_nc(filegrid,rows,cols)
    plt.imshow(image[0,:,:])
    plt.colormaps()
    plt.show()
    with rasterio.open(fileraster+'hasil.tif', 'w', **profile) as dst:
        dst.write(image.astype(rasterio.uint16))
    
else:
    print 'Check your input parameter[3]!!'