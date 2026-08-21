from agent import Agent
from tool import Tool
import logging

# 设置日志级别为INFO，方便查看日志输出
logging.basicConfig(level=logging.INFO)

# 定义一个真实工具函数
def get_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 包装成Tool对象
time_tool = Tool("get_time",'获取当前时间', get_time)

# 注册到Agent
agent = Agent()
agent.register_tool(time_tool)

# print(agent.get_tools_schema())  # 输出工具schema

# print(time_tool.run())  # 调用工具函数，获取当前时间

print(agent.chat("现在几点了"))  # 使用Agent进行对话，获取大模型响应

