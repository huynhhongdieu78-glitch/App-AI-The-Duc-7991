import streamlit as st

st.set_page_config(page_title="Trợ Lý AI Xuất Bản Tài Liệu - Chuẩn CV 7991", layout="wide")

st.title("⚽ Trợ Lý AI Xuất Bản Tài Liệu Dạy Học")
st.caption("Tác giả: Thầy Phan Hồ Bảo | Sản phẩm ứng dụng AI chuẩn Công văn 7991/BGDĐT")

st.divider()

doc_type = st.selectbox(
    "Chọn Loại Tài Liệu Cần Xuất Bản:",
    [
        "1. Kế hoạch bài dạy (Giáo án CV 7991)",
        "2. Slide bài giảng kèm Lời thoại (Presenter Notes)",
        "3. Ma trận Đề kiểm tra & Đáp án đánh giá"
    ]
)

subject = st.text_input("Tên Môn Học & Khối Lớp:", "Giáo dục thể chất 7 (Bộ sách Kết nối tri thức)")
lesson = st.text_input("Tên Bài Học / Chủ Đề:", "Bài 2: Chạy cự ly ngắn (Kỹ thuật xuất phát cao và chạy lao)")

if st.button("Tạo và Xuất Bản Tài Liệu AI"):
    st.success("Đã tạo và xuất bản tài liệu thành công!")
    st.markdown("---")
    
    if "1." in doc_type:
        st.subheader("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM")
        st.markdown("**Độc lập - Tự do - Hạnh phúc**")
        st.markdown(f"### KẾ HOẠCH BÀI DẠY (CHUẨN CÔNG VĂN 7991/BGDĐT)")
        st.write(f"**Môn học / Hoạt động:** {subject}")
        st.write(f"**Tên bài học:** {lesson}")
        st.write("**Thời lượng:** 1 tiết")
        
        st.markdown("---")
        st.markdown("#### I. MỤC TIÊU")
        st.markdown("1. **Về kiến thức:** Nêu và phân tích được kỹ thuật xuất phát cao và chạy lao sau xuất phát trong môn Chạy cự ly ngắn.")
        st.markdown("2. **Về năng lực:** Thực hiện đúng kỹ thuật động tác xuất phát cao, giữ thăng bằng tốt và bứt tốc ở giai đoạn chạy lao.")
        st.markdown("3. **Về phẩm chất:** Chăm chỉ, trung thực, kỷ luật cao và có trách nhiệm trong luyện tập thể dục thể thao.")
        
        st.markdown("#### II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU")
        st.write("- Sân tập bằng phẳng, còi, đồng hồ bấm giờ, tranh ảnh kỹ thuật.")
        
        st.markdown("#### III. TIẾN TRÌNH DẠY HỌC")
        st.markdown("**1. Hoạt động 1: Khởi động (8-10 phút)**")
        st.write("- Mục tiêu: Chuẩn bị cơ thể, tâm lý và làm nóng các khớp.")
        st.write("- Nội dung: Chạy chậm nhẹ nhàng vòng tròn, xoay các khớp cổ tay, cổ chân, gối, hông.")
        
        st.markdown("**2. Hoạt động 2: Hình thành kiến thức mới (15-20 phút)**")
        st.write("- Mục tiêu: Nắm vững lý thuyết và thao tác kỹ thuật xuất phát cao.")
        st.write("- Nội dung: Giáo viên phân tích, làm mẫu động tác (Vào chỗ, Chạy/Xuất phát).")
        
        st.markdown("**3. Hoạt động 3: Luyện tập (15 phút)**")
        st.write("- Mục tiêu: Sửa sai động tác và nâng cao thành tích cá nhân.")
        
        st.markdown("**4. Hoạt động 4: Vận dụng & Hồi tĩnh (5 phút)**")
        st.write("- Mục tiêu: Thả lỏng cơ bắp, đưa cơ thể về trạng thái bình thường.")

    elif "2." in doc_type:
        st.subheader(f"BỘ SLIDE TRÌNH CHIẾU BÀI GIẢNG: {lesson}")
        st.markdown("---")
        st.markdown("#### SLIDE 1: TRANG BÌA")
        st.write(f"- Tiêu đề: {lesson}")
        st.write(f"- Môn: {subject}")
        st.info("[Presenter Notes]: Giáo viên ổn định lớp, kiểm tra sĩ số và giới thiệu ngắn gọn nội dung bài học.")
        
        st.markdown("---")
        st.markdown("#### SLIDE 2: MỤC TIÊU BÀI HỌC")
        st.write("- Kiến thức: Kỹ thuật xuất phát cao & chạy lao.")
        st.write("- Phẩm chất & Năng lực: Kỷ luật, hợp tác nhóm.")
        st.info("[Presenter Notes]: Nhấn mạnh tầm quan trọng của việc khởi động kỹ trước khi chạy bứt tốc.")

        st.markdown("---")
        st.markdown("#### SLIDE 3: HOẠT ĐỘNG KHỞI ĐỘNG")
        st.write("- Hình ảnh minh họa: Bài tập xoay khớp & chạy bước nhỏ.")
        st.info("[Presenter Notes]: Cho lớp trưởng hô nhịp cho các bạn khởi động toàn thân trong 5 phút.")

    else:
        st.subheader("MA TRẬN ĐỀ KIỂM TRA ĐÁNH GIÁ ĐỊNH KỲ")
        st.write(f"**Môn:** {subject} - **Chủ đề:** {lesson}")
        st.markdown("---")
        st.markdown("#### 1. Bảng ma trận đặc tả đề kiểm tra:")
        st.write("- **Nhận biết (40%):** Trắc nghiệm nhận diện đúng khẩu lệnh trong chạy cự ly ngắn.")
        st.write("- **Thông hiểu (30%):** Giải thích được vì sao phải ngả người về phía trước sau khi xuất phát.")
        st.write("- **Vận dụng (20%):** Phân tích ưu/nhược điểm khi thực hiện động tác.")
        st.write("- **Vận dụng cao (10%):** Áp dụng kỹ thuật vào thi đấu thể thao tại trường.")
        
        st.markdown("#### 2. Đề kiểm tra mẫu:")
        st.write("Câu 1 (Nhận biết): Khẩu lệnh trong tư thế xuất phát cao gồm mấy bước?")
        st.write("Câu 2 (Thông hiểu): Nêu điểm khác biệt giữa giai đoạn chạy lao và chạy giữa quãng?")

        
