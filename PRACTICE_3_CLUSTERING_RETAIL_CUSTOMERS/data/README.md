# Dữ liệu đầu vào — Lab 3

Đặt file CSV tên `Mall_Customers.csv` trong thư mục này. Script mặc định đọc:

`PRACTICE_3_CLUSTERING_RETAIL_CUSTOMERS/data/Mall_Customers.csv`

## Cấu trúc cần có

Các cột cần thiết:
- `Gender`
- `Age`
- `Annual Income (k$)` (script cũng chấp nhận một số biến thể tên cột)
- `Spending Score (1-100)`
- `CustomerID` có thể có; không được dùng làm đặc trưng khoảng cách.

Bản Mall Customers phổ biến có 200 dòng. Không mặc định file tải về chắc chắn là bản đó: hãy kiểm tra số dòng, tên cột, giá trị thiếu, dòng trùng và miền giá trị trước khi chạy.

## Nguồn và license

Dataset này được nhiều trang lưu trữ lại; cần ghi URL tải, ngày tải và license của đúng bản CSV bạn sử dụng. Tài liệu tham khảo và mô tả schema nằm trong `../docs/DATASET_DOCUMENTATION.md` và `../docs/REFERENCES.md`. Không tự ý commit dữ liệu nếu chưa xác minh quyền phân phối.

## Kiểm tra nhanh trong Codespaces

```bash
python - <<'PY'
import pandas as pd
p = "data/Mall_Customers.csv"
df = pd.read_csv(p)
print("shape:", df.shape)
print("columns:", df.columns.tolist())
print("missing:\n", df.isna().sum())
print("duplicates:", df.duplicated().sum())
print(df.head())
PY
```
