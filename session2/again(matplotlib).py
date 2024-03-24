#Yet to be decoded 

import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 4, 9, 16, 25, 36])

# Fit a linear regression line
coefficients = np.polyfit(x, y, 1)
linear_fit = np.poly1d(coefficients)

# Plot the scatter plot
plt.scatter(x, y, label='Data Points')

# Plot the linear regression line
plt.plot(np.unique(x), linear_fit(np.unique(x)), label='Linear Fit', color='red')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()