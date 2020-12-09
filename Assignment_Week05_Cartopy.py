# Tyler Sharretts
# Week 05: Cartopy Assignment

### Setup

# Importing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

# Load in nc file dataset
treedata = xr.open_dataset("/Users/tshar/Documents/GEOG_673/geog473-673-master/geog473-673-master/datasets/treecov.nc")
treedata

# Removing values below 0
treedata = treedata.where(treedata.treecov > 0)

### Plotting

# Importing
import cartopy.feature as cf
import cartopy.crs as ccrs
from matplotlib import cm

# Get a green for map
new_cmap = cm.get_cmap('Greens')

# Set up figure
plt.figure(figsize = (10,6))

# Plot
fig = plt.figure(figsize = (16, 10))
ax1 = plt.axes(projection = ccrs.LambertConformal())
ax1.coastlines()
ax1.gridlines()
treedata.treecov.plot(ax = ax1, transform = ccrs.PlateCarree(), 
              vmin = 0, vmax = 100, cbar_kwargs = {'shrink' : 0.4}, cmap = new_cmap)








