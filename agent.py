import llm
import memory
import logging
import json

# 创建 logger（名字用模块名，方便知道日志来自哪个文件）
logger = logging.getLogger(__name__)

class Agent:
    # 初始化Agent类，设置系统提示和内存
    def __init__(self, system_prompt="你是一个乐于助人的助手, 你会尽力回答用户的问题"):
        self.memory = memory.Memory(system_prompt=system_prompt)
        self.tools = {}

    # 聊天函数，处理用户输入并返回大模型响应
    def chat(self, user_input):
        
        # 将用户输入添加到临时消息列表中
        temp_messages = self.memory.get_messages() + [{
            "role": "user",
            "content": user_input
        }]

        # 最多问 5 轮，防 AI 发疯
        for _ in range(5):
            try:
                # 调用chat函数获取大模型响应
                chat_result = llm.chat(temp_messages, tools=self.get_tools_schema())
            except Exception:
                logger.exception("调用大型语言模型时发生错误")
                return None
    
            # 返回的文字内容
            chat_content = chat_result.get('content', '')
            # 返回的工具调用信息
            tool_calls = chat_result.get('tool_calls', [])
    
            # 如果有工具调用，处理工具调用逻辑
            if tool_calls:
                temp_messages.append({
                    "role": "assistant",
                    "content": chat_content,
                    "tool_calls": tool_calls
                })
                for tool_call in tool_calls:
                    tool_id = tool_call.get('id')
                    tool_function = tool_call.get('function')
                    tool_function_name = tool_function.get('name')
                    tool_function_args = json.loads(tool_function.get('arguments', '{}'))
    
                    if tool_function_name in self.tools:
                        try:
                            # 调用工具函数
                            tool_result = self.tools[tool_function_name].run(**tool_function_args)
                            
                            # 将工具调用结果添加到临时消息列表中，以便大模型可以看到
                            temp_messages.append({
                                "role": "tool",
                                "tool_call_id": tool_id,
                                "content": f"工具 {tool_function_name} 的调用结果: {tool_result}"
                            })
                        except Exception as e:
                            logger.exception(f"调用工具 {tool_function_name} 时发生错误")
                            
                            temp_messages.append({
                                "role": "tool",
                                "tool_call_id": tool_id,
                                "content": f"工具 {tool_function_name} 的调用失败: {str(e)}"
                            })

            # AI返回内容了
            if chat_result["content"]:
                # 将用户输入添加到消息列表中
                self.memory.add("user", user_input)
                # 将大模型响应添加到消息列表中
                self.memory.add("assistant", chat_content)
                return chat_content
    

        logger.warning("大模型未返回有效响应")
        return None


    # 设置变量
    def set_variable(self, key, value):
        self.memory.set_variable(key, value)

    # 注册工具
    def register_tool(self, tool):
        self.tools[tool.name] = tool

    # 返回所有工具的schema，用于给LLM提供工具信息
    def get_tools_schema(self):
        tools = []
        for name, tool in self.tools.items():
            tools.append({
                "type": "function",
                "function": {
                    "name": name,
                    "description": tool.description,
                    "parameters": tool.parameters
                }
            })

        return tools
