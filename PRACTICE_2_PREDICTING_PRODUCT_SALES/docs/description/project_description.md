# Mô tả dự án — Dự báo doanh thu sản phẩm

## 1. Mục đích
Ước lượng doanh thu hằng tháng của từng sản phẩm được xác định bằng `StockCode`, dựa trên lịch sử doanh thu các tháng trước của chính sản phẩm đó. Kết quả đóng vai trò tham khảo ban đầu cho việc lập kế hoạch bán hàng và tồn kho theo sản phẩm.

## 2. Xác định bài toán
- **Loại bài toán:** hồi quy có giám sát trên bảng dữ liệu sản phẩm-tháng.
- **Bộ dữ liệu:** UCI Online Retail, mã bộ dữ liệu 352.
- **Một mẫu dữ liệu:** một sản phẩm (`StockCode`) trong một tháng dương lịch.
- **Biến mục tiêu:** `revenue = sum(Quantity × UnitPrice)`, đơn vị GBP, được tính theo từng sản phẩm và tháng.
- **Giá trị dự đoán:** doanh thu ước lượng không âm của một sản phẩm trong một tháng.
- **Không dự đoán:** số lượng giao dịch, tổng doanh thu toàn cửa hàng, giá trị vòng đời khách hàng hoặc tác động nhân quả của tiếp thị.

## 3. Đầu vào và đầu ra
**Dữ liệu thô:** các giao dịch gồm `InvoiceNo`, `StockCode`, `Quantity`, `InvoiceDate` và `UnitPrice`.

**Đặc trưng mô hình:** `StockCode`, `lag_1`, `lag_2`, `lag_3`, `rolling_mean_3` và `month_num`.

**Đầu ra:** bảng CSV so sánh mô hình, dự đoán trên tập kiểm tra, tệp JSON chứa chỉ số đánh giá, biểu đồ chẩn đoán, độ quan trọng đặc trưng nếu mô hình hỗ trợ và mô hình tốt nhất đã được tuần tự hóa.

## 4. Các bước xử lý
1. Chuyển đổi ngày và kiểu dữ liệu số; loại bỏ dòng không hợp lệ, hóa đơn hủy và giao dịch có số lượng hoặc đơn giá không dương.
2. Cộng doanh thu giao dịch theo từng sản phẩm và tháng.
3. Tạo bảng theo tháng cho mỗi sản phẩm, từ tháng đầu tiên sản phẩm xuất hiện đến tháng cuối cùng của bộ dữ liệu; các tháng không phát sinh doanh thu được gán bằng 0.
4. Tạo đặc trưng trễ và trung bình trượt đã dịch lùi để mỗi dòng chỉ sử dụng thông tin từ các tháng trước.
5. Chia dữ liệu theo trình tự thời gian; tinh chỉnh và lựa chọn mô hình bằng kiểm định chéo chuỗi thời gian trên tập huấn luyện.
6. Đánh giá các mô hình trên giai đoạn kiểm tra nằm sau giai đoạn huấn luyện.

## 5. Các mô hình
Hồi quy tuyến tính, Cây quyết định hồi quy, Rừng ngẫu nhiên hồi quy, Tăng cường Gradient hồi quy và một phiên bản Rừng ngẫu nhiên được tinh chỉnh tham số.

## 6. Đánh giá
MAE, MSE, RMSE và R² được tính trên biến mục tiêu GBP ở thang đo ban đầu. RMSE kiểm định chéo được dùng để chọn mô hình; các chỉ số trên tập kiểm tra chỉ dùng cho báo cáo cuối cùng, không dùng để lựa chọn mô hình.

## 7. Phạm vi và giới hạn
Bộ dữ liệu nguồn không có ngân sách tiếp thị, lượng hàng tồn, mô tả sản phẩm hoặc nhân khẩu học khách hàng. Dự án không tự tạo hoặc suy diễn các biến này. Lịch sử doanh thu có thể thưa và cơ cấu sản phẩm thay đổi theo thời gian; vì vậy mô hình chỉ là đường cơ sở dự báo, không bảo đảm nhu cầu tương lai.

## 8. Tiêu chí nghiệm thu
- [ ] Xác minh nguồn dữ liệu và các cột bắt buộc.
- [ ] Không để đặc trưng của tháng tương lai rò rỉ vào tháng quá khứ.
- [ ] Chia tập huấn luyện và kiểm tra theo thời gian.
- [ ] Chỉ dùng kiểm định chéo trên tập huấn luyện để lựa chọn mô hình.
- [ ] Chỉ số và biểu đồ được tạo từ lần chạy thực tế.
- [ ] Dự đoán và mô hình được lưu theo cách có thể tái lập.
