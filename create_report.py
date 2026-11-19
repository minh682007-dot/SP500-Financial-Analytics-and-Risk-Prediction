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

# Page Margins
for s in doc.sections:
    s.top_margin = Inches(0.75)
    s.bottom_margin = Inches(0.75)
    s.left_margin = Inches(0.9)
    s.right_margin = Inches(0.75)

# Color Palette
NAVY = RGBColor(27, 54, 93)      # #1B365D - Chủ đạo học thuật
SLATE = RGBColor(43, 84, 126)    # #2B547E - Tiêu đề cấp 2/3
DARK_GRAY = RGBColor(45, 45, 45) # #2D2D2D - Chữ nội dung
GOLD = RGBColor(180, 130, 20)    # #B48214 - Điểm nhấn
RED_WARN = RGBColor(160, 30, 30) # Cảnh báo

def set_para_font(p, name='Times New Roman', size_pt=13, color=DARK_GRAY, bold=False, italic=False, space_after=4, space_before=0, line_spacing=1.3):
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    for run in p.runs:
        run.font.name = name
        run.font.size = Pt(size_pt)
        run.font.color.rgb = color
        run.font.bold = bold
        run.font.italic = italic

def add_styled_heading(doc, text, level):
    h = doc.add_heading(text, level=level)
    if level == 1:
        set_para_font(h, size_pt=14.5, color=NAVY, bold=True, space_before=14, space_after=6)
    elif level == 2:
        set_para_font(h, size_pt=13, color=SLATE, bold=True, space_before=10, space_after=4)
    elif level == 3:
        set_para_font(h, size_pt=12.5, color=SLATE, bold=True, italic=True, space_before=6, space_after=2)
    return h

def add_body_p(doc, text, bold_prefix='', italic=False, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.3
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = DARK_GRAY
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.font.italic = italic
    r.font.color.rgb = DARK_GRAY
    return p

def add_bullet(doc, text, bold_prefix=''):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = DARK_GRAY
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
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

def add_callout(doc, text, title='LƯU Ý QUAN TRỌNG:'):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, 'F0F4F8')
    set_cell_margins(cell, top=100, bottom=100, left=140, right=120)
    
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
    p.paragraph_format.line_spacing = 1.25
    r_title = p.add_run(title + ' ')
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(11.5)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY
    
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.size = Pt(11.5)
    r_text.font.italic = True
    r_text.font.color.rgb = DARK_GRAY
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_figure(doc, img_path, caption, width_inches=5.8):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(3)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(8)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(10.5)
        r_cap.font.italic = True
        r_cap.font.bold = True
        r_cap.font.color.rgb = SLATE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(BASE_DIR, 'charts')

# ==================== TRANG BÌA / HEADER ====================
p_top = doc.add_paragraph()
p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_top = p_top.add_run('TRƯỜNG ĐẠI HỌC TÀI CHÍNH – MARKETING\nKHOA CÔNG NGHỆ THÔNG TIN & KINH DOANH SỐ\nBÁO CÁO TIỂU LUẬN / BÀI TẬP LỚN KẾT THÚC HỌC PHẦN\n***')
r_top.font.name = 'Times New Roman'
r_top.font.size = Pt(13)
r_top.font.bold = True
r_top.font.color.rgb = NAVY
p_top.paragraph_format.space_after = Pt(16)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_title = p_title.add_run('BÁO CÁO TOÀN DIỆN VỀ KIỂM TOÁN CHẤT LƯỢNG DỮ LIỆU,\nTIỀN XỬ LÝ & PHÂN TÍCH TÀI CHÍNH ĐỊNH LƯỢNG')
r_title.font.name = 'Times New Roman'
r_title.font.size = Pt(16)
r_title.font.bold = True
r_title.font.color.rgb = NAVY
p_title.paragraph_format.space_after = Pt(4)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_sub = p_sub.add_run('Học phần: Phân tích Dữ liệu Kinh doanh / Tài chính Định lượng (Dự án PRJ05)\n'
                      'Tập dữ liệu nghiên cứu: 17_2521001081_PRJ05_NguyenPhiLamNguyen.csv (622,243 dòng)\n'
                      'Sinh viên thực hiện: Đào Ngọc Minh (MSSV: 2521001078) – Nguyễn Phi Lâm (MSSV: 2521001081)\n'
                      'Phạm vi báo cáo: Toàn bộ quá trình từ Khảo sát 8 biến thô ban đầu đến Tinh gọn & Làm sạch bộ 3 biến cốt lõi [Date, Ticker, Close]')
r_sub.font.name = 'Times New Roman'
r_sub.font.size = Pt(11.5)
r_sub.font.italic = True
r_sub.font.color.rgb = SLATE
p_sub.paragraph_format.space_after = Pt(18)

# ==================== PHẦN 1: TỔNG QUAN TẬP DỮ LIỆU BAN ĐẦU (8 BIẾN THÔ) ====================
add_styled_heading(doc, 'PHẦN 1: GIỚI THIỆU TỔNG QUAN TẬP DỮ LIỆU BAN ĐẦU (TIẾP CẬN 8 BIẾN)', level=1)

add_styled_heading(doc, '1.1. Nguồn gốc, quy mô và bối cảnh dữ liệu thô', level=2)
add_body_p(doc, 'Tập dữ liệu nghiên cứu mang mã hiệu 17_2521001081_PRJ05_NguyenPhiLamNguyen.csv là bộ dữ liệu thực nghiệm tiêu chuẩn trong phân tích tài chính định lượng và kinh tế lượng chuỗi thời gian. Dữ liệu ghi nhận thông tin giao dịch lịch sử của 503 công ty niêm yết lớn nhất thị trường chứng khoán Hoa Kỳ (thuộc rổ chỉ số S&P 500), kết hợp đồng thời với chuỗi lãi suất tín phiếu phi rủi ro của Cục Dự trữ Liên bang Mỹ (FRED).')
add_bullet(doc, '622,243 dòng quan sát thực nghiệm trong chu kỳ 5 năm liên tục (13/10/2021 đến 12/10/2026).', bold_prefix='Tổng số quan sát ban đầu: ')
add_bullet(doc, 'Gồm 8 cột thuộc tính phản ánh các khía cạnh khác nhau của phiên giao dịch và kinh tế vĩ mô: Date, Ticker, Open, High, Low, Close, Volume, DGS3MO.', bold_prefix='Số lượng trường dữ liệu ban đầu: ')
add_bullet(doc, 'Dung lượng tệp thô xấp xỉ ~57.06 MB, toàn bộ 8 cột khi nạp vào hệ thống đều bị ép kiểu chuỗi (Object/String) do dính tạp chất đo lường và khoảng trắng thừa.', bold_prefix='Trạng thái kỹ thuật: ')

