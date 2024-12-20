import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('movie.csv')

# Select relevant columns for clustering (replace with actual column names)
# For demonstration, assuming 'Feature1' and 'Feature2' are numeric columns
features = data[['popularity', 'vote_average', 'vote_count']]

# Normalize the features
scaler = StandardScaler()
normalized_data = scaler.fit_transform(features)

# Perform hierarchical clustering
Z = linkage(normalized_data, method='ward')  # Use 'ward', 'complete', 'single', etc.

plt.figure(figsize=(20, 10))
dendrogram(Z, no_labels=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.savefig('images/hplot.png')
"""
# Plot the dendrogram
plt.figure(figsize=(10, 7))
#dendrogram(Z, labels=data.index, leaf_rotation=90, leaf_font_size=10)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()
"""
