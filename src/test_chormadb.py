import chromadb

client = chromadb.Client()
collection = client.create_collection(name="test")

collection.add(
    documents=["ADF taskflows manage navigation between pages"],
    ids=["1"]
)

results = collection.query(
    query_texts=["how does page flow work in ADF"],
    n_results=1
)

print(results)