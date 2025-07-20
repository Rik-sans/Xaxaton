import streamlit as st
import requests
import os

# Интерфейс
st.title("🤖 Langflow Chatbot")
user_input = st.chat_input("Введите ваш вопрос")

# Загружаем файл (опционально)
uploaded_file = st.file_uploader("Загрузите файл (необязательно)")
file_path = None
if uploaded_file:
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Файл {uploaded_file.name} сохранён")

# Отправка запроса к Langflow API
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    # Эндпоинт Langflow
    url = "http://localhost:7860/api/v1/run/f2561e64-5978-4b95-9e54-39492f739a5d"

    payload = {
        "question": user_input
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()

        # Вывод ответа
        answer = result.get("answer") or result.get("output") or str(result)
        with st.chat_message("assistant"):
            st.write(answer)

    except Exception as e:
        st.warning("Ошибка при запросе к Langflow API:")
        st.error(str(e))
