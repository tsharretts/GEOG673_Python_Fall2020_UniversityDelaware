# Tyler Sharretts
# Week 03: Xarray Tutorial 

### Importing 

import xarray as xr
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

### Load in the air temperature dataset

ds = xr.tutorial.load_dataset('air_temperature')

# Printing ds
print(ds)
print(ds.Conventions)
print(ds.attrs)
print(ds.lat)
print(ds.lon)
print(ds.time)

# ds types
type (ds)

# Breaking it down even further and extracting key metadata from it 
print(ds.air.attrs)
print(ds.air.values)
type(ds.air.values)

### Can use the .where function to clean the dataset 

# Taking out values that are less than zero because anything below 0 K is impossible
# and overwriting ds with ds > 0 
ds = ds.where(ds.air > 0)
print(ds)

### Getting rid of the time dimension by averaging it out with the .mean function (1 temperature per grid cell)
temp_K = ds.air.mean(dim = 'time')
print(temp_K)

### Using a plot function on a xarray data array 
temp_K.plot()

### Doing array math 

# Convert to Celsius 
temp_C = temp_K - 273.15
print(temp_C)
temp_C.plot()

### Adding two created datasets to original ds dataset 

# Adding temp_K & temp_C to original ds
ds['temp_kelvin'] = temp_K
ds['temp_celsius'] = temp_C
print(ds.temp_K)
print(ds.temp_C)

# There are no attributes to temp_K & temp_C
# Have to add attributes
ds.temp_kelvin.attrs['Description'] = 'Mean Air Temperature in Kelvin (through time)'
print(ds.temp_kelvin.attrs)

ds.temp_celsius.attrs['Description'] = 'Mean Air Temperature in Celsius (through time)'
print(ds.temp_celsius.attrs)

### Saving the dataset as a net CDF file 

ds.to_netcdf('/Users/tshar/Documents/GEOG_673/Python_files/Week03_AirTemp.nc')

### Indexing xarray datasets (Numpy way)

# Print the dataset 
ds

# Print a variable of the dataset 
ds.air

# Index it by the 1st latitude and 2nd longtiude for every time slice component
# NOTE: ":" operator means all of the time
ds.air[:, 1, 2]

# Use the plot functionality to plot the time series for the specific location
ds.air[:, 1, 2].plot()

### Indexing xarray datasets (Xarray way)
### Good if know exact location or coordinates
ds.air.sel(lat = 72.5, lon = 205.0)

# Can also put a time component on it
ds.air.sel(lat = 72.5, lon = 205.0, time = "2013-01-01")

# Plot it 
ds.air.sel(lat = 72.5, lon = 205.0).plot()

### Can also index based off of the index selection
### Good if you know exactly where you are in an array  

# Create 2 variables (0th lat & 0th lon)
lat0 = ds.lat[0]
lon0 = ds.lon[0]
print(lat0, lon0)

# We can index select
ds.air.isel(lat = 0, lon = 0)

# Plot it
ds.air.isel(lat = 0, lon = 0).plot()

# Can also plot it with other variables (like temp_celsius)
ds.temp_celsius.isel(lat = 0, lon = 0).plot()

# Can also select for one day (yyyy-mm-dd) 
ds.air.sel(time = '2013-01-02').plot()

# Can also select for a single time
# NOTE: when selecting time, pay attention to how it is stored (run a ds.time[1] to get sorted out at first)
ds.air.sel(time = '2013-01-02T06:00').plot()
