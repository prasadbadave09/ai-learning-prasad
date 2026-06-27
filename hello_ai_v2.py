from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant for an enterprise Java developer learning AI."
        },
        {
            "role": "user",
            "content": "What is Oracle ADF and how is it different from modern web frameworks?"
        }
    ]
)

print(response.choices[0].message.content)