# app.py

# Import the necessary libraries
import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# This is the first thing we do. We need to configure our app with the Gemini API key.
# Streamlit's "secrets" feature is the most secure way to do this.
#
# How to set up your API key:
# 1. Create a folder named ".streamlit" in your project directory.
# 2. Inside that folder, create a file named "secrets.toml".
# 3. Add your API key to the secrets.toml file like this:
#    GEMINI_API_KEY = "YOUR_API_KEY_HERE"

# Try to get the API key from Streamlit's secrets management.
api_key = st.secrets.get("GEMINI_API_KEY")

# If the key is not found in secrets (for example, when running locally without secrets),
# try to get it from an environment variable.
if not api_key:
    api_key = os.environ.get("GEMINI_API_KEY")

# If the API key is still not found, show an error message and stop the app.
if not api_key:
    st.error("Gemini API key not found. Please set it in Streamlit secrets or as an environment variable.")
    st.stop()

# Configure the Gemini library with your API key.
genai.configure(api_key=api_key)


# --- Model Initialization ---
# Here, we initialize the Gemini model. 'gemini-1.5-flash-latest' is a fast and efficient model.
# The previous 'gemini-pro' model name is outdated, which caused the error.
model = genai.GenerativeModel('gemini-1.5-flash-latest')


# --- Streamlit App ---
# Set the title and icon that appear in the browser tab.
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

# Set the main title of the web app.
st.title("🤖 AI ChatBot")
# Add a caption for more context.
st.caption("A simple chatBot by Abubackar Siddiq")

# --- Session State Initialization ---
# "Session state" is Streamlit's way of remembering things.
# If we don't do this, the chat history would be lost every time the user sends a message.
# We initialize an empty list called "messages" to store the chat history.
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat History ---
# This loop goes through all the messages currently stored in the session state
# and displays them on the screen.
for message in st.session_state.messages:
    # st.chat_message creates a chat bubble.
    # The "role" determines if it's a user message or an assistant message.
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input and Chat Logic ---
# st.chat_input() creates a text box at the bottom of the screen for the user to type in.
# The message the user types is stored in the 'prompt' variable.
prompt = st.chat_input("What would you like to ask?")

# This 'if' statement checks if the user has typed something and pressed Enter.
if prompt:
    # 1. Add the user's message to our chat history in the session state.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 2. Display the user's message in a chat bubble.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Get the assistant's response.
    with st.chat_message("assistant"):
        try:
            # Send the user's prompt to the Gemini model.
            response = model.generate_content(prompt)
            # Get the text part of the response.
            full_response = response.text
            # Display the assistant's response.
            st.markdown(full_response)
            # 4. Add the assistant's response to our chat history.
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            # If something goes wrong, show an error message.
            st.error(f"An error occurred: {e}")
            # Also add an error message to the chat history.
            error_message = "Sorry, I encountered an error."
            st.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# --- End of the Streamlit app ---