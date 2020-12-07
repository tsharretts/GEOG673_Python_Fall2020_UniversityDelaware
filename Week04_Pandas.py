# Tyler Sharretts
# Week 04: Pandas Tutorial

### Importing 
import pandas as pd
import matplotlib.pyplot as plt

### Panda intro with data tables and csv files

### We can work with data that is currently resting online 

# Work with Chipotle orders
orders = pd.read_table('http://bit.ly/chiporders')

# See what we are working with 
print(orders)
type(orders)

# Use the dot operators
orders.head()
orders.order_id
orders.item_price

# Use the bracketing method
orders['order_id']
orders['item_price']

# Check a variable
orders['item_name']

# Can index from there
# Only one way to index it and that is rows; that is why there is no parenthesese
# First 5 rows of item_name
orders['item_name'][0:5]

orders.item_name[0:5]

### Opening another online datset (with the read csv function)

# Work with UFO dataset
ufo = pd.read_csv('http://bit.ly/uforeports')

# Examine the column names 
ufo.columns
ufo.head

# Replacing 2 columns with the rename method and overwriting their names
ufo.rename(columns = {'Colors Reported' : 'Colors_Reported', 'Shape Reported' : 'Shape_Reported'}, inplace = True)
ufo.columns

# Replace column names by overwriting the columns attribute
# NOTE: list has to be in the same order all of the time
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
ufo.columns

# If we read in a file and already know the column names are bad, so we will give it the names right away 
# Reload the file in and use the names parameter
ufo = pd.read_csv('http://bit.ly/uforeports', header = 0, names = ufo_cols)
ufo.columns

# Replace all spaces with underscores in the column names using the "str.replace" method
ufo.columns = ufo.columns.str.replace(' ', '_')
ufo.columns

# Check data again 
ufo.head()

# If we want to add another column to the data (create a new location series)
# Combining city and state 
ufo['Location'] = ufo.city + ', ' + ufo.state
ufo.head()

# Describe function is also a way to check the data frame
# Descriptions of the statistics of the columns of the the dataset 
ufo.describe()

# Remove a single column (using the drop function)
ufo.drop('colors_reported', axis = 1, inplace = True)
ufo.head()

### Load in DEOS data 
deos_data = pd.read_csv('/Users/tshar/Documents/GEOG_673/geog473-673-master/geog473-673-master/datasets/DEOS.csv')
deos_data

# Check out columns 
deos_data.columns

# Run a type if ever confused as to what a dataset is
type(deos_data)

# Replace all columns names by overwriting the columns attribute
deos_cols = ['Timestamp', 'AirTemperature', 'DewPoint', 'WindSpeed', 'WindDirection', 'Barometric Pressure', 'SolarRadiation', 'WindGust', 'GagePrecipitation']

# Replace names of columns with deos columns list
deos_data.columns = deos_cols

# Double check
deos_data

# Set the index of the Pandas DataFrame to Date
deos_data.set_index('Timestamp', inplace = True)
deos_data

# Run a describe on the dataset 
deos_data.describe()

# Locate Nov 29th 2015
# yyyy/mm/dd hh/mm
deos_data.loc['2015-11-29 23:45']

# Find the largest temperatures in the dataset
# Finding the 5 largest
deos_data['AirTemperature'].nlargest(5)

# Find the smallest temperatures in the dataset
# Finding the 5 smallest
deos_data['AirTemperature'].nsmallest(5)

# NOTE: 2015-04-07 are most likely bad values, due to equipment error or other birds on sensors

# Create own series of Air Tempereature
temp_series = deos_data['AirTemperature']

# Grabbing 1 day of temperature from new temperature series
# Not overwriting it, it is going to be equal to
temp_series = temp_series['2015-06-01' : '2015-06-02']
temp_series

# Create a plot
# Be sure to run together
plt.figure(figsize = [7,4])
plt.plot(temp_series)

# We can also do this (plot) without creating a new variable; we can do this from our original deos_data
# Create plot of Air Temperature and Dew Point and add other aspects
# Same plot as above
deos_data['AirTemperature']['2015-06-01' : '2015-06-02'].plot(color = 'red', figsize = [8,5])

# Same thing with Dew Point
# Be sure to run together
deos_data['AirTemperature']['2015-06-01' : '2015-06-02'].plot(color = 'red', figsize = [8,5])
deos_data['DewPoint']['2015-06-01' : '2015-06-02'].plot(style = '.', color = 'blue')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (Celsius)')
plt.title('DEOS Data June 01 2015')
plt.legend()

### NOTE: ON EXERCISE: be sure to use .corr function to get the correlation coefficient and add it to the plot
deos_data.corr(.....












