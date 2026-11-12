# Thuật toán Rừng ngẫu nhiên hồi quy (Random Forest Regressor)

**Mục đích:** kết hợp nhiều cây quyết định để dự báo doanh thu sản phẩm-tháng và mô hình hóa quan hệ phi tuyến.

**Đầu vào và đầu ra:** sử dụng bộ đặc trưng và quy trình tiền xử lý chung của Lab 2; đầu ra là doanh thu tháng dự đoán, đơn vị GBP.

**Cách hoạt động:** huấn luyện nhiều cây trên các mẫu lấy bằng phương pháp lấy mẫu có hoàn lại và lựa chọn ngẫu nhiên đặc trưng. Kết quả dự đoán cuối cùng là trung bình dự đoán của các cây, giúp giảm phương sai so với một cây đơn lẻ.

**Tinh chỉnh tham số:** `RandomizedSearchCV` tìm kiếm các tham số `n_estimators`, `max_depth`, `min_samples_leaf` và `max_features`, sử dụng các phần kiểm định theo tháng và chỉ lấy dữ liệu từ tập huấn luyện.

**Đánh giá:** RMSE kiểm định chéo được dùng để lựa chọn mô hình; MAE, MSE, RMSE và R² trên tập kiểm tra được báo cáo riêng. Độ quan trọng đặc trưng chỉ được lưu nếu mô hình cây được chọn hỗ trợ.

**Ưu điểm và hạn chế:** mô hình hóa được quan hệ phi tuyến và tương tác, nhưng khó diễn giải hơn hồi quy tuyến tính và tốn tài nguyên tính toán hơn. Độ quan trọng đặc trưng không đồng nghĩa với quan hệ nhân quả.