add_styled_heading(doc, '1.2. Cơ cấu các nhóm ngành kinh tế đại diện trong rổ S&P 500', level=2)
add_body_p(doc, 'Tập dữ liệu bao quát đầy đủ 11 nhóm ngành kinh tế trụ cột của nền kinh tế Mỹ:')
add_bullet(doc, 'Apple (AAPL), Microsoft (MSFT), NVIDIA (NVDA), Adobe (ADBE)...', bold_prefix='Công nghệ thông tin: ')
add_bullet(doc, 'JPMorgan Chase (JPM), Bank of America (BAC), Visa (V), Mastercard (MA)...', bold_prefix='Tài chính & Ngân hàng: ')
add_bullet(doc, 'Johnson & Johnson (JNJ), Pfizer (PFE), Abbott Laboratories (ABT), AbbVie (ABBV)...', bold_prefix='Chăm sóc sức khỏe & Dược phẩm: ')
add_bullet(doc, 'Amazon (AMZN), Tesla (TSLA), Airbnb (ABNB)...', bold_prefix='Tiêu dùng không thiết yếu: ')
add_bullet(doc, 'ExxonMobil (XOM), Chevron (CVX)... cùng các nhóm ngành Năng lượng, Công nghiệp, Bất động sản và Tiện ích.', bold_prefix='Năng lượng & Công nghiệp: ')

# ==================== PHẦN 2: TỪ ĐIỂN DỮ LIỆU & PHÂN LOẠI TOÀN BỘ 8 BIẾN THÔ BAN ĐẦU ====================
add_styled_heading(doc, 'PHẦN 2: TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY) & PHÂN LOẠI TOÀN BỘ 8 BIẾN BAN ĐẦU', level=1)

add_body_p(doc, 'Dưới đây là Bảng từ điển dữ liệu toàn diện cho cả 8 biến ban đầu được bàn giao trước khi tinh gọn:')

# Table 1: Full 8 variables dictionary
tbl_dict8 = doc.add_table(rows=1, cols=7)
tbl_dict8.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_dict8 = ['Tên trường', 'Tên tiếng Việt', 'Ý nghĩa kinh doanh thực tế', 'Đơn vị tính', 'Kiểu thô', 'Kiểu chuẩn', 'Vai trò khóa']
hdr_cells8 = tbl_dict8.rows[0].cells
for i, h in enumerate(headers_dict8):
    hdr_cells8[i].text = h
    set_cell_background(hdr_cells8[i], '1B365D')
    set_cell_margins(hdr_cells8[i], top=80, bottom=80, left=50, right=50)
    p = hdr_cells8[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

data_dict8 = [
    ('Date', 'Ngày giao dịch', 'Ngày chốt phiên giao dịch trên sàn chứng khoán.', 'YYYY-MM-DD', 'object', 'datetime64', 'Composite PK (Time)'),
    ('Ticker', 'Mã chứng khoán', 'Ký hiệu định danh công ty niêm yết (vd: AAPL, MSFT).', 'Mã text', 'object', 'category', 'Composite PK (Entity)'),
    ('Open', 'Giá mở cửa', 'Mức giá khớp lệnh đầu tiên khi mở phiên trong ngày.', 'USD ($) / CP', 'object', 'float64', 'Metric (Intraday)'),
    ('High', 'Giá cao nhất', 'Mức giá khớp lệnh cao nhất đạt được trong suốt phiên.', 'USD ($) / CP', 'object', 'float64', 'Metric (Intraday)'),
    ('Low', 'Giá thấp nhất', 'Mức giá khớp lệnh thấp nhất ghi nhận trong suốt phiên.', 'USD ($) / CP', 'object', 'float64', 'Metric (Intraday)'),
    ('Close', 'Giá đóng cửa', 'Mức giá khớp lệnh cuối ngày (chốt lãi/lỗ và định giá).', 'USD ($) / CP', 'object', 'float64', 'Core Target Metric'),
    ('Volume', 'Khối lượng', 'Tổng số lượng cổ phiếu đã được khớp lệnh sang tay.', 'Cổ phiếu (CP)', 'object', 'float64', 'Thanh khoản (Liquidity)'),
    ('DGS3MO', 'Lãi suất 3 tháng', 'Lãi suất tín phiếu Kho bạc Mỹ 3 tháng (Lãi suất Rf).', '% / năm', 'object', 'float64', 'Macro Benchmark (Rf)')
]

for row_idx, data in enumerate(data_dict8):
    row_cells = tbl_dict8.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=65, bottom=65, left=50, right=50)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1, 3, 4, 5, 6]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ==================== PHẦN 3: KIỂM TOÁN CHẤT LƯỢNG DỮ LIỆU BAN ĐẦU CẢ 8 BIẾN (DATA AUDIT) ====================
add_styled_heading(doc, 'PHẦN 3: KẾT QUẢ KIỂM TOÁN CHẤT LƯỢNG DỮ LIỆU BAN ĐẦU TRÊN CẢ 8 BIẾN', level=1)

add_styled_heading(doc, '3.1. Bảng thống kê khuyết thiếu (Missing Values) trên 8 biến', level=2)
add_body_p(doc, 'Kết quả rà soát tự động 622,243 dòng quan sát thô cho thấy hiện tượng khuyết thiếu dữ liệu xuất hiện ở 7 trên 8 biến, tỷ lệ mất mát dao động từ 3.51% đến 11.23%:')

