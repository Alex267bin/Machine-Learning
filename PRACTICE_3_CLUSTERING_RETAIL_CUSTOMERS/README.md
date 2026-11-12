# Lab 3 — Phân cụm khách hàng bán lẻ

Bài thực hành phân cụm khách hàng trên bộ dữ liệu Mall Customers và phần mở rộng phân đoạn ảnh bằng K-Means.

## Cấu trúc thư mục
- `data/Mall_Customers.csv`: dữ liệu đầu vào, tải riêng theo hướng dẫn trong `data/README.md`.
- `scripts/cluster.py`: kiểm tra dữ liệu, chuẩn hóa, Elbow/Silhouette, K-Means, K-Medoids (PAM), DBSCAN, phân cụm phân cấp Ward, chỉ số đánh giá, hồ sơ cụm, PCA và biểu đồ cây.
- `scripts/image_segmentation.py`: áp dụng K-Means trên véc-tơ màu RGB của điểm ảnh.
- `notebooks/03_customer_clustering.ipynb`: sổ tay phân tích.
- `docs/`: tài liệu dữ liệu, phương pháp, kết quả, câu hỏi vấn đáp, tài liệu tham khảo, mô tả/thiết kế dự án và mô tả thuật toán.
- `outputs/`: các tệp CSV, JSON, PNG được tạo tự động.
- `logs/`: nhật ký chạy chương trình.

## Cài đặt môi trường (Python 3.12)

```bash
cd PRACTICE_3_CLUSTERING_RETAIL_CUSTOMERS
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Chuẩn bị dữ liệu

Đọc `data/README.md`. Không tự tạo dữ liệu giả khi chưa có tệp đầu vào. Kiểm tra CSV thực tế có các cột CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100), đồng thời ghi lại nguồn và giấy phép sử dụng.

## Chạy phân cụm

```bash
python scripts/cluster.py --data data/Mall_Customers.csv
python scripts/cluster.py --data data/Mall_Customers.csv --eps 0.75 --min-samples 5
python scripts/cluster.py --data data/Mall_Customers.csv --without-gender
```

Kết quả được lưu trong `outputs/`: metrics.csv, dbscan_parameter_sweep.csv, customer_cluster_assignments.csv, cluster_profiles.csv, clustering_report.json, elbow_values.csv, silhouette_by_k.csv và các hình trong `outputs/figures/`.

## Phân đoạn ảnh bằng K-Means

Sử dụng ảnh đầu vào mà bạn có quyền sử dụng:

```bash
python scripts/image_segmentation.py --image data/sample.jpg --k 5
```

Đầu ra gồm `outputs/segmented_image.png` và `outputs/figures/image_segmentation_comparison.png`. Đây là phân cụm màu của điểm ảnh, không phải phân đoạn ngữ nghĩa để nhận diện vật thể.

## Trước khi báo cáo

Đọc `docs/METHODOLOGY.md`, `docs/RESULTS.md`, `docs/VIVA_QUESTIONS.md` và `docs/REFERENCES.md`. Chỉ trình bày số liệu trong RESULTS sau khi chạy lại quy trình trên đúng bộ dữ liệu; không xem số liệu có sẵn là kết quả của lần chạy mới.
