Python
import streamlit as st
import docx
from io import BytesIO

# Cấu hình trang web
st.set_page_config(page_title="Trợ Lý AI Xuất Bản Giáo Án Thể Dục 7991", page_icon="⚽", layout="wide")

# Tiêu đề ứng dụng
st.title("⚽ Trợ Lý AI Xuất Bản Tài Liệu Dạy Học Môn Thể Dục (Chuẩn CV 7991/BGDĐT)")
st.caption("Tác giả: Thầy Phan Hồ Bảo | Sản phẩm tham dự Cuộc thi Thiết kế Ứng dụng AI Dạy học")

st.divider()

# Khung nhập liệu thông tin
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    mon_hoc = st.selectbox("Môn học:", ["Giáo dục thể chất (Thể dục)"])
with col2:
    khoi_lop = st.selectbox("Khối lớp:", ["Lớp 7"])
with col3:
    ten_bai = st.text_input("Tên bài học / Chủ đề:", "Kỹ thuật xuất phát thấp và chạy lao sau xuất phát")

ycd = st.text_area(
    "Yêu cầu cần đạt (YCĐ):", 
    "Thực hiện đúng các khẩu lệnh và kỹ thuật xuất phát thấp ('Vào chỗ' - 'Sẵn sàng' - 'Chạy'); Bước đầu thực hiện được kỹ thuật chạy lao sau xuất phát và biết phối hợp trong trò chơi vận động."
)

st.divider()

# Tab chức năng xuất bản
tab1, tab2, tab3 = st.tabs(["📝 Giáo án Thể dục (CV 7991)", "📊 Slide / Sơ đồ Tập luyện", "📋 Ma Trận & Bảng Đánh Giá"])

