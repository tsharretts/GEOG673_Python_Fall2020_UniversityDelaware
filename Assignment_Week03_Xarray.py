# Tyler Sharretts 
# Week 03: Xarray Assignment

### Importing modules 
import xarray as xr
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

### Preliminary Steps

# Load in dataset
ds = xr.tutorial.load_dataset('air_temperature') 

# Clean data; take out values less than 0 and overwrite 
ds = ds.where(ds.air > 0)

# Get rid of time dimension and find the mean (1 temperature per grid cell)
temp_K = ds.air.mean(dim = 'time')

# Calculate temperature celsius 
temp_C = temp_K - 273.15

# Add datasets to original data 
ds['temp_K'] = temp_K
ds['temp_C'] = temp_C

# temp_K and temp_C do not have attributes; add attributes
ds.temp_K.attrs['Description'] = 'Mean Air Temperature in Kelvin (through time)'
ds.temp_C.attrs['Description'] = 'Mean Air Temperature in Celsius (through time)'

### Question 1

# Find the 200th time dimension 
ds.air.time[200]

# 200th time is 2013-02-20T00:00:00
# Index & plot using the index select method
ds.air.sel(time = '2013-02-20T00:00:00').plot()

### Question 2

# Check time frame to make sure exact dates of the dataset
ds.air.time

# Time frame is 2013-01-01T00:00:00 to 2014-12-31T18:00:00 (fine to include all time)
# Need to extract location (Newark, DE: 39.6837 N, 75.7497 W)
# Data is coarse; use 40 N for lat, use 285 W for lon (-75 degrees from 360)
# Want to include all time (:) for the 14th lat (40 deg_N) & 34th lon (255 deg_W)
ds.air[:, 14, 34].plot()

### Question 3
ds.temp_C.isel(lat = 14, lon = 34).plot()
