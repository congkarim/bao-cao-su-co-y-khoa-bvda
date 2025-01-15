import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

# Cấu hình SMTP
SMTP_SERVER = "smtp.gmail.com"  # Máy chủ SMTP (Gmail)
SMTP_PORT = 587  # Cổng cho TLS
EMAIL_ADDRESS = "congkarim@gmail.com"  # Thay bằng email của bạn
EMAIL_PASSWORD = "ioqe ywmx oaiw lgya"  # Thay bằng mật khẩu ứng dụng email của bạn

def send_email(report_data):
    """
    Gửi báo cáo sự cố qua email.
    
    Args:
        report_data (dict): Dữ liệu báo cáo dưới dạng dictionary.
    """
    # Tạo nội dung email
    subject = f"[{str(report_data['Khoa/Phòng']).upper()}] - Báo cáo sự cố y khoa"
    body = "Báo cáo sự cố y khoa:\n\n"
    for key, value in report_data.items():
        body += f"{key}: {value}\n"

    # Tạo email
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "khthbvda@gmail.com"
    msg["Subject"] = subject

    # Thêm nội dung vào email
    msg.attach(MIMEText(body, "plain"))

    try:
        # Kết nối tới SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Kích hoạt mã hóa TLS
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Đăng nhập

        # Gửi email
        server.send_message(msg)
        server.quit()
        st.success("Báo cáo đã được gửi đến email khthbvda@gmail.com thành công!")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi gửi email: {e}")
