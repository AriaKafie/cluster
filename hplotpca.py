import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

# Load the CSV file
data = pd.read_csv('movie.csv')

# Select relevant columns for clustering (replace with actual column names)
# For demonstration, assuming 'Feature1' and 'Feature2' are numeric columns
features = data[['popularity', 'vote_average', 'vote_count']]

# Normalize the features
scaler = StandardScaler()
normalized_data = scaler.fit_transform(features)

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(normalized_data)

# Perform hierarchical clustering on reduced data
Z_reduced = linkage(reduced_data, method='ward')

plt.figure(figsize=(20, 10))
dendrogram(Z_reduced, no_labels=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.savefig('images/hplotpca.png')

