# Lab 2 — Predicting Product Sales

Dự báo **doanh thu theo StockCode và tháng** từ UCI Online Retail (ID 352). Target được nhóm tạo bằng cách cộng `Quantity × UnitPrice` theo sản phẩm-tháng (GBP). Đây là bài toán dự báo doanh thu, không phải số lượng bán hoặc tổng doanh thu toàn cửa hàng.

## Cấu trúc
- `data/`: dữ liệu cục bộ nếu cần; có thể tải từ UCI bằng script.
- `scripts/train.py`: làm sạch, tạo panel/lag, train, temporal CV tuning, đánh giá và lưu model.
- `scripts/predict.py`: dự báo từ lịch sử lag.
- `notebooks/02_sales_forecasting.ipynb`: notebook học tập.
- `docs/`: dataset, methodology, results, viva questions, references.
- `outputs/`: CSV, JSON và figures sinh khi chạy.
- `models/`: model artifact.
- `logs/`: log chạy.

## Cài đặt và chạy (Python 3.12)

```bash
cd PRACTICE_2_PREDICTING_PRODUCT_SALES
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/train.py
```

Windows PowerShell:
```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/train.py
```

Lần đầu cần Internet để `ucimlrepo` tải UCI nếu chưa có `data/Online Retail.xlsx`. Script không tạo dữ liệu giả khi tải thất bại.

## Dự báo minh họa

```bash
python scripts/predict.py --product-code "85123A" --lag-1 120 --lag-2 95 --lag-3 110 --month 12
```

Các giá trị đầu vào chỉ minh họa cú pháp, không phải số liệu thực tế được xác minh.

## Giới hạn quan trọng

Dataset không có biến quảng cáo, ngân sách marketing, tồn kho, nhân khẩu học hoặc đánh giá sản phẩm. Vì vậy dự án không thể kết luận tác động của các yếu tố đó. Xem `docs/METHODOLOGY.md`, `docs/RESULTS.md` và `docs/REFERENCES.md` để biết định nghĩa target, cách chia theo thời gian, metric và giới hạn.
