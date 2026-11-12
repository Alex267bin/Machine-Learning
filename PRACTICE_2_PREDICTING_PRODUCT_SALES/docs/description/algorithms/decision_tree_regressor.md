# Thuật toán Cây quyết định hồi quy (Decision Tree Regressor)

**Mục đích:** học các quy tắc phi tuyến để dự báo doanh thu theo từng sản phẩm-tháng.

**Đầu vào:** `StockCode`, `lag_1`, `lag_2`, `lag_3`, `rolling_mean_3` và `month_num`. Mã sản phẩm được mã hóa One-Hot; các đặc trưng số được điền giá trị thiếu bằng trung vị.

**Đầu ra:** doanh thu tháng dự đoán liên tục, đơn vị GBP. Giá trị dự đoán âm được đưa về 0 trước khi báo cáo.

**Cách hoạt động:** cây liên tục chia không gian đặc trưng tại các ngưỡng giúp giảm sai số bình phương. Mỗi nút lá dự đoán bằng giá trị trung bình của biến mục tiêu trong các mẫu huấn luyện thuộc nút đó.

**Đánh giá:** RMSE từ kiểm định chéo theo thời gian chỉ trên tập huấn luyện; MAE, MSE, RMSE và R² trên tập kiểm tra theo trình tự thời gian.

**Ưu điểm và hạn chế:** mô hình hóa được quy tắc phi tuyến và tương tác giữa đặc trưng; tuy nhiên có thể quá khớp và nhạy với thay đổi dữ liệu. Mã hiện tại đặt `random_state` nhưng chưa tinh chỉnh độ sâu của cây.
