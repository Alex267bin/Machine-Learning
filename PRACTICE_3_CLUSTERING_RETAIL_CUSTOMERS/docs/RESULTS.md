# Kết quả — Lab 3: Clustering Retail Customers

## 1. Cấu hình thí nghiệm

- Dataset: Mall Customers
- Số quan sát: 200
- Đặc trưng số: Age, Annual Income, Spending Score
- Scaling: StandardScaler
- So sánh hai cấu hình:
  - Có Gender: sử dụng One-Hot Encoding.
  - Không Gender: chỉ sử dụng ba đặc trưng số.
- Phạm vi khảo sát K-Means: k = 2 đến 15.
- K được chọn theo Silhouette Score cao nhất trong phạm vi khảo sát.

## 2. Kết quả khi có Gender

| Algorithm | Clusters | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---|---:|---:|---:|---:|
| K-Means | 13 | 0.3910 | 0.9361 | 78.21 |
| K-Medoids | 13 | 0.3617 | 0.9715 | 72.48 |
| DBSCAN | 7 | 0.1707 | 1.0296 | 30.99 |
| Hierarchical Ward | 13 | 0.3815 | 0.9175 | 74.71 |

DBSCAN sử dụng 174 mẫu để tính metric sau khi loại 26 điểm noise.

## 3. Kết quả khi không có Gender

| Algorithm | Clusters | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---|---:|---:|---:|---:|
| K-Means | 6 | 0.4274 | 0.8277 | 135.10 |
| K-Medoids | 6 | 0.4253 | 0.8337 | 134.71 |
| DBSCAN | 1 | N/A | N/A | N/A |
| Hierarchical Ward | 6 | 0.4201 | 0.8521 | 127.99 |

DBSCAN với eps = 0.75 tạo một cụm và 10 điểm noise. Vì chỉ có một cụm nên các metric đánh giá phân cụm không được tính.

## 4. Phân tích kết quả

### K-Means

- Khi có Gender, Silhouette là 0.3910.
- Khi không có Gender, K-Means chọn k = 6 với Silhouette = 0.4274.
- Trong phạm vi k = 2 đến 15, k = 6 có Silhouette cao nhất.
- Kết quả cho thấy cấu hình không sử dụng Gender phân tách dữ liệu tốt hơn theo các metric đang xét.

### K-Medoids

K-Medoids đạt Silhouette = 0.4253 khi không có Gender, khá gần K-Means (0.4274). K-Medoids sử dụng medoid là một quan sát thực tế làm đại diện cụm, trong khi K-Means sử dụng centroid là giá trị trung bình.

### DBSCAN

DBSCAN nhạy với tham số eps. Trong cấu hình không có Gender:

| eps | Số cụm | Noise | Silhouette |
|---:|---:|---:|---:|
| 0.3 | 10 | 134 | 0.5144 |
| 0.4 | 6 | 98 | 0.5190 |
| 0.5 | 6 | 60 | 0.4817 |
| 0.6 | 2 | 28 | 0.2730 |
| 0.75 | 1 | 10 | N/A |

Không thể kết luận eps = 0.4 là tốt nhất chỉ dựa trên Silhouette vì có 98/200 điểm bị loại khỏi phép tính metric. Cần xem đồng thời số cụm, tỷ lệ noise và số mẫu được đánh giá.

### Hierarchical Clustering

Hierarchical Ward với k = 6 đạt Silhouette = 0.4201 khi không có Gender. Kết quả khá gần K-Means và K-Medoids.

## 5. Phân tích 6 cụm K-Means không có Gender

| Cluster | Customers | Mean Age | Mean Income | Mean Spending |
|---|---:|---:|---:|---:|
| 0 | 33 | 41.94 | 88.94 | 16.97 |
| 1 | 45 | 56.33 | 54.27 | 49.07 |
| 2 | 24 | 25.25 | 25.83 | 76.92 |
| 3 | 39 | 32.69 | 86.54 | 82.13 |
| 4 | 38 | 26.68 | 57.58 | 47.79 |
| 5 | 21 | 45.52 | 26.29 | 19.38 |

Tổng số khách hàng trong sáu cụm là 200.

Nhận xét:

- Cluster 0: thu nhập trung bình cao, điểm chi tiêu thấp.
- Cluster 1: độ tuổi trung bình cao nhất, thu nhập và chi tiêu ở mức trung bình.
- Cluster 2: khách hàng trẻ, thu nhập thấp, điểm chi tiêu cao.
- Cluster 3: thu nhập và điểm chi tiêu đều cao.
- Cluster 4: khách hàng trẻ, thu nhập và điểm chi tiêu ở mức trung bình.
- Cluster 5: thu nhập và điểm chi tiêu thấp.

Đây là mô tả dựa trên giá trị trung bình của từng cụm, không phải nhãn phân loại có sẵn.

## 6. Kết luận

Trong thí nghiệm này, K-Means không sử dụng Gender là cấu hình có kết quả tốt nhất trong các thuật toán phân cụm có metric hợp lệ trên toàn bộ dữ liệu. Cấu hình chọn được k = 6 với Silhouette = 0.4274.

DBSCAN cho thấy ảnh hưởng đáng kể của eps và số lượng noise. Vì vậy, cần đánh giá DBSCAN bằng cả chất lượng cụm và tỷ lệ dữ liệu được phân cụm, không chỉ dựa trên Silhouette.

Lưu ý: các metric DBSCAN được tính sau khi loại noise, do đó không hoàn toàn so sánh trực tiếp với metric của các thuật toán sử dụng đủ 200 mẫu.