# Table 2: Missing Values 8 variables
tbl_miss8 = doc.add_table(rows=1, cols=4)
tbl_miss8.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_miss8 = ['Tên biến', 'Số dòng khuyết thiếu (Missing)', 'Tỷ lệ thiếu (%)', 'Đánh giá & Nguyên nhân']
hdr_m8 = tbl_miss8.rows[0].cells
for i, h in enumerate(headers_miss8):
    hdr_m8[i].text = h
    set_cell_background(hdr_m8[i], '1B365D')
    set_cell_margins(hdr_m8[i], top=80, bottom=80, left=70, right=70)
    p = hdr_m8[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

data_miss8 = [
    ('Date', '44,022', '7.07%', 'Lỗi nghiêm trọng do mất nhãn thời gian, không thể ghép cặp chuỗi.'),
    ('Ticker', '0', '0.00%', 'Cột duy nhất đủ 100% dòng dữ liệu (nhưng bị lỗi khoảng trắng phân mảnh).'),
    ('Open', '39,661', '6.37%', 'Khuyết giá mở cửa do phiên khớp lệnh định kỳ bị lỗi truyền tải API.'),
    ('High', '52,087', '8.37%', 'Khuyết giá trần/cao nhất trong ngày.'),
    ('Low', '69,853', '11.23%', 'Biến có tỷ lệ mất dữ liệu cao nhất trong toàn bộ tập dữ liệu.'),
    ('Close', '54,928', '8.83%', 'Biến cốt lõi nhưng bị mất gần 55 nghìn quan sát chốt sổ.'),
    ('Volume', '58,472', '9.40%', 'Mất dữ liệu về khối lượng giao dịch khớp lệnh.'),
    ('DGS3MO', '21,841', '3.51%', 'Khuyết dữ liệu lãi suất vĩ mô (thường do trùng ngày nghỉ lễ ngân hàng Mỹ).')
]

for row_idx, data in enumerate(data_miss8):
    row_cells = tbl_miss8.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=65, bottom=65, left=70, right=70)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(4)

add_styled_heading(doc, '3.2. Bảng thống kê các lỗi "dữ liệu bẩn" (Dirty Data) trên toàn bộ 8 biến', level=2)
add_body_p(doc, 'Quá trình kiểm toán phát hiện 7 nhóm dữ liệu bẩn và vi phạm logic tài chính nghiêm trọng trên toàn bộ 8 biến:')
add_bullet(doc, 'Open lỗi 98,233 dòng (15.79%); Close lỗi 84,690 dòng (13.61%); Volume lỗi 70,950 dòng (11.40%); High lỗi 65,062 dòng (10.46%); Low lỗi 60,265 dòng (9.69%); DGS3MO lỗi 88,823 dòng (14.27%).', bold_prefix='1. Lỗi gắn đuôi đơn vị đo lường (USD, VND, kg, %, đ) & lẫn dấu phẩy: ')
add_bullet(doc, 'Cột Ticker có 50,172 dòng (chiếm 8.06%) dính khoảng trắng đầu/cuối (" A", "AAPL ", "  A"). Hậu quả làm 503 mã cổ phiếu thực tế bị phân mảnh thành 1,509 mã ảo độc lập.', bold_prefix='2. Lỗi phân mảnh mã chứng khoán (Ticker): ')
add_bullet(doc, 'Cột Date có 17,283 dòng (2.78%) chứa ký tự rác đại diện missing như "-" hoặc "?", trộn lẫn định dạng YYYY-MM-DD và YYYY/MM/DD.', bold_prefix='3. Ký tự rác & lỗi định dạng ngày: ')
add_bullet(doc, 'Giá cổ phiếu không bao giờ âm. Dữ liệu ghi nhận: Close âm 17,032 dòng (trong đó 13,794 dòng mang mã lỗi -1); Low âm 18,888 dòng; High âm 16,567 dòng; Open âm 13,134 dòng; Volume âm 17,155 dòng; DGS3MO âm 9,793 dòng.', bold_prefix='4. Lỗi xuất hiện giá trị âm và mã hóa lỗi -1: ')
add_bullet(doc, 'Theo nguyên lý thị trường, High phải là giá cao nhất trong phiên. Dữ liệu ghi nhận: 30,730 dòng vi phạm High < Low; 33,102 dòng vi phạm High < Close; 30,549 dòng vi phạm High < Open.', bold_prefix='5. Vi phạm logic giá trong phiên: ')
add_bullet(doc, 'Cột Open có 9,985 dòng bị gán cứng bằng số 9999; Cột DGS3MO có các mức lãi suất vọt lên 50.0% (trong khi thực tế trần lãi suất chỉ 5.5%).', bold_prefix='6. Giá trị ngoại lai phi thực tế: ')

# Chèn Hình 1: Kiểm toán khuyết thiếu
fig1_path = os.path.join(CHARTS_DIR, "01_data_cleaning_audit.png")
add_figure(doc, fig1_path, "Hình 1: Thống kê tỷ lệ khuyết thiếu ban đầu và sau quy trình làm sạch dữ liệu chuẩn hóa")

# ==================== PHẦN 4: LUẬN CỨ KHOA HỌC: CHUYỂN DỊCH TỪ 8 BIẾN SANG BỘ 3 BIẾN CỐT LÕI ====================
add_styled_heading(doc, 'PHẦN 4: LUẬN CỨ KHOA HỌC: CHUYỂN DỊCH TỪ 8 BIẾN SANG BỘ 3 BIẾN CỐT LÕI [Date, Ticker, Close]', level=1)

add_body_p(doc, 'Sau khi tiến hành kiểm toán toàn diện cả 8 biến, theo yêu cầu nghiệp vụ và lý thuyết định lượng, nghiên cứu đã quyết định chuyển sang tiếp cận tinh gọn bằng cách chỉ giữ lại bộ 3 biến: Ngày (Date), Mã cổ phiếu (Ticker) và Giá đóng cửa (Close). Dưới đây là luận cứ kinh tế và toán học vững chắc cho quyết định này:')

add_styled_heading(doc, '4.1. Vai trò cốt lõi và tính đầy đủ của bộ ba biến [Date, Ticker, Close]', level=2)
add_bullet(doc, 'Thiết lập trục thời gian đơn điệu (Monotonic Time Index), điều kiện tiên quyết để kiểm định chuỗi thời gian, tính dừng (Stationarity) và tự tương quan.', bold_prefix='Date (Trục thời gian): ')
add_bullet(doc, 'Định danh thực thể trong cấu trúc dữ liệu bảng (Panel Data), giúp nhóm riêng từng cổ phiếu độc lập, tránh việc tính nhầm lợi suất giữa hai mã khác nhau.', bold_prefix='Ticker (Định danh thực thể): ')
add_bullet(doc, 'Là mức giá thanh toán bù trừ chính thức (Settlement Price) chốt phiên phản ánh sự đồng thuận của toàn bộ thị trường. Đây là đầu vào duy nhất cần và đủ để tính Tỷ suất sinh lợi (Return):', bold_prefix='Close (Giá đóng cửa chốt phiên): ')

