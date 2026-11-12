# K-Means

## Purpose
Partition customers into k groups around feature-space centroids.

## Input
Standardized Age, Annual Income and Spending Score, plus optional one-hot Gender.

## Output
One integer cluster label per customer, inertia, silhouette score, profiles and PCA visualization.

## How it works
1. Initialize k centroids.
2. Assign each observation to its nearest centroid.
3. Recompute each centroid as the mean of assigned observations.
4. Repeat assignment and update until convergence.

## Parameters in this project
The script tests k from 2 to min(max_k, n-1), uses n_init=20 and random_state=42, then selects the k with the highest silhouette score in that range.

## Evaluation
Silhouette is used for k exploration; final algorithm comparison also records Davies–Bouldin and Calinski–Harabasz.

## Strengths and limitations
Efficient and easy to interpret, but requires k and favors compact, roughly spherical groups. Results depend on scaling and initialization. Cluster IDs have no intrinsic ordering.
