from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are a senior Oracle ADF architect helping a developer transition to AI engineering."
    }
]

print("AI Assistant ready. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Session ended.")
        break

    messages.append(

        {
            "role": "user",
            "content": user_input

        }

    )
    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",
        messages=messages

    )  

    print(response.choices[0].message.content)
    print()
    messages.append(

        {
            "role": "assistant",
            "content": response.choices[0].message.content

        }

    )
    