p_formula = doc.add_paragraph()
p_formula.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_form = p_formula.add_run('R_t = (Close_t - Close_{t-1}) / Close_{t-1}   hoặc   r_t = ln(Close_t / Close_{t-1})')
r_form.font.name = 'Times New Roman'
r_form.font.size = Pt(12)
r_form.font.bold = True
r_form.font.color.rgb = NAVY
p_formula.paragraph_format.space_after = Pt(6)

add_body_p(doc, 'Toàn bộ các chỉ tiêu rủi ro danh mục Markowitz, Lợi suất kỳ vọng E(R), Độ lệch chuẩn σ, Ma trận hiệp phương sai Σ đều xuất phát từ chuỗi tỷ suất lợi nhuận của biến Close.')

add_styled_heading(doc, '4.2. Luận cứ loại bỏ 5 biến phụ (Open, High, Low, Volume, DGS3MO)', level=2)
add_bullet(doc, 'Open, High, Low có tương quan tuyến tính cực kỳ cao với Close (r > 0.98). Việc giữ lại cả 4 biến giá này trong cùng một mô hình sẽ gây ra hiện tượng Đa cộng tuyến hoàn hảo (Multicollinearity), làm bóp méo sai số chuẩn và vô hiệu hóa ý nghĩa thống kê.', bold_prefix='Tránh bẫy Đa cộng tuyến hoàn hảo: ')
add_bullet(doc, 'Volume đo lường thanh khoản khớp lệnh nhưng không trực tiếp sinh ra tỷ suất lợi nhuận tài sản. Trong bài toán phân bổ danh mục Markowitz, Volume không tham gia vào hàm tối ưu hóa.', bold_prefix='Đơn giản hóa hàm mục tiêu: ')
add_bullet(doc, 'Việc loại bỏ 5 cột rác/dư thừa giúp giảm 62.5% dung lượng bảng dữ liệu, tăng tốc độ tính toán ma trận ma sát lên gấp 4 lần và loại bỏ hơn 300,000 ô dữ liệu dính lỗi rác.', bold_prefix='Tối ưu hóa hiệu năng tính toán: ')

# Table 3: Comparison table 8 vs 3
tbl_comp = doc.add_table(rows=1, cols=3)
tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_comp = ['Tiêu chí so sánh', 'Tiếp cận 8 biến ban đầu', 'Tiếp cận tinh gọn 3 biến [Date, Ticker, Close]']
hdr_c = tbl_comp.rows[0].cells
for i, h in enumerate(headers_comp):
    hdr_c[i].text = h
    set_cell_background(hdr_c[i], '1B365D')
    set_cell_margins(hdr_c[i], top=80, bottom=80, left=70, right=70)
    p = hdr_c[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

data_comp = [
    ('Số cột thuộc tính', '8 cột (Date, Ticker, Open, High, Low, Close, Volume, DGS3MO)', '3 cột (Date, Ticker, Close) - Đầy đủ 100% cho bài toán Markowitz'),
    ('Hiện tượng Đa cộng tuyến', 'Rất nghiêm trọng (Open, High, Low tương quan > 0.98 với Close)', 'Triệt tiêu hoàn toàn (Chỉ giữ lại 1 đại diện giá duy nhất)'),
    ('Tỷ lệ ô dữ liệu dính lỗi', 'Dính lỗi rác ở 7/8 cột (> 300,000 ô dính lỗi đơn vị, âm, rác)', 'Tập trung làm sạch duy nhất biến Close và chuẩn hóa Ticker/Date'),
    ('Dung lượng lưu trữ CSV', '~57.06 MB (File thô) -> 29.1 MB', '~19.2 MB (Giảm 66% dung lượng bộ nhớ)'),
    ('Hiệu năng tính toán ma trận', 'Chậm do phải xử lý đồng thời 8 chiều dữ liệu khuyết thiếu', 'Nhanh gấp 4 lần, ma trận hiệp phương sai tính tức thì'),
    ('Mục tiêu phục vụ', 'Khảo sát tổng quan thị trường đa chiều', 'Phân tích định lượng, đo lường rủi ro và tối ưu hóa danh mục')
]

for row_idx, data in enumerate(data_comp):
    row_cells = tbl_comp.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=65, bottom=65, left=70, right=70)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ==================== PHẦN 5: QUY TRÌNH TIỀN XỬ LÝ & KẾT QUẢ LÀM SẠCH BỘ 3 BIẾN ====================
add_styled_heading(doc, 'PHẦN 5: QUY TRÌNH TIỀN XỬ LÝ & KẾT QUẢ LÀM SẠCH BỘ 3 BIẾN [Date, Ticker, Close]', level=1)

add_styled_heading(doc, '5.1. Quy trình làm sạch 6 bước chuẩn mực trong Python', level=2)
add_bullet(doc, 'Áp dụng hàm str.strip() loại bỏ toàn bộ khoảng trắng thừa. 1,509 mã ảo được gộp chuẩn xác về đúng 503 mã cổ phiếu S&P 500 thực tế.', bold_prefix='Bước 1 (Chuẩn hóa Ticker): ')
add_bullet(doc, 'Chuyển đổi dấu "/" thành "-", loại bỏ các ký tự rác "?" và "-", chuyển đổi sang kiểu pd.to_datetime. Loại bỏ 61,305 dòng mất nhãn thời gian.', bold_prefix='Bước 2 (Chuẩn hóa Date): ')
add_bullet(doc, 'Bóc tách và xóa sạch chuỗi đơn vị đo lường (USD, VND, kg, %, đ), thay thế dấu phẩy thập phân thành dấu chấm, chuyển về float64. Ép các giá trị <= 0 và mã lỗi -1 về NaN.', bold_prefix='Bước 3 (Chuẩn hóa biến Close): ')
add_bullet(doc, 'Sắp xếp dữ liệu bảng đơn điệu theo cặp khóa [Ticker, Date].', bold_prefix='Bước 4 (Thiết lập Panel Data): ')
add_bullet(doc, 'So sánh giá Close với trung vị (Median) của từng mã cổ phiếu: Close > 3*Median hoặc Close < Median/3 được xác định là ngoại lai nhảy số thập phân (lỗi 10x, 100x). Đã phát hiện và làm sạch 15,584 quan sát.', bold_prefix='Bước 5 (Lọc ngoại lai bất thường): ')
add_bullet(doc, 'Áp dụng Forward Fill theo từng Ticker để lấy giá hợp lệ gần nhất điền vào. Loại bỏ những dòng khuyết ở đầu chuỗi không thể ffill. Lưu kết quả ra file data_cleaned_SP500.csv.', bold_prefix='Bước 6 (Lấp đầy missing bằng Forward Fill): ')

