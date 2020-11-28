# Tyler Sharretts
# Week 02 Numpy Tutorial

### Import numpy 
import numpy as np

# Create numpy array of 3 integers
a = np.array([1, 2, 3])

# Print out a
a

# Print out number of dimensions
a.ndim

# Print out shape of array 
a.shape

# Print out data type 
a.dtype

# numpy array of 4 floats
b = np.array([1., 2., 3., 4.])

# Print out data type
b.dtype

# Print out shape of array
b.shape

# a range of values from (0) to 10
a = np.arange(10)

# a range of values from 1 to 10 (by 2) with a float 32 data 
a = np.arange(1, 10, 2, dtype ='float32')

# 5 linear spaced entries from 0 to 10
a = np.linspace(0, 10, 5)

# Convert degrees to radians 
np.radians(90)

# Convert radians to degrees 
np.degrees(1.5707963267948966)

# Declaring "not a number" values 
print(a)
a[1]
a[1] = np.nan
print(a)

### In-class exercise 
deg_list = [15, 36, 45, 88, 90]
rad_list = []

for d in deg_list:
    rad_list.append(np.radians(d))

print(rad_list)

### Numpy tutorial continued 

# Array operations (adding and multplying them together)
a = np.array([1, 2, 3])
b = np.array([6, 7, 8])

c = a + b

print(c)

c = a * b

print (c)

# Array operations (return evenly spaced numbers over a specified interval)
a = np.linspace(-np.pi, np.pi, 10)

print(a)

# Multiple dimensions (2-dimensional array with a range of 12 values with 3 rows and 4 columns)
a = np.arange(12).reshape(3, 4)
print(a)

a.ndim
a.shape
len(a)

# Can multiply the array 
a * 8

#Indexing and slicing arrays 
a = np.arange(10)
a[3]
a = np.arange(10, 20, 2)
print(a)
a[3]

# Reshaping arrays
b = np.arange(12).reshape(3, 4)
print(b)

# Slicing the array (row 1, column 2)
b[1, 2]

# Slice the a row (row 2)
b[2:,]

# Slice the column (column 2)
b[:,2]

# Returning the whole thing
b[:,:]

### In-class exercise

# Create a null vector (1-d array) of size 10 
a = np.zeros([10])

# Create a null vector (1-d array) of size 10, but with the fifth value being 1
a = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
print(a[5])

# Create a vector with values ranging from 10 to 49
a = np.arange(10,50)
print(a)
a = np.arange(10,50).reshape(5,8)
print(a)

# Reverse a vector (first elements becomes last)
a = np.arange(10,50)
print(a)
print("Array is :",a)
a_rev = a[::-1]
print("Resultant new reversed array:",a_rev)
print(a_rev)

### Numpy tutorial continued

# Logical indexing

# Selecting array elements with true / false statements and using it as a logical index 
a = np.arange(5) 
selection = np.array([True, False, False, True, True])

print(a[selection])

# Another helpful logical indexing form 
a = np.arange(5) 
print(a)
print(a[a > 2])
print(a[a >= 2])
np.nan = a[a > 2]

# Additional example 
a = np.array([34., 33., 32., 28., 28.])
np.nan = a[a < 32]
print(a)

# Masked arrays
a = np.ma.arange(12).reshape(3, 4)
print(a)

# Masking the 2nd row and 2nd column 
a[2, 2] = np.ma.masked
print(a) 

# Doing math with the masked value 
b = a * 4
print(b)

# Logical masking 
a[a > 6] = np.ma.masked
print(a)

# Unmasking an element 
a[2, 1] = 58
print(a)

### In-class exercise

# 3 x 3 matrix with values ranging from o to 8 & multiply by 2
a = np.arange(0,9)
print(a)
a = np.arange(0,9).reshape(3,3)
print(a)
b = 2 * a
print(b) 

# Masking values less than 3
a[a < 3] = np.ma.masked
print(a)

# Converting to array and masking all values greater than 1
a = np.array([-0.7, -1.5, 14, 0.3, 1, 1.8, 5])
print(a)

a[a > 1] = np.ma.masked
print(a)


