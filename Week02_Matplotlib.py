# Tyler Sharretts 
# Week 03 Matplotlib Tutorial 

### Import Matplotlib 
import matplotlib.pyplot as plt
import numpy as np

### The "easy" way

# Defining the x and y
x = np.arange(0,100,0.01)
y1 = np.cos(x)
y2 = np.sin(x)

# 3 different plots and their labels (run first two separately and then last one all at same time)
plt.plot(x, y1, label = 'cos(x)')
plt.plot(x, y2, label = 'sin(x)')
plt.axhline(y = 0, color = 'k')

# Another plot (run all at once)
plt.plot(x, y1, label = 'cos(x)')
plt.plot(x, y2, label = 'sin(x)')
plt.axhline(y = 0, color = 'k')
plt.xlim([0, 10])

# Adding in labels, titles, grids, and legends (run all at once)
plt.plot(x, y1, label = 'cos(x)')
plt.plot(x, y2, label = 'sin(x)')
plt.axhline(y = 0, color = 'k')
plt.xlim([0, 10])
plt.xlabel("x")
plt.ylabel("y")
plt.title("$sin(x)$ & $cos(x)$")
plt.grid()
plt.legend()

# End the plotting instance by closing it
plt.close()

### The "customizable" way

# Create sample data 
x = np.linspace(0, 2, 100)

# Explicitly create a figure and axes as OBJECTS 
fig, ax = plt.subplots(1, 1)

# Plot x variable on the x-axis and x^2 on the y-axis 
ax.plot(x, x**2)

# Add labels to the plot 
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Reprint fig
print(fig)

# Add a title with latex syntax 
ax.set_title('$y = x^2$', fontdict = {'size': 22})
print(fig)

# Figure size (inches & resolution)
fig, ax = plt.subplots(figsize=(6,4), dpi = 100)

# Plot of set of different plynomials
# The label argument is used when generating a legend 
ax.plot(x, x, label = '$x$')
ax.plot(x, x * x, label = '$x^2$')
ax.plot(x, x**3, label = '$x^3$')

# Add labels and title 
ax.set_xlabel('x')
ax.set_ylabel('f(x')
ax.set_title('Polynomials')

# Add gridlines 
ax.grid(True)

# Add a legend to the upper left corner of the plot
ax.legend(loc = 'upper left')
print(fig)

# Save with a path 
fig.savefig("chosen_path")

### In-class plotting exercise

# Creat range of numbers using Numpy 
x = np.arange(0,29,1)
deg_c = np.arange(0, 29, 1, dtype = 'float32')
deg_f = (deg_c * 9/5) + 32

# Plot parameters (run all at once)
plt.scatter(x, deg_c)
plt.scatter(x, deg_f)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.ylim(0,100)
