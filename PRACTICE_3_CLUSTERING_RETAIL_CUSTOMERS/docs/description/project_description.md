# Project Description — Retail Customer Clustering

## 1. Purpose
Explore customer groups using demographic and spending attributes, compare clustering algorithms, and summarize cluster characteristics to support descriptive customer segmentation.

## 2. Problem definition
- **Type:** unsupervised learning; no ground-truth class labels.
- **Dataset:** Mall Customers CSV supplied separately; source and license must be recorded by the user.
- **Observation:** one customer row.
- **Features:** Age, Annual Income, Spending Score, and optionally Gender.
- **Output:** cluster label per algorithm, internal validation metrics, cluster profiles, and visual diagnostics.

## 3. Input and output
Input CSV must contain `Gender`, `Age`, `Annual Income (k$)` (or accepted capitalization), and `Spending Score (1-100)` (or accepted en-dash variant). CustomerID may be present but is not used as a clustering feature.

Outputs include metrics, DBSCAN parameter sweep, per-customer assignments, K-Means profiles, elbow/silhouette tables, PCA visualization, Ward dendrogram, and JSON run summary.

## 4. Algorithms
1. K-Means — centroid-based partitioning; k selected by highest silhouette in the tested range.
2. K-Medoids (PAM) — custom Partitioning Around Medoids implementation using Euclidean pairwise distances.
3. DBSCAN — density-based clusters with noise label -1.
4. Hierarchical Agglomerative — Ward linkage with selected k.

## 5. Preprocessing
Numeric features are median-imputed and standardized. Gender is optionally most-frequent-imputed and one-hot encoded. The `--without-gender` option allows checking how gender inclusion changes the grouping.

## 6. Evaluation and interpretation
Silhouette, Davies–Bouldin and Calinski–Harabasz are computed on non-noise observations for DBSCAN. The report records the metric sample count and noise count. K-Means profiles are computed from original, unscaled attributes. Cluster labels are arbitrary identifiers, not ranked customer quality.

## 7. Image segmentation extension
A separate script applies K-Means to RGB pixel vectors, replacing each pixel with its cluster-centroid color. This is color quantization, not semantic object recognition.

## 8. Limitations
Clustering is exploratory and depends on scaling, feature choice, distance metric and parameters. The sample Mall dataset is small. DBSCAN metrics may use fewer observations than other algorithms because noise is excluded. A cluster profile is descriptive and does not prove a causal customer persona.

## 9. Acceptance checklist
- [ ] Correct source CSV and license/source details recorded.
- [ ] Required columns and row cleaning checked.
- [ ] Numeric scaling and optional Gender encoding documented.
- [ ] Four clustering methods run and assignments saved.
- [ ] DBSCAN noise and metric sample count reported.
- [ ] Profiles use original-scale data.
- [ ] Image segmentation uses an authorized image and is described as RGB clustering.
