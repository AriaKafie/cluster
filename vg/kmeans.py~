import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

file_path = 'movie.csv'
data = pd.read_csv(file_path)

selected_columns = ['popularity', 'vote_average', 'vote_count']
X = data[selected_columns].dropna()  # drop rows with missing values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=37)
kmeans_labels = kmeans.fit_predict(X_scaled)
centroids = kmeans.cluster_centers_

distances = np.linalg.norm(X_scaled - centroids[kmeans_labels], axis=1)

#define anomalies to be at or above the 99.5th percentile
threshold = np.percentile(distances, 99.5)
anomalies = distances > threshold

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
centroids_pca = pca.transform(centroids)

plt.figure(figsize=(10, 8))

plt.scatter(X_pca[~anomalies, 0], X_pca[~anomalies, 1], c=kmeans_labels[~anomalies], cmap='viridis', s=50, alpha=0.7)

plt.scatter(X_pca[anomalies, 0], X_pca[anomalies, 1], c='red', s=100, edgecolor='black', label="Anomalies")

plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], c='blue', marker='X', s=200, label='Centroids')

plt.title("K-Means Clustering with Anomaly Highlighting (Movies)")
plt.xlabel("PCA Dimension 1")
plt.ylabel("PCA Dimension 2")
plt.legend()
plt.show()
