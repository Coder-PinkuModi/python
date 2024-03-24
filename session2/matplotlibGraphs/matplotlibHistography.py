#Objective is to show the histograph of the given data.

import numpy as np
import matplotlib.pyplot as plt

#Data
ages=[22, 25, 30, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80]

#Creating a histograph
plt.hist(ages, bins=5,color='skyblue',edgecolor='black') #hist meethod is used to provoke the diagram of histogram
#bins are the total histogram


#Adding labels and title 
plt.xlabel('Age') 
plt.ylabel('Frequency')
plt.title('Distribution of Ages')

#Displaying the plot 
plt.show()