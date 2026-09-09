from scraper import create_documents, split_documents, save_documents
from retrieval import (
    create_embeddings,
    find_top_chunks
)

documents_file = "Scripts/documents.json"

urls = [
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/"
    ]


print("Downloading documents...")
documents = create_documents(urls)
save_documents(documents, documents_file)
chunks = split_documents(documents)


print("Documents:", len(documents))
print("Chunks:", len(chunks))


print("Creating embedings...")
embeddings = create_embeddings(chunks)


question = input("Ask a question: ")


top_chunks = find_top_chunks(
    question,
    chunks,
    embeddings
)

for i, (chunk, similarity) in enumerate(top_chunks, start=1):
    print(f"\nTOP {i}:")
    print("SOURCE:", chunk["source"])
    print("SECTION:", chunk["section"])
    print("TEXT:", chunk["text"])
    print("SIMILARITY:", similarity)
