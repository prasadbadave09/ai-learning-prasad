from groq import Groq
from dotenv import load_dotenv
import json


def get_words_count(paragraph):
    words = paragraph.split()
    return len(words)

load_dotenv()
client = Groq()

word_count_tool = {
    "type": "function",
    "function": {
        "name": "get_words_count",
        "description": "Returns the total number of words in a given string.",
        "parameters": {
            "type": "object",
            "properties": {
                "paragraph": {
                    "type": "string",
                    "description": "The text to count words in"
                }
            },
            "required": ["paragraph"]
        }
    }
}

messages = [
    {"role": "user", "content": "How many words are in this sentence: Oracle ADF is a powerful enterprise framework for building applications?"}
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=[word_count_tool]
)

tool_call = response.choices[0].message.tool_calls[0]
args = json.loads(tool_call.function.arguments)

if tool_call.function.name == "get_words_count":
    result = get_words_count(args["paragraph"])
    print(f"Tool executed. Result: {result}")

print(response.choices[0].message)

messages.append(response.choices[0].message)  # the LLM's tool-call request
messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": str(result)
})

final_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=[word_count_tool]
)

print(final_response.choices[0].message.content)





