import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

doc = Document()

# Margins
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.9)
    s.right_margin = Inches(0.8)

# Palette
NAVY = RGBColor(27, 54, 93)      # #1B365D
SLATE = RGBColor(43, 84, 126)    # #2B547E
DARK_GRAY = RGBColor(45, 45, 45) # #2D2D2D
GOLD = RGBColor(180, 130, 20)    # #B48214

def set_para_font(p, name='Times New Roman', size_pt=12.5, color=DARK_GRAY, bold=False, italic=False, space_after=4, space_before=0, line_spacing=1.25):
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    for run in p.runs:
        run.font.name = name
        run.font.size = Pt(size_pt)
        run.font.color.rgb = color
        run.font.bold = bold
        run.font.italic = italic

def add_heading_1(text):
    h = doc.add_heading(text, level=1)
    set_para_font(h, size_pt=14, color=NAVY, bold=True, space_before=12, space_after=5)
    return h

def add_heading_2(text):
    h = doc.add_heading(text, level=2)
    set_para_font(h, size_pt=12.5, color=SLATE, bold=True, space_before=9, space_after=3)
    return h

def add_body(text, bold_prefix='', italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
        r_pre.font.color.rgb = DARK_GRAY
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.italic = italic
    r.font.color.rgb = DARK_GRAY
    return p

def add_bullet(text, bold_prefix=''):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
        r_pre.font.color.rgb = DARK_GRAY
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.color.rgb = DARK_GRAY
    return p

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=80, bottom=80, left=70, right=70):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout(text, title='GIẢI THÍCH CHUYÊN SÂU:'):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, 'F0F4F8')
    set_cell_margins(cell, top=100, bottom=100, left=130, right=110)
    
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        '<w:left w:val="single" w:sz="24" w:space="0" w:color="1B365D"/>'
        '<w:top w:val="none"/>'
        '<w:right w:val="none"/>'
        '<w:bottom w:val="none"/>'
        '</w:tcBorders>'
    )
    cell._tc.get_or_add_tcPr().append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.2
    r_title = p.add_run(title + ' ')
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(11)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY
    
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.size = Pt(11)
    r_text.font.italic = True
    r_text.font.color.rgb = DARK_GRAY
    doc.add_paragraph().paragraph_format.space_after = Pt(3)

# HEADER
p_top = doc.add_paragraph()
p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_top = p_top.add_run('TRƯỜNG ĐẠI HỌC TÀI CHÍNH – MARKETING\nKHOA CÔNG NGHỆ THÔNG TIN & KINH DOANH SỐ\n***')
r_top.font.name = 'Times New Roman'
r_top.font.size = Pt(12)
r_top.font.bold = True
r_top.font.color.rgb = NAVY
p_top.paragraph_format.space_after = Pt(12)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_title = p_title.add_run('QUY TRÌNH CHI TIẾT KIỂM TOÁN VÀ LÀM SẠCH DỮ LIỆU\n(DATA CLEANING PIPELINE)')
r_title.font.name = 'Times New Roman'
r_title.font.size = Pt(15)
r_title.font.bold = True
r_title.font.color.rgb = NAVY
p_title.paragraph_format.space_after = Pt(4)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_sub = p_sub.add_run('Tập dữ liệu: 17_2521001081_PRJ05_NguyenPhiLamNguyen.csv (622,243 dòng)\n'
                      'Cổ phiếu S&P 500 giai đoạn 2021 – 2026\n'
                      'Sinh viên thực hiện: Đào Ngọc Minh (2521001078) – Nguyễn Phi Lâm (2521001081)')
r_sub.font.name = 'Times New Roman'
r_sub.font.size = Pt(11)
r_sub.font.italic = True
r_sub.font.color.rgb = SLATE
p_sub.paragraph_format.space_after = Pt(16)

# PHẦN 1
add_heading_1('PHẦN 1: BỐI CẢNH TẬP DỮ LIỆU VÀ QUYẾT ĐỊNH TINH GỌN BIẾN')
add_body('Tập dữ liệu thô ban đầu gồm 622,243 dòng quan sát và 8 trường thông tin: Date, Ticker, Open, High, Low, Close, Volume, DGS3MO. Khi nạp vào Python, toàn bộ 8 cột đều bị ép kiểu chuỗi ký tự (object) do chứa nhiều tạp chất đơn vị đo lường, khoảng trắng và ký tự lỗi.')
add_body('Quyết định then chốt của nhóm nghiên cứu là chuyển đổi từ tiếp cận 8 biến sang bộ 3 biến cốt lõi: Date (Ngày), Ticker (Mã cổ phiếu), Close (Giá đóng cửa chốt phiên).')

