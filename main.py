from agent import Agent

agent = Agent()

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

    agent_response = agent.chat(user_input)
    if agent_response is None:
        print("❌ 大模型未返回有效响应，请重试。")
        continue

    # 打印大模型响应
    print(f"🤖 爵特猛bot：{agent_response}")
