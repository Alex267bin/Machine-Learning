# Câu hỏi vấn đáp — Lab 3

## Input / Output / Purpose
- **Input:** Age, Annual Income, Spending Score, Gender.
- **Output:** cluster label cho từng khách hàng và profile thống kê từng cụm.
- **Purpose:** khám phá nhóm khách hàng tương đồng, không dự đoán nhãn có sẵn.

## Câu hỏi nền tảng
1. **Clustering là gì?** Unsupervised learning vì không có target label.
2. **Vì sao bỏ CustomerID?** Mã định danh không thể hiện hành vi.
3. **StandardScaler?** Trừ mean rồi chia standard deviation.
4. **Vì sao scaling?** Thuật toán dựa trên khoảng cách; biến có scale lớn có thể chi phối.
5. **Gender encoding?** One-Hot biến categorical thành cột nhị phân, không áp thứ tự giả.
6. **K-Means hoạt động?** Gán điểm vào centroid gần nhất, cập nhật centroid bằng mean, lặp đến hội tụ.
7. **Inertia?** Tổng bình phương khoảng cách tới centroid; thường giảm khi tăng k.
8. **K-Medoids khác K-Means?** Medoid là quan sát thật; centroid là mean có thể không phải điểm thật. PAM thường tốn tài nguyên hơn.
9. **DBSCAN parameters?** eps là bán kính; min_samples là số điểm tối thiểu để tạo vùng mật độ.
10. **DBSCAN có cần k?** Không, số cụm được hình thành từ mật độ.
11. **Noise -1?** Điểm không thuộc cụm nào theo eps/min_samples.
12. **Hierarchical Agglomerative?** Bắt đầu mỗi điểm là một cụm rồi lần lượt gộp cụm gần nhau.
13. **Ward linkage?** Chọn phép gộp làm tăng phương sai nội cụm ít nhất.
14. **Silhouette?** So sánh độ gần trong cụm và cụm gần nhất khác; gần 1 thường tốt, gần 0 là ranh giới, âm có thể gán sai.
15. **Davies-Bouldin / Calinski-Harabasz?** DB thấp thường tốt; CH cao thường tốt.
16. **Vì sao ghi metric_samples?** DBSCAN loại noise trước khi tính metric nên số mẫu khác thuật toán khác.
17. **PCA dùng làm gì?** Chiếu dữ liệu nhiều chiều xuống 2D để trực quan hóa, không thay thế clustering.
18. **Dendrogram?** Cây gộp cụm; chiều cao thể hiện khoảng cách tại bước gộp.
19. **Có thể tự đặt tên VIP?** Không trước khi xem profile; cần căn cứ số liệu cụm.
20. **Image segmentation có hiểu vật thể không?** Không; đây là clustering màu RGB pixel, không phải semantic segmentation.

## Câu hỏi xoáy
- Silhouette cao nhất luôn là k tốt nhất? Không; cần thêm Elbow, độ ổn định và khả năng diễn giải.
- DBSCAN toàn noise hoặc một cụm? Silhouette không hợp lệ; xem scaling và điều chỉnh eps/min_samples có cơ sở.
- Vì sao K-Means nhạy outlier? Mean/centroid bị kéo bởi giá trị cực đoan.
- Vì sao PAM có giới hạn dữ liệu? Bản triển khai tạo ma trận khoảng cách n×n.
