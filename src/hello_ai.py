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
            "content": "Explain what an LLM is in 3 sentences, simply."
        }
    ]
)

print(response.choices[0].message.content)