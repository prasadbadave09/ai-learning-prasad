# Week 1 Learning Notes

## What I built
- hello_ai.py — first LLM API call using Groq
- hello_ai_v2.py — explored system prompt persona changes
- multi_turn.py — multi-turn conversation with memory
- adf_explainer.py — ADF code review tool
- adf_explainer_v2.py — improved with few-shot + chain-of-thought
- adf_schema_doc.py — ADF schema documentation generator
- adf_explainer_json.py — structured JSON output version
- prompt_library.py — reusable prompt templates
- test_prompt_library.py — tests for the prompt library

## What I understood

**System prompt** controls the model's persona and behaviour. 
Same question with different system prompt = completely different output. 
This is how agents get their roles in a pipeline.

**Context window** is the total tokens the model can see at once — 
input + output combined. Beyond this limit, old messages get dropped.

**Tokens** are not words — they are subword chunks. 
1000 words ≈ 750 tokens. Technical code has higher token count.

**Multi-turn memory** works by maintaining a messages array. 
You append user and assistant messages manually. 
The model has no memory — you give it history every time.

**Few-shot prompting** means giving the model examples of 
input + expected output inside the system prompt. 
Result is more consistent and structured output.

**Chain-of-thought prompting** means telling the model to 
reason step by step before giving a final answer. 
Forces better analysis on complex inputs.

## Biggest insight
The system prompt is the developer's control lever. 
Every agent in an agentic pipeline is just a different system prompt 
giving the LLM a different role and responsibility.

**Structured JSON output** forces the LLM to return machine-readable 
data instead of plain text, by specifying the exact JSON structure in 
the system prompt and instructing "no explanation, no markdown, raw JSON 
only." Critical for agentic pipelines — one agent's JSON output becomes 
the next agent's input. Also needs defensive parsing (strip markdown 
fences) since the model doesn't always follow instructions perfectly.

**Prompt library** centralizes prompts into reusable, parameterized 
functions instead of hardcoding them in every script. Update once, 
use everywhere — same principle as a utility class in Java.

## Next week focus
- Connect external API + LLM in one pipeline