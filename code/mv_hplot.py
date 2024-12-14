import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

data = pd.read_csv('movie.csv')

features = data[['popularity', 'vote_average', 'vote_count']]

scaler = StandardScaler()
normalized_data = scaler.fit_transform(features)

Z = linkage(normalized_data, method='ward') #using squared Euclidean distance

plt.figure(figsize=(20, 10))
dendrogram(Z, no_labels=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()
