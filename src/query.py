import chromadb
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_collection(name="adf_docs")

question = "what is a view object"

results = collection.query(
    query_texts=[question],
    n_results=3
)

#print(results)
#print(f"question is : {question}")
print("Retrieved chunks:")
for doc, dist in zip(results['documents'][0], results['distances'][0]):
    print(f"[distance: {dist:.3f}] {doc[:100]}...")
print()



context = "\n\n".join(results['documents'][0])

groq_client = Groq()  # reads GROQ_API_KEY from environment

response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens=300,
    messages=[
        {
            "role": "system",
            "content": "Answer the question using ONLY the provided context. If the answer isn't in the context, say 'I don't know based on the provided documents.'"
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }
    ]
)

print(response.choices[0].message.content)