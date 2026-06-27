from groq import Groq
from dotenv import load_dotenv
import os

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
        "content": "You are an expert Oracle ADF architect and Java developer.  When given ADF code, explain what it does in plain English. Cover: 1. What the code does 2. Which ADF concept it uses (taskflow, binding, iterator, etc.) 3. Any potential issues or improvements"
            
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