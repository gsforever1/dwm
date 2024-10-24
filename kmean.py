import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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

# Define the number of clusters
k = 3

# Create the KMeans model
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)

# Add cluster labels to the original data
df['Cluster'] = kmeans.labels_

# Display the clustered data
print(df)

# Optional: Visualize the clusters (if 2D)
plt.scatter(df['Age'], df['Account Balance'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Account Balance')
plt.title('K-Means Clustering of Bank Customers')
plt.show()
