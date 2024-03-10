# Import the required libraries
import matplotlib.pyplot as plt #import matplotlib.pyplot as plt: This line imports the matplotlib.pyplot module and gives it the alias plt. This module provides a MATLAB-like plotting framework in Python.
import numpy as np #import numpy as np: This line imports the numpy library and gives it the alias np. Numpy is used for numerical operations and is often employed in conjunction with Matplotlib.

# Define the x and y coordinates for the points to be plotted
x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]

# Plot the points using red circles ('ro')
plt.plot(x, y, 'ro')

# Set the axis limits for the plot (xmin, xmax, ymin, ymax)
plt.axis([0, 6, 0, 35])

# regression line
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

# Display the plot in a new figure window
plt.show()

