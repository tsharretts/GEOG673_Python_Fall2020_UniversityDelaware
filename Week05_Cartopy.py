# Tyler Sharretts 
# Week 05: Cartopy Tutorial

### Importing
### NOTE: crs is coordinate reference system
import numpy as np
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib.pyplot as plt


### Projecting

# Reference some help for the PlateCaree function from the cartopy crs library
help(ccrs.PlateCarree())

# Plate Carree is a latitude and longtiude projection
# We can plot a figure based on the Plate Carree Projection
# Run all together
plt.figure()
ax = plt.axes(projection = ccrs.PlateCarree())

# Use coastlines function from Cartopy on the ax.axes
# Run all together
plt.figure()
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines()

# Working in Mollweide Projection to plot a stock satellite image
# Run all together 
plt.figure()
ax = plt.axes(projection = ccrs.Mollweide())
ax.stock_img()

# Can add text & lines to above plot
# Delcaring New York & New Delhi lon and lat
# Be sure to keep in format of lon first & lat second (x, y)
NY_lon, NY_lat = -75, 43
NewDelhi_lon, NewDelhi_lat = 77.23, 28.61

# We can make a new figure
# Run the stock image again 
# Change the projection from Mollweide to Plate Carree
# Run all together
plt.figure()
ax = plt.axes(projection = ccrs.PlateCarree())
ax.stock_img()

# Can add New York & New Delhi locations to the plot
# Draw a line between the 2 points
# Add a transform to the line so that it matches a geodetic projection (Only transforming the line; not the image or anything else)
# Add / subtract values to lon and lat values, so that the label does not overlap the location coordinate
# Plot all at once
plt.figure()
ax = plt.axes(projection = ccrs.PlateCarree())
ax.stock_img()
plt.plot([NY_lon, NewDelhi_lon], [NY_lat, NewDelhi_lat], 
         color = 'blue', linewidth = 2, marker = 'o', 
         transform = ccrs.Geodetic(),)
plt.text(NY_lon - 3, NY_lat - 12, 'New York', 
         horizontalalignment = 'right', 
         transform = ccrs.Geodetic())
plt.text(NewDelhi_lon + 3, NewDelhi_lat - 12, 'New Delhi', 
         horizontalalignment = 'left', 
         transform = ccrs.Geodetic())

# We can change the color and line style
# Transform based on Plate Carree (but this was not needed; could've just deleted "transform = ccrs.PlateCarree()")
# Run all at once
plt.figure()
ax = plt.axes(projection = ccrs.PlateCarree())
ax.stock_img()
plt.plot([NY_lon, NewDelhi_lon], [NY_lat, NewDelhi_lat], 
         color = 'red', linestyle = '--', 
         transform = ccrs.PlateCarree(),)
plt.text(NY_lon - 3, NY_lat - 12, 'New York', 
         horizontalalignment = 'right', 
         transform = ccrs.Geodetic())
plt.text(NewDelhi_lon + 3, NewDelhi_lat - 12, 'New Delhi', 
         horizontalalignment = 'left', 
         transform = ccrs.Geodetic())

### Cartopy Fundamentals

# Give our projection to the axes and then add the feature to the axes using Cartopy functions
# Run all at once
plt.figure()
ax = plt.axes(projection = ccrs.LambertConformal())
ax.add_feature(cf.COASTLINE)
ax.set_title("Title")

# Switch to Lakes 
# Run all at once
plt.figure()
ax = plt.axes(projection = ccrs.LambertConformal())
ax.add_feature(cf.LAKES)
ax.set_title("Title")

# More advance Cartopy plot with Numpy
# Declaring a few variables: central lon & lat of the US,extent
# NOTE: Extent format of the United States (x min, x max, y min, y max) = (lon min, lon max, lat min, lat max)
# Give it a figure size of 12 x 6 
# Declare the axes where it is given a projection (with central lon & central lat)
# Set extent based on the list
# Add features (oceans, lakes, lakes, & rivers)
# Add gridlines
# Run all together
central_lon = -96
central_lat = 37.5
extent = [-120, -70, 24, 50.5]
central_lon = np.mean(extent[:2])
central_lat = np.mean(extent[2:])
plt.figure(figsize = (12,6))
ax = plt.axes(projection = ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAND, edgecolor = 'black')
ax.add_feature(cf.LAKES, edgecolor = 'black')
ax.add_feature(cf.RIVERS)
ax.gridlines()

