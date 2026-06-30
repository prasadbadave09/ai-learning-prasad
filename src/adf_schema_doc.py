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
        "content": "You are an expert Oracle ADF architect, ADF documentation expert and PLSQL expert.  When given SQL, explain what it does in plain English. Cover: 1. Table purpose 2. Each column — what it likely represents in ADF context 3. Recommended ViewObject name 4.Recommended ADF binding type for each column "
            
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