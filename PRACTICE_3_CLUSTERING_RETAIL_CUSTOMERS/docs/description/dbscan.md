# Thuật toán DBSCAN

## Mục đích
Tìm các nhóm khách hàng có mật độ điểm dữ liệu cao mà không cần xác định trước số cụm, đồng thời phát hiện các điểm riêng lẻ được xem là nhiễu.

## Đầu vào
Các thuộc tính số đã chuẩn hóa và tùy chọn giới tính được mã hóa One-Hot; hai tham số chính là `eps` và `min_samples`.

## Đầu ra
Nhãn cụm cho từng khách hàng; nhãn `-1` biểu thị điểm nhiễu. Quy trình ghi lại số cụm, số điểm nhiễu và số mẫu được dùng để tính chỉ số.

## Cách hoạt động
Với mỗi điểm, DBSCAN xét các điểm nằm trong vùng lân cận có bán kính `eps`. Điểm có ít nhất `min_samples` điểm trong vùng lân cận được xem là điểm lõi. Thuật toán mở rộng cụm từ các điểm lõi thông qua quan hệ liên kết mật độ; các điểm không thuộc cụm có thể được đánh dấu là nhiễu.

## Tham số trong dự án
Giá trị mặc định: `eps=0.75` và `min_samples=5`. Chương trình khảo sát `eps` từ 0.3 đến 1.5, bước tăng 0.1.

## Lưu ý khi đánh giá
Các điểm nhiễu bị loại khỏi dữ liệu tính Silhouette, Davies–Bouldin và Calinski–Harabasz. Số lượng mẫu được chấm điểm cũng được lưu lại. Vì vậy, các chỉ số DBSCAN có thể được tính trên tập mẫu khác với K-Means, PAM hoặc phân cụm phân cấp; cần thận trọng khi so sánh trực tiếp.

## Ưu điểm và hạn chế
Có thể tìm cụm có hình dạng không đều và phát hiện nhiễu. Kết quả nhạy với `eps`, `min_samples` và thang đo khoảng cách; thuật toán khó xử lý tốt dữ liệu có mật độ thay đổi lớn.
