# Lab 2 — Dự báo doanh thu sản phẩm

Dự báo **doanh thu theo mã sản phẩm (StockCode) và tháng** từ bộ dữ liệu UCI Online Retail (ID 352). Biến mục tiêu được tạo bằng cách cộng `Quantity × UnitPrice` theo từng sản phẩm-tháng (GBP). Đây là bài toán dự báo doanh thu, không phải dự báo số lượng bán hoặc tổng doanh thu toàn cửa hàng.

## Cấu trúc thư mục
- `data/`: dữ liệu cục bộ nếu cần; có thể tải từ UCI bằng mã nguồn.
- `scripts/train.py`: làm sạch dữ liệu, tạo bảng theo tháng và đặc trưng trễ, huấn luyện, kiểm định chéo theo thời gian, đánh giá và lưu mô hình.
- `scripts/predict.py`: dự báo từ dữ liệu lịch sử.
- `notebooks/02_sales_forecasting.ipynb`: sổ tay hướng dẫn phân tích.
- `docs/`: tài liệu dữ liệu, phương pháp, kết quả, câu hỏi vấn đáp, tài liệu tham khảo, mô tả/thiết kế dự án và thuật toán.
- `outputs/`: tệp CSV, JSON và biểu đồ được tạo khi chạy.
- `models/`: mô hình đã huấn luyện.
- `logs/`: nhật ký chạy chương trình.

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

Lần chạy đầu tiên cần Internet để thư viện `ucimlrepo` tải dữ liệu UCI nếu chưa có tệp `data/Online Retail.xlsx`. Nếu tải thất bại, chương trình không tự tạo dữ liệu giả.

## Ví dụ dự báo

```bash
python scripts/predict.py --product-code "85123A" --lag-1 120 --lag-2 95 --lag-3 110 --month 12
```

Các giá trị đầu vào chỉ minh họa cách dùng lệnh, không phải số liệu thực tế đã được xác minh.

## Giới hạn quan trọng

Bộ dữ liệu không có thông tin quảng cáo, ngân sách tiếp thị, hàng tồn kho, nhân khẩu học hoặc đánh giá sản phẩm. Vì vậy dự án không thể kết luận tác động của những yếu tố này. Xem `docs/METHODOLOGY.md`, `docs/RESULTS.md` và `docs/REFERENCES.md` để biết định nghĩa biến mục tiêu, cách chia dữ liệu theo thời gian, chỉ số đánh giá và giới hạn của mô hình.
