# AI Learning - Prasad Badave

A hands-on learning journey transitioning from Oracle ADF/Java 
to Agentic AI Development.

## Projects
- **hello_ai.py** — First LLM API call using Groq. Sends a system 
  prompt and user message, parses and prints the response.

## Setup

1. Clone the repo
   git clone https://github.com/prasadbadave09/ai-learning-prasad.git

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install groq python-dotenv

4. Create a .env file in the root folder
   GROQ_API_KEY=your_groq_api_key_here

5. Run
   python hello_ai.py

## Output
The script explains what an LLM is using the 
llama-3.3-70b-versatile model via Groq API.

## Tech Stack
- Python 3.14
- Groq API
- LLM: llama-3.3-70b-versatile