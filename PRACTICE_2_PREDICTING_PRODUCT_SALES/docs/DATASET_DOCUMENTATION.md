# Tài liệu dữ liệu — Practice 2

Nguồn: UCI Online Retail, ID 352, DOI 10.24432/C5BW33, CC BY 4.0. Bộ dữ liệu ghi nhận giao dịch của nhà bán lẻ trực tuyến tại Anh từ 01/12/2010 đến 09/12/2011; UCI mô tả 541.909 instances.

| Cột | Ý nghĩa | Xử lý |
|---|---|---|
| InvoiceNo | Mã hóa đơn; tiền tố C thường biểu thị hủy | Loại hóa đơn hủy |
| StockCode | Mã sản phẩm | Dùng nhóm chuỗi thời gian |
| Description | Mô tả sản phẩm | Không dùng baseline |
| Quantity | Số lượng | Chỉ lấy giá trị dương |
| InvoiceDate | Ngày giờ | Tổng hợp theo tháng |
| UnitPrice | Đơn giá GBP | Chỉ lấy giá trị dương |
| CustomerID | Mã khách hàng | Không dùng baseline |
| Country | Quốc gia | Không dùng baseline |

Target tự tạo: tổng Quantity × UnitPrice theo sản phẩm-tháng. Features: lag_1, lag_2, lag_3, rolling_mean_3 (chỉ quá khứ), tháng và StockCode. Đây không phải cột Product Sales có sẵn. Do loại quantity âm, chỉ số đo gross sales trước hoàn trả, không phải doanh thu thuần kế toán. CustomerID/Description có thể thiếu.
