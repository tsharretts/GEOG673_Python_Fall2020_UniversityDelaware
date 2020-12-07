# Tyler Sharretts
# Week 04: Pandas Assignment

### Importing modules
import pandas as pd
import matplotlib.pyplot as plt

### Preliminary setup

# Load in DEOS dataset
deos_data = pd.read_csv('/Users/tshar/Documents/GEOG_673/geog473-673-master/geog473-673-master/datasets/DEOS.csv')

# Check data
deos_data
deos_data.columns
type(deos_data)

# Replace all column names by overwriting the columns attribute
deos_cols = ['Timestamp', 'AirTemperature', 'DewPoint', 'WindSpeed', 'WindDirection', 'BarometricPressure', 'SolarRadiation', 'WindGust', 'GagePrecipitation']

# Replace names of columns with deos columns list
deos_data.columns =  deos_cols

# Double check
deos_data

# Set the index of the Pandas Data Frame to Date
deos_data.set_index('Timestamp', inplace = True)
deos_data

# Run a describe on the dataset
deos_data.describe()

### Question 1
### Subset the dataset to October 2015 within the data
### For Wind Speed & Wind Gust
### yyyy/mm/dd hh/mm

# Create own series of Wind Gust & Wind Speed
WindGust_series = deos_data['WindGust']
WindSpeed_series = deos_data['WindSpeed']

# Extracting October 2015 from the new Wind Gust & Wind Speed series
WindGust_series = WindGust_series['2015-10-01' : '2015-11-01']
WindSpeed_series = WindSpeed_series['2015-10-01' : '2015-11-01']

# Double check
WindGust_series
WindSpeed_series

### Question 2
### Convert Wind Gust & Wind Speed from m/s to mph
### 1 m/s = 2.23694 mph

# Convert Wind Gust & Wind Speed
Oct2015_WindGust = WindGust_series * 2.23694
Oct2015_WindSpeed = WindSpeed_series * 2.23694

# Double check 
Oct2015_WindGust
Oct2015_WindSpeed

### Question 3
### Plotting Wind Gust & Wind Speed on the same plot
### Wind Gust as points; Wind Speed as lines
### Add legend
### Compute correlation coefficient berween Wind Gust and Wind Speed (using Pandas.dataframe.corr function)
### Add title to the plot

# Plotting
Oct2015_WindGust.plot(style = '.', color = 'red')
Oct2015_WindSpeed.plot(color = 'blue')
plt.xlabel('Timestamp')
plt.ylabel('Wind Gust & Wind Speed (in mph)')
plt.title('Oct 2015 Wind Gust and Wind Speed with a Correlation Coefficient of 0.98')
plt.legend()

# Calculate Correlation Coefficients
Oct2015_WindGust.corr(Oct2015_WindSpeed)
Oct2015_WindSpeed.corr(Oct2015_WindGust)


