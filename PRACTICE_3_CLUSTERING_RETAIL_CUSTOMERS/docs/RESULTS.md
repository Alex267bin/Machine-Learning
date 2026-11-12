# Kết quả — Lab 3

Chưa điền metrics giả định. Chạy pipeline với CSV thực tế để sinh:
- `outputs/metrics.csv`: bốn thuật toán và các metric.
- `outputs/clustering_report.json`: cấu hình, số cụm, noise, số mẫu dùng tính metric và eps sweep.
- `outputs/elbow_values.csv`, `outputs/silhouette_by_k.csv`.
- `outputs/customer_cluster_assignments.csv`: nhãn từng thuật toán.
- `outputs/cluster_profiles.csv`: profile K-Means từ dữ liệu gốc.
- `outputs/figures/`: Elbow, Silhouette, PCA 2D và dendrogram.

DBSCAN loại noise trước khi tính metric; phải đọc cột metric_samples khi so sánh.
