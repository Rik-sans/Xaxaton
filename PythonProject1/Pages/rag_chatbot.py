import streamlit as st
import requests
import os
from datetime import datetime

# --- Конфигурация ---
st.set_page_config(
    page_title="Гениальный RAG Чат-бот",
    page_icon="🤖",
    layout="wide"
)


# --- Стили ---
def load_css():
    st.markdown("""
    <style>
        .stChatInput {position: fixed; bottom: 2rem;}
        .stChatMessage {padding: 1rem; border-radius: 0.5rem;}
        .user-message {background-color: #f0f2f6; margin-left: 30%;}
        .bot-message {background-color: #e6f7ff; margin-right: 30%;}
        .timestamp {font-size: 0.8rem; color: #666; text-align: right;}
    </style>
    """, unsafe_allow_html=True)


load_css()

# --- Инициализация сессии ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.api_calls = 0


# --- Langflow API Client ---
class LangflowClient:
    def __init__(self):
        self.api_key = self._get_api_key()
        self.base_url = "http://localhost:7860/api/v1/run/f2561e64-5978-4b95-9e54-39492f739a5d"

    def _get_api_key(self):
        """Гениально получаем API ключ с проверкой всех возможных источников"""
        try:
            return os.environ["LANGFLOW_API_KEY"]
        except KeyError:
            try:
                from dotenv import load_dotenv
                load_dotenv()
                return os.environ["LANGFLOW_API_KEY"]
            except:
                st.error("LANGFLOW_API_KEY не найден. Пожалуйста, установите ключ в переменные окружения.")
                st.stop()

    def query_rag(self, question: str) -> str:
        """Совершенный метод запроса к RAG системе"""
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }

        payload = {
            "output_type": "chat",
            "input_type": "chat",
            "input_value": question
        }

        try:
            response = requests.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=30  # Оптимальный таймаут
            )

            response.raise_for_status()
            st.session_state.api_calls += 1

            return response.json().get("result", "Не удалось получить ответ от RAG системы")

        except requests.exceptions.RequestException as e:
            st.error(f"Ошибка соединения с Langflow API: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Неожиданная ошибка: {str(e)}")
            return None


# --- Интерфейс ---
def display_chat():
    """Безупречный интерфейс чата"""
    st.title("🧠 Гениальный RAG Чат-бот")
    st.caption(f"API вызовов сегодня: {st.session_state.api_calls}")

    # История сообщений
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("timestamp"):
                st.caption(message["timestamp"])

    # Ввод вопроса
    if prompt := st.chat_input("Задайте ваш вопрос..."):
        # Добавляем вопрос пользователя
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": timestamp
        })

        with st.chat_message("user"):
            st.markdown(prompt)
            st.caption(timestamp)

        # Получаем ответ от RAG
        with st.spinner("Думаю..."):
            langflow_client = LangflowClient()
            response = langflow_client.query_rag(prompt)

            if response:
                timestamp = datetime.now().strftime("%H:%M:%S")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "timestamp": timestamp
                })

                with st.chat_message("assistant"):
                    st.markdown(response)
                    st.caption(timestamp)


# --- Запуск ---
if __name__ == "__main__":
    display_chat()