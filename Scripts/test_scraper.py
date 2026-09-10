import os

from scraper import create_documents, split_documents, save_documents, load_documents

from retrieval import (
    create_embeddings,
    find_top_chunks,
    save_embeddings,
    load_embeddings,
)

documents_file = "Scripts/documents.json"
embeddings_file = "Scripts/embeddings.json"

update = input("Update documents? (y/n): ").strip().lower()


urls = [
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/",
]


if os.path.exists(documents_file) and update != "y":
    print("Loading documents fro cache...")
    documents = load_documents(documents_file)
else:
    print("Downloading documents...")
    documents = create_documents(urls)
    save_documents(documents, documents_file)


chunks = split_documents(documents)


print("Documents:", len(documents))
print("Chunks:", len(chunks))


embeddings = None


if os.path.exists(embeddings_file):
    cached_data = load_embeddings(embeddings_file)

    if (
        isinstance(cached_data, dict)
        and cached_data.get("model") == "qwen3-embedding:0.6b"
        and cached_data.get("chunks") == chunks
        and len(cached_data.get("embeddings", [])) == len(chunks)
    ):
        print("Loading embeddings from cache...")
        embeddings = cached_data["embeddings"]

if embeddings is None:
    print("Creating embeddings...")
    embeddings = create_embeddings(chunks)
    save_embeddings(chunks, embeddings, embeddings_file)


question = input("Ask a question: ")


top_chunks = find_top_chunks(question, chunks, embeddings)

for i, (chunk, similarity) in enumerate(top_chunks, start=1):
    print(f"\nTOP {i}:")
    print("SOURCE:", chunk["source"])
    print("SECTION:", chunk["section"])
    print("TEXT:", chunk["text"])
    print("SIMILARITY:", similarity)
