import streamlit as st
import requests
import json

def extract_text_from_json(json_data):
    # Если входные данные - строка JSON, загружаем их в словарь
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    # Извлекаем текст из структуры JSON
    try:
        # Путь к тексту в данном JSON
        text = data['outputs'][0]['outputs'][0]['results']['message']['text']
        return text
    except (KeyError, IndexError) as e:
        print(f"Ошибка при извлечении текста: {e}")
        return None

st.title("🤖 Пользовательский бот")
st.write("Задайте вопрос боту")

user_input = st.text_input("Например: 'Как почистить микроволновку?'")

api_key = "sk-15alwW6Kx9uZ1R5EUZxOZ2gVjIBUYgl5Nm-JaSqVGeg"
url = "http://localhost:7860/api/v1/run/f4db2ca5-cfcf-4ce6-bd1d-bcd7ee9b5f13"

if st.button("Ввод"):
    payload = {
        "output_type": "text",
        "input_type": "text",
        "input_value": user_input
    }

    print(payload)

    headers = {
        "Content-Type": "application/json",
        "x-api-key": "sk-15alwW6Kx9uZ1R5EUZxOZ2gVjIBUYgl5Nm-JaSqVGeg"  # Authentication key from environment variable
    }
    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = requests.post(url)
        response.raise_for_status()  # Raise exception for bad status codes
        if response.text:
            try:
                result = response.json()
                st.text(extract_text_from_json(result))
            except ValueError:
                st.text(response.text)
        else:
            st.warning("Пустой ответ от сервера")


    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP ошибка: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка запроса: {str(e)}")
    except Exception as e:
        st.error(f"Неожиданная ошибка: {str(e)}")
