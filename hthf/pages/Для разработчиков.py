import streamlit as st
import os

st.title("💻 Бот для разработчиков")
st.write("Задайте технический вопрос (Python, Streamlit, API и др.):")
col1, col2 = st.columns(2)
# Имитация бота
with col1:
    st.write('')
    user_input = st.chat_input("Например: 'Как создать кнопку в Streamlit?'")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    # Простые ответы бота (можно подключить ChatGPT или другой API)
    bot_responses = {
        "как создать кнопку в streamlit": "Используйте `st.button('Текст кнопки')`. Пример: `if st.button('Нажми меня'): st.write('Кнопка нажата!')`",
        "как установить streamlit": "Введите в терминале: `pip install streamlit`",
        "как запустить streamlit": "Запустите файл командой: `streamlit run ваш_файл.py`"
    }

    answer = bot_responses.get(user_input.lower(), "Я отвечаю на вопросы по Python, Streamlit и веб-разработке. Попробуйте уточнить запрос.")

    with st.chat_message("assistant"):
        st.write(answer)
with col2:
    uploaded_file = st.file_uploader('')

if uploaded_file is not None:
    # Создаем папку uploads, если ее нет
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    # Сохраняем файл
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Файл сохранен: {file_path}")