# Phân cụm phân cấp kết tụ — phương pháp Ward

## Mục đích
Xây dựng cấu trúc phân cấp gồm các cụm lồng nhau, sau đó tạo kết quả phân cụm cuối cùng với số cụm đã chọn.

## Đầu vào và đầu ra
Sử dụng ma trận đặc trưng đã biến đổi. Mô hình trả về một nhãn cụm cho mỗi khách hàng. Một ma trận liên kết Ward riêng được tính để vẽ biểu đồ cây phân cấp.

## Cách hoạt động
Ban đầu, mỗi quan sát là một cụm riêng. Thuật toán lần lượt gộp các cụm lại với nhau. Phương pháp Ward chọn phép gộp làm mức tăng tổng bình phương sai lệch bên trong cụm nhỏ nhất.

## Tham số trong dự án
`AgglomerativeClustering` sử dụng số cụm bằng giá trị k được chọn theo Silhouette của K-Means và `linkage="ward"`. Biểu đồ cây dùng `scipy linkage(method="ward")` trên một mẫu có thể tái lập, tối đa 100 dòng.

## Đánh giá
Sử dụng Silhouette, Davies–Bouldin và Calinski–Harabasz trên nhãn cụm cuối cùng.

## Ưu điểm và hạn chế
Cấu trúc phân cấp giúp quan sát các nhóm lồng nhau; biểu đồ cây thể hiện khoảng cách tại thời điểm các cụm được gộp. Phân cụm kết tụ tiêu tốn nhiều tài nguyên hơn K-Means khi dữ liệu lớn; phương pháp Ward gắn với hình học Euclid.
