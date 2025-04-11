# CLAT Chatbot Prototype 🤖📚

This is a simple rule-based/NLP-powered chatbot built to answer CLAT (Common Law Admission Test)–related queries using a basic knowledge base and Streamlit interface. 

---

## 🚀 Features

- Accepts user queries related to CLAT.
- Responds with relevant answers using a preprocessed knowledge base (`clat_kb.pkl`).
- Simple Streamlit frontend for interactive Q&A.
- Easy to expand with more FAQs or upgraded to GPT-based model.

---

## 💡 Sample Queries

- "What is the syllabus for CLAT 2025?"
- "How many questions are there in the English section?"
- "What was the cut-off for NLSIU Bangalore last year?"
- "Is there negative marking in CLAT?"

---

## 🧠 Architecture

- `streamlit_app.py`: Main Streamlit app to interact with user.
- `clat_kb.pkl`: Preprocessed dictionary-style knowledge base using keywords and sample responses.
- Uses basic NLP via keyword matching (can be extended using spaCy/NLTK/transformers).

---

## 🛠️ Setup Instructions

1. ### Clone the Repository:
   ```bash
   git clone https://github.com/Ron5866/chat_bot.git
   cd chat_bot
   ```
   
2. ### Create a Virtual Environment (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. ### Install Requirements:
   ```bash:
   pip install -r requirements.txt  # Or manually install streamlit, pickle5 if not already installed
   ```

4. ### Run the Streamlit App:
   ```bash:
   streamlit run streamlit_app.py
   ```

## 📦 Files
File	                 Description
streamlit_app.py   	 Main chatbot code
clat_kb.pkl	         Knowledge base(preprocessed)
.idea/	             IDE config(can be ignored)

## 📈 Future Scope
Upgrade to GPT-based chatbot fine-tuned on NLTI content.

Add semantic search using embeddings.

Store query history and analytics.

## 📬 Contact
Project by Ron5866

