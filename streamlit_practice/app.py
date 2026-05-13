import streamlit as st

st.title("Simple Streamlit")

name = st.text_input("이름 입력")

if st.button("확인"):
    st.success(f"안녕하세요 {name}님!")