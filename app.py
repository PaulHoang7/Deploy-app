import streamlit as st

# Hàm xử lý input
def analyze_input(user_input):
    result = user_input.upper()  # Xử lý: in hoa chuỗi
    print(f"Input: {user_input} -> Output: {result}")  # In kết quả ra console (chỉ khi chạy cục bộ)
    # Ghi log vào file
    with open("log.txt", "a") as log_file:
        log_file.write(f"Input: {user_input} -> Output: {result}\n")
    return result

# Giao diện Streamlit
st.title("Text Analyzer on Cloud")
user_input = st.text_input("Enter your text:")
if st.button("Submit"):
    if user_input:
        result = analyze_input(user_input)
        st.write("Result:", result)
    else:
        st.write("Please enter some text!")
