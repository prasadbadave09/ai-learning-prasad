# AI Learning - Prasad Badave

A hands-on learning journey transitioning from Oracle ADF/Java 
to Agentic AI Development.

## Projects

- **hello_ai.py** — First LLM API call using Groq. Sends a system 
  prompt and user message, parses and prints the response.

- **hello_ai_v2.py** — Same core call, rewritten from scratch with 
  a custom system prompt (senior ADF architect persona) to demonstrate 
  how persona changes the model's output.

- **multi_turn.py** — Multi-turn conversational AI with memory. 
  Maintains a messages array across a chat loop so the model retains 
  context from earlier exchanges.

- **adf_explainer.py** — Basic ADF code explainer. Takes pasted ADF 
  Java code and explains what it does, which ADF concepts it uses, 
  and potential issues — in plain text.

- **adf_explainer_v2.py** — Improved ADF code explainer using 
  few-shot examples and chain-of-thought prompting for more structured, 
  consistent analysis. Uses the shared prompt library.

- **adf_explainer_json.py** — Same ADF code explainer, but forces 
  structured JSON output (component type, methods, issues, risk level, 
  recommendation) instead of free text — designed for machine-to-machine 
  use in a future agentic pipeline.

- **adf_schema_doc.py** — ADF schema documentation generator. Takes a 
  SQL CREATE TABLE statement and generates ADF-specific documentation: 
  table purpose, column meanings, recommended ViewObject name, and 
  recommended ADF binding types.

- **prompt_library.py** — Reusable, parameterized prompt templates 
  (ADF explainer, schema doc, JSON explainer, generic code review) 
  used across multiple scripts instead of hardcoding prompts.

- **test_prompt_library.py** — Demonstrates and verifies the prompt 
  library functions, including parameterized calls (e.g. different 
  language/framework combinations).

## Setup

1. Clone the repo 
   git clone https://github.com/prasadbadave09/ai-learning-prasad.git

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install groq python-dotenv

4. Create a `.env` file in the root folder
   GROQ_API_KEY=your_groq_api_key_here

5. Run any script, for example
   python src/hello_ai.py y

## Tech Stack
- Python 3.14
- Groq API
- LLM: llama-3.3-70b-versatile

## Learning Notes
See [week1_notes.md](./week1_notes.md) for detailed concepts learned 
each week.