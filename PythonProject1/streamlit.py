import streamlit as st

st.title("Мое первое веб-приложение на Streamlit")

user_name = st.text_input("Как вас зовут?")

if st.button("Приветствовать!"):
    if user_name:
        st.write(f"Привет, {user_name}! Рад тебя видеть на моей странице.")
    else:
        st.write("Пожалуйста, введите ваше имя.")

age = st.slider("Сколько вам лет?", 0, 100, 25)
st.write(f"Вам {age} лет.") 

st.markdown("---") # Горизонтальная линия
st.write("Это простое приложение демонстрирует возможности Streamlit.")
