# Phương pháp — Lab 2: Predicting Product Sales

## 1. Phạm vi bài toán
Nguồn dữ liệu hiện được dùng là **UCI Online Retail (ID 352)**. Mỗi dòng giao dịch có mã hóa đơn, mã sản phẩm, số lượng, thời điểm và đơn giá. Pipeline quy đổi thành bài toán dự báo doanh thu **theo từng StockCode và tháng**:

- Doanh thu giao dịch = `Quantity × UnitPrice`.
- Target = tổng doanh thu giao dịch theo `StockCode, month`.
- Đơn vị tiền tệ: GBP theo dataset gốc.
- Đây là dự báo doanh thu sản phẩm-tháng, không phải dự báo số lượng bán hoặc tổng doanh thu toàn cửa hàng.

## 2. Làm sạch và tạo dữ liệu
1. Parse `InvoiceDate`, ép kiểu số cho `Quantity` và `UnitPrice`.
2. Loại dòng thiếu trường bắt buộc, hóa đơn hủy (InvoiceNo bắt đầu bằng C), Quantity không dương và UnitPrice không dương.
3. Tạo doanh thu, tổng hợp theo sản phẩm-tháng.
4. Reindex từng sản phẩm trên trục tháng đầy đủ; tháng không có giao dịch được xem là doanh thu 0 trong panel.
5. Tạo lag 1, 2, 3 tháng và rolling mean 3 tháng. Rolling mean dùng `shift(1)`, vì vậy không nhìn vào target tháng đang dự báo.

## 3. Đặc trưng
- `StockCode`: OneHotEncoder, hỗ trợ mã sản phẩm mới bằng `handle_unknown="ignore"`.
- `lag_1..lag_3`: doanh thu ở các tháng trước.
- `rolling_mean_3`: trung bình doanh thu của ba tháng trước.
- `month_num`: tháng trong năm, biểu diễn mùa vụ cơ bản.

Không đưa InvoiceNo, CustomerID hoặc doanh thu tháng hiện tại vào đầu vào. Không dùng thông tin sau thời điểm dự báo.

## 4. Chia tập và chống leakage
- Chia train/test theo thời gian; các tháng cuối cùng là holdout test.
- Không shuffle dữ liệu.
- RandomizedSearchCV chỉ chạy trên train.
- Cross-validation chia theo **tháng hoàn chỉnh**, không tách các sản phẩm của cùng một tháng sang cả train và validation.
- Test chỉ dùng một lần để báo cáo hiệu năng cuối.

## 5. Mô hình
Linear Regression, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting Regressor. Random Forest được tune bằng RandomizedSearchCV với số cây, độ sâu, min_samples_leaf và max_features.

## 6. Đánh giá
MAE, MSE, RMSE và R² được tính trên target GBP gốc. RMSE nhạy với sai số lớn; MAE dễ diễn giải theo đơn vị tiền; R² có thể âm nếu mô hình kém hơn baseline dự báo trung bình. Dự báo âm được chặn về 0 do doanh thu không âm theo định nghĩa dữ liệu đã lọc.

## 7. Giới hạn cần nêu khi bảo vệ
- UCI Online Retail chỉ bao phủ giai đoạn lịch sử 2010–2011, không đại diện thị trường hiện tại.
- Mã sản phẩm có độ thưa cao; One-Hot có thể tạo nhiều chiều.
- Dự báo dựa trên lịch sử doanh thu, chưa có giá khuyến mãi, tồn kho, quảng cáo hay ngày lễ.
- Việc xem tháng không có giao dịch là doanh thu 0 là giả định mô hình hóa; cần nêu rõ.
- Không khẳng định mô hình có thể dự báo tốt cho sản phẩm hoàn toàn mới nếu không có lịch sử.
