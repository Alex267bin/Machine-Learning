# Machine Learning — Lab 2 & Lab 3

Repository gồm hai bài thực hành độc lập:

| Thư mục | Bài toán | Thuật toán |
|---|---|---|
| PRACTICE_2_PREDICTING_PRODUCT_SALES | Regression — dự báo doanh thu sản phẩm-tháng | Linear Regression, Decision Tree, Random Forest, Gradient Boosting |
| PRACTICE_3_CLUSTERING_RETAIL_CUSTOMERS | Unsupervised Learning — phân cụm khách hàng | K-Means, K-Medoids (PAM), DBSCAN, Hierarchical |

## Nguyên tắc
- Tách riêng data, scripts, notebooks, docs, outputs, models, logs.
- Lab 2 holdout theo thời gian; tuning chỉ trên train; lag/rolling chỉ dùng lịch sử.
- Lab 3 scale biến số, mã hóa biến phân loại; DBSCAN noise được ghi nhận và loại khỏi metric.
- Không ghi số liệu kết quả giả. Chạy script với dataset thực để sinh metrics.
- Tài liệu, chú thích, câu hỏi vấn đáp viết bằng tiếng Việt; giữ thuật ngữ kỹ thuật tiếng Anh.

## Bắt đầu
Mỗi bài có README và requirements riêng. Dùng Python 3.12 và virtual environment riêng. Xem README trong từng thư mục để cài đặt/chạy.

## Dữ liệu
Không commit dataset lớn hoặc dữ liệu chưa rõ quyền phân phối. Kiểm tra nguồn, license và schema trong DATASET_DOCUMENTATION trước khi dùng.
