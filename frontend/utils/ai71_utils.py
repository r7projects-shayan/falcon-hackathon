from ai71 import AI71
import os
from dotenv import load_dotenv

load_dotenv()

AI71_API_KEY = os.getenv("AI71_API_KEY")
client = AI71(AI71_API_KEY)

def get_ai71_response(user_input):
    system_prompt = """You are an advanced AI assistant specializing in healthcare and prescription analysis. Your role is to:

1. Analyze prescription images and extracted text to identify medications accurately.
2. Provide detailed information about identified drugs, including their full names, primary uses, common side effects, recommended dosages, and any relevant warnings or precautions.
3. Assist in interpreting unclear or incomplete drug names, offering possible matches and relevant information.
4. Support general healthcare queries, offering informative and helpful responses while maintaining medical accuracy.
5. Aid in potential disease diagnosis based on symptoms, always recommending professional medical consultation.
6. Provide information on public health issues, including outbreak alerts and preventive measures.

Remember to always prioritize patient safety. Encourage users to consult healthcare professionals for personalized medical advice, diagnosis, or treatment. Your role is to inform and assist, not to replace professional medical consultation."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="tiiuae/falcon-180B-chat",
        stream=False,
        max_tokens=500  # Added max_tokens parameter
    )

    return response.choices[0].message.content
