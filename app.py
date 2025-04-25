
import requests
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()


# Set your OpenAI API key here
API_KEY = os.getenv("OPENAI_API_KEY")


API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Function to generate a response using OpenAI's Chat Completion API
def generate_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Use the chat model
        "messages": [
            {"role": "system", "content": "You are a helpful customer service assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"


def handle_user_input():
    user_input = st.session_state.input
    if user_input:
        response = generate_response(user_input)
        st.session_state.chat_history.append(f"👤: {user_input}")
        st.session_state.chat_history.append(f"🗣️: {response}")
        st.session_state.input = ""  # Clear input *before* next render

def main():
    st.set_page_config(page_title="Group 5 Chatbot", page_icon="💬")
    st.title("Group 5")
    st.markdown("Customer Service Chatbot")

    with st.expander("👥 Project Contributors"):
        st.markdown("""
        **Group 6 Contributors:**
        - ADEBOWALE ANU VICTOR – `SEN/19/0689`
        - ASHIFA ABDULMATEEN ADENIYI – `SEN/19/0702`
        - BALOGUN EMMANUEL AYOMIDE – `SEN/19/0708 `
        - OGUNKENU KAYODE AYOMIDE – `SEN/19/0724`
        - MAFO MOYOSOREOLUWA AYOMIDE – `SEN/19/0721`
        - SARAFADEEN IBRAHIM OYINKOLADE – `SEN/19/0742`
        - AKINTAN DAVID OLUWAYEMI – `SEN/19/0698`
        """)

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.chat_history.append("🗣️: Hello! I am your virtual assistant. How may I help you?")

    # Display chat history
    for msg in st.session_state.chat_history:
        st.markdown(msg)

    # Input box at the bottom, using a callback to handle input
    st.text_input(
        label="",
        placeholder="Ask me anything...",
        key="input",
        on_change=handle_user_input
    )

if __name__ == "__main__":
    main()
