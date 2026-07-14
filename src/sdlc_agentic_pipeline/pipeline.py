from typing import TypedDict
from groq import Groq
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
import os

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

class GraphState(TypedDict):
    feature_request: str
    brd: str
    tech_spec: str
    epics: str
    stories: str

def brd_node(state: GraphState) -> GraphState:
    feature_request = state["feature_request"]

    messages = [
        {
            "role": "system",
            "content": "You are an expert business analyst who writes the BRD based on the given feature_request. Do not add any outside facts, context and be onpoint to feature request"
        },
        {
            "role": "user",
            "content": feature_request
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    brd = response.choices[0].message.content
    return {"brd": brd}



graph = StateGraph(GraphState)

graph.add_node("BRD", brd_node)

graph.set_entry_point("BRD")
graph.add_edge("BRD", END)

app = graph.compile()


result = app.invoke({"feature_request": "Add a search bar to the employee dashboard that lets HR staff quickly find employee records by name, department, or employee ID."})
print(result)