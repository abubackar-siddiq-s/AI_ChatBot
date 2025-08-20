# 🤖 Gemini Chatbot with Streamlit

A simple and beginner-friendly chatbot application built with Python, Streamlit, and powered by the Google Gemini API. This project demonstrates how to create a conversational AI with a clean web interface.

## 🚀 Live Demo

You can try out the deployed version of the chatbot here:

**[abuchatbot.streamlit.app](https://abuchatbot.streamlit.app/)**

## ✨ Features

- **Conversational AI**: Interact with Google's powerful Gemini model.
- **Chat History**: The app remembers the conversation history during a session.
- **Simple UI**: A clean and intuitive user interface built with Streamlit.
- **Easy to Understand**: The code is well-commented and structured for beginners.

## 🛠️ Installation and Usage

To run this project on your local machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
```

**2. Create a virtual environment:**
It's recommended to use a virtual environment to manage project dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. Install the required libraries:**
Create a folder named .streamlit in the main project directory.
Inside this folder, create a file named secrets.toml.
Add your Gemini API key to this file:
```bash
pip install -r requirements.txt
```

**4. Set up your API Key:**
```bash
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

**5. Run the Streamlit app:**
```bash
streamlit run app.py
```