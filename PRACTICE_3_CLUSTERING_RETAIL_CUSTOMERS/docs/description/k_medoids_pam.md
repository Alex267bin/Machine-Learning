# Thuật toán K-Medoids — PAM

## Mục đích
Phân chia khách hàng xoay quanh các điểm đại diện thực tế trong dữ liệu (medoid), thay vì tâm cụm được tính bằng trung bình như K-Means.

## Đầu vào và đầu ra
Đầu vào là ma trận đặc trưng đã biến đổi giống các thuật toán phân cụm còn lại. Đầu ra gồm nhãn cụm của từng dòng và chỉ số các dòng được chọn làm medoid.

## Cách hoạt động
Chương trình khởi tạo k medoid khác nhau, gán mỗi điểm vào medoid gần nhất, sau đó thử hoán đổi từng medoid hiện tại với các điểm không phải medoid. Giữ lại phép hoán đổi nếu tổng khoảng cách giảm. Thuật toán dừng khi không còn phép hoán đổi cải thiện hoặc đạt số vòng lặp tối đa.

## Chi tiết triển khai
Kho mã nguồn có cài đặt PAM đơn giản bằng mã tự viết, sử dụng khoảng cách Euclid, `max_iter=100` và hạt giống ngẫu nhiên cố định. Chương trình tạo ma trận khoảng cách kích thước n × n và từ chối dữ liệu có hơn 5.000 dòng.

## Đánh giá
Sử dụng Silhouette, Davies–Bouldin và Calinski–Harabasz trên nhãn cụm thu được.

## Ưu điểm và hạn chế
Medoid là một quan sát thực tế nên có thể ít bị ảnh hưởng bởi giá trị ngoại lệ hơn trung bình. Tuy nhiên, việc thử hoán đổi và lưu ma trận khoảng cách từng cặp tốn nhiều tài nguyên khi dữ liệu lớn. Cài đặt hiện tại hướng đến bộ dữ liệu Mall Customers có quy mô nhỏ.