with tab1:
    st.subheader("Kế hoạch bài dạy (Giáo án) Môn Thể dục 7 theo Công văn 7991")
    if st.button("🚀 Tạo Giáo Án Tự Động Với AI", key="btn_ga"):
        st.success("Đã khởi tạo thành công giáo án chuẩn CV 7991!")
        
        # Nội dung giáo án
        ga_content = f"""
KẾ HOẠCH BÀI DẠY: {ten_bai.upper()}
Giáo viên thực hiện: Phan Hồ Bảo
Môn: Giáo dục thể chất - Lớp 7 | Thời lượng: 01 tiết (45 phút)

I. MỤC TIÊU
1. Về năng lực:
   - Năng lực chăm sóc sức khỏe: Biết vệ sinh sân tập, chuẩn bị trang phục thể thao ngăn nắp và thả lỏng phục hồi sau vận động.
   - Năng lực vận động cơ bản: Thực hiện đúng kỹ thuật xuất phát thấp và giai đoạn chạy lao.
   - Năng lực hoạt động TDTT: Quan sát động tác mẫu, tự sửa sai và ứng dụng vào bài tập phát triển sức nhanh.
2. Về phẩm chất:
   - Tự giác, kỷ luật, trách nhiệm và đảm bảo an toàn tuyệt đối trong luyện tập.

II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
- Giáo viên: Còi, đồng hồ bấm giây, bàn đạp xuất phát (hoặc vạch kẻ xuất phát), cờ hiệu.
- Học sinh: Trang phục thể thao, giày vải, nước uống cá nhân.

III. TIẾN TRÌNH DẠY HỌC (Đủ 4 Hoạt động - 4 Bước)

1. HOẠT ĐỘNG 1: MỞ ĐẦU (8 - 10 phút)
   - a) Chuyển giao nhiệm vụ: GV tập hợp 4 hàng ngang, kiểm tra sĩ số, sức khỏe HS; phổ biến nội dung. Khởi động chung (xoay các khớp) và khởi động chuyên môn (chạy bước nhỏ, nâng cao đùi, ép dọc, ép ngang).
   - b) Thực hiện nhiệm vụ: Cán sự điều khiển, HS thực hiện nghiêm túc.
   - c) Báo cáo, thảo luận: Cán sự báo cáo hoàn thành. GV kiểm tra nhanh tư thế chuẩn bị xuất phát.
   - d) Kết luận, nhận định: GV nhận xét khởi động và dẫn dắt vào bài.

2. HOẠT ĐỘNG 2: HÌNH THÀNH KIẾN THỨC MỚI (10 - 12 phút)
   - a) Chuyển giao nhiệm vụ: GV làm mẫu và phân tích kỹ thuật xuất phát thấp theo 3 lệnh ("Vào chỗ", "Sẵn sàng", "Chạy") và kỹ thuật chạy lao.
   - b) Thực hiện nhiệm vụ: HS quan sát, lắng nghe và mô phỏng động tác không còi theo hướng dẫn.
   - c) Báo cáo, thảo luận: GV gọi 2 HS thực hiện mẫu, cả lớp quan sát nhận xét góc nâng hông.
   - d) Kết luận, nhận định: GV chốt các lưu ý kỹ thuật (không xuất phát trước lệnh, dồn trọng tâm về trước).

3. HOẠT ĐỘNG 3: LUYỆN TẬP (15 - 18 phút)
   - a) Chuyển giao nhiệm vụ: Cho HS tập đồng loạt theo hiệu lệnh còi; tập theo cặp đôi sửa sai cho nhau; tổ chức trò chơi "Chạy tiếp sức 15m xuất phát thấp".
   - b) Thực hiện nhiệm vụ: HS tích cực luyện tập và tham gia trò chơi an toàn. GV sửa sai cho từng HS.
   - c) Báo cáo, thảo luận: Các tổ thực hiện thi đấu xuất phát 15m.
   - d) Kết luận, nhận định: GV tuyên dương tổ thắng cuộc, chỉ ra các lỗi sai phổ biến (đứng dậy quá sớm) và hướng dẫn cách khắc phục.

4. HOẠT ĐỘNG 4: VẬN DỤNG & HỒI TĨNH (5 phút)
   - a) Chuyển giao nhiệm vụ: Thực hiện thả lỏng (rung cơ bắp, hít thở sâu). GV đặt câu hỏi vận dụng về tầm quan trọng của phản xạ nhanh khi xuất phát.
   - b) Thực hiện nhiệm vụ: HS thả lỏng và trả lời câu hỏi.
   - c) Báo cáo, thảo luận: HS trả lời cá nhân trước lớp.
   - d) Kết luận, nhận định: GV tổng kết tiết học, giao bài tập rèn luyện sức nhanh tại nhà và xuống lớp.
        """
        st.text_area("Xem trước giáo án:", ga_content, height=400)
        
        # Tạo file Docx tải về
        doc = docx.Document()
        doc.add_heading(f"KẾ HOẠCH BÀI DẠY MÔN THỂ DỤC 7", 0)
        doc.add_paragraph(f"Giáo viên: Phan Hồ Bảo")
        doc.add_paragraph(ga_content)
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        
        st.download_button(
            "📥 Tải File Giáo Án (.docx)", 
            data=buffer, 
            file_name=f"Giao_An_The_Duc_7_PhanHoBao.docx", 
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

with tab2:
    st.subheader("Kịch bản Slide / Sơ đồ Tập luyện tương ứng")
    st.info("Chuyển đổi giáo án thành các Slide minh họa sơ đồ tập luyện và kỹ thuật động tác.")
    st.write("• **Slide 1:** Tiêu đề bài học & Yêu cầu cần đạt - Thầy Phan Hồ Bảo")
    st.write("• **Slide 2:** Khởi động & Khởi động chuyên môn (Sơ đồ 4 hàng ngang)")
    st.write("• **Slide 3:** Hình ảnh phân tích Kỹ thuật Xuất phát thấp (3 khẩu lệnh)")
    st.write("• **Slide 4:** Sơ đồ tổ chức luyện tập & Trò chơi tiếp sức 15m")
    st.write("• **Slide 5:** Hồi tĩnh & Bài tập rèn luyện sức nhanh tại nhà")

with tab3:
    st.subheader("Bảng Đánh Giá Kỹ Năng GDTC Lớp 7 (Thông tư 22/2021/BGDĐT)")
    st.write("• **Mức Đạt (Đ):** Thực hiện đúng 3 lệnh xuất phát thấp, góc ngả thân người khi chạy lao hợp lý, hoàn thành cự ly chạy 30m/50m đúng thời gian tiêu chuẩn.")
    st.write("• **Mức Chưa Đạt (CĐ):** Xuất phát sai hiệu lệnh, bật thẳng người ngay
