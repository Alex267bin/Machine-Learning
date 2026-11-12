# Project Design — Retail Customer Clustering

## WHAT
A Python analysis pipeline for customer segmentation with four clustering approaches, internal metrics, parameter exploration and descriptive profiles. A separate command-line tool demonstrates K-Means color quantization on an image.

## WHY
The dataset has no target labels, so supervised classification is inappropriate. Comparing centroid-, medoid-, density- and hierarchy-based methods shows how assumptions affect discovered groups. Scaling is necessary because age, income and spending score use different numeric ranges.

## HOW — customer pipeline
```text
Mall_Customers.csv
       |
       v
Column validation + type conversion
       |
       v
Remove incomplete rows + duplicates
       |
       v
StandardScaler (numeric)
+ optional OneHotEncoder (Gender)
       |
       v
K-Means sweep: k = 2 ... max-k
       |
       +--> Elbow / Inertia
       +--> Silhouette by k
       |
       v
Select k with highest silhouette
       |
       +--> K-Means
       +--> PAM K-Medoids
       +--> DBSCAN (eps, min_samples)
       +--> Agglomerative Ward
       |
       v
Metrics + assignments + profiles
       |
       v
PCA plot + Ward dendrogram + JSON report
```

## HOW — image segmentation extension
```text
Input image -> RGB -> resize -> flatten pixels (N x 3)
           -> K-Means -> pixel cluster labels
           -> replace each pixel by its centroid RGB
           -> save segmented image + comparison plot
```

## Design decisions
- CustomerID is an identifier and is not included as a feature.
- Numeric attributes are standardized; Gender is optional and one-hot encoded.
- K-Means uses `n_init=20`, fixed random state and silhouette search.
- PAM uses Euclidean pairwise distances and exhaustive medoid swaps; the implementation caps input at 5,000 rows to constrain its O(n²) distance matrix.
- DBSCAN exposes eps/min_samples and sweeps eps from 0.3 to 1.5.
- DBSCAN noise (-1) is excluded from internal metrics; noise count and metric sample count remain visible.
- Profiles are calculated from original values, not standardized values.
- Ward dendrogram is drawn on a reproducible sample of at most 100 observations.
- Image segmentation downsizes the image to a maximum side length to limit computation.

## Modules
- `scripts/cluster.py`: customer data pipeline and reports.
- `scripts/image_segmentation.py`: RGB image segmentation.
- `notebooks/03_customer_clustering.ipynb`: guided analysis.
- `outputs/`: generated tables, JSON and figures.
- `logs/`: runtime log.

## Interpretation risks
Silhouette-based k selection is a heuristic, not proof of the true number of customer types. DBSCAN scores are computed on its non-noise subset and therefore are not directly identical-sample comparisons. PCA is a 2D visualization, not the clustering space itself. Do not assign marketing personas without examining the actual profiles.
