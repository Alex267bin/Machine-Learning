# Lab 2 — Predicting Product Sales

Dự báo doanh thu theo **sản phẩm-tháng** từ UCI Online Retail (ID 352). Target = tổng Quantity × UnitPrice theo StockCode và tháng (GBP).

## Cấu trúc
- data/: dữ liệu cục bộ nếu cần.
- scripts/train.py: clean, tạo panel/lag, train, temporal CV tuning, đánh giá và lưu model.
- scripts/predict.py: dự báo từ lịch sử lag.
- notebooks/: notebook học tập.
- docs/: dataset, methodology, results, viva.
- outputs/: CSV, JSON và figures sinh khi chạy.
- models/: artifact; logs/: log chạy.

## Cài đặt và chạy (Python 3.12)
```bash
cd PRACTICE_2_PREDICTING_PRODUCT_SALES
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/train.py
```
Lần đầu cần Internet để ucimlrepo tải UCI. Nếu không có mạng/dataset, script sẽ báo lỗi thay vì tạo kết quả giả.

## Dự báo minh họa
```bash
python scripts/predict.py --product-code "85123A" --lag-1 120 --lag-2 95 --lag-3 110 --month 12
```
Các con số chỉ minh họa cú pháp, không phải kết quả thực nghiệm.

## Kết quả
Xem docs/RESULTS.md. Metrics được sinh từ holdout theo thời gian.
