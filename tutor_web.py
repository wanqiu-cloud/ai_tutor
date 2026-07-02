import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

st.set_page_config(page_title="AI学习助手", page_icon="🤖")
st.title("🤖 AI学习助手")
st.markdown("一个耐心的AI导师，随时解答你的编程和AI问题。")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个耐心的AI学习导师，专门帮助零基础学生学习编程和AI。你的回答要通俗易懂、鼓励性强，多用比喻来解释复杂概念。"}
    ]

for msg in st.session_state.messages:
    if msg["role"] in ["user", "system"]:
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])

if user_input := st.chat_input("在这里输入你的问题..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=st.session_state.messages
    )

    ai_reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})