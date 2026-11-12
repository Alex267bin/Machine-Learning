# DBSCAN

## Purpose
Find dense customer groups without specifying the number of clusters in advance, and identify isolated observations as noise.

## Input
Standardized numeric attributes and optional one-hot Gender; parameters eps and min_samples.

## Output
Cluster labels; label -1 denotes noise. The pipeline records cluster_count, noise_count and metric_samples.

## How it works
For each point, DBSCAN examines its eps-neighborhood. Points with at least min_samples neighbors are core points. Density-reachable points are expanded into clusters; points not assigned to a cluster are noise or border points.

## Parameters in this project
Defaults: eps=0.75 and min_samples=5. A sweep tests eps from 0.3 to 1.5 in increments of 0.1.

## Evaluation caveat
Noise observations are removed before calculating silhouette, Davies–Bouldin and Calinski–Harabasz. The number of scored observations is saved. Therefore DBSCAN metrics may not use the same sample set as K-Means, PAM or Hierarchical and must be interpreted carefully.

## Strengths and limitations
Can find irregularly shaped dense groups and detect noise. Results are sensitive to eps, min_samples and distance scale; varying densities are difficult to handle.
