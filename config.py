import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

AUTHOR = os.getenv("AUTHOR", "默认作者")

BOT_NAME = os.getenv("BOT_NAME", "智能AI助手")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

BASE_URL = "https://api.deepseek.com"

MODEL_NAME = "deepseek-v4-flash"

AGENT_DEBUG = os.getenv("AGENT_DEBUG", "0")  # 默认关闭调试模式
