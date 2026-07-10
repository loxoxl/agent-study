import config
from openai import OpenAI

client = OpenAI(
    api_key=config.DEEPSEEK_API_KEY,
    base_url=config.BASE_URL
    )


def chat(messages:list) -> str:
    response = client.chat.completions.create(
        model=config.MODEL_NAME,
        messages=messages
    )
    return response.choices[0].message.content

