# Practice 3 — Phân cụm khách hàng bán lẻ

## Mục tiêu
Khám phá nhóm khách hàng từ Age, Gender, Annual Income (k$), Spending Score (1–100). Không có nhãn đúng/sai; diễn giải cụm dựa trên profile thực tế.

## Dữ liệu
Đặt Mall_Customers.csv vào data/. Bản phổ biến có CustomerID, Gender, Age, Annual Income (k$), Spending Score (1–100), thường được chia sẻ trên Kaggle. Các bản sao có thể khác nhau; cần xác minh URL và điều khoản/giấy phép của đúng bản tải. Không commit dữ liệu chưa rõ quyền phân phối.

## Chạy
```bash
pip install -r requirements.txt
python scripts/cluster.py --data data/Mall_Customers.csv
python scripts/image_segmentation.py --image data/sample.jpg --k 5
```

## Phương pháp
So sánh K-Means, K-Medoids, DBSCAN, Hierarchical/Agglomerative; chọn k bằng Elbow/Silhouette; đánh giá Silhouette, Davies–Bouldin, Calinski–Harabasz khi điều kiện hợp lệ. DBSCAN noise (-1) không tính như một cụm thường.
Image segmentation là bài phụ độc lập: K-Means phân cụm pixel màu, thay pixel bằng centroid và tái tạo ảnh.
