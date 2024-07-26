from openai import OpenAI


class ChatClient:
    def __init__(self, apikey: str, secret: str) -> None:
        self.apikey = apikey
        self.secret = secret
        self.client = OpenAI(
            # 控制台获取key和secret拼接，假使APIKey是key123456，APISecret是secret123456
            api_key=f"{apikey}:{secret}",
            base_url='https://spark-api-open.xf-yun.com/v1'  # 指向讯飞星火的请求地址
        )

    def generate_stream(self, content: str) -> str:
        completion = self.client.chat.completions.create(
            model='general',  # 指定请求的版本
            messages=[
                {
                    "role": "user",
                    "content": f'你是一位小红书生成器，请针对用户的关键词编写一篇小红书文案，需要符合小红书风格，需要包括标题、正文和标签三部分。用户关键词是：{content}'
                }
            ],
            stream=True
        )
        for chunk in completion:
            data = str(chunk.choices[0].delta.content)
            data = data.replace('\n', '<br>')
            yield data

    def generate(self, content: str) -> str:
        completion = self.client.chat.completions.create(
            model='general',  # 指定请求的版本
            messages=[
                {
                    "role": "user",
                    "content": f'你是一位小红书生成器，请针对用户的关键词编写一篇小红书文案，需要符合小红书风格，需要包括标题、正文和标签三部分。用户关键词是：{content}'
                }
            ],
        )
        return str(completion.choices[0].message.content)
