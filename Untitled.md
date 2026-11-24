# Dàn ý tiểu luận PRJ‑05
**Tên đề xuất:** Phân tích biến động và dự báo lợi suất cổ phiếu thuộc S&P 500 bằng Python, giai đoạn 2021–2026. Xác nhận lại phạm vi ngày và danh sách mã trước khi chốt tên.

## Hướng làm toàn bài
Dùng giá đóng cửa để trả lời hai câu hỏi liên tiếp. Thứ nhất, các cổ phiếu và danh mục đã sinh lợi và biến động như thế nào? Thứ hai, thông tin đã biết sau khi đóng cửa hôm nay có giúp dự báo lợi suất phiên kế tiếp tốt hơn dự báo bằng 0 hay không? Câu đầu sử dụng thống kê lịch sử. Câu sau phải được đánh giá trên các ngày mô hình chưa từng thấy.

Tệp gốc DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv có 622.243 dòng dữ liệu và tám trường Date, Ticker, Open, High, Low, Close, Volume, DGS3MO. Phạm vi phân tích đã chọn dùng Date, Ticker, Close và các biến tự tính từ ba trường này. Dữ liệu mẫu đã cho thấy ngày dùng cả dấu gạch ngang và dấu gạch chéo. Các số liệu thiếu, số mã và kết quả mô hình phải được tính lại trên toàn bộ CSV.

## Phần đầu
Trang bìa, cam đoan, cảm ơn, mục lục tự động, danh mục viết tắt, bảng và hình. Viết tóm tắt 250–350 từ sau cùng, nêu bài toán, quy mô mẫu thực dùng, cách đánh giá và hai kết quả định lượng nổi bật.

## Chương 1. Tổng quan đề tài và mục tiêu nghiên cứu
**1.1 Bối cảnh.** Dùng ví dụ hai mã có mức tăng cuối kỳ tương tự nhưng mức dao động khác nhau để dẫn vào nhu cầu đo rủi ro.
**1.2 Câu hỏi.** Mã nào biến động mạnh trong cùng giai đoạn? Danh mục tỷ trọng đều có lợi suất và Sharpe bao nhiêu? Hồi quy có giảm sai số dự báo ngoài mẫu không?
**1.3 Mục tiêu.** Lập bảng biến động theo mã, xây dựng chuỗi lợi suất danh mục và đánh giá mô hình dự báo trước một phiên.
**1.4 Đối tượng và phạm vi.** Đơn vị gốc là một mã trong một phiên. Báo cáo ngày đầu, ngày cuối và số mã thực tế. Ghi tần suất ngày.
**1.5 Ý nghĩa.** Phục vụ theo dõi rủi ro và đánh giá xem dữ liệu giá quá khứ cung cấp bao nhiêu thông tin dự báo.

## Chương 2. Cơ sở lý thuyết và phương pháp
**2.1 Các đại lượng.** Lợi suất đơn ngày t bằng Close(t)/Close(t−1) − 1. Độ biến động 20 phiên là độ lệch chuẩn của 20 lợi suất liên tiếp. Với danh mục cân bằng tỷ trọng mỗi phiên, lợi suất ngày là trung bình lợi suất các mã trong rổ. Sharpe năm hóa bằng căn bậc hai của 252 nhân trung bình lợi suất ngày chia độ lệch chuẩn ngày, với giả định lãi suất phi rủi ro bằng 0. Nêu rõ giả định khi diễn giải.
**2.2 Tổng quan nghiên cứu.** Lập bảng tài liệu theo tác giả, dữ liệu, biến mục tiêu, cách chia mẫu, kết quả và điểm có thể vận dụng. Chỉ trích dẫn tài liệu đã đọc.
**2.3 Quy trình.** Kiểm kê → làm sạch → tạo chuỗi lợi suất → phân tích danh mục → kiểm định → dự báo → đánh giá.
**2.4 Phương pháp.** Giải thích ADF, hồi quy tuyến tính và Ridge. Giải thích vì sao cần mốc dự báo bằng 0. MAE cho biết sai số tuyệt đối trung bình, RMSE nhấn mạnh các phiên sai số lớn.
**2.5 Công cụ.** pandas cho xử lý bảng và thời gian, matplotlib cho biểu đồ, statsmodels cho ADF, scikit-learn cho hồi quy và đánh giá. Ghi phiên bản dùng thực tế.

