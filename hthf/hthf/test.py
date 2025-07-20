import streamlit as st
import os

uploaded_file = st.file_uploader("Загрузите файл для сохранения")

if uploaded_file is not None:
    # Создаем папку uploads, если ее нет
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    # Сохраняем файл
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Файл сохранен: {file_path}")