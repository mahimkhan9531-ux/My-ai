import streamlit as st
from duckduckgo_search import DDGS

# --- Master Admin Configuration ---
MASTER_NAME = "Mahim khan"

st.set_page_config(page_title="Master AI", page_icon="🧠", layout="wide")

# Custom UI for a 'Best AI' feel
st.markdown(f"<h1 style='text-align: center; color: #00FFAA;'>👑 {MASTER_NAME}'s Brain AI</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Unlimited Web Search Brain
def agentic_search(query):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=7)]
        return results

# Chat Interface
user_input = st.chat_input("Command the World's Best AI...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.spinner("Analyzing Global Data..."):
        try:
            search_data = agentic_search(user_input)
            response = f"Master {MASTER_NAME}, I have scanned the web. Here is the best information:\n\n"
            for res in search_data:
                response += f"📍 **{res['title']}**\n{res['body']}\n\n"
        except Exception as e:
            response = "Master, there was a temporary neural block. Please try again."
            
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display Chat
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])
