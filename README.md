# Machine Learning — Bài thực hành 2 và 3

Repository gồm hai bài thực hành độc lập:

- [Practice 2 — Dự đoán doanh số sản phẩm](PRACTICE_2_PREDICTING_PRODUCT_SALES/README.md)
- [Practice 3 — Phân cụm khách hàng bán lẻ](PRACTICE_3_CLUSTERING_RETAIL_CUSTOMERS/README.md)

## Môi trường
Python 3.10–3.12. Tạo môi trường ảo và cài dependencies riêng cho từng bài:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r PRACTICE_2_PREDICTING_PRODUCT_SALES/requirements.txt
pip install -r PRACTICE_3_CLUSTERING_RETAIL_CUSTOMERS/requirements.txt
```

Mỗi bài có dữ liệu, scripts, notebooks, docs, outputs và models riêng. Không commit dữ liệu thô, mô hình hoặc môi trường ảo.
