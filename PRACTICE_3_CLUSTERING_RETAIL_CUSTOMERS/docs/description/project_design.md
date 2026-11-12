# Thiết kế dự án — Phân cụm khách hàng bán lẻ

## WHAT — Xây dựng gì?
Một quy trình phân tích bằng Python để phân khúc khách hàng với bốn phương pháp phân cụm, các chỉ số đánh giá nội bộ, khảo sát tham số và hồ sơ mô tả từng cụm. Một công cụ dòng lệnh riêng minh họa lượng tử hóa màu ảnh bằng K-Means.

## WHY — Vì sao xây dựng?
Bộ dữ liệu không có nhãn mục tiêu nên không phù hợp để áp dụng bài toán phân loại có giám sát. So sánh các phương pháp dựa trên tâm cụm, medoid, mật độ và cấu trúc phân cấp giúp thấy được giả định khác nhau ảnh hưởng thế nào đến nhóm được phát hiện. Cần chuẩn hóa vì tuổi, thu nhập và điểm chi tiêu có thang đo số khác nhau.

## HOW — Quy trình phân cụm khách hàng

```text
             Mall_Customers.csv
                     |
                     v
        Kiểm tra cột + chuyển kiểu dữ liệu
                     |
                     v
       Loại dòng thiếu dữ liệu + dòng trùng
                     |
                     v
        Chuẩn hóa StandardScaler (số)
        + OneHotEncoder tùy chọn (giới tính)
                     |
                     v
       Khảo sát K-Means: k = 2 ... max-k
                     |
          +----------+----------+
          |                     |
          v                     v
     Elbow / Inertia      Silhouette theo k
          |                     |
          +----------+----------+
                     |
                     v
        Chọn k có Silhouette cao nhất
                     |
          +----------+----------+-----------+
          |          |          |           |
          v          v          v           v
       K-Means    PAM K-Medoids  DBSCAN   Ward kết tụ
                     |
                     v
        Chỉ số + nhãn cụm + hồ sơ cụm
                     |
                     v
        Biểu đồ PCA + cây Ward + JSON
```

## HOW — Phần mở rộng phân đoạn ảnh

```text
Ảnh đầu vào -> RGB -> đổi kích thước -> làm phẳng pixel (N x 3)
            -> K-Means -> nhãn cụm của pixel
            -> thay pixel bằng màu RGB của tâm cụm
            -> lưu ảnh phân đoạn + hình so sánh
```

## Các quyết định thiết kế
- CustomerID chỉ là mã định danh, không được đưa vào đặc trưng phân cụm.
- Đặc trưng số được chuẩn hóa; giới tính là đặc trưng tùy chọn và được mã hóa One-Hot.
- K-Means sử dụng `n_init=20`, hạt giống ngẫu nhiên cố định và khảo sát Silhouette.
- PAM sử dụng khoảng cách Euclid và thử hoán đổi medoid; giới hạn dữ liệu ở 5.000 dòng để kiểm soát ma trận khoảng cách O(n²).
- DBSCAN cho phép cấu hình `eps`/`min_samples` và khảo sát `eps` từ 0.3 đến 1.5.
- Điểm nhiễu DBSCAN (nhãn -1) bị loại khỏi phép tính chỉ số nội bộ; số điểm nhiễu và số mẫu dùng tính chỉ số vẫn được ghi nhận.
- Hồ sơ cụm được tính trên dữ liệu gốc, không phải dữ liệu đã chuẩn hóa.
- Biểu đồ cây Ward được tạo trên mẫu có thể tái lập, tối đa 100 quan sát.
- Phân đoạn ảnh giảm kích thước ảnh theo cạnh dài nhất để hạn chế chi phí tính toán.

## Các mô-đun
- `scripts/cluster.py`: quy trình dữ liệu khách hàng và báo cáo phân cụm.
- `scripts/image_segmentation.py`: phân đoạn ảnh theo màu RGB.
- `notebooks/03_customer_clustering.ipynb`: sổ tay phân tích có hướng dẫn.
- `outputs/`: bảng, JSON và biểu đồ được tạo.
- `logs/`: nhật ký chạy chương trình.

## Rủi ro khi diễn giải
Việc chọn k theo Silhouette chỉ là phương pháp tham khảo, không chứng minh số nhóm khách hàng thực sự tồn tại. Điểm DBSCAN được tính trên tập không có nhiễu nên không hoàn toàn cùng tập mẫu với các phương pháp khác. PCA hai chiều chỉ phục vụ trực quan hóa, không phải không gian phân cụm gốc. Không gán chân dung tiếp thị cho từng nhóm nếu chưa kiểm tra hồ sơ cụm thực tế.