add_callout('Luận cứ khoa học: (1) Ba biến giá Open, High, Low có tương quan tuyến tính > 0.98 với Close. Việc giữ cả 4 biến này sẽ gây ra hiện tượng Đa cộng tuyến hoàn hảo (Multicollinearity), làm méo sai số chuẩn và vô hiệu hóa ý nghĩa thống kê; (2) Close là mức giá bù trừ chính thức phản ánh đầy đủ thông tin thị trường, là đầu vào duy nhất cần và đủ để tính Tỷ suất sinh lợi (Return) và ma trận hiệp phương sai danh mục Markowitz; (3) Giúp loại bỏ hơn 300,000 ô dữ liệu rác ở các cột phụ, giảm dung lượng từ 57 MB xuống 19 MB và tăng tốc độ tính toán gấp 4 lần.', title='VÌ SAO CHỌN 3 BIẾN [Date, Ticker, Close]?')

# PHẦN 2: BẢNG KIỂM TOÁN CHẤT LƯỢNG
add_heading_1('PHẦN 2: BẢNG KIỂM TOÁN CHẤT LƯỢNG DỮ LIỆU BAN ĐẦU (DATA AUDIT)')
add_body('Kết quả rà soát tự động trước khi làm sạch:')

tbl = doc.add_table(rows=1, cols=4)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs = ['Tên biến', 'Số dòng khuyết thiếu', 'Tỷ lệ (%)', 'Dấu hiệu "dữ liệu bẩn" (Dirty Data)']
hdr_cells = tbl.rows[0].cells
for i, h in enumerate(hdrs):
    hdr_cells[i].text = h
    set_cell_background(hdr_cells[i], '1B365D')
    set_cell_margins(hdr_cells[i], top=80, bottom=80, left=60, right=60)
    p = hdr_cells[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

audit_data = [
    ('Date', '44,022 dòng', '7.07%', 'Chứa 17,283 ký tự rác ("?", "-"), lẫn lộn định dạng YYYY-MM-DD và YYYY/MM/DD.'),
    ('Ticker', '0 dòng', '0.00%', 'Có 50,172 dòng (8.06%) dính khoảng trắng đầu/cuối, làm 503 mã cổ phiếu bị hiểu lầm thành 1,509 mã ảo.'),
    ('Close', '54,928 dòng', '8.83%', 'Có 84,690 ô dính đơn vị đo (USD, VND, kg, %, đ), dùng dấu phẩy thay vì dấu chấm, dính 13,794 dòng mang mã lỗi -1 và giá trị âm.')
]

for row_idx, data in enumerate(audit_data):
    row_cells = tbl.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=65, bottom=65, left=60, right=60)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(6)

# PHẦN 3: 6 BƯỚC LÀM SẠCH CHI TIẾT
add_heading_1('PHẦN 3: CHI TIẾT 6 BƯỚC THỰC HIỆN TIỀN XỬ LÝ & LÀM SẠCH')

add_heading_2('Bước 1: Chuẩn hóa cột Mã cổ phiếu (Ticker)')
add_bullet('Lỗi phát hiện: Khoảng trắng thừa dạng " A", "AAPL ", "  A" khiến hệ thống hiểu là các thực thể khác nhau, phân mảnh 503 mã gốc thành 1,509 mã ảo.')
add_bullet('Thao tác kỹ thuật: Sử dụng hàm .str.strip() bóc tách khoảng trắng hai đầu.')
add_bullet('Mã thực thi Python: df["Ticker"] = df["Ticker"].astype(str).str.strip()')
add_bullet('Kết quả: Toàn bộ 1,509 mã ảo được quy tụ chính xác về đúng 503 mã cổ phiếu chuẩn của rổ S&P 500.')

add_heading_2('Bước 2: Chuẩn hóa cột Thời gian (Date)')
add_bullet('Lỗi phát hiện: Trộn lẫn dấu "/" và "-", chứa ký tự "?" và "-", cùng 44,022 quan sát khuyết trống hoàn toàn.')
add_bullet('Thao tác kỹ thuật: Đồng bộ ký tự ngăn cách sang "-", đưa các ký tự rác về NaN, chuyển đổi kiểu dữ liệu datetime64 bằng pd.to_datetime(..., errors="coerce").')
add_bullet('Loại bỏ dòng mất ngày: Trong phân tích chuỗi thời gian, quan sát không có nhãn thời gian là vô giá trị vì không thể ghép cặp chuỗi lợi suất.')
add_bullet('Mã thực thi Python: df["Date"] = pd.to_datetime(df["Date"].astype(str).str.replace("/", "-").replace(["-", "?", "nan"], np.nan), errors="coerce"); df = df.dropna(subset=["Date"])')

add_heading_2('Bước 3: Bóc tách tạp chất đo lường và làm sạch giá trị cột Close')
add_bullet('Lỗi phát hiện: 84,690 dòng bị gắn đuôi đơn vị "USD", "VND", "kg", "%", "đ", sử dụng dấu phẩy thập phân kiểu Việt Nam ("149,68"), xuất hiện giá trị âm và mã hóa lỗi -1.')
add_bullet('Lý do kinh tế lượng: Cổ phiếu có nguyên tắc trách nhiệm hữu hạn, thị giá không bao giờ âm. Nếu để số âm, khi tính tỷ suất lợi nhuận logarit r_t = ln(Close_t / Close_{t-1}) sẽ gây lỗi toán học (không tồn tại log số âm).')
add_bullet('Thao tác kỹ thuật: Bóc tách xóa sạch toàn bộ ký tự đơn vị, thay dấu "," thành ".", ép kiểu sang float64. Các giá trị <= 0, giá trị -1 và 9999 được gán thành NaN.')

