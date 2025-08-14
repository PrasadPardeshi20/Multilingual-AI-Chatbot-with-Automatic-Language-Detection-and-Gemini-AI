import streamlit as st
from langdetect import detect
from googletrans import Translator
import google.generativeai as genai
import os


st.set_page_config(page_title="Multilingual Chatbot", page_icon="🌐", layout="centered")

# Gemini API key
API_KEY = ""

if not API_KEY:
    API_KEY = st.text_input("🔑 Enter your Gemini API Key:", type="password")

if API_KEY:
    genai.configure(api_key=API_KEY)

# Translator setup
translator = Translator()


st.markdown("<h1 style='text-align:center;'>🌐 Multilingual Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>English 🇺🇸 • Hindi 🇮🇳 • Spanish 🇪🇸 • Tamil 🇱🇰</p>", unsafe_allow_html=True)
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_gemini_reply(user_input, lang_code):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"You are a helpful and culturally aware assistant. Reply in {lang_code} language. User said: {user_input}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div style='text-align:right; background-color:#0078D4; color:white; padding:8px; border-radius:12px; margin:4px 0;'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align:left; background-color:#EAEAEA; color:black; padding:8px; border-radius:12px; margin:4px 0;'>{msg['content']}</div>", unsafe_allow_html=True)


user_input = st.text_input("💬 Type your message:", key="user_input")
if st.button("Send") and user_input:
    # Detect language
    detected_lang = detect(user_input)
    
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get bot reply
    bot_reply = get_gemini_reply(user_input, detected_lang)
    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    
    st.rerun()

