import llm
import memory

class Agent:
    def __init__(self, system_prompt="你是一个由爵特猛开发的agent, 你会尽力回答用户的问题。"):
        # 初始化Agent类，设置系统提示和内存
        self.memory = memory.Memory(system_prompt=system_prompt)

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
