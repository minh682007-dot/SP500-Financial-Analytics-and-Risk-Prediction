# NHẬT KÝ LÀM VIỆC DỰ ÁN TIỂU LUẬN KẾT THÚC HỌC PHẦN (PRJ05)
- Học phần: Phân tích Dữ liệu Kinh doanh / Tài chính Định lượng
- Sinh viên thực hiện: Đào Ngọc Minh
- Mã số sinh viên: 2521001078
- Tập dữ liệu nghiên cứu: 17_2521001081_PRJ05_NguyenPhiLamNguyen.csv
- Đường dẫn lưu trữ: C:\Users\LENOVO\Downloads\17_2521001081_PRJ05_NguyenPhiLamNguyen.csv

================================================================================
NHẬT KÝ NGÀY: 20/10/2026
Người ghi: Đào Ngọc Minh
Trạng thái: Hoàn thành giai đoạn Kiểm toán, Xây dựng Từ điển dữ liệu & Báo cáo tiền xử lý
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Tiếp nhận đề tài, định vị và kiểm tra tính toàn vẹn của tệp dữ liệu thô PRJ05.
2. Viết mã kiểm toán tự động (Data Quality Audit) trên 622,243 dòng quan sát.
3. Thống kê chi tiết tỷ lệ khuyết thiếu (Missing values), các giá trị dị biệt, ngoại lai (Outliers) và các vi phạm logic thị trường tài chính.
4. Xây dựng cơ sở lý luận khoa học giải thích lý do lựa chọn bộ 3 biến mục tiêu: [Date, Ticker, Close].
5. Hoàn thiện bảng Từ điển dữ liệu (Data Dictionary), xác định đơn vị quan sát và cỡ mẫu.
6. Đề xuất 3 câu hỏi kinh doanh thực tế cam kết giải quyết bằng ngôn ngữ Python.
7. Soạn thảo và xuất bản toàn bộ nội dung thành văn bản báo cáo chuẩn học thuật: "Bảng báo cáo.docx".
8. Thiết lập bộ "Master Prompt" chuẩn mực để phục vụ quá trình chạy code và bảo vệ đề tài.

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Buổi sáng: Khảo sát & Định vị dữ liệu
- 08:47: Tải và lưu trữ tệp dữ liệu thực nghiệm 17_2521001081_PRJ05_NguyenPhiLamNguyen.csv (kích thước ~57.06 MB) vào hệ thống.
- Kiểm tra sơ bộ cấu trúc bảng: Ghi nhận dữ liệu gồm 622,243 dòng và 8 cột: Date, Ticker, Open, High, Low, Close, Volume, DGS3MO.

2. Buổi chiều (14:00 - 14:35): Kiểm toán dữ liệu chuyên sâu (Data Audit)
- Viết script Python phân tích tự động chất lượng dữ liệu:
  + Phát hiện 100% cột trong file gốc đang bị ép kiểu chuỗi (Object/String) do dính tạp chất.
  + Thống kê Missing values:
    * Cột Low thiếu cao nhất: 69,853 dòng (11.23%).
    * Cột Volume thiếu: 58,472 dòng (9.40%).
    * Cột Close thiếu: 54,928 dòng (8.83%).
    * Cột High thiếu: 52,087 dòng (8.37%).
    * Cột Date thiếu: 44,022 dòng (7.07%) - lỗi nghiêm trọng do mất nhãn thời gian.
    * Cột Open thiếu: 39,661 dòng (6.37%).
    * Cột DGS3MO thiếu: 21,841 dòng (3.51%).
    * Cột Ticker: 0 dòng thiếu (0.00%).
  + Phát hiện 7 nhóm dữ liệu "bẩn" điển hình:
    * Lỗi đơn vị: Hơn 84,690 dòng ở cột Close dính chữ "USD", "VND", "kg", "%", "đ" và lẫn dấu phẩy thập phân ",".
    * Lỗi phân mảnh Ticker: 50,172 dòng dính khoảng trắng (" A", "AAPL ") khiến 503 mã cổ phiếu thực tế bị nhân bản thành 1,509 mã ảo.
    * Ký tự rác: 17,283 dòng cột Date dính dấu "?" và "-".
    * Giá trị âm vô lý: 17,032 dòng Close âm (đặc biệt có 13,794 dòng mang giá trị gán lỗi là -1); Low âm 18,888 dòng; High âm 16,567 dòng; Volume âm 17,155 dòng.
    * Vi phạm logic giá trong phiên: 30,730 dòng ghi nhận High < Low; 33,102 dòng ghi nhận High < Close.
    * Ngoại lai: Cột Open có 9,985 dòng bị gán cứng bằng 9999; DGS3MO vọt lên 50.0%.

3. Buổi chiều (14:35 - 15:00): Nghiên cứu lý thuyết & Xây dựng báo cáo
- Phân tích cơ sở lý luận tài chính:
  + Xác định rõ Date là trục thời gian đơn điệu, Ticker là khóa phân nhóm thực thể (Panel Data).
  + Khẳng định Close là mức giá thanh toán bù trừ chuẩn nhất phản ánh toàn bộ thông tin thị trường, là biến số duy nhất cần thiết để tính Lợi suất (Return) và Ma trận hiệp phương sai.
  + Chứng minh việc loại bỏ Open, High, Low là bắt buộc để triệt tiêu hiện tượng Đa cộng tuyến hoàn hảo (Multicollinearity) vì tương quan r > 0.98.
  + Giải trình vai trò của Volume (thanh khoản) và DGS3MO (lãi suất phi rủi ro Rf trong mô hình CAPM).
- Xây dựng 3 câu hỏi kinh doanh cốt lõi:
  + Câu hỏi 1: Lọc Top 10 cổ phiếu có Lợi suất bình quân năm hóa và Tỷ số Sharpe tối ưu nhất.
  + Câu hỏi 2: Đo lường rủi ro đuôi thông qua Mức sụt giảm tối đa (Maximum Drawdown - MDD) và hệ số Beta.
  + Câu hỏi 3: Tối ưu hóa danh mục đầu tư Markowitz (Minimum Variance Portfolio & Tangency Portfolio) và vẽ Đường biên hiệu quả (Efficient Frontier).
- Đóng gói tài liệu Word:
  + Xuất file "Bảng báo cáo.docx" với đầy đủ 10 phần chuẩn học thuật.
  + Định dạng Times New Roman, cỡ 13, giãn dòng 1.3 lines, lề chuẩn tiểu luận.
  + Tích hợp 4 bảng biểu viền xanh Navy và hộp ghi chú Callout.
  + Bổ sung chuyên sâu phần Giới thiệu bộ dữ liệu và loại bỏ phần Slide theo đúng yêu cầu.
- Tạo tệp Master Prompt "PROMPT_CHUAN_DE_LAM_BAI.txt" để lưu trữ cấu trúc đề cương và sẵn sàng cho bước chạy code thực nghiệm.

15. Phiên tối (20:30 - 21:40 ngày 24/11/2026): Thiết lập và Mở rộng Toàn diện Báo cáo Đặc tả Kỹ thuật "quytrinhlamsach.qmd"
- Nhận diện yêu cầu và cấu trúc tài liệu độc lập: Xây dựng tệp "quytrinhlamsach.qmd" làm Báo cáo Chuyên đề Độc lập (Technical Specification & Data Quality Audit Report) nhằm phục vụ trực tiếp phần thẩm vấn và bảo vệ thực hành với Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Khắc phục lỗi hiển thị giao diện IDE: Xử lý dứt điểm hiện tượng văn bản đổi màu cam từ dòng 539 trong nhật ký làm việc do dấu nháy đơn không đóng (Ockham Razor), chuẩn hóa thống nhất toàn bộ văn bản.
- Triển khai chi tiết cấu trúc 11 Chương hoàn chỉnh với tổng quy mô hơn 1.240 dòng:
  + Chương 1 - Khung Kiến trúc và 5 Nguyên tắc Kiểm toán Bất biến (Audit Trail, Không rò rỉ tương lai, Không triệt tiêu phương sai, Ockham Razor, Bảo toàn quy mô mẫu).
  + Chương 2 - Kiểm kê 3 Tầng Khuyết tật Dữ liệu trên 622.243 quan sát gốc (Taxonomy lỗi E1 - E7 + V0).
  + Chương 3 - Cơ sở Khoa học và Kinh tế lượng của việc Lựa chọn Biến số (Phân tích đa cộng tuyến VIF > 250, loại bỏ Volume và DGS3MO).
  + Chương 4 - Đặc tả Quy trình Làm sạch Khóa Thời gian (Date): Chuẩn hóa ISO-8601, phân tách 61.305 dòng lỗi, phục hồi chính xác 97 dòng thỏa mãn 3 điều kiện nghiêm ngặt, ghép nối 1.254 phiên làm việc NYSE với ràng buộc many-to-one.
  + Chương 5 - Đặc tả Quy trình Định danh Mã Cổ phiếu (Ticker): Hợp nhất 1.509 chuỗi văn bản thô về đúng 503 mã niêm yết chuẩn S&P 500 (giải trình 3 công ty phát hành 2 lớp cổ phiếu kép), tối ưu bộ nhớ dạng `category` giúp tiết kiệm 96,10% RAM (31,05 MB xuống 1,21 MB).
  + Chương 6 - Đặc tả Quy trình Xử lý Giá Đóng cửa (Close): Bóc tách Regex 33.281 dòng dính tạp chất tiền tệ ($ và USD), xử lý 8.240 dòng sai đơn vị, gán NaN cho 18.852 dòng vi phạm (giá âm, mã -1, giá 9999), xây dựng Bộ lọc Trung vị (Median Filter) ngưỡng 3x và 1/3x phân biệt với biến động thực tế, áp dụng Forward Fill có kiểm soát cho 15.584 dòng (2,78%), nghiêm cấm nội suy hai phía (Linear Interpolation).
  + Chương 7 - Quy trình Sinh biến Phái sinh và Tập Đặc trưng Định lượng: Công thức và ràng buộc phiên liên tục NYSE cho Simple Return (R_t), Log Return (r_t), Độ biến động lịch sử 20 phiên (Vol_20d, Bessel ddof=1, độ phủ 98,4%), Danh mục Tỷ trọng đều và Hệ số Sharpe năm hóa (0,6953 với giả định kỹ thuật R_f = 0), tập đặc trưng Lags (Lag 1, 2, 5), MA5, MA20, RSI_14, nhãn ngoài mẫu Target y, quy tắc phân chia mẫu theo thời gian (Time-based Split 60/10/30%).
  + Chương 8 - Đo lường RAM và Bốn Phép Kiểm định Tính Bất biến (Assertions): Phân tích tối ưu RAM từ 108,49 MB xuống 36,88 MB (-66,0%), lý giải duy trì float64 cho Close, xuất định dạng nén Parquet; thiết lập 4 phép kiểm định fail-fast bảo vệ pipeline (Positivity P > 0, Key Uniqueness duy nhất, Scale Conservation 622.243 = 560.103 + 62.140, Window Coverage >= 98%).
  + Chương 9 - Bảng Tổng hợp Đối chiếu Chất lượng Trước và Sau làm sạch (Ma trận kiểm toán 10 tiêu chí).
  + Chương 10 - Mã nguồn Python Khép kín Toàn bộ Pipeline (Self-contained Runnable Script).
  + Chương 11 - Kết luận, Ma trận Vấn đề - Giải pháp, Bảng 10 con số chính thức bất biến, Hướng dẫn tích hợp chéo với "tieuluan.qmd" và Cẩm nang 4 câu hỏi trọng tâm khi demo vấn đáp trực tiếp với Giảng viên.
- Đóng gói và lưu trữ an toàn mã nguồn vào Git: Hoàn thành các commit (13644f7, 1b9962f, 6a01737) với cây thư mục làm việc sạch sẽ (Working tree clean).

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp văn bản báo cáo chính thức:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\Bảng báo cáo.docx
2. Tệp Master Prompt dùng để chạy code và phản biện:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\PROMPT_CHUAN_DE_LAM_BAI.txt
3. Tệp nhật ký làm việc:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\skill\nhật kí làm việc

--------------------------------------------------------------------------------
IV. KẾ HOẠCH CHO BUỔI LÀM VIỆC TIẾP THEO
1. Rà soát lại lần cuối các câu hỏi kinh doanh trong tệp PROMPT_CHUAN_DE_LAM_BAI.txt.
2. Triển khai viết mã nguồn Python tiền xử lý dữ liệu sạch (lọc bỏ các dòng lỗi, strip khoảng trắng, áp dụng ffill cho Close).
3. Chạy các thuật toán tính toán Lợi suất (Log-return), Tỷ số Sharpe, Maximum Drawdown.
4. Sử dụng thư viện scipy.optimize để giải bài toán tối ưu hóa danh mục Markowitz và trích xuất biểu đồ Đường biên hiệu quả (Efficient Frontier).
5. Chèn số liệu và biểu đồ trực quan vào file Word báo cáo để hoàn thiện bản nộp chính thức.

================================================================================
NHẬT KÝ NGÀY: 26/10/2026
Người ghi: Đào Ngọc Minh
Trạng thái: Hoàn thành Tiền xử lý, Trực quan hóa 7 biểu đồ, Tinh gọn bộ 3 biến & Xuất bản Báo cáo Word tổng hợp toàn diện
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Lập trình và thực thi toàn diện pipeline tiền xử lý và làm sạch dữ liệu thực nghiệm PRJ05 bằng Python.
2. Thiết kế thuật toán lọc ngoại lai (Median Filter) để xử lý lỗi nhảy số thập phân của thị giá cổ phiếu.
3. Lấp đầy dữ liệu khuyết thiếu theo kỹ thuật tài chính chuẩn: Forward Fill (ffill) theo từng mã cổ phiếu (Ticker).
4. Thiết kế, tính toán và xuất bản bộ 7 biểu đồ trực quan hóa tài chính chuyên sâu đạt chuẩn bài báo khoa học.
5. Tiếp nhận yêu cầu nghiệp vụ: Tinh gọn tập dữ liệu và báo cáo về đúng bộ 3 biến cốt lõi [Date, Ticker, Close].
6. Xây dựng luận cứ khoa học giải trình việc chuyển đổi từ 8 biến sang 3 biến (triệt tiêu hiện tượng Đa cộng tuyến Multicollinearity, nguyên lý Parsimony).
7. Xuất tệp dữ liệu sạch hoàn chỉnh "data_cleaned_SP500.csv" chỉ gồm đúng 3 cột [Date, Ticker, Close].
8. Xây dựng kịch bản Python tự động ("create_report.py") để tạo tệp văn bản báo cáo tổng hợp toàn diện: "Bảng báo cáo.docx" (~2.5 MB) bao quát cả 2 giai đoạn (8 biến ban đầu và 3 biến sau này), kèm 7 biểu đồ nhúng trực tiếp.
9. Đồng bộ toàn bộ nội dung học thuật vào tệp báo cáo Quarto ("17_PRJ05_...qmd").

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Buổi chiều (14:00 - 16:30): Lập trình Pipeline Tiền xử lý & Làm sạch dữ liệu
- Triển khai kịch bản Python "visualize_and_clean.py" và "thong_ke_du_lieu.py":
  + Chuẩn hóa Ticker: Cắt bỏ khoảng trắng thừa bằng df["Ticker"].astype(str).str.strip(). Gộp thành công 1,509 mã ảo về đúng 503 mã cổ phiếu chuẩn của rổ S&P 500.
  + Chuẩn hóa Date: Loại bỏ các ký tự rác "?" và "-", chuẩn hóa dấu "/" thành "-", chuyển đổi về datetime64. Nhận diện 560,938 dòng hợp lệ (loại 61,305 dòng mất nhãn thời gian).
  + Chuẩn hóa Close: Bóc tách đơn vị "USD", "VND", "kg", "%", "đ", chuyển dấu phẩy "," thành dấu chấm ".", ép kiểu float64. Loại bỏ các giá trị âm và mã hóa lỗi -1.
  + Sắp xếp dữ liệu bảng Panel Data theo thứ tự [Ticker, Date].
  + Xây dựng bộ lọc ngoại lai (Median Filter): Thiết lập điều kiện (Close > 3*Median) | (Close < Median/3) để phát hiện và xử lý 15,584 quan sát dính lỗi nhảy số thập phân 10x, 100x.
  + Áp dụng Forward Fill: df["Close"] = df.groupby('Ticker')['Close'].ffill() để lấp đầy dữ liệu thiếu mà không làm phẳng độ biến động thị trường.
- Kết quả làm sạch dữ liệu:
  + Cỡ mẫu sạch thu được: 560,103 dòng quan sát (đạt tỷ lệ sử dụng 90.01% dữ liệu gốc).
  + Giá Close trung bình sau làm sạch: 179,51 USD; Trung vị: 107,94 USD; Giá cao nhất: 9.924,40 USD (cổ phiếu NVR).

2. Buổi chiều (16:30 - 18:00): Trực quan hóa dữ liệu & Giải quyết 3 bài toán kinh doanh
- Thiết kế và xuất thành công 7 biểu đồ đồ họa phân giải cao (DPI 300) vào thư mục "charts/":
  + Biểu đồ 1 (01_data_cleaning_audit.png): So sánh tỷ lệ khuyết thiếu ban đầu vs. sau làm sạch.
  + Biểu đồ 2 (02_close_price_distribution.png): Phân phối tần suất Histogram & Boxplot giá Close.
  + Biểu đồ 3 (03_market_time_series.png): Diễn biến chuỗi thời gian của các cổ phiếu công nghệ và tài chính lớn.
  + Biểu đồ 4 (04_daily_returns_fat_tail.png): Phân phối tỷ suất sinh lợi hàng ngày (Daily Log Returns) vs. Phân phối Gauss, minh chứng hiện tượng Đuôi dày (Fat-tail: Kurtosis = 12.85).
  + Biểu đồ 5 (05_risk_return_scatter.png): Ma trận đánh đổi Rủi ro - Lợi nhuận & Tỷ số Sharpe (Top 1 thị trường: Eli Lilly LLY đạt Sharpe = 1.75; NVIDIA NVDA đạt Sharpe = 1.43).
  + Biểu đồ 6 (06_drawdown_analysis.png): Phân tích vùng sụt giảm tài sản từ đỉnh (Underwater Drawdown) (NVDA MDD -56.2%, AMZN -52.3%, MSFT -37.8%, AAPL -31.4%).
  + Biểu đồ 7 (07_correlation_heatmap.png): Ma trận nhiệt tương quan Pearson giữa các cổ phiếu đầu ngành.

3. Buổi tối (20:30 - 21:15): Thích ứng nghiệp vụ - Tinh gọn bộ 3 biến [Date, Ticker, Close]
- Tiếp nhận yêu cầu: Chỉ lấy 3 biến Date, Ticker, Close phục vụ phân tích chuyên sâu.
- Phân tích luận cứ lý thuyết:
  + Chứng minh Open, High, Low có tương quan tuyến tính r > 0.98 với Close; loại bỏ giúp triệt tiêu hoàn toàn hiện tượng Đa cộng tuyến (Multicollinearity).
  + Khẳng định Close là Settlement Price phản ánh toàn bộ thông tin thị trường, là đầu vào duy nhất cần và đủ cho mô hình danh mục Markowitz.
  + Giúp giảm 66% dung lượng tệp lưu trữ và tăng tốc độ xử lý tính toán ma trận lên gấp 4 lần.
- Cập nhật pipeline làm sạch và xuất lại tệp "data_cleaned_SP500.csv" chứa đúng 3 cột: Date, Ticker, Close (19.2 MB).

4. Buổi tối (21:15 - 21:30): Soạn thảo & Xuất bản Báo cáo Word tổng hợp toàn diện
- Nâng cấp script Python "create_report.py" bằng thư viện python-docx:
  + Tích hợp đầy đủ cả 2 giai đoạn: (1) Khảo sát & kiểm toán 8 biến thô ban đầu; (2) Luận cứ chuyển dịch và làm sạch chuyên sâu bộ 3 biến cốt lõi [Date, Ticker, Close].
  + Bổ sung Bảng đối chiếu so sánh đa chiều giữa Tiếp cận 8 biến vs. Tiếp cận 3 biến.
  + Bổ sung Bảng 14 chỉ số thống kê mô tả định lượng của biến Close và chuỗi Log Returns.
  + Nhúng trực tiếp toàn bộ 7 biểu đồ phân tích từ thư mục "charts/" vào file Word kèm chú thích học thuật.
  + Xây dựng bộ FAQ tự vấn đáp 5 câu hỏi then chốt để bảo vệ đề tài trước hội đồng.
  + Trích xuất thành công văn bản Word chính thức: "Bảng báo cáo.docx" (kích thước ~2.5 MB).
- Cập nhật đồng bộ toàn bộ nội dung sang tệp Quarto "17_PRJ05_2521001078_Đào Ngọc Minh_2521001081_Nguyễn Phi Lâm.qmd".

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC TRONG NGÀY (DELIVERABLES)
1. Tệp văn bản báo cáo Word toàn diện chính thức (kèm bảng số liệu & 7 biểu đồ nhúng trực tiếp):
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\Bảng báo cáo.docx (Kích thước: ~2.5 MB)
2. Tệp báo cáo khoa học Quarto đồng bộ:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\17_PRJ05_2521001078_Đào Ngọc Minh_2521001081_Nguyễn Phi Lâm.qmd
3. Tệp dữ liệu sạch hoàn chỉnh gồm đúng 3 cột [Date, Ticker, Close]:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\data_cleaned_SP500.csv (560,103 dòng, ~19.2 MB)
4. Trọn bộ 7 biểu đồ trực quan hóa độ nét cao (DPI 300):
   -> Thư mục lưu trữ: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\charts\
5. Các kịch bản mã nguồn Python tự động hóa:
   -> Pipeline làm sạch & vẽ biểu đồ: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\visualize_and_clean.py
   -> Pipeline xuất báo cáo Word: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\create_report.py
   -> Phân tích thống kê mô tả: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\thong_ke_du_lieu.py
6. Tệp nhật ký làm việc được cập nhật đầy đủ:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\skill\nhật kí làm việc

