import config
import logging
from openai import OpenAI
import json

# 创建 logger（名字用模块名，方便知道日志来自哪个文件）
logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=config.DEEPSEEK_API_KEY,
    base_url=config.BASE_URL
    )


def chat(messages:list, tools=None) -> dict:
    # 截取最后2条消息，用于存储日志
    message_last_2 = messages[-2:]
    # 在发送请求前记录日志，包含消息和工具信息
    logger.info(f"LLM请求数据: {json.dumps(message_last_2, ensure_ascii=False)} and tools: {json.dumps(tools, ensure_ascii=False)}")

    response = client.chat.completions.create(
        model=config.MODEL_NAME,
        messages=messages,
        tools=tools
    )

    content = response.choices[0].message.content
    tool_calls = response.choices[0].message.tool_calls

    if tool_calls:
        tool_calls = [t.model_dump() for t in tool_calls]

    result = {'content': content, 'tool_calls': tool_calls}

    logger.info(f"LLM返回结果: {json.dumps(result, ensure_ascii=False)}")

    return result

