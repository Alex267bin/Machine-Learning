# Thuật toán K-Means

## Mục đích
Chia khách hàng thành k nhóm dựa trên khoảng cách đến tâm cụm trong không gian đặc trưng.

## Đầu vào
Tuổi, thu nhập hằng năm và điểm chi tiêu đã chuẩn hóa; có thể bổ sung giới tính đã được mã hóa One-Hot.

## Đầu ra
Một nhãn cụm dạng số nguyên cho mỗi khách hàng, giá trị Inertia, điểm Silhouette, hồ sơ cụm và hình trực quan hóa PCA.

## Cách hoạt động
1. Khởi tạo k tâm cụm.
2. Gán mỗi quan sát vào tâm cụm gần nhất.
3. Tính lại tâm cụm bằng trung bình các quan sát được gán vào cụm đó.
4. Lặp lại bước gán và cập nhật cho đến khi hội tụ.

## Tham số trong dự án
Chương trình thử k từ 2 đến giá trị nhỏ hơn giữa `max_k` và `n-1`, sử dụng `n_init=20` và `random_state=42`, sau đó chọn k có Silhouette cao nhất trong phạm vi khảo sát.

## Đánh giá
Silhouette được dùng để khảo sát số cụm; phần so sánh thuật toán cuối cùng còn ghi nhận Davies–Bouldin và Calinski–Harabasz.

## Ưu điểm và hạn chế
Hiệu quả và dễ giải thích, nhưng phải xác định trước k và thường phù hợp với các cụm tương đối gọn, gần hình cầu. Kết quả phụ thuộc vào chuẩn hóa và cách khởi tạo. Số hiệu cụm không thể hiện thứ hạng hay chất lượng khách hàng.
