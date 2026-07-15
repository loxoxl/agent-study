class Memory:
    def __init__(self, system_prompt, max_messages=20):
        self.system_prompt = system_prompt
        self.history = []
        self.max_messages = max_messages

    # 添加消息
    def add(self, role, content):
        # 将消息添加到消息列表中
        self.history.append({
            "role": role,
            "content": content
        })
        # 限制消息数量
        if len(self.history) > self.max_messages:
            self.history.pop(0)

    # 获取消息列表
    def get_messages(self):
        return [{"role": "system", "content": self.system_prompt}] + self.history

    # 清空消息列表
    def clear(self):
        self.history = []