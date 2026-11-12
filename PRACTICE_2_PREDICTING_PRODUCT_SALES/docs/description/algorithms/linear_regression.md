# Thuật toán Hồi quy tuyến tính (Linear Regression)

## Mục đích
Tạo mô hình hồi quy có giám sát cơ bản, giả định mối quan hệ tuyến tính giữa các đặc trưng đầu vào và doanh thu sản phẩm theo tháng.

## Đầu vào
Quy trình nhận mã sản phẩm `StockCode`, doanh thu của ba tháng trước, trung bình trượt ba tháng đã dịch lùi một tháng và số tháng trong năm. Mã sản phẩm được mã hóa One-Hot; đặc trưng số được điền giá trị thiếu bằng trung vị.

## Đầu ra
Doanh thu tháng dự đoán liên tục, đơn vị GBP. Giá trị dự đoán âm được đưa về 0 trước khi đánh giá hoặc xuất kết quả.

## Cách hoạt động
Mô hình học các hệ số bằng cách tối thiểu hóa tổng bình phương phần dư. Các hệ số thể hiện mối liên hệ tuyến tính giữa đặc trưng đã mã hóa và doanh thu, không chứng minh quan hệ nhân quả.

## Đánh giá
MAE, MSE, RMSE và R² trên tập kiểm tra theo thời gian; RMSE kiểm định chéo trên các phần dữ liệu huấn luyện.

## Ưu điểm và hạn chế
Huấn luyện nhanh và dễ diễn giải. Mô hình có thể không nắm bắt được xu hướng phi tuyến, tương tác phức tạp hoặc biến động đột ngột.
