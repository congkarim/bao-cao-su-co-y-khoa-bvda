import streamlit as st

def footer():
    # CSS để ẩn dòng chữ "Made with Streamlit"
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    new_footer = """
        <div style="width: 100%; text-align: center;">
        <p>BỆNH VIỆN ĐA KHOA ĐÔNG ANH</p>
        </div>
    """
    st.markdown(new_footer, unsafe_allow_html=True)

