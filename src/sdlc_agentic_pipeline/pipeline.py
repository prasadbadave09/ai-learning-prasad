from typing import TypedDict
from groq import Groq
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


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
            "content": "You are an expert business analyst who writes the BRD based on the given feature_request. Do not add any outside facts, context and be onpoint to feature request",
        },
        {"role": "user", "content": feature_request},
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    brd = response.choices[0].message.content
    return {"brd": brd}


def tesc_spec_node(state: GraphState) -> GraphState:
    brd = state["brd"]

    messages = [
        {
            "role": "system",
            "content": "You are an expert technical architect who writes the techincal specifiaction document based on the given BRD. Do not add any outside facts, context and be onpoint to BRD",
        },
        {"role": "user", "content": brd},
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    tech_spec = response.choices[0].message.content
    return {"tech_spec": tech_spec}


def epeic_node(state: GraphState) -> GraphState:
    tech_spec = state["tech_spec"]

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert agile product owner who breaks down a technical "
                "specification into Epics. An Epic is a large body of work that can "
                "be broken down into smaller user stories. For each Epic, provide: "
                "a title, a short description, and its scope. "
                "Base the Epics ONLY on the given technical specification — "
                "do not invent scope or components not mentioned in it."
            ),
        },
        {"role": "user", "content": tech_spec},
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    epics = response.choices[0].message.content
    return {"epics": epics}


def story_node(state: GraphState) -> GraphState:
    epics_details = state["epics"]

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert agile product owner who breaks down Epics "
                "into user Stories. For each Story, provide: "
                "a title, the story in 'As a [role], I want [goal], so that [benefit]' format, "
                "and 2-3 acceptance criteria. "
                "Base the stories ONLY on the given epics — "
                "do not invent scope or components not mentioned in it."
            ),
        },
        {"role": "user", "content": epics_details},
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    stories = response.choices[0].message.content
    return {"stories": stories}


graph = StateGraph(GraphState)

graph.add_node("BRD", brd_node)
graph.add_node("Tech_Spec", tesc_spec_node)
graph.add_node("Epics", epeic_node)
graph.add_node("Stories", story_node)

graph.set_entry_point("BRD")
graph.add_edge("BRD", "Tech_Spec")
graph.add_edge("Tech_Spec", "Epics")
graph.add_edge("Epics", "Stories")
graph.add_edge("Stories", END)

app = graph.compile()


result = app.invoke(
    {
        "feature_request": "Add a search bar to the employee dashboard that lets HR staff quickly find employee records by name, department, or employee ID."
    }
)
print(result)
