# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 09:30:30 2017

@author: titik
"""
import matplotlib.pyplot as plt
import rasterio
#import gdal
import numpy as np
import csv
from netCDF4 import Dataset
import sys
import os

fileraster = sys.argv[1]
fileext = sys.argv[2]

#fileraster = '/home/titik/TXT/Sawah_2015.tif'
#fileext = 'nc'
## raster gdal
#image = gdal.Open(filename)
#data = image.ReadAsArray()
#bands,rows,cols = np.shape(data)
#image1 = image.reshape (rows*cols,bands)

## raster io
def raster_to_2d(filename):
    with rasterio.open(filename) as img:
        image = img.read()
        #img = rasterio.open(filename)
        # transform image
        bands,rows,cols = np.shape(image)
        image1 = image.transpose(1,2,0).reshape(rows*cols,bands)
        #image1 = image.reshape(bands,rows*cols)
        print(np.shape(image1))
      #  ncell = np.arange(0,rows*cols)  # 0,1,2,3,...,6253470
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
        #export = np.column_stack((ncell, image1))
        
    return image1;

def tulis_txt(filename, export):
    fname=filename+'.txt'
    with open(fname, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(export)
        fp.close() # close file
    print(fname)
    return;
    
def tulis_nc(filename, export):
    fname=filename+'.nc'
    #fname=fileraster+'.nc'  
    ncfile = Dataset(fname,'w') 
    ncell,nband = np.shape(grid)
    ncfile.createDimension('ncell',ncell)
    ncfile.createDimension('nband',nband)
    data = ncfile.createVariable('data',np.uint64,('ncell','nband'))
    data[:,:] = export
    ncfile.close()
    print(fname)
    return export.transpose();
    
    

##run app
grid = raster_to_2d(filename=fileraster)
if fileext == 'txt':
    tulis_txt(filename=fileraster,export=grid)
elif fileext == 'nc':
    hasil=tulis_nc(filename=fileraster,export=grid)
    nc4to5 = 'ncks '+ fileraster + '.nc' + ' -5 ' + fileraster +'.5.nc' 
    os.system(nc4to5)
else:
    tulis_nc(filename=fileraster,export=grid)
    tulis_txt(filename=fileraster,export=grid);
    


    




    
        
    

    