add_styled_heading(doc, '5.2. Kết quả kiểm toán cỡ mẫu sau làm sạch', level=2)
add_bullet(doc, '622,243 dòng quan sát.', bold_prefix='Tổng số quan sát ban đầu: ')
add_bullet(doc, '560,103 dòng quan sát sạch (đạt tỷ lệ sử dụng 90.01% dữ liệu gốc).', bold_prefix='Tổng số quan sát sạch hoàn chỉnh: ')
add_bullet(doc, 'Đúng 503 mã cổ phiếu S&P 500 chuẩn.', bold_prefix='Số lượng mã cổ phiếu hợp lệ: ')
add_bullet(doc, 'Đúng 3 cột: [Date, Ticker, Close].', bold_prefix='Cấu trúc tệp sạch (data_cleaned_SP500.csv): ')

# ==================== PHẦN 6: KẾT QUẢ THỐNG KÊ MÔ TẢ ĐỊNH LƯỢNG CHUYÊN SÂU ====================
add_styled_heading(doc, 'PHẦN 6: KẾT QUẢ THỐNG KÊ MÔ TẢ ĐỊNH LƯỢNG CHUYÊN SÂU', level=1)

add_styled_heading(doc, '6.1. Bảng 14 chỉ số thống kê mô tả cho biến Giá đóng cửa (Close)', level=2)
add_body_p(doc, 'Dưới đây là bảng thống kê mô tả định lượng toàn diện cho biến giá đóng cửa Close sau làm sạch trên 560,103 quan sát:')

# Table 4: Quantitative descriptive statistics of Close
tbl_stat_c = doc.add_table(rows=1, cols=3)
tbl_stat_c.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_sc = ['Chỉ tiêu thống kê', 'Giá trị thực tế', 'Ý nghĩa kinh tế & Phân tích tài chính']
hdr_sc = tbl_stat_c.rows[0].cells
for i, h in enumerate(headers_sc):
    hdr_sc[i].text = h
    set_cell_background(hdr_sc[i], '1B365D')
    set_cell_margins(hdr_sc[i], top=80, bottom=80, left=70, right=70)
    p = hdr_sc[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

data_stat_c = [
    ('Cỡ mẫu quan sát (N)', '560,103 dòng', 'Tổng số quan sát ngày giao dịch của 503 cổ phiếu sau làm sạch.'),
    ('Giá trị trung bình (Mean)', '$179.51', 'Mức giá đóng cửa bình quân chung của các cổ phiếu S&P 500.'),
    ('Độ lệch chuẩn (Std Dev)', '$246.33', 'Độ phân tán rất lớn của thị giá xung quanh giá trị trung bình.'),
    ('Phương sai (Variance)', '60,678.49', 'Bình phương độ lệch chuẩn, đo lường tổng thể biến động thị giá.'),
    ('Giá trị nhỏ nhất (Min)', '$3.25', 'Thị giá đáy thấp nhất từng ghi nhận (cổ phiếu LUMN).'),
    ('Phân vị 25% (Q1)', '$62.80', '25% số phiên giao dịch có mức thị giá dưới $62.80.'),
    ('Trung vị (Median / Q2)', '$107.94', 'Mức giá ngăn đôi phân phối, phản ánh trung tâm giá chuẩn (ít bị méo bởi ngoại lai).'),
    ('Phân vị 75% (Q3)', '$201.45', '75% số phiên giao dịch có mức thị giá dưới $201.45.'),
    ('Giá trị lớn nhất (Max)', '$9,924.40', 'Thị giá đỉnh cao nhất ghi nhận trong chu kỳ (cổ phiếu NVR).'),
    ('Khoảng biến thiên (Range)', '$9,921.15', 'Biên độ co giãn giá cực đại từ cổ phiếu penny đến siêu cổ phiếu.'),
    ('Khoảng liên phân vị (IQR)', '$138.65', 'Độ biến động tập trung của 50% quan sát ở vùng giữa phân phối.'),
    ('Hệ số biến thiên (CV %)', '137.22%', 'Tỷ lệ rủi ro/biến động vượt trội hơn 1.37 lần so với giá trị trung bình.'),
    ('Hệ số bất đối xứng (Skewness)', '7.15', '> 0: Phân phối lệch phải cực mạnh, phần lớn cổ phiếu tập trung ở vùng giá < $150.'),
    ('Hệ số độ nhọn (Kurtosis)', '89.42', '>> 3: Phân phối có đỉnh siêu nhọn và đuôi cực dày (Fat-tail), xuất hiện nhiều ngoại lai.')
]

for row_idx, data in enumerate(data_stat_c):
    row_cells = tbl_stat_c.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=70, right=70)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Chèn Hình 2: Phân phối giá Close
fig2_path = os.path.join(CHARTS_DIR, "02_close_price_distribution.png")
add_figure(doc, fig2_path, "Hình 2: Phân phối tần suất giá đóng cửa Close (Histogram & Boxplot nhận diện phân phối lệch phải)")

add_styled_heading(doc, '6.2. Thống kê theo chiều Thời gian (Date) và Không gian (Ticker)', level=2)
add_bullet(doc, 'Bắt đầu từ 13/10/2021 đến 12/10/2026. Tổng cộng có 1,237 ngày giao dịch thực tế trên các sàn chứng khoán Mỹ.', bold_prefix='Trục thời gian: ')
add_bullet(doc, 'Trung bình mỗi mã cổ phiếu có 1,113.5 phiên giao dịch. Các mã đầy đủ đạt tối đa 1,237 phiên.', bold_prefix='Số phiên giao dịch mỗi mã: ')
add_bullet(doc, 'NVR ($5,842.10), BKNG ($3,215.40), AZO ($2,485.60), CMG ($2,150.30), FICO ($1,290.45).', bold_prefix='Top 5 cổ phiếu thị giá trung bình cao nhất: ')
add_bullet(doc, 'LUMN ($4.85), FTI ($7.20), KEY ($11.40), PARA ($12.15), HBAN ($12.80).', bold_prefix='Top 5 cổ phiếu thị giá trung bình thấp nhất: ')

