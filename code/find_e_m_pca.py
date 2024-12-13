import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Load the CSV file
data = pd.read_csv('video_game_review.csv')  # Replace with your actual file path

# Select relevant columns for clustering
selected_columns = ['Comment Count', 'Likes Received', 'Rating/10']
features = data[selected_columns].dropna()  # Remove rows with missing values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# Apply PCA to reduce the dimensions
pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization
X_pca = pca.fit_transform(X_scaled)

# Perform DBSCAN clustering

for value_eps in np.arange(0.1, 0.5, 0.1):
    for value_min in np.arange(2, 10, 2):
        dbscan = DBSCAN(eps=value_eps, min_samples=value_min)  # Adjust eps and min_samples as needed
        dbscan_labels = dbscan.fit_predict(X_pca)

        valid_points = dbscan_labels != -1
        if valid_points.sum() > 1 and len(np.unique(dbscan_labels[valid_points])) > 1:
            sil_score = silhouette_score(X_scaled[valid_points], dbscan_labels[valid_points])
            print("e:", value_eps, "minpts:", value_min, "Sil score:", sil_score)
        else:
            print("not enough valid points")

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
    #    plt.show()
