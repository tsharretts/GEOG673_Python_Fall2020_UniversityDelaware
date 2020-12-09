# Tyler Sharretts
# Week 07: SciPy Tutorial

### Set-up

# Import 
import matplotlib.pyplot as plt
import cartopy
import cartopy.feature as cf
import cartopy.crs as ccrs
import xarray as xr
import numpy as np

# Load in nc file
OceanSST = xr.open_dataset("/Users/tshar/Documents/GEOG_673/geog473-673-master/geog473-673-master/datasets/OR_ABI-L2-SSTF-M3_G16_s20192081300453_e20192081400161_c20192081406297.nc")
OceanSST

# Band 15 is a long wave infrared band
# Take a look at it
OceanSST['Band15']

# Get the 0th timestamp from Band 15
OceanSST['Band15'][0]

# Check out lon & lat values
OceanSST['longitude'].values, OceanSST['latitude'].values

# NOTE: Projection is reprojected to PlateCarree from the original data feed

### Plotting (the "old-fashioned way" using matplotlib.pyplot)
### Run all components together

# Plot Band 15 Mosaic

fig = plt.figure(figsize = (16, 12))
ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())
ax.set_extent((-100, -60, 16, 52), crs = ccrs.PlateCarree())
im = ax.pcolormesh(OceanSST['longitude'].values, OceanSST['latitude'].values, OceanSST['Band15'][0].values,
                   cmap='jet', transform = ccrs.PlateCarree(), vmin = 250, vmax = 300)

# Plot in features

ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.BORDERS)
plt.colorbar(im, label = "Degrees Kelvin")

# Plot lon & lat tick marks
plt.xticks(np.arange(np.min(OceanSST['longitude'].values), np.max(OceanSST['longitude'].values), 10))
plt.yticks(np.arange(np.min(OceanSST['latitude'].values), np.max(OceanSST['latitude'].values), 10))

# Plot x & y labels
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Plot title
plt.title("Band 15 Brightness Temperature")

### Plotting (the "handy" way using xarray plotting function)

# Plot SST
# Run all together
fig = plt.figure(figsize = (16, 12))
ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())

OceanSST['SST'][0].plot(cmap = 'jet', vmin = 273, vmax = 300)
ax.add_feature(cf.COASTLINE, color = 'Gray', edgecolor = 'Black')
ax.add_feature(cf.BORDERS, color = 'Gray', edgecolor = 'Black')
ax.add_feature(cf.STATES, edgecolor = 'BLack')

# NOTE: there is data under the coastline and land; they just overlie the data
# NOTE: there is also bad data

### Plot (using Xarray) SST data where there are no clouds 

# Define new SST
# Using Band15 as the threshold, rather than data qulaity flag (DQF)
# Essentially converting all of the values greater than 280 to nans (masked out clouds)
OceanSST = OceanSST['SST'].where(OceanSST['Band15'] > 280)
print(OceanSST)

# Plot the cleaned SST data
# Getting rid of the clouds
# Masking successfully
# Run all together
fig = plt.figure(figsize = (16, 12))
ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())

OceanSST.plot(cmap = 'jet', vmin = 273, vmax = 300)
ax.add_feature(cf.COASTLINE, color = 'Gray', edgecolor = 'Black')
ax.add_feature(cf.BORDERS, color = 'Gray', edgecolor = 'Black')
ax.add_feature(cf.STATES, edgecolor = 'Black')

# OR #
fig = plt.figure(figsize = (16, 12))
ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())

OceanSST.plot(cmap = 'jet', vmin = 273, vmax = 300)
ax.add_feature(cf.COASTLINE, color = 'Gray', edgecolor = 'Black')
ax.add_feature(cf.BORDERS, color = 'Gray', edgecolor = 'Black')
ax.add_feature(cf.STATES, color = 'Gray', edgecolor = 'Black')

### Take-home NOTE:
# SciPy is working underneath of Xarray
# Xarray is higher level than SciPy

### Assignment

# Will be using DQF variable as the threshold, rather than a Band15

# Instead of using...
# OceanSST = OceanSST['SST'].where(OceanSST['Band15'] > 280),... 
# We only want the DQF when it equals zero

# Plot "old-fashioned way

# Submit


