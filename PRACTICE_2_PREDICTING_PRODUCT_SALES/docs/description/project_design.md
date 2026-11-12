# Thiết kế dự án — Dự báo doanh thu sản phẩm

## WHAT — Xây dựng gì?
Một quy trình Python có thể tái lập, chuyển dữ liệu giao dịch bán lẻ thành dự báo doanh thu theo từng sản phẩm-tháng, đồng thời so sánh bốn nhóm mô hình hồi quy và một mô hình Rừng ngẫu nhiên đã tinh chỉnh.

## WHY — Vì sao xây dựng?
Doanh thu theo sản phẩm-tháng là đại lượng có thể đo lường từ bộ dữ liệu hiện có. Đánh giá theo trình tự thời gian phản ánh bài toán dự báo thực tế tốt hơn cách chia ngẫu nhiên. Dự án chỉ đưa ra kết luận dựa trên những trường dữ liệu thực sự có trong UCI Online Retail.

## HOW — Quy trình xử lý

```text
UCI Online Retail / tệp Excel cục bộ
                 |
                 v
       Kiểm tra và làm sạch dữ liệu
                 |
                 v
 Cộng doanh thu theo sản phẩm và tháng
                 |
                 v
 Bảng tháng + đặc trưng trễ/trung bình trượt
                 |
                 v
 Chia tập huấn luyện / kiểm tra theo thời gian
                 |
                 v
       Tiền xử lý + kiểm định chéo
                 |
       +---------+----------+-----------+
       |         |          |           |
       v         v          v           v
 Hồi quy     Cây quyết   Rừng ngẫu    Tăng cường
 tuyến tính   định       nhiên        Gradient
                 |
                 v
       Chọn theo RMSE kiểm định chéo
                 |
                 v
       Đánh giá tập kiểm tra + biểu đồ
                 |
                 v
       JSON / CSV / hình / mô hình
```

## Các quyết định thiết kế
- **Đơn vị dữ liệu:** một dòng cho mỗi StockCode-tháng, tránh gộp nhầm các sản phẩm thành doanh thu toàn cửa hàng.
- **Biến mục tiêu:** tổng `Quantity × UnitPrice` (GBP); loại giao dịch hủy và giao dịch có số lượng/đơn giá không dương.
- **Tháng sản phẩm không phát sinh:** gán doanh thu bằng 0 sau tháng đầu tiên sản phẩm xuất hiện, không tạo các tháng trước thời điểm sản phẩm xuất hiện.
- **Đặc trưng thời gian:** doanh thu trễ 1, 2, 3 tháng và trung bình trượt ba tháng được dịch lùi một tháng.
- **Đặc trưng phân loại:** mã hóa One-Hot cho `StockCode`, bỏ qua mã chưa từng gặp khi biến đổi dữ liệu.
- **Tiền xử lý số:** điền giá trị thiếu bằng trung vị trong quy trình `ColumnTransformer`.
- **Kiểm định:** tạo các phần `TimeSeriesSplit` dựa trên các tháng huấn luyện duy nhất để sản phẩm thuộc cùng tháng luôn nằm trong cùng một phần dữ liệu.
- **Lựa chọn:** chọn mô hình có RMSE trung bình thấp nhất trên kiểm định chéo của tập huấn luyện. Không dùng tập kiểm tra để lựa chọn.
- **Khả năng tái lập:** cố định hạt giống ngẫu nhiên và lưu toàn bộ quy trình mô hình.

## Các mô-đun chính
- `scripts/train.py`: quy trình từ dữ liệu đến huấn luyện và báo cáo.
- `scripts/predict.py`: giao diện dự báo bằng dòng lệnh.
- `notebooks/02_sales_forecasting.ipynb`: sổ tay hướng dẫn.
- `outputs/`: chỉ số, dự đoán và biểu đồ được tạo.
- `models/`: tệp mô hình đã lưu.
- `logs/`: nhật ký thực thi.

## Rủi ro và cách diễn giải
Tập kiểm tra theo thời gian có thể khác đáng kể các phần kiểm định chéo nếu xu hướng bán hàng thay đổi. Cần báo cáo riêng điểm kiểm định chéo và điểm tập kiểm tra. Mã sản phẩm được mã hóa One-Hot không cung cấp ý nghĩa ngữ nghĩa của sản phẩm. Độ quan trọng đặc trưng của mô hình cây phụ thuộc vào mô hình và không thể diễn giải như quan hệ nhân quả.
