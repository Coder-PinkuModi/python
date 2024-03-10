# Pandas is a powerful data manipulation and analysis library for Python. Some of its key features include:

# DataFrame: Pandas introduces the DataFrame data structure, which is a two-dimensional, tabular data structure with labeled axes (rows and columns). It's similar to a spreadsheet or SQL table.

# Data Manipulation: Pandas provides a wide range of functions for data manipulation, including filtering, grouping, merging, reshaping, and more.

# Data Cleaning: It allows for handling missing data, converting data types, and other data cleaning operations.

# Data Analysis: Pandas supports various statistical and mathematical operations on data, making it suitable for data analysis tasks.

# Here's a simple example of using Pandas:

# Importing the Pandas library and aliasing it as 'pd'

import pandas as pd

# Creating a dictionary with sample data
data = {'Name': ['Alice', 'Bob', 'Charlie','Deepak','Pinku','Prince'],
        'Age': [25, 30, 22, 42, 50, 54],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Moon', 'Earth', 'Mars']}

# Creating a DataFrame from the dictionary dF is a variable
dF = pd.DataFrame(data)

# Displaying the DataFrame
print(dF)


#OUTPUT: 

#        Name  Age           City
#  0    Alice   25       New York
#  1      Bob   30  San Francisco
#  2  Charlie   22    Los Angeles
#  3   Deepak   42           Moon
#  4    Pinku   50          Earth
#  5   Prince   54          Mars