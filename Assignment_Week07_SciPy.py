# Tyler Sharretts
# Week 07: SciPy Assignment

### Set-up

# Import 
import matplotlib.pyplot as plt
import cartopy
import cartopy.feature as cf
import cartopy.crs as ccrs
import xarray as xr
import numpy as np

# Load in nc file dataset
OceanSST = xr.open_dataset("/Users/tshar/Documents/GEOG_673/geog473-673-master/geog473-673-master/datasets/OR_ABI-L2-SSTF-M3_G16_s20192081300453_e20192081400161_c20192081406297.nc")
OceanSST

# Check out DQF
OceanSST['DQF']

# Define new SST
# Use DQF as the threshold
# Converting all DQF values equal to 0 to nans and masking them
OceanDQF = OceanSST['SST'].where(OceanSST['DQF'] == 0)
OceanDQF

### Plotting

# Plot using Xarray function 
fig = plt.figure(figsize = (16, 12))
ax = fig.add_subplot(1, 1, 1, projection = ccrs.PlateCarree())
ax.set_extent((-100, -60, 16, 52), crs = ccrs.PlateCarree())
im = ax.pcolormesh(OceanSST['longitude'].values, OceanSST['latitude'].values, OceanSST['DQF'][0].values, 
                   cmap = 'jet', transform = ccrs.PlateCarree(), vmin = 0, vmax = 3)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.BORDERS)
plt.colorbar(im, label = "Data Quality Flag Grade")
plt.xticks(np.arange(np.min(OceanSST['longitude'].values), np.max(OceanSST['longitude'].values), 10))
plt.yticks(np.arange(np.min(OceanSST['latitude'].values), np.max(OceanSST['latitude'].values), 10))
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Data Quality Flag Grade")





