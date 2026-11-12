# Câu hỏi vấn đáp — Lab 2

## Input / Output / Purpose
- **Input:** StockCode, lag_1/lag_2/lag_3, rolling_mean_3, month_num.
- **Output:** doanh thu dự báo của một sản phẩm trong một tháng (GBP).
- **Purpose:** dự báo doanh thu sản phẩm-tháng từ lịch sử giao dịch.

## Câu hỏi nền tảng
1. **Dataset gồm gì?** UCI Online Retail có InvoiceNo, StockCode, Quantity, InvoiceDate, UnitPrice và các trường khác. Pipeline dùng trường cần thiết để tạo target.
2. **Target tạo thế nào?** Revenue giao dịch = Quantity × UnitPrice; target là tổng revenue theo StockCode và tháng.
3. **Vì sao loại InvoiceNo bắt đầu C?** Đây là hóa đơn hủy/return trong dataset; đồng thời loại Quantity/UnitPrice không dương theo định nghĩa doanh thu bán hàng của bài.
4. **Lag feature là gì?** Lag 1/2/3 là doanh thu một/hai/ba tháng trước.
5. **Rolling mean là gì?** Trung bình ba tháng trước; shift(1) để không lấy doanh thu tháng đang dự báo.
6. **Vì sao tạo tháng trống = 0?** Panel cần tháng liên tục; đây là giả định không có giao dịch quan sát được nghĩa là doanh thu 0.
7. **Vì sao One-Hot StockCode?** Mã sản phẩm là categorical, không có thứ tự số học.
8. **Vì sao chia theo thời gian?** Dự báo tương lai phải chỉ học từ quá khứ; random split có thể gây leakage.
9. **TimeSeriesSplit làm gì?** Tạo các fold train trước-validation sau. Code chia theo tháng hoàn chỉnh để không cắt một tháng thành hai phía.
10. **Vì sao tuning chỉ trên train?** Để test giữ vai trò holdout độc lập.
11. **MAE/MSE/RMSE/R²?** MAE là sai số tuyệt đối trung bình; MSE là bình phương sai số; RMSE cùng đơn vị target; R² so với baseline trung bình và có thể âm.
12. **R² âm có phải code sai?** Không nhất thiết; mô hình có thể kém hơn baseline trên test.
13. **Feature importance có nghĩa nhân quả?** Không, chỉ là mức độ sử dụng feature trong mô hình.
14. **Dự báo sản phẩm mới?** OneHotEncoder không lỗi với category mới, nhưng thiếu lịch sử lag nên không đảm bảo chất lượng.
15. **Nếu thêm promotion/inventory?** Chỉ dùng feature biết được tại thời điểm dự báo và kiểm tra leakage.
16. **RMSE lớn hơn MAE nhiều?** Có thể có một số sai số lớn kéo RMSE lên; cần kiểm tra residual/outlier.

## Câu hỏi xoáy
- Vì sao không dùng doanh thu hiện tại làm feature? Vì đó chính là target, gây target leakage.
- Vì sao không shuffle? Vì phá thứ tự thời gian.
- Vì sao dự báo âm bị chặn về 0? Target doanh thu được định nghĩa không âm; đây là post-processing và metrics được tính sau bước này.
- Hạn chế dataset? Dữ liệu lịch sử 2010–2011, thiếu promotion/inventory/marketing, không đại diện thị trường hiện tại.

## Câu hỏi xoáy bổ sung — Cross-validation và Model Selection

17. **Vì sao chọn mô hình theo CV RMSE thay vì Test RMSE?**
    Vì test cần được giữ độc lập để đánh giá cuối cùng. Nếu dùng test để chọn mô hình, kết quả đánh giá sẽ bị thiên lệch.

18. **Mô hình nào được chọn và vì sao?**
    Random Forest (tuned), vì có CV RMSE thấp nhất: 413.78 GBP.

19. **Tại sao Gradient Boosting có Test RMSE thấp nhất nhưng không được chọn?**
    Vì mô hình được chọn dựa trên CV RMSE của train, không dựa trên kết quả test.

20. **CV RMSE và Test RMSE khác nhau thế nào?**
    CV RMSE là sai số trung bình trên các fold validation trong tập train. Test RMSE là sai số trên tập holdout độc lập.

21. **Vì sao CV RMSE thấp hơn nhiều so với Test RMSE?**
    Có thể do phân phối doanh thu ở các tháng test khác với các tháng train. Đây có thể là dấu hiệu thay đổi theo thời gian trong dữ liệu.

22. **TimeSeriesSplit có giống K-Fold thông thường không?**
    Không. TimeSeriesSplit giữ thứ tự thời gian: dữ liệu train luôn nằm trước dữ liệu validation.

23. **Tuning Random Forest có sử dụng test không?**
    Không. RandomizedSearchCV chỉ sử dụng dữ liệu train và các fold CV.
