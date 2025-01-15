import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils.header import display_header
from utils.captcha import math_captcha_verification
import time as time_module
import utils.remove_footer  # Ẩn footer "Made with Streamlit"
from utils.sendmail import send_email



# File CSV lưu dữ liệu
FILE_PATH = "data/medical_incidents.csv"
FAVICON_PATH = "app/static/favicon.png"  # Đường dẫn đến favicon

# Thiết lập favicon cho ứng dụng Streamlit.
st.set_page_config(page_title="Báo cáo sự cố y khoa", page_icon=FAVICON_PATH)

# Hàm lưu dữ liệu vào file CSV
def save_to_csv(data):
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    
    try:
        # Kiểm tra xem file đã tồn tại chưa
        if not os.path.exists(FILE_PATH):
            # Tạo file mới với header
            df = pd.DataFrame([data])
            df.to_csv(FILE_PATH, index=False)
        else:
            # Thêm dữ liệu mới vào file
            df = pd.DataFrame([data])
            df.to_csv(FILE_PATH, mode='a', header=False, index=False)
        
        st.success("Dữ liệu đã được lưu thành công!")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")

# Gọi các hàm hiển thị favicon và logo trong sidebar
display_header()


# Đối tượng xảy ra sự cố
doi_tuong = st.selectbox("**1. Đối tượng xảy ra sự cố:**", ["Người bệnh", "Người nhà/Khách đến thăm", "Nhân viên y tế", "Trang thiết bị/Cơ sở hạ tầng"])

# Thông tin người bệnh (nếu có)
thong_tin_benh_nhan = ""
if doi_tuong == "Người bệnh":
    thong_tin_benh_nhan = st.text_area(
        "**2. Thông tin đối tượng xảy ra sự cố (Họ tên/Năm sinh/Số HSBA/Khoa điều trị):**"
    )

# Địa điểm xảy ra sự cố
dia_diem = st.text_input("**3. Địa điểm xảy ra sự cố:**", placeholder="Ví dụ: Cửa ra vào Khoa Cấp cứu")

# Thời điểm xảy ra sự cố
thoi_diem_option = st.radio("**4. Thời điểm xảy ra sự cố:**", ["Hiện tại", "Thời điểm khác"])

if thoi_diem_option == "Hiện tại":
    thoi_diem = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    st.write(f"Hiện tại: {thoi_diem}")
else:
    date = st.date_input("Chọn ngày xảy ra sự cố:")
    time = st.time_input("Chọn giờ xảy ra sự cố:")
    thoi_diem = datetime.combine(date, time).strftime("%d-%m-%Y %H:%M:%S")

# Phân loại sự cố
phan_loai = st.radio("**5. Phân loại về sự cố:**", ["Đã xảy ra", "Sắp xảy ra"])

# Xử trí ban đầu
xu_tri = st.text_area("**6. Xử trí ban đầu:**")

# Mức độ ảnh hưởng
muc_do = st.selectbox("**7. Mức độ ảnh hưởng:**", ["Nặng", "Trung bình", "Nhẹ"])

# Thông báo cho người có thẩm quyền
thong_bao_tham_quyen = st.radio("**8. Thông báo cho người có thẩm quyền phụ trách nơi xảy ra sự cố:**", ["Có", "Không", "Không ghi nhận"])

# Thông báo cho người nhà (nếu đối tượng là người bệnh)
thong_bao_nguoi_nha = ""
if doi_tuong == "Người bệnh":
    thong_bao_nguoi_nha = st.radio("**9. Thông báo cho người nhà/Người giám hộ:**", ["Có", "Không", "Không ghi nhận"])

# Ghi nhận vào HSBA
ghi_nhan_hsba = st.radio("**10. Ghi nhận vào HSBA - Giấy tờ liên quan:**", ["Có", "Không", "Không ghi nhận"])

# Người báo cáo
nguoi_bao_cao = st.text_input("**11. Người báo cáo:**")

# Khoa/Phòng báo cáo
khoa_phong = st.text_input("**12. Khoa/Phòng báo cáo:**")



# Biến trạng thái cho giao diện
if "show_submit_button" not in st.session_state:
    st.session_state["show_submit_button"] = False
if "last_report" not in st.session_state:
    st.session_state["last_report"] = None

# Bước 1: Hiển thị CAPTCHA
if not st.session_state["show_submit_button"]:
    st.markdown("### Xác thực CAPTCHA")
    if math_captcha_verification():
        st.session_state["show_submit_button"] = True

# Bước 2: Hiển thị nút gửi báo cáo nếu CAPTCHA đúng
if st.session_state["show_submit_button"]:
    st.markdown("### Gửi Báo Cáo")
    if st.button("Gửi báo cáo"):
        # Kiểm tra các trường bắt buộc
        if not nguoi_bao_cao:
            st.error("Vui lòng nhập tên người báo cáo.")
        elif not khoa_phong:
            st.error("Vui lòng nhập tên khoa/phòng.")
        elif not dia_diem:
            st.error("Vui lòng nhập địa điểm xảy ra sự cố.")
        else:
            # Tạo dữ liệu báo cáo
            data = {
                "Đối tượng xảy ra sự cố": doi_tuong,
                "Thông tin người bệnh": thong_tin_benh_nhan,
                "Địa điểm": dia_diem,
                "Thời điểm": thoi_diem,
                "Phân loại sự cố": phan_loai,
                "Xử trí ban đầu": xu_tri,
                "Mức độ ảnh hưởng": muc_do,
                "Thông báo cho thẩm quyền": thong_bao_tham_quyen,
                "Thông báo người nhà": thong_bao_nguoi_nha,
                "Ghi nhận vào HSBA": ghi_nhan_hsba,
                "Người báo cáo": nguoi_bao_cao,
                "Khoa/Phòng": khoa_phong,
            }
            # Lưu dữ liệu vào CSV
            save_to_csv(data)
           
            # Lưu thông tin báo cáo vào session để hiển thị
            st.session_state["last_report"] = data

            # Hiển thị popup với thời gian chờ 10s
            with st.spinner("Đang xử lý..."):
                time_module.sleep(1)  # Đợi 1s
                # Gửi email
                send_email(data)
            st.success("Báo cáo đã gửi thành công!")

            # Hiển popup với các nút "Gửi tiếp" hoặc "Kết thúc"
            option = st.radio(
                "Bạn muốn làm gì tiếp theo?",
                options=["Gửi báo cáo tiếp", "Kết thúc"],
                index=1,
                key="popup_option"
            )
            
            if option == "Gửi báo cáo tiếp":
                # Reset trạng thái và form
                st.session_state.clear()
                st.experimental_rerun()
            elif option == "Kết thúc":
                # Hiển thị thông tin báo cáo vừa gửi dưới dạng bảng dọc (2 cột)
                st.markdown("### Thông Tin Báo Cáo Vừa Gửi")
                report_data = pd.DataFrame(st.session_state["last_report"].items(), columns=["Tên Trường", "Giá Trị"])
                st.table(report_data)


# Ân footer "Made with Streamlit"
utils.remove_footer.footer()

