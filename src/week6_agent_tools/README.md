## Known Limitations / Lessons Learned

### Ungrounded LLM nodes can hallucinate confidently, with zero warning signal

Tested the `research_node` in the LangGraph pipeline with two topics:

- **"Oracle ADF"** — produced accurate, correct research (MVC architecture, 
  JSF, Entity/View Objects, real Oracle integrations) — matches real ADF knowledge.
- **"LangGraph"** — produced completely fabricated content, describing LangGraph 
  as "a transformer-based language model with an encoder/decoder architecture" — 
  which is entirely false. LangGraph is a workflow orchestration framework, not 
  a language model at all.

Both answers were delivered with identical confidence — no hedging, no "I'm not 
certain," nothing to distinguish the accurate answer from the hallucinated one.

**Lesson:** an LLM node with no grounding (no RAG, no source documents, no 
retrieved facts) is only as reliable as its training data happened to be on 
that specific topic — and it gives zero signal about which case you're in. 
A confident wrong answer looks identical to a confident right answer.

**Implication for the flagship SDLC pipeline:** a production agent pipeline 
shouldn't be "LLM generates from nothing" — it should be "LLM generates from 
provided, real context" (actual project docs, requirements, or RAG-retrieved 
chunks), the same grounding pattern used in the Week 5 ADF Knowledge Bot. 
Without this, a BRD Agent could confidently hallucinate requirements never 
actually requested by the business.