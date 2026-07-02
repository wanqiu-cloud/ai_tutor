import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = os.getenv("GEMINI_BASE_URL")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个可爱的ai，你会耐心、善于用比喻的老师，你的回答的最后一个字总是带个喵，你会很关心使用者的心情。"}
    ]

# 显示历史消息
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])

# 接收用户输入
if user_input := st.chat_input("在这里输入你的问题..."):
    # 显示用户消息
    with st.chat_message("user"):
        st.write(user_input)
    
    # 加入历史
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 调用大模型
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=st.session_state.messages
    )
    
    ai_reply = response.choices[0].message.content
    
    # 显示AI回复
    with st.chat_message("assistant"):
        st.write(ai_reply)
    
    # 加入历史
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})