add_heading_2('Bước 4: Sắp xếp cấu trúc Dữ liệu bảng (Panel Data Time-Series)')
add_bullet('Ý nghĩa phương pháp: Nhóm dữ liệu theo từng mã cổ phiếu độc lập và sắp xếp đơn điệu theo trục thời gian tăng dần từ 2021 đến 2026.')
add_bullet('Mã thực thi Python: df = df.sort_values(by=["Ticker", "Date"]).reset_index(drop=True)')
add_bullet('Kết quả: Đảm bảo chuỗi dữ liệu của từng công ty được phân tách rạch ròi, ngăn chặn hiện tượng tính nhầm lợi suất chéo giữa 2 mã cổ phiếu.')

add_heading_2('Bước 5: Lọc nhiễu ngoại lai bất thường (Outlier Detection - Median Filter)')
add_bullet('Lỗi phát hiện: Nhiều dòng bị lỗi nhảy dấu thập phân đột ngột (lỗi nhân 10x, 100x hoặc chia nhầm do lỗi hệ thống).')
add_bullet('Thao tác kỹ thuật: Tính giá trung vị (Median) theo từng mã cổ phiếu. Nhận diện các giá trị bất thường nằm ngoài khoảng [Median/3, 3*Median] và gán về NaN.')
add_bullet('Kết quả: Đã khoanh vùng và làm sạch 15,584 dòng ngoại lai phi thực tế.')

add_heading_2('Bước 6: Lấp đầy dữ liệu khuyết thiếu bằng kỹ thuật Forward Fill (ffill)')
add_bullet('Vì sao không điền Mean: Giá cổ phiếu là chuỗi bước đi ngẫu nhiên (Random Walk). Điền giá trị trung bình sẽ triệt tiêu độ biến động tự nhiên và bóp méo ma trận hiệp phương sai.')
add_bullet('Giải pháp chuẩn: Áp dụng Forward Fill (ffill) theo từng Ticker: df["Close"] = df.groupby("Ticker")["Close"].ffill().')
add_bullet('Ý nghĩa kinh tế: Nếu phiên hôm nay không có dữ liệu giao dịch mới, giá đóng cửa hợp lý nhất chính là giá chốt phiên hợp lệ gần nhất ngay trước đó.')
add_bullet('Xử lý đầu chuỗi: Loại bỏ những dòng khuyết ở đầu chuỗi không có dữ liệu phía trước để ffill.')

# PHẦN 4: KẾT QUẢ ĐẠT ĐƯỢC
add_heading_1('PHẦN 4: TỔNG KẾT KẾT QUẢ VÀ TỆP DỮ LIỆU ĐẦU RA')

res_tbl = doc.add_table(rows=1, cols=3)
res_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
hdrs_r = ['Chỉ tiêu', 'Trước khi làm sạch (Raw)', 'Sau khi làm sạch (Clean)']
hdr_r_cells = res_tbl.rows[0].cells
for i, h in enumerate(hdrs_r):
    hdr_r_cells[i].text = h
    set_cell_background(hdr_r_cells[i], '1B365D')
    set_cell_margins(hdr_r_cells[i], top=80, bottom=80, left=70, right=70)
    p = hdr_r_cells[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

res_data = [
    ('Tổng số quan sát (Dòng)', '622,243 dòng', '560,103 dòng (Tỷ lệ sử dụng đạt 90.01%)'),
    ('Số cột thuộc tính', '8 cột (nhiều cột rác, đa cộng tuyến)', '3 cột chuẩn mực [Date, Ticker, Close]'),
    ('Số lượng mã cổ phiếu', '1,509 mã ảo (do lỗi khoảng trắng)', 'Đúng 503 mã cổ phiếu S&P 500 thực tế'),
    ('Kiểu dữ liệu cột Close', 'Object / String (dính đơn vị, phẩy, âm)', 'Float64 (Số thực sạch, sẵn sàng tính toán)'),
    ('Dung lượng tệp lưu trữ', '~57.06 MB (File thô)', '~19.21 MB (data_cleaned_SP500.csv)'),
    ('Trạng thái sẵn sàng', 'Không thể tính toán do lỗi cú pháp', 'Hoàn tất tính Lợi suất & Danh mục Markowitz')
]

for row_idx, data in enumerate(res_data):
    row_cells = res_tbl.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=65, bottom=65, left=70, right=70)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(10)

out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Quy_trinh_lam_sach_du_lieu.docx')
doc.save(out_file)
print(f"✅ Đã tạo thành công file: {out_file}")

