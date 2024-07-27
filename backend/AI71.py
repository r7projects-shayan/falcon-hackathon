from ai71 import AI71
import os
from dotenv import load_dotenv

load_dotenv()

AI71_API_KEY = os.getenv("AI71_API_KEY")
client = AI71(AI71_API_KEY)

# Streaming chatbot:
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    content = input(f"User:")
    messages.append({"role": "user", "content": content})
    print(f"Falcon:", sep="", end="", flush=True)
    content = ""

    for chunk in client.chat.completions.create(
        messages=messages,
        model="tiiuae/falcon-180B-chat",
        stream=True,
    ):
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            print(delta_content, sep="", end="", flush=True)
            content += delta_content
    
    messages.append({"role": "assistant", "content": content})
    print("\n")