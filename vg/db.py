import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

# Load the CSV file
data = pd.read_csv('video_game_review.csv')  # Replace with your actual file path

# Select relevant columns for clustering
selected_columns = ['Comment Count', 'Likes Received', 'Rating/10']
features = data[selected_columns].dropna()  # Remove rows with missing values

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)  # Adjust eps and min_samples as needed
dbscan_labels = dbscan.fit_predict(X_scaled)

# Reduce dimensions to 2D using PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

# Plot the clustering result using a scatter plot
plt.figure(figsize=(8, 6))

# Plot clusters (using dbscan_labels as color code)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=dbscan_labels, cmap='viridis', marker='o')

# Highlight noise points (label = -1) in red
plt.scatter(X_2d[dbscan_labels == -1, 0], X_2d[dbscan_labels == -1, 1], c='red', marker='x', label='Noise')

# Adding titles and labels
plt.title("DBSCAN Clustering on Video Game Reviews (2D PCA)")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

# Show legend
plt.legend()

# Show the plot
plt.show()
