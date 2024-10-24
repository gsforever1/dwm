import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Sample data: Customer data with features like Age, Account Balance, and Transaction Frequency
data = {
    'Age': [22, 45, 35, 29, 50, 62, 39, 27, 41, 55],
    'Account Balance': [1500, 25000, 18000, 3000, 50000, 60000, 20000, 8000, 40000, 10000],
    'Transaction Frequency': [5, 15, 10, 2, 20, 25, 12, 3, 18, 7]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Standardizing the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Perform hierarchical clustering
linked = linkage(scaled_data, method='ward')

# Create a dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Customer Index')
plt.ylabel('Distance')
plt.show()

# Forming clusters
num_clusters = 3
clusters = fcluster(linked, num_clusters, criterion='maxclust')

# Add cluster labels to the original data
df['Cluster'] = clusters

# Convert to NumPy array for output
output_array = df.to_numpy()

# Display the clustered data as a NumPy array in the terminal
print("Clustered Customer Data (as NumPy Array):")
print(output_array)
