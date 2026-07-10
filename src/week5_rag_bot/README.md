# Oracle ADF Knowledge Bot — RAG Pipeline

A Retrieval-Augmented Generation system that answers questions about 
Oracle ADF using a custom document base, ChromaDB for vector storage, 
and Groq (llama-3.3-70b-versatile) for generation.

## How it works
1. `ingest.py` — reads ADF documentation, chunks it by paragraph 
   (with heading-merge logic to keep headings attached to their content), 
   embeds each chunk, and stores it in a persistent ChromaDB collection.
2. `query.py` — takes a user question, retrieves the top-3 most 
   similar chunks, and passes them to Groq's LLM to generate a 
   grounded answer.

## Setup
pip install chromadb sentence-transformers groq python-dotenv

Create a `.env` file in the project root with:
GROQ_API_KEY=your_groq_api_key_here

## Usage
python ingest.py   # run once to build the vector store
python query.py    # ask questions

## Example Q&As

### Example 1
**Q:** what is a view object
**Retrieved top chunk (distance 0.661):** "View Object (VO) / Retrieves data from one or more Entity Objects or SQL queries. View Objects can be read-only or updatable."
**A:** "A View Object (VO) retrieves data from one or more Entity Objects or SQL queries and can be either read-only or updatable."

### Example 2
**Q:** what are performance best practices
**Retrieved top chunk (distance 0.862):** "Performance Best Practices / Enable View Object range paging where appropriate. Fetch only required attributes..."
**A:** The performance best practices mentioned are:
1. Enable View Object range paging where appropriate.
2. Fetch only required attributes.
3. Avoid unnecessary View Object executions.
4. Tune Application Module pooling.
5. Use indexes for frequently queried database columns.
6. Reduce unnecessary partial page refresh operations.

### Example 3 — retrieval limitation found
**Q:** what are performance best practices and deployment steps
**Retrieved chunks:** Performance Best Practices (0.963), Deployment intro (1.216), Conclusion (1.564) — chunk 12 (actual numbered deployment steps) did not make the top 3.
**A:** According to the provided context, the performance best practices are: [full 6-point list]. The deployment steps mentioned are: 1. Applications are packaged as EAR files. 2. Deployed to Oracle WebLogic Server. *Note: the model correctly flagged that the context lacked specific steps beyond packaging and deployment.*

*This confirms the retrieval limitation described below — the chunk with the full 5-step deployment list scored too low to make the top-3 results.*