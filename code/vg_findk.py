import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

data = pd.read_csv('video_game_review.csv')

selected_columns = ['Comment Count', 'Likes Received', 'Rating/10']
X = data[selected_columns].dropna()  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

for value_k in range(2, 6):
    kmeans = KMeans(n_clusters=value_k, random_state=37)
    kmeans_labels = kmeans.fit_predict(X_scaled)
    centroids = kmeans.cluster_centers_


    s_score = silhouette_score(X_scaled, kmeans_labels)
    i_score = kmeans.inertia_

    score = (100000 - i_score) * s_score
    print("K =", value_k, "Silhouette score:", s_score, "Inertia:", i_score, "overall:", score)

