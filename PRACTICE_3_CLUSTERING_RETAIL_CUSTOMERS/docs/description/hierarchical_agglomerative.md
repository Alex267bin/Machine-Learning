# Hierarchical Agglomerative Clustering — Ward

## Purpose
Build a hierarchy of nested customer clusters and produce a flat partition with the selected k.

## Input / Output
Uses the transformed feature matrix. The estimator outputs one cluster label per customer. A separate Ward linkage matrix is computed for a dendrogram visualization.

## How it works
Agglomerative clustering starts with each observation as its own cluster and repeatedly merges clusters. Ward linkage chooses merges that minimize the increase in within-cluster sum of squares.

## Parameters in this project
AgglomerativeClustering uses n_clusters equal to the K-Means silhouette-selected k and linkage="ward". The dendrogram uses scipy linkage(method="ward") on a reproducible sample of at most 100 rows.

## Evaluation
Silhouette, Davies–Bouldin and Calinski–Harabasz on the final labels.

## Strengths and limitations
The hierarchy can reveal nested structure and the dendrogram helps explain merge distances. Standard agglomerative clustering is computationally more demanding than K-Means for larger datasets and Ward is tied to Euclidean geometry.
