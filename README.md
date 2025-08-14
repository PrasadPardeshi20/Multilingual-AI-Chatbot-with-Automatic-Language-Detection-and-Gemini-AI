# 🌐 Multilingual AI Chatbot
**English 🇺🇸 • Hindi 🇮🇳 • Spanish 🇪🇸 • Tamil 🇱🇰**

---

## 📌 Project Overview
This project is a **Multilingual AI-powered chatbot** built using **Google Gemini API** that supports English, Hindi, Spanish, and Tamil.  
It automatically detects the user’s language, processes the query using **Gemini AI**, and responds in the **same language** as the input.

Designed for **free-flow human-like conversation**, the chatbot can seamlessly switch between languages during the chat while keeping the context.  
The application is built using **Streamlit** for a smooth and interactive interface.

---

## 🚀 Features
- **Automatic Language Detection** using `langdetect`
- **4 Supported Languages**: English 🇺🇸, Hindi 🇮🇳, Spanish 🇪🇸, Tamil 🇱🇰
- **Gemini AI Integration** for intelligent, context-aware responses
- **Real-Time Translation** using `googletrans`
- **Seamless Language Switching** during conversation
- **Streamlit UI** with chat history

---

## 🛠️ Installation

1. **Clone this repository:**
```bash
git clone <your_repo_link>
cd Task5_Multilingual_Chatbot

2.  **Install dependencies:**
pip install -r requirements.txt

3. **Set up API Key

Get your Gemini API key from Google AI Studio.
here the link : https://aistudio.google.com/app/u/1/apikey
Create a file .streamlit/secrets.toml in the project folder and add:**
🔑 Enter your Gemini API Key: 'Your Api Key

## ▶️ Run the Application
cd <your folder location>
streamlit run app.py


## ScreenShots :


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/296b24e1-b1fc-43d6-890e-657dfcdbb9be" />

## 📊 Tech Stack

Python 🐍

Streamlit (Web UI)

Google Gemini API (AI Model)

langdetect (Language Detection)

googletrans (Translation)

## 🧪 Testing

To verify functionality:

Ask questions in English, Hindi, Spanish, Tamil

Switch languages mid-conversation

Check for correct and context-aware replies

Example Queries:

English: "Who is the Prime Minister of India?"

Hindi: "भारत की आज़ादी कब हुई थी?"

Spanish: "¿Cuál es la capital de España?"

Tamil: "இந்தியா எப்போது சுதந்திரம் பெற்றது?"