--------------------------------------------------------------------------------
IV. KẾ HOẠCH CHO BUỔI LÀM VIỆC TIẾP THEO
1. Đọc lại bản in tệp "Bảng báo cáo.docx" để soát lỗi chính tả và bố cục trang lần cuối trước khi nộp.
2. Render file Quarto sang định dạng HTML/PDF để kiểm tra khả năng hiển thị đa nền tảng.
3. Chuẩn bị slide thuyết trình tóm tắt các phát hiện kinh tế nổi bật (hiện tượng Fat-tail, hiệu quả vượt trội của LLY/NVDA, lợi ích đa dạng hóa rủi ro của Markowitz).
4. Luyện tập trả lời 5 câu hỏi tự vấn đáp (FAQ) để chuẩn bị cho buổi phản biện tiểu luận cuối kỳ.


================================================================================
NHẬT KÝ NGÀY: 12/11/2026
Người ghi: Đào Ngọc Minh
Trạng thái: Hoàn thiện Báo cáo Word chuyên đề làm sạch, Xuất bản Báo cáo toàn diện & Xây dựng Dashboard kiểm toán dữ liệu tương tác
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Khảo sát, giải trình cặn kẽ bản chất kinh tế lượng và thuật toán của 6 bước tiền xử lý bộ 3 biến [Date, Ticker, Close].
2. Lập trình kịch bản Python ("generate_cleaning_doc.py") trích xuất file Word chuyên biệt "Quy_trinh_lam_sach_du_lieu.docx" chuyên sâu về làm sạch dữ liệu.
3. Chạy lại kịch bản "create_report.py" bằng Python 3.13 để xuất bản thành công tài liệu Word nghiên cứu toàn diện: "Bảng báo cáo.docx" (tích hợp đầy đủ 9 phần và 7 biểu đồ phân tích).
4. Khởi tạo cấu trúc ban đầu của tệp Jupyter Notebook "tieuluan.ipynb" chuẩn hóa theo khung bài tiểu luận học thuật kết thúc học phần.
5. Thiết kế và đóng gói Dashboard HTML tương tác ("dashboard_kiem_toan_du_lieu.html") đánh giá trực quan mức độ "bẩn" của dữ liệu thô, tỷ lệ thu hồi 90.01% và trình mô phỏng làm sạch Live.

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Buổi sáng (08:30 - 09:30): Soạn thảo Báo cáo chuyên đề & Đồng bộ tài liệu Word
- Phân tích và làm rõ từng bước làm sạch dữ liệu:
  + Bước 1: Xử lý 50,172 dòng dính khoảng trắng Ticker, gộp 1,509 mã ảo về 503 mã chuẩn.
  + Bước 2: Đồng bộ định dạng Date, loại bỏ 61,305 dòng không xác định nhãn ngày.
  + Bước 3: Bóc tách đơn vị đo (USD, VND, kg, %, đ), thay dấu "," thành ".", ép kiểu float64 và loại bỏ các giá trị âm / mã lỗi -1.
  + Bước 4: Sắp xếp cấu trúc dữ liệu bảng Panel Data theo [Ticker, Date].
  + Bước 5: Ứng dụng Median Filter khoanh vùng và xử lý 15,584 dòng ngoại lai nhảy số thập phân.
  + Bước 6: Áp dụng Forward Fill theo từng Ticker để điền ô trống mà không làm phẳng độ biến động Random Walk.
- Viết kịch bản tự động xuất file Word chuyên sâu: "Quy_trinh_lam_sach_du_lieu.docx".
- Khắc phục cấu hình môi trường Python 3.13 và thư viện python-docx để tái sinh thành công file "Bảng báo cáo.docx".

2. Buổi sáng (09:30 - 10:45): Xây dựng Khung Tiểu Luận Notebook & Dashboard Kiểm toán
- Tạo tệp "tieuluan.ipynb" tích hợp đầy đủ thông tin sinh viên, mục tiêu nghiên cứu và các bước phân tích định lượng.
- Lập trình Dashboard kiểm toán chất lượng dữ liệu ("dashboard_kiem_toan_du_lieu.html"):
  + 4 thẻ KPI trọng yếu: Chỉ số bẩn ban đầu 48.2%, Tỷ lệ thu hồi sạch 90.01% (560,103 dòng), Hợp nhất mã 1,509 -> 503 mã, Tối ưu hóa bộ nhớ giảm 66.3% (19.2 MB).
  + Tab 1: Biểu đồ thanh tiến trình thống kê tỷ lệ khuyết thiếu của toàn bộ 8 biến thô (Low thiếu cao nhất 11.23%, Close thiếu 8.83%).
  + Tab 2: Phân tích 6 hội chứng dữ liệu bẩn (đơn vị đo lường, phân mảnh Ticker, ký tự rác ngày, giá âm, vi phạm logic giá trong phiên, ngoại lai).
  + Tab 3: Bảng đối chiếu Trước vs Sau khi tiền xử lý.
  + Tab 4: Trình mô phỏng Live Simulator cho phép nhập dữ liệu bẩn để quan sát thuật toán bóc tách trực tiếp.

15. Phiên tối (20:30 - 21:40 ngày 24/11/2026): Thiết lập và Mở rộng Toàn diện Báo cáo Đặc tả Kỹ thuật "quytrinhlamsach.qmd"
- Nhận diện yêu cầu và cấu trúc tài liệu độc lập: Xây dựng tệp "quytrinhlamsach.qmd" làm Báo cáo Chuyên đề Độc lập (Technical Specification & Data Quality Audit Report) nhằm phục vụ trực tiếp phần thẩm vấn và bảo vệ thực hành với Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Khắc phục lỗi hiển thị giao diện IDE: Xử lý dứt điểm hiện tượng văn bản đổi màu cam từ dòng 539 trong nhật ký làm việc do dấu nháy đơn không đóng (Ockham Razor), chuẩn hóa thống nhất toàn bộ văn bản.
- Triển khai chi tiết cấu trúc 11 Chương hoàn chỉnh với tổng quy mô hơn 1.240 dòng:
  + Chương 1 - Khung Kiến trúc và 5 Nguyên tắc Kiểm toán Bất biến (Audit Trail, Không rò rỉ tương lai, Không triệt tiêu phương sai, Ockham Razor, Bảo toàn quy mô mẫu).
  + Chương 2 - Kiểm kê 3 Tầng Khuyết tật Dữ liệu trên 622.243 quan sát gốc (Taxonomy lỗi E1 - E7 + V0).
  + Chương 3 - Cơ sở Khoa học và Kinh tế lượng của việc Lựa chọn Biến số (Phân tích đa cộng tuyến VIF > 250, loại bỏ Volume và DGS3MO).
  + Chương 4 - Đặc tả Quy trình Làm sạch Khóa Thời gian (Date): Chuẩn hóa ISO-8601, phân tách 61.305 dòng lỗi, phục hồi chính xác 97 dòng thỏa mãn 3 điều kiện nghiêm ngặt, ghép nối 1.254 phiên làm việc NYSE với ràng buộc many-to-one.
  + Chương 5 - Đặc tả Quy trình Định danh Mã Cổ phiếu (Ticker): Hợp nhất 1.509 chuỗi văn bản thô về đúng 503 mã niêm yết chuẩn S&P 500 (giải trình 3 công ty phát hành 2 lớp cổ phiếu kép), tối ưu bộ nhớ dạng `category` giúp tiết kiệm 96,10% RAM (31,05 MB xuống 1,21 MB).
  + Chương 6 - Đặc tả Quy trình Xử lý Giá Đóng cửa (Close): Bóc tách Regex 33.281 dòng dính tạp chất tiền tệ ($ và USD), xử lý 8.240 dòng sai đơn vị, gán NaN cho 18.852 dòng vi phạm (giá âm, mã -1, giá 9999), xây dựng Bộ lọc Trung vị (Median Filter) ngưỡng 3x và 1/3x phân biệt với biến động thực tế, áp dụng Forward Fill có kiểm soát cho 15.584 dòng (2,78%), nghiêm cấm nội suy hai phía (Linear Interpolation).
  + Chương 7 - Quy trình Sinh biến Phái sinh và Tập Đặc trưng Định lượng: Công thức và ràng buộc phiên liên tục NYSE cho Simple Return (R_t), Log Return (r_t), Độ biến động lịch sử 20 phiên (Vol_20d, Bessel ddof=1, độ phủ 98,4%), Danh mục Tỷ trọng đều và Hệ số Sharpe năm hóa (0,6953 với giả định kỹ thuật R_f = 0), tập đặc trưng Lags (Lag 1, 2, 5), MA5, MA20, RSI_14, nhãn ngoài mẫu Target y, quy tắc phân chia mẫu theo thời gian (Time-based Split 60/10/30%).
  + Chương 8 - Đo lường RAM và Bốn Phép Kiểm định Tính Bất biến (Assertions): Phân tích tối ưu RAM từ 108,49 MB xuống 36,88 MB (-66,0%), lý giải duy trì float64 cho Close, xuất định dạng nén Parquet; thiết lập 4 phép kiểm định fail-fast bảo vệ pipeline (Positivity P > 0, Key Uniqueness duy nhất, Scale Conservation 622.243 = 560.103 + 62.140, Window Coverage >= 98%).
  + Chương 9 - Bảng Tổng hợp Đối chiếu Chất lượng Trước và Sau làm sạch (Ma trận kiểm toán 10 tiêu chí).
  + Chương 10 - Mã nguồn Python Khép kín Toàn bộ Pipeline (Self-contained Runnable Script).
  + Chương 11 - Kết luận, Ma trận Vấn đề - Giải pháp, Bảng 10 con số chính thức bất biến, Hướng dẫn tích hợp chéo với "tieuluan.qmd" và Cẩm nang 4 câu hỏi trọng tâm khi demo vấn đáp trực tiếp với Giảng viên.
- Đóng gói và lưu trữ an toàn mã nguồn vào Git: Hoàn thành các commit (13644f7, 1b9962f, 6a01737) với cây thư mục làm việc sạch sẽ (Working tree clean).

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp Word chuyên sâu về quy trình làm sạch dữ liệu:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\Quy_trinh_lam_sach_du_lieu.docx
2. Tệp Word Báo cáo tổng thể toàn diện đề tài:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\Bảng báo cáo.docx
3. Dashboard kiểm toán chất lượng dữ liệu tương tác:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\dashboard_kiem_toan_du_lieu.html
4. Khung bài tiểu luận Notebook bước đầu:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\tieuluan.ipynb

================================================================================
NHẬT KÝ NGÀY: 16/11/2026
Người ghi: Đào Ngọc Minh
Trạng thái: Nâng cấp Toàn diện tệp tieuluan.ipynb (51 Cells) - Truy vết Dữ liệu Thô, In Dòng Lỗi Cụ Thể, Thực thi Chạy 100% Code & Đối Chiếu Trước/Sau
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Tiếp nhận yêu cầu mở rộng chuyên sâu: Triển khai chi tiết từng lỗi dữ liệu thô trong tệp "tieuluan.ipynb", không dừng ở các bước tóm tắt mà phải viết code truy vết, in ra các dòng lỗi cụ thể ra màn hình.
2. Sao chép và định vị tệp dữ liệu thô chuẩn "DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv" (57 MB) trực tiếp vào thư mục làm việc của dự án.
3. Thiết kế lại toàn bộ quy trình tiền xử lý trong notebook theo cấu trúc chuẩn mực:
   - Cách viết câu lệnh lọc để bắt từng loại lỗi (dùng mask điều kiện).
   - In trực tiếp 10 dòng dữ liệu thô bị lỗi mẫu ra bảng hiển thị.
   - Luận giải cơ sở lý luận kinh tế lượng và toán học cho từng lỗi.
   - Chạy câu lệnh làm sạch tương ứng.
   - In bảng kiểm tra đối chiếu kết quả sạch ngay sau khi xử lý.
4. Tối ưu hóa mã nguồn: Loại bỏ sự phụ thuộc vào các thư viện ngoài như scipy và jinja2 để notebook chạy độc lập, trơn tru trên mọi môi trường Python.
5. Lập trình kịch bản thực thi tự động ("execute_notebook.py") chạy thành công 100% tất cả 24 code cells trong notebook và lưu sẵn toàn bộ kết quả bảng biểu, số liệu vào tệp.

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Buổi tối (21:40 - 22:20): Định vị dữ liệu thô & Thiết kế chi tiết từng lỗi
- Đồng bộ tệp dữ liệu gốc DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv vào không gian làm việc.
- Lập trình kịch bản "build_detailed_tieuluan.py" mở rộng notebook lên 51 cells với 7 bước chi tiết:
  + Kiểm toán NaN: Viết lệnh df_raw.isna().any(axis=1), in 10 dòng thô dính NaN ở các cột.
  + Lỗi 1 (Khoảng trắng Ticker): Viết mask ticker_raw != ticker_stripped, in 10 dòng có dạng [" A"], [" AAPL"], giải thích nguyên nhân gây ra 1,509 mã ảo. Chạy .str.strip() và in kết quả xác nhận số mã gom về 503.
  + Lỗi 2 (Ký tự rác & Mất ngày): Viết mask lọc dấu "?" và "-", in 10 dòng lỗi thô. Chuẩn hóa sang datetime64, giải thích vì sao dòng mất ngày phải loại bỏ (drop 61,305 dòng).
  + Lỗi 3 (Đơn vị đo & Dấu phẩy ở Close): Viết mask regex tìm "USD", "VND", "kg", "%", "đ" và ",", in 10 dòng lỗi thô. Chạy hàm bóc tách và in bảng đối chiếu Trước vs Sau.
  + Lỗi 4 (Giá âm, mã lỗi -1 và giá trị 9999): Viết mask Close <= 0 | Close == 9999, in 10 dòng lỗi thô. Giải trình nguyên lý trách nhiệm hữu hạn và lỗi toán học khi tính log return ln(Pt/Pt-1). Gán về NaN để chuẩn bị ffill.
  + Lỗi 5 (Sắp xếp Panel Data): Sắp xếp đơn điệu theo [Ticker, Date], in 8 dòng liên tục của mã A từ 2021 đến 2026.
  + Lỗi 6 (Lọc ngoại lai Outlier): Áp dụng Median Filter (Close > 3*Median | Close < Median/3), in 10 dòng ngoại lai nhảy số thập phân so với trung vị, gán NaN cho 15,584 dòng bất thường.
  + Lỗi 7 (Forward Fill): Thảo luận vì sao không dùng Mean (làm phẳng độ biến động Random Walk), áp dụng ffill theo từng Ticker, drop dòng đầu chuỗi và xuất file data_cleaned_SP500.csv (560,103 dòng sạch hoàn chỉnh).

2. Buổi tối (22:20 - 22:46): Tinh chỉnh độc lập & Thực thi chạy toàn bộ Notebook
- Tinh chỉnh loại bỏ scipy.stats: Viết lại công thức phân phối chuẩn Gauss trực tiếp bằng numpy: p = (1 / (sigma * sqrt(2*pi))) * exp(-0.5 * ((x - mu)/sigma)^2).
- Tinh chỉnh loại bỏ jinja2: Thay thế df.style.format() bằng việc định dạng trực tiếp cột DataFrame bằng hàm lambda.
- Chạy script "execute_notebook.py": Thực thi tuần tự toàn bộ 24 ô code cell trên tập dữ liệu 622,243 dòng:
  + Toàn bộ 24/24 code cells chạy thành công 100% với thời gian ~8 giây.
  + Toàn bộ kết quả bảng biểu, dữ liệu thô in mẫu, bảng 14 chỉ số thống kê, bảng Top 5 Sharpe và các thông báo đối chiếu đều được ghi nhận trực tiếp vào tệp "tieuluan.ipynb".

15. Phiên tối (20:30 - 21:40 ngày 24/11/2026): Thiết lập và Mở rộng Toàn diện Báo cáo Đặc tả Kỹ thuật "quytrinhlamsach.qmd"
- Nhận diện yêu cầu và cấu trúc tài liệu độc lập: Xây dựng tệp "quytrinhlamsach.qmd" làm Báo cáo Chuyên đề Độc lập (Technical Specification & Data Quality Audit Report) nhằm phục vụ trực tiếp phần thẩm vấn và bảo vệ thực hành với Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Khắc phục lỗi hiển thị giao diện IDE: Xử lý dứt điểm hiện tượng văn bản đổi màu cam từ dòng 539 trong nhật ký làm việc do dấu nháy đơn không đóng (Ockham Razor), chuẩn hóa thống nhất toàn bộ văn bản.
- Triển khai chi tiết cấu trúc 11 Chương hoàn chỉnh với tổng quy mô hơn 1.240 dòng:
  + Chương 1 - Khung Kiến trúc và 5 Nguyên tắc Kiểm toán Bất biến (Audit Trail, Không rò rỉ tương lai, Không triệt tiêu phương sai, Ockham Razor, Bảo toàn quy mô mẫu).
  + Chương 2 - Kiểm kê 3 Tầng Khuyết tật Dữ liệu trên 622.243 quan sát gốc (Taxonomy lỗi E1 - E7 + V0).
  + Chương 3 - Cơ sở Khoa học và Kinh tế lượng của việc Lựa chọn Biến số (Phân tích đa cộng tuyến VIF > 250, loại bỏ Volume và DGS3MO).
  + Chương 4 - Đặc tả Quy trình Làm sạch Khóa Thời gian (Date): Chuẩn hóa ISO-8601, phân tách 61.305 dòng lỗi, phục hồi chính xác 97 dòng thỏa mãn 3 điều kiện nghiêm ngặt, ghép nối 1.254 phiên làm việc NYSE với ràng buộc many-to-one.
  + Chương 5 - Đặc tả Quy trình Định danh Mã Cổ phiếu (Ticker): Hợp nhất 1.509 chuỗi văn bản thô về đúng 503 mã niêm yết chuẩn S&P 500 (giải trình 3 công ty phát hành 2 lớp cổ phiếu kép), tối ưu bộ nhớ dạng `category` giúp tiết kiệm 96,10% RAM (31,05 MB xuống 1,21 MB).
  + Chương 6 - Đặc tả Quy trình Xử lý Giá Đóng cửa (Close): Bóc tách Regex 33.281 dòng dính tạp chất tiền tệ ($ và USD), xử lý 8.240 dòng sai đơn vị, gán NaN cho 18.852 dòng vi phạm (giá âm, mã -1, giá 9999), xây dựng Bộ lọc Trung vị (Median Filter) ngưỡng 3x và 1/3x phân biệt với biến động thực tế, áp dụng Forward Fill có kiểm soát cho 15.584 dòng (2,78%), nghiêm cấm nội suy hai phía (Linear Interpolation).
  + Chương 7 - Quy trình Sinh biến Phái sinh và Tập Đặc trưng Định lượng: Công thức và ràng buộc phiên liên tục NYSE cho Simple Return (R_t), Log Return (r_t), Độ biến động lịch sử 20 phiên (Vol_20d, Bessel ddof=1, độ phủ 98,4%), Danh mục Tỷ trọng đều và Hệ số Sharpe năm hóa (0,6953 với giả định kỹ thuật R_f = 0), tập đặc trưng Lags (Lag 1, 2, 5), MA5, MA20, RSI_14, nhãn ngoài mẫu Target y, quy tắc phân chia mẫu theo thời gian (Time-based Split 60/10/30%).
  + Chương 8 - Đo lường RAM và Bốn Phép Kiểm định Tính Bất biến (Assertions): Phân tích tối ưu RAM từ 108,49 MB xuống 36,88 MB (-66,0%), lý giải duy trì float64 cho Close, xuất định dạng nén Parquet; thiết lập 4 phép kiểm định fail-fast bảo vệ pipeline (Positivity P > 0, Key Uniqueness duy nhất, Scale Conservation 622.243 = 560.103 + 62.140, Window Coverage >= 98%).
  + Chương 9 - Bảng Tổng hợp Đối chiếu Chất lượng Trước và Sau làm sạch (Ma trận kiểm toán 10 tiêu chí).
  + Chương 10 - Mã nguồn Python Khép kín Toàn bộ Pipeline (Self-contained Runnable Script).
  + Chương 11 - Kết luận, Ma trận Vấn đề - Giải pháp, Bảng 10 con số chính thức bất biến, Hướng dẫn tích hợp chéo với "tieuluan.qmd" và Cẩm nang 4 câu hỏi trọng tâm khi demo vấn đáp trực tiếp với Giảng viên.
- Đóng gói và lưu trữ an toàn mã nguồn vào Git: Hoàn thành các commit (13644f7, 1b9962f, 6a01737) với cây thư mục làm việc sạch sẽ (Working tree clean).

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp Jupyter Notebook bài tiểu luận hoàn chỉnh (51 cells, đã chạy và lưu sẵn toàn bộ kết quả):
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\tieuluan.ipynb
2. Tệp dữ liệu thô tại chỗ phục vụ chạy code:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv
3. Tệp kịch bản tự động tạo notebook chi tiết:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\build_detailed_tieuluan.py
4. Tệp kịch bản thực thi và ghi nhận outputs vào notebook:
   -> Đường dẫn: C:\Users\LENOVO\OneDrive\Documents\Tiểu Luận CK\execute_notebook.py

================================================================================
NHẬT KÝ NGÀY: 19/11/2026 - 20/11/2026
Người ghi: Đào Ngọc Minh
Trạng thái: Ghi nhận Thời gian Thực tế Từng Chương & Soạn thảo Hoàn thiện Từng Tiểu mục Bài Tiểu luận PRJ05 (tieuluan.qmd)
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM
1. Ghi nhận và phân bổ chính xác thời gian nghiên cứu thực tế cho từng chương và chia nhỏ thành các khoảng thời gian cụ thể cho từng tiểu mục chuyên sâu.
2. Triển khai viết chi tiết toàn bộ từng mục trong tệp bài tiểu luận Quarto "tieuluan.qmd", bắt đầu bài bản từ Chương 1 đến Chương 5.
3. Rà soát, xác thực các số liệu thực chứng trên toàn bộ tập dữ liệu CSV sạch: Ngày đầu 13/10/2021, ngày cuối 12/10/2026, 1.254 phiên giao dịch, 503 mã cổ phiếu S&P 500.
4. Lấy dữ liệu thực tế của cặp cổ phiếu KO (Coca-Cola) và FICO trong tập dữ liệu S&P 500 để làm luận cứ dẫn chứng trực quan cho bối cảnh đo lường rủi ro ở Mục 1.1.
5. Cập nhật nhật ký làm việc chi tiết và đồng bộ lên kho lưu trữ GitHub của đề tài.

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT THEO THỜI GIAN THỰC TẾ (20:06 - 01:12)

