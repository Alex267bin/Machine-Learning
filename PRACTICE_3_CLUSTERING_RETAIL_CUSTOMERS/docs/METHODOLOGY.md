# Phương pháp — Practice 3

## Tiền xử lý
Bỏ CustomerID; xử lý missing; one-hot encode Gender; StandardScaler cho biến số. StandardScaler trừ mean và chia standard deviation để các thang đo không chi phối khoảng cách.

## Thuật toán
- **K-Means** — Input: ma trận đặc trưng và k. Output: nhãn và centroid. Lặp gán điểm vào centroid gần nhất, cập nhật mean. Nhanh; nhạy outlier/khởi tạo.
- **K-Medoids** — tâm là quan sát thực (medoid), tối ưu tổng khoảng cách. Bền hơn với outlier; tính toán tốn kém hơn. Phụ thuộc scikit-learn-extra.
- **DBSCAN** — dùng eps và min_samples để tìm vùng mật độ cao; điểm thưa gán noise -1. Không cần k; nhạy tham số và scaling.
- **Hierarchical/Agglomerative** — khởi đầu mỗi điểm là cụm, lần lượt gộp theo linkage; dendrogram biểu diễn quan hệ phân cấp. Trực quan nhưng tốn bộ nhớ với dữ liệu lớn.

Elbow theo inertia; Silhouette cao hơn thường tốt; Davies–Bouldin thấp hơn tốt; Calinski–Harabasz cao hơn tốt. Metric cần ít nhất 2 cụm và ít hơn số mẫu. Với DBSCAN bỏ noise trước khi tính. PCA chiếu dữ liệu xuống 2D để trực quan, không thay đổi clustering.
