import llm
import memory

class Agent:
    # 初始化Agent类，设置系统提示和内存
    def __init__(self, system_prompt="你是一个乐于助人的助手, 你会尽力回答用户的问题"):
        self.memory = memory.Memory(system_prompt=system_prompt)

    # 聊天函数，处理用户输入并返回大模型响应
    def chat(self, user_input):
        
        # 将用户输入添加到临时消息列表中
        temp_messages = self.memory.get_messages() + [{
            "role": "user",
            "content": user_input
        }]

        try:
            # 调用chat函数获取大模型响应
            response = llm.chat(temp_messages)
        except Exception:
            return None
        
        if not response.strip():
            return None
        
        # 将用户输入添加到消息列表中
        self.memory.add("user", user_input)

        # 将大模型响应添加到消息列表中
        self.memory.add("assistant", response)

        return response

    def set_variable(self, key, value):
        # 设置变量
        self.memory.set_variable(key, value)
