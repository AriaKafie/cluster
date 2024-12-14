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

for value_eps in np.arange(0.1, 0.5, 0.1):
    for value_min in np.arange(2, 10, 2):
        dbscan = DBSCAN(eps=value_eps, min_samples=value_min)
        dbscan_labels = dbscan.fit_predict(X_scaled)

        valid_points = dbscan_labels != -1
        if valid_points.sum() > 1 and len(np.unique(dbscan_labels[valid_points])) > 1:
            sil_score = silhouette_score(X_scaled[valid_points], dbscan_labels[valid_points])
            print("e:", value_eps, "minpts:", value_min, "Sil score:", sil_score)
        else:
            print("not enough valid points")


