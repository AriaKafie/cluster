import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

data = pd.read_csv('movie.csv')

features = data[['popularity', 'vote_average', 'vote_count']]

scaler = StandardScaler()
normalized_data = scaler.fit_transform(features)

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(normalized_data)

Z_reduced = linkage(reduced_data, method='ward')

plt.figure(figsize=(20, 10))
dendrogram(Z_reduced, no_labels=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

