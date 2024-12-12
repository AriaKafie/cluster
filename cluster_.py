
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

file_path = 'out.csv'
data = pd.read_csv(file_path)

# Drop rows with missing values in numerical columns to maintain alignment
data_clean = data.dropna(subset=['release_date', 'popularity', 'vote_average', 'vote_count'])
numerical_columns = ['release_date', 'popularity', 'vote_average', 'vote_count']
numerical_data = data_clean[numerical_columns]

# Scale the numerical data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)

# Perform clustering and detect anomalies
for k in range(2, 5):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)

    # Calculate distances of each point to its nearest cluster center
    distances = kmeans.transform(scaled_data).min(axis=1)

    # Set a threshold based on the 95th percentile of distances
    threshold = np.percentile(distances, 95)

    # Assign anomalies based on the threshold
    data_clean['is_anomaly'] = distances > threshold

    # Output the anomalies for the current value of k
    anomalies = data_clean[data_clean['is_anomaly']]

    print(f"Results from K = {k}")
    print(anomalies)
