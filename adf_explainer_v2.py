from groq import Groq
from dotenv import load_dotenv
import os
from prompt_library import get_adf_explainer_prompt
load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

print("Paste your ADF code below. Type 'END' on a new line when done:")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)
code = "\n".join(lines)

messages = [
    {
        "role": "system",
        "content": get_adf_explainer_prompt()
            
    },
    {
        "role": "user",
        "content": code
    }
    
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages



)
print(response.choices[0].message.content)