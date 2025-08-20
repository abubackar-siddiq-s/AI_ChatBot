🤖 AI Chatbot
A simple and beginner-friendly chatbot application built with Python, Streamlit, and powered by the Google Gemini API. This project demonstrates how to create a conversational AI with a clean web interface.

🚀 Live Demo
You can try out the deployed version of the chatbot here:

abuchatbot.streamlit.app

✨ Features
Conversational AI: Interact with Google's powerful Gemini model.

Chat History: The app remembers the conversation history during a session.

Simple UI: A clean and intuitive user interface built with Streamlit.

Easy to Understand: The code is well-commented and structured for beginners.

🛠️ Installation and Usage
To run this project on your local machine, follow these steps:

1. Clone the repository:

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

2. Create a virtual environment:
It's recommended to use a virtual environment to manage project dependencies.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required libraries:

pip install -r requirements.txt

4. Set up your API Key:

Create a folder named .streamlit in the main project directory.

Inside this folder, create a file named secrets.toml.

Add your Gemini API key to this file:

GEMINI_API_KEY = "YOUR_API_KEY_HERE"

5. Run the Streamlit app:

streamlit run app.py

The application should now be running in your web browser!

📂 Files in this Repository
app.py: The main Python script that contains all the Streamlit application code and logic for interacting with the Gemini API.

requirements.txt: A list of all the Python libraries required to run the application.

.gitignore: Specifies which files and directories should be ignored by Git, such as the secrets file and virtual environment folders.

This project was created as a simple introduction to building LLM-powered applications with Streamlit.