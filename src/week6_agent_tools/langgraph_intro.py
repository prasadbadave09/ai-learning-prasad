from typing import TypedDict
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

class GraphState(TypedDict):
    topic: str
    research_notes: str
    summary: str

def research_node(state: GraphState) -> GraphState:
    topic = state["topic"]

    messages = [
        {
            "role": "system",
            "content": "You are an expert researcher who researches the given topic and prepares detailed notes."
        },
        {
            "role": "user",
            "content": topic
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    research_notes = response.choices[0].message.content
    return {"research_notes": research_notes}

def summarize_node(state: GraphState) -> GraphState:
    research_notes = state["research_notes"]

    messages = [
        {
            "role": "system",
            "content": "You are an expert summarizer. Summarize ONLY the information contained in the provided research notes. Do not add any outside facts, context, or knowledge not present in the notes."
        },
        {
            "role": "user",
            "content": research_notes
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    research_summary = response.choices[0].message.content
    return {"summary": research_summary}

from langgraph.graph import StateGraph, END

graph = StateGraph(GraphState)

graph.add_node("research", research_node)
graph.add_node("summarize", summarize_node)

graph.set_entry_point("research")
graph.add_edge("research", "summarize")
graph.add_edge("summarize", END)

app = graph.compile()


result = app.invoke({"topic": "Oracle ADF"})
print(result)