from typing import Generator
from openai import OpenAI


class ChatClient:
    def __init__(self, base_url: str, apikey: str, model: str) -> None:
        self.base_url = base_url
        self.apikey = apikey
        self.model = model
        self.client = OpenAI(
            api_key=self.apikey,
            base_url=self.base_url
        )
        print(self.client.base_url, self.model)

    def generate_stream(self, content: str) -> Generator:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f'你是一位小红书生成器，请针对用户的关键词编写一篇小红书文案，需要符合小红书风格，需要包括标题、正文和标签三部分。用户关键词是：{content}'
                }
            ],
            top_p=0.7,
            temperature=0.9,
            stream=True
        )
        for chunk in completion:
            data = str(chunk.choices[0].delta.content)
            data = data.replace('\n', '<br>')
            yield data

    def generate(self, content: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,  # 指定请求的版本
            messages=[
                {
                    "role": "user",
                    "content": f'你是一位小红书生成器，请针对用户的关键词编写一篇小红书文案，需要符合小红书风格，需要包括标题、正文和标签三部分。用户关键词是：{content}'
                }
            ],
            top_p=0.7,
            temperature=0.9,
        )
        return str(completion.choices[0].message.content)