# a different way: downloading Rivers file explicitly
# Load in the physical feature "rivers_lake_centerlines" at 50 m resolution
# Leave lakes out just to extentuate the rivers on the map 
# NOTE: if a different resolution if ever needed for features, you can get them off of the cartopy website to use (will be downloaded directly from Python)
# Run all together
rivers_50m = cf.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m')
plt.figure(figsize = (12,6))
ax = plt.axes(projection = ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAND, edgecolor = 'black')
ax.add_feature(rivers_50m, facecolor = 'None', edgecolor = 'b')
ax.gridlines()

### More advanced example using Cartopy
### Plot Hurrican Katrina Path

# Have to load in more libraries
import matplotlib.patches as mpatches 
import matplotlib.pyplot as plt
import shapely.geometry as sgeom
import cartopy.crs as ccrs 
import cartopy.io.shapereader as shpreader

# Defining lons & lats from the HURDAT2 dataset 
# HURDAT2 dataset from AOML/NOAA: 
# http://www.aoml.noaa.gov/hrd/hurdat/newhurdat-all.html on 14th Dec 2012.
lons = [-75.1, -75.7, -76.2, -76.5, -76.9, -77.7, -78.4, -79.0,
        -79.6, -80.1, -80.3, -81.3, -82.0, -82.6, -83.3, -84.0,
        -84.7, -85.3, -85.9, -86.7, -87.7, -88.6, -89.2, -89.6,
        -89.6, -89.6, -89.6, -89.6, -89.1, -88.6, -88.0, -87.0,
        -85.3, -82.9]

lats = [23.1, 23.4, 23.8, 24.5, 25.4, 26.0, 26.1, 26.2, 26.2, 26.0,
        25.9, 25.4, 25.1, 24.9, 24.6, 24.4, 24.4, 24.5, 24.8, 25.2,
        25.7, 26.3, 27.2, 28.2, 29.3, 29.5, 30.2, 31.1, 32.6, 34.1,
        35.6, 37.0, 38.6, 40.1]

# Create a special function called "colorize state"
# Colorizing based on the geometry
# If track of Katrina intersects the geometry of the state, make the face color red; otherwise, make it green
# Run all chunks together
def colorize_state(geometry):
    facecolor = (0.9375, 0.9375, 0.859375)
    if geometry.intersects(track):
        facecolor = 'red'
    elif geometry.intersects(track_buffer):
        facecolor = '#FF7E00'
    return{'facecolor' : facecolor, 'edgecolor' : 'black'}

# Create the figure and add axes and give it a projection
# Chunk 1
# defining our states_shp
fig = plt.figure(figsize = (12,8))
ax = fig.add_axes([0, 0, 1, 1], projection = ccrs.LambertConformal())
ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

shapename = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution = '110m', category = 'cultural', name = shapename)

# Chunk 2
# making it visible
ax.background_patch.set_visible(False)
ax.outline_patch.set_visible(False)
ax.set_title('US States which intersect the track of Hurrican Katrina (2005)')

# Chunk 3
# X is a zip object
# Have to give it a zip object becuase that is what the track takes
# Then defining our track as track.buffer(2)
track = sgeom.LineString(zip(lons, lats))
track_buffer = track.buffer(2)

# Chunk 4
# Give the axes geomoetries (state lines)
# Load in shape reader package / function
# Read the feature
# Grab geometry from that shapefile
# Style the Plate Carree geometry based on colorized state
# Define our track buffer; every argument we need for the function is now defined
# Colorize the states based on whether or not the lines intersect the state
ax.add_geometries(shpreader.Reader(states_shp).geometries(),
                  ccrs.PlateCarree(),
                  styler = colorize_state)

