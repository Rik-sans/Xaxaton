import streamlit as st

st.title("💻 Бот для разработчиков")
st.write("Задайте технический вопрос (Python, Streamlit, API и др.):")

# Имитация бота
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