from memory import Memory

m = Memory(system_prompt="你是一个助手")
print(m.get_messages())

m2 = Memory('返回 JSON：{{"name": "test"}}')
print(m2.get_messages())