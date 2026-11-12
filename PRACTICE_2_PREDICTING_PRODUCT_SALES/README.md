# Practice 2 — Dự đoán doanh số sản phẩm

## Mục tiêu và định nghĩa target
Dự báo doanh thu tháng kế tiếp theo từng sản phẩm từ UCI Online Retail. Dữ liệu không có cột Product Sales; vì vậy target được tạo minh bạch là tổng Quantity × UnitPrice theo StockCode-tháng (GBP). Đây là bài toán regression theo thời gian, không dự báo doanh thu của chính giao dịch đang quan sát.

## Dữ liệu
UCI Online Retail, dataset ID 352, 541.909 giao dịch từ 01/12/2010 đến 09/12/2011. Các cột: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country. Nguồn: https://archive.ics.uci.edu/dataset/352/online+retail — CC BY 4.0. Tải bằng ucimlrepo; không commit dữ liệu gốc.

## Chạy
```bash
pip install -r requirements.txt
python scripts/train.py
python scripts/predict.py --product-code "85123A" --lag-1 120 --lag-2 100 --lag-3 90 --month 1
```
Các giá trị lag trên chỉ minh họa cú pháp, không phải số liệu thực nghiệm.

## Quy trình
EDA và làm sạch; loại hóa đơn hủy, quantity/unit price không dương; tổng hợp doanh thu tháng; tạo lag 1–3 và rolling mean chỉ từ quá khứ; chia train/test theo thời gian; so sánh Linear Regression, Decision Tree, Random Forest, Gradient Boosting; đánh giá MAE, MSE, RMSE, R²; lưu pipeline tốt nhất và dự báo.

## Giới hạn
Lịch sử chỉ hơn một năm; thiếu dữ liệu marketing, nhân khẩu học và đặc trưng mô tả sản phẩm. Không khẳng định mô hình dự báo mùa vụ dài hạn.
