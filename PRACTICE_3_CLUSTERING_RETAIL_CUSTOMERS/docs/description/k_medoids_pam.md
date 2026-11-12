# K-Medoids — PAM

## Purpose
Partition customers around representative observed customers (medoids), rather than arithmetic centroids.

## Input / Output
Input is the same transformed feature matrix as other clustering methods. Output is a cluster label per row and the selected medoid row indices.

## How it works
The implementation initializes k distinct medoids, assigns each point to its nearest medoid, then tests swaps between each current medoid and non-medoid candidates. A swap is retained when it reduces total distance. It stops when no improving swap is found or max_iter is reached.

## Implementation details
This repository contains a custom, straightforward PAM-style implementation using Euclidean distances, max_iter=100 and a fixed random seed. It materializes an n × n distance matrix and rejects more than 5,000 rows.

## Evaluation
Uses silhouette, Davies–Bouldin and Calinski–Harabasz on the resulting labels.

## Strengths and limitations
Medoids are actual observations and can be more robust to extreme values than means. Exhaustive swaps and the pairwise distance matrix are expensive for large datasets. The current implementation is intended for the small Mall Customers dataset.
