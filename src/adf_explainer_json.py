from groq import Groq
from dotenv import load_dotenv
import os
import json

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
        "content":"""You are an expert Oracle ADF architect. 
Analyze the given ADF Java code and respond ONLY with a valid JSON object.
No explanation text before or after. No markdown code blocks. Just raw JSON.

Use exactly this structure:
{
  "component_type": "",
  "methods": [
    {
      "name": "",
      "description": "",
      "adf_concept": "",
      "issues": []
    }
  ],
  "overall_risk": "Low/Medium/High",
  "recommendation": ""
}"""
            
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
raw = response.choices[0].message.content
# Strip markdown backticks if present
raw = raw.strip().replace("```json", "").replace("```", "").strip()
parsed = json.loads(raw)
print(json.dumps(parsed, indent=2))