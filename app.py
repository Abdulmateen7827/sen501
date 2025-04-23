
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

# Streamlit app
def main():
    st.title("Simple Customer Service Chatbot")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input
    user_input = st.text_input("You: ", "")

    if user_input:
        # Generate a response
        bot_response = generate_response(user_input)
        
        # Append the conversation to the chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {bot_response}")

    # Display the chat history
    for message in st.session_state.chat_history:
        st.text(message)

if __name__ == "__main__":
    main()