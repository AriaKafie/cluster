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

"""

# Perform hierarchical clustering
Z = linkage(normalized_data, method='ward')  # Use 'ward', 'complete', 'single', etc.

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z, labels=data.index, leaf_rotation=90, leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.savefig('images/hplot.png')
"""

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(normalized_data)

# Perform hierarchical clustering on reduced data
Z_reduced = linkage(reduced_data, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z_reduced, labels=data.index, leaf_rotation=90, leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram (PCA Reduced)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.savefig('images/hplot_reduced.png')
plt.show()
