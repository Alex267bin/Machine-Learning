# Phương pháp — Lab 3: Clustering Retail Customers

## 1. Dữ liệu và biến
Pipeline nhận CSV Mall Customers. Các cột tối thiểu: `Gender`, `Age`, `Annual Income`, `Spending Score`. Tên cột thu nhập/điểm chi tiêu có một số biến thể được chuẩn hóa. CustomerID không dùng làm đặc trưng vì chỉ là mã định danh.

## 2. Tiền xử lý
- Chuyển ba biến số về numeric; loại dòng thiếu biến bắt buộc và dòng trùng.
- Biến số được chuẩn hóa bằng StandardScaler: trừ mean và chia standard deviation.
- Gender được mã hóa OneHotEncoder.
- Chuẩn hóa quan trọng vì các thuật toán dựa trên khoảng cách; nếu không, thang đo thu nhập có thể lấn át biến tuổi hoặc spending score.

## 3. Chọn k
K-Means được chạy với k từ 2 đến min(10, n-1). Elbow (inertia) và Silhouette được xuất riêng. Chọn k có Silhouette cao nhất trong phạm vi khảo sát là một quy tắc thực nghiệm, không phải chân lý; cần xem thêm Elbow, profile và mục tiêu nghiệp vụ.

## 4. Thuật toán
- **K-Means:** tâm cụm là mean; phù hợp cụm tương đối cầu, nhạy outlier.
- **K-Medoids (PAM):** đại diện cụm là một quan sát thật (medoid); bản PAM trong script dùng ma trận khoảng cách Euclidean, phù hợp dataset lớp nhỏ. Có giới hạn 5.000 dòng vì chi phí bộ nhớ O(n²) và tính toán hoán đổi cao.
- **DBSCAN:** gom cụm theo mật độ; điểm nhiễu mang nhãn -1. Script cho phép chỉnh eps/min_samples và xuất sweep eps.
- **Hierarchical Agglomerative:** Ward linkage gộp cụm từ dưới lên; dendrogram dùng tối đa 100 quan sát đầu để dễ đọc.

## 5. Đánh giá
Silhouette càng cao thường càng tốt; Davies-Bouldin càng thấp thường càng tốt; Calinski-Harabasz càng cao thường càng tốt. Metric chỉ hợp lệ khi có ít nhất 2 cụm và ít hơn số điểm. Với DBSCAN, noise (-1) được loại khỏi phép tính metric và số mẫu metric được ghi lại. Vì mỗi thuật toán có thể loại số lượng noise khác nhau, không nên so sánh metric mà quên khác biệt tập mẫu.

## 6. Diễn giải
File cluster_profiles.csv thống kê số khách, tuổi, thu nhập, spending score và tỷ lệ giới tính cho từng cụm K-Means. Chỉ đặt tên persona sau khi xem profile thực tế; không gán nhãn “VIP”, “tiềm năng” hay “tiết kiệm” trước khi có bằng chứng.

## 7. Image Segmentation bổ sung
Ảnh RGB được resize để giới hạn chi phí; mỗi pixel được chuyển thành vector [R,G,B]. K-Means nhóm các màu, sau đó thay pixel bằng màu centroid tương ứng và reshape về kích thước ảnh. Đây là phân cụm màu, không phải phân đoạn ngữ nghĩa vật thể.
