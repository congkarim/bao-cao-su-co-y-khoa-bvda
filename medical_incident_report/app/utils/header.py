import streamlit as st

# Đường dẫn đến logo và favicon
LOGO_PATH = "https://benhviendonganh.com/DATA/INFO/2023/2/17/benh-vien-da-khoa-dong-anh-9937e.png"  # Đường dẫn đến logo


# Hiển thị logo và tiêu đề
def display_header():
    """
    Hiển thị logo và tiêu đề trên cùng một hàng, căn giữa theo chiều dọc.
    Trên giao diện mobile, logo nằm trên tiêu đề và khoảng cách giữa chúng được tối ưu hóa.
    """
    st.markdown(
        f"""
        <style>
            .header-container {{
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 20px;
                flex-wrap: wrap; /* Cho phép logo và tiêu đề xuống dòng */
            }}
            .header-container img {{
                width: 150px;
                margin-right: 20px;
            }}
            .header-container h1 {{
                font-weight: bold;
                margin: 0;
            }}
            /* Thiết lập cho màn hình nhỏ (mobile) */
            @media (max-width: 768px) {{
                .header-container {{
                    flex-direction: column; /* Logo nằm trên tiêu đề */
                    text-align: center;
                }}
                .header-container img {{
                    width: 200px; /* Giảm kích thước logo */
                    margin: 0 0 5px 0; /* Giảm khoảng cách dưới logo */
                }}
                .header-container h1 {{
                    margin-top: 5px; /* Giảm khoảng cách trên tiêu đề */
                }}
            }}
        </style>
        <div class="header-container">
            <img src="{LOGO_PATH}" alt="Logo">
            <h1>BÁO CÁO SỰ CỐ Y KHOA</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