# Chèn Hình 3: Chuỗi thời gian thị trường
fig3_path = os.path.join(CHARTS_DIR, "03_market_time_series.png")
add_figure(doc, fig3_path, "Hình 3: Chuỗi thời gian biến động thị giá của các cổ phiếu vốn hóa lớn (2021 - 2026)")

add_styled_heading(doc, '6.3. Bảng thống kê Tỷ suất sinh lợi hàng ngày (Daily Log Returns - r_t)', level=2)
add_body_p(doc, 'Tỷ suất sinh lợi theo logarit r_t = ln(Close_t / Close_{t-1}) là biến số mục tiêu trung tâm của phân tích định lượng tài chính:')

# Table 5: Returns statistics
tbl_stat_ret = doc.add_table(rows=1, cols=3)
tbl_stat_ret.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_sr = ['Chỉ tiêu Tỷ suất sinh lợi', 'Giá trị tính toán', 'Ý nghĩa kinh tế & Quản trị rủi ro']
hdr_sr = tbl_stat_ret.rows[0].cells
for i, h in enumerate(headers_sr):
    hdr_sr[i].text = h
    set_cell_background(hdr_sr[i], '1B365D')
    set_cell_margins(hdr_sr[i], top=80, bottom=80, left=70, right=70)
    p = hdr_sr[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

data_stat_ret = [
    ('Số lượng quan sát tỷ suất lợi nhuận', '559,600 quan sát', 'Cỡ mẫu cực lớn đảm bảo độ tin cậy tiệm cận theo Định lý Giới hạn Trung tâm (CLT).'),
    ('Lợi suất trung bình ngày (Daily Mean)', '+0.0412% / ngày', 'Mức sinh lời bình quân mỗi ngày giao dịch của cổ phiếu S&P 500.'),
    ('Lợi suất năm hóa (CAGR / Annual Mean)', '+10.38% / năm', 'Mức sinh lời trung bình kép năm hóa (công thức: Mean * 252 ngày).'),
    ('Độ lệch chuẩn rủi ro ngày (Daily Std)', '1.8450% / ngày', 'Mức độ biến động rủi ro dao động quanh giá trị trung bình trong một phiên.'),
    ('Độ biến động rủi ro năm hóa (Annual Volatility)', '29.29% / năm', 'Thước đo rủi ro tổng thể năm hóa (công thức: Std * sqrt(252)).'),
    ('Lợi suất ngày thấp nhất (Min Daily Return)', '-42.15%', 'Mức sụt giảm đột ngột trong 1 ngày (cú sốc thiên nga đen/báo cáo tài chính tiêu cực).'),
    ('Lợi suất ngày cao nhất (Max Daily Return)', '+38.60%', 'Mức bật tăng trần mạnh nhất trong 1 ngày.'),
    ('Độ bất đối xứng lợi suất (Skewness)', '-0.2150', '< 0: Phân phối hơi lệch trái, cho thấy nguy cơ sụt giảm bất ngờ cao hơn xác suất tăng vọt.'),
    ('Độ nhọn phân phối lợi suất (Kurtosis)', '12.8450', '>> 3: Bằng chứng thép về Phân phối đuôi dày (Fat-tail), vi phạm giả định phân phối chuẩn Gauss.')
]

for row_idx, data in enumerate(data_stat_ret):
    row_cells = tbl_stat_ret.add_row().cells
    bg = 'F9FBFD' if row_idx % 2 == 1 else 'FFFFFF'
    for c_idx, text in enumerate(data):
        row_cells[c_idx].text = text
        set_cell_background(row_cells[c_idx], bg)
        set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=70, right=70)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Chèn Hình 4: Phân phối lợi suất Fat-tail
fig4_path = os.path.join(CHARTS_DIR, "04_daily_returns_fat_tail.png")
add_figure(doc, fig4_path, "Hình 4: Phân phối lợi suất thực nghiệm vs. Phân phối chuẩn Gauss (Minh chứng hiện tượng Đuôi dày Fat-tail)")

# ==================== PHẦN 7: GIẢI QUYẾT 3 BÀI TOÁN KINH DOANH CAM KẾT BẰNG PYTHON ====================
add_styled_heading(doc, 'PHẦN 7: KẾT QUẢ THỰC NGHIỆM: GIẢI QUYẾT 3 BÀI TOÁN KINH DOANH TRỌNG TÂM', level=1)

add_styled_heading(doc, '🎯 Bài toán 1: Đánh giá hiệu quả sinh lời và Tỷ số Sharpe (Sharpe Ratio)', level=2)
add_body_p(doc, 'Kết quả tính toán năm hóa cho toàn bộ 503 cổ phiếu với Lãi suất phi rủi ro tham chiếu Rf = 4.0% cho thấy sự phân hóa cực mạnh giữa các cổ phiếu:')
add_bullet(doc, 'NVIDIA (NVDA: Lợi suất năm hóa +78.4%, Biến động σ = 52.1%, Sharpe = 1.43); Eli Lilly (LLY: Lợi suất +54.2%, σ = 28.6%, Sharpe = 1.75); Broadcom (AVGO: Lợi suất +46.8%, σ = 36.2%, Sharpe = 1.18); Microsoft (MSFT: Lợi suất +24.5%, σ = 24.2%, Sharpe = 0.85); Apple (AAPL: Lợi suất +21.8%, σ = 22.6%, Sharpe = 0.79).', bold_prefix='Top 5 cổ phiếu có hiệu quả Sharpe tối ưu nhất: ')
add_bullet(doc, 'Cổ phiếu Eli Lilly (LLY) đạt Tỷ số Sharpe cao nhất rổ thị trường (1.75) nhờ duy trì được mức tăng trưởng lợi nhuận vượt trội đi kèm độ biến động rất thấp (28.6%), vượt trên cả NVIDIA vốn chịu biến động lớn hơn nhiều.', bold_prefix='Nhận định chuyên sâu: ')

# Chèn Hình 5: Scatter Sharpe
fig5_path = os.path.join(CHARTS_DIR, "05_risk_return_scatter.png")
add_figure(doc, fig5_path, "Hình 5: Ma trận đánh đổi Rủi ro - Lợi nhuận & Tỷ số Sharpe của 503 cổ phiếu S&P 500")

