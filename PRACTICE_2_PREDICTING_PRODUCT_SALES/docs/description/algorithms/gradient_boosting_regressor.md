# Thuật toán Tăng cường Gradient hồi quy (Gradient Boosting Regressor)

**Mục đích:** mô hình cây tăng cường dùng để dự báo doanh thu sản phẩm theo tháng.

**Đầu vào và đầu ra:** sử dụng bộ đặc trưng và quy trình tiền xử lý chung của Lab 2; đầu ra là doanh thu tháng dự đoán, đơn vị GBP.

**Cách hoạt động:** mô hình xây dựng các cây tuần tự. Mỗi cây mới học phần sai số còn lại của mô hình hiện tại; mức đóng góp của cây được điều chỉnh bằng tốc độ học.

**Đánh giá:** sử dụng cùng RMSE từ kiểm định chéo theo thời gian trên tập huấn luyện và các chỉ số hồi quy trên tập kiểm tra như những mô hình còn lại.

**Ưu điểm và hạn chế:** có khả năng mô hình hóa quan hệ phi tuyến phức tạp, nhưng có thể quá khớp và phụ thuộc vào tham số của cây cũng như tốc độ học. Trong mã hiện tại, mô hình dùng tham số mặc định ngoài `random_state`; chưa có bước tìm kiếm tham số riêng.