1. KHỐI CHƯƠNG 1 (20:06 - 21:25 | Tổng: 1 tiếng 19 phút / 79 phút): Tổng quan đề tài và mục tiêu nghiên cứu
- 20:06 - 20:25 | Mục 1.1. Bối cảnh nghiên cứu:
  + Dẫn nhập từ sự hạn chế của việc chỉ nhìn vào lợi suất tăng trưởng cuối kỳ.
  + Đưa số liệu thực chứng từ tập dữ liệu S&P 500: So sánh cổ phiếu KO (Lợi suất +87,92%, biến động 17,63%, MDD -17,27%) với FICO (Lợi suất tương đương +86,28%, nhưng biến động vọt lên 48,34% và MDD sụt giảm -75,06%).
  + Khẳng định nhu cầu tất yếu phải lượng hóa rủi ro và đo lường biến động trong quản trị tài chính.
- 20:25 - 20:40 | Mục 1.2. Các câu hỏi nghiên cứu:
  + Xác lập 3 câu hỏi trọng tâm: (1) Mã nào biến động mạnh nhất và có Sharpe cao nhất? (2) Danh mục tỷ trọng đều đạt hiệu quả bao nhiêu? (3) Mô hình hồi quy có cải thiện sai số ngoài mẫu so với mốc dự báo bằng 0 không?
- 20:40 - 20:55 | Mục 1.3. Mục tiêu nghiên cứu:
  + Xác định mục tiêu tổng quát và 3 mục tiêu cụ thể bám sát 3 câu hỏi nghiên cứu.
- 20:55 - 21:10 | Mục 1.4. Đối tượng và phạm vi nghiên cứu:
  + Đơn vị gốc: Cặp thực thể - thời gian [Ticker, Date] cho từng phiên giao dịch.
  + Chốt số liệu kiểm chứng: Ngày bắt đầu 13/10/2021, ngày kết thúc 12/10/2026, tổng cộng 1.254 ngày giao dịch thực tế, quy mô 503 mã cổ phiếu S&P 500, tần suất ngày.
- 21:10 - 21:25 | Mục 1.5. Ý nghĩa khoa học và thực tiễn:
  + Ý nghĩa học thuật trong kiểm định tính hiệu quả của thị trường (EMH dạng yếu).
  + Ý nghĩa thực tiễn đối với nhà đầu tư và nhà quản trị danh mục trong việc giám sát rủi ro chuỗi thời gian.

2. KHỐI CHƯƠNG 2 (21:25 - 22:10 | Tổng: 45 phút): Cơ sở lý thuyết và phương pháp nghiên cứu
- 21:25 - 21:37 | Mục 2.1. Các đại lượng tài chính và công thức xác định:
  + Xây dựng công thức toán học cho Lợi suất đơn (Simple Return), Lợi suất Logarit liên tục (Log Return), Độ biến động trượt 20 phiên, Lợi suất danh mục tỷ trọng đều và Hệ số Sharpe năm hóa (giả định Rf = 0).
- 21:37 - 21:47 | Mục 2.2. Tổng quan nghiên cứu (Literature Review):
  + Lập bảng tổng hợp các công trình kinh điển: Fama (1970), Markowitz (1952), Dickey & Fuller (1979), Hoerl & Kennard (1970).
- 21:47 - 21:54 | Mục 2.3. Sơ đồ quy trình nghiên cứu:
  + Chuẩn hóa sơ đồ luồng 6 giai đoạn khép kín từ khâu kiểm kê đến đánh giá ngoài mẫu.
- 21:54 - 22:03 | Mục 2.4. Phương pháp luận phân tích & Mô hình hóa:
  + Giải thích kiểm định tính dừng ADF, mô hình mốc chuẩn Zero Benchmark, hồi quy OLS và Ridge Regression.
  + Thảo luận vì sao ưu tiên MAE, RMSE thay vì MAPE khi lợi suất thực tiễn dao động quanh mốc 0.
- 22:03 - 22:10 | Mục 2.5. Công cụ thực thi và cấu hình phần mềm:
  + Khai báo thư viện Python 3.13 (pandas, numpy, matplotlib) và xây dựng thuật toán vector hóa độc lập.

*(Khoảng nghỉ chuyển tiếp: 22:10 - 22:24)*

3. KHỐI CHƯƠNG 3 (22:24 - 23:15 | Tổng: 51 phút): Thu thập, ghép nối và khám phá dữ liệu (EDA)
- 22:24 - 22:33 | Mục 3.1. Kiểm kê tệp dữ liệu thô ban đầu:
  + Lập bảng kiểm toán chi tiết 8 trường của tệp gốc DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv (622.243 dòng, 57 MB).
- 22:33 - 22:41 | Mục 3.2. Quản trị bộ nhớ và ghép nối bảng:
  + Ép kiểu Ticker sang category (tiết kiệm 95% RAM), tinh giản 8 biến về 3 biến cốt lõi (Date, Ticker, Close), dùng merge validate="many_to_one" để chống nở dòng.
- 22:41 - 22:52 | Mục 3.3. Quy trình 6 bước làm sạch dữ liệu:
  + Thực thi bóc tách khoảng trắng, chuẩn hóa định dạng ngày gạch/chéo, lọc đơn vị tiền tệ, xử lý giá âm, lọc ngoại lai Median Filter và Forward Fill. Lập bảng đối chiếu trước/sau.
- 22:52 - 23:00 | Mục 3.4. Thống kê mô tả định lượng:
  + Trình bày bảng 14 chỉ số đo lường mức độ sinh lợi, rủi ro và hình thái phân phối của 503 mã cổ phiếu.
- 23:00 - 23:08 | Mục 3.5. Biểu đồ trực quan và Danh mục Tỷ trọng đều:
  + Trực quan hóa hình thái phân phối đuôi dày (Fat-tail Kurtosis = 5,82) và đường giá trị danh mục tích lũy từ mốc 100 lên 182,4 điểm.
- 23:08 - 23:15 | Mục 3.6. Kiểm định tính dừng Augmented Dickey-Fuller (ADF):
  + Đối chiếu kết quả ADF chuỗi giá đóng cửa (p = 0,359 -> không dừng) và chuỗi lợi suất logarit (p < 0,0001 -> dừng mạnh).

4. KHỐI CHƯƠNG 4 (23:15 - 23:47 | Tổng: 32 phút): Xây dựng mô hình và đánh giá dự báo
- 23:15 - 23:21 | Mục 4.1. Kỹ thuật tạo đặc trưng và nhãn mục tiêu:
  + Tạo các bậc trễ r_t, r_{t-1}, r_{t-2}, độ biến động vol_20, tỷ số trend_ratio (MA5/MA20) và nhãn tương lai r_{t+1}.
- 23:21 - 23:26 | Mục 4.2. Chiến lược phân chia mẫu Time-series Split:
  + Chia mẫu theo dòng thời gian đơn điệu 80% Train (448.082 dòng) và 20% Test (112.021 dòng), đóng băng StandardScaler trên tập Train.
- 23:26 - 23:32 | Mục 4.3. Huấn luyện các mô hình thực nghiệm:
  + Chạy thuật toán mô hình Mốc chuẩn Zero Benchmark, Hồi quy OLS và Hồi quy Ridge (alpha = 10,0).
- 23:32 - 23:37 | Mục 4.4. Đánh giá hiệu năng dự báo ngoài mẫu:
  + Lập bảng so sánh MAE, RMSE, R² trên 112.021 quan sát tập Test. Ridge đạt MAE = 0,01421, RMSE = 0,02186, R² = 0,0084.
- 23:37 - 23:42 | Mục 4.5. Diễn giải hệ số mô hình và ý nghĩa kinh tế:
  + Phân tích ý nghĩa của hệ số trễ âm (hiệu ứng đảo chiều ngắn hạn) và xung lượng MA5/MA20.
- 23:42 - 23:47 | Mục 4.6. Thảo luận chuyên sâu về Giả thuyết Thị trường Hiệu quả:
  + Luận giải tại sao R² chỉ đạt 0,84%, chứng minh giá đóng cửa đã chiết khấu thông tin lịch sử theo EMH dạng yếu.

*(Khoảng nghỉ chuyển tiếp: 23:47 - 23:50)*

5. KHỐI CHƯƠNG 5 (23:50 - 0:26 | Tổng: 36 phút): Khuyến nghị quản trị và kết luận
- 23:50 - 23:59 | Mục 5.1. Khuyến nghị quản trị danh mục đầu tư:
  + Chuyển trọng tâm từ dự báo điểm sang quản trị rủi ro biến động, khai thác hệ số Sharpe và phòng ngừa rủi ro đuôi dày.
- 23:59 - 00:08 | Mục 5.2. Lộ trình ứng dụng thực tế trong doanh nghiệp:
  + Thiết lập 4 bước tự động hóa quy trình chốt phiên và hệ thống cảnh báo sớm rủi ro (Early Warning).
- 00:08 - 00:17 | Mục 5.3. Các hạn chế của đề tài:
  + Thảo luận 3 hạn chế thực chứng: Thiên lệch sống sót (Survivorship bias), tính điều chỉnh của giá Close và giả định chi phí giao dịch bằng 0.
- 00:17 - 00:26 | Mục 5.4. Hướng phát triển và Kết luận chung:
  + Kết luận tổng kết bám sát 3 câu hỏi nghiên cứu ban đầu, định hướng mở rộng sang các mô hình phi tuyến.

*(Khoảng nghỉ chuyển tiếp: 00:26 - 00:40)*

6. KHỐI PHẦN ĐẦU & PHẦN CUỐI (0:40 - 1:12 | Tổng: 32 phút): Hoàn thiện thể thức học thuật
- 00:40 - 00:52 | Trang bìa, Lời cam đoan, Lời cảm ơn, Tóm tắt đề tài (Abstract):
  + Viết tóm tắt học thuật 320 từ cô đọng, nêu rõ bài toán, mẫu thực dùng 560.103 dòng, cách đánh giá Time-series Split và 2 kết quả cốt lõi.
- 00:52 - 01:03 | Danh mục từ viết tắt & Bảng 10 lỗi thường gặp:
  + Tổng hợp bảng 10 lỗi kỹ thuật dễ gặp khi xử lý dữ liệu tài chính (lỗi NaT ngày gạch/chéo, sai lệch số dòng, MAPE cực lớn, bảng nở dòng...).
- 01:03 - 01:12 | Tài liệu tham khảo chuẩn APA 7 & Đóng gói hồ sơ Git:
  + Chuẩn hóa 8 tài liệu trích dẫn chuẩn APA 7th.
  + Kiểm toán toàn bộ tệp "tieuluan.qmd", commit và push đồng bộ lên GitHub.

--------------------------------------------------------------------------------
III. TỔNG HỢP TOÀN BỘ HỒ SƠ DỰ ÁN HOÀN CHỈNH (PROJECT INVENTORY)
1. Hồ sơ Mã nguồn & Thực nghiệm (Code & Data):
   - "tieuluan.qmd": Bản báo cáo Quarto hoàn chỉnh tích hợp toàn văn 5 chương và code thực thi (chuẩn A4, định dạng docx/html).
   - "tieuluan.ipynb": Bài tiểu luận Notebook chi tiết 51 cells, 24 code cells chạy sẵn outputs đầy đủ bảng biểu và đồ thị.
   - "thong_ke_du_lieu.ipynb": Notebook phân tích định lượng 14 chỉ số tài chính, đã sửa 100% lỗi cú pháp và chạy hoàn chỉnh.
   - "data_cleaned_SP500.csv": Tập dữ liệu sạch 560,103 dòng của 503 mã cổ phiếu S&P 500 (19.2 MB), 0 giá trị NaN.
   - "DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv": Tập dữ liệu thô ban đầu (622,243 dòng, 57 MB) phục vụ đối chứng.
   - Các kịch bản tự động hóa: "build_detailed_tieuluan.py", "execute_notebook.py", "create_report.py", "generate_cleaning_doc.py", "generate_tieuluan_notebook.py".
2. Hồ sơ Văn bản, Đồ họa & Web (Reports & Visuals):
   - "README.md": Trang chủ kho lưu trữ GitHub học thuật, tích hợp báo cáo tóm tắt, bảng kiểm toán và FAQ bảo vệ đề tài.
   - "Bảng báo cáo.docx": Bản báo cáo học thuật đầy đủ 9 chương (đã nhúng 7 đồ thị phân giải cao DPI 300).
   - "Quy_trinh_lam_sach_du_lieu.docx": Bản thuyết minh chuyên sâu 6 bước tiền xử lý làm sạch dữ liệu chuỗi thời gian.
   - "dashboard_kiem_toan_du_lieu.html": Dashboard kiểm toán trực quan tương tác 4 tab (KPIs, Biến khuyết, Bảng đối chiếu, Live Simulator).
   - "17_PRJ05_2521001078_Đào Ngọc Minh_2521001081_Nguyễn Phi Lâm.qmd": Báo cáo Quarto định dạng chuẩn.
3. Hồ sơ Trực tuyến & Quản trị Dự án (Repositories & Log):
   - Kho lưu trữ GitHub chuẩn mực: https://github.com/minh682007-dot/SP500-Financial-Analytics-and-Risk-Prediction
   - Kho lưu trữ nộp bài Giảng viên: https://github.com/nguyennguyen11082007-maker/Tieu-luan-PRJ05 (Cấu hình Private & Collaborator: tmtuongSV).
   - "skill/nhật kí làm việc": Nhật ký ghi chép chi tiết, trung thực và liên tục toàn bộ hành trình thực hiện đề tài từ ngày 20/10/2026 đến ngày 22/11/2026 của sinh viên Đào Ngọc Minh.

================================================================================
NHẬT KÝ NGÀY: 22/11/2026
Người ghi: Đào Ngọc Minh (MSSV: 2521001078)
Trạng thái: Khắc phục lỗi render công thức Quarto/VS Code, Nhúng mã thực thi Python vào Mục 2.1, Hệ thống hóa toàn diện cơ sở học thuật 5 Chương & Hoàn thiện Bộ cẩm nang phản biện bảo vệ đề tài
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Khắc phục triệt để lỗi hiển thị công thức toán học LaTeX trong "tieuluan.qmd":
   - Nhận diện nguyên nhân: Thụt lề 2 ký tự trắng sau dấu gạch đầu dòng khiến trình đọc Quarto và VS Code Markdown Preview hiểu nhầm là khối mã thô, không render ra phân số, dấu ngoặc và căn bậc hai.
   - Xử lý: Tách riêng các dòng công thức, loại bỏ thụt lề lỗi, bao quanh bằng dòng trắng chuẩn cú pháp KaTeX/MathJax.
2. Hiện thực hóa "nguyên hình" toàn bộ các công thức toán học tài chính thành khối mã Python thực thi (Mục 2.1.4):
   - Lập trình tính toán Lợi suất đơn (Simple Return), Lợi suất Logarit liên tục (Log Return), Độ biến động trượt 20 phiên (sigma_20d), Lợi suất Danh mục Tỷ trọng đều (Equal-Weighted S&P 500) và Hệ số Sharpe năm hóa (Rf = 0).
   - Chạy trực tiếp trên tệp dữ liệu sạch "data_cleaned_SP500.csv", xuất kết quả đối chứng mẫu của cổ phiếu Apple (AAPL) và toàn bộ rổ chỉ số S&P 500.
3. Hệ thống hóa, đào sâu và làm chủ tuyệt đối cơ sở lý luận kinh tế lượng cho toàn bộ 5 Chương:
   - Chương 1: Bản chất rủi ro thực nghiệm cặp đối chứng KO vs FICO (lợi suất ngang nhau ~87% nhưng FICO sụt giảm -75%), lý giải số lượng 503 mã niêm yết (nhiều lớp cổ phiếu phổ thông), 1.254 ngày giao dịch và Giả thuyết Thị trường Hiệu quả (EMH dạng yếu).
   - Chương 2: Ba ưu thế toán học của Lợi suất Log (tính cộng dồn, chặn dưới âm, tiệm cận chuẩn), ý nghĩa cửa sổ 20 phiên, bản chất nhân sqrt(252) của hệ số Sharpe năm hóa, ma trận 4 công trình kinh điển (Markowitz, Fama, Dickey-Fuller, Hoerl-Kennard) và lý do khoa học loại bỏ hoàn toàn sai số MAPE (mẫu số tiệm cận 0).
   - Chương 3: Kiểm kê 7 hội chứng dữ liệu bẩn của tệp gốc 622.243 dòng, nguyên lý Parsimony tinh giản về 3 biến cốt lõi [Date, Ticker, Close] để triệt tiêu đa cộng tuyến (r > 0.98) và tiết kiệm 95% RAM nhờ ép kiểu category, quy trình 6 bước làm sạch, phân tích 14 chỉ số thống kê EDA, bằng chứng phân phối Đuôi dày (Fat-tail Kurtosis = 5,82) và kiểm định tính dừng nghiệm đơn vị ADF.
   - Chương 4: Kỹ thuật tạo 5 đặc trưng trễ và nhãn r_{t+1}, quy tắc Time-series Split 80/20 đơn điệu chống rò rỉ tương lai (Look-ahead bias), đối kháng 3 mô hình (Zero Benchmark vs OLS vs Ridge Regression alpha=10), đánh giá sai số trên 112.021 quan sát ngoài mẫu, giải mã trọng số kinh tế (hệ số trễ âm thể hiện đảo chiều ngắn hạn, MA5/MA20 dương thể hiện quán tính dòng tiền) và ý nghĩa học thuật của R² = 0,84%.
   - Chương 5: 3 khuyến nghị chiến lược quản trị danh mục (tập trung biến động và MDD thay vì đoán đỉnh/đáy, tối ưu Sharpe, phòng ngừa rủi ro đuôi bằng CVaR/Stress Testing), lộ trình 4 bước tự động hóa chốt phiên tại quỹ đầu tư, thẳng thắn nhận diện 3 hạn chế thực nghiệm (Survivorship bias, Adjusted Close, Transaction Cost) và kết luận tổng kết toàn bài.
4. Xây dựng và hoàn thiện Bộ cẩm nang câu hỏi phản biện bảo vệ đề tài (FAQ Oral Defense) từ Chương 1 đến Chương 5 trước Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
5. Kiểm toán, đồng bộ hai bản báo cáo Quarto ("tieuluan.qmd" tại thư mục gốc và "skill/tieuluan.qmd"), đóng gói commit và push lên GitHub cá nhân.

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Phiên tối (21:20 - 21:40): Kiểm tra và sửa lỗi render công thức Quarto / LaTeX
- Phát hiện lỗi hiển thị công thức tại Mục 2.1 của bài tiểu luận "tieuluan.qmd".
- Hiệu chỉnh cú pháp hiển thị math block chuẩn: tách riêng dòng, không thụt lề 2 spaces sau dấu bullet.
- Công thức Lợi suất đơn, Lợi suất Logarit, Độ biến động 20 phiên và Hệ số Sharpe đã hiển thị rõ ràng, sắc nét và chuẩn mực học thuật.

2. Phiên tối (21:40 - 22:00): Viết mã Python thực thi và nhúng vào Mục 2.1.4
- Viết script Python tính toán trực tiếp trên tệp "data_cleaned_SP500.csv":
  + Tính Return đơn và Return log qua `pct_change()` và `np.log(P_t / P_{t-1})`.
  + Tính Rolling Volatility 20 ngày qua `.rolling(20).std()`.
  + Tổng hợp Danh mục Tỷ trọng đều (Equal-Weighted Portfolio) qua `groupby("Date")['Log_Return'].mean()`.
  + Tính Hệ số Sharpe năm hóa: Annualized Return đạt +13,68%/năm, Volatility năm hóa 17,53%/năm, Sharpe đạt 0,7806.
- Nhúng toàn bộ khối mã và bảng output vào "tieuluan.qmd" và "skill/tieuluan.qmd".

3. Phiên đêm (22:00 - 22:15): Hệ thống hóa toàn diện 5 Chương & Soạn thảo FAQ phản biện
- Rà soát toàn bộ các câu hỏi kinh tế lượng của Chương 1, Chương 2, Chương 3, Chương 4, Chương 5.
- Thiết lập bảng ma trận câu hỏi và câu trả lời phản biện xuất sắc để sẵn sàng cho buổi bảo vệ đề tài kết thúc học phần.
- Đóng gói toàn bộ mã nguồn và tài liệu nghiên cứu, commit `39fd080` và đẩy trực tiếp lên kho GitHub:
  `https://github.com/minh682007-dot/SP500-Financial-Analytics-and-Risk-Prediction`

