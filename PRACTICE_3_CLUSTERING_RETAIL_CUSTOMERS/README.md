# Lab 3 — Clustering Retail Customers

Phân cụm Mall Customers và bài bổ sung K-Means Image Segmentation.

## Cấu trúc
- data/Mall_Customers.csv: dataset đầu vào.
- scripts/cluster.py: preprocessing, Elbow/Silhouette, K-Means, PAM K-Medoids, DBSCAN, Hierarchical, metrics, profiles, PCA, dendrogram.
- scripts/image_segmentation.py: clustering pixel theo màu.
- docs/: dataset, methodology, results, viva.
- outputs/: CSV/JSON/figures sinh tự động.

## Cài đặt (Python 3.12)
```bash
cd PRACTICE_3_CLUSTERING_RETAIL_CUSTOMERS
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Chạy clustering
```bash
python scripts/cluster.py --data data/Mall_Customers.csv
python scripts/cluster.py --data data/Mall_Customers.csv --eps 0.75 --min-samples 5
```

## Image Segmentation
```bash
python scripts/image_segmentation.py --image data/sample.jpg --k 5
```
Ảnh phải do người dùng cung cấp hoặc có quyền sử dụng. Kết quả lưu trong outputs/. Đây là clustering màu pixel, không phải semantic segmentation.

Đọc docs/METHODOLOGY.md và docs/VIVA_QUESTIONS.md; không đặt persona trước khi xem profile.
