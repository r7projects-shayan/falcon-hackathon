from ai71 import AI71
import os
from dotenv import load_dotenv

load_dotenv()

AI71_API_KEY = os.getenv("AI71_API_KEY")
client = AI71(AI71_API_KEY)

def get_ai71_response(user_input):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="tiiuae/falcon-180B-chat",
        stream=False,
    )

    return response.choices[0].message.content