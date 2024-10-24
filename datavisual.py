import matplotlib.pyplot as plt
import numpy as np
var_x = np.array([3,7,15,18,29,16,14,28,35,9,21,2,23])
var_y = np.array([90,86,75,146,69,80,89,90,122,76,92,93,99])
plt.scatter(var_x, var_y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y = np.array([40, 21, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show()


#Data Discretization    example - 1

import numpy as np
from sklearn.datasets import load_iris

# Load the Iris dataset
dataset = load_iris()
a = dataset.data
b = np.zeros(150)

# Extract the 2nd column (index 1) and sort it
for i in range(150):
    b[i] = a[i, 1]
b = np.sort(b)

# Create bins
bin1 = np.zeros((30, 5))  # Mean of bins
bin2 = np.zeros((30, 5))  # Boundaries of bins
bin3 = np.zeros((30, 5))  # Median of bins

# Compute means for each bin
for i in range(0, 150, 5):
    k = i // 5
    mean = (b[i] + b[i+1] + b[i+2] + b[i+3] + b[i+4]) / 5
    for j in range(5):
        bin1[k, j] = mean
print("Bin Mean: \n", bin1)

# Compute boundaries for each bin
for i in range(0, 150, 5):
    k = i // 5
    for j in range(5):
        if (b[i+j] - b[i]) < (b[i+4] - b[i+j]):
            bin2[k, j] = b[i]
        else:
            bin2[k, j] = b[i+4]
print("Bin Boundaries: \n", bin2)

# Compute medians for each bin
for i in range(0, 150, 5):
    k = i // 5
    median = b[i + 2]  # For a sorted list of length 5, the median is at index 2
    for j in range(5):
        bin3[k, j] = median
print("Bin Median: \n", bin3)


#Data Discretization    example - 2

import pandas as pd
import numpy as np

# Sample continuous data
data = {'Age': [22, 25, 47, 35, 46, 56, 48, 55, 4, 21]}
df = pd.DataFrame(data)

# Define the number of bins and the bin edges
bins = [0,18,35,50,100]
labels = ['Child', 'Young Adult', 'Adult', 'Senior']

# Apply discretization using pd.cut
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Display the original data and the new Age Group column
print(df)

