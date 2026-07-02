import streamlit as st
from openai import OpenAI

# 页面设置
st.set_page_config(page_title="AI学习助手", page_icon="🤖")
st.title("🤖 AI学习助手")
st.markdown("一个耐心的AI导师，随时解答你的编程和AI问题。")

# 配置客户端
client = OpenAI(
    api_key="sk-ws-H.RXLMHRH.9UIx.MEQCIDeKR8VeuSjdPu1_W02mtAG_A8ab3rtXSUwi4QNE5qdOAiAekK9PjRCAR4fHk932gUsIhYxv8TW5LNBtJt8W4C0R8w",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个耐心的AI学习导师，专门帮助零基础学生学习编程和AI。你的回答要通俗易懂、鼓励性强，多用比喻来解释复杂概念。"}
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
        model="qwen-plus-latest",
        messages=st.session_state.messages
    )
    
    ai_reply = response.choices[0].message.content
    
    # 显示AI回复
    with st.chat_message("assistant"):
        st.write(ai_reply)
    
    # 加入历史
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})