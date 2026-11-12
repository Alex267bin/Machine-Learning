# Câu hỏi vấn đáp — Practice 3

1. **Input là gì?** Tuổi, thu nhập năm, spending score và Gender đã mã hóa.
2. **Output?** Nhãn cụm cho từng khách hàng; không phải nhãn phân loại có sẵn.
3. **Purpose?** Khám phá nhóm khách hàng để hỗ trợ phân tích marketing.
4. **Vì sao bỏ CustomerID?** Đây là mã định danh, không phản ánh mức độ tương đồng.
5. **Vì sao chuẩn hóa?** Đưa các biến khác đơn vị/thang đo về thang so sánh để khoảng cách không bị một biến chi phối.
6. **K-Means hoạt động thế nào?** Khởi tạo k centroid, gán điểm vào centroid gần nhất, cập nhật mean và lặp đến hội tụ.
7. **K-Medoids khác gì?** Tâm cụm là một quan sát thực (medoid), không phải trung bình vector.
8. **DBSCAN cần k không?** Không; dùng eps và min_samples.
9. **Noise -1 là gì?** Điểm không thuộc vùng có mật độ đủ lớn.
10. **Linkage là gì?** Quy tắc đo khoảng cách giữa hai cụm trong quá trình gộp phân cấp.
11. **Silhouette?** So sánh độ gần trong cụm với cụm gần nhất khác; giá trị từ -1 đến 1.
12. **Elbow?** Điểm mà mức giảm inertia khi tăng k bắt đầu chậm lại.
13. **PCA dùng làm gì?** Chiếu dữ liệu nhiều chiều xuống 2D để trực quan hóa.
14. **Image segmentation khác customer clustering?** Image segmentation gom pixel theo màu; customer clustering gom khách hàng theo thuộc tính.
15. **Vì sao không gán tên nhóm trước?** Nhãn cụm tùy thuật toán; phải xem profile thực tế rồi mới diễn giải.
