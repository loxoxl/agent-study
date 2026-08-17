from agent import Agent
from tool import Tool

# 定义一个真实工具函数
def get_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

# 包装成Tool对象
time_tool = Tool("get_time",'获取当前时间', get_time)

# 注册到Agent
agent = Agent()
agent.register_tool(time_tool)

print(agent.get_tool_descriptions())  # 输出工具描述

print(time_tool.run())  # 调用工具函数，获取当前时间

