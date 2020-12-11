# Tyler Sharretts
# Final Project: Option 2

### Set-up 

# Import
import xarray as xr
import numpy as np
import pandas as pd
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib.pyplot as plt
from matplotlib import cm
import nc_time_axis
import netCDF4 as nc

# Extract data from: 
# ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_temp/
temp = pd.read_csv('ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_temp/')
temp
temp.describe()
temp.columns
# Data is a mess and I can't uderstand its format

# Load in nc file data
tmax1979 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1979.nc")
tmax1980 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1980.nc")
tmax1981 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1981.nc")
tmax1982 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1982.nc")
tmax1983 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1983.nc")
tmax1984 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1984.nc")
tmax1985 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1985.nc")
tmax1986 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1986.nc")
tmax1987 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1987.nc")
tmax1988 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1988.nc")
tmax1989 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1989.nc")
tmax1990 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1990.nc")
tmax1991 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1991.nc")
tmax1992 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1992.nc")
tmax1993 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1993.nc")
tmax1994 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1994.nc")
tmax1995 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1995.nc")
tmax1996 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1996.nc")
tmax1997 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1997.nc")
tmax1998 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1998.nc")
tmax1999 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.1999.nc")
tmax2000 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2000.nc")
tmax2001 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2001.nc")
tmax2002 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2002.nc")
tmax2003 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2003.nc")
tmax2004 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2004.nc")
tmax2005 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2005.nc")
tmax2006 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2006.nc")
tmax2007 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2007.nc")
tmax2008 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2008.nc")
tmax2009 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2009.nc")
tmax2010 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2010.nc")
tmax2011 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2011.nc")
tmax2012 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2012.nc")
tmax2013 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2013.nc")
tmax2014 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2014.nc")
tmax2015 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2015.nc")
tmax2016 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2016.nc")
tmax2017 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2017.nc")
tmax2018 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2018.nc")
tmax2019 = xr.open_dataset("/Users/tshar/Documents/GEOG_673/Python_FinalProject/tmax.2019.nc")

# See what we are working with (using 1979 as a sample)
tmax1979
tmax1979.tmax

### Question 3
### Global avg max temp for 2019 with coastlines

# Get rid of time dimension; take average with the mean function (for 2019)
temp_2019 = tmax2019.tmax.mean(dim = 'time')
temp_2019

# Get colors
new_cmap = cm.get_cmap('coolwarm')

# Plot
fig = plt.figure(figsize = (16, 10))
ax = plt.axes(projection = ccrs.Mercator())
plt.xlabel('longitude')
plt.ylabel('latitude')
ax.coastlines()
temp_2019.plot(ax = ax, transform = ccrs.PlateCarree(), 
               vmin = -50, vmax = 50, cbar_kwargs = {'shrink' : 0.4}, cmap = new_cmap)

### Question 4
### Difference in global avg max temp for 2019 & 1979

# Get rid of time dimension; take average with the mean function (for 1979)
temp_1979 = tmax1979.tmax.mean(dim = 'time')
temp_1979

# Difference for 2019 & 1979
temp_diff = temp_2019 - temp_1979

# Plot
fig = plt.figure(figsize = (16, 10))
ax = plt.axes(projection = ccrs.Mercator())
plt.xlabel('longitude')
plt.ylabel('latitude')
ax.coastlines()
temp_diff.plot(ax = ax, transform = ccrs.PlateCarree(), 
               vmin = -20, vmax = 20, cbar_kwargs = {'shrink' : 0.4}, cmap = new_cmap)

### Question 5
### Pittsburgh, PA (hometown) avg max temp for 2019

# Extract location for Pittsburgh, PA
# Pittsburgh, PA: lon of 79.9959 degrees W is approximately the 560th longtiude of the temp_2019 dataset
# Pittsburgh, PA: lat of 40.4406 degrees N is approximately the 99th latitude of the temp_2019 dataset

# Historgram
temp_2019.isel(lon = 560, lat = 99).plot()
plt.title('2019 Avgerage Maximum Temperature for the Pittsburgh, PA Region')

# Plot

temp2019 = tmax2019.tmax

temp2019.isel(lon = 560, lat = 99).plot()
plt.title('2019 Avgerage Maximum Temperature for the Pittsburgh, PA Region')

### Question 6
### 1979 - 2019 Time Series of the data
### I got really lost with this question; I did what I could
temp = pd.read_csv('ftp://ftp.cdc.noaa.gov/Datasets/cpc_global_temp/')

# The file was not letting me dive into the sub-variables (tmax & tmin) of temperature
# It started off by only letting me put one column into a dataset
# Even though there is time, tmax, tmin, lon, and lat, Python only wanted to recognize 1 variable for 1 column 
# So I wasn't even working with the full dataset from the get-go for this question
temp_cols = ['Temperature']
temp.columns = temp_cols
temp.Temperature.attrs['Description'] = 'Temperature (in Degrees C)'
temp_series = temp['Temperature']

# This is where my process started to fail and I hit a wall on what to do and ran out of ideas
temp_series = temp_series['1979-01-01' : '2019-12-31']

# Then this also got screwed up as a result
temp['Temperature'][:, 99, 560].plot(style = '.', color = 'blue')
plt.title('1979-2019 Temperature for the Pittsburgh, PA Region')

# This kinda (barely) worked for whatever reason
plt.plot(temp_series)

# Sorry about question 6; just spent way too many hours on it and was going nowhere