## Chương 3. Thu thập, ghép nối và khám phá dữ liệu
**3.1 Kiểm kê.** Lập bảng tám trường gốc, kiểu đọc ban đầu, đơn vị, số thiếu và vai trò. Ghi tên tệp được cấp. Chỉ ghi nguồn tải ban đầu khi có căn cứ.
**3.2 Ghép bảng và bộ nhớ.** Giữ một bảng giá chính. Từ đó tổng hợp bảng thống kê theo ngày gồm số mã có lợi suất và lợi suất bình quân. Ghép lại theo Date bằng merge với validate='many_to_one', đối chiếu số dòng và số ngày không khớp. Đo dung lượng trước/sau khi chuyển Ticker sang category. Ghi rõ bảng tổng hợp là sản phẩm dẫn xuất. Vì đầu vào được cấp là một CSV, cần xác nhận với giảng viên cách đáp ứng quy định đa tệp trước khi nộp.
**3.3 Làm sạch.** Giữ thứ tự dòng gốc để kiểm tra các đoạn mất ngày theo từng mã. Chuẩn hóa định dạng, kiểm tra khóa (Ticker, Date), giá thiếu và giá không dương. Chỉ phục hồi ngày khi hai mốc kẹp xác định duy nhất dãy phiên giao dịch, đúng số dòng và không tạo khóa trùng. Lưu cờ phục hồi. Giữ NaN trong bảng chính, lọc riêng theo từng phép tính.
**3.4 Thống kê mô tả.** Báo cáo số dòng gốc, số khóa hợp lệ, số lợi suất tính được và số quan sát dùng cho mô hình. So sánh các mã theo lợi suất trung bình, trung vị, biến động và độ phủ trên cùng kỳ.
**3.5 Biểu đồ và danh mục.** Trước làm sạch, vẽ tỷ lệ thiếu theo trường và độ phủ theo mã. Sau làm sạch, vẽ giá quy về 100 tại ngày đầu chung, biến động trượt và đường giá trị danh mục bắt đầu từ 100. Chọn rổ và ngày bắt đầu theo dữ liệu có sẵn tại thời điểm lập rổ. Với ngày thiếu lợi suất thành viên, đánh dấu thiếu và báo cáo độ phủ. Tính lợi suất tháng bằng tích (1+r) theo tháng trừ 1 bằng resample, chỉ báo cáo tháng đủ dữ liệu. Lập bảng lợi suất, biến động và Sharpe cùng khoảng thời gian.
**3.6 Kiểm định.** So sánh ADF trên chuỗi giá và chuỗi lợi suất của cùng mã đại diện. Ghi khoảng thời gian liên tục, số quan sát, độ trễ, thống kê và p-value. H0 là chuỗi có nghiệm đơn vị. Nếu p < 0,05, bác bỏ H0 theo đặc tả đã chọn. Phân biệt tính dừng với khả năng dự báo.

## Chương 4. Xây dựng mô hình và đánh giá
**4.1 Tạo đặc trưng.** Một hàng tại phiên t dùng lợi suất phiên t, lợi suất các phiên trước, biến động 20 phiên và tỷ số MA5/MA20. Nhãn là lợi suất từ cuối t đến cuối phiên kế tiếp. Tính mọi độ trễ theo mã, kiểm tra hai phiên liền kề trên lịch giao dịch. In năm hàng của một mã để kiểm tra nhãn thủ công.
**4.2 Chia tập.** Sắp xếp các ngày duy nhất, dùng khoảng 80% ngày đầu để huấn luyện và 20% cuối để kiểm tra. Mọi mã cùng ngày thuộc cùng một tập. Loại hàng huấn luyện có ngày nhãn chạm tập kiểm tra. Dùng Pipeline để chỉ học tham số chuẩn hóa trên tập huấn luyện.
**4.3 Huấn luyện.** So sánh dự báo bằng 0, hồi quy tuyến tính và Ridge trên cùng tập quan sát. Nếu chọn hệ số phạt Ridge, dùng các cửa sổ xác thực tiến dần trong tập huấn luyện.
**4.4 Đánh giá.** Bảng theo mô hình gồm số phiên, số quan sát, MAE, RMSE, R². Dùng cùng đơn vị và bổ sung kết quả theo mã để thấy chênh lệch. Vẽ lợi suất dự báo và thực tế trên một đoạn kiểm tra có ghi ngày.
**4.5 Diễn giải.** So sánh dấu và độ lớn hệ số sau chuẩn hóa. Giải thích đây là quan hệ dự báo có điều kiện. Kiểm tra tương quan giữa các đặc trưng khi hệ số thiếu ổn định.
**4.6 Thảo luận.** Mô hình nào giảm sai số so với mốc? Kết quả có phụ thuộc vài mã hoặc phiên biến động mạnh không? Nếu R² âm hoặc không vượt mốc, báo cáo kết quả thực tế và xem xét giới hạn của dữ liệu giá.

