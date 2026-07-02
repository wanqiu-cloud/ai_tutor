from openai import OpenAI

# 配置阿里云百炼
client = OpenAI(
    api_key="sk-ws-H.RXLMHRH.9UIx.MEQCIDeKR8VeuSjdPu1_W02mtAG_A8ab3rtXSUwi4QNE5qdOAiAekK9PjRCAR4fHk932gUsIhYxv8TW5LNBtJt8W4C0R8w",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

print("=" * 50)
print("🤖 AI学习助手已上线！输入'退出'结束对话")
print("=" * 50)

# 保存对话历史，让AI记住上下文
messages = [
    {"role": "system", "content": "你是一个耐心的AI学习导师，专门帮助零基础学生学习编程和AI。你的回答要通俗易懂、鼓励性强，多用比喻来解释复杂概念。"}
]

while True:
    # 获取用户输入
    user_input = input("\n🧑 你：")
    
    # 检查是否退出
    if user_input.lower() == "退出":
        print("\n👋 AI学习助手：加油，下次再见！")
        break
    
    # 把用户消息加入对话历史
    messages.append({"role": "user", "content": user_input})
    
    # 调用大模型
    response = client.chat.completions.create(
        model="qwen-plus-latest",
        messages=messages
    )
    
    # 获取AI回复
    ai_reply = response.choices[0].message.content
    
    # 把AI回复也加入对话历史
    messages.append({"role": "assistant", "content": ai_reply})
    
    # 打印回复
    print(f"\n🤖 AI导师：{ai_reply}")