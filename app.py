# app.py

# Import the necessary libraries
import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# Try to get the API key from Streamlit's secrets management.
api_key = st.secrets.get("GEMINI_API_KEY")

# If not found, check environment variables
if not api_key:
    api_key = os.environ.get("GEMINI_API_KEY")

# If still not found, stop the app
if not api_key:
    st.error("Gemini API key not found. Please set it in Streamlit secrets or as an environment variable.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Streamlit App Config ---
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI ChatBot")
st.caption("A simple chatBot with memory by Abubackar Siddiq")

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input and Chat Logic ---
prompt = st.chat_input("What would you like to ask?")

if prompt:
    # 1. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Prepare full conversation history
    conversation = []
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        conversation.append(f"{role}: {msg['content']}")

    conversation_text = "\n".join(conversation)

    # 4. Get assistant response using full history
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(conversation_text)
            full_response = response.text
            st.markdown(full_response)
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"An error occurred: {e}")
            error_message = "Sorry, I encountered an error."
            st.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# --- End of app ---
