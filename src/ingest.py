import chromadb

def load_and_chunk(filepath, sentences_per_chunk=3):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    raw_paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    merged = []
    buffer = ""
    for p in raw_paragraphs:
        if len(p) < 40 and not p.endswith('.'):
            # looks like a heading - hold onto it, merge with next
            buffer = p
        else:
            if buffer:
                merged.append(buffer + "\n" + p)
                buffer = ""
            else:
                merged.append(p)
    
    return merged

client = chromadb.PersistentClient(path="./chroma_storage")
#client.delete_collection(name="adf_docs")  # wipe old data 
collection = client.create_collection(name="adf_docs")


chunks = load_and_chunk("../data/Oracle_ADF_Sample_Notes.txt")

collection.add(
    documents=chunks,
    ids=[str(i) for i in range(len(chunks))]
)

print(f"Stored {len(chunks)} chunks in ChromaDB.")

result = collection.get(ids=["3"])
print(result)