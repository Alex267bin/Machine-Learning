# Phân đoạn ảnh bằng K-Means (lượng tử hóa màu RGB)

## Mục đích
Giảm số lượng màu khác nhau trong ảnh bằng cách nhóm các điểm ảnh có giá trị RGB tương tự nhau.

## Đầu vào
Một tệp ảnh mà thư viện Pillow có thể đọc. Ảnh được chuyển sang hệ màu RGB và thay đổi kích thước sao cho cạnh dài nhất không vượt quá `max_side` (mặc định 600).

## Đầu ra
Ảnh sau phân cụm và hình so sánh ảnh gốc với ảnh đã xử lý. Mỗi điểm ảnh được thay bằng màu RGB của tâm cụm mà nó thuộc về.

## Cách hoạt động
Ảnh được chuyển thành ma trận N × 3, mỗi dòng tương ứng với ba giá trị đỏ, lục và lam của một điểm ảnh. K-Means nhóm các véc-tơ màu thành k cụm. Màu của tâm cụm được dùng để thay thế màu ban đầu của từng điểm ảnh.

## Tham số
Mặc định: `k=5`, `max_side=600`, `n_init=10` và `random_state=42`. Chương trình kiểm tra tệp ảnh, giá trị k và số lượng điểm ảnh.

## Ưu điểm và hạn chế
Đây là ví dụ trực quan về phân cụm và lượng tử hóa màu. Thuật toán không hiểu vật thể, đường biên hay lớp ngữ nghĩa; vì vậy không phải phân đoạn ngữ nghĩa. Kết quả phụ thuộc vào k và khoảng cách Euclid trong không gian RGB.
