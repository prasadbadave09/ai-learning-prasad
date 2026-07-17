# SDLC Agentic Pipeline

A 4-node LangGraph pipeline that takes a plain-English feature request and 
progressively transforms it into a Business Requirements Document (BRD), 
Technical Specification, Epics, and User Stories — using Groq 
(llama-3.3-70b-versatile) at each stage, with each stage grounded strictly 
in the output of the previous one.

This is a Python re-implementation of the multi-agent SDLC concept from the 
Glean Enterprise AI project, built to understand the underlying mechanics 
(state, nodes, edges) rather than relying on a pre-built platform.

## How it works

The pipeline is a linear LangGraph graph with 4 nodes, each responsible for 
one stage:

1. **BRD node** — takes a `feature_request` string, generates a Business 
   Requirements Document. Grounded strictly to the feature request — 
   no invented scope.
2. **Tech Spec node** — takes the BRD's output, generates a Technical 
   Specification. Grounded to the BRD's content.
3. **Epics node** — takes the Tech Spec, breaks it into Epics (title, 
   description, scope), grouped by system component.
4. **Story node** — takes the Epics, breaks each into User Stories in 
   standard "As a [role], I want [goal], so that [benefit]" format, 
   with acceptance criteria.

State (`GraphState`) flows through all 4 nodes: each node reads what it 
needs from state, and returns only the field it updates — LangGraph merges 
this into the growing state object automatically.

## Setup

pip install langgraph groq python-dotenv

Create a `.env` file with:
GROQ_API_KEY=your_groq_api_key_here

## Usage

python pipeline.py

Currently the feature request is hardcoded in the `app.invoke(...)` call 
at the bottom of the script. Edit that string to try a different feature.

## Example run

**Input feature request:**
"Add a search bar to the employee dashboard that lets HR staff quickly 
find employee records by name, department, or employee ID."

**Output:** BRD → Tech Spec → 8 Epics → 16 User Stories (2 per Epic), 
all traceable back to the original feature request with no invented scope. 
See a full sample run in [sample_output.md](./sample_output.md) 
*(optional — add if you want to include the full text)*.

## Known Limitations / Lessons Learned

### 1. Ungrounded LLM nodes can hallucinate confidently, with zero warning signal

Early in development, the `research_node` (from an earlier LangGraph 
experiment reused here) was tested with two topics:

- **"Oracle ADF"** — produced accurate, correct output matching real 
  domain knowledge.
- **"LangGraph"** — produced entirely fabricated content, describing 
  LangGraph as "a transformer-based language model with an encoder/decoder 
  architecture," which is false — LangGraph is a workflow orchestration 
  framework, not a language model.

Both answers were delivered with identical confidence — no hedging, 
nothing to distinguish the accurate answer from the hallucinated one.

**Implication:** every node in this pipeline is explicitly grounded — 
each node's system prompt instructs it to work "ONLY" from the given 
upstream input (feature request → BRD → Tech Spec → Epics → Stories), 
never from the model's own general knowledge about the topic. This was 
a deliberate design choice made directly because of this finding.

### 2. Reasonable technical elaboration vs. fabricated specifics

The Tech Spec node adds real implementation detail not literally stated 
in the BRD — e.g., specific technologies (HTML/CSS/JS), database indexing 
strategy, RESTful API design. This is expected and healthy: a Tech Spec's 
job is to decide *how* to build something the BRD only describes *what* 
of. The distinction to watch for is between this kind of reasonable 
engineering elaboration versus fabricating specifics that aren't implied 
at all by the upstream input (e.g., naming a specific vendor or platform 
never mentioned) — the latter would be a real hallucination risk, not 
healthy elaboration.

### 3. Epic granularity is a judgment call, not a fixed rule

The pipeline generated 8 Epics for a single search-bar feature, including 
a dedicated "Testing and Validation" Epic. This is defensible but on the 
finer-grained end — a real sprint-planning conversation might fold testing 
into each functional Epic's acceptance criteria instead of its own Epic. 
Not a bug, just a design choice the LLM made that a human reviewer should 
sanity-check.

## Next steps / possible extensions

- Read `feature_request` from a file or CLI argument instead of hardcoding it
- Add a real Jira integration (via tool-use, similar to Week 6's agent) 
  to actually create Epics/Stories as tickets, rather than just text output
- Add conditional edges — e.g., route back to BRD node for clarification 
  if the feature request is too vague, rather than assuming it's always 
  complete