ax.add_geometries([track_buffer], ccrs.PlateCarree(),
                  facecolor = '#C8A2C8', alpha = 0.5)

ax.add_geometries([track], ccrs.PlateCarree(), 
                  facecolor = 'none', edgecolor = 'k')

# Chunk 5
# Add rectangle
# Add legend
direct_hit = mpatches.rectangle((0, 0), 1, 1, facecolor = "red")
within_2_deg = mpatches.Rectangle((0, 0), 1, 1, facecolor = "#FF7E00")
labels = ['State directly intersects \nwith track',
          'State is within \n2 degrees of track']
ax.legend([direct_hit, within_2_deg], labels, 
          loc = 'lower left', bbox_to_anchor = (0.025, -0.1), fancybox = True)

### Adding data to a cartopy plot

# We have temperature data 
# Declare lons & lats as 1-dimensional arrays (lons from -80 to 80 by 25) and (lats from 30 to 70 by 25)
# Mesh these two vectors together to get a mesh grid; make a grid / matrix
# Run all togeter
lon = np.linspace(-80, 80, 25)
lat = np.linspace(30, 70, 25)
lon2d, lat2d = np.meshgrid(lon, lat)
data = np.cos(np.deg2rad(lat2d) * 4) + np.sin(np.deg2rad(lon2d) * 4)

plt.figure(figsize=(10, 6))
plt.contourf(lon2d, lat2d, data)

# Overlap the data onto a cartoply plot with geospatial axes 
# Run all together
plt.figure(figsize = (12, 8))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data)

# We can do the same thing with another projection
# Pre-define pojection
projection = ccrs.RotatedPole(pole_longitude = -177.5, pole_latitude = 37.5)
# Run together
plt.figure(figsize = (12, 8))
ax = plt.axes(projection = projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data)

# This result is wrong because we need to add the transform argument in because the data comes from a different projection
# Fix
projection = ccrs.RotatedPole(pole_longitude = -177.5, pole_latitude = 37.5)

# Run together (correct above plot)
plt.figure(figsize = (12, 8))
ax = plt.axes(projection = projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data, transform = ccrs.PlateCarree())

### Assignment setup

# Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import xarray as xr

# Load in a built-in tutorial dataset
ds = xr.tutorial.load_dataset('air_temperature')
print(ds)

# Convert air temperature to farenhiet
ds['air'].values = (ds['air'].values - 273.15) * (9/5) + 32

# Select a time slice
# Create separate object and name it airtemp
airtemp = ds.air.sel(time = '2013-01-01 12:00', method = 'nearest')
print(airtemp)

# Bring in cartopy
# Give axes a projection of Robinson
# Transform from Plate Caree to Robinson
# Shrink the color bar
# Give it a min & max temp farenheit to plot
# Run all together
fig = plt.figure(figsize = (16, 10))
ax1= plt.axes(projection = ccrs.Robinson())
ax1.coastlines()
ax1.gridlines()
airtemp.plot(ax = ax1, transform = ccrs.PlateCarree(),
             vmin = 20, vmax = 50, cbar_kwargs = {'shrink' : 0.4})

# This was a default color map
# We can use different colors
# import color map module from matplotlib library
from matplotlib import cm

# Yellow orange red color map
new_cmap = cm.get_cmap('YlOrRd')

# New plot
# Run all together
fig = plt.figure(figsize = (16, 10))
ax1= plt.axes(projection = ccrs.Robinson())
ax1.coastlines()
ax1.gridlines()
airtemp.plot(ax = ax1, transform = ccrs.PlateCarree(),
             vmin = 20, vmax = 50, cbar_kwargs = {'shrink' : 0.4}, cmap = new_cmap)

### Assignment

# Reference tree cover dataset within class dataset folder
# Load in NetCDF
# Remove negative values of percentages using xr.where function
# Plot tree cover % of North America with a green cover map
# Plot in Lambert Conformal Projection 
# Submit