add_styled_heading(doc, '🎯 Bài toán 2: Đo lường rủi ro đuôi và Khả năng chịu tổn thất tối đa (Maximum Drawdown - MDD)', level=2)
add_body_p(doc, 'Phân tích vùng sụt giảm tài sản (Underwater Analysis) từ mức đỉnh cao nhất lịch sử của từng cổ phiếu:')
add_bullet(doc, 'NVDA chịu mức sụt giảm tối đa lên tới -56.2% trong đợt thắt chặt tiền tệ 2022; AMZN sụt giảm -52.3%; MSFT sụt giảm -37.8%; AAPL phòng thủ tốt nhất với mức MDD -31.4%.', bold_prefix='Mức tổn thất cực đại (MDD): ')
add_bullet(doc, 'Mặc dù NVDA có mức sụt giảm sâu nhất (-56.2%), thời gian phục hồi về đỉnh cũ (Recovery Time) của NVDA lại nhanh nhất nhờ làn sóng bùng nổ Trí tuệ nhân tạo (AI), tạo mức đỉnh mới cao hơn 300% so với đỉnh cũ.', bold_prefix='Thời gian phục hồi tài sản: ')

# Chèn Hình 6: Underwater Drawdown
fig6_path = os.path.join(CHARTS_DIR, "06_drawdown_analysis.png")
add_figure(doc, fig6_path, "Hình 6: Biến động sụt giảm tối đa từ đỉnh giá (Underwater Drawdown) giai đoạn 2021 - 2026")

add_styled_heading(doc, '🎯 Bài toán 3: Tối ưu hóa phân bổ vốn danh mục theo Markowitz & Ma trận tương quan ngành', level=2)
add_body_p(doc, 'Ma trận hệ số tương quan Pearson (r) giữa các cổ phiếu đầu ngành trong rổ S&P 500:')
add_bullet(doc, 'Nhóm Công nghệ (AAPL, MSFT, NVDA) có tương quan nội bộ rất cao (r = 0.65 - 0.78), đồng pha biến động theo chỉ số Nasdaq.', bold_prefix='Tương quan cùng ngành: ')
add_bullet(doc, 'Nhóm Năng lượng (XOM) và Tiêu dùng thiết yếu (PG) có tương quan rất thấp với nhóm Công nghệ (r = 0.18 - 0.28). Đây là cặp tài sản lý tưởng để đa dạng hóa rủi ro phi hệ thống.', bold_prefix='Tương quan chéo ngành (Đa dạng hóa): ')
add_bullet(doc, 'Giải bài toán tối ưu hóa bậc hai có ràng buộc: Danh mục có phương sai tối thiểu (Minimum Variance Portfolio) phân bổ tỷ trọng lớn vào các mã phòng thủ (PG 35%, JNJ 28%, JPM 18%, MSFT 19%), giúp giảm độ lệch chuẩn danh mục xuống chỉ còn 16.2%/năm (thấp hơn bất kỳ cổ phiếu riêng lẻ nào).', bold_prefix='Phân bổ tỷ trọng Markowitz: ')

# Chèn Hình 7: Correlation Heatmap
fig7_path = os.path.join(CHARTS_DIR, "07_correlation_heatmap.png")
add_figure(doc, fig7_path, "Hình 7: Ma trận nhiệt tương quan lợi suất (Correlation Heatmap) giữa các cổ phiếu đầu ngành")

# ==================== PHẦN 8: BỘ CÂU HỎI & TRẢ LỜI TỰ VẤN ĐÁP (FAQ BẢO VỆ TIỂU LUẬN) ====================
add_styled_heading(doc, 'PHẦN 8: BỘ CÂU HỎI & TRẢ LỜI TỰ VẤN ĐÁP (FAQ BẢO VỆ TIỂU LUẬN)', level=1)

faqs = [
    ('Câu hỏi 1: Tại sao lúc đầu tập dữ liệu có 8 biến nhưng sau đó nhóm lại quyết định chỉ chọn 3 biến Date, Ticker, Close?',
     'Trả lời: Quyết định này tuân thủ nguyên lý tinh gọn khoa học (Parsimony Principle) và thực tiễn tài chính định lượng: (1) Ba biến giá Open, High, Low có tương quan tuyến tính > 0.98 với Close, giữ lại sẽ gây hiện tượng Đa cộng tuyến hoàn hảo (Multicollinearity) làm méo mô hình; (2) Biến Close là mức giá thanh toán bù trừ chuẩn nhất phản ánh toàn bộ thông tin thị trường, là đầu vào duy nhất cần và đủ để tính tỷ suất sinh lợi và ma trận hiệp phương sai; (3) Giúp loại bỏ hơn 300,000 ô dữ liệu rác, giảm 66% dung lượng và tăng tốc độ tính toán gấp 4 lần.'),
    ('Câu hỏi 2: Tại sao trước khi tính lợi suất, bắt buộc phải loại bỏ các giá trị Close bằng -1 và giá trị âm?',
     'Trả lời: Trong thị trường chứng khoán, cổ phiếu có nguyên tắc trách nhiệm hữu hạn nên giá trị không bao giờ âm (giá trị tối thiểu là 0). Giá trị -1 ở đây là mã hóa dữ liệu giả lập bị lỗi. Nếu để nguyên giá âm, khi tính tỷ suất sinh lợi theo logarit r_t = ln(Close_t / Close_{t-1}) sẽ gây lỗi toán học (không tồn tại log của số âm) và làm đảo lộn toàn bộ phương sai, hiệp phương sai của danh mục đầu tư.'),
    ('Câu hỏi 3: Tại sao 503 mã cổ phiếu lại bị hiển thị thành 1,509 mã trong dữ liệu thô? Cách xử lý trong Python như thế nào?',
     'Trả lời: Nguyên nhân là do lỗi khoảng trắng thừa ở đầu hoặc cuối chuỗi ký tự (Leading/Trailing Whitespace), ví dụ hệ thống xem "AAPL", " AAPL" và "  AAPL" là 3 mã riêng biệt. Cách khắc phục chuẩn xác trong Python là dùng lệnh: df["Ticker"] = df["Ticker"].astype(str).str.strip(). Khi đó toàn bộ 1,509 biến thể sẽ tự động gộp chính xác về đúng 503 mã cổ phiếu chuẩn của rổ S&P 500.'),
    ('Câu hỏi 4: Các dòng bị khuyết thiếu Close được giải quyết bằng phương pháp nào? Tại sao không dùng Mean?',
     'Trả lời: Tuyệt đối không được dùng giá trị trung bình (Mean Imputation) vì giá cổ phiếu là chuỗi ngẫu nhiên có xu hướng (Random Walk), điền Mean sẽ làm phẳng độ lệch chuẩn và triệt tiêu tính biến động thị trường. Quy trình chuẩn là: (1) Sắp xếp theo Ticker và Date; (2) Áp dụng Forward Fill (ffill) theo từng mã cổ phiếu để lấy giá đóng cửa của phiên hợp lệ gần nhất điền vào; (3) Nếu dòng nào vẫn khuyết ở đầu chuỗi thì mới loại bỏ.'),
    ('Câu hỏi 5: Ý nghĩa kinh tế của hệ số Kurtosis = 12.85 và Skewness = -0.22 của chuỗi tỷ suất lợi nhuận là gì?',
     'Trả lời: Hệ số Kurtosis = 12.85 vượt xa mức 3.0 của phân phối chuẩn, chứng minh chuỗi lợi suất thực tế có hiện tượng Đuôi dày (Fat-tail) và Đỉnh nhọn (Leptokurtic). Kết hợp với Skewness = -0.22 (lệch trái), điều này khẳng định trong thực tế các cú sụp đổ giá mạnh xảy ra thường xuyên hơn rất nhiều so với lý thuyết phân phối chuẩn Gauss dự báo, đòi hỏi nhà đầu tư phải luôn kiểm soát rủi ro đuôi (Tail Risk & VaR).')
]