## Chương 5. Khuyến nghị quản trị và kết luận
**5.1 Khuyến nghị.** Liên hệ biến động, Sharpe và độ phủ để giải thích trường hợp nào cần theo dõi rủi ro. Chỉ đề xuất sử dụng tín hiệu dự báo khi có bằng chứng ngoài mẫu.
**5.2 Lộ trình.** Mỗi phiên cập nhật Close, kiểm tra khóa, tính lại chỉ tiêu, lưu dự báo và đối chiếu khi xuất hiện giá phiên sau.
**5.3 Hạn chế.** Dữ liệu thiếu, khả năng thiên lệch do chọn mã, tính điều chỉnh của Close chưa được xác nhận, giả định lãi suất bằng 0, chưa tính chi phí giao dịch. Lưu nguồn và nhật ký biến đổi để tái lập.
**5.4 Hướng phát triển và kết luận.** Đánh giá trên nhiều cửa sổ thời gian. Kết luận lần lượt theo ba câu hỏi chương 1, mỗi kết luận dẫn về một bảng hoặc hình.

## Các lỗi dễ gặp và cách xử lý
| Dấu hiệu | Nguyên nhân cần kiểm tra | Cách xử lý |
|---|---|---|
| Ngày hợp lệ thành NaT | Trộn dấu / và - | Thống kê từng mẫu, chuẩn hóa rồi đối chiếu dòng chuyển đổi lỗi. |
| Số ngày thiếu trước và sau không khớp | Dùng các lần chạy hoặc mẫu số khác nhau | Đối chiếu trên cùng bảng bằng số thiếu đầu kỳ trừ số phục hồi thực tế. Ví dụ 61.305 − 61.208 = 97. Nếu báo cáo còn 96 phải truy ra dòng chênh. |
| Lợi suất bằng 0 hàng loạt hoặc nhảy mạnh sau khoảng trống | Điền giá trước hoặc bỏ dòng thiếu trước khi tính | Giữ lịch từng mã, dùng pct_change(fill_method=None), kiểm tra khoảng cách phiên. |
| Một mã có hai giá cùng ngày | Khóa trùng, bản ghi xung đột | Gộp dòng giống hệt sau khi ghi số lượng. Cách ly khóa có giá mâu thuẫn. |
| Biến động đầu chuỗi bị thiếu | Cửa sổ chưa đủ 20 lợi suất | Giữ NaN, báo cáo số hàng còn đủ điều kiện. |
| Bảng nở dòng sau merge | Khóa bảng ngày chưa duy nhất | Kiểm tra khóa, quan hệ ghép và số dòng trước/sau. |
| Sharpe vô hạn hoặc tăng bất thường | Độ lệch chuẩn bằng 0, quá ít phiên hoặc lẫn đơn vị ngày/năm | Báo không xác định khi mẫu không đủ hoặc mẫu số bằng 0. Thống nhất đơn vị. |
| Sai số kiểm tra thấp bất thường | Nhãn tương lai lọt vào biến, chia ngẫu nhiên hoặc chuẩn hóa toàn mẫu | Kiểm tra ngày nguồn của đặc trưng và nhãn, tách theo ngày và chạy lại pipeline. |
| MAPE cực lớn | Lợi suất thực bằng hoặc gần 0 | Ưu tiên MAE, RMSE và R², giải thích giới hạn MAPE. |
| Đường tích lũy vẫn chạy qua phiên mất giá | Phép tích mặc định bỏ qua NaN | Chia thành đoạn đủ dữ liệu hoặc báo thiếu kết quả toàn kỳ. |

## Thứ tự thực hiện và hồ sơ nộp
1. Kiểm kê CSV và xuất bảng chất lượng trước xử lý. Chốt phương án đa tệp với giảng viên.
2. Làm sạch và kiểm tra khóa. Lưu bảng đối chiếu trước/sau và ghi nhật ký từng quyết định.
3. Kiểm tra lợi suất thủ công trên hai phiên liên tiếp, sau đó mới chạy toàn bộ mã, danh mục và ADF.
4. Chốt mốc chia theo ngày, tạo bảng đặc trưng và chạy ba phương án dự báo trên cùng mẫu.
5. Viết chương 3–4 từ kết quả thật, hoàn thiện chương 1–2, chương 5 và tóm tắt sau cùng.
6. Nộp MSSV_NhomXX_TieuLuan.pdf và workspace Antigravity IDE gồm mã Python, dữ liệu mẫu, nhật ký làm việc.md. Phụ lục A trình bày mã theo PEP 8, phụ lục B trích nhật ký. Tài liệu tham khảo theo APA 7. Báo cáo A4 dọc, lề trái 3 cm, các lề khác 2 cm, Times New Roman hoặc Calibri 12–13 pt, giãn dòng 1,3–1,5. Đặt tên bảng phía trên, nguồn bên dưới và tên hình dưới hình.
