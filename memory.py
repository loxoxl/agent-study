from string import Formatter

class Memory:
    # 初始化Memory类
    def __init__(self, system_prompt, max_messages=20, variables=None):
        # 设置系统提示
        self.system_prompt = system_prompt
        # 初始化消息列表
        self.history = []
        # 设置最大消息数量
        self.max_messages = max_messages

        # 初始化变量字典
        # 1. 找出模板里所有占位符
        fields = [item[1] for item in Formatter().parse(system_prompt) if item[1] is not None]

        # 2. 给每个占位符一个默认值（空字符串）
        self.variables = {field: "" for field in fields}

        # 3. 如果调用时传了 variables，覆盖默认值
        if variables:
            self.variables.update(variables)

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
        # 所有占位符都有默认值，永远不会 KeyError
        system_prompt = self.system_prompt.format(**self.variables)
        return [{"role": "system", "content": system_prompt}] + self.history

    # 清空消息列表
    def clear(self):
        self.history = []

    # 设置变量
    def set_variable(self, key, value):
        self.variables[key] = value