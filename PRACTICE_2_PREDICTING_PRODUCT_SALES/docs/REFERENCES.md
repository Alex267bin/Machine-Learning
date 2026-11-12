# Tài liệu tham khảo — Lab 2: Predicting Product Sales

Ngày truy cập: 2026-11-12.

## Dataset
- UCI Machine Learning Repository — Online Retail (ID 352): https://archive.ics.uci.edu/dataset/352/online-retail
- DOI: https://doi.org/10.24432/C5BW33
- UCI mô tả 541,909 giao dịch của nhà bán lẻ trực tuyến tại Anh trong giai đoạn 01/12/2010–09/12/2011; các trường gồm InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID và Country. Dataset có giấy phép CC BY 4.0; cần ghi công UCI.

## Phương pháp
- scikit-learn — TimeSeriesSplit: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
- scikit-learn — RandomizedSearchCV: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
- scikit-learn — Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html

## Trích dẫn
Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33

## Phạm vi
Nguồn UCI xác nhận các trường giao dịch thực có. Đặc trưng lag, rolling mean, doanh thu sản phẩm-tháng và target trong dự án được nhóm xây dựng từ dữ liệu gốc, không phải cột có sẵn. Không suy diễn tác động của quảng cáo, khuyến mãi, tồn kho hoặc nhân khẩu học vì dataset hiện dùng không cung cấp các biến này.
