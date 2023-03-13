import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_answer(info):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role":"user",
                "content": info
            }
        ]
    )
    return completion['choices'][0]['message']['content']


if __name__ == '__main__':
    ans = get_answer('写一篇科幻小说')
    print(ans)