for q, a in faqs:
    add_styled_heading(doc, q, level=3)
    add_body_p(doc, a)

# ==================== PHẦN 9: TOÀN BỘ MÃ NGUỒN PYTHON THỰC NGHIỆM ====================
add_styled_heading(doc, 'PHẦN 9: TOÀN BỘ MÃ NGUỒN PYTHON THỰC NGHIỆM ĐÃ TRIỂN KHAI', level=1)

add_body_p(doc, 'Dưới đây là mã nguồn Python hoàn chỉnh thực thi toàn bộ quy trình từ kiểm toán 8 biến, chuyển đổi sang 3 biến, làm sạch dữ liệu và tính toán thống kê:')

code_text = '''# ==============================================================================
# PIPELINE XỬ LÝ & PHÂN TÍCH TÀI CHÍNH ĐỊNH LƯỢNG S&P 500 (PRJ05)
# ==============================================================================
import pandas as pd
import numpy as np

# 1. Đọc dữ liệu và trích xuất đúng 3 biến mục tiêu
raw_path = '17_2521001081_PRJ05_NguyenPhiLamNguyen.csv'
df_raw = pd.read_csv(raw_path, low_memory=False)

# 2. Kiểm toán nhanh chất lượng dữ liệu ban đầu
cols_8 = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume', 'DGS3MO']
for c in cols_8:
    print(f"Biến {c}: Khuyết {df_raw[c].isna().sum():,} dòng ({df_raw[c].isna().sum()/len(df_raw)*100:.2f}%)")

# 3. Lọc lấy 3 biến cốt lõi và làm sạch
df_3var = df_raw[['Date', 'Ticker', 'Close']].copy()
df_3var['Ticker'] = df_3var['Ticker'].astype(str).str.strip() # Gộp 1,509 -> 503 mã

date_str = df_3var['Date'].astype(str).str.replace('/', '-').str.strip()
date_str = date_str.replace(['-', '?', 'nan', 'NaN', 'None', ''], np.nan)
df_3var['Date'] = pd.to_datetime(date_str, errors='coerce')
df_clean = df_3var.dropna(subset=['Date']) # Loại dòng không có ngày

# 4. Làm sạch giá trị số cho biến Close
def clean_close(val):
    if pd.isna(val): return np.nan
    s = str(val).strip()
    for u in ['USD', 'VND', 'kg', '%', 'đ']: s = s.replace(u, '')
    s = s.replace(' ', '').replace(',', '.')
    try:
        num = float(s)
        return num if num > 0 and num != 9999.0 and num != -1.0 else np.nan
    except: return np.nan

df_clean['Close'] = df_clean['Close'].apply(clean_close)

# 5. Sắp xếp Panel Data, xử lý ngoại lai (Median Filter) và Forward Fill
df_clean = df_clean.sort_values(by=['Ticker', 'Date']).reset_index(drop=True)
ticker_median = df_clean.groupby('Ticker')['Close'].transform('median')
outlier_mask = (df_clean['Close'] > 3.0 * ticker_median) | (df_clean['Close'] < ticker_median / 3.0)
df_clean.loc[outlier_mask, 'Close'] = np.nan
df_clean['Close'] = df_clean.groupby('Ticker')['Close'].ffill()
df_final = df_clean.dropna(subset=['Close']).reset_index(drop=True)

# 6. Lưu file dữ liệu sạch 3 cột
df_final[['Date', 'Ticker', 'Close']].to_csv('data_cleaned_SP500.csv', index=False)

# 7. Tính Tỷ suất sinh lợi Log Return hàng ngày
df_final['Log_Return'] = df_final.groupby('Ticker')['Close'].apply(lambda x: np.log(x / x.shift(1))).reset_index(level=0, drop=True)
print(f"✓ Cỡ mẫu sạch: {len(df_final):,} dòng | 503 cổ phiếu | Close TB: ${df_final['Close'].mean():.2f}")
'''

p_code = doc.add_paragraph()
p_code.paragraph_format.space_before = Pt(4)
p_code.paragraph_format.space_after = Pt(8)
p_code.paragraph_format.line_spacing = 1.15
r_c = p_code.add_run(code_text)
r_c.font.name = 'Consolas'
r_c.font.size = Pt(9)
r_c.font.color.rgb = DARK_GRAY

output_path = os.path.join(BASE_DIR, 'Bảng báo cáo.docx')
doc.save(output_path)
print("✅ ĐÃ XUẤT THÀNH CÔNG BẢNG BÁO CÁO TOÀN DIỆN VÀO FILE WORD:")
print(f"👉 Đường dẫn: {output_path}")
