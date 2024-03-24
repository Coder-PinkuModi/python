import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    'sex': ['Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting
df['sex'].value_counts().plot(kind='barh', color='lightgreen')
plt.xlabel('Frequency')
plt.ylabel('Sex')
plt.title('Distribution of Sex')

#to view the graph
plt.show()
