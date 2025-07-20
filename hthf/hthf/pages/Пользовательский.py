import streamlit as st
import os

st.title("🤖 Пользовательский бот")
st.write("Задайте вопрос боту, который поможет в бытовых вопросах:")
col1, col2 = st.columns(2)

# Имитация бота
with col1:
    st.write('')
    user_input = st.chat_input("Например: 'Как почистить микроволновку?'")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    # Простые ответы бота (можно заменить на реальную модель, например, OpenAI API)
    bot_responses = {
        "как почистить микроволновку": "Налейте в миску воду с лимонным соком, поставьте в микроволновку на 5 минут на высокой мощности, затем протрите губкой.",
        "рецепт блинов": "Смешайте 1 стакан муки, 1 яйцо, 1 ст.л. сахара, 300 мл молока и щепотку соли. Жарьте на сковороде без масла.",
        "как убрать пятно": "Нанесите на пятно смесь соды и уксуса, оставьте на 10 минут, затем постирайте."
    }

    answer = bot_responses.get(user_input.lower(), "Я могу помочь с рецептами, уборкой и другими бытовыми вопросами. Попробуйте уточнить запрос.")

    with st.chat_message("assistant"):
        st.write(answer)
with col2:
    uploaded_file = st.file_uploader("")

if uploaded_file is not None:
    # Создаем папку uploads, если ее нет
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    
    # Сохраняем файл
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Файл сохранен: {file_path}")