from llm import chat

# 初始化消息，设置agent身份
messages = [{
    "role": "system",
    "content": "你是一个由爵特猛开发的agent, 你会尽力回答用户的问题。"
}]

while True:
    # 获取用户输入
    user_input = input("👤 你：")

    # 检查用户是否输入了退出命令
    if user_input.lower() == "exit":
        print("退出对话。")
        break

    if not user_input.strip():
        print("❌ 输入不能为空，请重新输入。")
        continue
        
    # 将用户输入添加到消息列表中
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # 调用chat函数获取大模型响应
        response = chat(messages)
    except Exception as e:
        # 处理异常并打印错误信息
        print(f"❌ 出现错误：{e}")
        continue

    if not response.strip():
        print("❌ 大模型未返回有效响应，请重试。")
        continue
    
    # 将大模型响应添加到消息列表中
    messages.append({
        "role": "assistant",
        "content": response
    })

    # 打印大模型响应
    print(f"🤖 爵特猛bot：{response}")