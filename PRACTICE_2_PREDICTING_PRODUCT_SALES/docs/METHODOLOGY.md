# Phương pháp — Practice 2

Bài toán supervised regression dạng panel time series: dự báo doanh thu tháng kế tiếp cho mỗi StockCode.

- Sắp xếp theo StockCode và tháng; tạo lag 1/2/3 và rolling mean từ các tháng trước.
- Chia train/test theo mốc thời gian chung, không shuffle.
- Fit OneHotEncoder và mô hình chỉ trên train qua Pipeline để tránh leakage.
- So sánh Linear Regression, Decision Tree, Random Forest, Gradient Boosting.

| Mô hình | Input → Output | Cách hoạt động | Ưu / nhược |
|---|---|---|---|
| Linear Regression | Đặc trưng → số doanh thu | Tìm hệ số tuyến tính giảm tổng bình phương lỗi | Dễ giải thích; khó bắt phi tuyến |
| Decision Tree | Đặc trưng → giá trị lá | Chia vùng theo ngưỡng đặc trưng | Bắt phi tuyến; dễ overfit |
| Random Forest | Đặc trưng → trung bình nhiều cây | Bagging trên mẫu và đặc trưng ngẫu nhiên | Ổn định hơn cây đơn; khó giải thích |
| Gradient Boosting | Đặc trưng → dự báo cộng dồn | Thêm cây tuần tự để sửa lỗi còn lại | Mạnh; cần điều chỉnh learning rate/độ sâu |

MAE là lỗi tuyệt đối trung bình; MSE là lỗi bình phương trung bình; RMSE cùng đơn vị target và nhạy lỗi lớn; R² có thể âm trên test. Chọn mô hình theo RMSE holdout, không theo train.
