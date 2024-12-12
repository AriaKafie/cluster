import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

file_path = 'movie.csv'
data = pd.read_csv(file_path)

# specify columns (numerical only)
numerical_columns = ['popularity', 'vote_average', 'vote_count']
numerical_data = data[numerical_columns]

# skip lines with missing values
numerical_data = numerical_data.dropna()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)

# implement Principal component analysis (PCA) to reduce deminsionality
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

for k in range(2, 5):
    hierarchical = AgglomerativeClustering(n_clusters=k, linkage='ward')
    labels = hierarchical.fit_predict(pca_data)
    
    cluster_centers = [pca_data[labels == i].mean(axis=0) for i in range(k)]
    
    distances = np.min(
        np.array([np.linalg.norm(pca_data - center, axis=1) for center in cluster_centers]).T,
        axis=1
    )

    threshold = np.percentile(distances, 95)
    data['is_anomaly'] = distances > threshold

    anomalies = data[data['is_anomaly']]
    print(f"Results from Hierarchical Clustering with K = {k}")
    print(anomalies)
