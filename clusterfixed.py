import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

file_path = 'out.csv'
data = pd.read_csv(file_path)

numerical_columns = ['release_date', 'popularity', 'vote_average', 'vote_count']
numerical_data = data[numerical_columns]

# Check for missing values
print(numerical_data.isnull().sum())

# Handle missing values (e.g., fill with mean or drop rows)
numerical_data = numerical_data.fillna(numerical_data.mean())  # Or use .dropna() if you prefer

if numerical_data.empty:
    print("No data available after handling missing values.")
else:
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numerical_data)

    for k in range(2, 5):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled_data)

        cluster_centers = kmeans.cluster_centers_
        distances = kmeans.transform(scaled_data).min(axis=1)

        threshold = np.percentile(distances, 95)

        data['is_anomaly'] = distances > threshold

        anomalies = data[data['is_anomaly']]

        print("Results from K =", k)
        print(anomalies)
