import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

data = pd.read_csv('video_game_review.csv')

selected_columns = ['Comment Count', 'Likes Received', 'Rating/10']
features = data[selected_columns].dropna()


scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

value_eps = 0.4
value_min = 2

dbscan = DBSCAN(eps=value_eps, min_samples=value_min) 
dbscan_labels = dbscan.fit_predict(X_scaled)


pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)


plt.figure(figsize=(8, 6))

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=dbscan_labels, cmap='viridis', marker='o')


plt.scatter(X_2d[dbscan_labels == -1, 0], X_2d[dbscan_labels == -1, 1], c='red', marker='x', label='Noise')

plt.title("DBSCAN Clustering on Video Game Reviews (2D PCA)")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.legend()

plt.show();
