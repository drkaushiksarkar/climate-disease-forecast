from sklearn.cluster import KMeans
import pandas as pd

def cluster_hotspots(df, target):
    df = df.groupby(['lat', 'lon'])[target].mean().reset_index()
    kmeans = KMeans(n_clusters=3)
    df['cluster'] = kmeans.fit_predict(df[['lat', 'lon', target]])
    return df