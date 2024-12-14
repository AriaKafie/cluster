from sklearn.metrics import silhouette_score
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('movie.csv')


features = data[['popularity', 'vote_average', 'vote_count']]

scaler = StandardScaler()
normalized_data = scaler.fit_transform(features)

Z = linkage(normalized_data, method='ward')

num_clusters = 3
cluster_labels = fcluster(Z, num_clusters, criterion='maxclust')

sil_score = silhouette_score(normalized_data, cluster_labels)
print(f"Silhouette Score: {sil_score:.4f}")

centroids = np.array([normalized_data[cluster_labels == i].mean(axis=0) for i in range(1, num_clusters + 1)])

inertia = sum(
    np.sum((normalized_data[cluster_labels == i] - centroids[i - 1]) ** 2)
    for i in range(1, num_clusters + 1)
)
print(f"Inertia: {inertia:.4f}")
score = (100000 - inertia) * sil_score
print("overall:", score)
