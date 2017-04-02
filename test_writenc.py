# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:28:32 2017

@author: titik
"""

from netCDF4 import Dataset
from numpy import arange, dtype


# the output array to write will be nx x ny
nx = 6; ny = 12
# open a new netCDF file for writing.
ncfile = Dataset('simple_xy.nc','w') 
# create the output data.
data_out = arange(nx*ny) # 1d array
data_out.shape = (nx,ny) # reshape to 2d array
# create the x and y dimensions.
ncfile.createDimension('x',nx)
ncfile.createDimension('y',ny)
# create the variable (4 byte integer in this case)
# first argument is name of variable, second is datatype, third is
# a tuple with the names of dimensions.
data = ncfile.createVariable('data',dtype('int32').char,('x','y'))
# write data to variable.
data[:] = data_out
# close the file.
ncfile.close()
print '*** SUCCESS writing example file simple_xy.nc!'
