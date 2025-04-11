# clat_chatbot_streamlit.py
import streamlit as st
import pickle

# Load the knowledge base
with open("clat_kb.pkl", "rb") as f:
    kb = pickle.load(f)

# Matching function
def get_response(query):
    query = query.lower()
    for key in kb:
        if all(word in query for word in key.split()):
            return kb[key]
    return "❓ Sorry, I don't have an answer for that. Try asking differently."

# Streamlit UI
st.title("🧠 CLAT FAQ Chatbot")
st.write("Ask me anything about CLAT 2025!")

query = st.text_input("Your question")

if query:
    response = get_response(query)
    st.success(response)