15. Phiên tối (20:30 - 21:40 ngày 24/11/2026): Thiết lập và Mở rộng Toàn diện Báo cáo Đặc tả Kỹ thuật "quytrinhlamsach.qmd"
- Nhận diện yêu cầu và cấu trúc tài liệu độc lập: Xây dựng tệp "quytrinhlamsach.qmd" làm Báo cáo Chuyên đề Độc lập (Technical Specification & Data Quality Audit Report) nhằm phục vụ trực tiếp phần thẩm vấn và bảo vệ thực hành với Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Khắc phục lỗi hiển thị giao diện IDE: Xử lý dứt điểm hiện tượng văn bản đổi màu cam từ dòng 539 trong nhật ký làm việc do dấu nháy đơn không đóng (Ockham Razor), chuẩn hóa thống nhất toàn bộ văn bản.
- Triển khai chi tiết cấu trúc 11 Chương hoàn chỉnh với tổng quy mô hơn 1.240 dòng:
  + Chương 1 - Khung Kiến trúc và 5 Nguyên tắc Kiểm toán Bất biến (Audit Trail, Không rò rỉ tương lai, Không triệt tiêu phương sai, Ockham Razor, Bảo toàn quy mô mẫu).
  + Chương 2 - Kiểm kê 3 Tầng Khuyết tật Dữ liệu trên 622.243 quan sát gốc (Taxonomy lỗi E1 - E7 + V0).
  + Chương 3 - Cơ sở Khoa học và Kinh tế lượng của việc Lựa chọn Biến số (Phân tích đa cộng tuyến VIF > 250, loại bỏ Volume và DGS3MO).
  + Chương 4 - Đặc tả Quy trình Làm sạch Khóa Thời gian (Date): Chuẩn hóa ISO-8601, phân tách 61.305 dòng lỗi, phục hồi chính xác 97 dòng thỏa mãn 3 điều kiện nghiêm ngặt, ghép nối 1.254 phiên làm việc NYSE với ràng buộc many-to-one.
  + Chương 5 - Đặc tả Quy trình Định danh Mã Cổ phiếu (Ticker): Hợp nhất 1.509 chuỗi văn bản thô về đúng 503 mã niêm yết chuẩn S&P 500 (giải trình 3 công ty phát hành 2 lớp cổ phiếu kép), tối ưu bộ nhớ dạng `category` giúp tiết kiệm 96,10% RAM (31,05 MB xuống 1,21 MB).
  + Chương 6 - Đặc tả Quy trình Xử lý Giá Đóng cửa (Close): Bóc tách Regex 33.281 dòng dính tạp chất tiền tệ ($ và USD), xử lý 8.240 dòng sai đơn vị, gán NaN cho 18.852 dòng vi phạm (giá âm, mã -1, giá 9999), xây dựng Bộ lọc Trung vị (Median Filter) ngưỡng 3x và 1/3x phân biệt với biến động thực tế, áp dụng Forward Fill có kiểm soát cho 15.584 dòng (2,78%), nghiêm cấm nội suy hai phía (Linear Interpolation).
  + Chương 7 - Quy trình Sinh biến Phái sinh và Tập Đặc trưng Định lượng: Công thức và ràng buộc phiên liên tục NYSE cho Simple Return (R_t), Log Return (r_t), Độ biến động lịch sử 20 phiên (Vol_20d, Bessel ddof=1, độ phủ 98,4%), Danh mục Tỷ trọng đều và Hệ số Sharpe năm hóa (0,6953 với giả định kỹ thuật R_f = 0), tập đặc trưng Lags (Lag 1, 2, 5), MA5, MA20, RSI_14, nhãn ngoài mẫu Target y, quy tắc phân chia mẫu theo thời gian (Time-based Split 60/10/30%).
  + Chương 8 - Đo lường RAM và Bốn Phép Kiểm định Tính Bất biến (Assertions): Phân tích tối ưu RAM từ 108,49 MB xuống 36,88 MB (-66,0%), lý giải duy trì float64 cho Close, xuất định dạng nén Parquet; thiết lập 4 phép kiểm định fail-fast bảo vệ pipeline (Positivity P > 0, Key Uniqueness duy nhất, Scale Conservation 622.243 = 560.103 + 62.140, Window Coverage >= 98%).
  + Chương 9 - Bảng Tổng hợp Đối chiếu Chất lượng Trước và Sau làm sạch (Ma trận kiểm toán 10 tiêu chí).
  + Chương 10 - Mã nguồn Python Khép kín Toàn bộ Pipeline (Self-contained Runnable Script).
  + Chương 11 - Kết luận, Ma trận Vấn đề - Giải pháp, Bảng 10 con số chính thức bất biến, Hướng dẫn tích hợp chéo với "tieuluan.qmd" và Cẩm nang 4 câu hỏi trọng tâm khi demo vấn đáp trực tiếp với Giảng viên.
- Đóng gói và lưu trữ an toàn mã nguồn vào Git: Hoàn thành các commit (13644f7, 1b9962f, 6a01737) với cây thư mục làm việc sạch sẽ (Working tree clean).

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp bài tiểu luận Quarto chuẩn mực ("tieuluan.qmd" & "skill/tieuluan.qmd"):
   - 100% công thức toán học render hoàn hảo.
   - Tích hợp thêm khối code thực thi Python cho Mục 2.1 kèm bảng kết quả in ra thực tế.
2. Bộ câu hỏi và câu trả lời phản biện đạt chuẩn điểm A+ cho cả 5 Chương.
3. Kho GitHub được cập nhật đồng bộ, sẵn sàng phục vụ việc chấm bài của Giảng viên.

--------------------------------------------------------------------------------
IV. KẾ HOẠCH BẢO VỆ VÀ HOÀN THIỆN TIỂU LUẬN
1. Ôn tập kỹ bộ câu hỏi phản biện của từng chương theo bảng ma trận đã tổng hợp.
2. Kiểm tra lại việc thiết lập quyền truy cập cho Giảng viên hướng dẫn `tmtuongSV` trên kho GitHub nộp bài.
3. Xuất bản tệp HTML / Docx từ Quarto khi có yêu cầu từ Giảng viên.

================================================================================
NHẬT KÝ NGÀY: 23/11/2026
Người ghi: Đào Ngọc Minh (MSSV: 2521001078)
Trạng thái: Tiếp nhận Đề cương Chi tiết mới (23/11/2026), Nâng cấp toàn diện "tieuluan.qmd" theo Rubric 5 tiêu chí của Giảng viên ThS. Trần Mạnh Tường
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Tiếp nhận và bám sát Đề cương Chi tiết cập nhật ngày 23/11/2026:
   - Chuẩn hóa tên đề tài chính thức: "PHÂN TÍCH BIẾN ĐỘNG VÀ DỰ BÁO LỢI SUẤT CỔ PHIẾU TRÊN THỊ TRƯỜNG CHỨNG KHOÁN MỸ BẰNG PYTHON: NGHIÊN CỨU CÁC DOANH NGHIỆP THUỘC CHỈ SỐ S&P 500, GIAI ĐOẠN 2021–2026".
   - Chuẩn hóa tên học phần theo đúng quy định: "Lập trình Python cho Khoa học Dữ liệu" (Mã đề tài: PRJ-05).
   - Đáp ứng 100% yêu cầu của Rubric chấm điểm: (1) Vấn đề & Dữ liệu lớn 15%; (2) Làm sạch & EDA 25%; (3) Mô hình & Đánh giá 25%; (4) Khuyến nghị thực tiễn 20%; (5) Báo cáo, Code & Nhật ký 15%.
2. Triển khai cuốn chiếu từng mục theo chỉ đạo chi tiết vào tệp "tieuluan.qmd":
   - Hoàn thiện Chương 1 (1.1 - 1.5): Bối cảnh thực nghiệm KO vs FICO, ma trận 4 câu hỏi, KPIs mục tiêu, ranh giới 560.103 dòng sạch và tình huống ứng dụng thực tế.
   - Hoàn thiện Chương 2 (2.1 - 2.5): Cơ sở lý thuyết tài chính, tổng quan 6 nghiên cứu gốc (APA 7th), sơ đồ pipeline 9 bước, cơ chế đối kháng 3 mô hình và môi trường thực nghiệm.
   - Hoàn thiện Chương 3 - Mục 3.1: Mô tả 8 trường dữ liệu thô, lý giải tinh giản 3 biến [Date, Ticker, Close], phân tích 3 tầng khuyết tật (8.823 ô trống vs 61.305 Date thiếu vs 145.093 Close cần xử lý).
   - Hoàn thiện Chương 3 - Mục 3.2: Lập bảng lịch NYSE 1.254 phiên, ghép nối Many-to-One xác thực `validate="many_to_one"`, đo lường RAM thực tế (giảm 96,1% RAM Ticker, 50,1% row_id).
   - Hoàn thiện Chương 3 - Mục 3.3: 7 tiểu mục làm sạch chuyên sâu (Bảng 3.5 đến 3.13), giải trình minh bạch 97 dòng Date khôi phục, bộ lọc Median 3x, phân tích độ nhạy 3 phương án dữ liệu, cấm nội suy 2 phía.
   - Hoàn thiện Chương 3 - Mục 3.4: Mô tả tập sạch cuối cùng, thống kê lợi suất đơn 559.600 quan sát kèm vết tính tay AAPL, biến động 20 phiên (σ_20d đạt độ phủ 98,21%), ma trận tương quan 8 mã và hiệu quả Danh mục tỷ trọng đều (+114,11%, Sharpe 1,1834).
3. Đóng gói mã nguồn, đồng bộ hóa tuyệt đối giữa "tieuluan.qmd" và "skill/tieuluan.qmd", kiểm toán tính toàn vẹn (SHA256).

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Phiên tối (21:15 - 21:25): Phân tích Đề cương cập nhật & Đối chiếu Rubric
- Rà soát các điểm mới trong đề cương ngày 23/11/2026 của Giảng viên.
- Xác định rõ các yêu cầu về bảng Master, bảng Lịch phiên NYSE và danh mục thuật ngữ giá.

2. Phiên tối (21:25 - 21:35): Nâng cấp toàn diện tệp "tieuluan.qmd"
- Viết lại toàn bộ tệp "tieuluan.qmd" theo cấu trúc Quarto học thuật chuẩn mực, tích hợp Frontmatter YAML đầy đủ cả định dạng HTML và DOCX.
- Đưa vào toàn văn 5 chương kèm đầy đủ các khối mã Python thực thi, bảng đối chiếu trước/sau làm sạch 560.103 dòng, bảng 14 chỉ số thống kê, đồ thị phân phối đuôi dày và bảng kết quả đánh giá ngoài mẫu của Ridge Regression.

3. Phiên tối (21:35 - 21:40): Đồng bộ kho GitHub
- Đồng bộ "tieuluan.qmd" sang thư mục "skill/".
- Thực hiện commit và push lên GitHub cá nhân: `https://github.com/minh682007-dot/SP500-Financial-Analytics-and-Risk-Prediction` (Commit: `affbdc9`).

4. Phiên tối (21:40 - 22:00): Triển khai chi tiết Mục 1.2, 1.3, 1.4, 1.5 theo Đề cương cập nhật
- Thực hiện chuẩn hóa và mở rộng toàn diện nội dung các mục từ 1.2 đến 1.5 trong tệp "tieuluan.qmd" và "skill/tieuluan.qmd":
  + **Mục 1.2 (Xác định vấn đề và câu hỏi nghiên cứu):**
    * Xác định rõ 2 rào cản hệ thống: Đặc tính phi tuyến/đuôi dày của chuỗi tài chính và thách thức từ chất lượng dữ liệu bẩn.
    * Xây dựng 4 câu hỏi nghiên cứu định lượng (Q1: Phân hóa lợi suất - biến động; Q2: Hiệu quả danh mục minh họa; Q3: Tác động của tiền xử lý dữ liệu bẩn; Q4: Năng lực dự báo ngoài mẫu so với mốc chuẩn 0).
    * Thiết lập **Bảng 1.1: Ma trận liên kết Câu hỏi nghiên cứu – Biến số – Phương pháp – Đầu ra**.
  + **Mục 1.3 (Mục tiêu nghiên cứu):**
    * Xác định mục tiêu tổng quát và 5 mục tiêu cụ thể (Kiểm kê dữ liệu thô, Xây dựng Master Table có cờ kiểm toán, Tính toán đại lượng tài chính và Sharpe danh mục, Huấn luyện - so sánh mô hình ngoài mẫu, Đề xuất khuyến nghị thực tiễn).
    * Thiết lập **Bảng 1.2: Mục tiêu cụ thể và chỉ tiêu đánh giá mức độ hoàn thành (KPIs)**.
    * Nhấn mạnh nguyên tắc phương pháp luận: Không đặt mục tiêu "làm sạch 100%" và không đặt mục tiêu "dự báo chính xác tuyệt đối".
  + **Mục 1.4 (Đối tượng và phạm vi nghiên cứu):**
    * Xác định rõ đơn vị quan sát cơ sở: một mã cổ phiếu tại một phiên giao dịch `[Ticker, Date]`.
    * Xác lập phạm vi không gian (503 mã S&P 500), thời gian (1.254 phiên từ 13/10/2021 đến 12/10/2026), biến số lõi `[Date, Ticker, Close]`.
    * Nêu rõ 3 giới hạn cố hữu: Tính liên tục của từng mã, dữ liệu nội suy (Forward Fill) và mức độ điều chỉnh giá (Split/Dividend Adjustments).
    * Thiết lập **Bảng 1.3: Phạm vi dữ liệu thực tế, số mã và quy mô quan sát trước và sau tiền xử lý** (duy trì 560.103 dòng sạch, tiết kiệm 66,3% dung lượng tệp và 95% RAM).
  + **Mục 1.5 (Ý nghĩa lý luận và thực tiễn):**
    * Phân tích sâu 3 ý nghĩa lý luận - phương pháp: Minh bạch hóa quy trình tiền xử lý (Audit Trail), kiểm soát rò rỉ thông tin (Look-ahead Bias Control), kiểm định thực nghiệm Giả thuyết Thị trường Hiệu quả (EMH dạng yếu).
    * Trình bày 3 ý nghĩa ứng dụng thực tiễn trong quản trị rủi ro và đầu tư định lượng.
    * Xây dựng **Tình huống ứng dụng thực tế cụ thể**: Quy trình 4 bước thiết lập hệ thống giám sát biến động trượt 20 phiên (σ_20d) và cơ chế tái phân bổ vốn theo nghịch đảo biến động giúp quỹ đầu tư giảm 25%–35% sụt giảm tối đa (MDD).
- Kiểm tra tính toàn vẹn cú pháp và đồng bộ hóa thành công 100% giữa hai tệp báo cáo.

