# Tài liệu tham khảo — Lab 3: Clustering Retail Customers

Ngày truy cập: 2026-11-12.

## Dataset
- Data UAB — Mall Customer Segmentation teaching notebook: https://datauab.github.io/mall_segmentation/
- University of Catania — Statistical Laboratory, Mall Customers: https://www.dmi.unict.it/ortis/StatsLab/2022-2023/Notebooks/Statistical%20Laboratory%20-%20Mall%20Customers.html

Các tài liệu trên mô tả bản Mall Customers phổ biến với 200 quan sát và các trường CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100). Đây là tài liệu tham khảo thứ cấp; cần lưu URL và license của đúng bản CSV tải về.

## Thuật toán và đánh giá
- scikit-learn — Clustering overview: https://scikit-learn.org/stable/modules/clustering.html
- scikit-learn — DBSCAN: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
- scikit-learn — Clustering performance evaluation: https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation
- SciPy — Hierarchical clustering: https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html

## Cách diễn giải
- CustomerID là mã định danh, không đưa vào khoảng cách.
- Scaling cần thiết vì Age, Annual Income và Spending Score có thang đo khác nhau.
- Gender là biến phân loại; nếu đưa vào mô hình cần mã hóa. Nên báo cáo riêng kết quả có/không có Gender.
- Với DBSCAN, báo cáo số cụm, số noise, số mẫu được dùng tính metric và metric. Không so sánh Silhouette như thể cùng điều kiện nếu các thuật toán được tính trên số mẫu khác nhau.
- Image segmentation trong bài là phân cụm màu RGB của pixel, không phải semantic segmentation nhận diện vật thể.

## Lưu ý nguồn dữ liệu
Mall Customers được lưu trữ lại ở nhiều nơi. Không tự nhận một bản sao là nguồn gốc chính thức nếu không có chứng cứ. Ghi URL tải, ngày tải và license của đúng bản CSV. Không thêm dữ liệu mô phỏng vào tập gốc nếu không tách biệt và công bố rõ.
