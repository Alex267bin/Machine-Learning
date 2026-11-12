# Mô tả dự án — Phân cụm khách hàng bán lẻ

## 1. Mục đích
Khám phá các nhóm khách hàng dựa trên đặc điểm nhân khẩu học và hành vi chi tiêu, so sánh các thuật toán phân cụm và tổng hợp đặc điểm của từng nhóm để hỗ trợ phân khúc khách hàng ở mức mô tả.

## 2. Xác định bài toán
- **Loại bài toán:** học không giám sát; không có nhãn lớp đúng được cung cấp trước.
- **Bộ dữ liệu:** tệp CSV Mall Customers do người dùng chuẩn bị riêng; cần ghi lại nguồn và giấy phép của đúng phiên bản dữ liệu đã sử dụng.
- **Một quan sát:** một dòng tương ứng với một khách hàng.
- **Đặc trưng:** tuổi, thu nhập hằng năm, điểm chi tiêu và giới tính (tùy chọn).
- **Đầu ra:** nhãn cụm của từng thuật toán, chỉ số đánh giá nội bộ, hồ sơ cụm và biểu đồ trực quan.

## 3. Đầu vào và đầu ra
Tệp CSV cần có các cột `Gender`, `Age`, `Annual Income (k$)` (hoặc cách viết hoa được chương trình chấp nhận) và `Spending Score (1-100)` (hoặc biến thể dùng dấu gạch ngang dài). Có thể có `CustomerID`, nhưng cột này không được dùng làm đặc trưng phân cụm.

Đầu ra gồm bảng chỉ số, kết quả khảo sát tham số DBSCAN, nhãn cụm của từng khách hàng, hồ sơ cụm K-Means, bảng Elbow/Silhouette, biểu đồ PCA, biểu đồ cây Ward và bản tổng hợp kết quả dạng JSON.

## 4. Các thuật toán
1. **K-Means:** phân cụm dựa trên tâm cụm; k được chọn theo Silhouette cao nhất trong phạm vi thử nghiệm.
2. **K-Medoids (PAM):** cài đặt PAM bằng mã tự viết, sử dụng khoảng cách Euclid giữa các cặp điểm.
3. **DBSCAN:** phân cụm dựa trên mật độ; nhãn -1 biểu thị điểm nhiễu.
4. **Phân cụm phân cấp kết tụ:** sử dụng liên kết Ward với số cụm đã chọn.

## 5. Tiền xử lý
Đặc trưng số được điền giá trị thiếu bằng trung vị và chuẩn hóa. Giới tính (nếu sử dụng) được điền giá trị thiếu bằng giá trị xuất hiện phổ biến nhất rồi mã hóa One-Hot. Tùy chọn `--without-gender` cho phép kiểm tra ảnh hưởng của việc đưa giới tính vào phân cụm.

## 6. Đánh giá và diễn giải
Với DBSCAN, Silhouette, Davies–Bouldin và Calinski–Harabasz được tính trên các quan sát không bị xem là nhiễu. Báo cáo lưu số mẫu dùng để tính chỉ số và số điểm nhiễu. Hồ sơ K-Means được tính từ dữ liệu gốc chưa chuẩn hóa. Nhãn cụm chỉ là mã định danh, không phải thứ hạng chất lượng khách hàng.

## 7. Phần mở rộng phân đoạn ảnh
Một chương trình riêng áp dụng K-Means lên các véc-tơ màu RGB của điểm ảnh, thay mỗi điểm ảnh bằng màu tâm cụm tương ứng. Đây là lượng tử hóa màu, không phải nhận diện ngữ nghĩa của vật thể.

## 8. Giới hạn
Phân cụm mang tính khám phá và phụ thuộc vào chuẩn hóa, lựa chọn đặc trưng, thước đo khoảng cách và tham số. Bộ dữ liệu Mall Customers có quy mô nhỏ. Chỉ số DBSCAN có thể dùng ít mẫu hơn các thuật toán khác do loại điểm nhiễu. Hồ sơ cụm chỉ mô tả dữ liệu, không chứng minh một chân dung khách hàng có quan hệ nhân quả.

## 9. Tiêu chí nghiệm thu
- [ ] Ghi lại nguồn CSV và giấy phép sử dụng chính xác.
- [ ] Kiểm tra các cột bắt buộc và quá trình làm sạch dòng dữ liệu.
- [ ] Mô tả việc chuẩn hóa đặc trưng số và tùy chọn mã hóa giới tính.
- [ ] Chạy đủ bốn phương pháp phân cụm và lưu nhãn kết quả.
- [ ] Báo cáo số điểm nhiễu DBSCAN và số mẫu dùng tính chỉ số.
- [ ] Tính hồ sơ cụm trên thang đo dữ liệu gốc.
- [ ] Dùng ảnh có quyền sử dụng và mô tả phần mở rộng là phân cụm màu RGB.
