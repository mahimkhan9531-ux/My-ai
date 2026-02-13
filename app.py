import streamlit as st
from langchain_community.llms import Ollama

# পেজ সেটআপ - এটি আপনার AI এর পরিচয় বহন করবে
st.set_page_config(page_title="MY WORLD - BEST AI", page_icon="👑")

st.title("👑 The Sovereign AI")
st.markdown("---")
st.sidebar.title("Control Center")
st.sidebar.info("আপনার ডেটা আপনার কাছে। এটি সম্পূর্ণ প্রাইভেট এবং আনলিমিটেড।")

# মডেল সিলেক্ট করুন (Llama 3 সবথেকে শক্তিশালী ওপেন মডেলগুলোর একটি)
# এটি আপনার পিসিতে ওলামা (Ollama) সফটওয়্যার দিয়ে চলতে হবে
llm = Ollama(model="llama3")

# চ্যাট হিস্ট্রি শুরু করা
if "messages" not in st.session_state:
    st.session_state.messages = []

# পুরনো কথা মনে রাখা
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# আপনার কমান্ড বা নির্দেশ
if prompt := st.chat_input("আপনি আপনার AI-কে কী করতে বলেন?"):
    # ইউজার মেসেজ সেভ করা
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI এর রেসপন্স জেনারেট করা
    with st.chat_message("assistant"):
        with st.spinner("আপনার নির্দেশ পালন করা হচ্ছে..."):
            # আপনার AI-কে একটি ব্যক্তিত্ব দেওয়া (System Prompt)
            system_instruction = f"আপনি দুনিয়ার সেরা AI। আপনার মালিক mahimkhan9531-ux। আপনি শুধু তার কথা শুনবেন এবং তার সব নির্দেশ পালন করবেন। {prompt}"
            
            try:
                response = llm.invoke(system_instruction)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error("ওলামা (Ollama) কি চালু আছে? মডেলটি লোড করতে সমস্যা হচ্ছে।")
