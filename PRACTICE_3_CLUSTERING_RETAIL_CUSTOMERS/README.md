# Lab 3 — Clustering Retail Customers

Bài thực hành phân cụm khách hàng trên Mall Customers và phần mở rộng K-Means Image Segmentation.

## Cấu trúc
- `data/Mall_Customers.csv`: dữ liệu đầu vào, tải riêng theo hướng dẫn `data/README.md`.
- `scripts/cluster.py`: kiểm tra dữ liệu, scaling, Elbow/Silhouette, K-Means, K-Medoids (PAM), DBSCAN, Hierarchical Ward, metrics, profiles, PCA và dendrogram.
- `scripts/image_segmentation.py`: K-Means trên vector màu RGB của pixel.
- `notebooks/03_customer_clustering.ipynb`: notebook phân tích.
- `docs/`: dataset, methodology, results, viva questions, references.
- `outputs/`: CSV, JSON, PNG sinh tự động.
- `logs/`: nhật ký chạy.

## Môi trường (Python 3.12)

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

Đọc `data/README.md`. Không tạo dữ liệu giả khi file đầu vào chưa có. Kiểm tra file CSV thực tế có các cột CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100), và lưu lại nguồn/license của bản tải.

## Chạy phân cụm

```bash
python scripts/cluster.py --data data/Mall_Customers.csv
python scripts/cluster.py --data data/Mall_Customers.csv --eps 0.75 --min-samples 5
python scripts/cluster.py --data data/Mall_Customers.csv --without-gender
```

Kết quả được sinh vào `outputs/`: metrics.csv, dbscan_parameter_sweep.csv, customer_cluster_assignments.csv, cluster_profiles.csv, clustering_report.json, elbow_values.csv, silhouette_by_k.csv và hình trong `outputs/figures/`.

## K-Means Image Segmentation

Dùng ảnh đầu vào mà bạn có quyền sử dụng:

```bash
python scripts/image_segmentation.py --image data/sample.jpg --k 5
```

Đầu ra gồm `outputs/segmented_image.png` và `outputs/figures/image_segmentation_comparison.png`. Đây là phân cụm màu pixel, không phải semantic segmentation nhận diện vật thể.

## Trước khi báo cáo

Đọc `docs/METHODOLOGY.md`, `docs/RESULTS.md`, `docs/VIVA_QUESTIONS.md` và `docs/REFERENCES.md`. Chỉ trình bày số liệu RESULTS sau khi chạy lại pipeline trên đúng dataset; không coi số liệu ghi sẵn là kết quả của lần chạy mới.