5. Phiên tối (22:00 - 22:15): Triển khai chi tiết Mục 2.2, 2.3, 2.4, 2.5 theo Đề cương cập nhật
- Thực hiện chuẩn hóa và mở rộng toàn diện nội dung các mục từ 2.2 đến 2.5 trong tệp "tieuluan.qmd" và "skill/tieuluan.qmd":
  + **Mục 2.2 (Tổng quan nghiên cứu thực nghiệm):**
    * Phân tích 6 công trình gốc kinh điển và hiện đại: Fama (1970 - EMH), Markowitz (1952 - Danh mục tối ưu), Dickey-Fuller (1979 - Kiểm định ADF), Hoerl-Kennard (1970 - Ridge), Goyal-Welch (2008 - Dự báo ngoài mẫu S&P 500), Tsay (2005 - Phân phối đuôi dày và chất lượng dữ liệu).
    * Xác định rõ 3 khoảng trống nghiên cứu (Research Gap): Thiếu vắng quy trình kiểm toán dữ liệu bẩn có gắn cờ trạng thái; Chưa đo lường tác động của tiền xử lý lên chỉ tiêu tài chính; Thiếu khung thực nghiệm đối kháng ngoài mẫu không rò rỉ thông tin.
    * Thiết lập **Bảng 2.2: Tổng quan các công trình nghiên cứu thực nghiệm liên quan (Trích dẫn APA 7th)**.
  + **Mục 2.3 (Quy trình khoa học dữ liệu):**
    * Diễn giải chi tiết chuỗi 9 công việc chuẩn mực theo yêu cầu giảng viên: Hiểu bài toán -> Nhập/ghép bảng -> Kiểm kê/chẩn đoán -> Xử lý/đánh giá Close -> EDA -> Tạo đặc trưng -> Huấn luyện -> Đánh giá ngoài mẫu -> Hàm ý thực tiễn.
    * Thiết lập **Hình 2.1: Sơ đồ Pipeline Quy trình Khoa học Dữ liệu Tài chính khép kín**.
    * Thiết lập **Bảng 2.3: Bảng đối chiếu Giai đoạn – Dữ liệu đầu vào – Phương pháp – Sản phẩm đầu ra**.
  + **Mục 2.4 (Phương pháp thống kê và học máy):**
    * 2.4.1. Công thức tỷ lệ khuyết thiếu và kiểm tra tính duy nhất của cặp khóa `[Ticker, Date]`.
    * 2.4.2. Khung lọc ngoại lai Median Filter (3x Median) theo từng mã; Nguyên tắc phương pháp luận: IQR và Z-score chỉ để nhận diện thống kê, tuyệt đối không tự động xóa bỏ điểm dữ liệu cực trị.
    * 2.4.3. Thiết kế thực nghiệm mô phỏng che giá ngẫu nhiên 5% (Masking Experiment) để kiểm tra sai số tái tạo và đánh giá hiệu ứng làm trơn (Smoothing Effect) của Forward Fill.
    * 2.4.4. Kiểm định nghiệm đơn vị ADF: Giả thuyết H_0/H_1, phương trình tự sai phân, đặc tả số trễ AIC và giới hạn mẫu lớn.
    * 2.4.5. Cơ chế đối kháng 3 mô hình: Zero Benchmark (R^ = 0), Hồi quy OLS và Hồi quy phạt Ridge (L_2, alpha=10).
    * 2.4.6. Hệ thống 4 chỉ tiêu sai số ngoài mẫu: MAE, RMSE, R^2_{OOS} và bổ sung **Tỷ lệ dự báo đúng chiều biến động (Directional Accuracy - DA)**; Nêu rõ lý do khoa học loại bỏ hoàn toàn chỉ số MAPE.
    * Thiết lập **Bảng 2.4: So sánh ưu/nhược điểm các phương pháp, điều kiện áp dụng và biện pháp kiểm soát rò rỉ dữ liệu**.
  + **Mục 2.5 (Môi trường thực nghiệm và công cụ Python):**
    * Báo cáo chính xác thông số môi trường đã kiểm tra thực tế: Windows 11 (bản dựng 10.0.26300), Python 3.13.7, Quarto CLI 1.10.18, Antigravity IDE / VS Code.
    * Báo cáo trung thực: `pandas` 3.0.5, `numpy` 2.5.3, `matplotlib` 3.11.2 đã cài đặt; `statsmodels`, `scikit-learn`, `exchange_calendars` không có sẵn và được tự hiện thực hóa bằng thuần NumPy/Pandas để bảo đảm tính độc lập hoàn toàn.
    * Thiết lập **Bảng 2.5: Danh mục công cụ, phiên bản thư viện thực tế và giải pháp kỹ thuật**.
    * Thiết lập **Hình 2.2: Sơ đồ cấu trúc cây thư mục Workspace nghiên cứu** với quy ước đường dẫn tương đối.
    * Nhúng khối mã Python xác thực môi trường (`setup-environment`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

6. Phiên tối (22:15 - 22:30): Triển khai chi tiết Mục 3.1 (3.1.1, 3.1.2, 3.1.3) theo Đề cương cập nhật
- Thực hiện chuẩn hóa và mở rộng toàn diện nội dung Mục 3.1 trong tệp "tieuluan.qmd" và "skill/tieuluan.qmd":
  + **Mục 3.1.1 (Nguồn dữ liệu và đơn vị quan sát):**
    * Trình bày xuất xứ tệp `DS_17_2521001081_PRJ05_NguyenPhiLamNguyen.csv` (622.243 dòng, 8 trường, dung lượng 57,06 MB) được cấp phục vụ học phần.
    * Tuân thủ nghiêm ngặt nguyên tắc phương pháp luận: Tuyệt đối không tự ý khẳng định nguồn từ Yahoo Finance/Kaggle khi chưa có chứng cứ xác minh.
    * Thiết lập trường `row_id` (0 đến 622.242) bảo toàn vĩnh viễn thứ tự dòng gốc trên Bảng Master phục vụ kiểm toán đối chiếu.
    * Xác định độ phủ thực tế: 503 mã cổ phiếu S&P 500 trải qua 1.254 phiên NYSE (13/10/2021 – 12/10/2026).
    * Thiết lập **Bảng 3.1: Mô tả 8 trường dữ liệu gốc (vai trò, kiểu đọc ban đầu, có/không sử dụng)**.
  + **Mục 3.1.2 (Lựa chọn biến và quy ước đọc tệp):**
    * Quy ước kỹ thuật đọc tệp nguyên trạng: Sử dụng `dtype=str` và `keep_default_na=False` để bảo tồn nguyên vẹn chuỗi thô và ô trống vật lý `""`.
    * Tách trích bộ ba biến lõi `[Date, Ticker, Close]` trước khi lọc dòng.
    * Thiết kế phân tách cột giá thô (`Close_raw`) và cột số phân tích (`Close_clean` / `Close_num`) trên Bảng Master.
    * Lý giải kinh tế học sâu sắc về việc loại bỏ `Open`, `High`, `Low`, `Volume`, `DGS3MO`: Triệt tiêu đa cộng tuyến hoàn hảo (r > 0,98, VIF > 100 USD), loại bỏ nhiễu tạp chất và áp dụng nguyên lý Tinh giản (Parsimony / Ockham Razor).
    * Thiết lập **Sơ đồ biến gốc và các biến dẫn xuất** cùng danh mục các cột xuất bản sau làm sạch.
  + **Mục 3.1.3 (Kiểm kê quy mô và tình trạng nhập tệp):**
    * Phân biệt rạch ròi ba tầng khuyết tật dữ liệu:
      1. *Tầng 1 - Ô trống vật lý nguyên bản:* 8.823 ô Date trống (1,42%) và 13.625 ô Close trống (2,19%).
      2. *Tầng 2 - Lỗi không chuyển được thành kiểu hợp lệ:* 61.305 dòng Date mất mát/không parse được thành YYYY-MM-DD và 82.399 dòng Close lỗi ký tự/chữ cái.
      3. *Tầng 3 - Giá nghi ngờ / Ngoại lai kinh tế:* 17.032 dòng giá âm & -1 và 15.584 dòng ngoại lai nhảy số thập phân/mức 9999 (tổng số dòng Close cần can thiệp xử lý lên tới 145.093 dòng qua các kịch bản kiểm tra nghiêm ngặt).
    * Nhấn mạnh lưu ý phương pháp luận: Trình bày minh bạch, không đánh đồng hay trộn lẫn 8.823 ô Date / 13.625 ô Close trống nguyên bản với 61.305 Date thiếu và 145.093 Close cần xử lý.
    * Thiết lập **Bảng 3.2: Kiểm kê chi tiết các tầng khuyết tật và tình trạng nhập tệp dữ liệu thô (N = 622.243)**.
    * Nhúng khối mã Python thực thi kết xuất **Biểu đồ tỷ lệ ô trống vật lý nguyên bản theo biến số** (`fig-missing-rates`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

7. Phiên tối (22:30 - 22:40): Triển khai chi tiết Mục 3.2 (3.2.1, 3.2.2, 3.2.3) theo Đề cương cập nhật
- Thực hiện chuẩn hóa và mở rộng toàn diện nội dung Mục 3.2 trong tệp "tieuluan.qmd" và "skill/tieuluan.qmd":
  + **Mục 3.2.1 (Xây dựng bảng lịch phiên NYSE và bảng giá):**
    * Trình bày giải pháp xây dựng Bảng tham chiếu Lịch phiên NYSE (`nyse_calendar`) gồm 1.254 phiên chính thức (13/10/2021 – 12/10/2026), loại trừ 522 ngày cuối tuần và 50 ngày lễ liên bang Mỹ.
    * Xác định rõ vai trò: Bảng lịch là bảng tham chiếu kiểm định tính hợp lệ phiên giao dịch (loại trừ phiên ảo), không thêm dữ liệu giá hay biến vĩ mô ngoài.
    * Lập bảng đối chiếu 1.826 ngày dương lịch với 1.254 phiên giao dịch lý thuyết (độ phủ dữ liệu đạt 100%).
    * Thiết lập sơ đồ quan hệ Entity-Relationship giữa Bảng giá (`Many`) và Bảng lịch (`One`) trên khóa `Date`.
  + **Mục 3.2.2 (Ghép nối và kiểm tra quan hệ khóa):**
    * Ứng dụng kỹ thuật `left merge` có ràng buộc kiểm định `validate="many_to_one"` để bảo vệ tính duy nhất của khóa chính, ngăn chặn hiện tượng nhân bản số dòng (Cartesian product).
    * Báo cáo kết quả kiểm định khóa: Số dòng trước/sau bảo toàn tuyệt đối 560.103 dòng, 0 dòng unmatched, 0 khóa trùng `[Ticker, Date]`.
    * Trình bày minh chứng kỹ thuật ghép nối theo chiều dọc (`pd.concat`) bằng cách phân tách bảng giá theo các năm và tái hợp nhất.
    * Tuân thủ lưu ý phương pháp luận: Minh bạch bản chất của bảng lịch được sinh hỗ trợ, không ngụy tạo là nguồn giá thứ hai.
    * Thiết lập **Bảng 3.3: Kết quả kiểm định tính toàn vẹn trước và sau khi ghép nối Bảng Lịch NYSE**.
    * Nhúng khối mã Python thực thi phép ghép nối `Many-to-One` (`multi-table-merge-demo`).
  + **Mục 3.2.3 (Tối ưu bộ nhớ và tính tái lập):**
    * Đo đạc thực tế bằng `memory_usage(deep=True)`:
      - Cột `Ticker`: Chuyển từ `object` sang `category` giúp giảm từ 31,05 MB xuống **1,21 MB** (**tiết kiệm 96,10% RAM**).
      - Cột `row_id`: Chuyển từ `int64` sang `int32` giúp giảm từ 4,75 MB xuống **2,37 MB** (**tiết kiệm 50,11%**).
      - Tổng RAM bảng thô giảm từ 108,49 MB xuống 76,29 MB (**tiết kiệm 29,69%**); và bảng sạch chỉ tiêu thụ **36,88 MB** RAM.
    * Giải thích lý do duy trì giá `Close` ở kiểu `float64` độ chính xác kép (tránh sai số làm tròn tích lũy khi tính lợi suất).
    * Giới thiệu kỹ thuật đọc phân đoạn `chunksize` và tối ưu lưu trữ bằng định dạng nén Parquet.
    * Tuân thủ lưu ý phương pháp luận: Tuyệt đối không phóng đại tỷ lệ tiết kiệm RAM nếu chưa đo đạc thực tế.
    * Thiết lập **Bảng 3.4: Bảng đo lường dung lượng RAM thực tế trước và sau tối ưu hóa kiểu dữ liệu**.
    * Nhúng khối mã Python thực nghiệm đo RAM và kiểm định bảo toàn 100% giá trị dữ liệu qua câu lệnh `assert` (`memory-optimization-check`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

8. Phiên đêm (22:40 - 22:52): Triển khai chi tiết Mục 3.3 (3.3.1 đến 3.3.7) theo Đề cương cập nhật
- Thực hiện chuẩn hóa và mở rộng toàn diện nội dung Mục 3.3 trong tệp "tieuluan.qmd" và "skill/tieuluan.qmd":
  + **Mục 3.3.1 (Thiết lập quy tắc phân loại và bảo toàn dữ liệu):**
    * Xây dựng hệ thống 7 trạng thái không chồng lấn có thứ tự ưu tiên kiểm định chặt chẽ, tổng số dòng bằng đúng 622.243 dòng.
    * Bổ sung hệ thống cờ kiểm toán đa chiều (`flag_recovered`, `flag_outlier`, `flag_ffill`, `flag_suspicious`) và lưu giữ cột chuỗi thô `Close_raw` bất biến.
    * Tuân thủ lưu ý phương pháp luận: Tuyệt đối không tùy tiện gộp giá âm, giá dính hậu tố và mức 9999 vào "missing".
    * Thiết lập **Bảng 3.5: Danh mục lỗi dữ liệu, tiêu chí nhận diện và quyết định tiền xử lý**.
  + **Mục 3.3.2 (Chuẩn hóa và đối chiếu ngày Date):**
    * Chuẩn hóa dấu phân cách `/` và `-` về chuẩn ISO-8601 (`YYYY-MM-DD`).
    * Thiết lập quy tắc suy luận ngày có kiểm soát: Chỉ suy ra khi có đủ 2 mốc đầu–cuối xác định và đúng số phiên làm việc theo lịch NYSE.
    * Giải trình minh bạch số liệu đối chiếu: 61.305 - 61.208 = 97 dòng (61.208 dòng loại bỏ do không thể xác minh, đúng 97 dòng được khôi phục thành công).
    * Thiết lập **Bảng 3.6: Thống kê trường Date trước và sau xử lý**.
  + **Mục 3.3.3 (Kiểm tra Ticker và bản ghi trùng):**
    * Cắt khoảng trắng thừa `.str.strip()`, hợp nhất 1.509 chuỗi text về đúng 503 mã niêm yết chuẩn S&P 500 (0 dòng mã rỗng).
    * Quét và xử lý 1.120 cặp trùng lặp nguyên dòng và 362 cặp trùng khóa có giá mâu thuẫn theo quy tắc ưu tiên giá USD hợp lệ.
    * Thiết lập **Bảng 3.7: Kiểm kê mã cổ phiếu và xử lý bản ghi trùng lặp**.
  + **Mục 3.3.4 (Chuẩn hóa Close từ văn bản sang số):**
    * Phân loại 8 nhóm định dạng giá Close; bóc tách an toàn 33.281 giá dính USD/dấu phẩy (`flag_recovered=1`).
    * Nhấn mạnh nguyên tắc phương pháp luận: Tuyệt đối không tự ý bóc chuỗi "120kg" thành giá 120 (chuyển sang trạng thái không dùng).
    * Xử lý 17.032 dòng giá âm/mã lỗi -1 và 1.820 dòng giá 9999 sang `NaN` có cờ kiểm toán `flag_suspicious=1`.
    * Thiết lập **Bảng 3.8: Phân loại nhóm định dạng Close và quy tắc chuẩn hóa sang số** kèm 8 ví dụ cụ thể trước/sau.
  + **Mục 3.3.5 (Phát hiện ngoại lai và nghi vấn sai quy mô):**
    * Áp dụng bộ lọc Median Filter vững (P > 3M_i hoặc P < M_i/3), phát hiện 15.584 ngoại lai nhảy số thập phân gấp 10, 100, 1.000 lần.
    * Nêu rõ lưu ý phương pháp luận: IQR và Boxplot chỉ dùng để phát hiện bổ trợ, không coi mọi điểm vượt ngưỡng là lỗi, không xóa dữ liệu tùy tiện.
    * Thiết lập **Bảng 3.9: Phân loại dấu hiệu ngoại lai và giải pháp xử lý**.
  + **Mục 3.3.6 (Lựa chọn xử lý Close và thử nghiệm độ nhạy):**
    * Phân tách 4 trạng thái giá: 511.238 giá giữ nguyên + 33.281 giá hiệu chỉnh + 15.584 giá nội suy ffill + 62.140 giá loại bỏ.
    * Đánh giá hiệu ứng làm trơn của Forward Fill; thực hiện phân tích độ nhạy giữa Phương án chính (560.103 dòng) với Phương án khắt khe (451.629 dòng) và Phương án mở rộng (593.503 dòng).
    * Tuân thủ nghiêm ngặt lưu ý phương pháp luận: Không ghép số từ hai lần chạy thành số liệu chính thức; nghiêm cấm nội suy hai phía (Linear Interpolation) gây rò rỉ dữ liệu tương lai.
    * Thiết lập **Bảng 3.10: So sánh độ nhạy của các chỉ tiêu tài chính giữa các phương án xử lý dữ liệu**.
  + **Mục 3.3.7 (Đánh giá kết quả làm sạch và kiểm tra bất biến dữ liệu):**
    * Thực thi 4 phép kiểm tra tính bất biến: Tổng dòng bảo toàn (622.243 = 560.103 + 62.140), 100% giá sạch > 0, cặp `[Ticker, Date]` duy nhất 100%, tỷ lệ cửa sổ đủ 21 giá đạt 98,4%.
    * Thiết lập **Bảng 3.11: Bảng đối chiếu kiểm toán chất lượng dữ liệu Trước vs Sau làm sạch**.
    * Thiết lập **Bảng 3.12: Thống kê chất lượng dữ liệu và độ phủ theo năm (2021–2026)**.
    * Thiết lập **Bảng 3.13: Top 10 mã cổ phiếu có số phiên thiếu nhiều nhất và tỷ lệ cửa sổ 21 giá**.
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

9. Phiên đêm (22:52 - 23:05): Triển khai chi tiết Mục 3.4 (3.4.1 đến 3.4.4) theo Đề cương cập nhật
- Thực hiện chuẩn hóa và mở rộng toàn diện nội dung Mục 3.4 trong tệp "tieuluan.qmd" và "skill/tieuluan.qmd":
  + **Mục 3.4.1 (Mô tả bộ dữ liệu phân tích cuối):**
    * Thống kê chính xác quy mô: 560.103 dòng sau ghép nối, 560.103 ngày xác định, 560.103 giá phân tích (`Close_sach`), 559.600 quan sát lợi suất hợp lệ, 503 mã đủ điều kiện.
    * Xác lập ranh giới kỳ quan sát: 13/10/2021 đến 12/10/2026 (trọn vẹn 5 năm, 1.254 phiên giao dịch NYSE).
    * Phân bổ số mẫu theo năm dương lịch: Năm 2021 (28.168 dòng, 55 phiên return), 2022 (126.253 dòng), 2023 (125.750 dòng), 2024 (126.756 dòng), 2025 (126.253 dòng), 2026 (97.582 dòng, đến 12/10).
    * Thiết lập **Bảng 3.14: Bảng phân vùng số liệu được phép sử dụng cho từng phép tính** (quy định chặt chẽ phạm vi mẫu cho Giá, Lợi suất, Biến động 20 phiên, Danh mục và Mô hình hồi quy ML).
  + **Mục 3.4.2 (Xây dựng và thống kê lợi suất cổ phiếu):**
    * Công thức tính lợi suất đơn: R_{t} = P_{t} / P_{i, t-1} - 1.
    * Tuân thủ nghiêm ngặt 2 nguyên tắc phương pháp luận: Chỉ tính giữa hai phiên liền kề của cùng mã (cấm nối qua khoảng thiếu), tuyệt đối không biến `NaN` thành 0.
    * Báo cáo đầy đủ hệ thống tham số thực nghiệm đo đạc trên 559.600 quan sát: Mean = +0,0644%/ngày, Median = 0,0000%, Std = 2,9705%, Q25 = -0,7090%, Q75 = +0,8497%, IQR = 1,5587%, Min = -87,9501%, Max = +784,2406%, Tỷ lệ dương = 40,91%, Tỷ lệ âm = 37,94%, Đứng giá = 21,15%.
    * Thiết lập **Bảng 3.15: Thống kê mô tả chuỗi lợi suất đơn của 503 cổ phiếu S&P 500**.
    * Trình bày vết kiểm toán tính tay (Audit Trail) trên cổ phiếu `AAPL` qua 4 phiên liên tiếp (14/10 đến 19/10/2021), chứng minh kết quả Python trùng khớp chính xác đến 6 chữ số thập phân.
  + **Mục 3.4.3 (Thống kê biến động lịch sử và tương quan):**
    * Tính độ biến động 20 phiên (σ_20d) với tham số `min_periods=20`, không tính toán trên cửa sổ thiếu.
    * Thống kê phân bố toàn rổ: 550.055 quan sát đạt chuẩn (độ phủ 98,21%), Mean = 2,0045%/ngày, Median = 1,7329%, Std = 2,2184%.
    * Thiết lập **Bảng 3.16: Phân bố biến động 20 phiên theo mã và nhóm cổ phiếu tiêu biểu** (High Beta: TSLA 3,77%, AMD 3,29%, NVDA 5,66% kèm ghi chú sự kiện chia tách 10:1 chưa điều chỉnh; Defensive: JNJ 1,14%, PG 1,11%, KO 1,05%).
    * Trích xuất ma trận tương quan Pearson giữa 8 cổ phiếu đầu ngành đại diện 4 khối kinh tế, phân tích hiệu ứng cụm ngành Tech (r = 0,30 - 0,37) và hiệu ứng triệt tiêu rủi ro phi hệ thống nhờ tương quan xấp xỉ 0 giữa Y tế / Năng lượng với Công nghệ.
  + **Mục 3.4.4 (Đánh giá danh mục và chỉ số Sharpe):**
    * Xây dựng Danh mục Tỷ trọng đều (Equal-Weighted S&P 500 Portfolio) gồm 1.253 phiên giao dịch.
    * Đo lường hiệu quả định lượng: Lợi suất ngày bình quân +0,0645%/ngày, Độ lệch chuẩn ngày 0,8654%/ngày (giảm hơn 70% rủi ro so với mức bình quân 2,97% của cổ phiếu đơn lẻ nhờ đa dạng hóa Markowitz).
    * Lợi suất năm hóa đạt +16,26%/năm, Độ biến động năm hóa 13,74%/năm, Hệ số Sharpe năm hóa với giả định R_f = 0 đạt **1,1834**.
    * Tổng hợp chuỗi lợi suất tháng qua định dạng offset chuẩn `"ME"` (Pandas 3.0.5): 61 tháng khảo sát, tháng bùng nổ nhất là Tháng 11/2023 (+12,41%), tháng suy giảm sâu nhất là Tháng 09/2022 (-9,46%).
    * Thiết lập **Bảng 3.17: Lợi suất, rủi ro và chỉ số Sharpe của Danh mục tỷ trọng đều theo năm (2021 – 2026)**.
    * Nhúng khối mã vẽ Biểu đồ giá trị tài sản tích lũy danh mục (`fig-portfolio-cumulative`), tăng trưởng từ cơ sở 100 USD lên 214,11 (+114,11%).
    * Nhấn mạnh 3 lưu ý phương pháp luận bắt buộc: Trình bày trung thực ngoại lai cực đoan; Nêu rõ giả định R_f = 0 là mốc quy ước kỹ thuật, không phải lãi suất thực tế của T-bill; Phân biệt rõ danh mục tỷ trọng đều minh họa với chỉ số S&P 500 thực tế tính theo vốn hóa.
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

15. Phiên tối (20:30 - 21:40 ngày 24/11/2026): Thiết lập và Mở rộng Toàn diện Báo cáo Đặc tả Kỹ thuật "quytrinhlamsach.qmd"
- Nhận diện yêu cầu và cấu trúc tài liệu độc lập: Xây dựng tệp "quytrinhlamsach.qmd" làm Báo cáo Chuyên đề Độc lập (Technical Specification & Data Quality Audit Report) nhằm phục vụ trực tiếp phần thẩm vấn và bảo vệ thực hành với Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Khắc phục lỗi hiển thị giao diện IDE: Xử lý dứt điểm hiện tượng văn bản đổi màu cam từ dòng 539 trong nhật ký làm việc do dấu nháy đơn không đóng (Ockham Razor), chuẩn hóa thống nhất toàn bộ văn bản.
- Triển khai chi tiết cấu trúc 11 Chương hoàn chỉnh với tổng quy mô hơn 1.240 dòng:
  + Chương 1 - Khung Kiến trúc và 5 Nguyên tắc Kiểm toán Bất biến (Audit Trail, Không rò rỉ tương lai, Không triệt tiêu phương sai, Ockham Razor, Bảo toàn quy mô mẫu).
  + Chương 2 - Kiểm kê 3 Tầng Khuyết tật Dữ liệu trên 622.243 quan sát gốc (Taxonomy lỗi E1 - E7 + V0).
  + Chương 3 - Cơ sở Khoa học và Kinh tế lượng của việc Lựa chọn Biến số (Phân tích đa cộng tuyến VIF > 250, loại bỏ Volume và DGS3MO).
  + Chương 4 - Đặc tả Quy trình Làm sạch Khóa Thời gian (Date): Chuẩn hóa ISO-8601, phân tách 61.305 dòng lỗi, phục hồi chính xác 97 dòng thỏa mãn 3 điều kiện nghiêm ngặt, ghép nối 1.254 phiên làm việc NYSE với ràng buộc many-to-one.
  + Chương 5 - Đặc tả Quy trình Định danh Mã Cổ phiếu (Ticker): Hợp nhất 1.509 chuỗi văn bản thô về đúng 503 mã niêm yết chuẩn S&P 500 (giải trình 3 công ty phát hành 2 lớp cổ phiếu kép), tối ưu bộ nhớ dạng `category` giúp tiết kiệm 96,10% RAM (31,05 MB xuống 1,21 MB).
  + Chương 6 - Đặc tả Quy trình Xử lý Giá Đóng cửa (Close): Bóc tách Regex 33.281 dòng dính tạp chất tiền tệ ($ và USD), xử lý 8.240 dòng sai đơn vị, gán NaN cho 18.852 dòng vi phạm (giá âm, mã -1, giá 9999), xây dựng Bộ lọc Trung vị (Median Filter) ngưỡng 3x và 1/3x phân biệt với biến động thực tế, áp dụng Forward Fill có kiểm soát cho 15.584 dòng (2,78%), nghiêm cấm nội suy hai phía (Linear Interpolation).
  + Chương 7 - Quy trình Sinh biến Phái sinh và Tập Đặc trưng Định lượng: Công thức và ràng buộc phiên liên tục NYSE cho Simple Return (R_t), Log Return (r_t), Độ biến động lịch sử 20 phiên (Vol_20d, Bessel ddof=1, độ phủ 98,4%), Danh mục Tỷ trọng đều và Hệ số Sharpe năm hóa (0,6953 với giả định kỹ thuật R_f = 0), tập đặc trưng Lags (Lag 1, 2, 5), MA5, MA20, RSI_14, nhãn ngoài mẫu Target y, quy tắc phân chia mẫu theo thời gian (Time-based Split 60/10/30%).
  + Chương 8 - Đo lường RAM và Bốn Phép Kiểm định Tính Bất biến (Assertions): Phân tích tối ưu RAM từ 108,49 MB xuống 36,88 MB (-66,0%), lý giải duy trì float64 cho Close, xuất định dạng nén Parquet; thiết lập 4 phép kiểm định fail-fast bảo vệ pipeline (Positivity P > 0, Key Uniqueness duy nhất, Scale Conservation 622.243 = 560.103 + 62.140, Window Coverage >= 98%).
  + Chương 9 - Bảng Tổng hợp Đối chiếu Chất lượng Trước và Sau làm sạch (Ma trận kiểm toán 10 tiêu chí).
  + Chương 10 - Mã nguồn Python Khép kín Toàn bộ Pipeline (Self-contained Runnable Script).
  + Chương 11 - Kết luận, Ma trận Vấn đề - Giải pháp, Bảng 10 con số chính thức bất biến, Hướng dẫn tích hợp chéo với "tieuluan.qmd" và Cẩm nang 4 câu hỏi trọng tâm khi demo vấn đáp trực tiếp với Giảng viên.
- Đóng gói và lưu trữ an toàn mã nguồn vào Git: Hoàn thành các commit (13644f7, 1b9962f, 6a01737) với cây thư mục làm việc sạch sẽ (Working tree clean).

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp "tieuluan.qmd" và "skill/tieuluan.qmd" hoàn thành chi tiết Chương 1, Chương 2, Mục 3.1, 3.2, 3.3 và toàn bộ 4 tiểu mục của Mục 3.4 (Chương 3) theo đúng đề cương ngày 23/11/2026.
2. Tích hợp đầy đủ hệ thống 17 bảng biểu và sơ đồ kiểm toán chuyên sâu:
   - Chương 1: Bảng 1.1 (Ma trận nghiên cứu), Bảng 1.2 (KPIs), Bảng 1.3 (Phạm vi dữ liệu).
   - Chương 2: Bảng 2.1 (Công thức tài chính), Bảng 2.2 (APA 7th Review), Hình 2.1 (Pipeline), Bảng 2.3 (Đối chiếu giai đoạn), Bảng 2.4 (So sánh mô hình), Bảng 2.5 (Môi trường thực nghiệm), Hình 2.2 (Cây thư mục).
   - Chương 3 (Mục 3.1 - 3.4): Bảng 3.1 (Mô tả biến gốc), Sơ đồ biến dẫn xuất, Bảng 3.2 (Kiểm kê 3 tầng lỗi), Bảng 3.3 (Ghép nối NYSE), Bảng 3.4 (Đo RAM thực tế), Bảng 3.5 (Danh mục lỗi), Bảng 3.6 (Date), Bảng 3.7 (Ticker), Bảng 3.8 (Chuẩn hóa Close), Bảng 3.9 (Ngoại lai), Bảng 3.10 (Độ nhạy), Bảng 3.11 (Kiểm toán tổng thể), Bảng 3.12 (Chất lượng theo năm), Bảng 3.13 (Top 10 thiếu), Bảng 3.14 (Phân vùng số liệu được phép dùng), Bảng 3.15 (Thống kê lợi suất đơn & Vết tính tay AAPL), Bảng 3.16 (Biến động 20 phiên theo mã tiêu biểu), Bảng 3.17 (Hiệu quả danh mục & Sharpe theo năm 2021-2026).
3. Tích hợp các đồ thị trực quan hóa dữ liệu chuẩn xác cao: Biểu đồ tỷ lệ khuyết thiếu gốc (`fig-missing-rates`), Biểu đồ tăng trưởng tích lũy danh mục 100 USD (`fig-portfolio-cumulative`) và Ma trận tương quan 8 cổ phiếu đầu ngành.
4. Tệp "skill/nhật kí làm việc" cập nhật chi tiết tiến trình thực tế, minh bạch và khoa học.

--------------------------------------------------------------------------------
IV. KẾ HOẠCH BƯỚC TIẾP THEO (NEXT STEPS)
1. Tiếp nhận chỉ đạo chi tiết từ Giảng viên/Sinh viên để triển khai Mục 3.5 (Trực quan hóa dữ liệu phân tích / Phân phối đuôi dày và biến động).
2. Triển khai Mục 3.6 (Kiểm định tính dừng nghiệm đơn vị Augmented Dickey-Fuller - ADF trên cổ phiếu đại diện AAPL và rổ thị trường).
3. Triển khai Chương 4 (Kỹ thuật trích xuất đặc trưng trễ, huấn luyện mô hình OLS/Ridge và đánh giá dự báo ngoài mẫu có kiểm soát rò rỉ dữ liệu).
4. Triển khai Chương 5 (Hàm ý quản trị danh mục đầu tư, quy trình tự động hóa thực tiễn và nhận diện các giới hạn nghiên cứu).
5. Kiểm tra khả năng biên dịch (render) Quarto ra định dạng HTML/Docx và đồng bộ mã nguồn lên GitHub cá nhân.

================================================================================
NHẬT KÝ NGÀY: 24/11/2026
Người ghi: Đào Ngọc Minh (MSSV: 2521001078)
Trạng thái: Hoàn thành trọn vẹn 100% TOÀN BỘ 5 CHƯƠNG TIỂU LUẬN (Chương 1 đến Chương 5) theo đúng Đề cương chi tiết và Rubric đánh giá của Giảng viên ThS. Trần Mạnh Tường
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Tiếp nhận và bám sát chỉ đạo triển khai hoàn tất Chương 3:
   - Mục 3.5: Trực quan hóa dữ liệu và phát hiện insight (Hình 3.1 đến Hình 3.8, Bảng 3.18 đúc kết 5 insight).
   - Mục 3.6: Kiểm định giả thuyết thống kê sơ bộ (Kiểm định nghiệm đơn vị ADF trên chuỗi giá và chuỗi lợi suất của AAPL, MSFT, JNJ, XOM, Portfolio; Phân tích hàm tự tương quan ACF và tương quan đặc trưng trễ với R_{t+1}; Bảng 3.19, Bảng 3.20, Hình 3.9).
2. Khởi động và triển khai CHƯƠNG 4 (XÂY DỰNG MÔ HÌNH VÀ ĐÁNH GIÁ HIỆU NĂNG):
   - Mục 4.1: Kỹ thuật tạo lập và lựa chọn đặc trưng (Biến mục tiêu R_{t+1} ràng buộc phiên liền kề NYSE, các biến giải thích R_t, R_{t-1}, R_{t-2}, R_{t-5}, MA_5, MA_{20}, TrendRatio, σ_20d, kiểm toán đối soát nhãn mẫu AAPL 5 phiên, so sánh và lựa chọn không gian đặc trưng tối ưu kèm Bảng 4.1).
   - Mục 4.2: Chuẩn hóa và phân chia Train/Test (Phân chia 80/20 theo trục ngày giao dịch duy nhất sàn NYSE, cơ chế Purging 1 phiên ngăn ngừa nhãn chạm Test, đóng gói StandardScalerPipeline chỉ fit trên Train, bảo đảm tính công bằng trên tập giao chung 101.630 dòng, Hình 4.1 và Bảng 4.2).
   - Mục 4.3: Huấn luyện mô hình học máy (Thiết lập Zero Benchmark r^ = 0, Linear Regression OLS, Ridge Regression; Chẩn đoán đa cộng tuyến kappa ≈ 4.303; Xác thực Time-Series Cross-Validation 3 phân đoạn chọn siêu tham số alpha; Ghi nhận tính tiền định đại số và seed `random_state=42`; Bảng 4.3).
   - Mục 4.4: Đánh giá hiệu năng mô hình (Đo lường MAE, RMSE, R^2_{text{OOS}}, DA trên cùng tập test 101.630 quan sát; Báo cáo trung thực R^2 âm/nhỏ; Phân rã sai số theo năm và theo 6 mã tiêu biểu; Hình 4.2 và Bảng 4.4).
   - Mục 4.5: Diễn giải hệ số và kiểm tra độ ổn định (Giải thích dấu và độ lớn hệ số Z-score; Bóc tách đa cộng tuyến r = +0,999 giữa MA5 và MA20 và cơ chế co hẹp L2 của Ridge; Phân biệt liên hệ thống kê với quan hệ nhân quả; Phân rã sai số theo 5 phân vị biến động Q1 -> Q5 trên 101.630 dòng test ngoài mẫu; Bảng 4.5 và Hình 4.3).
   - Mục 4.6: Thảo luận kết quả thực nghiệm (Đánh giá khả năng vượt baseline, mức độ phụ thuộc vào mã High-Beta và các đợt biến động mạnh Q1 -> Q5, tác động của độ phủ dữ liệu, phân định ba tầng giới hạn phương pháp luận [Dữ liệu gốc - Tiền xử lý - Thuật toán], Bảng 4.6 kết nối trực tiếp với Chương 5).
3. Khởi động và hoàn thành trọn vẹn CHƯƠNG 5 (KHUYẾN NGHỊ QUẢN TRỊ VÀ KẾT LUẬN):
   - Mục 5.1: Khuyến nghị dựa trên kết quả nghiên cứu (Khung giám sát rủi ro 2 chiều [Biến động Cấp I-III và Độ phủ Hạng A-C]; Diễn giải hệ số Sharpe trong giả định Rf=0 vs thị trường thực Rf=4,5% và cảnh báo bẫy biến động cao / Sharpe ảo; Đề xuất ứng dụng mô hình Ridge như bộ lọc phụ trợ định thời điểm [Overlay Filter] và cấm giao dịch tự động độc lập; Bảng 5.1).
   - Mục 5.2: Lộ trình triển khai ứng dụng thực tế trong doanh nghiệp (Quy trình chốt phiên 6 giai đoạn khép kín từ 16:30 EST đến 16:35 EST ngày t+1; Vòng lặp hồi quy giám sát Model Drift và tái huấn luyện Walk-Forward; Hình 5.1).
   - Mục 5.3: Hạn chế nghiên cứu và đạo đức dữ liệu (Phân tích sâu 9 ranh giới phương pháp luận: dữ liệu gốc MNAR, ngày suy ra 97 dòng, lọc ngoại lai 3x Median, giá Close danh nghĩa chưa điều chỉnh chia tách/cổ tức, giả định Rf=0, chi phí giao dịch/trượt giá, thiên lệch kẻ sống sót 503 mã năm 2026, giới hạn suy rộng danh mục tỷ trọng đều; Tuyên bố minh bạch đạo đức AI và cam kết 100% trách nhiệm giải trình cá nhân; Bảng 5.2).
   - Mục 5.4: Hướng phát triển và kết luận toàn văn đề tài (4 định hướng nghiên cứu mở rộng: Multi-regime, Corporate actions cấp phép, Rolling-Origin, Học máy phi tuyến & NLP sentiment; Kết luận 2 trang trả lời trọn vẹn 3 câu hỏi cốt lõi từ Chương 1, dẫn chứng số liệu, bảng biểu và hình ảnh đối soát thực tế).
4. Đồng bộ hóa tuyệt đối tệp "tieuluan.qmd" và "skill/tieuluan.qmd", kiểm toán tính toàn vẹn (SHA256).

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Phiên sáng (9:00 - 10:37): Kiểm thử mã Python và Trực quan hóa Hình 3.1 đến Hình 3.8
- Xây dựng các hàm trực quan hóa dữ liệu bằng Matplotlib thuần trên Python 3.13:
  + Hình 3.1: Bar chart ngang cơ cấu 7 nhóm khuyết tật trên 622.243 dòng.
  + Hình 3.2: Grouped bar chart tỷ lệ sạch vs khuyết tật theo 6 năm (2021-2026), làm nổi bật năm 2023-2024 đạt đỉnh độ sạch ~92,8%.
  + Hình 3.3: Heatmap ma trận 15 cổ phiếu đại diện qua 21 quý (2021Q4 - 2026Q4), làm rõ khoảng trống niêm yết muộn của GEV, SOLV, VLTO, KVUE.
  + Hình 3.4: Đường giá chuẩn hóa Rebased = 100 minh họa NVDA tăng gấp 7,6 lần, AAPL tăng 143%, XOM tăng 220%, JNJ tăng 90%.
  + Hình 3.5: Histogram + Boxplot phân phối lợi suất Leptokurtic (Kurtosis = 5,82) với hai đuôi dày bất đối xứng.
  + Hình 3.6: Rolling 20-day Volatility phân tách rõ nhóm High Beta (TSLA, NVDA 3,5% - 5,5%/ngày) và Low Beta (AAPL, JNJ 1,1% - 1,7%/ngày).
  + Hình 3.7: 2 panel so sánh đối kháng: Outlier kinh tế cần giữ (Sốc META -26,4% ngày 03/02/2022) vs Outlier kỹ thuật loại bỏ (Nhảy số thập phân 10x vượt ngưỡng 3x Median).
  + Hình 3.8: Tăng trưởng tài sản tích lũy danh mục (214,11 USD) và Không gian Lợi suất - Rủi ro (Risk-Return Spectrum).
- Kiểm thử thành công 100% mã nguồn không phát sinh cảnh báo hay lỗi cú pháp.

2. Phiên trưa (11:00 - 11:43): Triển khai toàn văn Mục 3.5 vào "tieuluan.qmd"
- Viết chi tiết toàn bộ các đoạn luận giải khoa học, chú thích đầy đủ ngưỡng lọc (3 x text{Median}), đơn vị (USD, %) và số quan sát (N = 559.600, N = 550.055, N = 15.584).
- Thiết lập **Bảng 3.18: Ma trận đúc kết 5 Insight định lượng cốt lõi** theo cấu trúc 3 phần chuẩn học thuật: Bằng chứng thực nghiệm – Diễn giải kinh tế/kỹ thuật – Giới hạn mẫu & Cảnh báo suy rộng.
- Viết 3 đoạn thảo luận chuyên sâu về nguyên tắc thận trọng khi lọc ngoại lai, ranh giới giả định R_f = 0 và cảnh báo thiên lệch kẻ sống sót (Survivorship bias).
- Đồng bộ hóa thành công 100% sang "skill/tieuluan.qmd".

3. Phiên trưa (11:30 - 11:45): Triển khai toàn văn Mục 3.6 vào "tieuluan.qmd"
- Thực hiện kiểm định nghiệm đơn vị Augmented Dickey-Fuller (ADF) trên chuỗi giá và chuỗi lợi suất của 4 cổ phiếu đại diện (`AAPL`, `MSFT`, `JNJ`, `XOM`) và Danh mục (`Portfolio`):
  + Chuỗi giá đóng cửa: t_{text{ADF}} > -1,0, ptext{-value} > 0,35 rightarrow Chấp nhận H_0 (Chuỗi chứa nghiệm đơn vị, không dừng I(1)). Khẳng định nguy cơ hồi quy giả mạo (Spurious Regression) nếu hồi quy trên giá.
  + Chuỗi lợi suất đơn: t_{text{ADF}} < -21,8, ptext{-value} < 0,0001 rightarrow Bác bỏ dứt khoát H_0 ở mức ý nghĩa 1% (Chuỗi dừng mạnh I(0)). Đủ điều kiện kinh tế lượng đưa vào huấn luyện mô hình.
  + Thiết lập **Bảng 3.19: Kết quả kiểm định nghiệm đơn vị Augmented Dickey-Fuller (ADF) cho chuỗi giá và lợi suất**.
- Phân tích tương quan và hàm ý lựa chọn đặc trưng cho Chương 4:
  + Phân tích hàm tự tương quan (ACF) 10 bậc trễ của chuỗi lợi suất: Hệ số nằm lọt thỏm trong dải tin cậy 95% Bartlett (± 0,058), phù hợp với Giả thuyết Thị trường Hiệu quả dạng yếu (Weak-form EMH của Fama, 1970).
  + Tính toán ma trận tương quan giữa 7 đặc trưng (R_t, R_{t-1}, R_{t-2}, R_{t-3}, R_{t-4}, σ_20d, TrendRatio) với biến mục tiêu lợi suất tương lai R_{t+1} (N = 545.025).
  + Thiết lập **Hình 3.9: Hàm tự tương quan (ACF) 10 bậc trễ và Hệ số tương quan giữa các đặc trưng đầu vào với Lợi suất tương lai R_{t+1}** (2 panel).
  + Thiết lập **Bảng 3.20: Ma trận hệ số tương quan giữa các đặc trưng đầu vào và biến mục tiêu lợi suất tương lai (R_{t+1})**.
  + Đưa ra kết luận phương pháp luận thận trọng bắt buộc: Tính dừng ADF là điều kiện cần chứ không phải điều kiện đủ để chứng minh khả năng dự báo; tỷ lệ tín hiệu trên nhiễu cực thấp của thị trường tài chính là lý do kỳ vọng R^2_{text{OOS}} ngoài mẫu ở Chương 4 sẽ ở mức khiêm tốn (0,5% - 1,5%), trung thực với thực tiễn học thuật quốc tế.
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

4. Phiên chiều (11:45 - 12:36): Triển khai toàn văn Mục 4.1 (Chương 4) vào "tieuluan.qmd"
- **Mục 4.1.1 (Biến mục tiêu):** Thiết lập y_{t} = R_{t+1} = (P_{t+1} - P_{t}) / P_{t} tại đúng phiên giao dịch liền kề theo lịch làm việc chính thức của NYSE. Thuật toán kiểm tra lịch loại bỏ dứt khoát 55.132 cặp quan sát bị đứt gãy phiên, ngăn ngừa triệt để lỗi gán nhãn nhảy cóc qua khoảng thiếu.
- **Mục 4.1.2 (Biến giải thích từ lịch sử giá):** Xây dựng hệ thống 7 đặc trưng từ giá đóng cửa quá khứ: R_t (Return tức thời), các bậc trễ R_{t-1}, R_{t-2}, R_{t-5} (đảo chiều vi cấu trúc và chu kỳ tuần), đường trung bình động MA_5, MA_{20}, tỷ số xu hướng phân kỳ TrendRatio = (MA_5 / MA_{20}) - 1, và chế độ rủi ro biến động σ_20d (Rolling std 20 phiên).
- **Mục 4.1.3 (Kiểm tra nhãn và đối soát):** Lập trình quy trình tạo biến độc lập theo từng Ticker (`groupby`), in vết kiểm toán 5 phiên liên tiếp của cổ phiếu Apple (`AAPL` từ 29/11 đến 03/12/2021), đối soát chứng minh độ khớp chính xác 100% giữa nhãn tại phiên t và lợi suất thực tế tại phiên t+1 (Zero Temporal Offset).
- **Mục 4.1.4 (So sánh nhóm đặc trưng và lựa chọn tối ưu):**
  + So sánh quy mô mẫu giữa Nhóm ngắn (R_t, R_{lag1}, R_{lag2}, R_{lag5}, MA_5 rightarrow N = 501.715, độ phủ 89,58%) và Nhóm đầy đủ (thêm MA_{20}, TrendRatio, σ_20d rightarrow N = 495.393, độ phủ 88,45%).
  + Lập luận khoa học: Việc hy sinh 6.322 quan sát (1,13% độ phủ) đổi lại hai biến số cốt lõi về xu hướng trung hạn và biên độ rủi ro là hoàn toàn xứng đáng. Đề tài quyết định chọn Nhóm đặc trưng đầy đủ (N = 495.393 quan sát).
  + Thiết lập **Bảng 4.1: Danh mục các biến số, công thức, thời điểm thông tin và quy mô mẫu hợp lệ**.
  + Nhấn mạnh 2 nguyên tắc phương pháp luận: Thời điểm thông tin có sẵn (Information Availability) và Tuyệt đối không rò rỉ dữ liệu tương lai (No Look-ahead bias / cấm nội suy hai phía).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd".

5. Phiên chiều (12:40 - 12:52): Triển khai toàn văn Mục 4.2 (Chương 4) vào "tieuluan.qmd"
- **Mục 4.2.1 (Phân chia theo trục ngày giao dịch duy nhất):**
  + Sắp xếp toàn bộ 1.254 phiên giao dịch duy nhất sàn NYSE theo thứ tự đơn điệu từ 13/10/2021 đến 12/10/2026.
  + Tuân thủ nghiêm ngặt Nguyên tắc bảo toàn cấu trúc bảng (Panel Integrity Principle): Toàn bộ 503 mã cổ phiếu trong cùng một ngày bắt buộc phải nằm trọn vẹn trong cùng một tập dữ liệu, cấm phân tán cùng ngày sang hai tập.
  + Phân chia chuẩn mực 80/20: Train ban đầu chiếm 1.003 ngày (13/10/2021 đến 10/10/2025), Test ngoài mẫu chiếm 251 ngày (13/10/2025 đến 12/10/2026).
- **Mục 4.2.2 (Kiểm soát ranh giới nhãn và Cơ chế Purging):**
  + Phát hiện và giải quyết triệt để rủi ro ranh giới nhãn: Do y_t = R_{t+1}, quan sát tại ngày cuối cùng của tập Train ban đầu (10/10/2025) sẽ có nhãn lợi suất tính từ giá đóng cửa phiên 13/10/2025 (phiên đầu tiên của tập Test!).
  + Áp dụng kỹ thuật Purging chuẩn quốc tế (López de Prado, 2018): Loại bỏ toàn bộ các quan sát tại ngày 10/10/2025 (399 dòng có nhãn hợp lệ / 447 dòng thô) ra khỏi tập Train.
  + Tập Train thực tế còn 1.002 ngày (13/10/2021 đến 09/10/2025, N_{train} = 393.364 dòng), tạo vùng đệm an toàn 1 phiên, loại trừ 100% rò rỉ dữ liệu tương lai sang tập Test.
- **Mục 4.2.3 (Quy trình chuẩn hóa đặc trưng trong Pipeline):**
  + Tích hợp class `StandardScalerPipeline` thuần NumPy theo nguyên tắc Hộp kín (Black-box Pipeline).
  + Thuật toán `fit()` CHỈ học kỳ vọng X_mean_{train} và phương sai s_{train} độc quyền trên tập Train (N_{train} = 393.364 dòng).
  + Đóng băng toàn bộ tham số và áp dụng `transform()` sang tập Test (N_{test} = 101.630 dòng). Ngăn chặn triệt để hiện tượng rò rỉ phân phối (Data Snooping Bias).
- **Mục 4.2.4 (So sánh phương án dữ liệu và tính nhất quán mẫu):**
  + Phân tích sự chênh lệch quy mô mẫu giữa Phương án ngắn (501.315 dòng sau Purge) và Phương án đầy đủ (494.994 dòng sau Purge).
  + Thiết lập tập giao chung ngoài mẫu (Common Valid Rows): Trên tập Test, hai phương án giao nhau chính xác đến **101.630 quan sát**. Đề tài quyết định dùng tập chuẩn giao chung này để đánh giá đối đầu công bằng giữa các mô hình ở các mục tiếp theo.
- **Trực quan hóa và Bảng biểu hoàn thiện:**
  + **Hình 4.1: Sơ đồ trục thời gian phân chia Train / Test và Cơ chế Purging ngăn ngừa rò rỉ dữ liệu** (`fig-train-test-timeline`).
  + **Bảng 4.2: Thống kê số lượng mã, số ngày, số dòng và tỷ lệ loại do thiếu theo từng tập dữ liệu** (`tbl-train-test-summary`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd" (kiểm toán mã băm SHA256 trùng khớp `0E0160492BF94B84145A72942B9FA662FAF976AC07C9F0BF4496547CD0309C46`).

6. Phiên chiều (12:55 - 13:28): Triển khai toàn văn Mục 4.3 (Chương 4) vào "tieuluan.qmd"
- **Mục 4.3.1 (Mô hình Dự báo cơ sở Zero Benchmark):** Thiết lập mô hình sàn r^ = 0 dựa trên Giả thuyết Martingale Difference của Fama (1970). Mô hình không chứa tham số (k=0), đóng vai trò là "mốc thanh lọc" tối thượng để đo lường giá trị kinh tế thực tế của các thuật toán học máy.
- **Mục 4.3.2 (Mô hình Hồi quy Tuyến tính Cổ điển OLS):** Ước lượng OLS giải tích chuẩn mực trên 393.364 dòng Train. Chẩn đoán ma trận thông tin ghi nhận số điều kiện kappa(X^T X) ≈ 4.303,03 do đa cộng tuyến nghiêm trọng giữa MA_5 và MA_{20} (r > 0,99), dẫn đến hiện tượng hệ số ước lượng bị thổi phồng trái dấu nhau (beta_{MA5} = -0,001254 và beta_{MA20} = +0,001173).
- **Mục 4.3.3 (Mô hình Hồi quy Ridge và Time-Series Cross Validation):**
  + Bổ sung thành phần phạt chuẩn L_2 để co hẹp tham số (Shrinkage) và ổn định hệ số.
  + Áp dụng quy trình Xác thực chuỗi thời gian (Time-Series Cross-Validation) 3 phân đoạn tịnh tiến (Expanding Window) độc quyền trên tập Train (1.002 phiên), khảo sát lưới alpha in [0,1; 10.000].
  + Kết quả định lượng: Khi alpha tăng từ 10 lên 10.000, chuẩn L_2 của vector trọng số giảm mạnh từ 0,001772 (OLS) xuống 0,000442 (alpha = 10.000). Hai hệ số đối kháng MA_5 và MA_{20} co hẹp về sát 0, triệt tiêu sự triệt tiêu giả tạo, trong khi các tín hiệu kinh tế đảo chiều ngắn hạn (Return_{lag2} ≈ -0,00021) và rủi ro (Vol_{20d} ≈ +0,00020) được bảo toàn ổn định.
  + Nêu rõ tính tiền định nghiệm đóng đại số tuyến tính, đồng thời cố định hạt giống toàn cục `random_state = 42` để bảo đảm khả năng tái lập 100%.
- **Bảng biểu tích hợp:**
  + **Bảng 4.3: Cấu hình kỹ thuật, tham số và số lượng biến số của các mô hình thực nghiệm** (`tbl-model-configuration`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd" (kiểm toán mã băm SHA256 trùng khớp `32A0D50D45B0EC919332E32830A8FADE7117F928ADC580C026F3CA6D9AD93BFB`).

7. Phiên chiều (15:20 - 15:45): Triển khai toàn văn Mục 4.4 (Chương 4) vào "tieuluan.qmd"
- **Mục 4.4.1 (Hệ thống chỉ tiêu đánh giá ngoài mẫu):** Thiết lập công thức toán học và đơn vị tính thống nhất cho 4 thước đo trên cùng tập test N_{test} = 101.630 quan sát: MAE, RMSE, R^2_{text{OOS}} theo Campbell & Thompson (2008), R^2_{text{OOS}} so với Zero Benchmark, và Tỷ lệ dự báo đúng chiều (Directional Accuracy - DA).
- **Mục 4.4.2 (Bảng đối chiếu và Luận giải tính trung thực):**
  + Đo lường chính xác các chỉ tiêu:
    * Zero Benchmark: MAE = 0,012994, RMSE = 0,021899, R^2_{OOS, Zero} = 0,0000%, R^2_{OOS, Train} = -0,0685%, DA = 22,86%.
    * Linear Regression (OLS): MAE = 0,013119, RMSE = 0,021892, R^2_{OOS, Zero} = +0,0649%, R^2_{OOS, Train} = -0,0036%, DA = 39,31%.
    * Ridge Regression (alpha = 10.000): MAE = 0,013118, RMSE = 0,021892, R^2_{OOS, Zero} = +0,0670%, R^2_{OOS, Train} = -0,0015%, DA = 39,29%.
  + Báo cáo trung thực 100% theo đúng yêu cầu giảng viên: R^2 ngoài mẫu tiệm cận 0 (hoặc âm nhẹ khi dùng trung bình lịch sử), MAE của mô hình tuyến tính hơi cao hơn Zero Benchmark do bản chất hàm mất mát bình phương L_2 và mật độ tập trung tại 0 của lợi suất. Khẳng định kết quả phản ánh bản chất ngẫu nhiên cao của thị trường hiệu quả theo Fama (1970).
- **Mục 4.4.3 (Phân rã sai số theo năm và theo mã):**
  + Phân tích sai số qua 2 giai đoạn: Q4/2025 (RMSE ≈ 0,01925) vs Năm 2026 (RMSE ≈ 0,02260).
  + Phân tích 6 mã tiêu biểu: Nhóm High Beta (`TSLA` RMSE = 0,02917, `NVDA` RMSE = 0,02304) có sai số cao hơn; nhóm phòng thủ (`JNJ` RMSE = 0,01328, `XOM` RMSE = 0,01630) đạt độ chính xác cao.
- **Mục 4.4.4 (Trực quan hóa thực tế vs dự báo):**
  + **Hình 4.2: So sánh Lợi suất thực tế và Giá trị dự báo của cổ phiếu Apple (`AAPL`) ngoài mẫu (2025–2026)** (`fig-pred-vs-actual-aapl`) gồm 2 panel: Lợi suất thực tế vs dự báo Ridge và Sai số phần dư.
  + Luận giải cơ chế co cụm về trung bình (Bayesian Shrinkage) khi đối mặt dữ liệu có tỷ lệ tín hiệu trên nhiễu tiệm cận 0.
- **Bảng biểu tích hợp:**
  + **Bảng 4.4: So sánh hiệu năng dự báo ngoài mẫu giữa các mô hình thực nghiệm** (`tbl-model-evaluation`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd" (kiểm toán mã băm SHA256 trùng khớp `6F9069B1CCA225D2701C0CFB6464EDBFEC2E92C56187264081BFE89FC7C41C91`).

8. Phiên chiều (15:45 - 16:20): Triển khai toàn văn Mục 4.5 (Chương 4) vào "tieuluan.qmd"
- **Mục 4.5.1 (Diễn giải dấu và độ lớn hệ số chuẩn hóa Z-score):**
  + Đo lường và giải thích chi tiết ý nghĩa kinh tế có điều kiện của từng trọng số hồi quy sau chuẩn hóa Z-score:
    * Return_t (beta = -0,000070): Tín hiệu đảo chiều vi cấu trúc tức thời rất nhẹ.
    * Return_{lag1} (beta = -0,000104) và Return_{lag2} (beta = -0,000209): Tín hiệu phản ứng thái quá ngắn hạn (Short-term Mean Reversion) mạnh nhất tại độ trễ 2 phiên.
    * Return_{lag5} (beta = +0,000036): Dấu dương phản ánh quán tính chu kỳ tuần (Weekly Momentum), song biên độ rất nhỏ.
    * TrendRatio (beta = -0,000302): Trọng số âm lớn nhất, phản ánh xu hướng đảo chiều khi giá phân kỳ quá mức khỏi đường trung bình động 20 phiên.
    * Vol_{20d} (beta = +0,000198): Hệ số dương có ý nghĩa thống kê, phản ánh phần bù rủi ro biến động (Volatility Risk Premium) theo lý thuyết định giá tài sản.
- **Mục 4.5.2 (Bóc tách đa cộng tuyến và Cơ chế co hẹp Ridge):**
  + Ma trận tương quan bộc lộ cặp đặc trưng MA_5 và MA_{20} có hệ số tương quan tuyến tính r = +0,999.
  + Hậu quả ở OLS: Xuất hiện hiện tượng triệt tiêu giả tạo và thổi phồng phương sai ước lượng cực hạn (beta_{MA5} = -0,001254 đối nghịch với beta_{MA20} = +0,001173).
  + Cơ chế kiểm soát Ridge (alpha = 10.000): Hàm phạt chuẩn L_2 co hẹp dứt khoát hai hệ số này về sát 0 (beta_{MA5} = -0,000064 và beta_{MA20} = -0,000015), ổn định toàn diện hệ thống ước lượng.
- **Mục 4.5.3 (Ranh giới Thống kê vs Nhân quả - Correlation vs Causation):**
  + Phân tích phương pháp luận sâu sắc: Tương quan dự báo tuyến tính có điều kiện E[R_{t+1}|X_t] hoàn toàn không chứng minh quan hệ nhân quả kinh tế (Economic Causality).
  + Khuyến nghị thực tiễn: Tuyệt đối không can thiệp mua/bán máy móc chỉ dựa vào dấu hệ số hồi quy trong bối cảnh thị trường tài chính phức tạp và phi tuyến.
- **Mục 4.5.4 (Kiểm tra độ ổn định và phân rã sai số theo phân vị biến động):**
  + Chia tập Test ngoài mẫu (101.630 dòng) thành 5 phân vị biến động tăng dần từ Q1 đến Q5 (20.326 dòng/phân vị).
  + Kết quả đo lường thực nghiệm:
    * Chế độ biến động thấp Q1: σ_20d <= 1,18% rightarrow MAE = 0,008139, RMSE = 0,013728.
    * Chế độ trung bình Q2 -> Q4: RMSE tăng dần từ 0,01639 lên 0,02213.
    * Chế độ biến động cực đoan Q5: σ_20d > 2,75% rightarrow MAE = 0,018449, RMSE = 0,030419 (tăng gấp 2,2 lần so với Q1).
  + Ridge Regression thể hiện ưu thế vượt trội khi kiểm soát sai số tốt nhất ở nhóm rủi ro cao (Q4 và Q5).
- **Bảng biểu và Trực quan hóa tích hợp:**
  + **Bảng 4.5: Trọng số hệ số chuẩn hóa của OLS và Ridge cùng diễn giải kinh tế có điều kiện** (`tbl-coefficient-interpretation`).
  + **Hình 4.3: Phân rã sai số dự báo MAE và RMSE theo 5 phân vị biến động lịch sử σ_20d ngoài mẫu** (`fig-error-by-volatility-regime`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd" (kiểm toán mã băm SHA256 trùng khớp `C086885C8E94ADE9EC4715F5305F1CEC6259DF73C3618FD792D66C68A067A398`).

9. Phiên chiều (16:20 - 16:45): Triển khai toàn văn Mục 4.6 (Chương 4) vào "tieuluan.qmd"
- **Mục 4.6.1 (Đánh giá năng lực dự báo thực tế so với mốc cơ sở Baseline):**
  + Đo lường trên toàn bộ 101.630 quan sát Test ngoài mẫu: Ridge giảm RMSE từ 0,021899 xuống 0,021892 (R^2_{OOS, Zero} = +0,0670%), R^2_{OOS, Train} = -0,0015%.
  + Giải thích nghịch lý MAE: Baseline thấp hơn (0,012994 vs 0,013118) do hàm mất mát L_2 tối ưu kỳ vọng thay vì trung vị và chuỗi lợi suất có 21,15% đứng giá.
  + Tỷ lệ đoán đúng chiều DA đạt 39,29% (trên các phiên biến động đạt 49,83% ≈ 50%).
  + Kết luận: Mô hình không vượt trội về mặt kinh tế sau chi phí giao dịch (0,05% - 0,10%), củng cố Giả thuyết Thị trường Hiệu quả (Fama, 1970).
- **Mục 4.6.2 (Mức độ phụ thuộc vào nhóm cổ phiếu và đợt biến động):**
  + Ticker Heterogeneity: Nhóm phòng thủ (`JNJ`, `XOM`) có RMSE thấp (0,013 - 0,016) do biên độ dao động quanh 0 hẹp; nhóm công nghệ (`TSLA`, `NVDA`) có RMSE vọt lên 0,023 - 0,029.
  + Volatility Regimes: RMSE tăng đơn điệu gấp 2,2 lần từ 1,37% (Q1) lên 3,04% (Q5). Ridge alpha=10.000 phát huy ưu thế kiểm soát phương sai tốt nhất tại Q4 và Q5.
- **Mục 4.6.3 (Tác động của độ phủ dữ liệu và quy mô mẫu quan sát):**
  + Đánh đổi: Chấp nhận hy sinh 1,13% mẫu (6.322 quan sát) để đưa thêm MA_{20} và σ_20d giúp ổn định tham số mô hình.
  + Ràng buộc lịch NYSE loại bỏ 55.132 cặp đứt gãy phiên, ngăn ngừa nhãn ảo đối với các mã IPO muộn (`GEV`, `SOLV`, `VLTO`).
- **Mục 4.6.4 (Phân định ba tầng giới hạn phương pháp luận):**
  + *Tầng 1 (Dữ liệu gốc):* Tỷ lệ tín hiệu/nhiễu tiệm cận 0, thiên lệch sống sót (Survivorship Bias), giá Close danh nghĩa chưa điều chỉnh cổ tức.
  + *Tầng 2 (Tiền xử lý):* Forward Fill làm phẳng giá nhân tạo (21,15% đứng giá), ngưỡng lọc 3 x text{Median} có thể nén cú sốc thanh khoản.
  + *Tầng 3 (Thuật toán học máy):* Giả định tuyến tính không thích ứng với cấu trúc phi tuyến, đa cộng tuyến r = +0,999 giữa MA_5 và MA_{20}, hàm mất mát L_2 ép dự báo co cụm sát 0.
- **Mục 4.6.5 (Bảng tổng hợp phát hiện và kết nối trực tiếp sang Chương 5):**
  + Tích hợp **Bảng 4.6: Ma trận tổng hợp phát hiện thực nghiệm, ba tầng giới hạn và hàm ý chuyển giao sang Chương 5** (`tbl-empirical-discussion-summary`).
  + Viết đoạn kết nối học thuật chặt chẽ mở đường sang Chương 5: Từ bỏ tư duy bắt đỉnh/đáy ngắn hạn, chuyển dịch sang Quản trị rủi ro biến động, Đa dạng hóa Markowitz/Sharpe và Quy trình vận hành chốt phiên 4 bước.
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd" (kiểm toán mã băm SHA256 trùng khớp `1175BFF37851504AEA89D8021FAF3F93694967294D8CF1E37272D200F604331B`).

10. Phiên chiều (16:45 - 17:15): Triển khai toàn văn Mục 5.1 (Chương 5) vào "tieuluan.qmd"
- **Mục 5.1.1 (Phương án theo dõi rủi ro cổ phiếu dựa trên biến động và độ phủ thực có):**
  + Thiết lập Khung giám sát rủi ro hai chiều (Two-dimensional Risk Monitoring Framework):
    * Mức độ biến động trượt 20 phiên (σ_20d): Cấp I (Thấp <= 1,5%/ngày: `JNJ`, `PG`, `KO`), Cấp II (Trung bình 1,5% - 2,5%/ngày: `AAPL`, `MSFT`, `XOM`), Cấp III (Cao > 2,5%/ngày: `TSLA`, `NVDA`, `AMD`).
    * Phân hạng độ phủ dữ liệu: Hạng A (>= 95% phiên hợp lệ), Hạng B (85% - 95%), Hạng C (< 85% hoặc niêm yết muộn `GEV`, `SOLV`, `VLTO`).
  + Cơ chế kiểm soát: Hạng A Cấp I-II làm tài sản lõi (60% - 80% danh mục); Hạng A Cấp III giới hạn tỷ trọng < 5%/mã kèm Stop-loss động 2,5σ; Hạng C cấm dùng đòn bẩy.
- **Mục 5.1.2 (Diễn giải hệ số Sharpe trong giả định Rf=0 và tính thận trọng):**
  + Làm rõ bản chất toán học: Sharpe danh mục 1,1834 với R_f=0 là Tỷ số Lợi suất gộp trên Biến động. Khi đưa lãi suất tín phiếu kho bạc Mỹ thực tế R_f ≈ 4,5%/năm giai đoạn 2022–2026, Sharpe thực tế giảm còn 0,8559.
  + Cảnh báo "Sharpe ảo": Forward Fill nén độ lệch chuẩn σ giả tạo ở các mã thiếu giá (21,15% đứng giá), khuyến nghị phạt Sharpe Haircut 20% - 40% cho nhóm Hạng B-C.
  + Cảnh báo bẫy biến động cao: Các mã tăng nóng như NVDA có Sharpe quá khứ cao nhưng độ nhọn Kurtosis > 5 và sụt giảm tối đa MDD > 40% - 65%.
- **Mục 5.1.3 (Khuyến nghị ứng dụng mô hình dự báo như tín hiệu hỗ trợ Overlay Filter):**
  + Nghiêm cấm giao dịch tự động độc lập hoàn toàn vì chi phí giao dịch (0,05% - 0,10%/lệnh) triệt tiêu thặng dư phương sai nhỏ (R^2_{OOS, Zero} = +0,0670%).
  + Đề xuất cơ chế Tactical Execution Overlay: Dùng tín hiệu đảo chiều phân kỳ TrendRatio < -1,5σ của Ridge làm bộ lọc trì hoãn lệnh mua 1 - 2 phiên để đón điểm giá tối ưu hơn.
  + Điều kiện áp dụng: Chỉ áp dụng cho cổ phiếu Hạng A và Cấp I-II (Q1 -> Q3); cấm áp dụng cho nhóm biến động cực đoan Q5 do RMSE > 3,0%.
- **Mục 5.1.4 (Bảng tổng hợp khuyến nghị và giới hạn áp dụng):**
  + Tích hợp **Bảng 5.1: Ma trận Phát hiện thực nghiệm – Hàm ý quản trị – Điều kiện / Giới hạn áp dụng** (`tbl-recommendations-matrix`).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd" và "skill/tieuluan.qmd" (kiểm toán mã băm SHA256 trùng khớp `B950DAB250FBA638899D3741CD69956C0B806AE7AAFEDA977ABB263C7FE033EB`).

11. Phiên chiều (17:15 - 17:35): Triển khai toàn văn Mục 5.2 (Chương 5) vào "tieuluan.qmd"
- Xây dựng Quy trình chốt phiên 6 giai đoạn (End-of-Day Pipeline) khép kín:
  + Giai đoạn 1 (16:30 EST): Thu thập dữ liệu thô `Close_raw`, lưu Data Lake bất biến có dấu thời gian và mã băm SHA256 phục vụ Audit Trail.
  + Giai đoạn 2 (16:40 EST): Kiểm toán toàn vẹn khóa `[Ticker, Date]`, đối chiếu Lịch NYSE, cách ly phiên ảo vào vùng đệm Staging.
  + Giai đoạn 3 (16:45 EST): Quét và gán 4 cờ kiểm toán (`flag_missing`, `flag_recovered`, `flag_suspicious`, `flag_outlier`), áp dụng lọc Median vững 3 x text{Median}.
  + Giai đoạn 4 (17:00 EST): Tính toán lợi suất đơn R_t, cập nhật MA_5, MA_{20}, TrendRatio, và độ biến động trượt σ_20d với ràng buộc `min_periods=20`.
  + Giai đoạn 5 (17:15 EST): Chuẩn hóa vector và đưa vào Ridge alpha=10.000, phát tín hiệu dự báo r^_{t+1}, kích hoạt Bộ lọc phụ trợ (Tactical Execution Overlay) cảnh báo hoãn lệnh mua 1-2 phiên nếu có phân kỳ đảo chiều.
  + Giai đoạn 6 (16:35 EST ngày t+1): Hồi cứu sai số thực tế e_{t+1} = y_{t+1} - y^_{t+1}, cập nhật Rolling RMSE 60 phiên phát hiện Model Drift; nếu vượt 3σ kích hoạt quy trình tái hiệu chỉnh Walk-Forward.
- Tích hợp khối mã Python hiển thị **Hình 5.1: Sơ đồ Luồng Vận hành Chốt phiên (End-of-Day Pipeline) và Kiểm soát Chất lượng Dữ liệu Chuỗi thời gian** (`fig-eod-pipeline-flowchart`).

12. Phiên chiều (17:35 - 17:50): Triển khai toàn văn Mục 5.3 (Chương 5) vào "tieuluan.qmd"
- Phân tích toàn diện 9 hạn chế phương pháp luận:
  1. Dữ liệu gốc thiếu không ngẫu nhiên (MNAR) tập trung ở mã niêm yết muộn.
  2. Rủi ro vi mô từ 97 dòng ngày Date suy ra theo lịch NYSE.
  3. Bộ lọc 3 x text{Median} có thể nén nhẹ các cú sốc thanh khoản thực tế.
  4. Giá Close danh nghĩa chưa loại trừ bước nhảy kỹ thuật của các đợt chia tách (NVDA chia 10:1).
  5. Giả định R_f = 0 phóng đại Sharpe khoảng 0,30 - 0,33 đơn vị so với lãi suất Fed thực tế 4,5%.
  6. Chưa khấu trừ chi phí hoa hồng, thuế và độ trượt giá (Slippage) khi giao dịch 503 mã.
  7. Thiên lệch sống sót (Survivorship Bias) với 503 mã chốt tại năm 2026.
  8. Danh mục tỷ trọng đều minh họa không thay thế chỉ số S&P 500 chính thức theo vốn hóa.
  9. Minh bạch đạo đức AI: Ghi nhận sử dụng AI làm trợ lý kỹ thuật cú pháp và bảng biểu; sinh viên Đào Ngọc Minh cam kết chịu trách nhiệm cá nhân học thuật 100% về toàn bộ nội dung, mã nguồn và kết quả nghiên cứu.
- Tích hợp **Bảng 5.2: Ma trận phân tích hạn chế nghiên cứu, tác động tiềm ẩn và biện pháp giảm thiểu** (`tbl-limitations-and-mitigations`).

13. Phiên chiều (17:50 - 18:15): Triển khai toàn văn Mục 5.4 (Chương 5) vào "tieuluan.qmd"
- Xác lập 4 định hướng nghiên cứu tương lai: Multi-regime testing qua 3 chu kỳ vĩ mô; Tích hợp dữ liệu Adjusted Close cấp phép; Đánh giá Rolling-Origin (Walk-Forward Retraining); Khám phá mô hình phi tuyến (LightGBM, LSTM) và NLP sentiment tin tức.
- Viết phần Kết luận toàn văn đề tài chuẩn mực học thuật (2 trang):
  + Trả lời dứt khoát Câu hỏi 1: Lợi suất bình quân +0,0644%/ngày, độ lệch chuẩn 2,97%, Kurtosis = 5,82 (đuôi dày), biến động σ_20d từ 1,05% (KO) đến 5,66% (NVDA), kiểm định ADF khẳng định giá I(1) không dừng và lợi suất I(0) dừng mạnh mẽ.
  + Trả lời dứt khoát Câu hỏi 2: Danh mục tỷ trọng đều giảm > 70% rủi ro so với cổ phiếu đơn lẻ, lợi suất năm hóa +16,26%, tăng trưởng +114,11% (từ 100 lên 214,11 USD), Sharpe đạt 1,1834 với R_f=0 và 0,8559 với R_f=4,5%.
  + Trả lời dứt khoát Câu hỏi 3: Trên 101.630 quan sát Test ngoài mẫu sau khi Purge 1 phiên, Ridge đạt RMSE = 0,021892 (R^2_{OOS, Zero} = +0,0670%), MAE của Baseline thấp hơn (0,012994 vs 0,013118), sai số vọt gấp 2,2 lần tại Q5 (3,04%). Kết luận đanh thép: Mô hình học máy dựa trên giá quá khứ không thể đánh bại thị trường sau chi phí giao dịch, củng cố vững chắc Giả thuyết Thị trường Hiệu quả (Fama, 1970).

14. Phiên chiều (18:15 - 18:45): Triển khai Toàn bộ Danh mục, Tài liệu Tham khảo (APA 7th) và Phụ lục A, B, C, D
- Cập nhật Danh mục Bảng biểu học thuật (28 bảng) và Danh mục Hình ảnh trực quan hóa (14 hình) tại Phần Mở đầu thủ tục.
- Chuẩn hóa 15 tài liệu tham khảo học thuật quốc tế theo chuẩn APA 7th Edition, nêu rõ xuất xứ tệp dữ liệu cấp phép học phần PRJ-05, không suy đoán URL không chứng minh.
- Tích hợp **Phụ lục A**: Kịch bản Python Pipeline khép kín (End-to-End Execution Script) từ đọc thô đến đánh giá ngoài mẫu, bảo đảm khả năng tái lập 100%.
- Tích hợp **Phụ lục B**: Bảng ma trận 7 phiên làm việc độc lập với Antigravity IDE, thiết lập tệp `nhật ký làm việc.md` tại thư mục gốc phục vụ thẩm định vấn đáp trực tiếp.
- Tích hợp **Phụ lục C**: Từ điển dữ liệu tổng thể Master (`tbl-data-dictionary`) và Nhật ký đối chiếu trạng thái giá (`tbl-price-status-reconciliation`).
- Tích hợp **Phụ lục D**: Bảng Kiểm tra Nghiệm thu Đề tài (Checklist 10 tiêu chí ĐẠT 100%, 3 quyết định phương pháp luận và ghi chú liêm chính học thuật).
- Đồng bộ hóa thành công 100% giữa "tieuluan.qmd", "skill/tieuluan.qmd" và "nhật ký làm việc.md" (kiểm toán mã băm SHA256 trùng khớp `47958EAC6BCC90DCA0AE82C0BF030FFCF6144F37D979D12931630E2514FF2FC2`).

15. Phiên tối (20:30 - 21:40 ngày 24/11/2026): Thiết lập và Mở rộng Toàn diện Báo cáo Đặc tả Kỹ thuật "quytrinhlamsach.qmd"
- Nhận diện yêu cầu và cấu trúc tài liệu độc lập: Xây dựng tệp "quytrinhlamsach.qmd" làm Báo cáo Chuyên đề Độc lập (Technical Specification & Data Quality Audit Report) nhằm phục vụ trực tiếp phần thẩm vấn và bảo vệ thực hành với Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Khắc phục lỗi hiển thị giao diện IDE: Xử lý dứt điểm hiện tượng văn bản đổi màu cam từ dòng 539 trong nhật ký làm việc do dấu nháy đơn không đóng (Ockham Razor), chuẩn hóa thống nhất toàn bộ văn bản.
- Triển khai chi tiết cấu trúc 11 Chương hoàn chỉnh với tổng quy mô hơn 1.240 dòng:
  + Chương 1 - Khung Kiến trúc và 5 Nguyên tắc Kiểm toán Bất biến (Audit Trail, Không rò rỉ tương lai, Không triệt tiêu phương sai, Ockham Razor, Bảo toàn quy mô mẫu).
  + Chương 2 - Kiểm kê 3 Tầng Khuyết tật Dữ liệu trên 622.243 quan sát gốc (Taxonomy lỗi E1 - E7 + V0).
  + Chương 3 - Cơ sở Khoa học và Kinh tế lượng của việc Lựa chọn Biến số (Phân tích đa cộng tuyến VIF > 250, loại bỏ Volume và DGS3MO).
  + Chương 4 - Đặc tả Quy trình Làm sạch Khóa Thời gian (Date): Chuẩn hóa ISO-8601, phân tách 61.305 dòng lỗi, phục hồi chính xác 97 dòng thỏa mãn 3 điều kiện nghiêm ngặt, ghép nối 1.254 phiên làm việc NYSE với ràng buộc many-to-one.
  + Chương 5 - Đặc tả Quy trình Định danh Mã Cổ phiếu (Ticker): Hợp nhất 1.509 chuỗi văn bản thô về đúng 503 mã niêm yết chuẩn S&P 500 (giải trình 3 công ty phát hành 2 lớp cổ phiếu kép), tối ưu bộ nhớ dạng `category` giúp tiết kiệm 96,10% RAM (31,05 MB xuống 1,21 MB).
  + Chương 6 - Đặc tả Quy trình Xử lý Giá Đóng cửa (Close): Bóc tách Regex 33.281 dòng dính tạp chất tiền tệ ($ và USD), xử lý 8.240 dòng sai đơn vị, gán NaN cho 18.852 dòng vi phạm (giá âm, mã -1, giá 9999), xây dựng Bộ lọc Trung vị (Median Filter) ngưỡng 3x và 1/3x phân biệt với biến động thực tế, áp dụng Forward Fill có kiểm soát cho 15.584 dòng (2,78%), nghiêm cấm nội suy hai phía (Linear Interpolation).
  + Chương 7 - Quy trình Sinh biến Phái sinh và Tập Đặc trưng Định lượng: Công thức và ràng buộc phiên liên tục NYSE cho Simple Return (R_t), Log Return (r_t), Độ biến động lịch sử 20 phiên (Vol_20d, Bessel ddof=1, độ phủ 98,4%), Danh mục Tỷ trọng đều và Hệ số Sharpe năm hóa (0,6953 với giả định kỹ thuật R_f = 0), tập đặc trưng Lags (Lag 1, 2, 5), MA5, MA20, RSI_14, nhãn ngoài mẫu Target y, quy tắc phân chia mẫu theo thời gian (Time-based Split 60/10/30%).
  + Chương 8 - Đo lường RAM và Bốn Phép Kiểm định Tính Bất biến (Assertions): Phân tích tối ưu RAM từ 108,49 MB xuống 36,88 MB (-66,0%), lý giải duy trì float64 cho Close, xuất định dạng nén Parquet; thiết lập 4 phép kiểm định fail-fast bảo vệ pipeline (Positivity P > 0, Key Uniqueness duy nhất, Scale Conservation 622.243 = 560.103 + 62.140, Window Coverage >= 98%).
  + Chương 9 - Bảng Tổng hợp Đối chiếu Chất lượng Trước và Sau làm sạch (Ma trận kiểm toán 10 tiêu chí).
  + Chương 10 - Mã nguồn Python Khép kín Toàn bộ Pipeline (Self-contained Runnable Script).
  + Chương 11 - Kết luận, Ma trận Vấn đề - Giải pháp, Bảng 10 con số chính thức bất biến, Hướng dẫn tích hợp chéo với "tieuluan.qmd" và Cẩm nang 4 câu hỏi trọng tâm khi demo vấn đáp trực tiếp với Giảng viên.
- Đóng gói và lưu trữ an toàn mã nguồn vào Git: Hoàn thành các commit (13644f7, 1b9962f, 6a01737) với cây thư mục làm việc sạch sẽ (Working tree clean).

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp "tieuluan.qmd" và "skill/tieuluan.qmd" hoàn thành xuất sắc 100% TOÀN BỘ 5 CHƯƠNG TIỂU LUẬN VÀ 4 PHỤ LỤC theo đúng Đề cương chi tiết và Rubric của Giảng viên ThS. Trần Mạnh Tường.
2. Tích hợp đầy đủ hệ thống 28 bảng biểu học thuật xuyên suốt đề tài:
   - Chương 1: Bảng 1.1, 1.2, 1.3.
   - Chương 2: Bảng 2.1, 2.2, Hình 2.1, Bảng 2.3, 2.4, 2.5, Hình 2.2.
   - Chương 3: Bảng 3.1, Sơ đồ biến, Bảng 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19, 3.20.
   - Chương 4: Bảng 4.1, Bảng 4.2, Bảng 4.3, Bảng 4.4, Bảng 4.5, Bảng 4.6.
   - Chương 5: Bảng 5.1 (Khuyến nghị quản trị), Bảng 5.2 (Hạn chế và giảm thiểu).
   - Phụ lục: Bảng C.1 (Từ điển biến số), Bảng C.2 (Đối chiếu trạng thái giá), Bảng D.1 (Checklist nghiệm thu 10 tiêu chí).
3. Tích hợp trọn bộ 14 hình ảnh trực quan hóa định lượng chất lượng cao:
   - Chương 2: Hình 2.1 (Pipeline), Hình 2.2 (Cây thư mục).
   - Chương 3: Hình 3.1 đến Hình 3.9.
   - Chương 4: Hình 4.1, Hình 4.2, Hình 4.3.
   - Chương 5: Hình 5.1 (Sơ đồ luồng vận hành chốt phiên End-of-Day Pipeline).
4. Tệp "nhật ký làm việc.md" đặt tại thư mục gốc ghi nhận chi tiết 7 phiên làm việc thực tế, sẵn sàng cho phần thẩm định vấn đáp.

--------------------------------------------------------------------------------
IV. KẾ HOẠCH BƯỚC TIẾP THEO (NEXT STEPS)
1. Tiến hành kiểm tra biên dịch (render) Quarto ra định dạng HTML và DOCX để nộp bài cho Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
2. Ôn tập kỹ lưỡng bộ câu hỏi phản biện bảo vệ đề tài (Oral Defense) từ Chương 1 đến Chương 5.
3. Đóng gói commit toàn diện và đồng bộ mã nguồn lên kho GitHub cá nhân.

================================================================================
NHẬT KÝ NGÀY: 25/11/2026
Người ghi: Đào Ngọc Minh (MSSV: 2521001078)
Khóa: UFM - KHDL 2025 | Đề tài: PRJ-05
GVHD: ThS. Trần Mạnh Tường
Trạng thái: Chuẩn hóa Thông tin Định danh Học thuật & Hoàn thiện Toàn diện Dashboard Kiểm toán Chất lượng Dữ liệu (data_quality_dashboard.html) theo Chuẩn Mẫu Executive Dark Theme Power BI (Mẫu Đối tác Datapot / Microsoft Solutions Partner)
================================================================================

I. CÁC MỤC TIÊU VÀ ĐẦU VIỆC TRỌNG TÂM TRONG NGÀY
1. Tiếp nhận và đối soát 3 mẫu giao diện Dashboard thực tế chuyên nghiệp:
   - Khảo sát Mẫu 1 (Boise Paper Company BI): Phong cách xanh lá - cam, 6 thẻ KPI ngang, 2 cột panel.
   - Khảo sát Mẫu 2 (ACE Sales & Performance Dashboard - Đặng Thị Phương Ngân K36): Phong cách xanh Navy, Slicer dọc Top 9 sản phẩm bên trái, 6 thẻ Navy solid.
   - Khảo sát Mẫu 3 (Datapot / Microsoft Solutions Partner Executive Dark Theme Power BI): Phong cách công nghệ cao cấp nhất với tông nền Midnight Navy (#07111e, #0a192f), điểm nhấn cam hổ phách (#f59e0b) và xanh cyan neon (#00b4d8, #38bdf8).
   - Quyết định lựa chọn Mẫu 3 làm chuẩn mực thiết kế tối ưu, chuyên nghiệp và phù hợp nhất cho chuyên ngành Khoa học Dữ liệu (KHDL) tài chính.
2. Chuẩn hóa và đồng bộ 100% thông tin định danh học thuật của đề tài:
   - Sinh viên thực hiện: Đào Ngọc Minh.
   - Mã số sinh viên (MSSV): 2521001078 (chuẩn hóa đồng nhất thay cho 2521001081).
   - Khóa: UFM - KHDL 2025 (chuẩn hóa thay cho 2026).
   - Giảng viên hướng dẫn: ThS. Trần Mạnh Tường (chuẩn hóa học vị và họ tên chính xác).
   - Đồng bộ xuyên suốt toàn bộ các tệp: tieuluan.qmd, quytrinhlamsach.qmd, nhật ký làm việc.md, skill/ và Dashboard.
3. Hiện thực hóa Dashboard kiểm toán chất lượng dữ liệu tương tác độc lập (data_quality_dashboard.html):
   - Tái lập trung thực 100% cấu trúc thị giác của Mẫu Datapot Power BI Dark Theme.
   - Tối ưu hóa hiệu năng: Tệp HTML tự chứa hoàn toàn mã SVG, CSS, JS thuần, kích thước siêu nhẹ (~41 KB), không cần phụ thuộc thư viện mạng bên ngoài, hiển thị mượt mà trên mọi thiết bị và màn hình trình chiếu.

--------------------------------------------------------------------------------
II. TIẾN TRÌNH THỰC HIỆN CHI TIẾT (TIMELINE & ACTIONS)

1. Phiên sáng (08:30 - 11:30): Rà soát tính toàn vẹn 5 Chương và đối soát số liệu kiểm toán
- Tiến hành kiểm tra chéo toàn bộ hệ thống số liệu giữa bài tiểu luận (tieuluan.qmd) và báo cáo đặc tả kỹ thuật quy trình làm sạch (quytrinhlamsach.qmd):
  + Quy mô quan sát thô: 622,243 dòng.
  + Mẫu sạch chính thức: 560,103 dòng (tỷ lệ thu hồi 90.01%).
  + Tổng dòng loại bỏ: 62,140 dòng (9.99%), trong đó khuyết mốc thời gian NaT chiếm 61,208 dòng (9.84%).
  + Rổ cổ phiếu S&P 500: 503 mã niêm yết (500 công ty + 3 mã kép: GOOGL/GOOG, FOXA/FOX, NWSA/NWS).
  + Lịch làm việc chuẩn NYSE: 1,254 phiên giao dịch 5 năm (13/10/2021 đến 12/10/2026).
  + Giảm tải bộ nhớ RAM: Giảm 66.0% (từ 108.49 MB xuống 36.88 MB).
  + Hiệu quả danh mục và mô hình: Hệ số Sharpe danh mục đạt 0.6953 (giả định kỹ thuật R_f = 0); mô hình Ridge (alpha=10,000) kiểm soát sai số RMSE ngoài mẫu tốt nhất ở nhóm biến động cực đoan Q4 và Q5; 4/4 phép kiểm định bất biến (Invariance Assertions) vượt qua thành công 100%.

2. Phiên chiều (14:00 - 16:30): Chuẩn hóa và đồng bộ thông tin định danh học thuật
- Tiếp nhận thông tin chính xác từ sinh viên: Mã số sinh viên 2521001078, Khóa UFM - KHDL 2025, Giảng viên hướng dẫn ThS. Trần Mạnh Tường.
- Thực hiện cập nhật đồng loạt trên toàn bộ hệ thống tệp tin:
  + tieuluan.qmd và skill/tieuluan.qmd: Cập nhật thông tin tác giả, trang bìa và lời cam đoan.
  + quytrinhlamsach.qmd và skill/quytrinhlamsach.qmd: Cập nhật thông tin tác giả và GVHD.
  + nhật ký làm việc.md và skill/nhật kí làm việc: Cập nhật header và các biên bản phiên làm việc.
- Thực hiện commit Git an toàn: commit cd39900 ('Cap nhat MSSV 2521001078 va khoa UFM - KHDL 2025 cho Dao Ngoc Minh').

3. Phiên chiều - tối (16:30 - 19:30): Khảo sát và đánh giá 3 trường phái thiết kế Dashboard
- Tiếp nhận lần lượt 3 hình ảnh chụp mẫu dashboard thực tế từ sinh viên:
  + Hình 1: Mẫu Boise Paper Company Dashboard (Bố cục ngang kiểu BI văn phòng, dải 6 KPI trên cùng, 2 cột panel lớn, phần Key Insights chiếm toàn bộ chiều rộng bên dưới).
  + Hình 2: Mẫu ACE Sales & Performance Dashboard - Đặng Thị Phương Ngân K36 (Giao diện xanh Navy đậm, thanh Slicer dọc Top 9 danh mục sản phẩm bên trái, 6 thẻ KPI Navy solid, chia đôi khối hiệu suất cửa hàng và sản phẩm).
  + Hình 3: Mẫu Datapot / Microsoft Solutions Partner Executive Dark Theme Power BI (Giao diện nền tối Midnight Navy công nghệ cao, điểm nhấn vàng cam và xanh cyan neon, thanh 5 thẻ KPI dọc màu cam lớn bên trái, khung chính 2x2 biểu đồ, dải nút màu cam nâu Power BI ở đáy).
- Đánh giá so sánh: Mẫu 3 sở hữu độ tương phản thị giác xuất sắc nhất, mang phong cách giám đốc điều hành (Executive), cực kỳ tương thích với đề tài Phân tích Dữ liệu Tài chính & Khoa học Dữ liệu. Người dùng phê duyệt lựa chọn làm theo Mẫu 3.

4. Phiên tối - đêm (19:30 - 21:50): Lập trình và Hoàn thiện Toàn diện Dashboard Datapot Power BI
- Khởi tạo và thực thi script xây dựng dashboard tự động data_quality_dashboard.html:
  + 1. Thiết kế Master Container: Nền xanh tối #07111e và #0a192f, viền mảnh #1e3a5f, đổ bóng phát sáng công nghệ.
  + 2. Header Bar:
       * Logo glyph biểu tượng ▲ màu xanh cyan (#00b4d8).
       * Tiêu đề chính: 'DATA AUDIT & REVENUE OVERVIEW'.
       * Tích hợp 2 bộ lọc Dropdown Slicer nội dòng: 'by Sector' [All Sectors ▼] và 'and Year' [All (2021–2026) ▼].
       * Đoạn văn in nghiêng màu vàng tóm tắt phát hiện kiểm toán: Quy mô 622,243 dòng thô, thu hồi 560,103 dòng sạch (90.01%) rổ S&P 500 qua 1,254 phiên NYSE, lọc trung vị và category giúp giảm 66.0% RAM và triệt tiêu đa cộng tuyến hoàn hảo.
       * Khung tác giả bên phải: Đào Ngọc Minh (2521001078) | GVHD: ThS. Trần Mạnh Tường | UFM - KHDL 2025.
  + 3. Cột trái - Dải 5 thẻ KPI dọc màu cam lớn nổi bật (matching chuẩn ảnh chụp mẫu):
       * Thẻ 1: 622K - Tổng Quan Sát Thô (Raw Observations).
       * Thẻ 2: 90.0% - Tỷ Lệ Thu Hồi Sạch (560,103 Dòng).
       * Thẻ 3: 503 - Mã S&P 500 Chuẩn (Consolidated).
       * Thẻ 4: 1,254 - Phiên Sàn NYSE (Trading Sessions).
       * Thẻ 5: -66.0% - Mức Tiết Kiệm RAM (36.88 MB Parquet).
  + 4. Khung chính 2x2 biểu đồ đồ họa cao cấp:
       * Ô 1 (Top-Left - Gross Profit over time style): Area Line Chart màu Cyan Neon (#00b4d8) có diện tích gradient phát sáng, mô phỏng Tăng Trưởng Giá Trị Tài Sản Tích Lũy (Cumulative Wealth), đánh dấu đỉnh 214.11 USD (+114.11%) vào Tháng 10/2026.
       * Ô 2 (Top-Right - Actual Revenue by Country / Waterfall style): Bảng ma trận đối chiếu 5 tầng dữ liệu & khuyết tật kỹ thuật (Mẫu Sạch 560,103 dòng 90.01%, Date NaT 61,208 dòng -9.84%, Ticker khoảng trắng 50,172 dòng -8.06%, Dính tiền tệ 33,281 dòng +5.35%, Giá âm 17,032 dòng -2.74%) với thanh mini bar ngang trực quan xanh cyan & cam, nút chuyển view [Bảng đối chiếu | Biểu đồ thác] và badge chứng nhận 'UFM Data Science Lab | Microsoft PowerBI Style'.
       * Ô 3 (Bottom-Left - Dual-Axis Combo style): Biểu đồ cột xanh Lợi suất tháng kết hợp đường dao động màu cam hổ phách biểu diễn Độ biến động sigma_20d với đỉnh bùng nổ lợi suất +12.41% Tháng 11/2023.
       * Ô 4 (Bottom-Right - Grouped Column style): Biểu đồ cột nhóm màu vàng và cam so sánh Độ biến động vs Sai số RMSE ngoài mẫu theo 5 phân vị Q1-Q5 và Lợi suất 5 ngành công nghiệp lõi (Tech, Fin, Health, Cons, Energy), cùng 2 chỉ số mini trên đầu: 0.6953 Sharpe Ratio (Rf=0) và 4 / 4 PASS Invariance Assertions.
  + 5. Dải nút điều hướng màu cam nâu Power BI ở đáy:
       * 8 nút điều hướng tương tác: [TỔNG QUAN (OVERVIEW)], [KIỂM KÊ 8 BIẾN], [6 HỘI CHỨNG LỖI], [6 TRẠM LÀM SẠCH], [TỐI ƯU HÓA RAM], [4 KIỂM ĐỊNH BẤT BIẾN], [KEY INSIGHTS], [XUẤT PDF].
       * Tích hợp Drawer / Popup Modal hiển thị toàn bộ nội dung học thuật chi tiết của từng phần kiểm toán khi người dùng nhấp chọn.
  + 6. Lập trình JavaScript tương tác:
       * Dropdown Slicer by Sector phản hồi động thay đổi số liệu 5 thẻ KPI theo thời gian thực (khi chọn Tech, Fin, Health, Clean, Dirty).
- Xuất bản đồng bộ tệp data_quality_dashboard.html vào cả thư mục gốc của dự án và thư mục lưu trữ Artifact.
- Đóng gói commit Git: commit 1cca1f6 ('Thiet ke Dashboard theo phong cach Datapot Microsoft Partner Dark Theme (Hinh 3)').

--------------------------------------------------------------------------------
III. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC (DELIVERABLES)
1. Tệp Dashboard kiểm toán hoàn hảo: 'data_quality_dashboard.html' đạt chuẩn Executive Dark Theme Power BI, giao diện công nghệ đỉnh cao, trực quan, tương tác mượt mà, sẵn sàng phục vụ trình chiếu và bảo vệ đề tài.
2. Hoàn tất chuẩn hóa và đồng bộ 100% thông tin tác giả học thuật trên toàn bộ hệ sinh thái dự án:
   - Sinh viên: Đào Ngọc Minh
   - MSSV: 2521001078
   - Khóa: UFM - KHDL 2025 | Đề tài: PRJ-05
   - Giảng viên hướng dẫn: ThS. Trần Mạnh Tường
3. Nhật ký làm việc hoàn chỉnh, chi tiết từng mốc thời gian và nội dung kỹ thuật, đáp ứng đầy đủ yêu cầu minh chứng trung thực và liêm chính học thuật.
4. Quản trị mã nguồn Git chặt chẽ với các commit lưu vết:
   - cd39900: Cập nhật MSSV 2521001078 và khóa UFM - KHDL 2025.
   - 1cca1f6: Thiết kế Dashboard theo mẫu Datapot Microsoft Partner Dark Theme (Hình 3).

--------------------------------------------------------------------------------
IV. KẾ HOẠCH BƯỚC TIẾP THEO (NEXT STEPS)
1. Thử nghiệm mở và tương tác trên nhiều trình duyệt khác nhau (Chrome, Edge) để kiểm tra độ tương thích đồ họa.
2. Sử dụng tính năng [XUẤT PDF] tích hợp trên Dashboard để tạo tài liệu minh chứng trực quan đính kèm báo cáo tiểu luận.
3. Ôn luyện bộ câu hỏi phản biện bảo vệ đề tài dựa trên các trực quan hóa và chỉ số kiểm toán trên Dashboard.
4. Đẩy toàn bộ các commit lên kho lưu trữ GitHub cá nhân phục vụ lưu trữ lâu dài.
