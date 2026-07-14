from typing import TypedDict

class GraphState(TypedDict):
    topic: str
    research_notes: str
    summary: str

def research_node(state: GraphState) -> GraphState:
    topic = state["topic"]
    # For now, fake the "research" - just simulate it
    fake_research = f"Some research notes about {topic}: Oracle ADF is a Java framework for enterprise applications."
    return {"research_notes": fake_research}    

def summarize_node(state: GraphState) -> GraphState:
    research_notes = state["research_notes"]
    fake_summary = f"Summary: {research_notes[:50]}..."
    return {"summary": fake_summary}

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