import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

BASE_URL = "https://api.deepseek.com"

MODEL_NAME = "deepseek-v4-flash"
