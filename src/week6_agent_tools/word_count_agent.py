from groq import Groq
from dotenv import load_dotenv
import json
import re

def check_table_naming_convention(name: str) -> dict:
    if " " in name:
        return {
            "valid": False,
            "message": "Entity Object name should not contain spaces."
        }

    pattern = r"^[A-Z][a-zA-Z0-9]*EO$"

    if not re.match(pattern, name):
        return {
            "valid": False,
            "message": (
                "Entity Object name must follow PascalCase and end with 'EO'. "
                "Example: EmployeeEO"
            )
        }

    return {
        "valid": True,
        "message": "Valid Entity Object name."
    }


check_table_naming_convention_tool = {
    "type": "function",
    "function": {
        "name": "check_table_naming_convention",
        "description": (
            "Validates Oracle ADF Entity Object (EO) naming convention ONLY. "
            "Checks that the name follows PascalCase and ends with 'EO' suffix "
            "(e.g. EmployeeEO). Do NOT use this for View Objects (VO), "
            "Application Modules (AM), or any other ADF component type — "
            "this tool only validates Entity Objects."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The Entity Object name to validate, e.g. EmployeeEO"
                }
            },
            "required": ["name"]
        }
    }
}

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
    {"role": "system", "content": "Use tools when needed to answer the user's question."},
    {"role": "user", "content": "How many words are in this sentence: I am Petter Parker"}
]

while True:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=[word_count_tool, check_table_naming_convention_tool]
    )

    message = response.choices[0].message
    messages.append(message)

    if not message.tool_calls:
        # No more tool calls needed - this is the final answer
        print(message.content)
        break

    # Execute each requested tool call
    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)

        if tool_call.function.name == "get_words_count":
            result = get_words_count(args["paragraph"])
        elif tool_call.function.name == "check_table_naming_convention":
            result = check_table_naming_convention(args["name"])

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })







