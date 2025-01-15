import random
import streamlit as st

# Tạo bài toán Math CAPTCHA
def generate_math_captcha():
    """
    Tạo bài toán CAPTCHA đơn giản (cộng hoặc trừ).
    Returns:
        question (str): Câu hỏi bài toán.
        result (int): Kết quả đúng của bài toán.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    if operator == '+':
        result = num1 + num2
    else:
        result = num1 - num2
    question = f"{num1} {operator} {num2} = ?"
    return question, result

# Xác thực CAPTCHA
def math_captcha_verification():
    """
    Hiển thị CAPTCHA và kiểm tra đầu vào của người dùng.
    Returns:
        bool: True nếu người dùng xác thực đúng, False nếu sai.
    """
    if "captcha_result" not in st.session_state:
        # Tạo bài toán CAPTCHA nếu chưa tồn tại
        question, result = generate_math_captcha()
        st.session_state['captcha_question'] = question
        st.session_state['captcha_result'] = result
    
    # Hiển thị câu hỏi
    st.markdown(f"**Giải bài toán CAPTCHA:** {st.session_state['captcha_question']}")
    user_input = st.text_input("Nhập kết quả:", key="math_captcha_input")
    
    if st.button("Xác nhận CAPTCHA"):
        if user_input.isdigit() and int(user_input) == st.session_state['captcha_result']:
            st.success("Xác thực CAPTCHA thành công!")
            return True
        else:
            st.error("Kết quả không đúng. Vui lòng thử lại.")
            # Tạo bài toán mới sau mỗi lần sai
            del st.session_state['captcha_result']
            del st.session_state['captcha_question']
            return False
