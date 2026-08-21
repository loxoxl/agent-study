from agent import Agent
import logging
from tool import Tool
import sys

# 设置日志级别为INFO，方便查看日志输出
logging.basicConfig(level=logging.INFO)

# 重新配置标准输出为UTF-8编码，确保在控制台正确显示中文字符
sys.stdout.reconfigure(encoding='utf-8')

# 系统提示词
system_prompt = "你是一个由{author}开发的agent, 你会尽力回答用户的问题"

agent = Agent(system_prompt=system_prompt)
# 设置提示词里的变量
agent.set_variable("author", "爵特猛")
# agent.set_variable("date", date.today().strftime("%Y-%m-%d"))

# 定义一个时间工具函数
def get_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 注册时间工具，包装成Tool对象
agent.register_tool(Tool('get_time', '获取当前时间', get_time))

while True:
    # 获取用户输入
    user_input = input("👤 你：")

    # 检查用户是否输入了退出命令
    if user_input.lower() == "exit" or user_input.lower() == "退出":
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
